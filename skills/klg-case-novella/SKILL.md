---
name: klg-case-novella
description: "Create a quasi-fictionalized novella or short story based on a case to aid absorption of key facts, legal concepts, and policies. Use when the user says 'case novella', 'case narrative', 'write a story about the case', 'fictionalized account', 'novella', 'short story for the case', 'narrative preparation', 'story-based prep', 'build a case narrative', 'dramatize the case', 'narrative oral argument prep', or references creating a fictionalized account of any matter. Also triggers when the oral argument skill offers the narrative add-on. Produces a .docx novella (10-14 chapters, 15,000-25,000 words) for reading or audiobook conversion via Speechify. Phases A-B are interactive (story design and blueprint); C-D run autonomously in a parallel Chat tab. NOT for brief drafting, case assessment, or research. Pairs with klg-oral-argument but runs independently at any stage."
---

# KLG Case Novella

## Purpose

Produce a quasi-fictionalized biographical account of a case —
a novella or short story — that helps the attorney absorb and
visualize key facts, legal concepts, institutional dynamics,
and policy tensions. The output is a polished .docx suitable
for reading or conversion to audiobook format via Speechify.

This is not ordinary creative writing. It is a litigation
preparation tool that teaches the case through story — making
the attorney feel why one legal framing is natural and the
competing framing is strained.

## Required Context

Before beginning, read these project files:

1. `/mnt/project/claude.md` — Citation standards, output rules,
   quality controls
2. `references/workflow-patterns.md` — Session logging (Pattern 3)
3. `references/style-palette.md` — Author voice profiles,
   blending rules, and style selection guidance

Do not skip these reads.

## Required Inputs

- Case materials sufficient to ground the narrative. Any of:
  - Case assessment memo
  - Response plan memo
  - Research compilation memo
  - Briefs (ours and/or opposing)
  - Key orders, rulings, or transcripts

The more context provided, the richer the narrative. But even
a single case assessment memo is enough to start.

## Helpful But Not Required

- Oral argument prep materials (Phase B argument map, panel
  intelligence)
- Record excerpts with specific factual scenes
- Client communications showing the human stakes
- Prior research memos or authority analyses
- The user's own notes on what themes matter most

## Phase Overview

Four phases. Phases A and B are interactive and require the
user's input. Phases C and D run autonomously — designed to
execute in a parallel Chat tab while the user works elsewhere.

- **Phase A: Story Design** (~15 min, interactive)
- **Phase B: Blueprint** (~10 min, interactive)
- **Phase C: Drafting** (~30–45 min, autonomous)
- **Phase D: Assembly & Debrief** (~10 min, minimal interaction)

---

## Mode Selection

Before starting, present the mode selection prompt:

```
Before we start the case novella, how would you like
to run this?

CHAT (recommended — runs in a parallel tab):
  ✓ Phases A and B take ~25 minutes of interactive work.
    After that, you approve the blueprint and Phase C
    drafts all chapters autonomously — no babysitting.
  ✓ You can run this in a second tab while oral argument
    prep or other work continues in the main session.
  ✗ You'll need to upload: case assessment, briefs, and
    any other materials you want the story grounded in.

COWORK:
  ✓ I can pull everything from the matter folder — no
    uploads needed.
  ✗ Ties up Cowork for 60–90 minutes total. Since most
    of Phase C is autonomous drafting, this is an
    expensive use of Cowork.

Recommendation: Start in Chat. Upload the case assessment
and briefs. The novella doesn't need the full record — it
needs the synthesized legal analysis.

Which do you prefer?
```

**Exception:** Skip if the user has already uploaded documents
or is clearly in a mode.

---

## Phase A: Story Design (Interactive)

### Purpose

Ingest case materials, diagnose the case type, and collaborate
with the user to select the story approach, author voice, and
narrative focus.

### Before starting: Set expectations.

Before asking any questions, present the interactive roadmap
so the user knows exactly what's ahead and when they're free
to walk away:

```
Here's how this works. I need your input for a few
decisions up front, and then the drafting runs on its
own — no babysitting needed.

You have two options:

EXPRESS (1 decision):
  I analyze the case, make all the design choices
  (story type, narrator mode, author voice, focus
  areas, treatment, chapter blueprint), and present
  the complete blueprint for your approval. You
  review it once and say "go." One decision, then
  I draft autonomously.

GUIDED (6 decisions):
  We walk through each choice together:
    1. Story type
    2. Narrator mode (who tells the story)
    3. Author voice
    4. Focus areas and scope
    5. Treatment selection
    6. Blueprint approval
  More control, but takes ~25 minutes of back-and-forth.

Either way, once the blueprint is approved, drafting
runs unattended (~30–45 minutes). You can walk away.

Express or guided?
```

### Express lane.

If the user chooses express:

1. Run Steps A.1a through A.1d (ingest, pull oral argument
   intelligence, identify preparation gaps, produce the
   case diagnosis). This is internal analysis — no user
   input needed.

2. Based on the diagnosis, make all design decisions:
   - Select the best story type
   - Select the best narrator mode (observer frame vs.
     direct POV) — for fact-intensive cases, default to
     observer frame and select the observer type
   - Select the best primary author voice (and secondary
     if warranted)
   - Select focus areas based on preparation gaps
   - Choose scope (full novella vs. short story)
   - Generate the single best treatment (not three — pick
     the winner)
   - Build the story spine (per Step B.0), including the
     observer character if observer frame was selected
   - Build the full chapter blueprint

