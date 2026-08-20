# KLG Skill Eval Harness

Regression testing for KLG's `SKILL.md` files, built on Anthropic's
`skill-creator` eval tooling (`evals.json` / `grading.json` / `benchmark.json`
schemas and `eval-viewer/generate_review.py`). Delegation-batch Task #11.

## What this is for

Every time a claude.md rule or a `SKILL.md` changes (a style rule, a
citation format, a workflow step), there's a real chance an existing skill
stops honoring it — the skill file wasn't touched, but the global rule it
depends on shifted, or the skill's own rewrite introduced a regression
elsewhere. This harness gives a repeatable way to check: hand the skill a
realistic prompt, capture what it actually produces, and grade the output
against explicit, checkable assertions tied to the specific rules at stake.

This is **not** a benchmark of whether a skill is worth having (that's
skill-creator's normal with_skill vs. without_skill comparison). It's a
compliance smoke test: does the skill, as currently written, still produce
output that follows the current global rules.

## Layout

Each skill that has evals keeps them with the skill itself, per
skill-creator's own convention:

```
skills/<skill-name>/evals/evals.json   # prompts + assertions for that skill
```

Run results live here, in `eval-harness/`, organized by a workspace name and
iteration (skill-creator's own convention, kept separate from the skills
tree so results don't get committed as if they were part of the skill):

```
eval-harness/
  <workspace-name>/
    iteration-N/
      eval-<id>-<descriptive-name>/
        eval_metadata.json
        with_skill/
          outputs/output.md      # what the skill actually produced
          grading.json           # assertion-by-assertion grade + evidence
      benchmark.json             # aggregated pass rates across all evals in the iteration
```

## Pilot run (2026-08-19)

First run of the harness. Scope was deliberately narrow: 3 skills, 1 eval
each, chosen because they're the skills most directly exercised by this
session's own rule changes — a "did we just break the thing we changed"
check, not a firm-wide audit.

- **klg-cite-check** — placeholder-flagging eval, testing the `[VERIFY:
  short description]` tag unification (claude.md v0.9.0) and the
  pre-filing safeguard.
- **klg-brief-elevation** — typography-and-heading-labels eval, testing the
  em-dash Typography rule and the full-path heading-label convention
  (claude.md v0.9.0 / Task #8).
- **klg-style-guide-check** — forbidden-phrases-and-em-dash eval, testing
  the pre-existing forbidden stock-phrase list together with the new
  em-dash rule, since this skill is the one meant to enforce both.

Result: all 3 pilot skills passed every assertion (4/4, 4/4, 7/7) on their
one fabricated-fixture prompt. See `pilot-workspace/iteration-1/benchmark.json`
for the graded detail, or open the delivered static viewer HTML to read the
actual outputs side by side with the grading.

**Read the pass rate honestly.** This is 1 run per eval, no repeated
trials, no adversarial or edge-case prompts, and no automated grader — I
graded each output against its checklist by reading it, the same way the
grading.json evidence fields show. A 100% pass rate here means "no
regression detected on this one prompt," not "this rule can't be broken."
Expanding trial count, adding harder/adversarial prompts per skill, and
covering the remaining ~19 firm skills is future work, not done here.

**Explicitly not covered by this pilot:** the TOC-block rule and the
fetch-patch-verify protocol (Tasks #9 and #10). Both govern how Claude edits
a live Notion page over multiple turns, not what a one-shot prompt-in/
output-out skill produces — they don't fit this eval format without a
multi-turn Notion-session harness, which is a larger build than this pilot.
Spot-check those two directly in a live Notion session instead.

**Correction (2026-08-19, same day):** 2 of the 11 assertions in this pilot
(the "doubled modifier" checks in the klg-brief-elevation and
klg-style-guide-check evals) were described and graded as if they tested a
claude.md rule. They don't — claude.md has no doubled-modifier rule.
That rule exists only in KLG's separate Cowork org-level instructions
(set in the Cowork admin settings, not in this repo). The pass/fail
results themselves are unaffected, but the rule attribution was wrong.
Left the assertions in place since they're a reasonable style check
either way, and logged a backlog item — "Bring claude.md style rules in
line with the firm's Cowork org-level instructions" — to close the actual
gap (doubled modifiers, throat-clearing, the file-ready/final language
ban, and the fix_docx_standalone.py-after-pack.py step all live in the
org instructions today but not in claude.md).

## Extending this

To add a regression eval for a skill:

1. Write a realistic test prompt using fabricated/fixture content — never
   real client data, per firm confidentiality rules.
2. Write assertions that are objectively checkable from the output alone
   (a phrase present/absent, a format followed, a fact not fabricated) —
   not subjective quality judgments.
3. Add the eval to that skill's `evals/evals.json` (create the file if it
   doesn't exist, using the schema in
   `/mnt/skills/examples/skill-creator/references/schemas.md`).
4. Spawn a subagent pointed at the skill's `SKILL.md` and the prompt, save
   its output, grade it against the assertions, and add the run to a new
   `eval-harness/<workspace>/iteration-N/` directory.
5. Run `generate_review.py --static` to produce a reviewable HTML and share
   it, the same way any other landing gets shared.

**Where this plugs into the landing pipeline:** when a future session lands
a claude.md or SKILL.md change (per `VERSIONING.md`'s promotion path), add
"run or update the affected skill's regression eval" as a step before
calling the change landed — the same way a code change would get a test
run before merge. This wasn't retrofitted onto the 5 rule-landings already
in this repo's history; starting it here, going forward.
