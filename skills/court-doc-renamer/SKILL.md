---
name: court-doc-renamer
description: "Rename court documents and legal filings to follow a consistent naming convention: [YYYY-MM-DD] [Abbreviated Title], and OCR scanned PDFs to make them searchable. Use this skill whenever the user asks to rename, organize, clean up, or standardize filenames for court filings, legal documents, case files, litigation documents, or appellate records. Also trigger when users mention 'naming convention', 'file naming', 'rename files', 'OCR', 'make searchable', or 'scanned PDF' in a legal/litigation context, even if they don't say 'court documents' explicitly."
---

# Court Document File Renamer

You are helping a litigation team rename court documents to follow a standardized naming convention and ensure all PDFs are text-searchable. This is important because consistent file names make it much easier to locate documents in a case — especially when assembling appellate records or working in Clearbrief, where chronological ordering by date matters. Many litigation tools (Clearbrief, Westlaw, document review platforms) require searchable text in PDFs to function properly, so scanned documents need to be OCR'd as part of this workflow.

## The Naming Convention

Every filename follows this pattern:

```
[Date] [Abbreviated Title].pdf
```

### Date Format

Use **YYYY-MM-DD** format (e.g., `2024-01-15`). This is the appellate record format and is the default.

If the user specifically requests Clearbrief format, use **Mon. DD, YYYY** instead (e.g., `Jan. 15, 2024`). But unless told otherwise, always default to YYYY-MM-DD.

### Title Abbreviations

Use concise, standard legal abbreviations. The title should be descriptive but not overly verbose. Here are the standard abbreviations:

| Full Title | Abbreviated |
|---|---|
| Complaint for Breach of Contract and Fraud | Compl. |
| First Amended Complaint | FAC |
| Second Amended Complaint | SAC |
| Third Amended Complaint | TAC |
| Answer | Ans. |
| Cross-Complaint | Cross-Compl. |
| First Amended Cross-Complaint | FACC |
| Second Amended Cross-Complaint | SACC |
| Motion to Compel Production of Documents | Mot. to Compel |
| Motion for Summary Judgment | MSJ |
| Motion for Judgment Notwithstanding the Verdict | Mot. for JNOV |
| Motion for New Trial | Mot. for New Tr. |
| Motion for Judgment on the Pleadings | MJOP |
| Motion in Limine | MIL |
| Motion for Sanctions | Mot. for Sanctions |
| Motion to Strike | Mot. to Strike |
| Motion for Leave to Intervene | Mot. for Leave to Intervene |
| Notice of Appeal | Notice of Appeal |
| Plaintiff's Proposed Jury Instructions | Pl. Prop. Jury Instr. |
| Declaration of [Name] | [Last Name] Decl. |
| Minute Order | Min. Order |
| Tentative Ruling | Tentative Ruling |
| Final Ruling | Final Ruling |
| Opposition | Opp. |
| Reply in Support of | Reply ISO |
| Supplemental Brief | Suppl. Br. |
| Demurrer | Demurrer |
| Trial Brief | Trial Br. |
| Brief re [Topic] | Br. re [Topic] |
| Order | Order |
| Plaintiff's | Pl.'s |
| Defendants' / Defendants and Cross-Complainants' | Defs. |
| Ex Parte Application | Ex Parte Appl. |

