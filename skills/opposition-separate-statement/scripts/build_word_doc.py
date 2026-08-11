#!/usr/bin/env python3
"""Build the final opposition separate statement Word document.

Inputs:
  - Word shell .docx (the firm's template the user is filling in)
  - Parsed UMFs from PDF (parsed_umfs.json)
  - Parsed Issues from PDF (parsed_issues.json) — optional; if absent, no Issue tables added
  - Parsed Notion responses (notion_umf_responses.json) — optional; if absent, only Phase 1 done
  - Parsed Notion AMFs (notion_amfs.json) — optional

Workflow:
  1. Unpack the .docx using the docx skill's unpack.py
  2. Parse document.xml, identify the UMF table
  3. PHASE 1 — for each UMF in the PDF that doesn't already have a row in the
     shell, create a new row before the closing </w:tbl>
  4. PHASE 2 — if Notion data present:
       a. Fill empty right cells with response + Supporting Evidence: + evidence
       b. Add Issue tables after the UMF table (each with Defendants'
          incorporation language, blank right column)
       c. Add AMF table at the end (each AMF with empty right column)
  5. Repack with --validate false (templates often have broken xref to a .dot)

Usage:
    python build_word_doc.py \
        --shell template.docx \
        --pdf-umfs parsed_umfs.json \
        [--pdf-issues parsed_issues.json] \
        [--notion-umfs notion_umf_responses.json] \
        [--notion-amfs notion_amfs.json] \
        --out output.docx \
        --skill-scripts /path/to/docx-skill/scripts
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from helpers import (
    escape_xml,
    text_to_runs,
    make_paragraphs,
    populated_right_cell,
    empty_right_cell,
    SUPPORTING_EVIDENCE_HEADER,
    find_in_xml,
)


def unpack_docx(shell_path: str, work_dir: Path, docx_skill_scripts: str) -> Path:
    """Run unpack.py from the docx skill against the .docx file."""
    work_dir.mkdir(parents=True, exist_ok=True)
    unpacked = work_dir / "unpacked"
    if unpacked.exists():
        shutil.rmtree(unpacked)
    cmd = [
        sys.executable,
        f"{docx_skill_scripts}/office/unpack.py",
        shell_path,
        str(unpacked),
    ]
    subprocess.run(cmd, check=True)
    return unpacked / "word" / "document.xml"


def repack_docx(unpacked_dir: Path, out_path: str, original_shell: str,
                docx_skill_scripts: str):
    """Run pack.py with --validate false (templates often fail strict validation
    due to broken .dot references on a Windows network drive)."""
    cmd = [
        sys.executable,
        f"{docx_skill_scripts}/office/pack.py",
        str(unpacked_dir),
        out_path,
        "--original",
        original_shell,
        "--validate",
        "false",
    ]
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------------------
# Phase 1: insert UMF rows that aren't already in the shell
# ---------------------------------------------------------------------------

def make_umf_row(umf: dict, cell_width: int = 4711) -> str:
    """Build a UMF row XML: left cell with bookmark + number + tab + fact +
    Supporting Evidence: header + evidence; right cell empty."""
    fact = escape_xml(umf["fact"])
    evidence = escape_xml(umf["evidence"])
    num = umf["num"]
    return f'''<w:tr w:rsidR="00000000" w14:paraId="00000{num:03d}" w14:textId="77777777">
    <w:tc>
      <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
      <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
        <w:pPr>
          <w:pStyle w:val="BodyText"/>
          <w:spacing w:line="240" w:lineRule="auto"/>
          <w:ind w:firstLine="0"/>
        </w:pPr>
        <w:bookmarkStart w:id="{num}" w:name="UMF{num}"/>
        <w:r><w:t>{num}</w:t></w:r>
        <w:bookmarkEnd w:id="{num}"/>
        <w:r><w:t>.</w:t><w:tab/><w:t xml:space="preserve">{fact}</w:t></w:r>
      </w:p>
      {SUPPORTING_EVIDENCE_HEADER}
      <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
        <w:pPr>
          <w:pStyle w:val="BodyText"/>
          <w:spacing w:line="240" w:lineRule="auto"/>
          <w:ind w:firstLine="0"/>
        </w:pPr>
        <w:r><w:t xml:space="preserve">{evidence}</w:t></w:r>
      </w:p>
    </w:tc>
    <w:tc>
      <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
      <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
        <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>
      </w:p>
    </w:tc>
  </w:tr>
'''


def find_umf_table_close(doc: str, last_existing_umf: int) -> int:
    """Find the </w:tbl> that closes the UMF table by looking after the last
    existing UMF bookmark."""
    if last_existing_umf == 0:
        # No existing UMFs — caller should have hard-stopped before reaching here
        return -1
    anchor = f'<w:bookmarkStart w:id="{last_existing_umf}" w:name="UMF{last_existing_umf}"/>'
    idx = doc.find(anchor)
    if idx < 0:
        # Try without explicit ID (sometimes IDs differ)
        anchor = f'w:name="UMF{last_existing_umf}"'
        idx = doc.find(anchor)
    if idx < 0:
        return -1
    return doc.find("</w:tbl>", idx)


def detect_existing_umfs_in_doc(doc: str) -> set:
    """Detect UMF numbers already present in the Word shell. Look at both:
      (a) bookmark anchors `w:name="UMFN"`, and
      (b) non-bookmarked rows that start their left cell with `N. <text>` —
          common when the user typed the row by hand without explicit bookmarks.
    """
    bookmarked = set(int(b) for b in re.findall(r'w:name="UMF(\d+)"', doc))
    # Pattern: <w:r><w:t>N</w:t>...<w:t>.</w:t> or <w:t xml:space="preserve">N. </w:t>
    # Look for pattern of <w:t>NUMBER</w:t><w:t>.</w:t> right after a bookmark or at start of paragraph
    # Simpler heuristic: look for cell text starting with "N. " where N is plausible UMF number
    inline = set()
    for m in re.finditer(r'<w:t[^>]*>(\d{1,3})\.\s*</w:t>', doc):
        n = int(m.group(1))
        if 1 <= n <= 200:
            inline.add(n)
    # Also look for split form: <w:t>N</w:t>... <w:t>. </w:t>
    for m in re.finditer(r'<w:t[^>]*>(\d{1,3})</w:t>\s*(?:<w:bookmarkEnd[^/]+/>)?\s*<w:r[^>]*>\s*<w:t[^>]*>\.\s*</w:t>', doc):
        n = int(m.group(1))
        if 1 <= n <= 200:
            inline.add(n)
    return bookmarked | inline


def phase1_add_umf_rows(doc: str, pdf_umfs: list) -> str:
    """Insert rows for any UMFs in the PDF that aren't already in the shell."""
    existing = detect_existing_umfs_in_doc(doc)
    # For finding the UMF table close, use only BOOKMARKED UMFs (anchors).
    # Inline-detected numbers may be in body prose like 'Issue 9 incorporates
    # UMFs 1-3, 21-48, and 55-57' which would mislead find_umf_table_close.
    bookmarked = set(int(b) for b in re.findall(r'w:name="UMF(\d+)"', doc))
    last_bookmarked = max(bookmarked) if bookmarked else 0
    to_add = [u for u in pdf_umfs if u["num"] not in existing]
    if not to_add:
        print(f"Phase 1: all {len(pdf_umfs)} UMFs already present, no rows added")
        return doc

    rows_xml = "".join(make_umf_row(u) for u in to_add)
    tbl_close = find_umf_table_close(doc, last_bookmarked) if last_bookmarked else -1
    if tbl_close < 0:
        # Fallback: find the first table that contains 'Moving Party' header
        marker = doc.find("Moving Party")
        if marker > 0:
            tbl_close = doc.find("</w:tbl>", marker)
    if tbl_close < 0:
        raise RuntimeError("Cannot find UMF table close — shell structure unrecognized")

    new_doc = doc[:tbl_close] + rows_xml + doc[tbl_close:]
    print(f"Phase 1: added {len(to_add)} UMF rows (UMFs {[u['num'] for u in to_add[:3]]}…)")
    return new_doc


