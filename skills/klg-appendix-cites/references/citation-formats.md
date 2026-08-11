# KLG Appendix Citation Formats

## Placeholder Citation Formats (Pre-Compilation)

These are used during drafting and elevation, before the appendix
volumes exist.

### Document-Name Format (Most Common)

```
(YYYY-MM-DD Document Name, PDF p. X.)
(YYYY-MM-DD Document Name, PDF pp. X–Y.)
```

Examples:
- `(2024-11-13 Statement of Decision, PDF p. 18.)`
- `(2025-02-20 Preliminary Injunction, PDF pp. 2–3.)`
- `(2026-01-27 Judgment, PDF p. 4.)`
- `(2025-11-03 Permanent Injunction, PDF p. 4.)`

Key characteristics:
- Date prefix matches the document's file date
- "PDF p." refers to the PDF page number of the standalone
  document (not any internal page numbering)
- PDF page numbers are used because they are absolute — court
  documents often lack sequential internal page numbers, or
  contain duplicate page numbers
- The filename typically becomes the document description in
  the appendix volume index

### Declaration Format

```
(YYYY-MM-DD Name Decl. at X.)
(YYYY-MM-DD Name Decl. at X–Y.)
```

Examples:
- `(2026-02-03 Lindsay Hoopes Decl. at 2–3.)`
- `(2026-02-03 Spencer Hoopes Decl. at 3–4.)`

Key characteristics:
- "at" instead of "PDF p." but the page reference is still the
  PDF page number
- Declaration names may be abbreviated (first name + last name)

### REF Bates Format

```
(REF[MatterNumber]-[PageNumber].)
```

Examples:
- `(REF251021-00001.)`
- `(REF251021-00042.)`

Key characteristics:
- Matter number is 6-digit date: YYMMDD
- Page number is zero-padded sequential (5 digits)
- REF stamps appear at the bottom of each page
- The matter number identifies the document set; the page number
  identifies the specific page

### Exhibit/Prior Volume Format

```
(PA, Vol. X, Exh. Y, at p. Z.)
```

Examples:
- `(PA, Vol. 4, Exh. 16, at p. 802.)`

Key characteristics:
- References a previously compiled appendix volume
- May need updating if volumes are recompiled

### Transcript Format

```
(TT page:line.)
(TT page:line–page:line.)
(Vol. X RT page:line.)
```

Examples:
- `(TT 1708:4–1709:12.)`
- `(TT 1719:4–1723:19, 1726:1–9, 1731:6–17.)`

Key characteristics:
- "TT" = trial transcript
- "RT" = reporter's transcript (may be used interchangeably
  depending on context)
- May go in separate RT volumes with their own pagination
- Conversion approach varies by case — confirm with attorney

### Paragraph Reference Format

```
(YYYY-MM-DD Document Name, PDF [¶ X].)
```

Examples:
- `(2023-12-22 Second Amended Complaint, PDF [¶ 25].)`

Key characteristics:
- References a paragraph number rather than a page
- Conversion to appendix page requires finding the actual page
  where the paragraph appears
- May need manual resolution

---

## Final Appendix Citation Format (Post-Compilation)

### Standard Format

```
(V-PA-P.)       — Petitioner's Appendix
(V-AA-P.)       — Appellant's Appendix
```

Where:
- V = volume number (1, 2, 3, ...)
- PA/AA = appendix type abbreviation
- P = page number

Examples:
- `(1-PA-1.)`
- `(1-PA-62.)`
- `(2-PA-305.)`
- `(1-AA-150.)`

Key rules:
- No spaces within the citation
- Period inside the closing parenthesis
- Page numbers reflect the pagination printed at the bottom of
  each compiled volume page

### Page Ranges

```
(V-PA-P1–P2.)
```

Examples:
- `(1-PA-201–202.)`
- `(1-PA-45–62.)`

Key rules:
- Use en dash (–) between page numbers
- Both pages use the same volume prefix if within the same volume
- If a range spans volumes (rare), cite each volume separately

### Short Form (Subsequent References)

```
(V-PA-P at p. X.)
(V-PA-P at pp. X–Y.)
```

Short forms use "p." for a single page and "pp." for a range.

---

## Conversion Arithmetic

### The Offset Formula

```
appendix_page = (document_start_page - 1) + pdf_page_number
```

Or equivalently:
```
appendix_page = document_start_page + (pdf_page_number - 1)
```

Why: PDF page 1 of the document IS the document's appendix start
page. So PDF page 1 → start_page, PDF page 2 → start_page + 1,
and so on.

### Example

Document: 2024-11-13 Statement of Decision
Appendix start page: 45 (from Volume 1 index)
Brief cites: PDF p. 18

Calculation: (45 - 1) + 18 = 62
Final cite: `(1-PA-62.)`

Verification: Open Volume 1, go to page 62. It should show
page 18 of the Statement of Decision.

### Page Ranges

For `PDF pp. 2–3` with a start page of 200:
- Start: (200 - 1) + 2 = 201
- End: (200 - 1) + 3 = 202
- Final cite: `(1-PA-201–202.)`

### Declaration Page References

Declarations use "at X" instead of "PDF p. X" but the arithmetic
is the same — the number after "at" is the PDF page number.

### REF Bates Conversion

For REF citations, the page number in the REF stamp corresponds
to the sequential page within the Bates-stamped document set.
If the same documents are included in the appendix, the mapping
requires:
1. Identify which document the REF page belongs to (using the
   matter number date and page sequence)
2. Determine that document's position in the appendix
3. Apply the offset arithmetic

This is more complex than document-name conversion and may
require a separate REF-to-document mapping.

---

## Volume Index Format

Volume 1 of the compiled appendix includes an index, typically
in the first few pages. The index lists:

| Document Description | Date | Volume | Page |
|---|---|---|---|
| Complaint | October 20, 2022 | 1 | 1 |
| Second Amended Complaint | December 22, 2023 | 1 | 25 |
| Statement of Decision | November 13, 2024 | 1 | 45 |
| ... | ... | ... | ... |

The "Page" column shows the starting page of each document.
This is the authoritative source for the conversion mapping.

Note: The index page numbers themselves are part of the sequential
pagination. If the index occupies pages 1–4, the first document
starts at page 5 (or wherever the index indicates).
