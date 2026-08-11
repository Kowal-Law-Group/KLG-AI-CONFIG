---
name: klg-content-research
description: "Batch-process the Research database Need Research queue for content production (blog, podcast, newsletter). Harvests all items from the Blog This: Add Research view, triages each as case vs. article, resolves citations, generates a Westlaw Find and Print list, and after Westlaw output is uploaded extracts case text into each Notion record and flips status to Further Review. Use whenever the user says 'process the content queue', 'research the blog queue', 'run content research', 'batch research', 'process need research items', 'blog research pipeline', 'content pipeline', 'process the need research view', or references batch-processing the Need Research items for content production. NOT for case-level deep research (use klg-deep-research-prompts) or case assessments."
---

# KLG Content Research Pipeline

## Purpose

Batch-process the "Blog This: Add Research" view in the
Research database. This view contains recent cases, articles,
and legal news items tagged for potential content production
(blog posts, podcast episodes, newsletter items) whose
"Publish or Pass?" status is "Need Research."

The skill automates what William currently does manually:
finding each case, copying the text, pasting it into Notion,
and updating the status. It handles cases (via Westlaw) and
non-case items (via URL fetch) in a single batch run.

## Required Context

Before running, read these reference files:

1. `references/notion-schema.md` -- Research database properties
2. `references/triage-rules.md` -- How to classify items
3. `references/comet-westlaw-prompt.md` -- Westlaw prompt template
4. `references/parsing-guide.md` -- Westlaw file extraction
5. `references/handoff-standards.md` -- Handoff format

## Three Phases

**Phase A -- Triage & Citation Harvest (Claude)**
Query Notion, classify each item, resolve citations, produce
a Westlaw Find & Print list.

**Phase B -- Westlaw Find & Print (William via Comet)**
Standard batch pull. No Claude involvement.

**Phase C -- Extraction & Distribution (Claude)**
Parse Westlaw output, match to Notion records, insert text,
flip statuses.

## Running Mode

This skill runs in **Chat** (recommended). It does not need
the matter folder -- it reads from Notion and writes back to
Notion. The only uploaded file is the Westlaw .doc in Phase C.

If the user asks about Cowork vs. Chat, explain:

```
This skill runs entirely in Chat. It reads from the Notion
Research database and writes back to it. The only file you'll
need to upload is the Westlaw .doc after William runs the
Find & Print.

No matter folder access is needed.
```

---

## PHASE A: TRIAGE & CITATION HARVEST

### Step 1: Query the Need Research View

Fetch the "Blog This: Add Research" view from the Research
database using the Notion connector:

```
View ID: view://16c0fc06-a06c-8091-ac93-000c48d0e6e6
```

Use `notion-query-database-view` with this view URL. This
returns all items where:
- Research Tags contains the "Blog or Pod This" tag
- Publish or Pass? = "Need Research"

For each item returned, record:
- **Notion page URL** (the unique identifier for matching)
- **Title** (the item name as shown in the database)
- **URL field** (the source URL, if populated)
- **Research Tags** (for context)
- **Created date** (for recency sorting)
- **Case Pub Date** (if populated)

Present a brief inventory:

```
CONTENT RESEARCH QUEUE
======================
Items in queue: [N]
Date range: [earliest Created] to [latest Created]

  [1] [Title] -- [URL domain or "no URL"]
  [2] [Title] -- [URL domain or "no URL"]
  ...
```

If the queue has more than 25 items, warn the user:

```
The queue has [N] items. Processing all of them will
produce a large Westlaw pull list and take longer in
Phase C. Would you like to:

  a. Process all [N] items
  b. Process only the most recent [suggest N/2]
  c. Let me pick which ones to process
```

Wait for confirmation before proceeding.

If the queue is empty, report it and stop:

```
The Need Research queue is empty -- nothing to process.
```

### Step 2: Triage Each Item

For each item, classify it into one of three categories.
See `references/triage-rules.md` for detailed rules.

**CASE** -- An item that references a specific court decision.
Indicators: party names in "v." format, reporter citations,
court and date references, link to calapp.blogspot.com or
a court website, or a Westlaw/Lexis URL.

**ARTICLE** -- An item about legal news, commentary, policy,
or analysis that is NOT a specific court decision. Indicators:
no "v." in title, link to a news site / LinkedIn / blog,
descriptive title without case-name structure, or references
a topic rather than a specific ruling.

**AMBIGUOUS** -- Cannot confidently classify from title and
URL alone.

Present the triage results:

```
TRIAGE RESULTS
==============

CASES ([N]):
  [1] Combs v. Broomfield (9th Cir. - March 12, 2026)
      URL: calapp.blogspot.com/...
      Citation: [resolved or "needs resolution"]
  ...

ARTICLES ([N]):
  [A1] AI work product is protected?
       URL: linkedin.com/...
  ...

AMBIGUOUS ([N]):
  [?1] [Title]
       URL: [if any]
       Reason: [why it's ambiguous]
  ...
```

For AMBIGUOUS items, ask the user to classify each one:

```
I couldn't confidently classify these items. For each,
please tell me: (C)ase, (A)rticle, or (S)kip.

  [?1] "[Title]" -- C / A / S?
  [?2] "[Title]" -- C / A / S?
```

Wait for the user's response before proceeding.

### Step 3: Resolve Citations for Cases

For each item classified as CASE, attempt to resolve the
full reporter citation:

**If the title already contains a reporter citation**
(e.g., "Baird v. Bonta (9th Cir. 2026) 163 F.4th 723"):
Extract it directly. No further resolution needed.

**If the title contains party names + court + date but no
citation** (e.g., "Combs v. Broomfield (9th Cir. - March
12, 2026)"):
1. First, check the URL field. If it links to a blog post
   or court site, fetch the URL and look for the citation
   in the page content.
2. If no URL or URL fetch fails, do a web search for the
   case name + court + date to find the citation.
3. If still not resolved, mark as "CITATION NOT FOUND" and
   flag for manual lookup.

**If the title is a short case name without court or date**
(e.g., just a case name reference):
1. Search using available context (URL, tags, created date).
2. If not resolved, flag for manual lookup.

After resolution, present the results:

```
CITATION RESOLUTION
===================
Resolved: [N] of [total cases]

  [1] Combs v. Broomfield -- 2026 WL XXXXXX (or
      [Vol] [Reporter] [Page])
  [2] B.B. v. Capistrano USD -- [citation]
  ...

UNRESOLVED ([N]):
  [U1] [Title] -- could not find citation
  [U2] [Title] -- could not find citation

For unresolved cases, you can:
  a. Provide the citations manually (paste them here)
  b. Skip these items for now (they'll stay as Need Research)
  c. Have William look them up before the Westlaw run
```

Wait for user input on unresolved cases.

### Step 4: Process Articles via URL Fetch

For each item classified as ARTICLE that has a URL:

1. Fetch the URL content using `web_fetch`.
2. Extract the relevant text -- the article body, stripping
   navigation, ads, sidebars, and boilerplate.
3. If the URL is a LinkedIn post, extract the post content.
4. If the URL fetch fails, note the failure.

For articles WITHOUT a URL, flag them:

```
These articles have no source URL. They'll need manual
research or will be skipped:
  [A3] "[Title]" -- no URL
```

After processing articles, present results:

```
ARTICLE PROCESSING
==================
Fetched: [N] of [total articles]
Failed: [N] (URL not accessible or no URL)

Ready to update in Notion:
  [A1] "AI work product is protected?" -- 1,200 words extracted
  [A2] "Good, Adam Feldman on clerking" -- 800 words extracted
  ...

Failed:
  [A3] "[Title]" -- [reason: no URL / fetch failed / paywall]
```

### Step 5: Update Notion for Completed Articles

For each successfully fetched article, update the Notion
record immediately (do not wait for the Westlaw phase):

1. **Insert content** into the page body using
   `notion-update-page` with `update_content`. Structure:

```
## Source Content

**Source:** [URL]
**Fetched:** [today's date]
**Word count:** [approximate]

---

[Extracted article text, preserving paragraph structure.
Use Notion markdown.]

---

*Content fetched automatically by the KLG Content Research
Pipeline. Attorney review required before publication.*
```

2. **Update status:** Change "Publish or Pass?" from
   "Need Research" to "Further Review".

Report progress as each article is updated:

```
  [checkmark] Updated: "[Title]" -- status changed to Further Review
```

### Step 6: Generate Westlaw Pull List

Compile the Westlaw Find & Print authority list from all
resolved case citations. Follow the format in
`references/comet-westlaw-prompt.md`:

- Reporter volume, reporter name, and start page ONLY
- One authority per line
- No case names or years
- Deduplicated
- Batches of 100 max

Present the handoff using the standard format from
`references/handoff-standards.md`:

