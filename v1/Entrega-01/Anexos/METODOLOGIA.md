# Metodologia — por que a PoC foi feita desta maneira

Este documento explica as escolhas por trás do pipeline em `README.md`, não
os resultados em si. Serve tanto para justificar as decisões na conversa com
o David quanto como registro para retomar/estender o trabalho depois.

## 1. Por que a página HTML da EUR-Lex por CELEX, e não a API SPARQL/Cellar
A via "correta" para um projeto de escala (o projeto do David cobre toda a
legislação da UE sobre transição verde) é a API SPARQL da Cellar, que permite
consultar metadados e localizar atos em lote sem depender de busca por texto
na interface web. Para uma PoC de 4 atos escolhidos a dedo, isso seria
engenharia prematura: eu já sabia o CELEX de cada ato de antemão, então bastou
uma requisição HTTP por ato à página de texto integral
(`.../TXT/HTML/?uri=CELEX:<id>`). A migração para SPARQL é o primeiro passo
recomendado se o escopo crescer para dezenas/centenas de atos — ver seção 8.

## 2. Por que 4 atos escolhidos a dedo, um por mecanismo, em vez de um corpus amplo
Uma busca ampla por "transição verde" na EUR-Lex devolveria centenas de atos,
a maioria irrelevante para intermediação. Antes de construir uma busca
automática (que precisa de critérios de inclusão/exclusão já calibrados), a
pergunta que a PoC precisa responder é mais simples: **o método de triagem
funciona quando o mecanismo-alvo está de fato presente?** Por isso escolhi um
ato por mecanismo em que a literatura/a própria prática regulatória já indica
que aquele mecanismo é central:

- reportar/auditoria → CSRD (a diretiva existe para isso)
- certificação → EU Ecolabel (certificação de produto por "competent bodies")
- ranking/rating → Regulamento de Climate Benchmarks (administradores de
  índices de referência climáticos)
- auditoria (+ certificação em camada) → Verificação/Acreditação do EU ETS

Isso é uma amostra de conveniência com casos-alvo conhecidos, não uma amostra
representativa da legislação de transição verde como um todo — o objetivo é
validar o método, não ainda mapear o universo.

## 3. Por que os 4 mecanismos vêm da própria proposta do David, não de uma taxonomia externa
A primeira versão desta nota técnica (`03_nota_tecnica_abordagem.md`) usava a
tipologia de Abbott, Levi-Faur & Snidal (2017), mais granular. Troquei para os
quatro mecanismos primários da própria proposta (seção A4: reportar,
certificação, ranking/rating, auditoria) porque (a) é o vocabulário que ele
vai usar para avaliar o trabalho, (b) mapeia diretamente nos 4 pacotes de
trabalho empíricos da proposta (WP2–WP5), o que facilita comparar esta PoC com
o desenho que ele já tem, e (c) uma taxonomia mais simples é mais fácil de
operacionalizar como regras de busca nesta primeira rodada.

## 4. Por que triagem por palavra-chave/regex, e não NLP/ML, nesta fase
Um classificador de texto (mesmo um modelo de linguagem) exigiria dados
rotulados para validar precisão/recall, que não existem ainda. Regras de
palavra-chave são: (a) auditáveis por leitura direta da regra, (b) baratas de
ajustar depois de ver os falsos positivos/negativos de uma amostra, e (c)
adequadas ao objetivo desta etapa, que é *triagem* (alto recall, precisão
avaliada por amostragem manual), não classificação final. NLP/ML entra depois,
como camada de pré-seleção sobre um volume maior de atos — não substitui a
validação manual, só reduz o quanto precisa ser lido.

## 5. Por que rastrear artigo de origem e trecho de evidência, não só contar ocorrências
Cada linha do dataset carrega `carrier_article` (o "Article N" mais próximo
antes do parágrafo) e o trecho de texto que gerou o match — não apenas um
contador por mecanismo. Isso replica deliberadamente o padrão já usado no
inventário documental do CNJ: um código sem uma citação direta do texto não é
auditável, e um dataset de intermediários que não permite voltar ao texto
legal exato tem pouco valor para o tipo de teoria fundamentada que a proposta
do David propõe construir (RQ1–RQ3).

