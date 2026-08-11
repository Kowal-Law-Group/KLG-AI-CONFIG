---
name: klg-conflict-waiver
description: "Generate client conflict waiver letters for joint representation on KLG letterhead. Use whenever the user says 'conflict waiver', 'conflict letter', 'joint representation waiver', 'dual representation letter', 'conflict disclosure', 'conflict consent', 'waiver letter', 'generate a conflict waiver', 'we need a conflict waiver for', 'prepare the conflict waiver', 'dual rep waiver', or references needing a conflict disclosure and consent letter for representing multiple clients in the same matter. Also triggers when the user says 'new client letter' and the context involves joint representation. Produces a .docx letter on KLG letterhead with the standard six-point disclosure, case-specific conflict examples, waiver/consent language, and signature blocks for each client. Do NOT use for engagement letters, retainer agreements, or non-conflict-related client communications."
---

# KLG Conflict Waiver Letter Generator

Generate conflict disclosure and consent letters for joint
representation of multiple clients in the same matter, on KLG
letterhead.

## Overview

This skill produces a professional conflict waiver letter that:
- Uses the KLG letterhead template (clone-and-edit workflow)
- Addresses the primary client contact
- Identifies all jointly represented clients and the matter
- Discloses six standard conflict-related issues per California
  Rules of Professional Conduct
- Includes case-specific examples of how conflicts might arise
- Provides waiver/consent language with signature blocks for
  each client
- Formats the closing with Tim's signature block

## Phase A: Information Gathering

Before generating the letter, gather all required information.
Use the `ask_user_input` tool where possible for structured
choices, and direct questions for open-ended fields.

### Required Information

