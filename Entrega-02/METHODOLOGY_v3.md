# Methodology v3

Supersedes `METHODOLOGY_v2.md` and `METODOLOGIA.md` (both kept in `v1/PoC/`
for the record — most of their content still holds and is not repeated
here; this file covers what changed).

## Conceptual architecture
```
REGULATORY CONTEXT
        v
REGULATORY ARCHITECTURE
        v
R - I - T RELATIONSHIP
        v
REGULATORY INTERMEDIATION
Actors + Mechanisms + Strategies
        v
INTERMEDIARY INSTITUTIONAL DESIGN
        v
AUTONOMY / ACCOUNTABILITY INDICATORS
        v
FAILURE RISKS / SAFEGUARDS
        v
[future empirical analysis] Effectiveness / Legitimacy / Trust
        v
[future aggregate analysis] Monocentric <-> Polycentric Governance
```
This pilot's coding stops at the "institutional design" and "autonomy/
accountability indicators" layers (partially, per `DATA_DICTIONARY_v3.md`).
Everything below the second dashed line is explicitly out of scope for
legal-text coding, not silently assumed.

## Mandatory methodological chain
Every observation must be reconstructable along:
**Legal provision → regulatory architecture → candidate relationship →
R-I-T adjudication → mechanism → strategy → intermediary institutional
design → observable governance indicators → structured data.**
Never work backwards from a desired category to text that seems to confirm
it.

## Why three stages, not two
v2 conflated "screening confidence" with "intermediary validated" in
practice: a paragraph-level `intermediary_validated` column sat inside the
same dataset as lexical hits, even though a paragraph can support several
relationships and a relationship can depend on several provisions. Stage B
(relational adjudication) is now a **separate dataset** at a **separate
unit of analysis** (`candidate`, not `provision`) from both Stage A
(`provision × signal`) and Stage C (`relationship`). See
`RIT_CODEBOOK_v3.md` for the full three-stage definition.

## Why the population question is still open
Unchanged from `METHODOLOGY_v2.md`: SPARQL/Cellar solves retrieval, not
population definition. The order remains population definition → inclusion/
exclusion criteria → sampling frame → SPARQL query → Stage A → Stage B →
Stage C. Not resolved in this round — still the first item for the next one.

## Why this round did not add new acts or expand the corpus
Same four acts (CSRD, Ecolabel, Climate Benchmarks, ETS Verification),
same raw HTML already collected — no new network collection was needed.
The corrections this round are about **construct validity and data
normalization**, not corpus coverage: fixing role-multiplicity direction
(RIT-007), splitting compound actor cells (RIT-004/005), separating
datasets by unit of analysis, and fixing screening patterns that bundled
more than one ontology. Ten adjudicated candidates (7 positive, 2 negative,
1 conditional) — up from nine in v2, because normalizing Ecolabel Art. 9(7)
correctly split one compound candidate into two atomic ones (testing vs.
verification body) — remain the right size for this stage: enough to
exercise every rule in `RIT_CODEBOOK_v3.md` (role multiplicity, chains,
negative controls, a conditional case), not enough to claim corpus coverage.

## A caught and corrected error, documented rather than hidden
The first draft of the accreditation relationship in the ETS chain (now
RIT-007) coded the national accreditation body as `R` with no distinct `I`
— effectively a dyadic reading that, if left uncorrected, would have
undermined the role-multiplicity claim built on it. Re-reading the evidence
already on file (the Article-14 peer-evaluation body's oversight of national
accreditation bodies, quoted in `SCREENING_CODEBOOK_v3.md`'s certification
examples) resolved the national accreditation body to `I`, with the Art-14
body as `R`. This is kept visible in `candidate_adjudications_v3.csv`'s
`adjudication_note` for CAND-09 rather than silently fixed, because the
correction process itself is evidence the relational test does real work,
not just confirms a first impression.
