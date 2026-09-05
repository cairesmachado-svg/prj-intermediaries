"""Triagem lexical (Stage A) dos quatro mecanismos de intermediacao (reportar,
certificacao, ranking/rating, auditoria) sobre o texto de um ato da UE ja
coletado por collect.py.

v3 (pos-revisao critica): esta etapa e explicitamente "screening", nao
codificacao final de intermediarios. Ela responde "este paragrafo contem um
sinal textual associado a um mecanismo?", nao "existe aqui um regulatory
intermediary, entre quem e quem, sob que desenho institucional?" - essa
segunda pergunta e respondida em Stage B (ver ../data/rit_coded_sample.csv e
../RIT_CODING.md), a partir dos paragrafos que esta triagem localiza.

Mudancas de nomenclatura em relacao a v2 (ver GOLD_STANDARD_VALIDATION.md):
- status="confirmado"/"candidato" -> screening_confidence="high"/"low". Um
  match de alta confianca e um sinal textual forte, nao uma confirmacao de
  que a arquitetura R-I-T (regulator-intermediary-target) esta presente.
- verificar_humano removido (redundante com screening_confidence="low").
- nova coluna intermediary_validated (0/1): 0 por padrao em toda a base;
  so recebe 1 nas linhas cobertas pela codificacao R-I-T manual de
  rit_coded_sample.csv, feita fora deste script.
- nova coluna provision_type (recital/article): recitals (paragrafos do
  preambulo, numerados "(n)" antes do primeiro "Article 1") tem peso
  juridico diferente de dispositivos operativos (artigos) - um nao deveria
  herdar automaticamente o status do outro.
- nova coluna amended_act: quando o ato processado e ele proprio uma diretiva
  ou regulamento modificador (ex.: a CSRD altera a Directive 2013/34/EU, a
  2006/43/EC, a 2004/109/EC e o Regulation 537/2014), esta coluna registra
  qual ato esta sendo alterado no trecho em questao, distinguindo-o do
  source_act (o CELEX processado). Detectado a partir do subtitulo
  "Amendments to Directive/Regulation ..." (classe oj-sti-art) que antecede
  cada bloco de emenda no HTML da EUR-Lex.

Uso:
    python codebook_screen.py csrd 32022L2464

Le ../data/<slug>_raw.html e escreve ../data/<slug>_dataset.csv
"""
import csv
import re
import sys
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Os quatro mecanismos primarios da proposta de David Levi-Faur (secao A4).
# "anchor": confirma o mecanismo sozinho (screening_confidence=high).
# "weak": sinal generico, insuficiente sozinho (screening_confidence=low).
# "exclude": descarta o match mesmo com anchor/weak presente.
MECHANISM_RULES = {
    "reportar": {
        "anchor": [
            r"sustainability reporting",
            r"sustainability report\b",
            r"non-financial (report|statement)",
            r"reporting (obligation|requirement)s?",
            r"management report",
            r"consolidated (management|sustainability) report",
        ],
        "weak": [
            r"\bshall report\b",
            r"\bshall disclose\b",
            r"\bshall publish\b",
            r"\breport\b",
        ],
        "exclude": [
            r"shall present a report to the European Parliament",
            r"report on the application of this (regulation|directive)",
            r"review (clause|report) (on|of) this (regulation|directive)",
        ],
    },
    "certificacao": {
        "anchor": [
            r"(competent|accredited) bod(y|ies)",
            r"conformity assessment (body|bodies)",
            r"independent assurance services provider",
            r"national accreditation bod(y|ies)",
            r"certification (body|bodies|scheme)",
            r"accreditation (process|scheme|body)",
        ],
        "weak": [
            r"\bcertificat\w*",
            r"\baccreditation\b",
            r"\baccredited\b",
        ],
        "exclude": [],
    },
    "ranking_rating": {
        "anchor": [
            r"benchmark administrator",
            r"benchmark methodology",
            r"credit rating agenc(y|ies)",
            r"rating agenc(y|ies)",
            r"EU (Climate Transition|Paris-aligned) Benchmark",
        ],
        "weak": [
            r"\bbenchmark\w*",
            r"\brating\b",
            r"\branking\b",
            r"\bscore\b",
        ],
        "exclude": [
            r"shall present a report to the European Parliament",
            r"review (clause|report) (on|of) this (regulation|directive)",
        ],
    },
    "auditoria": {
        "anchor": [
            r"statutory auditor",
            r"audit firm",
            r"(EU ETS )?(lead )?auditor",
            r"assurance (engagement|opinion|provider|services)",
            r"verification (team|report|body)",
            r"accredited verifier",
            r"quality assurance review",
        ],
        "weak": [
            r"\baudit\w*",
            r"\bassurance\b",
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
RECITAL_PATTERN = re.compile(r"^\((\d+)\)\s")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def _first_match(patterns, text):
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return pattern, match.group(0)
    return None, None


def classify(mechanism: str, text: str):
    """Retorna (screening_confidence, regra, trecho) ou None se nao houver match."""
    rules = MECHANISM_RULES[mechanism]

    if any(re.search(p, text, flags=re.IGNORECASE) for p in rules["exclude"]):
        return None

    pattern, keyword = _first_match(rules["anchor"], text)
    if pattern:
        return "high", pattern, keyword

    pattern, keyword = _first_match(rules["weak"], text)
    if pattern:
        return "low", pattern, keyword

    return None


def screen(html: str, celex: str):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    carrier_article = None
    carrier_section = None
    amended_act = ""
    seen_first_article = False

    for p in soup.find_all("p"):
        classes = set(p.get("class") or [])
        text = normalize(p.get_text())
        if not text:
            continue

        if ARTICLE_CLASS in classes:
            carrier_article = text
            seen_first_article = True
            continue
        if classes & SECTION_CLASSES:
            carrier_section = text
            continue
        if SUBTITLE_CLASS in classes and AMENDS_PATTERN.search(text):
            amended_act = text
        if not (classes & BODY_CLASSES):
            continue

        provision_type = "recital" if not seen_first_article else "article"

        for mechanism in MECHANISM_RULES:
            result = classify(mechanism, text)
            if result is None:
                continue
            confidence, pattern, keyword = result
            rows.append(
                {
                    "source_act": celex,
                    "amended_act": amended_act,
                    "carrier_article": carrier_article or "",
                    "carrier_section": carrier_section or "",
                    "provision_type": provision_type,
                    "mechanism": mechanism,
                    "screening_confidence": confidence,
                    "intermediary_validated": 0,
                    "matched_pattern": pattern,
                    "matched_keyword": keyword,
                    "evidence_text": text[:500],
                }
            )

    return rows


def main() -> None:
    if len(sys.argv) != 3:
        print("Uso: python codebook_screen.py <slug> <CELEX>")
        raise SystemExit(1)

    slug, celex = sys.argv[1], sys.argv[2]
    html_path = DATA_DIR / f"{slug}_raw.html"
    if not html_path.exists():
        print(f"Nao encontrado: {html_path}. Rode collect.py primeiro.")
        raise SystemExit(1)

    html = html_path.read_text(encoding="utf-8")
    rows = screen(html, celex)

    out_path = DATA_DIR / f"{slug}_dataset.csv"
    fieldnames = [
        "source_act",
        "amended_act",
        "carrier_article",
        "carrier_section",
        "provision_type",
        "mechanism",
        "screening_confidence",
        "intermediary_validated",
        "matched_pattern",
        "matched_keyword",
        "evidence_text",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    high = sum(1 for r in rows if r["screening_confidence"] == "high")
    low = sum(1 for r in rows if r["screening_confidence"] == "low")
    print(f"{len(rows)} linhas escritas em {out_path}")
    print(f"  screening_confidence=high: {high}")
    print(f"  screening_confidence=low: {low}")
    by_mechanism = {}
    for row in rows:
        key = (row["mechanism"], row["screening_confidence"])
        by_mechanism[key] = by_mechanism.get(key, 0) + 1
    for (mechanism, confidence), count in sorted(by_mechanism.items()):
        print(f"    {mechanism} / {confidence}: {count}")


if __name__ == "__main__":
    main()
