---
name: klg-daily-triage
description: >
  Daily task triage, weekly planning, team pulse, comms log triage,
  and email surfacing for KLG. Pulls tasks from Motion via Zapier
  MCP, audits deadline hygiene, scans Outlook inbox for critical
  items, triages the Notion Comms Log for unactioned items, and
  produces prioritized reports with Slack notifications and Notion
  project pages. Use whenever the user says daily triage, morning
  triage, plan my day, plan my week, weekly planning, time block,
  what do I need to do today, whats on my plate, whats urgent,
  triage my inbox, inbox zero, email triage, comms log triage,
  comms log review, team pulse, team status, whos overloaded,
  good morning, start my day, morning briefing, daily standup,
  what should I work on, triage report, prepare for team meeting,
  meeting prep, or wants to review tasks, plan schedule, triage
  emails, check team workload, or review the comms log. Also
  trigger for general status overviews. NOT for specific case
  skills or skill navigator.
---

# KLG Daily Triage

## Purpose

Cross-cutting operational skill built on four pillars:

1. **Surface critical emails** — mid-week rescue when the inbox
   is drowning Tim. Not full inbox management, just "here's what
   you can't afford to miss."
2. **Protect important from urgent** — flag when high-priority
   matters (HB Voter ID, cert petitions) are stalling because
   low-priority urgent requests eat all the oxygen.
3. **Motion deadline audit** — systematic hygiene check. Stale
   and illogical deadlines get surfaced and reported to Brittney
   via Slack as cleanup items.
4. **Comms log triage** — the centerpiece. Review what's been
   routed to the Notion comms log, classify it, generate an
   actionable report as a Notion project page, and send Slack
   notifications. Prevent routed emails from going dark.

Unlike other KLG skills, this is NOT case-specific. It operates
across all matters and team members.

## Required Context

1. This SKILL.md — core workflow, four pillars, and mode logic
2. `references/comms-log-triage.md` — comms log classification
   system, thread deduplication, report generation, Notion
   project page architecture, and close-the-loop mechanics.
   **Read on every triage run.**
3. `references/email-triage.md` — Outlook inbox categorization
   rules and one-at-a-time triage workflow for Tim's interactive
   email review sessions.
4. `references/visualizer-specs.md` — widget layouts for
   dashboards. Read when user requests a visual dashboard.

## Connectors Required

| Connector | Tool | Purpose |
|-----------|------|---------|
| Zapier (Motion) | Find Task | Pull tasks across workspaces |
| Zapier (Motion) | Create Task | Tasks from triage decisions |
| Zapier (Motion) | Update Task | Priority/status/deadline changes |
| Zapier (Outlook) | Find/Flag/Move/etc. | Inbox write ops |
| Notion | Fetch, Search, Query, Create | Comms log + Projects |
| M365 | outlook_email_search | Inbox scan (read) |
| Slack | search, send_message_draft | Notifications |

### Connector Preflight

On every run, verify in this order:
1. **Notion** — Fetch Comms Log database
   (`2e40fc06-a06c-8197-a806-c1f6f28a847c`) and Projects
   database (`01c88dba-9dd8-4715-82f4-335837d3fa89`).
2. **Zapier/Motion** — Call Find Task with minimal params.
3. **M365** — Quick email search to verify access.
4. **Slack** — Search for a known channel.

If Notion is missing, STOP — the comms log triage cannot run.
If Motion is missing, offer degraded mode (comms log + email
only). If Slack is missing, warn that notifications will be
skipped.

---

## Global Rules

### Always use `slack_send_message_draft`

All Slack messages composed during any triage mode MUST use
the draft widget. No exceptions. All drafts follow `claude.md`
Slack rules.

### Default to Brittney, not Tim

The skill's job is to produce a **report with recommendations
that Brittney can act on** — not to present Tim with a
questionnaire. Auto-classify as much as possible. Route
ambiguous items to Brittney for triage, not to Tim. Tim sees
only: (a) items requiring attorney judgment, and (b) strategy
follow-ups for meeting discussion.

### Team-runnability

This skill can be run by any team member — Tim, Brittney, or
William. The default mode produces the report autonomously.
Tim can opt into interactive mode by saying "walk me through
them." When Brittney or William runs it (especially before
team meetings), it should work identically — pull data,
classify, generate the Notion project page and Slack
notification, done. No Tim-specific knowledge required.

---

## Mode Selection

On trigger, present mode selection:

```
What kind of triage today?

📋 FULL TRIAGE — Comms log + deadlines + inbox + report.
   Generates a Notion triage report and Slack notification.
   (~10–15 min)

☀️ MORNING TRIAGE — Quick: today's tasks, urgent inbox,
   deadline alerts. (~5 min)

📅 WEEKLY PLANNING — Full week capacity, deadline overlay,
   time-block suggestions. (~15 min)

👥 TEAM PULSE — Cross-team task status, bottlenecks,
   overdue items. (~5 min)

📨 COMMS LOG ONLY — Just the comms log triage and report.
   (~10 min)

📧 EMAIL ONLY — Just surface critical inbox items. (~3 min)
```

