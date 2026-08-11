---
name: opposition-separate-statement
description: Build or update a California Opposition Separate Statement to a Motion for Summary Judgment by transferring a moving party's UMFs from a PDF into a Word shell, filling in Plaintiff's responses from a Notion page, and adding Issue tables and Plaintiff's Additional Material Facts (AMFs). Triggers when the user mentions "separate statement," "MSJ opposition," "summary judgment opposition," "UMFs," "AMFs," "undisputed material facts," "CRC 3.1350," "fill in Plaintiff's responses," "transfer the PDF into the Word doc," "mirror the moving party's separate statement," or any combination — even if they don't say all the words. Also triggers when the user provides a Defendants' Separate Statement PDF and a Word shell template together. Use this proactively whenever a user is preparing an opposition to a summary judgment or summary adjudication motion in a California civil case.
---

# Opposition Separate Statement Builder

## What this skill does

This skill automates the full workflow of building or updating a Plaintiff's Opposition Separate Statement to a California Motion for Summary Judgment / Summary Adjudication (per California Rules of Court 3.1350(e)).

The workflow has two phases that the skill runs sequentially in a single invocation:

- **Phase 1 — Mirror the moving party's PDF.** Parse the Defendants'/Movant's Separate Statement PDF (which uses a 2-column layout with line numbering and pleading paper) and transfer every Undisputed Material Fact (UMF) and supporting evidence citation into the LEFT column of the Plaintiff's Word shell, preserving the shell's existing formatting.
- **Phase 2 — Fill in Plaintiff's responses.** Pull drafted responses + Plaintiff's supporting evidence from a Notion page and populate the RIGHT column of the UMF table. Add a separate table for each Issue (1–N) mirroring the PDF's structure with the Defendants' incorporation language verbatim and a blank right column. Add a final table for Plaintiff's Additional Material Facts (AMFs) with the AMF text and Plaintiff's evidence on the left and a blank right column for the Defendants' future response.

The output mirrors the moving party's PDF format exactly while preserving the formatting of the user's Word shell template.

## When to trigger

Trigger this skill whenever a user asks for help with any of the following:

- "Make my Word doc match the Defendants' separate statement PDF"
- "Fill in the Plaintiff's responses from Notion into my opposition"
- "Build the opposition separate statement"
- "Add the AMFs to my separate statement"
- "Mirror the PDF into the Word doc"
- "Transfer the UMFs from the PDF"
- A user provides a Defendants'/Movant's Separate Statement PDF and a Word shell at the same time, even without an explicit verb — that combination implies this workflow.

Do not require the user to say "California" or "CRC 3.1350" — the skill is California-specific by default since the format originates from CRC 3.1350.

## Inputs the skill needs

Before doing any real work, ask the user for these (use AskUserQuestion if available, or ask in the chat). Confirm each one rather than guessing:

1. **Moving party's Separate Statement PDF** — path to the file.
2. **Word shell template** — path to the .docx the user is filling in. This is the document that will be modified (a fresh copy will be saved; the original is preserved).
3. **Notion page URL** — the source of Plaintiff's drafted responses + AMFs. If the user doesn't have one, accept "no Notion" or "Phase 1 only" and skip Phase 2.
4. **Optional context:** case name, parties, your client, filing deadline, any special instructions about combined responses or exhibit reconciliation.

Don't proceed until you have items 1 and 2. Item 3 is optional.

## Workflow

The workflow has four stages: Discovery → Pre-flight → Confirmation Gate → Execute & Deliver. The skill must complete each stage before moving to the next.

### Stage 1: Discovery (extract everything before changing anything)

Run the parsers in parallel where possible:

