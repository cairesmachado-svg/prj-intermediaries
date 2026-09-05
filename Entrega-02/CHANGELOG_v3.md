# Changelog v3

## v3 — 05/09/2026 — three-stage architecture, dataset separation, normalization
Triggered by a review arguing the v2 count ("nine R-I-T relationships")
mislabeled adjudicated candidates (including negatives and a conditional
case) as relationships, that `intermediary_validated` mixed two units of
analysis in one dataset, and that at least one relationship cell violated
one-row-one-relationship.

**Changed:**
- **Three-stage pipeline** replaces two: Stage A (candidate detection) →
  Stage B (relational adjudication, new) → Stage C (institutional coding).
  See `RIT_CODEBOOK_v3.md`.
- **Three separate datasets** replace one mixed file:
  `screening_hits_v3.csv` (1,079 rows, provision×signal, no
  `intermediary_validated` column), `candidate_adjudications_v3.csv` (10
  rows, one per candidate, with `relational_test_result`), and
  `rit_relationships_v3.csv` (7 rows, positive-only, one row = one
  relationship). Plus a new lookup table, `actors_v3.csv` (19 actor
  identities), so relationship rows reference actor ids rather than
  repeating free-text descriptions.
- **Corrected count and language:** "nine R-I-T relationships" (v2) →
  **"ten adjudicated candidate cases: 7 positive, 2 negative, 1
  conditional"** — only the 7 positive cases appear in
  `rit_relationships_v3.csv`.
- **One-row-one-relationship enforced.** Ecolabel Art. 9(7) (testing body
  vs. verification body — two distinct accredited-body functions) was
  split into two relationships (RIT-004, RIT-005) instead of one compound
  cell. A disjunctive legal list naming alternative eligible entities for
  the *same* function (CSRD Art. 27a(1)(b)) is still coded as one
  relationship (RIT-002) — the normalization rule distinguishes these two
  cases explicitly (`RIT_CODEBOOK_v3.md`).
- **Fixed a genuine coding error, not just a presentation issue:** the ETS
  accreditation relationship (RIT-007) initially had the national
  accreditation body as `R` with the verifier as the only other party
  (dyadic, undermining the role-multiplicity claim). Re-reading the
  Article-14 peer-evaluation evidence already on file resolved the national
  accreditation body to `I`, with a new actor (the Article-14 body) as `R`
  — see `METHODOLOGY_v3.md` and CAND-09's adjudication note.
- **Screening pattern ontology bug fixed and re-run:** `verification
  (team|report|body)` and `assurance (engagement|opinion|provider|services)`
  each bundled more than one `semantic_role` under one pattern; split into
  separate patterns in `scripts/screening_v3.py`. Re-running screening on
  the same four acts produced identical totals (1,079 hits) — confirms this
  was a metadata fix, not a matching-behaviour change.
- **Strategies of intermediation reframed** as two independent,
  non-dichotomous indicator batteries (`responsibilization_present`,
  `empowerment_present`) instead of one categorical column — defined in
  `DATA_DICTIONARY_v3.md`, not yet populated.
- **`observability_class` and per-field `evidence_required`/`coding_rule`**
  added systematically in `DATA_DICTIONARY_v3.md`, following the
  construct → dimension → indicator → variable → evidence chain uniformly
  for every populated variable.
- **"dominant mechanism" language checked**: retained only where it means
  "generated the most screening hits" (Stage A), never implying
  institutional centrality — unchanged finding from v1/v2 that hit-count
  is not a centrality measure.
- File renames finalized with `_v3` suffixes per the review's requested
  structure; all v1/v2 files kept in `v1/` for the record, none deleted.

**Not changed / deliberately not expanded:**
- Same four acts, same raw HTML (no new network collection this round).
- Autonomy and accountability indicator batteries remain mostly deferred
  (only `legal_independence_required` and `supervision_present` populated) —
  same reasoning as v2: populating them for 7 relationships without a
  second coder would manufacture false precision.
- Stage B/C validation (inter-coder reliability) is written as a protocol
  (`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`) but not run — no second coder
  engaged yet.
- Population definition for corpus-scale expansion remains open
  (`METHODOLOGY_v3.md`).

## v2 — 05/09/2026 — relational restructuring (superseded, kept in `v1/PoC/`)
Introduced the R-I-T unit of analysis, chains, role multiplicity, negative
cases, and the `screening_confidence`/"pilot reference sample" terminology
fixes. Superseded by v3's dataset separation and one-row-one-relationship
normalization — the concepts introduced in v2 were correct; the
implementation had inconsistencies (mixed-unit dataset, one compound actor
cell, one dyadic-vs-triadic misread) that v3 corrects.

## v1 — 05/09/2026 — initial PoC (superseded, kept in `v1/PoC/`)
Lexical screening (Stage A only) of four EU acts, one per mechanism, with
anchor/weak/exclusion rules and a paragraph-level pilot precision/recall
check.
