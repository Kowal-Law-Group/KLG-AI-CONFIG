# Word XML patterns

Reference XML structures the build script must produce or match. All cell widths default to 4711 DXA (about 3.27 inches), which gives a balanced two-column layout on US Letter with 1-inch margins. Override if the firm's template uses different widths.

## 1. UMF row (left cell populated, right cell empty)

```xml
<w:tr w:rsidR="00000000" w14:paraId="00000XXX" w14:textId="77777777">
  <w:tc>
    <w:tcPr><w:tcW w:w="4711" w:type="dxa"/></w:tcPr>
    <w:p>
      <w:pPr>
        <w:pStyle w:val="BodyText"/>
        <w:spacing w:line="240" w:lineRule="auto"/>
        <w:ind w:firstLine="0"/>
      </w:pPr>
      <w:bookmarkStart w:id="N" w:name="UMFN"/>
      <w:r><w:t>N</w:t></w:r>
      <w:bookmarkEnd w:id="N"/>
      <w:r>
        <w:t>.</w:t>
        <w:tab/>
        <w:t xml:space="preserve">FACT TEXT...</w:t>
      </w:r>
    </w:p>
    <!-- Bold "Supporting Evidence:" header -->
    <w:p>
      <w:pPr>...</w:pPr>
      <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Supporting Evidence:</w:t></w:r>
    </w:p>
    <!-- Evidence text -->
    <w:p>
      <w:pPr>...</w:pPr>
      <w:r><w:t>EVIDENCE TEXT...</w:t></w:r>
    </w:p>
  </w:tc>
  <w:tc>  <!-- Empty right cell -->
    <w:tcPr><w:tcW w:w="4711" w:type="dxa"/></w:tcPr>
    <w:p><w:pPr>...</w:pPr></w:p>
  </w:tc>
</w:tr>
```

The bookmark MUST be present — it's the anchor for finding rows in subsequent operations.

## 2. Right cell populated (Plaintiff's response + evidence)

```xml
<w:tc>
  <w:tcPr><w:tcW w:w="4711" w:type="dxa"/></w:tcPr>
  <!-- Response text — possibly multi-paragraph; convert *italic* and **bold** -->
  <w:p>
    <w:pPr>...</w:pPr>
    <w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t>italic part</w:t></w:r>
    <w:r><w:t> normal part</w:t></w:r>
  </w:p>
  <!-- Bold "Supporting Evidence:" header -->
  <w:p>
    <w:pPr>...<w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>
    <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Supporting Evidence:</w:t></w:r>
  </w:p>
  <!-- Evidence text -->
  <w:p>
    <w:pPr>...</w:pPr>
    <w:r><w:t>EVIDENCE TEXT...</w:t></w:r>
  </w:p>
</w:tc>
```

## 3. Issue heading (centered bold all-caps, full page width)

```xml
<w:p>
  <w:pPr>
    <w:pStyle w:val="BodyText"/>
    <w:spacing w:before="240" w:after="240" w:line="240" w:lineRule="auto"/>
    <w:ind w:firstLine="0"/>
    <w:jc w:val="center"/>
    <w:rPr><w:b/><w:bCs/></w:rPr>
  </w:pPr>
  <w:r>
    <w:rPr><w:b/><w:bCs/></w:rPr>
    <w:t>ISSUE N: HEADING TEXT IN ALL CAPS</w:t>
  </w:r>
</w:p>
```

## 4. Issue table (2-column with header row + content row)

Same structure as the UMF table but with only one content row per Issue. Left cell has the "Defendants hereby incorporate by reference Undisputed Facts Nos. X, Y, Z." text + bold "Supporting Evidence:" header + the matching evidence-incorporation language. Right cell is blank.

After the table, include a spacer paragraph: `<w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>`.

## 5. AMF row (similar to UMF row, but bookmarked AMFN)

```xml
<w:tr>
  <w:tc>
    <w:tcPr><w:tcW w:w="4711" w:type="dxa"/></w:tcPr>
    <w:p>
      <w:pPr>...</w:pPr>
      <w:bookmarkStart w:id="1XXX" w:name="AMFN"/>
      <w:r><w:t>N</w:t></w:r>
      <w:bookmarkEnd w:id="1XXX"/>
      <w:r><w:t xml:space="preserve">. </w:t></w:r>
      <!-- AMF fact text (may include italic title at start) -->
      <w:r><w:rPr><w:i/></w:rPr><w:t>Italic subtitle</w:t></w:r>
    </w:p>
    <!-- Continuation paragraphs of fact text -->
    <w:p>...</w:p>
    <!-- Bold Supporting Evidence header -->
    <w:p>...</w:p>
    <!-- Evidence text -->
    <w:p>...</w:p>
  </w:tc>
  <w:tc>  <!-- Empty right cell — Defendants haven't responded yet -->
    <w:tcPr>...</w:tcPr>
    <w:p>...</w:p>
  </w:tc>
</w:tr>
```

Use bookmark IDs in the 1000+ range for AMFs (e.g., AMF 13 → id="1013") so they don't collide with UMF ids.

## 6. Table-level wrapping

Each new table needs:

```xml
<w:tbl>
  <w:tblPr>
    <w:tblStyle w:val="TableGrid"/>
    <w:tblW w:w="0" w:type="auto"/>
    <w:tblLook w:val="04A0" .../>
  </w:tblPr>
  <w:tblGrid>
    <w:gridCol w:w="4711"/>
    <w:gridCol w:w="4711"/>
  </w:tblGrid>
  <!-- header row + content rows -->
</w:tbl>
<w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>  <!-- spacer after table -->
```

The spacer paragraph after the table is important: it prevents subsequent content from being absorbed into the table layout in some Word versions.

## 7. Where to insert each piece

| Phase | Insertion target |
|-------|------------------|
| New UMF rows | Just before the `</w:tbl>` of the existing UMF table |
| Right-cell fill | Replace the empty right cell of an existing UMF row |
| Issue tables | After the UMF table's closing `</w:tbl>` |
| AMF table | After the last Issue table's closing `</w:tbl>` (with its spacer paragraph) |

If no Issue tables are present, the AMF table goes immediately after the UMF table.

## 8. Cell content rules

- Each `<w:p>` inside a cell becomes a separate paragraph.
- Use `<w:tab/>` to insert a tab, e.g., between the UMF number and fact text.
- Use `<w:br/>` for a soft line break within a paragraph (rare; usually a new `<w:p>` is better).
- `<w:r>` runs can have `<w:rPr>` for formatting (bold, italic, font, color, etc.).
- If a `<w:t>` element contains leading/trailing whitespace, add `xml:space="preserve"`.
