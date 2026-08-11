# Triage Rules: Case vs. Article Classification

## Purpose

Each item in the "Blog This: Add Research" view must be
classified as CASE, ARTICLE, or AMBIGUOUS before processing.
This classification determines the processing path:
- CASE -> Westlaw Find & Print -> full opinion text
- ARTICLE -> URL fetch -> article content extraction
- AMBIGUOUS -> user decides

## Classification Rules

### CASE Indicators (any ONE is sufficient)

**Strong indicators (high confidence):**
- Title contains "[Party] v. [Party]" format
- Title contains a reporter citation (e.g., "163 F.4th 723"
  or "75 Cal.App.5th 1234")
- URL points to a court website or official opinion repository
- URL points to Westlaw or Lexis

**Moderate indicators (combine with other signals):**
- Title contains a court abbreviation: "9th Cir.", "Cal. Ct.
  App.", "S. Ct.", "SCOTUS", "Cal. Sup. Ct."
- Title contains a case date in parentheses:
  "(March 12, 2026)" or "(2026)"
- URL points to calapp.blogspot.com (the California Appellate
  Report -- this blog always discusses specific cases, even
  though the URL is a blog)
- Title starts with "GOOD." prefix (KLG's internal flag for
  noteworthy cases)

**Weak indicators (need additional signals):**
- Title mentions a ruling, decision, or holding
- Title references a specific legal issue that could be a
  case holding

### ARTICLE Indicators (any ONE is sufficient)

**Strong indicators (high confidence):**
- Title is a question or topic description without party names
  (e.g., "AI work product is protected?")
- Title references a person by name without "v." (e.g.,
  "Good, Adam Feldman on clerking")
- URL points to LinkedIn, a news outlet, or a non-legal blog
- Title references a policy, exam, or institutional action
  (e.g., "State Bar Ponder Admission Exam Without California
  Section")

**Moderate indicators:**
- Title is descriptive/editorial rather than case-name format
- URL points to reason.com, nytimes.com, or other news outlets
- No court or date references in the title

### AMBIGUOUS Cases

Classify as AMBIGUOUS when:
- The title could be either a case discussion or a commentary
  piece and there is no URL to disambiguate
- The title references a case name but the URL points to a
  commentary or analysis piece (not the opinion itself)
- The title is too vague to classify (e.g., a one-word topic)

## Special Patterns

### Blog posts about cases (calapp.blogspot.com)

The California Appellate Report (calapp.blogspot.com) posts
summaries of recent California appellate decisions. Items
linking to this blog should be classified as CASES because:
1. The primary value is the underlying court opinion
2. The blog URL can be fetched to extract the citation
3. The opinion text should come from Westlaw, not the blog

### "POD:" prefix items

Items with "POD:" prefix are podcast-flagged items. They
follow the same triage rules. The prefix does not affect
classification.

### "GOOD." prefix items

Items with "GOOD." prefix are marked as particularly
noteworthy cases. Strong indicator of CASE classification.

### Draft motions and internal documents

Items like "Draft Motion to Enforce Stay..." are neither
cases nor articles -- they are internal work product that
may have been tagged accidentally. Classify as ARTICLE and
skip URL fetch. Flag for the user:

```
This item appears to be internal work product, not an
external case or article. It may have been tagged
accidentally. Skip? (Y/N)
```

### Items referencing multiple cases

Some items compare or discuss multiple cases. Classify as
CASE and identify the primary case (usually the one named
in the title). Note secondary cases in the triage report
but only process the primary case through Westlaw.

## URL Domain Quick Reference

| Domain | Likely Classification |
|---|---|
| calapp.blogspot.com | CASE (blog about cases) |
| plus.lexis.com | CASE |
| 1.next.westlaw.com | CASE |
| reason.com | ARTICLE |
| linkedin.com | ARTICLE |
| metnews.com | CASE or ARTICLE (check title) |
| courts.ca.gov | CASE |
| supremecourt.gov | CASE |
| law.com | ARTICLE |
| nytimes.com, wsj.com | ARTICLE |

## Output Format

For each item, record:

```
{
  "notion_url": "[page URL]",
  "title": "[item title]",
  "source_url": "[URL field value or null]",
  "classification": "CASE | ARTICLE | AMBIGUOUS",
  "confidence": "HIGH | MEDIUM | LOW",
  "citation_resolved": "[citation or null]",
  "notes": "[any special observations]"
}
```
