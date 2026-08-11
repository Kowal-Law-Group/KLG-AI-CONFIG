---
name: klg-prebill-audit
description: "Monthly pre-bill hardening audit. Scans a Clio time-entry export before bills are finalized and flags the fee entries that draw cuts on a later fee motion: long entries with thin descriptions, block billing, duplicate or near-duplicate narratives, intra-firm conferencing, clerical work billed at professional rates, vague conferences/emails with no subject, and billing-hygiene problems. Produces an .xlsx workbook with a suggested-supplement column the billing team works through. Use whenever the user says 'pre-bill audit', 'audit our pre-bills', 'review the pre-bills', 'bill review', 'clean up the time entries', 'fee entry audit', 'harden the bills', 'monthly billing review', 'block billing check', 'fee bill QC', 'are our bills defensible', or uploads a Clio time export for billing review. Run it every month before finalizing bills, and again before assembling any fee motion. NOT for drafting the fee motion, computing the lodestar, or substantive case work."
---

# KLG Pre-Bill Audit

## Purpose

Fee entries that survive a contested fee motion and fee entries that
read well to a paying client are the same entries. Courts cut time for
predictable reasons: a five-hour block that says "continue working on
AOB," two consecutive days with the identical narrative, "e-filing,
formatting, bookmarking, uploading" billed at a paralegal rate, a
conference billed by three timekeepers at once. Those cuts are
avoidable. The fix is not better arguments after the bill is
challenged — it is catching the patterns before the bill goes out.

This skill runs a deterministic scan over a month's time entries,
surfaces every entry that matches a known cut pattern, and hands back
a working list the billing team can act on: supplement the thin
narratives, split the block-billed entries, write off the clerical
time, and confirm the duplicates are distinct work. The goal is bills
that are transparent to the client and unshakeable on a fee motion.

The single highest-value catch is the long-block-thin-description
pattern — the entry that is two or more hours with a narrative too
vague to test. That is the pattern that produced the largest cut in
the order this skill was built from.

## When to Run

Two recurring triggers:

1. **Monthly, before finalizing pre-bills.** Run it on the month's
   Clio export, work the flagged list, then finalize and send. This
   is the primary use.
2. **Before assembling any fee motion.** Run it across the full
   recoverable period so the records are hardened before they go in
   front of a court.

This is firm-wide operational QC, not matter work. It does not need a
Case Portal entry or a project page, and it is Chat-native — upload
the export and run. No SharePoint or matter-folder access required.

## Required Inputs

- A **Clio time-entry export for the period** (.csv preferred). The
  export needs, at minimum, columns for date, timekeeper, hours, and
  description; rate, amount, and matter columns make the output more
  useful. Column headers vary between Clio exports — the script maps
  them automatically via aliases and tells you if it cannot resolve a
  required column.
- If only a **pre-bill PDF** is available, extract the entries to a
  CSV first (date, timekeeper, matter, hours, rate, description), then
  run the script on the CSV. Do not try to scan the PDF directly — the
  detection logic needs structured columns.

## Workflow

### Phase 1 — Mechanical scan (the script does this)

Run the detection engine. It is deterministic and reproducible — the
same export always produces the same flags — which is what you want
for a recurring QC pass.

```bash
cd <skill-dir>
pip install openpyxl --break-system-packages   # if not already present
python scripts/prebill_audit.py <export.csv> -o <Period>_prebill_audit.xlsx --period "<Month Year>"
```

The engine over-flags on purpose. It is tuned for recall: better to
surface a borderline entry the human clears in two seconds than to
miss a real one. Precision is the human's job in Phase 2, except for
clerical detection, which uses word-boundary matching to avoid
flagging substantive work.

What it flags, and why each one gets cut — full doctrinal grounding is
in `references/fee-cut-doctrine.md`:

- **Long entry, thin description** — at or above 2.0 hours with a
  narrative too short or too generic to test. The marquee cut pattern.
- **Block billing** — multiple discrete tasks lumped in one entry. A
  court cannot assess the reasonableness of any single task, so it
  discounts or strikes the block.
- **Duplicate / near-duplicate** — same or near-identical narrative by
  one timekeeper within the period. Reads as the same work billed
  twice even when it is not.
- **Intra-firm conference** — two or more timekeepers billing the same
  meeting on the same day. Confirm multiple billers were necessary.
- **Clerical / non-billable** — filing, formatting, bookmarking,
  uploading, calendaring, memoranda of costs. Overhead, not separately
  compensable at a professional rate.
