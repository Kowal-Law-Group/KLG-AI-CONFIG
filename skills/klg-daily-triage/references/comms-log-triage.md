# Comms Log Triage Reference

## Overview

The comms log triage is the centerpiece of the daily triage skill.
It solves the "out of sight, out of mind" problem: Tim routes
emails to the comms log to unblock his inbox, but those emails
risk going dark if nobody tracks follow-through.

This triage generates an **actionable Notion project page** that
Brittney works from directly. Slack gets a brief notification
with a link — the report itself lives in Notion.

## Notion Infrastructure

### Comms Log database
- ID: `2e40fc06-a06c-8197-a806-c1f6f28a847c`
- Data source: `collection://2e40fc06-a06c-81f0-aca8-000bce804f3f`
- Default view (sorted by Created desc): `view://2e40fc06-a06c-8169-b8b2-000ca05057a3`
- Key fields: Name, From, Comm Date, Summary, Email Text,
  Actions (Done/Respond/N/A), Downloaded, Has Download Link,
  Pin, Case Portal (relation), Reply To (self-relation),
  Attachments, Projects (relation)

### Projects database
- ID: `01c88dba-9dd8-4715-82f4-335837d3fa89`
- Data source: `df007c24-ffac-40d7-8e91-fb6763b6ecf6`
- Key fields: Project name (title), Status (Backlog/Planning/
  In progress/Paused/Done/Canceled), Priority, Owner, Dates,
  Summary, Team Portals (relation), Comms Log (relation),
  Blocked By / Is Blocking (self-relations)

### PC Intake & Case Management Team Portal
- ID: `3250fc06-a06c-80c2-9d28-da7c0b81c6b8`
- Has embedded Projects view — triage pages automatically
  appear here when linked via Team Portals relation.

---

## Step 1: Close Prior Triage Loop

Before generating a new report, check for last week's triage:

1. Search Projects for the most recent "Comms Log Triage"
   project page with Status "In progress."
2. Fetch that page's content.
3. Parse the to-do items. For each checked item:
   - Extract the comms log entry URL/ID embedded in the line.
   - Update that comms log entry's Actions field to "Done"
     (for action items that were completed) or "N/A" (for
     items marked as resolved/informational).
4. For unchecked items, carry them forward into this week's
   report with a "⏩ Carried over from [date]" marker.
5. Set last week's project Status to "Done."

**ID extraction:** When generating the triage page, embed
comms log entry IDs in a parseable format at the end of each
line: `[CL:3290fc06a06c81a1]`. This is invisible to Brittney
(it looks like a Notion link) but gives the skill a reliable
key for the close-the-loop step.

---

## Step 2: Pull and Deduplicate

### Pull

Query the Comms Log default view. Filter for entries where:
- Actions field is empty (not Done, Respond, or N/A)
- Created within the last N days (default 5, configurable)

### Pin = Tim's Review Queue

Any entry with Pin = YES gets surfaced in the "Tim's Decision
Queue" section regardless of auto-classification. These are
emails Tim flagged as "I routed this but I need to come back
to it."

### Thread Deduplication

**Never delete entries.** Deduplication is report-layer only.

Group entries by thread using these signals:
1. **Subject root** — strip "Re:", "RE:", "Fwd:", "Fw:" prefixes
   and compare. Entries with matching roots are likely the
   same thread.
2. **Reply To chain** — entries linked via the Reply To
   relation are definitively the same thread.
3. **Case Portal link** — entries linked to the same Case
   Portal entry AND sharing a subject root are the same thread.

Within each thread group:
- Identify the **most recent entry** (by Comm Date or Created)
  as the authoritative one. Present only this entry in the
  report.
- The older entries are silently skipped in the report. They
  are NOT modified in the comms log.
- Count and note: "5 entries in this thread" so the report
  shows thread volume.

### Duplicate detection

Two entries from different senders (e.g., Tim forwarded the
same email that Brittney also forwarded) with matching subject
roots and overlapping email content = duplicate. Present only
the most recent.

---

## Step 3: Auto-Classify

### Six Classification Buckets

| # | Bucket | What goes here |
|---|--------|---------------|
| 1 | **Action — assign/delegate** | Someone needs to own this task |
| 2 | **Action — Tim must handle** | Requires Tim's legal judgment |
| 3 | **Action — new PC intake** | New potential client needing PC Portal entry |
| 4 | **Info — team is handling** | Workflow in progress, no intervention |
| 5 | **Info — no action needed** | FYI, resolved, directive sent |
| 6 | **Strategy / follow-up** | Direction set, verify at next meeting |

### Auto-Classification Patterns

**Bucket 5 (no action needed):**
- Tim's outbound email with a directive, no pending question
- Client acknowledgment/thank-you with no request
- Tim answered a question definitively + recipient acknowledged
- Josue + billing/collections keywords (team managing)
- Email recall notifications
- Newsletter/marketing forwards
- System notifications (TrueFiling confirmations where no
  action is implied beyond filing)

**Bucket 4 (team is handling):**
- Brittney is the most recent KLG sender + no open client
  question in the thread
- Retainer/AdobeSign sent to client, awaiting signature
- Standard intake workflow steps in progress
- William executing a research or download task

**Bucket 3 (new PC intake):**
- Any entry mentioning a person not in the Case Portal +
  language suggesting potential representation, referral,
  or new matter
- Clio Grow intake form notifications
- Referrals from other attorneys mentioning a new case
- Cross-check: does a Case Portal entry exist? If no →
  flag as intake gap