# ---------------------------------------------------------------------------
# Phase 2a: fill empty right cells with Notion responses
# ---------------------------------------------------------------------------

def phase2a_fill_responses(doc: str, notion_umfs: dict) -> str:
    if not notion_umfs:
        return doc
    existing = set(int(b) for b in re.findall(r'w:name="UMF(\d+)"', doc))
    filled = 0
    for num in sorted(existing):
        key = str(num)
        if key not in notion_umfs:
            continue
        response = notion_umfs[key].get("plaintiff_response", "")
        evidence = notion_umfs[key].get("plaintiff_evidence", "")
        if not response and not evidence:
            continue

        anchor = f'<w:bookmarkStart w:id="{num}" w:name="UMF{num}"/>'
        idx = doc.find(anchor)
        if idx < 0:
            anchor = f'w:name="UMF{num}"'
            idx = doc.find(anchor)
            if idx < 0:
                continue
        left_close = doc.find("</w:tc>", idx)
        right_start = doc.find("<w:tc>", left_close + len("</w:tc>"))
        right_close = doc.find("</w:tc>", right_start)
        if right_start < 0 or right_close < 0:
            continue

        # Skip if right cell already has substantive content (user manually filled)
        right_cell = doc[right_start:right_close]
        text_pieces = re.findall(r"<w:t[^>]*>([^<]+)</w:t>", right_cell)
        existing_text = "".join(text_pieces).strip()
        if len(existing_text) > 5:
            # Right cell has user content — don't overwrite (caller should have hard-stopped)
            continue

        new_cell = populated_right_cell(response, evidence)
        doc = doc[:right_start] + new_cell + doc[right_close + len("</w:tc>"):]
        filled += 1

    print(f"Phase 2a: filled {filled} right cell(s) from Notion")
    return doc


