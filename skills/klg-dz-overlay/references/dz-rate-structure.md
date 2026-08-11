# DZ Rate Structure

This file defines the rate structure applied by `klg-dz-overlay`
after `klg-case-assessment` classifies a DZ-sourced matter. The
structure is two-tier with asymmetric presentation: Preferred is a
single blended figure; Standard is unblended per personnel level.

The structure is in effect from [pending Tim's conversation with
David — see DZ Restructure Decision Memo, May 18, 2026]. Until
that conversation completes and David accepts the new terms, the
overlay produces output using the new structure for INTERNAL
planning purposes; engagement letters still use existing terms
for matters David and KLG agree to continue under legacy rates.

---

## Tier Rates

### DZ Preferred — $450/hour (blended)

A single blended firm rate. KLG deploys whichever combination of
personnel is appropriate for the work; the rate is uniform.

The bill does not break out per-attorney hours. David receives a
single line entry per time block at the blended rate. This is the
relationship-rate framing — one number, no granularity.

### DZ Standard — unblended

Three rate lines:

| Personnel | Rate |
|---|---|
| Timothy Kowal | $650/hour |
| Other Attorneys | $475–$550/hour |
| Paralegal | $175/hour |

The bill breaks out per-personnel hours and rates. David sees what
each level of work costs.

---

## Asymmetry Rationale

The two-tier presentation is deliberately asymmetric. Both
elements of the asymmetry carry signaling work.

### Why Preferred is blended

A blended figure is what a relationship rate looks like — one
number, no breakdown. It signals trust and simplicity. David does
not need to think about which attorney is on the matter or what
the per-personnel costs are. The relationship absorbs the
internal staffing question.

For Preferred matters specifically, the blended approach also
removes the per-attorney transparency that has historically
reinforced David's mental model of "Tim plus cheap team labor."
On a Preferred matter, the firm is the unit of value. The rate
reflects that.

### Why Standard is unblended

Standard is market-adjacent. The unblended presentation makes
Tim's higher rate visible on the bill, which sends two signals:

1. **Cost signal.** When David sees that Tim's hours cost $650
   each, he is reminded that he is paying for senior strategic
   work. If David wants the cost to come down, the path is to
   route matters as Preferred (which means bringing them in
   early enough for normal pipeline and not insisting on
   urgent-or-difficult posture).

2. **Routing signal.** When David sees that other attorneys cost
   $475–$550 per hour and paralegal time is $175, he sees that
   KLG can deploy a less-expensive labor mix when the matter
   allows it. The transition over time is for more of the
   Standard work to be done by other attorneys — which is good
   for KLG (Tim's time freed up) and good for David (lower
   effective per-matter cost).

### Dynamic incentive

The unblended Standard creates a dynamic incentive that compounds
over time. Today, with Tim doing most of the hours on hard
matters, the effective per-matter rate on Standard work runs
high (Tim at $650 across 70%+ of the work). As the firm
transition matures and Ted, Richard, and other attorneys absorb
more of the Standard load, the deployment mix shifts and the
effective rate drops without any change in the rate lines
themselves.

David benefits from KLG's transition success rather than just
being told about it. The structure rewards the transition.

### Fee-motion defense (incidental)

Unblended Standard rates are easier to defend in the rare
scenario where a DZ matter goes to fee motion (statutory recovery,
sanctions, fee-shifting). Blended rates draw judicial
skepticism; itemized per-attorney rates are the convention.

Preferred matters are unlikely to ever face fee-motion review
(no court will see KLG's billing breakdown on ghostwritten work),
so the blended approach there is fine.

---

## Effective Rate Math

For attorney planning, here are illustrative effective rates
under Standard given different deployment mixes. The actual
deployment mix on any given matter depends on the work required.

**Today's typical Standard mix (Tim-heavy):**
- Tim 70% × $650 = $455
- Other attorneys 20% × $510 (midpoint) = $102
- Paralegal 10% × $175 = $17.50
- **Effective rate: ~$575/hour**

**Mid-transition Standard mix (more team involvement):**
- Tim 40% × $650 = $260
- Other attorneys 50% × $510 = $255
- Paralegal 10% × $175 = $17.50
- **Effective rate: ~$533/hour**

**Mature Standard mix (Tim as architect, team executes):**
- Tim 20% × $650 = $130
- Other attorneys 60% × $510 = $306
- Paralegal 20% × $175 = $35
- **Effective rate: ~$471/hour**

The numbers move in the right direction as the firm transition
matures. David sees the benefit on every Standard matter.

---

## Caps and Flat Fees

### Caps

Caps available at either tier when requested. Apply the universal
rate-and-cap rule from `klg-case-assessment-standards.md` Section
6.3:

- If a cap is requested at Preferred ($450 blended), set at the
  upper end of plausible work.
- If a cap is requested at Standard (unblended), set at the
  upper end of plausible work using a Tim-heavy deployment
  assumption (since the actual mix may skew toward Tim
  initially).
- Never accept a "low rate + low cap" stacking arrangement. If
  the requested cap is below the cost estimate, STOP and flag
  for attorney decision.

For DZ matters specifically, the historical pattern has been
caps below the cost estimate (David seeking margin protection).
The overlay should explicitly call this out: "Requested cap is
$X. Cost estimate is $Y. This is a low-cap proposal that
combined with the relationship rate would create the 'hurt
twice' problem. Recommend either raising the cap to $Y or
moving the matter to Standard rates."

### Flat fees

Available at either tier for defined deliverables (specific
brief, specific petition, specific writ). Paid in advance. Not
paid on completion. KLG keeps the upside on efficient execution.

For Preferred matters, a flat fee is computed from a
Work-Breakdown Structure at $450/hour blended. For Standard
matters, a flat fee is computed from a WBS at the unblended
rates and presented as a single number.

---

## Attribution

KLG attribution on filings is the default at both tiers.
Invisibility is available as a priced line item.

### Default (attribution visible)

KLG appears as counsel of record on filings. David's name appears
alongside or in place of KLG's based on the matter; this is a
case-by-case decision based on appearance practice but does not
change KLG's attribution.

### Invisibility (priced)

David can request invisibility on a per-matter basis. The
surcharge is [TBD — currently $250–$500 per filing OR 5–10%
premium on matter fee; final number locked before the conversation
with David].

Until the surcharge is finalized, the overlay produces a
placeholder and flags it for attorney completion. Do not silently
default to invisibility without applying the surcharge.

The invisibility surcharge reflects three real costs to KLG:

1. **Reputational opportunity cost.** On filings that demonstrate
   high-quality work (Christopher U. petition, Hoopes
   supersedeas, etc.), KLG loses the reputational benefit of
   public attribution.
2. **Marketing-content cost.** Invisible matters cannot be cited
   on the KLG website, in BD content, or in podcast episodes.
3. **Compliance cost.** Maintaining proper attribution on
   internal records while suppressing it on external filings
   requires additional administrative discipline.

The surcharge prices these costs explicitly rather than absorbing
them as relationship overhead.

---

## What the Overlay Outputs

The DZ Engagement Summary produced by `klg-dz-overlay` includes
the rate quote in Section 3 (Rate Structure):

**For Preferred matters:**

> Rate: $450/hour (blended). KLG deploys whichever combination
> of personnel is appropriate; bill shows a single line per time
> block at the blended rate.

**For Standard matters:**

> Rates (unblended):
> - Timothy Kowal: $650/hour
> - Other Attorneys: $475–$550/hour
> - Paralegal: $175/hour
>
> Bill shows per-personnel breakdown.

Section 4 (Cost Estimate) applies the rates to the
Work-Breakdown Structure for the deliverable.
