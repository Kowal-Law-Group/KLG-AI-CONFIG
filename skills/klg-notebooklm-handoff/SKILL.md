---
name: klg-notebooklm-handoff
description: "Generate a NotebookLM handoff page in Notion with source upload checklist, prompt queue, and Comet automation block for evidence intelligence via NotebookLM. Triggers: 'NotebookLM review,' 'NotebookLM braid,' 'NotebookLM handoff,' 'set up NotebookLM,' 'comprehensive review through NotebookLM,' 'evidence intelligence pass,' 'stress test through NotebookLM,' 'run NotebookLM on,' 'have NotebookLM look at,' or references using NotebookLM on case materials. Produces per-source digest prompts (opinions, moving papers, transcripts, depositions, exhibits, research memos, working draft) Claude can fetch later, plus analytical prompts for evidence inventory, gap analysis, defense preemption, authority deployment, and brief economy. Comet drives the cycle; results land in Notion automatically. Posts matter-channel Slack. NOT for case assessments (klg-case-assessment), response plans (klg-response-plan), or ChatGPT Deep Research (klg-deep-research-prompts)."
---

# KLG NotebookLM Handoff

## Purpose

Generate a self-contained Notion page that lets a human (Tim or
Brittney) build a NotebookLM notebook, then hands off to Comet to
run a comprehensive evidence-intelligence pass through NotebookLM
without further human intervention. Comet pastes all responses
back into the same Notion page under designated headings. Claude
later reads from the same page to integrate findings into the next
phase of work.

This is the NotebookLM analog of `klg-deep-research-prompts` (which
generates ChatGPT Deep Research prompts). Both skills emit a
Notion page with a Comet automation block; the difference is the
target tool (NotebookLM vs. ChatGPT) and what the prompts ask for.

## When to use this skill

Use whenever the user wants to leverage NotebookLM's strengths:
cross-document synthesis across many sources at once, structured
per-source digests, citation-traceable analytical findings.
Common contexts:

- After a brief is drafted and needs comprehensive stress-testing
  before filing (the Weinstein use case)
- Mid-stream in brief drafting when the user wants to ensure all
  available evidence is being optimally deployed
- After a case assessment when new documents arrive and the user
  wants to see how they affect the prior analysis
- When the source corpus is large (50+ documents) and Claude alone
  cannot hold all of them in context

Do NOT use for:
- Initial case assessment (use `klg-case-assessment`)
- Response plan memos (use `klg-response-plan`)
- ChatGPT Deep Research pipeline (use `klg-deep-research-prompts`)
- Single-source review or quick Q&A (run NotebookLM manually)

## Required Context

Read these reference files in the skill's `references/` directory:

1. `references/claude-md-standards.md` — Citation formats and
   terminology rules (Data Bank not NPDB; trial court not lower
   court; California Style Manual)
2. `references/klg-style-guide.md` — Writing voice and forbidden
   transitions
3. `references/handoff-standards.md` — Two-zone handoff structure
4. `references/workflow-patterns.md` — Iterative case memo and
   session logging patterns
5. `references/comet-notebooklm-block.md` — The canonical Comet
   automation block template (drop-in, with placeholders to fill)
6. `references/prompt-templates.md` — Per-source digest template
   and analytical prompt templates
7. `references/notion-page-structure.md` — The Notion page layout
   and output zone conventions

## Required Inputs

Minimum viable inputs:
- The matter name and case number
- The Case Portal entry (URL or ID)
- The workflow posture (MSJ opposition, brief draft, supplement,
  research synthesis)
- Confirmation of what source categories will be uploaded (the
  skill produces an upload checklist; the user confirms or amends)

If the user does not provide these, ask before proceeding. Do not
guess.

### Running in Chat vs. Cowork

This skill runs cleanly in either mode. Notion connector and Slack
connector are available in both. The Notion page itself is the
deliverable — there is no .docx file produced.

In Cowork, Claude can also browse the SharePoint matter folder to
identify what source files exist. In Chat, ask the user to confirm
the source list.

## Workflow

### Step 1 — Identify the matter and confirm posture

If the matter is not obvious from session context, ask. Then ask
the user which workflow posture applies. Use `ask_user_input` with
this single-select panel:

Question: "What workflow phase is this NotebookLM pass for?"
Options:
- Trial court MSJ or MSA opposition
- Appellate brief draft (any stage)
- Case assessment supplement (new documents arrived)
- Research synthesis (cross-cutting across many memos)

The posture determines which conditional prompts get included
(see Step 4).

### Step 2 — Project preflight

Before creating any Notion deliverables, search the Projects
database for an existing project for this matter and posture.
Project preflight rules per `claude.md`:

