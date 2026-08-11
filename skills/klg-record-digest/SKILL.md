---
name: klg-record-digest
description: "Ingest appellate record volumes (appendix and reporter's transcript) from SharePoint into structured per-volume Notion digests with a searchable master index. Triggers: 'digest the record', 'ingest the record', 'index the record', 'record digest', 'process the appendix', 'process the transcripts', 'find where in the record', 'what page is X on', 'check the record for'. Run early in any appellate matter, before case assessment or brief drafting. Also triggers when Claude needs to verify a record citation or find record support for a proposition. NOT for case assessments, research pipelines, or brief drafting — those are separate skills."
---

# KLG Record Digest

## Purpose

Produce structured, searchable digests of every volume in an
appellate record — both the Appendix (AA) and the Reporter's
Transcript (RT). The digests live in Notion, linked to the
matter's Case Portal entry, and serve as Claude's institutional
memory of the record across all future sessions.

**The problem this solves:** Claude cannot hold a multi-thousand-
page appellate record in a single context window. Without
digests, Claude drafts briefs from excerpts and prior-session
notes, leading to misattributed citations (e.g., citing
instruction pages as factual support, citing the cross-complaint
as the complaint, citing verdict-form pages that are actually
jury instructions). Digests give every future session a reliable
map of what is on every page of the record.

**Architecture:** NotebookLM is the ingestion engine — it holds
the full record simultaneously and answers structured questions
across all volumes. Claude is the orchestrator and structurer —
it generates the questions, processes NotebookLM's output, and
builds the Notion digests. Notion is the access layer — it
stores the digests where Claude can search them via MCP during
any future session.

## When to Run

- **Ideal:** Immediately after the record is compiled and
  uploaded to SharePoint, before any case assessment or response
  plan.
- **Acceptable:** At any point during the matter lifecycle. Late
  is better than never.
- **Trigger for issue-specific extraction:** After a case
  assessment or response plan identifies key issues, run Phase D
  to extract issue-specific compilations from the digests.

## Ingestion Mode Selection

Before starting, present the options:

```
How would you like to process the record?

OPTION 1 — NotebookLM + Claude (recommended):
  ✓ NotebookLM ingests the full record at once — no
    context limitations. Cross-references across all
    volumes simultaneously.
  ✓ Generates audio overview for attorney prep.
  ✓ Claude structures the results into searchable
    Notion digests for all future sessions.
  ✗ Requires manual upload to NotebookLM and paste
    of results back to Notion.
  Time: ~20 min Claude setup + ~30 min NotebookLM
  processing + ~30 min Claude structuring.

OPTION 2 — Claude only (Cowork):
  ✓ Fully automated — reads from SharePoint, writes
    to Notion, no manual steps.
  ✗ Processes one volume at a time. Cannot cross-
    reference across volumes. May miss connections
    and produce gaps.
  Best for: small records under ~500 pages.
  Time: ~60-90 min in Cowork.

OPTION 3 — Both (belt and suspenders):
  ✓ NotebookLM does the primary ingestion. Claude
    does an independent Cowork pass. Discrepancies
    are flagged and resolved.
  Best for: high-stakes matters or first time using
  this workflow.
  Time: ~2-3 hours total.
```

Skip this question if the user specifies a mode.

## Phase A — Inventory and Setup

This phase runs in Claude (Chat or Cowork).

### Step A.1: Locate the record volumes.

Search SharePoint for the matter folder. List all PDF files
that appear to be record volumes. Present the list:

```
I found the following record volumes in the matter folder:

APPENDIX (AA):
  1-AA.pdf (XX pages)
  2-AA.pdf (XX pages)
  ...

REPORTER'S TRANSCRIPT (RT):
  Vol1.RT.pdf (XX pages)
  Vol2.RT.pdf (XX pages)
  ...

Total: [N] volumes, approximately [X] pages.

Does this look complete, or are there additional volumes?
```

### Step A.2: Create the project page.

Run project preflight per claude.md. Create a project in the
Projects database:
- Category: Case Support
- Support Type: Ad Hoc Task
- Title: `[Matter Name] — Record Digest ([Case No.])`
- Icon: 🔧
- Priority: per deadline proximity rules
- Summary: "Structured digests of all appellate record
  volumes. Master index and per-volume summaries in Notion."

