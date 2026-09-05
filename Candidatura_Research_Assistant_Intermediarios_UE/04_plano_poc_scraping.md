Plano — produto de demonstração (prova de conceito) para acompanhar a
candidatura. Responde à pergunta: dá para construir isso por raspagem?

---

## Resposta curta
Sim. Mas "raspagem" no sentido de baixar HTML bruto da EUR-Lex não é a melhor
via — existe uma API/SPARQL oficial, os dados são informação pública da UE de
reuso livre, e usar a via oficial produz um pipeline mais robusto e mais fácil
de defender tecnicamente numa entrevista.

## Fontes de dados (em ordem de preferência)
1. **SPARQL endpoint da Cellar** (`publications.europa.eu/webapi/rdf/sparql`)
   — repositório semântico oficial de toda a legislação da UE. Permite
   consultar metadados (data, tipo de ato, área temática, idioma) e obter o
   identificador CELEX de cada documento sem baixar HTML.
2. **EUR-Lex REST/search** — busca por palavra-chave e recorte temático
   (ex.: "green transition", "environmental", "taxonomy regulation"),
   devolvendo lista de atos com CELEX.
3. **Texto integral** — a partir do CELEX, baixar o texto (HTML ou Formex/XML)
   de cada ato pela própria EUR-Lex. Isso tecnicamente é uma requisição HTTP
   por documento, então ainda envolve "raspagem" nesse último passo — mas
   sobre uma lista de documentos já filtrada pela API, não sobre a busca
   inteira do site.

Só cair para scraping puro de HTML (sem SPARQL/REST) se algum recorte não for
alcançável pela API — pouco provável para legislação, mais provável para
documentos de acompanhamento/implementação de agências específicas.

## Escopo do PoC (deliberadamente pequeno, viável em poucos dias)
Não tentar cobrir "toda a legislação da UE sobre transição verde" — isso é o
projeto inteiro do David. O PoC deve provar o método num recorte fechado:

- Escolher **um único ato ou pacote pequeno** (ex.: o Regulamento da
  Taxonomia Verde, ou um único ato do pacote "Fit for 55") como corpus de
  teste.
- Coletar o texto integral desse ato via CELEX.
- Aplicar o codebook simplificado dos **quatro mecanismos primários** já
  definidos em `03_nota_tecnica_abordagem.md` (reportar, certificação,
  ranking/rating, auditoria) como regras de triagem por palavra-chave/padrão.
- Produzir uma tabela pequena (CSV) com: CELEX, artigo, mecanismo, trecho de
  evidência (citação direta), tipo de ator (Estado/ONG/empresa/profissão).
- Validar manualmente cada linha da amostra (é pequena o bastante para isso).

## Etapas e sequência (ordem de grandeza, não cronograma fechado)
1. Definir o ato/recorte de teste e os termos-gatilho por mecanismo.
2. Consultar a Cellar/EUR-Lex para obter o CELEX e o texto integral do ato.
3. Escrever o coletor em Python (requisição HTTP + parsing do HTML/XML).
4. Escrever as regras de triagem (busca por padrão/keyword por mecanismo) e
   rodar sobre o texto coletado.
5. Validar manualmente as linhas geradas, ajustar regras onde houver ruído.
6. Empacotar: script(s) Python, dataset CSV de saída, README curto explicando
   o método e suas limitações (é uma prova de conceito de um único ato, não
   uma amostra representativa).

## Cuidados técnicos e éticos
- Preferir a API/SPARQL a HTML bruto sempre que possível.
- Se precisar buscar HTML diretamente, respeitar `robots.txt` e manter uma
  taxa de requisição baixa (não é um corpus grande o suficiente para precisar
  de paralelismo agressivo).
- Dados da EUR-Lex são informação do setor público, license aberta — uso para
  pesquisa é seguro; não há dado pessoal envolvido (é texto legislativo).
- Documentar a trilha de decisões de codificação desde o início, mesmo no
  PoC — é o mesmo padrão já usado no inventário do CNJ e é isso que o David
  provavelmente vai querer ver.

## Decisão em aberto: quando entregar o PoC
Duas opções:
- **Enviar já com a resposta inicial** — mostra iniciativa concreta, mas
  atrasa o envio (o PoC leva alguns dias) e arrisca construir algo fora do
  escopo que ele realmente quer.
- **Oferecer como próximo passo** — enviar a resposta com background/
  interesses agora (mais rápido, sem prazo conhecido) e propor o PoC como
  demonstração se ele responder com interesse em prosseguir.

Recomendação: a segunda opção. `01_resposta_david.md` já pergunta prazo e
formato esperado — faz sentido calibrar o PoC a partir da resposta dele, em
vez de adivinhar o escopo antes de qualquer contato.
