---
name: klg-case-assessment
description: "Generate comprehensive initial case assessment memos for potential appellate matters from uploaded trial court records. Use this skill whenever the user says 'create a case assessment', 'evaluate this case', 'initial case assessment', 'intake memo', 'should we take this case', or uploads trial court records (clerk's records, reporter's records, transcripts, pleadings, motions, orders, exhibits) and asks for analysis. Also triggers for supplemental assessments when new documents are added to an existing case evaluation. Produces a fully cited evaluation with traffic light ratings (merits, equities, ability to pay, practice alignment) and a take/decline recommendation. Output is a professional Word document (.docx) following KLG formatting standards. Do NOT use for post-intake work like response plan memos or research database generation."
---

# KLG Initial Case Assessment

## Purpose

Generate a comprehensive initial case assessment memo from uploaded
trial court records for a potential appellate matter. This is the
firm's first-pass attorney analysis of whether to take the case.
It produces a fully cited evaluation with traffic light ratings and
a take/decline recommendation.

When supplemental documents are later provided, this skill also
handles supplemental assessments that update the analysis without
starting from scratch.

## Required Context

Before writing anything, read these reference files in the skill's
`references/` directory for firm standards:

1. `references/claude-md-standards.md` — Citation formats, quality
   controls, AI transparency requirements
2. `references/klg-style-guide.md` — Writing voice and conventions
3. `references/klg-case-assessment-standards.md` — Analytical
   framework, traffic light definitions, cost anchors, current
   rate sheet, and engagement structure principles
4. `references/workflow-patterns.md` — Iterative case memo and
   client memo patterns
5. **KLG Brief Quality Rubric** (Notion, fetched, not a local
   file) — shared Brief Quality and Value Contribution vocabulary
   also used by `klg-brief-elevation` and `klg-brief-postmortem`.
   v0.1, not yet attorney-calibrated — use it, but don't treat its
   grade anchors as settled.

If any of these files are missing from the skill folder, prompt the
user to provide them. The skill cannot produce compliant output
without these standards.

## Required Inputs

- Case file documents (any combination of: clerk's record, reporter's
  record/transcripts, pleadings, motions, orders, exhibits, trial
  counsel analysis)
- If not apparent from documents, ask for: party names, case number,
  jurisdiction, trial court, and whether an NOA has been filed
- **Referral source.** Ask early in intake. If the matter is referred
  by David Zarmi (DZ), the DZ overlay skill (`klg-dz-overlay`) runs
  after this skill completes. Do not embed DZ-specific pricing logic
  here.

### Running in Chat vs. Cowork

Before starting, ask the user which mode they want to run in:

```
Before we start the case assessment, how would you like
to run this?

COWORK (recommended for case assessments):
  ✓ I can browse the full record — clerk's records,
    reporter's records, motions, orders, exhibits.
    This produces the most thorough assessment.
  ✗ Ties up Cowork for approximately 30–60 minutes.

CHAT:
  ✓ Keeps Cowork free for other work.
  ✗ You'll need to upload all relevant documents:
    the clerk's record, any reporter's records,
    key motions, orders, and the ruling being
    challenged. If documents are missing, the
    assessment may have gaps.

Which do you prefer?
```

**Skip this question if:** the user explicitly says "in Cowork"
or "in Chat," the user has already uploaded documents (clearly
chose Chat), or the user is in Cowork with the matter folder
already mounted (clearly chose Cowork).

**Cross-mode transitions:** If the user is in Chat and chooses
Cowork, provide step-by-step instructions to switch (click
Cowork in the top nav, select the matter folder) plus a
copy-paste start prompt for the Cowork session. If the user
is in Cowork and chooses Chat, provide instructions to switch
(click Chat, upload documents) plus a copy-paste start prompt.

### Cowork-to-Chat Offboard Point

After delivering the case assessment, tell the user:

"The case assessment is complete. You can now close this
Cowork session. For any follow-on work (research prompts,
response plan, client memo), open a Chat tab in the KLG
Appellate Practice project and upload the case assessment
memo. That single document contains everything Claude needs
to continue."

Then provide a copy-paste Chat resume prompt:

```
I have the case assessment for [Case Name] ([Case No.]).
[Describe the follow-on task, e.g., "Please generate deep
research prompts" or "Please create a response plan."]
```

## Interaction Rules

