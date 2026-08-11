#!/usr/bin/env python3
"""Run the pre-flight discrepancy check before building the document.

Reads the parsed PDF UMFs, parsed PDF Issues, parsed Notion UMF responses,
parsed Notion AMFs, and the Word shell .docx, then produces a report classifying
findings as:

  - HARD STOP: needs explicit user confirmation before proceeding
  - SOFT WARNING: surfaces in the final report but doesn't block
  - INFO: just structural facts, no action needed

Usage:
    python preflight_check.py \
        --pdf-umfs parsed_umfs.json \
        --pdf-issues parsed_issues.json \
        --notion-umfs notion_umf_responses.json \
        --notion-amfs notion_amfs.json \
        --word-shell template.docx \
        [--filing-deadline YYYY-MM-DD] \
        [--out preflight_report.json]

Prints a human-readable summary to stdout AND writes a structured JSON report
to --out, so the calling agent can parse the hard_stops list and decide
whether to proceed.
"""
import argparse
import json
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path


def read_json(path):
    if not path or not Path(path).exists():
        return None
    return json.loads(Path(path).read_text(encoding="utf-8"))


def inspect_word_shell(docx_path):
    """Extract document.xml from .docx and identify existing UMF rows + their fill state."""
    if not docx_path or not Path(docx_path).exists():
        return {"exists": False}
    with zipfile.ZipFile(docx_path) as z:
        try:
            xml = z.read("word/document.xml").decode("utf-8")
        except KeyError:
            return {"exists": False, "error": "No word/document.xml in archive"}

    # Find all UMF bookmarks
    bookmarks = re.findall(r'<w:bookmarkStart[^/]+w:name="UMF(\d+)"', xml)
    umf_numbers = sorted(set(int(b) for b in bookmarks))

    # Detect existing right-cell content. Crude heuristic: for each UMF row,
    # look at the right cell and check whether it has more than the empty
    # paragraph template. We use the bookmark as anchor; find the second </w:tc>
    # and look at the </w:tc>...</w:tc> span between (right cell content).
    partial_fills = []
    for n in umf_numbers:
        anchor = f'<w:bookmarkStart w:id="{n}" w:name="UMF{n}"/>'
        i0 = xml.find(anchor)
        if i0 < 0:
            anchor_alt = f'w:name="UMF{n}"'
            i0 = xml.find(anchor_alt)
            if i0 < 0:
                continue
        # End of LEFT cell
        left_close = xml.find("</w:tc>", i0)
        if left_close < 0:
            continue
        # Start of RIGHT cell
        right_start = xml.find("<w:tc>", left_close)
        if right_start < 0:
            continue
        right_close = xml.find("</w:tc>", right_start)
        if right_close < 0:
            continue
        right_cell = xml[right_start:right_close]
        # Look for <w:t> content with non-trivial length
        text_pieces = re.findall(r"<w:t[^>]*>([^<]+)</w:t>", right_cell)
        joined = "".join(text_pieces).strip()
        if len(joined) > 5:
            partial_fills.append({"umf": n, "preview": joined[:150]})

    return {
        "exists": True,
        "umf_bookmarks": umf_numbers,
        "umf_count": len(umf_numbers),
        "partial_response_fills": partial_fills,
    }


def detect_combined_groups(notion_umfs):
    """Find UMFs whose response starts with 'Combined response with' or
    references another UMF group."""
    groups = {}
    for k, v in (notion_umfs or {}).items():
        resp = (v.get("plaintiff_response") or "").lower()
        m = re.search(r"combined response (?:to|with) umfs?\s*([\d\-,–\s]+)", resp)
        if m:
            groups[k] = m.group(1).strip()
    return groups


def detect_short_responses(notion_umfs, threshold=20):
    """Flag responses that are suspiciously short (likely placeholder)."""
    short = []
    for k, v in (notion_umfs or {}).items():
        resp = (v.get("plaintiff_response") or "").strip()
        if 0 < len(resp) < threshold:
            short.append({"umf": int(k), "response": resp})
    return short


