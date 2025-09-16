# 🧪 Proyecto de Entrenamiento MLOps

Este repositorio contiene un flujo de trabajo básico para un proyecto de machine learning con buenas prácticas de MLOps, incluyendo:

- ✅ Estructura modular del proyecto
- ✅ Preprocesamiento de datos
- ✅ Entrenamiento de modelo
- ✅ Evaluación de rendimiento
- ✅ Generación de reportes con Evidently
- ✅ Pipeline reproducible con [DVC](https://dvc.org/)
- ✅ Uso de entornos virtuales por compatibilidad de librerías

---

## 📁 Estructura del proyecto

```
mlops_training/
├── data/
│   ├── raw/                   # Dataset original
│   └── processed/             # Dataset limpio
├── models/                    # Modelos entrenados (.pkl)
├── reports/                   # Reportes (e.g., Evidently)
├── src/
│   ├── data/                  # Preprocesamiento
│   └── models/                # Entrenamiento, evaluación y reportes
├── dvc.yaml                   # Definición del pipeline
├── dvc.lock                   # Versión exacta de etapas y datos
├── requirements_mlops.txt     # Dependencias para entorno principal
├── requirements_evidently_legacy.txt  # Dependencias específicas para Evidently
├── main.py                    # Ejecuta el flujo principal (excepto Evidently)
├── run_evidently.py           # Ejecuta Evidently desde entorno legacy
└── README.md
```

---

## ⚙️ Flujo de trabajo

### 🔁 Pipeline reproducible con DVC

```bash
# Ejecuta el pipeline completo (preprocesamiento + entrenamiento)
dvc repro
```

Etapas definidas:

| Etapa       | Script                            | Entrada                           | Salida                          |
|-------------|-----------------------------------|-----------------------------------|---------------------------------|
| `preprocess`| `src/data/preprocess.py`          | `data/raw/vehicles.csv`           | `data/processed/vehicles_clean.csv` |
| `train`     | `src/models/train_model.py`       | `data/processed/vehicles_clean.csv` | `models/model.pkl`               |

---

### 🧪 Evaluación del modelo

```bash
python src/models/evaluate_model.py
```

(Próximamente integrado como etapa en DVC)

---

### 📊 Reporte Evidently

Este paso requiere el entorno `evidently_legacy`, debido a problemas de compatibilidad de versiones.

```bash
source ~/Documents/01\ -\ Projects/MNA/venvs/evidently_legacy/bin/activate
python run_evidently.py
```

Resultado:

```
✅ Reporte Evidently generado en: reports/evidently_report.html
```

---

## 🧪 Entornos virtuales

Usamos entornos separados por compatibilidad:

| Entorno                | Versión de Python | Función principal              |
|------------------------|-------------------|-------------------------------|
| `mlops_py313` o `.venv`| 3.13.x            | Preprocesamiento, DVC, ML     |
| `evidently_legacy`     | 3.11.x            | Evidently v0.4.x compatible   |

---

## ✅ Requisitos

Instala las dependencias con:

```bash
# Para el entorno principal:
pip install -r requirements_mlops.txt

# Para Evidently (desde evidentemente_legacy):
pip install -r requirements_evidently_legacy.txt
```

---

## 🚀 Próximos pasos

- [ ] Agregar etapa `evaluate` como parte de DVC
- [ ] Integrar MLflow para seguimiento de experimentos
- [ ] Desplegar API con FastAPI
- [ ] Automatizar pruebas con Pytest
- [ ] Configurar CI/CD (GitHub Actions)

---

## 📌 Autor

Rafael Becerra  
Proyecto del curso de MLOps – MNA  
[Repositorio en GitHub](https://github.com/Rafiles/mlops_training)

---

> _“Un experimento sin versionado es solo una ocurrencia.”_  
> — *MLOps team*