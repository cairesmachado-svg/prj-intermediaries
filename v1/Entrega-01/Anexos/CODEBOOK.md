# Codebook de strings — Stage A (screening lexical de mecanismos)

Referência canônica das regras aplicadas em `scripts/codebook_screen.py`
(v3). Contagens e exemplos vêm da rodada real sobre os 4 atos
(`data/combined_dataset.csv`, 1.079 linhas).

**Este é o codebook do Stage A, não da codificação final de
intermediários.** Ele responde "este parágrafo tem um sinal textual
associado a um mecanismo?" — uma pergunta de triagem, não "existe aqui um
regulatory intermediary, entre quem e quem?". Essa segunda pergunta é
respondida em `RIT_CODING.md` (Stage B), a partir dos parágrafos que este
Stage A localiza. Ver também `GOLD_STANDARD_VALIDATION.md` para a medição de
precision/recall desta triagem.

## Como ler este documento
Cada mecanismo tem três listas de padrões (ver `METODOLOGIA.md`, seção 9):

- **Âncora** — confirma o mecanismo sozinho. `screening_confidence=high`.
- **Fraca** — sinal genérico, insuficiente sozinho. `screening_confidence=low`.
- **Exclusão** — descarta o match mesmo com âncora/fraca presente.

Cada padrão também recebe uma **ontologia**: se o termo nomeia um **ator**
(um papel institucional — "quem"), um **mecanismo** (uma ação/processo —
"o quê"), ou um **instrumento** (um documento/artefato produzido pelo
processo — "o registro"). Esta coluna é a resposta direta ao ponto mais
importante da revisão crítica deste trabalho: o codebook original misturava
essas três ontologias sob um único rótulo. Só padrões marcados **ator**
apontam diretamente para um candidato a *intermediary* no sentido da
proposta do David; mecanismo e instrumento são contexto de apoio, não a
entidade a codificar.

Regra de decisão (ordem de avaliação, por parágrafo x mecanismo):
```
se qualquer padrao de exclusao casa com o texto:
    descartar (sem linha no dataset)
senao se qualquer padrao de ancora casa com o texto:
    screening_confidence = high
senao se qualquer padrao fraco casa com o texto:
    screening_confidence = low
senao:
    sem match (sem linha no dataset)
```
Todos os padrões são regex, case-insensitive, aplicados ao texto normalizado
do parágrafo.

---

## 1. Reportar (report duty)

**Definição (proposta do David, seção A4):** mecanismo pelo qual um ator é
obrigado a divulgar informação sobre si mesmo ou sobre terceiros a um público
regulador ou geral. Ator tipicamente líder: **Estado**.

**Nota de ontologia:** nenhum padrão-âncora deste mecanismo nomeia um ator —
todos nomeiam o mecanismo (o dever) ou o instrumento (o documento). Isso é
consistente com o achado do Stage B (`RIT_CODING.md`): "reportar" sozinho
tende a não ter um intermediário distinto — o intermediário aparece quando
"reportar" se combina com "auditoria" (alguém que verifica o relatório).

### Âncora (`screening_confidence=high`)

| Padrão (regex) | Ontologia | n high | Exemplo de evidência real |
|---|---|---|---|
| `sustainability reporting` | mecanismo | 255 | "Many stakeholders consider the term 'non-financial' to be inaccurate [...]" (CSRD) |
| `management report` | instrumento | 27 | "1. Large undertakings [...] shall include in the management report [...]" (CSRD, Art. 19a) |
| `sustainability report\b` | instrumento | 13 | "Member States should be able to inform the Commission [...] on the sustainability report [...]" (CSRD) |
| `non-financial (report\|statement)` | instrumento | 7 | "[...] amended Directive 2013/34/EU as regards disclosure of non-financial information [...]" (CSRD) |
| `reporting (obligation\|requirement)s?` | mecanismo | 7 | "Different reporting requirements result in [...]" (CSRD) |

### Fraca (`screening_confidence=low`, requer verificação humana)

| Padrão (regex) | Ontologia | n low | Exemplo de evidência real |
|---|---|---|---|
| `\breport\b` | instrumento | 155 | "[...] amended Directive 2013/34/EU as regards disclosure of non-financial information by certain [...]" (CSRD) |
| `\bshall report\b` | mecanismo | 5 | "Large undertakings [...] which are public-interest entities [...] shall [...] report [...]" (CSRD, Art. 1) |
| `\bshall disclose\b` | mecanismo | 1 | "Where no EU Climate Transition Benchmark [...] is available [...] shall disclose [...]" (Climate Benchmarks, Art. 19d) |
| `\bshall publish\b` | mecanismo | 1 | "The body recognised under Article 14 [...] shall publish and communicate the outcome [...]" (ETS Verificação, Art. 65) |

