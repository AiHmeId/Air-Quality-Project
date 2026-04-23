# src/gb_model.py
# Author: John 

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score


def train_gb(X_train, y_train, n_estimators=200, learning_rate=0.05,
             max_depth=4, random_state=42):
    """
    Trains a Gradient Boosting Regressor.
    Returns the fitted model.
    """
    model = GradientBoostingRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        random_state=random_state
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


def cross_validate_gb(X_train, y_train, n_estimators=200, learning_rate=0.05, cv=5):
    """
    5-fold CV on training set. Returns (mean_mae, std_mae).
    """
    model = GradientBoostingRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        random_state=42
    )
    scores = cross_val_score(model, X_train, y_train,
                             cv=cv, scoring='neg_mean_absolute_error')
    return -scores.mean(), scores.std()