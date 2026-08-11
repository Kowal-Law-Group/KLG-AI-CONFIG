# Versioning convention

This repo uses semantic versioning, tagged at the repo level (not per-file):
`MAJOR.MINOR.PATCH`.

- **MAJOR** — a breaking change to skill behavior or claude.md rules that
  changes how existing workflows must be invoked (e.g., a renamed trigger
  phrase, a removed skill, a restructured handoff format).
- **MINOR** — a new skill, a new claude.md section, or a substantive
  behavioral addition that doesn't break existing usage.
- **PATCH** — wording fixes, style-rule tweaks, typo corrections, or
  additions to reference tables (e.g., a new Slack channel ID row).

## Review process (PR-style diffs)

1. Every change lands as its own commit with a message in the form:
   `<file/skill>: <what changed> — <why, one line>`.
2. Before merging a multi-file sweep (e.g., a style-rule batch touching
   claude.md and three skills), open the diff and read it end-to-end the
   way a reviewer would — this repo doesn't have a second human reviewer by
   default, so the diff read *is* the review. Treat it as non-optional.
3. Tag the commit that lands a version bump: `git tag vX.Y.Z`.
4. Add a `CHANGELOG.md` entry under that version with a one-line rationale
   per change.
5. Mirror the changelog entry into the Notion changelog page.

## Rollback

Because this is Git, rollback is `git revert <commit>` or
`git checkout vX.Y.Z -- <path>` for a single file — no more hand-pasted
snapshot pages. The pre-Git snapshots already captured in Notion (e.g. the
2026-06-17 Config Archive page) stay as historical record; they are not
superseded, just no longer how new rollback points get created.