def detect_pdf_typos(pdf_umfs):
    """Surface common typos / inconsistencies in the PDF text."""
    typos = []
    seen_names = set()
    if not pdf_umfs:
        return typos

    full_text = "\n".join(u["fact"] + " " + u["evidence"] for u in pdf_umfs)

    # Skoosky vs Skootsky inconsistency
    has_skoosky = "Skoosky" in full_text
    has_skootsky = "Skootsky" in full_text
    if has_skoosky and has_skootsky:
        typos.append("Inconsistent spelling: 'Skoosky' vs 'Skootsky' both appear (likely typo)")
    elif has_skoosky and not has_skootsky:
        typos.append("'Skoosky' appears but the more conventional spelling is 'Skootsky' — verify against signature blocks")

    # Missing space after pp.
    if re.search(r"pp\.\d", full_text):
        typos.append("Some pin cites have 'pp.NN' without a space after 'pp.'")

    # Semicolon in page range (e.g., "103:10-103;19" should be "103:10-103:19")
    if re.search(r"\d+:\d+-\d+;\d+", full_text):
        typos.append("Detected a semicolon inside a page range (likely should be colon, e.g., '103;19' → '103:19')")

    # Unbalanced brackets
    for u in pdf_umfs:
        for field in ("fact", "evidence"):
            t = u.get(field, "")
            opens = t.count("[")
            closes = t.count("]")
            if opens != closes:
                typos.append(f"UMF {u['num']} {field}: unbalanced brackets ({opens} '[' vs {closes} ']')")

    # Missing space after comma in dates (e.g., "May 16,2018")
    if re.search(r"[A-Z][a-z]+ \d+,\d{4}", full_text):
        typos.append("A date is missing a space after the comma (e.g., 'May 16,2018' should be 'May 16, 2018')")

    return typos


def detect_verify_flags(notion_umfs, notion_amfs):
    flagged = []
    for source, items in (("UMF", notion_umfs or {}), ("AMF", notion_amfs or {})):
        for k, v in items.items():
            blob = " ".join(v.values())
            if "[VERIFY]" in blob or "VERIFY" in blob:
                flagged.append(f"{source} {k}")
    return flagged


def umf_text_diff(pdf_umfs, word_shell):
    """If the user has manually edited a UMF in the Word shell so it differs
    significantly from the PDF, flag it. Requires a deeper inspection — for
    now, just check rough character-count similarity."""
    # This is a stub for the future; when we read existing rows from the shell,
    # we can compare. For now, return empty.
    return []


def filing_deadline_warning(deadline_str):
    if not deadline_str:
        return None
    try:
        d = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    days_left = (d - datetime.now().date()).days
    if days_left <= 7:
        return f"Filing deadline is {d.isoformat()} — only {days_left} days away. Confirm there's time for attorney review before signing."
    return None


