# DZ Engagement Letter Provisions

This file contains the standard verbatim language for the four
DZ-specific engagement letter provisions: out-of-hours
communications, scope and revisions, attribution, and
communication routing.

These provisions appear in every DZ engagement letter regardless
of tier. They do not vary by tier and they do not get waived.

---

## 1. Out-of-Hours Communications

**Use:** All DZ matters, all tiers, every engagement letter.

**Verbatim language:**

> "KLG responds to email and routine communications during
> business hours, Monday through Friday, 9:00 AM to 6:00 PM
> Pacific Time. Genuine emergencies — filings due that day,
> court-ordered actions, opposing-counsel deadlines that bear
> on the matter within the same business day — receive same-day
> response regardless of timing. Routine communications outside
> business hours are addressed the next business day."

**Variation if requested:** The hours window can be adjusted by
mutual agreement at engagement (e.g., 8:00 AM to 5:00 PM, or
extended hours during specific filing periods). The principle —
business hours as the default, emergencies as the exception —
does not change.

**Rationale to share if asked:** This provision reflects KLG's
firm-wide operating model. It is not specific to DZ matters.
The provision protects both sides: David and his clients know
when to expect response, and KLG's attorneys are not on call
24/7 in a way that erodes work-product quality on every matter.

---

## 2. Scope and Revisions

**Use:** All DZ matters with capped or flat-fee engagements.
For uncapped hourly engagements, the provision is unnecessary
(all rounds bill hourly).

**Verbatim language:**

> "The capped [or flat] fee covers initial drafting of the
> [deliverable — e.g., 'opening brief,' 'petition for review,'
> 'writ petition'] plus one substantive revision round following
> delivery of the draft. Additional client-driven revisions are
> billed hourly at the applicable rate without cap. KLG relies
> on the referring attorney to manage client revision
> expectations."

**Variation if requested:** The included revision count can be
increased by mutual agreement at engagement (e.g., "plus two
substantive revision rounds"). The cap-on-additional-rounds
principle does not change. KLG never agrees to unlimited
revisions within a capped fee.

**Rationale to share if asked:** Past DZ matters (specifically
Petersen and Hoopes) involved multiple rounds of client edits
after delivery that exceeded the cap. KLG absorbed the cost.
The provision sets a clear contractual stopping point. The
referring attorney's role in managing client revision
expectations is explicit — KLG cannot manage the client
directly when invisibility is in place, so the duty falls on
the referring attorney.

---

## 3. Attribution

**Use:** All DZ matters. The clause varies based on whether
default (visible attribution) or invisibility is chosen at
engagement.

### 3.A. Default — Attribution Visible

**Verbatim language:**

> "KLG will appear as counsel of record on all filings and
> communications related to this matter. The referring attorney
> [name] appears [as co-counsel / as lead counsel with KLG as
> appellate counsel / on the cover with KLG's name listed
> separately — adapt to the appearance practice for the matter]."

### 3.B. Invisibility (Surcharged)

**Verbatim language:**

> "KLG's work on this matter is ghostwritten for the referring
> attorney [name], who appears alone as counsel of record on
> filings and communications. KLG does not appear on any
> external document related to this matter. The invisibility
> surcharge of [amount or percentage — pending Tim's
> finalization] applies in addition to the rate structure
> stated above, reflecting the reputational opportunity cost,
> marketing-content cost, and administrative cost of suppressed
> attribution."

**Variation if requested:** Hybrid arrangements (KLG attribution
on internal communications but not on filings; KLG attribution
on petitions but not on briefs) are possible by mutual agreement
at engagement. The surcharge scales with the scope of
invisibility — full invisibility carries the full surcharge;
hybrid invisibility carries a reduced surcharge negotiated at
engagement.

**Rationale to share if asked:** The invisibility surcharge
prices three real costs that the legacy structure absorbed as
relationship overhead — reputational opportunity cost (KLG
loses public credit for high-quality work product),
marketing-content cost (invisible matters cannot be cited on
the firm website or in BD content), and compliance cost
(maintaining proper attribution on internal records while
suppressing it on external filings requires extra discipline).
The new structure makes the cost explicit rather than implicit.

---

## 4. Communication Routing

**Use:** All DZ matters. The clause states the operational
ground rule for matter communications.

**Verbatim language:**

> "Routine matter communications, document delivery, and case-file
> management on this matter route through [designated paralegal —
> default: Brittney Bishop], who serves as the primary contact
> for the referring attorney. Tim Kowal is available for
> substantive legal questions, strategic decisions, and matters
> requiring partner-level attention. To preserve the efficiency
> of this arrangement, documents and routine inquiries should
> reach KLG through the designated paralegal contact in the first
> instance."

**Variation if requested:** The designated paralegal can be
named differently for different matters (e.g., if Brittney is
on leave or if a different paralegal owns a particular file).
The principle — routing through a paralegal rather than through
Tim directly — does not change.

**Rationale to share if asked:** This provision reflects KLG's
firm-wide operating model. It is not specific to DZ matters,
but it has extra force for DZ engagements because past practice
has routed everything through Tim directly. The provision
redirects routine traffic to where it belongs and preserves
Tim's time for substantive legal work. It also gives the
designated paralegal direct ownership of the matter file, which
is operationally cleaner.

---

## 5. How These Provisions Appear in the Engagement Summary

The DZ Engagement Summary produced by `klg-dz-overlay` includes
the verbatim language for each applicable provision in Section
6 (Engagement Letter Provisions). For default attribution, only
clause 3.A appears; for invisibility, only clause 3.B appears.

The Engagement Summary then feeds into the actual engagement
letter draft, where the provisions are integrated with the
boilerplate engagement-letter terms (scope of representation,
limits on liability, governing law, etc.).

---

## 6. When These Provisions Do Not Apply

These four provisions are universal to DZ matters. They do not
apply to:

- **Non-DZ matters.** The universal versions of out-of-hours
  communications and scope-and-revisions (from
  `klg-case-assessment-standards.md` Sections 6.4 and 6.5) apply
  instead. Non-DZ matters do not have attribution or routing
  provisions — those are DZ-specific because of the historical
  invisibility expectation and the historical Tim-routing
  pattern.
- **Existing DZ engagements under legacy terms.** Matters
  engaged before the new structure takes effect continue under
  their existing engagement letters. The provisions apply to
  new engagements only.

---

## 7. When to Update This File

If a future engagement letter introduces a new standard
provision (e.g., a privilege-and-confidentiality clause specific
to DZ matters, or a co-counsel relationship structure), log the
update to the AI OS Improvement Backlog with `klg-dz-overlay`
as the target skill. This file should remain the canonical
source of verbatim language; it should not drift into
out-of-date copy.
