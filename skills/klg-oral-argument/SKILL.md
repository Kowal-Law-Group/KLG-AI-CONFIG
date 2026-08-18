---
name: klg-oral-argument
description: "Prepare for appellate oral argument with panel intelligence, strategic argument mapping, NotebookLM audio prompts, and interactive murder board drill. Use whenever the user says 'oral argument prep', 'prepare for oral argument', 'argument prep', 'murder board', 'moot court', 'hot bench', 'panel prep', 'get ready for argument', 'oral argument is coming up', 'we have argument scheduled', 'prep me for argument', 'who is on the panel', 'research the panel', 'generate NotebookLM prompts', 'notebook prompts for argument', or references upcoming oral argument in any appellate matter. Also triggers when user says 'drill me', 'practice argument', 'run me through questions', or 'what will the panel ask'. Covers four phases: panel research, strategic outline, NotebookLM prompt generation, and interactive drill. NOT for brief drafting (use klg-brief-elevation), case assessment, or research compilation."
---

# KLG Oral Argument Prep

## Purpose

Prepare the attorney for appellate oral argument through a
comprehensive four-phase workflow: panel intelligence research,
strategic argument mapping, NotebookLM audio session prompt
generation, and interactive murder board drill. The skill
ensures the attorney walks into the courtroom having internalized
the case narrative, stress-tested every argument, anticipated
hostile questions, and confirmed that all procedural and
jurisdictional prerequisites are solid.

This is the final skill in the KLG pipeline — it runs after
the brief is filed and argument is scheduled.

## Required Context

Before beginning any phase, read these project files:

1. `/mnt/project/claude.md` — Citation standards, output rules,
   quality controls
2. `references/workflow-patterns.md` — Session logging (Pattern 3)
3. `references/argument-map-framework.md` — Argument inventory
   structure, procedural gauntlet checklist, zinger categories
4. `references/notebooklm-prompts.md` — Five NotebookLM prompt
   templates and customization instructions

Do not skip these reads. The quality of the preparation depends
on having these standards loaded.

## Required Inputs

- Our brief (the filed version — AOB, RB, ARB, or writ petition)
- The opposing brief(s)
- Panel information: court, division/circuit, and/or individual
  justice/judge names

## Helpful But Not Required

- Case assessment memo
- Response plan memo
- Research compilation memo
- Key orders/rulings being challenged
- Record excerpts (especially any referenced in the briefs)
- Prior oral argument notes or strategy memos

## Phase Overview

The skill has four phases. They are designed to be run
sequentially (A → B → C → D), but the user can enter at
any phase or skip phases:

- **Phase A: Panel Intelligence Briefing** — Research the panel
- **Phase B: Strategic Outline & Argument Map** — Map all
  arguments, vulnerabilities, themes, and procedural issues
- **Phase C: NotebookLM Prompt Generation** — Generate five
  tailored audio session prompts
- **Phase D: Murder Board Drill** — Interactive oral argument
  exercise

## Notion Page Structure

When creating the oral argument Notion page (the default
deliverable for Phases A, B, and C), follow this structure:

### Table of Contents

Always include a table of contents at the top of the page
so the user can jump to any section. Use Notion's heading
structure with clear, descriptive headings for each section
and phase. The TOC should list all major sections:

```
# Table of Contents
- Panel Intelligence Memo (Phase A)
- Strategic Outline & Argument Map (Phase B)
  - Case Posture & Relief
  - Argument Inventory (Offense)
  - Vulnerability Inventory (Defense)
  - Best and Worst Case Scenarios
  - Theme Analysis
  - Procedural Gauntlet
  - Zinger Anticipation
  - Concessions & Landmines
  - Close-Out Toolkit
- NotebookLM Prompts (Phase C)
  - Prompt 1: Our Strongest Case
  - Prompt 2: The 30,000-Foot View
  - Prompt 3: The Hot Bench
  - Prompt 4: The Other Side's War Room
  - Prompt 5: The Procedural Gauntlet
```