If the user's message clearly indicates a mode, skip selection.
"Prepare for team meeting" → Full Triage. "Plan my week" →
Weekly Planning. "Triage the comms log" → Comms Log Only.

---

## Pillar 1: Surface Critical Emails

Use M365 `outlook_email_search` to pull recent unread and
flagged emails (last 24–48 hours). Focus on surfacing items
Tim can't afford to miss — not comprehensive inbox management.

High-signal indicators: client emails with questions, court
notices, co-counsel with deadlines, anything with "urgent" or
a date in the near future.

In **Full Triage** and **Morning Triage** modes, present a
short "can't miss" list (3–5 items max). In **Email Only**
mode, read `references/email-triage.md` and run the
interactive one-at-a-time workflow with Tim.

---

## Pillar 2: Protect Important from Urgent

After pulling Motion tasks, cross-reference against a
**priority watchlist** of matters that should be making
progress but may be stalling:

Known high-priority matters (update as needed):
- HB Voter ID (cert petition)
- Any matter with an upcoming oral argument
- Any matter where Tim is the primary drafter

Detection: if no tasks in these projects have been completed
or moved to "In Progress" in the last 14 days, flag:

> ⚠️ **Priority drift: [Matter]** — no task progress in [N]
> days. This is a high-priority matter at risk of stalling
> while urgent lower-priority requests consume capacity.

Include priority drift alerts in the triage report summary.

---

## Pillar 3: Motion Deadline Audit

Pull all non-completed tasks from Motion across all workspaces.
Apply three hygiene filters before presenting anything as
"overdue":

### Filter 1: Stale deadline detection

Next Deadline or due date in the past on an active project →
flag as stale data, not a missed deadline. Collect into a
**Data Hygiene Punch List** for Brittney.

### Filter 2: "Their deadline" detection

Parse project/task names for "their," "opposing," "other side,"
"respondent's" (when KLG is not that party), or "[brief type]
due [date] in default." Classify as monitoring deadline.

### Filter 3: Cascade dependency / illogical deadlines

Known dependency chains:
1. Opposing brief → Response plan → First draft → Second
   review → Cite check → Formatting → Filing
2. Record designation → Record prep → Record received →
   Briefing
3. Case assessment → Research → Compilation → Brief drafting

Flag any task due before its logical predecessor.

### Output buckets

| Bucket | Meaning | Action |
|--------|---------|--------|
| 🔴 Real overdue | Genuine missed deadline | Tim's attention |
| ⚠️ Data quality | Stale, cascade error | Cleanup punch list |
| 👁️ Monitoring | Their deadline | Track only |

Include the punch list in the Notion triage report and offer
to send it to Brittney via Slack.

---

## Pillar 4: Comms Log Triage

This is the centerpiece. Read `references/comms-log-triage.md`
before executing. High-level flow:

1. **Pull** unactioned comms log entries (Actions field empty)
   from the last N days (default 5).
2. **Close prior loop** — fetch last week's triage project
   page, identify checked-off items, batch-update those comms
   log entries' Actions field to Done/N/A.
3. **Deduplicate** — group entries by thread (subject root +
   Reply To chain + Case Portal link). Present only the most
   recent entry per thread. Do NOT delete older entries.
4. **Auto-classify** into six buckets using calibrated patterns.
5. **Generate** a Notion project page in the Projects database,
   linked to the PC Intake & Case Management team portal.
6. **Send** a Slack notification via `slack_send_message_draft`
   with a summary and link to the Notion page.

### Six classification buckets

| # | Bucket | Description |
|---|--------|-------------|
| 1 | Action — assign/delegate | Someone needs to own this |
| 2 | Action — Tim must handle | Requires attorney judgment |
| 3 | Action — new PC intake | New potential client; trigger intake |
| 4 | Informational — team handling | Workflow in progress |
| 5 | Informational — no action | FYI, resolved, directive sent |
| 6 | Strategy / follow-up | Direction set; verify at meeting |

Detailed classification patterns, report structure, and
close-the-loop mechanics are in
`references/comms-log-triage.md`.

---

## Mode A: Full Triage

Runs all four pillars and produces the complete report.

### Step A.1: Close prior triage loop

Fetch last week's triage project page. Parse checked items,
extract comms log IDs, batch-update Actions fields. Mark
prior project as Done. Carry over unchecked items.

### Step A.2: Pull Motion tasks + deadline audit (Pillar 3)

Pull tasks across all workspaces. Apply hygiene filters.
Identify real overdue items, data quality issues, and
monitoring deadlines.

### Step A.3: Check priority drift (Pillar 2)

