# Declaração de uso de IA - atividade Streamlit

**Nome:** Rodrigo José Dantas de Oliveira

**Turma:** 5A

**Data de preparação:** 01/11/2026

**Data de entrega informada:** 02/11/2026

**Repositório:** https://github.com/Rodrigo603/AVD-20262-pratica-streamlit

**Escopo:** exclusivamente a atividade de dashboards Streamlit das Aulas 21 a 23.

**Skill oficial do Streamlit:** utilizada na Aula 22 e na preparação da Aula 23; não utilizada no esqueleto inicial da Aula 21.

Este arquivo registra os usos efetivos desta atividade, incluindo propostas de métricas e justificativas produzidas com IA. Não declara que todos os usos se enquadram nas permissões da atividade. A versão final do PDF foi revisada e assinada pelo autor; em 02/11/2026, ele informou ter conversado com a professora e recebido concordância para continuar a entrega.

## Registro bloco a bloco (Seção 5, Opção B)

### Uso 1

- **Data:** 31/10/2026
- **Ferramenta:** Codex; família GPT-6; plano não informado
- **Parte:** app.py (esqueleto), entregas/rascunho-dashboard1.jpg e README.md
- **Finalidade efetiva:** Esqueleto, organização do projeto e interface.
- **O que foi pedido:** Preparar o fork da professora para a atividade Streamlit e separar os commits por aula.
- **Aproveitado e modificado:** Estrutura de pastas, rascunho técnico gerado durante a implementação, filtros iniciais e documentação. Não foi uma foto de rascunho desenhado pelo aluno.
- **Verificação realizada:** AppTest dos widgets; inspeção dos commits pelo usuário e aprovação antes do envio.
- **Referência:** prompts/prompts-utilizados.md; commits e417cc6, 977a3d2 e f423ff5.

### Uso 2

- **Data:** 31/10/2026 a 01/11/2026
- **Ferramenta:** Codex; família GPT-6; plano não informado
- **Parte:** Integração dos dados com o Streamlit: data/clean/dataset.csv, src/data_loader.py e célula de exportação em notebooks/eda-com-downloads.ipynb.
- **Finalidade efetiva:** Adaptação da leitura e exportação de dados para o aplicativo Streamlit.
- **O que foi pedido:** Preparar a entrega da Aula 21 com o dataset tratado disponível no repositório.
- **Aproveitado e modificado:** Leitura do CSV local, célula de exportação e integração dos dados já tratados com o aplicativo.
- **Verificação realizada:** Células executadas em sequência e CSV exportado comparado ao anterior; o notebook recebido foi preservado.
- **Referência:** entregas/validacao-aula22.md; prompts/prompts-utilizados.md.

### Uso 3

- **Data:** 01/11/2026
- **Ferramenta:** Codex e Skill oficial developing-with-streamlit (Streamlit 1.66.1)
- **Parte:** Dashboard 1, src/analysis.py, src/charts.py, .streamlit/config.toml
- **Finalidade efetiva:** Sintaxe de gráficos Altair, cache, identidade visual e depuração.
- **O que foi pedido:** Preparar o commit da segunda aula.
- **Aproveitado e modificado:** Mapa de calor, histogramas, filtros compartilhados, cache e tema. A Skill oficial foi consultada e instalada globalmente porque o Windows não permitiu os links simbólicos do projeto. Ela não havia sido usada no esqueleto inicial da Aula 21.
- **Verificação realizada:** Testes de 0/1/2+ variáveis, constantes, ausentes, métodos de correlação e recortes vazios; revisão visual.
- **Referência:** entregas/validacao-aula22.md; commit 2b1a1e1.

### Uso 4

