---
name: klg-style-guide-check
description: "Check legal briefs and filings for conformity with the KLG Style Guide, producing a redlined Word document with tracked changes and comments plus a written conformance report. Use this skill whenever the user says 'style check', 'style guide check', 'check this brief', 'proofread this brief', 'edit this brief', 'tighten this brief', 'review this brief for style', 'KLG style check', 'redline this', 'check formatting', 'check citations', or uploads a .docx brief and asks for review, editing, proofreading, or style conformance. Also triggers when the user references checking a document against the KLG Style Guide or wants tracked-change edits to a brief. Produces a redlined .docx with Word tracked changes and comments, plus a conformance report. Do NOT use for case assessments, research memos, or response plans — those have their own skills."
---

# KLG Style Guide Check

## Purpose

Review legal briefs and filings against KLG writing standards and
produce a redlined Word document with tracked changes the attorney
can accept or reject in Word, plus a written conformance report.

This skill edits the actual .docx file using Word tracked changes
(w:ins / w:del) and Word comments, so the attorney gets the same
experience as receiving edits from a human editor.

## Required Context

Before analyzing any document, read these files:

1. `/mnt/project/klg-style-guide.md` — The authoritative style
   guide. This controls if any conflict arises.
2. `/mnt/project/claude.md` — Citation standards, output
   requirements, quality controls, and the style checks section.
3. `/mnt/skills/public/docx/SKILL.md` — For the tracked-changes
   XML editing workflow (unpack → edit → pack).
4. `references/workflow-patterns.md` — Workflow patterns
   (Patterns 1, 2, and session logging reference)

Do not skip reading these files. The style guide and claude.md
are the single sources of truth. This skill does not maintain
its own copy of style rules.

If the brief targets a specific court (e.g., Ninth Circuit vs.
California Court of Appeal), note this — it affects font size
requirements and citation format.

## Required Inputs

- A .docx file (the brief or filing to review)
- Optional: target court, word/page limits, filing type

## Step 1: Scope Selection

At the start of every review, ask the user to choose the scope:

```
What scope of review do you want?

1. **Full edit** — Style conformance + mechanics + flow,
   clarity, brevity, and punch. (Most thorough.)

2. **Style conformance only** — Enforce KLG Style Guide rules:
   terminology, headings, citations, formatting, prohibited
   words/phrases. No substantive rewriting.

3. **Mechanics only** — Typos, grammar, punctuation, citation
   formatting. No style or flow edits.

4. **Custom** — Tell me what to focus on.
```

Wait for the user's selection before proceeding.

## Step 2: Read and Analyze

Read the entire document before making any edits:

1. Read the project style files:
   ```
   /mnt/project/klg-style-guide.md
   /mnt/project/claude.md
   ```

2. Read the docx skill for XML editing mechanics:
   ```
   /mnt/skills/public/docx/SKILL.md
   ```

3. Extract text from the uploaded brief using pandoc:
   ```bash
   pandoc document.docx -o document.md
   ```

4. Read the extracted text completely.

5. Analyze against the rules from the style guide and claude.md
   (based on scope selected). Build an internal edit plan
   organized by the enforcement categories below before touching
   any XML.

## Enforcement Categories

These categories define what to check. The specific rules for
each come from the style guide and claude.md — those files are
the authority. This section tells you how to organize and
prioritize the review.

### Category A: Terminology violations
Find-and-fix using tracked changes. The style guide and
claude.md contain explicit "instead of X, use Y" rules. Key
targets include: "lower court," "instant case," "furthermore,"
"therefore," "as such," "hereinabove," "aforementioned," "i.e.,"
"However" as a sentence opener, "Moreover," "argued" attributed
to a court, and "WHEREFORE" or other fusty prayer language
("Comes now," "respectfully prays," "for good cause shown").
Also check: lowercase "superior court" — should be either
"Superior Court" (capitalized, formal name of the court) or
"trial court" (lowercase, generic descriptor). Never lowercase
"superior court."
Also check: **party designations** — refer to our client by
their appellate party designation (e.g., "respondent,"
"appellant"), not trial-court designations like "plaintiff" or
"defendant," unless quoting from a trial court document. Flag
every instance where a party is referred to by a trial-court
designation outside of a direct quotation.

