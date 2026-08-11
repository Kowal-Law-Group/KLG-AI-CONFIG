# KLG Brief Word Styles

This reference documents the custom Word styles used in KLG appellate
briefs, their formatting properties, and the XML templates needed
to generate them programmatically.

## Style Definitions

### P1Pleading1 — Top-Level Section Headings

Used for: Statement of Case, Standard of Review, Argument,
Conclusion, Memorandum of Points and Authorities, Introduction,
Petition for Writ of Supersedeas, and other major section breaks.

Visual appearance: Centered, small caps, Century Schoolbook 13pt.

XML template:
```xml
<w:p w14:paraId="{paraid}" w14:textId="{textid}"
     w:rsidR="00A96F5E" w:rsidRDefault="00A96F5E" w:rsidP="00A61E3D">
  <w:pPr>
    <w:pStyle w:val="P1Pleading1"/>
    <w:numPr>
      <w:ilvl w:val="0"/>
      <w:numId w:val="0"/>
    </w:numPr>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r>
    <w:t>{text}</w:t>
  </w:r>
</w:p>
```

Notes:
- The `<w:numPr>` with `numId="0"` suppresses any auto-numbering
  that the style definition might carry.
- `<w:jc w:val="center"/>` ensures centering even if the style
  definition doesn't include it.
- Small caps are defined in the style itself (in styles.xml),
  not in each paragraph instance.

### P2Pleading2 — Lettered Argument Subsections

Used for: A., B., C., D. level argument headings.
These are the primary argument divisions.

Visual appearance: Bold, left-aligned, Century Schoolbook 13pt.
Typically formatted as complete persuasive sentences.

**Numbering behavior:** P2Pleading2 is linked to a numbering
definition (typically numId=1, ilvl=1) that provides automatic
"A.", "B.", "C." lettering. Do NOT include `<w:numPr>` with
`numId="0"` — that suppresses automatic numbering and forces
manual letter prefixes, which breaks if headings are reordered.
Do NOT include manual "A." or "B." text in the heading — let
the numbering definition handle it.

XML template (relies on style-defined numbering):
```xml
<w:p w14:paraId="{paraid}" w14:textId="{textid}"
     w:rsidR="00A96F5E" w:rsidRDefault="00A96F5E" w:rsidP="00A61E3D">
  <w:pPr>
    <w:pStyle w:val="P2Pleading2"/>
  </w:pPr>
  <w:r>
    <w:t>{text}</w:t>
  </w:r>
</w:p>
```

### P3Pleading3 — Numbered Argument Subsections

Used for: 1., 2., 3. level argument sub-subsections within
a lettered section.

Visual appearance: Bold or bold-italic, left-aligned,
Century Schoolbook 13pt.

**Numbering behavior:** P3Pleading3 is linked to a numbering
definition (typically numId=1, ilvl=2) that provides automatic
"1.", "2.", "3." numbering. Same rule as P2: do NOT include
`<w:numPr>` with `numId="0"`, and do NOT include manual number
prefixes in the heading text. Let the style handle it.

XML template (relies on style-defined numbering):
```xml
<w:p w14:paraId="{paraid}" w14:textId="{textid}"
     w:rsidR="00A96F5E" w:rsidRDefault="00A96F5E" w:rsidP="00A61E3D">
  <w:pPr>
    <w:pStyle w:val="P3Pleading3"/>
  </w:pPr>
  <w:r>
    <w:t>{text}</w:t>
  </w:r>
</w:p>
```

### BodyText — Standard Body Paragraphs

Used for: All substantive body text, citations, and narrative
content.

Visual appearance: Century Schoolbook 13pt, single spacing
(line=240 twips), justified alignment.

The BodyText style is already defined in pandoc's output when
using a KLG reference doc. No XML template needed — just ensure
the `<w:pStyle w:val="BodyText"/>` attribute is present.

Key formatting properties (half-points for font size):
- Font: Century Schoolbook
- Size: 26 half-points (13pt)
- Line spacing: 240 twips (single)
- Alignment: justified

### Italic Narrative Subheadings

