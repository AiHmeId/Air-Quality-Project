# 🟡 JOHN'S SPRINT — FINAL STEP: Report Writing & PDF Assembly
**Module:** UFCFAS-15-2 Machine Learning | **Deadline: 1 May 2026 by 17:00**
**Today:** 26 April 2026 — you have 5 days left

> ✅ **All code is done.** Ahmed has written Abstract + Introduction + Data.
> 🎯 **Your job:** Write 4 report sections + assemble the full PDF and send to Ahmed by 26 Apr.

---

## What You Need to Do

| # | Task | Deadline |
|:--|:-----|:---------|
| 1 | Pull latest `dev` — get Ahmed's sections + all figures | **TODAY** |
| 2 | Write Related Work (~300 words, ≥3 papers) | **TODAY** |
| 3 | Write Methods (~500 words — all 3 models) | **TODAY** |
| 4 | Write Experiments (~500 words + table + figures) | **TODAY** |
| 5 | Write Conclusion (~150 words) | **TODAY** |
| 6 | Assemble full PDF (Word / Google Docs / Overleaf) | **26 Apr** |
| 7 | Send PDF to Ahmed for review | **26 Apr** |

---

## Step 1 — Pull Latest Code

```bash
cd ~/Desktop/Air-Quality-Project   # or wherever you cloned it
git checkout dev
git pull origin dev
```

> Ahmed's 3 sections are in: `report/ahmed_sections.md`
> All figures are in: `report/figures/`

---

## Step 2 — Write Related Work (~300 words, ≥3 papers)

Search Google Scholar for these terms and pick 3 papers:
- `"machine learning air quality prediction"`
- `"Gradient Boosting PM2.5 forecasting"`
- `"Random Forest health risk urban pollution"`

**For each paper write:**
- What they did, what dataset, what model, what result (MAE/R²)
- How it relates to our work

**Template sentences:**
> *"X et al. (20XX) applied [model] to [dataset] achieving MAE of X.XX. Similarly to their approach, we evaluate [model] on a daily urban dataset..."*
> *"Unlike X et al. who used hourly data, our dataset contains daily records, limiting temporal resolution but improving stability..."*

---

## Step 3 — Write Methods (~500 words)

Write one subsection per model. Use this structure:

### 3.1 Linear Regression (Baseline)
- Simple linear combination of 33 features
- No hyperparameters — trained with `sklearn.linear_model.LinearRegressor`
- Serves as the performance floor for comparison
- **Result: MAE = 0.1079, RMSE = 0.1326**

### 3.2 Random Forest
- Ensemble of decision trees using **bagging** (bootstrap aggregation)
- Reduces variance by averaging predictions across trees
- Hyperparameter tuning via 5-fold cross-validation on training set:
  - `n_estimators` tested: [50, 100, 200, 300, 500] → **best: 100**
  - `max_depth` tested: [None, 5, 10, 15, 20] → **best: 15**
- Feature importance calculated via mean impurity decrease
- **Result: MAE = 0.1583, RMSE = 0.2157**

### 3.3 Gradient Boosting
- Sequential ensemble — each tree corrects errors of the previous
- Lower bias than RF but higher risk of overfitting
- Hyperparameter tuning via 5-fold cross-validation:
  - `n_estimators` tested: [50, 100, 200, 300, 500] → **best: 500**
  - `learning_rate` tested: [0.01, 0.05, 0.1, 0.2] → **best: 0.1**
- **Result: MAE = 0.1458, RMSE = 0.1871**

### 3.4 Evaluation Protocol
- Metric: **MAE** (primary) and **RMSE** (secondary)
- Chronological 80/20 train-test split (800 train / 200 test)
- 5-fold CV applied **only to training set** — test set used once
- All models trained on the same preprocessed 33-feature dataset

---

## Step 4 — Write Experiments (~500 words)

### Results Table (copy this into your report)

