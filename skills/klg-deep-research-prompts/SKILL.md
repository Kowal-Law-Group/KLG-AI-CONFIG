---
name: klg-deep-research-prompts
description: "Generate tiered deep research prompts (3–12) from a case file or case assessment memo, optimized for ChatGPT Deep Research via Comet browser. Prompts are categorized into three tiers (Core, Important, Optional) and the user selects which to run. Use whenever the user says 'generate research prompts', 'create deep research prompts', 'research this case', 'start the research pipeline', 'deep research prompts', 'run the research pipeline', 'prepare research for briefing', or references generating research prompts from a case assessment. This is Step 1 of the KLG Research Pipeline. Also triggers when the user completes a case assessment and wants to move to research, or says 'what's the next step' after an assessment. Produces a Notion page with user-selected prompts, a research map, Comet launch instructions, and next-step guidance. Do NOT use for case assessments (intake memos), response plan memos, or research compilation (Step 2)."
---

# KLG Deep Research Prompt Generator

## Purpose

Analyze a case file (or existing case assessment memo) and generate
precisely targeted deep research prompts optimized for ChatGPT
Deep Research. Prompts are categorized into three priority tiers
(Core, Important, Optional) and the user selects which tiers or
individual prompts to run — from as few as 3 to as many as 12.
The selected prompts are delivered via a Notion page in the
Research database, which Comet will read, use to launch Deep
Research sessions, and write the completed research back into.

This is Step 1 of the KLG Research Pipeline:
1. **THIS SKILL** → Generate research prompts, user selects
   which to run, selected prompts posted to Notion
2. User gives Notion page URL to Comet → Comet launches Deep
   Research in ChatGPT → Comet pastes completed research back
   into the same Notion page under each prompt
3. User tells Claude the research is done → Skill 4 reads the
   Notion page, compiles, and extracts authorities
4. User gives Westlaw authority list to Comet → Find & Print
5. User uploads Westlaw PDF → Skill 4 finalizes package

## Required Context

Before generating prompts, read these reference files in the
skill's `references/` directory:

1. `references/claude-md-standards.md` — Citation formats
2. `references/klg-style-guide.md` — Writing voice
3. `references/klg-case-assessment-standards.md` — Analytical
   framework
4. `references/handoff-standards.md` — Handoff instruction format
5. `references/prompt-template.md` — Canonical prompt template
6. `references/notion-page-structure.md` — Notion page layout
7. `references/workflow-patterns.md` — Iterative case memo and
   client memo patterns

## Required Inputs

- Case file documents OR an existing case assessment memo
- Jurisdiction (if not apparent — default California)
- Key issues identified (from case assessment or attorney direction)

If an Initial Case Assessment has already been produced in a prior
conversation or exists in the matter folder, use it.

### Running in Chat vs. Cowork

This skill works in BOTH Chat and Cowork sessions. The Notion
connector and file creation tools are available in both modes.

**In Cowork:** The matter folder is auto-mounted. Claude can
browse the case files directly.

**In Chat:** The user must upload the relevant documents at the
start of the conversation. At minimum, upload:
- The case assessment memo (if one exists — this is the most
  important document since it synthesizes all issues)
- The opposing brief (if this is a response/reply project)
- Any key orders or rulings being challenged

Claude should check: "Do I have enough context to identify the
key legal issues? If not, ask the user to upload more."

The advantage of Chat mode is that multiple research projects
can run in parallel — one per Chat tab.

## Interaction Rules

- Read ALL provided materials before generating prompts.
- If you have a case assessment, use its issue identification to
  target the prompts. Do not duplicate work already done.
- If you only have raw case files and no assessment, identify the
  key issues yourself before generating prompts.
- Ask for jurisdiction if not apparent. Default to California.
- Do not stall. Generate the best prompts you can with what you have.

## Prompt Generation Rules

### Structure of Each Prompt

Each prompt must be:
- Self-contained (ChatGPT will have no prior context)
- Jurisdiction-specific
- Issue-focused (one legal issue or cluster per prompt)
- Formatted to produce a formal research memo with cited authorities
- Explicit about wanting: rule statements, key cases, circuit splits,
  and practical application to facts like ours

