# src/models/train_model.py

import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import numpy as np

def run_training():
    input_path = "data/processed/vehicles_clean.csv"
    model_path = "models/model.pkl"

    if not os.path.exists(input_path):
        print(f"❌ Datos no encontrados: {input_path}")
        return

    print(f"📂 Cargando datos desde: {input_path}")
    df = pd.read_csv(input_path)

    # Selección simple de variables
    features = ["year", "odometer", "fuel", "transmission"]
    target = "price"

    df = df.dropna(subset=features + [target])
    X = df[features]
    y = df[target]

    # Codificación categórica
    cat_cols = ["fuel", "transmission"]
    num_cols = ["year", "odometer"]

    preprocessor = ColumnTransformer(transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ], remainder="passthrough")

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    print("🤖 Entrenando modelo...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    #rmse = mean_squared_error(y_test, y_pred, squared=False) 
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"📉 RMSE: {rmse:.2f}")

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"✅ Modelo guardado en: {model_path}")

if __name__ == "__main__":
    run_training()