### Exclusão

| Padrão (regex) | O que descarta e por quê |
|---|---|
| `shall present a report to the European Parliament` | Cláusula de revisão institucional genérica, não é o dever de reportar de um regulado a um regulador. |
| `report on the application of this (regulation\|directive)` | Mesmo motivo. |
| `review (clause\|report) (on\|of) this (regulation\|directive)` | Idem. |

**Nota de calibração:** `\breport\b` isolado (155 hits, o mais frequente do
codebook inteiro) permanece `low` de propósito — no ETS a mesma palavra
aparece predominantemente como parte de "emission report"/"verification
report" (o documento sendo auditado, não uma nova instância do dever de
reportar). Ver METODOLOGIA.md, seção 9.

---

## 2. Certificação (certification)

**Definição:** mecanismo pelo qual um intermediário atesta formalmente que
um ator, produto ou processo cumpre um padrão. Ator tipicamente líder: **ONG**
(ou organismo técnico independente).

**Nota de ontologia:** ao contrário de "reportar", todos os padrões-âncora
aqui nomeiam um **ator** — este é o mecanismo mais diretamente alinhado à
tarefa de "codificar intermediários" tal como pedida pelo David.

### Âncora (`screening_confidence=high`)

| Padrão (regex) | Ontologia | n high | Exemplo de evidência real |
|---|---|---|---|
| `national accreditation bod(y\|ies)` | ator | 105 | "When implementing Article 15 of Directive 2003/87/EC [...] national accreditation bodies [...]" (ETS Verificação) |
| `(competent\|accredited) bod(y\|ies)` | ator | 73 | "It is appropriate to provide for the conditions under which the EU Ecolabel may be used [...] require competent bodies [...]" (Ecolabel) |
| `independent assurance services provider` | ator | 26 | "Considering the key role of statutory auditors when providing assurance of sustainability reporting [...]" (CSRD) |
| `conformity assessment (body\|bodies)` | ator | 4 | "'independent assurance services provider' means a conformity assessment body accredited [...]" (CSRD, Art. 1) |

### Fraca (`screening_confidence=low`, requer verificação humana)

| Padrão (regex) | Ontologia | n low | Exemplo de evidência real |
|---|---|---|---|
| `\baccreditation\b` | mecanismo | 32 | "An overall framework of rules for the accreditation of verifiers is necessary [...]" (ETS Verificação) |
| `\baccredited\b` | mecanismo (status) | 8 | "Pursuant to Article 6 of Directive 2007/36/EC [...] shareholders [...] accredited [...]" (CSRD) |
| `\bcertificat\w*` | mecanismo/instrumento | 7 | "the ability to draw up certificates, records and reports demonstrating that assessments have been carried out." (Ecolabel, Art. 20) |

### Exclusão
Nenhuma calibrada nesta rodada — sem falsos positivos sistemáticos
observados na amostra (ver GOLD_STANDARD_VALIDATION.md, precision=100%).

---

## 3. Ranking/rating

**Definição:** mecanismo pelo qual um intermediário ordena, pontua ou
classifica atores/produtos de forma comparativa. Ator tipicamente líder:
**empresa**.

**Alerta de validade de construto:** o único ato-âncora deste mecanismo
(Climate Benchmarks) foi avaliado em `RIT_CODING.md` como **condicional**,
não confirmado — um benchmark financeiro climático não é automaticamente um
"rating"/"ranking" regulatório no sentido da proposta do David. Ver
`RIT_CODING.md`, seção 3, antes de usar este ato como exemplo canônico do
mecanismo com o David.

### Âncora (`screening_confidence=high`)

| Padrão (regex) | Ontologia | n high | Exemplo de evidência real |
|---|---|---|---|
| `EU (Climate Transition\|Paris-aligned) Benchmark` | instrumento | 26 | "Regulation (EU) 2016/1011 [...] establishes uniform rules for benchmarks in the Union [...]" (Climate Benchmarks) |
| `benchmark administrator` | ator | 13 | "Regulation (EU) 2020/852 [...] creates a classification system [...]" (CSRD) |
| `benchmark methodology` | instrumento | 1 | "all criteria and methods, including selection and weighting factors [...]" (Climate Benchmarks, Art. 2) |

### Fraca (`screening_confidence=low`, requer verificação humana)

