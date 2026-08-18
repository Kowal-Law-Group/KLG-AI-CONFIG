# Changelog

All notable changes to KLG's claude.md, klg-context.md, skill navigator, and
SKILL.md files are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). See `VERSIONING.md` for the
version-bump rules.

## [0.7.0] — 2026-08-18

### Added — narrow skill-updates cluster (Backlog Triage Lane 2)
8 of 11 items landed; 3 flagged back (see below).

- `klg-appendix-cites` — new Phase C (repagination rebuild for
  amended appendices: chronological-index extraction, mapping
  table, offset formula, tracked-changes redline), and a new Step
  A.5 (omitted-documents audit: full-document-set list, docket
  review, three-column reconciliation, attorney sign-off gate),
  renumbering the old Step A.5 (deliver) to A.6.
- `klg-cite-check` Phase B — SharePoint auto-sourcing before asking
  for a manual Westlaw upload; confidence-discipline rule (rate
  only from text read this session, never from training memory);
  the holding-accuracy table rebuilt as a proposition-support chart
  with Source/Signal/Confidence/Basis columns; bare-citation Find &
  Print list for unassessed authorities.
- `klg-oral-argument` — new Step B.4 (Step B.5 was Deliver, now
  renumbered): fresh-authority scan across each issue in the
  argument map for authority decided in the last 6–12 months,
  drafts a rule 8.254 letter for attorney review when genuinely
  new, and explicitly declines to draft one when an authority isn't
  clearly new (the Palmieri v. Foondos failure mode).
- `klg-dz-overlay` — new Phase 0: the three gating questions (pitch,
  ask, gazelle-or-squirrel) run before any merits deep-dive or
  hours estimate on a DZ-sourced matter.
- `klg-response-plan` — new "Payment Schedule" subsection (both
  modes) that proposes the three-checkpoint advance-payment
  schedule when a fee estimate exists, and asks the attorney to
  confirm before handing it to accounts — chose propose-and-confirm
  over silent auto-generation since it commits the client to
  payment dates.
- `klg-daily-triage` — new Pillar 5 (silent-task scan: Notion task
  pages created in the last 14 days with an assignee but no Slack
  broadcast in that window), wired into Mode A as Step A.6,
  renumbering A.6–A.8 to A.7–A.9.
