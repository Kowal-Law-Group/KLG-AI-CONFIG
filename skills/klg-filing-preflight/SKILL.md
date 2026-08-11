---
name: klg-filing-preflight
description: "Run the final pre-filing checklist on a writ petition or emergency application before attorney sign-off. Use whenever the user says 'pre-filing checklist', 'filing preflight', 'ready to file', 'final check before filing', 'run the preflight', 'is this ready to file', or asks for a last-pass review of a writ petition, petition for writ of mandate/prohibition, emergency application, or ex parte application immediately before it goes out. Runs as the last gate in the pipeline, after klg-cite-check and klg-style-guide-check have already run — do not use this in place of either of those. Do NOT use for substantive brief review (klg-brief-elevation), citation verification (klg-cite-check), or style conformance (klg-style-guide-check) — this skill assumes those already passed and checks a different, narrower set of filing-mechanics failure modes."
---

# KLG Filing Preflight

## Why this exists

The Second District summarily denied two consecutive writ petitions in
the ADF surrogacy matter (B355938 / B356109) for record inadequacy —
neither reached the merits. Rule 8.486(b)(4) permits summary denial for
an incomplete record with no notice-and-cure obligation, and the five-day
cure right in rule 8.486(c)(2) reaches only the form of supporting
documents, not their content. **[VERIFY: confirm current text and
subdivision numbering of rule 8.486 before relying on these citations —
carried over from the backlog entry that spawned this skill, not
independently confirmed in this session.]** There is no second chance
built into the rule, so the firm needs one of its own: a final,
mechanical gate that runs after substantive review and citation
verification are already done, immediately before attorney sign-off.

A third-attempt review of the same petition surfaced defect classes
beyond record completeness: a verification carried over from a prior
filing that predated the facts it verified, 85 unaccepted tracked
changes still live in the filing copy, a fact redacted in one place but
printed in clear text in two others, and citations to a document outside
the appendix. This skill's seven gates cover that full defect surface,
not just record completeness.

## When this runs

Last step before attorney sign-off, after `klg-cite-check` (Phase A and
B) and `klg-style-guide-check` have both already run on the document.
This skill does not check citation accuracy or prose style — it assumes
those passes already happened and checks filing mechanics: is the
record actually complete, are the required declarations present and
internally consistent, is the stay showing coherent, does the cover page
follow the court's formatting rules, are redactions actually redacted,
and is the file itself clean (no tracked changes, no stale metadata).

## Required inputs

- The filing draft (the actual document going out), in its near-final
  or final form
- The appendix or record supporting the filing, with REF/page numbers
- The Register of Actions (or trial court docket) for the underlying
  matter, to reconcile against
- Any prior writ petitions in the same matter (numbers and dispositions)
  and their rulings, if this is a renewed or successive filing
- The applicable stay order or ruling being challenged, if a stay is at
  issue

If any of these is missing, ask for it before running Gate 1 — record
completeness can't be checked against a Register of Actions that isn't
in front of Claude.

## The seven gates

Run all seven in order. Do not stop at the first failure — flag every
failure found, then report all of them together (see Output Format).
A single missed gate is exactly the failure mode this skill exists to
catch, so partial runs defeat the purpose.

### Gate 1 — Record completeness

1. **Rule 8.486(b) reconciliation.** Walk the Register of Actions
   entry by entry against the appendix. Every entry that could bear on
   the issues raised must either be in the appendix or be affirmatively
   explained as immaterial. Flag any gap.
2. **Page-span audit.** Catch notices of motion filed without their
   supporting memoranda, exhibits referenced but not attached, and
   orders referenced but not included. `scripts/page_span_audit.py`
   (in this skill folder) does the mechanical half of this: it reads a
   simple CSV of appendix entries (document name, start page, end page)
   and flags entries whose declared page span doesn't match the actual
   PDF page count, and flags any document that is cited in the brief
   but absent from the CSV. Run it; don't hand-count page spans.
3. **Extra-record citation sweep.** Every record citation in the
   filing must resolve to a REF number or page that actually exists in
   the appendix as compiled. Flag any citation to a document that is
   not in the appendix.
4. **Rule 8.486(b)(2) exigency declaration.** If anything material is
   genuinely unavailable (transcript not yet prepared, order not yet
   entered), confirm the exigency declaration is present and specific
   about what's missing and why.

### Gate 2 — Required declarations

Confirm each of the following is present, dated, and internally
consistent with the filing's own facts:

- Verification, and that its date is not earlier than the facts it
  verifies. A verification carried over from a prior filing is exactly
  the defect that triggered this skill — check the verification date
  against every factual assertion's date, not just the caption date.
- Exigency declaration (if Gate 1.4 applies)
- Transcript declaration (if transcripts are referenced but not yet
  final)
- Authenticity declaration for any document whose authenticity could
  be questioned
- Notice-of-stay-request declaration
- Word count declaration, and confirm the stated count matches an
  actual recount after final edits (see Gate 7)
- Certificate of interested persons
- Proof of service

### Gate 3 — Immediate stay showing

- What specifically is stayed, stated with the same precision in both
  the caption/cover page and the argument.
- Effective date of the stay request, and where that date comes from
  (an order, a deadline, a hearing date) — not just asserted.
- Prejudice if the stay is denied, tied to a concrete consequence and
  date, not a general hardship statement.
- Relief sought in the trial court, if any, and its disposition.
- If this is a renewed filing with a different stay date than the
  prior one, an explicit explanation for the shift. An unexplained date
  change between successive filings reads as either a drafting error
  or a credibility problem — either way it needs to be caught here.

