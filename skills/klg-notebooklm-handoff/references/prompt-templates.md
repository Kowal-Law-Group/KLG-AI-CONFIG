# NotebookLM Prompt Templates

These are the canonical prompt templates the skill assembles into
the prompt queue. Each prompt is followed by the appropriate
PASTE TARGET heading. Adapt the bracketed values to the specific
matter.

## Universal Prompts (always include)

### PROMPT 1 — Setup and context

**PASTE TARGET:** `## OUTPUT — Setup confirmation`

**TEMPLATE:**

```
You are providing analytical support for [POSTURE DESCRIPTION —
e.g., "an opposition to a motion for summary judgment, and a
cross-motion for summary adjudication, in [Matter Name] ([Court]
Case No. [Case No.]). The hearing is set for [date] before
[Judge], [Department]."]

[PARTIES PARAGRAPH — brief description of plaintiff(s) and
defendant(s), including individual defendants and their roles.]

[OPERATIVE THEORY PARAGRAPH — the case theory in 3–5 sentences,
including the key chronology and the harm.]

[LAW OF THE CASE PARAGRAPH — if applicable. Identify any prior
appellate opinion that established law of the case, with case
number and date. List the holdings that bind the trial court on
remand.]

[OPPOSITION'S ARGUMENTS PARAGRAPH — if applicable. Brief inventory
of what defendants/respondents/appellees raise.]

[CROSS-MOTION OR AFFIRMATIVE RELIEF PARAGRAPH — if applicable.]

Throughout this analysis: [TERMINOLOGY RULES — e.g., "refer to the
National Practitioner Data Bank as 'the Data Bank' (not 'NPDB')."
Always include: "Refer to the lower court as 'trial court' or
'Superior Court,' never 'lower court.' When citing California
cases, use the California Style Manual format (Party v. Party
(Year) Volume Cal.App.5th Page)."]

Confirm you have read and understood this context, and briefly
restate the operative theory in your own words. Then proceed when
I give you the next prompt.
```

### PROMPT 2 — Source ingestion confirmation

**PASTE TARGET:** `## OUTPUT — Source inventory`

**TEMPLATE (use as-is, no per-matter adaptation needed):**

```
List every source document you have access to in this notebook.
For each, provide:

(a) The document title or filename as you see it.
(b) The document type — deposition transcript, hearing transcript,
    exhibit, brief, court opinion, research memorandum, separate
    statement, declaration, etc.
(c) The date or date range it covers, if discernible.
(d) The approximate length (pages or words).
(e) Whether you can read the full text, or whether any portion
    appears unreadable, scanned-without-OCR, or otherwise
    inaccessible.

After the list, identify any source category that you would expect
to see in [POSTURE-SPECIFIC RECORD — e.g., "an MSJ opposition
record" or "an appellate opening brief record"] but cannot find in
this notebook. For example: a deposition volume, a hearing session,
the operative complaint, a key exhibit, a brief, the Court of
Appeal opinion. Flag each missing item explicitly so the user can
upload it before we proceed.
```

### Per-source digest prompts (one per source category present)

**PASTE TARGET pattern:** `## DIGEST — [Source Category Name]`

**STRUCTURED DIGEST TEMPLATE:**

```
Provide a structured digest of [SOURCE CATEGORY]. Organize as:

(1) Overview — what the document is, when it issued, what role
    it plays in the case.

(2) Key facts established — the most important factual propositions
    this source establishes, with internal citations to the source
    (page, line, paragraph as applicable).

(3) Key admissions or concessions — anything the source contains
    that is adverse to the side that produced it (defendants'
    admissions in their own brief; plaintiff's admissions in his
    deposition; etc.). Quote each admission and provide the
    citation.

(4) Notable silences — what one would expect this source to address
    that it does not.

(5) Evidentiary value mapped to causes of action and defenses —
    for each of the following issues, list the strongest specific
    propositions in this source supporting plaintiff's position:
    [LIST OF CAUSES OF ACTION AND AFFIRMATIVE DEFENSES specific
    to the matter]

(6) Cross-references — passages in this source that contradict
    or corroborate other sources in the notebook.

[OPTIONAL — for transcripts and depositions, add:]
(7) `[VERIFY: ...]` resolution — for each `[VERIFY: ...]` flag in the
    working draft that points to this source generically, identify
    the specific page and line that supports the cited proposition.

[OPTIONAL — for the Court of Appeal opinion, add:]
(7) Page citations to anchor `[VERIFY: ...]` flag resolution — for each
    of the following propositions in the working draft, identify
    the actual page in the opinion that supports it: [LIST OF
    `[VERIFY: ...]`-FLAGGED PROPOSITIONS]

Use specific citations throughout (page:line for transcripts,
volume.page for depositions, page or paragraph for opinions and
briefs).
```

### Per-source digest variants

Source categories typically present in KLG matters and their
canonical headings:

| Source category | Heading |
|---|---|
| Court of Appeal opinion (single) | `## DIGEST — Court of Appeal opinion ([B-number])` |
| Defendants' MSJ moving papers | `## DIGEST — Defendants' MSJ moving papers` |
| Opposing brief (appellate) | `## DIGEST — [Opposing party]'s brief` |
| Hearing transcripts | `## DIGEST — Hearing transcripts` |
| Deposition transcripts | `## DIGEST — [Deponent] deposition transcripts` |
| Key exhibits | `## DIGEST — Key exhibits` |
| Research memos | `## DIGEST — Research memos` |
| Working draft | `## DIGEST — Working draft ([Brief type])` |
| Operative pleading | `## DIGEST — Operative pleading` |

For each source category that exists in the matter, emit one
digest prompt using the structured digest template above. Skip
categories that are not in the source corpus.

### PROMPT — Evidence inventory by cause of action / issue

**PASTE TARGET:** `## EVIDENCE INVENTORY by [cause of action OR
issue on appeal]`

**TEMPLATE:**

```
For each [cause of action / issue on appeal] and [cross-MSJ /
prayer for relief — if applicable], produce a master inventory
of every piece of evidence in the source corpus that supports
each element. Organize as a structured list.

Cover these claims and elements:

[ENUMERATE EACH CAUSE OF ACTION AND ITS ELEMENTS, OR EACH ISSUE
ON APPEAL AND ITS REQUIRED SHOWINGS. Adapt to matter.]

[ENUMERATE EACH AFFIRMATIVE DEFENSE TO REBUT, IF APPLICABLE]

For each element, provide:
- Element name
- Supporting evidence (specific source, page/line)
- Strength rating (strong / moderate / weak)
- Currently cited in the working draft (yes / no / partially)

After the inventory, summarize: (i) the elements with the weakest
evidentiary support; (ii) the elements with strong evidence not
currently cited in the working draft; (iii) [POSTURE-SPECIFIC
DECLARATIONS GAP CLOSURE — e.g., "the elements where the planned
declarations will need to fill the gap"]
```

### PROMPT — Gap analysis (fact-citation completeness)

**PASTE TARGET:** `## GAP ANALYSIS — Fact-citation completeness`

**TEMPLATE:**

```
Read the working draft. Identify every factual assertion that
is currently supported only by a generic citation — for example,
"[GENERIC CITATION EXAMPLES SPECIFIC TO MATTER]" — without a
specific page or page/line citation. For each:

(a) Quote the assertion as it appears in the brief, with the
    section number.
(b) Identify the specific page or page/line in the source documents
    that provides the strongest support.
(c) Provide the exact quote from the source.
(d) Recommend the precise citation format.

Also resolve every `[VERIFY: ...]` flag in the working draft. For each,
quote the proposition the brief asserts and identify the specific
page in [WHATEVER OPINION OR DOCUMENT THE FLAGS POINT TO] that
supports it.

Finally, identify any factual assertion in the working draft that
you cannot find direct support for in the uploaded source documents.
Flag each as a potential overstatement and recommend either (i)
finding the support, (ii) softening the assertion, or (iii)
removing it.
```

### PROMPT — Authority deployment audit

**PASTE TARGET:** `## AUTHORITY DEPLOYMENT audit`

**TEMPLATE (adapt only the research-memo count):**

```
Compare the cases cited in the working draft against the cases
discussed in the [N] research memos. Produce four lists:

(1) Cases discussed in research memos but NOT cited in the working
    draft. For each, briefly explain the case's holding, the
    proposition it would support in the brief, and which section
    it would best fit into.

(2) Cases cited in the working draft where a stronger or more
    recent authority exists in the research memos. Recommend
    specific substitutions.

(3) Adverse or contrary authority in the research memos that the
    working draft does not address or distinguish. For each,
    recommend whether to (i) distinguish in a footnote,
    (ii) distinguish in the main text, or (iii) ignore as not
    directly on point.

(4) Cases cited in the working draft that are weaker than the
    research memos suggest — for example, cases the memos
    identified as marginal but the brief now relies on heavily.

Throughout, flag any out-of-state federal authority cited in the
brief that has a California analog identified in the research
memos. California analogs should be preferred for state-court
briefing.
```

## Conditional Prompts

### PROMPT — Defense preemption audit (if opposing brief is in corpus)

**PASTE TARGET:** `## DEFENSE PREEMPTION audit`

**TEMPLATE:**

