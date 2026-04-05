# src/preprocessing.py
# Author: Ahmed Deraz
# Student ID: 24046227
# Role: Project Lead — Shared Preprocessing Pipeline

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def load_and_preprocess(filepath='../data/urban_air_quality.csv', target='AQI_Target'):
    """
    Loads the UrbanAirNet dataset, imputes missing values, encodes categoricals,
    scales numeric features, and returns a chronological train/test split.

    Args:
        filepath (str): Path to the CSV dataset.
        target (str): Name of the target column (default: 'AQI_Target').

    Returns:
        X_train, X_test, y_train, y_test, feature_names
        - X_train / X_test: numpy arrays (scaled)
        - y_train / y_test: numpy arrays (target values)
        - feature_names: list of column names used as features
    """

    # ── 1. Load dataset ──────────────────────────────────────────────────────
    df = pd.read_csv(filepath)
    print(f"[preprocessing] Raw data shape: {df.shape}")

    # ── 2. Drop columns with >40% missing values ─────────────────────────────
    threshold = 0.4
    missing_fraction = df.isnull().mean()
    cols_to_drop = missing_fraction[missing_fraction > threshold].index.tolist()
    if cols_to_drop:
        print(f"[preprocessing] Dropping {len(cols_to_drop)} high-missingness columns: {cols_to_drop}")
    df = df.drop(columns=cols_to_drop)

    # ── 3. Impute remaining numeric missing values with column median ─────────
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if target in numeric_cols:
        numeric_cols.remove(target)
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    # ── 4. Encode station_id (categorical → integer codes) ───────────────────
    if 'station_id' in df.columns:
        df['station_id'] = df['station_id'].astype('category').cat.codes

    # ── 5. Drop non-feature columns (datetime, identifiers) ──────────────────
    drop_candidates = ['timestamp', 'date', 'datetime', 'time', 'Date', 'Datetime']
    drop_cols = [c for c in drop_candidates if c in df.columns]
    if drop_cols:
        print(f"[preprocessing] Dropping identifier columns: {drop_cols}")
    df = df.drop(columns=drop_cols)

    # ── 6. Separate features and target ──────────────────────────────────────
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in dataset. "
                         f"Available columns: {list(df.columns)}")
    X = df.drop(columns=[target])
    y = df[target]
    feature_names = X.columns.tolist()
    print(f"[preprocessing] Features: {len(feature_names)}  |  Samples: {len(y):,}")

    # ── 7. Scale numeric features with StandardScaler ────────────────────────
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ── 8. Chronological 80/20 split (NO shuffle — respects time ordering) ───
    split_idx = int(len(X_scaled) * 0.8)
    X_train = X_scaled[:split_idx]
    X_test  = X_scaled[split_idx:]
    y_train = y.values[:split_idx]
    y_test  = y.values[split_idx:]

    print(f"[preprocessing] Train: {X_train.shape[0]:,} rows  |  Test: {X_test.shape[0]:,} rows")
    return X_train, X_test, y_train, y_test, feature_names
