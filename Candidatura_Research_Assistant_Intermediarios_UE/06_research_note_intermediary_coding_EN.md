---
title: "Coding Regulatory Intermediaries in EU Green-Transition Legislation"
author: "Igor Caires Machado — Postdoctoral Researcher, ENAP · ORCID 0009-0008-9547-5223"
date: "5 September 2026"
lang: en
---

## Purpose

This note reports on work done in response to the call for a research
assistant/partner to help code intermediaries in EU legislation on the green
transition ("Governance by and of Intermediaries"). It presents a two-stage
pipeline — a reproducible screening layer that locates candidate
intermediation provisions, and a substantive coding layer that converts
those provisions into theoretically grounded observations of who the
intermediary is, between which regulator and target it operates, and under
what institutional design. The screening layer accelerates corpus analysis;
it does not replace substantive coding. Full technical detail (patterns,
counts, validation, code) is kept in four short annexes rather than in this
note, so this stays a working document, not a technical report.

## The theoretical problem

The proposal ("Can Intermediaries Save Liberal Governance?") argues that the
democratic-reform agenda should turn to **regulatory intermediaries** — the
rule-brokers between rule-makers and rule-takers. Regulation scholarship
still treats this relation as bipartite, leaving who certifies, audits,
ranks and reports under-theorised. The proposal identifies four gaps
(attention, conceptualisation, proliferation, subtheorisation) and three
aims: mapping and measuring intermediaries and mechanisms; explaining their
diffusion; and connecting intermediation design to democratic theory
(mono/polycentric governance). Four primary mechanisms structure the
empirical work packages (WP2–WP5): **reporting** (state-led), **certification**
(NGO-led), **ranking/rating** (business-led), and **audit** (profession-led).

## Stage A — screening layer

Four EU acts were collected in full text from EUR-Lex by CELEX number, one
per mechanism, chosen because each is a known anchor case:

| Act | CELEX | Target mechanism |
|---|---|---|
| Corporate Sustainability Reporting Directive | `32022L2464` | reporting + audit |
| EU Ecolabel Regulation | `32010R0066` | certification |
| Climate Benchmarks Regulation | `32019R2089` | ranking/rating (conditional — §4) |
| EU ETS Verification & Accreditation Regulation | `32018R2067` | audit (+ certification) |

Each paragraph was screened with a two-tier lexical rule set per mechanism
(anchor patterns confirm the mechanism on their own; weak patterns are
generic and need review; exclusion patterns discard known false-positive
contexts). The output records `screening_confidence` (`high`/`low`) rather
than "confirmed" — a lexical match is a strong textual signal, not
confirmation that an R-I-T (Regulator–Intermediary–Target) structure is
present. It also records `provision_type` (`recital`/`article`) and
`amended_act` (the directive actually being amended, for amending acts like
the CSRD, distinct from the source CELEX processed).

Result: 1,079 paragraph-level hits, 71% `high` confidence, 29% `low`. Each
act shows a clearly dominant, coherent mechanism. One unplanned finding: in
the ETS act, the dominant hits are not "audit" (87) but "certification"
(149, mostly "accreditation") — the regime creates an auditor who is itself
accredited by another intermediary, two mechanisms stacked in one act (see
Stage B, §4). Full pattern list, per-pattern counts and an actor/mechanism/
instrument tag for every pattern are in **Annex A — Codebook**.

## Stage B — R-I-T coding

For one key provision per act, I read the full text and coded the
Regulator–Intermediary–Target structure explicitly, together with legal
nature, sector, independence and accreditation requirements — the
attributes the proposal itself asks about.

- **CSRD, Art. 27a (assurance of consolidated sustainability reporting):**
  R = Member State competent authority; I = group auditor, itself
  supervising a chain of independent assurance services providers,
  statutory auditors and audit firms; T = undertaking/group. Mandatory,
  independence required, approval required. The article shows one
  intermediary supervising others — a layered chain, not a flat triad.
- **Ecolabel, Art. 9 (award of the EU Ecolabel):** R = European Commission
  (sets criteria, maintains the public register); I = competent body
  (designated per Member State); T = operator/applicant. Voluntary, hybrid
  sector, partial reliance on accredited testing bodies.
