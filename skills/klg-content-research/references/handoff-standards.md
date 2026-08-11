# KLG Pipeline Handoff Standards

## Core Principle

Every KLG AI skill that requires a human handoff must provide
crystal-clear, step-by-step instructions at the transition point.
The entire KLG team uses these skills — not just the attorney who
designed the workflow. Every handoff must be fool-proof.

## Handoff Instruction Requirements

At every handoff point, the skill must provide:

1. **What just happened** — 1–2 sentences confirming what was
   completed in this step.
2. **What to do next** — Numbered, sequential steps. Each step
   must be a single concrete action. No ambiguity.
3. **Where to go** — Include URLs, file paths, or database names.
   Use actual links, not placeholders, whenever possible.
4. **What to say** — Provide the exact trigger phrase to give
   Claude (or Comet) to start the next step. Put it in bold
   or a code block so it's copy-paste ready.
5. **What to expect** — Tell the user what will happen after
   the handoff (how long it takes, what the output looks like).
6. **What could go wrong** — Flag common failure modes and
   what to do if they occur.

## Formatting Standard

Use this visual format for all handoff instructions:

```
═══════════════════════════════════════════════════
✅ STEP [N] COMPLETE: [what just happened]
═══════════════════════════════════════════════════

WHAT TO DO NEXT:

1. [First concrete action]
2. [Second concrete action]
3. [Third concrete action]
   → [Sub-step if needed]
4. [Action that triggers the next AI step]

TRIGGER PHRASE (copy-paste this to Claude/Comet):
───────────────────────────────────────────────────
[exact phrase]
───────────────────────────────────────────────────

⏱️ EXPECTED: [what happens next and how long]
⚠️ IF SOMETHING GOES WRONG: [troubleshooting]
═══════════════════════════════════════════════════
```

## Pipeline-Specific Handoffs

### Research Pipeline (Skills 3 → 4)

The research pipeline has these handoff points:

1. **Claude → Human → Comet** (Skill 3 output)
   Claude creates the Notion Research page with prompts.
   Human gives the Notion page URL to the Comet agent.
   Comet launches Deep Research sessions AND pastes results
   back into the Notion page.

2. **Comet → Human → Claude** (Skill 4 Phase A trigger)
   Comet finishes all research and pastes into Notion.
   Human tells Claude: "The research memos are ready."
   Claude reads the Notion page and compiles.

3. **Claude → Human → Comet** (Skill 4 Westlaw handoff)
   Claude generates the Westlaw authority list.
   Human gives the list to Comet for Westlaw Find & Print.
   Comet downloads the PDF.

4. **Comet → Human → Claude** (Skill 4 Phase B trigger)
   Human uploads the Westlaw PDF to the matter folder.
   Human tells Claude: "The Westlaw authorities are downloaded."
   Claude finalizes the research package.

## Voice

All handoff instructions should be written in the KLG Style
Guide voice: direct, friendly, no jargon, active voice. Write
as if you're explaining to a competent colleague who has never
done this particular task before.
