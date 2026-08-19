---
name: klg-brief-elevation
description: "High-level strategic review and elevation of draft appellate briefs via an elite appellate panel. Use whenever the user says 'review this brief', 'elevate this brief', 'triage this brief', 'get this file-ready', 'brief elevation', 'improve this brief', or uploads a draft brief seeking strategic feedback or quality assessment. Also triggers for client revision review - 'client sent back the brief', 'client has comments', 'client edits', 'client revisions', 'review client comments', 'process client changes', 'client wants changes', or uploads a brief returned by the client with comments, tracked changes, or requested revisions. Assesses the brief's state, recommends a path (triage vs. systematic elevation vs. client revision review), and executes improvements. NOT for line editing or style checks (use klg-style-guide-check), case assessments, response plans, or research."
---

# KLG Brief Elevation

## Purpose

Provide elite-level strategic review of draft appellate briefs to
identify and execute the highest-leverage improvements. This skill
treats the brief as a work-in-progress that needs to reach its
full potential — whether that means a focused triage pass to get
it file-ready under time pressure, a systematic multi-phase
elevation to elite status, or a disciplined review of client
comments and requested revisions to determine which to incorporate
and which to push back on.

The skill assembles a virtual panel of elite appellate advocates
(modeled on the combined perspectives of Bryan Garner, Paul Clement,
and Lisa Blatt) to provide strategic assessment and concrete
recommendations. It then works with the attorney to execute
those recommendations.

This is NOT a proofreading or style-conformance tool — that is
the `klg-style-guide-check` skill. This skill operates upstream
of style checks, at the level of strategy, structure, framing,
and argument development.

## Required Context

Before analyzing any brief, read these project files:

1. `/mnt/project/klg-style-guide.md` — Writing standards and voice
2. `/mnt/project/claude.md` — Citation standards, output rules,
   quality controls
3. `/mnt/project/handoff-standards.md` — Handoff formatting
4. `references/workflow-patterns.md` — Iterative case memo,
   client memo, and session logging patterns

Then read the detailed review frameworks in this skill's
`references/` directory:

5. `references/elite-panel-framework.md` — Strategic review criteria,
   deliverable structure, and add-on review modes
6. `references/final-draft-review.md` — Near-final review framework
   including fact-checking, quote verification, and citation accuracy
7. `references/briefing-standards.md` — KLG brief argument structure,
   citation conventions, and drafting standards
8. `references/client-revision-review.md` — Client revision review
   workflow (Steps D.1–D.7): feedback extraction, evaluation
   framework, sensitive item walkthrough, redline production,
   and email synopsis generation. Read this when Path D triggers.
9. **KLG Brief Quality Rubric** (Notion, fetched, not a local
   file) — shared Brief Quality and Value Contribution vocabulary
   also used by `klg-case-assessment` and `klg-brief-postmortem`.
   v0.1, not yet attorney-calibrated — use it, but don't treat its
   grade anchors as settled.

Do not skip these reads. The review quality depends on having these
standards loaded.

## Required Inputs

- A .docx brief (the draft to review)
- Helpful but not required: case assessment memo, response plan
  memo, opposing brief(s), relevant orders/rulings, the appellate
  record or key record excerpts

## CRITICAL: Getting the .docx Binary

The tracked-changes workflow (unpack → edit XML → repack) requires
the actual .docx binary file in the container filesystem. This is
the ONLY reliable path for producing a redlined brief that Word
can open.

**How to get the .docx:**

1. **User uploaded it** — use the file from `/mnt/user-data/uploads/`.
   This is the preferred path.

2. **Cowork with matter folder** — copy from the mounted folder.
   Also reliable.

3. **SharePoint via M365 connector** — the connector can READ TEXT
   CONTENT from .docx files but CANNOT download the binary .docx
   to the container. This means you can read the brief's text for
   analysis, but you CANNOT unpack/edit/repack it.

**If the .docx binary is not available (SharePoint-only access):**

Do NOT attempt to generate the elevated brief from scratch using
docx-js or any other from-scratch method. From-scratch generation
is fragile, loses the attorney's formatting, styles, front matter,
and back matter, and risks producing corrupt files.

Instead, tell the user:

> "I can read the brief text through SharePoint for the strategic
> review, but I can't download the binary .docx to produce a
> tracked-changes redline. To get the redlined output, please
> upload the .docx file here in chat. You can download it from
> SharePoint at: [provide the webUrl from the search result]."

Then proceed with the strategic review (Phase 1/Phase 2A) using
the text content from SharePoint. When the user uploads the .docx,
proceed with the tracked-changes workflow.

**If the user cannot or will not upload the .docx:**

