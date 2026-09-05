"""Stage A - Candidate Detection (v3).

Fixes the ontology-mixing bug flagged in review: a single regex pattern
must not bundle actor and instrument/mechanism alternatives together
(e.g. the old "verification (team|report|body)" mixed an actor
alternative - team/body - with an instrument alternative - report - under
one semantic_role). Each pattern below carries exactly one semantic_role.

Question this stage answers: does this provision contain textual evidence
potentially associated with regulatory intermediation? It performs
screening only - it does not determine whether a regulatory intermediary
exists. That determination is Stage B (relational adjudication, see
candidate_adjudications_v3.csv, built by hand from this output plus full
reading of the source article).

Usage:
    python screening_v3.py

Reads ../data/raw_html/<slug>_raw.html for slug in ACTS and writes
../data/screening_hits_v3.csv
"""
import csv
import re
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_DIR = DATA_DIR / "raw_html"

ACTS = {
    "csrd": "32022L2464",
    "ecolabel": "32010R0066",
    "climate_benchmarks": "32019R2089",
    "ets_verification": "32018R2067",
}

# Each entry: (regex, semantic_role). semantic_role in {actor, mechanism,
# instrument}. A pattern may only carry ONE semantic_role - bundled
# alternatives spanning more than one ontology must be split into separate
# entries (this is the v3 fix; see SCREENING_CODEBOOK_v3.md).
MECHANISM_RULES = {
    "reporting": {
        "anchor": [
            (r"sustainability reporting", "mechanism"),
            (r"sustainability report\b", "instrument"),
            (r"non-financial (report|statement)", "instrument"),
            (r"reporting (obligation|requirement)s?", "mechanism"),
            (r"management report", "instrument"),
            (r"consolidated (management|sustainability) report", "instrument"),
        ],
        "weak": [
            (r"\bshall report\b", "mechanism"),
            (r"\bshall disclose\b", "mechanism"),
            (r"\bshall publish\b", "mechanism"),
            (r"\breport\b", "instrument"),
        ],
        "exclude": [
            r"shall present a report to the European Parliament",
            r"report on the application of this (regulation|directive)",
            r"review (clause|report) (on|of) this (regulation|directive)",
        ],
    },
    "certification": {
        "anchor": [
            (r"(competent|accredited) bod(y|ies)", "actor"),
            (r"conformity assessment (body|bodies)", "actor"),
            (r"independent assurance services provider", "actor"),
            (r"national accreditation bod(y|ies)", "actor"),
            (r"certification (body|bodies)", "actor"),
            (r"certification scheme", "instrument"),
            (r"accreditation (process|scheme)", "mechanism"),
            (r"accreditation body", "actor"),
        ],
        "weak": [
            (r"\bcertificat\w*", "mechanism"),
            (r"\baccreditation\b", "mechanism"),
            (r"\baccredited\b", "mechanism"),
        ],
        "exclude": [],
    },
    "ranking_rating": {
        "anchor": [
            (r"benchmark administrator", "actor"),
            (r"benchmark methodology", "instrument"),
            (r"credit rating agenc(y|ies)", "actor"),
            (r"rating agenc(y|ies)", "actor"),
            (r"EU (Climate Transition|Paris-aligned) Benchmark", "instrument"),
        ],
        "weak": [
            (r"\bbenchmark\w*", "instrument"),
            (r"\brating\b", "instrument"),
            (r"\branking\b", "mechanism"),
            (r"\bscore\b", "instrument"),
        ],
        "exclude": [
            r"shall present a report to the European Parliament",
            r"review (clause|report) (on|of) this (regulation|directive)",
        ],
    },
    "auditing": {
        "anchor": [
            (r"statutory auditor", "actor"),
            (r"audit firm", "actor"),
            (r"(EU ETS )?(lead )?auditor", "actor"),
            (r"assurance provider", "actor"),
            (r"assurance (engagement|opinion|services)", "mechanism"),
            (r"verification (team|body)", "actor"),
            (r"verification report", "instrument"),
            (r"accredited verifier", "actor"),
            (r"quality assurance review", "mechanism"),
        ],
        "weak": [
            (r"\baudit\w*", "mechanism"),
            (r"\bassurance\b", "mechanism"),
        ],
        "exclude": [
            r"Court of Auditors",
        ],
    },
}

ARTICLE_CLASS = "oj-ti-art"
SUBTITLE_CLASS = "oj-sti-art"
SECTION_CLASSES = {"oj-ti-section-1", "oj-ti-section-2"}
BODY_CLASSES = {"oj-normal", "oj-sti-art"}
AMENDS_PATTERN = re.compile(
    r"Amendments? to (Directive|Regulation) \(?[A-Z]*\)?\s*[\d/]+", re.IGNORECASE
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def _first_match(patterns, text):
    for pattern, role in patterns:
        m = re.search(pattern, text, flags=re.IGNORECASE)
        if m:
            return pattern, role, m.group(0)
    return None, None, None


def classify(mechanism: str, text: str):
    rules = MECHANISM_RULES[mechanism]
    if any(re.search(p, text, flags=re.IGNORECASE) for p in rules["exclude"]):
        return None
    pattern, role, keyword = _first_match(rules["anchor"], text)
    if pattern:
        return "high", pattern, role, keyword
    pattern, role, keyword = _first_match(rules["weak"], text)
    if pattern:
        return "low", pattern, role, keyword
    return None


def screen_act(slug: str, celex: str, counter):
    html_path = RAW_DIR / f"{slug}_raw.html"
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    rows = []
    carrier_article = None
    carrier_section = None
    amended_act = ""

    for p in soup.find_all("p"):
        classes = set(p.get("class") or [])
        text = normalize(p.get_text())
        if not text:
            continue
        if ARTICLE_CLASS in classes:
            carrier_article = text
            continue
        if classes & SECTION_CLASSES:
            carrier_section = text
            continue
        if SUBTITLE_CLASS in classes and AMENDS_PATTERN.search(text):
            amended_act = text
        if not (classes & BODY_CLASSES):
            continue

        provision_type = "recital" if carrier_article is None else "article"

        for mechanism in MECHANISM_RULES:
            result = classify(mechanism, text)
            if result is None:
                continue
            confidence, pattern, role, keyword = result
            counter[0] += 1
            rows.append(
                {
                    "screening_id": f"SCR-{counter[0]:05d}",
                    "source_celex": celex,
                    "amended_act": amended_act,
                    "article": carrier_article or "",
                    "carrier_section": carrier_section or "",
                    "provision_type": provision_type,
                    "candidate_mechanism": mechanism,
                    "semantic_role": role,
                    "matched_pattern": pattern,
                    "matched_keyword": keyword,
                    "screening_confidence": confidence,
                    "evidence_text": text[:500],
                }
            )
    return rows


def main() -> None:
    fieldnames = [
        "screening_id", "source_celex", "amended_act", "article",
        "carrier_section", "provision_type", "candidate_mechanism",
        "semantic_role", "matched_pattern", "matched_keyword",
        "screening_confidence", "evidence_text",
    ]
    all_rows = []
    counter = [0]
    for slug, celex in ACTS.items():
        rows = screen_act(slug, celex, counter)
        all_rows.extend(rows)
        high = sum(1 for r in rows if r["screening_confidence"] == "high")
        low = len(rows) - high
        print(f"{slug}: {len(rows)} hits ({high} high, {low} low)")

    out_path = DATA_DIR / "screening_hits_v3.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nTotal: {len(all_rows)} linhas escritas em {out_path}")


if __name__ == "__main__":
    main()