| Padrão (regex) | Ontologia | n low | Exemplo de evidência real |
|---|---|---|---|
| `\bbenchmark\w*` | instrumento | 25 | "A wide variety of indices are currently grouped together as low-carbon indices [...]" (Climate Benchmarks) |

`\brating\b`, `\branking\b` e `\bscore\b` (ator: nenhum desses três nomeia
ator diretamente — nomeariam o produto/mecanismo; o ator correspondente seria
"rating agency", já coberto como padrão-âncora) estão definidos mas **não
dispararam nenhum match** nos 4 atos — mantidos para atos futuros (ex.:
agências de rating de crédito).

### Exclusão

| Padrão (regex) | O que descarta e por quê |
|---|---|
| `shall present a report to the European Parliament` | Cláusula de revisão institucional genérica. |
| `review (clause\|report) (on\|of) this (regulation\|directive)` | Idem. |

---

## 4. Auditoria (audit)

**Definição:** mecanismo pelo qual um intermediário verifica de forma
independente a exatidão de uma alegação ou relatório. Ator tipicamente
líder: **profissão** (auditores, verificadores).

### Âncora (`screening_confidence=high`)

| Padrão (regex) | Ontologia | n high | Exemplo de evidência real |
|---|---|---|---|
| `statutory auditor` | ator | 74 | "The conclusion of a reasonable assurance engagement is usually provided [...]" (CSRD) |
| `verification (team\|report\|body)` | ator/instrumento (team, body = ator; report = instrumento) | 51 | "To avoid entanglement between the role of the competent authority and the verifier [...]" (ETS Verificação) |
| `(EU ETS )?(lead )?auditor` | ator | 36 | "The assurance profession distinguishes between limited assurance engagements [...]" (CSRD) |
| `assurance (engagement\|opinion\|provider\|services)` | ator (provider) / mecanismo (demais) | 31 | "The subsidiary undertaking [...] with the assurance opinion [...]" (CSRD) |
| `audit firm` | ator | 10 | "'audit firm' means a legal person [...] approved in accordance with this Directive [...]" (CSRD, Art. 1) |
| `quality assurance review` | mecanismo | 3 | "the persons who carry out quality assurance reviews shall have appropriate professional education [...]" (CSRD, Art. 28a) |
| `accredited verifier` | ator | 2 | "During the accreditation process and the monitoring of accredited verifiers [...]" (ETS Verificação, Art. 45) |

### Fraca (`screening_confidence=low`, requer verificação humana)

| Padrão (regex) | Ontologia | n low | Exemplo de evidência real |
|---|---|---|---|
| `\baudit\w*` | mecanismo | 44 | "In its resolution of 29 May 2018 on sustainable finance [...]" (CSRD) |
| `\bassurance\b` | mecanismo | 37 | "On 17 June 2019, the Commission adopted its Guidelines on reporting climate-related information [...]" (CSRD) |

### Exclusão

| Padrão (regex) | O que descarta e por quê |
|---|---|
| `Court of Auditors` | Instituição da UE (fiscalização orçamentária), não um intermediário regulatório no sentido da teoria de David. |

---

## Resumo quantitativo (4 atos, 1.079 linhas)

| Mecanismo | Padrões âncora (ator) | Padrões âncora (outro) | Padrões fracos | high | low |
|---|---|---|---|---|---|
| reportar | 0 | 5 | 4 | 309 | 162 |
| certificação | 4 | 0 | 3 | 208 | 47 |
| ranking/rating | 1 | 2 | 4 (1 ativo) | 40 | 25 |
| auditoria | 5 | 2 | 2 | 207 | 81 |

A coluna "âncora (ator)" é a leitura mais honesta de quão perto cada
mecanismo já está de "codificar intermediários": certificação e auditoria
têm a maioria de suas âncoras nomeando atores; reportar não tem nenhuma —
ver a discussão completa em `RIT_CODING.md`.

## Como estender este codebook
1. Rodar `codebook_screen.py` sobre um ato novo.
2. Amostrar aleatoriamente os hits `low` desse ato (nunca menos que ~10 por
   mecanismo).
3. Só promover um padrão fraco a âncora se a amostra mostrar que ele é
   consistentemente inequívoco.
4. Só adicionar exclusão a partir de um falso positivo real observado.
5. Classificar a ontologia do novo padrão (ator/mecanismo/instrumento) antes
   de adicioná-lo — um padrão "instrumento" não deveria, sozinho, virar prova
   de que um intermediário foi encontrado (ver Stage B, `RIT_CODING.md`).
6. Atualizar este arquivo no mesmo commit/sessão que `codebook_screen.py`.