Update the TOC as each phase is completed and posted.

### SharePoint Brief Links

Near the top of the Notion page (below the TOC), include
a "Source Documents" section with direct SharePoint URLs
to the briefs and key filings. Use the Microsoft 365
`sharepoint_search` tool to locate the briefs by filename
and matter folder. Search for the case name or party names
plus "brief" or "petition" within the matter folder.

Format the section as:

```
## Source Documents
- Our Brief: [filename] — [SharePoint URL]
- Opposing Brief: [filename] — [SharePoint URL]
- Key Order/Ruling: [filename] — [SharePoint URL]
```

If SharePoint search does not return results (e.g., the
briefs have not been filed to SharePoint yet, or the
filenames are non-obvious), note which documents are
missing and ask the user to provide the SharePoint paths
or confirm the filenames.

---

## Mode Selection

Before starting, present the mode selection prompt:

```
Before we start oral argument prep, how would you like
to run this?

CHAT (recommended for most phases):
  ✓ Runs in a tab — you can keep working in parallel.
  ✓ Phases A, C, and D are inherently Chat-native (web
    search, prompt generation, and interactive drill).
  ✗ You'll need to upload: our brief, the opposing brief,
    and any case assessment/response plan memos.

COWORK:
  ✓ I can pull briefs and memos directly from the matter
    folder — no uploads needed.
  ✓ Best for Phase B if you want me to cross-check record
    citations and pull in additional context.
  ✗ Ties up Cowork for the duration.

Which do you prefer?
```

**Exception:** Skip this prompt if the user has already uploaded
documents in Chat or is clearly in Cowork with the matter folder.

---

## Phase A: Panel Intelligence Briefing

### Purpose

Research the appellate panel to understand what types of
arguments, framing, and tone will be most effective with
these specific judges.

### Execution

**Step A.1: Gather panel information.**

Ask the user (if not already provided):

```
Who is on the panel? Please provide:
- Court and division/circuit (e.g., Second District,
  Division 4; or Ninth Circuit)
- Individual justice/judge names if known
- Argument date if scheduled
```

**Step A.2: Default research (Claude via web search).**

For each justice/judge, use web search to research:

1. Judicial philosophy and writing tendencies
2. Published opinions on topics similar to the issues in
   this case (standards of review, procedural fairness,
   statutory interpretation, etc.)
3. Patterns in how they respond to record-based arguments
   vs. rhetorical/policy arguments
4. Preferred persuasion styles — textual precision,
   institutional legitimacy, judicial restraint, pragmatic
   balancing
5. Recurring patterns in majority vs. dissenting opinions
6. Any known hot-button issues or pet peeves

Synthesize into a **Panel Intelligence Memo** with these
sections:
- One-paragraph profile of each justice/judge
- Arguments this panel tends to find persuasive
- Arguments they tend to distrust or push back on
- Rhetorical techniques and framing that resonate
- Tactical recommendations for oral argument — what to
  emphasize, what to avoid, how to structure responses

**Step A.3: Offer Deep Panel Research upgrade.**

After delivering the default research, offer:

```
This covers the publicly available basics. Would you like
a deeper research cycle?

DEEP PANEL RESEARCH (optional):
  I'll generate a Deep Research prompt focused on this
  panel's past decisions on topics directly relevant to
  your case — [list 2-3 specific topics from the briefs].
  This goes to Notion for Comet to execute via ChatGPT
  Deep Research, and produces a more thorough profile.

  ✓ Catches patterns in unpublished opinions
  ✓ Finds how these judges have handled your specific
    legal issues before
  ✗ Adds a research cycle (Comet turnaround time)

Do you want the deep research prompt, or is the current
briefing sufficient?
```

If the user wants Deep Panel Research, generate a prompt
following the format in references/notebooklm-prompts.md
(Section: Deep Research Panel Prompt) and post it to Notion.

**Step A.4: Deliver.**

Post the Panel Intelligence Memo to the Notion page for
this matter. If the user also wants a .docx, produce one.

