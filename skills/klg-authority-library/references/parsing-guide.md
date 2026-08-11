# Parsing Guide: Westlaw .doc Files

## File Format

Westlaw's "Word" delivery format produces an RTF file with
a `.doc` extension. It is NOT a true `.docx` file.

### Conversion

```bash
# Check file type
file [uploaded_file]
# Expected: "Rich Text Format data, version 1, ANSI"

# Convert to plain text
pandoc -f rtf -t plain [uploaded_file] -o westlaw_extracted.txt
```

## Boundary Detection Algorithm

Each authority in a merged Westlaw file is separated by
predictable boundary patterns.

### Case Boundaries

Cases begin with a citation line followed by a court name
line. The pattern is:

```
[Volume] [Reporter] [Page], [parallel cites if any]

[Court Name]
```

Court name patterns to match:
- `Supreme Court of California`
- `Court of Appeal, [District] District, [Division], California`
- `Court of Appeal, [District] District, California`
- `Supreme Court of the United States`
- `United States Court of Appeals, [Circuit]`
- `United States District Court, [District]`
- `United States Court of Federal Claims`

### Case End Boundaries

Each case ends with:
```
All Citations

[citation text]

End of Document   © [year] Thomson Reuters...
```

The "End of Document" line with the Thomson Reuters
copyright notice is the most reliable end marker.

### Parsing Algorithm

```
1. Read the full text file.
2. Split on "End of Document" markers.
3. For each segment:
   a. Find the first line matching a citation pattern
      (e.g., "11 Cal.3d 842" or "49 Fed.Cl. 248")
   b. Find the court name line.
   c. Find the case name (parties line, typically between
      the citation and the court name, or right after).
   d. Extract the full opinion text.
4. For each parsed case, record:
   - case_name: party names
   - citation: full citation string
   - court: court name
   - year: decision year
   - full_text: everything between the header and
     "All Citations" / "End of Document"
```

### Statute Boundaries

Statutes are simpler — they typically begin with the code
name and section number, followed by the statutory text.
The "End of Document" marker still applies.

### Stripping Proprietary Content

Westlaw includes editorial content that should NOT be
saved to the library:

- **HEADNOTES** section — remove everything between
  "HEADNOTES" and "COUNSEL" (or the opinion start)
- **Key Numbers** — lines starting with "()" or
  containing classification codes
- **SUMMARY** section — Westlaw's summary, not the
  court's syllabus
- **West's classification headers** — "Classified to
  California Digest of Official Reports" etc.

**DO preserve:**
- The court's own syllabus (if present — typically
  labeled as such or part of the opinion)
- Counsel/attorney listings
- The full opinion text
- Concurrences and dissents
- Footnotes (formatted as tables in pandoc output)

### Handling Large Files

A typical Westlaw Find & Print with 100+ authorities
will produce 20,000–50,000+ lines of text. Process
authorities one at a time during parsing — do not
attempt to hold all parsed authorities in memory
simultaneously during the Notion creation phase.