### Gate 4 — Writ-worthiness

- No adequate remedy by appeal, argued affirmatively, not assumed.
- Irreparable harm tied to a specific date or event, not a general
  assertion of harm.
- Why the issue merits discretionary writ review beyond "we disagree
  with the ruling" — novelty, recurring importance, or clear error
  causing irreparable harm.
- If this is a Palma-track petition, confirm the Palma prerequisites
  are met and stated (informal opposition invited, or explained why
  not).
- Confirm the harm showing appears in both the verified petition
  itself and the argument section — a harm showing that appears only
  in argument, unverified, is a defect.

### Gate 5 — Cover page mechanics

- The Superior Court (not the opposing litigants) is named as
  respondent.
- Real parties in interest are disclosed and correctly captioned.
- A STAY REQUESTED block is present if a stay is sought, formatted per
  the court's local rules.
- Judge and department are correctly identified.
- If a related appeal is pending, a Related Appeal Pending notice is
  present with the correct appellate case number.
- Prior writ petition numbers and their dispositions are disclosed if
  this is a renewed or successive filing in the same matter.

### Gate 6 — Redaction and sealing consistency

This gate requires inspecting the actual file layers, not the rendered
view — a fact redacted in the visible PDF can still be present in the
underlying text layer or in an earlier draft's tracked-change history.

1. **Same-fact audit.** Every fact subject to a sealing or redaction
   order must be redacted everywhere it appears in the document, not
   just at its first occurrence. Search the full text (not just visual
   scan) for every instance of the sealed fact — name, date, dollar
   figure, or whatever the order covers — and confirm each instance is
   actually redacted.
2. **New-text audit.** Anything added to the document after the
   controlling sealing order was entered needs its own redaction pass —
   don't assume new text inherits redaction from the surrounding
   paragraph.
3. **Replacement audit.** If a redacted fact was replaced with a
   placeholder (e.g., "[Minor Child]"), confirm the placeholder is used
   consistently and doesn't itself leak identifying information (e.g.,
   initials that are still identifying in a small-party case).
4. **Index/TOC reconciliation.** If a heading was rewritten to remove a
   sealed fact, confirm the table of contents and any cross-references
   were updated to match — a TOC entry that still names the sealed fact
   defeats the redaction.
5. **Real-redaction confirmation.** Confirm redaction removes the
   underlying text rather than just visually covering it (a black box
   or highlight over selectable text is not a redaction). For a PDF,
   extract the text layer directly — with `pdftotext` or the `pdf`
   skill's extraction tooling — and confirm the "redacted" text does not
   appear in the extracted output. Do not rely on how the page looks
   when rendered.

### Gate 7 — Document hygiene

This gate also requires inspecting the file's XML, not the rendered
document — Word can render a document as clean while tracked changes,
comments, or stale metadata remain in the underlying file.

1. **Tracked changes and comments.** Unpack the .docx (see the `docx`
   skill's unpack script) and grep `word/document.xml` for `<w:ins`,
   `<w:del`, and comment reference tags. Any hit means unaccepted
   tracked changes or live comments are still in the file — the exact
   defect (85 unaccepted tracked changes) that triggered this skill.
   Zero tolerance: every hit must be resolved before filing, not just
   flagged.
2. **Metadata.** Check document properties (author, company, revision
   history) for anything that shouldn't go out the door — a prior
   matter's name in the template metadata, for instance.
3. **Word count.** Recompute the word count after all final edits and
   confirm it matches the Gate 2 word-count declaration. A stale word
   count declaration is a certification error.
4. **Internal date consistency.** Every date in the chronology,
   argument, and declarations should agree with the record and with
   each other. Flag any internal contradiction.
5. **Cross-references and bookmarks.** Confirm internal
   cross-references (e.g., "see Section III.B above") resolve to the
   section they claim to, and that bookmarks/hyperlinks in the final
   file aren't broken from earlier drafting.

## Output format

Produce a single report, one section per gate, in gate order. For each
gate, state a clear PASS or FAIL, and under FAIL list every specific
defect found (not just the first one) with enough detail that the
attorney can locate and fix it without re-running the gate. Close with:

- **Overall: READY TO FILE / NOT READY.** Not ready if any gate failed.
- **Fix list**, ordered by how likely each defect is to cause a summary
  denial (record completeness and required-declaration defects first;
  document-hygiene defects last).
- Any `[VERIFY]` items — including the rule 8.486 citations flagged
  above — collected in one list so the attorney can clear them before
  relying on this skill's output as final.

## Execution rules

1. Do not skip a gate because an earlier one failed — run all seven,
   report all findings together.
2. Do not fabricate rule or case citations. If a specific court rule
   needs to be cited (beyond what a prior filing or the backlog entry
   already supplied) and Claude cannot confirm its current text, write
   `[VERIFY]` and name the rule number, don't guess at subdivision
   language.
3. Gate 6 and Gate 7 checks that require XML or PDF-text-layer
   inspection are not satisfied by looking at the rendered document —
   actually unpack the file and inspect the underlying layer. This is
   the entire reason those two gates exist.
4. This is internal, pre-filing work product for attorney review — not
   client-facing. Include the AI-assisted-draft transparency note
   consistent with other KLG skills, but no legal-advice disclaimer is
   needed since this isn't client-facing output.
5. If Gate 1's Register-of-Actions reconciliation or Gate 3's stay-date
   sourcing can't be completed because a required input (see "Required
   inputs" above) wasn't provided, say so explicitly in that gate's
   section rather than marking it PASS by default. A gate that could not
   be run is not the same as a gate that passed.
