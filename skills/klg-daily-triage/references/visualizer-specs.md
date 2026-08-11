# Visualizer Widget Specifications

## General Design Principles

- Use CSS variables for theming (light/dark mode support).
- Keep background transparent.
- Use clean, professional typography.
- Color coding: 🔴 red = urgent/overdue, 🟡 yellow = upcoming,
  🟢 green = on track, 🔵 blue = informational.
- Interactive elements should use `sendPrompt()` to trigger
  Claude actions (e.g., "Delegate this task to William").
- Load the appropriate Visualizer read_me module before
  rendering (diagram, chart, interactive, or mockup).

---

## Morning Triage Widget

### Layout

```
┌──────────────────────────────────────────────┐
│  ☀️ Morning Triage — [Date]                  │
│  [X] tasks today · [Y] emails · [Z] deadlines│
├──────────────────────────────────────────────┤
│                                              │
│  🔴 DEADLINE ALERTS                          │
│  ┌──────────────────────────────────────┐    │
│  │ Matter    │ Deadline │ Days │ Type   │    │
│  │ Meehan    │ Mar 25   │  6   │ Brief  │    │
│  │ Sparagos  │ Mar 22   │  3   │ Filing │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  📋 TODAY'S TASKS (by priority)              │
│  ┌──────────────────────────────────────┐    │
│  │ ⬆ ASAP  │ Review Meehan brief      │    │
│  │ ⬆ HIGH  │ DZ call re: Petersen     │    │
│  │ → MED   │ Sparagos research review  │    │
│  │ ↓ LOW   │ Update firm website copy  │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  📧 INBOX (categorized)                      │
│  ┌──────────────────────────────────────┐    │
│  │ 🔴 3 Client action                   │    │
│  │ 🟡 1 Court notice                    │    │
│  │ 🔵 2 Co-counsel                      │    │
│  │ 🟢 5 FYI                             │    │
│  │ ⚪ 2 Delegatable                     │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  🎯 RECOMMENDED FOCUS                        │
│  1. [Top priority item] (~X min)             │
│  2. [Second priority] (~Y min)               │
│  3. [Third priority] (~Z min)                │
│                                              │
│  [Delegate via Slack] [Draft reply] [Refresh]│
└──────────────────────────────────────────────┘
```

### Implementation Notes

- Build as a single HTML widget (not React — HTML is simpler
  for data-heavy dashboards).
- Use a card-based layout with sections.
- Deadline alerts section: table with conditional row colors
  (red for ≤3 days, yellow for ≤7 days).
- Tasks section: sorted list with priority icons.
- Email section: collapsible categories with counts. Clicking
  a category expands to show individual emails.
- Action buttons use `sendPrompt()`:
  - "Delegate via Slack" → `sendPrompt("Delegate the
    [task/email] to [person] via Slack")`
  - "Draft reply" → `sendPrompt("Draft a reply to the
    email from [sender] about [subject]")`
- Responsive: should work on both desktop and mobile widths.

---

## Weekly Planning Widget

### Layout

```
┌──────────────────────────────────────────────┐
│  📅 Weekly Plan — [Date Range]               │
├──────┬──────┬──────┬──────┬──────┬──────────┤
│ MON  │ TUE  │ WED  │ THU  │ FRI  │ Capacity │
├──────┼──────┼──────┼──────┼──────┼──────────┤
│ Task │ Task │ Task │ Task │ Task │ 5/6 hrs  │
│ Task │      │ Task │ Task │      │ 3/6 hrs  │
│ 📌   │      │      │ 📌   │      │          │
├──────┴──────┴──────┴──────┴──────┴──────────┤
│  📌 = Filing deadline                        │
│  ⚠️ Mon, Thu: OVERCOMMITTED                  │
│  💡 Tue, Fri: CAPACITY AVAILABLE             │
│                                              │
│  Suggestions:                                │
│  • Block Tue AM for Meehan brief writing     │
│  • Move [task] from Mon → Wed                │
│                                              │
│  [Apply suggestions] [Refresh]               │
└──────────────────────────────────────────────┘
```

### Implementation Notes

- Five-column grid (Mon–Fri) with task cards.
- Task cards show: name, project/matter, priority icon,
  estimated duration.
- Capacity bar under each day (filled/total hours).
- Deadline pins (📌) overlaid on the relevant days.
- Color: red for overcommitted days, green for under-
  committed, neutral for balanced.
- Suggestions section at the bottom with actionable items.
- "Apply suggestions" button uses `sendPrompt()` to
  trigger Motion task updates.

---

## Team Pulse Widget

### Layout

```
┌──────────────────────────────────────────────┐
│  👥 Team Pulse — [Date]                      │
├──────────────────────────────────────────────┤
│                                              │
│  Team Member  │ Tasks │ Overdue │ Status     │
│  ─────────────┼───────┼─────────┼────────    │
│  Tim          │  12   │   2     │ ⚠️ Heavy   │
│  Ted          │   5   │   0     │ 🟢 OK      │
│  William      │   8   │   1     │ 🟡 Watch   │
│  Brittney     │   4   │   0     │ 🟢 OK      │
│  Richard      │   3   │   0     │ 🟢 OK      │
│  Ryan         │   6   │   1     │ 🟡 Watch   │
│                                              │
│  🔥 BOTTLENECKS                              │
│  • William: 3 research jobs queued           │
│  • Tim: 2 overdue tasks (Meehan, Sparagos)  │
│                                              │
│  [Reassign tasks] [Post to Slack] [Refresh]  │
└──────────────────────────────────────────────┘
```

### Implementation Notes

- Table layout with team members as rows.
- Status column uses traffic light colors.
- Bottleneck section highlights specific issues.
- Action buttons for reassignment and Slack posting.
- If team member data requires multiple Find Task calls,
  batch them efficiently to stay within Zapier task budget.
