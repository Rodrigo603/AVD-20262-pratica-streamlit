"""Esqueleto do Dashboard 1 - entrega da Aula 21."""
import streamlit as st
from src.data_loader import load_data

st.set_page_config(page_title="Copa em Dados", page_icon="⚽", layout="wide")

VARS_QUANT = {
    "world_cup_year": "Ano da Copa",
    "fulltime_score_team1": "Gols no tempo integral - Time 1",
    "fulltime_score_team2": "Gols no tempo integral - Time 2",
    "gols_totais": "Total de gols no tempo integral",
    "extra_time_score_team1": "Placar de prorrogação - Time 1",
    "extra_time_score_team2": "Placar de prorrogação - Time 2",
    "penalty_score_team1": "Disputa de pênaltis - Time 1",
    "penalty_score_team2": "Disputa de pênaltis - Time 2",
}

df = load_data()
with st.sidebar:
    st.header("Filtros")
    variaveis = st.multiselect(
        "Variáveis quantitativas", options=list(VARS_QUANT),
        default=list(VARS_QUANT)[:4], format_func=VARS_QUANT.get, key="variaveis",
    )
    anos = st.slider(
        "Intervalo de edições", min_value=int(df.world_cup_year.min()),
        max_value=int(df.world_cup_year.max()),
        value=(int(df.world_cup_year.min()), int(df.world_cup_year.max())), key="anos",
    )

recorte = df[df.world_cup_year.between(*anos)]
st.title("Copa em Dados")
st.subheader("Laboratório de distribuição e correlação")
st.caption(f"{len(recorte)} de {len(df)} registros no intervalo selecionado. "
           f"{recorte.gols_totais.notna().sum()} com placar de tempo integral.")
st.write("Variáveis selecionadas: " + (", ".join(VARS_QUANT[v] for v in variaveis) or "nenhuma"))

correlacao, distribuicao = st.columns([1, 1.5])
with correlacao:
    st.subheader("Correlação")
    if len(variaveis) < 2:
        st.info("Selecione pelo menos duas variáveis para a futura matriz de correlação.")
    else:
        st.info("Espaço reservado para o mapa de calor. Implementação na Aula 22.")
with distribuicao:
    st.subheader("Distribuição")
    if not variaveis:
        st.info("Selecione uma variável para os futuros histogramas.")
    elif recorte.empty:
        st.warning("Não há partidas no intervalo selecionado.")
    else:
        st.info(f"Espaço reservado para {len(variaveis)} histogramas, um por variável. "
                "Implementação na Aula 22.")

st.divider()
st.caption("Fonte: FIFA World Cup All Matches (1930–2026), Kaggle, conforme a EDA. "
           "Base estática, sem atualização automática ou validação independente dos resultados.")
st.caption("Time 1/2 representam ordem de registro. O walkover sem placar permanece na base, "
           "mas não entra nas estatísticas de gols. Total de gols usa apenas os campos fulltime_score.")
