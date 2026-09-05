"""Junta os datasets por ato em um unico CSV consolidado, com coluna 'ato'.

Uso:
    python combine.py csrd ecolabel climate_benchmarks ets_verification
"""
import csv
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        print("Uso: python combine.py <slug1> <slug2> ...")
        raise SystemExit(1)

    fieldnames = [
        "ato",
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
    out_path = DATA_DIR / "combined_dataset.csv"
    total = 0
    with out_path.open("w", newline="", encoding="utf-8") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        for slug in slugs:
            csv_path = DATA_DIR / f"{slug}_dataset.csv"
            if not csv_path.exists():
                print(f"Aviso: {csv_path} nao encontrado, pulando.")
                continue
            with csv_path.open(encoding="utf-8") as in_f:
                for row in csv.DictReader(in_f):
                    row["ato"] = slug
                    writer.writerow(row)
                    total += 1

    print(f"{total} linhas combinadas em {out_path}")


if __name__ == "__main__":
    main()
