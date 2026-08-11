# NotebookLM Prompt Templates

This reference contains the five NotebookLM audio session
prompt templates for oral argument preparation. Each prompt
generates a distinct audio conversation approaching the case
from a different angle.

When customizing these prompts, replace all bracketed
placeholders with case-specific content from the Phase B
Argument Map. The prompts should be posted to the Notion
page as code blocks so they paste cleanly into NotebookLM.

---

## Recommended Listening Order

1. **Prompt 1 — "Our Strongest Case"** — Listen first to
   internalize the narrative and conviction
2. **Prompt 2 — "The 30,000-Foot View"** — Balanced
   perspective on both sides
3. **Prompt 3 — "The Hot Bench"** — Hear how the panel
   might think about the case
4. **Prompt 4 — "The Other Side's War Room"** — Understand
   opposing strategy
5. **Prompt 5 — "The Procedural Gauntlet"** — Confirm
   procedural foundation is solid

---

## NotebookLM Setup Instructions

Include these instructions on the Notion page for the
person setting up the sessions:

```
FOR EACH PROMPT BELOW:
1. Open a new NotebookLM notebook
2. Upload the source documents listed under "Sources"
   for that specific prompt (each prompt has different
   source requirements — do not upload the same set for
   all five)
3. In the "Customize Audio Overview" dialog, set the
   Format, Length, and Language per the table below
4. Copy the prompt text into the "What should the AI
   hosts focus on in this episode?" field
5. Generate the audio overview
6. Save the audio file with the session name

NOTEBOOKLM SETTINGS PER PROMPT:

  Prompt 1 — "Our Strongest Case"
    Format:   Deep Dive
    Length:   Long
    Language: English

  Prompt 2 — "The 30,000-Foot View"
    Format:   Debate
    Length:   Long
    Language: English

  Prompt 3 — "The Hot Bench"
    Format:   Deep Dive
    Length:   Default
    Language: English

  Prompt 4 — "The Other Side's War Room"
    Format:   Deep Dive
    Length:   Default
    Language: English

  Prompt 5 — "The Procedural Gauntlet"
    Format:   Critique
    Length:   Default
    Language: English

WHY THESE SETTINGS:
- Deep Dive: Used for collaborative, exploratory
  conversations (prompts 1, 3, 4) where two speakers
  are working through ideas together.
- Debate: Used when the two speakers take genuinely
  opposing positions (prompt 2 — advocate vs. skeptic).
- Critique: Used when one speaker is evaluating the
  other's position (prompt 5 — the procedural hawk
  testing the advocate's procedural foundations).
- Long: Used for prompts that need to develop a full
  narrative arc (prompts 1 and 2). Default is fine for
  the more focused sessions (prompts 3, 4, 5).

IMPORTANT — Source Documents:
- Download the source files from SharePoint using the
  URLs listed in the "Source Documents" section at the
  top of this page.
- Each prompt lists exactly which documents to upload.
  Do NOT upload the full reporter's transcript or
  appendix volumes unless specifically noted — the
  briefs already contain the relevant record citations
  and the full record is too large for NotebookLM.
- If a prompt says "optionally add" a document, use
  your judgment — include it if the file is reasonably
  sized (under ~50 pages) and adds useful context.

Repeat for each of the five prompts. Each is a separate
NotebookLM session with its own sources.
```

---

## Prompt 1 — "Our Strongest Case" (The Narrative Session)

### NotebookLM Settings
- **Format:** Deep Dive
- **Length:** Long
- **Language:** English

### Purpose
Pure persuasive synthesis. No devil's advocate. This session
distills our strongest legal arguments, strongest facts,
strongest equities, all woven into our most compelling
framing, case narrative, and themes. The attorney listens
to this to internalize the conviction of their position —
ideally on the drive to court.

### Sources to Upload
- Our brief (filed version)
- Case assessment memo (if available, optional)
- Do NOT include opposing briefs — this session is pure advocacy
- Do NOT include the reporter's transcript or appendix volumes

### Prompt Template

