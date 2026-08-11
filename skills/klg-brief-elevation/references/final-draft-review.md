# Final Draft Review Framework

This reference file contains the detailed review criteria for
near-final briefs. It is used in Phase 2B Step 4 (Final Review)
and in Triage mode when the brief is already in near-final or
final state. It draws from the ChatGPT Final Draft Review and
Proofread prompt in the KLG AI OS.

## When to Use This Framework

Use this framework when:
- The brief is classified as NEAR FINAL or FINAL / POLISH
- The user is doing a final review before filing
- Phase 2B Step 4 (after strategic changes are implemented)
- The user specifically requests a final-draft review

## Materials Needed

For the most thorough review, Claude should have:
- (A) The near-final brief draft
- (B) The KLG Style Guide (read from /mnt/project/)
- (C) All source documents supporting factual assertions
  (record excerpts, exhibits, declarations, transcripts)
- (D) All legal authorities cited in the brief
  (Westlaw downloads if available)

If some materials are unavailable, proceed with what is
available and flag limitations.

## Review Scope

### A. Substantive Legal Analysis

Evaluate the logical strength and coherence of arguments:

1. **Argument strength assessment** — For each main argument,
   rate as Strong / Moderate / Weak with explanation.

2. **Logical gaps** — Identify places where the reasoning
   skips steps or makes unwarranted assumptions.

3. **Ambiguities** — Flag language that could be read multiple
   ways or that invites adverse interpretation.

4. **Missing elements** — Has the brief established every
   element of every claim/defense it asserts?

5. **Standard of review alignment** — Does each argument
   correctly identify and apply its standard of review?
   Does the analysis match the standard? (e.g., not making
   credibility arguments under de novo review)

6. **Preservation** — For each issue, has the brief established
   that the issue was preserved in the trial court? If not,
   has it identified an applicable exception?

7. **Prejudice** — For each claimed error, has the brief
   established prejudice? Has it applied the correct prejudice
   standard (Watson/Chapman/structural)?

8. **High-leverage improvements** — Suggest reorganizations
   or reframings that increase clarity and persuasiveness.
   Always provide exact proposed language with insertion points.

### B. Fact-Checking

For every factual assertion in the brief:

1. **Citation present?** — Confirm it has a record citation.
   Flag any factual assertion without a citation.

2. **Citation accuracy** — If source documents are available,
   verify that the cited source fully supports the stated fact.

3. **Characterization accuracy** — Is the characterization
   fair? Flag any statements that overstate, understate, or
   mislead about what the record shows.

4. **Missing facts** — Are there favorable facts in the record
   that the brief fails to mention?

5. **Unfavorable facts** — Are unfavorable facts acknowledged
   appropriately? (Hiding them is worse than addressing them.)

Produce a fact-checking table:

| Assertion | Citation | Verified? | Notes |
|-----------|----------|-----------|-------|
| [fact] | [cite] | ✅/⚠️/❌ | [details] |

### C. Quote Verification

For every quoted passage in the brief:

1. Compare the quote to its underlying source (if available).
2. Verify accuracy down to punctuation, brackets, and ellipses.
3. Check that emphasis designations are correct ("emphasis
   added" vs. "emphasis in original").
4. Verify that the quote is not taken out of context.

Flag discrepancies in a table:

| Location | Brief Quote | Source Text | Issue |
|----------|-------------|-------------|-------|
| [page/¶] | [brief text] | [source text] | [discrepancy] |

### D. Legal Citation Accuracy

For every legal authority cited:

1. **Citation format** — Correct California Style Manual or
   Bluebook format? (Per /mnt/project/claude.md standards.)

2. **Holding accuracy** — Does the cited case actually stand
   for the proposition stated? Flag any mischaracterization.

3. **Still good law?** — If the authority seems old or
   questionable, flag for Westlaw verification.
   Use [VERIFY — check if still good law].

4. **Parenthetical quality** — Are explanatory parentheticals
   present where required? (No naked cites per KLG standards.)

5. **Pincites** — Are pincites present for all quoted or
   closely paraphrased propositions?

6. **Short form consistency** — Are short form citations
   consistent and correct? (Must use p./pp. before pincite
   page numbers per KLG standards.)

### E. Introduction Review

The introduction is the most-read part of the brief. Verify:

1. **Roadmap** — Does it provide an effective preview of the
   issues, the controlling rules, and the conclusions?

2. **Case narrative** — Does it present a compelling story?

3. **Legal framework** — Does it show why the client wins on
   the law?

4. **Equities** — Does it show why fairness supports the client?

5. **Error and prejudice** — Does it identify the trial court
   error and explain why it matters?

6. **Funnel approach** — Does it move from the general (what
   the dispute is about) to the specific (what the appeal is
   about)?

If the introduction needs improvement, provide a complete
rewritten version.

## Output Format

### I. High-Leverage and Critical Changes

Organized by section of the brief. For each change:

- **Issue** — What the problem is
- **Why it matters** — Impact on persuasiveness or accuracy
- **Severity** — Critical / High-Leverage / Medium / Low
- **Location in brief** — With enough quoted text to find it
- **Proposed revision** — Complete paste-ready replacement

### II. Quote and Citation Accuracy Table

| Issue | Brief Text | Source Text | Corrected Text | Citation |
|-------|-----------|-------------|----------------|----------|
| [type] | [original] | [source] | [corrected] | [cite] |

### III. Argument Structure and Strategy

Narrative analysis covering:
- Strength of each main argument
- Opportunities to front-load strongest points
- Logical flow improvements
- Narrative clarity
- Any reorganizations that increase persuasiveness

## Citation Placement Convention

Tim's preference (enforce in all proposed revisions):
- End the sentence with normal punctuation
- Add a separate citation-only sentence immediately after
- Do NOT place citations at the end of the substantive
  sentence — make citations their own sentences

Example:
  The trial court applied the wrong standard.
  (Smith v. Jones (2020) 50 Cal.App.5th 100, 110.)

Not:
  The trial court applied the wrong standard (Smith v.
  Jones (2020) 50 Cal.App.5th 100, 110).

## Guardrails

- Base all corrections strictly on provided materials.
- If a source is missing, identify the gap — do not guess.
- If a fact or quote is ambiguous, flag it rather than
  assuming what the source says.
- Never fabricate or invent authorities.
- Never change legal strategy — flag concerns and recommend.
