# PoC — Screening (Stage A) + codificação R-I-T (Stage B) em 4 atos da UE (transição verde)

Prova de conceito para a candidatura a Research Assistant/Partner do Prof.
David Levi-Faur ("Governance by and of Intermediaries"). Estrutura em dois
estágios, seguindo a revisão crítica de 05/09/2026 (ver `RIT_CODING.md`):

- **Stage A — screening lexical**: "este parágrafo tem um sinal textual
  associado a um mecanismo de intermediação?" — este arquivo e
  `CODEBOOK.md`.
- **Stage B — codificação R-I-T**: "existe aqui um regulatory intermediary,
  entre quem e quem, sob que desenho institucional?" — `RIT_CODING.md`, a
  partir dos parágrafos que o Stage A localiza.
- **Validação**: `GOLD_STANDARD_VALIDATION.md` mede precision/recall/F1 do
  Stage A contra leitura manual sem regex.
- **Porquê de cada escolha metodológica**: `METODOLOGIA.md`.

O Stage A não é a entrega final — é o funil que torna o Stage B viável em
escala. Um match de alta confiança no Stage A é um "high-confidence textual
hit", não uma confirmação de que a arquitetura R-I-T está presente naquele
dispositivo; por isso a v3 do schema usa `screening_confidence`
(`high`/`low`) em vez de `status` (`confirmado`/`candidato`), e reserva
`intermediary_validated=1` só para as linhas efetivamente codificadas em
Stage B.

## Atos analisados

| Ato | CELEX | Mecanismo-alvo | Por que este ato |
|---|---|---|---|
| CSRD (Corporate Sustainability Reporting Directive) | `32022L2464` | reportar + auditoria | Obriga reporte de sustentabilidade e sua garantia (assurance) por auditor/provedor independente |
| Rótulo Ecológico da UE (EU Ecolabel) | `32010R0066` | certificação | "Competent Bodies" certificam produtos com base em critérios ambientais |
| Referenciais Climáticos (Climate Benchmarks) | `32019R2089` | ranking/rating (validade condicional — ver `RIT_CODING.md`) | Cria categorias de índices de referência (benchmarks) alinhados ao clima, com requisitos de metodologia para os administradores |
| Verificação e Acreditação no EU ETS | `32018R2067` | auditoria (+ certificação) | Regula os verificadores de emissões de gases de efeito estufa e sua acreditação |

## Como rodar

```
cd scripts
python collect.py <CELEX> <slug>            # repetir para cada ato
python codebook_screen.py <slug> <CELEX>    # repetir para cada ato
python combine.py csrd ecolabel climate_benchmarks ets_verification
```

Saída: `data/<slug>_raw.html`, `data/<slug>_dataset.csv` por ato (Stage A), e
`data/combined_dataset.csv` com os 4 juntos. `data/rit_coded_sample.csv` é o
Stage B (codificação manual, não gerada pelo script).

## Resultados do Stage A (screening)

Cada linha carrega `screening_confidence` (`high`/`low`), `provision_type`
(`recital`/`article`), `amended_act` (quando aplicável) e
`intermediary_validated` (0 por padrão; 1 nas 76 linhas cobertas pelo Stage
B). Resumo: **764 de 1.079 linhas (71%) saem como `high`**, sem necessidade
de checagem humana imediata; **315 (29%) ficam como `low`**.

| Ato | Parágrafos | Artigos | Total | high | low |
|---|---|---|---|---|---|
| CSRD | 1.084 | 32 | 559 | 472 | 87 |
| Ecolabel | 394 | 20 | 94 | 73 | 21 |
| Climate Benchmarks | 208 | 7 | 61 | 37 | 24 |
| ETS Verificação | 1.067 | 79 | 365 | 182 | 183 |
| **Total** | | | **1.079** | **764 (71%)** | **315 (29%)** |

Cada um dos 4 atos tem um mecanismo claramente dominante e coerente com o
motivo da escolha (tabela acima) — os quatro mecanismos da proposta do David
têm pelo menos um ato-âncora com sinal forte, embora com validade de
construto diferente entre eles (ver `RIT_CODING.md` para o caso condicional
de Climate Benchmarks).

