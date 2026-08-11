# Email Triage Reference

## Core Workflow: One Email at a Time

Email triage presents emails **one at a time** with action options.
Do NOT batch-categorize and dump a sorted list. The goal is that
by the end of triage, every email is resolved: replied, delegated,
tasked, or explicitly skipped.

### Per-Email Flow

For each email:

1. **Present** the email: sender, subject, brief content summary,
   matter association (if identifiable from Case Portal or sender).

2. **Offer actions** via `ask_user_input` (single select):
   - **Reply now** — draft a reply
   - **Delegate** — compose a Slack delegation draft
   - **Create task** — create a Motion task
   - **Flag for later** — flag in Outlook via Zapier
   - **Skip / archive** — no action needed

3. **Execute** the chosen action immediately:
   - Reply now → use `message_compose` tool for the email draft,
     or compose inline for quick one-liners. If substantive legal
     judgment is needed, flag it.
   - Delegate → compose via `slack_send_message_draft` to the
     matter channel. Include: what needs doing, which matter,
     any deadline.
   - Create task → use Motion Create Task via Zapier. Include
     task name, project/workspace, assignee, priority, due date.
   - Flag → use Zapier Flag/Unflag Email tool. Pass email subject
     in the instructions field.
   - Skip → move on. Optionally suggest archiving.

4. **Move to the next email** only after the current one is resolved.

### End-of-Triage Consolidation

After all emails are processed:

1. **Per-person delegation punch lists.** If multiple items were
   delegated to the same person (e.g., three things for Brittney),
   compose ONE consolidated Slack draft (via `slack_send_message_draft`)
   summarizing all their items. Do NOT send separate messages per
   delegation — consolidate.

2. **Summary stats.** Report:
   - Total emails triaged
   - Actions taken: X replied, Y delegated, Z tasked, W flagged,
     V skipped
   - Items still needing Tim's attention (if any)

## Categorization Buckets

Use these categories for internal classification and to inform
how each email is presented. The user sees the email and action
options — not the category label directly.

| Category | Icon | Description | Typical Action |
|----------|------|-------------|---------------|
| Client action | 🔴 | Client email requiring substantive response | Reply now or flag |
| Court/filing | 🟡 | Court notices, filing confirmations, deadlines | Flag, note deadlines |
| Co-counsel | 🔵 | DZ, Ted, or other attorney communications | Reply or flag |
| Team internal | 🟣 | William, Brittney, Josue, Andi, Richard, Ryan | Delegate or reply |
| FYI | 🟢 | Newsletters, notifications, confirmations | Skip / archive |
| Delegatable | ⚪ | Items someone else can handle | Delegate |
| Low priority | ⬛ | Marketing, spam, subscriptions | Skip / archive |

## Categorization Rules

### Client Action (🔴)

Trigger: Email from a known client, or from an address
associated with an active matter in the Case Portal.

Subcategories:
- **Substantive question** — client asks about case strategy,
  timing, next steps, or outcome. Requires attorney judgment.
- **Document provision** — client sends requested documents.
  May be delegatable to Brittney for filing.
- **Scheduling** — client asks about meeting times, hearing
  dates, etc. May be delegatable.
- **Fee/billing** — payment questions, invoice disputes.
  Route to Andi.

### Court/Filing (🟡)

Trigger: Email from a court, clerk's office, or case management
system. Also: filing confirmations from Clearbrief, TypeLaw,
or TrueFiling.

Always flag — never auto-archive. Check for:
- New deadline (hearing date, briefing schedule, status conference)
- Ruling or tentative ruling
- Filing confirmation (note what was filed and when)

### Co-counsel (🔵)

Trigger: Email from DZ (David Zarmi), or from attorneys
associated with active co-counsel relationships.

Priority indicators:
- References a deadline → treat as 🟡
- Asks a substantive question → flag for Tim
- FYI/status update → lower priority

### Delegatable (⚪)

Trigger: Any email where the action can be completed by a
team member without attorney judgment:
- Document filing or formatting → Brittney
- Research requests from clients → William (after Tim review)
- Administrative tasks → Andi or Josue
- Calendar/scheduling → Andi

## Draft Reply Guidelines

When drafting email replies during triage:

- Match tone to the client relationship (professional but
  approachable for established clients; more formal for new).
- Always identify the matter and specific question.
- If reply involves substantive legal judgment, flag it:
  "⚠️ This draft touches on [issue]. Please review before
  sending."
- Keep replies concise. Clients appreciate brevity.
- Do NOT use legalese. Write like a normal person.
- Sign off as Tim unless instructed otherwise.
- Use the `message_compose` tool for email drafts so Tim
  gets the formatted compose widget with send options.

## Slack Delegation Format

When composing Slack delegations via `slack_send_message_draft`:

- Lead with "This is Claude posting on Tim's behalf."
- Include: what needs doing, which matter/case, any deadline,
  and where to find relevant files (SharePoint link if known
  from Motion custom fields).
- Post to the **matter channel**, not a DM.
- Use bare URLs — no angle brackets or markdown link syntax.
- If the matter channel is unknown, search Slack by case name
  before falling back to a DM.