```markdown
Role: Create an audio conversation between two speakers who
have read all uploaded sources.

Speaker A (Lead Counsel): The attorney arguing the case.
Confident, passionate, deeply familiar with every fact
and authority. Speaks as someone who believes completely
in this case.

Speaker B (Strategic Advisor): A senior appellate mentor.
Draws out the best version of every argument, helps
sharpen the framing, and connects the legal arguments
to the equities and the remedy.

Overall goal:
Produce a persuasive synthesis of our STRONGEST case for
[CASE NAME] ([CASE NUMBER]). This is not a balanced
overview — this is the best version of our position,
designed to help the attorney internalize the narrative
and walk into the courtroom with conviction.

Episode structure:

1. THE STORY (5 min): Tell the story of this case from
   our client's perspective. What happened, why it was
   wrong, and why the court should care. Weave in the
   strongest facts from the record.
   [INSERT KEY SYMPATHETIC FACTS FROM ARGUMENT MAP]

2. THE STRONGEST LEGAL ARGUMENTS (10 min): Walk through
   our top legal arguments in order of strength:
   [INSERT TOP 2-3 LEGAL ARGUMENTS WITH AUTHORITIES]
   For each: state the rule, the key authority, and why
   it controls here. Make it feel inevitable.

3. THE EQUITIES (5 min): Why fairness demands this result.
   [INSERT STRONGEST EQUITABLE ARGUMENTS]
   Connect the equities to the legal standard — show how
   the law and fairness point in the same direction.

4. THE REMEDY (3 min): What exactly we are asking the court
   to do:
   [INSERT SPECIFIC RELIEF SOUGHT]
   Why this remedy is clean, narrow, and correct. Address
   any fallback remedy.

5. THE THEME (5 min): Bring it all together. What is the
   one-sentence version of why we win?
   [INSERT PRIMARY THEME/NARRATIVE]
   How does this theme connect the law, the facts, and
   the equities into one coherent story?

6. THE CONVICTION CLOSE (2 min): End with the most powerful
   version of our closing — the 60-second statement that
   captures everything. This is what the attorney should
   hear ringing in their ears walking to the podium.

Style and constraints:
- Tone: confident, passionate, precise. Not arrogant.
- Use full citations when referencing authorities.
- Use record citations when referencing facts.
- No counterarguments in this session — save that for the
  other prompts.
- Make it feel like two people who deeply believe in this
  case preparing to win it.

Output check before ending:
Did you state the strongest legal arguments with authorities?
Did you weave in the strongest facts and equities?
Did you articulate the specific remedy?
Did you deliver a compelling closing?
```

---

## Prompt 2 — "The 30,000-Foot View" (Advocate vs. Skeptic)

### NotebookLM Settings
- **Format:** Debate
- **Length:** Long
- **Language:** English

### Purpose
Balanced overview of the case — strongest arguments on each
side, policy angles, concessions, and the close-out toolkit.
This is "what is the case really about and how does it look
from the outside?"

### Sources to Upload
- Our brief (filed version)
- Opposing brief(s)
- Key orders/rulings being challenged (optional)
- Do NOT include the full reporter's transcript or appendix
  volumes — the briefs contain the relevant record citations

### Prompt Template

