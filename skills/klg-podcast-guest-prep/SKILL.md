---
name: klg-podcast-guest-prep
description: "Discover podcast guests by topic or landscape scan, research confirmed guests, and build interview outlines with sourced questions and NotebookLM prompts for CALP. Triggers: 'podcast guest prep', 'interview prep', 'guest research', 'find podcast guests', 'who should we interview about', 'podcast guest discovery', 'suggest podcast guests', 'suggest podcast topics', 'whats hot for the podcast', 'podcast topic scan', 'find guests for CALP', 'landscape scan', 'podcast outline', 'CALP guest prep', 'prep for the interview', 'NotebookLM prompts for the podcast', 'whos writing about'. Also triggers when naming a guest for an upcoming episode, asking for a pre-interview briefing, or asking who is active in an area of California law. NOT for oral argument prep (klg-oral-argument), case-level deep research (klg-deep-research-prompts), or content queue (klg-content-research)."
---

# KLG Podcast Guest Prep

## Purpose

Two integrated workflows for the California Appellate Law
Podcast (CALP):

1. **Guest Discovery (Phase 0)** — Identify potential podcast
   guests by researching who is actively writing, speaking,
   or litigating on topics relevant to California trial and
   appellate attorneys. Supports topic-driven searches and
   recurring "What's Hot" landscape scans.

2. **Guest Preparation (Phases A–D)** — Once a guest is
   confirmed, build a comprehensive interview package: guest
   intelligence, interview architecture with style-calibrated
   questions, optional NotebookLM audio prompts, and a
   condensed briefing packet for recording day.

The hosts are Tim Kowal and Jeff Lewis. The podcast covers
appellate law, constitutional law, legal thought, and the
judicial process. The tone is intelligent, curious, and often
explores deeper themes — institutional trust, moral reasoning,
the craft of legal writing, and how courts actually work.

The target audience is **California trial and appellate
attorneys** — practitioners who want actionable insight, not
academic abstraction. Every guest and topic should pass the
test: "Would a trial lawyer in Riverside or a solo appellate
practitioner in San Francisco find this worth 45 minutes?"

## Required Context

Before beginning, read these files:

1. `/mnt/project/claude.md` — Citation standards, output
   rules, Slack posting rules, handoff structure, session
   logging, delivery format guidance, project preflight
   protocol, cross-platform handoff protocol
2. `references/interview-styles.md` — Interviewer style
   models and question category definitions
3. `references/notebooklm-prompts.md` — NotebookLM prompt
   templates for podcast prep (read only if Phase C is
   selected)
4. `references/workflow-patterns.md` — Session logging
   (Pattern 3)

## Entry Point Detection

The skill has two entry modes. Detect which one based on the
user's input:

**Discovery mode (Phase 0)** — The user provides a topic,
issue, legal development, or asks for a landscape scan.
No specific guest is named. Examples:
- "Find guests for the podcast on anti-SLAPP developments"
- "Who should we interview about appellate fee-shifting?"
- "What's hot for the podcast?"
- "Suggest podcast guests on AI in courts"
- "Monthly content scan"

**Prep mode (Phases A–D)** — The user names a specific guest
or references a confirmed upcoming interview. Examples:
- "Prep me for the interview with Justice Liu"
- "Guest prep for Professor Smith"
- "We're interviewing the author of that arbitration article"

If the input is ambiguous (e.g., "podcast help"), ask:

```
Are you looking to:
1. Discover potential guests for a topic or scan what's
   timely right now (Phase 0 — Guest Discovery)
2. Prep for a specific guest who's already confirmed
   (Phases A–D — Interview Prep)
```

## Running Mode

This skill runs in **Chat** (recommended). It does not need
the matter folder — it pulls from web search, Outlook, and
Notion. No Cowork access required.

If the user asks about Cowork vs. Chat:

```
This skill runs entirely in Chat. I'll research guests and
topics via web search, check Outlook for any email threads,
and search Notion for prior content and existing projects.
No matter folder needed.

Estimated time:
- Phase 0 (discovery): 15–25 minutes
- Phases A–B (guest prep): 15–30 minutes
- Phase C (NotebookLM): add 10 minutes
- Phase D (briefing packet): add 5 minutes
```

---

