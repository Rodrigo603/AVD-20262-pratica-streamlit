"""Verificações dos filtros e estados de borda exigidos na Aula 22."""
from pathlib import Path
import sys
import unittest
import pandas as pd
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.analysis import (filter_matches, correlation_table, VARS_QUANT,
                          indicator_values, valid_scores, filter_selected_editions)
from src.charts import (histogram_chart, correlation_chart, edition_chart,
                        phase_chart, result_chart)


class DashboardTests(unittest.TestCase):
    def test_filters_preserve_missing_without_inventing_score(self):
        df = pd.DataFrame({
            "world_cup_year": [1930, 1930, 1938, 2022],
            "stage": ["Final", "Group Stage", "Walkover", "Final"],
            "team1": ["A", "A", "A", "B"], "team2": ["B", "C", "C", "C"],
            "gols_totais": [2., 5., float("nan"), 3.],
        })
        args = (df, (1930, 1938), list(df.stage.unique()), "A", (0, 2))
        self.assertEqual(len(filter_matches(*args, False)), 1)
        with_missing = filter_matches(*args, True)
        self.assertEqual(len(with_missing), 2)
        self.assertEqual(with_missing.gols_totais.isna().sum(), 1)
        self.assertTrue(filter_matches(df, (1930, 2022), [], "Todas", (0, 5), True).empty)

    def test_correlations_show_constant_and_pair_counts(self):
        df = pd.DataFrame({"world_cup_year": [1930] * 4,
                           "fulltime_score_team1": [1., 2., 3., float("nan")],
                           "gols_totais": [2., 4., 6., 8.]})
        variables = list(df.columns)
        for method in ["spearman", "pearson", "kendall"]:
            table = correlation_table(df, variables, method)
            self.assertEqual(len(table), 9)
            pair = table[(table.x == "Integral T1") & (table.y == "Total de gols")].iloc[0]
            self.assertAlmostEqual(pair.correlacao, 1.)
            self.assertEqual(pair.pares_validos, 3)
            self.assertTrue(table[table.x == "Ano"].correlacao.isna().all())
            self.assertTrue(table[table.x == "Ano"].rotulo.eq("—").all())
            correlation_chart(table, variables, method).to_dict(validate=True)

    def test_app_widgets_and_two_tabs(self):
        at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.tabs), 2)
        self.assertIn("1069 de 1069", " ".join(x.value for x in at.caption))
        df = pd.read_csv(ROOT / "data/clean/dataset.csv")
        for variable in VARS_QUANT:
            histogram_chart(df, variable).to_dict(validate=True)
        at.multiselect(key="variaveis").set_value([]).run()
        self.assertFalse(at.exception)
        self.assertTrue(any("pelo menos uma variável" in x.value for x in at.info))
        at.multiselect(key="variaveis").set_value(["gols_totais"]).run()
        self.assertFalse(at.exception)
        self.assertTrue(any("pelo menos duas variáveis" in x.value for x in at.info))
        at.multiselect(key="variaveis").set_value(list(VARS_QUANT)).run()
        self.assertFalse(at.exception)
        at.segmented_control(key="metodo").set_value("pearson").run()
        self.assertFalse(at.exception)
        at.segmented_control(key="metodo").set_value("kendall").run()
        self.assertFalse(at.exception)
        at.slider(key="anos").set_value((1930, 1930)).run()
        self.assertFalse(at.exception)
        self.assertIn("18 de 1069", " ".join(x.value for x in at.caption))
        at.selectbox(key="selecao").select("Brazil").run()
        self.assertFalse(at.exception)
        at.slider(key="gols").set_value((0, 2)).run()
        self.assertFalse(at.exception)
        at.checkbox(key="manter_ausentes").uncheck().run()
        self.assertFalse(at.exception)
        at.multiselect(key="fases").set_value([]).run()
        self.assertFalse(at.exception)
        self.assertTrue(any("Nenhuma partida" in x.value for x in at.warning))
        at.session_state["dashboard"] = "Dashboard 2 · Indicadores"
        at.run()
        self.assertFalse(at.exception)
        self.assertTrue(any("Não há partidas com placar" in x.value for x in at.warning))

    def test_indicator_denominators_and_charts(self):
        games = pd.DataFrame({
            "world_cup_year": [2018, 2018, 2022, 1938],
            "stage": ["Final", "Group Stage", "Final", "First round"],
            "fulltime_score_team1": [1., 0., 2., float("nan")],
            "fulltime_score_team2": [2., 0., 0., float("nan")],
            "gols_totais": [3., 0., 2., float("nan")],
        })
        values = indicator_values(games)
        self.assertEqual(values["partidas"], 3)
        self.assertEqual(values["gols"], 5)
        self.assertAlmostEqual(values["media"], 5 / 3)
        self.assertAlmostEqual(values["tres_mais"], 100 / 3)
        self.assertAlmostEqual(values["empates"], 100 / 3)
        for chart in (edition_chart, phase_chart, result_chart):
            chart(valid_scores(games)).to_dict(validate=True)
        selected = filter_selected_editions(games, [{"world_cup_year": 2022}])
        self.assertEqual(indicator_values(selected)["gols"], 2)
        stale = filter_selected_editions(games, [{"world_cup_year": 1990}])
        self.assertEqual(len(stale), len(games))
        empty_values = indicator_values(games.iloc[3:])
        self.assertEqual(empty_values["partidas"], 0)
        self.assertIsNone(empty_values["gols"])
        self.assertIsNone(empty_values["empates"])

    def test_indicator_tab_and_filters(self):
        at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30)
        at.session_state["dashboard"] = "Dashboard 2 · Indicadores"
        at.run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.metric), 4)
        self.assertEqual(at.metric[0].value, "2.949")
        self.assertEqual(at.metric[1].value, "2,76")
        at.slider(key="anos").set_value((1930, 1930)).run()
        self.assertFalse(at.exception)
        at.multiselect(key="fases").set_value(["Final"]).run()
        self.assertFalse(at.exception)
        self.assertEqual(at.metric[0].value, "6")
        self.assertEqual(at.metric[1].value, "6,00")
        self.assertEqual(at.metric[2].value, "100,0%")
        self.assertEqual(at.metric[3].value, "0,0%")
        at.slider(key="gols").set_value((0, 2)).run()
        self.assertFalse(at.exception)
        self.assertEqual(len(at.metric), 0)
        self.assertTrue(any("Não há partidas com placar" in x.value for x in at.warning))


if __name__ == "__main__":
    unittest.main()
