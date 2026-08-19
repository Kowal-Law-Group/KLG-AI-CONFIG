# klg-ai-config

Version-tracked source of truth for Kowal Law Group's Claude configuration:
`claude.md`, `klg-context.md`, `klg-skill-navigator-final.md`, and every
`SKILL.md` file the firm has authored.

This repo exists so that no skill or config edit is ever made without a
pre-change snapshot. It implements **Option D** from the backlog item
["Build skills/config audit log"](https://app.notion.com/p/35b0fc06a06c8187886bdc40e49f0a79):
Git as the canonical source, with a lightweight Notion changelog page
alongside it for anyone who doesn't want to open GitHub.

This is a companion repo to `edwyn128/klg-ai-os` (the Alfred/Bloodhound
production app). It is deliberately separate: klg-ai-os is fast-moving
application code touched by three concurrent agents (Claude Code, Antigravity,
Claude Desktop); this repo is slow-moving firm configuration that should be
reviewable as clean, isolated diffs.

## What's in here

```
claude.md                      Global behavioral rules (real file, landed 2026-08-17)
klg-context.md                 Firm/team/matter context file (STATUS: still a placeholder, see below)
klg-skill-navigator-final.md   Skill Navigator data (seeded from a 2026-03-16 Notion export — STALE, see note in file)
klg-shared-scripts/            Shared utility scripts (fix_docx_standalone.py, etc.)
skills/<skill-name>/SKILL.md   One folder per KLG-authored skill
skills/<skill-name>/evals/     Regression-eval prompts for that skill, where they exist (see eval-harness/)
eval-harness/                  Skill regression-test harness + run results (Task #11, see eval-harness/README.md)
CHANGELOG.md                   Dated, human-readable change log
VERSIONING.md                  Semantic versioning convention for this repo
```

Anthropic/platform-provided skills (docx, pdf, pptx, xlsx, skill-creator,
morning, dataviz, claude-in-chrome, explain-usage, setup-cowork,
cowork-plugin-management) are intentionally excluded — they aren't
firm-authored and aren't what the backlog item is protecting against
uncontrolled edits.

## STATUS: claude.md landed; klg-context.md is still a placeholder

`claude.md` is now the real file — Tim's August 15, 2026 working copy,
supplied by Edwyn from his OneDrive on 2026-08-17. It replaces the
placeholder seeded in v0.1.0. Two things worth knowing about this pass:

- The source file was a docx-to-markdown export with markdown special
  characters backslash-escaped and blank lines rendered as `&#x20;`
  entities. Both were mechanically stripped before landing it here —
  content wasn't otherwise reworded or reflowed. The original's
  one-sentence-per-line wrapping style was left as-is rather than
  reflowed into normal paragraphs, so the diff against any future
  Tim-supplied version stays minimal and reviewable.
- Landing this file also let two Urgent backlog items close out their
  claude.md half: the Westlaw Find & Print global rule (new section
  under Citation Standards) and the never-CC-clients-on-emails-to-
  opposing-counsel rule (new "Client Email Routing" subsection under
  Client Communication Rules). Both were staged in
  `PENDING_CLAUDE_MD_CHANGES.md` — see CHANGELOG for detail.
- v0.6.0 added four more rules on top of that same file — from the
  Backlog Triage's Batch 2 "claude.md style rules" cluster — before
  any of it has gone live in Tim's Project Knowledge. See CHANGELOG
  for detail; none of this needs a separate upload, it's all in the
  one standalone file already pending Tim's swap.

`klg-context.md` (firm/team/matter context — the Slack User ID team
table, etc.) is still the v0.1.0 placeholder. Same gap as before:
**action needed from Edwyn/Tim** to supply the current file.

## Promotion path

1. Edit a skill or config file in a Claude/Cowork session as usual.
2. Land the change here as a commit with a clear message.
3. Bump the version per `VERSIONING.md` and add a `CHANGELOG.md` entry.
4. Mirror the entry to the Notion changelog page (linked from the AI OS hub)
   for anyone who works Notion-first.

## Related

- GitHub: https://github.com/Kowal-Law-Group/KLG-AI-CONFIG (moved from Stuarth128/KLG-AI-CONFIG)
- Delegation batch project: https://app.notion.com/p/3b80fc06a06c81e2a8e4da5205f88c58
- Backlog entry (this task): https://app.notion.com/p/35b0fc06a06c8187886bdc40e49f0a79
- klg-ai-os (Alfred/Bloodhound app): https://github.com/edwyn128/klg-ai-os

## Pushing this repo (Edwyn)

The Cowork session that builds this repo has no push access to GitHub —
confirmed by a direct push attempt, rejected by GitHub's proxy with "not
in this session's authorized repository set." So every update ships to
Edwyn as a `.zip` with full git history, and he pushes it from his own
machine.

**Repo location moved.** It was originally created at
`github.com/Stuarth128/KLG-AI-CONFIG` (personal account) and has since
been transferred to the firm org: `github.com/Kowal-Law-Group/KLG-AI-CONFIG`.
GitHub redirects pushes to the old URL automatically, but point the local
remote at the real location going forward:

```bash
git remote set-url origin https://github.com/Kowal-Law-Group/KLG-AI-CONFIG.git
git push origin master:main --tags
```

History through v0.5.1 is live on `main` as of 2026-08-17. For a fresh
clone (no existing `origin`), use `git remote add origin` instead of
`set-url`. Every later update is a normal `git push --tags` from the
updated local clone Claude sends.
