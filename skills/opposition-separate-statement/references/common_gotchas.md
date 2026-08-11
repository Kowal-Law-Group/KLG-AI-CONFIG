# Common gotchas

These are the non-obvious technical pitfalls that took an hour to debug the first time. Read this before generating any XML changes.

## 1. Search XML by literal Unicode characters, not by entities

When searching `document.xml` for an anchor or marker text that contains smart apostrophes/quotes, search for the **literal Unicode character**, not the XML entity.

**Wrong:**

```python
marker = 'ISSUE 9: PLAINTIFF&#x2019;S CAUSE OF ACTION'  # entity
idx = doc.find(marker)  # returns -1
```

**Right:**

```python
marker = 'ISSUE 9: PLAINTIFF’S CAUSE OF ACTION'  # literal Unicode
# or simply: marker = 'ISSUE 9: PLAINTIFF’S CAUSE OF ACTION'
idx = doc.find(marker)  # returns the offset
```

Why: the docx skill's `unpack.py` script preserves Unicode characters as literal UTF-8 bytes in the unpacked XML, not as `&#x2019;` entities. If you write the entity form into your search string, `find()` returns -1, and downstream insertion logic silently inserts at offset `-1 + len(pattern)` — which is somewhere inside the document head — corrupting the document.

The `find_in_xml()` helper in `helpers.py` tries both forms as a safety net. Use it when in doubt.

## 2. Pack with `--validate false`

Pleading templates created from a Word `.dot` file on a network drive almost always have a stale relationship pointing to a path like `file:///L:\Lynne\TVA%20PLEADING%20TEMPLATE%20-%20California.dot`. This relationship doesn't affect Word's ability to open the document, but the docx skill's strict validation rejects it.

**Always pass `--validate false` to `pack.py`** when working with these templates. The output `.docx` opens correctly in Word; the broken `.dot` reference is harmless.

## 3. Use bookmark anchors, not text content, to find rows

Each UMF row should be anchored by `<w:bookmarkStart w:id="N" w:name="UMFN"/>`. Find rows by bookmark name. Why:

- Content text changes over time (the user edits a UMF's fact).
- Bookmark names are stable and unique.
- `w:name="UMFN"` is the canonical identifier.

When inserting new UMF rows, always include a bookmark so future runs can find them.

## 4. Sequential UMF detection — state machine, not regex match

A naïve regex `r"\n(\d+)\.\s"` will match wrap-induced lines like:

```
…the Notice was reissued on August 16,
2017.
```

It'll think "2017." is the start of UMF 2017. Use the state-machine approach in `helpers.py` `detect_sequential_items()`: walk lines, track `expected_next` (starts at 1), only treat a line as a new UMF if its number equals `expected_next`. Otherwise, treat the line as continuation of the current UMF.

## 5. Column cropping coordinates for California pleading paper

For standard California pleading paper with line numbers 1–28 in the left margin and a centered footer:

- **Left column body:** x = 100 to 340, y = 50 to 720
- **Full page width** (for Issue headings): x = 100 to 540

These work for letter-size (612×792 pt) PDFs. If the firm uses different margins, override via the `--left/--right/--top/--bottom` flags on `extract_umfs_from_pdf.py`.

## 6. The right column of a moving party's separate statement is empty

In a moving-party-only separate statement, the right column ("Opposing Party's Response and Supporting Evidence") is empty. So when you crop the LEFT column, you get all the substantive content. The wrap-induced indentation in the layout text is just paragraph wrapping inside the left cell, not actual content in the right column.

## 7. Combined responses → duplicate text, don't merge cells

When the Notion has "Combined response with UMFs 13-15" or "Combined response with UMF 52", duplicate the response text into all rows of the group rather than merging cells. Reasons:

- Cell-merging in pleading templates is fragile (alignment can break on subsequent edits).
- Duplicating preserves a clean row-by-row correspondence with the moving party's row count, which is what California courts expect.
- The user-confirmed preference is duplicate.

The Notion parser handles this automatically — it copies the primary response from the lowest-numbered group member into every other member's JSON entry.

## 8. Italic markdown → Word italic; bold markdown → Word bold

Notion exports use `*italic*` and `**bold**` markers. The `text_to_runs()` helper in `helpers.py` is a state machine that converts these into separate `<w:r>` runs with `<w:i/>` or `<w:b/>` formatting. **Don't** strip the markers; **don't** insert them as literal asterisks. They have to become OOXML run properties.

## 9. Smart quotes preserved as XML entities (when WRITING new XML)

When generating new XML to insert, write smart quotes as XML entities:

- `&#x2018;` for ‘ (left single)
- `&#x2019;` for ’ (right single / apostrophe)
- `&#x201C;` for “ (left double)
- `&#x201D;` for ” (right double)

The `escape_xml()` helper does this automatically. This is the inverse of gotcha #1: when *searching* the doc, use literal Unicode (because that's what's in the file); when *writing* new XML, use entities (because that's safer across editors).

## 10. Validate after each insertion phase

After each phase (Phase 1, 2a, 2b, 2c), parse the XML to confirm it's still well-formed:

```python
import xml.etree.ElementTree as ET
ET.parse('unpacked/word/document.xml')
```

If validation fails, the offset for the next insertion is no longer reliable. Stop, debug, fix.

## 11. The user's original file may be open in Word — don't try to overwrite

If the user has the .docx open in Word, the OS will deny write permission to the destination. Save the output as a fresh copy with a different filename (e.g., add `(Updated)` or a date stamp). The user can replace the original later when they close Word.