```
Read [opposing party]'s [moving papers / opposition brief / reply
brief]. For every legal argument, affirmative defense, and
[undisputed material fact / record characterization] [opposing
party] asserts:

(1) State the argument or assertion concisely.
(2) Identify the section of the working draft that responds (or
    note "unaddressed").
(3) Assess whether the response is complete, partial, or absent.
(4) [FOR MSJ POSTURE: For UMFs, identify the corresponding
    response in plaintiff's separate statement and assess the
    strength of the counter-evidence (strong / moderate / weak).]
(5) [LAW-OF-THE-CASE FORECLOSURE — if applicable: Identify any
    place where [opposing party]'s argument is foreclosed by
    [prior opinion] as law of the case but the working draft
    does not flag the foreclosure.]

Then produce a top-line list of:
- The five most dangerous arguments — those with the strongest
  evidentiary support and the weakest current response.
- Any argument the working draft entirely fails to address.
- Any [UMF / record characterization] whose response could be
  strengthened with evidence already in the source corpus.
```

### PROMPT — Brief economy recommendations (if working draft is in corpus)

**PASTE TARGET:** `## BRIEF ECONOMY recommendations`

**TEMPLATE:**

```
The Phase 2 plan calls for these cuts to the working draft:

[LIST OF SECTIONS WITH PERCENTAGE CUTS OR RESTRUCTURE INSTRUCTIONS]

For each section above, identify:

(1) The lowest-value paragraphs (quote the first sentence of each
    candidate). These are paragraphs that are repetitive,
    defensive, developed elsewhere in the brief, or that hedge
    in ways the case posture does not require.

(2) Specific consolidations — places where two or three paragraphs
    make essentially the same point and could be combined.

(3) String cites of three or more cases where one or two would
    carry the same weight. For each, identify the strongest case
    in the string and the cases that should be cut.

(4) Defensive hedging language that should be excised — phrases
    like "to be clear," "respectfully," "even assuming," and
    similar that signal weakness without adding substance.

[FOR SECTIONS REQUIRING RESTRUCTURE: Propose a revised section
opening (one paragraph) that establishes the new lead-with framing.]
```

### PROMPT — Cross-MSJ stress test (if cross-motion is being filed)

**PASTE TARGET:** `## CROSS-MSJ stress test`

**TEMPLATE:**

```
[Section number and topic of the cross-MSJ] seeks summary
adjudication on [claim]. List every fact the cross-MSJ relies on.
For each:

(a) Identify the proposition.
(b) Identify the specific source evidence supporting it.
(c) State whether the proposition is genuinely undisputed (admitted
    in defendants' separate statement, established by document and
    not contradicted in any source, or both).
(d) Flag any fact that is genuinely disputed — meaning a reasonable
    juror could find against plaintiff — that would defeat
    summary adjudication on this element.

Then identify the strongest argument [opposing party] will make in
opposition to the cross-MSJ. Identify where the cross-MSJ section
preempts that argument and whether the preemption is adequate.
```

### PROMPT — Theory convergence and divergence (research synthesis posture only)

**PASTE TARGET:** `## THEORY CONVERGENCE AND DIVERGENCE`

**TEMPLATE:**

```
Across all research memos in the corpus:

(1) Convergence — identify every legal proposition or strategic
    recommendation supported by two or more memos. Quote the
    converging language from each memo and identify the proposition
    the convergence supports.

(2) Divergence — identify every legal proposition or strategic
    recommendation where the memos disagree. Quote the conflicting
    language and identify the strongest argument on each side.

(3) Gaps — identify every legal issue raised in [opposing
    party]'s [brief or anticipated arguments] that none of the
    research memos directly addresses.

(4) Synthesis recommendation — for each divergence, recommend
    which side has the stronger position in the context of this
    matter, and why.
```

### PROMPT — Impact on prior analysis (case assessment supplement posture only)

**PASTE TARGET:** `## IMPACT ON PRIOR ANALYSIS`

**TEMPLATE:**

```
The original case assessment for this matter is in the source
corpus. New documents have been added: [LIST OF NEW DOCUMENT
CATEGORIES].

For each conclusion in the original assessment:

(a) State the original conclusion.
(b) Identify which of the new documents bear on the conclusion.
(c) State whether the new documents strengthen, weaken, or change
    the conclusion. If they change it, propose the revised
    conclusion.
(d) Identify any factual finding in the original assessment that
    the new documents contradict.

Then identify any new legal theory or factual avenue the new
documents open that the original assessment did not explore.
```

## Audio Overview Prompts (Manual Section)

These are NOT for Comet — they go in a separate "Manual review
prompts" section at the bottom of the page. Tim runs them himself
when he wants to listen on a drive or walk.

```
1. "Walk me through every weakness in [the opposition / this
   brief] that opposing counsel will exploit on reply."
2. "What is the single strongest piece of evidence on each
   [cause of action / issue on appeal], and is it cited
   prominently in the working draft?"
3. "If I had to cut 30% of this brief tonight without weakening
   any argument, what would go?"
4. "What is the most damaging fact in [opposing party]'s
   [moving papers / brief] that [the opposition / our brief]
   does not adequately address?"
5. [POSTURE-SPECIFIC: For oral argument prep — "What three
   questions will the panel most likely ask, and what is the
   ideal one-sentence answer to each?"]
```
