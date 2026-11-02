"""Copa em Dados - dashboards baseados na EDA de partidas das Copas."""
# [IA] Codex - estrutura dos dois dashboards, filtros, indicadores e interface.
import streamlit as st
from src.data_loader import load_data
from src.analysis import (VARS_QUANT, filter_matches, correlation_table,
                          valid_scores, indicator_values, filter_selected_editions)
from src.charts import (correlation_chart, histogram_chart, edition_chart,
                        phase_chart, result_chart)

st.set_page_config(page_title="Copa em Dados", page_icon="⚽", layout="wide")
st.caption("ANÁLISE E VISUALIZAÇÃO DE DADOS · 2026.2")
st.title("Copa em Dados")
st.write("Explore as partidas das Copas do Mundo a partir da sua EDA.")

df = load_data()
with st.sidebar:
    st.header("Filtros das partidas")
    anos = st.slider(
        "Intervalo de edições", min_value=int(df.world_cup_year.min()),
        max_value=int(df.world_cup_year.max()),
        value=(int(df.world_cup_year.min()), int(df.world_cup_year.max())), key="anos",
    )
    fases = st.multiselect("Fases", options=sorted(df.stage.unique()),
                           default=sorted(df.stage.unique()), key="fases")
    selecao = st.selectbox("Seleção", options=["Todas"] + sorted(set(df.team1) | set(df.team2)),
                           key="selecao")
    gols = st.slider("Total de gols no tempo integral", min_value=0,
                     max_value=int(df.gols_totais.max()), value=(0, int(df.gols_totais.max())),
                     key="gols")
    manter_ausentes = st.checkbox("Manter registros sem placar", value=True, key="manter_ausentes")
    st.caption("Os filtros de partidas afetam as duas abas. Registros sem placar não entram nos cálculos de gols.")
    st.divider()
    st.subheader("Controles do laboratório")
    variaveis = st.multiselect(
        "Variáveis quantitativas", options=list(VARS_QUANT),
        default=list(VARS_QUANT)[:4], format_func=VARS_QUANT.get, key="variaveis",
    )
    metodo = st.segmented_control("Correlação", options=["spearman", "pearson", "kendall"],
                                  default="spearman", format_func=str.title, key="metodo") or "spearman"

recorte = filter_matches(df, anos, fases, selecao, gols, manter_ausentes)
st.caption(f"{len(recorte)} de {len(df)} registros no recorte · "
           f"{recorte.gols_totais.notna().sum()} com placar de tempo integral")
laboratorio, indicadores = st.tabs(
    ["Dashboard 1 · Laboratório", "Dashboard 2 · Indicadores"],
    key="dashboard", on_change="rerun",
)

if laboratorio.open:
    with laboratorio:
        st.subheader("Distribuição e correlação")
        if recorte.empty:
            st.warning("Nenhuma partida no recorte. Amplie os intervalos ou selecione outras fases.")
        elif not variaveis:
            st.info("Selecione pelo menos uma variável quantitativa no painel lateral.")
        else:
            with st.container(border=True):
                st.subheader(f"Correlação · {metodo.title()}")
                if len(variaveis) < 2:
                    st.info("Selecione pelo menos duas variáveis para o mapa de calor.")
                else:
                    tabela = correlation_table(recorte, variaveis, metodo)
                    st.altair_chart(correlation_chart(tabela, variaveis, metodo),
                                     key="correlacao", width="stretch",
                                     alt="Correlação entre as variáveis selecionadas; passe o cursor para consultar os pares válidos.")
                    st.caption("Células com — indicam variável constante ou menos de dois pares válidos. "
                               "Cada par usa somente seus valores completos.")
                st.caption("Correlação não demonstra causalidade. O total de gols é a soma dos dois placares de tempo integral.")
            st.subheader("Distribuições")
            for inicio in range(0, len(variaveis), 2):
                colunas = st.columns(2)
                for coluna, variavel in zip(colunas, variaveis[inicio:inicio + 2]):
                    with coluna:
                        with st.container(border=True):
                            st.markdown(f"**{VARS_QUANT[variavel]}**")
                            serie = recorte[variavel].dropna()
                            if serie.empty:
                                st.info("Sem valores disponíveis para esta variável no recorte.")
                            else:
                                st.altair_chart(histogram_chart(recorte, variavel),
                                                 key=f"hist_{variavel}", width="stretch",
                                                 alt=f"Distribuição de {VARS_QUANT[variavel]} nas partidas selecionadas.")
                                st.caption(f"Válidos: {len(serie)} · Ausentes: {len(recorte)-len(serie)}; "
                                           f"média: {serie.mean():.2f} · mediana: {serie.median():.2f}")
            with st.expander("Estatísticas descritivas"):
                st.dataframe(recorte[variaveis].describe().rename(columns=VARS_QUANT),
                              width="stretch", alt="Estatísticas descritivas das variáveis selecionadas.")

