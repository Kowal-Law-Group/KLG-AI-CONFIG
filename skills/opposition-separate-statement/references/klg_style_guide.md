# Kowal Law Group style guide (as applied by this skill)

These conventions reflect what the firm requires and what a human attorney would normally apply with a Word style checker. They are non-negotiable — failing to apply them flags content as machine-generated, which is unacceptable in court filings.

## What the skill auto-corrects

The skill applies these transformations automatically inside `klg_style.py` to every piece of text it transfers from a Notion export or a PDF before it lands in the Word document:

### 1. Smart quotes (no straight quotes anywhere)

| Wrong (straight)  | Right (curly) |
|-------------------|---------------|
| `"Plaintiff said..."` | `"Plaintiff said…"` |
| `Plaintiff's`     | `Plaintiff's` |
| `don't`           | `don't` |
| `boys'`           | `boys'` |
| `'twas`           | `'twas` |

The skill uses positional heuristics: an apostrophe inside or at the end of a word becomes the right single quote (’), an apostrophe at the start of a word becomes the left single quote (‘), a double quote after whitespace becomes the left double quote (“), and a double quote elsewhere becomes the right double quote (”).

Notion exports typically come through with backslash-escaped straight quotes (`\"`) which the parser unescapes before applying smart-quote conversion.

### 2. Closed em dashes (no spaces around them)

| Wrong (open)             | Right (closed)        |
|--------------------------|-----------------------|
| `Plaintiff — a doctor — testified` | `Plaintiff—a doctor—testified` |
| `15 — 16 months`         | `15—16 months`        |

The skill removes any horizontal whitespace (spaces and tabs) on either side of an em dash. Newlines around an em dash are preserved (an em dash at the end of a line is a deliberate break and shouldn't be collapsed).

This is the "closed" or "Chicago tight" em-dash style. The "open" style with spaces is AP / news style and is one of the most frequent AI tells in long-form prose.

### 3. Double-space cleanup

Two or more consecutive spaces inside a line are collapsed to a single space. This catches:

- "French spacing" (two spaces after periods) — disfavored in modern legal style
- Paragraph reflow artifacts from PDF copy-paste
- Stray double spaces in Notion exports

Newlines and tab characters are preserved.

## What the skill does NOT auto-correct (but flags as soft warnings)

- **Em-dash overuse.** Em dashes are appropriate in moderation. If a paragraph has more than two em dashes, the skill leaves them alone but the user should review.
- **Hedging language.** Phrases like "It's worth noting…", "It's important to remember…", "In essence…" are AI fingerprints. The skill does not remove them — substantive editing is the attorney's call.
- **Sentence rhythm.** AI-generated prose tends to use long parallel constructions. The skill cannot detect this.
- **Three-dot ellipses.** The skill does NOT convert `...` to `…` (Unicode ellipsis). Three dots is the conventional form in California legal writing per the California Style Manual; the Unicode ellipsis is itself an AI tell.
- **Hyphen vs. en-dash vs. em-dash distinctions.** If the source uses a hyphen where an en-dash or em-dash would be technically correct (e.g., "pages 24-30" should be "pages 24–30"), the skill leaves it alone — these are deliberate stylistic choices.

## When to override

If a future case requires DIFFERENT style conventions (e.g., open em dashes for an out-of-state filing), the skill caller can pass `--no-style-normalize` to skip all auto-corrections and copy text verbatim. The default is always on.

## Why this matters

Legal writing is held to a higher standard than ordinary prose. A motion that looks templated invites scrutiny. Worse, if opposing counsel can plausibly argue that the filing is machine-generated, that becomes a sanctions issue under Rule 11 (federal) or CCP § 128.7 (California). Applying the firm's style guide automatically — exactly as a human attorney would — is the price of using AI tooling in this practice area.
