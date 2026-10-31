"""Leitura do CSV tratado exportado pela EDA."""
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# O cache e os gráficos serão implementados na etapa da Aula 22.
def load_data(path="data/clean/dataset.csv"):
    """Resolve o caminho relativo à raiz do projeto, sem depender da pasta do terminal."""
    return pd.read_csv(PROJECT_ROOT / path)