# ---------------------------------------------------------------------------
# Phase 2b: insert Issue tables after the UMF table
# ---------------------------------------------------------------------------

def make_issue_section(issue: dict, cell_width: int = 4711) -> str:
    title = escape_xml(issue["heading"])
    umfs = escape_xml(issue["umfs"])
    ev_umfs = escape_xml(issue.get("evidence_umfs") or issue["umfs"])
    incorp = f"Defendants hereby incorporate by reference Undisputed Facts Nos. {umfs}."
    ev_incorp = f"Defendants incorporate herein by reference all evidence cited in support of Undisputed Facts Nos. {ev_umfs}."

    heading = f'''<w:p w:rsidR="00000000" w:rsidRDefault="00000000">
      <w:pPr>
        <w:pStyle w:val="BodyText"/>
        <w:spacing w:before="240" w:after="240" w:line="240" w:lineRule="auto"/>
        <w:ind w:firstLine="0"/>
        <w:jc w:val="center"/>
        <w:rPr><w:b/><w:bCs/></w:rPr>
      </w:pPr>
      <w:r><w:rPr><w:b/><w:bCs/></w:rPr>
        <w:t>ISSUE {issue["num"]}: {title}</w:t>
      </w:r>
    </w:p>'''

    return f'''{heading}
    <w:tbl>
      <w:tblPr>
        <w:tblStyle w:val="TableGrid"/>
        <w:tblW w:w="0" w:type="auto"/>
        <w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
      </w:tblPr>
      <w:tblGrid>
        <w:gridCol w:w="{cell_width}"/>
        <w:gridCol w:w="{cell_width}"/>
      </w:tblGrid>
      <w:tr w:rsidR="00000000">
        <w:tc>
          <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>
            <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Moving Party&#x2019;s Undisputed Material Facts and Supporting Evidence:</w:t></w:r>
          </w:p>
        </w:tc>
        <w:tc>
          <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>
            <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Opposing Party&#x2019;s Response and Supporting Evidence:</w:t></w:r>
          </w:p>
        </w:tc>
      </w:tr>
      <w:tr w:rsidR="00000000">
        <w:tc>
          <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>
            <w:r><w:t>{escape_xml(incorp)}</w:t></w:r>
          </w:p>
          {SUPPORTING_EVIDENCE_HEADER}
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>
            <w:r><w:t>{escape_xml(ev_incorp)}</w:t></w:r>
          </w:p>
        </w:tc>
        {empty_right_cell(cell_width)}
      </w:tr>
    </w:tbl>
    <w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>
'''


