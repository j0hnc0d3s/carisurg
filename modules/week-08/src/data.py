"""
src/data.py — loading only.

Column selection and row-dropping now live in src/features.py's
select_features(), to match the load/clean vs. engineer/encode split the
Week 8 tutorials use. This module's only job is getting the raw CSV into
memory and failing clearly if it isn't where config.yaml says it is.

Note: triage_cleaned_v1.csv arrives already cleaned (Week 5 pipeline) —
there is no separate clean() step here the way the tutorial's generic
example assumes for a raw export. If a future dataset arrives less clean,
that step belongs in this module, before features.py touches it.
"""
from pathlib import Path
import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """Load the cleaned triage CSV from disk.

    Raises FileNotFoundError with a clear message rather than a bare pandas
    traceback, since this is usually the first thing a new hire runs.
    """
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Could not find dataset at '{csv_path}'. "
            f"Confirm 'data.path' in config.yaml and that the file has been placed there — "
            f"see docs/HANDOVER.md for data governance / provenance."
        )
    return pd.read_csv(csv_path)
