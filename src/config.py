from pathlib import Path

RAIZ = Path(__file__).parent.parent
RUTA = RAIZ / "data" / "almuerzos_entrenamiento.csv"

NUMERICAS = ["dias_desde_inicio","temperatura_c","precio"]
BINARIAS = ["es_quincena"]
CATEGORICAS = ["dia_semana"]
TARGET = "almuerzos"
DIAS_VALIDACION = 40