## Phase 0: Guest Discovery

### Overview

Identify potential podcast guests through targeted topic
research or broad landscape scanning. Produces a ranked
candidate shortlist with fit analysis, delivered to the
Notion Projects and Research databases.

Phase 0 has two modes:

- **Mode A: Topic-Driven Discovery** — The user provides a
  specific topic, legal issue, or theme. Claude researches
  who is active in that space.
- **Mode B: "What's Hot" Landscape Scan** — Claude scans
  recent California appellate developments, legal news, and
  the CLE circuit to surface timely topic/guest pairings.

### Step 0.1 — Project Preflight

**This step is mandatory before any research or Notion
deliverables are created.**

Follow the project preflight protocol from `claude.md`:

1. Search the Projects database
   (`df007c24-ffac-40d7-8e91-fb6763b6ecf6`) for an existing
   discovery project matching the topic or a recent landscape
   scan.

2. **If a project exists:** Link new deliverables to it.
   Check status and update as needed.

3. **If no project exists:** Create one:
   - **Title:**
     - Topic-driven: `CALP Guest Discovery — [Topic]`
     - Landscape scan: `CALP Guest Discovery — [Month Year]
       Scan`
   - **Category:** Operations
   - **Icon:** 🏗️
   - **Status:** In progress
   - **Priority:** Low (no court deadline; set Medium if
     tied to a scheduled recording date)
   - **Target Date:** 30 days from creation (default review
     target). If tied to a recording date or content
     calendar milestone, use that date instead.
   - **Team Portals relation:** Content & Networking
   - **Summary:** One paragraph describing the discovery
     scope and purpose
   - **Content:** Project overview, task checklist (see
     below), related resources

**Task checklist template for the project page:**

```
## Task Checklist

- [ ] Complete discovery research (Claude)
- [ ] Review candidate shortlist and select guest(s) (Tim)
- [ ] Deep research on selected candidate(s) (if warranted)
- [ ] Transition to interview prep (Phase A)
- [ ] Mark this project Done when episode prep is complete
      or discovery is closed
```

### Step 0.2 — Gather Discovery Intelligence

#### Mode A: Topic-Driven Discovery

The user has provided a topic, issue, or theme. Run these
research sweeps:

**Web search — legal publications and commentary:**
- Search for recent articles, blog posts, and commentary
  on the topic from California-focused legal publications
  (Daily Journal, Daily Appellate Report, California
  Lawyer, ABTL Report)
- Search national legal media (Law.com, ABA Journal,
  Jurist) for California-relevant coverage
- Search law review articles and SSRN papers on the topic
  (last 12–18 months)
- Search for CLE presentations, bar association panels,
  and conference talks on the topic
- Search for practitioners who have litigated significant
  recent cases on the topic (check appellate opinions
  for counsel of record)

**Web search — appellate opinions:**
- Search for recent published California appellate opinions
  on the topic (Court of Appeal and Supreme Court)
- Identify the authoring justices and any notable concurrences
  or dissents
- Note any pending petitions for review or cert petitions
  on the topic

**Web search — practitioners and academics:**
- Search for attorneys who have authored amicus briefs on
  the topic
- Search for law professors with expertise in the area
  (California law schools and national faculty writing
  about California law)
- Search for judges or former judges who have spoken
  publicly about the topic

**Notion search — prior CALP coverage:**
- Search the Content Production database
  (`dbce7904-f1f1-4356-a25f-9b5379257ae1`) for prior
  episodes on overlapping topics
- Search the Research database
  (`622bfafd-45b1-451a-b518-f72d86767cb0`) for any
  existing research on the topic
- Note what ground has been covered and what angles
  remain fresh

#### Mode B: "What's Hot" Landscape Scan

No topic provided — Claude scans the landscape. Run these
sweeps:

**Recent California appellate developments (last 60 days):**
- Search for significant published opinions from California
  Courts of Appeal and Supreme Court
- Search for grants of review by the California Supreme
  Court
- Search for cert grants or notable Ninth Circuit opinions
  touching California law
- Search for pending California Supreme Court cases with
  upcoming oral arguments
- Prioritize opinions that generated media coverage,
  practitioner commentary, or bar association discussion

**Legal news and trends:**
- Search Daily Journal, Daily Appellate Report, and
  California legal blogs for trending topics