def phase2b_add_issues(doc: str, pdf_issues: list) -> str:
    if not pdf_issues:
        return doc
    # Find UMF table close (after the last UMF row)
    existing = sorted(set(int(b) for b in re.findall(r'w:name="UMF(\d+)"', doc)))
    if not existing:
        print("Phase 2b: skipping — no UMF rows present")
        return doc
    tbl_close = find_umf_table_close(doc, existing[-1])
    if tbl_close < 0:
        return doc
    insertion_point = tbl_close + len("</w:tbl>")
    issues_xml = "".join(make_issue_section(iss) for iss in pdf_issues)
    new_doc = doc[:insertion_point] + "\n    " + issues_xml + doc[insertion_point:]
    print(f"Phase 2b: inserted {len(pdf_issues)} Issue section(s)")
    return new_doc


# ---------------------------------------------------------------------------
# Phase 2c: AMF table
# ---------------------------------------------------------------------------

def make_amf_row(num: int, fact: str, evidence: str, cell_width: int = 4711) -> str:
    fact_paras = make_paragraphs(fact)
    evidence_paras = make_paragraphs(evidence)
    return f'''<w:tr w:rsidR="00000000">
    <w:tc>
      <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
      <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
        <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>
        <w:bookmarkStart w:id="{1000 + num}" w:name="AMF{num}"/>
        <w:r><w:t>{num}</w:t></w:r>
        <w:bookmarkEnd w:id="{1000 + num}"/>
        <w:r><w:t xml:space="preserve">. </w:t></w:r>
        {text_to_runs(fact.split(chr(10))[0]) if fact else ''}
      </w:p>
      {make_paragraphs(chr(10).join(fact.split(chr(10))[1:])) if chr(10) in fact else ''}
      {SUPPORTING_EVIDENCE_HEADER}
      {evidence_paras}
    </w:tc>
    {empty_right_cell(cell_width)}
  </w:tr>'''