- Projects database: `df007c24-ffac-40d7-8e91-fb6763b6ecf6`
- Search by matter name and case number
- If a project exists (e.g., the parent project for a brief in
  progress), the NotebookLM page links to it via the Projects
  relation
- If no parent project exists, create one with Category = Case
  Support, Support Type = Research Pipeline, icon 🔍, target
  date = the operative deadline (filing deadline for MSJ
  opposition, etc.)

The NotebookLM page itself is a Research database entry, not a
project page. It links UP to the project page via the Projects
relation.

### Step 3 — Build the source upload checklist

Identify which source categories should be uploaded to NotebookLM.
The standard categories are:

**Drafting record (always include if applicable):**
- Working draft (the brief being analyzed)
- Opposition architecture or response plan memo
- Separate statement (for trial court MSJ posture)

**Research foundation (always include if applicable):**
- Research memos (existing, from prior pipeline runs)
- Westlaw verification output (cases file and statutes file)

**Opposition's papers (if applicable to posture):**
- Opposing brief and supporting separate statement
- Opposing party's declarations

**Court opinions:**
- Any prior appellate opinion (e.g., a reversal that established
  law of the case)
- Any trial court ruling being challenged

**Trial record (always include what's available):**
- Hearing transcripts
- Deposition transcripts
- Key exhibits

**Operative pleading and procedural posture:**
- The operative complaint or petition
- Any prior dismissed pleading for procedural context

**Co-counsel correspondence:**
- Emails or memos from referring counsel that frame the matter

Tailor the checklist to the matter. If a category does not apply
(e.g., no opposing brief in a brief-draft posture), omit it.

The checklist appears in the Notion page as a checkbox list the
user can tick off as they upload.

### Step 4 — Assemble the prompt queue

The prompt queue follows this structure. Universal prompts are
always included; conditional prompts are included based on what
sources are present and what posture was selected.

**Always include:**
1. Setup (case-posture context with terminology rules)
2. Source ingestion confirmation
3. Per-source digest prompts — one per source category present
   (court opinions, moving papers, transcripts, depositions,
   exhibits, research memos, working draft)
4. Evidence inventory by cause of action or issue on appeal
5. Gap analysis (fact-citation completeness)
6. Authority deployment audit

**Conditionally include:**
7. Defense preemption audit — only if there is an opposing brief
   in the corpus
8. Brief economy recommendations — only if there is a working
   draft in the corpus
9. Cross-MSJ stress test — only if the posture is MSJ opposition
   AND a cross-motion is being filed
10. Theory convergence/divergence — only if posture is research
    synthesis
11. Impact-on-prior-analysis — only if posture is case assessment
    supplement

For the exact prompt text, use `references/prompt-templates.md`.
Adapt each template to the specific matter:
- Substitute the case posture details
- Substitute the parties and individual defendants
- Substitute the operative legal claims and affirmative defenses
- Substitute the law-of-the-case anchor (if any)
- Substitute the working draft section structure (if applicable)
- Substitute the planned cuts/restructurings (if applicable)

### Step 5 — Build the Comet automation block

Use `references/comet-notebooklm-block.md` as the drop-in template.
Fill in:
- The total prompt count
- The notebook URL placeholder (user pastes after creating notebook)
- The full prompt queue with paste-target headings

The Comet block must be visually bordered with `═══` separators so
it is unmistakable as the automation unit. It must contain the
full workflow imperatively — capability declaration, preconditions,
workflow steps with explicit waits, error handling, stop condition.

### Step 6 — Build the output zones

Below the Comet block, emit empty paste-target headings — one per
prompt — in the order Comet will execute. Each heading is followed
by `*(Awaiting Comet output.)*` placeholder text. Comet pastes
under these headings.

Use `references/notion-page-structure.md` for the canonical layout.

### Step 7 — Add the close-the-loop section

After the output zones, emit a `## CLOSE-THE-LOOP` section. Comet
posts the completion confirmation here when finished. This section
also instructs the user what to do after Comet finishes:

> When Comet posts the close-the-loop confirmation, message Claude
> in chat: "Comet finished the NotebookLM review for [matter].
> Integrate the findings." Claude reads from this page and proceeds
> with the next phase of work.

### Step 8 — Add the manual-review prompts section

Audio overview prompts cannot be automated by Comet (audio is not
pasteable). Emit a final section with 3–5 audio overview customization
prompts the user can run themselves when they want to listen on a
drive or walk.

### Step 9 — Create the Notion page

Create the page in the Research database with these properties:
- Title: `NotebookLM Handoff — [Matter Short Name] ([Posture])`
- Icon: 🎧
- Case Portal: linked to the matter's Case Portal entry
- Projects: linked to the parent project (if any)
- Tags: Claude Session Log
- Salience: ★★★

Page content per `references/notion-page-structure.md`.

### Step 10 — Post Slack notification

Post to the matter-specific Slack channel (or fall back to
`#case-management` C0AA65K626B if no matter channel exists).

Use the two-zone structure from `claude.md`. Zone 1 (action items)
must include:
1. Build the NotebookLM notebook (10-minute task)
2. Paste the notebook URL into the Comet block placeholder
3. Launch Comet on the page
4. Post close-the-loop confirmation when Comet finishes

Zone 2 (for reference) lists the prompts in the queue and the
estimated runtime.

Tag the appropriate person:
- Default: `<@U07PYJDNGT0>` (Tim Kowal) for upload + Comet
- If user delegates upload to Brittney: `<@U09EKSYTF6K>` for upload,
  then handoff to Tim or William for Comet

Begin with: "This is Claude posting on [name]'s behalf." where
[name] is the current user.

Bare URLs only. No angle brackets around URLs. User mentions in
`<@USER_ID>` format.

### Step 11 — Hand off to user in chat

End the session with a clear handoff per `references/handoff-standards.md`:

- What just happened (NotebookLM page created, Slack posted)
- What to do next (build notebook, launch Comet)
- Notion page URL and Slack channel
- Trigger phrase to give Claude when Comet finishes
- Expected runtime
- Common failure modes

## Posture-Specific Variations

### MSJ or MSA opposition (trial court)

- Setup prompt frames the case in trial court posture
- Evidence inventory organized by cause of action and affirmative
  defense
- Defense preemption audit included (defendants' MSJ in corpus)
- Brief economy recommendations included (working draft in corpus)
- Cross-MSJ stress test included if applicable
- Style: California Style Manual; trial court terminology

### Appellate brief draft (any stage)

- Setup prompt frames the case in appellate posture
- Evidence inventory organized by issue on appeal
- Defense preemption audit included if opposing brief is in corpus
  (RB analyzes AOB; ARB analyzes RB)
- Brief economy recommendations included
- No cross-MSJ stress test
- Style: California Style Manual + Bluebook for federal

### Case assessment supplement

- Setup prompt frames as supplemental analysis
- Per-source digests focus on the new documents
- Evidence inventory not included (assessment did this already)
- Special prompt: "Impact on prior analysis" — for each conclusion
  in the original assessment, identify whether the new documents
  strengthen, weaken, or change the conclusion
- No defense preemption or brief economy

### Research synthesis

- Setup prompt frames as cross-cutting research analysis
- Per-source digests focus on research memos
- Special prompt: "Theory convergence and divergence" — identify
  where memos agree, disagree, and what gaps remain
- Authority deployment audit emphasizes substitution recommendations
- No defense preemption or brief economy

## Execution Rules

1. Always run project preflight before creating Notion deliverables.
   The NotebookLM page is a Research database entry; the parent
   project is a Projects database entry.
2. Tailor the source upload checklist to what the matter actually
   has — do not list generic placeholders.
3. The setup prompt must include the case-posture context tailored
   to the matter, not a generic template. Cite the specific Court
   of Appeal opinion (if any), the specific affirmative defenses,
   the specific causes of action.
4. The Comet automation block must be self-contained and written
   imperatively. No "first, you might want to..." human-tutorial
   language. Comet treats the block as agent instructions.
5. Each prompt must have an explicit `PASTE TARGET` value matching
   an empty heading in the output zones below. The heading text
   in the prompt and the heading text in the output zone must
   match exactly.
6. The page is the deliverable. Do not also produce a .docx.
7. Always post a Slack notification after creating the page. The
   page exists to be used; without the Slack ping, it sits unused.
8. Apply the KLG Style Guide voice in any instructional prose
   (Quick start, manual prompts section, etc.). The prompts
   themselves use legal style appropriate for NotebookLM.
9. Follow the session logging pattern from `claude.md` — append
   the session log prompt at the end of the response if this
   skill is run inside a substantive session (otherwise the page
   creation IS the session deliverable and no log is needed).

## What to do when Comet finishes

When the user returns saying Comet finished the NotebookLM review,
this skill's job is complete. The next step is integration — that
work is done by whatever skill matches the next phase:

- For brief rewrites: `klg-brief-elevation` reads the digests and
  analytical outputs and applies the recommended changes
- For declarations drafting: read the deposition and exhibit digests
  to identify what each declaration must establish
- For oral argument prep: `klg-oral-argument` reads the B318163
  digest and the working draft digest as panel-question rehearsal

The digests are durable. They live on the NotebookLM page
indefinitely and can be fetched in any later session for any
purpose.