### Category B: Citation format errors
Check against the citation standards in claude.md. Key targets:
naked cites (missing explanatory parentheticals), missing
pincites, superscript in reporters, wrong short-form format
(missing p./pp.), wrong California Style Manual or Bluebook
format, hyperlinks in brief text. Also check: Rules of Court
short form — after the first full citation, the correct short
form is lowercase "rule" with no "Cal." prefix (e.g.,
"rule 8.108(e)(2)," not "Cal. Rules of Court, rule 8.108(e)(2)"
or "Rules of Ct., rule 8.108(e)(2)"). The first citation should
use the full form; all subsequent citations use the bare
lowercase "rule" short form.

### Category C: Heading issues
Check against the heading rules in the style guide, which draw two
different conventions depending on the kind of heading:
- **Standard brief section labels** (Introduction, Conclusion,
  Statement of the Case, Statement of Facts, Issue(s) Presented,
  Petition for Review, Standard of Review, and the like) are labels,
  not sentences. Correct form: Title Case, no concluding punctuation.
  Flag ALL CAPS. Do not flag these for missing terminal punctuation
  or for reading as a label rather than a persuasive sentence — that
  is the correct form for this category.
- **Argument point headings** are complete persuasive sentences.
  Correct form: sentence case, concluding punctuation, active verbs.
  Flag ALL CAPS, missing terminal punctuation, missing active verbs,
  and any heading that reads as a bare topic label instead of a
  persuasive sentence.
Also check: SOC subheadings (P3-level or italic narrative) must be
complete sentences, not fragments — a reader scanning headings alone
should understand the story. Also check headings orphaned at page
bottoms.

