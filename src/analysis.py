"""Filtros e cálculos utilizados pelo laboratório de análise."""
# [IA] Codex - filtros, correlação e cálculo dos indicadores.
import pandas as pd

VARS_QUANT = {
    "world_cup_year": "Ano da Copa",
    "fulltime_score_team1": "Gols no tempo integral - Time 1",
    "fulltime_score_team2": "Gols no tempo integral - Time 2",
    "gols_totais": "Total de gols no tempo integral",
    "extra_time_score_team1": "Placar de prorrogação - Time 1",
    "extra_time_score_team2": "Placar de prorrogação - Time 2",
    "penalty_score_team1": "Disputa de pênaltis - Time 1",
    "penalty_score_team2": "Disputa de pênaltis - Time 2",
    "halftime_score_team1": "Gols no intervalo - Time 1",
    "halftime_score_team2": "Gols no intervalo - Time 2",
}
SHORT_LABELS = {
    "world_cup_year": "Ano",
    "fulltime_score_team1": "Integral T1",
    "fulltime_score_team2": "Integral T2",
    "gols_totais": "Total de gols",
    "extra_time_score_team1": "Prorrog. T1",
    "extra_time_score_team2": "Prorrog. T2",
    "penalty_score_team1": "Pênaltis T1",
    "penalty_score_team2": "Pênaltis T2",
    "halftime_score_team1": "Intervalo T1",
    "halftime_score_team2": "Intervalo T2",
}


def filter_matches(df, years, stages, team, goals, keep_missing):
    """Intervalos inclusivos; os ausentes do placar têm controle explícito."""
    mask = df.world_cup_year.between(*years) & df.stage.isin(stages)
    if team != "Todas":
        mask &= df.team1.eq(team) | df.team2.eq(team)
    mask &= df.gols_totais.between(*goals) | (df.gols_totais.isna() & keep_missing)
    return df.loc[mask].copy()


def correlation_table(df, variables, method):
    """Correlação por pares completos, com o tamanho de cada par disponível."""
    corr = df[variables].corr(method=method, min_periods=2)
    # O pandas pode retornar 1 na diagonal de Kendall mesmo para uma constante.
    # Sem variação, o coeficiente não é definido, inclusive nessa diagonal.
    constants = [v for v in variables if df[v].nunique(dropna=True) < 2]
    corr.loc[constants, :] = float("nan")
    corr.loc[:, constants] = float("nan")
    present = df[variables].notna().astype(int)
    counts = present.T @ present
    rows = []
    for row in variables:
        for column in variables:
            value = corr.loc[row, column]
            rows.append({
                "x": SHORT_LABELS[column], "y": SHORT_LABELS[row],
                "variavel_x": VARS_QUANT[column], "variavel_y": VARS_QUANT[row],
                "correlacao": value, "pares_validos": int(counts.loc[row, column]),
                "rotulo": f"{value:.2f}" if pd.notna(value) else "—",
            })
    return pd.DataFrame(rows)


def valid_scores(df):
    """O walkover não entra no denominador de nenhuma métrica de gols."""
    return df.dropna(subset=["fulltime_score_team1", "fulltime_score_team2", "gols_totais"]).copy()


def indicator_values(df):
    games = valid_scores(df)
    if games.empty:
        return {"partidas": 0, "gols": None, "media": None, "tres_mais": None, "empates": None}
    return {
        "partidas": len(games),
        "gols": int(games.gols_totais.sum()),
        "media": float(games.gols_totais.mean()),
        "tres_mais": float(games.gols_totais.ge(3).mean() * 100),
        "empates": float(games.fulltime_score_team1.eq(games.fulltime_score_team2).mean() * 100),
    }


def filter_selected_editions(df, selection):
    """Ignora seleções antigas de edições que já saíram do filtro lateral."""
    years = [item["world_cup_year"] for item in selection
             if item.get("world_cup_year") in set(df.world_cup_year)]
    return df[df.world_cup_year.isin(years)].copy() if years else df.copy()