The exact prompt template is in `references/prompt-template.md`.

### CRITICAL: Output Format Instruction in Each Prompt

Each prompt MUST include this instruction at the end, before the
closing of the prompt:

```
OUTPUT FORMAT REQUIREMENT: Your entire memo must be delivered as
plain text inside a single code block. Do not use markdown
formatting outside the code block. Include all citations in full
text within the memo body. This is essential for automated
processing.
```

This ensures Comet can extract the research memo text and paste
it back into Notion cleanly.

### How to Allocate Prompts

Start by identifying ALL issues from the case assessment or case
file. Then categorize every prompt into one of three tiers:

**TIER 1 — Core (critical, high-leverage prompts):**
These are the issues the case turns on. If you only ran three
prompts, these are the three. Includes:
- The strongest appellate issues (one prompt per major issue)
- Any threshold/jurisdictional issues that could be dispositive
- The single most dangerous opposing argument (know-your-enemy)

**TIER 2 — Important (secondary but valuable prompts):**
These strengthen the case or close gaps but aren't make-or-break.
Includes:
- Secondary appellate issues
- Preservation and procedural issues
- Remedies and relief
- Additional opposing arguments beyond the strongest one

**TIER 3 — Optional (context and depth prompts):**
These provide background, explore emerging trends, or go deeper
on issues already covered in Tier 1–2. Includes:
- Comprehensive standard of review analysis (if not already
  embedded in a Tier 1 prompt)
- Policy, equitable considerations, emerging trends
- Circuit splits or secondary jurisdictions
- Exploratory research on novel theories

The total across all tiers should be 3–12 prompts. Never pad
with low-value prompts to reach a number. If only 4 issues
exist, generate 4 prompts. If 15 issues exist, prioritize the
top 10–12 and note excluded issues.

### Prompt Selection — User Chooses What to Run

**CRITICAL: Do NOT post prompts to Notion until the user
selects which ones to run.**

After generating all prompts, present them to the user in a
structured selection menu. Use this format:

```
I've identified [N] research prompts across three priority
tiers. Here's the breakdown:

TIER 1 — CORE ([N] prompts, recommended for all projects):
  [1] [Short title] — [one-sentence description of issue]
  [2] [Short title] — [one-sentence description]
  [3] [Short title] — [one-sentence description]

TIER 2 — IMPORTANT ([N] prompts, recommended for briefing):
  [4] [Short title] — [one-sentence description]
  [5] [Short title] — [one-sentence description]

TIER 3 — OPTIONAL ([N] prompts, for comprehensive research):
  [6] [Short title] — [one-sentence description]
  [7] [Short title] — [one-sentence description]

How would you like to proceed? You can select by tier, by
number, or both:
  - "Tier 1 only" — runs [N] prompts (~[time estimate])
  - "Tiers 1 and 2" — runs [N] prompts (~[time estimate])
  - "All" — runs all [N] prompts (~[time estimate])
  - Or pick specific prompts by number: e.g., "1, 3, 5"
```

Wait for the user's selection before proceeding to Notion.
Only the selected prompts are posted to the Notion page.
Unselected prompts are noted in the Research Map as "Not
selected — available for future research" so nothing is lost.

**Time estimates:** Use 5–10 minutes per prompt for ChatGPT
Deep Research. A 3-prompt Tier 1 run is ~15–30 minutes; a
full 10-prompt run is ~50–90 minutes.