- Read ALL uploaded materials before writing anything.
- If referenced documents are not provided (e.g., the judgment is
  mentioned but not uploaded), ask specifically for them before
  proceeding. Do not guess at contents of missing documents.
- If you have enough to proceed but some documents are missing,
  proceed with clearly labeled assumptions and flag what's missing.
- Default to California unless told otherwise.
- Do not stall. If you can produce a useful analysis with what you
  have, do it, and flag the gaps.

## Project Preflight

Before producing ANY deliverables, check for and create the
project page per `claude.md` "Project Page as Source of Truth."

1. Search the Projects database (data source:
   `collection://df007c24-ffac-40d7-8e91-fb6763b6ecf6`) for an
   existing project matching the matter name or case number.

2. **If a project exists** (e.g., from a prior intake): Link
   the assessment deliverable to it. Do not create a duplicate.

3. **If no project exists:** Create one in the Projects database:
   - **Project name:** `[Matter] — Case Assessment ([Case No.])`
     (e.g., "Emmons — Case Assessment (B351005)")
   - **Category:** Case Project
   - **Case Stage:** Intake
   - **Icon:** ⚖️
   - **Status:** In progress
   - **Priority:** Set based on any known deadlines:
     - High if compliance deadline or NOA deadline ≤14 days
     - Medium if appellate deadline ≤30 days or active inquiry
     - Low if no external deadline (speculative evaluation)
   - **Target Date:** The earliest known deadline — compliance
     date, NOA deadline, or consultation callback date. If none
     is known yet, set to 14 days from today as a review target
     and note in Summary that it's a placeholder.
   - **Case Portal:** Link to the matter's Case Portal entry
     (create one if needed, per the Case Portal preflight)
   - **Team Portals:** Link to PC Intake & Case Management
     (`3250fc06-a06c-80c2-9d28-da7c0b81c6b8`)
   - **Summary:** One paragraph describing the intake evaluation

4. Store the project page URL for the in-chat handoff.

---

## Output Format

The output is a Word document (.docx) produced by cloning the KLG
Case Memo template and editing it — never by generating from scratch.

### Template Location

1. **Cowork:** Look for an existing KLG case memo `.docx` in the
   working folder (identifiable by the KLG logo header and
   Century Schoolbook typography). If found, clone it.
   If not found, prompt the user:
   "I don't see an existing KLG case memo in the working folder.
   Should I (a) use the project template, or (b) point me to a
   specific file?"

2. **Chat or fallback:** Use `/mnt/project/KLG_Case_Memo.docx`.

3. If neither is available, ask the user to upload the template.
   Do NOT fall through to from-scratch generation.

### .docx Generation Workflow

1. Read `/mnt/skills/public/docx/SKILL.md` — specifically the
   "Editing Existing Documents" section.
2. Copy the template to the working directory.
3. Unpack:
   ```
   python /mnt/skills/public/docx/scripts/office/unpack.py template.docx unpacked/
   ```
4. Examine `unpacked/word/document.xml` to understand the template's
   XML structure, named styles, and placeholder content.
5. Edit `unpacked/word/document.xml` using `str_replace`:
   - Replace placeholder text within `<w:t>` elements.
   - Preserve ALL `<w:pPr>` (paragraph properties) and `<w:rPr>`
     (run properties) blocks — these carry the KLG formatting.
   - Add new content sections by cloning existing paragraph
     structures and changing their text content.
   - Use smart quote entities: `&#x2018;` `&#x2019;` `&#x201C;`
     `&#x201D;`
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
9. Copy to `/mnt/user-data/outputs/` and present.

**CRITICAL:** Do not specify fonts, margins, or page sizes in the
generation script. The template carries all formatting. Do not use
docx-js to generate from scratch. Do not define explicit formatting
in code — if you find yourself writing `font:` or `size:` or
`spacing:` in a generation script, you are on the wrong path.

### Content Guide

The Document Structure below defines WHAT goes in each section.
The template defines HOW it is formatted. When editing the XML,
populate sections with the content specified below, but let the
template's styles control the appearance.

---

## Document Structure

### HEADER

**INITIAL CASE ASSESSMENT**
**Prepared by:** [AI-generated draft — requires attorney review]
**Date:** [date]
**Status:** DRAFT — AI ASSISTED

### 0. EXECUTIVE SUMMARY

1–2 paragraphs (cap ~150 words) identifying:
- Who we would represent on appeal
- The procedural posture
- The order challenged
- The strongest argument and whether it will likely win
- The complexity and estimated cost of the appeal
- The potential upside if the PC wins
- Whether we recommend taking or declining the case

