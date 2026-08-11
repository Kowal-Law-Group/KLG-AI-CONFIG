# Client Revision Review — Detailed Workflow

This reference file contains the detailed instructions for
Phase 2D (Path D — Client Revision Review) of the brief
elevation skill. Read this file when the user indicates the
client has returned a brief with comments or requested revisions.

---

## Step D.1: Extract Client Feedback

Read the uploaded .docx using the unpack workflow:

```bash
python /mnt/skills/public/docx/scripts/office/unpack.py client-brief.docx unpacked/
```

Extract ALL client feedback from the document:

**Word comments (balloon annotations):**
- Parse `unpacked/word/comments.xml` for `<w:comment>` elements
- For each comment: extract the author, date, comment text, and
  the commented-on text range (identified by `w:commentRangeStart`
  / `w:commentRangeEnd` markers in `document.xml`)
- Also check `unpacked/word/commentsExtended.xml` if present
  (contains reply threading)

**Tracked changes:**
- Parse `unpacked/word/document.xml` for `<w:ins>` and `<w:del>`
  elements
- For each: extract the author, date, and the inserted/deleted text
- Distinguish client-authored changes from Claude-authored or
  attorney-authored changes by the `w:author` attribute
- If the brief previously went through a KLG review pass, Claude's
  tracked changes may still be present — do not re-process those

**Inline annotations (colored text, highlighted text, marginal notes):**
- Look for text runs with unusual formatting that differs from the
  document's base style — these may be client annotations
- Highlight color (`<w:highlight>`) or font color changes
  (`<w:color>`) applied to specific passages
- If detected, flag these for the user: "I found what appears to be
  inline annotations (highlighted/colored text). Should I treat
  these as client comments?"

**Plain text notes:**
- If the client has typed notes directly into the text (e.g.,
  "[CLIENT NOTE: ...]" or text in brackets), detect and extract these

Compile a **Client Feedback Inventory** — a numbered list of every
piece of client feedback with:
- Item number
- Type (comment / tracked change / inline annotation / text note)
- Location in brief (section heading + approximate page/paragraph)
- The brief text the comment refers to (quoted, max ~2 sentences)
- The client's comment or requested change

---

## Step D.2: Present the Inventory for Review

Present the inventory to the user in a clear, scannable format:

```
CLIENT FEEDBACK INVENTORY — [Case Name]
[X] items found ([Y] comments, [Z] tracked changes, etc.)

  #1 [COMMENT] — Section II.A, ¶3
  Brief text: "The trial court abused its discretion when it..."
  Client says: "Why didn't we cite Smith v. Jones here? That
  case is directly on point."
  ⚡ Sensitivity: This questions our case selection.

  #2 [TRACKED CHANGE] — Introduction, ¶1
  Client deleted: "The central question in this appeal is..."
  Client inserted: "This appeal presents the critical issue of..."
  ⚡ Sensitivity: None — stylistic preference.

  #3 [COMMENT] — Section III, ¶5
  Brief text: "Plaintiff failed to exhaust administrative remedies."
  Client says: "This is wrong — we DID exhaust. See the June 12
  letter attached to our complaint."
  ⚡ Sensitivity: Client is correcting a factual claim.

  [etc.]
```

**Sensitivity flagging:** Mark items with ⚡ where:
- The client criticizes the quality of our work
- The client says we got something wrong
- The client questions why we omitted something
- The client expresses frustration or displeasure
- The client requests an argument that may be legally unsound

After presenting the inventory, ask:

```
I've cataloged [X] items of client feedback. Before I process
them, do you want to:

1. Walk through each one together (recommended for items
   flagged ⚡ sensitive — I'll help you evaluate and draft
   the client response for each)
2. Let me process them all and present my recommendations
   (faster — you review my calls after)
3. Flag specific items you want to discuss first, then
   I'll process the rest

Which approach?
```

---

## Step D.3: Evaluate Each Item

For each item in the inventory, apply this evaluation framework:

**Category A — Incorporate (good idea, strategically sound):**
- Client's suggested language is clear, accurate, and improves
  the brief or is at least neutral
- Client provides a factual correction backed by record evidence
- Client's stylistic preference doesn't weaken the argument
- Client identifies a genuinely missing authority or argument