- Search for recent California legislation affecting civil
  litigation and appeals
- Search for recent California Rules of Court amendments
  or proposed amendments
- Search for notable sanctions, disqualification orders, or
  procedural developments that affect trial practice

**CLE and conference circuit:**
- Search for upcoming CLE programs, ABTL events, bar
  association panels, and legal conferences with
  California appellate content
- Identify speakers and panelists who are presenting on
  timely topics
- Note anyone giving talks on topics CALP hasn't covered

**Notion — content history and ideas:**
- Search the Content Production database for recent
  episodes to identify gaps and avoid repeats
- Search Notion for any "Ideas" or content planning pages
  that might have queued topics

**Cross-reference for freshness:**
- For each topic surfaced, check whether CALP has covered
  it in the last 12 months. If so, note the episode and
  assess whether a new angle justifies revisiting.
- Prioritize topics where there is both timeliness (recent
  development) and a clear guest candidate (someone who
  wrote about it, litigated it, or decided it)

### Step 0.3 — Build the Candidate Shortlist

Compile findings into a ranked shortlist of 5–8 candidates.
For each candidate, provide:

```
## Candidate Shortlist

### 1. [Candidate Name]
**Role:** [Title, organization]
**The hook:** [Why this person, why now — the timely angle]
**Topic fit:** [What specific topic they'd cover]
**Audience value:** [Why California trial/appellate attorneys
  would care — what's the takeaway for practitioners?]
**CALP fit:** [What makes this a good CALP conversation vs.
  a generic CLE talk? Is there a story, a debate, a
  perspective that makes it interesting?]
**Evidence of public engagement:** [Prior podcast appearances,
  articles, CLE talks, public commentary — signals they'd
  be a good interview, not just knowledgeable]
**Potential episode angle:** [1–2 sentence pitch for the
  episode]
**Deep research warranted?** [Yes/No — Yes if the topic
  involves novel legal theories, cross-jurisdictional
  issues, quantitative data, or if the candidate's body
  of work needs thorough review before outreach]
**Prior CALP coverage:** [Any related episodes, or "None"]
```

**Ranking criteria (in order of weight):**

1. **Timeliness** — Is there a reason to do this episode
   NOW? Recent opinion, pending legislation, cert grant,
   emerging trend.
2. **Audience alignment** — Will California litigators
   find this actionable? Does it help them win cases,
   avoid errors, or understand emerging risks?
3. **Interview potential** — Will this person be an
   engaging guest? Evidence of public speaking, prior
   interviews, strong writing voice, or willingness to
   take positions.
4. **Topic freshness** — Has CALP covered this recently?
   Is there a genuinely new angle?
5. **Accessibility** — Is this person likely to say yes?
   Practitioners and academics are more accessible than
   sitting justices.

### Step 0.4 — Present Shortlist and Offer Next Steps

Present the shortlist to the user. Then offer:

```
Here are [N] candidates ranked by timeliness and audience
fit. For each one, I can:

1. **Start interview prep now** — Jump to Phase A with
   the discovery research already loaded. Best if you've
   already confirmed the guest or want to build the
   outline before reaching out.

2. **Run deep research** — Invoke the full deep research
   pipeline for a thorough review of the candidate's
   body of work, positions, and the legal landscape
   around their topic. Best for candidates with novel
   theories, complex issues, or where you want to be
   deeply prepared before the first email.

3. **Draft an outreach email** — I can draft an
   invitation email to the candidate proposing the
   episode angle.

4. **Save and revisit** — The shortlist is on the Notion
   project page. Come back when you're ready to pick
   a guest.

Which candidate(s) interest you, and what would you like
to do next?
```

Use `ask_user_input` for quick selection:

**Panel 1 — "Which candidate interests you most?"**
Options: [Top 4 candidate names from the shortlist, plus
"Show me more options"]

**Panel 2 — "What's the next step?"**
Options:
- "Start interview prep (Phase A)"
- "Run deep research first"
- "Draft outreach email"
- "Save for later"

### Step 0.5 — Deep Research Path (When Selected)

When the user selects "Run deep research" for a candidate:

**Invoke `klg-deep-research-prompts` with the following
adaptations:**

