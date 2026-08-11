#!/usr/bin/env python3
"""Extract Issue 1-N section headings + the "Defendants hereby incorporate by
reference Undisputed Facts Nos. X, Y, Z" language from a moving party's PDF.

Each Issue in a CRC 3.1350(d) separate statement has:
  - A bold all-caps heading spanning the page width (e.g. "ISSUE 1: PLAINTIFF'S
    CLAIMS ARE BARRED BECAUSE PLAINTIFF FAILED TO EXHAUST...")
  - A 2-column table whose left cell says "Defendants hereby incorporate by
    reference Undisputed Facts Nos. X, Y, Z" and "Supporting Evidence:
    Defendants incorporate herein by reference all evidence cited in support of
    Undisputed Facts Nos. X, Y, Z"

This script extracts both pieces for each Issue.

Usage:
    python extract_issues_from_pdf.py path/to/movant_separate_statement.pdf [--out parsed_issues.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed.", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from klg_style import klg_style_normalize


# Wider crop than UMF extraction since Issue headings span both columns
DEFAULT_LEFT = 100
DEFAULT_RIGHT = 540
DEFAULT_TOP = 50
DEFAULT_BOTTOM = 720


def extract_full_width_text(pdf_path: str, left, right, top, bottom) -> str:
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            cropped = page.crop((left, top, right, bottom))
            chunks.append(cropped.extract_text() or "")
    return "\n".join(chunks)


def parse_issues(text: str) -> list:
    """Find all 'ISSUE N:' blocks and extract heading + UMF list + evidence list."""
    # Locate each Issue's start
    starts = [(m.start(), int(m.group(1))) for m in re.finditer(r"ISSUE (\d+):", text)]
    starts.append((len(text), None))

    issues = []
    for i in range(len(starts) - 1):
        start_idx, num = starts[i]
        end_idx = starts[i + 1][0]
        block = text[start_idx:end_idx]

        # Clean: collapse whitespace, remove line numbers, strip line breaks
        block = re.sub(r"\n\s*\d+\s*", " ", block)  # remove embedded line numbers
        block = re.sub(r"\s+", " ", block).strip()

        # Find heading: "ISSUE N: <heading>" up to "MOVING PARTY"
        heading_m = re.match(r"ISSUE \d+:\s*(.*?)\s*MOVING PARTY", block)
        heading = heading_m.group(1).strip() if heading_m else ""

        # Find UMF incorporation list
        umf_m = re.search(
            r"Defendants hereby incorporate by reference Undisputed Facts Nos\.\s*([^.]+?)\.\s*Supporting Evidence",
            block,
        )
        umfs = umf_m.group(1).strip() if umf_m else ""

        # Find evidence incorporation list
        ev_m = re.search(
            r"Defendants incorporate herein by reference all evidence cited in support of Undisputed Facts Nos\.\s*([^.]+?)\.",
            block,
        )
        evidence_umfs = ev_m.group(1).strip() if ev_m else umfs

        # Fix PDF wrap-induced gaps in number ranges (e.g., '37- 50' → '37-50')
        umfs = re.sub(r"(\d)-\s+(\d)", r"\1-\2", umfs)
        evidence_umfs = re.sub(r"(\d)-\s+(\d)", r"\1-\2", evidence_umfs)

        issues.append({
            "num": num,
            "heading": klg_style_normalize(heading),
            "umfs": umfs,
            "evidence_umfs": evidence_umfs,
        })
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", default="parsed_issues.json")
    ap.add_argument("--left", type=int, default=DEFAULT_LEFT)
    ap.add_argument("--right", type=int, default=DEFAULT_RIGHT)
    ap.add_argument("--top", type=int, default=DEFAULT_TOP)
    ap.add_argument("--bottom", type=int, default=DEFAULT_BOTTOM)
    args = ap.parse_args()

    text = extract_full_width_text(args.pdf, args.left, args.right, args.top, args.bottom)
    issues = parse_issues(text)

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(issues)} Issues → {args.out}")
    for iss in issues:
        print(f"  Issue {iss['num']}: incorporates UMFs {iss['umfs']!r}")


if __name__ == "__main__":
    main()