| Model | MAE | RMSE | vs Baseline |
|:------|:----|:-----|:------------|
| Linear Regression *(baseline)* | 0.1079 | 0.1326 | — |
| Random Forest | 0.1583 | 0.2157 | ▲ 46.7% worse |
| Gradient Boosting | 0.1458 | 0.1871 | ▲ 35.1% worse |

### Figures to embed (from `report/figures/`):
1. `model_comparison.png` — MAE/RMSE bar chart for all 3 models
2. `rf_feature_importance.png` — RF top 15 features
3. `gb_feature_importance.png` — GB top 15 features
4. `lr_scatter.png` or `gb_scatter.png` — predicted vs actual

### Analysis to write:

**Which model won and why?**
> Linear Regression achieved the best MAE (0.1079), outperforming both ensemble methods. This suggests the Health Risk Score has a predominantly linear relationship with the input features, a finding supported by the high correlation between the target and meteorological variables such as dew point and wind gust observed in the EDA correlation heatmap.

**Feature importance findings:**
> Both RF and GB ranked `dew`, `windgust`, and `Severity_Score` as the top predictors — consistent with domain knowledge that humidity and wind conditions strongly influence pollutant dispersion and health impact.

**Why did ensembles underperform?**
> With only 1,000 records, the dataset is relatively small for ensemble methods, which typically require larger training sets to realise their capacity advantage. Additionally, random shuffling was avoided in favour of chronological splitting — ensemble models may be more sensitive to the distributional shift between earlier and later time periods.

---

## Step 5 — Write Conclusion (~150 words)

**Template:**
> This study compared Linear Regression, Random Forest, and Gradient Boosting for predicting the Health Risk Score from urban air quality and weather data. Linear Regression achieved the best performance (MAE = 0.1079), demonstrating that ensemble complexity does not guarantee improvement on small, linearly-structured datasets.
>
> **Limitations:** The dataset contains only 1,000 daily records across 10 US cities, limiting generalisation. Daily granularity prevents analysis of intra-day pollution spikes. The target variable is composite and may not reflect clinical health outcomes directly.
>
> **Future work:** Larger multi-city datasets, LSTM networks for temporal modelling, and real-time streaming pipelines could significantly improve prediction accuracy. Incorporating socioeconomic variables (traffic density, industrial proximity) may also improve model performance.

---

## Step 6 — Assemble Full PDF

**Report structure (6 pages max, excluding references):**

| Section | Author | Words |
|:--------|:-------|:------|
| Abstract | Ahmed ✅ | ~150 |
| 1. Introduction | Ahmed ✅ | ~300 |
| 2. Related Work | **John** | ~300 |
| 3. Data | Ahmed ✅ | ~350 |
| 4. Methods | **John** | ~500 |
| 5. Experiments | **John** | ~500 |
| 6. Conclusion | **John** | ~150 |
| References | **John** | — |

**Tips:**
- Use Google Docs or Word (LaTeX if you have time)
- Copy Ahmed's text from `report/ahmed_sections.md` (on GitHub `dev` branch)
- Embed figures: insert images from `report/figures/` folder
- Save as `report/report.pdf`
- Keep total to 6 pages max (references can go on page 7)

---

## Step 7 — Send PDF to Ahmed

Once assembled:
1. Commit the PDF to the repo:
```bash
git add report/report.pdf
git commit -m "John: assembled full report PDF"
git push origin dev
```
2. Message Ahmed: *"PDF is pushed to report/report.pdf on dev — please review"*

---

## ⚠️ If You're Short on Time

Minimum viable submission order:
1. Results table + figure in Experiments ← most marks (30%)
2. Methods section ← most marks (30%)
3. Conclusion ← quick to write (5%)
4. Related Work ← find 3 papers, write brief summaries (10%)
5. Assemble PDF

> **Do NOT skip the results table and model comparison figure — that's the core of the Experiments section and worth the most marks.**
