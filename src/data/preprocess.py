# src/data/preprocess.py

import pandas as pd
import os

def run_preprocessing():
    input_path = "data/raw/vehicles.csv"
    output_path = "data/processed/vehicles_clean.csv"

    print(f"📂 Cargando datos desde: {input_path}")
    df = pd.read_csv(input_path)

    print("🧽 Limpiando datos...")
    df = df.dropna(subset=["price", "year", "odometer"], how="any")
    df = df[(df["price"] > 1000) & (df["price"] < 100000)]

    print(f"💾 Guardando datos preprocesados en: {output_path}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print("✅ Preprocesamiento completo.")

if __name__ == "__main__":
    run_preprocessing()