**Bucket 6 (strategy / follow-up):**
- Tim + attorney discussed approach and set a direction
- Someone was told to do X but no trackable task was created
- "Can you respond?" / "Please handle" directives without
  confirmed execution

**Bucket 2 (Tim must handle):**
- Client asks a substantive legal question
- Co-counsel requests Tim's specific input on strategy
- Pinned entries (Pin = YES)
- Items requiring attorney judgment to decide next steps

**Bucket 1 (assign/delegate):**
- Client sends documents for filing (→ Brittney)
- Co-counsel requests action that a team member can handle
- Follow-up on directives Tim already gave (verify execution)
- Court filings that suggest new deadlines or work
- Download links not yet processed (→ William)

### Confidence and fallback

If the skill cannot confidently classify an entry, default to
**Bucket 1 (assign/delegate to Brittney)**, NOT Bucket 2 (Tim
must handle). The whole point is to keep Tim's list short.

### Court filings and new deadlines

Entries containing TrueFiling service notifications or court
notices should be checked for deadline implications. If the
entry mentions a new hearing date, briefing schedule, or
filing deadline, include it in the report with the deadline
highlighted and suggest posting to the relevant Slack matter
channel.

### Download link tracking

Entries with "Has Download Link" = Yes and "Downloaded" = NO
should be flagged for William's attention as part of his daily
download task.

---

## Step 4: Generate the Notion Triage Report

### Create the Project page

Create a new page in the Projects database with:
- **Project name:** "Comms Log Triage — Week of [date range]"
- **Status:** In progress
- **Priority:** High
- **Owner:** The person running the triage
- **Dates:** Start and end of the triage period
- **Summary:** "[X] entries triaged. [Y] action items, [Z]
  informational, [W] carried over."
- **Team Portals:** Link to PC Intake & Case Management Team
  (`3250fc06-a06c-80c2-9d28-da7c0b81c6b8`)
- **Comms Log:** Link to all comms log entries covered (where
  feasible within API limits)

### Page content structure

Use this structure for the page body:

```
> **Weekly Comms Log Triage Report**
> [X] entries triaged · [Y] action · [Z] informational
> *Generated [date] by Claude on [runner]'s behalf*

---

# Tim's decision queue

[Only items requiring Tim's legal judgment. 3–5 max.
Each with checkbox, instruction, and Notion link.]

---

# Action items — Brittney

## New PC intakes
[Checkbox items for new potential clients needing Portal entries]

## [Matter name 1]
[Checkbox items with specific instructions and Notion links]

## [Matter name 2]
[Checkbox items...]

## Download processing — William
[Items with unprocessed download links]

---

# Strategy / follow-up — flag for [day] meeting

[Checkbox items for directions set but not yet verified]

---

# Auto-resolved — informational (no action needed)

[Table: Entry | Matter | Reason — for the record only]

---

# Carried over from last week

[Any unchecked items from last week's report, with age]

---

# Triage metadata

[Period, count, breakdown, run type, notes]
```

### Per-item format

Each checkbox item should include:
1. **Bold matter name** and brief description
2. **Specific instruction to Brittney** (what to do, what
   info she needs from Tim, who to contact)
3. **Notion link** to the comms log entry
4. **Embedded ID** for parsing: `[CL:entry_id_here]`

Example:
```
- [ ] **ICN v. Palazuelos — prepare 30-day extension app.**
  Tim directed this. Brief due April 14, co-counsel out of
  state April 3–12. [Comms log](https://www.notion.so/...)
  [CL:3280fc06a06c81a2]
```

---

## Step 5: Send Slack Notification

Via `slack_send_message_draft` to #all-kowallawgroup. Format:

```
This is Claude posting on [runner]'s behalf.

📋 **Weekly Comms Log Triage Report — [Date Range]**

[X] comms log entries reviewed:
• [Y] action items for Brittney (including [Z] new PC intakes)
• [W] items needing Tim's decision
• [V] strategy items for Monday meeting
• [U] auto-resolved informational

**Highest priority:** [Top 1–2 items with deadlines]

Full report with checkboxes:
https://www.notion.so/[project_page_id]

Brittney — please work through the checklist on that page.
```

Keep the Slack message under 3,000 characters. All detail
lives on the Notion page.

---

## Step 6: Close the Loop (Next Run)

On the next triage run, Step 1 reads the prior project page:
- Checked items → update comms log Actions to Done/N/A
- Unchecked items → carry forward to new report
- Prior project → Status set to Done

Over time, the comms log's Actions field gets populated
through this cycle. The skill handles all writes — Brittney
never edits comms log records directly.

---

## Team-Runnability Notes

When Brittney or William runs the triage (e.g., "prepare for
team meeting" or "run comms log triage"):

- Skip the interactive mode. Go straight to report generation.
- The triage runs autonomously: pull → deduplicate → classify
  → generate Notion page → send Slack notification.
- The runner does NOT need to answer classification questions.
  The skill auto-classifies using the patterns above.
- Tim can opt into interactive mode ("walk me through the
  comms log items") — in that case, present entries one at a
  time with classification options, same as the calibration
  session format.

---

## Maintenance: Updating Classification Patterns

The patterns above were calibrated from a 15-entry sample on
March 20, 2026. As more triage runs are completed and Tim
provides feedback on misclassifications, update the patterns
in this file. Key areas likely to evolve:

- New team members or external contacts
- New matter types with different workflow patterns
- Changes to the comms log schema (new fields, new views)
- Refinement of the "new PC intake" detection heuristic