### Step A.3: Create the master index page (skeleton).

Create a page in the Research database:
- Title: `[Matter Name] — Record Master Index`
- Case Portal: linked
- Projects: linked to the digest project
- Tags: Research
- Content: skeleton with headers for each volume.

### Step A.4: Create the NotebookLM handoff page.

If using Option 1 or 3, create a page in the Research database
following the cross-platform handoff protocol:
- Title: `[Matter Name] — NotebookLM Handoff: Record Ingestion`
- Direction: Claude → NotebookLM
- Content: the structured question set (see Phase B)
- Output section: where the user pastes NotebookLM responses

## Phase B — NotebookLM Ingestion (Options 1 and 3)

### Step B.1: Generate the structured question set.

Claude generates a comprehensive interrogatory for the record.
Post this to the NotebookLM handoff page in Notion. The
question set has two parts.

**Customization:** Before generating the question set, Claude
should review the case assessment or response plan (if one
exists) and add case-specific questions targeting the legal
issues already identified.

**Part 1 — AA (Appendix) Questions:**

```
INSTRUCTIONS: I have uploaded the full appellate appendix
for [case name], [case number]. Please answer each question
below with specific page numbers (use the AA page stamps at
the bottom of each page, formatted as [volume]-AA-[page],
e.g., 1-AA-107 or 3-AA-2946).

1. DOCUMENT MAP: For each distinct document in the appendix,
   identify:
   a. The AA page range (start and end)
   b. The document title or type (complaint, cross-complaint,
      answer, motion, opposition, order, minute order, jury
      instruction, verdict form, judgment, notice, declaration,
      exhibit, etc.)
   c. The filing date (if visible)
   d. The filing party (plaintiff, defendant, court, or joint)
   e. For jury instructions: the CACI number or special
      instruction designation

2. COMPLAINT vs. CROSS-COMPLAINT: Identify the exact page
   ranges for (a) the plaintiff's complaint and (b) any
   cross-complaint. Who is the plaintiff? Who is the
   defendant? Who are the cross-complainants?

3. JURY INSTRUCTIONS: List every jury instruction with its
   CACI number (or special instruction designation), its AA
   page number, and a one-sentence summary of what it
   instructs. Separately identify:
   a. Generic/housekeeping instructions (duties of jurors,
      evidence rules, burden of proof, etc.)
   b. Cause-of-action instructions (breach of contract,
      fiduciary duty, conversion, Penal Code 496, unjust
      enrichment, etc.)
   c. Damages instructions
   d. Special instructions

4. VERDICT FORMS: Identify the exact page range for the
   verdict forms. For each verdict form question, state
   the cause of action, the dollar amount awarded (if any),
   and the AA page number.

5. JUDGMENT: Identify the page range for the judgment.
   What is the total judgment amount? How was it calculated?
   Were damages trebled? Under what statute?

6. POST-TRIAL MOTIONS: Identify each post-trial motion
   (new trial, JNOV, motion to vacate, etc.), its filing
   date, its AA page range, and the ruling (with the ruling's
   AA page range).

7. NOTICE OF APPEAL: Page number and date filed.

8. PARTIES: List all parties to the lawsuit, including any
   business entities. For each, state whether they are a
   plaintiff, defendant, cross-complainant, cross-defendant,
   or intervenor. Cite the page where this is established.

9. KEY ALLEGATIONS: For each cause of action in the
   complaint, identify:
   a. The cause of action name and number
   b. The complaint paragraph numbers
   c. The AA page range
   d. A 2-3 sentence summary of what is alleged
   e. The specific conduct alleged as wrongful
```