**`provision_type`, medido, não suposto:** dos 1.079 hits, 890 (82%) caem em
`article` e 189 (18%) em `recital`. Na CSRD especificamente, 413 de 559
(74%) são `article`. Isso corrige uma suposição de uma rodada anterior deste
documento, que afirmava que "a maioria dos hits vem do preâmbulo" sem ter
medido — a maioria, na verdade, já cai em dispositivo operativo.

**Ponto fraco remanescente, documentado em vez de escondido:** no ETS, o
mecanismo "reportar" ficou com só 5 `high` contra 119 `low`. Não é falha da
regra — o vocabulário de reporte do ETS ("emission report", "verification
report") está estruturalmente colado ao processo de auditoria (é o documento
que o verificador audita), então a regra corretamente hesita em confirmar
sozinha se aquele trecho é sobre o dever de reportar em si ou só menciona o
relatório enquanto objeto da verificação. Fica como `low` de propósito — ver
`METODOLOGIA.md`, seção 9.

## Validação
`GOLD_STANDARD_VALIDATION.md` cobre a validação rigorosa (leitura manual sem
regex, precision/recall/F1: 100% / 94,3% / 97,1% sobre 35 unidades
julgadas). Abaixo, a validação qualitativa original por amostra:

- **CSRD — reportar/auditoria**: hits relevantes ("reporting requirement",
  "sustainability report", "auditor", "assurance engagement").
- **Ecolabel — certificação**: limpo, com atribuição de artigo (Art. 4, 9,
  20).
- **Climate Benchmarks — ranking/rating**: hits lexicalmente limpos, mas ver
  o alerta de validade de construto em `RIT_CODING.md`, seção 3.
- **ETS Verificação — auditoria e certificação**: limpo e com atribuição de
  artigo. Os hits de "certificação" nesse ato são sobre a acreditação dos
  próprios verificadores — ver achado abaixo.

## Achado que vale registrar
No ETS, o mecanismo dominante nos hits automáticos não foi "auditoria" (87
linhas: 70 high + 17 low) e sim "certificação" (149 linhas: 107 high + 42
low), quase toda por "accreditation". Ao ler o texto, isso não é ruído: o
regime cria um **auditor que é, ele próprio, credenciado por um organismo de
acreditação** — os dois mecanismos aparecem empilhados no mesmo ato, um
garantindo o outro. Codificado explicitamente em `RIT_CODING.md`, seção 4,
como parte da tríade R-I-T do EU ETS.

## Limitações conhecidas
- Os 29% de hits `low` ainda não foram revisados um a um fora dos 4 artigos
  cobertos pelo Stage B; são a fila de verificação humana, não um resultado
  final.
- `GOLD_STANDARD_VALIDATION.md` usa os artigos mais ricos de cada ato, não
  uma amostra aleatória — os números de precision/recall são um teto
  otimista, não uma estimativa para o corpus inteiro.
- Fonte é a página HTML da EUR-Lex por CELEX, não a API SPARQL/Cellar —
  adequado para 4 atos escolhidos a dedo. Antes de migrar para SPARQL/Cellar
  em escala, falta um passo anterior: **definir a população** ("o que conta
  como legislação da UE sobre transição verde?") — SPARQL resolve *retrieval*,
  não define o universo. Ver `METODOLOGIA.md`, seção 10.
- O Stage B (`RIT_CODING.md`) cobre 4 provisões, não o corpus — é prova de
  que o passo é executável a partir do Stage A, não uma codificação em
  escala.

## Arquivos
- `scripts/collect.py` — coleta o HTML de um ato por CELEX.
- `scripts/codebook_screen.py` — Stage A: aplica a triagem lexical e gera o
  CSV por ato.
- `scripts/combine.py` — junta os CSVs por ato em `combined_dataset.csv`.
- `data/*_raw.html` — HTML bruto de cada um dos 4 atos.
- `data/*_dataset.csv` — dataset de saída do Stage A por ato.
- `data/combined_dataset.csv` — os 4 juntos, com coluna `ato`.
- `data/rit_coded_sample.csv` — Stage B: codificação R-I-T manual das 4
  provisões-âncora.
- `CODEBOOK.md` — strings, ontologia (ator/mecanismo/instrumento) e
  contagens do Stage A.
- `RIT_CODING.md` — leitura das 4 codificações R-I-T, incluindo o caso
  condicional de Climate Benchmarks.
- `GOLD_STANDARD_VALIDATION.md` — precision/recall/F1 do Stage A.
- `METODOLOGIA.md` — porquê de cada escolha de desenho.
