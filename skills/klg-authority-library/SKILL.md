---
name: klg-authority-library
description: "Ingest Westlaw authorities into the KLG Research database as individual, searchable, annotatable case entries. Use whenever the user says 'save these authorities', 'add to the library', 'ingest authorities', 'build the authority library', 'save the key cases', 'extract cases to Notion', or references saving Westlaw research output as individual entries in the Research database. Also triggers when the user says 'check the library' or 'do we already have this case' to search for existing authorities before running Westlaw. This is an OPTIONAL post-pipeline step — it runs after the research compilation skill's Phase B finalization, or standalone when the user uploads a Westlaw .doc file. Do NOT use for research prompt generation, compilation, or case assessments."
---

# KLG Authority Library

## Purpose

Parse a Westlaw Find & Print output file into individual
authorities (cases, statutes, regulations) and selectively
ingest them into the KLG Research database as standalone,
searchable, annotatable entries. Over time, this builds a
firm-wide research library that reduces redundant Westlaw
lookups and preserves attorney annotations across matters.

## Two Modes

### Mode 1: Ingest Authorities

Parse a Westlaw .doc file, present the authorities to the
user for selection, and create Research database entries for
the selected authorities.

**Triggers:** "save these authorities," "add to the library,"
"ingest authorities," "save the key cases," or when the
compilation skill's Phase B completes and the user opts in.

### Mode 2: Library Lookup

Search the Research database for authorities before running
Westlaw. If an authority already exists in the library, skip
it from the Westlaw list.

**Triggers:** "check the library," "do we already have,"
"search the authority library," or automatically during the
compilation skill's Phase A authority extraction.

## Required Context

Before running, read these reference files:

1. `references/parsing-guide.md` — How to parse Westlaw
   .doc files into individual authorities
2. `references/notion-schema.md` — Research database schema
   and property format requirements

## Mode 1: Ingest Authorities

### Step 1: Parse the Westlaw File

The user uploads a Westlaw .doc file (which is actually RTF
despite the .doc extension).

1. Check the file type: `file [uploaded_file]` — expect
   "Rich Text Format data"
2. Convert to plain text:
   ```
   pandoc -f rtf -t plain [uploaded_file] -o westlaw_extracted.txt
   ```
3. Parse into individual authorities by identifying case
   boundaries. See `references/parsing-guide.md` for the
   boundary detection algorithm.

### Step 2: Build the Authority Inventory

Produce a brief inventory of all parsed authorities:

```
WESTLAW AUTHORITY INVENTORY
═══════════════════════════
File: [filename]
Total authorities parsed: [N]

CASES:
  [1] [Case Name], [Citation] ([Court], [Year])
  [2] [Case Name], [Citation] ([Court], [Year])
  ...

STATUTES:
  [N+1] [Code § Section] — [Short description if available]
  ...
```

### Step 3: User Selection

Present the selection interface. The user chooses which
authorities to save to the library. Offer smart defaults
based on context:

```
Which authorities would you like to save to the library?

SUGGESTED (high-leverage — cited in 3+ research memos):
  [1] [Case Name] — cited in Prompts 1, 3, 7
  [4] [Case Name] — cited in Prompts 2, 4, 5, 8

OPTIONS:
  - "suggested" — save only the suggested cases above
  - "all cases" — save all [N] cases (skip statutes)
  - "all" — save everything (cases + statutes)
  - Pick by number: e.g., "1, 4, 7, 12"
  - "none" — skip ingestion
```

If the compilation skill's convergence analysis is available
(i.e., this was triggered from post-pipeline options), use
the convergence data to identify which authorities were cited
across multiple research memos. Those are the "suggested"
high-leverage authorities.

If no convergence data is available (standalone mode), skip
the "suggested" section and just present the numbered list.

Wait for the user's selection before proceeding.

### Step 4: Deduplication Check

Before creating any entries, search the Research database
for each selected authority to check for duplicates:

For each authority:
1. Search the Research database (`collection://622bfafd-45b1-451a-b518-f72d86767cb0`)
   for the case name or citation.