1. **Parse the PDF** — run `scripts/extract_umfs_from_pdf.py <pdf>` to get a JSON of all UMFs with their fact text and supporting evidence. This script handles the 2-column California layout (line numbers stripped, firm watermark stripped, page footers stripped) and uses a sequential state-machine to detect UMF numbers (so it doesn't get fooled by date stubs like "August 16, 2017."). See `references/word_xml_patterns.md` for the column-cropping coordinates that work for standard pleading paper.
2. **Parse the Issues** — run `scripts/extract_issues_from_pdf.py <pdf>` to get the heading text + UMF incorporation list for each Issue (Issue 1: incorporates UMFs 1-3, 22-27, 37-50; etc.).
3. **Parse the Notion page** (if provided) — run `scripts/parse_notion_responses.py <notion_text_file>` to produce two JSON files: one for UMF responses (keyed by UMF number, with response text + Plaintiff's evidence), and one for AMFs (keyed by AMF number, with fact + evidence). Notion pages are often >100k characters; if the user shares a URL, fetch it via the Notion connector first and save the raw text to a temp file.
4. **Inspect the Word shell** — unpack the .docx using the docx skill's `scripts/office/unpack.py`, read `word/document.xml`, and identify: existing UMF rows (by `<w:bookmarkStart w:name="UMFN"/>` markers), partial fills in right cells, table grid widths, column widths. This tells you whether Phase 1 has already been done and which UMFs already have user-typed responses.

Save all parsed data to a temporary working directory so the user can see them if needed.

### Stage 2: Pre-flight check (compose the discrepancy report)

Run `scripts/preflight_check.py` against the parsed data. The script produces a summary report covering:

**Counts and structure:**
- N UMFs found in PDF / M UMF responses found in Notion (flag if N ≠ M)
- K Issues found in PDF (with their incorporation lists)
- J AMFs found in Notion (with numbering range)
- Word shell state: existing rows, bookmarks, partial fills

**Detected anomalies (hard-stops):**
- UMF count mismatch between PDF and Notion
- Word shell has partial response fills for some UMFs (lists them)
- Word shell has no UMF rows yet (fresh template — confirm building from scratch)
- Combined-response markers detected in Notion ("Combined response with UMFs X and Y") — confirm duplicate-not-merge approach
- Issue incorporation language doesn't match standard pattern
- AMFs present but ambiguous placement instruction
- Notion page heading structure unfamiliar (not `## UMF N` / `## AMF N`)
- PDF parse anomaly (fewer/more sections than expected, OCR garbage, columns not detectable)
- Filing deadline within 7 days (if user provided deadline)
- A UMF response in Notion shorter than 20 characters (likely placeholder)
- PDF UMF text differs significantly from existing Word UMF text (user has edited)

**Soft warnings (flagged but not blocking):**
- Typos detected in PDF (e.g., "Skoosky" vs. "Skootsky" inconsistency, missing brackets, missing commas)
- `[VERIFY]` flags in Notion (count + list)
- `B318163` or other unpublished citations (informational)
- Exhibit numbering mismatch between PDF and Notion (reconciliation needed manually)

### Stage 3: Confirmation Gate

If the pre-flight report contains **any hard-stop anomalies**: present the full summary to the user, ask explicitly: **"Proceed / Fix / Abort?"** Wait for an explicit "go" before continuing.

If the report contains **only soft warnings**: present a brief summary, note the warnings, and **proceed silently** — the user gets the warnings reported at the end of the run.

If the report is **clean**: proceed silently, no confirmation needed.

This gate is the most important part of the skill. The whole point is to avoid silently producing a wrong document when the inputs don't match the standard pattern.

### Stage 4: Execute and deliver

Run `scripts/build_word_doc.py` with the parsed JSON files and the Word shell. The script:

1. Unpacks the .docx
2. Updates `word/document.xml` with the changes (see `references/word_xml_patterns.md` for the exact XML patterns)
3. Repacks with `pack.py --validate false` (pleading templates often have broken `.dot` references that don't affect Word but fail strict XML schema validation)
4. Saves the result to the user's workspace folder as a fresh copy named `[YYYY-MM-DD] [Case shortname] Opposition Separate Statement.docx`. Never overwrite the user's original.
5. Optionally converts to PDF preview (using soffice) for visual sanity-check.

After delivery, report to the user:
- Path to the new file (with `computer://` link)
- Page count
- Soft warnings list (typos, [VERIFY] flags, etc.)
- Anything the user should review before signing

## KLG style guide (mandatory, applied automatically)

Every piece of text the skill transfers — Notion responses, PDF UMFs, AMFs, Issue headings — is run through `scripts/klg_style.py` before it lands in the Word document. This applies the Kowal Law Group's house style: straight quotes ("dumb quotes") become curly quotes ("smart quotes"), em dashes have all surrounding whitespace removed (closed style: `word—word`, never `word — word`), and double spaces inside lines are collapsed.

This is non-optional. AI-generated prose is recognizable in part by AP-style open em dashes and stray straight quotes; leaving these in a court filing flags it as machine-generated, which is unacceptable in this practice area. The skill should never leave them. See `references/klg_style_guide.md` for the full convention list and the few things the skill deliberately does NOT auto-correct.

## Critical patterns the build script must follow

Read `references/word_xml_patterns.md` and `references/common_gotchas.md` before invoking the build script — they document the non-obvious technical details that took an hour to debug the first time. The most important ones:

1. **Search XML by literal Unicode characters, not by entities.** When finding text inside `document.xml`, search for `'` (U+2019), not `&#x2019;`. The unpack script preserves Unicode characters as-is in the file, so XML-entity searches return -1, which silently breaks insertion logic and corrupts the document head.
2. **Pack with `--validate false`.** The user's pleading template very likely has a broken reference to a network-drive `.dot` file from when it was first created. Strict validation rejects this. Word itself doesn't care.
3. **Use bookmark anchors for finding rows.** Each UMF row should have a `<w:bookmarkStart w:id="N" w:name="UMFN"/>` marker. Find rows by bookmark name, not by content text — content can change but bookmarks are stable.
4. **Preserve the user's existing UMF rows.** If the Word shell already has UMFs 1–4 with responses the user typed in, do not overwrite them. Only fill in empty rows.
5. **Combined responses → duplicate text across rows, do not merge cells.** Cell-merging in California pleading templates can break alignment with the moving party's row count. Duplicating preserves row-by-row correspondence.
6. **Italic markdown (`*text*`) and bold markdown (`**text**`) from Notion → convert to Word `<w:i/>` / `<w:b/>` runs.** See `helpers.py` `text_to_runs()` function.
7. **Smart quotes preserved as XML entities** (`&#x201C;`, `&#x2019;`, etc.) when writing new XML. Apostrophes in legal writing should always be curly.

## When the skill should hand back to the user

Always hand back at the confirmation gate when discrepancies are found. The user is the source of truth for the substantive decisions (overwrite vs. skip partial fills, merge vs. duplicate combined responses, where to place AMFs).

Also hand back if the PDF parse fails (PDF is image-only, scanned, or formatting wildly differs). In that case, suggest the user check whether the PDF is OCR'd; if not, recommend running it through OCR first.

## Limitations

- Assumes the moving party's PDF uses the standard California 2-column pleading-paper format with line numbers in the left margin (1–28) and a centered footer. Non-standard formats will break the column-cropping in `extract_umfs_from_pdf.py`.
- Assumes Notion page uses the labeled-block structure (`**Plaintiff's Response:**`, `**Plaintiff's Supporting Evidence:**`, etc.) under `## UMF N` / `## AMF N` headings. Different structures need a custom parser.
- Assumes Word shell is .docx (not legacy .doc — convert first via the docx skill's `soffice.py`).
- Does not reconcile exhibit numbering between the moving party's AOE numbering and Plaintiff's compendium numbering. That's a manual step before signing — see soft warnings.
- Does not validate the legal sufficiency of responses. The skill is a transcription assistant, not a substantive review.

## Reference files

- `references/california_separate_statement.md` — CRC 3.1350 background, format requirements, a