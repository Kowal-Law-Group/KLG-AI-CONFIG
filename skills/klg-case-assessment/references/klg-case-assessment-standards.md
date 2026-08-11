# KLG Case Assessment Standards

This file defines the analytical framework, traffic light criteria,
cost anchors, current rate sheet, and engagement structure principles
used in initial case assessments. It applies to every intake regardless
of referral source. DZ-specific rate structures and routing rules are
layered on top by the `klg-dz-overlay` skill.

---

## 1. Current Rate Sheet (effective June 2026)

| Line | Rate |
|---|---|
| Timothy Kowal — Standard | $750/hour |
| Timothy Kowal — Consulting | $1,050/hour |
| Senior Attorneys | $595–$650/hour |
| Other Attorneys | $400–$575/hour |
| Paralegals | $175/hour |
| Administrative | Not separately billed (firm overhead) |
| Initial Evaluations | $1,750–$5,500 flat |
| Appellate Appendices / Excerpts of Record | $1,300 flat (automated service, no markup) |

The Consulting rate applies when the client is buying Tim alone (no
team leverage, no firm pipeline, responsive to client tempo). The
Standard rate applies when the client is buying the firm (Tim leading
a system of attorneys, paralegals, and AI workflows). The distinction
matters at intake — when a potential client signals they want Tim's
personal attention on a recurring or real-time basis, quote
Consulting, not Standard.

**Flat rates** are available on a case-by-case basis and are quoted
based on the work-breakdown structure for the specific deliverable
(see Cost Anchors below).

---

## 2. Cost Anchors

Use these anchors when sizing a Cost Horizon estimate. The estimate
is a planning figure to help the client decide whether to retain;
it is not a cap unless explicitly converted to one.

| Cost Horizon | Hours Range | Typical Dollar Range (Standard Rates) |
|---|---|---|
| Normal | 80–150 | $30,000–$75,000 |
| Medium | 150–300 | $75,000–$175,000 |
| High | 300+ | $175,000+ |

**Work Breakdown Structure (WBS) format** for preliminary estimates:

1. List each stage of the engagement (e.g., record review, AOB
   drafting, RB review, ARB drafting, oral argument prep).
2. Estimate hours for each stage at the appropriate personnel level.
3. Apply multipliers for known complexity drivers (multi-issue
   appeals, complex record, novel legal questions, expedited
   deadlines).
4. Add a 10–20% buffer for unforeseen issues.
5. Express the total as a range, not a single number.

For DZ matters, the WBS uses DZ tier rates (see `klg-dz-overlay`),
not the standard rate sheet.

---

## 3. Analytical Framework

### Issue Strength Assessment

For each principal issue, classify as:

- **Strong.** Clear legal error or abuse of discretion; favorable
  standard of review; well-preserved; controlling authority supports
  reversal; prejudice is straightforward to establish.
- **Mixed.** Arguable error or mixed authority; some preservation
  concerns or unfavorable standard of review; prejudice debatable.
- **Weak.** No clear error; serious preservation problems;
  deferential standard of review; adverse authority dominates;
  prejudice unlikely to be found.

State the classification with reasoning tied to specific record
citations. Never rate without citing.

### Preservation Analysis

For each appellate issue, answer four questions:

1. Was it raised in the trial court?
2. Was a ruling obtained?
3. Was the objection timely?
4. If not preserved, does an exception apply? (Pure question of
   law, jurisdictional, misinstruction, futility, constitutional
   or structural error.)

Unpreserved issues without applicable exception = Red flag.

### Standard-of-Review Mapping

For each issue, assign and cite the applicable standard:

- **De novo** — questions of law, statutory interpretation, MSJ
  grant, demurrer, constitutional questions
- **Substantial evidence** — factual findings, jury verdicts on
  contested evidence
- **Abuse of discretion** — discretionary trial court rulings,
  evidentiary rulings, fees, sanctions, equitable doctrines
- **Clear error** — federal fact findings (Ninth Circuit)
- **Harmless / prejudicial error** — applies after error is found,
  to determine whether reversal is warranted

Cite a short authority for each assignment.

---

## 4. Traffic Light Definitions

### Merits (Should the PC have won?)

- **Green.** Strong legal error well-preserved; favorable SoR;
  strong supporting authority; prejudice clear.
- **Yellow.** Arguable error; mixed preservation or SoR concerns;
  authority mixed; prejudice debatable.
- **Red.** No clear error; preservation seriously deficient;
  deferential SoR; adverse authority dominates.

### Equities (Is the PC in the right?)

- **Green.** PC is the wronged party; sympathetic facts;
  affirmance would produce harsh or unjust result.
- **Yellow.** Equities are mixed or arguable on both sides.
- **Red.** PC is the wrongdoer or the equities clearly favor
  the opposing party; affirmance produces a fair result.

### Ability to Pay

- **Green.** Hourly engagement or funded flat fee with prepayment;
  client has stable counsel history and demonstrated ability to
  fund litigation through trial.
- **Yellow.** Payment plan; client has resources but cash flow is
  uneven; trial counsel reports payment compliance but not without
  effort.
- **Red.** Contingency request (unless strong public-interest
  case); client is unrepresented or has gone through multiple past
  attorneys; client signals price sensitivity that suggests
  inability to fund through resolution.

### Practice Alignment

- **Green (Core).** Business litigation, anti-SLAPP, civil
  procedure, judgment enforcement, contract disputes, real
  property and trust disputes within KLG's existing practice
  depth.
