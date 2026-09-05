# R-I-T Codebook v3 — three-stage coding manual

Supersedes `RIT_CODEBOOK.md` (v2, kept in `v1/PoC/` for the record). Adds a
third stage, formalises the relational test into five explicit conditions,
and fixes the normalization rule that v2 violated in places (see
CHANGELOG_v3.md).

## Core principle
**Do not code labels; code relationships.** Sequence: legal provision →
regulatory architecture → candidate relationship → R-I-T adjudication →
mechanism → strategy → intermediary institutional design → observable
governance indicators → structured data. Never invert this to fit text into
a pre-decided category.

## Three stages

### Stage A — Candidate detection
*Does this provision contain textual evidence potentially associated with
regulatory intermediation?* Screening only. Unit: `provision × lexical
signal`. Output: `data/screening_hits_v3.csv`. Does not determine whether an
intermediary exists.

### Stage B — Relational adjudication
*Does the candidate evidence support an analytically distinct regulatory
relationship involving a regulator, an intermediary and a target?* Unit:
`candidate regulatory relationship`. Output: `data/candidate_adjudications_v3.csv`.
Result is one of `positive` / `negative` / `conditional` / `insufficient_evidence`.
Negative and conditional cases stay in this dataset — they do not disappear,
and they are not promoted to Stage C.

### Stage C — Institutional coding
Only `positive` (and, once resolved, formerly-`conditional`) cases proceed
here. *What kind of regulatory intermediation is this, and how is it
institutionally designed?* Unit: `regulatory intermediation relationship`.
Output: `data/rit_relationships_v3.csv`. Codes actors (via `actors_v3.csv`),
mechanisms, and the institutional attributes the provision can actually
support (see `DATA_DICTIONARY_v3.md` for what is populated vs. deferred).

## The relational test (five conditions, Stage B)
A candidate receives `relational_test_result = positive` only when **all
five** hold, each with a written note in `adjudication_note`:

a) An identifiable rule-maker/regulator (R) exists.
b) An identifiable rule-taker/target (T) exists.
c) A third actor or institutional role, analytically distinct from R and T,
   is present.
d) That third actor performs a regulatory function that *mediates* the
   R–T relationship (not merely advises the regulator, and not merely
   receives the same obligation as T).
e) The relationship can be supported by explicit legal text or a clearly
   documented institutional reconstruction (never invented).

If only R→T is present — even with `reporting_mechanism_present = 1` — there
is no intermediary. See CAND-03 (`candidate_adjudications_v3.csv`): a direct
reporting duty, correctly adjudicated `negative`.

## Actor roles are relational, not intrinsic
The same actor identity (one row in `actors_v3.csv`) can occupy different
positions across different relationships. Demonstrated in this pilot:
`ACT-16` (verifier) is `I_actor_id` in RIT-006 and `T_actor_id` in RIT-007.
The **actor table never stores a role** — role is a property of the
relationship row, never of the actor identity. An earlier draft of this
relationship incorrectly coded the national accreditation body as `R` with
no distinct `I` (see CAND-09's adjudication note for the correction): once
the Article-14 peer-evaluation body was identified as the actual regulator
of the accreditation infrastructure, the national accreditation body
resolved to `I`, not `R` — a concrete example of why the relational test
must be re-applied rather than assumed from an initial reading.

## One row = one relationship (normalization rule)
A cell must never contain more than one actor identity joined by "/" or ";"
representing *simultaneous, distinct* actors in the *same* relationship.
Two situations look similar but are coded differently:

- **Disjunctive legal alternatives for the same function** (the law names
  several entity types, any one of which can fill the same role in a given
  case) → **one relationship**, with the alternatives documented in the
  actor label and the adjudication note. Example: RIT-002's `I_actor_id`
  (`ACT-04`) names five eligible entity types from Art. 27a(1)(b) as
  alternatives for one function, not five actors.
- **Two distinct functions named in the same sentence** → **separate
  relationships**. Example: Ecolabel Art. 9(7) names testing (ISO 17025) and
  verification (EN 45011) as two distinct accredited-body functions — coded
  as RIT-004 and RIT-005, not folded into one row.

When in doubt, split. A row that cannot be read aloud as "R regulates I,
which mediates for T" without an "and" or a list is not yet atomic.

## Chains and meta-regulation
`chain_id` groups relationships that are part of the same multi-level
structure; `intermediation_level` (`L1`/`L2`) and `parent_relationship_id`
record the position within it. `L2` marks a relationship in which the
regulator of that specific link is itself an intermediary in a `L1`
relationship, or in which the intermediary is itself governed by another
intermediary/regulator. This is an **operational proposal for this
dataset**, not a classification already fixed in Levi-Faur's proposal.

## Mechanisms
Four primary types (per the proposal's empirical design, not claimed as an
exhaustive ontology): `reporting`, `certification`, `ranking_rating`,
`auditing`. `secondary_mechanism` records a second mechanism present in the
same relationship (e.g. RIT-004/RIT-005 combine `auditing` and
`certification`).

**Reporting is not automatically intermediation.** Code
`reporting_mechanism_present` and `intermediary_present` as independent
0/1 fields on every relationship/candidate — CAND-03 has
`reporting_mechanism_present = 1`, `intermediary_present = 0`.

## Strategies of intermediation (not yet populated — see DATA_DICTIONARY_v3.md)
Per the proposal, responsibilization and empowerment are **not necessarily
dichotomous** — a relationship can show evidence of both, one, or neither.
The correct design is therefore **two independent 0/1/`unclear`/`NOE`
indicator batteries** (`responsibilization_present`,
`empowerment_present`), never a single categorical `strategy` column forcing
a choice between them. Preliminary, exploratory indicator lists for each are
defined in `DATA_DICTIONARY_v3.md`; none are populated in this pilot round —
scoring them for seven relationships without a second coder to check the
judgment calls would manufacture precision this pilot cannot support.

## Uncertainty and missingness codes
`1`=explicitly present, `0`=explicitly absent, `NA`=not applicable,
`UNK`=unknown/insufficient information, `NOE`=not observable from the legal
text alone, `EXT`=requires external evidence. Never blank as a substantive
value.

## Observability classes
`DIRECT` (observable in the text), `INFERRED` (institutional reconstruction
with documented reasoning — e.g. RIT-007's R actor), `EXTERNAL` (requires a
source beyond the legal text), `NOT_OBSERVABLE`. Tag every Stage C variable
in `DATA_DICTIONARY_v3.md` with its class; never convert `NOT_OBSERVABLE`
into `0`.

## Failures are risks addressed by design, not observed events
A conflict-of-interest rule means `design_addresses_capture = 1`, never
`capture_present = 1`. Not populated for any of the 7 relationships in this
round (would require checking each provision specifically for a preventive
clause, not done yet) — defined in `DATA_DICTIONARY_v3.md` for the next
round.

## What legal-text coding cannot measure
Effectiveness, legitimacy and trust are downstream theoretical outcomes.
Legislative language invoking them (e.g. a recital citing "reliability") is
coded as `stated_regulatory_objective`, never as evidence of an achieved
outcome. Likewise, no single relationship is coded `polycentric`/
`monocentric` — only structural indicators (`number_of_authority_centres`,
`public_private_mix`, etc., defined but not populated) that could support
future regime-level analysis.
