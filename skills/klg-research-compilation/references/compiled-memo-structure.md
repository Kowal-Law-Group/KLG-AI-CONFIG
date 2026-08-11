# Compiled Research Memorandum — Document Structure

This is the canonical structure for the compiled research memo
produced in Phase A. Every compiled memo must follow this layout.

## Header

```
COMPILED LEGAL RESEARCH MEMORANDUM

Case: [Full case name]
Prepared: [Date]
Source: Notion Research Page — [title and URL]
Source Memos: [N] Deep Research memos compiled
Status: DRAFT — AI ASSISTED — Citations require Westlaw verification
Pipeline Stage: Step 4 of 6 — Research Compilation
```

## Table of Contents

Generated from section headers.

## Executive Summary

2–3 paragraphs synthesizing all research findings:
- Strongest authority favoring our position (with citation)
- Most dangerous adverse authority (with citation)
- Key themes and patterns across the research
- Overall assessment of the legal landscape
- Any significant gaps in the research

Cap at ~250 words.

## Convergence Analysis

### High-Confidence Authorities (cited in 3+ memos)

| Authority | Full Citation | Cited in Memos | Issue |
|-----------|--------------|----------------|-------|
| [name] | [citation] | 1, 3, 5, 7 | [issue] |

### Moderate-Confidence Authorities (cited in 2 memos)

| Authority | Full Citation | Cited in Memos | Issue |
|-----------|--------------|----------------|-------|

### Single-Source Authorities (cited in 1 memo — verify carefully)

| Authority | Full Citation | Source Memo | Issue | Flag |
|-----------|--------------|-------------|-------|------|

## Issue-by-Issue Analysis

For each legal issue:

### Issue [N]: [Title]

**Source Memos:** [which memos addressed this]

**Governing Rule:** Synthesized rule statement with lead citation.

**Key Favorable Authority:**
- [Citation] — [parenthetical]

**Key Adverse Authority:**
- [Citation] — [parenthetical]

**Analysis:** Synthesized discussion. Note agreements, divergences,
and weight of authority.

**Strength Assessment:** Strong / Moderate / Weak — with explanation.

**Research Gaps:** What still needs verification.

## Potential Hallucination Flags

| Citation | Reason Flagged | Source Memo | Priority |
|----------|---------------|-------------|----------|
| [cite] | [reason] | Memo [N] | Verify First |

## Master Authority List

| # | Authority | Full Citation | Cited in Memo(s) | Issue | Confidence |
|---|-----------|--------------|-------------------|-------|------------|
| 1 | [name] | [citation] | Memos 1, 3, 7 | [issue] | High |

## Citation Format Requirements

- California: Cal. Style Manual (*Party v. Party* (Year) Vol Cal.5th Page)
- Federal: Bluebook (*Party v. Party*, Vol F.3d Page (9th Cir. Year))
- Include pincites and explanatory parentheticals (no naked cites)
- Italicize case names only
