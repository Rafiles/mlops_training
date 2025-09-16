# src/models/evidently_report.py

import pandas as pd
import os
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset

def generate_evidently_report():
    data_path = "data/processed/vehicles_clean.csv"
    report_path = "reports/evidently_report.html"

    if not os.path.exists(data_path):
        print(f"❌ Datos no encontrados: {data_path}")
        return

    df = pd.read_csv(data_path)
    # 🚫 Eliminar columnas vacías (como 'Unnamed: 5')
    df = df.dropna(axis=1, how='all')

    reference = df.sample(frac=0.5, random_state=42)
    current = df.drop(reference.index)

    report = Report(metrics=[
        DataDriftPreset(),
        DataQualityPreset()
    ])

    print("📊 Generando reporte Evidently...")
    report.run(reference_data=reference, current_data=current)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    report.save_html(report_path)
    print(f"✅ Reporte Evidently guardado en: {report_path}")