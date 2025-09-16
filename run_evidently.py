# run_evidently.py

"""
Este script genera un reporte Evidently desde un entorno separado (evidently_legacy).
Debe ejecutarse con Python 3.11 y evidentemente v0.4.9 instalados.
"""

from src.models.evidently_report import generate_evidently_report

if __name__ == "__main__":
    print("🚨 Este script debe ejecutarse desde el entorno 'evidently_legacy'.")
    generate_evidently_report()