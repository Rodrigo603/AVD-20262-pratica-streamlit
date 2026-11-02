# Copa em Dados - AVD 2026.2

Projeto individual de Rodrigo José Dantas de Oliveira (turma 5A), desenvolvido a partir do [repositório-modelo da disciplina](https://github.com/mfal-school/AVD-20262-pratica-streamlit).

**Aplicação publicada:** [Abrir Copa em Dados](https://avd-20262-pratica-app-esinvgkzeu54ts2nfappsuq.streamlit.app/)

**Repositório:** [Rodrigo603/AVD-20262-pratica-streamlit](https://github.com/Rodrigo603/AVD-20262-pratica-streamlit)

## Preparação inicial

- Tema da EDA: **FIFA World Cup All Matches (1930–2026)**, de laxmikantaroy, no Kaggle.
- [EDA original do trabalho](notebooks/eda-rjdo.ipynb): arquivo recebido, preservado sem alterações de análise ou código.
- O notebook de referência da professora permanece em `notebooks/arquivo-eda-original.ipynb`.
- Aula 21: EDA, exportação dos dados, rascunho e esqueleto com seletor e slider.
- Aula 22: os dois dashboards estão implementados com Altair, filtros compartilhados, quatro indicadores e três visuais no Dashboard 2.
- Entregas registradas separadamente: Aula 21 (dados e esqueleto), Aula 22 (dashboards e documentação) e Aula 23 (finalização e publicação).
- Aula 23: app publicado e testado; declaração assinada destinada à entrega pelo Classroom.
- Apoio de IA nesta preparação: Codex, para organização do repositório e redação desta seção.


## Entrega da Aula 21

- `notebooks/eda-rjdo.ipynb`: EDA original, preservada.
- `notebooks/eda-com-downloads.ipynb`: mesma EDA com leitura do CSV local e célula final de exportação. As saídas foram limpas para permitir nova execução.
- `data/clean/dataset.csv`: dados tratados da EDA de futebol (1.069 registros e 1.068 placares válidos), substituindo os dados do exemplo Heart Disease.
- `entregas/rascunho-dashboard1.jpg`: rascunho estrutural do laboratório.
- `app.py`: o esqueleto está no commit da Aula 21; a versão atual acrescenta o laboratório da Aula 22.

### Reproduzir os dados

Baixe o CSV `fifa_world_cup_all_matches_1930_2026.csv` do [dataset utilizado na EDA](https://www.kaggle.com/datasets/laxmikantaroy/fifa-world-cup-all-matches-19302026), versão 2, e coloque-o em `data/raw/`. O dado bruto fica local, conforme o `.gitignore` do modelo. Execute `notebooks/eda-com-downloads.ipynb` a partir da raiz do projeto ou da pasta `notebooks/`; a última célula exporta `data/clean/dataset.csv`. O app lê somente esse CSV tratado versionado.

Os tratamentos preservam as decisões da EDA: grupos/cidade recodificados, zeros estruturais em prorrogação e pênaltis, ausências do intervalo preservadas, gols recalculados pelos placares de tempo integral e goleadas mantidas. A partida sem placar permanece com gols ausentes.

## Entrega da Aula 22

O Dashboard 1 possui mapa de calor de Spearman, Pearson ou Kendall e um histograma para cada variável selecionada. A seleção de variáveis controla o laboratório; os filtros de edição, fase, seleção e total de gols controlam os registros das duas abas. Registros sem placar podem ser mantidos na contagem por uma caixa de seleção, mas não entram nos cálculos que exigem esse placar.

O mapa informa o número de pares válidos no tooltip. Variáveis constantes ou sem pares suficientes aparecem com coeficiente indefinido. As distribuições mostram válidos, ausentes, média e mediana; não há imputação adicional no aplicativo.

A identidade visual usa os tons roxos da EDA por meio de `.streamlit/config.toml`, sem CSS personalizado. A leitura do CSV utiliza `@st.cache_data` com validade de uma hora.

### Dashboard 2 - indicadores para jornalistas esportivos

O painel apresenta quatro métricas de tempo integral: gols nas partidas selecionadas, média de gols por partida, percentual de partidas com três ou mais gols e percentual de empates. As fórmulas e as justificativas técnicas para revisão individual estão em [entregas/justificativa-metricas.md](entregas/justificativa-metricas.md).

Os três visuais são: média de gols por edição (linha), média por fase (barras horizontais) e proporção de empates e placares não empatados por edição (barras empilhadas a 100%). O rascunho está em [entregas/rascunho-dashboard2.jpg](entregas/rascunho-dashboard2.jpg).

Um clique em uma edição no primeiro gráfico filtra os cartões e os dois gráficos seguintes. Shift + clique permite selecionar várias edições; clique duplo no fundo do gráfico limpa a seleção. O gráfico de linha mantém o contexto dos filtros laterais. Edições de uma seleção anterior que deixaram de pertencer ao recorte lateral são ignoradas.

As quatro métricas excluem a partida sem placar tanto da soma quanto dos denominadores. Um recorte sem partidas válidas exibe uma mensagem em lugar dos cartões. Empate aqui é igualdade do placar de tempo integral, e não o desfecho final após prorrogação ou pênaltis. Time 1/2 não são usados como mandante/visitante.

### Verificações

```bash
python -m unittest discover -s tests -v
```

Cinco testes automatizados verificam filtros combinados, seleção de 0/1/2+ variáveis, métodos de correlação, variável constante, recorte vazio, alternância entre abas, os denominadores dos indicadores e as quatro métricas em um subconjunto conhecido. Os gráficos de todas as variáveis também tiveram seus esquemas Altair validados. As 41 células de código da EDA adaptada foram executadas em sequência e reproduziram o mesmo CSV tratado, sem alterar a EDA original.

A revisão visual local e o teste da seleção por clique estão descritos em `entregas/validacao-aula22.md`. Os testes locais não substituem o teste do app publicado da Aula 23. O registro de usos e os prompts relevantes estão em `prompts/`. A declaração assinada será enviada pelo autor diretamente no Classroom, para preservar os dados pessoais incorporados ao certificado.

## Entrega da Aula 23

O app está publicado no Streamlit Community Cloud a partir da branch main e de app.py. O conteúdo visual publicado foi testado com o commit da Aula 22 (2b1a1e1). O repositório inclui a documentação e as dependências de produção. A declaração assinada será entregue separadamente pelo Classroom.

- [Checklist de publicação e testes](entregas/checklist-aula23.md).
- [Evidência do app publicado](entregas/evidencia-app-publicado.jpg).
- [Registro de usos de IA](prompts/declaracao-uso-ia.md) e [prompts relevantes](prompts/prompts-utilizados.md).
- Declaração de uso de IA: documento assinado entregue separadamente pelo Classroom; não disponibilizado publicamente para proteger os dados pessoais do certificado.

### Dependências

`requirements.txt` contém somente as bibliotecas do app, nas versões testadas. Para executar os notebooks, instale também:

```bash
python -m pip install -r requirements-notebooks.txt
```

A EDA original utiliza Kaggle; a versão adaptada lê o CSV bruto local. O app publicado utiliza apenas o CSV tratado versionado.

### Registro de autoria e revisão

O projeto recebeu apoio de Codex para implementação, interface, rascunhos, documentação, testes, proposta de métricas e justificativas técnicas. A Skill oficial do Streamlit foi usada na Aula 22 e na preparação da Aula 23. Os trechos de código desta implementação estão marcados com `# [IA]`.

O registro de usos descreve o apoio recebido. A versão assinada da declaração será enviada pelo autor no Classroom. Em 02/11/2026, o autor informou ter conversado com a professora e recebido sua concordância para prosseguir com a entrega.

## Orientações do repositório-modelo


Repositório utilizado para aula prática relacionada a Streamlit na disciplina Análise e Visualização de Dados da Cesar School no período de 2026.2.

Repositório-modelo das Aulas 21, 22 e 23: construção de dois dashboards em Streamlit a partir da EDA desenvolvida em sala. O deploy dos dashboards ocorrerá via Streamlit Community Cloud e serão os seguintes:

- Dashboard 1 = correlação + distribuição das variáveis quantitativas
- Dashboard 2 = KPIs

## Setup

Versão validada neste projeto: **Python 3.14**. As dependências do app estão fixadas em `requirements.txt`; use essa versão também nas configurações avançadas do deploy. Confira a sua versão antes de começar:

| Sistema | Verificar versão |
| --- | --- |
| macOS / Linux | `python3 --version` |
| Windows | `py --version` |

### 1. Criar e ativar o ambiente virtual

O nome do comando do Python muda por sistema (em muitas máquinas `python` nem existe). Use a linha do seu sistema:

| Sistema | Criar | Ativar |
| --- | --- | --- |
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows (PowerShell) | `py -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `py -m venv .venv` | `.venv\Scripts\activate.bat` |

Se você tem várias versões instaladas, escolha uma compatível, por exemplo `python3.12 -m venv .venv` (macOS/Linux) ou `py -3.12 -m venv .venv` (Windows).

Com o ambiente ativo, o terminal mostra `(.venv)` no início da linha. **A partir daqui os comandos são iguais em todos os sistemas**, porque dentro do venv `python` e `pip` sempre existem.

### 2. Instalar, configurar a IA e rodar

```bash
python -m pip install -r requirements.txt

# Skills de IA do Streamlit (ver seção "IA neste projeto")
streamlit skills --yes

streamlit run app.py
```

### Problemas comuns

- **`python: command not found` / `python` não é reconhecido:** use `python3` (macOS/Linux) ou `py` (Windows) só para criar o venv; depois de ativado, `python` funciona.
- **Linux (Debian/Ubuntu): `ensurepip is not available` ou `No module named venv`:** instale `sudo apt install python3-venv` (ou `python3.X-venv` para a sua versão).
- **Windows: "a execução de scripts foi desabilitada" ao ativar no PowerShell:** rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, ou use o cmd.
- **Python fora de 3.11–3.15:** instale uma versão compatível em [python.org](https://www.python.org/downloads/) e crie o venv com ela, como no exemplo acima.
- **Apareceu `ModuleNotFoundError` ou `streamlit: command not found`:** o venv provavelmente não está ativo. Ative de novo e confira o `(.venv)` no prompt.
- **Erro de certificado no `pip install` (macOS, Python do python.org):** rode `Install Certificates.command`, na pasta Python 3.X em Aplicativos.
- **`DatasetNotFoundError` ao baixar o dataset no notebook (macOS, Python do python.org):** é o mesmo problema de certificado SSL (o `pandas` não consegue ler o CSV da UCI). Rode `Install Certificates.command` e reinicie o kernel. O notebook `eda-com-downloads.ipynb` já define `SSL_CERT_FILE` com o `certifi` como contorno.

## Estrutura de dados: `data/raw` vs `data/clean`

- `data/raw/`: o dataset **bruto**, como foi baixado. Nunca é editado à mão.
- `data/clean/`: o dataset **já tratado**, exportado na última célula do notebook de EDA (ex.: `df.to_csv("data/clean/dataset.csv", index=False)`). O `app.py` lê **somente** desta pasta, via `src/data_loader.py`.

### O que vai para o Git

| Pasta | Versionada? | Por quê |
| --- | --- | --- |
| `data/raw/` | **Não** (só o `.gitkeep`) | O bruto pode ser grande ou ter dados sensíveis, e o app não o usa. |
| `data/clean/` | **Sim** | O Streamlit Community Cloud faz deploy a partir do GitHub e só enxerga o que está no repositório. Sem o CSV tratado no repo, o app funciona na sua máquina e **quebra no deploy**. |

### Antes de dar `git push` com o dado tratado

- **O dado é público ou pode ser compartilhado?** Se não for claramente público, use um **repositório privado** (o Community Cloud permite conectar repositórios privados ao autorizar o GitHub; confirme na hora do deploy). Nesse caso, dê acesso de leitura ao professor (como colaborador ou pela organização).
- **Dado sensível** (nomes, CPF, e-mail, telefone, localização exata etc.): remova ou anonimize na EDA, antes de exportar para `data/clean/`. Isso vale mesmo em repositório privado.
- **Tamanho:** o GitHub rejeita arquivos acima de **100 MB**. Se o CSV tratado for grande, reduza colunas e linhas na EDA ou exporte em Parquet (`df.to_parquet(...)`, exige `pyarrow`).
- **Lembre de commitar o arquivo:** confira com `git status` que `data/clean/dataset.csv` aparece como novo arquivo.

## Passo a passo

O passo a passo detalhado de cada aula (Aulas 21, 22 e 23), com pré-requisitos e objetivos, está em [ROTEIRO.md](ROTEIRO.md). Comece por ele depois do Setup.

**Link do app (Aula 23):** [Copa em Dados](https://avd-20262-pratica-app-esinvgkzeu54ts2nfappsuq.streamlit.app/)

## IA neste projeto

Este projeto usa o **streamlit skills**: um conjunto de instruções (arquivos `SKILL.md`) que a ferramenta de IA lê para escrever código Streamlit seguindo boas práticas (estrutura de layout, cache, widgets, etc.).

**Como instalar:** depois do `pip install -r requirements.txt`, rode na raiz do projeto:

```bash
streamlit skills        # interativo
streamlit skills --yes  # sem confirmações
```

O comando cria *symlinks* para as skills que acompanham a sua instalação do Streamlit, então elas se atualizam sozinhas quando você atualiza o pacote. (A opção `--global` instala para todos os projetos, em vez de só este.)

**Onde fica instalado:**

- `.claude/skills/`: lido pelo Claude Code.
- `.agents/skills/`: lido pelo Gemini CLI, que já encontra essa pasta sozinho.

Essas pastas **não são versionadas** (ver `.gitignore`): os symlinks apontam para o seu ambiente virtual e não funcionam em outra máquina. Cada pessoa roda `streamlit skills` no próprio clone.

**Se você usa outra ferramenta** (ChatGPT, Copilot Chat, etc.): abra o `SKILL.md` correspondente em `.agents/skills/` e cole o conteúdo manualmente no início do chat, antes do seu pedido.

O uso de IA deve ser declarado conforme a seção abaixo.

## Pasta `prompts/`

A pasta [prompts/](prompts) guarda só o que é sobre **uso de IA**: o template de prompt para transformar o rascunho de layout em esqueleto de código e a **Declaração de Uso de IA** exigida pelo Plano de Ensino. Veja [prompts/README.md](prompts/README.md).

## Pasta `entregas/`

A pasta [entregas/](entregas) guarda os artefatos de entrega que não são sobre IA: os rascunhos de layout de cada dashboard (`.jpg` ou `.png`) e a justificativa das métricas do Dashboard 2. Veja [entregas/README.md](entregas/README.md) para o detalhe de cada arquivo e o checklist por aula. Não coloque esses arquivos no `.gitignore`.
