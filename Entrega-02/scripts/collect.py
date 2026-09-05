"""Coleta o texto integral de um ato da UE via EUR-Lex, pelo numero CELEX.

Uso:
    python collect.py 32022L2464 csrd

Salva o HTML bruto em ../data/<slug>_raw.html
"""
import sys
import time
from pathlib import Path

import requests

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
HEADERS = {"User-Agent": "Mozilla/5.0 (academic research PoC; non-commercial)"}


def fetch_celex(celex: str) -> str:
    url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{celex}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.text


def main() -> None:
    if len(sys.argv) != 3:
        print("Uso: python collect.py <CELEX> <slug>")
        raise SystemExit(1)

    celex, slug = sys.argv[1], sys.argv[2]
    DATA_DIR.mkdir(exist_ok=True)
    out_path = DATA_DIR / f"{slug}_raw.html"

    html = fetch_celex(celex)
    out_path.write_text(html, encoding="utf-8")
    print(f"Salvo: {out_path} ({len(html)} bytes)")

    # taxa de requisicao deliberadamente baixa - PoC de um unico ato por vez
    time.sleep(1)


if __name__ == "__main__":
    main()
