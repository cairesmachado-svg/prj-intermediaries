---
title: "Codificação de Intermediários Regulatórios na Legislação da UE sobre Transição Verde"
subtitle: "Compreensão conceitual, operacionalização e proposta de codificação — relatório preparado para discussão com o Prof. David Levi-Faur"
author: "Igor Caires Machado — Postdoctoral Researcher, ENAP · ORCID 0009-0008-9547-5223"
date: "5 de setembro de 2026"
lang: pt-BR
---

## Objetivo deste documento

Este relatório apresenta, de forma consolidada, o trabalho realizado em resposta
à chamada do Prof. David Levi-Faur por um assistente/parceiro de pesquisa para
codificar intermediários na legislação da UE sobre transição verde
("Governance by and of Intermediaries"). Cobre quatro frentes: (1) a
compreensão do tema e do problema teórico proposto; (2) a compreensão
conceitual dos mecanismos de intermediação; (3) como isso foi operacionalizado
numa prova de conceito (PoC) empírica; e (4) a proposta de codificação
resultante, fundamentada não apenas na teoria do próprio David, mas também na
minha experiência prévia de construção de codebooks no programa de pesquisa
ARENAS, onde codifico elementos espaciais e mecanismos sociomateriais de
implementação de políticas públicas há vários ciclos de pesquisa.

## Compreensão do tema e do problema teórico

