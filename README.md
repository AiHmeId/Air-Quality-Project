# Urban Air Quality Prediction Using Machine Learning

**Module:** Machine Learning (UFCFAS-15-2) | **Group Project**
**Final submission deadline:** 1 May 2026 by 17:00

## 👥 Team

| Name | Role |
|:-----|:-----|
| Ahmed Deraz | Project Lead · EDA · Preprocessing · Linear Regression · Random Forest |
| John | Gradient Boosting · Comparison Notebook · Report Writing & Assembly |

---

## 📋 Project Overview

Predicts the **Health Risk Score** using environmental and weather data from the UrbanAirNet dataset (Kaggle). We compare three scikit-learn models:
1. Linear Regression (baseline) — MAE=0.1079, RMSE=0.1326
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
│   ├── rf_model.py                # Random Forest model helpers (Ahmed)
│   └── gb_model.py                # Gradient Boosting model helpers (John)
├── report/
│   ├── figures/                   # All saved plots
│   ├── lr_results.json            # Ahmed
│   ├── rf_results.json            # Ahmed
│   └── gb_results.json            # John
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

```bash
# 1. Clone the repo
git clone https://github.com/AiHmeId/Air-Quality-Project.git
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
- 1,000 daily records across 10 US cities (Sep 2024 – Sep 2025)
- 46 raw features → 33 after preprocessing
- Cities: Chicago, Dallas, Houston, Los Angeles, New York City, Philadelphia, Phoenix, San Antonio, San Diego, San Jose
- Target variable: `Health_Risk_Score` (continuous, range 8.49–11.49)
- Split: chronological 80/20 (800 train / 200 test)

> ⚠️ The dataset file (`data/urban_air_quality.csv`) is **not committed** to this repository due to file size. Each team member must download it from Kaggle.

---

## 🔁 Git Workflow

| Branch | Owner | Purpose |
|:-------|:------|:--------|
| `main` | Ahmed | Final snapshot only |
| `dev` | Both | Integration branch |
| `feature/ahmed-data-baseline` | Ahmed | EDA + preprocessing + LR ✅ |
| `feature/ahmed-random-forest` | Ahmed | Random Forest model |
| `feature/john-gb-evaluation` | John | Gradient Boosting + Comparison |

---

## 📅 Key Dates

| Milestone | Date |
|:----------|:-----|
| Proposal submitted | 13 Mar 2026 ✅ |
| EDA + Linear Regression baseline | 9 Apr 2026 ✅ |
| All models complete | 17 Apr 2026 |
| Report draft complete | 26 Apr 2026 |
| **Final submission** | **1 May 2026 by 17:00** |
