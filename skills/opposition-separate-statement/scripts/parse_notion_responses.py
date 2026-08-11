#!/usr/bin/env python3
"""Parse a Notion page export (text format) into structured JSON for
opposition-separate-statement.

The Notion page is the source of truth for Plaintiff's drafted responses. Each
entry uses ### UMF N or ### AMF N as a heading, followed by labeled bold
markers (**Defendant's UMF:**, **Plaintiff's Response:**, etc.).

Combined responses (e.g., 'Combined response with UMFs 14 and 15') are
detected and the response text is duplicated across every member of the group
so each row in the Word table can be filled independently. (User preference:
duplicate text rather than merging cells.)

Usage:
    python parse_notion_responses.py notion_export.txt --umf-out responses.json --amf-out amfs.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from klg_style import klg_style_normalize


LABELS = {
    "umf_fact": [r"\*\*Defendant['’]s UMF:\*\*", r"\*\*Movant['’]s UMF:\*\*"],
    "umf_evidence": [r"\*\*Defendant['’]s Supporting Evidence:\*\*", r"\*\*Movant['’]s Supporting Evidence:\*\*"],
    "response": [r"\*\*Plaintiff['’]s Response:\*\*", r"\*\*Opposing Party['’]s Response:\*\*"],
    "response_evidence": [r"\*\*Plaintiff['’]s Supporting Evidence:\*\*", r"\*\*Opposing Party['’]s Supporting Evidence:\*\*"],
    "amf_fact": [r"\*\*Plaintiff['’]s AMF:\*\*", r"\*\*Plaintiff['’]s Additional Material Fact[^:]*:\*\*"],
    "amf_evidence": [r"\*\*Plaintiff['’]s Supporting Evidence:\*\*"],
}


def normalize_input(text):
    """Convert JSON-escaped Notion exports (literal '\\n' sequences, '\\['
    bracket escapes) into a plain markdown form with real newlines."""
    if "\\n" in text and text.count("\n") < 50:
        text = text.replace("\\n", "\n")
        text = text.replace("\\[", "[").replace("\\]", "]")
        text = text.replace('\\"', '"').replace("\\'", "'")
        text = text.replace("\\\\", "\\")
        text = text.replace("\\$", "$")
        text = text.replace("\\&", "&")
        text = text.replace("\\#", "#").replace("\\<", "<").replace("\\>", ">")
    return text


def find_section_blocks(text, prefix):
    """Find all blocks like '### UMF N\\n...content...' until the next ## or ###."""
    pattern = re.compile(
        rf"###\s+{prefix}\s+(\d+)\b(.*?)(?=\n###\s|\n##\s|\Z)",
        re.DOTALL,
    )
    return [(int(m.group(1)), m.group(2)) for m in pattern.finditer(text)]


def extract_label_value(block, label_patterns):
    """Extract text following a labeled bold marker, stopping at the next labeled marker."""
    for pat in label_patterns:
        full_pat = rf"{pat}\s*(.*?)(?=\n\s*\*\*[A-Z][^:]{{0,80}}:\*\*|\Z)"
        m = re.search(full_pat, block, re.DOTALL)
        if m:
            return m.group(1).strip()
    return ""


def parse_member_list(s):
    """Parse a list like '13-15' or '14 and 15' into [13,14,15]."""
    s = s.replace("–", "-").replace(" and ", ",")
    members = []
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            try:
                a, b = part.split("-")
                members.extend(range(int(a.strip()), int(b.strip()) + 1))
            except ValueError:
                continue
        else:
            try:
                members.append(int(part))
            except ValueError:
                continue
    return members


def parse_combined_groups(umf_blocks):
    """Detect combined-response groups by 'Combined response with UMFs ...' or
    'See combined response to UMFs ...' markers."""
    groups = {}
    for num, block in umf_blocks:
        m = re.search(r"[Cc]ombined response with UMFs?\s+([\d, and\-–]+)", block)
        if m:
            raw = m.group(1).strip().rstrip(".")
            members = parse_member_list(raw)
            members.append(num)
            members = sorted(set(members))
            for m2 in members:
                groups[m2] = members
            continue
        m = re.search(r"[Ss]ee combined response (?:to|with) UMFs?\s+([\d, and\-–]+)", block)
        if m:
            raw = m.group(1).strip().rstrip(".")
            members = parse_member_list(raw)
            members.append(num)
            members = sorted(set(members))
            for m2 in members:
                groups[m2] = members
    return groups


def parse_umfs(text):
    blocks = find_section_blocks(text, "UMF")
    parsed = {}
    for num, block in blocks:
        response = klg_style_normalize(extract_label_value(block, LABELS["response"]))
        evidence = klg_style_normalize(extract_label_value(block, LABELS["response_evidence"]))
        parsed[str(num)] = {
            "plaintiff_response": response,
            "plaintiff_evidence": evidence,
        }

    combined = parse_combined_groups(blocks)
    seen_groups = set()
    for member_num, group_members in combined.items():
        key = tuple(sorted(group_members))
        if key in seen_groups:
            continue
        seen_groups.add(key)
        primary = None
        for m in sorted(group_members):
            entry = parsed.get(str(m))
            if entry and len(entry["plaintiff_response"]) > 50 \
                    and not entry["plaintiff_response"].lower().startswith(("see combined", "*see combined")):
                primary = m
                break
        if primary is None:
            continue
        primary_data = parsed[str(primary)]
        for m in group_members:
            if str(m) in parsed:
                parsed[str(m)] = {
                    "plaintiff_response": primary_data["plaintiff_response"],
                    "plaintiff_evidence": primary_data["plaintiff_evidence"],
                }
    return parsed


def parse_amfs(text):
    blocks = find_section_blocks(text, "AMF")
    parsed = {}
    for num, block in blocks:
        fact = klg_style_normalize(extract_label_value(block, LABELS["amf_fact"]))
        evidence = klg_style_normalize(extract_label_value(block, LABELS["amf_evidence"]))
        parsed[str(num)] = {
            "fact": fact,
            "evidence": evidence,
        }
    return parsed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("notion_text")
    ap.add_argument("--umf-out", default="notion_umf_responses.json")
    ap.add_argument("--amf-out", default="notion_amfs.json")
    args = ap.parse_args()

    text = Path(args.notion_text).read_text(encoding="utf-8")
    text = normalize_input(text)
    umfs = parse_umfs(text)
    amfs = parse_amfs(text)

    with open(args.umf_out, "w", encoding="utf-8") as f:
        json.dump(umfs, f, indent=2, ensure_ascii=False)
    with open(args.amf_out, "w", encoding="utf-8") as f:
        json.dump(amfs, f, indent=2, ensure_ascii=False)

    print