Collect the following. If the user provides some of this upfront
(e.g., "generate a conflict waiver for Maxine Gilliam and
Exquisite Affirmations LLC in [case name]"), extract what you
can and ask only for what's missing.

1. **Jointly represented clients** (minimum 2):
   - Full legal name of each client
   - Whether the client is an individual or entity
   - If entity: title of the person signing on its behalf
     (e.g., "President," "Managing Member")
   - Address for each client (can be shared if same address;
     use c/o format if one client is care-of another)
   - Email for each client

2. **Primary addressee**: Which client should the letter be
   addressed to? (Usually the individual who is the contact
   person; the letter will address them by first name in the
   salutation.)

3. **Matter information**:
   - Full case caption (e.g., "Maxine Gilliam and Exquisite
     Affirmations LLC v. Homeowners First LLC")
   - Court (e.g., "Los Angeles County Superior Court")
   - Case number (e.g., "21STPB07775")
   - Appellate case number (if applicable)
   - Whether this is a lawsuit or appeal (determines word
     choice: "lawsuit" vs. "appeal")

4. **Delivery method**: Default "Via Email" (bold). Offer
   alternatives: Via Mail, Via Certified Mail, Hand Delivered.

5. **Date**: Default to today's date. Allow override.

6. **Case-specific conflict scenarios** (optional but
   recommended): Ask the user if there are any particular
   ways conflicts might arise given the facts of this case.
   Examples from past letters include:
   - Individual client vs. entity client having different
     settlement preferences
   - One party being a guarantor while another is the
     primary obligor
   - Different clients having different risk tolerances
   - Insurance allocation disputes between co-clients

   If the user provides scenarios, weave them into the
   "Second" disclosure paragraph as concrete examples.
   If not, use the standard language about litigation and
   settlement strategy differences.

### Gathering Strategy

Present the information request efficiently. If the user
uploaded documents or mentioned a case, extract what you can
from context (Notion Case Portal, past chats, uploaded files).
Then present a summary of what you've gathered and ask the user
to confirm and fill in any gaps.

Example prompt after extracting partial information:

> Here's what I have so far for the conflict waiver:
>
> **Clients:** [Client 1], [Client 2]
> **Matter:** [Case caption], [Court], case no. [number]
> **Date:** [today's date]
> **Delivery:** Via Email
>
> I still need:
> - Addresses and emails for each client
> - Which client is the primary addressee
> - Whether there are any case-specific conflict scenarios
>   to include
>
> Can you fill those in?

## Phase B: Document Generation

Once all information is gathered and confirmed, generate the
letter using the clone-and-edit workflow.

### Step 1: Set Up

```bash
# Copy letterhead template to working directory
cp /mnt/skills/user/klg-conflict-waiver/assets/KLG_Letterhead.docx /home/claude/conflict_waiver_template.docx

# Unpack
python /mnt/skills/public/docx/scripts/office/unpack.py /home/claude/conflict_waiver_template.docx /home/claude/cw_unpacked/
```

### Step 2: Generate and Run the Edit Script

Write a single Python script that performs ALL XML edits to
`document.xml` in one execution. The script must:

1. **Replace the Date bookmark content** with the letter date
2. **Replace the Addressee block** (left table cell) with
   client name(s), address(es), and email(s)
   - For two-column addressee layout (individual + entity),
     populate both table cells
   - For single addressee, populate left cell only
3. **Replace the Subject line** with the Re: line containing
   the case caption, court, and case number(s)
   - Case name should be italic in the Re: line
   - Court and case number in regular text
4. **Replace the salutation** with "Dear [First Name]:" or
   "Dear [First Name] and [First Name]:" as appropriate
5. **Replace the body** with the full letter text (see
   Letter Body Structure below)
6. **Replace the closing** with signature blocks for each
   client, followed by "Very truly yours," and
   "Timothy M. Kowal"
7. **Remove** the "Enclosures" line and filename field

### Letter Body Structure

The letter body uses these styles:
- `BodyText` for first paragraphs after headings/salutation
  (has first-line indent)
- `BodyTextContinued` for continuation paragraphs (has
  first-line indent)

All paragraphs use `BodyText` or `BodyTextContinued` style
with standard first-line indent. The letter has no headings —
it is a continuous letter format.

#### Opening Paragraph

Customize based on the number and type of clients:

> You have requested that our law firm, Kowal Law Group, APC,
> represent both [Client 1] and [Client 2], in the [lawsuit/
> appeal] mentioned above. Whenever an attorney has more than
> one client in the same [lawsuit/appeal], there is a potential
> for conflicts. After discussing the case with you, it appears
> there are no conflicts now. But things may change, and parties
> may wish to pursue different strategies or objectives in the
> case. These and other things may create a potential for a
> future conflict.

For more than two clients, list all names with commas and "and."

#### Professional Conduct Paragraph

> The California Rules of Professional Conduct requires that
> I obtain your informed consent, in writing, that you are
> aware of the potential of future conflicts, and the
> consequences. In other words, while sharing an attorney holds
> out certain advantages to parties whose interests appear to
> be aligned, there may be reasons why it could be a bad idea.
> So I need to disclose to you the ways in which it might be a
> bad idea so you can consider them independently.

#### Six Numbered Disclosures

Each begins with a bold ordinal ("First," "Second," etc.)
followed by the disclosure text. These are the standard six
points — see `references/boilerplate.md` for the exact text.

**Important:** The "Second" disclosure (about litigation and
settlement strategies) is the one most likely to include
case-specific examples. If the user provided case-specific
scenarios, integrate them here.

#### Consent Introduction

> Given there is currently no conflict of interest, we may
> jointly represent the clients in this matter, provided that
> the clients give informed consent in writing. Each client
> should feel free to consult with independent counsel before
> finalizing the client's decision to proceed with the joint
> representation, including whether to sign this conflict
> disclosure and waiver. As the attorney, I need to emphasize
> that each client remains free to seek independent counsel at
> any time even if the client decides to sign this consent.

#### Waiver Language

> With those disclosures having been made, please carefully
> consider consenting to the following waiver:

Then indented waiver text:

> The attorney's current understanding is that each client
> desires to have the attorney jointly represent them in
> connection with the matter referenced above. By signing this
> Disclosure and Consent, each client expressly acknowledges
> that the client:
>
> (1) has carefully read and fully understands the disclosures
> described above;
>
> (2) has carefully considered all of the circumstances and
> potential conflicts described above;
>
> (3) has had the opportunity to consult with independent
> counsel regarding the disclosures and consent in this
> agreement; and
>
> (4) agrees to the joint representation of the clients by the
> attorney in connection with the referenced matter.

#### Signature Blocks

For each client, include:

```
Client Name: [Full Legal Name]

Signed: __________________________________ Date: ___________________
```

If the client is an entity, add the signer's title below
the signature line:

```
Client Name: [Entity Name]

Signed: __________________________________ Date: ___________________
         [Title]
```

#### Closing

```
Very truly yours,

[blank line for signature]

Timothy M. Kowal
```

**Do not** include a signature image — Tim will sign manually
or via e-sign.

### Step 3: Pack and Fix

```bash
# Repack the document
python /mnt/skills/public/docx/scripts/office/pack.py /home/claude/cw_unpacked/ /home/claude/conflict_waiver_output.docx --original /home/claude/conflict_waiver_template.docx

# Fix standalone attribute
python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py /home/claude/conflict_waiver_output.docx
```

### Step 4: Deliver

```bash
cp /home/claude/conflict_waiver_output.docx /mnt/user-data/outputs/
```

Use `present_files` to deliver the document.

### Filename Convention

Name the output file using the pattern:
`[YYYY-MM-DD]_Conflict_Waiver_[Primary Client Last Name].docx`

Example: `2026-03-17_Conflict_Waiver_Gilliam.docx`

## XML Editing Notes

### Key Template Landmarks

The letterhead template uses these bookmarks that the
continuation page header references via REF fields:
- `Date` — letter date (continuation header pulls this)
- `Name` — addressee name (continuation header pulls this)
- `Subject` — Re: line content (continuation header pulls this,
  italicized)
- `Sender` — "Timothy M. Kowal" (closing pulls this)

**Critical:** When replacing bookmark content, preserve the
bookmark start/end tags and the REF field structure so the
continuation page headers auto-populate correctly.

### Style References

- `BodyText` — standard body paragraph with first-line indent
- `BodyTextContinued` — continuation paragraph (same indent)
- `Addressees` — addressee block style
- `Subject` — Re: line style (includes tab after "Re:")

### Smart Quotes

Use XML entities for smart typography:
- `&#x2018;` left single quote
- `&#x2019;` right single quote / apostrophe
- `&#x201C;` left double quote
- `&#x201D;` right double quote
- `&#x2014;` em dash

### Italic Text in Body

For italic text (like case names in citations), wrap in a
separate run with italic formatting:

```xml
<w:r><w:rPr><w:i/><w:iCs/></w:rPr><w:t>Flatt v. Superior Court</w:t></w:r>
<w:r><w:t xml:space="preserve"> (1994) 9 Cal.4th 275, 284.</w:t></w:r>
```

### Bold Text in Body

For bold ordinals ("First," "Second," etc.):

```xml
<w:r><w:rPr><w:b/><w:bCs/></w:rPr><w:t xml:space="preserve">First, </w:t></w:r>
<w:r><w:t>you need to be aware that...</w:t></w:r>
```

## Reference Files

- `references/boilerplate.md` — Full text of the six standard
  disclosure points and all boilerplate language. Read this
  before generating the letter body to ensure exact language
  fidelity.
