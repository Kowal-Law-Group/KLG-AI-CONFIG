# Changelog

All notable changes to KLG's claude.md, klg-context.md, skill navigator, and
SKILL.md files are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). See `VERSIONING.md` for the
version-bump rules.

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
