---
name: klg-dz-overlay
description: "Apply the DZ-specific engagement-structure overlay to potential client matters referred by David Zarmi. Runs after klg-case-assessment completes. Triggers when the user says 'run the DZ overlay', 'DZ engagement summary', 'classify the DZ matter', 'DZ tier classification', or after klg-case-assessment prompts to proceed with the overlay on a DZ-sourced matter. Produces a DZ Engagement Summary that classifies the matter as DZ Preferred (blended firm rate) or DZ Standard (per-attorney unblended rates), sets attribution terms, and articulates the two engagement-letter provisions (out-of-hours communications, scope-and-revisions). Output feeds into the engagement letter draft. Do NOT use for non-DZ matters or for the underlying case-merits evaluation — those are handled by klg-case-assessment."
---

# KLG DZ Engagement Overlay

## Purpose

This skill applies the DZ-specific engagement-structure layer to
matters referred by David Zarmi. It runs AFTER `klg-case-assessment`
has produced the universal merits/equities/ability-to-pay analysis.
It does NOT re-evaluate the case on the merits.

Output is a DZ Engagement Summary that:

1. Classifies the matter into DZ Preferred or DZ Standard tier.
2. Quotes the applicable rate structure.
3. States the attribution decision (default visible; invisibility
   available as priced line item).
4. Articulates the two universal engagement-letter provisions as
   they apply to this matter (out-of-hours communications;
   scope-and-revisions).