```
=============================================
PHASE A COMPLETE: Triage and citation harvest
=============================================

SUMMARY:
  Total items processed: [N]
  Articles updated in Notion: [N] (already done)
  Cases ready for Westlaw: [N]
  Skipped/unresolved: [N]

WHAT TO DO NEXT:

1. Give the Westlaw authority list below to William.
2. William runs Westlaw Find & Print via Comet.
3. William downloads the .doc file.
4. Come back to this Chat tab and upload the .doc file.
5. Say: "The Westlaw file is ready."

COMET WESTLAW INSTRUCTIONS:
-------------------------------------------
[Insert the full Comet prompt from
 references/comet-westlaw-prompt.md with the
 authority list filled in]
-------------------------------------------

EXPECTED: Westlaw pull for [N] authorities takes
approximately [estimate] minutes.

IF SOMETHING GOES WRONG: If Westlaw cannot find a
citation, skip it. William should note which ones
failed so we can flag them.
=============================================
```

IMPORTANT: The Comet prompt must be in its own standalone
code block. The user will copy-paste it directly to Comet.

### Step 7: Write Citation Map to Working Memory

Before the Westlaw handoff, Claude must preserve the
mapping between citations and Notion page URLs. This is
critical for Phase C matching.

Store the citation map as a clearly formatted reference
that Claude can use when the user returns with the Westlaw
file. Include it at the end of the Phase A output in a
collapsible section:

```
CITATION MAP (for Phase C matching -- do not delete)
====================================================
Citation -> Notion Page URL -> Title
----------------------------------------------------
[Vol] [Reporter] [Page] -> [Notion URL] -> [Title]
[Vol] [Reporter] [Page] -> [Notion URL] -> [Title]
...
====================================================
```

This map is the bridge between Phase A and Phase C.
Without it, Claude cannot match Westlaw output back to
the correct Notion records. If the user starts a NEW
chat session for Phase C, they must paste this map.

---

## PHASE B: WESTLAW FIND & PRINT

No Claude involvement. William runs the Westlaw pull
via Comet using the authority list from Phase A.

---

## PHASE C: EXTRACTION & DISTRIBUTION

### Trigger

The user uploads the Westlaw .doc file and says something
like "the Westlaw file is ready" or "here's the Westlaw
output" or "process the Westlaw file."

### Step 1: Verify Context

Check whether the citation map from Phase A is still in
the conversation context.

**If YES:** Proceed to Step 2.

**If NO** (new chat session): Ask the user to paste the
citation map from the Phase A session:

```
I need the citation map from Phase A to match the Westlaw
cases to the correct Notion records. Please paste the
CITATION MAP section from the Phase A output.
```

Wait for the map before proceeding.

### Step 2: Parse the Westlaw File

Follow the standard Westlaw parsing workflow from
`references/parsing-guide.md`:

1. Check file type: `file [uploaded_file]`
   (expect RTF despite .doc extension)
2. Convert: `pandoc -f rtf -t plain [file] -o extracted.txt`
3. Parse into individual cases using "End of Document"
   boundary markers.
4. For each parsed case, extract:
   - Case name (party names)
   - Full citation
   - Court name
   - Decision year
   - Full opinion text (stripped of Westlaw headnotes
     and proprietary content per parsing guide)

Present the parse results:

```
WESTLAW PARSE RESULTS
=====================
File: [filename]
Cases parsed: [N]

  [1] [Case Name], [Citation] ([Court], [Year])
      Text length: ~[N] words
  [2] [Case Name], [Citation] ([Court], [Year])
      Text length: ~[N] words
  ...
```

### Step 3: Match to Notion Records

Using the citation map from Phase A (or pasted by user),
match each parsed case to its Notion record.

**Match strategy:**
1. Primary: Match on the base citation (volume + reporter
   + start page). This is the most reliable match because
   both the citation map and the Westlaw output use the
   same reporter citation.
2. Fallback: If the citation format differs slightly
   (e.g., parallel citation vs. primary), match on case
   name (party names).
3. If no match: Flag for manual review.

Report matches:

```
MATCHING RESULTS
================
Matched: [N] of [total parsed]
Unmatched: [N]

MATCHED:
  [checkmark] [Case Name] -> "[Notion Title]"
  ...

UNMATCHED (need manual assignment):
  [?] [Case Name], [Citation] -- no matching Notion record
  ...
```

For unmatched cases, ask the user whether to skip them or
manually assign them to Notion records.

### Step 4: Update Notion Records

For each matched case, update the Notion record:

1. **Insert content** into the page body:

```
## Case Text

**Citation:** [Full citation with parallel cites]
**Court:** [Court name]
**Decision date:** [Date]
**Fetched via:** Westlaw Find & Print ([today's date])

---

[Full opinion text, preserving paragraph structure.
Strip Westlaw headnotes, key numbers, and proprietary
editorial content. Include only the court's opinion,
syllabus if present, and any concurrences/dissents.
Use Notion markdown.]

---

*Case text extracted automatically by the KLG Content
Research Pipeline. Attorney review required before
publication.*
```

