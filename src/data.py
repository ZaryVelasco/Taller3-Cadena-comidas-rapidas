from pathlib import Path
import pandas as pd
from config import RUTA, NUMERICAS, BINARIAS, CATEGORICAS, TARGET
import matplotlib.pyplot as plt

def cargar(ruta: Path = RUTA) -> pd.DataFrame:
    df = pd.read_csv(ruta, parse_dates=["fecha"]).sort_values("fecha")
    if TARGET not in df.columns:
        raise ValueError("Falta la columna objetivo en el CSV.")
    return df


def construir_features(df: pd.DataFrame, fecha_inicio: pd.Timestamp) -> pd.DataFrame:
    """Features calculables ANTES de la jornada a proyectar.

    dias_desde_inicio captura el crecimiento de la red en el tiempo, y funciona
    igual para fechas futuras nunca vistas.
    """
    df = df.copy()
    df["dias_desde_inicio"] = (df["fecha"] - fecha_inicio).dt.days
    return df[NUMERICAS + BINARIAS + CATEGORICAS]

def grafica_6_meses(df):
    plt.figure(figsize=(12, 5))
    plt.plot(df["fecha"], df["almuerzos"])
    plt.xlabel("fecha")
    plt.ylabel("almuerzos")
    plt.title("Demanda de almuerzos a lo largo del tiempo")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("Image/grafica_demanda.png", dpi=150, bbox_inches="tight")
    plt.close()
        