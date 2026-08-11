# Pending claude.md changes

This file collects every backlog item whose fix is "add/change a rule in
claude.md," staged here because this repo does not yet have the real,
current claude.md to edit (see README "STATUS" and Task 1 in the AI OS —
Edwyn delegation batch). The moment the real file lands, these should be
applied together as one clean, reviewed commit — consistent with the
"figure out the right home, implement once, cleanly" preference noted on
the Westlaw item below — rather than piecemeal edits that each need their
own diff review.

Each entry: source backlog link, proposed section, exact text to add,
scope/applies-to notes.

---

## 1. Westlaw Find & Print format (global rule)

- **Source:** [Honor Westlaw Find & Print format](https://app.notion.com/p/3650fc06a06c81b09fd3f4dd54d12b1e) (Urgent)
- **Proposed section:** new "Westlaw Find & Print" heading (Tim's own note:
  the global claude.md rule is the right home since the defect recurs
  across skills with contradictory instructions)
- **Status:** the skill-level half of this fix already shipped —
  `klg-cite-check` v0.2.0 (2026-08-11) — see CHANGELOG.md. This entry is
  only the *ad hoc session* half: the rule needs to apply even when no
  skill is invoked.
- **Text to add:**

  > **Westlaw Find & Print format.** Whenever producing a Find & Print
  > list — inside a skill or ad hoc — format it as the bare reporter
  > citation only: volume/reporter/page, no case names, no years, no
  > pincites, no parentheticals, no priority labels. One citation per
  > line, deduplicated. Example:
  > ```
  > 19 Cal.2d 807
  > 11 Cal.App.5th 626
  > 579 U.S. 197
  > ```
  > Anything else gets rejected by Westlaw's Find & Print search box.

---

## 2. Never CC clients on emails to opposing counsel

- **Source:** [Never CC clients on emails to opposing counsel](https://app.notion.com/p/3670fc06a06c817fb9a3e6436b438847) (Urgent)
- **Proposed section:** new subsection under "Client Communication Rules"
  (or a peer section), titled "Client Email Routing"
- **Status:** claude.md-only — no skill file or shared reference exists
  to carry a partial fix; nothing else to do until the real file arrives.
- **Text to add** (drafted in the backlog entry itself, reproduced here
  verbatim so it doesn't need re-fetching):

  > **Never CC clients on emails to opposing counsel or third parties.**
  > When sending correspondence to opposing counsel, opposing parties,
  > courts, mediators, or other external third parties, do not include
  > the client (or any party whose communications should remain
  > privileged) on the CC line. Instead, send the email first and then
  > forward a separate copy to the client. This applies equally when
  > (a) Claude is drafting an email for the firm to send, (b) Claude is
  > producing instructions for staff (Slack handoffs, punch lists,
  > paralegal directions), and (c) Claude is suggesting a distribution
  > list in any client-communication context.
  >
  > The rule exists because CC'ing the client makes the client a thread
  > participant. A single Reply All can then route attorney-client
  > communications, strategic discussion, or settlement positioning
  > directly to opposing counsel. Forwarding separately preserves the
  > client's access to the communication without creating that exposure.
  >
  > Exception: when the client is the *recipient* of the email and
  > opposing counsel is being CC'd (e.g., transmitting a draft to the
  > client with opposing counsel in the loop as a courtesy), the rule
  > does not apply because the email's primary audience is already
  > internal. This should be rare.

- **Scope note:** applies across all correspondence skills
  (klg-conflict-waiver, future demand/settlement-letter skills),
  client-communication skills (response plan and case-assessment client
  memos), klg-daily-triage (email routing suggestions), and all ad hoc
  email drafting and staff Slack handoffs for correspondence tasks.

---

*(Add new entries below this line as Lane 2/3 backlog items are worked
through one by one.)*