A proposta de pesquisa do Prof. Levi-Faur ("Can Intermediaries Save Liberal
Governance? Toward Effective and Legitimate Regulatory Intermediation") parte
da premissa de que a agenda de reforma democrática deve se voltar para os
**intermediários regulatórios** — os "corretores de regras" entre reguladores
(rule-makers) e regulados (rule-takers). A literatura de regulação ainda trata
essa relação como bipartite, deixando de teorizar quem certifica, audita,
classifica, rotula e reporta. Quando os intermediários funcionam bem, aumentam
a capacidade de resolver problemas e a disposição a cumprir regras; quando
falham, corroem a legitimidade da governança.

A proposta identifica quatro lacunas na literatura (de atenção, de
conceitualização, de proliferação e de subteorização) e formula três
objetivos: (1) mapear e medir intermediários e mecanismos; (2) explicar sua
difusão entre temas, países e no tempo; (3) ligar o desenho da intermediação à
teoria democrática (regimes mono/policêntricos). O projeto se organiza em oito
pacotes de trabalho, quatro deles (WP2–WP5) dedicados cada um a um mecanismo
primário de intermediação. A chamada específica a que respondo — codificar
intermediários na legislação da UE sobre transição verde — é uma aplicação
empírica direta desse desenho teórico a um domínio concreto.

## Compreensão conceitual dos mecanismos

A proposta define a intermediação como uma tríade **atores + mecanismos +
estratégias**, com quatro mecanismos primários, cada um associado a um modo de
governança predominante:

- **Dever de reportar** (report duty) — tipicamente liderado pelo Estado.
- **Certificação** (certification) — tipicamente liderado por ONGs.
- **Ranking/rating** — tipicamente liderado por empresas.
- **Auditoria** (audit) — tipicamente liderado pela profissão.

A proposta também especifica atributos dos intermediários (formalidade,
voluntarismo, nível, esfera, motivação, modo de operação, centralidade, grau
de separação) e quatro tipos de falha (subcomprometimento,
sobrecomprometimento, captura, incompetência). Adotei esses quatro mecanismos
— e não uma taxonomia externa mais granular (como a de Abbott, Levi-Faur &
Snidal, 2017, que também considerei inicialmente) — como esqueleto do
codebook, por três razões: (a) é o vocabulário que o próprio projeto usa para
organizar seus pacotes de trabalho empíricos; (b) mapeia diretamente para
WP2–WP5, facilitando comparação futura; (c) uma taxonomia mais simples é mais
fácil de operacionalizar e validar numa primeira rodada.

## Operacionalização empírica

Para testar se o método funciona antes de propor uma escala maior, construí
uma prova de conceito com dados reais (não simulados) de quatro atos
legislativos da UE, cada um escolhido como âncora de um dos quatro mecanismos:

| Ato | Mecanismo-alvo | Por que este ato |
|---|---|---|
| Corporate Sustainability Reporting Directive (CELEX 32022L2464) | reportar + auditoria | Obriga reporte de sustentabilidade e sua garantia (assurance) por auditor/provedor independente |
| Rótulo Ecológico da UE (CELEX 32010R0066) | certificação | "Competent Bodies" certificam produtos com base em critérios ambientais |
| Regulamento de Referenciais Climáticos (CELEX 32019R2089) | ranking/rating | Requisitos de metodologia para administradores de índices de referência climáticos |
| Verificação e Acreditação no EU ETS (CELEX 32018R2067) | auditoria (+ certificação) | Regula verificadores de emissões de gases de efeito estufa e sua acreditação |

O texto integral de cada ato foi coletado programaticamente da EUR-Lex por
número CELEX (não por busca textual livre no site, que devolveria ruído
incontrolável) e processado parágrafo a parágrafo, com rastreamento do artigo
de origem de cada trecho — a mesma exigência de rastreabilidade que utilizo em
qualquer corpus documental que construo (ver seção 6). O resultado desta
rodada: 1.079 parágrafos com sinal de algum mecanismo, distribuídos de forma
coerente com o motivo da escolha de cada ato — inclusive um achado não
buscado deliberadamente: no ato do EU ETS, o mecanismo dominante nos hits foi
"certificação" (via acreditação), não "auditoria", porque o regime cria um
auditor que é, ele próprio, credenciado por um organismo de acreditação — os
dois mecanismos aparecem empilhados no mesmo ato.

## Proposta de codificação

O codebook resultante classifica cada parágrafo, por mecanismo, em três
camadas de regras:

- **Âncora** — termos ou frases de papel/função específicos o suficiente para
  confirmar o mecanismo sozinhos (ex.: "statutory auditor", "national
  accreditation body", "benchmark administrator"). Gera `status = confirmado`.
- **Fraca** — termos genéricos isolados que também ocorrem fora do sentido de
  intermediação (ex.: "report", "audit" solto, "rating" solto). Gera
  `status = candidato`, com sinalização explícita de necessidade de
  verificação humana.
- **Exclusão** — padrões de contexto que descartam o match mesmo com âncora ou
  termo fraco presente (ex.: cláusulas genéricas de revisão ao Parlamento
  Europeu; "Court of Auditors", instituição da UE e não um intermediário
  regulatório no sentido da teoria).

Cada linha do dataset carrega, além do mecanismo e do status: o ato e o
artigo de origem, o padrão que disparou o código, e o trecho de texto exato
que gerou o match — nunca um código sem a evidência que o sustenta. Na rodada
atual (4 atos, 1.079 linhas), 71% dos códigos são `confirmado` (sem
necessidade de revisão humana) e 29% ficam como `candidato`. A verificação
humana foi deliberadamente desenhada como último recurso, não como padrão —
princípio detalhado na seção seguinte.

## Fundamentação metodológica: experiência prévia no modelo ARENAS

As escolhas de desenho acima não partiram do zero. Elas replicam, adaptados a
um novo domínio teórico e empírico, princípios que já uso e testo no programa
de pesquisa ARENAS, onde codifico elementos espaciais e mecanismos
sociomateriais de implementação de políticas públicas.

**6.1 — Classificação de saliência em camadas.** No programa ARENAS, uso uma
classificação de saliência N1/N2/N3 para determinar o quanto um documento ou
observação trata a materialidade (espaço, objetos, infraestrutura) como
constitutiva do mecanismo, como variável secundária, ou como contexto passivo
sem papel analítico — com uma taxa de tratamento ativo (N1/(N1+N2+N3)) como
indicador-síntese. A divisão `confirmado`/`candidato` proposta aqui para os
intermediários é uma adaptação direta desse princípio: em vez de tratar todo
match de palavra-chave como equivalente, distingo sinais que, por si só,
constituem evidência forte (equivalente a N1) de sinais que exigem contexto
adicional para interpretar (equivalente a N2/N3, aqui operacionalizado como
alerta de revisão humana).

**6.2 — Codificação ancorada em evidência verbatim.** O protocolo de
observação sociomaterial que uso em campo no ARENAS exige que cada código
(mecanismo A–E, ator, fricção, recurso) seja registrado junto com um campo de
evidência explícito (nota de campo, foto, fala transcrita, documento ou
medida ambiental) — nunca um rótulo sem o dado bruto que o sustenta. É o
mesmo princípio que apliquei ao dataset de intermediários: cada linha carrega
o trecho de texto exato que motivou o código, permitindo auditoria e
recodificação por qualquer pessoa da equipe, sem depender da minha leitura
original.

**6.3 — Ancoragem teórica explícita dos mecanismos, não taxonomia genérica.**
A matriz de mecanismos ARENAS (A. Tradução e instrumentação espacial; B.
Mediação do trabalho; C. Mediação da experiência; D. Legibilidade
institucional; E. Aprendizagem e redesenho) define, para cada mecanismo, sua
"ancoragem teórica principal" e sua "evidência esperada" — de modo que a
codificação empírica sempre remete de volta à teoria que a justifica, não a
uma lista de sinônimos construída ad hoc. Apliquei a mesma lógica aqui:
escolhi ancorar o codebook nos quatro mecanismos que já estruturam a própria
proposta do David (não numa tipologia externa mais granular), justamente para
que cada código remeta diretamente à teoria que está sendo testada.

**6.4 — Validação incremental, não codificação exaustiva de partida.** Os
codebooks do programa ARENAS são tratados explicitamente como protocolos
vivos: definem padrão de confiabilidade esperado (concordância entre
codificadores, kappa mínimo antes de prosseguir para codificação em escala),
mas a aplicação plena é faseada — primeiro se valida o método numa amostra
calibrada, só depois se codifica o corpus inteiro. Segui o mesmo princípio
aqui: as regras de âncora, termo fraco e exclusão desta PoC foram calibradas a
partir da leitura manual de uma amostra real de hits (não definidas a priori),
e a validação desta rodada foi por amostragem dirigida — suficiente para
propor o método, não para declará-lo pronto para aplicação em escala a toda a
legislação de transição verde.

## Limitações reconhecidas

- A atribuição ao artigo de origem fica vazia para trechos do preâmbulo dos
  atos (antes do primeiro "Article"), onde recai boa parte dos códigos —
  corrigível rastreando também a numeração dos considerandos.
- Os 29% de códigos `candidato` ainda não foram revisados um a um; são a fila
  de verificação humana, não um resultado final.
- A coleta usa a página de texto integral da EUR-Lex por número CELEX
  conhecido, adequada para um punhado de atos escolhidos a dedo — não para
  identificar automaticamente centenas de atos relevantes, o que exigiria
  migrar para a API SPARQL/Cellar.
- Um mecanismo pode aparecer empilhado sobre outro no mesmo trecho de texto
  (como no caso do EU ETS) — o codebook atual permite múltiplos mecanismos por
  parágrafo, mas não modela formalmente a relação de dependência entre eles.

## Próximos passos propostos

1. Migrar a seleção de atos de "escolha a dedo" para consulta programática à
   API SPARQL/Cellar, por critérios temáticos e temporais.
2. Rastrear a numeração dos considerandos, não só dos artigos, para fechar a
   lacuna de atribuição de origem no preâmbulo.
3. Usar a amostra já validada como referência para calibrar um segundo
   codificador (humano ou assistido por NLP) e medir concordância — nos
   mesmos moldes do padrão de kappa que já utilizo no ARENAS.
4. Expandir o codebook com os atributos dos intermediários definidos na
   proposta (formalidade, voluntarismo, nível, esfera, motivação, modo de
   operação, centralidade, grau de separação), hoje ainda não codificados.
5. Discutir com o Prof. Levi-Faur o escopo definitivo do corpus e o formato de
   entrega esperado, para calibrar as próximas rodadas a partir de seu
   retorno.

## Conclusão

O trabalho apresentado demonstra compreensão do problema teórico proposto,
uma operacionalização empírica funcional (não apenas conceitual) sobre texto
legal real, e uma proposta de codificação que já resolve a maior parte dos
casos sem intervenção humana, reservando o alerta de verificação humana para
os casos genuinamente ambíguos. As escolhas de desenho — classificação em
camadas de confiança, exigência de evidência verbatim, ancoragem teórica
explícita e validação incremental — não são arbitrárias: replicam princípios
já testados e refinados ao longo de vários ciclos do meu programa de pesquisa
ARENAS, aplicados agora a um novo domínio empírico e a uma nova teoria.