2. If found: note it as "already in library" and skip creation.
   Instead, add the current Case Portal relation to the
   existing entry (so it's linked to both matters).
3. If not found: proceed to creation.

Report:
```
DEDUPLICATION CHECK
═══════════════════
Selected: [N]
Already in library: [N] (will add case relation only)
New entries to create: [N]
```

### Step 5: Create Research Database Entries

For each NEW authority, create a page in the Research database
(`collection://622bfafd-45b1-451a-b518-f72d86767cb0`).

**Properties to set:**
- **Title:** "[Case Name], [Full Citation]"
  - Example: "Conover v. Hall, 11 Cal.3d 842 (1974)"
  - For statutes: "Cal. Civ. Proc. Code § 437c"
- **Case Portal:** JSON array with the current matter's
  Case Portal page URL:
  `"[\"https://www.notion.so/CASE_PORTAL_PAGE_ID\"]"`
- **📚Related Research:** JSON array with the research
  project page URL (the parent Notion Research page from
  the pipeline):
  `"[\"https://www.notion.so/RESEARCH_PROJECT_PAGE_ID\"]"`
- **Tags:** `["Research", "Westlaw Authority"]`
  (NOTE: "Westlaw Authority" may need to be added as a new
  multi-select option. Use `notion-update-data-source` with
  an ALTER COLUMN statement if the option does not already
  exist.)
- **Publish or Pass?:** "Not Applicable"
- **Note:** "[Court], [Year]. Cited in [N] research memos
  for [Matter Short Name]."
- **Date:** [today's date]

**Page content:** The full text of the authority as extracted
from the Westlaw file. Use Notion markdown. Structure:

```
**Citation:** [Full citation with parallel cites if available]
**Court:** [Court name]
**Date:** [Decision date]
**Ingested from:** [Research project page link]
**Matter:** [Case name and number]

---

## Opinion

[Full opinion text, preserving paragraph structure.
Do NOT include Westlaw headnotes, key numbers, or
proprietary editorial content — include only the
court's opinion, syllabus if present, and any
concurrences/dissents.]

---

## Attorney Notes

*[No notes yet. Attorneys can add annotations, key
holdings, distinguishing factors, and practice tips
here over time.]*
```

For DUPLICATE authorities (already in library), update the
existing page:
- Add the current Case Portal to the existing Case Portal
  relation (append, don't replace)
- Add the research project page to 📚Related Research
- Optionally add a note in the page content: "Also cited
  in [new matter name] ([date])."

### Step 6: Report

```
AUTHORITY LIBRARY UPDATE
════════════════════════
New entries created: [N]
Existing entries updated: [N] (new case relations added)
Skipped (user did not select): [N]

New entries:
  ✓ [Case Name], [Citation] — [Notion page URL]
  ✓ [Case Name], [Citation] — [Notion page URL]
  ...

Updated (already in library):
  ↻ [Case Name], [Citation] — added [Matter] relation
  ...
```

---

## Mode 2: Library Lookup

### Step 1: Receive Authority List

The user provides a list of citations (from the compilation
skill's Phase A authority extraction, or manually).

### Step 2: Search the Library

For each citation, search the Research database for a match.
Use the case name and reporter citation as search terms.

### Step 3: Report

```
LIBRARY CHECK
═════════════
Authorities checked: [N]
Found in library: [N] — can skip Westlaw
Not in library: [N] — include in Westlaw list

IN LIBRARY (skip Westlaw):
  ✓ [Case Name], [Citation] — [Notion page URL]
  ...

NOT IN LIBRARY (send to Westlaw):
  ✗ [Case Name], [Citation]
  ...

REDUCED WESTLAW LIST ([N] authorities):
[paste-ready list for Westlaw Find & Print]
```

This directly reduces Westlaw costs and processing time.

---

## Execution Rules

1. Always convert Westlaw .doc files using pandoc — they
   are RTF despite the .doc extension.
2. Never create duplicate entries. Always search before
   creating.
3. Case Portal relations must use JSON array format:
   `"[\"https://www.notion.so/PAGE_ID\"]"`
4. Respect the user's selection. Never ingest authorities
   the user did not select.
5. Strip Westlaw proprietary content (headnotes, key
   numbers, editorial annotations) from the opinion text.
   Include only the court's own words.
6. If the Notion API rate-limits during batch creation,
   add a brief delay between calls. Do not fail silently.
7. For large batches (50+ authorities), warn the user
   about processing time before starting.
8. This skill is OPTIONAL. It should never block the
   critical path of the research pipeline. If it fails
   partway through, report what succeeded and what didn't.
9. When triggered from the compilation skill's post-pipeline
   options, the convergence analysis and Case Portal are
   already known — use them to populate the "suggested"
   selection and the Case Portal relation.
10. The "Attorney Notes" section in each page is sacred.
    Never overwrite or modify it — it contains human work
    product that accumulates over time.