Used for: Subheadings within the Statement of Case that serve
as narrative section markers (e.g., "The property and the
license.", "The enforcement action.").

These are NOT a named style — they're BodyText paragraphs with
italic run properties and keepNext to prevent orphaning.

XML template:
```xml
<w:p w14:paraId="{paraid}" w14:textId="{textid}"
     w:rsidR="00A96F5E" w:rsidRDefault="00A96F5E">
  <w:pPr>
    <w:pStyle w:val="BodyText"/>
    <w:keepNext/>
    <w:spacing w:before="240"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:i/>
      <w:iCs/>
    </w:rPr>
    <w:t>{text}</w:t>
  </w:r>
</w:p>
```

Notes:
- `<w:keepNext/>` prevents the subheading from appearing at the
  bottom of a page with no following text.
- `<w:spacing w:before="240"/>` adds space above the subheading
  (240 twips = 1/6 inch) for visual separation.
- The italic formatting is on the run (`<w:rPr>`) not the
  paragraph, so it applies to the text only.

### Quote — Block Quotes

Used for: Extended quotations from court opinions, statutes,
or contractual provisions where the exact wording matters.

Visual appearance: Indented left and right (1440 twips = 1 inch
on each side), Century Schoolbook 13pt.

**Formatting rules:**
- Do NOT wrap block-quoted text in quotation marks. The
  indentation itself signals a direct quotation. Adding
  quotation marks is redundant.
- The citation paragraph immediately after a block quote should
  use BodyTextContinued style (see below), not BodyText.

If the template has a named "Quote" style, use it:
```xml
<w:pPr>
  <w:pStyle w:val="Quote"/>
</w:pPr>
```

If no Quote style exists, fall back to BodyText with explicit
indentation:
```xml
<w:pPr>
  <w:pStyle w:val="BodyText"/>
  <w:ind w:left="1440" w:right="1440"/>
  <w:spacing w:before="120" w:after="120"/>
</w:pPr>
```

When remapping pandoc's BlockText style, replace the style
reference and add the indentation properties.

### BodyTextContinued — Citation After Block Quote

Used for: The citation paragraph immediately following a block
quote. Visually identical to BodyText except it has no first-
line indent, which keeps the citation visually connected to the
block quote above it.

If the template has a named "BodyTextContinued" style, use it:
```xml
<w:pPr>
  <w:pStyle w:val="BodyTextContinued"/>
</w:pPr>
```

If no BodyTextContinued style exists, use BodyText with an
explicit first-line indent of zero:
```xml
<w:pPr>
  <w:pStyle w:val="BodyText"/>
  <w:ind w:firstLine="0"/>
</w:pPr>
```

## Other Styles (Preserved from Template)

These styles appear in KLG briefs but are not generated by
pandoc — they're preserved from the template document:

- **CourtLines** — Cover page court identification lines
  (bold, all caps, centered)
- **CapRight** — Right-aligned caption elements
- **TOC1, TOC2, TOC3** — Table of Contents levels with dot
  leaders
- **TOAEntry** — Table of Authorities entries

## Pandoc → KLG Style Mapping Summary

| Pandoc Output Style | KLG Target Style | Context |
|---|---|---|
| `Heading1` | `P1Pleading1` | Always |
| `Heading2` | `P2Pleading2` | Always |
| `Heading3` | `P3Pleading3` | Inside Argument section |
| `Heading3` | Italic BodyText | Inside Statement of Case |
| `FirstParagraph` | `BodyText` | Always |
| `BlockText` | `Quote` (or `BodyText` + indent) | Always |
| `BodyText` | `BodyText` | No change |

## Generating Unique Paragraph IDs

Word requires unique `w14:paraId` and `w14:textId` attributes
on every paragraph. When generating new paragraphs, use a
counter-based scheme:

```python
counter = 0x1000  # Start above any existing IDs
counter += 1
paraid = f"AB{counter:06X}"
textid = f"CD{counter:06X}"
```

The prefix letters (AB, CD) are arbitrary — they just need to
not collide with existing IDs in the template document.
