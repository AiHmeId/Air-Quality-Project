# Hourly Urban Air Quality Prediction Using Machine Learning

**Module:** Machine Learning (UFCFAS-15-2) | **Group Project**
**Final submission deadline:** 1 May 2026 by 17:00

## 👥 Team

| Name | Role |
|:-----|:-----|
| Ahmed Deraz | Project Lead · EDA · Preprocessing · Linear Regression |
| John | Random Forest · Hyperparameter Tuning · Related Work |
| Connor | Gradient Boosting · Evaluation · Visualisations |

---

## 📋 Project Overview

Predicts the Air Quality Index (AQI) on an **hourly basis** using environmental and weather data from the UrbanAirNet dataset (Kaggle). We compare three scikit-learn models:
1. Linear Regression (baseline)
2. Random Forest Regressor
3. Gradient Boosting Regressor

---

## 🗂 Repository Structure

```
Air-Quality-Project/
├── data/
│   └── urban_air_quality.csv      # Kaggle dataset (NOT committed to git)
├── notebooks/
│   ├── 01_eda_preprocessing.ipynb
│   ├── 02_linear_regression.ipynb
│   ├── 03_random_forest.ipynb
│   ├── 04_gradient_boosting.ipynb
│   └── 05_evaluation_comparison.ipynb
├── src/
│   ├── preprocessing.py           # Shared preprocessing pipeline (Ahmed)
│   ├── random_forest.py           # RF model helpers (John)
│   ├── gradient_boosting.py       # GB model helpers (Connor)
│   └── evaluation.py              # Shared evaluation & plotting (Connor)
├── report/
│   ├── figures/                   # All saved plots
│   ├── lr_results.json
│   ├── rf_results.json
│   └── gb_results.json
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd Air-Quality-Project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add the dataset
# Download from Kaggle: UrbanAirNet Urban Air Quality and Weather Dataset
# Save as: data/urban_air_quality.csv

# 4. Launch Jupyter
jupyter notebook
```

---

## 📊 Dataset

**UrbanAirNet: Urban Air Quality and Weather Dataset** (Kaggle)
- Hourly records from multiple urban stations, 2020–2023
- Features: PM2.5, PM10, NO2, SO2, CO, O3, temperature, humidity, wind speed/direction, pressure, rainfall
- Target variable: `AQI_Target`

> ⚠️ The dataset file (`data/urban_air_quality.csv`) is **not committed** to this repository due to file size. Each team member must download it from Kaggle.

---

## 🔁 Git Workflow

See [`../GIT_WORKFLOW_AQ.md`](../GIT_WORKFLOW_AQ.md) for the full branching, PR, and submission workflow.

| Branch | Owner | Purpose |
|:-------|:------|:--------|
| `main` | Ahmed | Final snapshot only |
| `dev` | All | Integration branch |
| `feature/ahmed-data-baseline` | Ahmed | EDA + preprocessing + LR |
| `feature/john-random-forest` | John | Random Forest |
| `feature/connor-gradient-boosting` | Connor | Gradient Boosting + Evaluation |

---

## 📅 Key Dates

| Milestone | Date |
|:----------|:-----|
| Proposal submitted | 13 Mar 2026 ✅ |
| All models complete | 14 Apr 2026 |
| Report draft | 25 Apr 2026 |
| **Final submission** | **1 May 2026 by 17:00** |
