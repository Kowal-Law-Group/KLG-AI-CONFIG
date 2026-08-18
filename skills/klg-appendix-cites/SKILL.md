---
name: klg-appendix-cites
description: "Manage appendix citation lifecycle: audit placeholder cites against the compile folder, build the mapping table after volumes are compiled, and convert placeholders to final appendix page cites via Word tracked changes. Use when the user says 'convert the cites', 'update appendix cites', 'replace placeholder cites', 'check the compile folder', 'appendix cite conversion', 'PA cites', 'AA cites', 'map the appendix', 'build the mapping table', 'cross-check the appendix', 'finalize the cites', 'the appendix volumes are ready', 'volumes are compiled', or 'here are the PA volumes'. Phase A: pre-compilation completeness audit. Phase B: post-compilation cite conversion with tracked changes. NOT for brief elevation, style checks, or citation format auditing without appendix context."
---

# KLG Appendix Citation Manager

## Purpose

This skill manages the full lifecycle of appendix citations in
appellate briefs. During drafting and elevation, the brief uses
placeholder citations that reference source documents by filename
and PDF page number — because the final appendix volumes don't
exist yet. Once the appendix is compiled by a service, those
placeholders need to be converted to the correct volume-and-page
citations (e.g., `(1-PA-350.)`).

The conversion is high-stakes: every single cite must land on the
right page, and errors are difficult to catch in a filed brief.
This skill handles the process in a way that builds in human
verification at every step — from a mapping table the attorney
can review before any changes are made, to Word tracked changes
that let the attorney confirm each individual conversion by
comparing the old placeholder against the new appendix cite.

## When to Run

This skill has two phases that run at different points in the
briefing timeline:

```
Brief Elevation → Assembly → PHASE A: COMPLETENESS AUDIT →
  [Appendix compiled by service] →
  PHASE B: CITE CONVERSION → Style Check → File
```

**Phase A** runs after the brief is assembled but before the
appendix is compiled. It ensures every cited document is in the
compile folder and every compile folder document is accounted for.

**Phase B** runs after the compiled appendix volumes are available.
It converts all placeholder cites to final appendix page cites.

The attorney may invoke either phase independently depending on
where they are in the process.

## Required Context

Before starting, read:
1. `references/citation-formats.md` — Placeholder and final
   citation format specifications, with examples
2. `/mnt/project/claude.md` — KLG citation standards (especially
   the record citation and appendix citation sections)

## CRITICAL: Citation Integrity

This skill converts citations — it must never fabricate them.

1. **Every conversion must trace to a source.** When converting
   placeholder cites to final appendix cites, every new citation
   must come from the mapping table built in Phase B. Never
   invent volume numbers, page numbers, or citation formats.
2. **If a placeholder cannot be mapped, flag it.** Write
   `[APPENDIX CITE NOT FOUND — verify manually]` rather than
   guessing.
3. **Present the mapping table for attorney review** before
   executing any conversions in the document.
4. **Never dispatch a subagent to generate citations.** Citation
   mapping must be done by reading the compiled appendix volumes
   directly.

## Phase A: Pre-Compilation Completeness Audit

### Step A.1: Extract All Document Citations from the Brief

Read the brief (`.docx` or `.md`) and build a comprehensive
inventory of every record-document citation. For each citation,
extract:

- **Document identifier:** The filename or description
  (e.g., "2024-11-13 Statement of Decision")
- **Page reference:** The internal PDF page number cited
  (e.g., "PDF p. 18")
- **Location in brief:** Section name and approximate position
- **Citation count:** How many times this document is cited

Group citations by unique document. The output is a document
citation inventory — a table showing every unique source document,
how many times it's cited, which pages are referenced, and the
citation format used.

Recognize these placeholder formats:
- Document-name format: `(2024-11-13 Statement of Decision, PDF p. 18.)`
- REF Bates format: `(REF251021-00001.)`
- Declaration format: `(2026-02-03 Lindsay Hoopes Decl. at 4–5.)`
- Exhibit format: `(PA, Vol. 4, Exh. 16, at p. 802.)`
- Transcript format: `(TT 1708:4–1709:12.)`

