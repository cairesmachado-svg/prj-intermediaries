Nota técnica — como eu abordaria a construção do dataset de intermediários na
legislação da UE sobre transição verde. Rascunho para revisão; pode ser anexado
à resposta ou guardado para uma segunda rodada de conversa, conforme o plano em
`00_plano_execucao.md`.

---

## 1. Escopo e unidade de análise
Definir primeiro a unidade de codificação: artigo/dispositivo de um ato
legislativo da UE (regulamento, diretiva, ato delegado) que atribui, cria ou
reconhece uma função de intermediação. Delimitar o universo (ex.: pacote
"Fit for 55", legislação de rotulagem ambiental, ETS, taxonomia verde,
CSRD/due diligence) antes de decidir a estratégia de busca.

## 2. Taxonomia de funções (ponto de partida)
Usar como esqueleto inicial os **quatro mecanismos primários da própria
proposta de David** (seção A4), cada um associado a um modo de governança
diferente — o que já dá, de saída, uma hipótese testável sobre quem tende a
operar cada mecanismo na legislação da UE:

- **Dever de reportar** (report duty) — tipicamente liderado pelo Estado.
- **Certificação** (certification) — tipicamente liderado por ONGs.
- **Ranking/rating** — tipicamente liderado por empresas.
- **Auditoria** (audit) — tipicamente liderado pela profissão (auditores,
  peritos).

Complementar com os **atributos dos intermediários** também definidos na
proposta (formalidade, voluntarismo, nível, esfera, motivação, modo de
operação, centralidade, grau de separação) como colunas adicionais do
codebook, e registrar candidatos aos **quatro tipos de falha** (subcompro-
metimento, sobrecomprometimento, captura, incompetência) sempre que o próprio
texto legal já preveja algum controle sobre isso (ex.: mecanismos de
supervisão do intermediário, sanções por captura). Adaptar/expandir
empiricamente a partir dos primeiros textos codificados, sem fechar a
taxonomia a priori — mas partindo do vocabulário que David já usa, em vez de
uma tipologia externa, facilita tanto a comparação entre os pacotes de
trabalho (WP2–WP5) quanto a conversa inicial com ele.

## 3. Protocolo de triagem (adaptado do que já uso no CNJ)
- Estratégia de busca documentada e versionada (fontes: EUR-Lex, registros de
  atos delegados/implementação).
- Critérios de inclusão/exclusão explícitos, com fluxo tipo PRISMA
  (identificados → triados → incluídos), permitindo auditoria externa.
- Dupla checagem de uma amostra para taxa de concordância entre codificadores
  (mesmo que o "segundo codificador" seja uma segunda passada com regras
  revisadas, na ausência de equipe).

## 4. Codebook e extração de evidências
- Codebook estruturado: id do ato, artigo, tipo de intermediário, função,
  setor, base legal, se é intermediário público/privado/híbrido, se há
  delegação explícita de autoridade.
- Cada código ligado a um trecho de evidência (citação direta do texto legal),
  não só a um rótulo — mesma lógica de trilha de auditoria usada no inventário
  do CNJ.

## 5. Pipeline reproduzível
- Coleta programática de textos (Python), com controle de versão do corpus.
- Camada de triagem assistida por regras (e, se fizer sentido depois de
  validar manualmente uma amostra, apoio de NLP para pré-seleção de trechos
  candidatos) — mas a codificação final permanece auditável e não uma
  caixa-preta.
- Dataset final em formato tabular versionado, com dicionário de dados e
  script de construção documentado, para que qualquer pessoa da equipe
  reproduza o resultado a partir do corpus bruto.

## 6. O que fica em aberto para conversar com David
- Escopo exato do corpus (que legislação entra, qual recorte temporal).
- Se o objetivo é um dataset descritivo (mapeamento) ou se já há uma pergunta
  analítica específica que o dataset precisa responder.
- Formato de entrega esperado e se há outros membros de equipe (postdocs/PhDs
  mencionados na proposta) com quem coordenar o codebook.
