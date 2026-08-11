# KLG Brief Structures

This reference documents the structural components of each type
of California appellate brief, the boundaries that the assembly
script needs to identify, and which sections get replaced vs.
preserved during assembly.

## General Structure Principles

All KLG appellate briefs share these front-matter and back-matter
components:

**Front Matter (always preserved):**
1. Cover page (court name, case caption, parties, counsel info)
2. Certificate of Interested Entities or Parties
3. Table of Contents (needs updating after assembly)
4. Table of Authorities (needs updating after assembly)

**Back Matter (always preserved):**
1. Certificate of Word Count (number needs updating)
2. Proof of Service (if present)
3. Attachment / Appendix references

## Writ Petition (Petition for Writ of Supersedeas / Mandate)

Writ petitions have a unique two-part structure. The first part
is the formal petition with numbered averments. The second part
is a legal memorandum that contains the substantive argument.

### Structure
```
[FRONT MATTER — preserve]
  Cover Page
  Certificate of Interested Entities
  Table of Contents
  Table of Authorities

[INTRODUCTION — replace body text, preserve heading]
  Introduction heading (P1Pleading1)
  Body paragraphs (BodyText) ← REPLACE THESE

[FORMAL PETITION — preserve entirely]
  "Petition for Writ of Supersedeas" heading
  I. Parties and Jurisdiction (numbered averments)
  II. Background (numbered averments)
  III. Irreparable Harm (numbered averments)
  IV. Request for Immediate Temporary Stay
  V. Authenticity of Exhibits and Prayer for Relief
  Prayer for Relief (WHEREFORE paragraph + bullet list)
  Signature block
  Verification

[MEMORANDUM — replace body, preserve page break + heading]
  Page break
  "Memorandum of Points and Authorities" heading (P1Pleading1)
  Statement of the Case ← REPLACE FROM HERE
  Standard of Review
  Argument (A, B, C, D with subsections)
  Conclusion ← THROUGH HERE

[BACK MATTER — preserve]
  Certificate of Word Count
  Signature block
  Attachment reference
```

### Boundary Detection for Writ Petitions
Find these markers (all should have P1Pleading1 style nearby):
- `Introduction` — marks end of front matter, start of body
- `Petition for Writ of Supersedeas` — start of formal petition
- `Memorandum of Points and Authorities` — start of legal argument
- `Certificate of Word Count` — start of back matter

### What Gets Replaced
1. **Introduction body:** Everything between the Introduction
   heading and the Petition heading. The heading itself is
   preserved; only the body paragraphs are replaced.
2. **Memorandum body:** Everything between the Memorandum heading
   and the Certificate of Word Count. The page break and heading
   are regenerated; the body (Statement of Case through Conclusion)
   is replaced with new content.

### What Gets Preserved
- All front matter (cover page, cert, TOC, TOA)
- The Introduction heading itself
- The entire formal petition (sections I–VI, Prayer, signature,
  Verification)
- All back matter (Certificate of Word Count, Attachment)

## Opening Brief

Opening briefs have a simpler structure — one continuous document
with no formal petition section.

### Structure
```
[FRONT MATTER — preserve]
  Cover Page
  Certificate of Interested Entities
  Table of Contents
  Table of Authorities

[BODY — replace]
  Introduction ← REPLACE FROM HERE
  Statement of the Case
  Standard of Review
  Argument (A, B, C, D with subsections)
  Conclusion ← THROUGH HERE

[BACK MATTER — preserve]
  Certificate of Word Count
  Proof of Service
```

### Boundary Detection for Opening Briefs
- `Introduction` — start of replaceable content
- `Certificate of Word Count` — start of back matter

### What Gets Replaced
Everything from the Introduction heading through the Conclusion.

### What Gets Preserved
Front matter and back matter.

## Reply Brief

Reply briefs typically omit the Statement of Case and Standard
of Review (unless the respondent misstated the record or applied
the wrong standard). Structure is more compact.

### Structure
```
[FRONT MATTER — preserve]

[BODY — replace]
  Introduction ← REPLACE FROM HERE
  Argument (organized as responses to RB arguments)
  Conclusion ← THROUGH HERE

[BACK MATTER — preserve]
```

### What Gets Replaced
Introduction through Conclusion. The argument section typically
follows the RB's organization rather than the AOB's.

## Respondent's Brief

Respondent's briefs follow the same structure as opening briefs
but from the respondent's perspective.

### Structure
```
[FRONT MATTER — preserve]

[BODY — replace]
  Introduction ← REPLACE FROM HERE
  Statement of the Case (respondent's framing)
  Standard of Review
  Argument (responding to appellant's arguments)
  Conclusion ← THROUGH HERE

[BACK MATTER — preserve]
```

## Assembly Script Boundary Format

The assembly script expects boundary line numbers as a
comma-separated argument. The specific boundaries needed
depend on the brief type:

### Writ Petition Boundaries
```
--boundaries "intro_heading:<N>,petition_start:<N>,memo_pagebreak:<N>,cert_pagebreak:<N>"
```
- `intro_heading`: The 0-based line of the Introduction heading
  paragraph's `<w:p` opening tag
- `petition_start`: The 0-based line of the Petition heading
  paragraph's `<w:p` opening tag
- `memo_pagebreak`: The 0-based line of the page break paragraph
  before the Memorandum heading
- `cert_pagebreak`: The 0-based line of the page break paragraph
  before the Certificate of Word Count

### Opening/Reply/Respondent's Brief Boundaries
```
--boundaries "intro_heading:<N>,cert_pagebreak:<N>"
```
- `intro_heading`: The 0-based line where the Introduction heading
  paragraph starts
- `cert_pagebreak`: The 0-based line where the Certificate of
  Word Count page break starts

For these simpler brief types, the entire body between
Introduction and Certificate is replaced with the new content.

## Markdown Input Format

The markdown content should follow these conventions:

### For Introduction (all brief types)
Plain paragraphs only. No headings. Just body text that will
be styled as BodyText.

### For Memorandum / Body (writ petitions)
```markdown
# Statement of the Case

### The property and the license.

Body text...

### The enforcement action.

Body text...

# Standard of Review

Body text...

# Argument

## A. First argument heading as a complete persuasive sentence.

Body text...

### 1. First sub-argument.

Body text...

### 2. Second sub-argument.

Body text...

## B. Second argument heading.

Body text...

# Conclusion

Body text...
```

### For Body (opening/reply/respondent's briefs)
Same format but starting with `# Introduction`:
```markdown
# Introduction

Body text...

# Statement of the Case
...
# Standard of Review
...
# Argument
...
# Conclusion
...
```

## Post-Assembly Checklist

After assembly, these items need attention (usually done by
the attorney in Word):

1. **Update TOC:** Right-click the Table of Contents → Update
   Field → Update Entire Table
2. **Update TOA:** Right-click the Table of Authorities → Update
   Field → Update Entire Table
3. **Update word count:** Count words in the substantive sections
   (Introduction through Conclusion, excluding formal petition
   in writ petitions) and update the Certificate of Word Count
4. **Verify page breaks:** Check that section transitions don't
   create orphan blank pages
5. **Check heading rendering:** Confirm P1Pleading1 headings
   appear centered with small caps, P2Pleading2 appears bold,
   P3Pleading3 appears correctly
6. **Review signature blocks:** Ensure all signature blocks and
   date fields are intact
7. **Check [RECORD CITE NEEDED] placeholders:** Search for any
   remaining citation placeholders