1. The "case file" input is the candidate shortlist entry
   plus any articles, opinions, or publications gathered
   during discovery. Claude synthesizes these into the
   context that the deep research skill needs.

2. The project page created in Step 0.1 serves as the
   parent project. The deep research skill's project
   preflight should find and link to this existing project
   rather than creating a new one. If the deep research
   skill creates its own sub-project (Category = Case
   Support, Support Type = Research Pipeline), that is
   acceptable — link it to the same Team Portal (Content &
   Networking) and note the parent discovery project in
   the summary.

3. **Prompt generation focus for podcast discovery:**
   Research prompts should be tuned to the podcast
   context, not the litigation context. Instead of
   "What are the grounds for reversal?" the prompts
   should explore:
   - The candidate's published positions and how they've
     evolved
   - Counter-arguments and critiques of the candidate's
     views
   - The practical implications for California litigators
   - The current state of the law in the candidate's
     area, including circuit splits and pending cases
   - Background on the candidate's career, notable cases,
     and public commentary
   - Any controversies, retractions, or position changes
     that would make for compelling interview material

4. **Tier guidance for podcast research:**
   - **Core (always run):** The candidate's main thesis
     or area of expertise and its current legal landscape
   - **Important (run if time permits):** Counter-arguments,
     practical implications for practitioners, and the
     candidate's track record
   - **Optional (run for high-profile guests):** Deep
     background, career arc, public commentary beyond
     their primary topic

5. After deep research prompts are generated, the standard
   pipeline takes over: William (or Tim) runs Comet,
   Claude compiles, etc. The discovery project page tracks
   progress.

6. **Return from deep research:** When the research
   pipeline completes, the compiled research pre-loads
   into Phase A as context for the guest intelligence
   step.

### Step 0.6 — Outreach Email Path (When Selected)

When the user selects "Draft outreach email":

Follow the delivery format protocol from `claude.md`. For
a guest outreach email, the inline message composer
(`message_compose_v1`, kind: "email") is the default —
skip the format question.

Generate 2–3 strategic variants:

1. **Direct pitch** — Concise, professional, leads with
   the episode angle and why their expertise matters to
   CALP's audience
2. **Collegial approach** — Warmer, references a specific
   piece of their work, positions the invitation as a
   conversation between peers
3. **Referral hook** — If someone in Tim's network
   recommended the guest, leads with that connection

Each variant should include:
- Who CALP is and its audience (brief — 1–2 sentences)
- The specific episode angle (not just "we'd like to
  have you on")
- Why now (the timely hook)
- Logistics overview (format, length, scheduling)
- Tim's signature block

### Step 0.7 — Deliver Discovery Research to Notion

Create a **Research database entry** with:

- **Title:** `Guest Discovery — [Topic or "Landscape Scan
  Month Year"]`
- **Tags:** CALP - Guest Discovery, KLG Podcast - CALP
- **Date:** Today
- **Projects relation:** Link to the discovery project
  created in Step 0.1
- **Content:** The full shortlist with all candidate
  profiles, ranking rationale, prior CALP coverage
  analysis, and any deep research links

Also update the **project page** with:
- Links to the Research entry
- Updated checklist (mark discovery research complete)
- Notes on any candidates the user expressed interest in

---

## Phase 0 → Phase A Transition

When the user selects a guest from the shortlist (or when a
guest is confirmed via outreach), the discovery project
becomes the umbrella project for the full episode prep
workflow.

**Update the project page:**
- **Title:** Update to include the guest name:
  `CALP — [Guest Name]: [Episode Topic] (from [original
  discovery topic])`
- **Status:** Keep "In progress"
- **Priority:** Update if a recording date is set (Medium
  if within 30 days, High if within 14 days)
- **Target Date:** Update to the recording date if known
- **Checklist:** Add the Phase A–D tasks:
  ```
  - [x] Complete discovery research (Claude)
  - [x] Select guest (Tim)
  - [ ] Deep research (if applicable)
  - [ ] Guest intelligence and profile (Phase A)
  - [ ] Interview outline (Phase B)
  - [ ] NotebookLM prompts (Phase C, if selected)
  - [ ] Briefing packet (Phase D, if selected)
  - [ ] Recording complete
  - [ ] Mark this project Done
  ```

**Pre-load discovery context into Phase A:**
When entering Phase A after discovery, Claude already has
the candidate profile from Step 0.3. Skip redundant
research — Phase A.1 should focus on filling gaps the
discovery didn't cover (email threads, deeper career
background, prior podcast appearances), not repeating
the discovery sweep.

