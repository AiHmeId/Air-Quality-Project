# src/rf_model.py
# Author: Ahmed Deraz (24046227)

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score


def train_rf(X_train, y_train, n_estimators=200, max_depth=None,
             min_samples_split=2, random_state=42):
    """
    Trains a Random Forest Regressor.
    Returns the fitted model.
    """
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    """
    Returns dict with mae, rmse, y_pred.
    """
    y_pred = model.predict(X_test)
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = float(np.sqrt(mean_squared_error(y_test, y_pred)))
    return {"mae": round(mae, 4), "rmse": round(rmse, 4), "y_pred": y_pred}


def cross_validate_rf(X_train, y_train, n_estimators=200, cv=5):
    """
    5-fold CV on training set. Returns (mean_mae, std_mae).
    """
    model = RandomForestRegressor(n_estimators=n_estimators,
                                  random_state=42, n_jobs=-1)
    scores = cross_val_score(model, X_train, y_train,
                             cv=cv, scoring='neg_mean_absolute_error')
    return -scores.mean(), scores.std()
