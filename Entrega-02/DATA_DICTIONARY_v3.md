# Data dictionary v3

Supersedes `DATA_DICTIONARY.md` (v2). Covers three datasets
(`screening_hits_v3.csv`, `candidate_adjudications_v3.csv`,
`rit_relationships_v3.csv`) plus the lookup table `actors_v3.csv`. Each
populated variable gets the full field set requested in review; deferred
variables (not coded in this pilot) are listed in condensed form at the end,
each tagged with why.

Missingness codes throughout: `1`=explicitly present, `0`=explicitly absent,
`NA`=not applicable, `UNK`=unknown/insufficient information,
`NOE`=not observable from legal text alone, `EXT`=requires external
evidence.

---

## `intermediary_present` (rit_relationships_v3.csv / candidate_adjudications_v3.csv)
- **theoretical_construct:** Regulatory intermediation
- **dimension:** Relational structure
- **operational_definition:** Whether a third actor, analytically distinct from R and T, mediates the relationship (relational test, RIT_CODEBOOK_v3.md)
- **unit_of_analysis:** relationship / candidate
- **allowed_values:** `1`, `0`
- **observability_class:** INFERRED (requires applying the five-condition test, not a single lexical marker)
- **evidence_required:** Explicit text naming the third actor's mediating function, or a documented institutional reconstruction
- **coding_rule:** `1` only if all five relational-test conditions hold
- **positive_example:** RIT-006 — verifier named alongside operator and competent authority as a distinct responsibility-holder (Art. 27(3)(j))
- **negative_example:** CAND-03 — direct reporting duty, no third actor
- **ambiguity_rule:** If condition (a) or (e) cannot be shown, code `conditional`, not `1`
- **theoretical_source:** Levi-Faur proposal, section A4 (intermediation as actors+mechanisms+strategies mediating R-T)

## `reporting_mechanism_present` (rit_relationships_v3.csv)
- **theoretical_construct:** Reporting mechanism
- **dimension:** Mechanism
- **operational_definition:** Whether a duty to disclose information exists in the relationship, independent of whether an intermediary is present
- **unit_of_analysis:** relationship
- **allowed_values:** `1`, `0`
- **observability_class:** DIRECT
- **evidence_required:** Explicit disclosure/reporting obligation in the text
- **coding_rule:** Code independently of `intermediary_present` — never conflate the two
- **positive_example:** RIT-001 (`reporting_mechanism_present=1`, `intermediary_present=1`)
- **negative_example:** RIT-003 (`reporting_mechanism_present=0` — Ecolabel Art. 9 is a certification act, not a reporting duty)
- **ambiguity_rule:** A provision can have `reporting_mechanism_present=1` and `intermediary_present=0` (CAND-03) — this combination is expected, not an error
- **theoretical_source:** Levi-Faur proposal, mechanism taxonomy (A4)

## `primary_mechanism` / `secondary_mechanism` (rit_relationships_v3.csv, screening_hits_v3.csv as `candidate_mechanism`)
- **theoretical_construct:** Mechanism typology
- **dimension:** Mechanism
- **operational_definition:** The dominant / a secondary mechanism through which the intermediary operates
- **unit_of_analysis:** relationship (Stage C); provision×signal (Stage A, as `candidate_mechanism`)
- **allowed_values:** `reporting`, `certification`, `ranking_rating`, `auditing`, `other_mechanism` (reserved, unused), blank
- **observability_class:** DIRECT (Stage A) / INFERRED (Stage C, when the relationship combines mechanisms)
- **evidence_required:** Verbatim text supporting the assigned mechanism
- **coding_rule:** A relationship may have both a primary and a secondary mechanism (e.g. RIT-004: auditing + certification)
- **positive_example:** RIT-002 — `auditing` (assurance work review)
- **negative_example:** —
- **ambiguity_rule:** These four are the mechanisms selected for the proposal's empirical design, not claimed as an exhaustive ontology — `other_mechanism` exists for future cases that do not fit
- **theoretical_source:** Levi-Faur proposal, section A4

