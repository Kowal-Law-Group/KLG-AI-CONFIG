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
claude.md                      Global behavioral rules (STATUS: placeholder, see below)
klg-context.md                 Firm/team/matter context file (STATUS: placeholder, see below)
klg-skill-navigator-final.md   Skill Navigator data (seeded from a 2026-03-16 Notion export — STALE, see note in file)
klg-shared-scripts/            Shared utility scripts (fix_docx_standalone.py, etc.)
skills/<skill-name>/SKILL.md   One folder per KLG-authored skill
CHANGELOG.md                   Dated, human-readable change log
VERSIONING.md                  Semantic versioning convention for this repo
```

Anthropic/platform-provided skills (docx, pdf, pptx, xlsx, skill-creator,
morning, dataviz, claude-in-chrome, explain-usage, setup-cowork,
cowork-plugin-management) are intentionally excluded — they aren't
firm-authored and aren't what the backlog item is protecting against
uncontrolled edits.

## STATUS: claude.md and klg-context.md are placeholders

I could not locate a single authoritative current copy of the full
`claude.md` or `klg-context.md` text anywhere I have access to in this
session:

- The org-level AI instructions injected into my own Cowork session are
  much shorter than the ~2,245-line `claude.md` referenced in the
  2026-06-17 Config Archive Notion page, and don't contain sections that
  page and other backlog entries clearly describe (Slack Posting Rules /
  Team Slack User ID table, Connector Preflight Check, Handoff Message
  Structure, Iterative Work Product — Notion First, etc.). So the two are
  not the same file.
- The Notion "Config Archive — 2026-06-17 pre-drafting-sweep snapshot" page
  only *describes* a snapshot — the actual 2,245-line file was delivered to
  Tim directly as `claude.md.pre-sweep-snapshot-2026-06-17.md` outside
  Notion. I don't have access to that delivery.
- `klg-context.md` isn't quoted in full anywhere I could find either.

**Action needed from Edwyn/Tim:** paste or upload the current live
`claude.md` and `klg-context.md` text (wherever the primary Alfred/Claude.ai
session that treats them as project-knowledge files currently keeps them),
and I'll seed real v1.0.0 history from the actual files instead of these
placeholders.

## Promotion path

1. Edit a skill or config file in a Claude/Cowork session as usual.
2. Land the change here as a commit with a clear message.
3. Bump the version per `VERSIONING.md` and add a `CHANGELOG.md` entry.
4. Mirror the entry to the Notion changelog page (linked from the AI OS hub)
   for anyone who works Notion-first.

## Related

- GitHub: https://github.com/Stuarth128/KLG-AI-CONFIG
- Delegation batch project: https://app.notion.com/p/3b80fc06a06c81e2a8e4da5205f88c58
- Backlog entry (this task): https://app.notion.com/p/35b0fc06a06c8187886bdc40e49f0a79
- klg-ai-os (Alfred/Bloodhound app): https://github.com/edwyn128/klg-ai-os

## Pushing this repo (Edwyn)

The Cowork session that builds this repo has no push access to GitHub —
confirmed by a direct push attempt, rejected by GitHub's proxy with "not
in this session's authorized repository set." So every update ships to
Edwyn as a `.zip` with full git history, and he pushes it. The remote
repo was created with an auto-generated `README.md` on `main`, which is
unrelated history to this repo's `master` branch, so the first push needs
one of:

```bash
# unzip the delivered archive, then from inside klg-ai-config/:
git remote add origin https://github.com/Stuarth128/KLG-AI-CONFIG.git

# Option A — replace the placeholder README with this repo's real history
# (recommended; the auto-generated README has no content worth keeping):
git push origin master:main --force --tags

# Option B — keep both histories (merge commit, more history noise):
git fetch origin main
git merge origin/main --allow-unrelated-histories -m "merge: initial GitHub README"
git push origin master:main --tags
```

Every later update is a normal `git pull` + apply the new zip's commits
(or just `git push --tags` again from the updated local clone Claude sends).