def run_preflight(args):
    pdf_umfs = read_json(args.pdf_umfs)
    pdf_issues = read_json(args.pdf_issues)
    notion_umfs = read_json(args.notion_umfs)
    notion_amfs = read_json(args.notion_amfs)
    shell = inspect_word_shell(args.word_shell)

    hard_stops = []
    soft_warnings = []
    info = []

    # ---- Counts and structure (info) ----
    if pdf_umfs is not None:
        info.append(f"PDF: found {len(pdf_umfs)} UMFs (numbered {pdf_umfs[0]['num']}-{pdf_umfs[-1]['num']})" if pdf_umfs else "PDF: no UMFs found")
    if pdf_issues is not None:
        info.append(f"PDF: found {len(pdf_issues)} Issue sections")
        for iss in pdf_issues:
            info.append(f"  Issue {iss['num']}: incorporates UMFs {iss['umfs']!r}")
    if notion_umfs is not None:
        info.append(f"Notion: drafted responses for {len(notion_umfs)} UMFs")
    if notion_amfs is not None:
        if notion_amfs:
            keys = sorted(int(k) for k in notion_amfs.keys())
            info.append(f"Notion: {len(notion_amfs)} AMFs (numbered {keys[0]}-{keys[-1]})")
        else:
            info.append("Notion: no AMFs drafted")
    if shell.get("exists"):
        info.append(f"Word shell: {shell['umf_count']} existing UMF row(s)")

    # ---- Hard stops ----

    # 1. UMF count mismatch
    if pdf_umfs and notion_umfs:
        pdf_nums = set(u["num"] for u in pdf_umfs)
        notion_nums = set(int(k) for k in notion_umfs.keys())
        missing_in_notion = pdf_nums - notion_nums
        extra_in_notion = notion_nums - pdf_nums
        if missing_in_notion:
            hard_stops.append({
                "type": "umf_count_mismatch",
                "message": f"Notion is missing responses for UMFs: {sorted(missing_in_notion)}",
                "remediation": "Either fill them in Notion first, or skip those UMFs (they'll be left empty in Word).",
            })
        if extra_in_notion:
            hard_stops.append({
                "type": "umf_count_mismatch",
                "message": f"Notion has responses for UMFs that don't exist in PDF: {sorted(extra_in_notion)}",
                "remediation": "Verify the PDF parse is complete, or remove the extras from Notion.",
            })

    # 2. Word shell partial fills
    if shell.get("partial_response_fills"):
        hard_stops.append({
            "type": "shell_partial_fills",
            "message": f"Word shell has user-typed responses for UMFs: {[p['umf'] for p in shell['partial_response_fills']]}",
            "remediation": "Confirm: overwrite with Notion versions, OR keep existing and skip these UMFs?",
        })

    # 3. Word shell has no UMFs yet
    if shell.get("exists") and shell["umf_count"] == 0:
        hard_stops.append({
            "type": "fresh_shell",
            "message": "Word shell has no existing UMF rows — looks like a fresh template.",
            "remediation": "Confirm: build the entire UMF table from the PDF, OR is the shell incomplete?",
        })

    # 4. Combined-response groups
    combined = detect_combined_groups(notion_umfs)
    if combined:
        hard_stops.append({
            "type": "combined_responses",
            "message": f"Combined-response groups detected: {combined}",
            "remediation": "Confirm: duplicate response text across rows (default), OR merge cells?",
        })

    # 5. Issue incorporation language doesn't match standard
    if pdf_issues:
        weird = [iss["num"] for iss in pdf_issues if not iss.get("umfs")]
        if weird:
            hard_stops.append({
                "type": "issue_format_unusual",
                "message": f"Issue(s) {weird} did not parse a standard 'incorporate by reference Undisputed Facts Nos.' clause.",
                "remediation": "Inspect the PDF manually and decide whether to skip or hand-fill these.",
            })

    # 6. AMFs present but no placement instruction
    # The skill should have asked the user upfront; if user didn't say where to put AMFs,
    # this is flagged at runtime by the calling agent. Here we just info-log.
    if notion_amfs and len(notion_amfs) > 0:
        info.append(f"AMFs will be placed in a single table at the end (default). Confirm if you'd prefer per-Issue placement.")

    # 7. Notion structure unfamiliar — handled at parse time (parser returns empty).
    if notion_umfs is not None and len(notion_umfs) == 0:
        hard_stops.append({
            "type": "notion_parse_empty",
            "message": "Notion parser returned 0 UMF responses. Heading structure may be unfamiliar.",
            "remediation": "Inspect the Notion page and confirm headings follow the '## UMF N' pattern with labeled blocks.",
        })

    # 8. PDF parse anomaly (no UMFs detected)
    if pdf_umfs is not None and len(pdf_umfs) == 0:
        hard_stops.append({
            "type": "pdf_parse_empty",
            "message": "PDF parser returned 0 UMFs. May be image-only / scanned / non-standard layout.",
            "remediation": "Run OCR first, or check whether the PDF uses the standard 2-column California pleading layout.",
        })

    # 9. Filing deadline within 7 days
    deadline_msg = filing_deadline_warning(args.filing_deadline)
    if deadline_msg:
        hard_stops.append({
            "type": "deadline_close",
            "message": deadline_msg,
            "remediation": "Confirm there's time for attorney review and finalization.",
        })

    # 10. Short responses (likely placeholder)
    short = detect_short_responses(notion_umfs)
    if short:
        hard_stops.append({
            "type": "short_responses",
            "message": f"Some Notion responses are <20 chars (likely placeholders): {[s['umf'] for s in short]}",
            "remediation": "Confirm these short responses are intentional, or fill them in before continuing.",
        })

    # ---- Soft warnings ----
    typos = detect_pdf_typos(pdf_umfs)
    for t in typos:
        soft_warnings.append({"type": "pdf_typo", "message": t})

    verify_flags = detect_verify_flags(notion_umfs, notion_amfs)
    if verify_flags:
        soft_warnings.append({
            "type": "verify_flags",
            "message": f"[VERIFY] flags found in: {verify_flags}",
        })

    report = {
        "info": info,
        "hard_stops": hard_stops,
        "soft_warnings": soft_warnings,
        "should_pause": len(hard_stops) > 0,
    }

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False))

    # Human-readable summary
    print("=" * 70)
    print("PRE-FLIGHT CHECK")
    print("=" * 70)
    print("\n--- Info ---")
    for line in info:
        print(f"  • {line}")

    if hard_stops:
        print(f"\n--- HARD STOPS ({len(hard_stops)}) — CONFIRM BEFORE PROCEEDING ---")
        for h in hard_stops:
            print(f"  ⛔ {h['message']}")
            print(f"     → {h['remediation']}")

    if soft_warnings:
        print(f"\n--- Soft warnings ({len(soft_warnings)}) — flag at end ---")
        for w in soft_warnings:
            print(f"  ⚠  {w['message']}")

    if not hard_stops and not soft_warnings:
        print("\n✅ All clear — safe to proceed silently.")

    print("\n" + "=" * 70)
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-umfs", help="parsed_umfs.json from extract_umfs_from_pdf.py")
    ap.add_argument("--pdf-issues", help="parsed_issues.json from extract_issues_from_pdf.py")
    ap.add_argument("--notion-umfs", help="notion_umf_responses.json")
    ap.add_argument("--notion-amfs", help="notion_amfs.json")
    ap.add_argument("--word-shell", help="path to the Word shell .docx")
    ap.add_argument("--filing-deadline", help="ISO date YYYY-MM-DD (optional)")
    ap.add_argument("--out", default="preflight_report.json")
    args = ap.parse_args()

    report = run_preflight(args)
    sys.exit(1 if report["should_pause"] else 0)


if __name__ == "__main__":
    main()