### Step A.2: Scan the Compile Folder

Read the contents of the AA compile or PA compile folder. For
each document, record:
- Filename
- File size (as a rough proxy for page count)
- If possible, actual page count (read the PDF to count pages)

### Step A.3: Cross-Check (Bidirectional)

Produce a completeness report with three sections:

**Documents cited in the brief that are in the compile folder:**
For each, show the brief's citation format alongside the matching
filename. Flag any filename mismatches that might cause confusion
during compilation (e.g., the brief says "Statement of Decision"
but the file is named "SOD_Final_v2.pdf").

**Documents cited in the brief that are NOT in the compile folder:**
These are gaps — the compile folder is missing documents that the
brief relies on. Flag these as critical issues that must be
resolved before compilation.

**Documents in the compile folder that are NOT cited in the brief:**
These are potentially unnecessary. For each, report:
- The document name
- The page count
- A note that the attorney should decide whether to include it
  for completeness or remove it to reduce appendix bulk

Summarize: total documents cited, total in compile folder,
overlap count, gaps count, uncited count, and total uncited pages.

### Step A.4: Validate Placeholder Accuracy

For documents that are in the compile folder, spot-check that
the placeholder cites are accurate:
- Open the cited PDF
- Navigate to the cited PDF page number
- Verify the content matches what the brief says is there

This is a sampling check, not exhaustive — focus on the most
frequently cited documents and any citations that look suspicious
(e.g., very high page numbers, citations to documents that are
only a few pages long).

### Step A.5: Omitted-Documents Audit (False-Negative Check)

Steps A.1–A.4 catch false positives — citations that point to
documents missing from the compile folder. They do not catch the
failure mode that actually causes summary denials: a document the
firm holds for the matter, that the appendix should include, that
was never cited or added in the first place, so nothing in A.1–A.4
ever flags it. Run this step against the full universe of documents
the firm holds for the matter, not just what's already in the
compile folder or already cited.

1. **Omitted-documents list.** Search the matter's full document
   set (SharePoint case folder, not just the compile folder) for
   every document the firm holds. List every one that is NOT in
   the proposed appendix, regardless of whether the brief cites it.
2. **Docket review.** Read the trial court docket (Register of
   Actions) for the matter. Flag any docket entry for a document
   the firm does not have on hand at all, where the brief's
   arguments plausibly require it — for example, a demurrer or
   preliminary-injunction ruling that is being challenged, or that
   the challenged ruling relies on.
3. **Three-column reconciliation.** Produce a table with one row
   per document relevant to the matter:
   - **Included** — in the proposed appendix
   - **Deliberately omitted** — held by the firm, not included,
     with a stated reason (irrelevant, cumulative, sealed, etc.)
   - **On the docket but not in our possession** — needs to be
     obtained before the appendix can be called complete
4. **Attorney sign-off gate.** This reconciliation is a
   legal-judgment call — whether the brief's arguments actually
   need a given document — not a clerical check. Present the table
   and hold the appendix as incomplete until an attorney reviews it
   against the brief's arguments and cited authorities and confirms
   the "Deliberately omitted" reasons are sound.

### Step A.6: Deliver the Completeness Report

Produce the report as a markdown file with clear action items,
including the Step A.5 three-column reconciliation table. Then
present it:

```
The completeness audit is done. Here's the summary:

- [N] documents cited in the brief
- [N] are in the compile folder ✓
- [N] are cited but MISSING from the compile folder ✗
- [N] documents in the compile folder are not cited
  ([N] total pages of uncited material)
- [N] documents the firm holds are not in the proposed appendix
  (see reconciliation table)
- [N] docket entries suggest a document we don't have at all

[If gaps exist:]
Before compiling the appendix, you need to add these
documents to the compile folder:
  1. [document name] — cited [N] times in the brief
  ...

[If uncited documents exist:]
These documents are in the compile folder but not cited:
  1. [document name] — [N] pages
  ...
Do you want to keep them for completeness or remove them?

Before this appendix can be called complete, an attorney needs to
sign off on the reconciliation table below — confirm each
"deliberately omitted" reason, and let me know how to handle
anything listed as on the docket but not in our possession.

[Three-column reconciliation table from Step A.5]

Would you like me to also produce this as a spreadsheet
for easier tracking?
```

