# Relationship validation protocol v3 (Stage B / Stage C — not yet run)

This protocol is written but **not executed** — a second coder is required
and has not yet been engaged. Documenting the protocol before running it is
deliberate: it commits the design to a fixed procedure before any data from
a second coder could bias it.

## What is being validated
Not precision/recall (that fits Stage A's binary flag/no-flag question).
Stage B/C coding assigns roles, chain structure and multiple attributes per
relationship — the right instrument is **inter-coder agreement**, computed
per field, not one aggregate score.

## Procedure
1. A second coder receives: the same four source articles (full text, not
   pre-highlighted), `RIT_CODEBOOK_v3.md`, and `DATA_DICTIONARY_v3.md` —
   but **not** `candidate_adjudications_v3.csv` or `rit_relationships_v3.csv`
   from this round.
2. The second coder independently identifies candidates, applies the
   five-condition relational test, and codes positive cases into the same
   schema as `rit_relationships_v3.csv`.
3. Compare, per candidate/relationship:
   - Candidate identification (did both coders flag the same provisions as
     worth adjudicating?)
   - `relational_test_result` (positive/negative/conditional agreement)
   - `R_actor_id`/`I_actor_id`/`T_actor_id` identification (same actors,
     independent of id labels)
   - `primary_mechanism`/`secondary_mechanism`
   - The populated Stage C attributes (`formal_role_present`,
     `participation_in_scheme_voluntary`, `regulatory_level`, `sphere_primary`,
     `mode_of_operation`, `organizational_separation`,
     `legal_independence_required`, `supervision_present`)
4. Compute proportion agreement for every field above; compute Cohen's kappa
   where the category counts are large enough to support it (unlikely at
   n=7 relationships — proportion agreement plus a qualitative discussion of
   every disagreement is the realistic output of a pilot this size).
5. Adjudicate every disagreement explicitly. Where a disagreement reveals an
   ambiguous instruction in `RIT_CODEBOOK_v3.md` (not just a careless read),
   revise the codebook and record the revision in `CHANGELOG_v3.md`.

## Why this has not been run
Nine (now ten, after normalization) relationships coded by one person
demonstrate that the architecture is executable — they do not demonstrate
that it is reliable across coders. Claiming reliability without this step
would repeat, at the relationship level, the exact overclaiming the
`screening_confidence` renaming was meant to fix at the paragraph level
(`SCREENING_VALIDATION_v3.md`). This protocol is the next concrete task, not
a formality.

## Interim honesty
Until this runs, every relationship in `rit_relationships_v3.csv` should be
read as *this project's best single-coder reading*, evidence-anchored and
reasoned in `adjudication_note`, not as an inter-subjectively validated
fact.