## `chain_id` / `intermediation_level` / `parent_relationship_id` (rit_relationships_v3.csv)
- **theoretical_construct:** Meta-regulation / enhanced self-regulation
- **dimension:** Institutional design
- **operational_definition:** Groups relationships in which one intermediary is itself governed by another; `L1` = mediates the primary R-T relationship, `L2` = a second intermediary/regulator governs the `L1` actor
- **unit_of_analysis:** relationship
- **allowed_values:** free-text chain id or blank; `L1`/`L2`/`NA`; `relationship_id` or blank
- **observability_class:** INFERRED
- **evidence_required:** Two or more relationships whose actors overlap across a governance layer
- **coding_rule:** Never compress a chain into one artificial triad — decompose (see RIT_CODEBOOK_v3.md normalization rule)
- **positive_example:** CHAIN-ETS-1 (RIT-006 L1 → RIT-007 L2)
- **negative_example:** RIT-003 (`chain_id` present but it is the L1 anchor, `parent_relationship_id` blank)
- **ambiguity_rule:** Marked explicitly as an operational proposal for this dataset, not a classification already fixed in the proposal
- **theoretical_source:** Levi-Faur proposal's discussion of enhanced self-regulation / meta-regulation (extrapolated terminology, flagged as such)

## `R_actor_id` / `I_actor_id` / `T_actor_id` (rit_relationships_v3.csv)
- **theoretical_construct:** R-I-T architecture
- **dimension:** Relational structure
- **operational_definition:** Foreign keys into `actors_v3.csv` identifying the regulator, intermediary and target *in this specific relationship*
- **unit_of_analysis:** relationship
- **allowed_values:** `actor_id` from `actors_v3.csv`
- **observability_class:** DIRECT (identity) + INFERRED (role assignment)
- **evidence_required:** `verbatim_evidence` field on the same row
- **coding_rule:** The three ids on one row must be pairwise distinct (R≠I≠T within the same relationship); role assignment must be re-derived per relationship, never copied from the actor's role in another relationship
- **positive_example:** RIT-007, where correcting the initial (incorrect) direct national-accreditation-body→verifier reading required introducing ACT-19 as R once the peer-evaluation evidence was found
- **negative_example:** an earlier draft had `I_actor_id = T_actor_id = ACT-16` on one row — caught and fixed before finalising (see CHANGELOG_v3.md)
- **ambiguity_rule:** If R cannot be identified from the specific provision, mark `R_actor_id` as the closest documented instrument (e.g. "not named in this article - see Regulation X") rather than leaving blank, and lower `construct_validity` accordingly
- **theoretical_source:** Levi-Faur proposal, core R-I-T framing

