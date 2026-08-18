---
name: klg-response-plan
description: "Dual-mode strategic memo skill. RESPONDENT MODE: Analyze an opponent's appellate brief with argument-by-argument counter-analysis, reframing strategies, and briefing recommendations. APPELLANT MODE: Analyze a trial court ruling/judgment to identify grounds for reversal, assess preservation and prejudice, and plan the opening brief. Triggers: 'create a response plan', 'response plan memo', 'analyze opposing brief', 'plan our response', 'respond to the RB/ARB', 'counter their arguments', 'opening brief strategy', 'plan the opening brief', 'plan our attack', 'strategy memo for the appeal', 'grounds for reversal', 'plan the AOB', 'identify the errors', 'what should we appeal'. Also triggers on uploads of opposing briefs or trial court rulings with requests for strategic analysis. Delivers to Notion for iterative refinement; .docx as terminal step. NOT for case assessments, research prompts, or deep research memos."
---

# KLG Strategy Memo — Dual Mode

## Purpose

This skill operates in two modes:

**Respondent Mode** — Analyze an opponent's appellate brief and
generate a strategic Response Plan Memo that identifies their
strongest arguments, proposes counter-arguments with authority,
and recommends framing strategies.

**Appellant Mode** — Analyze a trial court ruling, judgment,
statement of decision, or order and generate an Opening Brief
Strategy Memo that identifies grounds for reversal, assesses
preservation and prejudice, proposes argument structure, and
recommends the brief's strategic frame.

Both modes produce a memo read by clients, trial counsel, and
the internal legal team. Both must be precise, strategically
useful, and ready to inform briefing decisions and client
communications.

## Required Context

Before writing anything, read these reference files in the skill's
`references/` directory for firm standards:

1. `references/claude-md-standards.md` — Citation formats, quality
   controls, AI transparency requirements
2. `references/klg-style-guide.md` — Writing voice and conventions
3. `references/klg-response-plan-standards.md` — Analytical
   framework, argument labeling, steel-manning requirements
4. `references/workflow-patterns.md` — Iterative case memo and
   client memo patterns

If any of these files are missing from the skill folder, prompt the
user to provide them. The skill cannot produce fully compliant
output without these standards, but should proceed with best-effort
analysis using the embedded standards below.

---

## Mode Detection

At launch, determine which mode to run. Claude should infer the
mode from context when possible:

**Infer Respondent Mode when:**
- The user uploads or references an opponent's appellate brief
- The user says "respond to," "counter," "their brief," "the
  RB," "the ARB," "the AOB" (when KLG is respondent)
- The context makes clear KLG is responding to an existing
  appellate brief

**Infer Appellant Mode when:**
- The user uploads or references a trial court ruling, judgment,
  statement of decision, or order
- The user says "opening brief," "plan the appeal," "grounds for
  reversal," "plan our attack," "the AOB" (when KLG is appellant)
- The context makes clear KLG is the appellant planning the
  opening brief

**If ambiguous**, ask:

```
Are we planning a response to an opposing appellate brief, or
are we planning our opening brief based on the trial court's
ruling?

— Response to opposing brief (Respondent Mode)
— Opening brief strategy (Appellant Mode)
```

Use `ask_user_input` for this question.

---

## Required Inputs

### Respondent Mode

- Opponent's brief (PDF)
- Our brief, if the opponent is responding to one (AOB, RB, or ARB)
- Any additional materials if available: record excerpts, prior
  filings, orders, existing case memo

### Appellant Mode

**Required:**
- The trial court's ruling, order, judgment, statement of
  decision, or tentative ruling being challenged (PDF or .docx)

**Strongly recommended:**
- Key trial court briefing (our motion/opposition/reply, their
  motion/opposition/reply) — these are where preservation lives
- The judgment or order after which the appeal was taken (if
  different from the ruling being challenged)
- Existing case assessment memo (if one exists)

**Optional but valuable:**
- Key evidence or exhibits that bear on the ruling
- Reporter's transcript excerpts (especially oral argument on
  the motion, hearings on evidentiary objections, trial testimony
  relevant to the challenged ruling)
- Prior appellate filings (e.g., if there was a writ petition)
- Statement of appealability considerations (if appealability is
  in question)

### Running in Chat vs. Cowork

Before starting, ask the user which mode they want to run in:

**Respondent Mode prompt:**

