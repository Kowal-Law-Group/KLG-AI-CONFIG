---
name: klg-email-voice
description: >
  Draft or rewrite emails and Slack messages in Tim's actual voice
  — cold open, bold-prefix paragraph leads, short declarative
  sentences, confident unhedged takes, direct asks, signed "-Tim" —
  rather than formal brief-voice prose. Detects the recipient and
  tunes the register (bluntest with DZ, more formal with trial
  counsel, warmer with clients). Use whenever the user asks to
  draft an email, reply to an email, draft a Slack message in Tim's
  voice, or says "make this sound like Tim," "too formal," "sounds
  like a brief," "tighten this email," "draft a reply to DZ," or
  similar. NOT for brief prose or formal client memos — those go
  through the brief-voice conventions (klg-style-exemplars, once
  built) or the standard klg-response-plan/klg-case-assessment
  memo formats, which are deliberately more formal than this
  skill's email register.
---

# KLG Email Voice

## Purpose

Claude's drafted emails default to brief-voice: formal, slow to
the point, over-explained, structured with headers and parallel
lists. That's wrong for peer-to-peer email between appellate
lawyers who talk daily. This skill drafts or rewrites emails (and
Slack messages, which share the same voice problem) to sound like
Tim actually writes, not like a memo compressed into an email
wrapper.

This is the email-specific counterpart to the brief-voice work
(`klg-style-exemplars`, not yet built). Brief voice and email voice
are different enough — different length, cadence, audience, and no
citation patterns in email — that they're handled as separate
skills, but both draw cadence and structural moves from real
examples rather than imitating phrasing verbatim.

## Voice Patterns to Encode

These come from analysis of Tim's actual sent emails to DZ (May
2026) and hold across recipients, subject to the register tuning
below:

- **Cold open.** No "Thanks for the email," no "Hope you're well."
  The first sentence is the substance.
- **Bold-prefix paragraph leads instead of headers.** `**On the
  motion.**` `**On the 1542.**` `**Proposal:**` `**Looking
  forward:**` — not `## Section Heading`.
- **Short declarative sentences.** Verb-driven. Contractions
  throughout ("don't," "we're," "that's").
- **Direct questions when warranted.** "What's the rush?" "Am I
  missing something?" "What's the proposed scope?"
- **Confident, unhedged takes.** "About zero, I think." "That's a
  bad bargain." "Cleaner fit." State the position; don't wrap it in
  qualifiers unless there's a genuine, material uncertainty.
- **One-line answers when a one-line answer works.** Don't pad a
  simple answer with a doctrine walkthrough.
- **Direct ask at the end**, not a flowery sign-off. If the email
  needs something from the recipient, say what, plainly.
- **Sign off `-Tim`** — never "Best," "Regards," or "Sincerely,"
  when drafting as Tim.
- **Lists only when content is genuinely list-like**, and tight —
  no parallel structure imposed for its own sake.
- **Pushes back.** Challenges sloppy framings. Counter-questions
  when an assumption in the incoming email is wrong, rather than
  quietly working around it.
- **No throat-clearing legalese.** No "please be advised," no "I
  write to inform you," no "as discussed" as a filler opener.

## Workflow

1. **Read the reference notes.** If `references/voice-notes.md`
   exists in this skill folder, read it — it holds the distilled,
   evolving voice principles (the list above is the seed; the
   reference file is where refinements accumulate over time, per
   `my-writing-style`-style learning). If it doesn't exist yet,
   proceed on the seed patterns above.
2. **Calibrate to the relationship register.** Optionally pull 2-4
   recent sent emails from Tim to the same recipient via the M365
   connector (`sender=tim@kowallawgroup.com` + recipient filter) to
   confirm tone and cadence for that specific relationship before
   drafting. Skip this step for a first-time recipient with no
   prior thread.
3. **Draft or rewrite** applying the voice patterns above, tuned by
   the recipient register table below.
4. **Deliver through the inline message composer** (`message_compose_v1`
   for email, `slack_send_message_draft` for Slack), consistent
   with `claude.md`'s communication-delivery rules. Never send
   directly — draft only, for the attorney to review and send.

## Recipient Register

Detect the recipient and adjust:

| Recipient type | Register |
|---|---|
| DZ (David Zarmi) — peer co-counsel | Bluntest. Full voice pattern set, no softening. |
| Trial counsel (e.g., McCarthy) | More formal than DZ, but still cold-open and direct — not brief-voice. |
| Clients | Warmer and more explanatory than the DZ register — clients need the reasoning, not just the conclusion, but still short sentences and no legalese throat-clearing. |

If the recipient doesn't match a known pattern, default to the
trial-counsel register (moderate formality, still direct) and note
the assumption to the user.

## Scope Note

This skill covers both email and Slack messages, since they share
the same over-formality failure mode. It does not cover brief
prose, client memos, or any document that gets filed or read by a
court — those stay in their existing, more formal registers.

## What Not To Do

Don't imitate Tim's phrasing verbatim from past emails — draw the
cadence, structural moves, and tonal register, not a copy-paste
template. Don't add a doctrine walkthrough, a hedge, or a
contingency analysis where Tim's actual pattern is a flat,
confident answer. Don't add a header, a numbered list, or a formal
sign-off unless the content is genuinely list-like or the recipient
register calls for more formality.