**Part 2 — RT (Reporter's Transcript) Questions:**

```
INSTRUCTIONS: I have uploaded the full reporter's transcript
for [case name], [case number]. Please answer each question
below with specific volume and page numbers (formatted as
[volume]-RT-[page], e.g., 3-RT-651 or 7-RT-1840).

1. WITNESS MAP: For each witness who testified, identify:
   a. Full name
   b. Relationship to the parties (party, employee, expert,
      lender, family member, etc.)
   c. Called by which party
   d. Volume and page range for direct examination
   e. Volume and page range for cross-examination
   f. Volume and page range for redirect (if any)
   g. Key topics covered (list each with page range)

2. OPENING STATEMENTS: Volume and page range for each
   party's opening statement. Key themes or promises made.

3. CLOSING ARGUMENTS: Volume and page range for each
   party's closing argument and rebuttal. For each party:
   a. The specific dollar amounts requested
   b. The exact pages where damages figures are stated
   c. The legal theories emphasized
   d. Key rhetorical moves or characterizations

4. KEY ADMISSIONS: Identify every instance where a party
   or witness made an admission against interest:
   a. The exact quote (or close paraphrase)
   b. The volume and page number
   c. Who said it and in what context

5. OWNERSHIP TESTIMONY: Compile all testimony about the
   ownership structure of the businesses:
   a. Who claims to own what percentage
   b. How the arrangement was described (oral agreement,
      nominee, partnership, succession plan, etc.)
   c. Contradictions between witnesses or between a
      witness's different descriptions
   d. Documentary evidence discussed (K-1s, W-2s, corporate
      records, tax filings)

6. VALUATION TESTIMONY: Compile all testimony about the
   value of the businesses:
   a. Who provided valuation testimony
   b. Whether they were qualified as an expert
   c. The specific dollar figures stated
   d. The methodology described (if any)
   e. Real estate values stated separately from business
      values

7. CORPORATE GOVERNANCE: Any testimony about:
   a. Who controlled the corporate bank accounts
   b. Who had signing authority
   c. When and why access was changed
   d. Corporate creditors, loans, or obligations discussed
   e. Employees or payroll discussed
   f. Vendor relationships discussed

8. DISPUTED EVENTS: For each key disputed event (e.g.,
   the confrontation, the stock transfer demand, the bank
   account cutoff), compile each party's version with
   citations.

9. EXHIBITS: List all exhibits discussed during testimony,
   with the witness who discussed them and the page range.

10. JURY INSTRUCTION CONFERENCE: If there was a recorded
    colloquy about jury instructions, identify the volume
    and page range. Note which instructions were disputed,
    stipulated, or refused.
```

### Step B.2: User uploads to NotebookLM.

Provide the user with instructions:

```
Here's what to do in NotebookLM:

1. Go to notebooklm.google.com and create a new notebook.
   Name it: [Matter Name] — Appellate Record ([Case No.])

2. Upload all record volumes as sources:
   [list each PDF file name from the SharePoint inventory]

3. Wait for NotebookLM to process all sources (this may
   take a few minutes for large records).

4. Optional but recommended: Generate an Audio Overview.
   This creates a ~15-minute podcast-style discussion of
   the record. Useful for attorney prep — listen during a
   commute or workout to build intuitive familiarity with
   the case. Save or download it.

5. Paste the AA questions from the handoff page into the
   NotebookLM chat and submit. When it responds, copy the
   full response and paste it into the "Output — AA" section
   of the handoff page on Notion:
   [handoff page URL]

6. Then paste the RT questions and do the same — paste the
   response into the "Output — RT" section.

7. Let me know when both outputs are posted. I'll structure
   them into the Notion digests.
```

### Step B.3: Claude structures the output.

When the user confirms the NotebookLM output is on the handoff
page, Claude reads it and creates per-volume digest pages in
Notion following the templates in `references/digest-template.md`.

For each volume:
1. Create a Notion page in the Research database.
2. Parse NotebookLM's answers into the template fields.
3. Add the mandatory Cautions field for every AA document.
4. Add standardized topic tags.
5. Update the master index with the volume summary.

### Step B.4: Verification pass.

After structuring all digests, Claude runs a self-check:
- Do the page ranges cover the full volume without gaps?
- Are complaint and cross-complaint clearly distinguished?
- Are jury instructions and verdict forms clearly
  distinguished?
- Do document counts match the volume inventory?
- Are there any pages NotebookLM flagged as unclear?

For critical citations (key admissions, damages figures,
disputed facts), pull the actual page from SharePoint to
confirm. NotebookLM can hallucinate page numbers.

Flag any issues for the user to resolve.

## Phase C — Claude-Only Ingestion (Option 2 or Option 3)

This phase runs in **Cowork only.**

If the user is in Chat, provide Cowork switch instructions:

```
Record ingestion needs access to the full matter folder.
Here's how to switch to Cowork:

1. Click 'Cowork' in the top navigation bar.
2. Select the matter folder for [case name].
3. Once the Cowork session starts, paste this:

"Run the record digest skill for [case name], Claude-only
mode. The record volumes are in the matter folder."
```

### Step C.1: Process one volume at a time.

**CRITICAL: One volume per cycle.** Read the volume (in chunks
of 50-100 pages for large volumes), write its digest to Notion
following the templates in `references/digest-template.md`,
update the master index, then move to the next volume.

Do not attempt to hold multiple volumes in context
simultaneously.

### Step C.2: For each AA volume.

1. Read the volume via SharePoint or direct file access.
2. Identify every distinct document (watch for document
   boundaries: tab dividers, filing stamps, caption changes).
3. For each document, create a template entry with all fields
   including the mandatory Cautions field.
4. Write the volume digest to a Notion page.
5. Update the master index.

### Step C.3: For each RT volume.

1. Read the volume.
2. Identify every witness examination and procedural segment.
3. For each segment, create a template entry with all fields.
4. Write the volume digest to a Notion page.
5. Update the master index.

### Step C.4: Confirm each volume.

After each digest is written:

```
✅ [Volume ID] digest complete. [N] documents/witnesses
   indexed. Moving to [next volume].
```

Proceed without waiting for user input unless the user
intervenes.

### Step C.5: Cross-check (Option 3 only).

If Option 3 was selected, compare Claude's digests against
the NotebookLM-derived digests. Flag discrepancies:
- Documents identified by one source but not the other
- Different page ranges for the same document
- Different characterizations (e.g., one says "complaint,"
  the other says "cross-complaint")
- Witnesses or topics found by one source but not the other

Present discrepancies to the user for resolution.

## Phase D — Issue-Specific Extraction (On Demand)

Runs at any time after digests are created. Trigger phrases:
"extract from the digests," "find in the record," "what does
the record say about," "check the record for."

### Step D.1: Choose the extraction source.

```
I can search for this in:

1. The Notion digests (fastest — no manual steps)
2. NotebookLM (most thorough — if the notebook is
   still active, paste this question and I'll process
   the answer)
3. Both (belt and suspenders)
```

### Step D.2: Search and compile.

For Notion-based extraction:
1. Search the master index for relevant volume digests.
2. Read the relevant digest pages.
3. Identify specific page ranges.
4. Pull actual pages from SharePoint for precise citations.

For NotebookLM-based extraction:
1. Generate a targeted question for the user to paste.
2. User pastes the response to the handoff page.
3. Claude verifies the citations against the record.

### Step D.3: Deliver.

Write an issue-specific compilation page in Notion:
- Title: `[Matter Name] — Record Extract: [Issue]`
- Content: exact quotes and facts with precise page citations

## Phase E — Incremental Updates

When new volumes are added (supplemental appendix, additional
RT volumes):
1. Run Phase A inventory on the new volumes only.
2. Run Phase B or C on the new volumes only.
3. Update the master index.

If a NotebookLM notebook is still active, add the new volumes
as sources to the existing notebook.

## Completion

When all volumes are digested:
1. Update the project page status to Done.
2. Post in the matter Slack channel:
   "Record digest complete for [matter name]. [N] volumes
   indexed. Master index: [Notion URL]."
3. Note on the project page which ingestion mode was used.

## Quality Standards

- **Page numbers must be exact.** Do not estimate or round.
  Flag uncertain pages with [PAGE TBD].
- **Document identification must be precise.** Distinguish
  complaint from cross-complaint, instructions from verdict
  forms, motions from orders. Note the filing party.
- **Cautions field is mandatory for AA digests.** Every entry
  must flag potential misidentification risks.
- **Topic tags must be specific enough to search.** Not
  "testimony about the business" but "founding of SMI,"
  "50/50 arrangement," "K-1/W-2 documentation," "stock
  transfer demand."
- **NotebookLM output must be verified.** NotebookLM can
  hallucinate page numbers. For critical citations, pull the
  actual page from SharePoint to confirm.