**Case Vitals Table:**

| Field | Detail |
|-------|--------|
| Potential Client(s) | [names] |
| Trial Counsel | [names] |
| Full Case Name | [case name] |
| Trial Court | [court name] |
| Case Number | [number] |
| Trial Judge | [name] |
| Date of Challenged Order | [date] |
| Notice of Appeal | [date, or "None filed"] |
| Referral Source | [name, or "Direct inquiry"] |

**Immediate Risks if No Action Is Taken:**

After the Case Vitals table, include a short block (3–8 lines)
identifying every deadline or risk bearing down on the potential
client right now. This is a CYA section — it ensures the client
is on notice even if they do not retain KLG. Cover three categories:

1. **Compliance deadlines** — any court-ordered performance dates:
   injunction compliance, document production, payment due dates,
   anything the client must *do* by a specific date. State the date,
   what must be done, and the consequence of noncompliance (contempt,
   sanctions, waiver, etc.).
2. **Appellate deadlines** — NOA filing (60-day and 180-day clocks),
   writ petition windows, stay or bond deadlines already running.
   State each deadline, the triggering event, and the consequence
   of missing it.
3. **Other time-sensitive risks** — opposition briefing schedules
   already running, pending hearings, statute of limitations on
   related claims, or any other time-sensitive exposure identified
   in the record.

For each item, state: what it is, the date, how many calendar days
from the date of this memo, and what happens if missed.

Close with this standing disclaimer (adapt as needed):

> "KLG identifies these deadlines as part of its initial evaluation.
> KLG will not monitor, calendar, or act on any deadline unless
> formally retained."

If no immediate deadlines or risks are identified in the reviewed
documents, affirmatively state: "No immediate compliance or
appellate deadlines were identified in the reviewed documents.
This assessment is based on the materials provided; additional
documents may reveal deadlines not reflected here."

### 1. CASE BRIEF RECAP

~1 page (~250 words). Plain-English elevator pitch in 2–3 paragraphs
summarizing facts, claims, defenses, and trial outcome.

Requirements:
- Fully cited to the record using REF numbers (preferred) or
  document-name-plus-page (alternative). Every factual statement
  must have a citation.
- State the court (full name + county).
- Preview answers to "Should the PC have won?" and "Did the right
  party win?" Note uncertainty where it exists.

### 2. LEGAL ISSUES & TRIAL COURT DECISION

- Identify the issues the court decided.
- State the legal theories (claims, defenses, cross-claims).
- Summarize the court's dispositive reasoning.

### 3. STRENGTH OF CHALLENGE

For each principal issue, assess: strong / mixed / weak.
Note whether the issue is legal, discretionary, or factual.

### 4. STANDARD OF REVIEW

For each issue, assign the applicable standard: de novo, substantial
evidence, abuse of discretion, clear error, or harmless/prejudicial
error. Include a short authority citation for each standard assigned.

### 5. PRESERVATION

For each potential appellate issue:
- Was it raised in the trial court?
- Was a ruling obtained?
- Was it timely?
- If not preserved: is there an applicable exception? (pure question
  of law, jurisdictional, misinstruction, futility,
  constitutional/structural)
- Flag unpreserved issues with a red indicator and explain the risk.

### 6. OTHER POTENTIAL CHALLENGES

Assess whether error can be demonstrated on: evidentiary rulings,
pretrial rulings (demurrers, MSJ, motions in limine, etc.), jury
instructions and verdict forms, post-trial motions (JNOV, new trial),
and doctrine of implied findings (Statement of Decision / CCP § 632).

### 7. PREJUDICIAL ERROR

Apply the applicable prejudice test for each identified error.
Tie the prejudice analysis to the verdict and/or damages. An error
without prejudice is not reversible — state this explicitly where
applicable.

### 8. TIMELINESS & RELIEF

- Confirm whether the appeal or writ appears timely.
- Identify any tolling issues.
- State the relief available if we prevail.

### 9. COST HORIZON

- Flag whether this looks like a normal, medium, or high-cost appeal.
- Assess the value of success to the client and whether that value
  offsets the likely costs.
- Reference the cost anchors in the case assessment standards for
  ranges.
- If enough information is available, provide a preliminary cost
  estimate using the Work Breakdown format: stages + estimated
  hours + $ ranges, assumptions and multipliers, total range =
  base + multipliers + 10–20% buffer.
