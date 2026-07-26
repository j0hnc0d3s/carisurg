"""
src/utils.py — small shared helpers used across the pipeline.
"""
import json
import random
from pathlib import Path

import numpy as np
import yaml
import joblib


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    """Seed every source of randomness the pipeline touches.

    NumPy's global seed covers most of scikit-learn's internals; Python's
    `random` is seeded too in case any helper code uses it directly.
    """
    random.seed(seed)
    np.random.seed(seed)


def save_artifacts(model, scaler, metrics: dict, model_path: str, scaler_path: str, metrics_path: str) -> None:
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    if scaler is not None:
        joblib.dump(scaler, scaler_path)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)


def load_artifacts(model_path: str, scaler_path: str | None = None):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path) if scaler_path and Path(scaler_path).exists() else None
    return model, scaler