```
Before we start the response plan, how would you like
to run this?

COWORK (recommended):
  ✓ I can cross-check the opponent's record citations
    against the actual record and spot mischaracterizations.
    I can also pull in the case assessment if one exists.
  ✗ Ties up Cowork for approximately 30–60 minutes.

CHAT:
  ✓ Keeps Cowork free for other work.
  ✗ You'll need to upload: (1) the opposing brief, and
    (2) the case assessment memo (if one exists). I won't
    be able to verify record citations against the
    original documents.

Which do you prefer?
```

**Appellant Mode prompt:**

```
Before we start the opening brief strategy memo, how
would you like to run this?

COWORK (recommended for appellant mode):
  ✓ I can read the full trial court record — the ruling,
    the briefing that preceded it, key evidence, and
    transcripts. This produces the most thorough error
    analysis and preservation assessment.
  ✗ Ties up Cowork for approximately 30–60 minutes.

CHAT:
  ✓ Keeps Cowork free for other work.
  ✗ You'll need to upload: (1) the ruling/order/judgment
    being challenged, (2) the key trial court briefing
    (our papers and theirs), and (3) any case assessment
    memo. Without the full record, my preservation
    analysis may have gaps.

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

**Respondent Mode:** After delivering the response plan, tell
the user:

"The response plan is complete. For follow-on work, open a
Chat tab and upload the response plan memo (and the case
assessment if available). Claude can generate research
prompts, client memos, or begin brief drafting from there."

Then provide a copy-paste Chat resume prompt:

```
I have the response plan for [Case Name] ([Case No.]).
[Describe the follow-on task, e.g., "Please generate deep
research prompts based on this response plan."]
```

**Appellant Mode:** After delivering the opening brief strategy
memo, tell the user:

"The strategy memo is complete. For follow-on work, open a
Chat tab and upload the strategy memo (and the case assessment
if available). Claude can generate deep research prompts,
draft argument outlines, or begin brief drafting from there."

Then provide a copy-paste Chat resume prompt:

```
I have the opening brief strategy memo for [Case Name]
([Case No.]). [Describe the follow-on task, e.g., "Please
generate deep research prompts for the issues we're
appealing."]
```

## Interaction Rules

### Both Modes

- Read ALL uploaded documents completely before writing anything.
- If additional materials (record excerpts, prior filings, orders)
  are uploaded, incorporate them and update strategy accordingly.
- If the case is complex, offer to work interactively
  section-by-section while maintaining coherence.
- If key inputs are missing (jurisdiction, posture, deadlines),
  do not stall. Proceed with best-effort analysis and clearly state
  assumptions and what additional materials would improve accuracy.
- Default to California unless told otherwise.

### Respondent Mode

- Before beginning, confirm what briefs are available. Ask:
  "(1) Have you uploaded the opponent's brief? (2) Is the opponent's
  brief responding to our brief, and if so, have you uploaded it?
  Once we have the opponent's brief and our brief (if applicable),
  I'll get started."

### Appellant Mode

- Before beginning, confirm what materials are available. Ask:
  "(1) Have you uploaded the trial court ruling or order being
  challenged? (2) Do you have the trial court briefing that led to
  the ruling (our papers and theirs)? (3) Is there an existing case
  assessment memo? Upload whatever you have and I'll get started —
  I'll flag where gaps in the record limit my analysis."

## Defining "Major Issues"

### Respondent Mode

A "major issue" means any argument presented under a heading or
subheading in either party's brief that could independently support
affirmance or reversal, or any discrete contention the opponent
develops with authority or record citations. Avoid over-fragmentation;
group minor variations under the closest major issue.

### Appellant Mode

A "major issue" means any ruling, finding, or legal determination
by the trial court that could independently support reversal if
error is established, or any discrete ground for challenging the
judgment. This includes: legal errors in applying the wrong
standard, factual findings unsupported by substantial evidence,
procedural errors (evidentiary rulings, discovery orders, due
process violations), abuse of discretion findings, and errors in
the remedy or relief granted.

Avoid over-fragmentation — group related sub-rulings under the
primary error they support. But do not collapse genuinely
independent grounds for reversal into a single issue just because
they arise from the same proceeding.

## Project Preflight

Before producing ANY deliverables, check for and create the
project page per `claude.md` "Project Page as Source of Truth."

1. Search the Projects database (data source:
   `collection://df007c24-ffac-40d7-8e91-fb6763b6ecf6`) for an
   existing project matching the matter name, case number, or
   "Response Plan" / "Opening Brief" / "Strategy Memo."

2. **If a project exists** for this matter's briefing lifecycle
   (e.g., a Case Project for the RB or AOB): Link the strategy
   memo deliverable to it. Do not create a duplicate.

3. **If no project exists:** Create one in the Projects database:
   - **Project name (Respondent Mode):**
     `[Matter] — Response Plan ([Case No.])`
   - **Project name (Appellant Mode):**
     `[Matter] — Opening Brief Strategy ([Case No.])`
   - **Category:** Case Support
   - **Support Type:** Memos
   - **Icon:** 📄
   - **Status:** In progress
   - **Priority:** Set based on our brief's filing deadline:
     - High if deadline ≤14 days or active emergency
     - Medium if deadline ≤30 days
     - Low if no external deadline
   - **Target Date:** Our brief filing deadline.
     If unknown, ask the user.
   - **Case Portal:** Link to the matter's Case Portal entry
   - **Team Portals:** Link to PC Intake & Case Management
     (`3250fc06-a06c-80c2-9d28-da7c0b81c6b8`)
   - **Summary:** One paragraph describing the strategy memo scope

4. Store the project page URL for the in-chat handoff.

---

## Delivery — Notion First, .docx Last

### Principle

This skill produces iterative work product — the strategy memo
will be refined, discussed, and revised before it informs brief
drafting. The drafting canvas is Notion. The .docx is a terminal
finishing step, produced only when the text is finalized.

### Default Delivery Flow

1. **Write the full memo to a Notion page** in the Research
   database, linked to the Case Portal entry and the project page.

   Notion page properties:
   - **Title (Respondent Mode):**
     `[Matter] — Response Plan Memo`
   - **Title (Appellant Mode):**
     `[Matter] — Opening Brief Strategy Memo`
   - **Case Portal:** linked to the matter
   - **Projects:** linked to the active project page
   - **Tags:** `["Strategy Memo"]`
   - **Date:** today
   - **Note:** 1–2 sentence summary of the memo's scope and
     key recommendation

2. **Present the memo in chat** alongside the Notion link so the
   user can read it immediately and iterate.

3. **After the user is satisfied with the substance**, offer
   .docx generation:

   ```
   The strategy memo is on Notion and ready for your review:
   [Notion URL]

   When you're satisfied with the substance, say "generate the
   docx" and I'll produce the formatted Word document on the
   KLG case memo template.
   ```

4. Only when the user requests the .docx, follow the .docx
   Generation Workflow below.

### When to Skip Notion and Go Straight to .docx

- The user explicitly asks for a Word document up front
- The user says "final version" or "file-ready" — signaling
  no further iteration is expected
- The memo is being appended to an existing .docx case memo
  (Pattern 1 — "add to existing case memo")

Even in these cases, still create the Notion page as a
permanent record — but produce the .docx simultaneously
rather than waiting for a second request.

### Workflow Patterns (Post-Delivery)

After the memo is delivered (to Notion and/or .docx), follow
the workflow patterns in `references/workflow-patterns.md`:

- **Pattern 1 (Iterative Case Memo):** Ask whether to add the
  strategy memo to the existing case memo or keep standalone.
- **Pattern 2 (Client Memo):** Ask whether a client-facing
  version is needed. Client version excludes internal strategy
  labels ("damage control," "concede"), AI drafting notes, and
  candid weakness assessments.

---

## Document Structure — Respondent Mode

### HEADER

**RESPONSE PLAN MEMO**

**Case:** [case name and number]
**Brief Analyzed:** [Appellant's/Appellee's/Reply Brief]
**Filed:** [date of opponent's brief]
**Our Response Deadline:** [date, or "TBD — VERIFY"]
**Prepared by:** [AI-generated draft — requires attorney review]
**Date:** [date]
**Status:** DRAFT — AI ASSISTED

---

### EXECUTIVE SUMMARY

3–5 sentences providing:
- Overview of opponent's strategy and central theme
- Their strongest argument
- Our recommended response approach
- Overall threat assessment

---

### ARGUMENT-BY-ARGUMENT ANALYSIS

For each major issue identified in the briefs, use this four-part
format:

#### Issue [N]: [Descriptive Title]

**[N].a. Our Argument**
Concise statement of our position on this issue. Summary of our
main points. Cite to our brief: (AOB at [page]), (RB at [page]),
or (ARB at [page]).

If we did not brief this issue (e.g., the opponent raises it for
the first time), state: "Not addressed in our brief. This is a
new argument raised in [their brief type]."

**[N].b. Their Response**
Steel-manned summary of how the opponent responds. Present their
argument in its strongest, fairest framing. Include direct quotes:
short quotes in-text, longer quotes block-indented. Cite to their
brief: (RB at [page]) or (ARB at [page]).

Always present their argument in its strongest form. Do not
strawman or minimize. The value of this memo depends on honest
assessment of threat level.

**[N].c. Standard of Review**
State the correct standard of review for this issue with authority.
If unclear, note the likely standard(s) and the strategic
implications of each. Cite the governing authority.

**[N].d. Our Planned Response**

Assess the strength of their argument first:

If their argument is **weak**: give a succinct rebuttal identifying
the specific defect (waiver, preservation failure, logical flaw,
misstatement of record, wrong standard).

If their argument is **strong**: provide a deeper rebuttal:
- Identify our 2–3 strongest counter-authorities and record evidence
- Provide full case citations with pincites (California Style Manual
  for CA, Bluebook for federal)
- Quote key language from our best authorities
- Explain how each authority supports our position
- Cite back to our brief where relevant (AOB/RB/ARB)
- Identify the pivot: how do we recharacterize or reframe this
  issue to put our case in the best light?

Label each argument honestly:
- "Winning argument" — we can prevail on this issue
- "Damage control" — we likely lose but can minimize the impact
- "Concede and minimize" — not worth fighting; acknowledge and
  move on

Continue this pattern for all major issues:
[N+1].a, [N+1].b, [N+1].c, [N+1].d, etc.

---

### STRUCTURE AND THEME OF OUR RESPONSE

After addressing all individual arguments, provide high-level
strategic guidance:

**Recommended approach:** Should we respond point-by-point or
reframe around stronger themes? What is the organizing principle
for our brief?

**Our narrative:** What is the story we want the court to see?
What is the one-sentence version of our case?

**Recommended argument order:** Which arguments to lead with
(strongest first, but consider logical flow).

**Statement of Facts strategy:** What to lead with. What facts
favor us most, with record citations.

**What NOT to engage with:** Arguments the opponent raised that
we should decline to address, and why (engaging would elevate a
weak point, or the issue is waived, or a non-response is more
powerful).

**Page/word budget allocation:** Rough recommendation for how to
distribute our page or word limit across the arguments based on
their relative importance and threat level.

---

### RED FLAGS AND OPPORTUNITIES

**Concessions opponent made that we should exploit:**
Identify any points where the opponent conceded ground, limited
their argument, or made admissions that help us. Cite to their
brief.

**Mischaracterizations of the record we must correct:**
Cross-reference their record citations against the actual record.
Flag any that are inaccurate, misleading, or taken out of context.
Provide the correct record cite and what it actually shows.

**Cases they cite that actually help us:**
Identify any authorities in their brief that, on closer reading,
support our position or can be distinguished favorably.

**Arguments they conspicuously avoided:**
Note any arguments they did not make that one might expect. Explain
why the omission matters (waiver, weakness, strategic choice).

---

### ACTION ITEMS

**Action item:** [single clear next step]
**Next stage:** [what follows after completion]

---

### PAYMENT SCHEDULE (when a fee estimate is available)

Only include this section when the memo identifies both a briefing
deadline and a fee estimate for this phase. If an estimate hasn't
been set yet, skip this section rather than guessing at one.

Don't auto-generate the schedule silently — propose it and ask the
attorney to confirm before it goes to accounts, since it commits
the client to specific payment dates:

```
This phase's estimate is [$X] against the [deadline]. Proposed
advance-payment schedule, per the retainer's phase-based
payment clause:

- First payment: [$ amount] at [date — 30 days from today]
- Second payment: [$ amount] at [date — 60 days from today]
- Final payment: [$ amount] at [date — 30 days before the
  deadline, or before drafting begins, whichever is earlier]

Checkpoints are tied to the initial/soft deadline, not the hard
deadline. Confirm this schedule (or adjust it) before I hand it to
accounts.
```

Once confirmed, hand off in a format legible for the accounts team
(Josué) to track: phase, estimate, and the three checkpoint dates
and amounts — as a Slack message or a line in the matter's Notion
project page, whichever the accounts handoff pattern already uses.

---

## Document Structure — Appellant Mode

### HEADER

**OPENING BRIEF STRATEGY MEMO**

**Case:** [case name and number]
**Ruling Challenged:** [description — e.g., "Order granting
summary judgment," "Statement of decision after bench trial,"
"Order sustaining demurrer without leave to amend"]
**Ruling Date:** [date of the ruling/judgment]
**Notice of Appeal Filed:** [date, or "TBD — VERIFY"]
**Opening Brief Deadline:** [date, or "TBD — VERIFY"]
**Prepared by:** [AI-generated draft — requires attorney review]
**Date:** [date]
**Status:** DRAFT — AI ASSISTED

---

### EXECUTIVE SUMMARY

3–5 sentences providing:
- What the trial court did and why we believe it was wrong
- The strongest ground(s) for reversal
- The most significant litigation risk (preservation, SoR,
  harmless error)
- Recommended strategic approach for the opening brief
- Overall assessment: strong appeal / viable appeal / uphill
  appeal (with brief explanation)

---

### APPEALABILITY AND THRESHOLD ISSUES

Address these before the merits analysis. If any threshold
issue is fatal, the merits analysis is academic — flag it
prominently.

**Appealability:** Is the ruling/judgment appealable? From
what? Final judgment, collateral order doctrine, death knell
doctrine, order after judgment? Cite the statutory basis
(Code Civ. Proc., § 904.1, subd. (a)(1), etc.).

**Timeliness:** Was the notice of appeal timely filed? Note
the triggering document (notice of entry, file-stamped order,
clerk's mailing), the deadline, and the actual filing date.
Flag any California Rules of Court, rule 8.104 / 8.108 issues.

**Standing:** Does the appellant have standing? Was the
appellant aggrieved by the ruling? Any issues with real party
in interest, capacity, or substitution?

**Mootness:** Is there any risk the appeal has become moot?
Voluntary act doctrine, subsequent events, change in
circumstances?

If all threshold issues are clear, state so briefly and move
to the merits. Do not belabor clean threshold issues.

---

### ISSUE-BY-ISSUE ERROR ANALYSIS

For each major issue (ground for reversal), use this five-part
format:

#### Issue [N]: [Descriptive Title]

**[N].a. The Trial Court's Ruling**
What the trial court did or found on this issue. Quote the key
language from the ruling, statement of decision, or order. Cite
to the ruling document: ([Ruling document name] at [page].) or
(REF number.) If the trial court gave reasoning, summarize it
fairly — we need to know what we're attacking.

If the trial court did not address the issue (e.g., it was
raised but not ruled on), state that explicitly — this may
affect both preservation and the standard of review.

**[N].b. Preservation**
Was this issue preserved for appeal? Specifically:
- Was the argument raised in our trial court briefing? Cite to
  the specific document and page.
- Was a timely objection made (if applicable)? Cite to the
  transcript or written objection.
- Did the trial court rule on it? A ruling is required for
  most preserved issues — an argument raised but never ruled on
  may be deemed forfeited.
- Are there any exceptions to forfeiture that apply? (Pure
  questions of law, jurisdictional issues, public interest,
  futility.)

Rate preservation:
- 🟢 **Clean** — fully briefed, objected to, ruled on
- 🟡 **Arguable** — raised but not squarely ruled on, or
  preserved under an exception theory
- 🔴 **At risk** — not raised below, or raised too late, or
  raised in the wrong form

If preservation is 🔴, assess whether this issue is still worth
raising (e.g., pure question of law, jurisdictional defect) or
should be dropped.

**[N].c. Standard of Review**
State the correct standard of review with authority. Explain its
practical significance — does this standard help us or hurt us?

For issues where the standard is contested or could be
characterized multiple ways (e.g., mixed question of law and
fact), identify the competing standards and recommend which one
to argue for, with authority supporting our preferred
characterization.

Note any independent/de novo review triggers: constitutional
questions, statutory interpretation, undisputed facts.

**[N].d. The Case for Reversal**
Our affirmative argument for why the trial court erred:
- State the legal error precisely — what rule did the court
  misapply, what finding was unsupported, what procedure was
  violated
- Identify our 2–3 strongest authorities with full citations
  and pincites (California Style Manual for CA, Bluebook for
  federal)
- Quote key language from controlling or persuasive authority
- Cite to the record evidence that supports reversal
- Identify the pivot: what is the most compelling framing of
  this error? Lead with the frame that makes reversal feel
  inevitable, not just technically correct.
- If there are multiple theories supporting reversal on this
  issue, identify the primary theory and note alternatives.

**[N].e. Prejudice and Anticipated Defenses**
Prejudice analysis:
- How did this error affect the outcome? Would the result have
  been different absent the error?
- What is the applicable prejudice standard? (*People v. Watson*
  (1956) 46 Cal.2d 818 — reasonable probability; *Chapman v.
  California* (1967) 386 U.S. 18 — beyond a reasonable doubt
  for constitutional error; structural error requiring no
  prejudice showing.)
- What evidence in the record demonstrates prejudice?

Anticipated defenses:
- What will the respondent argue in response? (Harmless error,
  alternative grounds for affirmance, invited error, waiver,
  substantial evidence supports the finding, etc.)
- How do we preemptively address these defenses in our opening
  brief?

**Strength Assessment:**
Label each issue honestly:
- 🟢 "Strong ground for reversal" — clear error, well-preserved,
  favorable SoR, demonstrable prejudice, strong authority
- 🟡 "Viable but contested" — arguable error, some preservation
  risk, mixed authority, prejudice requires development
- 🔴 "Weak / include only if strategic" — preservation problems,
  deferential SoR, thin authority, harmless error risk

State confidence level: High / Medium / Low.

Continue this pattern for all major issues:
[N+1].a, [N+1].b, [N+1].c, [N+1].d, [N+1].e, etc.

---

### STRUCTURE AND THEME OF OUR OPENING BRIEF

After addressing all individual issues, provide high-level
strategic guidance:

**Recommended approach:** Should we lead with the strongest
single issue or build a cumulative-error narrative? Is there a
unifying theme that ties multiple errors together, or are they
independent grounds?

**Our narrative:** What is the story we want the court to see?
What is the one-sentence version of this appeal? The narrative
should make the court want to reverse before it reaches the
legal analysis.

**Recommended argument order:** Which issues to lead with.
Consider: (1) strongest first, but (2) logical flow matters —
sometimes a threshold issue (e.g., wrong legal standard) should
come first because it reframes everything that follows.

**Statement of Facts strategy:** The Statement of Facts is the
most important section of the opening brief. What facts lead?
What record evidence makes the trial court's ruling feel wrong
before the reader reaches the argument section? What facts does
the respondent want to lead with, and how do we neutralize them?

**Issues to drop:** Any issues from the error analysis that
should NOT be included in the brief. Weak arguments dilute
strong ones. Identify any issues rated 🔴 that should be
dropped, and explain why. (Rule of thumb: if the issue requires
more pages to explain why it's preserved than to argue the
merits, consider dropping it.)

**Page/word budget allocation:** Rough recommendation for how to
distribute the page or word limit across the arguments based on
their strength, complexity, and strategic importance.

**Cumulative prejudice:** If multiple errors are identified,
assess whether a cumulative prejudice argument is available.
Even if no single error independently requires reversal, the
cumulative effect of multiple errors may deprive the appellant
of a fair proceeding.

---

### RED FLAGS AND OPPORTUNITIES

#### Appellant Mode

**Favorable findings buried in the ruling:**
Identify any findings, statements, or reasoning in the trial
court's ruling that actually support our position or undermine
the court's own conclusion. Quote them with cites.

**Judicial statements that undermine the ruling:**
Did the trial court express doubt, acknowledge competing
considerations, or make statements inconsistent with its
ultimate ruling? These are gold for the opening brief.

**Respondent's concessions at trial:**
Identify any concessions, admissions, or stipulations made by
the opposing party in the trial court proceedings that limit
their ability to defend the ruling on appeal.

**Record evidence the trial court ignored or misweighed:**
Key evidence that was before the trial court but not addressed
in the ruling, or evidence the trial court acknowledged but
gave insufficient weight. Cite to both the evidence and the
ruling.

**Structural advantages:**
Note any favorable procedural posture: de novo review issues,
constitutional dimensions that elevate scrutiny, recent
authority shifts that favor our position, pending cases that
could affect the outcome.

**Alternative grounds for affirmance risk:**
Can the respondent defend the judgment on grounds the trial
court did not rely on? (*D'Amico v. Board of Medical Examiners*
(1974) 11 Cal.3d 1, 19.) Identify the most likely alternative
grounds and assess whether we can preempt them.

#### Respondent Mode

**Concessions opponent made that we should exploit:**
Identify any points where the opponent conceded ground, limited
their argument, or made admissions that help us. Cite to their
brief.

**Mischaracterizations of the record we must correct:**
Cross-reference their record citations against the actual record.
Flag any that are inaccurate, misleading, or taken out of context.
Provide the correct record cite and what it actually shows.

**Cases they cite that actually help us:**
Identify any authorities in their brief that, on closer reading,
support our position or can be distinguished favorably.

**Arguments they conspicuously avoided:**
Note any arguments they did not make that one might expect. Explain
why the omission matters (waiver, weakness, strategic choice).

---

### ACTION ITEMS

**Action item:** [single clear next step]
**Next stage:** [what follows after completion]

---

### PAYMENT SCHEDULE (when a fee estimate is available)

Only include this section when the memo identifies both a briefing
deadline and a fee estimate for this phase. If an estimate hasn't
been set yet, skip this section rather than guessing at one.

Don't auto-generate the schedule silently — propose it and ask the
attorney to confirm before it goes to accounts, since it commits
the client to specific payment dates:

```
This phase's estimate is [$X] against the [deadline]. Proposed
advance-payment schedule, per the retainer's phase-based
payment clause:

- First payment: [$ amount] at [date — 30 days from today]
- Second payment: [$ amount] at [date — 60 days from today]
- Final payment: [$ amount] at [date — 30 days before the
  deadline, or before drafting begins, whichever is earlier]

Checkpoints are tied to the initial/soft deadline, not the hard
deadline. Confirm this schedule (or adjust it) before I hand it to
accounts.
```

Once confirmed, hand off in a format legible for the accounts team
(Josué) to track: phase, estimate, and the three checkpoint dates
and amounts — as a Slack message or a line in the matter's Notion
project page, whichever the accounts handoff pattern already uses.

---

## Execution Rules

### Both Modes

1. Read all uploaded documents completely before writing anything.
2. For case citations: provide full citations with pincites. Quote
   accurately. Flag uncertainty with [VERIFY]. Do not fabricate
   authority. If you believe a legal principle applies but cannot
   identify the specific authority, write [RESEARCH NEEDED] and
   describe the principle.
3. For record citations: use the record accurately. When the
   appellate record is designated, cite using the standard formats:
   Clerk's Transcript (1-CT-1.), Appellant's Appendix (1-AA-1.),
   Reporter's Transcript (1-RT-1.) — where the first number is
   the volume and the second is the pincite page, no spaces, period
   inside the closing parenthesis. If working from pre-record files,
   use REF numbers or document-name format per claude-md-standards.
   If a record citation is needed but not available, insert
   [Record cite needed].
4. Use narrative prose by default. Use bullets only for listing
   authorities, evidence, or factors.
5. Tone: clear, succinct, precise, brief-ready. Confident but not
   verbose. No rhetorical flourishes.
6. This is internal work product. Do not include legal-advice
   disclaimers. Do include the AI transparency notice that this
   is an AI-assisted draft requiring attorney review.
7. Apply the KLG Style Guide throughout: write like a normal person,
   no legalese, active voice, punchy openers.
8. Target length: 3,000–5,000 words depending on complexity and
   number of issues.
9. All [VERIFY], [RESEARCH NEEDED], and [Record cite needed] flags
   must be collected in a summary list under Action Items.
10. After delivering the strategy memo AND the workflow pattern
    questions, provide the Cowork-to-Chat offboard instructions
    (see "Cowork-to-Chat Offboard Point" above).
11. **Terminal project status update:** After the strategy memo
    is delivered and all workflow pattern questions are answered,
    search the Projects database for the project page associated
    with this memo (by matter name or case number). Set the
    project's **Status** to "Done." This is a mandatory terminal
    step — strategy memo projects must not remain "In progress"
    after the memo is delivered. If the strategy memo is linked
    to a Case Project (not a standalone Memos project), do NOT
    mark the Case Project as Done — only mark standalone Case
    Support / Memos projects as Done.

### Respondent Mode — Additional Rules

12. Steel-man every opposing argument. Present it in its strongest
    form. The value of this memo is in preparing for the strongest
    version of their case, not a caricature.
13. Cross-reference every record citation the opponent makes. Note
    any that are inaccurate or misleading.
14. The pivot/reframe for each strong argument is the most valuable
    part of this memo. Spend real analytical effort here. Do not
    just say "we disagree" — explain how we recharacterize the issue.
15. Never recommend ignoring a strong argument. Always have a response,
    even if the response is "concede and minimize."
16. Distinguish between "winning" arguments and "damage control"
    arguments. Label them honestly. Candor about litigation risk is
    expected.
17. Apply the reply brief x/y/z format where applicable: "In the
    AOB, we argue x. In the RB, respondents argue y. But y is
    wrong because z."

### Appellant Mode — Additional Rules

12. Pressure-test every ground for reversal. The value of this memo
    is in honestly assessing which issues are strong enough to carry
    and which will waste pages. Do not include a weak argument just
    to pad the brief — three strong arguments beat six mediocre ones.
13. Preservation analysis must be rigorous. For each issue, trace the
    specific document and page where the argument was raised below.
    If you cannot find it in the uploaded materials, write
    [Preservation cite needed — verify in full record] and flag it.
    Do not assume preservation.
14. Prejudice analysis must be concrete. "The error was prejudicial"
    without record-specific explanation is not useful. Explain what
    would have been different — what evidence would have come in, what
    finding would have changed, what outcome would have resulted.
15. The anticipated-defenses section for each issue is critical. Think
    like opposing counsel. What is their best argument for harmless
    error? For alternative grounds? For waiver? Build our argument
    to preempt these.
16. Identify the "lead issue" — the single strongest ground for
    reversal that should anchor the brief. If the court reads only
    one argument, which one should it be?
17. For rulings involving discretionary decisions (e.g., evidentiary
    rulings, discovery sanctions, fee awards), explain specifically
    how the trial court exceeded the bounds of discretion — what
    factors it ignored, what it misweighed, or what arbitrary
    determination it made. Abuse of discretion requires more than
    disagreement with the outcome.

---

## Cross-Platform Collaboration Offers

### Respondent Mode

**Alternative counter-strategies (after argument analysis):**
If any arguments are labeled "damage control" or "concede and
minimize," offer:

> "For Issue [N] — which I've labeled 'damage control' — would
> you like ChatGPT to take a fresh look at counter-strategies?
> Sometimes a second platform finds reframings I can't see from
> inside the same analytical framework."

Collaboration type: Type 2.

**Narrative and theme brainstorming (before Structure section):**

> "I have the argument inventory mapped. Before I write the
> theme and narrative section, would you like ChatGPT to
> brainstorm alternative narrative frames?"

Collaboration type: Type 3.

### Appellant Mode

**Independent error-spotting (after initial analysis):**

> "I've identified [N] grounds for reversal. Before we finalize,
> would you like ChatGPT to independently read the ruling and
> spot errors I may have missed? Most useful for complex rulings
> with multiple legal theories."

Collaboration type: Type 1.

**Narrative and theme brainstorming (before Structure section):**

> "I have the error inventory mapped. Before I write the
> brief structure and theme section, would you like ChatGPT to
> brainstorm alternative narrative frames? For an opening brief,
> the narrative is often the difference between a technically
> correct brief and a persuasive one."

Collaboration type: Type 3.

**Red team / anticipated defenses (after full analysis):**

> "The strategy memo is drafted. Would you like ChatGPT to do a
> red team pass — playing respondent's counsel and identifying
> the strongest defenses to each of our arguments? I'll
> incorporate the findings into the anticipated-defenses sections."

Collaboration type: Type 5.

All ChatGPT collaboration offers follow the Cross-Platform
Handoff Protocol in `claude.md`: Notion handoff page first,
then the ChatGPT launch prompt. No exceptions.

---

## .docx Generation Workflow

This workflow runs only when the user requests the .docx —
either after iterating in Notion, or immediately if the user
requests .docx up front.

1. Read `/mnt/skills/public/docx/SKILL.md` — specifically the
   "Editing Existing Documents" section.
2. Copy the template (see Template Location below) to the working
   directory.
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
8. Fix standalone declarations (prevents Word "unreadable content"
   error):
   ```
   python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py output.docx
   ```
9. Copy to `/mnt/user-data/outputs/` and present.

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

**CRITICAL:** Do not specify fonts, margins, or page sizes in the
generation script. The template carries all formatting. Do not use
docx-js to generate from scratch. Do not define explicit formatting
in code — if you find yourself writing `font:` or `size:` or
`spacing:` in a generation script, you are on the wrong path.

---

## Style Quick-Reference

These rules apply regardless of whether reference files are
populated:

- Write like a normal person. No legalese.
- Active voice. Punchy sentence openers.
- No block quotes unless truly necessary (prefer integrated quotes).
- Reply brief x/y/z format (Respondent Mode): "In the AOB, we
  argue x. In the RB, respondents argue y. But y is wrong
  because z."
- Case names italicized. California Style Manual for CA authorities,
  Bluebook for federal.
- REF citation format: (REF[MatterNumber]-[PageNumber].)
- Document-name fallback: (2026-02-03 Tentative_Ruling at 2.)
- Record cites: (1-CT-1.), (1-AA-1.), (1-RT-1.) — volume-prefix-page,
  no spaces, period inside closing paren.
- Every factual assertion must cite to the record or source document.
- Flag uncertainty: [VERIFY], [RESEARCH NEEDED], [Record cite needed].
- Never fabricate case citations.