- **Rates** — use the current KLG rate sheet (June 2026):
  - Timothy Kowal (standard): $750/hour
  - Timothy Kowal (consulting): $1,050/hour
  - Senior Attorneys: $595–$650/hour
  - Other Attorneys: $400–$575/hour
  - Paralegals: $175/hour
  - Initial Evaluations: $1,750–$5,500 flat
  - Appellate Appendices (automated service): $1,300 flat
- **DZ matters:** Do NOT quote rates in this section if the referral
  source is David Zarmi. The DZ overlay skill handles tier
  classification and rate quoting in a separate pass after this
  assessment completes. Simply note: "DZ matter — engagement
  structure and rates handled by overlay."

### 10. CITATIONS

All citations throughout the document must follow these rules:
- Preferred: REF control numbers stamped at bottom of pages.
  Format: (REF[MatterNumber]-[PageNumber].)
  Example: (REF251021-00042.)
- Alternative: Full document name (without extension) plus PDF page.
  Example: (2026-02-03 Tentative_Ruling at 2.)
- Case citations: italicize case names only. Follow California Style
  Manual for CA authorities, Bluebook for federal.
- No naked cites. Include explanatory parentheticals.

### 11. EXECUTIVE ASSESSMENT

#### Do we have enough information to decide?
State whether the available information is sufficient for an intake
decision. If not, identify what's missing and how it would change
the analysis.

#### Traffic Light Coding

**Should the PC have won? (Merits)** — Green / Yellow / Red
Summarize rulings, strongest arguments, hurdles (SoR, preservation,
prejudice). Assign traffic light with explanation.

**Is the PC in the right? (Equities)** — Green / Yellow / Red
Assess the equities. Assign traffic light with explanation.

**Can the PC pay?** — Green / Yellow / Red
- Hourly/funded flat fee: Green
- Payment plan: Yellow
- Contingency: Red (unless strong public-interest case)
- Stable counsel history: Green
- Unrepresented or multiple past attorneys: Red

**Practice alignment?**
- Green = Core: business litigation, anti-SLAPP, civil procedure
- Yellow = Secondary: trust, employment
- Red = Lower: family law
- Discretionary = Public-interest

#### Tentative Case Classification

**Overall:** Promising / Borderline / Decline
**One-sentence reason:** [state it]
**Cost horizon:** Normal / Medium / High

#### Bottom Line

**Should we take this case?** Yes / No
**What $ cap or estimate should we provide?** [amount or range]
**Special pros and cons to keep in mind:** [list]

### 12. ENGAGEMENT STRUCTURE FLAGS

Surface any engagement-structure issues that the engagement letter
will need to address. This section applies the universal principles
documented in `references/klg-case-assessment-standards.md` (see
"Engagement Structure Principles") and gives attorney guidance
before the engagement letter is drafted.

For each principle below, state explicitly whether it applies and
how:

**Cap proposal.** If the PC or referring attorney requests a cap,
flag whether the proposed cap is at the upper end of plausible
work (acceptable) or below KLG's reasonable estimate (NOT
acceptable). State the recommended cap or estimate range. Apply
the rule: caps protect the client from overruns; they are not a
floor for someone else's margin.

**Flat-fee proposal.** If a flat fee is contemplated, flag whether
prepayment is in place. State the rule: flat fees only when paid
in advance. Payment-on-completion flat fees defeat the purpose
and should be declined or converted to hourly with cap.

**Rate-and-cap interaction.** If a relationship rate below the
rate sheet is proposed AND a cap is also proposed, flag this as
a "low rate + low cap" stacking risk. State the rule: if KLG
accepts a low rate, the cap must be high or omitted. If KLG
accepts a low cap, the rate must be standard. Never both.

**Scope-and-revisions.** Identify the deliverable scope and note
that the engagement letter should include the standard
scope-and-revisions language: capped or flat-fee engagements
cover initial drafting plus one substantive revision round.
Additional client-driven rounds bill hourly without cap.

**Out-of-hours communications.** Note that the engagement letter
should include the standard out-of-hours communications language:
KLG responds during business hours; genuine emergencies receive
same-day response; routine after-hours communications are
addressed the next business day.

For DZ matters, this section produces only a one-line note: "DZ
matter — Engagement Structure Flags handled by DZ overlay skill
in a separate pass." The overlay applies these principles with
DZ-specific tier classification and routing terms.