3. Present everything as a single package for approval:

```
I've analyzed the case and built a complete novella
blueprint. Here's what I'm recommending:

STORY TYPE: [type] — [one-sentence reason]
NARRATOR: [observer frame / direct POV] — [reason]
  [If observer: Observer character: (name), a (role).
  The frame is fiction; the painting is fact — (name)'s
  life is invented, but everything they witness or
  learn about the case is grounded in the record.]
VOICE: [primary] with [secondary] — [one-sentence reason]
FOCUS: [list focus areas] — [why these matter]
SCOPE: [full novella / short story] — [X] chapters

STORY SPINE:
  Protagonist: [name, description, desire, fear]
  [If observer frame: Observer: (name), a (role).
  They want (desire). They see the case through
  (lens). Their arc is (trajectory).]
  Inciting event: [what happens]
  Central question: [the human question]
  Plot arc: [beginning → complication → confrontation
    → resolution]
  Emotional trajectory: [start feeling → end feeling]
  Supporting cast: [names and roles]

TREATMENT:
  [one-paragraph premise]
  [one-paragraph what it teaches]
  [POV characters]
  [narrative arc]

CHAPTER BLUEPRINT:
  [full chapter outline per Phase B format]

GUARDRAILS:
  [do-not-overstate list]
  [If observer frame: FACTUAL FIDELITY RULES —
  see guardrails section]

Approve and start drafting?
  1. Approved — start drafting (you can walk away now)
  2. Looks good but change [specific thing]
  3. Switch to guided mode — I want to make the
     choices myself
```

If approved, proceed directly to Phase C (drafting).
If the user wants a change, make the adjustment and
re-present for approval — still a single decision loop.
If the user switches to guided mode, restart at Step A.2
(the diagnosis is already done) and follow the guided
path from there.

### Guided path.

If the user chooses guided, proceed with Step A.1 through
A.6 and Phase B as documented below, with progress
indicators at each step.

### Step A.1: Ingest and diagnose.

**A.1a: Read case materials.**

Read all uploaded case materials (briefs, case assessment,
response plan, research memos, etc.).

**A.1b: Pull oral argument intelligence (if available).**

If the user has completed oral argument prep for this matter,
search for the oral argument Notion page using `notion-search`
(search for the case name + "oral argument" or "argument map"
in the Research database). If found, read it using
`notion-fetch` and extract:

- **Vulnerability inventory** — the arguments where our
  position is weakest or most exposed
- **Zinger anticipation** — the hardest questions the panel
  is likely to ask
- **Concessions and landmines** — areas where we may need
  to give ground or where missteps are costly
- **Procedural gauntlet items** — preservation issues,
  jurisdictional questions, standard of review challenges
- **Panel intelligence** — what this specific panel cares
  about, what framing resonates with them

If no oral argument page exists, ask the user:

```
I don't see an oral argument prep page for this matter
in Notion. Do you have one I should check, or should I
work from the briefs and case assessment alone?
```

**A.1c: Identify preparation gaps.**

Based on the case materials AND the oral argument
intelligence (if available), identify:

1. **Underexplored areas** — legal theories, factual
   dimensions, or policy implications that the briefs
   touch on but don't fully develop. These are areas
   where the novella can build the user's intuition
   beyond what the briefs cover.

2. **Trap zones** — arguments or factual areas where the
   panel or opposing counsel is likely to press hard,
   and where the user needs to have internalized the
   strongest possible framing. The novella should make
   the user viscerally comfortable in these zones.

3. **Opponent's best moves** — the strongest version of
   the other side's argument. The novella should force
   the reader to sit inside that argument and understand
   why it ultimately fails.

4. **Emotional and narrative gaps** — aspects of the case
   that are legally significant but that the briefs
   (appropriately) treat analytically. The novella can
   make these concrete and felt.

Present these findings as part of the Case Diagnosis.

**A.1d: Produce the Case Diagnosis.**

Combine the above into a Case Diagnosis with these elements:

1. **Case type classification:**
   - Fact-intensive (credibility, sufficiency of evidence,
     competing narratives about what happened)
   - Law/policy-intensive (statutory interpretation, regulatory
     framework, competing legal theories)
   - Procedural (preservation, jurisdiction, standard of review
     as the real battlefield)
   - Mixed (identify the dominant axis)

2. **Narrative potential assessment:**
   - What scenes or moments have dramatic potential?
   - What institutional dynamics are at work?
   - What characters (real or composite) could embody the
     legal conflicts?
   - What is the emotional core of the case?

3. **Preparation gap analysis** (from A.1c above):
   - Areas the novella should strengthen
   - Trap zones to inoculate against
   - Opponent framing to internalize and defeat

4. **Recommended story approach** (with reasoning):
   Based on the diagnosis AND the preparation gaps,
   recommend which story type and author voice would be
   most effective for this case. Explain why — including
   how the recommendation addresses identified gaps.

### Step A.2: Story type selection.

Present the story type menu as an interactive choice:

```
What kind of novella would be most useful for your
preparation? Here are the approaches, with my
recommendation marked:

STORY TYPES:

1. FACT-IMMERSIVE
   Dramatize the specific facts of your case through
   characters who lived them. Composite characters
   based on the parties, witnesses, and players.
   Best for: cases where the factual record is the
   battlefield — credibility disputes, sufficiency
   challenges, cases where you need to internalize
   what happened and in what order.

2. LAW/POLICY THOUGHT EXPERIMENT
   Explore how the legal issues feel to various
   institutional players — not a retelling of your
   specific facts, but a fictionalized scenario that
   embodies the same legal tensions.
   Best for: cases driven by statutory interpretation,
   regulatory frameworks, or policy questions where the
   facts are relatively stipulated but the legal framing
   is everything.

3. COURT-INTERNAL
   Tell the story from inside the Court of Appeal —
   the justices' law clerks researching the issues, the
   panel's conference discussion, the competing draft
   opinions. How does the court see this case?
   Best for: cases where you need to internalize the
   judicial perspective — what makes a justice
   uncomfortable, what makes the result feel inevitable.

4. ADVERSARIAL POV
   Tell the story from opposing counsel's perspective,
   or from the trial judge's chambers. What does the
   other side believe? What is the trial judge's
   reasoning? Where are they confident, and where are
   they nervous?
   Best for: cases where understanding the opponent's
   strongest framing will sharpen your response.

5. BLENDED / MULTI-POV
   Combine approaches — e.g., fact-immersive chapters
   alternating with court-internal chapters, or
   adversarial POV intercut with the client's experience.
   Best for: complex cases with multiple dimensions.

⭐ MY RECOMMENDATION: [X] because [reasoning].

Which approach, or what blend?

[Step 1 of 6 — 5 more decisions after this, then
drafting runs on its own.]
```

### Step A.3: Narrator mode selection.

After the story type is chosen, present the narrator mode.
This is how the story handles the boundary between invented
and factual material.

**When to present this:** Always. But the recommendation
changes based on the case type from Step A.1d.

```
Next, let's decide who tells the story. This matters
especially for how the novella handles facts versus
fiction.

Think of it like a painting in a frame. The FRAME is
fiction — invented characters, atmospheric details,
the narrator's inner life. The PAINTING is fact — the
actual case events, record evidence, legal rulings,
what people really said and did. The question is how
we build that frame.

NARRATOR MODES:

1. OBSERVER FRAME (Nick Carraway model)
   A fictional character at the periphery of real
   events — a friend, a family member, a paralegal,
   a court clerk, a journalist. The observer's life
   is clearly invented. The case events they witness
   or learn about maintain factual integrity.

   Your brain naturally sorts the two: "things about
   the observer" = fiction. "Things the observer sees
   or hears about the case" = fact. No contamination
   risk.

   When the observer learns about a key event, the
   prose can shift into a cinematic rendering of the
   actual scene — you're transported THERE, not stuck
   listening to someone recount it. Then the prose
   pulls back to the observer processing what they
   learned.

   OBSERVER TYPES:
   • Family member or friend — sees personal cost,
     hears the dinner-table version of the case
   • Court clerk or judicial assistant — sees both
     sides, watches the judge react in real time
   • Paralegal or junior associate — close enough to
     understand the strategy, junior enough to doubt
   • Journalist or writer — researching the broader
     legal issue, this case is their entry point
   • Other (describe — we can build any observer)

   ⭐ Recommended for fact-intensive cases.

2. DIRECT POV (multiple character POV)
   The story rotates through the actual characters —
   parties, attorneys, judges — as POV narrators. All
   characters are fictionalized composites. Their inner
   lives, dialogue, and atmospheric details are invented.

   This is how The App Is Never Wrong worked — Eddie,
   Marisol, Kim, and the others were all fictional.
   There was no contamination risk because the entire
   scenario was a thought experiment.

   ⭐ Recommended for law/policy cases where the
   facts are stipulated or not the battleground.

   ⚠️ CAUTION for fact-intensive cases: When characters
   are based on real parties and you invent their inner
   life and dialogue, those invented details can bleed
   into your factual recall. If you choose this mode
   for a fact-driven case, the drafting guardrails will
   enforce strict separation — but the observer frame
   is the safer structural choice.

3. HYBRID
   An observer frame for the fact-intensive parts of
   the case, with direct POV chapters for the law/policy
   dimensions (e.g., a fictional regulator, a composite
   opposing counsel). Useful for mixed cases.

⭐ MY RECOMMENDATION: [X] because [reasoning —
reference the case diagnosis and whether facts are
contested or stipulated].

Which mode? If observer frame, which observer type?

[Step 2 of 6 — 4 more decisions after this.]
```

### Step A.4: Author voice selection.

After the narrator mode is chosen, present the voice palette.
Read `references/style-palette.md` for the full profiles.

The voice selection has three parts: case-specific
recommendations, the full palette, and custom input.

**Part 1: Case-specific recommendations.**

Based on the case diagnosis, recommend 2–3 authors from the
full palette with specific explanations of why each fits
THIS case. Do not just list generic descriptions — explain
the match. For example:

```
Based on this case, here are the voices I'd recommend:

⭐ TOM WOLFE — primary recommendation
   This case turns on how an institution's incentive
   structure produces harm while insisting it isn't
   responsible. Wolfe's technique of revealing
   institutional behavior through accumulated status
   details and interior monologue is exactly how to
   make [specific issue] feel visceral rather than
   abstract. His onomatopoeia and sensory detail will
   anchor the [specific scenes] in the reader's memory.

   GEORGE ORWELL — strong secondary option
   The regulatory framework here has a "language
   controls thought" dimension — the way [party] uses
   terminology to reframe what is actually happening.
   Orwell's clarity and his instinct for how
   institutional language obscures reality would give
   this novella a sharper political edge.

   KEN FOLLETT — if you want structural sweep
   With [X] parallel storylines converging on [event],
   Follett's multi-POV architecture would let us track
   each thread simultaneously and build toward the
   collision point at [climactic moment].
```

