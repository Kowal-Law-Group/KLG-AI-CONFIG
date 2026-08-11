"""Shared helpers for the opposition-separate-statement skill.

These utilities are imported by extract_umfs_from_pdf.py, parse_notion_responses.py,
and build_word_doc.py. The functions here encode the lessons learned from the first
time this workflow was done by hand — see references/common_gotchas.md for context.
"""
import re


# ---------------------------------------------------------------------------
# XML escaping
# ---------------------------------------------------------------------------

def escape_xml(s: str) -> str:
    """Escape text for safe inclusion in OOXML.

    Smart quotes are converted to XML entities (legal writing should always use
    curly quotes). Section / pilcrow symbols are left as literal Unicode since
    they don't conflict with XML syntax.
    """
    if not s:
        return ""
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace("“", "&#x201C;")  # left double quote
    s = s.replace("”", "&#x201D;")  # right double quote
    s = s.replace("‘", "&#x2018;")  # left single quote
    s = s.replace("’", "&#x2019;")  # right single quote / apostrophe
    return s


# ---------------------------------------------------------------------------
# Markdown italic/bold → OOXML runs
# ---------------------------------------------------------------------------

def text_to_runs(text: str) -> str:
    """Convert text containing markdown *italic* and **bold** markers into a
    sequence of <w:r> runs with proper formatting.

    The Notion export uses Markdown-style emphasis. We need to translate it to
    Word's <w:i/> / <w:b/> run properties so the document looks right.

    State machine: walk character by character, toggling bold/italic state when
    we see ** or *. Build a run for each contiguous text segment.
    """
    if not text:
        return ""
    runs = []
    i = 0
    state = {"b": False, "i": False}

    while i < len(text):
        # Bold toggle: ** (but not part of *** or **** etc.)
        if text[i:i + 2] == "**" and (i + 2 >= len(text) or text[i + 2] != "*"):
            state["b"] = not state["b"]
            i += 2
            continue
        # Italic toggle: single * (must not be part of ** or surrounded by **)
        if text[i] == "*" and (i + 1 >= len(text) or text[i + 1] != "*") \
                and (i == 0 or text[i - 1] != "*"):
            state["i"] = not state["i"]
            i += 1
            continue

        # Find the next emphasis marker
        next_marker = len(text)
        for marker in ("**", "*"):
            idx = text.find(marker, i)
            if 0 <= idx < next_marker:
                next_marker = idx

        segment = text[i:next_marker]
        if segment:
            rpr_parts = []
            if state["b"]:
                rpr_parts.append("<w:b/><w:bCs/>")
            if state["i"]:
                rpr_parts.append("<w:i/><w:iCs/>")
            rpr = f"<w:rPr>{''.join(rpr_parts)}</w:rPr>" if rpr_parts else ""
            escaped = escape_xml(segment)
            preserve = ' xml:space="preserve"' if segment != segment.strip() else ""
            runs.append(f"<w:r>{rpr}<w:t{preserve}>{escaped}</w:t></w:r>")
        i = next_marker
    return "".join(runs)


def make_paragraphs(text: str, style: str = "BodyText") -> str:
    """Convert text (possibly multi-paragraph via newlines) into a sequence of
    <w:p> elements, each with the BodyText style and zero first-line indent.

    Empty paragraphs are dropped. Inline emphasis is preserved via text_to_runs.
    """
    if not text:
        return ""
    out = []
    for para in text.split("\n"):
        para = para.strip()
        if not para:
            continue
        runs = text_to_runs(para)
        out.append(
            f'<w:p w:rsidR="00000000" w:rsidRDefault="00000000">'
            f'<w:pPr><w:pStyle w:val="{style}"/>'
            f'<w:spacing w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:firstLine="0"/></w:pPr>'
            f"{runs}</w:p>"
        )
    return "\n          ".join(out)


# ---------------------------------------------------------------------------
# OOXML cell builders (used by build_word_doc.py)
# ---------------------------------------------------------------------------

SUPPORTING_EVIDENCE_HEADER = (
    '<w:p w:rsidR="00000000" w:rsidRDefault="00000000">'
    '<w:pPr><w:pStyle w:val="BodyText"/>'
    '<w:spacing w:line="240" w:lineRule="auto"/>'
    '<w:ind w:firstLine="0"/>'
    '<w:rPr><w:b/><w:bCs/></w:rPr></w:pPr>'
    '<w:r><w:rPr><w:b/><w:bCs/></w:rPr>'
    '<w:t>Supporting Evidence:</w:t></w:r></w:p>'
)


def populated_right_cell(response: str, evidence: str, cell_width: int = 4711) -> str:
    """Build the right cell of a UMF row — Plaintiff's response + bold
    'Supporting Evidence:' header + Plaintiff's supporting evidence text.
    """
    response_xml = make_paragraphs(response)
    evidence_xml = make_paragraphs(evidence)
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>'
        f'{response_xml}'
        f'{SUPPORTING_EVIDENCE_HEADER}'
        f'{evidence_xml}'
        f'</w:tc>'
    )


def empty_right_cell(cell_width: int = 4711) -> str:
    """Build an empty right cell — used for Issue tables and AMF tables where
    the opposing party hasn't responded yet.
    """
    return (
        f'<w:tc><w:tcPr><w:tcW w:w="{cell_width}" w:type="dxa"/></w:tcPr>'
        f'<w:p w:rsidR="00000000" w:rsidRDefault="00000000">'
        f'<w:pPr><w:pStyle w:val="BodyText"/>'
        f'<w:spacing w:line="240" w:lineRule="auto"/>'
        f'<w:ind w:firstLine="0"/></w:pPr></w:p>'
        f'</w:tc>'
    )


# ---------------------------------------------------------------------------
# Sequential UMF/AMF detection
# ---------------------------------------------------------------------------

def detect_sequential_items(text: str, start_num: int = 1):
    """Walk through `text` line by line, treating a line that starts with the
    *next expected* integer + period as the start of a new item. This avoids
    false positives where a line like 'August 16, 2017.' wraps to a new line.

    Returns list of (number, content_text) tuples.
    """
    items = []
    current_num = 0
    current_text = []
    expected = start_num

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if m and int(m.group(1)) == expected:
            if current_num > 0:
                items.append((current_num, " ".join(current_text)))
            current_num = int(m.group(1))
            current_text = [m.group(2)]
            expected = current_num + 1
        else:
            current_text.append(line)

    if current_num > 0:
        items.append((current_num, " ".join(current_text)))
    return items


# ---------------------------------------------------------------------------
# Smart Word doc search (handles the literal-Unicode-vs-entity gotcha)
# ---------------------------------------------------------------------------

def find_in_xml(doc: str, search_str: str) -> int:
    """Find a string in a document.xml, where the string may contain smart
    apostrophes/quotes. The doc may have either literal Unicode or XML entities
    for these characters; we try both forms.

    Returns the offset of the first match, or -1 if not found.
    """
    # Try literal Unicode (the form the unpack script preserves)
    idx = doc.find(search_str)
    if idx >= 0:
        return idx
    # Try with smart-quote entities
    s = search_str
    s = s.replace("‘", "&#x2018;")
    s = s.replace("’", "&#x2019;")
    s = s.replace("“", "&#x201C;")
    s = s.replace("”", "&#x201D;")
    return doc.find(s)
