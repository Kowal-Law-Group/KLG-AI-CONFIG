---
name: klg-cite-check
description: "Two-phase citation audit and authority verification for appellate briefs. Phase A: format, completeness, placeholders, pincites, and hallucination triage producing a Westlaw pull list. Phase B: cross-check citations against Westlaw source text to verify existence, holding accuracy, and good-law status. Triggers: 'cite check', 'verify citations', 'verify authorities', 'check for hallucinations', 'are the cites real', 'authority verification', 'cross-check the cites', 'Westlaw verification', 'find missing cites', 'check for placeholders'. Run after brief elevation and before style-guide-check. NOT for substantive review (use klg-brief-elevation) or style conformance (use klg-style-guide-check)."
---

# KLG Citation Audit & Authority Verification

## Purpose

This skill systematically audits every citation in an appellate
brief in two phases:

**Phase A — Citation Audit & Hallucination Triage:** Checks
format, completeness, placeholders, pincites, and short-form
consistency. Then triages every case citation for hallucination
risk — flagging citations Claude cannot confidently confirm as
real and producing a Westlaw Find & Print list. This phase
catches format problems and identifies which authorities need
external verification.

**Phase B — Authority Verification:** After Westlaw materials
are uploaded, cross-checks each case citation against the actual
authority text. Verifies the case exists, the holding matches the
proposition for which it is cited, and the authority is still
good law. Produces a verification report with traffic-light
ratings.

The value: every hallucinated citation that makes it into a filed
brief is a career-ending credibility risk. Every mischaracterized
holding is an invitation for opposing counsel to destroy your
argument in a footnote. This skill catches those problems before
the attorney's final review.

## When to Run

This skill fits into the KLG pipeline after brief elevation and
before (or concurrent with) the style-guide-check:

```
Case Assessment → Research → Brief Elevation → CITE CHECK → Style Check → File
```

Phase A can run immediately after elevation. Phase B runs after
Comet delivers the Westlaw materials. The two phases can run in
the same session (if Westlaw is fast) or across sessions.

## Required Inputs

**Phase A:**
- A brief (.docx or .md) to audit
- Helpful but not required: the appellate record or key record
  documents (to verify record citations)

**Phase B (in addition to Phase A outputs):**
- Westlaw Find & Print output (.doc or .docx) for the
  authorities flagged in Phase A
- KeyCite status for each authority (good law / yellow flag /
  red flag / overruled)

## Required Context

Before auditing, read:
1. `references/citation-rules.md` — KLG citation format rules
2. `references/authority-verification.md` — Hallucination
   detection heuristics and verification protocol
3. The KLG Style Guide (`/mnt/project/klg-style-guide.md`) —
   citation placement standards
4. The project claude.md (`/mnt/project/claude.md`) — record
   citation format conventions

## Phase A: Citation Audit & Hallucination Triage

### Step A.1: Extract All Citations

Read the brief and build a comprehensive inventory of every
citation. Categorize each as:

**Case citations:** Party v. Party (Year) Volume Reporter Page
- Note whether it has a pincite
- Note whether it's the first occurrence (full cite) or a
  subsequent occurrence (short form)
- Note whether it has an explanatory parenthetical

**Statute citations:** Code, § Section
- Note the specific code and section

**Record citations:** Various formats:
- REF format: (REF251021-00001.)
- Appendix: (1-AA-1.)
- Reporter's Transcript: (RT page:line)
- Document-name format: (2024-11-13 Statement of Decision,
  PDF p. 18.)
- Note whether the page/line cite is specific

**Other citations:** Constitutional provisions, rules of court,
secondary sources

### Step A.2: Check for Completeness

For each paragraph in the brief, verify:

1. **Factual assertions have record support.** Any statement
   about what happened in the case should have a record
   citation. Flag uncited factual assertions.

2. **Legal propositions have case support.** Any statement of
   law should cite controlling authority. Flag unsupported
   legal propositions.

3. **Case citations have pincites.** Every case citation that
   supports a specific proposition should include a page
   reference. A bare volume cite is acceptable only for the
   general holding.

4. **First occurrences are full cites.** The first time a case
   appears, it should have the full citation.

5. **Short forms are consistent.** Check that short-form
   citations match their full-cite antecedents.