---

## Phase B: Strategic Outline & Argument Map

### Purpose

Produce a comprehensive argument map covering offense,
defense, themes, procedural posture, and anticipated
questions — the full strategic picture for oral argument.

### Execution

**Step B.1: Ingest all materials.**

Read and analyze:
- Our brief (the filed version)
- The opposing brief(s)
- Case assessment and/or response plan (if available)
- Panel Intelligence Memo from Phase A (if completed)
- Any additional record excerpts or orders provided

**Step B.2: Identify themes.**

Before generating the outline, identify:

1. **Themes from our briefs** — narrative threads, recurring
   framings, and rhetorical motifs already developed in the
   briefing
2. **Themes Claude proposes** — additional framings suggested
   by the argument map, panel intel, or policy implications
3. **Ask the user:**

```
I've identified these themes from the briefing:
[list themes found]

I'd also suggest considering:
[list proposed themes]

Are there themes you have in mind that should be
stress-tested during argument prep?
```

**Step B.3: Generate the Strategic Outline.**

Produce the full argument map following the structure in
`references/argument-map-framework.md`. The outline has
these sections:

1. **Case Posture & Relief** — single-sentence "why we win,"
   specific relief sought, procedural posture
2. **Argument Inventory (Offense)** — our strongest legal
   arguments, equitable arguments, most compelling remedies,
   and strongest theme/narrative — with authorities
3. **Vulnerability Inventory (Defense)** — our biggest legal
   weakness, other side's best equities, remedy problems,
   and their strongest theme/narrative — with authorities
4. **Best and Worst Case Scenarios** — full win, full loss,
   and most likely outcome
5. **Theme Analysis** — themes from briefs, proposed themes,
   user themes, stress-tested
6. **Procedural Gauntlet** — appealability, timeliness,
   preservation/forfeiture for each issue, standing/mootness,
   sua sponte concerns
7. **Zinger Anticipation** — questions beyond what the briefs
   address, from uncited authority, internal tensions, policy
   consequences, adverse record facts, workability concerns
8. **Concessions & Landmines** — safe concessions, dangerous
   topics, safe routes
9. **Close-Out Toolkit** — three likely opening questions,
   three crisp answers, 20-second closing

**Step B.4: Fresh-authority scan.**

California's rule 8.254 letter of additional authority requires
the authority be genuinely new — unlike federal practice, where
any additional authority can be lodged regardless of age. Missing
that distinction cost a real argument: at Palmieri v. Foondos
(Third District, June 15, 2026), a Rule 8.254 letter was denied
because the cited authority wasn't new, while a March 2026 opinion
on point that would have qualified went unsurfaced.

For each issue in the Argument Inventory and Vulnerability
Inventory (Step B.3), run a targeted search for authority decided
in the last 6–12 months on that issue. For anything genuinely new:

1. Flag it in the argument map under the relevant issue, noting
   why it's new (decision date) and what it adds.
2. Draft a Rule 8.254 letter of additional authority for
   attorney review — do not file anything; this is a draft only.
3. If a candidate authority isn't clearly new, say so rather than
   drafting a letter that risks the same denial as Palmieri —
   flag it as "found but not clearly within the new-authority
   window" and let the attorney decide.

Confirm with the attorney whether an 8.254 letter is proper here
before drafting one — the new-authority requirement is California
practice; don't assume it carries over from a federal-court habit.

**Step B.5: Deliver.**

Default deliverable is a Notion page. Before posting, ask:

```
The argument map is ready. How would you like it delivered?

1. **Notion page** (default) — I'll post it to the
   Research database linked to [case name].

2. **Notion page + Word memo** — I'll post to Notion and
   also produce a .docx. Should the .docx be:
   a. Standalone memo
   b. Appended to the existing case memo

Which do you prefer?
```

If the user wants a .docx, produce it using the KLG Case
Memo template following the clone-and-edit workflow from
the docx skill. Follow Pattern 1 (Iterative Case Memo) in
`references/workflow-patterns.md` if appending.