- **Data:** 01/11/2026
- **Ferramenta:** Codex; família GPT-6; plano não informado
- **Parte:** Dashboard 2, entregas/rascunho-dashboard2.jpg e entregas/justificativa-metricas.md
- **Finalidade efetiva:** Proposição de público, métricas e gráficos; cálculo, implementação e redação de justificativas técnicas para revisão.
- **O que foi pedido:** O aluno pediu que a IA escolhesse opções para sua avaliação e, depois, autorizou preparar tudo para o commit.
- **Aproveitado e modificado:** A IA propôs jornalistas esportivos, quatro indicadores e três gráficos. O aluno pediu explicação do total de gols, deu aval à preparação e autorizou o commit após a apresentação da prévia. As justificativas técnicas foram redigidas pela IA; não devem ser apresentadas como reflexão pessoal escrita pelo aluno.
- **Verificação realizada:** Testes com placares conhecidos; navegador verificou seleção de 2022 (64 jogos), 2022+2026 (168) e limpeza (1.068). O autor enviou sua reflexão e os motivos de escolha em 01/11/2026.
- **Referência:** prompts/prompts-utilizados.md; entregas/justificativa-metricas.md; commit 2b1a1e1.

### Uso 5

- **Data:** 31/10/2026 a 01/11/2026
- **Ferramenta:** Codex; família GPT-6; plano não informado
- **Parte:** tests/test_dashboard.py, Git e documentação de validação
- **Finalidade efetiva:** Testes, depuração, organização de commits e documentação técnica.
- **O que foi pedido:** Separar as entregas por aula e mostrar as alterações antes de cada commit.
- **Aproveitado e modificado:** Testes automatizados, correção de constante na diagonal de Kendall, prévias e commits aprovados pelo aluno.
- **Verificação realizada:** Cinco testes passaram na entrega da Aula 22; arquivos locais e origin/main foram conferidos após o push.
- **Referência:** entregas/validacao-aula22.md; histórico Git.

### Uso 6

- **Data:** 01/11/2026
- **Ferramenta:** Codex, Skill oficial do Streamlit e habilidade PDF
- **Parte:** Aula 23: dependências, README, prompts e preparação da declaração
- **Finalidade efetiva:** Preparação de deploy, registro de usos e preenchimento técnico do template.
- **O que foi pedido:** Realizar a parte da Aula 23; nome e turma fornecidos pelo aluno.
- **Aproveitado e modificado:** Separação de dependências do app/notebooks, marcações no código, registros e preenchimento do template com os dados e a reflexão fornecidos pelo autor. O deploy foi realizado pelo aluno no Chrome; o agente verificou o app público e seus controles sem login. O aluno confirmou o teste em janela anônima. A versão final revisada e assinada foi fornecida pelo autor em 02/11/2026.
- **Verificação realizada:** Cinco testes locais; app público acessível; edições, fases, seleção, gols, ausentes, variáveis, métodos e abas testados. Seleção de edições por clique também conferida remotamente. PDF renderizado para revisão.
- **Referência:** entregas/checklist-aula23.md; prompts/declaracao-uso-ia.md.

## Reflexão individual

Texto enviado pelo próprio autor em 01/11/2026, preservado integralmente no PDF:

Durante o trabalho, a IA me ajudou a entender melhor a parte das métricas. Escolhi o total de gols, a média por partida, o percentual de jogos com 3 ou mais gols e o percentual de empates. Entendi que o total de gols sozinho engana, porque o número de partidas muda entre as edições. A média por partida corrige isso e permite comparar edições de tamanhos diferentes. O percentual de jogos com 3+ gols mostra quão ofensivas as partidas foram, e o percentual de empates mostra o equilíbrio entre as seleções. Cada métrica responde a uma pergunta diferente, e foi isso que justificou a minha escolha. A IA também me ajudou a decidir os gráficos. Fiz três: a média de gols por edição, a média por fase e a proporção de empates por edição. Vi que a escolha do tipo de gráfico muda a leitura dos dados. Evoluções ao longo do tempo pedem uma visualização que mostre a tendência, e comparações entre categorias, como as fases, pedem outra. Mesmo com esse apoio, avaliei as sugestões e tomei as decisões finais. O processo me deu mais segurança para analisar dados e explicar minhas escolhas.

## Responsabilidade e assinatura

Os dados de identificação e a reflexão foram fornecidos pelo autor. A declaração final assinada foi recebida em 02/11/2026 e permanece somente no computador do autor, para entrega pelo Classroom. O PDF assinado não integra o histórico público desta entrega, a fim de proteger os dados pessoais incorporados ao certificado.