### Step A.3: Check for Placeholders

Claude's own placeholder standard (per claude.md) is the single
uniform tag `[VERIFY: short description]` — but a brief in cite
check may carry legacy tags from before that standard existed, or
placeholders inserted by co-counsel or outside drafters using their
own conventions. Search the entire brief broadly, then normalize:
- `[VERIFY: ...]` — the canonical form; still needs resolving
- `[RECORD CITE NEEDED]` or variations
- `[VERIFY]` or `[VERIFY CITE]` (bare, pre-standardization)
- `[RESEARCH NEEDED]`
- `[CITE]` or `[CITE NEEDED]` or `[CITE TBD]`
- `[TBD]` or `[TODO]`
- `[INSERT]` or `[ADD]`
- Square brackets containing instructions

This search doubles as the pre-filing safeguard against a repeat of
the LASSO near-miss (a petition nearly filed with unresolved
placeholders because a search for "verify" and "cite" alone missed
placeholders using other terminology). Report a literal count and
list of every match found, regardless of which variant it uses, and
do not treat the brief as filing-ready until that list is empty or
every item has been explicitly cleared by the attorney. When
recommending fixes, convert any non-canonical variant to
`[VERIFY: short description]` so future searches only need one term.

### Step A.4: Check Format Compliance

For each citation, verify format per `references/citation-rules.md`.

### Step A.5: Hallucination Triage

**THIS IS THE CRITICAL NEW STEP.**

For every case citation in the brief, apply the hallucination
detection protocol from `references/authority-verification.md`.
Classify each citation into one of three categories:

**🟢 CONFIRMED — High confidence this is a real case:**
Claude recognizes the case, the reporter/volume/page combination
is consistent with known patterns, the year is plausible for
the reporter series, and the holding as cited is consistent with
Claude's training data. These still go on the Westlaw list for
verification but are low priority.

**🟡 UNCERTAIN — Cannot confidently confirm:**
Claude has partial recognition (e.g., recognizes the case name
but not the specific volume/page, or recognizes the reporter
but the page seems off), or the citation comes from a source
known to hallucinate (e.g., ChatGPT Deep Research output that
was compiled into the brief). Flag for mandatory Westlaw
verification.