```markdown
Role: Create an audio conversation between two speakers who
have read all uploaded sources (all appellate briefs and the
appellate record).

Speaker A (Advocate): Fair but favorable to [OUR CLIENT]'s
position.

Speaker B (Skeptic): Serious, probing, critical but fair,
channeling an appellate panel's outside-observer perspective.

Overall goal:
Surface the big-picture narrative (30,000-foot view) and
what an outside panel is likely to think about [CASE NAME]
([CASE NUMBER]).
Identify the strongest arguments for us and the strongest
counterarguments against us, including policy and
institutional-concern angles beyond the parties.
Stress-test with lightning-round hostile questions.
End with likely opening questions, crisp answers, and a
short closing.

Use of sources:
Derive answers from the uploaded briefs and record (and any
key cases cited there).
[IF APPLICABLE: Continually test the theme: "[INSERT PRIMARY
THEME]." Explain when it helps us, when it doesn't, and what
the other side will say back.]
When referencing legal authorities, always give full-text
citations.
When referencing factual materials, always give full-text
citations to the record (AA, RT, or related sources).

Episode structure:

Orientation (Panel's Vantage Point): In your own words: What
is the single-sentence reason [OUR CLIENT] should win? What
relief is being sought? Top 2-3 issues on appeal (ranked)?
Flag genuine disputes vs. undisputed facts.

Standards and Posture: One-line procedural posture. Standards
of review only if outcome-relevant or contested.

Best Case for Us vs. Best Case Against Us: Advocate lays out
top 2-3 arguments with most persuasive record and legal
support. Skeptic steel-mans top 2-3 counterarguments. Go
point-counterpoint. Zoom out to policy/institutional stakes
where helpful. [IF APPLICABLE: Probe the theme "[INSERT
THEME]": when compelling, when it risks overreach, how to
cabin it.]

Concessions and Calibration: Narrow concessions to prepare.
Landmines (adverse authority, waiver/forfeiture, SoR traps)
and safe routes.

Lightning Round (Hostile Bench): Skeptic fires 5-7 quick,
tough questions. Advocate answers in 1-2 sentences each.

What the Panel Likely Cares About: Top concerns and how each
side will frame them.

Close-Out Toolkit:
(1) Three likely opening questions from the bench.
(2) Three crisp one-sentence answers.
(3) A 20-second closing linking the standard of review, the
clean rule, and why relief is correct.

Style: Probing, serious, critical but fair. Conversational.
No block quotes or pincites. If uncertain, say so and propose
the most panel-persuasive framing. Be explicit about tradeoffs.

Output checks:
Did you state the single-sentence "why we win," relief, and
ranked issues?
Did you present both strongest for and against?
Did you include Lightning Round and Close-Out Toolkit?
```

---

## Prompt 3 — "The Hot Bench" (Judicial Conference)

### NotebookLM Settings
- **Format:** Deep Dive
- **Length:** Default
- **Language:** English

### Purpose
Hear the case discussed as if by the actual panel in a
pre-argument conference. Gives the attorney an over-the-
shoulder view of how the judges might be thinking before
argument begins.

### Sources to Upload
- Our brief (filed version)
- Opposing brief(s)
- Panel Intelligence Memo from Phase A (if available —
  paste key excerpts into the prompt if NotebookLM cannot
  accept it as a separate source)
- Do NOT include the full reporter's transcript or appendix

### Prompt Template

```markdown
Role: Create an audio conversation between two appellate
judges discussing [CASE NAME] ([CASE NUMBER]) as if in a
pre-argument conference. They have read all uploaded briefs
and materials.

[IF PANEL INTEL AVAILABLE:]
Speaker A: Modeled on [JUSTICE/JUDGE NAME 1] — known for
[INSERT KEY TENDENCIES FROM PHASE A: e.g., textualist
approach, skepticism of broad equitable arguments, emphasis
on record evidence].

Speaker B: Modeled on [JUSTICE/JUDGE NAME 2] — known for
[INSERT KEY TENDENCIES FROM PHASE A: e.g., pragmatic
balancing, concern for administrability, attention to
procedural regularity].

[IF PANEL INTEL NOT AVAILABLE:]
Speaker A: A sympathetic judge who sees merit in [OUR
CLIENT]'s position but has genuine questions.
Speaker B: A skeptical judge who leans toward affirmance but
is open to persuasion.

Overall goal:
Simulate a pre-argument judicial conference about this case.
The judges discuss what concerns them, what questions they
plan to ask each side, where they think the case turns, and
what result they are tentatively leaning toward.

Episode structure:

1. First Impressions (3 min): Each judge shares their
   initial reaction after reading the briefs. What jumped out?
   What is the case really about? Any immediate concerns?

2. The Key Issues (10 min): Walk through the top issues.
   For each:
   - What is the strongest argument on each side?
   - Which side has the better of it?
   - What questions do they want to ask counsel?
   [INSERT TOP 2-3 ISSUES FROM ARGUMENT MAP]

3. Procedural Concerns (3 min): Any threshold issues?
   [INSERT ANY PROCEDURAL GAUNTLET CONCERNS]
   Are they inclined to reach the merits or dispose on
   procedural grounds?

4. What They Want to Hear (5 min): For each side:
   - What would [OUR CLIENT]'s counsel need to say to
     win you over?
   - What would [OPPOSING PARTY]'s counsel need to say?
   - What concessions would be helpful?

5. Tentative Leanings (3 min): Where are they leaning?
   What would change their mind? Any chance of a split?

6. Questions They Plan to Ask (5 min): Each judge
   identifies 3-4 questions they plan to ask. Explain
   why each question matters and what answer they're
   looking for.

Style: Collegial but candid. Judges speak frankly to each
other. They refer to the parties' arguments by substance,
not by party name when possible. They express genuine
uncertainty where it exists.

Do not simulate timekeeping or clerk interactions.
```

