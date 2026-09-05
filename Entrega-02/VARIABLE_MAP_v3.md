# Variable map v3

Supersedes `VARIABLE_MAP.md`. Same purpose — make
**construct → dimension → indicator → variable → unit → evidence** explicit
— updated for the three-dataset structure.

| Theoretical construct | Dimension | Indicator | Variable | Unit | Evidence | Status |
|---|---|---|---|---|---|---|
| Regulatory intermediation | Relational structure | Intermediary mediates R-T | `intermediary_present` | relationship / candidate | provision(s) | populated |
| Regulatory intermediation | Relational structure | Regulator/intermediary/target identity | `R_actor_id`/`I_actor_id`/`T_actor_id` | relationship | provision(s) | populated |
| Regulatory intermediation | Role multiplicity | Same actor, different role across relationships | cross-reference of actor ids across `rit_relationships_v3.csv` rows | relationship (cross-row) | provision(s) | populated (RIT-006/007) |
| Regulatory intermediation | Meta-regulation | Intermediary governed by another intermediary | `chain_id`, `intermediation_level`, `parent_relationship_id` | relationship | provision(s), chained | populated |
| Mechanism (Levi-Faur A4) | Reporting | State-led disclosure duty | `primary_mechanism`/`reporting_mechanism_present` | relationship | provision | populated |
| Mechanism (Levi-Faur A4) | Certification | NGO/technical-body attestation | `primary_mechanism` = `certification` | relationship | provision | populated |
| Mechanism (Levi-Faur A4) | Ranking/rating | Business-led ordering/scoring | `primary_mechanism` = `ranking_rating` | candidate (quarantined) | provision | populated, `conditional` |
| Mechanism (Levi-Faur A4) | Auditing | Profession-led verification | `primary_mechanism` = `auditing` | relationship | provision | populated |
| Intermediary attribute | Formal/legal role | Explicit legislative establishment | `formal_role_present` | relationship | provision | populated |
| Intermediary attribute | Voluntarism | Scheme participation vs. intermediary use | `participation_in_scheme_voluntary`, `use_of_intermediary_mandatory` | relationship | provision | populated |
| Intermediary attribute | Level | Jurisdictional level | `regulatory_level` | relationship | provision | populated |
| Intermediary attribute | Sphere | Policy domain | `sphere_primary` | relationship | provision | populated |
| Intermediary attribute | Mode of operation | State/business/NGO/professional-led | `mode_of_operation` | relationship | provision | populated |
| Intermediary attribute | Degree of separation | Internal/external | `organizational_separation` | relationship | provision | populated (undecomposed) |
| Intermediary attribute | Motivation | Underlying incentive | `motivation` | relationship | would require evidence beyond the provision | deferred |
| Intermediary attribute | Centrality | Institutional importance | `intermediation_centrality` | relationship | requires a non-frequency criterion | deferred |
| Autonomy | Independence | Legal independence requirement | `legal_independence_required` | relationship | provision | populated (partial battery) |
| Autonomy | Independence (full battery) | Conflict of interest, appointment, removal, financial independence | 9 variables, `DATA_DICTIONARY_v3.md` | relationship | provision, per-relationship check | deferred |
| Accountability | Oversight | Supervisory authority present | `supervision_present` | relationship | provision | populated (partial battery) |
| Accountability | Oversight (full battery) | Reporting, sanctions, transparency, appeal | 11 variables, `DATA_DICTIONARY_v3.md` | relationship | provision, per-relationship check | deferred |
| Strategy | Responsibilization | Mandatory, sanction-backed duty | `responsibilization_present`, `responsibilization_confidence` | relationship | provision | deferred |
| Strategy | Empowerment | Discretion, self-regulatory space, adaptive review | `empowerment_present`, `empowerment_confidence` | relationship | provision | deferred |
| Failure typology | Risk addressed by design | Preventive rule type | `design_addresses_capture` etc. | relationship | provision, interpreted cautiously | deferred |
| Polycentric/monocentric governance | Structural indicators | Number of authority centres, public/private mix | 6 variables, `DATA_DICTIONARY_v3.md` | act / regime (not relationship) | requires act-level reading | deferred |
| Downstream outcomes | Effectiveness / legitimacy / trust | Stated objective in the text | `stated_regulatory_objective` | relationship | provision (as objective, not outcome) | out of scope for this layer |

## What changed from v2's variable map
- Split `rule_source`/`direct_regulator`/`oversight_authority` (v2's
  deferred columns) is still deferred, but the actor table (`actors_v3.csv`)
  now at least separates actor **identity** from relationship-specific
  **role**, which v2's free-text `R_actor`/`I_actor`/`T_actor` columns did
  not.
- `ranking_rating` now explicitly shown as populated-but-quarantined
  (`conditional`), not silently counted alongside confirmed mechanisms.
- Strategies row split into two independent indicators (`responsibilization`,
  `empowerment`), replacing v2's implicit single-category framing.