### 13. OPEN ITEMS & NEXT STEPS

- Documents or information still needed
- Whether the file is ready for attorney decision or needs more info
- Immediate deadlines to watch
- Research priorities if we take the case
- **If DZ matter:** flag that `klg-dz-overlay` should run next to
  produce the DZ engagement summary.

---

## Supplemental Assessment Mode

When the user provides new information after an initial assessment
has been completed in the same conversation, produce a Supplemental
Assessment with this structure:

### 1. UPDATED EXECUTIVE SUMMARY
Write a fresh executive summary using ALL information (old + new).
Do not describe the iteration history. Just the current best
bottom line.

### 2. WHAT CHANGED SINCE THE PREVIOUS ASSESSMENT
Briefly state:
a) What the initial bottom line was (1–3 bullets)
b) What new information/documents were provided (bulleted list)
c) Whether and how the new materials changed the analysis
   (if no change, say so explicitly)

### 3. FULL UPDATED ASSESSMENT
Produce the rest of the assessment as if starting fresh, but
incorporating the new information. Maintain the same structure
and formatting as the initial assessment.

---

## Execution Rules

1. Read the entire case file before writing anything. Start with
   the judgment and work backward through motions and orders.
   When reading any order, judgment, or injunction, identify every
   date or time period that imposes a deadline or obligation on any
   party. Flag each one for the Immediate Risks section regardless
   of whether it appears relevant to the appellate analysis.
   Compliance deadlines in the underlying orders are as important
   as appellate deadlines — the client needs to know what is
   bearing down on them now, not just what the appeal timeline
   looks like.
2. Every factual assertion must cite to the record. No exceptions.
3. Never rate an issue without citing specific record pages and
   explaining the reasoning.
4. When in doubt, rate conservatively (Yellow, not Green).
5. Flag every follow-up item — missing Bates/REF number, uncertain
   citation, or anything else needing human review — with the
   single uniform tag `[VERIFY: short description]` per claude.md's
   placeholder standard. Collect them in a summary list at the end
   under Open Items.
6. If the record is incomplete, say so explicitly and identify
   what's missing and how it would affect the analysis.
7. Do not invent or assume facts not in the record.
8. Do not fabricate case citations. If you believe a legal
   principle applies but cannot identify the specific authority,
   write `[VERIFY: research needed — description of principle]`
   per claude.md's uniform placeholder standard.
9. Target length: 2,000–4,000 words depending on complexity.
   The executive summary should be capped at ~150 words.
10. Apply the KLG Style Guide throughout: write like a normal
    person, no legalese, active voice, punchy sentence openers,
    no block quotes unless truly necessary.
11. This is internal work product. Do not include legal-advice
    disclaimers. Do include the AI transparency notice that this
    is an AI-assisted draft requiring attorney review.
12. At the end of every assessment, state clearly:
    "Action item:" [single clear next step]
    "Next stage:" [what follows after completion]
13. **If this is a DZ matter (referral source = David Zarmi):**
    after delivering the assessment, prompt:
    "This is a DZ-sourced matter. The next step is to run
    `klg-dz-overlay` to produce the DZ engagement summary
    (tier classification, rate selection, attribution decision,
    and routing terms). Should I proceed with the overlay now?"
14. After delivering the assessment, follow the workflow patterns:
    - Pattern 1 (Iterative Case Memo): This is typically the first
      deliverable for a matter, so it becomes the seed of the
      evolving case memo. If a prior case memo exists, ask whether
      to add this as a new section or produce standalone.
    - Pattern 2 (Client Memo): Ask whether a client-facing version
      is needed. Client version excludes traffic lights, cost
      estimates, internal strategy, and AI-assisted drafting notes.
15. After delivering the assessment AND the workflow pattern
    questions, provide the Cowork-to-Chat offboard instructions
    (see "Cowork-to-Chat Offboard Point" above).
16. **Terminal project status update:** After the case assessment
    memo is delivered and all workflow pattern questions are
    answered, update the project page:
    - If this was a standalone intake evaluation and the user
      decides to decline: set Status → Done.
    - If the user decides to take the case: set Case Stage →
      Evaluation (or the appropriate next stage). Leave Status
      as "In progress" — the project continues.
    - If the user hasn't decided yet: leave Status as "In
      progress" but update the Target Date to the decision
      deadline if one was discussed.