## 6. Por que validação manual por amostragem, e não das 714 linhas inteiras
Ler 714 linhas linha a linha não cabe no tempo de uma PoC e não é o que uma
triagem de alto recall pede — o objetivo da amostragem foi verificar, por
mecanismo e por ato, se os hits são *estruturalmente* corretos (o parágrafo
realmente fala de um intermediário daquele tipo) ou se a regra está gerando
ruído sistemático. Os quatro mecanismos-âncora (um por ato) vieram limpos na
amostra; o volume alto de "reportar"/"auditoria" na CSRD é esperado (o ato
inteiro é sobre isso) e fica marcado como não totalmente revisado.

## 7. O que a PoC prova e o que não prova
**Prova:** o pipeline coleta texto real da EUR-Lex, aplica um codebook
alinhado ao vocabulário da própria proposta do David, produz um dataset com
trilha de evidência e artigo de origem, e os quatro mecanismos aparecem com
sinal limpo em pelo menos um ato cada — inclusive revelando um padrão
substantivo (auditor accreditado por outro intermediário, no ETS) que não foi
buscado de propósito, só apareceu na leitura.

**Não prova:** que a triagem generaliza para toda a legislação de transição
verde sem ajuste; que a taxa de falsos positivos nas ~450 linhas não
amostradas da CSRD é baixa; que o método captura intermediários descritos sem
usar as palavras-gatilho escolhidas (ex.: um mecanismo de rating chamado só de
"scheme" ou "index" sem a palavra "rating"/"benchmark").

## 9. v2 — âncora/fraca/exclusão, para que a verificação humana seja exceção
A v1 (seções 1–8) tratava qualquer match de palavra-chave como um "candidato"
igual a outro, destinado à amostragem manual. Isso é adequado para validar o
método, mas não escala: se todo match pede checagem humana, o pipeline não
economiza tempo de leitura, só o organiza. A v2 divide as regras de cada
mecanismo em três camadas:

- **Âncora** — frases multi-palavra ou termos de papel/função específicos o
  suficiente para confirmar o mecanismo sozinhos (ex.: "statutory auditor",
  "national accreditation body", "benchmark administrator"). Match de âncora
  → `screening_confidence="high"`.
- **Fraca** — palavras genéricas isoladas que também ocorrem fora do sentido
  de intermediação (ex.: "report", "audit" bare, "rating" bare). Match só de
  regra fraca → `screening_confidence="low"`.
- **Exclusão** — padrões de contexto que descartam o match mesmo com âncora ou
  fraca presente, calibrados a partir de falsos positivos reais observados na
  amostra (ex.: "shall present a report to the European Parliament... on the
  impact of this Regulation" — clausula de revisão genérica, não uma
  instância do mecanismo "reportar"; "Court of Auditors" — instituição da UE,
  não um intermediário regulatório no sentido da teoria).

As âncoras e exclusões não foram escolhidas a priori: vieram de uma
amostragem aleatória de ~12 linhas por mecanismo no dataset combinado da v1
(714 linhas), lendo o texto de fato antes de decidir o que promover a âncora,
o que rebaixar a fraca, e o que excluir. Esse é o mesmo princípio de
auditabilidade da seção 5 aplicado às próprias regras: cada âncora/exclusão
tem um exemplo real que a motivou, não é uma lista genérica de sinônimos.

**Resultado:** dos 1.079 matches na rodada v2, 764 (71%) saem como `high` e
315 (29%) como `low` — a verificação humana virou a exceção pedida, não a
regra. O ponto mais fraco remanescente (ETS/"reportar", 5 `high` contra 119
`low`) não foi forçado a subir: o vocabulário de relatório do ETS ("emission
report", "verification report") está estruturalmente colado ao processo de
auditoria, e promover "report" bare a âncora ali geraria confirmações falsas
toda vez que o parágrafo só menciona o relatório como objeto da verificação,
não como uma instância nova do dever de reportar. Deixar como `low` é a
decisão certa, não uma lacuna a esconder — é exatamente o tipo de caso em que
a teoria dos mecanismos precisa de um humano para decidir se há um
mecanismo, dois, ou um mecanismo compondo outro (o mesmo padrão de
empilhamento observado na seção 7/README para certificação+auditoria).

**Ressalva importante, adicionada após revisão crítica de 05/09/2026:**
`screening_confidence=high` significa "sinal textual forte", não "presença
confirmada de um intermediário". Renomeei o campo (era `status`/
`verificar_humano` até esta revisão) porque o nome antigo (`confirmado`)
sugeria mais do que a triagem lexical de fato garante — ver seção 11.

