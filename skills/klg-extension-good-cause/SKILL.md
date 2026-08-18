---
name: klg-extension-good-cause
description: >
  Draft the good-cause / reasons section of an appellate extension-
  of-time application — Court of Appeal (APP-006 + APP-031A
  continuation) or U.S. Supreme Court cert extension. Assembles the
  item-9 narrative, addresses the rule 8.63 good-cause factors (or
  the Supreme Court Rule 30 analog for cert), pulls the live
  competing-deadline list, leads with what's new since the last
  grant, genericizes confidential/DZ matters, and checks cross-
  matter factual consistency on recurring facts. Use whenever the
  user says "draft an extension," "extension of time," "good cause
  section," "APP-006," "cert extension," "extension application,"
  "we need more time," "ask for an extension," "reply brief
  extension," or references a court or clerk granting/requiring an
  extension request. NOT for the merits of the underlying brief or
  for general deadline tracking — this skill drafts one section of
  one form/application.
---

# KLG Extension-of-Time Good-Cause Drafter

## Purpose

KLG has hand-drafted the good-cause section of extension
applications at least three times in two months (Koppi v. Brown
second and third reply-brief extensions; the HB Voter ID SCOTUS
cert extension) with no reusable scaffolding. The rule 8.63
good-cause factors — and the Supreme Court Rule 30 analog for cert
— don't change between requests. Only the matter-specific
obligations, the competing-deadline list, and what's new since the
last grant change. That's a templatable task, and inconsistency
here carries real cost: it's a filing read by a court, on a request
asking that court for leniency.

This skill drafts the good-cause / reasons narrative only. It does
not draft the rest of the extension application (captions, proof
of service, signature blocks) unless the user asks for the full
document.

## Two Modes

**Court of Appeal mode (APP-006).** Assembles the item-9 narrative
plus the APP-031A continuation list (used when the competing-matter
list is too long for the form's item 9 field). Addresses the rule
8.63 good-cause factors and affirmatively states the absence of
prejudice — the form's own prompt.

**U.S. Supreme Court cert mode.** Same narrative logic, addressed to
the Rule 30 extension standard rather than rule 8.63. Use when the
matter is a certiorari petition or a SCOTUS filing deadline.

Infer the mode from context (which court, which form, which brief
type) or ask if genuinely ambiguous.

## Required Inputs

Before drafting, gather:

1. **The prior extension application(s) for this matter**, if any
   — pull from the matter's SharePoint folder. Each new request
   must build on, not contradict, what was previously represented
   to the court. If a prior application isn't readily found, ask
   the user for it or confirm this is the first request.
2. **The live competing-deadline list** — pull from Motion (via
   Zapier Find Task) or the Notion matter set, rather than asking
   the user to re-type it. Cross-reference against what active
   deadlines genuinely exist right now.
3. **What's new since the court's last grant** — the specific
   development (new filing, new matter, health issue, record delay,
   etc.) driving this request.
4. **Confidentiality flags** — which competing matters, if any, are
   confidential or DZ-sourced and need generic description rather
   than naming.

## Drafting Rules

**Lead with what's new.** Open the narrative with the development
that has changed since the prior grant (if any), not with a
recitation of the standing caseload. Repeating the same matters
across successive requests invites a "no further extensions" order
— this is exactly what happened on the Koppi third request, where
five matters from the April list reappeared verbatim on the June
list. De-emphasize or omit matters already cited in the prior
application unless they still carry live, unresolved weight.

**Handle confidential/DZ matters generically.** Never name a
confidential or DZ-sourced matter in the narrative. Describe it by
function and posture instead — e.g., "an emergency writ matter in a
separate appeal" — following the pattern used in the Koppi second-
extension draft's treatment of the Diller supersedeas matter.

**Enforce cross-matter factual consistency.** Any fact that recurs
across filings (a death date, a filing date, a procedural posture)
must match what was represented in the prior application for that
same matter. Example: Ryan Merker's death was stated as March 2026
in the Huntington Beach cert extension — any later filing referring
to that fact must not drift to a different month. If the user's
draft or the prior application conflicts with a fact stated
elsewhere, flag the discrepancy rather than silently picking one
version.

**Address the good-cause factors affirmatively**, not just by
listing competing obligations:
- The specific reason more time is needed (not merely "counsel is
  busy," but the concrete obligation or development).
- Absence of prejudice to the opposing party — state this
  affirmatively; the form prompts for it and a bare recitation of
  workload without this element reads as thin.
- For a second or subsequent request, address why the additional
  time wasn't anticipated in the prior request, if it wasn't.

## Output

Draft the narrative section in the form's own numbered-item
structure (item 9 for APP-006, continuation list on APP-031A when
needed) or, for cert mode, in the structure the Rule 30 application
uses. Deliver as a Word document via the docx skill, or as inline
text for the user to paste into the existing form, per the user's
preference — ask if unclear.

Flag, rather than resolve silently: any competing-deadline conflict
that looks illogical (a matter's deadline already passed, or is
inconsistent with Motion), any fact that appears to drift from a
prior filing, and any judgment call about how much of the standing
caseload to include versus omit. This is a court filing; the
attorney reviews and signs off before it goes out.
