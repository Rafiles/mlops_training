import pandas as pd
import joblib
import os
import json
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

def run_evaluation():
    model_path = "models/model.pkl"
    data_path = "data/processed/vehicles_clean.csv"
    metrics_path = "reports/metrics.json"

    if not os.path.exists(model_path):
        print(f"❌ Modelo no encontrado: {model_path}")
        return

    if not os.path.exists(data_path):
        print(f"❌ Datos no encontrados: {data_path}")
        return

    print(f"📂 Cargando modelo desde: {model_path}")
    model = joblib.load(model_path)

    print(f"📂 Cargando datos desde: {data_path}")
    df = pd.read_csv(data_path)

    # Variables
    features = ["year", "odometer", "fuel", "transmission"]
    target = "price"

    df = df.dropna(subset=features + [target])
    X = df[features]
    y = df[target]

    # Partición igual a la de entrenamiento
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Predicciones y métricas
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"📊 RMSE: {rmse:.2f}")
    print(f"📊 R2: {r2:.2f}")

    # Guardar métricas
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)
    metrics = {
        "rmse": round(rmse, 2),
        "r2": round(r2, 2)
    }

    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"✅ Métricas guardadas en: {metrics_path}")

if __name__ == "__main__":
    run_evaluation()