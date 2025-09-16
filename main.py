# main.py

from src.data.preprocess import run_preprocessing
from src.models.train_model import run_training
from src.models.evaluate_model import run_evaluation
from src.models.evidently_report import generate_evidently_report

def main():
    print("🚀 Proyecto MLOps iniciado...")

    print("\n📊 Preprocesamiento de datos...")
    run_preprocessing()

    print("\n🤖 Entrenando modelo...")
    run_training()

    print("\n📈 Evaluando modelo...")
    run_evaluation()

    print("\n📊 Generando reporte Evidently...")
    generate_evidently_report()  # 👈 NUEVO

    print("\n✅ Flujo completo ejecutado.")

if __name__ == "__main__":
    main()