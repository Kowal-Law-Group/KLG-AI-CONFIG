#!/usr/bin/env python3
"""
Gate 1 helper for klg-filing-preflight: page-span audit.

Checks a CSV of appendix entries against the actual PDF page counts and
against the set of documents actually cited in the filing draft, so a
human doesn't have to hand-count page spans (the failure mode this
script exists to prevent).

Usage:
    python page_span_audit.py appendix_index.csv --pdfs appendix_dir/ \
        --brief brief.txt

appendix_index.csv columns (header row required):
    document_name,start_page,end_page,pdf_filename

--pdfs is a directory containing the PDFs named in pdf_filename.
--brief is a plain-text (or already-extracted) copy of the filing draft,
used only for a naive citation sweep — this is a first-pass filter, not
a replacement for Gate 1.3's manual extra-record citation sweep.

Exits non-zero if any flag is raised, so it can be used as a simple
pass/fail gate in addition to printing the detail.
"""
import argparse
import csv
import os
import re
import sys

try:
    from pypdf import PdfReader
except ImportError:  # pragma: no cover
    PdfReader = None


def load_index(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_page_spans(rows, pdf_dir):
    problems = []
    for row in rows:
        name = row["document_name"]
        try:
            declared = int(row["end_page"]) - int(row["start_page"]) + 1
        except (KeyError, ValueError):
            problems.append(f"{name}: start_page/end_page missing or not integers")
            continue

        pdf_path = os.path.join(pdf_dir, row.get("pdf_filename", "")) if pdf_dir else None
        if not pdf_path or not os.path.isfile(pdf_path):
            problems.append(f"{name}: no PDF file found to verify against ({row.get('pdf_filename')})")
            continue

        if PdfReader is None:
            problems.append(
                f"{name}: pypdf not installed — cannot verify actual page count "
                f"(declared span: {declared} pages)"
            )
            continue

        try:
            actual = len(PdfReader(pdf_path).pages)
        except Exception as e:  # noqa: BLE001
            problems.append(f"{name}: could not read PDF ({e})")
            continue

        if actual != declared:
            problems.append(
                f"{name}: declared span is {declared} pages "
                f"(start {row['start_page']}, end {row['end_page']}) "
                f"but the PDF has {actual} pages — mismatch"
            )
    return problems


def check_extra_record_citations(rows, brief_path):
    if not brief_path or not os.path.isfile(brief_path):
        return [f"No brief text file provided or found at {brief_path} — skipping citation sweep"]

    with open(brief_path, encoding="utf-8", errors="ignore") as f:
        text = f.read()

    known_names = {row["document_name"].lower() for row in rows}
    # Naive REF-number sweep: flags any "REF######-#####" style cite so a
    # human can eyeball whether each one maps to something in the index.
    # This is intentionally conservative — it does not try to resolve
    # citations automatically, only surfaces the raw list for Gate 1.3.
    ref_cites = sorted(set(re.findall(r"REF\d+-\d+", text)))

    problems = []
    if not ref_cites:
        problems.append(
            "No REF-style citations found in the brief text — if this filing "
            "uses REF citations, check that the text extraction actually "
            "captured them before trusting this result."
        )
    return problems, ref_cites


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index_csv")
    parser.add_argument("--pdfs", default=None, help="Directory containing appendix PDFs")
    parser.add_argument("--brief", default=None, help="Plain-text copy of the filing draft")
    args = parser.parse_args()

    rows = load_index(args.index_csv)
    print(f"Loaded {len(rows)} appendix entries from {args.index_csv}\n")

    span_problems = check_page_spans(rows, args.pdfs)
    print("=== Page-span audit ===")
    if span_problems:
        for p in span_problems:
            print(f"  FLAG: {p}")
    else:
        print("  No page-span mismatches found.")

    print("\n=== Extra-record citation sweep (Gate 1.3 pre-filter) ===")
    result = check_extra_record_citations(rows, args.brief)
    cite_problems, ref_cites = result if isinstance(result, tuple) else (result, [])
    for p in cite_problems:
        print(f"  NOTE: {p}")
    if ref_cites:
        print(f"  Found {len(ref_cites)} REF-style citation(s) in the brief text.")
        print("  Manually confirm each one resolves to an appendix entry above —")
        print("  this script does not do that resolution automatically.")
        for c in ref_cites:
            print(f"    {c}")

    total_flags = len(span_problems) + (1 if cite_problems and "No REF" in cite_problems[0] else 0)
    if total_flags:
        print(f"\n{total_flags} item(s) need attorney/paralegal attention before Gate 1 can PASS.")
        sys.exit(1)
    print("\nNo automated flags raised. Gate 1.2 mechanical check clears; "
          "Gates 1.1, 1.3, and 1.4 still require the manual review described in SKILL.md.")
    sys.exit(0)


if __name__ == "__main__":
    main()
