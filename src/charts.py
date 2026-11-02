"""Gráficos Altair; os cálculos são realizados sobre o recorte filtrado."""
# [IA] Codex - sintaxe Altair, histogramas, mapa de calor e seleção entre gráficos.
import altair as alt
from src.analysis import VARS_QUANT, SHORT_LABELS

PURPLE = "#7252B8"


def correlation_chart(table, variables, method):
    labels = [SHORT_LABELS[v] for v in variables]
    base = alt.Chart(table).encode(
        x=alt.X("x:N", sort=labels, title=None, axis=alt.Axis(labelAngle=-35)),
        y=alt.Y("y:N", sort=labels, title=None),
        tooltip=[alt.Tooltip("variavel_x:N", title="Variável X"),
                 alt.Tooltip("variavel_y:N", title="Variável Y"),
                 alt.Tooltip("correlacao:Q", title=method.title(), format=".3f"),
                 alt.Tooltip("pares_validos:Q", title="Pares válidos")],
    )
    cells = base.mark_rect(stroke="white", strokeWidth=1).encode(
        color=alt.condition(
            "isValid(datum.correlacao)",
            alt.Color("correlacao:Q", title=method.title(),
                      scale=alt.Scale(scheme="redblue", domain=[-1, 1], domainMid=0),
                      legend=alt.Legend(orient="bottom", direction="horizontal", gradientLength=220)),
            alt.value("#E4DFEC"),
        ),
    )
    text = base.mark_text(fontSize=12).encode(
        text="rotulo:N",
        color=alt.condition("abs(datum.correlacao) > 0.6", alt.value("white"), alt.value("#2D223A")),
    )
    return (cells + text).properties(height=max(300, 40 * len(variables))).configure_view(stroke=None)


def histogram_chart(df, variable):
    values = df[[variable]].dropna()
    if variable == "world_cup_year":
        bins = alt.Bin(step=4, anchor=1928)
    else:
        bins = alt.Bin(step=1, extent=[float(values[variable].min()) - .5,
                                      float(values[variable].max()) + .5])
    return (
        alt.Chart(values)
        .mark_bar(color=PURPLE, opacity=.9, binSpacing=2)
        .encode(
            x=alt.X(f"{variable}:Q", bin=bins, title=SHORT_LABELS[variable]),
            y=alt.Y("count():Q", title="Partidas", axis=alt.Axis(tickMinStep=1)),
            tooltip=[alt.Tooltip(f"{variable}:Q", bin=bins, title="Intervalo"),
                     alt.Tooltip("count():Q", title="Partidas")],
        )
        .properties(height=220)
        .interactive()
    )


def edition_chart(games):
    summary = games.groupby("world_cup_year", as_index=False).agg(
        media=("gols_totais", "mean"), partidas=("gols_totais", "size"))
    click = alt.selection_point(name="edicao", fields=["world_cup_year"], nearest=True)
    base = alt.Chart(summary).encode(
        x=alt.X("world_cup_year:Q", title="Edição", axis=alt.Axis(format="d"),
                scale=alt.Scale(zero=False)),
        y=alt.Y("media:Q", title="Gols por partida", scale=alt.Scale(zero=True)),
        tooltip=[alt.Tooltip("world_cup_year:O", title="Edição"),
                 alt.Tooltip("media:Q", title="Gols por partida", format=".2f"),
                 alt.Tooltip("partidas:Q", title="Partidas com placar")],
    )
    line = base.mark_line(color=PURPLE, strokeWidth=3)
    points = base.mark_point(color=PURPLE, filled=True, size=75).encode(
        opacity=alt.condition(click, alt.value(1), alt.value(.3)),
    ).add_params(click)
    return (line + points).properties(height=260)


def phase_chart(games):
    summary = games.groupby("stage", as_index=False).agg(
        media=("gols_totais", "mean"), partidas=("gols_totais", "size"))
    return (
        alt.Chart(summary)
        .mark_bar(color=PURPLE, cornerRadiusEnd=3)
        .encode(
            x=alt.X("media:Q", title="Gols por partida"),
            y=alt.Y("stage:N", title=None, sort="-x", axis=alt.Axis(labelLimit=190)),
            tooltip=[alt.Tooltip("stage:N", title="Fase"),
                     alt.Tooltip("media:Q", title="Média de gols", format=".2f"),
                     alt.Tooltip("partidas:Q", title="Partidas com placar")],
        )
        .properties(height=max(200, len(summary) * 26))
    )


def result_chart(games):
    data = games[["world_cup_year", "fulltime_score_team1", "fulltime_score_team2"]].copy()
    tied = data.fulltime_score_team1.eq(data.fulltime_score_team2)
    data["placar"] = tied.map({True: "Empate", False: "Placar não empatado"})
    summary = data.groupby(["world_cup_year", "placar"], as_index=False).size()
    summary["percentual"] = summary["size"] / summary.groupby("world_cup_year")["size"].transform("sum")
    return (
        alt.Chart(summary)
        .mark_bar()
        .encode(
            x=alt.X("world_cup_year:O", title="Edição", axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("size:Q", stack="normalize", title="Percentual de partidas", axis=alt.Axis(format=".0%")),
            color=alt.Color("placar:N", title="Tempo integral",
                            scale=alt.Scale(domain=["Empate", "Placar não empatado"],
                                            range=["#7252B8", "#D7CBE9"]),
                            legend=alt.Legend(orient="bottom")),
            tooltip=[alt.Tooltip("world_cup_year:O", title="Edição"),
                     alt.Tooltip("placar:N", title="Placar de tempo integral"),
                     alt.Tooltip("size:Q", title="Partidas"),
                     alt.Tooltip("percentual:Q", title="Percentual", format=".1%")],
        )
        .properties(height=260)
    )
