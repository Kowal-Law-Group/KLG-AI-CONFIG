# Changelog

All notable changes to KLG's claude.md, klg-context.md, skill navigator, and
SKILL.md files are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). See `VERSIONING.md` for the
version-bump rules.

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