**Category B — Incorporate with modification (right instinct,
needs legal refinement):**
- Client's suggestion points to a real issue but the proposed
  language is legally imprecise or could create problems
- Client wants to add an argument that has merit but needs proper
  framing and authority support
- Client's factual correction is partially right but overstated

**Category C — Decline (not strategically sound):**
- Client wants to add an argument that is legally incorrect,
  waived, or would undermine credibility
- Client's proposed language overstates the record or
  mischaracterizes authority
- Client wants to remove a necessary concession or qualification
  that protects the brief's integrity
- Client's suggestion would violate court rules or ethical
  obligations
- Client's preferred framing would weaken the argument even
  though it feels emotionally satisfying

**Category D — Needs attorney judgment (cannot resolve without
the attorney's input):**
- Client's comment raises a factual question that requires
  record verification
- Client requests a strategic shift that changes the brief's
  overall theory
- The right call depends on information Claude doesn't have
- The client's frustration level makes this a relationship
  management issue beyond the brief itself

---

## Step D.4: Sensitive Item Walkthrough

For items flagged ⚡ sensitive — especially where the client is
critical of our work — Claude walks the user through drafting
the response. The goal: candid, professional, and firm without
being defensive or admitting fault where none exists.

### Framework for Responding to Client Criticism

First, identify the actual situation (help the user think through
this):

1. **We made an error.** If we genuinely got something wrong —
   own it cleanly. "You're right — we should have cited Smith v.
   Jones. We've added it at [location]." No over-apologizing,
   no excuses. Just fix it.

2. **The client didn't give us the information.** This is common.
   The client says "you should have included X" but never told us
   about X, or provided the documents late, or mentioned it only
   in passing. Frame the response as: "Thank you for flagging
   this — we didn't have [the June 12 letter / this background /
   etc.] when we drafted this section. Now that we have it, we've
   incorporated it at [location]." Do NOT say "you didn't tell
   us" — frame it as information we now have that we didn't
   before.

3. **The client is wrong on the law.** The client wants an
   argument that doesn't work, or wants to cite a case that
   doesn't say what they think it says. Be respectful but clear:
   "We considered [the client's suggestion] but ultimately
   concluded that [reason]. [Authority] holds that [rule], which
   means [explanation]. Including this argument could [risk:
   undermine credibility / invite a damaging response / etc.].
   We recommend keeping the current approach because [reason]."

4. **It's a judgment call and we chose differently.** Sometimes
   the client's instinct is reasonable but we went another way
   for good reasons. Explain the reasoning without being
   dismissive: "This is a fair point, and we considered [their
   approach]. We went with [our approach] because [strategic
   reason]. That said, if you feel strongly about this, we can
   [offer a compromise or alternative]."

5. **The client is venting.** Sometimes the comment is really
   about frustration with the case, the opposing party, or the
   process — not about the brief. Acknowledge the frustration
   without changing the brief in ways that would weaken it:
   "We understand the frustration with [situation]. The brief
   addresses this at [location] by [how we handle it]. We've
   [small accommodation if possible] to give this more emphasis."

### Presenting Sensitive Items

For each sensitive item, Claude presents:

```
ITEM #[X] — [Brief description]

Client's comment: "[quoted]"

What's actually going on here:
  [Claude's assessment of which category above applies,
  with reasoning]

Draft response for the client:
  "[Proposed language for the email synopsis]"

Incorporated: [Yes / Yes with modifications / No]
```

Wait for the user's approval or edits on each sensitive item
before finalizing. The user may have context Claude doesn't —
perhaps the client DID provide the information, or perhaps
there's a relationship dynamic that affects tone.

---

## Step D.5: Produce the Redlined .docx

After all items are evaluated and the user has approved the
disposition of sensitive items, produce a redlined version of
the brief:

1. Copy the client's marked-up brief to the working directory
2. Unpack it
3. For each item:

   **Category A (incorporate as-is):**
   - If the client used tracked changes: accept them (remove
     the tracking markup and keep the client's text)
   - If the client left a comment with suggested language:
     implement the change as a new tracked change authored by
     "KLG — Rev. Review" and resolve/delete the client's comment
   - If the client left a comment without specific language:
     implement the appropriate change as a tracked change
     authored by "KLG — Rev. Review"

   **Category B (incorporate with modification):**
   - If the client used tracked changes: reject the client's
     version and insert the refined version as a tracked change
     authored by "KLG — Rev. Review"
   - If the client left a comment: implement the refined version
     as a tracked change and add a reply comment explaining the
     modification

   **Category C (decline):**
   - If the client used tracked changes: reject them (remove
     the client's `<w:ins>` content and restore the `<w:del>`
     content)
   - If the client left a comment: add a reply comment authored
     by "KLG — Rev. Review" with a brief note: "Not incorporated
     — see email for explanation."
   - Do NOT silently ignore declined items — they must be visibly
     addressed in the document

   **Category D (needs attorney judgment):**
   - Add a comment authored by "KLG — Rev. Review" flagging the
     item: "⚠️ Requires attorney review — see email synopsis
     item #[X]."

4. Repack and validate:
   ```bash
   python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ brief-REVISED.docx --original client-brief.docx
   python /mnt/skills/public/docx/scripts/office/validate.py brief-REVISED.docx
   ```

5. Deliver as `[case-name]-REVISED.docx`

**Author attribution:** Use "KLG — Rev. Review" as the author
for all tracked changes and comments produced in this path.
This distinguishes client revision review edits from elevation
edits ("Claude — Brief Elevation") and style check edits
("Claude"), so the attorney can see the provenance of each
change in Word's review pane.

---

## Step D.6: Generate the Email Synopsis

Produce a paste-ready email synopsis the attorney can send (or
adapt) to the client. Format as a numbered list corresponding to
the inventory numbers. The synopsis should be professional, warm,
and direct.

**Email synopsis format:**

```
Subject: [Case Name] — Response to Your Comments on [Brief Type]

[Client name],

Thank you for your careful review of the [brief type]. Your
input is valuable — several of your suggestions strengthened
the brief, and we've incorporated them. Below is a summary of
each item and how we addressed it.

1. [LOCATION] — [Brief description of the commented text]
   Your comment: [Concise paraphrase of what the client said]
   Our response: [What we did and why]
   Status: Incorporated / Incorporated with modification /
   Not incorporated

2. [LOCATION] — [Brief description]
   Your comment: [Paraphrase]
   Our response: [Explanation]
   Status: [Status]

[Continue for all items]

The revised brief is attached with tracked changes so you can
see exactly what was modified. Please let us know if you have
any questions or would like to discuss any of these items.

[Closing]
```

**Tone rules for the synopsis:**
- Start by thanking the client and acknowledging that their
  review improved the brief (if it did — don't say this if
  most items were declined)
- For incorporated items: brief and positive. "Good catch —
  incorporated." or "We've added this citation at [location]."
- For modified items: explain what we kept and what we refined.
  "We incorporated your suggestion with some refinement to
  [reason]."
- For declined items: firm, professional, and substantive. Never
  dismissive. Always explain the strategic or legal reason.
  Never say "we disagree" without saying why.
- For items where the client was critical of our work: use the
  language drafted in Step D.4, reviewed by the attorney
- Never be defensive, never grovel, never blame the client
- If multiple items are related, group them: "Items 3, 5, and
  7 all relate to [topic]. We've [summary of approach]."

Present the complete synopsis to the user for review before
finalizing. The user may want to adjust tone, add context, or
handle certain items differently based on the client relationship.

---

## Step D.7: Delivery

Present both deliverables:

```
═══════════════════════════════════════════════════
✅ CLIENT REVISION REVIEW COMPLETE
═══════════════════════════════════════════════════

DELIVERABLES:

1. REDLINED BRIEF: [filename]-REVISED.docx
   [X] changes incorporated, [Y] declined, [Z] modified
   Author: "KLG — Rev. Review" for all new tracked changes
   Open in Word → Review tab to accept/reject

2. EMAIL SYNOPSIS: Ready to paste (displayed above)
   Review and adjust tone as needed before sending

NEXT STEPS:

1. Review the redlined brief in Word — accept/reject changes
2. Review the email synopsis — adjust tone/wording as needed
3. Once the brief is clean, consider running a style-guide
   check: "Please run a style guide check on this brief."

⏱️ If additional client revisions come back, upload the new
version and say: "Client sent back another round of comments."
═══════════════════════════════════════════════════
```
