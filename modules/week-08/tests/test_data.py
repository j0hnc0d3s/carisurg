"""
tests/test_data.py — schema sanity check.

This is not testing that the model is good. It's testing that if someone
changes the raw CSV, renames a column, or the arrival-mode encoding shifts
again, the pipeline fails loudly here instead of silently training on
garbage or a zeroed-out feature.
"""
import pandas as pd
import pytest

from src.data import load_raw_data
from src.features import select_features, build_features
from src.utils import load_config


@pytest.fixture(scope="module")
def config():
    return load_config("config.yaml")


def test_raw_data_loads_and_has_expected_columns(config):
    df = load_raw_data(config["data"]["path"])

    assert len(df) > 0, "Dataset loaded but is empty"
    assert config["data"]["target"] in df.columns, "Target column 'esi' missing from raw data"
    assert config["features"]["arrival_mode_column"] in df.columns, (
        "Raw arrival-mode column missing — arrival_ambulance cannot be derived"
    )


def test_arrival_ambulance_is_not_all_zero(config):
    """Guards against the exact bug Weeks 5/6 hit: a case mismatch on the
    arrival-mode string silently zeroes out the whole feature."""
    df = load_raw_data(config["data"]["path"])
    df = build_features(
        df,
        arrival_mode_column=config["features"]["arrival_mode_column"],
        arrival_mode_value=config["features"]["arrival_mode_value"],
    )
    assert df["arrival_ambulance"].sum() > 0, (
        "arrival_ambulance is all zero — check config.yaml's 'arrival_mode_value' "
        "against the raw data's actual casing"
    )


def test_select_features_has_no_missing_values(config):
    df = load_raw_data(config["data"]["path"])
    df = build_features(
        df,
        arrival_mode_column=config["features"]["arrival_mode_column"],
        arrival_mode_value=config["features"]["arrival_mode_value"],
    )
    model_df = select_features(df, config["features"]["columns"], config["data"]["target"])

    assert not model_df.isna().any().any(), "select_features should drop all missing values"
    assert set(config["features"]["columns"]).issubset(model_df.columns)


def test_select_features_raises_on_missing_column(config):
    df = pd.DataFrame({"age": [1, 2, 3]})  # deliberately missing everything else
    with pytest.raises(KeyError):
        select_features(df, config["features"]["columns"], config["data"]["target"])