## Phase B: Post-Compilation Cite Conversion

### Step B.1: Read the Appendix Index

The compiled appendix Volume 1 includes an index (typically in
the first few pages) listing every document, which volume it
appears in, and its starting page number. Read this index and
build the authoritative document-to-page mapping.

For each document in the index, record:
- Document name (as it appears in the index)
- Volume number
- Starting page number in the appendix
- Page count (calculated from the gap to the next document's
  start page, or from the end of the volume)

If the index is not clearly readable from the PDF, ask the
attorney to provide it in another format or point you to the
correct pages.

**Pagination notes:**
- Pages are sequentially numbered across all volumes. If Volume 1
  ends at page 300, Volume 2 starts at page 301.
- Every page is numbered, including volume cover pages.
- Follow the pagination as printed at the bottom of each page —
  this is the authoritative source.
- Ninth Circuit appeals may use different pagination conventions;
  always defer to what appears on the actual pages.

### Step B.2: Build the Mapping Table

Create a mapping table that connects each placeholder citation
format to its final appendix citation. This is the critical
intermediate artifact — the attorney reviews this table before
any changes are made to the brief.

The mapping table should show:

| Document | Placeholder Format | Appendix Volume | Start Page | Final Cite Formula |
|---|---|---|---|---|
| 2024-11-13 Statement of Decision | `(2024-11-13 Statement of Decision, PDF p. X.)` | 1 | 45 | `(1-PA-[44+X].)` |
| 2026-01-27 Judgment | `(2026-01-27 Judgment, PDF p. X.)` | 1 | 112 | `(1-PA-[111+X].)` |
| ... | ... | ... | ... | ... |

The formula column shows the arithmetic: the appendix start page
minus 1, plus the internal PDF page number. For example, if the
Statement of Decision starts at appendix page 45 and the brief
cites PDF p. 18, the final cite is `(1-PA-62.)` because
45 + 18 - 1 = 62.

**Why minus 1:** PDF page 1 of the document corresponds to the
appendix start page itself, not start page + 1. So the offset
is (start_page - 1) + pdf_page.

Also produce a concrete conversion preview — take 5–10 actual
citations from the brief and show the full before/after:

```
BEFORE: (2024-11-13 Statement of Decision, PDF p. 18.)
AFTER:  (1-PA-62.)

BEFORE: (2025-02-20 Preliminary Injunction, PDF pp. 2–3.)
AFTER:  (1-PA-201–202.)

BEFORE: (2026-02-03 Lindsay Hoopes Decl. at 4–5.)
AFTER:  (2-PA-305–306.)
```

### Step B.3: Attorney Review of Mapping Table

Present the mapping table and conversion preview to the attorney:

```
Here is the mapping table for converting placeholder cites to
final appendix page cites. Please review:

1. Does each document map to the correct appendix location?
2. Do the sample conversions look right?
3. Are there any documents I missed?

Once you confirm, I'll produce a tracked-changes version of
the brief where every placeholder cite is converted. You'll
be able to verify each conversion individually in Word.
```

Wait for confirmation before proceeding. The attorney may want
to spot-check specific mappings against the actual volumes.

### Step B.4: Convert Citations with Tracked Changes

After the attorney confirms the mapping table, produce a
tracked-changes version of the brief.

Read the docx skill (`/mnt/skills/public/docx/SKILL.md`) for
XML editing mechanics, then:

1. Copy the brief .docx to the working directory
2. Unpack:
   ```bash
   python /mnt/skills/public/docx/scripts/office/unpack.py brief.docx unpacked/
   ```