## `formal_role_present` (rit_relationships_v3.csv, as `formal_role_present`)
- **theoretical_construct:** Formal/legal role (intermediary attribute)
- **dimension:** Institutional design
- **operational_definition:** Whether the intermediary's role is explicitly established in legislation
- **unit_of_analysis:** relationship
- **allowed_values:** `1`, `0`
- **observability_class:** DIRECT
- **evidence_required:** Explicit textual designation of the role
- **coding_rule:** `1` if the act itself names/defines the role (e.g. defines "audit firm"); `0` if the actor appears without formal designation
- **positive_example:** RIT-001 (Art. 27a explicitly assigns the group auditor's role)
- **negative_example:** RIT-004 (`formal_role_present=0` — ISO 17025 accreditation is referenced, not formally established by this Regulation itself)
- **ambiguity_rule:** —
- **theoretical_source:** Levi-Faur proposal, intermediary attributes list

## `participation_in_scheme_voluntary` / `use_of_intermediary_mandatory` (rit_relationships_v3.csv)
- **theoretical_construct:** Voluntarism (intermediary attribute)
- **dimension:** Institutional design
- **operational_definition:** Separates whether *joining the scheme* is voluntary from whether, once joined, *using the intermediary* is mandatory
- **unit_of_analysis:** relationship
- **allowed_values:** `0`, `1`
- **observability_class:** DIRECT
- **evidence_required:** Explicit statement of voluntary application vs. mandatory procedure once engaged
- **coding_rule:** Code both fields independently — a scheme can be voluntary to join and mandatory to comply with once joined
- **positive_example:** RIT-003 (Ecolabel: `participation_in_scheme_voluntary=1`, `use_of_intermediary_mandatory=1` — applying is optional, but an applicant must go through the competent body)
- **negative_example:** RIT-001 (CSRD: both effectively mandatory — no opt-in)
- **ambiguity_rule:** —
- **theoretical_source:** Levi-Faur proposal, voluntarism attribute — this specific two-field split is this dataset's operationalisation, not Levi-Faur's own wording

## `regulatory_level` (rit_relationships_v3.csv)
- **theoretical_construct:** Level (intermediary attribute)
- **dimension:** Institutional design
- **operational_definition:** Jurisdictional level(s) at which the arrangement operates
- **unit_of_analysis:** relationship
- **allowed_values:** `EU`, `national`, `hybrid (...)`, free text describing a multi-level arrangement
- **observability_class:** DIRECT
- **evidence_required:** Text naming the jurisdiction(s) involved
- **coding_rule:** Use free text for genuinely multi-level cases rather than forcing a single category
- **positive_example:** RIT-003 (`"hybrid (EU criteria; Member-State-designated body)"`)
- **negative_example:** —
- **ambiguity_rule:** —
- **theoretical_source:** Levi-Faur proposal, level attribute

## `mode_of_operation` (rit_relationships_v3.csv)
- **theoretical_construct:** Mode of operation (intermediary attribute)
- **dimension:** Institutional design
- **operational_definition:** Which of the proposal's four governance modes the intermediary's role most resembles
- **unit_of_analysis:** relationship
- **allowed_values:** `state_led`, `business_led`, `NGO_led`, `professional_led`, `hybrid`, `unclear`
- **observability_class:** INFERRED
- **evidence_required:** Actor type and institutional context of the intermediary
- **coding_rule:** Analytical coding, not an ontological property of the actor — the same actor type could be coded differently in a different relationship
- **positive_example:** RIT-006 (`professional_led` — accredited verification profession)
- **negative_example:** —
- **ambiguity_rule:** —
- **theoretical_source:** Levi-Faur proposal, mode-of-operation attribute (mapped directly to the proposal's four mechanism-led categories)

## `organizational_separation` (rit_relationships_v3.csv)
- **theoretical_construct:** Degree of separation (intermediary attribute)
- **dimension:** Institutional design
- **operational_definition:** Whether the intermediary is organisationally internal or external to R/T
- **unit_of_analysis:** relationship
- **allowed_values:** `internal`, `external`, `hybrid`, `NA`
- **observability_class:** INFERRED
- **evidence_required:** Institutional description of the intermediary's organisational location
- **coding_rule:** Not decomposed further (functional/financial separation) in this pilot — see deferred variables below
- **positive_example:** RIT-001 (`external` — the group auditor is external to both the competent authority and the undertaking)
- **negative_example:** —
- **ambiguity_rule:** —
- **theoretical_source:** Levi-Faur proposal, degree-of-separation attribute

## `legal_independence_required` (rit_relationships_v3.csv)
- **theoretical_construct:** Autonomy (independence)
- **dimension:** Autonomy — the only autonomy indicator populated in this pilot
- **operational_definition:** Whether the act explicitly requires the intermediary's independence
- **unit_of_analysis:** relationship
- **allowed_values:** `1`, `0`, `UNK`, `EXT`
- **observability_class:** DIRECT when coded `1`; otherwise the honest default is `UNK`, not `0`
- **evidence_required:** Explicit independence requirement in the text
- **coding_rule:** Only code `1` on explicit textual basis (Directive 2006/43/EC's independence regime for statutory auditors, referenced for RIT-001/RIT-006); leave `UNK` rather than inferring absence
- **positive_example:** RIT-001, RIT-006 (`1`)
- **negative_example:** RIT-002 (`UNK` — not verified for the subsidiary-level provider specifically in this reading)
- **ambiguity_rule:** The full autonomy battery (conflict-of-interest, appointment, removal, financial independence) remains deferred — see below
- **theoretical_source:** Levi-Faur proposal, autonomy as second-order construct

## `supervision_present` (rit_relationships_v3.csv)
- **theoretical_construct:** Accountability (oversight) — the only accountability indicator populated in this pilot
- **dimension:** Accountability
- **operational_definition:** Whether a named authority supervises the intermediary's work
- **unit_of_analysis:** relationship
- **allowed_values:** `1`, `0`, `UNK`
- **observability_class:** DIRECT
- **evidence_required:** Text naming a supervisory authority and function
- **coding_rule:** —
- **positive_example:** RIT-006 (competent authority receives and can act on the verification report)
- **negative_example:** RIT-004 (`UNK` — not established in the single sub-paragraph read)
- **ambiguity_rule:** Full accountability battery deferred — see below
- **theoretical_source:** Levi-Faur proposal, accountability as second-order construct

## `relational_test_result` (candidate_adjudications_v3.csv)
- **theoretical_construct:** —
- **dimension:** Adjudication outcome
- **operational_definition:** Outcome of applying the five-condition relational test to a candidate
- **unit_of_analysis:** candidate
- **allowed_values:** `positive`, `negative`, `conditional`, `insufficient_evidence`
- **observability_class:** INFERRED (requires applying all five conditions)
- **evidence_required:** `adjudication_note` on the same row
- **coding_rule:** Only `positive` rows receive a `resulting_relationship_id` and are promoted to `rit_relationships_v3.csv`
- **positive_example:** CAND-01 → `positive` → RIT-001
- **negative_example:** CAND-03, CAND-06 → `negative`
- **ambiguity_rule:** CAND-07 → `conditional` — held in quarantine, not force-resolved
- **theoretical_source:** This dataset's operationalisation of the relational test, grounded in Levi-Faur's R-I-T framing

---

## Deferred variables (defined, not populated in this pilot)

| Variable(s) | Construct | Why deferred |
|---|---|---|
| `motivation` | Motivation | Cannot be safely inferred from organisational form alone; requires `NOE` unless stated explicitly — not checked per-relationship in this round |
| `intermediation_centrality` | Centrality | Requires a criterion beyond mention count (explicitly not hit-count); not yet defined operationally |
| `conflict_of_interest_rule`, `appointment_by_regulator`, `appointment_by_target`, `removal_protection`, `financial_independence_rule`, `discretionary_authority`, `professional_independence`, `organizational_independence_required`, `impartiality_required` | Autonomy (full battery) | Only `legal_independence_required` populated this round; the rest need a second coder to check before being trusted across 7 relationships |
| `reporting_to_regulator`, `recordkeeping_obligation`, `periodic_review`, `accreditation` (as a 0/1 accountability field, distinct from `accreditation_present`), `licensing_or_approval`, `sanction`, `withdrawal_or_suspension`, `transparency_requirement`, `appeal_or_review`, `external_audit`, `peer_review` | Accountability (full battery) | Only `supervision_present` populated this round; same reasoning as autonomy |
| `responsibilization_present`, `responsibilization_confidence`, `empowerment_present`, `empowerment_confidence` | Strategies of intermediation | Explicitly designed as two independent, non-dichotomous batteries (RIT_CODEBOOK_v3.md); not scored in this round |
| `design_addresses_capture`, `design_addresses_incompetence`, `design_addresses_under_commitment`, `design_addresses_over_commitment` | Failure risks addressed by design | Requires checking each relationship specifically for a preventive rule; not done for all 7 rows |
| `number_of_authority_centres`, `public_private_mix`, `self_regulatory_component`, `regulatory_competition`, `multilevel_governance`, `multiple_intermediaries` | Polycentric/monocentric structural indicators | Act-level or regime-level, not relationship-level — require broader reading than one provision |
| `stated_regulatory_objective` (effectiveness/legitimacy/trust language) | Downstream outcomes | Explicitly out of scope for legal-text coding — see RIT_CODEBOOK_v3.md |

Populating these for seven relationships without a second coder to check the
harder judgment calls would manufacture a false sense of precision — they
are scoped for the next round (`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`),
not silently skipped.