As a last resort, produce the elevated content as a standalone
replacement document with inline elevation notes (blue-bordered
boxes explaining each change). Make clear this is NOT a redline —
it is a parallel document that Ted/the attorney must work from
side-by-side with the original. Always run the file integrity
validation (step 8 in the Tracked-Changes Workflow) before
delivering any .docx produced outside the unpack/repack path.

## CRITICAL: Revision vs. Fresh Build Checkpoint

Before touching any .docx file, determine which path applies:

**Is this a revision to an existing document the user has already
edited, or a fresh build/elevation from an earlier draft?**

- If the user uploads a document they have already hand-edited
  and asks for targeted changes (add citations, change heading
  case, remove a section, fix numbering, replace phrases), this
  is a **SURGICAL REVISION**. ALWAYS unpack the user's current
  file and make targeted XML edits to only the affected
  paragraphs. NEVER unpack an earlier template or regenerate
  content from scratch — doing so obliterates every edit the user
  has made.

- If the user uploads a draft for full strategic elevation (the
  normal brief-elevation workflow), use the tracked-changes
  workflow below, which also operates on the user's document.

The only time it is acceptable to rebuild from a template is when
the user explicitly asks for a fresh build. When in doubt, ask.

## CRITICAL: Citation Integrity

When inserting or adding citations from a source document (case
memo, research memo, record, or any other source):

1. **Read the actual source document** and extract the literal
   citation strings as they appear.
2. **Present the extracted citations to the user** for
   confirmation before inserting them into the brief.
3. **Never invent or infer citation formats.** If a citation
   cannot be found in the source, flag it as missing rather than
   guessing. Write `[RECORD CITE NEEDED — not found in source]`
   and move on.
4. **Never fabricate record volume or page numbers.** Formats
   like `(CT 6)` or `(1 CT 10)` must come from an actual source
   document — never generated from inference.
5. **Never dispatch a subagent to generate citations.** Citation
   extraction must be done by reading the source directly, not
   by asking a subagent to produce them from memory.

## Appellate Style Rules

These apply whenever this skill produces or modifies brief text:

- **Party designations:** Refer to our client by their appellate
  party designation (e.g., "respondent," "appellant"), not
  trial-court designations like "plaintiff" or "defendant," unless
  quoting from a trial court document.
- **Emphasis:** Use italics for emphasis in brief text. Bold is
  acceptable only for dates. Never use bold for textual emphasis.
- **Block quotes from rules/statutes:** Extended quotations from
  rules or statutes must use block-quote formatting (Quote style),
  not inline quotation.
