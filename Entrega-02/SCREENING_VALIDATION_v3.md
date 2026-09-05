# Screening validation v3 (Stage A only)

Renames and supersedes `GOLD_STANDARD_VALIDATION.md` (v1) and
`VALIDATION_PROTOCOL.md` (v2) for Stage A. "Gold standard" is retired for
good — replaced by **manually adjudicated pilot reference sample**,
reflecting what a small, non-random sample can actually support.

## Method (unchanged from v1/v2)
For one article per act, every paragraph was read manually, without regex,
and marked for whether it substantively concerns intermediation content
(not merely whether it repeats an anchor term). That reading was compared
against `screening_v3.py`'s output on the same paragraphs. Re-running the
comparison after the v3 pattern split (`SCREENING_CODEBOOK_v3.md`) changes
nothing numerically — the split only reclassified `semantic_role`, not
which paragraphs matched.

## Result
**35 judged paragraphs: precision 100% (33/33), recall 94.3% (33/35), F1
97.1%.** Both misses share one cause: the paragraph describes the
relationship from the regulator's or target's side without repeating the
intermediary's own name. Full detail and both misses quoted in full:
`v1/PoC/GOLD_STANDARD_VALIDATION.md` (kept for the record, terminology
superseded here).

## Scope limits
- Small, non-random sample (the richest article per act).
- Tests only whether Stage A flags paragraphs that concern *some*
  intermediation content — not whether the mechanism assigned is correct,
  and not recall outside the four coded articles.
- **Does not validate Stage B or Stage C.** A `screening_confidence=high`
  paragraph is strong lexical evidence, nothing more — every candidate it
  produces still requires the full five-condition relational test
  (`RIT_CODEBOOK_v3.md`) before being treated as an intermediary. This
  sentence exists because an earlier draft of this project's own
  documentation once read as if `high` meant "no human review needed" —
  it does not, and no phrasing here should be read that way again.

## What is not yet done
Stage B and Stage C validation (inter-coder reliability) — see
`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`.