def phase2c_add_amf_table(doc: str, notion_amfs: dict, after_marker_text: str = None) -> str:
    if not notion_amfs:
        return doc

    heading = '''<w:p w:rsidR="00000000" w:rsidRDefault="00000000">
      <w:pPr>
        <w:pStyle w:val="BodyText"/>
        <w:spacing w:before="240" w:after="240" w:line="240" w:lineRule="auto"/>
        <w:ind w:firstLine="0"/>
        <w:jc w:val="center"/>
        <w:rPr><w:b/><w:bCs/></w:rPr>
      </w:pPr>
      <w:r><w:rPr><w:b/><w:bCs/></w:rPr>
        <w:t>PLAINTIFF&#x2019;S ADDITIONAL MATERIAL FACTS</w:t>
      </w:r>
    </w:p>'''

    cell_width = 4711
    rows = []
    for num in sorted(int(k) for k in notion_amfs.keys()):
        amf = notion_amfs[str(num)]
        rows.append(make_amf_row(num, amf.get("fact", ""), amf.get("evidence", "")))

    table = f'''{heading}
    <w:tbl>
      <w:tblPr>
        <w:tblStyle w:val="TableGrid"/>
        <w:tblW w:w="0" w:type="auto"/>
        <w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
      </w:tblPr>
      <w:tblGrid>
        <w:gridCol w:w="{cell_width}"/>
        <w:gridCol w:w="{cell_width}"/>
      </w:tblGrid>
      <w:tr w:rsidR="00000000">
        <w:tc>
          <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>
            <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Plaintiff&#x2019;s Additional Material Facts and Supporting Evidence:</w:t></w:r>
          </w:p>
        </w:tc>
        <w:tc>
          <w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>
          <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
            <w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>
            <w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t>Defendants&#x2019; Response and Supporting Evidence:</w:t></w:r>
          </w:p>
        </w:tc>
      </w:tr>
      {''.join(rows)}
    </w:tbl>
    <w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>
'''

    # Insert after last Issue table close (or at end of body)
    if after_marker_text:
        marker_idx = find_in_xml(doc, after_marker_text)
        if marker_idx >= 0:
            tbl_close = doc.find("</w:tbl>", marker_idx)
            spacer = doc.find('<w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>', tbl_close)
            if spacer >= 0:
                end = spacer + len('<w:p w:rsidR="00000000" w:rsidRDefault="00000000"/>')
                return doc[:end] + "\n    " + table + doc[end:]

    # Fallback: insert before </w:body>
    body_close = doc.rfind("</w:body>")
    return doc[:body_close] + "\n    " + table + doc[body_close:]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shell", required=True, help="Word shell .docx")
    ap.add_argument("--pdf-umfs", required=True)
    ap.add_argument("--pdf-issues", default=None)
    ap.add_argument("--notion-umfs", default=None)
    ap.add_argument("--notion-amfs", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--work-dir", default="./build_work")
    ap.add_argument("--skill-scripts", required=True,
                    help="Path to docx skill scripts dir (containing office/unpack.py and office/pack.py)")
    args = ap.parse_args()

    work = Path(args.work_dir)
    doc_xml_path = unpack_docx(args.shell, work, args.skill_scripts)

    pdf_umfs = json.loads(Path(args.pdf_umfs).read_text(encoding="utf-8"))
    pdf_issues = json.loads(Path(args.pdf_issues).read_text(encoding="utf-8")) if args.pdf_issues else None
    notion_umfs = json.loads(Path(args.notion_umfs).read_text(encoding="utf-8")) if args.notion_umfs else None
    notion_amfs = json.loads(Path(args.notion_amfs).read_text(encoding="utf-8")) if args.notion_amfs else None

    doc = doc_xml_path.read_text(encoding="utf-8")

    # Phase 1: ensure all UMFs from PDF have rows
    doc = phase1_add_umf_rows(doc, pdf_umfs)

    # Phase 2a: fill responses from Notion
    if notion_umfs:
        doc = phase2a_fill_responses(doc, notion_umfs)

    # Phase 2b: Issue tables
    last_issue_marker = None
    if pdf_issues:
        doc = phase2b_add_issues(doc, pdf_issues)
        # Save the last Issue's heading text (using literal Unicode apostrophe)
        # so we can find where to insert the AMF table
        if pdf_issues:
            last = pdf_issues[-1]
            # Use the actual heading text as it appears in the doc
            last_issue_marker = f"ISSUE {last['num']}: {last['heading']}"

    # Phase 2c: AMF table
    if notion_amfs:
        doc = phase2c_add_amf_table(doc, notion_amfs, after_marker_text=last_issue_marker)

    doc_xml_path.write_text(doc, encoding="utf-8")
    repack_docx(doc_xml_path.parent.parent, args.out, args.shell, args.skill_scripts)
    print(f"\n✅ Built: {args.out}")


if __name__ == "__main__":
    main()