**General abbreviation principles:**
- "Motion" → "Mot." (except in compound abbreviations like MSJ, MIL, MJOP)
- "Opposition to" → "Opp. to"
- "Reply in Support of" → "Reply ISO"
- "Supplemental" → "Suppl."
- "Declaration" → "Decl."
- "Declarations" → "Decls."
- "Complaint" → "Compl."
- "Plaintiff's" → "Pl.'s"
- "Defendants'" → "Defs."
- "Testimony" → "Test."
- "Brief" → "Br."
- "Application" → "Appl."
- "Objections" → "Objs."
- Keep proper nouns (case names, people's names) intact
- If a title is very long, identify the main part and abbreviate — use good judgment
- End the abbreviated title with a period if the last word is abbreviated (e.g., `Compl.`, `Decl.`) — this means some filenames will have two dots before `.pdf` (like `Compl..pdf`), and that's correct

## OCR for Scanned PDFs

Many court filings arrive as scanned images with no searchable text layer. These are unusable with litigation tools like Clearbrief, Westlaw, and document review platforms. As part of the renaming workflow, detect and OCR these files automatically.

### Detecting scanned PDFs

Use pymupdf (fitz) to check whether a PDF has extractable text. A PDF with little or no text on its first few pages is almost certainly a scanned image:

```python
import fitz

def needs_ocr(pdf_path):
    """Returns True if the PDF has no extractable text (likely scanned)."""
    try:
        doc = fitz.open(pdf_path)
        total_text = ""
        for page_num in range(min(3, len(doc))):
            total_text += doc[page_num].get_text()
        doc.close()
        return len(total_text.strip()) < 50
    except Exception:
        return False
```

### Running OCR

Use pdf2image + pytesseract + pymupdf to convert scanned pages into a searchable PDF that replaces the original:

```python
import os
from pdf2image import convert_from_path
import pytesseract
import fitz

def ocr_pdf(pdf_path):
    """OCR a scanned PDF and replace it with a searchable version."""
    try:
        images = convert_from_path(pdf_path, dpi=300)
        merged = fitz.open()
        for img in images:
            pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
            page_doc = fitz.open("pdf", pdf_bytes)
            merged.insert_pdf(page_doc)
            page_doc.close()

        temp_path = pdf_path + ".ocr_temp"
        merged.save(temp_path)
        merged.close()
        os.replace(temp_path, pdf_path)
        return True
    except Exception:
        if os.path.exists(pdf_path + ".ocr_temp"):
            os.remove(pdf_path + ".ocr_temp")
        return False
```

For large PDFs (over 50 pages), process in batches of 10 pages to avoid memory issues.

### OCR rules

- **Replace the original** — the searchable PDF overwrites the scanned version. Don't create separate `_OCR` copies. The visual appearance is preserved; only a hidden text layer is added.
- **Only OCR files that need it** — skip PDFs that already have extractable text. Most e-filed documents already have text layers.
- **OCR runs before date extraction** — this is important because once a scanned PDF has searchable text, you can extract filing dates, clerk stamps, and other metadata from it. Without OCR, those dates would be invisible to the date extraction step.
- **Use 300 DPI** — this gives reliable OCR results for court documents, which are mostly typed text.
- **Report results** — in the summary, note how many files were OCR'd and flag any that failed.

## Workflow

### Step 1: Scan the folder and OCR scanned PDFs

List all files in the user's selected folder and subfolders. Identify which files need renaming by checking whether they already follow the convention.

A file follows the convention if its name starts with a date in YYYY-MM-DD format followed by a properly abbreviated title. Files that already look correct can be skipped (unless they have issues like missing abbreviation periods, inconsistent abbreviation style, or trailing spaces).

While scanning, also check each PDF to see if it needs OCR (using the `needs_ocr()` function above). Run OCR on any scanned PDFs before proceeding to Step 2 — this ensures date extraction can read text from previously-scanned documents.

### Step 2: Find dates for files that are missing them

Many files will have dates embedded in their existing filenames in various formats:
- `12-7-2021` or `12-7-21` → 2021-12-07
- `7-14-2023` → 2023-07-14
- `Jan 29 2018` or `January 29, 2018` → 2018-01-29
- `July 3, 2019` or `— July 3, 2019` → 2019-07-03
- `Feb 27` (with year context) → need to infer year
- `4-109-25` → likely a typo for `4-10-25` → 2025-04-10

For files with NO date in the filename, use this **date priority hierarchy** when extracting a date from the document itself. This order matters because court documents can contain multiple dates, and the filing date is the one that belongs in the filename:

1. **Filed/Filing date** — Look on the first page for a court clerk's stamp or printed label showing a "Filed" date. This is the most authoritative date and should always be used when available.

   > **CRITICAL: "FILED" vs "RECEIVED" stamps.** California e-filed documents often have TWO separate stamps from the Clerk's office: an **"Electronically RECEIVED"** stamp (the date the document was uploaded to the e-filing system) and an **"Electronically FILED"** stamp (the date the Clerk formally accepted and filed it). These dates can differ by days or even weeks. **Always use the "FILED" date, never the "RECEIVED" date.** The FILED stamp is the official filing date of record. Be especially careful because text extraction tools (like pymupdf) may only pick up one of these stamps — the other may be rendered as an image overlay or header watermark. If you only find a "RECEIVED" date in extracted text, visually inspect the PDF or use OCR on the first page to check for a separate "FILED" stamp before relying on the RECEIVED date.

2. **Case Document List or index** — Check if there's a "Case Document List" or similar index file in the folder that maps documents to dates.
3. **Execution date** — If no filing stamp exists, look for the date the document was signed or executed (often found on the signature page or near the end of the document).
4. **Proof of Service date** — If neither a filing stamp nor execution date is available, use the date from any attached Proof of Service.
5. **Other dates within the document** — For non-court documents (e.g., letters, internal memos, expert reports), it's fine to use dates found elsewhere in the document.
6. **No date found** — If no reliable date can be determined, **do not fabricate a date** and **do not add any placeholder prefix** like `[NO DATE]`. Simply use the cleaned/abbreviated title alone as the filename (e.g., `Cohen Decl..pdf`) and list the file separately in the summary as needing a date. The `[NO DATE]` prefix clutters filenames and makes them harder to sort — a clean title-only name is always preferable.

### Step 3: Show a preview

Before renaming anything, present a clear table showing:
- Current filename → Proposed new filename
- Flag any files you're uncertain about (date unclear, ambiguous title, etc.)
- Flag suspected duplicates (files with the same date and similar titles — compare file sizes and content if possible)

Ask the user to confirm before proceeding.

### Step 4: Rename

After the user confirms, rename the files. Use Python's `os.rename()` for reliability. Handle edge cases:
- Files with special characters (smart quotes, em dashes, parentheses with doc IDs)
- Trailing spaces in filenames
- Files that can't be opened due to encoding issues — still rename based on filename parsing

### Step 5: Flag duplicates

After renaming, check for suspected duplicates:
- Files with the same date and very similar titles (in the same folder or across folders)
- Compare file sizes first — if sizes differ by more than 5%, they're likely different documents (different versions, one may include exhibits)
- If sizes are very close, try to compare content (e.g., extract text from both PDFs)
- Present the findings to the user and let them decide what to do — don't delete anything without explicit permission

### Step 6: Summary

Report what was done:
- How many files were OCR'd (and how many failed OCR, if any)
- How many files were renamed
- How many were already correct and skipped
- Any files that couldn't be processed (with reasons)
- List of suspected duplicates, if any

## Important Notes

- Always preserve the original file extension
- Never rename non-document utility files (like "Case Document List.docx", "Last Numbered.txt", etc.) unless the user specifically asks
- If a file already follows the convention correctly, skip it — don't rename it to the same name
- When a folder contains both a well-named and poorly-named version of the same document, flag them as potential duplicates rather than silently overwriting
- Handle subfolders: scan and rename within subfolders, keeping files in their current location unless the user asks to move them