2. **Update status:** Change "Publish or Pass?" from
   "Need Research" to "Further Review".

3. **Update Note property:** Add a brief note:
   "[Court], [Year]. Full text loaded [today's date]."

Process records one at a time and report progress:

```
NOTION UPDATES
==============
  [checkmark] [1/N] "[Title]" -- updated, status: Further Review
  [checkmark] [2/N] "[Title]" -- updated, status: Further Review
  ...
```

### Idempotency Check

Before updating any record, fetch it first and check:
- If the page body already contains a "## Case Text" or
  "## Source Content" section, the record was already
  processed. SKIP it and report:

```
  [skip] "[Title]" -- already processed (has content)
```

This prevents duplicate processing if Phase C is re-run.

### Step 5: Final Report

```
=============================================
CONTENT RESEARCH PIPELINE COMPLETE
=============================================

SUMMARY:
  Total items in queue: [N]
  Articles processed (Phase A): [N]
  Cases processed (Phase C): [N]
  Skipped (already had content): [N]
  Failed/unresolved: [N]

  Items moved to Further Review: [N]
  Items still at Need Research: [N] (unresolved)

REMAINING ITEMS (if any):
  [list any items that could not be processed
   with reason: no citation, URL fetch failed, etc.]

The processed items are now in the "Blog This: Review"
view in the Research database, ready for Tim's review.
=============================================
```

---

## CONTENT LENGTH CONSIDERATIONS

Full appellate opinions can be very long (10,000-50,000+
words). Notion pages can handle large content, but very
long opinions may make the page slow to load.

**Strategy:**
- For opinions under 10,000 words: insert full text.
- For opinions over 10,000 words: insert full text but
  wrap the opinion body in a toggle block:

```
<details>
<summary>Full Opinion ([N] words)</summary>

[opinion text]

</details>
```

- Always include the citation, court, and date outside
  the toggle so they're immediately visible.

---

## EDGE CASES

### Items with both case and article characteristics

Some items reference a case but link to a blog post
analyzing it (e.g., calapp.blogspot.com posts). These
should be classified as CASES because the primary value
is the court opinion, not the blog commentary. The blog
URL is useful for citation resolution but the blog text
itself is not what gets inserted into Notion.

### Very recent cases without reporter citations

Cases decided in the last few weeks may only have slip
opinion citations or Westlaw-only citations (e.g.,
"2026 WL XXXXXX"). These are valid for Westlaw Find &
Print. Use the WL citation if no reporter citation is
available yet.

### Items that reference multiple cases

Some titles reference multiple cases (e.g., comparing
two rulings). Classify as CASE and attempt to resolve
the primary case citation. Note the secondary case in
the triage report. Only the primary case goes through
Westlaw.

### Westlaw pull returns nothing for a citation

If Westlaw could not find certain citations, William
should report which ones failed. In Phase C, those
items remain at "Need Research" and are listed in the
final report.

### Notion API rate limits

When updating many records in Phase C (or Phase A for
articles), the Notion API may rate-limit. If a request
fails, wait 2 seconds and retry once. If it fails again,
log the failure and continue with the next record.
Report all failures at the end.

---

## EXECUTION RULES

1. Always query the Notion view fresh at the start of
   Phase A. Do not rely on cached or remembered data.
2. Never skip the triage step. Every item must be
   classified before processing.
3. Articles with successful URL fetches are updated in
   Notion during Phase A -- do not defer them to Phase C.
4. The Comet Westlaw prompt must be in a standalone code
   block for copy-paste.
5. The citation map is the critical bridge between Phase A
   and Phase C. Always present it and warn the user to
   preserve it.
6. Idempotency: always check before writing. Never insert
   duplicate content into a Notion record.
7. Strip Westlaw proprietary content (headnotes, key
   numbers, editorial summaries) from case text. Include
   only the court's own words.
8. Status updates: "Need Research" -> "Further Review".
   Never set any other status.
9. If a batch has more than 100 Westlaw citations, split
   into batches of 100 per the Comet prompt standards.
10. Pull the user through every step with crystal-clear
    handoff instructions per `references/handoff-standards.md`.
11. After every substantive response in this pipeline,
    append the session log prompt per `claude.md` global
    behavior -- but note this is a content production
    session, not tied to a specific case matter.
12. For very large queues (25+ items), recommend the user
    consider processing in batches across multiple sessions
    rather than one massive run.
13. When fetching article URLs, respect paywalls. If a
    site returns a paywall or login page, report the
    failure and do not attempt to bypass it.
14. This skill reads from and writes to the same Notion
    database records. There is no separate output file.
    All work product lives in Notion.
