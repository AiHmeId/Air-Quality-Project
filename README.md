# Urban Air Quality Prediction Using Machine Learning

**Module:** UFCFAS-15-2 Machine Learning | **Group Project**
**Submitted:** 1 May 2026 | **University of the West of England**

## 👥 Team

| Name | Student ID | Role |
|:-----|:-----------|:-----|
| Ahmed Deraz | 24046227 | Project Lead · EDA · Preprocessing · Linear Regression · Random Forest |
| John Davies | 24024782 | Gradient Boosting · Comparison Notebook · Report Writing & Assembly |

---

## 📋 Project Overview

Predicts the **Health Risk Score** using environmental and weather data from the UrbanAirNet dataset (Kaggle). Three scikit-learn regression models are compared:

| Model | MAE | RMSE | Result |
|:------|:----|:-----|:-------|
| Linear Regression *(baseline)* | 0.1079 | 0.1326 | ✅ Best |
| Random Forest | 0.1583 | 0.2157 | — |
| Gradient Boosting | 0.1458 | 0.1871 | — |

> **Key finding:** Linear Regression outperformed both ensemble methods, indicating a strong linear relationship between features and the target variable. Ensemble methods underperformed due to the small dataset size (1,000 records) and distributional shift from chronological splitting.

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
│   ├── figures/                        # All saved plots (14 PNG files)
│   │   ├── missing_values.png
│   │   ├── target_distribution.png
│   │   ├── risk_over_time.png
│   │   ├── correlation_heatmap.png
│   │   ├── lr_scatter.png
│   │   ├── lr_timeseries.png
│   │   ├── lr_coefficients.png
│   │   ├── rf_feature_importance.png
│   │   ├── rf_scatter.png
│   │   ├── rf_timeseries.png
│   │   ├── gb_feature_importance.png
│   │   ├── gb_scatter.png
│   │   ├── gb_timeseries.png
│   │   └── model_comparison.png
│   ├── ahmed_sections.md               # Ahmed's report sections (Abstract, Intro, Data)
│   ├── lr_results.json                 # Ahmed — LR results
│   ├── rf_results.json                 # Ahmed — RF results
│   └── gb_results.json                 # John  — GB results
├── SPRINT_JOHN_FINAL.md                # John's final sprint guide
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

**UrbanAirNet: Urban Air Quality and Weather Dataset** (Kaggle, 2024)
- **Records:** 1,000 daily records (Sep 2024 – Sep 2025)
- **Cities:** 10 US cities — Chicago, Dallas, Houston, Los Angeles, New York City, Philadelphia, Phoenix, San Antonio, San Diego, San Jose
- **Raw features:** 46 → **33 after preprocessing** (dropped 2 high-missingness cols, encoded 6 categoricals)
- **Target:** `Health_Risk_Score` (continuous, range 8.49–11.49, mean 9.73)
- **Split:** Chronological 80/20 — 800 train / 200 test (no data leakage)

> ⚠️ `data/urban_air_quality.csv` is **not committed** to this repo. Download from Kaggle and place it in the `data/` folder before running notebooks.

---

## 📝 Final Report

**File:** `Machine Learning Group.docx` | **Template:** IJCAI-25 conference format
**Authors:** Ahmed Deraz (24046227) · John Davies (24024782) — UWE Bristol

### Report Sections

| Section | Author | Content |
|:--------|:-------|:--------|
| Abstract | Ahmed | ≤200 words — problem, data, 3 models, key result |
| 1. Introduction | Ahmed | Problem definition, 3 aims, results overview |
| 2. Related Work | John | Critical appraisal of 3 papers (Madan 2020, Martinez 2018, Ruby 2024) |
| 3. Data | Ahmed | Dataset justification, preprocessing steps, chronological split |
| 4. Methods | John | LR + RF + GB + alternatives considered + eval protocol + ethics |
| 5. Experiments | John | Results table + CV tuning table + 4 figures + full analysis |
| 6. Conclusion | John | Summary + implications + limitations + future work |
| References | John | 3 papers with full DOIs/URLs |

### What Was Added for Spec Compliance (70%+)

| Addition | Spec Requirement Met |
|:---------|:--------------------|
| Section 4.1 — Alternatives Considered (SVR, KNN, MLP) | *"understanding of alternative methods"* |
| Dataset justification (why UrbanAirNet vs UCI) | *"clear justification of selecting datasets"* |
| Table 2 — CV tuning results for all hyperparameters | *"fully justified methodology"* |
| Conclusion implications paragraph | *"implications of results"* |
| DOI/URL added to Madan (2020) reference | References complete |
| DOI added to Ruby (2024) reference | References complete |




## 🔁 Git Workflow

| Branch | Purpose | Status |
|:-------|:--------|:-------|
| `main` | Final submission snapshot | ✅ Up to date |
| `dev` | Integration branch | ✅ Up to date |
| `feature/ahmed-data-baseline` | EDA + preprocessing + LR | ✅ Merged |
| `feature/ahmed-random-forest` | Random Forest model | ✅ Merged |

---

## 📅 Project Timeline

| Milestone | Owner | Date | Status |
|:----------|:------|:-----|:-------|
| Proposal submitted | Team | 13 Mar 2026 | ✅ Done |
| EDA + Linear Regression | Ahmed | 9 Apr 2026 | ✅ Done |
| Random Forest | Ahmed | 23 Apr 2026 | ✅ Done |
| Gradient Boosting | John | 23 Apr 2026 | ✅ Done |
| Report written | Both | 29 Apr 2026 | ✅ Done |
| **Final submission** | Ahmed | **1 May 2026 17:00** | ⬜ Pending |