if indicadores.open:
    with indicadores:
        st.subheader("Indicadores para jornalistas esportivos")
        st.write("Compare os placares das edições e das fases selecionadas.")
        validos = valid_scores(recorte)
        if validos.empty:
            st.warning("Não há partidas com placar no recorte. Amplie os filtros para calcular os indicadores.")
        else:
            metricas_area = st.container()
            st.subheader("Média de gols por edição")
            st.caption("Clique em um ponto para filtrar os cartões e os dois gráficos abaixo. "
                       "Shift + clique adiciona edições; clique duas vezes no fundo para limpar.")
            evento = st.altair_chart(edition_chart(validos), key="edicoes", on_select="rerun",
                                     selection_mode="edicao", width="stretch",
                                     alt="Média de gols por edição da Copa, com seleção de edições por clique.")
            selecionados = filter_selected_editions(validos, evento.selection.get("edicao", []))
            valores = indicator_values(selecionados)
            with metricas_area:
                edicoes_ativas = sorted(selecionados.world_cup_year.unique())
                st.caption(f"Base dos indicadores: {valores['partidas']} partidas com placar · "
                           f"{len(edicoes_ativas)} edição(ões). Todos os valores usam o tempo integral.")
                total_col, media_col = st.columns(2)
                total_col.metric("Gols nas partidas selecionadas", f"{valores['gols']:,}".replace(",", "."),
                                 border=True, help="Soma de gols_totais nas partidas com placar.")
                media_col.metric("Gols por partida", f"{valores['media']:.2f}".replace(".", ","),
                                 border=True, help="Soma de gols dividida pelo número de partidas com placar.")
                tres_col, empate_col = st.columns(2)
                tres_col.metric("Partidas com 3+ gols", f"{valores['tres_mais']:.1f}%".replace(".", ","),
                                border=True, help="Percentual de partidas com gols_totais maior ou igual a 3.")
                empate_col.metric("Empates no tempo integral", f"{valores['empates']:.1f}%".replace(".", ","),
                                  border=True, help="Percentual com fulltime_score_team1 igual a fulltime_score_team2.")
            st.subheader("Média de gols por fase")
            st.altair_chart(phase_chart(selecionados), key="fases_indicadores", width="stretch",
                             alt="Média de gols por fase nas edições e partidas selecionadas.")
            st.caption("O tooltip informa a quantidade de partidas por fase. Os nomes das fases são os da base original.")
            st.subheader("Empates e placares não empatados por edição")
            st.altair_chart(result_chart(selecionados), key="resultados_indicadores", width="stretch",
                             alt="Proporção de empates e placares não empatados no tempo integral por edição.")
            st.caption("Empate aqui significa igualdade no placar de tempo integral; "
                       "não indica necessariamente o resultado final após prorrogação ou pênaltis.")

with st.expander("Fonte e tratamento dos dados"):
    st.write("Fonte: FIFA World Cup All Matches (1930–2026), Kaggle, conforme a EDA. "
             "Base estática, sem atualização automática ou validação independente dos resultados esportivos.")
    st.write("Time 1/2 representam ordem de registro. O walkover sem placar permanece na base, "
             "mas não entra nas estatísticas de gols. Total de gols usa apenas os campos fulltime_score, "
             "sem somar prorrogação ou disputa de pênaltis.")
    st.caption("Os campos de prorrogação e pênaltis incluem zeros estruturais preenchidos na EDA. "
               "Placares de intervalo ausentes permanecem ausentes; nenhuma goleada foi removida.")
