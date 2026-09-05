# Stage B — codificação R-I-T (Regulator–Intermediary–Target)

O screening lexical (`codebook_screen.py`, ver README.md e CODEBOOK.md)
responde: "este parágrafo contém um sinal textual associado a um mecanismo de
intermediação?" — é **Stage A**. Essa pergunta não é a mesma que a proposta
do David faz: "existe aqui um regulatory intermediary, entre quem e quem,
sob que desenho institucional?" Este documento é **Stage B**: a partir dos
parágrafos que o Stage A localizou com maior densidade de sinal, li o artigo
completo e codifiquei a relação R-I-T explicitamente. Dataset completo em
`data/rit_coded_sample.csv` (4 linhas — uma por ato/mecanismo-âncora); a
tabela abaixo é a mesma informação em formato de leitura.

## 1. CSRD — auditoria (Article 27a, dentro de emenda à Directive 2006/43/EC)

| Campo | Valor |
|---|---|
| **R** (regulador) | Autoridade competente do Estado-Membro |
| **I** (intermediário) | Group auditor — que por sua vez supervisiona uma cadeia de outros intermediários: independent assurance services provider(s), third-country auditor(s), statutory auditor(s), audit firm(s) |
| **T** (alvo) | Undertaking / grupo de empresas (parent e subsidiárias) |
| Natureza jurídica | Obrigatória |
| Setor | Privado (profissão regulada), com órgãos de supervisão pública para entidades de terceiros países |
| Independência exigida | Sim — regras de independência da Directive 2006/43/EC aplicam-se ao longo de todo o dispositivo |
| Acreditação/aprovação exigida | Sim — statutory auditors/audit firms aprovados; auditores/IASPs de terceiros países sob regime equivalente |
| **Validade de construto** | Confirmada |

**Achado:** este artigo mostra um intermediário supervisionando outros
intermediários (o group auditor avalia e revisa o trabalho de assurance
providers subordinados) — uma cadeia de intermediação em camadas, não uma
relação R-I-T simples de três pontos.

## 2. Ecolabel — certificação (Article 9)

| Campo | Valor |
|---|---|
| **R** | Comissão Europeia (define critérios e mantém registro público, Art. 8) |
| **I** | Competent body (designado por cada Estado-Membro, Art. 4) |
| **T** | Operador (requerente/produtor que coloca o produto no mercado) |
| Natureza jurídica | Voluntária (o operador solicita; o rótulo não é condição de acesso ao mercado) |
| Setor | Híbrido — órgão público designado pelo Estado-Membro, operando sob critérios definidos a nível da UE |
| Independência exigida | Não explicitada para o competent body em si |
| Acreditação/aprovação exigida | Parcial — o competent body se apoia em testes acreditados ISO 17025 e verificações acreditadas EN 45011 quando disponíveis (Art. 9(7)) |
| **Validade de construto** | Confirmada |

## 3. Climate Benchmarks — ranking/rating (Article 19b) — caso condicional

| Campo | Valor |
|---|---|
| **R** | Não nomeado neste artigo — estabelecido em outro lugar do Regulamento (UE) 2016/1011 (ESMA / autoridades nacionais competentes supervisionam administradores de referenciais em geral) |
| **I** | Administrador do referencial (benchmark administrator) |
| **T** | Duplo e indireto: (a) empresas cujos ativos são selecionados/ponderados/excluídos conforme sua trajetória de descarbonização; (b) gestores de ativos/investidores que usam o rótulo do referencial para alegações de conformidade |
| Natureza jurídica | Obrigatória para o uso do rótulo "EU Climate Transition Benchmark" |
| Setor | Privado |
| Independência exigida | Não tratada neste artigo |
| Acreditação/aprovação exigida | Não tratada neste artigo (autorização do administrador é exigência separada do Regulamento 2016/1011, não repetida aqui) |
| **Validade de construto** | **Condicional** |

**Por que condicional, não confirmada:** um referencial financeiro climático
não é automaticamente um "rating" ou "ranking" no sentido regulatório da
proposta do David — pode ser apenas um índice de referência para comparação
de desempenho financeiro, sem constituir uma avaliação regulatória dos
próprios rule-takers. O Article 19b mostra o administrador selecionando e
ponderando ativos com base em critérios de descarbonização — isso *é* um ato
de classificação/pontuação de empresas segundo um padrão pré-definido (a
definição de "rating" na proposta do David), mas o regulador (R) que
disciplina essa atividade não aparece neste artigo específico, e o T
"principal" (a empresa cujos ativos são pontuados) é diferente do usuário
final que a teoria de intermediação regulatória tipicamente tem em mente
(investidores que dependem do rótulo). Mantenho o caso, mas como validado
condicionalmente — não forcei um R-I-T limpo onde a evidência textual não o
sustenta sozinha. Se este caso for usado como exemplo canônico do mecanismo
"ranking/rating" na conversa com o David, vale perguntar a ele diretamente se
aceita esta configuração ou se prefere um caso mais direto (ex.: agências de
rating de crédito, para as quais o codebook já tem padrões-âncora não usados
nesta rodada por não aparecerem nos 4 atos escolhidos).

## 4. ETS Verificação — auditoria (+ certificação) (Article 27)

| Campo | Valor |
|---|---|
| **R** | Autoridade competente (recebe o relatório de verificação, Art. 27(2)) |
| **I** | Verificador — com diferenciação interna de papéis: EU ETS lead auditor, EU ETS auditor, independent reviewer, technical expert |
| **T** | Operador / operador de aeronave |
| Natureza jurídica | Obrigatória |
| Setor | Privado (organismos de verificação acreditados), sob supervisão pública de acreditação |
| Independência exigida | Sim — revisão independente da verificação (Art. 25, referenciada no Art. 27(3)(t)) |
| Acreditação/aprovação exigida | Sim — o verificador precisa ser acreditado. Este é o próprio caso de empilhamento de mecanismos já documentado em METODOLOGIA.md: um auditor que é, ele próprio, credenciado por outro intermediário (o organismo nacional de acreditação) |
| **Validade de construto** | Confirmada |

**Achado mais rico da amostra:** o próprio artigo nomeia as três posições da
tríade na mesma frase — "(j) the responsibilities of the operator or
aircraft operator, the competent authority and the verifier" — um raro caso
em que R, I e T aparecem explicitamente lado a lado no texto legal, sem
precisar de inferência.

## O que este Stage B não é
Quatro artigos codificados não são um dataset de intermediários da
legislação de transição verde da UE — são uma prova de que o passo de
codificação R-I-T é executável a partir do que o Stage A localiza, com
critérios explícitos (natureza jurídica, setor, independência, acreditação)
já alinhados aos atributos que a proposta do David pede. Escalar isso para o
corpus inteiro é o próximo passo, não algo já feito aqui.