- **Rules of Court short form:** After the first full citation,
  the correct short form is lowercase "rule" with no "Cal." prefix
  (e.g., "rule 8.108(e)(2)," not "Cal. Rules of Court, rule
  8.108(e)(2)").
- **Caption blocks:** Use cross-references to the "Parties"
  bookmark to maintain consistency with the template.
- **Thesis placement:** For each argument section, check whether
  the section's controlling claim appears in the preamble — the
  prose between the section heading and the first subsection — or
  is buried several paragraphs into a subsection. If buried, flag
  it for restructuring: the thesis belongs up front, with
  subsections developing it rather than introducing it for the
  first time.
- **Subheading discipline:** During the elevation pass, check every
  subheading against the claude.md rule — no new heading unless the
  analysis exceeds roughly two pages or a distinct analytical step
  warrants separation. Where a subheading was spawned for a minor
  sub-point that doesn't meet that bar, merge the segment back into
  running prose as a tracked change, so the attorney can review and
  accept or reject the merge rather than have it silently applied.

## Mode Selection — Cowork Default

This skill defaults to Cowork because the assessment phase benefits
enormously from full matter-folder access: Claude can cross-check
record citations, pull in the case assessment, review opposing
briefs, and verify factual claims against source documents.

**At the start of every session, present this:**

```
Before we start, how would you like to run this?

COWORK (recommended for brief elevation):
  ✓ I can read the full record, case assessment, opposing
    briefs, and any prior memos — giving me the context to
    provide the most thorough strategic review.
  ✓ I can cross-check record citations and verify factual
    claims against the source documents.
  ✗ Ties up Cowork for approximately 30–90 minutes depending
    on the path you choose.

CHAT:
  ✓ Keeps Cowork free for other work.
  ✗ You'll need to upload: (1) the draft brief, (2) any
    case assessment or response plan memos, (3) the opposing
    brief if one exists, and (4) key record excerpts for
    fact-checking. Without the full record, my ability to
    verify claims and spot opportunities will be limited.

Which do you prefer?
```

**Skip this question if:** the user explicitly says "in Cowork"
or "in Chat," the user has already uploaded the brief (clearly
chose Chat), the user is in Cowork with the matter folder
already mounted, or the user indicates this is a client revision
review (Path D is Chat-native — just upload the client's
marked-up brief).

**Cross-mode transitions:** Follow the standard patterns in
`/mnt/project/claude.md` for switching between modes.

## Pre-Phase 0 (Optional): Record Digest

If the matter folder contains a substantial record (multiple
PDFs, clerk's transcript, reporter's transcript), consider
producing a structured record digest before starting the
elevation. This front-loads the fact-finding work that otherwise
gets repeated every time a citation needs verification.

This step is optional — skip it for briefs where the record is
small or the attorney says to jump straight to elevation.

Record Digest format:
- **Key dates:** filing, trial, decisions, orders, judgment
- **Key findings:** with exact PDF page citations
- **Key quotes:** with exact transcript citations (RT page:line)
- **Monetary figures:** penalties, fees, costs, judgment totals
- **Parties and their roles:** who did what, corporate structure
- **Procedural posture:** where the case stands now

This digest becomes a reference document during elevation,
reducing the need to re-read source documents for each citation.
Flag any facts that appear in the brief but cannot be verified
from the available record — these become [RECORD CITE NEEDED]
placeholders.

Save the digest as `[Case Name] Record Digest.md` in the working
directory. Reference it throughout the elevation process.

## Phase 0: Brief Intake and State Assessment

### Step 0.1: Read Everything

Read the draft brief completely. Also read any supplementary
materials: case assessment, response plan, opposing briefs,
key orders. If in Cowork, browse the matter folder for these.
If a record digest was produced in Pre-Phase 0, load it now.

### Step 0.2: Classify the Brief's State

After reading, classify the brief into one of these states:

**EARLY DRAFT** — The brief has significant structural gaps:
missing sections (no introduction, no SOF, incomplete arguments),
placeholder text, arguments that are outlines rather than prose,
missing or sparse citations. Needs substantial work before it
could be filed.
→ *Tracked changes: No.* The brief needs restructuring and
  substantial new content, not incremental edits. Produce a
  strategic review report with paste-ready revisions instead.

**MID DRAFT** — All major sections exist and contain substantive
content, but arguments are underdeveloped, the narrative lacks
coherence, the structure may need reorganization, and citations
need work. Could be filed in an emergency but would not
represent KLG's best work.
→ *Tracked changes: Conditional.* If the user chooses Triage
  (Path B), produce a redlined version with the high-leverage
  changes as tracked changes so the attorney can accept/reject
  in Word. If the user chooses Systematic Elevation (Path A),
  defer tracked changes until the brief reaches near-final
  state through the revision process.

**NEAR FINAL** — Arguments are developed, citations are mostly
present, the narrative is coherent. But it could be significantly
stronger with strategic improvements: tighter framing, better
issue sequencing, sharper narrative, stronger authority
integration, punchier prose.
→ *Tracked changes: Yes.* Produce a redlined .docx with all
  proposed revisions as Word tracked changes and comments, in
  addition to the strategic review report. This gives the
  attorney the choice to accept/reject each change in Word.

**FINAL / POLISH** — The brief is substantially complete and
well-crafted. Improvements at this stage are incremental:
fine-tuning the introduction, sharpening transitions, tightening
language, ensuring the strongest possible first and last
impressions. This is where the "last 10%" of quality lives.
→ *Tracked changes: Yes.* All proposed changes delivered as
  tracked changes in the .docx. At this stage the brief is
  close enough that every change should be individually
  reviewable. Also run the final-draft review framework
  (references/final-draft-review.md) automatically.

### Step 0.2b: Identify the Brief Type

After classifying the brief state, also classify the brief type.
This affects structural expectations and determines which sections
are subject to elevation:

**WRIT PETITION** (supersedeas, mandate, habeas)
- Two-part structure: formal petition body (numbered sections
  I–VI with averments) + Memorandum of Points and Authorities
- Formal petition sections are preserved during elevation —
  they are formulaic and need only citation/fact accuracy, not
  rhetorical improvement
- Only the Introduction body and Memorandum content are elevated
- Argument is organized around the writ standard (e.g.,
  irreparable harm, substantial questions, balance of equities
  for supersedeas; inadequate remedy at law for mandate)

**OPENING BRIEF** (AOB, appellant's opening brief)
- Single continuous document: Introduction → Statement of the
  Case → Standard of Review → Argument → Conclusion
- Full content is subject to elevation
- Typically the most thorough elevation target

**REPLY BRIEF** (ARB, appellant's reply brief)
- Organized as responses to respondent's arguments
- Typically no Statement of the Case or Standard of Review
- Arguments follow RB structure, not AOB structure
- Each argument should follow the pattern: "We argued X → They
  argue Y → Y is wrong because Z"
- Tone calibration matters: firm but not defensive

**RESPONDENT'S BRIEF** (RB)
- Respondent's framing of facts and procedural history
- Arguments respond to appellant's claimed errors
- Must address every issue raised; failure to respond =
  concession risk

Include the brief type in the Phase 0 assessment presented to
the attorney.

### Step 0.3: Present the Assessment

Present the classification to the user with a brief explanation
of what you observed — including the brief type and the tracked-
changes plan for their state. Be specific and candid. Then
present the path options.

## Phase 1: Path Selection

After the state assessment, present the user with options:

```
Based on my review, this brief is in [STATE] condition.
Here is what I recommend:

PATH A — SYSTEMATIC ELEVATION (recommended if time allows)
  Multi-pass process to take this brief to elite status.
  Steps:
  1. Strategic review: framing, issue selection, structure,
     argument force, tone (I'll provide a full assessment
     with prioritized recommendations)
  2. Research gap analysis: identify weak or missing
     authorities, areas where deeper research would
     strengthen the brief
  3. Structural reorganization: if needed, propose a
     revised outline with reframing
  4. Execution: work through the high-priority changes
     with you, section by section
  5. Final review: near-final polish and quality check
  6. Hand off to style-guide-check for tracked-changes
     redlining
  ⏱️ Estimated: 2–4 hours across multiple sessions

PATH B — TRIAGE (for time-sensitive deadlines)
  Single-pass, high-leverage review. I'll identify the
  3–5 changes that would most improve this brief and
  provide paste-ready revisions. No deep research, no
  major reorganization — just the highest-impact fixes
  within the brief's existing structure.
  ⏱️ Estimated: 30–60 minutes

PATH C — TARGETED REVIEW
  Tell me what to focus on. Options include:
  - Introduction and framing only
  - Specific argument section(s)
  - Statement of Facts / Statement of the Case
  - Hostile-panel stress test
  - Aggressive trimming (cut 20%)
  - [Or describe your own focus]

PATH D — CLIENT REVISION REVIEW
  The client has returned the brief with comments, tracked
  changes, or requested revisions. I'll:
  1. Extract and catalog every client comment and change
  2. Evaluate each for strategic soundness and legal merit
  3. Produce a redlined .docx incorporating good changes
     and rejecting problematic ones
  4. Generate a paste-ready email synopsis: what they asked
     for, what we did, and why (with firm but professional
     explanations for anything we declined)
  ⏱️ Estimated: 30–60 minutes

Which path would you like to take?
```

Wait for the user's selection before proceeding.

## Phase 2A: Triage Mode

If the user selects Path B, execute a single high-leverage pass:

1. Read `references/elite-panel-framework.md` for the review
   criteria (focus on the Executive Assessment and High-Leverage
   Recommendations deliverables).

2. Produce a triage report structured as:

   **BRIEF ELEVATION — TRIAGE REPORT**
   **Case:** [case name]
   **Brief type:** [AOB/RB/ARB/Reply/Writ Petition]
   **Date:** [date]
   **Status:** AI-assisted review — requires attorney review

   **A. Executive Assessment** (2–3 paragraphs)
   - Current strengths
   - Critical weaknesses
   - The single most important improvement

   **B. Top 5 High-Leverage Changes** (prioritized)
   For each:
   - What to change and why it matters
   - Location in brief
   - Paste-ready proposed revision (complete replacement
     paragraph, not fragments)

   **C. Quick Wins** (can be fixed in minutes)
   - Specific line-level improvements that punch above
     their weight

3. Deliver the report as a .docx file using the docx creation
   workflow (read `/mnt/skills/public/docx/SKILL.md`).

4. **If the brief is MID DRAFT or above:** Also produce a
   redlined version of the brief with the proposed changes
   implemented as Word tracked changes. Follow the tracked-
   changes workflow described in "Tracked Changes Production"
   below. This gives the attorney a redlined .docx they can
   open in Word and accept/reject each change alongside the
   strategic report.

   If the brief is EARLY DRAFT, skip the redline — the changes
   are too structural to be expressed as tracked changes. The
   report with paste-ready revisions is the deliverable.

5. After delivery, offer:
   ```
   The triage report is complete. [If redlined: "I've also
   produced a redlined version with the proposed changes as
   Word tracked changes."] Would you like me to:

   1. Work through the proposed changes with you now
      (I'll present each one for your approval/modification)
   2. Hand off to a style-guide-check for mechanical redlining
   3. Both — work through strategic changes first,
      then run the style check
   ```

## Phase 2B: Systematic Elevation

If the user selects Path A, execute the full elevation process:

### Step 1: Strategic Review

Read `references/elite-panel-framework.md` and execute the
full elite panel review. Produce a comprehensive assessment
document with:

**A. Executive Assessment**
- Candid assessment of strengths and weaknesses
- The single most important improvement
- Brief's current "ceiling" vs. its potential

**B. High-Leverage Recommendations** (prioritized list)
Each recommendation explains:
- What to change
- Why it matters for appellate persuasion
- How to implement it
- Which panel perspective drives this recommendation
  (Garner/Clement/Blatt — only where it illuminates the point)

**C. Research Gaps**
- Authorities that need strengthening or verification
- Legal issues where deeper research could yield better support
- Missing contrary authority that should be addressed preemptively
- If significant: recommend generating deep research prompts
  (hand off to Skill 3)

**D. Structural Assessment**
- Does the brief need reorganization?
- Proposed revised outline (if reorganization recommended)
- Issue consolidation or reordering recommendations
- SOF/SOC restructuring if needed

**E. Introduction and Conclusion Rewrite**
- Proposed rewritten introduction following the funnel approach
  from the KLG Style Guide
- Proposed rewritten conclusion
- Both should be paste-ready

Deliver as a .docx file. Then consult with the user:

```
The strategic review is complete. Here is what I recommend
as the path forward:

[Summarize the top 3–5 recommendations with estimated
 effort for each]

How would you like to proceed?

1. Work through all recommendations in priority order
2. Select specific recommendations to pursue
3. Pause for research (I can generate deep research
   prompts for the identified gaps)
4. Proceed to structural reorganization first
```

### Step 2: Execute Changes

Work through the selected recommendations with the user.
For each recommendation:

1. Present the proposed change with context
2. Show the current text and the proposed replacement
3. Wait for the user's approval, modification, or rejection
4. Once approved, provide the final paste-ready text with
   exact location markers

For major rewrites (introduction, argument sections), read
`references/briefing-standards.md` to ensure the new text
follows KLG brief argument structure.

### Step 2b: Iterative Revision Rounds

After the initial execution pass, the attorney will typically
review the output and provide targeted feedback on specific
sections. This is normal and expected — it's how the brief
reaches its full potential.

For each round of attorney feedback:

1. Read the feedback carefully. Note which sections are affected
   and what specifically the attorney wants changed.

2. For each requested change, identify whether it's:
   - A content change (new framing, different emphasis, added facts)
   - A structural change (reorganize, merge, split sections)
   - A tone/voice change (stronger/softer, more/less formal)
   - A citation change (add, fix, or verify a citation)

3. Make the changes in the section-by-section draft, preserving
   all content outside the affected sections.

4. Present the revised section(s) to the attorney, showing what
   changed and why.

5. After revisions are accepted, check for ripple effects:
   - Does the Introduction still accurately preview the arguments?
   - Do cross-references between sections still work?
   - Are citation short forms still valid?

Common patterns from experience:
- The Introduction often takes 2–3 rounds of refinement because
  it must capture the entire case in compressed form
- The attorney may want specific framing language ("mandatory"
  vs. "prohibitory," "would shut down" vs. "shut down") that
  should be applied consistently throughout
- Em dashes, citation format, and terminology choices often need
  global find-and-replace after being identified in one section
- When the attorney gives a direction that applies broadly
  ("use 'mandatory' throughout," "always cite the SOD by PDF
  page"), implement it everywhere, not just in the section being
  discussed

### Step 3: Research Gap Resolution (if applicable)

If research gaps were identified and the user wants to pursue
them:

- Generate targeted research prompts (can hand off to
  `klg-deep-research-prompts` if a full pipeline run is
  warranted, or produce focused prompts inline for quick
  research)
- After research is completed, integrate new authorities
  into the brief

### Step 4: Final Review and Redline

After all changes are implemented, read
`references/final-draft-review.md` and perform:

- Fact-checking against source documents (if available)
- Quote verification
- Citation accuracy check
- Introduction effectiveness review
- Overall coherence and flow assessment
- Strength assessment of each main argument

Produce a final review report flagging any remaining issues.

**Tracked changes at this stage:** If the brief started as
EARLY or MID DRAFT and has now been elevated through the
revision process, produce a redlined .docx of the revised
brief with any remaining proposed changes as Word tracked
changes. The brief should now be developed enough that
incremental edits are the right tool. Follow the "Tracked
Changes Production" workflow below.

If the brief started as NEAR FINAL or FINAL, the tracked-
changes redline was already produced in Step 1. At this stage,
produce a fresh redline of the revised brief incorporating
any changes from Steps 2–3.

### Step 4.5: Assembly (Before Style Check)

After the elevation changes are finalized and the section-by-
section draft is complete, the elevated content needs to be
assembled into the KLG brief template (.docx). This step bridges
elevated markdown content and the final Word document.

If the `klg-brief-assembly` skill is available:

```
The elevated content is ready. Before the style check, I need
to assemble this into the KLG brief template. I'll use the
brief assembly skill to:

1. Convert the elevated markdown to properly styled Word XML
2. Remap all heading styles to KLG custom styles
   (P1Pleading1, P2Pleading2, P3Pleading3)
3. Splice the new content into the existing brief template
4. Preserve front matter, formal sections, and back matter

After assembly, you'll want to:
- Update the TOC and TOA in Word
- Update the Certificate of Word Count
- Review heading formatting (centered small caps for P1, etc.)

Then we can run the style-guide-check on the assembled brief.
```

If the assembly skill is not available, provide manual guidance:

```
The elevated content needs to be placed into the .docx template.
The content is in markdown format with # / ## / ### headings.
You can either:

1. Copy-paste sections into the existing .docx in Word
2. Use pandoc conversion + style remapping (pandoc converts
   markdown to Heading1/2/3, which must be remapped to
   P1Pleading1/P2Pleading2/P3Pleading3)

Key mapping:
  # headings  → P1Pleading1 (centered, small caps)
  ## headings → P2Pleading2 (bold)
  ### headings in Argument → P3Pleading3
  ### headings in Statement of Case → italic subheadings
```

### Step 5: Style Check Handoff

After assembly (or if no assembly is needed because changes
were made directly in the .docx), offer to hand off to the
style-guide-check skill:

```
═══════════════════════════════════════════════════
✅ BRIEF ELEVATION COMPLETE
═══════════════════════════════════════════════════

The strategic review and revisions are done. [If a redlined
version was produced: "The redlined .docx is ready for your
review in Word — accept or reject each change."]

[If assembly was performed: "The assembled brief is ready.
Remember to update the TOC, TOA, and word count in Word."]

The next step is a style-guide conformance check, which will
produce an additional redlined .docx focused on mechanical
and style issues (terminology, citations, formatting, etc.).

You may also want to run a citation audit (klg-cite-check)
to catch any missing pincites, uncited factual assertions,
or unresolved placeholders before filing.

WHAT TO DO NEXT:

1. Review the redlined brief and accept/reject changes.
2. Once you have a clean version with accepted changes,
   upload it and say:

   "Please run a style guide check on this brief."

   Or for a citation audit:
   "Check the citations on this brief."

⏱️ EXPECTED: The style check takes 10–20 minutes and
produces a redlined document plus a conformance report.
═══════════════════════════════════════════════════
```

## Phase 2C: Targeted Review

If the user selects Path C, execute only the requested focus
area. Read `references/elite-panel-framework.md` for the
relevant criteria. For each available focus mode:

**Introduction and framing only:**
Review and rewrite the introduction using the funnel approach.
Assess the brief's overall framing and narrative.

**Specific argument section(s):**
Deep-dive on the identified sections: argument structure,
authority usage, rule application, persuasive force.

**Statement of Facts / Statement of the Case:**
Review for narrative effectiveness, appropriate emphasis,
completeness, proper record citations, and separation of
facts from procedural history.

**Hostile-panel stress test:**
Assume a skeptical or hostile panel. Identify vulnerabilities,
weak points, and places where the brief could lose credibility.
Recommend preemptive reframing. (See the "Hostile panel" add-on
in `references/elite-panel-framework.md`.)

**Aggressive trimming:**
Assume the brief must be cut by 20%. Identify what should be
deleted or consolidated first, prioritized by what loses the
least persuasive value.

## Phase 2D: Client Revision Review

If the user selects Path D — or if the user indicates the client
has returned a brief with comments or requested revisions — execute
the client revision review workflow.

### Auto-Detection

If the user uploads a brief and says anything indicating it came
back from the client with comments or edits, skip the normal Phase 0
state assessment and Phase 1 path selection. Go directly to Path D.
The user does not need to know the internal path labels. Trigger
phrases include: "client sent this back," "client has comments,"
"client wants changes," "client marked this up," "here are the
client's edits," "client feedback on the brief."

### Path D is Chat-native

Client revision review does not require Cowork. The client's
marked-up brief contains all the feedback. Skip the mode selection
prompt unless the user specifically wants to cross-check client
comments against the record (in which case Cowork helps).

### Workflow Overview

Path D produces two deliverables:

1. **Redlined .docx** — incorporates good changes, rejects bad
   ones, flags items needing attorney judgment. All tracked
   changes authored by "KLG — Rev. Review" (distinct from
   elevation and style-check authors).

2. **Paste-ready email synopsis** — numbered list the attorney
   can send to the client: what they asked for, what we did,
   and why. Firm but professional explanations for declined items.

For sensitive items (client criticism of our work, frustration,
factual disputes), Claude walks the attorney through a five-
category framework to draft the right response — from owning
genuine errors to diplomatically explaining when the client
didn't give us enough information.

### Detailed Instructions

Read `references/client-revision-review.md` for the complete
step-by-step workflow (Steps D.1 through D.7):

1. **D.1** — Extract all client feedback (comments, tracked
   changes, inline annotations, text notes)
2. **D.2** — Present the Client Feedback Inventory with
   sensitivity flags
3. **D.3** — Evaluate each item (incorporate / modify /
   decline / needs attorney judgment)
4. **D.4** — Sensitive item walkthrough with the attorney
5. **D.5** — Produce the redlined .docx
6. **D.6** — Generate the email synopsis
7. **D.7** — Deliver both and hand off to style check

## Cowork-to-Chat Offboard Point

The brief assessment (Phase 0) and strategic review (Phase 2B,
Step 1) benefit most from Cowork's full matter access. After
the strategic review is delivered, the remaining work (executing
changes, style check) can run in Chat.

**Path D (Client Revision Review) is Chat-native.** The user
uploads the client's marked-up brief and Claude processes it.
No matter folder access is needed — the brief itself contains
all the client feedback. Cowork is only useful if the attorney
wants Claude to cross-check client comments against the record
(e.g., the client says "this fact is wrong" and the attorney
wants Claude to verify against the source documents).

**After delivering the strategic review, tell the user:**

"The strategic review is complete. If you'd like to free up
Cowork, you can continue the execution phase in Chat. Here's
what to upload:"

Then list the specific files:
- The draft brief (.docx)
- The strategic review report just produced
- The case assessment memo (if one exists)
- The opposing brief (if relevant)
- Any specific record excerpts referenced in the review

Provide a copy-paste Chat resume prompt:

```
I have the draft [brief type] and the strategic review
report for [Case Name] ([Case No.]). Please help me work
through the recommended changes. [Describe which
recommendations to start with.]
```

## Execution Rules

1. Read the ENTIRE brief before making any assessment. Do not
   start writing the review after reading only part of the brief.

2. Be candid but constructive. This is an elite review — the
   attorney needs honest assessment, not reassurance. But frame
   weaknesses in terms of opportunities for improvement.

3. Never change legal strategy without the attorney's approval.
   Present options and recommendations; let the attorney decide.

4. All proposed replacement text must be paste-ready: complete
   paragraphs with citations, not fragments or outlines.

5. Apply KLG Style Guide standards to all proposed text.
   Citations in California Style Manual format for CA authorities,
   Bluebook for federal.

6. Never fabricate case citations. Flag anything needing human
   follow-up — an uncertain citation, a legal principle that needs
   authority support — with the single uniform tag
   `[VERIFY: short description]` per claude.md's placeholder
   standard. No other lead word.

7. Record citations: use REF format, appendix format, or
   document-name format per claude.md. Insert [Record cite
   needed] where a cite is required but unavailable.

8. For every proposed change, explain WHY it matters for
   appellate persuasion — not just what to change.

9. The "elite panel" framing is a device for generating
   high-quality analysis. Use it naturally — don't artificially
   attribute every point to Garner/Clement/Blatt. The panel
   perspectives are useful when they illuminate different
   dimensions of the same issue (e.g., Garner on prose clarity
   vs. Clement on strategic framing vs. Blatt on narrative force).

10. This skill produces tracked changes when the brief state
    and path warrant it (see Phase 0 state classifications).
    The tracked changes focus on strategic and structural
    improvements — not mechanical style fixes. For mechanical
    redlining (terminology, citation format, prohibited words),
    hand off to klg-style-guide-check after elevation is done.

11. After completing any deliverable, follow the handoff format
    from `/mnt/project/handoff-standards.md`.

12. After delivering the final review or report, offer to log
    this session to Notion (Pattern 3 in
    `references/workflow-patterns.md`), linked to the appropriate
    Case Portal entry.

13. This is internal work product. Include the AI transparency
    notice that this is an AI-assisted review requiring attorney
    review.

## Tracked Changes Production

When the brief state warrants tracked changes (see Phase 0
classifications), use the docx skill's XML editing workflow to
produce a redlined version of the original brief.

### When to Produce Tracked Changes

| Brief State   | Triage (Path B) | Systematic (Path A) | Targeted (Path C) | Client Rev. (Path D) |
|---------------|-----------------|---------------------|-------------------|----------------------|
| EARLY DRAFT   | No              | No (until Step 4)   | No                | Yes (always)         |
| MID DRAFT     | Yes             | No (until Step 4)   | If focused edit   | Yes (always)         |
| NEAR FINAL    | Yes             | Yes (Step 1)        | Yes               | Yes (always)         |
| FINAL/POLISH  | Yes             | Yes (Step 1)        | Yes               | Yes (always)         |

### Tracked-Changes Workflow

1. Read `/mnt/skills/public/docx/SKILL.md` for the XML editing
   mechanics (unpack → edit → pack → validate).

2. Copy the original brief to the working directory.

3. Unpack:
   ```bash
   python /mnt/skills/public/docx/scripts/office/unpack.py brief.docx unpacked/
   ```

4. Edit `unpacked/word/document.xml` using str_replace. For each
   proposed change:

   **Strategic revisions → tracked changes:**
   - Rewritten paragraphs (introduction, argument sections,
     SOF passages, conclusion)
   - Reframed headings
   - Restructured argument flow
   - Strengthened authority integration
   - Tightened prose where meaning changes

   **Suggestions that need attorney judgment → comments only:**
   - Major structural reorganizations (reordering entire sections)
   - Alternative framing options (present 2–3 choices)
   - Research gaps and suggested additional authorities
   - Questions about facts or strategy
   - Points where the attorney needs to make a judgment call

   **Tracked change mechanics:**
   - Use `w:del` with `w:delText` for deletions
   - Use `w:ins` with `w:t` for insertions
   - Author: "Claude — Brief Elevation" (distinct from
     "Claude" used by the style-guide-check skill, so the
     attorney can distinguish strategic edits from mechanical
     edits if both skills have been run)
   - Date: today's date in ISO format
   - Unique sequential w:id values
   - Preserve the original run's `<w:rPr>` formatting

   **Comment mechanics:**
   ```bash
   python /mnt/skills/public/docx/scripts/comment.py unpacked/ [id] "Comment text"
   ```

5. Repack:
   ```bash
   python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ brief-ELEVATED.docx --original brief.docx
   ```

6. Validate:
   ```bash
   python /mnt/skills/public/docx/scripts/office/validate.py brief-ELEVATED.docx
   ```

7. Fix standalone declarations (prevents Word "unreadable content" error):
   ```bash
   python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py brief-ELEVATED.docx
   ```

8. **MANDATORY: Validate file integrity before delivery.**
   ```bash
   python3 -c "
   import zipfile, sys
   path = 'brief-ELEVATED.docx'
   try:
       with zipfile.ZipFile(path, 'r') as z:
           names = z.namelist()
           assert 'word/document.xml' in names, 'Missing document.xml'
           assert z.read('word/document.xml')[:5] != b'\x00'*5, 'document.xml is null bytes'
       print(f'PASSED: {path} is a valid docx ({len(names)} entries)')
   except Exception as e:
       print(f'FAILED: {path} is corrupt — {e}')
       sys.exit(1)
   "
   ```
   If this check fails, **do not deliver the file.** Tell the user:
   "The .docx file failed integrity validation — it may be corrupt.
   This can happen when the file was generated from scratch rather
   than edited from the original. Please upload the original .docx
   brief and I'll redo the elevation using the tracked-changes
   workflow, which is more reliable."

   Do NOT silently deliver a file that fails this check.

9. Deliver as `[original-name]-ELEVATED.docx`.

### Division of Labor with Style-Guide-Check

This skill's tracked changes focus on **strategic and structural
improvements**: reframing, reorganization, argument strengthening,
narrative sharpening, prose tightening for persuasive impact.

The style-guide-check skill's tracked changes focus on
**mechanical conformance**: terminology fixes, citation format
corrections, heading formatting, prohibited words, punctuation,
and other KLG Style Guide rules.

Both can be run sequentially. The elevation pass runs first
(strategic), then the style check runs second (mechanical).
The different author names ("Claude — Brief Elevation" vs.
"Claude" vs. "KLG — Rev. Review") allow the attorney to
distinguish which pass produced which edit:

- **"Claude — Brief Elevation"** = strategic elevation edits
- **"KLG — Rev. Review"** = client revision review edits
- **"Claude"** = style-guide-check mechanical edits

## .docx Generation (Reports)

When producing report documents (triage report, strategic review),
clone the KLG Case Memo template and edit it — do not generate
from scratch with docx-js.

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
   all `<w:pPr>` and `<w:rPr>` formatting blocks. For proposed
   replacement text, use the template's block-quote or indented
   style if available, or add a thin left border to the paragraph
   properties.
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
all formatting. If you find yourself writing `font:` or `size:` or
`spacing:` in a script, you are on the wrong path.

## What This Skill Does NOT Do

- **Mechanical style conformance** → Use `klg-style-guide-check`
  (This skill does produce tracked changes for strategic edits,
  but it does not check for terminology, citation formatting,
  prohibited words, heading formatting, or other Style Guide
  rules. Run the style-guide-check after elevation for those.)
- **Case assessment** → Use `klg-case-assessment`
- **Response plan** → Use `klg-response-plan`
- **Deep research** → Use `klg-deep-research-prompts`
- **Research compilation** → Use `klg-research-compilation`

This skill focuses exclusively on strategic, structural, and
persuasive improvements to an existing draft brief.
