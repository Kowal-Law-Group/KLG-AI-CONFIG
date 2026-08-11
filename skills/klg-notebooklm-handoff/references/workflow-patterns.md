# KLG Workflow Patterns

These patterns apply across all KLG pipeline skills. Every skill
that produces a memo or research deliverable must follow these
patterns at the appropriate point in the workflow.

---

## Pattern 1: Iterative / Evolving Case Memo

### Principle

KLG prefers to maintain a single evolving case memo per matter
rather than producing disconnected standalone documents. Each new
analysis — case assessment, response plan, research compilation,
supplemental assessment — can be added as a new section to the
existing case memo, building a comprehensive single document
that grows with the matter.

### When to Apply

At the conclusion of producing ANY of these deliverables:
- Initial Case Assessment
- Supplemental Case Assessment
- Response Plan Memo
- Compiled Research Memorandum
- Any other analytical memo for a matter

### What to Do

Before generating the final output, ask the user:

```
This [memo type] is ready. How would you like it delivered?

1. **Add to existing case memo** — I'll append this as a new
   section to the current case memo for [matter name].
   (Preferred — keeps everything in one evolving document.)

2. **Create as a standalone memo** — I'll produce this as a
   separate document.

Which do you prefer?
```

If the user chooses option 1:
- Ask for the existing case memo (if not already in context).
- Add the new content as a clearly labeled new section with
  a date stamp and section title.
- Maintain the existing content unchanged.
- Update the table of contents if one exists.
- The section header format should be:

```
══════════════════════════════════════════════════
[SECTION TYPE] — Added [Date]
══════════════════════════════════════════════════
```

For example:
```
══════════════════════════════════════════════════
RESPONSE PLAN MEMO — Added March 1, 2026
══════════════════════════════════════════════════
```

or:

```
══════════════════════════════════════════════════
COMPILED RESEARCH MEMORANDUM — Added March 3, 2026
══════════════════════════════════════════════════
```

If the user chooses option 2:
- Produce the deliverable as a standalone .docx as normal.

### Important Notes

- Never overwrite or modify existing sections when adding new ones.
- If this is the FIRST deliverable for a matter (e.g., the initial
  case assessment), there is no existing memo to append to. In that
  case, produce it as a standalone document — it becomes the seed
  of the evolving case memo.
- The evolving case memo should maintain a running table of contents
  at the top listing all sections with dates.

---

## Pattern 2: Client-Facing Memos

### Principle

Internal work product often contains analysis, strategy, and
candid assessments that should not be shared with clients. But
clients benefit from seeing a polished, professional memo that
demonstrates the quality of our analysis without exposing internal
deliberations. Client memos showcase our ability to produce
hyperlinked, well-cited, clearly written legal analysis.

### When to Apply

At the conclusion of producing ANY of these deliverables:
- Initial Case Assessment
- Response Plan Memo
- Compiled Research Memorandum
- Any analytical memo that could have a client-facing version

### What to Do

After delivering the internal memo, ask the user:

```
Would you like a client-facing version of this memo?

1. **No** — Internal version only.

2. **Yes** — I'll create a client-ready version now.

3. **Yes, but let me revise the internal memo first** — Make
   your edits, then come back and I'll generate the client
   version from the revised memo.
```

If the user chooses option 2, generate the client memo immediately.
If option 3, wait for the user to return with the revised memo.

### Client Memo Guidelines

When producing a client-facing version:

**Include:**
- Clear statement of the legal issues
- Summary of relevant legal standards and authorities
- Key cases with proper citations (hyperlinked where possible)
- The strength of the client's position (in measured terms)
- Recommended next steps
- Professional formatting with firm header

**Exclude:**
- Internal strategy discussions ("we should frame this as...")
- Candid assessments of weaknesses that are attorney work product
- Traffic light ratings and internal classification systems
- Cost estimates and billing projections
- References to AI-assisted drafting
- Internal "open items" and research gap lists
- Anything that reads as attorney-to-attorney deliberation

**Tone:**
- Confident but measured (not the internal candor voice)
- Accessible to a sophisticated layperson
- Professional, not casual
- Frame uncertainties as "considerations" not "risks we're worried about"

**Format:**
- Standalone .docx with KLG header
- Title: "Legal Memorandum — [Topic]"
- "Prepared for [Client Name]" not "Prepared by AI"
- Include a brief cover note if appropriate
- Hyperlink case citations where possible

### Sequencing

The client memo question should come AFTER the iterative case
memo question. The flow is:

1. Produce the deliverable
2. Ask: standalone or add to case memo? (Pattern 1)
3. Deliver the internal version
4. Ask: client-facing version? (Pattern 2)
5. If yes, produce the client memo

---

## Pattern 3: Incremental Session Logging to Notion

### Principle

Every Claude session that produces work product for a matter
should be logged to the Notion Research database as a permanent
record. Logging happens incrementally — after each substantive
response, Claude offers to create or update the session log.
This ensures nothing is lost if a session ends unexpectedly,
and keeps the Notion record current throughout the conversation.

### When to Apply

**This pattern is triggered globally, not by individual skills.**
It applies to every substantive response in a session that
relates to a specific matter — whether that session is a formal
skill execution (case assessment, response plan, etc.) or an
ad hoc analysis, brainstorming, or research question.

"Substantive response" means any response that involves legal
analysis, produces work product, or advances the matter. It
does NOT include:
- Trivial exchanges ("thanks" / "you're welcome")
- Mode selection prompts (Cowork vs. Chat questions)
- Clarifying questions before work begins
- Sessions unrelated to a specific matter (pipeline development,
  skill editing, system configuration)

### The Per-Response Prompt

After every substantive response in a matter-related session,
Claude appends a brief, unobtrusive offer:

```
📝 Update the Notion session log? (yes / not yet / always / never)
```

This goes at the very end of the response, after all substantive
content. It should be a single line — not a block or a big
callout. Keep it lightweight so it doesn't disrupt the flow.

### User Responses and What They Mean

- **"yes"**: Create the page (first time) or append the latest
  exchange(s) to the existing page.
- **"not yet"**: Skip this response. Ask again after the next
  substantive response.
- **"always"**: Auto-log after every response for the rest of
  this session. Do not ask again — just log silently.
- **"never"**: Stop offering for this session entirely. Do not
  ask again.

If the user ignores the prompt and asks a new question instead,
treat that as "not yet" — carry the unlogged exchanges forward
and include them in the next update.

### First-Time Setup (Creating the Page)

The first time the user says "yes" (or on the first auto-log if
"always" was selected), Claude needs to set up the Notion page:

**Step 1: Identify the Case Portal entry.**

If the case name and Case Portal entry are obvious from context
(e.g., the user is in a Cowork session with a matter folder, or
the case name is in the conversation), proceed. If not, ask:

```
Which case portal entry should this session be linked to?
```

**Step 2: Get the Chat URL (Chat sessions only).**

If this is a Chat session (not Cowork), ask:

```
Please paste the chat URL from your browser's address bar
so I can link it in the Notion page. (Or type "skip" to
log without the URL.)
```

For Cowork sessions, skip this — there is no persistent URL.

**Step 3: Create the Notion page.**

Create a page in the Research database
(data source: `collection://622bfafd-45b1-451a-b518-f72d86767cb0`)
with these properties:

- **Title**: `[Case Name] — [Topic or Skill Name] [Session Type] Log — [Date]`
  - Session Type is "Chat" or "Cowork"
  - Date format: March 4, 2026
  - For skill executions, use the skill name as the topic:
    `Burris-Toles — Response Plan Chat Log — March 4, 2026`
  - For ad hoc sessions, use a descriptive topic:
    `Diller v. Weiss — Mootness Risk Analysis Cowork Log — March 4, 2026`
- **Case Portal**: relation to the appropriate Case Portal entry
- **Tags**: `["Claude Session Log"]`
- **Date**: today's date
- **URL**: the Claude chat URL (Chat sessions only; leave blank
  for Cowork)
- **Publish or Pass?**: `Not Applicable`
- **Note**: 1–2 sentence summary of the session so far
  (update this on subsequent logs if the scope evolves)

**Step 4: Write the initial page content.**

The page body should contain:

1. A **Session Summary** section at the top:
   - Session type (Chat or Cowork)
   - Date and approximate time
   - Skill used (or "Ad hoc" for non-skill sessions)
   - Matter folder path (for Cowork sessions)
   - Chat URL (if available), formatted as a clickable link

2. A **Transcript** section with each question-and-answer pair
   under its own toggle:

```
<details>
<summary><strong>Q:</strong> [Abbreviated version of the user's question — first ~80 characters]</summary>

**User:**
[Full text of the user's message]

---

**Claude:**
[Full text of Claude's response]

</details>
```

Include ALL substantive exchanges from the session up to this
point — not just the most recent one.

### Subsequent Updates (Appending to Existing Page)

On subsequent "yes" responses (or auto-logs if "always" mode),
Claude appends the new exchange(s) to the existing Notion page
using `insert_content_after`. Append after the last toggle in
the Transcript section.

Also update the Session Summary if the scope has evolved (e.g.,
a new deliverable was produced, or the analysis shifted
direction). Update the **Note** property if the summary has
materially changed.

### Content Rules for the Transcript

- Include ALL substantive exchanges. Omit only trivial
  back-and-forth (e.g., "thanks" / "you're welcome").
- For very long responses (e.g., full memo drafts), include
  the complete text. Do not truncate.
- Preserve code blocks, citations, and formatting from the
  original exchange.
- If Claude produced a file (e.g., .docx), note the filename
  in the response section: "[Produced file: case-assessment.docx]"
- For multi-turn exchanges within a single logical task, group
  them under one toggle if they're tightly related, or separate
  toggles if they address distinct questions.
- Do NOT include the "📝 Update the Notion session log?" prompt
  itself in the logged transcript.

### Cowork Session Specifics

Cowork sessions have no persistent URL, but they are otherwise
logged identically to Chat sessions:

- Title includes "Cowork" instead of "Chat"
- URL property is left blank
- Session Summary notes "Cowork Session" and includes the
  matter folder path from the Cowork context panel
- If the Cowork session accessed specific files from the matter
  folder, list them in the Session Summary under "Files accessed"

### Relationship to Patterns 1 and 2

Session logging is independent of Patterns 1 and 2. It runs
throughout the session, while Patterns 1 and 2 trigger at
specific delivery milestones. There is no sequencing dependency
between them.

### When NOT to Log

- Sessions that don't relate to a specific matter (e.g., general
  pipeline development, skill editing, system configuration)
- Sessions where the user has said "never" for this session
- Trivial interactions (e.g., "What can you do?" → Quick Start)
- Responses that are purely procedural (mode selection, file
  upload instructions, clarifying questions)

---

## How Skills Should Reference These Patterns

Each skill's SKILL.md should include in its execution rules:

```
[N]. After producing the final deliverable, follow the workflow
     patterns in `references/workflow-patterns.md`:
     - Pattern 1 (Iterative Case Memo): Ask whether to add
       to existing case memo or produce standalone.
     - Pattern 2 (Client Memo): Ask whether a client-facing
       version is needed.
```

Pattern 3 (Session Logging) is handled globally per the
project's `claude.md` and does not need to be referenced in
individual skill execution rules. It triggers automatically
after every substantive response.

Skills should read `references/workflow-patterns.md` and follow
the exact prompts and guidelines described there.