---

## Prompt 4 — "The Other Side's War Room" (Opposing Counsel)

### NotebookLM Settings
- **Format:** Deep Dive
- **Length:** Default
- **Language:** English

### Purpose
Know thy enemy. Hear how opposing counsel would prepare for
argument — their best pitch, where they think we're
vulnerable, and what questions they hope the court asks us.

### Sources to Upload
- Opposing brief(s)
- Our brief (filed version)
- Do NOT include the full reporter's transcript or appendix

### Prompt Template

```markdown
Role: Create an audio conversation between two speakers
preparing the OPPOSING side for oral argument in [CASE NAME]
([CASE NUMBER]).

Speaker A (Lead Counsel for [OPPOSING PARTY]): The attorney
who will argue for [OPPOSING PARTY]. Smart, experienced,
preparing seriously.

Speaker B (Appellate Strategist): A senior consultant helping
[OPPOSING PARTY]'s counsel prepare. Pushes for the strongest
framing and anticipates what the court will care about.

Overall goal:
Simulate [OPPOSING PARTY]'s oral argument preparation session.
This should feel authentic — these are competent lawyers
preparing to win. The listener ([OUR CLIENT]'s attorney)
should come away understanding the other side's best strategy.

Episode structure:

1. Their Story (5 min): How does [OPPOSING PARTY] frame
   the case? What is their one-sentence narrative? What
   facts do they emphasize?

2. Their Strongest Arguments (10 min): Walk through
   [OPPOSING PARTY]'s top 2-3 arguments:
   [INSERT OPPOSING PARTY'S STRONGEST ARGUMENTS FROM
   VULNERABILITY INVENTORY]
   For each: the rule, the key authority, and why it
   controls. Make the strongest case.

3. Their Theme / Narrative (3 min): What is the overarching
   story from their perspective?
   [INSERT THEIR STRONGEST THEME FROM VULNERABILITY INVENTORY]

4. Where They Think We're Vulnerable (5 min): What do they
   see as our weaknesses?
   [INSERT OUR BIGGEST LEGAL WEAKNESS AND REMEDY PROBLEMS]
   What questions do they hope the court asks us?

5. Their Concession Strategy (3 min): What are they prepared
   to concede? What narrow ground do they want to defend?

6. Their Worry List (3 min): What keeps them up at night?
   Where do they think they might lose? What questions do
   they NOT want the court to ask them?

7. Their Ideal Questions for Us (3 min): If they could
   whisper questions to the judges to ask [OUR CLIENT]'s
   counsel, what would they be?

Style: Professional, strategic, realistic. These are good
lawyers having a serious prep session. Not cartoonishly
adversarial.

Output check:
Did you present their strongest arguments with authorities?
Did you identify where they think we're vulnerable?
Did you surface their concession strategy and worry list?
```

---

## Prompt 5 — "The Procedural Gauntlet"

### NotebookLM Settings
- **Format:** Critique
- **Length:** Default
- **Language:** English

### Purpose
Stress-test every threshold issue — appealability, timeliness,
preservation, forfeiture, standing, mootness. This session
ensures the attorney is not caught flat-footed on any
procedural question.

### Sources to Upload
- Our brief (filed version)
- Opposing brief(s)
- Notice of appeal and any relevant procedural filings
- Key orders/rulings (especially the order being challenged)
- Include relevant reporter's transcript excerpts ONLY if
  preservation of issues is contested (e.g., the transcript
  pages where the objection or colloquy occurred)
- Include relevant appendix excerpts ONLY if appealability
  turns on the specific content of the order or judgment
- In most cases, the briefs plus procedural filings are
  sufficient — do NOT upload entire transcript volumes or
  full appendix sets

### Prompt Template