---

## Phase C: NotebookLM Prompt Generation

### Purpose

Generate five tailored NotebookLM prompts, each producing
a distinct audio session that approaches oral argument prep
from a different angle.

### Execution

**Step C.1: Generate the five prompts.**

Read `references/notebooklm-prompts.md` for the full
template of each prompt, including the recommended
NotebookLM settings (Format, Length, Language) for each.
Customize each prompt with:

- Case name, parties, and case number
- Specific issues, arguments, and authorities from the
  argument map (Phase B)
- Themes identified in Phase B
- Panel intelligence from Phase A (especially for Prompt 3)
- Record citations where relevant
- Any user-specified themes or concerns

The five prompts are:

**Prompt 1 — "Our Strongest Case" (The Narrative Session)**
Two speakers: Lead Counsel and Strategic Advisor. Distills
our strongest legal arguments, strongest facts, strongest
equities, woven into our most compelling framing and case
narrative. No devil's advocate — pure persuasive synthesis.
The session to internalize our story.

**Prompt 2 — "The 30,000-Foot View" (Advocate vs. Skeptic)**
Two speakers: Advocate (favorable) and Skeptic (probing).
Balanced overview of the big-picture narrative, strongest
arguments on each side, policy angles, concessions, and
the close-out toolkit.

**Prompt 3 — "The Hot Bench" (Judicial Conference)**
Two speakers: both playing appellate judges calibrated to
the actual panel (using Phase A intel). They discuss the
case as if in a pre-argument conference — concerns,
planned questions, leanings.

**Prompt 4 — "The Other Side's War Room" (Opposing Counsel)**
Two speakers: opposing counsel and their strategist. How
they would prepare, their best pitch, where they think
we're vulnerable, questions they hope the court asks us.

**Prompt 5 — "The Procedural Gauntlet"**
Two speakers: a procedural hawk and an advocate trying to
get past threshold issues to the merits. Stress-tests
appealability, timeliness, preservation, forfeiture,
standing, and mootness.

**Step C.2: Package on the Notion page.**

Post all five prompts to the Notion page with:
- Clear labels and one-sentence descriptions
- Recommended listening order
- **NotebookLM settings per prompt** — Format (Deep Dive,
  Debate, or Critique), Length (Long or Default), and
  Language (English). See the settings table in
  `references/notebooklm-prompts.md`.