### Category D: Prohibited words and legalese
The style guide and claude.md list specific banned words and
phrases. Scan the full document for any occurrence. Also scan for
nominalization and gerund constructions where an active verb is
available — watch for the patterns "in its [noun] of," "upon
[noun] of," and possessive + nominalization + "of" (e.g., "the
court's adoption of," "plaintiffs' opposition to"). Flag each with
the active-verb rewrite (e.g., "the court adopted," "plaintiffs
opposed").

### Category E: Mechanics
Typos, grammar, punctuation, em dash spacing (no spaces), double
spaces after periods, date format (full dates, no ordinal
suffixes), straight quotes that should be curly, possessive
formation.

### Category F: Flow and clarity (full edit scope only)
Weak transitions, throat-clearing, passive voice, long paragraphs,
buried points, sentences that start with case names instead of
explaining why the case matters first.

### Category G: Block quote violations
The style guide has a strong presumption against block quotes
with only three exceptions. Flag any block quote that discusses
a case. Also check formatting: block quotes should use the
Quote style (or BodyText with left/right indentation) and must
NOT be wrapped in quotation marks — the indentation itself
signals a direct quotation. The citation paragraph immediately
after a block quote should use BodyTextContinued style (no
first-line indent), not BodyText.

### Category H: Emphasis violations
Boldface in brief text, multiple emphasis styles on the same
text (e.g., bold + italics). The rule: use italics for textual
emphasis. Bold is acceptable only for dates. Flag every instance
of bold used for textual emphasis (not dates) and propose
replacing with italics. Also check: extended quotations from
rules or statutes must use block-quote formatting (Quote style
or BodyText with left/right indentation), not inline quotation
with quotation marks around the text.

## Step 3: Edit the Document (Tracked Changes + Comments)

Use the docx skill's editing workflow:

### 3a. Unpack
```bash
python /mnt/skills/public/docx/scripts/office/unpack.py document.docx unpacked/
```

### 3b. Edit XML with tracked changes

Use the str_replace tool to edit `unpacked/word/document.xml`.
Follow these rules strictly:

**Tracked change mechanics:**
- Use `w:del` with `w:delText` for deletions
- Use `w:ins` with `w:t` for insertions
- Author: "Claude" for all changes
- Date: use today's date in ISO format
- Assign unique sequential w:id values across all changes
- Preserve the original run's `<w:rPr>` formatting in tracked
  change runs
- Replace entire `<w:r>` elements — never inject tracked change
  tags inside a run

**What to change via tracked changes:**
- Terminology fixes (Categories A, D)
- Mechanical fixes (Category E)
- Citation format corrections (Category B)
- Heading capitalization fixes (Category C — formatting only)
- Simple clarity improvements where the fix is clear and
  unambiguous

**What to handle via comments only (not tracked changes):**
- Subjective flow/rewriting suggestions (Category F)
- Block quote concerns (Category G — comment suggesting removal
  or shortening)
- Structural suggestions (paragraph splitting, reordering)
- Alternative transitions (comment with 2–3 options)
- Aggressive tightening options (comment with the tighter version)
- Headings that need substantive revision (comment with the
  suggested persuasive sentence — do not rewrite the heading)
- Potential citation issues that need verification
- Legal substance concerns (never change; comment only)

**Comment mechanics:**
Use the comment.py script:
```bash
python /mnt/skills/public/docx/scripts/comment.py unpacked/ [id] "Comment text"
```
Then add comment range markers in document.xml around the
relevant text. See the docx skill for exact XML patterns.

**One tracked change per issue rule:**
When there are multiple valid ways to fix something, make one
tracked change (the safest/most conservative fix) and add a
Word comment explaining the alternative(s).

**Smart quotes:**
Use XML entities for all new text:
- `&#x2018;` left single quote
- `&#x2019;` right single / apostrophe
- `&#x201C;` left double quote
- `&#x201D;` right double quote

### 3c. Repack
```bash
python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ output.docx --original document.docx
```

### 3d. Validate
```bash
python /mnt/skills/public/docx/scripts/office/validate.py output.docx
```

### 3e. Fix standalone declarations (prevents Word "unreadable content" error)
```bash
python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py output.docx
```

If validation fails, inspect the error, fix the XML, and repack.

## Step 4: Produce the Conformance Report

After the redlined document is complete, produce a separate
conformance report as a markdown file. Structure:

```
# KLG Style Guide Conformance Report

**Document:** [filename]
**Date:** [date]
**Scope:** [Full edit / Style only / Mechanics only / Custom]
**Status:** AI-assisted review — requires attorney review

---

## Top Findings

3–7 bullets summarizing the most significant patterns. Focus on
systemic issues, not individual typos. Example:
- Headings throughout use ALL CAPS instead of sentence case
  with Small Caps formatting — 14 instances corrected.
- Multiple naked cites in the argument section — 8 explanatory
  parentheticals added.

## Style Conformance Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Terminology: "trial court" not "lower court" | ✅ / ⚠️ | [details] |
| Party designations: appellate not trial-court | ✅ / ⚠️ | [details] |
| Court names: "Superior Court" or "trial court" | ✅ / ⚠️ | [details] |
| No fusty prayer language (WHEREFORE, etc.) | ✅ / ⚠️ | [details] |
| Rules of Court: bare "rule" short form (no Cal. prefix) | ✅ / ⚠️ | [details] |
| Headings: section labels Title Case/no punctuation, argument headings sentence case/punctuated | ✅ / ⚠️ | [details] |
| Language: active verbs over nominalizations/gerunds | ✅ / ⚠️ | [details] |
| SOC subheadings: complete sentences | ✅ / ⚠️ | [details] |
| No ALL CAPS | ✅ / ⚠️ | [details] |
| Citations: no naked cites | ✅ / ⚠️ | [details] |
| Citations: pincites present | ✅ / ⚠️ | [details] |
| Citations: Cal Style Manual / Bluebook format | ✅ / ⚠️ | [details] |
| No superscript in reporters | ✅ / ⚠️ | [details] |
| Short form cites use p./pp. | ✅ / ⚠️ | [details] |
| Em dashes without spaces | ✅ / ⚠️ | [details] |
| Single space after periods | ✅ / ⚠️ | [details] |
| No prohibited words/phrases | ✅ / ⚠️ | [details] |
| No legalese | ✅ / ⚠️ | [details] |
| No boldface in brief text (except dates) | ✅ / ⚠️ | [details] |
| Emphasis: italics only, sparingly | ✅ / ⚠️ | [details] |
| Rule/statute quotes: block-quote format | ✅ / ⚠️ | [details] |
| Block quotes: justified exceptions only | ✅ / ⚠️ | [details] |
| Block quotes: no quotation marks, Quote style | ✅ / ⚠️ | [details] |
| Block quote cites: BodyTextContinued style | ✅ / ⚠️ | [details] |
| Dates: full dates with year | ✅ / ⚠️ | [details] |
| Names: last names preferred | ✅ / ⚠️ | [details] |
| No unnecessary acronyms | ✅ / ⚠️ | [details] |
| Possessives: as pronounced | ✅ / ⚠️ | [details] |
| Footnotes: sparingly | ✅ / ⚠️ | [details] |
| Record cites: REF format or doc+page | ✅ / ⚠️ | [details] |

## Summary of Tracked Changes

| Category | Count | Examples |
|----------|-------|---------|
| Terminology fixes | [n] | [brief examples] |
| Citation corrections | [n] | [brief examples] |
| Heading fixes | [n] | [brief examples] |
| Prohibited word replacements | [n] | [brief examples] |
| Mechanical fixes | [n] | [brief examples] |
| Clarity improvements | [n] | [brief examples] |

## Comments Requiring Attorney Decision

List each comment that presents alternatives or flags a
subjective issue:

1. **[Location]:** [summary of the comment and options]
2. **[Location]:** [summary]
...

## Items Flagged for Verification

Any citations, facts, or references that could not be verified:

- [citation or reference] — [reason flagged]
```

## Step 5: Deliver

1. Copy the redlined .docx to `/mnt/user-data/outputs/`
   with filename: `[original-name]-REDLINED.docx`
2. Copy the conformance report to `/mnt/user-data/outputs/`
   with filename: `[original-name]-Conformance-Report.md`
3. Present both files to the user.
4. Provide a brief summary: number of tracked changes, number
   of comments, and the 2–3 most significant findings.

## Execution Rules

1. Read the ENTIRE document before making any edits. Build
   the complete edit plan first.
2. Never change legal assertions, citations to the record,
   or requested relief. Flag concerns via comments only.
3. Never invent or modify case citations. If a citation looks
   wrong, add a comment flagging it for verification. Never
   fabricate record volume or page numbers — if a cite cannot
   be verified against a source document, flag it as needing
   verification rather than guessing.
4. Preserve defined terms exactly as established in the document
   unless the style guide requires a change.
5. When in doubt between changing and commenting, comment.
   The attorney can always make the change; undoing an unwanted
   change is harder.
6. Keep tracked changes minimal and precise. Change only what
   needs changing — do not rewrite surrounding text.
7. For large documents, work section by section to avoid
   XML corruption. Validate after each major batch of edits.
8. If the document has existing tracked changes, preserve them.
   Add new changes with author "Claude" so they are visually
   distinct.
9. This is internal work product. Include the AI transparency
   notice that this is an AI-assisted review requiring attorney
   review.
10. After delivering the redlined document and conformance
    report, do NOT proceed to workflow patterns 1 or 2 (iterative
    case memo or client-facing version). This skill produces
    an edited version of the input document, not a new
    deliverable.

## Guardrails

- Never change the substance of a legal argument.
- Never delete or modify record citations (REF numbers,
  appendix cites, RT cites) — comment if something looks wrong.
- Never remove or rewrite a heading's legal content — only fix
  formatting (case, punctuation, caps).
- If word or page limits are provided, track word count and
  suggest prioritized cuts if the document is over limit.
- Be explicit in comments about which edits are objective
  (rule violations) vs. subjective (style preferences).

## Handling Edge Cases

**Very long documents (50+ pages):**
Process in chunks. Unpack once, edit section by section, validate
periodically, pack once at the end. Tell the user this will take
longer and provide progress updates.

**Documents with existing tracked changes:**
Preserve all existing changes. Add new tracked changes with
author "Claude" and today's date. Note in the conformance report
that pre-existing tracked changes were preserved.

**Non-brief documents (letters, memos, motions):**
The style guide applies to all KLG documents, but some rules are
brief-specific (e.g., funnel approach, reply brief format). Skip
brief-specific rules for non-brief documents and note this in
the conformance report.

**Documents with no issues:**
If the document is fully compliant, say so clearly. Produce a
conformance report with all ✅ marks. Do not invent issues.