- `klg-brief-elevation` + claude.md — subheading discipline rule
  ("no new heading unless the analysis exceeds ~2 pages or a
  distinct analytical step warrants separation") landed in both:
  the principle in claude.md's Brief Argument Structure, the
  enforcement (merge as tracked change) in brief-elevation's
  Appellate Style Rules.

### Flagged back — did not clear the Lane 2 bar
- **klg-daily-triage Think Tank hygiene scan**: the entry's own
  dependency (Think Tank added as a Projects Category in claude.md)
  isn't landed — confirmed no "Think Tank" references exist yet in
  claude.md's three-tier Category system. Adding a fourth category
  is a schema decision, not a narrow skill update.
- **Shepardizing step via Westlaw Litigation Document Analyzer**:
  the entry itself says "no design beyond identifying the gap" and
  poses an open architectural question (augment Find & Print, or
  replace it?) that Tim flagged for a manual pilot before automating.
- **New Petition for Supersedeas template**: the entry lists five
  open structural questions for an Attorney Roundtable (verification
  placement, memorandum integration, paragraph numbering, rule
  8.112 citation to verify, component order) and ends with "AI
  proposes; conventions are an attorney determination." Not mine to
  decide unilaterally.

## [0.6.1] — 2026-08-18

### Added
- Built the [KLG Brief Quality Rubric](https://app.notion.com/p/3c00fc06a06c81bb9194f59662dc6c75) Notion page — three sections (Brief Quality letter-grade rubric across 7 criteria, 100-point Ketchum-anchored Value Contribution framework, categorical Case Starting Difficulty) per the spec in ["Build KLG Brief Quality Rubric Notion page"](https://app.notion.com/p/3590fc06a06c81508cd3cc3d4d266eef). Marked v0.1, explicitly flagged as not yet attorney-calibrated. The two `Ketchum v. Moses` (2001) 24 Cal.4th 1122 citations were checked against a secondary source before use; the "Results obtained" component is left `[VERIFY]` — it's commonly paired with the Ketchum/Serrano factors in fee-award practice but wasn't confirmed this pass as a holding of either case specifically.
- Referenced the new rubric page from `klg-case-assessment` and `klg-brief-elevation`'s Required Context sections (item #5 and #9 respectively), per the backlog item's own sequencing note.

### Not done yet — flagged back, not landed
- **Seed Exemplar Database with 5–10 real exemplars**: re-reading the entry, this needs Tim to personally select "the briefs he's most proud of" — that's a judgment call, not something to guess at from this session. Doesn't clear the Lane 2 bar ("no Tim input needed"); recommend treating as Lane 3.
- **Standard linked views on project pages**: depends on the Work Product DB existing with a two-way Projects relation — and "Create Work Product database" is explicitly listed under Lane 1 (architecture, needs Tim, do not touch) in the Backlog Triage page. Can't be built without that dependency; flagged back rather than attempted.

## [0.6.0] — 2026-08-18

### Added
- claude.md — four of the five Batch 2 "claude.md style rules" from the
  Backlog Triage's Lane 2 list, each landed as a self-contained rule:
  - **Heart of a section up front** — new bullet in Brief Argument
    Structure: a section's thesis belongs in the preamble, not buried in
    a subsection. Fixes ["Style rule — heart of a section..."](https://app.notion.com/p/3620fc06a06c816b8a2cff7d9eede777).
  - **Active verbs over nominalizations/gerunds** — new bullet in Style
    Checks. Fixes ["Style rule — active verbs..."](https://app.notion.com/p/3620fc06a06c81f1b42bf096e5981df5).
  - **Heading conventions** — replaced the over-broad "sentence case
    with punctuation" heading rule (which mis-flagged "Issue Presented"
    and "Petition for Review" on a real petition draft) with the
    two-part rule: brief section labels are Title Case/no punctuation,
    argument headings are punctuated sentences. Fixes
    ["Heading conventions..."](https://app.notion.com/p/3b50fc06a06c812c8c8dd08341552670).
  - **Client Communication Voice** — new subsection under Client
    Communication Rules: first-person plural ("we"/"us") in client-facing
    communications signed under firm letterhead, not first-person
    singular. Fixes ["Use first-person plural..."](https://app.notion.com/p/35a0fc06a06c81a2b60ad0c64b12fb79).
- `klg-style-guide-check` — Category C rewritten to mirror the new
  two-part heading rule (so the redline stops flagging correct section
  labels); Category D extended to flag nominalization/gerund patterns;
  checklist table row updated to match both fixes.
- `klg-brief-elevation` — new Appellate Style Rules bullet: flag a
  section whose thesis is buried in a subsection rather than stated in
  the preamble.

### Not done yet
- The fifth item in that Lane 2 cluster, "Word round-trip for
  Notion-first drafts," is not a rule addition — the backlog entry
  itself frames it as an open workflow question ("bookmarked for a
  later workflow discussion") with no proposed fix to implement. Not
  landed here; flagged back to the triage as likely Lane 3 (needs a
  scope call), not Lane 2. See the entry's own page for detail.
- None of these four rules have been mirrored into the actual KLG
  Style Manual document (each backlog entry asks for both claude.md
  and the Style Manual) — this repo doesn't have that file. Needs
  Edwyn/Tim to apply the same four edits there.
- Same blocker as v0.5.0/v0.5.1: this claude.md still hasn't gone live
  in Tim's Project Knowledge. These four rules ship in the same
  standalone file already pending his upload — no separate action
  needed once that happens.

## [0.5.2] — 2026-08-17

### Changed
- README: repo confirmed pushed to GitHub through v0.5.1 (full history,
  all tags). Updated the GitHub URL — GitHub reported the repo moved
  from `Stuarth128/KLG-AI-CONFIG` (personal account) to the firm org,
  `Kowal-Law-Group/KLG-AI-CONFIG` — and rewrote the push instructions to
  use `git remote set-url` pointed at the new location instead of the
  old first-push merge instructions, which are no longer needed now that
  a real push has landed.

## [0.5.1] — 2026-08-17

### Verified
- `klg-filing-preflight` — cleared the `[VERIFY]` flag on the rule 8.486
  citations. Confirmed (b)(4), (b)(2), and (c)(2) against the current
  rule text at courts.ca.gov: (b)(4) authorizes summary denial with no
  cure period when the record or an exigency showing is missing; (c)(2)'s
  five-day cure applies only to (c)(1) formatting defects, not missing
  or substantively deficient content. This commit was cut earlier but
  never actually landed — catching that now.

## [0.5.0] — 2026-08-17

### Added
- Real `claude.md` — Tim's August 15, 2026 working copy, supplied by
  Edwyn from his OneDrive. Replaces the v0.1.0 placeholder. Source was
  a docx-to-markdown export with backslash-escaped markdown characters
  and `&#x20;` blank-line entities; both stripped mechanically, no
  content reworded. Original one-sentence-per-line wrapping style left
  as-is so future diffs against Tim's own edits stay minimal.
- New "Westlaw Find & Print Format" subsection under Citation Standards
  — the ad hoc-session half of the ["Honor Westlaw Find & Print
  format"](https://app.notion.com/p/3650fc06a06c81b09fd3f4dd54d12b1e)
  item (Urgent). Closes it out; the skill-level half shipped in v0.2.0
  and was confirmed live on the org skill in v0.4.2.
- New "Client Email Routing" subsection under Client Communication
  Rules — the never-CC-clients-on-emails-to-opposing-counsel rule from
  the ["Never CC clients"](https://app.notion.com/p/3670fc06a06c817fb9a3e6436b438847)
  item (Urgent). This closes that item completely — it was claude.md
  only, no skill-level half.
- Both rules were staged in `PENDING_CLAUDE_MD_CHANGES.md` since
  2026-08-11, waiting on exactly this file. That staging file is now
  cleared.

### Not done yet
- `klg-context.md` real content — still the v0.1.0 placeholder. Needs
  Edwyn/Tim to supply it the same way claude.md just arrived.

## [0.4.2] — 2026-08-14

### Verified
- Confirmed `klg-cite-check`'s Step A.6 fix (v0.2.0 — split attorney-review
  list vs. bare-cite Find & Print list) is now live on the org skill.
  Before replacing, confirmed the live copy was stale — unchanged for
  ~3 months, predating the fix — same repo-vs-org gap pattern as
  0.4.1. Edwyn replaced it directly via the org's Skills admin console.
  Partially closes the AI OS Improvement Backlog's ["Honor Westlaw Find &
  Print format"](https://app.notion.com/p/3650fc06a06c81b09fd3f4dd54d12b1e)
  item (Urgent) — the skill-level half. The global `claude.md` half is
  still blocked on real `claude.md` content (see
  `PENDING_CLAUDE_MD_CHANGES.md`).

## [0.4.1] — 2026-08-14

### Verified
- Confirmed the `klg-deep-research-prompts` and `klg-research-compilation`
  fixes from 0.4.0 are live on the actual org skills, not just this repo.
  Initial confusion during verification (Claude's `ListSkills` tool briefly
  showed two IDs per skill name) turned out to be a session-side artifact,
  not a real duplicate — Edwyn confirmed via the org's Skills admin console
  that each skill has exactly one entry, and it now carries the corrected
  language. No further action needed on this item.

### Flagged (not fixed here)
- `klg-daily-triage` still has several William-only references (report
  framing at line ~107, default-mode language at ~109, ID lookups at
  ~349/354, report-mode framing at ~363/372) that assume William is the one
  running/reporting the research pipeline. This was called out as "Also
  related" on the backlog item ["Update research pipeline to support Edwyn
  as runner"](https://app.notion.com/p/3590fc06a06c81e3886ec2069ba458b6),
  but wasn't one of that item's named target skills — needs its own pass.

## [0.4.0] — 2026-08-13

### Changed
- `klg-deep-research-prompts` — added Edwyn Sierra's Slack ID
  (U0AS9KZQ69X) to the runner routing table. The assignee logic itself
  was already generic; this table was the one gap.
- `klg-research-compilation` — generalized the hardcoded Tim/William
  binary throughout (Purpose section, Interaction Rules, Step 5 Final
  Handoff logic, the Slack notification template, Execution Rule 13)
  so any assigned runner works, not just William. Tim stays fixed as
  the post-pipeline reviewer role regardless of who ran the mechanical
  pipeline. Added a Runner Slack ID reference table matching
  `klg-deep-research-prompts`.
- Fixes the AI OS Improvement Backlog's ["Update research pipeline to
  support Edwyn as runner"](https://app.notion.com/p/3590fc06a06c81e3886ec2069ba458b6)
  item (Important). **Correction:** this item was marked Done in
  Notion, but verification against the actual skill files found
  `klg-research-compilation` had not been touched at all — the Notion
  status was stale. Corrected here; see the item's page for the
  updated status.

## [0.3.1] — 2026-08-11

### Changed
- README: added the real GitHub URL (https://github.com/Stuarth128/KLG-AI-CONFIG,
  created by Edwyn) and push instructions, since this session still has no
  push access and every update ships as a zip for Edwyn to push himself.

## [0.3.0] — 2026-08-11

### Added
- New skill `klg-filing-preflight` — seven-gate final pre-filing checklist
  for writs and emergency applications (record completeness, required
  declarations, immediate stay showing, writ-worthiness, cover-page
  mechanics, redaction/sealing consistency, document hygiene), plus a
  `scripts/page_span_audit.py` helper for the Gate 1 mechanical page-span
  check. Built fresh from the backlog entry's spec — the August 2 draft
  SKILL.md referenced in that entry was not available in this session, so
  this build has not been reconciled against it. Two `[VERIFY]` items
  flagged inside the skill itself: the rule 8.486 citations carried over
  from the backlog entry, unconfirmed here. Fixes the AI OS Improvement
  Backlog's "New skill: klg-filing-preflight" item (Urgent).

## [0.2.1] — 2026-08-11

### Added
- `PENDING_CLAUDE_MD_CHANGES.md` — staging file for backlog items whose fix
  is a claude.md rule addition, so they land as one clean commit once the
  real claude.md is available instead of piecemeal edits. Seeded with two
  Urgent items: the Westlaw Find & Print ad hoc-session rule, and "Never CC
  clients on emails to opposing counsel" ([backlog entry](https://app.notion.com/p/3670fc06a06c817fb9a3e6436b438847)).

## [0.2.0] — 2026-08-11

### Changed
- `klg-cite-check` Step A.6 ("Generate Westlaw Pull List") — split the single
  output into two explicit lists. The attorney-review list (case names, flag
  reasons, priority tiers) stays as-is. Added a second, separate paste-ready
  Find & Print list in the correct bare-reporter-cite format (volume/reporter/
  page only, no case names, years, pincites, or parentheticals, one per line,
  deduplicated across tiers) — matching `klg-research-compilation` Rule 5.
  Fixes the AI OS Improvement Backlog's "Honor Westlaw Find & Print format"
  item (Urgent; recurred on the Diller v. Weiss filing-day cite-check). The
  companion global `claude.md` rule from that same backlog entry is not done
  here — still blocked on Task 1's claude.md-source gap — so ad hoc sessions
  outside a skill invocation aren't covered yet by this fix alone.

## [0.1.0] — 2026-08-11

Initial import. Repo created as Task 1 of the "AI OS — Edwyn delegation
batch (Aug–Sep 2026)" — the gating item that must exist before any batch
skill edits (style-rule batch, fetch-patch-verify protocol, TOC block).

### Added
- Imported 22 KLG-authored `SKILL.md` files as currently synced to this
  session, verbatim, no edits: klg-appendix-cites, klg-authority-library,
  klg-brief-assembly, klg-brief-elevation, klg-case-assessment,
  klg-case-novella, klg-cite-check, klg-conflict-waiver,
  klg-content-research, klg-daily-triage, klg-deep-research-prompts,
  klg-dz-overlay, klg-notebooklm-handoff, klg-oral-argument,
  klg-podcast-guest-prep, klg-prebill-audit, klg-record-digest,
  klg-research-compilation, klg-response-plan, klg-style-guide-check,
  court-doc-renamer, opposition-separate-statement.
- Imported `klg-shared-scripts/` (SKILL.md + fix_docx_standalone.py)
  verbatim.
- Seeded `klg-skill-navigator-final.md` from the Notion "Claude Skill
  Navigator Data" page, dated 2026-03-16 in that page's own version field.
  **Known stale:** that JSON lists only 12 skills; at least 10 more
  KLG skills now exist (klg-conflict-waiver, klg-prebill-audit,
  klg-record-digest, klg-dz-overlay, klg-content-research,
  klg-notebooklm-handoff, klg-podcast-guest-prep, klg-daily-triage,
  court-doc-renamer, opposition-separate-statement). Refreshing the
  navigator data is not part of Task 1 — flagging it here so it doesn't
  get lost; candidate for the backlog dedup pass or its own entry.
- Added placeholder `claude.md` and `klg-context.md` with an explanatory note
  on why they're placeholders — see README "STATUS" section. No authoritative
  full-text source for either was reachable from this session.

### Excluded (by design)
- Anthropic/platform-provided skills (docx, pdf, pptx, xlsx, skill-creator,
  morning, dataviz, claude-in-chrome, explain-usage, setup-cowork,
  cowork-plugin-management) — not firm-authored, out of scope for this
  audit log.

### Not done yet
- claude.md / klg-context.md real content (blocked on getting the
  authoritative current text from Edwyn/Tim).
- Notion changelog page mirroring this file (queued right after this
  commit lands).
