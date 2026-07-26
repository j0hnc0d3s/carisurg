"""
src/features.py — engineer & encode.

Matches the Week 8 tutorial's expected module contract:
  - select_features(...)       choose columns; exclude leakage/admin/demographics
  - add_clinical_features(X)   engineered clinical features (hook — see note below)
  - encode_demographics(X, df) one-hot demographics (off by default — fairness)

Only add_arrival_ambulance and select_features are actually used by the
pinned model. add_clinical_features and encode_demographics exist as
documented, tested hooks for future weeks — they are pass-through no-ops
by default so the pinned model's numbers do not change silently if someone
adds a call to them without also updating config.yaml.
"""
import pandas as pd


def add_arrival_ambulance(df: pd.DataFrame, arrival_mode_column: str, arrival_mode_value: str) -> pd.DataFrame:
    """Derive a binary arrival_ambulance flag from the raw arrival-mode column.

    NOTE: the raw value in this dataset is lowercase ('ambulance'), not
    title-case. A case mismatch here silently zeroes out the whole feature
    without raising an error — this was caught the hard way in Week 5/6.
    """
    out = df.copy()
    if arrival_mode_column not in out.columns:
        raise KeyError(
            f"'{arrival_mode_column}' not found in dataframe — cannot derive arrival_ambulance."
        )
    out["arrival_ambulance"] = (out[arrival_mode_column] == arrival_mode_value).astype(int)
    return out


def select_features(df: pd.DataFrame, feature_columns: list[str], target: str) -> pd.DataFrame:
    """Return only the pinned model's columns, dropping rows with any
    missing value among them.

    Leakage columns (disposition, previousdispo) and demographics are
    excluded by construction — feature_columns comes from config.yaml's
    top-10 shortlist, which never included them in the first place. No
    imputation here: Week 5/6/7 all chose these columns partly because
    they are reliably populated in the source data.
    """
    missing_cols = [c for c in feature_columns + [target] if c not in df.columns]
    if missing_cols:
        raise KeyError(
            f"Expected column(s) missing from the dataset: {missing_cols}. "
            f"Check config.yaml's 'features.columns' / 'data.target' against the raw CSV schema."
        )
    return df[feature_columns + [target]].dropna()


def add_clinical_features(X: pd.DataFrame) -> pd.DataFrame:
    """Hook for engineered clinical features (e.g. shock index, red-flag
    vitals flags) explored in the Week 7 tutorial exercise notebook.

    Pass-through no-op: the pinned model (docs/model-selection.md) does not
    use any engineered features beyond arrival_ambulance, so this returns
    its input unchanged. Kept as a named function, rather than omitted
    entirely, so a future week that DOES want these features has an
    obvious, single place to add them — and so config.yaml can gain an
    explicit `features.use_clinical_engineering: true/false` flag instead
    of the behaviour changing silently.
    """
    return X.copy()


def encode_demographics(X: pd.DataFrame, df: pd.DataFrame, enable: bool = False) -> pd.DataFrame:
    """Hook for one-hot encoding demographic columns (age band, ethnicity,
    etc.) — OFF by default.

    This is intentional, not an oversight: the pinned model's top-10
    feature shortlist (docs/decisions/, Week 5 memo) does not include
    demographics at all, specifically so the model's ESI recommendation
    cannot depend on a patient's demographic group. `enable=True` exists
    for future fairness-auditing work (e.g. checking whether the CURRENT
    demographic-free model has disparate error rates across groups) —
    it must never be silently turned on for the model actually shipped.
    """
    if not enable:
        return X
    raise NotImplementedError(
        "encode_demographics(enable=True) is not implemented — the pinned model "
        "is demographic-free by design (see docs/HANDOVER.md, Known Limitations). "
        "Implement this only for a deliberate fairness-audit study, not for the shipped model."
    )


def build_features(df: pd.DataFrame, arrival_mode_column: str, arrival_mode_value: str) -> pd.DataFrame:
    """Apply all feature-engineering steps used by the pinned model, in order."""
    return add_arrival_ambulance(df, arrival_mode_column, arrival_mode_value)
