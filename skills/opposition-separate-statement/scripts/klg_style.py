"""KLG (Kowal Law Group) style guide normalization.

Applied to all transferred text BEFORE it enters the Word document. The goal
is to suppress common AI/word-processor "tells" that legal professionals use
to flag content as machine-generated:

  1. Straight quotes ("dumb quotes")  →  curly quotes ("smart quotes")
  2. Em dashes with surrounding spaces  →  closed em dashes (no spaces)

Both transformations match the conventions a human attorney would apply by
running the document through a Word style checker. Failing to apply them
makes the output look templated.

Apply via `klg_style_normalize(text)` after parsing source content (Notion,
PDF, etc.) but BEFORE passing to the XML-runs builder. The builder handles
markdown emphasis (* and **) so leave those characters alone here.
"""
import re


# ---------------------------------------------------------------------------
# Smart quotes
# ---------------------------------------------------------------------------

def smart_quote_text(text: str) -> str:
    """Convert straight quotes to curly quotes using positional heuristics.

    Rules:
      - Apostrophe inside a word ('s, 't, 'd, etc.) → right single (')
      - Apostrophe at end of word (boys', plaintiffs') → right single (')
      - Apostrophe at start of word ('twas, '90s) → left single (')
      - Bare ' between non-letters: prefer right single
      - Double quote after whitespace or open punctuation → left double (")
      - Double quote elsewhere → right double (")

    These heuristics handle the overwhelming majority of legal-writing cases
    correctly. Edge cases (e.g., nested single quotes inside a quotation) may
    need manual review during the final pass.
    """
    if not text:
        return text

    # Apostrophes inside or at end of words come first because they are the
    # most common case in legal prose.
    text = re.sub(r"(\w)'(\w)", r"\1’\2", text)        # don't → don’t
    text = re.sub(r"(\w)'(?=\W|$)", r"\1’", text)       # boys' → boys’
    # Leading apostrophe (start of string or after non-word char): use \W or ^
    text = re.sub(r"(^|\W)'(\w)", r"\1‘\2", text)        # 'twas → ‘twas

    # Double quotes — walk and toggle
    out_chars = []
    in_double = False
    for i, c in enumerate(text):
        if c == '"':
            prev = text[i - 1] if i > 0 else ' '
            # Opening if the previous char is whitespace or an open delimiter
            if prev in ' \t\n([{<' or i == 0:
                out_chars.append('“')   # left double “
                in_double = True
            else:
                out_chars.append('”')   # right double ”
                in_double = False
        else:
            out_chars.append(c)

    # Any remaining literal apostrophe (single ') after the word-based rules
    # is rare and usually a stray case; default it to right single quote.
    result = "".join(out_chars).replace("'", "’")
    return result


# ---------------------------------------------------------------------------
# Closed em dashes
# ---------------------------------------------------------------------------

def close_em_dashes(text: str) -> str:
    """Remove spaces (and tabs) around em dashes — but preserve newlines.

    A space-padded em dash (' — ') is the AP / Chicago "open" style. KLG
    style is "closed" — no spaces around em dashes. We do not collapse
    paragraph breaks (newlines) since those are intentional.
    """
    if not text:
        return text
    # Match horizontal whitespace (spaces, tabs) on either side of an em dash
    return re.sub(r"[ \t]*—[ \t]*", "—", text)


# ---------------------------------------------------------------------------
# Other minor cleanups
# ---------------------------------------------------------------------------

def collapse_double_spaces(text: str) -> str:
    """Collapse runs of two or more spaces into a single space within a line.

    Common artifact of paragraph reflow in PDFs and copy-paste from Notion.
    Two-space-after-period ("French spacing") is also explicitly disfavored
    in modern legal style guides.
    """
    if not text:
        return text
    return re.sub(r" {2,}", " ", text)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def klg_style_normalize(text: str) -> str:
    """Run the full KLG-style normalization on a string.

    Order matters:
      1. Smart-quote conversion runs first because em-dash detection doesn't
         depend on quote shape.
      2. Em-dash closing runs second to clean up the most common AI tell.
      3. Double-space collapse runs last as a final tidy.
    """
    if not text:
        return text
    text = smart_quote_text(text)
    text = close_em_dashes(text)
    text = collapse_double_spaces(text)
    return text


def klg_style_normalize_dict(d):
    """Apply normalization in-place to all string leaves of a dict."""
    if isinstance(d, dict):
        return {k: klg_style_normalize_dict(v) for k, v in d.items()}
    if isinstance(d, list):
        return [klg_style_normalize_dict(v) for v in d]