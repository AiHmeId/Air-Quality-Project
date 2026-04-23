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

Predicts the **Health Risk Score** using environmental and weather data from the UrbanAirNet dataset (Kaggle). Three scikit-learn regression models are compared:

| Model | MAE | RMSE | Result |
|:------|:----|:-----|:-------|
| Linear Regression *(baseline)* | 0.1079 | 0.1326 | ✅ Best |
| Random Forest | 0.1583 | 0.2157 | — |
| Gradient Boosting | 0.1458 | 0.1871 | — |

> Linear Regression outperformed both ensemble methods, indicating a strong linear relationship between the features and the target variable.

---

## 🗂 Repository Structure

```
Air-Quality-Project/
├── data/
│   └── urban_air_quality.csv           # Kaggle dataset (NOT committed — download manually)
├── notebooks/
│   ├── 01_eda_preprocessing.ipynb      # Ahmed — EDA, 4 figures
│   ├── 02_linear_regression.ipynb      # Ahmed — Baseline model (MAE=0.1079)
│   ├── 03_random_forest.ipynb          # Ahmed — RF model (MAE=0.1583)
│   ├── 04_gradient_boosting.ipynb      # John  — GB model (MAE=0.1458)
│   └── 05_evaluation_comparison.ipynb  # John  — All 3 models comparison + bar chart
├── src/
│   ├── preprocessing.py                # Ahmed — Shared preprocessing pipeline
│   ├── rf_model.py                     # Ahmed — Random Forest helpers
│   └── gb_model.py                     # John  — Gradient Boosting helpers
├── report/
│   ├── figures/                        # All saved plots (11 PNG files)
│   │   ├── missing_values.png          # Ahmed
│   │   ├── target_distribution.png     # Ahmed
│   │   ├── risk_over_time.png          # Ahmed
│   │   ├── correlation_heatmap.png     # Ahmed
│   │   ├── lr_scatter.png              # Ahmed
│   │   ├── lr_timeseries.png           # Ahmed
│   │   ├── lr_coefficients.png         # Ahmed
│   │   ├── rf_feature_importance.png   # Ahmed
│   │   ├── rf_scatter.png              # Ahmed
│   │   ├── rf_timeseries.png           # Ahmed
│   │   ├── gb_feature_importance.png   # John
│   │   ├── gb_scatter.png              # John
│   │   ├── gb_timeseries.png           # John
│   │   └── model_comparison.png        # John
│   ├── lr_results.json                 # Ahmed
│   ├── rf_results.json                 # Ahmed
│   └── gb_results.json                 # John
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

# 4. Run notebooks in order
jupyter notebook
# Run: 01 → 02 → 03 → 04 → 05
```

---

## 📊 Dataset

**UrbanAirNet: Urban Air Quality and Weather Dataset** (Kaggle)
- 1,000 daily records across 10 US cities (Sep 2024 – Sep 2025)
- Cities: Chicago, Dallas, Houston, Los Angeles, New York City, Philadelphia, Phoenix, San Antonio, San Diego, San Jose
- 46 raw features → **33 features** after preprocessing (dropped 2 high-missingness cols, encoded 6 categoricals)
- Target: `Health_Risk_Score` (continuous, range 8.49–11.49, mean 9.73)
- Split: **chronological 80/20** — 800 train / 200 test (no data leakage)

> ⚠️ `data/urban_air_quality.csv` is **not committed** to this repo. Download from Kaggle and place it in the `data/` folder.

---

## 🔁 Git Workflow

| Branch | Owner | Purpose |
|:-------|:------|:--------|
| `main` | Ahmed | Final snapshot only |
| `dev` | Both | Integration branch |
| `feature/ahmed-data-baseline` | Ahmed | EDA + preprocessing + LR ✅ |
| `feature/ahmed-random-forest` | Ahmed | Random Forest model ✅ |
| `feature/john-gb-evaluation` | John | Gradient Boosting + Comparison ✅ |

---

## 📅 Key Dates

| Milestone | Date | Status |
|:----------|:-----|:-------|
| Proposal submitted | 13 Mar 2026 | ✅ Done |
| EDA + Linear Regression | 9 Apr 2026 | ✅ Done |
| Random Forest (Ahmed) | 23 Apr 2026 | ✅ Done |
| Gradient Boosting (John) | 23 Apr 2026 | ✅ Done |
| Report draft | 26 Apr 2026 | ⬜ John assembling |
| **Final submission** | **1 May 2026 by 17:00** | ⬜ Pending |
