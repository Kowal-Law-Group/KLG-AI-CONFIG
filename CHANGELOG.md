# Changelog

All notable changes to KLG's claude.md, klg-context.md, skill navigator, and
SKILL.md files are recorded here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). See `VERSIONING.md` for the
version-bump rules.

## [0.11.0] — 2026-08-19

### Added — table of contents on multi-section Notion pages (delegation-batch Task #10)
- claude.md — new subsection "Table of Contents on Multi-Section Notion
  Pages" under "Output Requirements (Default)," placed right after
  "Iterative Work Product — Notion First"'s closing "Exception" paragraph
  and before "Quality Controls." Rule: insert a table-of-contents block
  near the top of any Notion page with 3+ distinct heading sections —
  after any intro callout/header, before the first section heading. Skip
  it on 1–2 section pages. Individual skills may override placement or
  the section-count threshold in their own SKILL.md.
- Syntax correction: the backlog entry guessed `[toc]` bracket syntax but
  flagged its own uncertainty ("verify against current Notion MCP
  enhanced markdown spec at implementation time — syntax may vary").
  Fetched the actual `notion://docs/enhanced-markdown-spec` resource and
  confirmed the correct block is `<table_of_contents color?="Color"/>` —
  `[toc]` does not render. The rule as written uses the verified syntax
  and calls out the `[toc]` form as wrong, so a future editor doesn't
  reintroduce it.
- claude.md-only per the entry's own scope — no per-skill edits needed;
  Notion-writing skills inherit this from claude.md rather than
  restating formatting rules locally.

## [0.10.0] — 2026-08-19

### Added — fetch-patch-verify protocol (delegation-batch Task #9)
- claude.md — new subsection "Editing live drafts: fetch-patch-verify"
  under "Notion as Claude's Authoring Workspace," placed right after the
  section's "Claude writes; humans review" framing since this rule is
  the direct implementation of the "humans review" half of that model.
  Four-step protocol per the backlog entry: fetch the live page
  immediately before editing (never edit from a cached copy), patch
  only the requested change, write surgically by default (`update_content`/
  `insert_content`) with `replace_content` reserved for genuine full
  rewrites — and even then built from fetched-current-content, not a
  reconstruction — then re-fetch to verify the change landed and nothing
  else moved. Added the turn-taking rule (write only when handed the pen)
  and the rich-block-type caveat (callouts/toggles/columns/synced blocks
  can round-trip lossy) from the entry.
- claude.md-only per the entry's own "Target skill" — no per-skill edits
  needed, since every Notion-writing skill inherits global claude.md
  behavior rather than restating tool-usage rules locally.
- Not run: the entry's own suggested validation ("test update_content/
  insert_content for reliability, promote to default if reliable").
  This session's own Notion edits throughout today used `insert_content`
  and `notion-create-comment` successfully and repeatedly, which is
  consistent with — but short of — a real reliability test. Wrote the
  rule to prefer surgical edits by default based on that experience,
  flagging that a rigorous test wasn't separately run.

## [0.9.0] — 2026-08-19

### Added — style-rule batch into klg-style-guide-check (delegation-batch Task #8)
4 items batched per Task #8's own grouping; one of the 4 turned out to
already be resolved as a duplicate (see below) rather than needing new work.

- **Em dashes: no flanking spaces** — added a new `### Typography`
  subsection under Output Requirements in claude.md (the entry's own
  suggested home). The entry claimed this rule was "already explicitly
  codified in claude.md" — it was not; grepped the whole file and found
  no em-dash rule anywhere before this edit. Added fresh rather than
  "promoted," and flagged that discrepancy rather than assuming the
  entry's premise. Also flagged, not fixed: claude.md's own prose (as
  imported from Tim's original docx) uses spaced em dashes pervasively —
  208 same-line instances plus roughly 18 cross-line instances via the
  file's one-clause-per-line, blank-line-continued formatting. Fixing
  that is a mechanical cleanup of the entire file, not part of what this
  backlog item asked for (encoding the rule going forward), and risks
  corrupting the file's unusual line-wrap structure if done as a bulk
  find/replace without care. Left as a flagged, separately schedulable
  cleanup rather than attempted here.
- **Full-path heading labels (II.A, II.B, II.A.1)** — augmented the
  existing "Subheading numbering" bullet in claude.md's Style Checks
  with the full-path labeling rule, using the entry's own paste-ready
  text. Did not touch the separate KLG Style Manual .docx (SharePoint,
  read-only via connector) — same limitation noted in every prior style
  rule landed this way.
- **Standardize placeholder format to `[VERIFY: description]`** —
  replaced `[CITE TBD]` and bare `[VERIFY]` in claude.md's "What You
  Must Never Do" with the single uniform tag, and normalized every
  skill-level variant found across the repo: `klg-brief-elevation`,
  `klg-response-plan` (three separate occurrences — `[VERIFY]`,
  `[RESEARCH NEEDED]`, `[Record cite needed]` all collapsed to one
  tag), `klg-case-assessment` (two occurrences), and the three copies
  of the `klg-notebooklm-handoff`/`klg-research-compilation`/
  `klg-case-assessment` placeholder reference stub. `klg-cite-check`
  Step A.3 (Check for Placeholders) keeps detecting the old variants
  too — a brief may carry legacy or outside-counsel placeholders — but
  now explicitly ties that search to the pre-filing safeguard the entry
  asked for: report a literal count/list of every match and don't treat
  the brief as filing-ready until it's empty or attorney-cleared.
  `klg-notebooklm-handoff`'s ChatGPT-facing prompt templates updated to
  match, since the handoff protocol assumes Claude's own drafts now only
  carry the one tag.

### Verified — duplicate, not new work
- **Heading-case convention** (["Fix heading-case convention"](https://app.notion.com/p/3860fc06a06c819caed5f527a1b6f483),
  Task #8's second item) turned out to be the identical fix already
  landed in v0.6.0 as ["Heading conventions"](https://app.notion.com/p/3b50fc06a06c812c8c8dd08341552670)
  — same two-part rule (title-case section labels, no period; sentence-
  case argument headings, with period), confirmed live in claude.md's
  Style Checks. The one part of this entry not covered by the v0.6.0
  fix — auditing `klg-brief-assembly`'s heading-style mapping — was
  checked: the mapping assigns Word styles by markdown heading level
  (`#`/`##`/`###`) and section identity, not by heading-text casing, and
  the levels already correspond correctly to the two heading categories.
  No change needed there.

## [0.8.0] — 2026-08-18

### Added — narrow new-skills cluster (Backlog Triage Lane 2)
3 of 15 items landed as genuinely self-contained; 12 flagged back
(see below). Triage re-read each item's full page, not just the
Backlog Triage summary line, since the "no Tim input needed" bar
turned out not to hold for most of this cluster despite its Lane 2
placement.

- New skill `klg-extension-good-cause` — drafts the good-cause /
  reasons section of Court of Appeal (APP-006 + APP-031A) and
  U.S. Supreme Court cert extension applications. Encodes the
  rule 8.63 factors, pulls the live competing-deadline list from
  Motion/Notion instead of re-typing it, leads with what's new
  since the last grant, genericizes confidential/DZ matters, and
  checks cross-matter factual consistency on recurring facts
  (the Ryan Merker death-date pattern).
- New skill `klg-email-voice` — drafts/rewrites emails and Slack
  messages in Tim's actual voice (cold open, bold-prefix leads,
  short declaratives, confident unhedged takes, `-Tim` sign-off)
  instead of brief-voice prose, with a recipient-register table
  (DZ bluntest, trial counsel more formal, clients warmer).
- `klg-daily-triage` — new Pillar 6 (Appeal Watch Scan): scans
  SharePoint matter folders for newly added judgments, orders, and
  notices of entry, applies Tim's flat 60-day deadline rule (no
  Rule 8.104/8.108 logic), and surfaces detected items for
  attorney confirmation before anything becomes a hard deadline.
  Built as a Pillar 6 sub-routine rather than a standalone skill
  or scheduled agent, per Tim's own May 12, 2026 note that v1
  should be "a skill first, agent later... likely a sub-routine
  inside klg-daily-triage." Uses the same rolling 14-day window as
  Pillar 5, which sidesteps the entry's open "where does the watch
  list live" question — v1 needs no persistent storage, since
  nothing must survive between runs beyond what the report already
  shows. Wired into Mode A as Step A.7, renumbering A.7–A.9 to
  A.8–A.10.

### Flagged back — did not clear the Lane 2 bar
- **klg-client-revision-review**: entry's own "Open design
  questions" section leaves input-format handling, architecture
  (standalone vs. klg-brief-elevation extension), and output format
  as the author's leanings, not decisions.
- **klg-brief-postmortem**: entry states its own build sequence —
  "klg-exemplar-harvest first... then this skill" — and
  klg-exemplar-harvest hasn't landed.
- **klg-friday-team-meeting**: four explicit open design questions
  (output destination, auto-population of "wins," postmortem
  auto-linking, run cadence).
- **klg-slack-harvest**: unverified technical dependency — the
  entry itself asks whether the Slack MCP connector reliably
  exposes emoji reactions per message, with no fallback confirmed
  — plus open DM-scanning and scan-window questions.
- **Brief Introduction default + outline generator**: entry ends
  with a direct quote from Tim — "We should actually work through
  that skill update carefully" — requesting a dedicated working
  session. The opposite of "no Tim input needed."
- **PNC intake-screening gate**: foundational architecture question
  unresolved (standalone skill vs. gate inside klg-case-assessment
  vs. claude.md behavioral rule).
- **klg-cert-petition**: page has no content — no spec exists to
  build from.
- **Lock petition-for-review structure**: unresolved Rule
  8.504(b)(1) reading question (does "begin with" require the
  issues statement first, ahead of the petitioning paragraph?) that
  needs attorney verification before the structure can be locked,
  plus a sequencing dependency on the Palmieri petition being
  finalized.
- **klg-exemplar-harvest**: two open sourcing questions (sealed/
  paywalled briefs; Ninth Circuit vs. California fee-shifting
  treatment) unresolved.
- **klg-exemplar-onboard**: explicitly gated on seeding the
  Exemplar Database with 5-10 real exemplars first — same blocked
  dependency flagged in v0.6.1.
- **klg-style-exemplars**: two-deep dependency chain (seeding →
  klg-exemplar-onboard → this skill), neither link landed.
- **klg-dz-overlay (full build)**: this backlog entry is Status
  "In progress," not New — a v1 bundle already exists outside this
  repo. The one substantive open item, the invisibility-surcharge
  dollar figure, is explicitly Tim's call ("Tim needs to pick a
  number before the conversation with David"), and the item is also
  waiting on that conversation's outcome. Not re-attempted here;
  distinct from the narrow Phase 0 gating-questions item already
  landed on this skill in v0.7.0.

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
