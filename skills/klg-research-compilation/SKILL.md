---
name: klg-research-compilation
description: "Compile Deep Research memos into a single research memorandum, extract authorities for Westlaw verification, and finalize the research package. Use whenever the user says 'compile the research memos', 'research memos are ready', 'extract authorities', 'compile and extract', 'process the research', 'finalize the research package', 'Westlaw authorities are downloaded', 'finalize the research', 'post-pipeline review', 'research pipeline is complete', or 'run the post-pipeline review'. This is Steps 4-5 of the KLG Research Pipeline (Phase A: compile + extract; Phase B: finalize after Westlaw; Post-Pipeline Review: strategic analysis after the assigned runner completes the mechanical pipeline). Also triggers when the user completed deep research prompts and returns with completed memos. Produces a compiled .docx research memo with convergence analysis, a paste-ready Westlaw authority list, and a final PDF research package. Do NOT use for case assessments, response plans, or research prompt generation (Step 1)."
---

# KLG Research Compilation & Authority Extraction

## Purpose

This skill handles two phases of the KLG Research Pipeline:

**Phase A (Compilation):** Read the completed Deep Research memos
from the Notion Research page (where Comet pasted them), compile
into a single research memorandum (.docx), perform convergence and
quality analysis, and generate a paste-ready Westlaw Find & Print
authority list for the Comet browser.

**Phase B (Finalization):** After Westlaw authorities are downloaded,
combine them with the compiled research memo into a final PDF
research package for the matter file.

This is Steps 4–5 of the KLG Research Pipeline:
1. Skill 3 generated research prompts into a Notion page
2. The assigned runner (William, Edwyn, or someone else) ran Comet
   Deep Research and pasted results back into Notion
3. (Comet completed — memos are on the Notion page)
4. **THIS SKILL (Phase A)** → Read Notion, compile, extract authorities
   → The runner runs Comet Westlaw Find & Print
5. **THIS SKILL (Phase B)** → Finalize research package
   → The runner notifies Tim with the completed package

