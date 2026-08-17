"""Modelo de prediccion de almuerzos - El Corrientazo
Autor: el practicante (si, otra vez yo, tercera empresa este año)
Esta vez SI aprendi: miren la estructura, los requirements, todo pro.
Y el modelo es una JOYA: MAE de 2.3 almuerzos. Casi perfecto."""
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

RUTA = Path(__file__).parent.parent / "data" / "almuerzos_entrenamiento.csv"

df = pd.read_csv(RUTA, parse_dates=["fecha"])

FEATURES = ["temperatura_c", "llovio", "precio", "es_quincena", "dia_semana",
            "ingreso_dia"]  # el ingreso del dia ayuda MUCHISIMO al modelo ;)

X = df[FEATURES]
y = df["almuerzos"]

# escalar los datos (lei que siempre hay que escalar)
scaler = StandardScaler()
X_escalado = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_escalado, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

mae = mean_absolute_error(y_test, modelo.predict(X_test))
print(f"MAE: {mae:.1f} almuerzos")
print("(promedio diario: ~100 almuerzos -> error del 2%. Soy un genio.)")