3. Edit `unpacked/word/document.xml` — for each placeholder
   citation, create a tracked change that:
   - **Deletes** the old placeholder text (using `w:del` with
     `w:delText`)
   - **Inserts** the new appendix citation (using `w:ins` with
     `w:t`)
   - **Author:** `"Claude — Appendix Cites"` (distinct from
     elevation and style-check authors)
   - **Date:** today's date in ISO format
   - **Unique sequential `w:id` values** for each change
   - **Preserves** the original run's `<w:rPr>` formatting

   The tracked change should make the conversion visible in
   Word's review pane:
   - Deleted (strikethrough red): `(2024-11-13 Statement of Decision, PDF p. 18.)`
   - Inserted (underline red): `(1-PA-62.)`

   This lets the reviewer see both citations side-by-side and
   verify they point to the same content.

4. Repack:
   ```bash
   python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ brief-APPENDIX-CITES.docx --original brief.docx
   ```
5. Validate:
   ```bash
   python /mnt/skills/public/docx/scripts/office/validate.py brief-APPENDIX-CITES.docx
   ```
6. Fix standalone declarations (prevents Word "unreadable content" error):
   ```bash
   python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py brief-APPENDIX-CITES.docx
   ```

### Step B.5: Produce the Conversion Log

Alongside the tracked-changes brief, produce a conversion log
as a spreadsheet (.xlsx or .md table) listing every single
conversion made:

| # | Location | Old Citation | New Citation | Document | PDF Page | Appendix Page |
|---|---|---|---|---|---|---|
| 1 | Introduction, ¶2 | `(2024-11-13 Statement of Decision, PDF p. 18.)` | `(1-PA-62.)` | Statement of Decision | 18 | 62 |
| 2 | Statement of Case, ¶1 | `(2025-02-20 Preliminary Injunction, PDF p. 2.)` | `(1-PA-201.)` | Preliminary Injunction | 2 | 201 |
| ... | ... | ... | ... | ... | ... | ... |

This log serves as a checklist — the attorney (or paralegal)
can work through it line by line while reviewing the tracked
changes in Word.

### Step B.6: Deliver and Explain

```
The cite conversion is complete. I've produced:

1. [Brief name]-APPENDIX-CITES.docx — the brief with all
   [N] placeholder cites converted to appendix page cites,
   shown as Word tracked changes

2. Conversion Log — a line-by-line record of every conversion
   with the old cite, new cite, and underlying arithmetic

HOW TO REVIEW:
Open the .docx in Word with Track Changes visible. For each
change, you'll see the old placeholder (deleted, strikethrough)
and the new appendix cite (inserted, underline). To verify:

1. Note the old cite (e.g., "Statement of Decision, PDF p. 18")
2. Open that document in the appendix volume
3. Confirm the content at the new page number matches
4. Accept the change if correct; reject if not

After accepting all changes, the brief will have clean final
appendix citations ready for filing.

WHAT TO DO NEXT:
- Run a style-guide-check on the final version
- Update the TOC and TOA in Word
- Update the Certificate of Word Count
```

## Phase C: Repagination Rebuild for Amended Appendices

Run this phase when the Appellant's or Respondent's Appendix gets
repaginated mid-briefing — new material added, a motion to augment
the record granted, or a scope error caught late that pushes page
counts forward and may shift volume boundaries. The mechanics are
the same as Phase B (build a mapping table, apply a tracked-changes
redline); only the inputs differ — old final cites map to new final
cites, instead of placeholders mapping to final cites.

### Step C.1: Pre-Work (runnable before the amended appendix lands)

1. **Extract the chronological index from the current appendix
   volumes.** TypeLaw-compiled PDFs carry this index at the front
   of Volume 1: every document with tab number, name, date, volume,
   and starting page. Derive each document's ending page by
   subtracting one from the next tab's starting page.
