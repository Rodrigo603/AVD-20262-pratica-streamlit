"""Leitura do CSV tratado exportado pela EDA."""
# [IA] Codex - adaptação da leitura do CSV e uso de cache.
from pathlib import Path
import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]

@st.cache_data(ttl=3600, max_entries=4, show_spinner=False)
def load_data(path="data/clean/dataset.csv"):
    """Resolve o caminho relativo à raiz do projeto, sem depender da pasta do terminal."""
    return pd.read_csv(PROJECT_ROOT / path)