---

## Phase A: Guest Intelligence

### Step A.1 — Gather Context from All Sources

Run these in parallel. **If this phase follows Phase 0,
skip research that was already completed during discovery
and focus on filling gaps.**

**Web search (always):**
- Guest's professional background, current role, bio
- Recent publications, articles, blog posts, or notable
  opinions (last 6 months especially)
- Prior podcast appearances (other shows) — note their
  interview style, favorite topics, and any positions
  they've staked out
- Any current controversies, recent honors, or timely
  developments in their area
- Social media presence and recent public commentary

**Outlook email search (always):**
- Search for the guest's name in Outlook to find the
  invitation thread, topic agreements, scheduling details,
  and any documents shared
- Note who invited the guest (Tim, William, or someone
  else) and what the original hook was
- Pull any topic suggestions or constraints from the
  email exchange

**Notion search (always):**
- Search the Content Production database for any existing
  episode record for this guest
- Search the Research database for any prior research
  related to the guest's topics or area of law
- Check for prior CALP episodes on overlapping topics
  (avoid repeating ground already covered unless
  deliberately revisiting)
- **If following Phase 0:** Check for the discovery
  research page and any deep research outputs already
  linked to the project

### Step A.2 — Build the Guest Profile

Compile findings into a structured profile:

```
## Guest Profile

**Name:** [Full name with titles/honorifics]
**Current Role:** [Title, organization]
**Background:** [2–3 sentence summary of career arc]
**Notable Work:** [Key publications, opinions, or positions]
**Interview Style Notes:** [Based on prior appearances —
  e.g., "conversational and candid," "precise and formal,"
  "likes to tell stories," "tends to deflect personal
  questions"]
**The Hook:** [Why this guest, why now — the timely angle]
**Email Context:** [Summary of any topic agreements or
  constraints from the invitation thread]
**Prior CALP Coverage:** [Any related episodes or research]
**Discovery Context:** [If following Phase 0 — summary of
  how this guest was identified and key findings from
  discovery research]
```

### Step A.3 — Present Profile and Confirm Scope

Present the guest profile to the user. Then ask:

```
Here's what I've found on [Guest Name]. Before I build
the outline, a few questions:
```

Use `ask_user_input` for efficient selection:

**Panel 1 — Scope:**
- "What's the main focus for this episode?"
  Options: [Generate 3–4 specific angle options based on
  research, plus "Other — I'll describe"]

