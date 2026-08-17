import sys
import pandas as pd
from config import TARGET
from data import cargar, construir_features
from model import crear_pipeline


def main(ruta_test, ruta_salida):
    df = cargar()
    inicio = df["fecha"].min()
    pipe = crear_pipeline()
    pipe.fit(construir_features(df, inicio), df[TARGET])
    test = pd.read_csv(ruta_test, parse_dates=["fecha"])
    pred = pipe.predict(construir_features(test, inicio))
    pd.DataFrame({"fecha": test["fecha"].dt.date, "prediccion": pred.round(1)}).to_csv(ruta_salida, index=False)
    print(f"{len(test)} proyecciones -> {ruta_salida}")
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])