**Exception — Skip the selection menu when:** If the user has
already reviewed and explicitly approved all prompts during the
conversation (e.g., they described the issues, Claude proposed
specific prompts, and the user said "yes, proceed with all of
those"), skip the tier selection menu and post all approved
prompts directly to Notion. The selection menu exists to give
the user control — if they have already exercised that control,
repeating the menu wastes time. When skipping, confirm briefly:
"You've already approved all [N] prompts. Posting them to
Notion now."

---

## OUTPUT DELIVERY: NOTION RESEARCH PAGE

### Step 0: Prior Work Search, Project Preflight, and Task Creation

Before creating ANY Notion deliverables, complete all three
sub-steps below. This prevents duplicate projects, orphaned
research pages, and ensures iterative work builds on prior
analysis.

#### Step 0a: Prior Work Search

Search for existing work on this topic BEFORE creating anything.
This is especially important for content/podcast research that
may not be tied to a Case Portal entry.

1. **Search the Projects database** (data source:
   `collection://df007c24-ffac-40d7-8e91-fb6763b6ecf6`) using
   semantic search on the topic keywords (not just exact case
   name/number). Example: for birthright citizenship research,
   search "birthright citizenship" — not just the case number.

2. **Search the Research database** (data source:
   `collection://622bfafd-45b1-451a-b518-f72d86767cb0`) for
   existing research pages on the same topic. Use semantic
   search with topic keywords.

3. **Present any matches to the user before creating anything:**

   "I found existing work on this topic:
   - [Project: title and URL]
   - [Research pages: titles and URLs]

   Should I link the new research cycle to this existing
   project? Or is this a separate initiative?"

4. If matches are found and the user confirms they're related:
   - Use the existing project (do NOT create a new one)
   - Note all related research page URLs for the `📚Related
     Research` relation in Step 2

5. If no matches are found, or the user says this is separate:
   proceed to Step 0b to create a new project.

#### Step 0b: Project Preflight

Per `claude.md` "Project Page as Source of Truth" rules:

1. If an existing project was identified in Step 0a, use it.
   Store the project page URL.

2. If no project exists, create one in the Projects database:
   - **Project name:** `[Matter/Topic] — [Research Focus]
     ([Case No. or "Content"])`
   - **Category:** Case Support
   - **Support Type:** Research Pipeline
   - **Icon:** 🔍
   - **Status:** In progress
   - **Priority:** Set based on deadline proximity:
     - High if deadline ≤14 days or active emergency
     - Medium if deadline ≤30 days
     - Low if no external deadline
   - **Target Date:** The brief filing deadline, episode
     recording date, or other deadline this research supports.
     If no specific deadline, set to 30 days from today and
     note in Summary.
   - **Case Portal:** Link to the matter's Case Portal entry
     (found in Step 1 below). For content/podcast research
     without a Case Portal, leave blank.
   - **Team Portals:** Link to the appropriate portal:
     - Case work → PC Intake & Case Management
       (`3250fc06-a06c-80c2-9d28-da7c0b81c6b8`)
     - Content/podcast → Content & Networking
   - **Summary:** One paragraph describing the research focus

**Categorization note for content/podcast research:** Research
pipelines that use the 5-step process (prompts → Comet → compile
→ Westlaw → finalize) are always Category = Case Support,
Support Type = Research Pipeline — regardless of whether the
research supports a case or content production. The pipeline
mechanics are the same. The distinction is captured by the
Team Portals relation and the presence (or absence) of a Case
Portal link.

#### Step 0c: Create the Task

Create a task in the **Tasks** database (data source:
`collection://c60b4989-61ac-40b3-956f-8fdce828da32`) to track
this research cycle as an assignable, dateable work unit.

**Properties to set:**
- **Task name:** `Deep Research: [Research Focus] ([N] prompts)`
  (e.g., "Deep Research: Jurisdiction & Dual Nationality
  (10 prompts)")
- **Status:** In progress
- **Assignee:** The person who will run the prompts. Default
  is William Hernandez. If the user specifies a different
  person (including themselves), assign to that person instead.
  ASK if not clear from context. The assignee identity has
  NO effect on what deliverables are produced — see
  "Identity-Agnostic Deliverables" below.
- **Priority:** Match the project's priority
- **Due:** The target completion date for this research cycle
  (not the brief deadline — estimate based on prompt count:
  ~2 days for ≤4 prompts, ~3–4 days for 5–10 prompts)
- **Deadline Type:** Set to "Soft" (internal research target,
  not a court deadline) or "Hard" (if the brief deadline is
  imminent and this research is blocking)
- **Project:** Link to the project page from Step 0b
  (JSON array: `["https://www.notion.so/PROJECT_ID"]`)
- **Tags:** Set based on context:
  - "Client Matters" for case research
  - "Podcast" for podcast/content research
- **Summary:** Brief description of the research focus and
  how it connects to the project

**One task per pipeline cycle.** The [1/5] through [5/5]
title prefix on the Research page tracks steps within the
single task. Do NOT create separate tasks for prompt
generation, Comet run, compilation, Westlaw, and finalization.
Create a new task only when the user initiates a new round of
research on the same topic.

Store the task page URL — it is needed for the Research page
(Step 2) and the Slack message.

### Step 1: Find or Create the Case Portal

Before creating the Research page, look for an existing Case
Portal entry for this matter:

1. Search the Case Portal database (data source:
   `collection://2da0fc06-a06c-8033-978b-000bd2803cd4`) for the
   matter name.
2. If found, note its page URL for the relation field.
3. If NOT found, ask the user:

   "I don't see an existing Case Portal for [matter name].
   Would you like me to create one, or do you want to point me
   to an existing one? (If the case portal is under a different
   name, let me know.)"

   Only create a new Case Portal entry if the user confirms.

### Step 2: Create the Research Page in Notion

Create a new page in the **Research** database (data source:
`collection://622bfafd-45b1-451a-b518-f72d86767cb0`).

**Properties to set:**
- **Title:** "[1/5] [Short Research Description] — [Case Short Name] ([Case No.])"
  - The `[1/5]` prefix is the pipeline progress indicator.
    It updates at each stage: Comet changes it to `[3/5]`
    when all memos are pasted; Claude changes it to `[4/5]`
    and `[5/5]` during compilation and finalization.
  - The short research description should be a concise phrase
    (3–8 words) capturing the focus of the research project,
    derived from the selected prompts. Examples:
    - "[1/5] Supersession and Preservation Issues — Toles (B342169)"
    - "[1/5] Summary Judgment Standard of Review — Bejarano (G063127)"
    - "[1/5] Limited Remand Viability — Lopez (B341558)"
  - Do NOT use the generic prefix "Deep Research Prompts."
    Every research page should be identifiable by its subject
    matter at a glance in the Notion database.
- **Case Portal:** Set using a JSON array containing the Case Portal
  page URL. Example: `"Case Portal": "[\"https://www.notion.so/PAGE_ID\"]"`
  where PAGE_ID is the UUID (with or without dashes) of the Case
  Portal entry found in Step 1. This MUST be a JSON-encoded array
  string — a bare URL or page ID will silently fail.
- **Tags:** ["Research"]
- **Publish or Pass?:** "Not Applicable"
- **Note:** "Step 1 of KLG Research Pipeline. [N] of [TOTAL
  generated] Deep Research prompts selected for [brief type].
  Launch via Comet browser."
- **Date:** [today's date]
- **Salience:** "★★★"
- **Projects:** Link to the project page from Step 0b.
  JSON array: `["https://www.notion.so/PROJECT_ID"]`
- **Tasks:** Link to the task from Step 0c.
  JSON array: `["https://www.notion.so/TASK_ID"]`
- **📚Related Research:** If Step 0a found existing research
  pages on the same topic, link them here. JSON array of page
  URLs. This relation connects the new research cycle to prior
  work so it's visible in both directions.
  If no prior research was found, leave empty.

### Step 3: Link the Task to the Research Page

After the Research page is created, update the Task (from
Step 0c) to link to the Research page via the `✍️ Legal
Research` relation. This completes the three-tier linkage:
Project → Task → Research page.

Use `notion-update-page` on the Task page ID with:
```
"✍️ Legal Research": "[\"https://www.notion.so/RESEARCH_PAGE_ID\"]"
```

### Step 4: Build the Notion Page Content

The page layout is defined in `references/notion-page-structure.md`.
Read that file for the exact structure. Key sections:

1. **Header block** — Matter name, pipeline stage, date, status
2. **Comet Agent Instructions** — TWO toggles on the page:
   (a) The full Comet automation code block (Phase 1 parallel
   launch / Phase 2 harvest / Phase 3 finalize) — this is the
   PRIMARY instruction set, placed directly on the page so
   Comet can read it without needing the chat handoff.
   (b) Manual fallback instructions for human operators.
   BOTH sets of instructions use parallel execution — launch
   all prompts first in separate tabs, then harvest as they
   complete. See `references/notion-page-structure.md` for
   the exact content of both toggles.
   **BATCH SIZE:** If there are more than 4 prompts, the
   instructions split the launch into two waves (1-4, then
   5-[N]) to avoid overwhelming the browser.
3. **Research Map — Checklist** — To-do list with one checkbox per
   prompt, showing issue title, priority, and a compilation status
   field. See `references/notion-page-structure.md` for format.
4. **Prompts** — Each SELECTED prompt in its own section with:
   - A heading: `## PROMPT [N] OF [SELECTED COUNT]: [TITLE]`
   - A copy-paste label: `📋 **COPY THIS PROMPT** — Select all
     text in the code block below and paste it into a new ChatGPT
     Deep Research session.`
   - The complete prompt in a code block (```javascript block)
   - A placeholder section: `### Research Output — Prompt [N]`
     with text: "[Comet will paste the completed Deep Research
     memo here]"
   - Unselected prompts are NOT posted to the Notion page but
     are listed in the Research Map as "Not selected"
5. **Breadcrumb Links** — Case Portal link, skill pipeline references
6. **Pipeline Status** — Current step, last completed, next
   action, and estimated time. Pre-populated with step 4
   instructions so the user sees them when Comet finishes.

### Step 5: Present to the User

After creating the Notion page:

1. Provide the Notion page URL.
2. Deliver the handoff instructions per the handoff standards.

DO NOT output the prompts in a Word document. DO NOT output
them in the chat as a long message. The prompts live in Notion
so that Comet can read them and paste research output back in.

---

## IDENTITY-AGNOSTIC DELIVERABLES — HARD RULE

The following deliverables are ALWAYS produced in full,
identically, regardless of who will run the prompts:

1. The Notion research page — complete with ALL sections:
   header, Comet agent instructions (both toggles: automation
   code block AND manual fallback), research map checklist,
   all prompt code blocks with copy-paste labels, output
   placeholders, breadcrumb links, and pipeline status.
2. The Comet automation script — the full Phase 1/2/3 code
   block, placed BOTH on the Notion page AND in the chat
   handoff (Section 2 below).
3. The chat handoff — all three sections (Section 1 status,
   Section 2 Comet automation prompt, Section 3 next steps
   and Chat offboarding).

The ONLY things that change based on the runner's identity:
- The Task assignee (Step 0c above)
- The Slack notification target and channel (below)
- Whether a Slack notification is sent at all (if the user
  is running the prompts themselves and does not want a
  notification, skip the Slack message — but still produce
  the full Notion page and chat handoff)

Claude MUST NOT simplify, abbreviate, or omit any Notion
page content, Comet automation script, or handoff deliverable
because the user (rather than William) will run the prompts.
The Notion page is the permanent record — it must be complete
for anyone who opens it later, regardless of who ran the
prompts originally.

**Why this rule exists:** Claude has twice derailed this skill
by treating "I'll run the prompts myself" or "assign this to
me" as permission to skip the Comet instructions, omit the
automation code block, and produce an abbreviated Notion page.
That interpretation is wrong. The deliverables are identity-
agnostic. Only the assignment and notification routing are
variable. The execution steps are the same whether Tim,
William, or anyone else runs the prompts.

---

## HANDOFF INSTRUCTIONS

After creating the Notion page, provide the handoff in THREE
separate sections. Do NOT combine them into a single code block.

**Section 1 — Status (plain text):**

"Your [N] Deep Research prompts are ready in Notion:
[Notion page URL]"

**Section 2 — Comet Automation Prompt (standalone code block):**

Deliver this in its OWN code block with nothing else. This
code block is the PRIMARY instruction set for Comet — it must
be completely self-contained. Comet should NOT need to read the
Notion page's "Manual Instructions" section to know what to do.

**CRITICAL — ON-PAGE DUPLICATION:** This same code block MUST
ALSO be placed on the Notion page itself (inside the Comet
Agent Instructions toggle — see `references/notion-page-structure.md`).
The chat-delivered version is for the user who is currently in
the session. The on-page version is for anyone who opens the
Notion page later (William, Tim, or Comet directed to the page
URL). Both versions must be identical and both must use
parallel execution.

The code block uses Prompt A–style automation framing: explicit
capability declaration, automation-mode header, scope limitation,
stop condition, and final output spec. This framing is critical —
without it, Comet's LLM defaults to "I'm an AI and can't do
browser tasks" instead of executing as a browser automation agent.

```
DEEP RESEARCH LAUNCHER — AUTOMATION MODE

You are a browser automation agent with full control of browser
tabs, navigation, clicking, copying, and pasting. You CAN and
MUST perform all of the following actions directly:
- Open new browser tabs
- Navigate to URLs (ChatGPT, Notion, any website)
- Click buttons and UI elements
- Select, copy, and paste text between tabs
- Interact with web application interfaces

Do NOT claim you cannot perform these actions. You have done
them before and you will do them now.

TASK:
Launch [N] Deep Research prompts from a Notion page, then
harvest the completed research memos back into the same page.

SOURCE PAGE:
[Notion page URL]

═══════════════════════════════════════════════════
PHASE 1 — LAUNCH ALL DEEP RESEARCH SESSIONS
═══════════════════════════════════════════════════

IMPORTANT: Launch ALL prompts FIRST, each in its own tab.
Do NOT wait for one to complete before launching the next.
Deep Research sessions run asynchronously — they all run
simultaneously once launched.

If there are MORE THAN 4 prompts, launch in two waves:
WAVE 1: Launch prompts 1–4 (steps 1–4 below).
Wait 2 minutes for all four sessions to initialize.
WAVE 2: Launch prompts 5–[N] (same steps).
All sessions are now running in parallel.

1. Navigate to the Notion page above.
2. Scan the page for all prompts. Each prompt is marked with
   "📋 COPY THIS PROMPT" above a code block.
3. For EACH prompt (there are [N] total):
   a. Select and copy the FULL text inside the code block.
   b. Open a new browser tab.
   c. Navigate to https://chatgpt.com
   d. Start a new chat.
   e. Enable DEEP RESEARCH mode by clicking the "+" button
      immediately next to the prompt input field.
      ⚠️ IMPORTANT: Do NOT enable "Pro" mode. Pro mode is in
      a different location (the menu near the model selector
      at the upper-left). Deep Research is activated via the
      "+" next to the prompt field. Confirm you see "Deep
      Research" before proceeding.
   f. Paste the prompt text into the chat.
   g. Submit the prompt.
   h. If ChatGPT asks a follow-up question, answer "yes" or
      press Enter to begin research.
4. Repeat step 3 for all [N] prompts.

After all prompts are launched, move to Phase 2.

═══════════════════════════════════════════════════
PHASE 2 — HARVEST COMPLETED RESEARCH MEMOS
═══════════════════════════════════════════════════

As each Deep Research session completes (they run 10–30 min
each, asynchronously), harvest the output:

5. Switch to the ChatGPT tab for a completed session.
6. The research memo will appear as a code block in the
   ChatGPT response.
   ⚠️ DO NOT click to expand the code block to full screen
   (this causes browser lag and may crash the tab).
7. Click the DOWNLOAD ICON at the top-right corner of the
   code block. Select "Copy contents."
   Do NOT use any "export" or "download file" options.
8. Switch to the Notion tab with the source page.
9. Find the section "Research Output — Prompt [N]" that
   corresponds to this prompt.
10. Replace the placeholder text with a new code block and
    paste the copied contents.
11. Scroll up to the "Research Map — Checklist" section.
    Find the checkbox for this prompt and check it off.
12. Repeat steps 5–11 for each completed research memo.

═══════════════════════════════════════════════════
PHASE 3 — FINALIZE
═══════════════════════════════════════════════════

When ALL [N] research memos have been pasted into Notion:

13. Update the Notion page title: change "[1/5]" to "[3/5]"
    at the start of the title. Leave the rest unchanged.
14. Display this completion message to the user:

    ═══════════════════════════════════════════════
    ✅ ALL [N] DEEP RESEARCH MEMOS COMPLETE
    ═══════════════════════════════════════════════
    All research has been pasted into the Notion page:
    [Notion page URL]

    WHAT TO DO NEXT:
    1. Go to Claude (claude.ai).
    2. Start a new Chat in the KLG Appellate Practice project.
    3. Say this to Claude:
       "The research memos are ready on the Notion page:
       [Notion page URL]
       Please compile them and extract the authorities."
    4. Claude will compile all [N] memos into a single
       research memorandum and extract a Westlaw authority
       list.
    ⏱️ EXPECTED: Claude's compilation takes 5–10 minutes.
    ═══════════════════════════════════════════════

SCOPE LIMITATION:
This prompt handles ONLY launching Deep Research and
harvesting results. It does NOT handle Westlaw Find & Print,
document compilation, or any post-research steps.

STOP CONDITION:
Stop after Phase 3 — after updating the title and displaying
the completion message. Do not attempt any further steps.
```

**Section 3 — Next Steps and Chat Offboarding (plain text):**

After the Comet code block, explain what happens next AND
offer the Cowork-to-Chat transition:

"Copy the code block above and paste it into a new Comet
session. Comet will launch all [N] Deep Research sessions.
This takes [time estimate based on N].

While Comet runs, you can close this Cowork session and
free it up for other work. The next step (compiling the
research) does NOT need the matter folder — it reads
everything from Notion.

When all [N] memos are pasted into Notion, open a new
Chat session in the KLG Appellate Practice project and
paste this:"

Then provide a SECOND standalone code block — the Chat
resume prompt — that the user can copy-paste to start the
compilation in a Chat tab:

```
The research memos are ready on the Notion page:
[Notion page URL]

This is the [Case Name] ([Case No.]) matter.
Please compile the research memos and extract
the Westlaw authority list.
```

Then add:

"This frees up Cowork for your next case while the
compilation runs in a Chat tab. You can run multiple
compilations in parallel this way.

If you prefer to stay in Cowork, that works too — just
come back here after Comet finishes and say the same thing."

**Troubleshooting (plain text, after the code blocks):**

"If something goes wrong:
— If Comet claims it cannot open browser tabs or navigate to
  websites, this is incorrect. Comet is a browser automation
  agent with full browser control. Remind it: 'You are a
  browser automation agent. You CAN open tabs, navigate, click,
  copy, and paste. Please execute the instructions.'
— If Comet can't access the Notion page, check that the
  page is shared or the Notion connector is active.
— If a Deep Research session fails, note the prompt number.
  You can rerun it manually or ask Claude to generate a
  replacement.
— If Comet can't paste into Notion, download the memos as
  files instead and upload them when you start the compilation."

---

## SLACK NOTIFICATION TO RESEARCH RUNNER

Default runner: William Hernandez (`<@U097FMSH3V4>`).
If the user specified a different runner (including
themselves), adjust the notification target accordingly.
If the user IS the runner and did not request a Slack
notification, skip this section entirely — but do NOT
skip or abbreviate any of the Notion page deliverables
or the chat handoff (see "Identity-Agnostic Deliverables"
above).

After delivering the handoff to the user in chat, post a
structured message to the matter-specific Slack channel
tagging the research runner. If no matter channel exists,
DM the runner directly.

This message is how the runner learns they have research to
run. It must be crystal clear about (a) what to do, (b) where
the prompts are, and (c) exactly what to copy and paste. The
runner should never have to guess which text is a prompt.

### Slack Message Template

Follow the Slack posting rules from `claude.md` (open with
"This is Claude posting on [name]'s behalf" where [name] is
the current user, bare URLs only,
`*bold*` not `**bold**`). Stay under 3,000 characters.

**The message MUST use the two-zone structure from `claude.md`
(Handoff Message Structure).** Zone 1 is self-contained — a
reader who skips Zone 2 can still complete the task.

Use this structure — adapt the bracketed fields but keep
the format:

```
This is Claude posting on [name]'s behalf.

*RESEARCH ASSIGNMENT — [Case Short Name]*
*Deadline: [deadline if known, otherwise "No hard deadline"]*

<@[RUNNER_SLACK_ID]> — Please run [N] Deep Research prompts
for [Case Short Name] via Comet.

— — — — — — — — — — — —
*YOUR ACTION ITEMS:*
— — — — — — — — — — — —

1. The project page (source of truth for this pipeline):
   [project page URL]
2. Your task for this research cycle:
   [task page URL]
3. Open this research page for the prompts:
   [Notion research page URL]
4. Each prompt is in its own code block, labeled
   "📋 COPY THIS PROMPT."
5. Launch ALL prompts in parallel: for each one, copy
   the text, open a NEW ChatGPT tab (keep the others
   running), enable Deep Research, paste, and submit.
   If there are more than 4 prompts, launch in two
   waves of 4. Do NOT wait for one to finish before
   starting the next — they run simultaneously.
6. As each research memo completes, paste it back into
   the Notion page under the "Research Output" heading
   for that prompt.
7. When all [N] are done, update the Notion page title:
   change "[1/5]" to "[3/5]" at the start. Leave the
   rest of the title unchanged.
8. Then notify Tim in this channel that research is done.

Full step-by-step instructions are also at the top of
the Notion page under "COMET AGENT INSTRUCTIONS."

— — — — — — — — — — — —
*FOR YOUR REFERENCE (no action needed):*
— — — — — — — — — — — —

*Prompt topics ([N] total):*
1. [Short title of prompt 1]
2. [Short title of prompt 2]
[... one line per selected prompt ...]

*Context:* [brief background on the case/research focus]

*Priority:* [priority context — e.g., "These need to be
completed today if possible. The opposition is due [date]."]
```

### Slack Message Rules

1. The prompt topic list in Slack is FOR REFERENCE ONLY —
   it tells the runner what the research covers. It is NOT the
   text they copy into Comet. It lives in Zone 2, explicitly
   labeled as reference content.
2. The completion/hand-back step ("update the title and notify
   Tim") is a NUMBERED ITEM in Zone 1, not a loose paragraph
   at the end.
3. If the user provided a deadline or urgency context,
   include it prominently. Otherwise write "No hard
   deadline — complete when available."
4. Do NOT paste the full prompt text into the Slack message.
   The prompts are too long for Slack (3,000 char limit) and
   they live in Notion — that's the single source of truth.
5. Always include the step "Each prompt is in its own code
   block, labeled '📋 COPY THIS PROMPT'" so the runner knows
   exactly what to look for on the Notion page.
6. When posting the actual Slack message, use `<@SLACK_ID>`
   for the runner's mention so Slack renders it as a clickable
   ping. The angle-bracket restriction in `claude.md` applies
   to URLs, not to Slack user mentions.

### Runner Slack IDs (quick reference)

| Runner | Slack ID |
|---|---|
| William Hernandez (default) | U097FMSH3V4 |
| Edwyn Sierra | U0AS9KZQ69X |
| Tim Kowal | U07PYJDNGT0 |
| Brittney Bishop | U09EKSYTF6K |
| Ted Davis | U09EKSXH7GX |

---

## Execution Rules

1. Read the entire case file or assessment before generating
   any prompts.
2. Each prompt must be self-contained. ChatGPT Deep Research
   sessions have no shared context.
3. Tailor the factual context in each prompt to the specific
   issue without identifying actual party names.
4. Do not fabricate legal issues. If uncertain, include but
   note uncertainty in the Research Map.
5. Match jurisdiction to the case. Default California.
6. Prompts must request California Style Manual citations for
   CA authorities and Bluebook for federal.
7. Always include the authority hierarchy instruction.
8. Each prompt must include the OUTPUT FORMAT REQUIREMENT
   instruction for code-block output.
9. Generate prompts for all identified issues (typically 3–12),
   categorize into tiers, and present the selection menu to the
   user. Only post the user's selected prompts to Notion.
10. Apply the KLG Style Guide voice in all instructional text.
11. ALL output goes to Notion. Do not generate .docx files.
12. Always end with handoff instructions per the handoff
    standards. Never leave the user wondering what to do next.
13. After producing the final deliverable, follow the workflow
    patterns in `references/workflow-patterns.md`:
    - Pattern 2 (Client Memo): Not typically applicable for
      research prompts, but if the user asks, offer to produce
      a client-facing summary of the research plan.