```markdown
Role: Create an audio conversation between two speakers
examining the procedural foundations of the appeal in
[CASE NAME] ([CASE NUMBER]).

Speaker A (Procedural Hawk): Fixated on jurisdiction,
timeliness, preservation, and forfeiture. Looks for any
procedural defect that could dispose of the case without
reaching the merits. Thorough, relentless, fair.

Speaker B (Advocate): Trying to demonstrate that all
procedural prerequisites are satisfied and the court
should reach the merits. Prepared, but tested hard.

Overall goal:
Stress-test every procedural and jurisdictional foundation
of this appeal. Surface any issue the panel might raise
sua sponte or that opposing counsel might spring. The
listener should walk away either confident that the
procedural foundation is solid, or aware of exactly where
the vulnerabilities are and how to address them.

Episode structure:

1. Appealability (5 min):
   [INSERT APPEALABILITY ANALYSIS FROM PROCEDURAL GAUNTLET]
   - Is this order/judgment appealable?
   - Any one-final-judgment issues?
   - If writ: extraordinary relief factors?
   Hawk probes. Advocate defends.

2. Timeliness (5 min):
   [INSERT TIMELINESS ANALYSIS]
   - Key dates: entry, notice of entry, NOA filing
   - Was the NOA timely? Any tolling? Premature notice?
   Hawk probes. Advocate defends.

3. Preservation — Issue by Issue (10 min):
   [FOR EACH ISSUE, INSERT PRESERVATION ANALYSIS]
   Take each issue raised on appeal and examine:
   - Where in the record was it raised below?
   - Was the objection specific enough?
   - Any invited error?
   - If not preserved: is there a basis to argue anyway?
   Go issue by issue. Do not gloss over any.

4. Standing and Mootness (3 min):
   [INSERT ANY STANDING/MOOTNESS CONCERNS]
   - Any changed circumstances during appeal?
   - Mootness exceptions applicable?

5. Sua Sponte Risks (3 min):
   - What might the court raise on its own?
   - Compliance with appellate rules?
   - Anything neither party briefed?

6. Verdict (3 min): Procedural Hawk delivers a verdict:
   Are the procedural foundations solid? Where are the
   cracks? What should the advocate be prepared to say
   if questioned on any procedural point?

Style: Thorough, serious, fair. The Hawk is not trying to
be difficult — they're trying to ensure nothing is missed.
The Advocate should give real answers, not hand-waves.

Output check:
Did you examine appealability, timeliness, and preservation
for every issue?
Did you address standing and mootness?
Did you identify sua sponte risks?
Did you deliver a clear verdict on procedural soundness?
```

---

## Deep Research Panel Prompt (Optional Phase A Upgrade)

When the user opts for the Deep Panel Research upgrade in
Phase A, generate this prompt for Comet/ChatGPT Deep Research:

```markdown
You are ChatGPT-5. Conduct a Deep Research project on the
appellate panel for my upcoming oral argument in [CASE NAME]
([CASE NUMBER]).

The panel: [INSERT COURT, DIVISION/CIRCUIT, JUSTICE/JUDGE
NAMES]

Research each justice or judge's judicial philosophy, prior
opinions (published and unpublished), and writing tendencies.
Focus especially on:

(1) Their treatment of arguments like those raised in my
case, including: [INSERT TOP 2-3 LEGAL ISSUES FROM THE
CASE — e.g., "standards of review for summary judgment,"
"interpretation of statutory NOAPOL clauses," "respondeat
superior in the gig economy context"]

(2) Past decisions on these specific legal topics — how have
these judges ruled when faced with similar issues? Include
both published and unpublished opinions.

(3) How they respond to record-based arguments vs. rhetorical
or policy-based arguments — especially [INSERT SPECIFIC
THEME, e.g., "arguments that a trial court misapplied a
discretionary standard"].

(4) Their preferred persuasion styles — textual precision,
institutional legitimacy, judicial restraint, pragmatic
balancing — and what kinds of policy appeals or tone they
find effective.

(5) Recurring patterns in majority vs. dissenting opinions
that indicate openness to broader institutional arguments,
fairness narratives, or rule-based outcomes.

(6) Any known hot-button issues, pet peeves, or tendencies
that would affect how they receive our arguments.

Synthesize this research into a briefing that identifies:
• Arguments this panel tends to find persuasive
• Reasoning they distrust or push back on
• Specific framing strategies that resonate with them
• Tactical recommendations for oral argument — what to
  emphasize, what to avoid, how to structure responses
• Any past opinions directly on point to our issues
```