**Panel 2 — Style:**
- "What interview style fits this guest?"
  Options: [Present 3–4 style options from the style
  models — see references/interview-styles.md — selected
  based on the guest's personality and the episode angle]

**Panel 3 — Depth:**
- "How deep should we go?"
  Options:
  - "Full outline with 8–12 segments"
  - "Focused outline with 4–6 segments"
  - "Lightning round only — quick-hit questions"

Also ask (inline, not as buttons):
- "Are there specific topics you or Jeff want to make sure
  we cover?"
- "Any topics that are off-limits?"
- "Is there a time constraint for the episode?"

### Step A.4 — Cross-Platform Collaboration Offer

After building the guest profile and before moving to
Phase B, offer a ChatGPT collaboration if the guest or
topic warrants deeper independent analysis:

> "Before I build the interview outline, would you like
> ChatGPT to do an independent research pass on [Guest
> Name]'s positions? This is most useful for guests with
> complex or controversial views where you want to stress-
> test the angles before recording. ChatGPT would read the
> guest profile and independently suggest interview angles,
> potential pushback points, and topics I might have missed."

Collaboration type: Type 1 (Second-Opinion Issue Spotting).

If accepted, follow the Cross-Platform Handoff Protocol
from `claude.md` — create the Notion handoff page first,
then generate the ChatGPT prompt. The handoff page links
to the discovery/prep project.

---

## Phase B: Interview Architecture

### Step B.1 — Select Question Categories

Based on the user's style selection and the guest's profile,
select the appropriate question categories. The full category
menu is defined in `references/interview-styles.md`. Not
every category applies to every guest — select based on fit.

**Always include:**
- At least one substantive legal/professional category
- At least one personal/reflective category
- A closing segment (lightning round or signature close)

**Category selection logic:**
- Judicial guests → Bench & Bar, Scalia or Holmes?, Personal
- Practitioner guests → Brief-Writing Room, Bench & Bar,
  Lawyer as Citizen
- Academic guests → Thinking Like a Lawyer, Scalia or Holmes?,
  Lawyer as Citizen
- Legal media/commentator guests → Brief-Writing Room,
  Lawyer as Citizen, Personal
- Non-legal guests → Adapt categories to their domain;
  use Lawyer as Citizen and Personal as anchors

### Step B.2 — Build the Segment Outline

For each segment, generate:

1. **Segment title** — Descriptive, not just the category name
   (e.g., "The Oral Argument Craft" not just "Bench & Bar")
2. **Segment purpose** — One sentence on what this segment
   is trying to draw out
3. **3–5 questions** — Sourced where possible (referencing
   the guest's own writing, a recent case, a prior statement)
4. **Tim's angle** — What Tim might specifically probe or
   push back on (based on KLG's appellate specialist
   perspective)
5. **Jeff's angle** — Where Jeff might take the conversation
   (if the topic suggests a natural split)
6. **Suggested follow-ups** — 1–2 follow-up directions if
   the guest gives a particularly interesting answer

### Step B.3 — Calibrate to the Selected Style

Apply the selected interviewer style to the questions. This
is not just tone — it affects question structure:

- **Buckley-style questions** lead with a provocative premise
  and invite the guest to engage with it
- **Russ Roberts-style questions** are Socratic and open-ended,
  designed to explore assumptions
- **Metaxas-style questions** are deeply informed but delivered
  with irreverent humor — they disarm the guest and open up
  unexpected terrain
- **Brian Lamb-style questions** are minimalist — short,
  direct, and let the guest fill the space
- **Ezra Klein-style questions** interrogate frameworks and
  mental models
- **Dick Cavett-style questions** are literary and witty,
  with elegant irreverence

See `references/interview-styles.md` for the complete style
guide. The user can also request a blend (e.g., "Buckley with
a Metaxas edge").

### Step B.4 — Flag Research Gaps

After building the outline, identify any claims, references,
or topics that need verification before recording. Categorize:

- **Quick verification (web search before recording)** — e.g.,
  confirm a case citation, check current status of litigation
- **Deep research (full pipeline)** — e.g., quantitative
  data on a trend, multi-source verification of a claim.
  If selected, invoke `klg-deep-research-prompts` linked
  to the episode prep project.
- **Not critical** — color commentary or tangent material
  that the guest will supply

### Step B.5 — Deliver to Notion

Create or update the episode record in the **Content
Production database** (data source:
`dbce7904-f1f1-4356-a25f-9b5379257ae1`).

**If an episode record already exists:** Update it with the
outline content.

**If no episode record exists:** Create one with:
- **Name:** `CALP — [Guest Name]: [Episode Title]`
- **Type:** 🎙Podcast
- **✳Status:** 📝 In Progress
- **Recording Date:** [If known from email context]
- **Icon:** 🎙

Also create a **Research database entry** (or update the
existing discovery research page if Phase 0 ran) with:
- **Title:** `Podcast Interview Prep — [Guest Name]:
  [Topic Summary]`
- **Tags:** CALP - Guest, KLG Podcast - CALP, Claude
  Session Log
- **Publish or Pass?:** Podcast
- **Date:** Today
- **Projects relation:** Link to the project page
- **Content:** The full outline with guest profile, segment
  structure, questions, research gaps, and production notes

Link the Research entry to the Content Production entry
via the appropriate relation if available, or note the
cross-reference in both pages.

### Step B.6 — Offer Next Steps

After delivering the outline:

```
The interview outline is live in Notion. Here's what's
available next:

1. **NotebookLM prompts** — I can generate audio session
   prompts so you and Jeff can absorb the guest's work
   and positions before recording. (Phase C)
2. **Briefing packet** — A condensed one-pager for
   recording day with key talking points, logistics,
   and must-ask questions. (Phase D)
3. **Research gap resolution** — I can run quick
   verifications on the flagged items now, or kick off
   the full deep research pipeline for deeper gaps.
4. **Guest email** — I can draft a pre-interview email
   to the guest with proposed topics (using the message
   composer).
5. **ChatGPT red team** — I can hand off the outline to
   ChatGPT for a devil's advocate pass — what pushback
   points and uncomfortable questions should Tim and Jeff
   be ready for?

Which would you like?
```

---

## Phase C: NotebookLM Prompt Generation

### When to Run

When the user selects NotebookLM prompts from the Phase B
menu, or explicitly asks for "NotebookLM prompts for the
podcast," "generate notebook prompts," or similar.

### Step C.1 — Read the NotebookLM Reference

Read `references/notebooklm-prompts.md` for the prompt
templates and NotebookLM settings.

### Step C.2 — Generate Prompts

Generate 2–3 tailored NotebookLM prompts based on the
guest profile and episode angle. The templates in the
reference file provide the starting framework — customize
with guest-specific content.

**Standard prompt set for podcast guest prep:**

1. **"The Guest's Best Case"** — Deep Dive into the guest's
   thesis, recent publications, or notable positions. Two
   speakers explore and steelman the guest's ideas.
2. **"The Pushback Episode"** — Debate format where one
   speaker challenges the guest's positions. Prepares Tim
   and Jeff to ask informed, challenging questions.
3. **"The Background Briefing"** — Primer on the guest's
   area of expertise, recent developments, and the
   landscape the episode will cover. Designed for
   absorption, not advocacy.

Not every episode needs all three. Select based on:
- High-profile or controversial guest → all three
- Technical/specialist guest → prompts 1 and 3
- Casual/conversational episode → prompt 3 only
- Guest whose positions Tim wants to challenge → prompt 2
  is essential

### Step C.3 — Specify Source Documents

For each prompt, list exactly which documents should be
uploaded to NotebookLM:

- Guest's recent articles or publications (provide URLs
  or note that William should download them)
- The interview outline itself (export from Notion)
- Any case opinions or legal documents relevant to the
  episode topics
- Prior CALP episodes on related topics (if available
  as transcripts)
- Deep research memos (if the deep research pipeline was
  run for this guest during Phase 0)

**Important:** NotebookLM works best with focused source
sets. Do NOT tell the user to upload everything — curate
the sources for each prompt.

### Step C.4 — Post to Notion and Offer Slack Handoff

Add the NotebookLM prompts as a new section on the existing
Research database page (the interview prep page created in
Phase B or carried forward from Phase 0).

Then offer:

```
The NotebookLM prompts are on the Notion page. Would you
like me to send the setup instructions to William (or
another team member) via Slack so they can generate the
audio sessions?
```

If yes, post a Slack message to the appropriate channel
(or `#all-kowallawgroup` if no episode-specific channel
exists) following the two-zone handoff structure:

**Zone 1 — ACTION ITEMS:**
1. Open the Notion page: [URL]
2. For each NotebookLM prompt listed on the page:
   - Open a new NotebookLM notebook
   - Upload the source documents listed for that prompt
   - Set the Format, Length, and Language per the settings
     table on the Notion page
   - Copy the prompt text into the custom prompt field
   - Generate the audio overview
   - Save the audio file with the session name
3. When all audio sessions are generated, post in this
   channel: "NotebookLM sessions complete for [episode
   name]."

**Zone 2 — FOR YOUR REFERENCE:**
- Episode: [Guest name and topic]
- Recording date: [If known]
- Number of prompts: [N]
- Estimated time: ~5 minutes per prompt setup

---

## Phase D: Briefing Packet

### When to Run

When the user requests a briefing packet, or when the
recording date is imminent and the user says "prep me for
tomorrow's recording" or similar.

### Step D.1 — Generate the Packet

Produce a condensed one-page briefing:

```
# Pre-Interview Briefing: [Guest Name]
## [Episode Title]
### Recording: [Date, Time, Platform]

## Guest at a Glance
[3–4 bullet summary: who they are, the hook, their style]

## Must-Ask Questions (Top 5)
[The five strongest questions from the outline — the ones
that will definitely make the episode. Sourced and ready.]

## Key Facts to Have Ready
[Specific dates, case names, statistics, or claims that
Tim/Jeff should have at their fingertips]

## Potential Tangents Worth Pursuing
[2–3 natural tangent directions if the conversation opens up]

## Research Verification Status
[Quick status on each flagged research gap — verified,
unverified, or not critical. Include deep research status
if the pipeline was run.]

## Production Notes
[Platform link, scheduling conflicts, any guest preferences]
```

### Step D.2 — Deliver

Ask the user how they want the briefing delivered:
- **Inline** (default for a quick one-pager)
- **Notion** (append to the existing interview prep page)
- **PDF** (for printing or reading on a device)

---

## Notion Delivery Standards

### Projects Database

The Projects database
(ID: `df007c24-ffac-40d7-8e91-fb6763b6ecf6`) holds the
discovery/episode project page. See Step 0.1 for the
project setup.

### Content Production Database

The Content Production database
(ID: `dbce7904-f1f1-4356-a25f-9b5379257ae1`) is the
canonical location for episode records. Use the schema
returned by fetching the database — do not assume property
names.

### Research Database

The Research database
(ID: `622bfafd-45b1-451a-b518-f72d86767cb0`) holds the
detailed research and interview prep content. Standard
properties:

- **Title:** Varies by phase:
  - Discovery: `Guest Discovery — [Topic or "Landscape
    Scan Month Year"]`
  - Interview prep: `Podcast Interview Prep — [Guest]:
    [Topic]`
- **Tags:** CALP - Guest Discovery or CALP - Guest (as
  appropriate), KLG Podcast - CALP, Claude Session Log
- **Publish or Pass?:** Podcast
- **Date:** Today's date
- **Projects relation:** Link to the project page
- **Note:** Brief description of the content

### Cross-References

When both a Content Production entry and a Research entry
exist, note the cross-reference in both:
- On the Research page: "Episode record: [Content
  Production page URL]"
