---
name: klg-brief-assembly
description: "Assemble elevated brief content into a KLG .docx brief template with correct formatting and styles. Use whenever the user says 'assemble the brief', 'put this in the template', 'build the brief', 'put the brief together', 'format the brief', 'assemble in KLG format', or references inserting elevated/drafted content into an existing KLG brief .docx. Also triggers when the user finishes a brief elevation and says 'now put it together', 'build the final version', or 'make the docx'. This skill handles the technical document assembly — converting markdown content to properly styled Word XML and splicing it into the existing brief template while preserving front matter, formal sections, and back matter. Do NOT use for substantive brief writing (use klg-brief-elevation), style checking (use klg-style-guide-check), or case assessments."
---

# KLG Brief Assembly

## Purpose

This skill bridges the gap between substantive brief work (which produces markdown or section-by-section drafts) and the final .docx deliverable. It takes elevated content and assembles it into an existing KLG brief template with correct formatting, styles, and structure.

The core problem it solves: KLG briefs use custom Word styles (P1Pleading1, P2Pleading2, P3Pleading3, BodyText) that pandoc doesn't know about. Content converted through pandoc arrives with generic heading styles that render incorrectly. This skill handles the style mapping, structural boundary detection, and XML splicing needed to produce a correctly formatted brief.

## Prerequisites

Before starting, read these files:

1. **The docx skill** — for unpack/repack utilities:
   Read the docx SKILL.md at the sibling skill path (typically `mnt/.skills/skills/docx/SKILL.md`) to understand the unpack → edit → repack workflow. The key scripts are:
   - `unpack.py` — extracts .docx to editable XML
   - `pack.py` — repacks edited XML into .docx

2. **This skill's reference files:**
   - `references/klg-styles.md` — Complete style definitions and mapping rules
   - `references/brief-structures.md` — Structural templates for each brief type

## Required Inputs

