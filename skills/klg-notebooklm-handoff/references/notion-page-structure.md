# NotebookLM Handoff Page — Notion Page Structure

This is the canonical layout for the NotebookLM handoff page in
the Research database. The skill assembles content into this
structure.

## Page properties

| Property | Value |
|---|---|
| Title | `NotebookLM Handoff — [Matter Short Name] ([Posture])` |
| Icon | 🎧 |
| Case Portal | linked to matter's Case Portal entry |
| Projects | linked to parent project (if any) |
| Tags | Claude Session Log |
| Salience | ★★★ |

Title posture suffix examples:
- `(Phase 2a — MSJ Opposition)`
- `(AOB Stress Test)`
- `(RB Defense Audit)`
- `(Case Assessment Supplement)`
- `(Research Synthesis)`

## Page layout

The page has eight ordered sections. Section names with `═══`
borders are visually emphasized so Comet (and humans) can find
them at a glance.

### 1. Header / metadata

A short bullet-style block at the top with: matter name and case
number; phase; driver (Comet); tool (NotebookLM); status. No more
than 5–6 lines.

### 2. Quick start (for Tim or Brittney before launching Comet)

A numbered 4-step list:
1. Build the NotebookLM notebook (link to notebooklm.google.com,
   notebook title to use, source upload reference)
2. Paste the notebook URL into the `[PASTE NOTEBOOK URL HERE]`
   placeholder in the Comet block
3. Open this Notion page in a second tab; launch Comet
4. When Comet posts the close-the-loop confirmation, message
   Claude in chat with the trigger phrase (provide the exact
   phrase)

### 3. Source upload checklist

Checkbox list grouped by source category. Each item is one source
to upload. Categories appear in this order:
- Drafting record
- Research foundation
- Opposing party's papers (if applicable)
- Court opinions
- Trial record
- Operative pleading and procedural posture
- Co-counsel correspondence

Tailor the checklist to the matter — do not list categories that
do not apply, and do not list generic placeholders. List actual
documents.

### 4. ═══ COMET AGENT INSTRUCTIONS ═══

The Comet automation block from `comet-notebooklm-block.md`. Box-
drawing borders. Self-contained imperative agent instructions.
Workflow steps with explicit waits and error handling. Stop
condition.

### 5. ═══ PROMPT QUEUE ═══

The full prompt list, in execution order. Each prompt is delimited
with:

```
### PROMPT [N] — [Short label]

**PASTE TARGET:** `## [Heading text]`

**PROMPT TEXT:**

```
[full prompt text]
```
```

The PROMPT TEXT is wrapped in triple backticks so Comet can copy
the prompt cleanly from a code block.

After the last prompt, emit `### END OF PROMPT QUEUE` to mark the
boundary clearly.

### 6. ═══ OUTPUT ZONES ═══

Empty paste-target headings, one per prompt, in the same order
Comet executes. Each heading is followed by `*(Awaiting Comet
output.)*` placeholder text on the line below.

The heading text under OUTPUT ZONES must EXACTLY MATCH the
PASTE TARGET value in the corresponding prompt. If they don't
match character-for-character, Comet will fail to find the
target.

### 7. CLOSE-THE-LOOP

A single section heading `## CLOSE-THE-LOOP` followed by italic
placeholder text describing what Comet posts here when finished
and what the user does next. Comet replaces the placeholder with
the completion confirmation.

### 8. Manual review prompts (run these yourself)

Audio overview prompts and any other prompts that Comet cannot
automate. Always include a brief note explaining why these are
manual ("Comet cannot capture audio" or similar).

### 9. Notes for Claude (post-Comet integration)

Brief instructions for Claude on what to do when the user returns
saying Comet finished. List the next-phase skills that will
consume the digests:
- Brief rewrites: `klg-brief-elevation`
- Declarations drafting: read deposition and exhibit digests
- Oral argument prep: `klg-oral-argument` reads opinion and
  working draft digests

This section is for Claude's benefit in a future session — it
ensures the digests get used.

## Heading conventions

Use these exact heading patterns so Comet's heading-matching is
reliable:

- Output zone headings always start with `## ` (H2)
- Output zone headings use the pattern `## [TYPE] — [Specifics]`
  where TYPE is one of: OUTPUT, DIGEST, EVIDENCE INVENTORY,
  GAP ANALYSIS, DEFENSE PREEMPTION, AUTHORITY DEPLOYMENT,
  BRIEF ECONOMY, CROSS-MSJ, THEORY CONVERGENCE AND DIVERGENCE,
  IMPACT ON PRIOR ANALYSIS
- The em dash separator between TYPE and specifics is a real em
  dash (U+2014), not two hyphens
- Section dividers (Comet block, prompt queue, output zones) use
  `═══════════════════════════════════════════════════════════`
  (box-drawing horizontal line, U+2550, repeated)

## Why this layout works

Comet processes the page top-to-bottom. The Quick Start tells the
human what to do first. The source checklist forces the human to
verify the upload before launching Comet. The Comet block is
visually unmistakable so Comet recognizes it as agent instructions
rather than narrative. The prompt queue is delimited so each prompt
is parseable. The output zones below give Comet explicit paste
targets. The close-the-loop section closes the workflow.

The page is also human-readable — Tim can scroll through it after
Comet finishes and read each digest in sequence without having to
hunt for content.
