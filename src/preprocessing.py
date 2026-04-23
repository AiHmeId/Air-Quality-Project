# src/preprocessing.py
# Author: Ahmed Deraz
# Student ID: 24046227
# Role: Project Lead — Shared Preprocessing Pipeline

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_and_preprocess(filepath='../data/urban_air_quality.csv',
                        target='Health_Risk_Score'):
    """
    Loads the air quality/weather dataset, cleans and encodes all columns,
    scales numeric features, and returns a chronological 80/20 train/test split.

    Args:
        filepath (str): Path to the CSV dataset.
        target (str): Name of the target column (default: 'Health_Risk_Score').

    Returns:
        X_train, X_test, y_train, y_test, feature_names
        - X_train / X_test : numpy arrays (scaled)
        - y_train / y_test : numpy arrays (target values)
        - feature_names    : list of column names used as features
    """

    # ── 1. Load ───────────────────────────────────────────────────────────────
    df = pd.read_csv(filepath)
    print(f"[preprocessing] Raw shape: {df.shape}  |  Target: '{target}'")

    # ── 2. Sort chronologically by datetime (keeps temporal ordering) ─────────
    if 'datetime' in df.columns:
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.sort_values('datetime').reset_index(drop=True)

    # ── 3. Drop pure-text / high-cardinality / leakage columns ───────────────
    drop_always = [
        'datetime', 'datetimeEpoch',   # temporal identifiers
        'sunrise', 'sunset',            # time strings (epoch versions kept)
        'sunriseEpoch', 'sunsetEpoch',  # correlated with datetime → leakage
        'description',                  # free-text
        'stations',                     # high-cardinality station list strings
        'source',                       # data-source tag, not a feature
        'precip',                       # precipprob + precipcover already capture this
    ]
    df = df.drop(columns=[c for c in drop_always if c in df.columns])

    # ── 4. Drop columns with >40% missing values ──────────────────────────────
    miss = df.isnull().mean()
    high_miss = miss[miss > 0.4].index.tolist()
    if high_miss:
        print(f"[preprocessing] Dropping high-missingness cols: {high_miss}")
    df = df.drop(columns=high_miss)

    # ── 5. Encode low-cardinality categoricals ────────────────────────────────
    cat_encode = ['City', 'Season', 'Day_of_Week', 'conditions', 'icon', 'preciptype']
    for col in cat_encode:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown').astype('category').cat.codes

    # ── 6. Encode boolean ─────────────────────────────────────────────────────
    if 'Is_Weekend' in df.columns:
        df['Is_Weekend'] = df['Is_Weekend'].astype(int)

    # ── 7. Impute remaining numeric missing values with column median ──────────
    for col in df.select_dtypes(include=[np.number]).columns:
        if col != target and df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    # ── 8. Separate features and target ───────────────────────────────────────
    if target not in df.columns:
        raise ValueError(
            f"Target '{target}' not found. Available columns: {list(df.columns)}")

    X = df.drop(columns=[target])
    y = df[target]
    feature_names = X.columns.tolist()
    print(f"[preprocessing] Features used: {len(feature_names)}  |  Samples: {len(y):,}")
    print(f"[preprocessing] Feature list: {feature_names}")

    # ── 9. Scale with StandardScaler ──────────────────────────────────────────
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ── 10. Chronological 80/20 split (NO random shuffle) ────────────────────
    split_idx = int(len(X_scaled) * 0.8)
    X_train, X_test = X_scaled[:split_idx], X_scaled[split_idx:]
    y_train, y_test = y.values[:split_idx], y.values[split_idx:]

    print(f"[preprocessing] Train rows: {X_train.shape[0]:,}  |  Test rows: {X_test.shape[0]:,}")
    return X_train, X_test, y_train, y_test, feature_names