**The assigned runner runs both phases.** Tim re-enters only after
the final package is delivered. The runner defaults to William
(matching Skill 3's default) unless the user specifies otherwise
or context makes clear a different runner (e.g., Edwyn) is doing
the mechanical pipeline. Tim's role — post-pipeline strategic
review — does not change regardless of who ran the mechanical
steps.

## Required Context

Before writing anything, read these reference files in the skill's
`references/` directory:

1. `references/claude-md-standards.md` — Citation formats
2. `references/klg-style-guide.md` — Writing voice
3. `references/compiled-memo-structure.md` — Document template
4. `references/comet-westlaw-prompt.md` — Westlaw prompt template
5. `references/handoff-standards.md` — Handoff instruction format
6. `references/workflow-patterns.md` — Iterative case memo and
   client memo patterns

## Required Inputs

### For Phase A:
- The Notion Research page URL (containing completed Deep Research
  memos pasted by Comet under each prompt)
- OR: Individual Deep Research memo files (PDFs or text) if the
  Notion workflow was not used

### For Phase B:
- The compiled research memorandum (produced in Phase A)
- The Westlaw Find & Print .doc file (downloaded by user after Comet run)

### Running in Chat vs. Cowork

This skill works in BOTH Chat and Cowork sessions. The Notion
connector and file creation tools are available in both modes.

**In Cowork:** The matter folder is auto-mounted. File outputs
save directly to the matter folder.

**In Chat:** The user provides the Notion page URL (same as
Cowork). For Phase B, the user uploads the Westlaw .doc into
the chat. File outputs are delivered as downloads in the
conversation — the user must manually save them to the matter
folder.

The advantage of Chat mode is that multiple compilation
projects can run in parallel. For example, while one Chat tab
is compiling Case A's research, another tab can be compiling
Case B's research simultaneously.

## Interaction Rules

- When the user says the research memos are ready, ask for the
  Notion page URL if not provided.
- Use the Notion connector to fetch and read the full page content,
  including all research outputs pasted under each prompt.
- If some research outputs are missing (Comet didn't paste them),
  flag which prompts are incomplete and ask the user whether to
  proceed with what's available or wait.
- Pull the user through every step with crystal-clear handoff
  instructions. Never leave them wondering what to do next.
- Determine which phase to enter based on user context:
  - "research memos are ready" / "compile" → Phase A
  - "Westlaw authorities are downloaded" / "finalize" → Phase B
  - "post-pipeline review" / "research pipeline is complete" →
    Skip to Step 6 (post-pipeline review). Read the Notion page
    to get the compilation data, then present the high-leverage
    findings and multiple-choice options. This entry point is
    used when the assigned runner ran Phases A–B and Tim is
    picking up the strategic review.

---

## PHASE A: COMPILATION & AUTHORITY EXTRACTION

### CRITICAL: Efficiency Guidance

The research memos will typically total 30,000–50,000 words.
DO NOT attempt to re-read or re-analyze the full text multiple
times. Follow this lean workflow:

1. **Single-pass reading:** Read each memo ONCE. During that
   single read, extract: (a) the memo's key conclusions,
   (b) every citation to authority, and (c) any red flags.
   Do not go back and re-read memos.

2. **Extract authorities mechanically:** Citations follow
   predictable patterns (volume + reporter + page for cases,
   code + section for statutes). Extract them with pattern
   matching during the single read. Do not do a separate
   "analysis pass" for citations.

3. **Compile in one shot:** Build the compiled document as
   you read, not after multiple review passes. Each memo
   becomes one section of the compiled document.

4. **Do not stall.** If the Notion page is very large, read
   it in chunks but process each chunk immediately. Do not
   buffer everything and then re-process.

Target: Phase A should complete in 10–15 minutes, not hours.

### Step 1: Ingest from Notion

Fetch the Notion Research page using the Notion connector. Read
the full page content. For each prompt (1–10), locate the
"Research Output — Prompt [N]" section and extract the research
memo text.

Produce a BRIEF inventory (do not assess quality — just confirm
presence and approximate length):

```
RESEARCH MEMO INVENTORY
═══════════════════════
Notion page: [title]
Memos received: [N] of 10

✓ Prompt 1: [title] — present
✓ Prompt 2: [title] — present
...
✗ Prompt [N]: [title] — MISSING

Proceeding with compilation of [N] memos.
```

If all memos are present, proceed WITHOUT asking for confirmation.
Only pause if memos are missing and ask the user whether to
proceed or wait.

### Step 2: Single-Pass Extract and Compile

In ONE pass through the memos, do the following simultaneously:

**For each memo (1 through 10):**

a. Read the memo text.

b. Extract the key findings: governing rule, lead authorities,
   strongest arguments for and against, and the memo's conclusion.
   Summarize each in 2–3 sentences (not full reproduction).

c. Extract every citation to authority. Record: case name,
   full citation, which memo it appeared in.

d. Note any citation that looks suspicious (unusual reporter,
   non-standard format). Mark with ⚠️.

e. Move to the next memo. Do not re-read.

**After reading all memos:**

f. Build the convergence table: sort authorities by how many
   memos cite them. This is a simple count — do not re-analyze.

g. Build the hallucination flag list from the suspicious
   citations noted in step (d).

### Step 3: Produce the Compiled Document

Produce the compiled .docx by cloning the KLG Case Memo template
and editing it. The content structure is in
`references/compiled-memo-structure.md`. Do NOT generate from
scratch with docx-js.

**Template location:**
1. **Cowork:** Look for an existing KLG case memo `.docx` in the
   working folder. If found, clone it. If not found, prompt:
   "Should I (a) use the project template, or (b) point me to
   a specific file?"
2. **Chat or fallback:** Use `/mnt/project/KLG_Case_Memo.docx`.
3. If neither is available, ask the user to upload the template.

**Clone-and-edit workflow:**
1. Read `/mnt/skills/public/docx/SKILL.md` — "Editing Existing
   Documents" section.
2. Copy the template to the working directory.
3. Unpack:
   ```
   python /mnt/skills/public/docx/scripts/office/unpack.py template.docx unpacked/
   ```
4. Examine `unpacked/word/document.xml` for the template's XML
   structure and named styles.
5. Edit `unpacked/word/document.xml` using `str_replace` —
   replace placeholder text within `<w:t>` elements, preserving
   all `<w:pPr>` and `<w:rPr>` formatting blocks.
6. Repack:
   ```
   python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ output.docx --original template.docx
   ```
7. Validate:
   ```
   python /mnt/skills/public/docx/scripts/office/validate.py output.docx
   ```
8. Fix standalone declarations (prevents Word "unreadable content" error):
   ```
   python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py output.docx
   ```
9. Deliver to `/mnt/user-data/outputs/`.

Do not specify fonts, margins, or page sizes. The template carries
all formatting.

**Key efficiency rule:** For the "Issue-by-Issue Analysis"
sections, use the summaries extracted in Step 2 — do not go
back to the original memos. The compiled memo synthesizes
findings; it does not reproduce them in full.

Name the file: `[CaseShortName]-Compiled-Research-[YYYY-MM-DD].docx`

### Step 3a: Update the Notion Checklist

After compiling, update the Research Map checklist on the Notion
page. For each prompt that was included in the compilation,
update its "(Compiled: —)" field with the compilation filename.

For example, replace:
`- [x] **Prompt 1:** Supersession doctrine — HIGH *(Compiled: —)*`

With:
`- [x] **Prompt 1:** Supersession doctrine — HIGH *(Compiled: Toles-Compiled-Research-2026-03-01.docx)*`

Use the Notion `update-page` tool with `replace_content_range`.
The unique text per line (prompt number + issue title) ensures
reliable matching.

If any prompts were NOT included in the compilation (e.g.,
missing research output), leave their "(Compiled: —)" unchanged
and note in the compilation which prompts were excluded.

### Step 3b: Update Pipeline Indicator on Notion Page

After compiling and updating the checklist, update TWO things
on the Notion Research page:

**1. Title prefix:** Change `[3/5]` (or `[1/5]` if Comet did
not update it) to `[4/5]` at the start of the title. Leave
the rest of the title unchanged.

**2. Pipeline Status section:** Update the `## 🔄 Pipeline Status`
section. **Important — resilient update strategy:** Do NOT rely
on exact string matching of the existing Pipeline Status content.
Instead, fetch the page first to get the current text, then use
the `## 🔄 Pipeline Status` heading as the anchor and replace
everything from that heading to the end of the page (or to the
next `##` heading if one follows). If the exact `old_str` match
fails, fall back to `replace_content` on the full section using
a broader anchor. The content to write:

```
**Current step:** 4 of 5 — Research compiled, authorities extracted
**Last completed:** [N] memos compiled into [filename] ([Date])
**Next action:** Give the Westlaw authority list to Comet for Find & Print (see Comet prompt above)
**After that:** Upload the Westlaw .doc and say: "The Westlaw authorities are downloaded. Please finalize the research package."
**Estimated time for next step:** ~10–20 min for Comet Westlaw run; then ~5–10 min for Claude finalization
```

**Fallback if update_content fails:** If the string-match
replacement fails silently (returns success but the page content
doesn't change), fetch the page again, identify the actual
current text of the Pipeline Status section, and retry with the
correct `old_str`. Never assume the pre-populated template text
is still exactly as written — Comet, the user, or Notion
formatting may have altered it.

### Step 3c: Write Executive Summary to Notion Page

After updating the checklist and pipeline status, write a 3–5
paragraph executive summary directly into the Notion page. Insert
it between the Research Map checklist section and the first
prompt section.

Use this heading: `## 📋 Research Summary`

The summary should cover:
1. **The core question** — What was this research trying to
   answer? (1 sentence)
2. **What the research found** — The bottom-line answer across
   all memos. (1–2 paragraphs)
3. **Strongest authorities** — Name the 3–5 most important cases
   or statutes and what they establish. Include short-form cites.
4. **Gaps and conflicts** — Any areas where the memos disagree,
   where authority is thin, or where further research is needed.
5. **Practical bottom line** — What this means for the case
   strategy. (1 paragraph)

This summary serves as the quick-reference so the attorney can
assess the research results without downloading and reading the
full compiled .docx.

**After Phase B (Westlaw verification):** If any authorities
were flagged as hallucinated, modified, or overruled, update the
Research Summary to reflect the corrected picture. Add a note:
"Updated [Date] after Westlaw verification: [N] authorities
confirmed, [N] removed/corrected."

### Step 4: Generate Westlaw Authority List

Produce a clean, deduplicated authority list formatted for
Westlaw Find & Print:

- Cases: reporter volume, reporter name, and start page ONLY
- Statutes: code name and section number
- One authority per line
- Deduplicate before generating (same authority with different
  pincites = include base citation only once)

**If the list is 100 or fewer items:** produce a single batch.

**If the list exceeds 100 items:** split into batches of 100
or fewer, labeled sequentially (Batch 1 of N, Batch 2 of N, etc.).

### Step 4a: Write Authority List to Notion

Write the authority list (and batches, if applicable) directly
to the Notion Research page. Add a new section at the bottom
of the page, before the "📎 Links and References" section:

```
## Westlaw Authority List

**Total authorities:** [N]
**Batches:** [1 / N] (Westlaw Find & Print limit: 100 per batch)
**Status:** DRAFT — AI ASSISTED — Pending Westlaw verification
**Pipeline Stage:** Step 4 of 5 — Westlaw Find & Print pending

### Batch 1 of [N] (items 1–100):

```
75 Cal.App.5th 1234
33 Cal.4th 653
592 F.3d 1063
Cal. Prob. Code § 8200
...
```

### Batch 2 of [N] (items 101–[M]):

```
...
```
```

Each batch goes in its own code block so Comet can copy-paste
it directly into Westlaw's Find & Print input field.

Also produce the authority list as a separate .txt file for
the user's records.

### Step 5: Generate Comet Westlaw Prompt

Read `references/comet-westlaw-prompt.md` for the base template.
Instead of embedding the full authority list in the Comet prompt,
direct Comet to the Notion page where the batches are posted.

The Comet instruction should handle ALL batches in a single
session without human intervention.

### Step 6: Handoff Instructions

CRITICAL FORMATTING RULE: The handoff to the user must consist
of THREE separate outputs, clearly separated. Do NOT combine
them into a single code block or a single message.

**Output 1 — Status Report (plain text, NOT in a code block):**

Tell the user what just happened, in regular chat text:

"[N] legal authorities have been extracted from 10 Deep
Research memos and posted to the Notion Research page
([B] batch(es), under the Westlaw limit). Backup .txt
file saved to your folder."

**Output 2 — Comet Prompt (standalone code block):**

Deliver the Comet instruction in its OWN code block with
NOTHING else — no status report, no instructions to the user,
no preamble. Just the Comet instruction that the user will
copy-paste directly:

```
Go to this Notion page:
[Notion page URL]

Scroll to the section "Westlaw Authority List."
You will find [B] batch(es) of authorities, each
in its own code block.

For EACH batch, do the following:

a. Copy the full contents of the batch code block.
b. Open a new browser tab.
c. Navigate to Westlaw Find & Print.
d. If a login screen appears, pause for user login.
e. Paste the batch into the Find & Print input field.
f. Verify the pasted content matches.
g. NEVER choose "Substitute with reporter images
   when available (PDF)" or similar options.
h. Apply these settings:
   - Documents: Full text documents
   - Cases: Full text documents with reporter images
   - Statutes & Court Rules: Statutory text only
   - Delivery: Download
   - Format: Word (.doc)
   - Output: Single merged file
i. If Westlaw reports citations are out of plan,
   unselect them. Do not incur additional charges.
j. If Westlaw does not accept certain citations,
   skip them and note which ones at the end.
k. Execute Find & Print and download the .doc file.
l. Move to the next batch and repeat steps a–k.

When ALL batches are done, confirm to the user
which citations were successfully retrieved and
which were rejected or out of plan.
```

**Output 3 — Next Steps (plain text, NOT in a code block):**

After the Comet code block, tell the user what to do:

"Copy the code block above and paste it into a new Comet
session. Comet will handle all [B] batch(es) automatically.

When Comet finishes:
1. Save the Westlaw .doc file(s).
2. Come back to THIS Claude Chat session.
3. Upload the Westlaw .doc file(s).
4. Say: 'The Westlaw authorities are downloaded. Please
   finalize the research package.'

I'll produce the final research package. Once that's done,
you'll notify Tim in the matter Slack channel that the
pipeline is complete."

DO NOT ask the user about the case memo, client memo,
high-leverage findings, or recursive research at this point.
Those questions are strategic attorney decisions that belong
in the post-pipeline review — which runs either at the end of
Phase B (if Tim is running this session) or in a separate Tim
session (if the assigned runner ran the mechanical pipeline).
Either way, the user needs to go run Comet right now — do not
delay them with questions.

---

## PHASE B: FINALIZATION

Triggered when the user says the Westlaw authorities have been
downloaded or are available.

### Step 1: Verify Westlaw Output

**IMPORTANT:** Westlaw's "Word" delivery format produces an RTF
file with a `.doc` extension — NOT a true `.docx` file. Do NOT
attempt to unpack it as a `.docx` (it will fail). Instead:

1. Check the file type: `file [uploaded_file]` — expect "Rich
   Text Format data"
2. Convert to plain text using pandoc:
   ```
   pandoc -f rtf -t plain [uploaded_file] -o westlaw_extracted.txt
   ```
3. Read `westlaw_extracted.txt` to verify and count authorities.

Check:
- How many authorities were successfully retrieved?
- Were any citations rejected or missing?
- Were any out-of-plan authorities excluded?

Report:
```
WESTLAW RESULTS
═══════════════
Authorities requested: [N]
Successfully retrieved: [N]
Not found / rejected: [list any]
Out of plan (excluded): [list any]
```

### Step 2: Cross-Reference

Compare Westlaw results against hallucination flags from Phase A:
- Which flagged citations were confirmed real?
- Which flagged citations were not found (likely hallucinated)?
- Surprises — citations expected to be real but not found?

Update confidence ratings accordingly.

### Step 3: Produce Final Research Package

**3a. Generate the combined PDF** using the PDF skill:

1. **Cover Page** — Title, case info, date, TOC
2. **Compiled Research Memorandum** — Updated with Westlaw
   verification results
3. **Authority Verification Summary** — Confirmed, unconfirmed,
   hallucinations removed
4. **Westlaw Authorities** — Full text from Westlaw .doc merged in

Deliver this PDF to `/mnt/user-data/outputs/` for the user to
download. Name it: `[CaseShortName]-Final-Research-Package-[YYYY-MM-DD].pdf`

Tell the user: "The final research package PDF is ready for
download. Save it to the matter folder on SharePoint under
`KLG Research/`."

**3b. Create the Compiled Research child page in Notion.**

This is the working copy that Claude will use in future sessions.
Create a child page UNDER the original Research page (using the
Research page ID as the parent `page_id`):

Title: `Compiled Research — [Case Short Name] ([Case No.])`

Content (as Notion-flavored markdown):

```
**Matter:** [Full case name], Case No. [Number]
**Date:** [Date]
**Status:** DRAFT — AI ASSISTED
**Source:** Compiled from [N] Deep Research memos

---

## Compiled Research Memorandum

[The full compiled memo text — the same content that went into
the PDF, but as Notion text rather than a formatted document.
Include all section headings, analysis, and citations.]

---

## Authority Verification Summary

**Authorities requested:** [N]
**Confirmed via Westlaw:** [N]
**Not found / rejected:** [list any]
**Likely hallucinated (flagged and removed):** [list any]

[Include the full verification table showing each authority,
which memos cited it, and its verification status.]

---

## Convergence Analysis

[The convergence table from Phase A showing which authorities
appeared across multiple memos, sorted by citation count.]

---

## High-Leverage Findings

[The strategic distillation from Step 6a — eureka ideas,
key authorities, and deployment recommendations.]
```

This child page is text-only — no file attachments needed.
Claude can read it in any future session via a single Notion
fetch of the parent page (which will show the child page link)
or by searching for the case name in the Research database.

### Step 4: Update the Notion Parent Page

Update the original Notion Research page to reflect completion:

**1. Title prefix:** Change `[4/5]` to `[5/5]` at the start
of the title. Leave the rest of the title unchanged.

**2. Page properties:**
- Change the "Publish or Pass?" status to "Not Applicable"
- Add a note that the research pipeline is complete
- Add the date of completion

**3. Pipeline Status section:** Update the `## 🔄 Pipeline Status`
section using the same resilient strategy as Phase A — fetch the
page first to get the current text, use the heading as the anchor,
and replace the section content. If exact string matching fails,
fall back to a broader anchor. The content to write:

```
**Current step:** 5 of 5 — Research pipeline complete ✅
**Last completed:** Final research package produced ([Date])
**Compiled research:** [link to child page created in Step 3b]

**Post-pipeline review (Tim):** Open a new Claude Chat in the KLG Appellate Practice project and paste:
"The research pipeline is complete for [Case Name] ([Case No.]). The Notion page is: [Notion page URL]. Please run the post-pipeline review."

**Archive the case law (choose one or more):**
1. **Ingest to library:** Ask Claude to run the KLG Authority Library skill to save selected high-leverage authorities to the Research database.
2. **Download & save:** Download the final research package PDF from the Claude session and save to SharePoint → [Matter Folder]/KLG Research/
3. **Rerun in Cowork:** Start a Cowork session and say: "Finalize the research package for [Case Name] and save to the matter folder." Claude will save the PDF directly to SharePoint.
```

**4. Project status update:** Search the Projects database for
the project page associated with this research pipeline (by
matter name or case number, with Support Type = Research
Pipeline). Set the project's **Status** to "Done." This is
a mandatory terminal step — research pipeline projects must
not remain "In progress" after Phase B finalization completes.
If no project page is found, note this as a gap but do not
create one retroactively.

### Step 5: Final Handoff

Present the completion summary in plain text (NOT in a code block):

"Research pipeline complete. [N] memos compiled, [N] authorities
verified via Westlaw, [N] confirmed hallucinations removed.
The final research package and Notion page have been updated."

**Determine whether Tim or the assigned runner is running this
session.** The simplest signal: if this session was started by
pasting the compilation prompt from the Comet completion message
(i.e., the research pipeline was delegated to a runner — William
by default, or Edwyn or someone else if specified earlier in the
pipeline), then that runner is running this session. If the user
is Tim (identified by context, prior messages, or explicit
statement), proceed directly to Step 6 as before.

If it's unclear who the runner was (e.g., no earlier context
carried the assignee forward), ask: "Is this Tim picking up the
post-pipeline review, or is this the runner (William, Edwyn, or
someone else) closing out the mechanical pipeline?"

**If a runner (not Tim) is running this session:**

Present the Slack notification for the runner to post (or offer
to post it via the Slack connector):

"The mechanical pipeline is done. The post-pipeline review
(high-leverage findings, case memo decisions, client memo,
recursive research) is Tim's call. Let me notify him."

Post (or offer to post) via the Slack connector to the
matter channel, substituting the runner's name and the Slack
ID reference table below:

```
This is Claude posting on [Runner Name]'s behalf.

*RESEARCH PIPELINE COMPLETE — [Case Short Name]*

<@U07PYJDNGT0> — The full research pipeline for [Case Name]
([Case No.]) is done.

*Deliverables:*
• Final research package (PDF): available for download or
  saved to the matter folder
• Compiled research memo and verification summary posted to
  Notion
• Notion page (now [5/5]):
  [Notion page URL]

*Summary:* [N] Deep Research memos compiled, [N] authorities
verified via Westlaw. [N] hallucinations removed, [N]
authorities confirmed.

*Post-pipeline review ready when you are.* Open a new Claude
Chat in the KLG Appellate Practice project and paste:

"The research pipeline is complete for [Case Name] ([Case No.]).
The Notion page is: [Notion page URL]
Please run the post-pipeline review."
```

The `<@U07PYJDNGT0>` mention stays fixed on Tim regardless of
who ran the pipeline — Tim is always the post-pipeline reviewer,
that role doesn't change with the runner.

### Runner Slack IDs (quick reference)

| Runner | Slack ID |
|---|---|
| William Hernandez (default) | U097FMSH3V4 |
| Edwyn Sierra | U0AS9KZQ69X |
| Tim Kowal | U07PYJDNGT0 |

If the runner confirms, post via the Slack connector to the
matter channel. If no matter channel exists, DM Tim.

**STOP HERE if a runner (not Tim) is running this session.** Do
not proceed to Step 6. The post-pipeline review runs when Tim
opens a new Chat and pastes the prompt from the Slack message.

**If Tim is running this session:**

Proceed IMMEDIATELY to the post-pipeline review steps below.
Do not wait for user input.

### Step 6: Deep Research Project Review

#### Step 6a: High-Leverage Findings

Using the summaries from Phase A (do NOT re-read the original
memos), produce the strategic distillation in plain text:

```
══════════════════════════════════════════════════
HIGH-LEVERAGE FINDINGS
[Matter Name] — [Date]
══════════════════════════════════════════════════

1. [Eureka idea title]
   Authority: [key citation]
   Why it matters: [1–2 sentences]
   How to deploy: [1–2 sentences]

2. [Eureka idea title]
   ...

3–5. [etc.]
══════════════════════════════════════════════════
```

#### Step 6b: Recursive Research Review

Using the research summaries and any case materials in context,
identify whether additional research rounds would be productive.
Look for: new legal theories not in the original 10 prompts,
secondary arguments worth exploring, adverse authority needing
deeper counter-research, creative angles, and unfilled gaps.

#### Step 6c: Present All Post-Pipeline Questions

After presenting the findings and any recursive research
opportunities, present ALL remaining questions to the user
in a SINGLE interaction. Use a multiple-choice format:

```
══════════════════════════════════════════════════
POST-PIPELINE OPTIONS
══════════════════════════════════════════════════

1. HIGH-LEVERAGE FINDINGS — Add to case memo?
   a. Yes — add to the evolving case memo
   b. No — keep it separate
   c. Yes, but let me review/edit first

2. COMPILED RESEARCH MEMO — Delivery preference?
   a. Add to existing case memo as a new section
   b. Keep as standalone document

3. CLIENT MEMO — Want a client-facing version?
   a. No — internal version only
   b. Yes — create client-ready version now
   c. Yes, but let me revise the internal memo first

4. ADDITIONAL RESEARCH — [describe what you found,
   or "No additional research areas identified"]
   a. Yes — run all [N] areas identified above
   b. Yes — but let me select which areas
   c. No — the research is sufficient

5. ARCHIVE CASE LAW — Save Westlaw authorities?
   a. Ingest selected authorities to the Research
      database (I'll show you which ones to pick)
   b. I'll download the PDF and save to SharePoint
      myself
   c. Let me rerun this final step in Cowork so
      Claude saves directly to the matter folder
   d. Skip — no archival needed
══════════════════════════════════════════════════
```

IMPORTANT: Present this as a SINGLE set of questions, not
spread across multiple messages. The user should be able to
answer all five at once (e.g., "1a, 2a, 3b, 4c, 5a") and
Claude executes all selected actions.

If the user selects option 5a (ingest authorities):
- Trigger the `klg-authority-library` skill in Mode 1.
- Pass the Westlaw .doc file (still in the session) and
  the convergence data from Phase A.
- The authority library skill handles selection, dedup,
  and Notion creation from there.

If the user selects option 5c (rerun in Cowork):
- Provide a copy-paste Cowork resume prompt:

```
Finalize the research package for [Case Name]
([Case No.]) and save to the matter folder.

The compiled research is on the Notion page:
[Notion page URL]

Save the final PDF to: KLG Research/
```

If the user selects additional research (option 4a or 4b):
- Generate new prompts using Skill 3 methodology
- Create a NEW Notion page: "[Case] (Round 2)"
- Link to same Case Portal
- Follow standard Skill 3 handoff

---

## Execution Rules

1. Read every research memo completely before compiling.
2. Never silently drop a citation. Every authority mentioned
   in any memo must appear in the master list.
3. Flag duplicate citations across memos as convergent signals.
4. Hallucination detection is critical. Err on the side of flagging.
5. Westlaw authority list: cases by reporter volume/name/page only,
   no case names or years, one per line, deduplicated, written to
   the Notion Research page in batches of 100 or fewer. Also save
   as a .txt backup file.
6. Compiled memo must be usable standalone before Westlaw verification.
7. Write in KLG Style Guide voice. No legalese. Plain English.
8. Pull the user through every step with crystal-clear handoff
   instructions. Follow the handoff standards format.
9. Phase A output: compiled .docx + authority list .txt
   Phase B output: final merged PDF research package
10. If the user provides the Notion page URL, always use the Notion
    connector to read the research. Only fall back to uploaded files
    if the user explicitly provides them instead.
11. Update the Notion page status when the pipeline completes.
12. At the end of every phase, state clearly:
    "Action item:" [single clear next step]
    "Next stage:" [what follows after completion]
13. ALL post-pipeline questions (case memo, client memo,
    high-leverage findings, recursive research, case law
    archival) are presented ONCE as a single multiple-choice
    interaction. NEVER ask these questions during Phase A or
    at the Westlaw handoff point. If Tim is running this
    session, present them at the end of Phase B. If a runner
    (William, Edwyn, or someone else) ran the mechanical
    pipeline, these questions are deferred to Tim's
    post-pipeline review session (triggered separately).
14. The Comet prompt at the Westlaw handoff MUST be in its own
    standalone code block with no other content. The user will
    copy-paste it directly into Comet. Do not mix it with
    status reports or instructions.