2. **Extract the citation inventory from the current brief.** All
   `(N-AA-M)` / `(N-AA-M-P)` patterns (or `PA` equivalents) with
   surrounding context. Normalize PDF-text artifacts where digits
   may have been split by spaces (e.g., `2-AA-49 2` → `2-AA-492`).
   For each cite, identify which document it falls in and the
   within-document offset.
3. **Flag for human review:** placeholder gaps (`___` markers left
   for cites not yet filled in) and any cite whose range crosses a
   tab boundary in the current appendix — almost always a typo to
   fix before remapping, not a real spanning cite.

### Step C.2: Rebuild (triggered when the amended appendix lands)

4. **Extract the new appendix's chronological index.** Match
   documents across versions by name (fuzzy-match for renames) and
   date. New documents get new tabs.
5. **Build the mapping table.** For each old document, capture its
   old vol/page range and new vol/page range. Volume boundaries may
   shift — going from 2 volumes to 3–4 is common when substantial
   new material is added.
6. **Apply the offset formula** to every cite in the brief:
   `new_page = new_doc_start + (old_page - old_doc_start)`.
   Translate the volume number based on which volume contains the
   new page.
7. **Produce a tracked-changes redline** of the brief (.docx) with
   all cite updates, using the same Phase B conversion engine.
   Editor as the tracked-change author, per `claude.md`.
8. **Separate analytical pass for new cites:** walk the Statement
   of the Case and any party-specific argument sections to identify
   where additional record support is needed for newly added
   material — this is a substantive read, not a mechanical one.

### When this comes up

Not a one-off pattern — recurs whenever a scope error is caught
late in briefing, the court orders additional record material
included, co-counsel adds a new theory requiring new record
support, or a motion to augment the record is granted. Save the
Step C.1 citation inventory as a CSV with context so the team can
review and verify before the Step C.2 redline pass runs.

## Special Cases

### Page Ranges

When the placeholder cites a page range (e.g., `PDF pp. 2–3`),
convert both endpoints:
- Before: `(2025-02-20 Preliminary Injunction, PDF pp. 2–3.)`
- After: `(1-PA-201–202.)`

Use an en dash (–) between page numbers, matching KLG style.

### Paragraph References

When the placeholder cites a paragraph number rather than a page
(e.g., `PDF [¶ 25]`), the conversion requires finding the actual
page where that paragraph appears. This may require reading the
source document in the appendix. Flag these for manual review if
the page cannot be determined programmatically.

### Transcript Citations

Reporter's Transcript citations (`TT page:line`) typically go in
a separate volume (Reporter's Transcript or RT volumes) with their
own pagination. These may not follow the same conversion pattern
as document appendix citations. Confirm with the attorney how RT
cites should be handled — they may stay as-is or convert to a
different format.

### REF Bates Numbers

REF-format placeholders (e.g., `(REF251021-00001.)`) can be
mapped to appendix pages if the Bates-stamped originals are the
same documents included in the appendix. The REF date code
identifies the document; the page number identifies the page
within it. Apply the same offset arithmetic.

### Pre-Existing Appendix Citations

Some citations may already reference appendix volumes from a
prior compilation (e.g., `(PA, Vol. 4, Exh. 16, at p. 802.)`).
These may need to be preserved as-is or updated to reflect new
volume compilation. Confirm with the attorney.

### Ninth Circuit and Other Variations

Different circuits may use different appendix citation formats
or pagination conventions. Always defer to the pagination as
printed on the actual compiled volume pages, and confirm the
citation format with the attorney for the specific court.

## What This Skill Does NOT Do

- **Compile the appendix volumes** — A service handles the
  physical compilation. This skill audits completeness before
  compilation and converts cites after.
- **Substantive brief review** → Use `klg-brief-elevation`
- **Style conformance** → Use `klg-style-guide-check`
- **Citation format auditing** → Use `klg-cite-check` (for
  checking pincites, orphaned short forms, etc., independent
  of appendix page numbers)
- **Research** → Use `klg-deep-research-prompts`
