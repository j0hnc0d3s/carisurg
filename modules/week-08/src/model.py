"""
src/model.py — build & evaluate.

Matches the Week 8 tutorial's expected module contract:
  - build_model(name, params, seed)   construct the model from config
  - evaluate(model, X, y)             score it: accuracy, precision, recall, F1, inference time

The pinned model is a logistic regression (Week 7 decision — see
docs/model-selection.md). Random Forest and Gradient Boosting are
deliberately NOT implemented here; this module is for the one model that
was chosen, not a model zoo. The exploratory notebooks in notebooks/ are
where the rejected candidates live.
"""
import time
from dataclasses import dataclass, field

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
)


@dataclass
class TrainedArtifacts:
    model: object
    scaler: object
    metrics: dict = field(default_factory=dict)


def build_model(model_config: dict):
    """Construct the (untrained) model from config. Only logistic_regression
    is supported on purpose — see module docstring."""
    model_type = model_config.get("type")
    if model_type != "logistic_regression":
        raise ValueError(
            f"Unsupported model type '{model_type}'. This module only builds the pinned "
            f"logistic_regression model. To explore alternatives, use the notebooks/ folder."
        )
    return LogisticRegression(**model_config["params"])


def split_data(X, y, split_config: dict):
    return train_test_split(
        X, y,
        test_size=split_config["test_size"],
        random_state=split_config["random_state"],
        stratify=y if split_config.get("stratify") else None,
    )


def evaluate(model, X, y, train_time_s: float = 0.0) -> dict:
    """Score a fitted model on held-out X, y.

    Returns accuracy, macro precision/recall, ESI-1 recall specifically
    (the metric this project treats as primary — see docs/model-selection.md
    and docs/decisions/2026-week-7-model-choice.md), weighted/macro F1,
    and inference time per prediction.
    """
    t0 = time.perf_counter()
    y_pred = model.predict(X)
    infer_ms_per_pred = (time.perf_counter() - t0) / len(X) * 1000

    esi1_recall = recall_score(y, y_pred, labels=[1], average=None, zero_division=0)
    esi1_recall = float(esi1_recall[0]) if len(esi1_recall) else 0.0

    return {
        "accuracy": float(accuracy_score(y, y_pred)),
        "macro_precision": float(precision_score(y, y_pred, average="macro", zero_division=0)),
        "macro_recall": float(recall_score(y, y_pred, average="macro", zero_division=0)),
        "esi1_recall": esi1_recall,
        "weighted_f1": float(f1_score(y, y_pred, average="weighted", zero_division=0)),
        "macro_f1": float(f1_score(y, y_pred, average="macro", zero_division=0)),
        "train_time_s": round(train_time_s, 4),
        "inference_ms_per_prediction": round(infer_ms_per_pred, 5),
        "n_test": int(len(X)),
    }


def train_and_evaluate(X, y, config: dict) -> TrainedArtifacts:
    """End-to-end: split, scale (if configured), train, evaluate.

    Returns a TrainedArtifacts bundle rather than printing — callers
    (scripts/train.py, tests/) decide what to do with the result.
    """
    X_train, X_test, y_train, y_test = split_data(X, y, config["split"])

    scaler = None
    X_train_fit, X_test_fit = X_train, X_test
    if config["model"].get("scale_features"):
        scaler = StandardScaler()
        X_train_fit = scaler.fit_transform(X_train)
        X_test_fit = scaler.transform(X_test)

    model = build_model(config["model"])

    t0 = time.perf_counter()
    model.fit(X_train_fit, y_train)
    train_time_s = time.perf_counter() - t0

    metrics = evaluate(model, X_test_fit, y_test, train_time_s=train_time_s)
    metrics["n_train"] = int(len(X_train))

    return TrainedArtifacts(model=model, scaler=scaler, metrics=metrics)
