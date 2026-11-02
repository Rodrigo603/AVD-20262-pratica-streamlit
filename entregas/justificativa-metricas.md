# Justificativa das métricas - Dashboard 2

Versão de planejamento para revisão e validação individual do autor antes do commit. Público, métricas e visuais seguem a proposta apresentada nesta conversa. As razões abaixo são justificativas técnicas submetidas à revisão, e não uma reflexão pessoal do estudante.

## Público-alvo e objetivo

Jornalistas esportivos interessados em comparar as edições e fases da Copa do Mundo para preparar pautas e consultar estatísticas de placares. O painel permite selecionar o período, fases, uma seleção e a faixa de gols. Um clique no gráfico de média por edição restringe também os indicadores e os dois gráficos seguintes.

## Base comum e definições

- Uma linha representa um registro de partida; o walkover sem placar não entra em nenhum denominador ou soma deste dashboard.
- Para todos os indicadores, considerar apenas partidas com os dois campos fulltime_score preenchidos.
- `gols_totais = fulltime_score_team1 + fulltime_score_team2`, conforme a EDA.
- Não somar extra_time_score, penalty_score ou as colunas originais total_goals_team1/2.
- Os filtros laterais são aplicados antes do cálculo. Uma seleção de edição no gráfico aplica um recorte adicional aos cartões e aos gráficos de fases e resultados.
- Se não houver partidas válidas, exibir uma mensagem e não apresentar zero como se fosse uma estatística calculada.

## Métrica 1: gols nas partidas selecionadas

- **Variável:** gols_totais.
- **O que mede:** quantidade acumulada de gols no tempo integral; soma dos valores válidos no recorte.
- **Por que foi escolhida (justificativa técnica para revisão):** contextualiza o volume de gols associado ao conjunto consultado.
- **Público-alvo:** jornalistas esportivos.
- **Qual decisão pode ser apoiada:** definir o conjunto de partidas a destacar em uma pauta e consultar seu total acumulado.
- **O que comunica:** quantos gols foram registrados nas partidas selecionadas.
- **Limitação:** depende da quantidade de jogos; comparar totais entre torneios de tamanhos diferentes exige observar também a média por partida.

## Métrica 2: gols por partida

- **Variável:** gols_totais.
- **O que mede:** soma de gols dividida pelo número de partidas com placar válido no recorte.
- **Por que foi escolhida (justificativa técnica para revisão):** oferece uma medida por partida, complementar ao total acumulado.
- **Público-alvo:** jornalistas esportivos.
- **Qual decisão pode ser apoiada:** escolher edições ou fases para uma comparação editorial de frequência média de gols.
- **O que comunica:** quantos gols, em média, ocorreram em cada jogo considerado.
- **Limitação:** a média é sensível a goleadas e a composição das fases pode variar entre recortes.

## Métrica 3: percentual de partidas com 3 ou mais gols

- **Variável:** gols_totais.
- **O que mede:** 100 vezes a quantidade de partidas com gols_totais >= 3 dividida pelo número de partidas com placar válido.
- **Por que foi escolhida (justificativa técnica para revisão):** complementa a média com a frequência de jogos acima de um limite explícito de contagem.
- **Público-alvo:** jornalistas esportivos.
- **Qual decisão pode ser apoiada:** selecionar recortes para uma pauta sobre frequência de partidas com ao menos três gols.
- **O que comunica:** de cada 100 jogos do recorte, qual proporção teve três ou mais gols.
- **Limitação:** o limite é uma definição operacional, não uma classificação objetiva da qualidade ou da emoção do jogo.

## Métrica 4: percentual de empates no tempo integral

- **Variáveis:** fulltime_score_team1 e fulltime_score_team2.
- **O que mede:** 100 vezes a quantidade de jogos cujos dois placares são iguais dividida pelo número de partidas com placar válido.
- **Por que foi escolhida (justificativa técnica para revisão):** acrescenta um indicador de igualdade do placar ao conjunto de medidas de gols.
- **Público-alvo:** jornalistas esportivos.
- **Qual decisão pode ser apoiada:** escolher edições para uma comparação sobre frequência de empates no tempo integral.
- **O que comunica:** a proporção de partidas com os dois placares de tempo integral iguais.
- **Limitação:** não equivale ao campo winner; uma partida empatada no tempo integral pode ter vencedor após prorrogação ou pênaltis.

## Visuais além dos cartões

1. **Linha: média de gols por edição.** Eixo x = world_cup_year; eixo y = média de gols_totais. O tooltip apresenta a quantidade de jogos válidos. Mantém o contexto das edições dos filtros laterais; clique em um ponto restringe os cartões e os outros dois gráficos. Permite consultar a sequência de médias sem comparar apenas totais.
2. **Barras horizontais: média de gols por fase.** Eixo y = stage; eixo x = média de gols_totais, ordenada por média. O tooltip também informa o tamanho do grupo. Permite comparar fases dentro do recorte; preserva os nomes originais e não presume amostras equivalentes.
3. **Barras empilhadas a 100%: empates e placares não empatados por edição.** Eixo x = edição; eixo y = proporção de jogos válidos; cor = igualdade ou diferença do placar de tempo integral. O tooltip informa quantidade e percentual. Compara as proporções sem atribuir vantagem de mandante à posição Time 1/2.

## Conferência dos cálculos

Os testes usam um conjunto pequeno com placares conhecidos, incluem um jogo sem placar e verificam denominadores, soma, média, percentuais, subconjuntos de edição e recortes vazios. A mesma filtragem alimenta os indicadores e os gráficos. O teste da seleção por clique no navegador é registrado separadamente da simulação de widgets.