Always explain the recommendation in terms of the specific
case — what issues, scenes, or dynamics make this author
the right fit.

**Part 2: Full palette.**

After the recommendations, present the complete roster
with brief descriptions so the user can browse alternatives:

```
FULL VOICE PALETTE:

Core voices:
  Tom Wolfe — New Journalism: immersive detail,
    institutional satire, onomatopoeia as memory aid
  Malcolm Gladwell — Explanatory narrative: counterintuitive
    turns, "here's what's really happening"
  Joseph Epstein — Urbane essayist: understated irony,
    drama in restraint and implication
  Ken Follett — Historical sweep: multiple POV threads
    converging on a single event
  John Grisham — Legal procedural: courtroom mechanics
    rendered as suspense
  Michael Lewis — Contrarian character study: the person
    who saw what no one else saw
  Erik Larson — Dual narrative: parallel timelines that
    converge with dramatic irony

Additional voices:
  Agatha Christie — Puzzle architecture: clues planted
    early, satisfying reveals, the reader as detective
  James Michener — Epic scope: deep historical context
    building toward the present moment
  Albert Camus — Existential clarity: moral weight,
    institutional absurdity, spare and direct prose
  George Orwell — Political precision: how language
    shapes reality, institutional doublespeak exposed
  Larry McMurtry — Western American realism: landscape
    as character, pragmatic voices, unsentimental truth

Or name any author you'd like — we can use anyone.
```

**Part 3: Custom input.**

Always close with:

```
Is there a specific author or influence not listed here
that you'd like to use? We can build a voice profile
for anyone.

IMPORTANT: Pick one primary voice. You can add a
secondary influence, but more than two will cancel
each other out. Think of it as: "Write like [X],
with touches of [Y]."

Primary voice?
Secondary influence (optional)?

[Step 3 of 6 — 3 more decisions after this.]
```

### Step A.5: Focus and scope.

Present the focus areas. If preparation gaps were identified
in Step A.1c, pre-check the relevant items and explain why:

```
Based on the case diagnosis [and the oral argument prep
materials], I've pre-selected the focus areas where the
novella can do the most work. Adjust as you see fit:

FOCUS AREAS — what should the novella help you
absorb? (pick all that apply)

☑ [Pre-checked items with explanation, e.g.:
   "The opponent's strongest arguments — the argument
   map flagged [specific vulnerability] as your biggest
   exposure at oral argument. The novella should make
   you comfortable sitting inside that argument."]
☑ [Another pre-checked item with explanation]

□ The factual chronology and key events
□ The legal framework and how it applies
□ The policy tensions and institutional incentives
□ The human stakes and emotional dimensions
□ The procedural history and preservation issues
□ The opponent's strongest arguments (to stress-test)
□ The judicial perspective on the case
□ Specific trap zones from oral argument prep:
  [list identified traps from A.1c, if available]
```

Then present POV and scope choices:

```
POV CHARACTERS — any specific perspectives you want?

□ The client or affected party
□ Opposing party or their counsel
□ The trial judge
□ The appellate panel / law clerk
□ A regulatory body or institutional actor
□ An insurance adjuster, expert, or third party
□ Other (describe)

SCOPE:

□ Full novella (10–14 chapters, ~20,000 words)
□ Short story (4–6 chapters, ~8,000 words)
□ Let Claude recommend based on the material

[Step 4 of 6 — 2 more decisions after this.]
```

### Step A.6: Treatment proposals.

After all selections, produce **three treatment proposals**.
Each treatment should include:

1. A one-paragraph premise
2. A one-paragraph statement of what the story teaches
3. A list of POV characters (3–7)
4. A two-sentence description of the narrative arc
5. Which oral-argument intuitions it trains
6. **Which preparation gaps it addresses** — specifically
   identify which trap zones, vulnerabilities, or
   underexplored areas from Step A.1c this treatment is
   designed to strengthen. Every treatment should address
   the identified gaps, but they may prioritize different
   ones.

Then recommend the best treatment with reasoning.

Present and ask the user to choose:

```
Here are three treatments. I recommend Treatment [X]
because [reasoning].

[Treatment 1]
[Treatment 2]
[Treatment 3]

Which treatment? Or should I adjust one of these?

[Step 5 of 6 — one more decision after this (the
chapter blueprint), then drafting runs unattended.]
```

**This is the last major decision point before
autonomous drafting begins.**

---

## Phase B: Blueprint (Interactive)

### Purpose

Lock the full chapter outline so Phase C can run without
further user input. The blueprint must define a genuine
STORY — with characters, a plot, and dramatic tension —
not a sequence of legal topics organized into chapters.

### Step B.0: Story spine.

Before outlining chapters, define the story spine. This
is the single most important step in the entire skill.
A novella without a story spine will read like a narrated
legal brief — which is the primary failure mode to avoid.

The story spine answers these questions:

1. **Who is the protagonist?** A specific person (composite
   or real) with a name, a life, a problem, and something
   at stake. Not "the appellant" — a person. What do they
   want? What are they afraid of? What do they not
   understand about their own situation?

2. **What is the inciting event?** The moment that sets the
   story in motion. An accident, a lawsuit filed, a ruling,
   a phone call, a letter — something concrete that happens
   and changes someone's life.

3. **What is the central dramatic question?** Not "what is
   the legal issue" — but what is the HUMAN question the
   reader needs to see answered? "Will Eddie ever be free
   of the app?" "Will the system acknowledge what it did?"
   "Will the judge see through the argument?"

4. **What is the plot arc?** Beginning (world before the
   conflict), middle (escalation, complications, failed
   attempts), end (confrontation, resolution or irresolution).
   The legal proceedings are PART of the plot, not THE plot.

5. **What is the emotional trajectory?** How does the reader
   feel at the beginning vs. the end? What shifts?

6. **Who are the supporting characters?** Each one must be
   a person with their own perspective, not a mouthpiece
   for a legal position. Even institutional actors (judges,
   opposing counsel, adjusters) have interior lives — they
   eat lunch, they worry about their kids, they have days
   where they doubt themselves.

7. **If observer frame mode:** Define the observer character
   with the same depth as the protagonist:
   - Name, occupation, relationship to the case
   - Why are they in a position to observe these events?
   - What is THEIR story? (The observer needs their own
     arc, even if it's simple — curiosity turning to
     understanding, detachment turning to concern,
     confusion turning to clarity.)
   - What do they know and not know? (The observer's
     limited perspective is a feature, not a bug — it
     creates natural dramatic tension when the reader
     realizes the observer doesn't have the full picture.)
   - How do they learn about case events? (Direct
     observation, conversations, reading documents,
     attending hearings, overhearing phone calls.)

   The observer is the FRAME. Their life, reactions, and
   atmospheric details are freely invented. The PAINTING
   — the case events they witness or learn about — must
   be faithful to the record.

   **The cinematic shift:** When the observer learns about
   a key event, the prose should shift from the observer's
   perspective into a close rendering of the actual scene.
   The reader is transported FROM the observer's living
   room TO the courtroom, the accident scene, the
   conference room where the decision was made. Then the
   prose pulls back to the observer. This prevents the
   story from becoming a secondhand retelling — the
   observer is the doorway, not the wall.

Present the story spine to the user as part of the
blueprint. Example format:

```
STORY SPINE:

Protagonist: [Name], a [description]. They want
[desire]. They're afraid of [fear]. The thing they
don't understand is [blind spot].

[If observer frame:]
Observer: [Name], a [role/relationship]. They
encounter the case through [how]. Their own arc:
[trajectory]. They know [X] but not [Y].
THE FRAME: [Name]'s life — invented, clearly
fictional. THE PAINTING: Everything [Name] sees
or learns about the case — grounded in the record.

Inciting event: [What happens to start the story.]

Central question: [The human question — not the
legal issue, but what the reader needs resolved.]

Plot arc:
  Beginning: [The world before]
  Complication: [What goes wrong, escalates]
  Confrontation: [The moment of truth]
  Resolution: [How it ends — or doesn't]

Emotional trajectory: The reader starts feeling
[X] and ends feeling [Y].

Supporting cast:
  [Name] — [role, personality, what they want]
  [Name] — [role, personality, what they want]
  [Name] — [role, personality, what they want]
```

### Step B.1: Chapter outline.

Based on the story spine AND the approved treatment,
produce a detailed outline. Each chapter must be a
SCENE in the story, not a topic:

For each chapter (10–14 for a full novella, 4–6 for a
short story):

- **Chapter number and title** (evocative, not descriptive
  — "SURGE" not "The Rideshare Industry")
- **POV character** (who are we inside?)
- **What happens** (a scene — something occurs, a decision
  is made, a conversation happens, a discovery is made.
  NOT "this chapter covers the standard of review.")
- **Where and when** (a specific physical setting — an
  office, a kitchen table, a courtroom hallway, a car)
- **Legal ideas embedded** (what doctrine or tension does
  the reader absorb through the scene — without being
  told about it directly?)
- **Oral-argument intuition trained** (what should the
  reader feel after this chapter?)
- **Connects to story spine** (how does this chapter
  advance the plot? What changes between the beginning
  and end of the chapter?)

**Chapter title test:** If the chapter title could be a
heading in a legal brief, it's wrong. "The Standard of
Review" is a brief heading. "The Morning After" is a
chapter title. "Vicarious Liability Analysis" is a brief
heading. "The Email Chain" is a chapter title.

**If observer frame mode:** For each chapter, additionally
note:
- **Frame or painting?** Is this chapter primarily in the
  observer's world (frame) or transported to a case event
  (painting)? Most chapters will have both — the observer
  provides the entry and exit, with the case scene in the
  middle.
- **How does the observer learn about this event?** (Direct
  witness, told by the client, reads a document, attends
  a hearing, overhears a conversation.)
- **What does the observer NOT know?** (Their incomplete
  picture creates tension and mirrors the reader's own
  process of coming to understand the case.)

### Step B.2: Guardrails.

Produce a **"Do Not Overstate" list** — specific doctrinal,
factual, and policy boundaries the drafting must respect:

- Settled law vs. contested law
- Record facts vs. inference
- Policy arguments vs. adjudicative facts
- Where composite characters diverge from real parties
- Any ethical or sensitivity considerations

**If observer frame mode, add Factual Fidelity Rules:**

```
FACTUAL FIDELITY RULES (observer frame):

THE FRAME (freely invented):
  • The observer character's life, job, home, routine
  • The observer's thoughts, feelings, reactions
  • Atmospheric details in the observer's scenes
    (weather, food, decor, what they're wearing)
  • Non-substantive dialogue (small talk, emotional
    reactions, logistical conversation)
  • How the observer learns about events (the
    specific phone call, the specific conversation)

THE PAINTING (must match the record):
  • All case events, timeline, and procedural history
  • What parties actually said (testimony, statements)
  • What documents say (rulings, orders, filings)
  • Legal holdings, standards, and statutory text
  • Which arguments were made and how the court ruled
  • Any detail that could come up at oral argument

THE BORDER (use with care):
  • Reasonable inferences from the record (flag in
    continuity log)
  • The emotional state of real parties (can be
    inferred from testimony/behavior but not invented
    wholesale)
  • Dialogue that closely paraphrases record testimony
    (acceptable if clearly sourced from the record)
  • Institutional atmosphere (what a courtroom or
    office generally feels like — not case-specific
    invented detail)

RULE: If you would hesitate to assert a detail at
oral argument, it belongs in the frame, not the
painting.
```

### Step B.3: User approval.

```
Here is the full blueprint. Once you approve, Phase C
will draft all chapters autonomously — no further input
needed until the finished novella is ready.

Please review:
- Chapter outline: [X] chapters
- Voice: [primary] with [secondary] influence
- Story type: [selected type]
- Guardrails: [summary]

Approve the blueprint?
  1. Approved — start drafting
  2. Adjust (tell me what to change)
  3. Let me think — I'll come back to this

[Step 6 of 6 — THIS IS YOUR LAST DECISION. Once you
approve, you are free to walk away. I'll draft all
chapters and assemble the finished .docx without any
further input. Come back when you're ready to review
the completed novella.]
```

If the user approves, provide the **parallel tab prompt**:

```
Blueprint approved. You're done — no more input needed.

I'll now draft all [X] chapters and assemble the
finished .docx. This will take approximately 30–45
minutes. You can:

  • Stay and watch the chapters come in
  • Walk away and come back when it's done
  • Start this in a parallel Chat tab (paste the
    prompt below) and keep working here

If you want to run this in a parallel tab, paste this:

---

I have an approved blueprint for the [CASE NAME]
case novella. The blueprint was approved in another
session. Here it is:

[PASTE FULL BLUEPRINT — Claude includes the complete
blueprint text here so the user can copy it]

Please draft all chapters per this blueprint. Use
the [VOICE] style. Draft in batches of 2–3 chapters,
maintaining a continuity log between batches. When
all chapters are complete, assemble into a .docx
and extract the oral-argument themes appendix.

---

Or if you want to continue drafting in this session,
just say "start drafting."
```

---

## Phase C: Drafting (Autonomous)

### Purpose

Draft all chapters per the approved blueprint. This phase
is designed to run without user interaction.

### Execution

**Step C.1: Load required context.**

Read the docx skill at `/mnt/skills/public/docx/SKILL.md`
before producing any document.

Read `references/style-palette.md` for the selected author
voice profile and drafting constraints.

**Step C.2: Draft in batches.**

Draft 2–3 chapters per turn. For each batch:

1. Write the full chapter text as SCENES, not summaries.
2. Maintain the selected author voice consistently.
3. At the end of each batch, produce a **continuity note**:
   - Characters introduced so far
   - Timeline position
   - Plot threads opened and their status
   - Any assumptions made
   - Setup planted for future chapters

4. Immediately continue to the next batch — do not wait
   for user input. Simply proceed to the next 2–3 chapters.

**Step C.3: What "writing a scene" means.**

This is the most critical instruction in the entire skill.
The output must read like fiction, not like a narrated legal
brief. Every chapter must be a SCENE — something happening
in a specific place, at a specific time, to a specific
person.

A scene has ALL of these elements:

- **A physical setting.** Not "the courtroom" — describe
  the room. The fluorescent light. The court reporter's
  fingers. The water pitcher with a crack in the lid.
  Ground the reader in a PLACE.

- **A character who wants something.** In this scene, what
  does the POV character want? To win a motion? To get
  through the day? To understand why this is happening?
  To convince someone? Every scene has a character with
  a desire.

- **Action and dialogue.** People talk to each other. They
  make phone calls. They read documents and react. They
  drive to work and think. Things HAPPEN. A scene is not
  a description of a legal issue — it is a sequence of
  events that the reader experiences in real time.

- **Interior life.** What is the character thinking? Not
  "she considered the standard of review" — what is she
  FEELING? Frustrated that the judge didn't read the
  brief? Worried about the client? Annoyed that opposing
  counsel is late? The character's inner monologue should
  sound like a person, not a treatise.

- **Sensory detail.** What does the character see, hear,
  smell, touch? The hum of the HVAC. The coffee going
  cold. The weight of the record binder. These details
  make the scene real and — critically — make the legal
  content memorable because the reader's brain encodes
  it alongside sensory experience.

- **Something changes.** By the end of the scene, something
  is different. The character learned something, decided
  something, lost something, understood something. If
  nothing changes, it's not a scene — it's exposition.

**The legal content enters through the scene, not despite
it.** The reader learns about the standard of review because
they watch a law clerk explain it to the justice over lunch.
They understand the preservation problem because they see the
trial attorney hesitate before objecting and then decide not
to. They feel the weight of the statute because a character
reads it at their kitchen table and realizes what it means
for their case.

**WRONG — narrated legal analysis disguised as a chapter:**

"The central issue in the case was whether the trial
court had applied the correct standard. Under California
law, the abuse of discretion standard applies to
evidentiary rulings, while questions of law are reviewed
de novo. The appellant argued that the trial court's
interpretation of the statute was a legal question
subject to independent review. The respondent countered
that the trial court's ruling involved a factual
determination entitled to deference."

This is a legal brief with the citations removed. It has
no characters, no setting, no action, no dialogue, no
interior life. The reader learns nothing they wouldn't
learn faster by reading the actual brief.

**RIGHT — a scene that teaches the same legal content:**

A law clerk sits in her office at 7 AM, reading our
brief with a highlighter. She pauses at the standard-of-
review section. She pulls up the statute on her screen
and reads it twice. She walks down the hall to the
justice's chambers. "I think they're right that this is
de novo," she says. The justice looks up from his coffee.
"Why?" She explains. He pushes back. They argue about it
for five minutes, and the justice finally says, "Write me
a memo on it — but I think the trial court got too
comfortable with its own reading." The clerk walks back
to her office thinking: this is closer than either side
knows.

The reader just learned the standard-of-review issue,
the competing positions, and the court's likely
temperature — and they'll REMEMBER it because they
experienced it as a scene with people in it.

**Step C.4: Quality standards during drafting.**

- **Ground everything in case materials.** Do not invent
  legal holdings, statutes, or procedural events.
- **Distinguish record fact from inference.** If the prose
  relies on likely inference rather than express record
  support, note it in the continuity log.
- **Respect the "Do Not Overstate" guardrails** from the
  blueprint.
- **Follow the story spine.** Every chapter must advance
  the plot. If a chapter doesn't move the story forward,
  it doesn't belong — even if it covers an important
  legal issue. Find a way to embed the legal issue in a
  scene that ALSO advances the plot.
- **Avoid failure modes:**
  - **THE NARRATED BRIEF** — This is the primary failure
    mode. If a paragraph could appear in a legal brief
    with citations added, it is not fiction. Rewrite it
    as a scene with characters, setting, and action.
  - **The topic-organized chapter** — If a chapter is
    organized around a legal topic rather than a scene,
    it will read like a brief section. Reorganize around
    what HAPPENS, not what the legal issue IS.
  - **Characters as mouthpieces** — If a character exists
    only to articulate a legal position, they are not a
    character. Give them a life outside the legal issue.
  - **Summary narration** — "Over the next several weeks,
    the parties briefed the motion..." is summary. Show
    ONE specific moment from those weeks in real time.
  - Turning the work into a law-school lecture
  - Overstating unsettled doctrine
  - Treating jury instructions or committee comments as
    binding law
  - Presenting campaign rhetoric or policy inference as
    adjudicative fact
  - Writing cartoon villains instead of institutional actors
  - Losing the author voice mid-draft

- **The core principle:** Do not treat the story as a vehicle
  for "explaining the law." Treat it as a vehicle for making
  the reader feel why one legal framing is natural and the
  competing framing is strained.

- **The scene test:** Before finalizing each chapter, ask:
  "Could I close my eyes and SEE this chapter happening?
  Do I know what room we're in? Can I hear the characters
  talking? Does something happen?" If the answer to any of
  these is no, the chapter needs rewriting.

**Step C.5: Observer frame transitions (if applicable).**

When the narrator mode is observer frame, the drafting must
handle transitions between the frame (observer's world) and
the painting (case events) with care. This is what prevents
the story from becoming secondhand reportage.

**The cinematic shift pattern:**

1. **FRAME:** The observer is in their world — at a kitchen
   table, in a courthouse hallway, on a phone call. They
   encounter a case event through their own experience
   (reading a document, being told about something,
   attending a hearing, overhearing a conversation).

2. **TRANSITION:** A white space, a section break, or a
   prose shift. The observer's setting dissolves. The
   tense may shift. The sensory details change. The
   reader is no longer with the observer.

3. **PAINTING:** The reader is INSIDE the actual case event,
   experiencing it in real time — the courtroom, the
   accident scene, the conference room, the phone call.
   This is written in full scenic mode with setting,
   dialogue, action, sensory detail. All factual content
   in these passages must be faithful to the record.

4. **RETURN:** The prose pulls back to the observer. They
   react, reflect, misunderstand, or connect this event
   to something else they know. The reader processes the
   case event through the observer's lens.

**Example:**

   Rosa sat at the kitchen table with the deposition
   transcript open in front of her. It was 342 pages.
   She had made it to page 58. Her coffee was cold.
   She turned the page and stopped.

   —

   The conference room was too warm. The court reporter's
   machine made a soft clicking that no one else seemed
   to hear. Judy Peck sat with her hands flat on the
   table, answering questions in a voice that did not
   waver...

   [full scenic rendering of the deposition — grounded
   in the record]

   —

   Rosa closed the transcript and pressed her palms
   against her eyes. She had not expected it to feel
   like that — like being in the room.

**Rules for the cinematic shift:**
- The frame passages can be freely invented (Rosa's
  kitchen, her coffee, her reaction).
- The painting passages must be faithful to the record
  (what was said in the deposition, how the hearing
  went, what the ruling stated).
- The transition should feel natural, not mechanical.
  Vary the technique — sometimes use white space,
  sometimes let the prose flow from one setting to
  another, sometimes use the observer falling asleep
  or remembering or imagining.
- Not every chapter needs the full shift. Some chapters
  can stay entirely in the frame (the observer's own
  life) or entirely in the painting (a courtroom scene
  the observer attended in person). The shift is a tool,
  not a formula.

**Step C.6: Chapter target lengths.**

- Full novella: 1,500–2,500 words per chapter
- Short story: 1,500–2,000 words per chapter
- Final chapter may run longer to resolve threads

---

## Phase D: Assembly & Debrief (Minimal Interaction)

### Purpose

Compile the drafted chapters into a finished .docx, and
extract an appendix of oral-argument preparation themes.

### Step D.1: Assemble the document.

Read `/mnt/skills/public/docx/SKILL.md` for production
instructions. Create a new .docx (do NOT use the KLG Case
Memo template — the novella has its own format).

**Document structure:**

```
TITLE PAGE
  [Title]
  A Novella (Draft)
  Based on [Case Name] ([Case No.])
  Prepared for oral argument preparation
  [Date]
  CONFIDENTIAL — ATTORNEY WORK PRODUCT

[blank page]

TABLE OF CONTENTS

CHAPTER 1 — [TITLE]
  [POV character notation in italics]
  [Chapter text]

[... remaining chapters ...]

APPENDIX: ORAL-ARGUMENT THEMES & SOUNDBITES
  [Extracted themes, metaphors, and soundbites]

CONTINUITY & SOURCE NOTES
  [Consolidated continuity log]
  [Record/authority grounding notes]
```

**Formatting:**

- Font: Century Schoolbook, 12pt body text
- Chapter titles: 14pt bold
- POV markers: italic, in parentheses
- Generous margins for reading comfort
- Page numbers in footer
- Single spacing with space between paragraphs

### Step D.2: Extract argument themes.

After assembly, produce an **Oral-Argument Themes Appendix**
at the end of the document:

1. **Key metaphors and images** — vivid phrasings from the
   narrative that could translate to oral argument
2. **Soundbites** — one-sentence formulations that capture
   the core of each legal issue
3. **Emotional anchors** — scenes or images that make the
   legal position feel inevitable
4. **Counterargument inoculation** — moments where the story
   surfaced the opponent's strongest point and showed why
   it fails
5. **Themes by chapter** — quick-reference index of which
   legal issues are dramatized where

### Step D.3: Produce PDF (if requested).

If the user requested PDF output (for Speechify or other
audiobook services), convert the .docx to PDF:

```bash
python /mnt/skills/public/docx/scripts/office/soffice.py \
  --headless --convert-to pdf novella.docx
```

### Step D.4: Deliver and offer Notion posting.

Present the finished files and offer:

```
The novella is ready:
- [Title].docx — [X] chapters, approximately [Y] words
- [Title].pdf (if produced)

Would you like me to:
1. Post a link to the matter's Notion page
2. Post a notification to the matter's Slack channel
3. Both
4. Neither — I'll handle distribution
```

---

## Cross-Reference: Oral Argument Skill

The `klg-oral-argument` skill should offer the novella as an
optional add-on after completing any phase. Add this prompt
at the end of Phase D (murder board) or after any phase
completion:

```
Would you also like to build a narrative preparation piece
for this case? A quasi-fictionalized novella that helps you
absorb and visualize the key facts, legal concepts, and
policy tensions through story.

Say "build a case novella" to start. This runs in a
parallel tab — it won't interrupt your current work.
```

The novella skill can also run independently at any stage
of a matter — during briefing, after research compilation,
or even during case assessment when the attorney wants to
internalize a complex case early.

---

## Pipeline Position

- **Before this skill:** Any stage — case assessment, research,
  briefing, or oral argument prep can feed this skill
- **After this skill:** Oral argument (the novella is a
  preparation tool, not a filing)
- **Phase badge:** Argument (when paired with oral argument
  prep) or Research (when used standalone for case absorption)
- **Skill Navigator icon:** 📖

---

## Execution Rules

1. Read all Required Context files before starting.
2. Maintain strict fidelity to case materials. Never invent
   holdings, statutes, or record facts.
3. The interactive phases (A and B) are the ONLY phases that
   require user input. Design all decisions to be resolved
   before Phase C begins.
4. Phase C should auto-continue between chapter batches
   without waiting for user prompts.
5. The .docx is a narrative document, NOT a case memo.
   Do not use the KLG Case Memo template. Create a fresh
   document styled for reading.
6. When producing .docx, follow the docx skill instructions
   at `/mnt/skills/public/docx/SKILL.md`.
7. Session logging (Pattern 3) is handled globally per
   `claude.md`. Append the per-response logging prompt
   after substantive responses in Phases A and B.
   Phase C logs only at the end when drafting is complete.
8. All composite characters must be clearly fictional.
   Do not use real names of parties, witnesses, or judges
   unless the user expressly requests it and the materials
   are attorney work product.
9. Include the CONFIDENTIAL — ATTORNEY WORK PRODUCT
   designation on the title page.
