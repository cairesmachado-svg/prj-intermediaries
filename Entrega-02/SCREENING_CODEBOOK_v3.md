# Screening codebook v3 (Stage A — candidate detection)

Supersedes `SCREENING_CODEBOOK.md`/`CODEBOOK.md` (v2, kept in `v1/PoC/` for
the record). The mechanism categories and pattern counts are essentially
unchanged (same 1,079 total hits over the same four acts); what changed is
the **ontology discipline** of the patterns themselves.

## The bug this version fixes
Two v2 patterns bundled more than one `semantic_role` under a single regex,
flagged directly in review:

- `verification (team|report|body)` mixed **actor** alternatives (team,
  body) with an **instrument** alternative (report) under one pattern and
  one tag.
- `assurance (engagement|opinion|provider|services)` mixed an **actor**
  alternative (provider) with **mechanism/instrument** alternatives
  (engagement, opinion, services).

Both were split in `scripts/screening_v3.py`:
- `verification (team|body)` → `actor`; `verification report` → `instrument`
  (separate patterns).
- `assurance provider` → `actor`; `assurance (engagement|opinion|services)`
  → `mechanism` (separate patterns).

Re-running the full four-act screening with the split patterns produced
**exactly the same totals** (1,079 hits, same per-act high/low split) —
confirming the fix corrected metadata, not matching behaviour.

## Rule going forward
Every pattern in `screening_v3.py` carries exactly one `semantic_role`
(`actor` / `mechanism` / `instrument`). A pattern that would need to express
alternatives spanning more than one ontology must be split into separate
regex entries, never merged under one tag. Only `actor`-tagged hits point
directly at a Stage B candidate; `mechanism`/`instrument` hits locate
relevant context, nothing more.

## Where the patterns and counts live
`data/screening_hits_v3.csv` (1,079 rows, one per paragraph×mechanism hit)
carries `candidate_mechanism`, `semantic_role`, `matched_pattern`,
`screening_confidence` (`high`/`low` — never "confirmed"; see
RIT_CODEBOOK_v3.md), and `evidence_text`. It does **not** carry
`intermediary_validated` — that determination belongs to
`candidate_adjudications_v3.csv`, a different unit of analysis (see
CHANGELOG_v3.md, point on dataset separation).

## Semantic-role tally (this run)
| Mechanism | actor | mechanism | instrument |
|---|---|---|---|
| reporting | 0 | 269 | 202 |
| certification | 208 | 47 | 0 |
| ranking_rating | 13 | 0 | 52 |
| auditing | 133 | 115 | 40 |

Unchanged from v2's finding: `reporting` still has zero `actor`-tagged
patterns — consistent with Stage B's finding that reporting alone rarely
yields a standalone intermediary (CAND-03).
