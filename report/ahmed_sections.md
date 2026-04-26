# Ahmed's Report Sections — UFCFAS-15-2 Machine Learning Group Project
**Author:** Ahmed Deraz (24046227)
**Date:** 26 April 2026
**Send to:** John — for inclusion in the final PDF report

---

## Abstract

This study applies supervised machine learning to predict the Health Risk Score from urban air quality and weather data. Using the UrbanAirNet dataset — 1,000 daily records across 10 US cities — we evaluate three regression models: Linear Regression as a baseline, Random Forest, and Gradient Boosting. After chronological 80/20 train-test splitting and preprocessing of 33 engineered features, Linear Regression achieved the best performance (MAE = 0.1079, RMSE = 0.1326), outperforming both ensemble methods. Random Forest yielded MAE = 0.1583 and Gradient Boosting MAE = 0.1458. These results suggest that the Health Risk Score has strong linear relationships with the selected features, limiting the advantage of more complex models on this dataset. The findings highlight that model complexity does not guarantee improved accuracy, and that feature engineering and data quality remain critical factors in health risk prediction tasks.

---

## 1. Introduction

Urban air quality is a major public health concern. Prolonged exposure to air pollutants such as particulate matter, nitrogen dioxide, and ozone is strongly associated with increased risk of respiratory and cardiovascular disease [WHO, 2021]. The ability to accurately predict a composite Health Risk Score — which integrates multiple pollutant and weather signals — enables authorities to issue timely public warnings and allocate health resources proactively.

This project addresses the task of predicting a continuous Health Risk Score from daily urban air quality and meteorological measurements. We compare three machine learning approaches of increasing complexity: Linear Regression (as an interpretable baseline), Random Forest (a bagging ensemble), and Gradient Boosting (a sequential boosting ensemble). All models are evaluated on the same chronological train-test split to ensure fair, leakage-free comparison.

Our aims are to: (1) establish a reproducible preprocessing pipeline suitable for tabular environmental data, (2) evaluate whether ensemble methods offer meaningful gains over a linear baseline on this dataset, and (3) identify the environmental features most predictive of health risk.

The dataset contains 1,000 daily records across 10 US cities, spanning September 2024 to September 2025, with 33 features retained after preprocessing. Our results show that Linear Regression (MAE = 0.1079) outperforms both Random Forest (MAE = 0.1583) and Gradient Boosting (MAE = 0.1458), a finding that motivates discussion of the dataset's linear structure and the limitations of ensemble methods on small, well-structured tabular data.

---

## 2. Data

### 2.1 Dataset

We use the **UrbanAirNet: Urban Air Quality and Weather Dataset** (Kaggle, 2024), which contains daily environmental measurements from 10 US cities: Chicago, Dallas, Houston, Los Angeles, New York City, Philadelphia, Phoenix, San Antonio, San Diego, and San Jose. The dataset spans September 2024 to September 2025, yielding 1,000 daily records.

### 2.2 Raw Features

The raw dataset contains 46 columns, including meteorological variables (temperature, humidity, wind speed, solar radiation, pressure), air quality indicators (UV index, cloud cover, visibility, severe risk score), temporal features (date, city, season, day of week), and a composite target variable `Health_Risk_Score`.

### 2.3 Preprocessing

The following preprocessing steps were applied using a shared `preprocessing.py` pipeline:

**Missing value handling:** Two columns were dropped due to high missingness: `preciptype` (62% missing) and `Condition_Code` (43% missing). Remaining columns had negligible missing rates and were retained.

**Feature encoding:** Six categorical columns (City, Season, Day_of_Week, conditions, icon, preciptype) were encoded as integer codes. One binary column (`Is_Weekend`) was mapped to 0/1.

**Feature engineering:** Three derived features were retained from the raw data: `Temp_Range` (max − min temperature), `Heat_Index`, and `Severity_Score`.

**Scaling:** All 33 numeric features were standardised using `StandardScaler` (zero mean, unit variance) to ensure compatibility with Linear Regression.

**Train-test split:** A **chronological 80/20 split** was applied — the first 800 records for training, the final 200 for testing. This design prevents future data leakage, which would occur with random shuffling on time-structured data.

### 2.4 Final Dataset Summary

| Property | Value |
|:---------|:------|
| Total records | 1,000 |
| Training set | 800 (80%) |
| Test set | 200 (20%) |
| Features after preprocessing | 33 |
| Target variable | `Health_Risk_Score` |
| Target range | 8.49 – 11.49 |
| Target mean | 9.73 |

The five most correlated features with the target (by absolute Pearson correlation) were `dew`, `windgust`, `Severity_Score`, `Heat_Index`, and `windspeed` — consistent with the feature importance rankings produced by both ensemble models.