- **Per-prompt source document instructions** — for each
  prompt, specify exactly which documents to upload to
  that NotebookLM session:

  **Prompt 1 ("Our Strongest Case"):**
  Sources: Our brief only. Optionally add the case
  assessment memo if available. Do NOT include opposing
  briefs — this session is pure advocacy.

  **Prompt 2 ("The 30,000-Foot View"):**
  Sources: Our brief AND the opposing brief(s). Optionally
  add key orders/rulings. Do NOT include the full record
  (reporter's transcript, appendix volumes) — the briefs
  contain the relevant record citations and this session
  focuses on the legal arguments, not granular record facts.

  **Prompt 3 ("The Hot Bench"):**
  Sources: Our brief, opposing brief(s), AND the Panel
  Intelligence Memo from Phase A (paste key excerpts into
  the prompt if NotebookLM cannot accept it as a separate
  source). Do NOT include the full record.

  **Prompt 4 ("The Other Side's War Room"):**
  Sources: Opposing brief(s) AND our brief. Both sides'
  briefs are needed so opposing counsel can identify our
  vulnerabilities. Do NOT include the full record.

  **Prompt 5 ("The Procedural Gauntlet"):**
  Sources: Our brief, opposing brief(s), the notice of
  appeal, and key procedural filings (e.g., the order
  being challenged, any tolling motions, any motions to
  dismiss the appeal). Include relevant portions of the
  reporter's transcript ONLY if preservation of issues
  is contested and the transcript contains the relevant
  objections or colloquy. Include relevant appendix
  excerpts ONLY if appealability turns on the specific
  content of the order or judgment. In most cases, the
  briefs and procedural filings are sufficient.

  **General guidance for NotebookLM sources:**
  - Briefs are always included (they contain record cites
    and legal authorities).
  - The full reporter's transcript and appendix volumes
    are generally NOT needed — they are too large for
    NotebookLM to process effectively and the briefs
    already distill the relevant portions.
  - Exception: If a specific factual dispute is central
    to the case and the transcript/appendix pages are
    critical to understanding it, include only the
    relevant excerpt (not the entire volume).
  - Always note the SharePoint URLs (from the Source
    Documents section) so the person setting up the
    sessions knows where to find each file.

**Step C.3: Send Slack notification to the matter channel.**

Send a Slack message to the **matter channel** tagging
William Hernandez (Slack user ID: `U097FMSH3V4`),
notifying him that the NotebookLM prompts are ready and
need to be set up as audio sessions.

**Finding the matter channel:** Use `slack_search_channels`
to search for the matter name or client name (e.g., search
"Palmieri" to find `#palmieri`). Matter channels are named
in lowercase after the matter or client name. Search both
public and private channels (`channel_types:
"public_channel,private_channel"`).

If no matter channel exists, fall back to sending a DM
to William using his user ID as the channel_id.

Before sending, confirm with the user:

```
I'll post to the #[matter-name] channel tagging William
with the Notion page URL and instructions to create the
five NotebookLM audio sessions. Should I:

1. Post to #[matter-name] tagging William (default)
2. Post to a different channel or person (tell me which)
3. Skip the Slack message — I'll handle it myself
```

Unless the user says to skip, compose and send the Slack
message following the Slack posting rules in
`/mnt/project/claude.md`:

- Begin with "This is Claude posting on Tim's behalf."
- Tag William with `<@U097FMSH3V4>` (or the alternate
  user's Slack ID if redirected)
- Paste bare Notion page URL (no angle brackets, no
  markdown link syntax)
- Include these instructions in the message:

```
This is Claude posting on Tim's behalf.

<@U097FMSH3V4> — The oral argument prep for [CASE NAME]
is ready. Please create the five NotebookLM audio
sessions from the prompts on this Notion page:

[NOTION PAGE URL]

The page has everything you need:
- Five prompts (each in a code block — copy into the
  "What should the AI hosts focus on?" field)
- NotebookLM settings for each prompt (Format, Length)
- Source documents to upload for each session (with
  SharePoint download links)
- Recommended listening order

Please create each session in a shared NotebookLM space
so Tim can access them. One notebook per prompt. Thanks!
```

If the user redirects to someone other than William, use
`slack_search_users` to find that person's Slack user ID
and tag them instead.

---

## Phase D: Murder Board Drill (Interactive)

### Purpose

Live back-and-forth oral argument exercise simulating an
appellate bench, calibrated to the actual panel.

### Execution

**Step D.1: Set up the drill.**

```
Ready for the murder board drill. Here's how it works:

I'll play the bench — asking one question at a time,
alternating between sympathetic and skeptical tones.
Questions will be calibrated to [panel names if known].

After each of your answers, I'll:
• Rate your response (e.g., 7/10)
• Note what worked well
• Suggest authorities, framing, or points to add
• Then move to the next question

I'll draw from the argument map, zinger list, and
procedural gauntlet. Expect questions on:
- Your lead argument and rule articulation
- Record support and factual disputes
- Remedy — what exactly you're asking for
- Concessions — what you're prepared to give up
- Policy consequences of the rule you want
- Procedural threshold issues

We'll end with a refreshed close-out toolkit.

Ready? Let's begin.
```

**Step D.2: Conduct the drill.**

Ask one question at a time. After each user response:

1. **Rate** the answer briefly (e.g., "7/10 — solid on the
   rule, but the remedy ask needs to be crisper")
2. **What worked** — specific strengths
3. **What to add** — authorities, framing, factual support,
   or record cites that would strengthen the answer
4. **Follow-up or next question** — if the answer was weak,
   press harder before moving on

Throughout the drill:
- Alternate sympathetic and skeptical tones
- Push on concessions — "What are you prepared to concede?"
- Test remedy articulation — "What exactly are you asking
  this court to do?"
- Probe rule workability — "How would your rule apply in
  [hypothetical]?"
- Mix in procedural questions — "Counsel, was this issue
  preserved below?"
- Occasionally ask the attorney to restate the issue in
  one sentence
- Draw on the zinger anticipation and procedural gauntlet
  from Phase B
- If Phase A was completed, calibrate questioning style
  to the actual panel

**Step D.3: Close out.**

After 15–20 questions (or when the user is ready to wrap),
produce a refreshed close-out toolkit:

1. Three most likely opening questions (refined based on
   drill performance)
2. Three crisp one-sentence answers
3. A 20-second closing statement linking the standard of
   review, the clean rule, and why the relief is correct
4. Key takeaways — what improved during the drill, what
   still needs work

**Step D.4: Log the session.**

The murder board session should be logged to Notion per
Pattern 3 in `references/workflow-patterns.md`. The
transcript summary is especially valuable here — it
captures refined answers and coaching notes.

**Step D.5: Offer the Case Novella.**

After the murder board drill (or after completing any
phase, if the user indicates they are done with oral
argument prep for now), offer the narrative add-on:

```
One more option: would you like to build a case novella
for this matter?

This is a quasi-fictionalized short story based on the
case — a narrative preparation piece that helps you
absorb and visualize the key facts, legal concepts, and
policy tensions through story. The finished product is
a .docx you can read or convert to audiobook via
Speechify.

The interactive part takes about 25 minutes (choosing
the story type, author voice, and approving the chapter
blueprint). After that, drafting runs autonomously in a
parallel Chat tab — no babysitting needed.

Say "build a case novella" to start, or skip this for now.
```

Do NOT push the novella if the user is under time pressure
or has indicated they just want to drill. Offer it once;
if declined, do not re-offer in this session.

---

## Entry Points and Phase Independence

The user does not have to run all four phases sequentially.
Common entry patterns:

- **Full prep:** A → B → C → D (recommended)
- **Quick drill:** D only (user already knows the case cold,
  just wants to practice)
- **Panel research only:** A only (argument is months away,
  just want early intel)
- **Audio prep only:** C (user has done their own outline,
  just wants NotebookLM prompts)
- **Argument map + drill:** B → D (skip panel research and
  audio, focus on substance)

When the user enters at a phase other than A, ask for any
missing context that phase needs (e.g., Phase D without
Phase B means Claude needs the briefs to generate questions).

---

## Pipeline Position

- **Before this skill:** Brief Elevation → Brief Assembly →
  Cite Check → Style Guide Check → Appendix Cites →
  Brief filed
- **After this skill:** Case Novella (optional narrative
  preparation), then the oral argument itself
- **Phase badge:** Argument
- **Skill Navigator icon:** 🎤

---

## Execution Rules

1. Read all Required Context files before starting any phase.
2. Follow citation standards from `/mnt/project/claude.md`
   in all written deliverables.
3. Default deliverable format is Notion page. Always ask
   whether the user also wants a .docx (standalone or
   appended to case memo).
4. When producing .docx memos, use the KLG Case Memo
   template via the clone-and-edit workflow (unpack → edit
   XML → repack with `--original`). Read the docx skill
   at `/mnt/skills/public/docx/SKILL.md` before producing.
5. For Slack messages, follow the Slack posting rules in
   `/mnt/project/claude.md`.
6. Session logging (Pattern 3) is handled globally per
   `claude.md`. Append the per-response logging prompt
   after each substantive response.
7. After producing the Phase B argument map deliverable,
   follow Pattern 1 (Iterative Case Memo) and Pattern 2
   (Client Memo) from `references/workflow-patterns.md`
   if the user requested a .docx.