- **Conference/email without subject** — a communication entry with no
  "re." The client and the court should both see what was discussed.
- **Large single block / billing judgment** — any entry at or above
  6.0 hours, surfaced for a judgment call.
- **Off-increment, missing description, bad duration, possible
  cross-matter reference** — hygiene checks.
- **Firm-level note** — if too high a share of entries land on
  whole/half hours, the bill reads as estimated rather than
  contemporaneous.

Thresholds and keyword lists live in the `CONFIG` block at the top of
the script. Tune them to firm policy; do not hand-edit the export.

### Phase 2 — Judgment layer (Claude does this)

Open the workbook and work the **Flagged Entries** sheet. For each
flagged entry, exercise the judgment the script cannot:

1. **Cull false positives.** Some flags will be clearly fine on a read
   (a genuinely substantive 3-hour entry that happens to be terse, a
   "conference" that is actually with opposing counsel and properly
   billed). Note them as cleared in the Resolution column rather than
   deleting the row — the cleared list is itself a record of judgment
   exercised.
2. **Write the suggested supplement.** For thin and block-billed
   entries, draft a replacement narrative in the "Suggested fix /
   supplemented language" column that itemizes the discrete tasks and
   says what each produced — drawn only from what the work actually
   was. Do not invent detail. If the underlying work is unknown, mark
   the entry for the timekeeper to supplement, not for Claude to guess.
3. **Pair the duplicates and conferences.** For each duplicate cluster
   and each intra-firm conference, state the question the biller needs
   to answer (distinct work? necessary second attendee?) so the
   resolution is a yes/no, not an essay.
4. **Roll up the numbers.** Confirm the Summary sheet's flagged hours
   and dollars, and call out the two or three timekeepers or matters
   carrying the most exposure.

Hold the line on the firm's standards while doing this: no boilerplate
padding, active verbs, real task detail. A supplemented narrative that
is merely longer and vaguer is worse than the original.

### Phase 3 — Deliver

Present the workbook and a short summary covering: total flagged hours
and dollars, the worst two or three patterns this month, and the
specific timekeepers who should adjust capture habits. Keep it tight —
the billing team works the workbook, not the summary.

If the user wants it routed, offer to post a brief note to the billing
or operations channel pointing the team to the workbook (follow the
Slack and handoff rules in `claude.md` — introduce yourself, bare
URLs, action items separated from reference).

## Output

A single .xlsx workbook:

- **Summary** — counts and flagged hours/dollars, broken down by issue
  category and by timekeeper, plus firm-level notes.
- **Flagged Entries** — one row per flagged entry, sorted by severity
  then hours, with the original narrative, every issue flagged, a
  column for Claude's suggested supplement, and a Resolution column the
  billing team fills in.

The workbook is the working artifact. The billing team edits Clio from
it; the cleared-and-resolved workbook is the month's audit record.

## Additional hardening guidelines

Beyond the automated scans, these are worth a human eye each month —
some are hard to automate reliably, all of them harden the bill:

- **Top-heavy staffing.** Senior-rate time on work a junior or
  paralegal should carry (routine research, document assembly) invites
  a rate or hours reduction and is delegable. Flag senior timekeepers
  on plainly delegable tasks.
- **Review-stacking.** Layers of "review and revise" on the same
  document by multiple attorneys. Some supervision is reasonable;
  three passes on a routine filing is not.
- **Write-down candidates.** Long entries the timekeeper would discount
  on reflection. Surface them for a billing-judgment call rather than
  sending full value and hoping.
- **Travel time at full rate.** Confirm travel is billed per firm
  policy (often reduced), not at the full hourly rate.
- **Proportionality.** Time that is large relative to the task (hours
  to "review a one-page order"). The script flags magnitude; the human
  judges proportion.
- **Privilege and work-product exposure.** Narratives detailed enough
  to reveal strategy. Specificity defeats vagueness cuts but should not
  hand the other side a roadmap — find the line.

## The institutional point

This audit is a backstop, not the cure. Every entry it flags is an
entry that should have been captured cleanly the first time. The
durable fix is contemporaneous, task-itemized capture — timers running
in real time, one task per entry, a stated subject on every
communication. Use the monthly pattern data to coach the specific
habits driving the flags, so next month's list is shorter. Fix the
system, not just the instance.

## A note on the authorities

`references/fee-cut-doctrine.md` names the leading California and
federal cases behind each cut category. Confirm every citation,
pinpoint, and year against the source before any of it appears in a
filed fee motion — the reference file is internal training material,
not verified citation text.
