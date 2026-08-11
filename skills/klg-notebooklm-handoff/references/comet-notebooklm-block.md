# Comet NotebookLM Automation Block — Canonical Template

## Purpose

This is the drop-in agent-instruction block that goes inside the
NotebookLM handoff Notion page. Comet reads it as a self-contained
workflow and executes without further human input. Replace the
`{{PLACEHOLDER}}` values with matter-specific content. Do not
modify the structural language — Comet is sensitive to imperative
voice and explicit waits.

---

## Template

````
═══════════════════════════════════════════════════════════
COMET AGENT INSTRUCTIONS
═══════════════════════════════════════════════════════════

You are operating as an autonomous browser agent. Execute the
workflow below without asking the user for confirmation between
steps. The user has uploaded all sources and prepared everything
you need.

CAPABILITIES YOU NEED:
- Navigate to web URLs
- Wait for page elements to render
- Type text into input fields
- Click buttons
- Copy text from rendered chat responses
- Switch between browser tabs
- Paste text into Notion pages under specific headings

PRECONDITIONS (the user has done these):
- A NotebookLM notebook has been created at the URL below
  containing all source documents
- This Notion page is open in a separate browser tab
- You have edit access to this Notion page

NOTEBOOK URL: `[PASTE NOTEBOOK URL HERE]`

WORKFLOW:

1. Navigate to the notebook URL above.

2. For each prompt in the PROMPT QUEUE section below, in order:
   a. Click the chat input field at the bottom of NotebookLM.
   b. Paste the full prompt text exactly as written. Do not
      modify, summarize, or shorten it.
   c. Submit the prompt (press Enter or click the send icon).
   d. Wait for the response to fully complete. NotebookLM is
      finished generating when (i) the "Stop generating" control
      is replaced by a regenerate icon, AND (ii) the inline
      source citations like [1] [2] [3] have rendered after
      the text.
   e. Copy the entire response text, including the inline
      citations.
   f. Switch to the Notion tab containing this page.
   g. Locate the heading that matches the prompt's PASTE TARGET
      value (e.g., `## DIGEST — Hearing transcripts`).
   h. Paste the response immediately below that heading,
      replacing any placeholder text under it.
   i. Switch back to the NotebookLM tab and proceed to the next
      prompt.

3. After all prompts are executed, return to this Notion page
   and paste the following text under `## CLOSE-THE-LOOP`:

   ✅ Comet automation complete. All {{PROMPT_COUNT}} prompts
   executed and findings posted. Ready for Claude integration.
   — [timestamp]

ERROR HANDLING:
- If a NotebookLM response appears truncated or fails,
  regenerate once. If it fails again, paste
  `[GENERATION FAILED — RETRY MANUALLY]` under the target
  heading and continue to the next prompt.
- If you cannot find the paste-target heading on the Notion
  page, paste the response at the bottom of the page with a
  note identifying which prompt it belongs to.
- Do not edit or summarize any response — paste verbatim.
- Preserve the inline `[N]` source citations from NotebookLM.
  They are valuable for verification.

STOP CONDITION:
All {{PROMPT_COUNT}} prompts in PROMPT QUEUE have been executed
and pasted under their target headings. Close-the-loop
confirmation has been posted under `## CLOSE-THE-LOOP`.

═══════════════════════════════════════════════════════════
END COMET AGENT INSTRUCTIONS
═══════════════════════════════════════════════════════════
````

## Placeholder values

| Placeholder | Replacement |
|---|---|
| `{{PROMPT_COUNT}}` | Total number of prompts in the queue (count after assembling) |
| `[PASTE NOTEBOOK URL HERE]` | Leave verbatim — user replaces with actual URL after building notebook |

## Style rules

- Use box-drawing characters `═══` for the section borders.
  Comet recognizes these as block delimiters.
- Use imperative voice throughout. No "you might want to," no
  "if you'd like," no "as needed."
- Capability declaration must come before workflow steps. Comet
  uses the capability list to confirm it can execute.
- Stop condition must be explicit and verifiable.
- Error handling must give Comet a path to continue when something
  fails. Without explicit error handling, Comet will halt on first
  failure and ask the user — defeating the autonomy.

## What goes outside this block

The Comet block is self-contained for the AUTOMATION. But the
Notion page also includes:

1. **Above the Comet block:** Quick start instructions for the
   human (Tim or Brittney) — how to build the notebook, where to
   paste the URL, how to launch Comet.
2. **Above the Comet block:** Source upload checklist (checkboxes).
3. **Inside or after the Comet block:** The PROMPT QUEUE itself,
   with each prompt clearly delimited and a PASTE TARGET value.
4. **Below the Comet block:** Output zones (empty paste-target
   headings).
5. **Below the output zones:** Close-the-loop section.
6. **Bottom of page:** Manual review prompts (audio overview, etc.).

The PROMPT QUEUE can be inside or after the Comet block. Inside
is cleaner — Comet reads one continuous instruction set.

## Why this format works

Per KLG operational learnings: "Notion research pages need
self-contained automation commands (not human-tutorial style)
with explicit capability declarations and stop conditions, so
Comet executes as a browser agent rather than deferring."

Comet has a tendency to defer to the user when instructions are
written conversationally. Explicit imperative voice + capability
declaration + stop condition = autonomous execution.
