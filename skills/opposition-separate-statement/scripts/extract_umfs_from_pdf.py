#!/usr/bin/env python3
"""Extract Undisputed Material Facts (UMFs) from a California moving party's
Separate Statement PDF.

The PDF uses the standard 2-column California pleading paper format: line
numbers 1-28 in the left margin, a firm-name watermark on the left side, a
centered "DEFENDANTS' SEPARATE STATEMENT…" footer, and content in two columns
(left = moving party UMFs, right = opposing party response — usually empty in
the moving party's filing).

Strategy:
1. Crop each page to the LEFT-COLUMN content area (x ≈ 100–340, y ≈ 50–720)
   to skip line numbers, the firm watermark, and the right column.
2. Strip orphaned line numbers, the firm-name watermark, page footers, and
   REF codes line by line.
3. Walk the cleaned text with a sequential-number state machine: a line that
   starts with the *next expected* UMF number + "." starts a new UMF. This
   avoids false positives where a wrapped date like "August 16, 2017." would
   otherwise look like the start of UMF 2017.
4. Within each UMF, split on "Supporting Evidence:" to separate the fact text
   from the evidence citations.

Usage:
    python extract_umfs_from_pdf.py path/to/movant_separate_statement.pdf [--out parsed_umfs.json]

Output: JSON list of {"num": int, "fact": str, "evidence": str}.
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Run: pip install pdfplumber --break-system-packages", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from helpers import detect_sequential_items
from klg_style import klg_style_normalize


# Standard column-cropping coordinates for California pleading paper.
# Override via --left/--right/--top/--bottom if a particular firm uses different margins.
DEFAULT_LEFT = 100   # skip line numbers (which sit around x=60-95)
DEFAULT_RIGHT = 340  # right edge of left column
DEFAULT_TOP = 50     # skip top header
DEFAULT_BOTTOM = 720 # skip bottom footer


def extract_left_column_text(pdf_path: str, left: int, right: int,
                             top: int, bottom: int) -> str:
    """Pull the left-column text from every page and join."""
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            cropped = page.crop((left, top, right, bottom))
            chunks.append(cropped.extract_text() or "")
    return "\n".join(chunks)


def clean_lines(text: str, firm_watermark: str = None) -> str:
    """Remove orphan line numbers, firm watermark, page footers, REF codes.

    `firm_watermark` is the stylized firm name that appears as a vertical
    watermark on the left side (e.g., "DAVID WEISS LAW"). If None, we just
    strip common ones.
    """
    cleaned = []
    common_watermarks = {
        "DAVID WEISS LAW",
        # add more known watermarks here as we encounter them
    }
    if firm_watermark:
        common_watermarks.add(firm_watermark.upper())

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Skip lone line numbers (1, 2, 10, 28, etc.)
        if re.match(r"^\d{1,2}$", line):
            continue
        # Skip firm watermark
        if line in common_watermarks:
            continue
        # Skip the standard footer
        if "DEFENDANTS’ SEPARATE STATEMENT" in line or "DEFENDANTS' SEPARATE STATEMENT" in line:
            continue
        if line == "MOTION FOR SUMMARY JUDGMENT/ADJUDICATION":
            continue
        # Skip REF codes (printer reference numbers, e.g., REF46-09053)
        if re.match(r"^REF\d+", line):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def find_table_start(text: str) -> int:
    """Find where the first UMF starts. Look for the most distinctive UMF 1
    pattern: '1. ' followed by a capital letter at start of line."""
    # Common starts
    for marker in ("1. On ", "1. The ", "1. Plaintiff ", "1. Defendant "):
        idx = text.find(marker)
        if idx >= 0:
            return idx
    # Fallback: just find the first instance of "1. <Capital>"
    m = re.search(r"^1\.\s+[A-Z]", text, re.MULTILINE)
    return m.start() if m else 0


def find_table_end(text: str) -> int:
    """Find where the UMF table ends (before signature block / Issues section)."""
    # Look for signature block patterns
    for marker in ("\nDated:", "\nRespectfully submitted", "\nDATED:"):
        idx = text.find(marker)
        if idx > 0:
            return idx
    # Look for Issues section (some moving parties put Issues right after UMFs)
    issues_idx = text.find("ISSUE 1:")
    if issues_idx > 0:
        return issues_idx
    return len(text)


def parse_umfs(text: str) -> list:
    """Walk the cleaned text, identifying UMFs and splitting fact from evidence."""
    table = text[find_table_start(text):find_table_end(text)]

    # Strip per-page repeated column headers
    table = re.sub(
        r"MOVING PARTY[’']S UNDISPUTED.*?SUPPORTING EVIDENCE\n",
        "",
        table,
    )
    # Some PDFs split the header across lines like "MOVING PARTY'S UNDISPUTED OP\nMATERIAL FACTS AND SUP\nSUPPORTING EVIDENCE\n"
    table = re.sub(
        r"MOVING PARTY[’']S UNDISPUTED OP?\s+MATERIAL FACTS AND SUP?\s+SUPPORTING EVIDENCE\s*",
        "",
        table,
    )

    items = detect_sequential_items(table, start_num=1)

    parsed = []
    for num, content in items:
        if "Supporting Evidence:" in content:
            fact, evidence = content.split("Supporting Evidence:", 1)
        else:
            fact, evidence = content, ""

        # Final clean-up: collapse whitespace, strip header noise
        def clean(t: str) -> str:
            t = re.sub(
                r"\s*MOVING PARTY[’']S UNDISPUTED.*?SUPPORTING EVIDENCE\s*",
                " ",
                t,
            )
            return re.sub(r"\s+", " ", t).strip()

        parsed.append({
            "num": num,
            "fact": klg_style_normalize(clean(fact)),
            "evidence": klg_style_normalize(clean(evidence)),
        })
    return parsed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", default="parsed_umfs.json")
    ap.add_argument("--firm-watermark", default=None,
                    help="Firm-name watermark to strip (uppercase, e.g. 'DAVID WEISS LAW')")
    ap.add_argument("--left", type=int, default=DEFAULT_LEFT)
    ap.add_argument("--right", type=int, default=DEFAULT_RIGHT)
    ap.add_argument("--top", type=int, default=DEFAULT_TOP)
    ap.add_argument("--bottom", type=int, default=DEFAULT_BOTTOM)
    args = ap.parse_args()

    raw = extract_left_column_text(args.pdf, args.left, args.right, args.top, args.bottom)
    cleaned = clean_lines(raw, firm_watermark=args.firm_watermark)
    umfs = parse_umfs(cleaned)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(umfs, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(umfs)} UMFs → {args.out}")
    if umfs:
        print(f"First: UMF {umfs[0]['num']}: {umfs[0]['fact'][:80]}…")
        print(f"Last:  UMF {umfs[-1]['num']}: {umfs[-1]['fact'][:80]}…")


if __name__ == "__main__":
    main()