- **Template brief** (.docx): An existing KLG brief with correct front matter, formal sections, and back matter. This is typically the current draft or the brief being elevated.
- **Elevated content** (markdown): The new substantive content — typically a section-by-section draft produced by the brief elevation skill or manual drafting.
- **Brief type**: Identify which structure applies (writ petition, opening brief, reply brief, respondent's brief). When uncertain, ask the attorney.

## CRITICAL: Revision vs. Fresh Build Checkpoint

Before starting any work, determine which path applies:

**Is this a revision to an existing document the user has already
edited, or a fresh build from a blank template?**

- If the user uploads a document they have already worked on and
  asks for changes (add citations, fix headings, remove a section,
  fix numbering, change phrasing), this is a **REVISION**. ALWAYS
  unpack the user's current file and make surgical XML edits to
  only the affected paragraphs. NEVER rebuild from a template or
  regenerate content. The default path is: unpack the user's
  document → identify only the specific XML elements that need to
  change → edit those elements → repack.

- If the user explicitly asks for a fresh build ("assemble the
  brief," "put this in the template," "build from scratch"), this
  is a **FRESH BUILD**. Use the full assembly workflow below.

When in doubt, ask: "You already have edits in this document. Do
you want me to make targeted changes to your current version, or
rebuild from the template? Rebuilding will overwrite your edits."

## CRITICAL: Citation Integrity

When inserting citations from a source document (case memo,
research memo, or any other source):

1. **Read the actual source document** and extract the literal
   citation strings as they appear.
2. **Present the extracted citations to the user** for
   confirmation before inserting them into the brief.
3. **Never invent or infer citation formats.** If a citation
   cannot be found in the source, flag it as missing rather than
   guessing. Write `[RECORD CITE NEEDED — not found in source]`
   and move on.
4. **Never fabricate record volume or page numbers.** Formats
   like `(CT 6)` or `(1 CT 10)` must come from an actual source
   document — never generated from inference.

## Appellate Style Rules

These apply whenever this skill produces or modifies brief text:

- **Party designations:** Refer to our client by their appellate
  party designation (e.g., "respondent," "appellant"), not
  trial-court designations like "plaintiff" or "defendant," unless
  quoting from a trial court document.
- **Emphasis:** Use italics for emphasis in brief text. Bold is
  acceptable only for dates. Never use bold for textual emphasis.
- **Block quotes from rules/statutes:** Extended quotations from
  rules or statutes must use block-quote formatting (Quote style),
  not inline quotation.
- **Rules of Court short form:** After the first full citation,
  the correct short form is lowercase "rule" with no "Cal." prefix
  (e.g., "rule 8.108(e)(2)," not "Cal. Rules of Court, rule
  8.108(e)(2)").
- **Caption blocks:** Use cross-references to the "Parties"
  bookmark to maintain consistency with the template.

## Assembly Workflow

### Phase 1: Structural Analysis

Unpack the template brief and identify structural boundaries in the document.xml.

```bash
DOCX_SCRIPTS="<path-to-docx-skill>/scripts/office"
python3 "$DOCX_SCRIPTS/unpack.py" "<template.docx>" unpack_orig/
```

Then analyze `unpack_orig/word/document.xml` to find the key boundary lines. The boundaries depend on the brief type — see `references/brief-structures.md` for the specific sections to look for in each type.

**How to find boundaries:** Use grep to locate key heading text in the XML:
```bash
grep -n '<w:t' unpack_orig/word/document.xml | grep -i 'introduction\|memorandum\|certificate of word\|verification\|statement of the case\|argument'
```

Cross-reference with style markers to distinguish TOC entries from actual headings:
```bash
grep -n 'P1Pleading1' unpack_orig/word/document.xml
```

A heading in the TOC will appear at an early line number without a P1Pleading1 style nearby. The actual section heading will have P1Pleading1 in its paragraph properties. Always verify by checking a few lines around each match to confirm you have the actual heading, not the TOC entry.

Record the 1-based line numbers for each boundary. These are critical for the splice.

### Phase 2: Content Conversion

Prepare clean markdown files for each content section that needs to be replaced. Strip any metadata, notes-for-attorney sections, or formatting instructions — just the substantive text.

**Markdown heading conventions for KLG briefs:**
- `# Heading` → P1Pleading1 (top-level section headings: Statement of Case, Standard of Review, Argument, Conclusion)
- `## Heading` → P2Pleading2 (lettered argument subsections: A, B, C, D)
- `### Heading` → Context-dependent (this is the tricky part):
  - Inside Statement of Case: italic narrative subheadings ("The property and the license.")
  - Inside Argument sections: P3Pleading3 numbered subsections ("1. The injunction enjoins...")
- Body text → BodyText
- `> Block quote` → Quote style (or BodyText + indent). Do NOT
  include quotation marks around block-quoted text — indentation
  signals the quotation. The citation paragraph after a block
  quote uses BodyTextContinued style (no first-line indent).

Convert each markdown file to .docx using pandoc with the template brief as the reference doc:
```bash
pandoc content.md -o content.docx --reference-doc="<template.docx>"
```

Then unpack the pandoc output:
```bash
python3 "$DOCX_SCRIPTS/unpack.py" content.docx unpack_content/
```

### Phase 3: Style Remapping

This is the critical step. Pandoc generates these styles that need remapping:

| Pandoc Style | KLG Target | Notes |
|---|---|---|
| `Heading1` | `P1Pleading1` | Centered, small caps in Word |
| `Heading2` | `P2Pleading2` | Bold, left-aligned |
| `Heading3` (in Argument) | `P3Pleading3` | Numbered subsections |
| `Heading3` (in Statement of Case) | Italic BodyText | Narrative subheadings |
| `FirstParagraph` | `BodyText` | Pandoc's first-after-heading style |
| `BlockText` | `Quote` (or `BodyText` + indent) | Block quotes — no quotation marks |
| `BodyText` | `BodyText` | No change needed |

Use the assembly script at `scripts/assemble_brief.py` to handle the style remapping and splice. The script:
1. Extracts body paragraphs from pandoc-generated XML
2. Splits them into individual `<w:p>` elements
3. Remaps styles based on context (tracking whether we're in Statement of Case vs. Argument sections)
4. Rebuilds headings using proper KLG XML templates
5. Splices everything into the template document.xml at the correct boundary lines

```bash
python3 "<skill-path>/scripts/assemble_brief.py" \
  --template unpack_orig/ \
  --content-intro intro_clean.md \
  --content-memo memo_clean.md \
  --brief-type petition \
  --output-dir unpack_final/ \
  --boundaries "intro_heading:3856,petition_start:4262,memo_pagebreak:5491,cert_pagebreak:7435"
```

### Phase 4: Repack and Verify

Repack the modified XML into a .docx:
```bash
python3 "$DOCX_SCRIPTS/pack.py" unpack_final/ "<output.docx>" \
  --original "<template.docx>" --validate false
```

Fix standalone declarations (prevents Word "unreadable content" error):
```bash
python3 /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py "<output.docx>"
```

Then verify by converting to PDF and visually checking key pages:
- Cover page and front matter preserved
- Introduction renders with correct body text styling
- Section headings appear centered with small caps (in Word; PDF converters may not render custom styles)
- Formal petition sections preserved exactly
- Memorandum headings and subheadings use correct hierarchy
- Block quotes are indented
- Certificate of Word Count preserved

**Important notes for the attorney:**
- The TOC and TOA will need updating in Word (right-click → Update Field)
- The Certificate of Word Count number will need updating after TOC refresh
- Custom styles (P1Pleading1, P2Pleading2, P3Pleading3) render correctly in Microsoft Word but may appear as plain text in LibreOffice or PDF converters

## When the Script Isn't Available

If the assembly script isn't accessible, you can perform the assembly manually using Python. The key operations are:

1. **Extract pandoc body paragraphs:** Parse the XML between `<w:body>` tags, excluding `<w:sectPr>`
2. **Split into `<w:p>` elements:** Use regex to find each `<w:p ...>...</w:p>`
3. **Detect style:** Look for `<w:pStyle w:val="StyleName"/>` in each paragraph
4. **Track context:** When you encounter a Heading1, note which section you're entering (Statement of Case, Standard of Review, Argument, Conclusion)
5. **Remap:** Replace the style value based on the mapping table above. For headings that need complete rebuilding (P1Pleading1, P2Pleading2, P3Pleading3, italic subheadings), use the XML templates from `references/klg-styles.md`
6. **Splice:** Concatenate: original lines through intro heading → new intro body → original petition sections → page break + memorandum heading + new memo body → original certificate through end
7. **Write and repack**

## Common Issues and Solutions

**TOC entry found instead of actual heading:** When searching for boundary text like "Memorandum of Points and Authorities," the first match is often the TOC entry (early in the document). The actual heading appears later with a P1Pleading1 style. Always verify the line number is past the TOC/TOA section.

**FirstParagraph style:** Pandoc assigns "FirstParagraph" to the first paragraph after each heading. This renders differently from BodyText (often with different spacing). Always remap to BodyText.

**Heading3 context ambiguity:** The same markdown `###` syntax produces headings that should map to completely different styles depending on location. The assembly script tracks this by setting a flag when it enters the "Argument" section (after seeing "Argument" as a Heading1).

**Blank pages:** Can occur at section boundaries due to page breaks in the original template. Check for orphaned `<w:br w:type="page"/>` elements.

**Block quotes rendering as compressed text:** If BlockText isn't remapped to Quote style (or BodyText with explicit `<w:ind w:left="1440" w:right="1440"/>`), it may render incorrectly. Use 1440 twips (1 inch) for indentation, matching the Quote style definition.

**P2/P3 numbering overrides:** Do NOT include `<w:numPr>` with `numId="0"` on P2Pleading2 or P3Pleading3 paragraphs — this suppresses automatic numbering and forces manual letter/number prefixes. The style definitions already link to the correct numbering list (typically numId=1). Omit the numPr element entirely and do not include manual "A." or "1." text in headings. See `references/klg-styles.md` for details.