Cross-reference Motion tasks against priority watchlist.
Flag stalled high-priority matters.

### Step A.4: Scan inbox for critical items (Pillar 1)

Pull recent unread/flagged emails. Surface top 3–5 items
Tim can't miss. Brief summary only.

### Step A.5: Comms log triage (Pillar 4)

Pull, deduplicate, classify, generate Notion project page.

### Step A.6: Produce consolidated summary

Conversational summary in this order:
1. Real overdue items (Motion)
2. Priority drift alerts
3. Critical inbox items (top 3–5)
4. Comms log summary stats (X items, Y need action)
5. Data hygiene punch list (count + offer to Slack)
6. Link to the Notion triage report page

### Step A.7: Send Slack notification

Via `slack_send_message_draft` to #all-kowallawgroup (or a
dedicated triage channel). Brief summary + Notion link.
Brittney works from the Notion page, not from Slack.

### Step A.8: Time blocking (optional)

Offer to propose time blocks and write to Motion. Batch
decisions first, then execute. Each call = 2 Zapier tasks.

---

## Mode B: Weekly Planning

### Step B.1: Pull full week tasks + deadline audit

All non-completed tasks across workspaces, organized by day.
Apply Pillar 3 hygiene filters.

### Step B.2: Capacity analysis

Use Motion task durations (100% populated). Compare against
6 productive hours/day. Flag overcommitted and available days.

### Step B.3: Priority drift check (Pillar 2)

Flag stalled high-priority matters.

### Step B.4: Recommendations + time blocking

Suggest task moves, deep-work blocks, then offer Step A.8.

### Step B.5: Summary + visual dashboard

Conversational summary, then offer widget from
`references/visualizer-specs.md`.

---

## Mode C: Team Pulse

Pull tasks across all team members and workspaces. Apply
hygiene filters. Flag bottlenecks: 3+ real overdue tasks,
5+ due this week, unassigned approaching deadlines, William's
research queue, Brittney's formatting queue.

Known assignee IDs: Tim (`bK4I5zZ4MKQkYX1SsaVyV7WoHnn1`),
Brittney (`WSOQbtHisLdCnjGSfMrNCK3rikP2`), Ted
(`nzsyuTkRPodyVOEfhaJDfy3F5hl1`), William
(`vWYPVO9qNGMyT8CpqTEzro6eGz63`).

---

## Mode D: Comms Log Only

Runs Pillar 4 only: pull, deduplicate, classify, generate
Notion project page, send Slack notification. Skips Motion,
inbox, and priority drift. Ideal for Brittney/William running
before a team meeting.

---

## Mode E: Email Only

Runs Pillar 1 only. In interactive mode (Tim), reads
`references/email-triage.md` and presents emails one at a
time with action options. In report mode (Brittney/William),
produces a categorized inbox summary.

---

## First-Run Data Discovery

### Motion workspaces

Call Find Task without `workspaceId`. If only one workspace
appears, tell user. Known: ⭐KLG Briefing Projects
(`PmtZ3B45kZe6DCV30YlPh`). Expected but undiscovered:
HB Voter ID, cert petitions, consulting projects.

### Motion field mapping (confirmed)

Statuses: Todo, In Progress, Blocked, On Hold, Completed,
Canceled. Priorities: MEDIUM, HIGH. Custom fields: Case Name,
Next Deadline (date), Slack Channel (url), SharePoint (url),
etc. Duration and due dates: 100% populated.

### Notion databases (confirmed)

- Comms Log: `2e40fc06-a06c-8197-a806-c1f6f28a847c`
- Case Portal: `2da0fc06-a06c-8033-978b-000bd2803cd4`
- Projects: `01c88dba-9dd8-4715-82f4-335837d3fa89`
- Projects data source: `df007c24-ffac-40d7-8e91-fb6763b6ecf6`
- Case Mgmt Team Portal: `3250fc06-a06c-80c2-9d28-da7c0b81c6b8`

### Comms Log schema (confirmed)

Key fields: Name (title), From (email), Comm Date (text),
Summary (text), Email Text (text), Actions (select: Done /
Respond / N/A), Downloaded (checkbox), Has Download Link
(text), Pin (checkbox), Case Portal (relation), Projects
(relation), Reply To (self-relation), Attachments (file),
Tag (select).

---

## Slack Posting Rules (Skill-Specific)

Posts only when a specific action is needed. All posts use
`slack_send_message_draft`. The triage report Slack message
is a brief summary + Notion link — not the full report.

---

## Session Logging

Not matter-specific — no session logs. Exception: if triage
reveals a deadline risk for a specific matter, offer to log.

---

## Chat Only

All data from connectors. No Cowork needed.

---

## Zapier Task Budget

Each Motion or Outlook call = 2 Zapier tasks. Typical full
triage: 1–3 Motion calls + Notion reads/writes (free). Batch
decisions before executing write operations.