## 10. Como isso escalaria para o projeto real (não feito aqui, só o caminho)
1. **Definir a população antes de consultar a Cellar.** SPARQL resolve
   *retrieval* (buscar atos que já sei que quero), não define o universo. A
   ordem correta é: definição da população ("o que conta como legislação da
   UE sobre transição verde?") → critérios de inclusão/exclusão → sampling
   frame → consulta SPARQL → screening (Stage A) → codificação (Stage B).
   Consultar a API antes de fechar os critérios produziria uma busca
   tecnicamente sofisticada sobre um universo conceitualmente indefinido.
2. ~~Rastrear também a numeração dos considerandos~~ — feito na v3: a coluna
   `provision_type` (`recital`/`article`) já distingue os dois, e a medição
   mostrou que a suposição inicial (metade dos hits no preâmbulo) estava
   errada — são 18% recital / 82% article no total (ver README.md).
3. Usar a amostra já validada aqui (Stage B, `RIT_CODING.md`, e o gold
   standard em `GOLD_STANDARD_VALIDATION.md`) como conjunto de referência
   para calibrar um segundo codificador (humano ou assistido por NLP) e medir
   concordância.
4. Expandir os atributos do codebook (formalidade, voluntarismo, nível,
   esfera, motivação, modo de operação, centralidade, grau de separação — já
   listados em `03_nota_tecnica_abordagem.md`) como colunas do Stage B, não
   como novos padrões de screening.
5. Implementar a regra de vizinhança de parágrafo identificada em
   `GOLD_STANDARD_VALIDATION.md` (os dois falsos negativos encontrados eram
   parágrafos adjacentes a um hit de alta confiança, descrevendo a mesma
   relação pelo ângulo do regulador ou do alvo, sem repetir o nome do
   intermediário).

## 11. Stage A não é Stage B — a correção mais importante desta revisão
Uma revisão crítica externa (05/09/2026) identificou o problema central desta
PoC antes desta seção existir: o pipeline responde bem "este parágrafo
contém um sinal textual associado a reporting, certification, ranking/rating
ou auditing?", mas a pergunta relevante da proposta do David é "existe aqui
um regulatory intermediary? Quem é? Entre quais rule-maker e rule-taker ele
opera? Sob qual desenho institucional?". Um match de `statutory auditor` é
um sinal textual de alta confiança, não uma confirmação de arquitetura R-I-T.

A correção não foi descartar o screening — é nomeá-lo corretamente como
**Stage A** (triagem/localização de candidatos) e tratar a codificação R-I-T
como **Stage B**, um passo qualitativo distinto que consome a saída do Stage
A em vez de ser confundido com ela. Mudanças concretas decorrentes disso:

- `status` (`confirmado`/`candidato`) virou `screening_confidence`
  (`high`/`low`) — nome que não promete mais do que a triagem lexical entrega.
- Nova coluna `intermediary_validated` (0/1), 0 em toda a base por padrão;
  só recebe 1 nas linhas efetivamente cobertas pela codificação manual do
  Stage B (`rit_coded_sample.csv`).
- `CODEBOOK.md` ganhou uma coluna de **ontologia** por padrão (ator/
  mecanismo/instrumento) — só padrões "ator" apontam diretamente para um
  candidato a intermediary; a contagem de hits por mecanismo (ex.: "149 hits
  de certificação no ETS") mede densidade textual, não número de
  intermediários distintos, e não deve ser lida como tal.
- O caso de Climate Benchmarks foi reavaliado com ceticismo deliberado em vez
  de aceito por analogia lexical — ver `RIT_CODING.md`, seção 3. Nem todo
  objeto vagamente numérico é um "rating" no sentido da teoria.
