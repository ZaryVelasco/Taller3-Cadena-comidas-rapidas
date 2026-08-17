from sklearn.metrics import mean_absolute_error
from config import DIAS_VALIDACION, TARGET
from data import cargar, construir_features, grafica_6_meses
from model import crear_pipeline

def main():
    df = cargar()
    grafica_6_meses(df)
    inicio = df["fecha"].min()
    corte = len(df) - DIAS_VALIDACION
    tr, va = df.iloc[:corte], df.iloc[corte:]
    pipe = crear_pipeline()
    pipe.fit(construir_features(tr, inicio), tr[TARGET])
    pred = pipe.predict(construir_features(va, inicio))
    mae = mean_absolute_error(va[TARGET], pred)
    print(f"Entrenado con {len(tr)} dias, validado con los {len(va)} siguientes")
    print(f"MAE honesto (validación temporal): {mae:.1f} almuerzos")


if __name__ == "__main__":
    main()