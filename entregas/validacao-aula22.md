# Verificação local da Aula 22

Data: 01/11/2026. Estado: alterações preparadas para revisão antes do commit.

## Testes automatizados

Comando: `python -m unittest discover -s tests -v`.

Cinco testes verificam:

- Filtros combinados e controle de preservação do registro sem placar.
- Correlações e tamanhos dos pares completos; variável constante indefinida, inclusive na diagonal de Kendall.
- Seleção de zero, uma e várias variáveis; fases vazias; intervalos e alternância das duas abas.
- Soma, média e percentuais em um conjunto pequeno de placares conhecidos. O jogo sem placar não entra nos denominadores; um recorte sem placares não produz indicadores fictícios.
- Quatro métricas no app, filtros do Dashboard 2 e conferência do recorte da final de 1930: 6 gols, média 6,00, 100% de partidas com 3+ gols e 0% de empates no tempo integral.

Os esquemas dos gráficos Altair são validados durante os testes.

## Conferência no navegador local

Endereço de revisão: `http://127.0.0.1:8502/`.

- Dashboard 1: mapa de calor e histogramas inspecionados visualmente.
- Dashboard 2: quatro cartões e os três visuais carregaram sem erro na versão conferida.
- Base inicial dos indicadores: 1.068 partidas com placar em 23 edições.
- Clique no ponto de 2022: cartões e gráficos inferiores passaram para 64 partidas e uma edição.
- Shift + clique no ponto de 2026: o recorte passou para 168 partidas em duas edições.
- Limpeza da seleção: retorno às 1.068 partidas e 23 edições.
- Os cartões exibiram 2.949 gols, média 2,76, 50,2% de partidas com 3+ gols e 25,7% de empates no recorte inicial do arquivo.

Esses valores descrevem o CSV da EDA; não representam conferência independente da fonte esportiva.

## Reprodução da EDA

As 41 células de código do notebook adaptado foram executadas em sequência usando backend de gráficos sem janela. O CSV exportado foi comparado ao anterior e resultou idêntico: 1.069 registros, 27 colunas e 1.068 placares válidos. A EDA original `notebooks/eda-rjdo.ipynb` permanece intacta.

## Pendências reservadas

- Revisão e aprovação individual do conteúdo e do commit pelo autor.
- Registros de prompts e declaração, reservados para o final conforme combinado.
- Publicação, URL no README e testes em janela anônima do app publicado: etapa da Aula 23.
