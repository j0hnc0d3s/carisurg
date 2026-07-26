#!/usr/bin/env python3
"""
scripts/train.py — entry point that reads config.yaml and trains the pinned model.

Usage:
    python scripts/train.py --config config.yaml
"""
import argparse
import sys
from pathlib import Path

# Allow running from repo root without installing the package.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.utils import load_config, set_seed, save_artifacts
from src.data import load_raw_data
from src.features import build_features, select_features
from src.model import train_and_evaluate


def main(config_path: str) -> None:
    config = load_config(config_path)
    set_seed(config["split"]["random_state"])

    print(f"[1/4] Loading data from {config['data']['path']}")
    df = load_raw_data(config["data"]["path"])

    print("[2/4] Building features (arrival_ambulance)")
    df = build_features(
        df,
        arrival_mode_column=config["features"]["arrival_mode_column"],
        arrival_mode_value=config["features"]["arrival_mode_value"],
    )

    model_df = select_features(
        df,
        feature_columns=config["features"]["columns"],
        target=config["data"]["target"],
    )
    X = model_df[config["features"]["columns"]]
    y = model_df[config["data"]["target"]]
    print(f"      {len(model_df):,} rows ready for modelling")

    print("[3/4] Training + evaluating pinned model (logistic regression)")
    artifacts = train_and_evaluate(X, y, config)

    print("[4/4] Saving model, scaler, and metrics to records/")
    save_artifacts(
        artifacts.model, artifacts.scaler, artifacts.metrics,
        model_path=config["output"]["model_path"],
        scaler_path=config["output"]["scaler_path"],
        metrics_path=config["output"]["metrics_path"],
    )

    print("\n=== METRICS ===")
    for k, v in artifacts.metrics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train the pinned Phase 3 triage model.")
    parser.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    args = parser.parse_args()
    main(args.config)