- **Climate Benchmarks, Art. 19b — conditional case:** I = benchmark
  administrator; T is dual and indirect (constituent companies scored for
  inclusion/weighting; asset managers who use the label). R is not named in
  this article — it sits elsewhere in Regulation (EU) 2016/1011. A climate
  benchmark is not automatically a "rating" in the proposal's regulatory
  sense; it may just be a reference index for financial comparison. I keep
  the case but mark construct validity as **conditional**, not confirmed —
  worth asking David directly whether this counts, or whether a more direct
  case (e.g. credit rating agencies) should anchor this mechanism instead.
- **ETS Verification, Art. 27 (verification report):** R = competent
  authority; I = verifier (with internal role differentiation: lead auditor,
  auditor, independent reviewer, technical expert); T = operator/aircraft
  operator. This article names all three positions explicitly in the same
  sentence — "the responsibilities of the operator or aircraft operator, the
  competent authority and the verifier" — the clearest R-I-T statement found
  in the sample.

Full coding table: **Annex B — R-I-T coding**.

## Validation

Screening hits alone only test false positives. For the same four
provisions, I read every paragraph manually, without regex, marking whether
it substantively concerns an intermediation relationship — the gold
standard — then compared it against what the screening layer actually
caught in those paragraphs.

**Result (35 judged units): precision 100% (33/33), recall 94.3% (33/35),
F1 97.1%.** No false positives in the sample. The two misses share one
cause: the paragraph describes the same relationship from the regulator's or
the target's side, without repeating the intermediary's own name (e.g. "the
operator may place the EU Ecolabel on the product only after conclusion of
the contract" — describes the target's resulting right, never says
"competent body"). This is not fixed by adding synonyms; it needs a
paragraph-adjacency rule (flag paragraphs next to a high-confidence hit for
review, even without their own lexical match) — not yet implemented, logged
as the best-supported next design change. This is a small, non-random
sample (the richest article per act) — an optimistic ceiling, not a
corpus-wide estimate. Full method and both misses: **Annex C — Gold-standard
validation**.

## Methodological grounding

The design choices above — confidence tiering, evidence-anchored coding,
and calibrating rules against a read sample rather than a priori — draw on
my prior experience building evidence-anchored, iteratively validated
codebooks in the ARENAS research programme, where I code spatial elements
and sociomaterial mechanisms of policy implementation.

## Limitations

- Screening's 29% `low`-confidence hits outside the four coded provisions
  remain an unreviewed queue, not a final result.
- The validation sample is small and non-random (§5).
- Collection uses EUR-Lex's per-CELEX HTML page, workable for four
  hand-picked acts, not for identifying the relevant population at scale.
- Stage B covers four provisions, proving the step is executable from Stage
  A's output — not a corpus-scale coding exercise.

## Next steps

1. **Define the population before querying Cellar/SPARQL.** SPARQL solves
   retrieval, not population definition — the order should be: population
   definition → inclusion/exclusion criteria → sampling frame → SPARQL query
   → screening → coding.
2. Implement the paragraph-adjacency review rule identified in §5.
3. Use the validated sample as a reference to calibrate a second coder
   (human or NLP-assisted) and measure agreement.
4. Expand Stage B's attributes (formality, voluntariness, level, sphere,
   motivation, mode of operation, centrality, degree of separation) as
   coding columns, not as new screening patterns.
5. Resolve the Climate Benchmarks construct-validity question directly with
   David before treating it as the canonical ranking/rating case.

## Conclusion

I first built a reproducible screening layer to locate candidate
intermediation provisions. I then convert those provisions into
theoretically grounded R-I-T observations, identifying the intermediary,
mechanism, legal basis, institutional attributes and verbatim evidence. The
screening layer accelerates corpus analysis; it does not replace substantive
coding. The architecture, documentation, traceability and codebook
demonstrate the research-organisation capacity the call asks for; the R-I-T
layer is what makes the output speak directly to the theory being tested.

---

**Annexes** (separate files): A — Codebook (`CODEBOOK.md`); B — R-I-T coding
(`RIT_CODING.md`, `data/rit_coded_sample.csv`); C — Gold-standard validation
(`GOLD_STANDARD_VALIDATION.md`); D — Methodology and design rationale
(`METODOLOGIA.md`).
