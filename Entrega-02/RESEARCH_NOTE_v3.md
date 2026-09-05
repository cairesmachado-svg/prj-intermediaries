---
title: "Coding Regulatory Intermediaries in EU Green-Transition Legislation (v3)"
author: "Igor Caires Machado — Postdoctoral Researcher, ENAP · ORCID 0009-0008-9547-5223"
date: "5 September 2026"
lang: en
---

## Purpose

This is the third iteration of a response to the call for a research
assistant/partner to help code intermediaries in EU legislation on the
green transition. Each iteration corrected a specific limitation: v1 built
a lexical mechanism-screening pipeline and mistook it for intermediary
coding; v2 introduced the R-I-T relational unit but mixed units of analysis
in one dataset and left at least one relationship insufficiently
normalized. This version separates the pipeline into three stages, each
with its own dataset, and enforces one rule throughout: **a dataset row must
correspond to exactly one analytical unit** — one screening signal, one
adjudicated candidate, or one fully individuated regulatory relationship,
never a blend.

## Conceptual framework

```
Regulatory context
       |
Regulatory architecture
       |
R - I - T relationship  <-- coded now (Stage C)
       |
Regulatory intermediation: actors + mechanisms + strategies
       |
Intermediary institutional design  <-- partially coded now
       |
Autonomy / accountability indicators  <-- defined, mostly deferred
       |
Failure risks / safeguards  <-- defined, deferred
       | - - - - - - - - - - - - - - - - - - - - - -  (boundary of this coding layer)
[future] Effectiveness / legitimacy / trust
       |
[future] Monocentric <-> polycentric governance (regime-level)
```
Only theoretical constructs Levi-Faur's proposal actually sustains are
attributed to it; operationalisations proposed here for this dataset, and
possibilities reserved for future analysis, are labelled as such throughout
the annexes (`DATA_DICTIONARY_v3.md`, `VARIABLE_MAP_v3.md`).

## Operational model — three stages, three datasets

| Stage | Question | Unit | Dataset |
|---|---|---|---|
| A — Candidate detection | Does this provision contain textual evidence potentially associated with intermediation? | provision × lexical signal | `screening_hits_v3.csv` |
| B — Relational adjudication | Does the evidence support an analytically distinct R-I-T relationship? | candidate | `candidate_adjudications_v3.csv` |
| C — Institutional coding | What kind of intermediation is this, and how is it designed? | relationship | `rit_relationships_v3.csv` (+ `actors_v3.csv`) |

Full coding manual: `RIT_CODEBOOK_v3.md`. Full pattern reference:
`SCREENING_CODEBOOK_v3.md`.

## Pilot evidence

Same four acts as before (CSRD, Ecolabel, Climate Benchmarks, ETS
Verification) — no new corpus collection this round. Stage A: 1,079
screening hits (unchanged in total from the previous round; the underlying
lexical patterns were corrected for ontology-mixing, with identical
matching results). Stage B: **ten adjudicated candidates — seven positive,
two negative, one conditional.** Stage C: **seven fully individuated
regulatory intermediation relationships**, including:

- Two chains demonstrating meta-regulation (CSRD: a group auditor
  supervising a subsidiary-level assurance provider; ETS: a national
  accreditation body itself overseen by an EU-level peer-evaluation body
  before it accredits a verifier).
- One case of role multiplicity: the ETS verifier is the intermediary in
  one relationship (between the competent authority and the operator) and
  the target in the linked accreditation relationship.
- Two deliberate negative controls: a direct CSRD reporting duty with no
  mediating actor, and an EU Ecolabel advisory board that fails the
  relational test (it advises the regulator; it does not mediate an
  existing regulator-target relationship).

Ten adjudicated cases, not thousands of hits, is deliberate: the priority is
demonstrating that every rule in the codebook has been exercised at least
once, not corpus coverage.

## Construct-validity tests

Two cases required explicit scrutiny rather than default acceptance:

- **Climate Benchmarks** (quarantined as `conditional`, not promoted to
  Stage C): the administrator selects, weights and excludes assets against
  a predefined decarbonisation standard — rating-like — but the regulator
  is not named in the specific provision read, and the target is dual and
  indirect (scored companies; separately, asset managers who use the
  label). Held for direct discussion with David rather than force-included.
- **ETS accreditation relationship**: an initial reading treated the
  national accreditation body as the regulator with no distinct
  intermediary — a dyadic misread that would have undermined the
  role-multiplicity claim built on it. Re-reading the Article-14
  peer-evaluation evidence already on file corrected this. Documented, not
  silently fixed (`METHODOLOGY_v3.md`).

## Validation

Stage A: precision 100%, recall 94.3%, F1 97.1% over a 35-paragraph
**manually adjudicated pilot reference sample** (not a "gold standard" —
retired for good). Stage B/C: **not yet validated by a second coder** — a
full protocol is written (`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`) and is
the next concrete task, not a formality to skip.

## What legal-text coding can and cannot measure

Directly codeable from the provisions read: actor identity, R-I-T role
assignment, mechanism, a partial set of institutional-design attributes
(formal role, voluntarism, level, sphere, mode of operation,
organisational separation), and two governance indicators (independence
requirement, supervision). **Not** measured by this layer, and not claimed
to be: motivation, institutional centrality, the full autonomy and
accountability indicator batteries, intermediation strategy, and any
regime-level polycentricity classification — all defined operationally in
`DATA_DICTIONARY_v3.md` for a future round with a second coder, none
fabricated here. Effectiveness, legitimacy and trust are treated as
downstream theoretical outcomes outside this layer's evidentiary reach; text
invoking them is coded as a stated regulatory objective, never as evidence
of an achieved result.

## Next steps

1. Define the population and sampling frame in writing before any
   SPARQL/Cellar query at scale.
2. Run the Stage B/C inter-coder validation protocol with a second coder.
3. Resolve the Climate Benchmarks construct-validity question with David.
4. Populate the deferred autonomy, accountability and strategy batteries
   once a second coder is in place.

## Conclusion

Regulatory intermediation is operationalised here as a relational
construct, not a lexical category. Screening identifies candidates;
relational adjudication determines whether a genuine R-I-T structure
exists, with negative and conditional outcomes preserved as evidence of
discriminant validity, not discarded; institutional coding then records
mechanisms and the attributes the text can actually support, while autonomy,
accountability and strategy remain decomposed into explicitly deferred
indicators rather than premature indices. Effectiveness, legitimacy, trust
and polycentric governance are reserved for later empirical and aggregate
analysis that this layer is not designed to perform.

---

**Annexes** (separate files): `RIT_CODEBOOK_v3.md`,
`SCREENING_CODEBOOK_v3.md`, `DATA_DICTIONARY_v3.md`, `VARIABLE_MAP_v3.md`,
`METHODOLOGY_v3.md`, `SCREENING_VALIDATION_v3.md`,
`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`, `CHANGELOG_v3.md`,
`data/screening_hits_v3.csv`, `data/candidate_adjudications_v3.csv`,
`data/rit_relationships_v3.csv`, `data/actors_v3.csv`.