**🔴 SUSPECT — Likely hallucinated or fabricated:**
Claude does not recognize the case at all, the reporter/volume/
page combination is impossible or implausible (e.g., a Cal.5th
volume that doesn't exist yet, a page number that exceeds the
volume's range), the year is inconsistent with the reporter
series, or the stated holding contradicts what Claude knows
about the area of law. Flag as critical — must verify before
filing.

**Hallucination risk factors (from reference file):**
- Citation was generated by ChatGPT or another AI tool
- Citation appeared in a Deep Research memo
- Case name sounds generic or formulaic
- Reporter volume is at the edge of known publication
- Page number is suspiciously round (e.g., p. 100, p. 500)
- Holding as stated is too perfectly tailored to the argument
- Case is from a jurisdiction or era where Claude has sparse
  training data
- Citation includes an unusual or unfamiliar party name paired
  with a well-known legal proposition

### Step A.6: Generate Westlaw Pull List

Produce two things, in this order. Do not merge them — they
serve different purposes and different formats.

**1. The attorney-review list.** Organized by priority, with
case names and flag reasons so a human can act on it:

```
WESTLAW PULL LIST — ATTORNEY REVIEW
Brief: [title]
Date: [date]
Total authorities to verify: [N]

🔴 CRITICAL — Verify immediately (likely hallucinated):
1. [Full citation] — [reason for flag]
2. ...

🟡 MANDATORY — Verify before filing:
1. [Full citation] — [reason for flag]
2. ...

🟢 ROUTINE — Confirm good law status:
1. [Full citation]
2. ...
```

**2. The paste-ready Find & Print list.** This is what
actually goes into Westlaw's Find & Print search box, and it
is NOT the list above with the labels stripped off. Format
per the same rule as `klg-research-compilation` Rule 5 —
bare reporter cite only, one per line, deduplicated across
all three priority tiers, nothing else:

```
19 Cal.2d 807
11 Cal.App.5th 626
579 U.S. 197
```

No case names, no years, no pincites, no parentheticals, no
priority labels, no headers. Westlaw's Find & Print rejects
anything else. Deduplicate before printing — the same
citation may appear in more than one priority tier above.

### Step A.7: Produce Phase A Audit Report

Structure the report as:

```
CITATION AUDIT REPORT — PHASE A
Brief: [title]
Date: [date]
Status: AI-assisted audit — requires attorney review

SUMMARY
- Total citations found: [N]
- Case citations: [N] (with pincites: [N], without: [N])
- Record citations: [N]
- Statute citations: [N]
- Placeholders found: [N]
- Format issues: [N]
- Hallucination triage: [N] 🟢 / [N] 🟡 / [N] 🔴

HALLUCINATION FLAGS
[List all 🔴 and 🟡 citations with explanations]

CRITICAL ISSUES (must fix before filing)
[Format/completeness problems]

IMPORTANT ISSUES (should fix)
[Gaps that weaken the brief]

MINOR ISSUES (style preferences)
[Format improvements]

PLACEHOLDER INVENTORY
[All unresolved placeholders]

CITATION INDEX
[Complete list of every authority cited]

WESTLAW PULL LIST
[Paste-ready list for Comet/Westlaw]
```

### Step A.8: Deliver and Offer Next Steps

```
Phase A citation audit is complete. I found:
- [N] format/completeness issues ([N] critical)
- [N] unresolved placeholders
- [N] authorities flagged for Westlaw verification
  ([N] 🔴 suspect, [N] 🟡 uncertain, [N] 🟢 routine)

The Westlaw pull list is ready. Next steps:

1. Send the pull list to Comet for Westlaw Find & Print
2. Once Westlaw materials are back, upload them and say
   "verify the authorities" to run Phase B
3. Or, run the style-guide-check in parallel while waiting
```


## Phase B: Authority Verification

Phase B runs after the user uploads Westlaw materials. The
trigger is any of: "verify the authorities", "Westlaw is back",
"here are the Westlaw downloads", "run Phase B", "check the
authorities against Westlaw", or the user uploading .doc/.docx
files identified as Westlaw output.

### Step B.0: Prepare Westlaw Materials

**Check SharePoint before asking for an upload.** Many matters
already have a Westlaw Find & Print batch sitting in the matter's
KLG Research folder from an earlier pass. Search that folder first
for individual case PDFs and/or a combined Find & Print PDF. If
found, read each with `read_resource` and use that text as the
source for Steps B.1–B.4 — no manual upload needed. Only fall back
to asking the user to run and upload Westlaw output for authorities
that SharePoint doesn't cover.

Some matters have both a SharePoint batch and CoCounsel-grounded
holdings from earlier in the session. When both exist, prefer the
SharePoint full text; fall back to a CoCounsel-grounded summary
only when no full text is available, and label anything sourced
that way medium confidence, never high.

If the Westlaw output is in .doc format, convert to .docx:
```bash
python /mnt/skills/public/docx/scripts/office/soffice.py \
  --headless --convert-to docx westlaw.doc
```

Note: soffice.py outputs to root (`/`), not the working
directory. Copy the converted file to the working directory.

Extract text using pandoc:
```bash
pandoc westlaw.docx -t plain -o westlaw.txt
```

Parse the extracted text to identify individual cases. Westlaw
Find & Print output typically separates cases with headers
containing the case name, citation, and court information.

### Step B.1: Match Citations to Westlaw Text

For each case citation in the brief, find the corresponding
authority in the Westlaw output. Match on case name and
citation. If a cited authority is NOT in the Westlaw output,
flag it — it either wasn't pulled or doesn't exist.

### Step B.2: Verify Existence

For each matched authority, confirm:
1. **The case exists.** The Westlaw text contains the case.
2. **The citation is correct.** The reporter, volume, and
   starting page match what Westlaw shows.
3. **The year is correct.** The decision year matches.
4. **The court is correct.** The deciding court matches any
   court designation in the citation.

If any of these fail, the citation is either hallucinated or
contains an error. Flag as 🔴 CRITICAL.

### Step B.3: Verify Holding Accuracy

For each verified authority, read the Westlaw text and assess:

1. **Does the case address the legal issue cited?** Read the
   holding and key passages. Does the case actually discuss
   the legal principle for which it is cited in the brief?

2. **Does the holding support the proposition?** The brief
   cites this case for a specific proposition. Does the case
   actually hold or say what the brief claims? Rate as:
   - ✅ ACCURATE — The case clearly supports the proposition
   - ⚠️ CLOSE BUT IMPRECISE — The case addresses the topic
     but the brief overstates, understates, or slightly
     mischaracterizes the holding
   - ❌ INACCURATE — The case does not support the
     proposition as stated, or the holding is materially
     different from what the brief claims

3. **Pincite accuracy.** If a specific page is cited, does
   that page contain the relevant discussion? (This requires
   the Westlaw text to include page breaks or star pagination.)

4. **Parenthetical accuracy.** If the citation includes a
   parenthetical quote or characterization, verify it against
   the actual text.

**Confidence discipline (non-negotiable):** rate an authority's
support only from text actually read this session — SharePoint
full text or a freshly-uploaded Westlaw pull. Never rate a holding
from training memory. An authority with no source text on hand is
marked "not assessed," routed to the bare-citation Find & Print
list below, and never given a 🟢 signal.

### Step B.4: Check KeyCite Status

For each authority, record the KeyCite status:
- **Green** — Good law, no negative treatment
- **Yellow flag** — Distinguished or limited but not overruled
  (note the distinguishing case and assess relevance)
- **Red flag** — Overruled or superseded on the cited point
  (CRITICAL — must address before filing)
- **Not found** — Authority not in Westlaw (CRITICAL —
  likely hallucinated)

### Step B.5: Produce Phase B Verification Report

```
AUTHORITY VERIFICATION REPORT — PHASE B
Brief: [title]
Date: [date]
Status: AI-assisted verification — requires attorney review

SUMMARY
- Authorities verified: [N] of [N] total
- ✅ Verified accurate: [N]
- ⚠️ Close but imprecise: [N]
- ❌ Inaccurate or unsupported: [N]
- 🔴 Not found / likely hallucinated: [N]
- KeyCite flags: [N] yellow, [N] red

CRITICAL FINDINGS (must fix before filing)
[List each ❌ and 🔴 finding with details]

PROPOSITION-SUPPORT CHART
| # | Citation | Proposition in Brief | Source Available | Signal | Confidence | Basis | Notes |
|---|----------|----------------------|-------------------|--------|------------|-------|-------|
| 1 | [cite]   | [what brief says]    | SharePoint Y/N    | 🟢/🟡/🔴 | High/Med/Low | Full text / CoCounsel-grounded / Not assessed | [details] |

Signal legend: 🟢 supported, 🟡 questionable, 🔴 not supported.
An authority marked "Not assessed" under Basis never carries a 🟢
signal — see the confidence-discipline rule in Step B.3.

RECOMMENDED FIXES
For each 🟡 and 🔴 finding:
1. [Citation] — [What's wrong] — [Suggested fix]

BARE-CITATION FIND & PRINT LIST
For every authority marked "Not assessed" — no source text on hand
this session. Bare reporter citation only (volume/reporter/page),
one per line, deduplicated, per the Westlaw Find & Print Format
rule in claude.md — no case names, years, pincites, or
parentheticals, so the list pastes directly into the Westlaw batch
box. Statutes go in their own separate batch-safe list.
```

### Step B.6: Deliver and Offer Next Steps

```
Phase B authority verification is complete.

[N] authorities verified:
- [N] ✅ accurate
- [N] ⚠️ need refinement
- [N] ❌ inaccurate — must fix
- [N] 🔴 not found — must replace or remove

Would you like me to:
1. Work through the fixes now (I'll propose replacement
   language for each problem)
2. Run the style-guide-check on the corrected brief
3. Both — fix citation problems, then run the style check
```


## What This Skill Does NOT Do

- **Rewrite prose** — Use klg-brief-elevation for substantive
  improvements.
- **Check style conformance beyond citations** — Use
  klg-style-guide-check for terminology, heading formatting,
  prohibited words, etc.
- **Generate new research** — Use klg-deep-research-prompts if
  the audit reveals areas that need additional authority.
- **Run Westlaw searches** — Phase B requires Westlaw materials
  to be uploaded. The skill generates the pull list; Comet or
  the user executes the Westlaw search.