5. Sets the routing-and-communication terms (intake routes through
   the paralegal; David's response-expectation discipline).

The summary is a Notion page in the matter's project workspace, and
its contents feed into the engagement letter draft.

## When to Run

Run this skill when ALL of the following are true:

- `klg-case-assessment` has been completed for the matter (or the
  matter is already at a stage past assessment).
- The referral source is David Zarmi.
- The user wants to proceed toward an engagement (i.e., the
  classification is Promising or Borderline, and the attorney
  decision to take the case is in place or pending).

Do NOT run this skill:

- For non-DZ matters. The engagement structure for non-DZ matters
  is governed entirely by the universal principles in
  `klg-case-assessment` Section 12. No overlay needed.
- Before `klg-case-assessment` is complete. The overlay assumes the
  merits analysis is already in hand.
- For declined matters. If the case is being declined, no
  engagement structure is needed.

## Required Context

Before producing output, read:

1. `references/dz-tier-rubric.md` — Tier classification rubric:
   what makes a matter Preferred vs. Standard, with worked examples
   and edge cases.
2. `references/dz-rate-structure.md` — Current DZ rate structure
   (Preferred blended, Standard unblended) with the rationale for
   the asymmetry and the dynamic-incentive logic.
3. `references/dz-engagement-letter-provisions.md` — Standard
   language for the out-of-hours communications provision, the
   scope-and-revisions provision, the attribution clause, and the
   communication-routing clause.

If any of these reference files are missing, prompt the user to
provide them. The skill cannot produce compliant output without
the rubric and rate structure.

## Required Inputs

- The completed case assessment memo (uploaded or referenced by
  Notion URL).
- Confirmation that the referral source is David Zarmi.
- Any pre-engagement communications with David that indicate
  expectations on timeline, cap, attribution, or other terms.

If the user does not provide the case assessment, ask for it.
Do not attempt to classify a matter on the merits independently.

## Project Preflight

This skill produces a deliverable that links to the existing Case
Project for the matter (created by `klg-case-assessment`). It does
NOT create a separate project.

1. Search the Projects database for the matter's existing
   Case Project (created during case assessment).
2. Link the DZ Engagement Summary Notion page to that project via
   the Projects relation on the Research database.
3. If no Case Project exists yet, ask the user whether to run this
   overlay before or after the case assessment is logged. Default
   is to wait for the case assessment.

---

## Workflow

### Phase 0 — Three Gating Questions

Answer these three before any merits deep-dive or hours estimate,
for every DZ-sourced potential matter. Keep each answer pitch-length
— this is a framing gate, not a memo.

1. **What is the case about?** The 30-second elevator pitch, and
   why the client is right on the law and the equities. Just the
   pitch, not a full assessment.
2. **What is David (or trial counsel) asking?** What specific
   problem are they dealing with right now, and what is their idea
   for addressing it?
3. **Does this project risk trapping Tim into a Tim-only
   representation?** Tim is the alpha lion of the firm — he can't
   spend his time chasing squirrels; he has to bring home big game
   to keep the team fed. Assess whether this matter is delegable to
   the team and scales into something substantial (an appeal, a
   repeat referral stream, precedent-setting work), or whether it
   locks Tim personally into low-leverage solo effort. Give a clear
   read: gazelle or squirrel, and whether the work is delegable.

Billing data backs Question 3's premise: Tim's personal time on DZ
matters rose from roughly 15% of his hours (2025) to roughly 27%
(2026), while DZ's share of firm revenue held flat around 15–16%.
The work is becoming less delegable, not more — that divergence
(rising Tim-hours per unit of revenue) is exactly the signal this
question screens for.

Present the three answers together before moving to Phase 1.

### Phase 1 — Tier Classification

Apply the rubric in `references/dz-tier-rubric.md`. The two-tier
question is binary: Preferred or Standard.

**DZ Preferred** applies when EITHER of the following is true:

1. **Normal timeline.** The matter has briefing deadlines or oral
   argument dates that allow KLG to engage at least one
   extension request, and the engagement window gives the firm's
   normal pipeline (research, brief drafting, internal review)
   adequate runway. Specifically, KLG is brought in before or
   within the original briefing deadline, with the ability to
   secure 60-day extensions if needed.

2. **Interesting matter.** The case presents an issue aligned with
   KLG practice values — constitutional, civil-procedural,
   appealability, anti-SLAPP, structural-error, or other matters
   where KLG has an editorial or doctrinal interest beyond
   billable work. The Hoopes constitutional matter and the
   Christopher U. petition for review are paradigm examples.
   This is case-by-case at intake, not categorical. Specifically,
   petitions for review and petitions for rehearing are NOT
   categorically interesting — they tend to come on short fuses
   and often arise on the hard matters.

**DZ Standard** applies when BOTH of the following are true:

1. **Urgent or unusually difficult.** Either (a) urgent — KLG must
   begin substantive work without the normal-pipeline lead time
   (briefing deadlines compressed by prior representation, oral
   argument set within the next 60 days, expedited writ
   timelines); OR (b) unusually difficult at intake — no clear
   path to a colorable issue without Tim's personal strategic
   involvement to identify and frame the appellate theory.

2. **Not categorically interesting.** The matter does not
   independently qualify as Preferred under the "interesting"
   prong.

If only the urgency/difficulty prong is met, the matter is
Standard. If only the interesting prong is met, the matter is
Preferred (the urgency or difficulty is absorbed into the
Preferred rate as part of the relationship investment in the
interesting work). If both are met, default to Preferred — KLG
wants to encourage interesting matters, and the relationship rate
is the right vehicle for that.

State the classification clearly with the reasoning.

### Phase 2 — Rate Structure Quote

Based on the tier, quote the applicable rate structure from
`references/dz-rate-structure.md`:

**DZ Preferred — $450/hour (blended).**
Single rate; KLG deploys whichever combination of personnel is
appropriate for the work. No per-attorney breakdown on the bill.

**DZ Standard — unblended:**
- Timothy Kowal: $650/hour
- Other attorneys: $475–$550/hour
- Paralegal: $175/hour

Bill shows per-personnel breakdown. The asymmetry is deliberate
— Preferred is the relationship-rate framing; Standard is
market-adjacent and itemized so the labor mix is visible.

### Phase 3 — Cap, Flat-Fee, and Estimate Decision

Apply the universal rate-and-cap interaction rule from
`klg-case-assessment-standards.md` Section 6.3:

- If a cap is requested at Preferred, set at the upper end of
  plausible work; never below the cost estimate.
- If a cap is requested at Standard, set at the upper end of
  plausible work; never below the cost estimate.
- If a low cap and a relationship rate are both requested,
  STOP and flag for attorney decision. Never accept both.

For flat fees:

- Available at either tier for defined deliverables (specific
  brief, specific petition, specific writ).
- Paid in advance. Not paid on completion.
- KLG keeps the upside on efficient execution.

Produce a cost estimate range using the Work Breakdown Structure
from `klg-case-assessment-standards.md` Section 2, applying the
DZ tier rates (not the standard rate sheet).

### Phase 4 — Attribution Decision

KLG attribution on filings is the default for all DZ matters.
Invisibility — David's preferred-historical default — is now
available as a priced line item, not as the default.

The invisibility surcharge is [TBD — currently parked for the
David conversation; expected to land at $250–$500 per filing or
5–10% premium on matter fee]. Until the surcharge is locked, the
overlay produces a placeholder and flags it for attorney
finalization.

Document the attribution decision explicitly in the summary:

- Default: KLG attribution on filings.
- Invisibility (if requested): priced at [surcharge], applied to
  each filing as a separate line item.

### Phase 5 — Engagement Letter Provisions

Articulate the two universal provisions for this matter:

**Out-of-hours communications.** Standard language from
`references/dz-engagement-letter-provisions.md`. Notes that the
provision applies even if past practice between Tim and David has
been more responsive to late-evening emails. The provision is
now the rule, not the aspiration.

**Scope and revisions.** Standard language from
`references/dz-engagement-letter-provisions.md`. Important for
DZ matters specifically because of the Petersen and Hoopes
patterns — DZ clients have a history of multiple revision rounds.
The provision caps included revisions at one round and bills
additional rounds hourly without cap.

### Phase 6 — Routing and Communication Terms

State the routing terms:

- Single point of contact for case intake and document delivery
  is the designated paralegal (default: Brittney Bishop). Tim is
  available for substantive legal questions.
- Documents come to the team first, not Tim personally.
- David is expected to respond to team inquiries with the same
  promptness he expects from KLG. This goes both directions.
- Matter communications run through the matter-specific Slack
  channel and the Notion project page for KLG's internal record.
  External communications with David and his client use email.

These terms are part of the engagement structure but not
necessarily printed in the engagement letter — they are the
operational ground rules for the matter.

---

## Output: DZ Engagement Summary

Produce a Notion page in the matter's project workspace with the
following structure:

### Page Title

`DZ Engagement Summary — [Matter Name] ([Case No.])`

### Page Content

**Section 1 — Matter Overview**
- Matter name and case number
- Referral source: David Zarmi
- Case-assessment classification (Promising / Borderline / Decline)
- Link to the case assessment memo

**Section 2 — Tier Classification**
- DZ Preferred OR DZ Standard
- Reasoning (which prong of the rubric applies; one paragraph)

**Section 3 — Rate Structure**
- The applicable rate(s) for the tier
- Whether a cap is proposed and if so at what amount
- Whether a flat fee is proposed and if so at what amount

**Section 4 — Cost Estimate**
- Work Breakdown Structure for the deliverable
- Total range (base + multipliers + 10–20% buffer)
- At DZ tier rates

**Section 5 — Attribution Decision**
- Default (KLG attributed on filings) OR invisibility (with
  surcharge line item)

**Section 6 — Engagement Letter Provisions**
- Out-of-hours communications provision (verbatim language)
- Scope-and-revisions provision (verbatim language)
- Attribution clause (if invisibility chosen)
- Communication-routing clause

**Section 7 — Open Items & Next Steps**
- Anything pending attorney decision (invisibility surcharge,
  cap negotiation, etc.)
- Next step: engagement letter draft or further intake discussion

### Output Format

Notion page as primary deliverable. The Notion page is the source
of truth for the engagement structure and is linked from the
Case Project page.

If the user requests a `.docx` version (e.g., for the engagement
letter file), produce it on the KLG letterhead template, following
the same workflow as `klg-case-assessment` for `.docx` generation.

---

## Execution Rules

1. Never run this skill without a completed case assessment in hand.
   If the user requests the overlay without an assessment, prompt:
   "I need the case assessment first. Should we run
   `klg-case-assessment` now, or do you have an existing assessment
   I can read?"

2. Never re-evaluate the merits. The case assessment is authoritative
   on merits, equities, ability to pay, and practice alignment. The
   overlay only adds the engagement structure layer.

3. Apply the tier rubric strictly. The rubric is documented in
   `references/dz-tier-rubric.md`. If a matter sits on the boundary,
   default to Standard (the more protective tier for KLG) and flag
   the borderline case for attorney decision.

4. Flag every "low rate + low cap" stacking attempt. This is the
   universal rule from `klg-case-assessment-standards.md` Section 6.3
   and it applies to DZ matters with extra force, because the
   stacking pattern is the historical norm in DZ engagements.

5. The invisibility surcharge is pending finalization. Until Tim
   locks the number, produce placeholders and flag for attorney
   completion.

6. The two engagement letter provisions (out-of-hours communications;
   scope-and-revisions) are MANDATORY on every DZ engagement.
   They do not vary by tier and they do not get waived.

7. After producing the DZ Engagement Summary, prompt:
   "The DZ Engagement Summary is ready. Next step is the engagement
   letter draft. Should I proceed with the letter now, or wait for
   attorney review of this summary first?"

8. Update the Case Project page to reflect that the DZ overlay has
   been completed. Add a relation to the DZ Engagement Summary
   Notion page.

9. Log the matter classification to the AI OS Improvement Backlog
   if it surfaces a rubric edge case that isn't covered by the
   current `references/dz-tier-rubric.md`. The rubric should evolve
   with experience.
