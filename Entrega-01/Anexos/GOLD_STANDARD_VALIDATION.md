# Validação gold-standard (precision / recall / F1)

A calibração original do codebook (README.md, METODOLOGIA.md seção 9) media
apenas se os *hits* do screening eram bons — permite avaliar falsos
positivos, não falsos negativos. Este documento fecha essa lacuna: para um
artigo por ato, fiz uma leitura manual completa, sem regex, de todos os
parágrafos, marcando se cada um contém substantivamente uma relação de
intermediação (não apenas se repete a palavra-âncora) — esse é o gold
standard. Depois comparei contra o que `codebook_screen.py` de fato
encontrou nesses mesmos parágrafos.

## Escopo
Um artigo por ato (mesmo recorte usado na codificação R-I-T de
`rit_coded_sample.csv`), escolhido por ser o mais rico em conteúdo de
intermediação dentro do ato:

| Ato | Artigo | Unidades julgadas (parágrafos) |
|---|---|---|
| CSRD | Article 27a | 13 |
| Ecolabel | Article 9 | 18 (13 positivas + 5 negativas) |
| Climate Benchmarks | Article 19b | 6 (2 positivas + 4 negativas) |
| ETS Verificação | Article 27 | 5 (nível de parágrafo numerado, não por item de lista — ver nota) |

**Nota sobre granularidade no ETS:** o Article 27 tem uma lista de 21 itens
(a)–(u) descrevendo o *conteúdo* do relatório de verificação. Tratei cada
parágrafo numerado (1–5) como uma unidade, não cada item de lista — uma
enumeração de conteúdo obrigatório é uma proposição só, não 21. Isso é uma
decisão de design explícita, não uma omissão.

**Isto não é uma amostra aleatória do corpus.** É o artigo mais promissor de
cada ato — os mesmos que já tínhamos escolhido para ancorar cada mecanismo.
Os números abaixo são um teto otimista, não uma estimativa de
precision/recall para os outros ~1.000 parágrafos do corpus.

## Resultado agregado

| Métrica | Valor |
|---|---|
| Verdadeiros positivos (TP) | 33 |
| Falsos negativos (FN) | 2 |
| Falsos positivos (FP) | 0 |
| **Precision** | **100%** (33/33) |
| **Recall** | **94,3%** (33/35) |
| **F1** | **97,1%** |

## Os dois falsos negativos (Ecolabel, Article 9)
Nenhum falso positivo apareceu na amostra — todo parágrafo que o screening
marcou realmente tratava de um intermediário. Os dois erros são de recall,
e os dois têm a mesma causa: o parágrafo descreve a relação de intermediação
**sem repetir o substantivo "competent body"**, usando em vez disso o outro
lado da relação:

1. *"Applications shall include all relevant documentation, as specified in
   the relevant Commission measure establishing EU Ecolabel criteria [...]"*
   — fala do papel do regulador (Comissão) que define os critérios que o
   competent body depois aplica; não nomeia o intermediário.
2. *"The operator may place the EU Ecolabel on the product only after
   conclusion of the contract [...]"* — descreve o direito do *T* (operador)
   resultante do contrato com o intermediário; não nomeia o intermediário.

**Implicação para o desenho do codebook:** uma triagem lexical ancorada no
nome do papel do intermediário confirma bem os parágrafos em que ele é
sujeito da frase, mas tende a perder parágrafos vizinhos que descrevem a
mesma relação pelo ângulo do regulador ou do alvo. Isso não se resolve
adicionando mais sinônimos de "competent body" — precisa de uma regra de
*vizinhança de parágrafo* (se um parágrafo tem screening_confidence=high para
um mecanismo, os parágrafos imediatamente adjacentes dentro do mesmo artigo
ganham prioridade de revisão humana, mesmo sem match lexical próprio). Não
implementado nesta rodada; registrado aqui como o próximo ajuste de
desenho mais bem fundamentado empiricamente.

## O que este exercício não testa
- Não testa se o *mecanismo* atribuído está certo (ex.: um parágrafo marcado
  "reportar" que deveria ser só "auditoria") — testa apenas presença/ausência
  de conteúdo de intermediação no parágrafo.
- Não testa recall fora dos 4 artigos escolhidos — um ato inteiro nunca lido
  manualmente pode ter mecanismos descritos com vocabulário totalmente fora
  do codebook atual (ex.: um mecanismo de rating chamado só de "index" ou
  "scheme").
- Não substitui dupla codificação entre codificadores — é uma checagem
  solo contra o próprio código, não uma medida de concordância entre
  pessoas.