- **Yellow (Secondary).** Trust and probate, employment, areas
  KLG handles but with less concentration.
- **Red (Lower).** Family law, criminal, immigration, areas
  outside KLG's typical practice mix.
- **Discretionary (Public-interest).** Constitutional, civil
  rights, election law, or similar matters where KLG's
  philosophical alignment justifies taking the case even if
  it falls outside Green or Yellow.

---

## 5. Tentative Classification

Combine the four traffic lights into one of three classifications:

- **Promising.** Merits Green or Yellow; Equities Green or
  Yellow; Ability to Pay Green or Yellow; Practice Alignment
  Green, Yellow, or Discretionary. Recommend take.
- **Borderline.** One Red traffic light that doesn't fall under
  Practice Alignment Red. Recommend take only with explicit
  attorney decision about the risk; document the reason.
- **Decline.** Two or more Red traffic lights, OR Merits Red,
  OR Practice Alignment Red without Discretionary override.

State the one-sentence reason for the classification.

---

## 6. Engagement Structure Principles (Universal)

These principles apply to every engagement letter regardless of
referral source. They surface as "Engagement Structure Flags" in
Section 12 of the case assessment memo.

### 6.1 Caps philosophy

A cap protects the client from cost overruns. It is not a tool
for the referring attorney or client to program a minimum margin
for themselves.

**Rule.** When a cap is proposed, set it at the upper end of
plausible work for the deliverable — not the lower end. Never
accept a cap that falls below KLG's reasonable estimate of the
work required.

**Flag when:**
- A cap is proposed at or below the midpoint of the cost estimate.
- The referring attorney pushes for a cap "to give the client
  certainty" but the proposed number is suspiciously close to
  the floor of the estimate.

### 6.2 Flat fees philosophy

Flat fees only work when paid in advance. Two benefits drive the
structure: KLG bears no collections risk, and KLG keeps the upside
on efficient execution. Both benefits disappear if the flat fee is
paid on completion.

**Rule.** Flat fees only when paid in advance. Payment-on-completion
flat fees should be declined or converted to an hourly engagement
with a cap.

**Flag when:**
- A flat fee is proposed but the client or referring attorney
  resists prepayment.
- A "flat fee" is structured as a series of milestone payments
  tied to deliverables (this is a fixed-payment hourly arrangement,
  not a flat fee).

### 6.3 Rate-and-cap interaction

This is the rule that prevents "getting hurt twice." If KLG accepts
a relationship rate below the rate sheet AND a cap below the
reasonable estimate, the firm absorbs both the rate discount and
the cap shortfall. That is the wrong structure.

**Rule.** If KLG accepts a low rate, the cap must be set high or
omitted entirely. If KLG accepts a low cap, the rate must be
standard. Never both.

**Flag when:** A discounted rate is proposed AND a cap is proposed.
This combination requires explicit attorney decision before
proceeding.

### 6.4 Scope-and-revisions discipline

Capped and flat-fee engagements need explicit scope-and-revisions
terms or KLG bears unlimited revision risk after delivery. The
Petersen and Hoopes matters surfaced this — client rounds of
edits continued past the cap with no contractual stopping point.

**Rule.** Every capped or flat-fee engagement letter includes:

> "The capped fee covers initial drafting of the [deliverable]
> plus one substantive revision round following delivery.
> Additional client-driven revisions are billed hourly at the
> applicable rate without cap."

**Flag when:** A capped or flat-fee engagement is proposed without
explicit scope-and-revisions terms.

### 6.5 Out-of-hours communications

KLG operates during business hours. Genuine emergencies — filings
due that day, court-ordered actions, opposing-counsel deadlines —
receive same-day response regardless of timing. Routine
after-hours communications are addressed the next business day.

**Rule.** Every engagement letter includes:

> "KLG responds to email and routine communications during
> business hours, Monday through Friday. Genuine emergencies —
> filings due that day, court-ordered actions, opposing-counsel
> deadlines — receive same-day response regardless of timing.
> Routine communications outside business hours are addressed
> the next business day."

**Flag when:** Always. This is standard engagement letter language
and should appear in every new engagement going forward.

### 6.6 Communication routing

For matters with referring attorneys or co-counsel, identify the
single point of contact for document delivery, case-file management,
and routine matter communications. Default is the paralegal handling
the matter, not Tim personally.

**Rule.** The engagement letter should designate a single KLG team
member as the primary contact for routine matter communications,
with Tim available for substantive legal questions. This applies
especially to matters where prior practice has routed everything
through Tim.

**Flag when:** A referring attorney has a history of routing
matter communications exclusively through Tim. The engagement
letter should explicitly redirect routine traffic to the
designated paralegal.

---

## 7. DZ Matters

For matters referred by David Zarmi, this skill identifies the DZ
referral source but does NOT apply DZ-specific rate tiers, attribution
terms, or routing rules. Those are handled by `klg-dz-overlay`, which
runs after this assessment completes.

Section 12 (Engagement Structure Flags) of the case assessment memo
produces a one-line note for DZ matters: "DZ matter — Engagement
Structure Flags handled by DZ overlay skill in a separate pass."

Section 13 (Open Items & Next Steps) flags that `klg-dz-overlay`
should run next.

The case-assessment skill does not embed DZ-specific pricing because
the DZ structure is evolving and isolating it in the overlay skill
lets it iterate without touching the universal intake rubric.