- On the Content Production page: "Interview prep:
  [Research page URL]"

Both should also link to the project page.

---

## Session Logging

This skill follows the global session logging protocol
defined in `claude.md` and detailed in
`references/workflow-patterns.md` Pattern 3. After every
substantive response, append the one-liner prompt:

```
📝 Update the Notion session log? (yes / not yet / always / never)
```

For podcast guest prep sessions, the session log is
typically the Research database entry itself (the
discovery research page or interview prep page). If the
user says "yes" and the Research page already exists,
append the latest exchange to that page rather than
creating a separate session log entry.

---

## Pipeline Position

This skill bridges the **Content & Networking** track and
the **Research Pipeline** when deep research is invoked:

- **Before Phase 0:** Content calendar planning, topic
  ideation, listener feedback (manual or via content
  planning sessions)
- **Phase 0 → Deep Research (optional):** Invokes
  `klg-deep-research-prompts` for candidates warranting
  thorough research. The full five-step pipeline runs
  under the discovery project.
- **Phase 0 → Phase A:** Discovery research pre-loads
  into guest intelligence
- **Phase A → ChatGPT handoff (optional):** Cross-platform
  second opinion on interview angles
- **After Phase D:** Recording, editing, publication
  (manual)

**Project lifecycle:**
- A discovery project (Category: Operations) is created
  at Phase 0 and carries through the entire workflow
- The project title updates when a guest is selected
- The project reaches Done when episode prep is complete
  (Phase D delivered) or the discovery is closed without
  selecting a guest

**When deep research is invoked:**
The deep research pipeline creates its own Research
database entries and may create a sub-project (Category:
Case Support, Support Type: Research Pipeline). These
link to the same Team Portal (Content & Networking) and
reference the parent discovery project. The compiled
research feeds into Phase A.

---

## What This Skill Does NOT Do

- **Record or edit the podcast** — That's manual
- **Generate show notes or transcripts** — Post-production
- **Schedule the recording** — Andi handles scheduling
- **Manage the content calendar** — Use the Content
  Production database directly
- **Process the blog/newsletter queue** — Use
  `klg-content-research` for that
- **Oral argument prep** — Use `klg-oral-argument`
- **Deep research on case issues** — Use
  `klg-deep-research-prompts` directly for case-level
  research not tied to podcast guest discovery
