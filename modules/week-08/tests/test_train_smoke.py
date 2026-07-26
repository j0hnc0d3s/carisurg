"""
tests/test_train_smoke.py — training smoke test.

Runs the real train_and_evaluate() pipeline on ~50 synthetic rows. This is
not checking model quality (50 rows can't support that) — it is checking
that the pipeline runs start-to-finish without raising, and that the config
contract (keys the code expects) hasn't drifted from config.yaml.
"""
import numpy as np
import pandas as pd
import pytest

from src.model import train_and_evaluate
from src.utils import load_config


@pytest.fixture(scope="module")
def config():
    return load_config("config.yaml")


@pytest.fixture
def synthetic_frame(config):
    """~50 rows with the right dtypes and a value range that won't blow up
    StandardScaler or LogisticRegression, but is otherwise fake data."""
    rng = np.random.default_rng(42)
    n = 50
    cols = config["features"]["columns"]
    data = {}
    for col in cols:
        if col.startswith("cc_") or col == "arrival_ambulance":
            data[col] = rng.integers(0, 2, size=n)
        elif col == "age":
            data[col] = rng.integers(1, 95, size=n)
        elif col == "triage_vital_o2":
            data[col] = rng.integers(85, 100, size=n)
        elif col == "triage_vital_rr":
            data[col] = rng.integers(10, 30, size=n)
        elif col == "triage_vital_hr":
            data[col] = rng.integers(50, 140, size=n)
        else:
            data[col] = rng.integers(0, 2, size=n)
    # Stratified split requires >= 2 members per class. Guarantee that directly
    # rather than hoping a probability-weighted draw covers the rare classes.
    guaranteed = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    remaining = n - len(guaranteed)
    esi = guaranteed + list(rng.choice([1, 2, 3, 4, 5], size=remaining, p=[0.05, 0.3, 0.4, 0.2, 0.05]))
    rng.shuffle(esi)
    data[config["data"]["target"]] = esi
    return pd.DataFrame(data)


def test_pipeline_runs_end_to_end_on_small_frame(config, synthetic_frame):
    X = synthetic_frame[config["features"]["columns"]]
    y = synthetic_frame[config["data"]["target"]]

    artifacts = train_and_evaluate(X, y, config)

    assert artifacts.model is not None, "train_and_evaluate did not return a fitted model"
    assert "accuracy" in artifacts.metrics
    assert "esi1_recall" in artifacts.metrics
    assert 0.0 <= artifacts.metrics["accuracy"] <= 1.0

    # Predictions should only ever be valid ESI levels
    X_check = X.iloc[:5]
    if artifacts.scaler is not None:
        X_check = artifacts.scaler.transform(X_check)
    preds = artifacts.model.predict(X_check)
    assert set(preds).issubset({1, 2, 3, 4, 5}), f"Model predicted invalid ESI level(s): {set(preds)}"
