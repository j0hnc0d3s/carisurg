# Week 8 — Reproducibility & Modular Project Design

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 8 is the handover week. Martina Griffith's standard: *can a new hire, arriving Monday morning, clone this repo, read the README, and be running the model by end of day?* The Week 7 model comparison is finalised into one pinned decision, the exploratory notebook code is refactored into a proper `src/` package, two pytest sanity checks make the pipeline fail loudly instead of silently, and a one-page handover document answers the "Monday morning" question directly.

No new modelling this week — one decision, one model, one set of hyperparameters, committed.

---

## Assignments

> *Folder name follows the same convention as prior weeks — confirm the exact assignment number against your programme portal.*

| Folder | Type | Description |
|--------|------|-------------|
| `src/`, `scripts/`, `tests/`, `config.yaml` | Code | Modular refactor of the Week 6–7 exploratory notebooks |
| `modules/week-08/docs/week08_selection.md` | Table | Every model trained across Weeks 6–7, winner marked, audit trail |
| `modules/week-08/docs/week08_handover.md` | Document | One-page handover: summary, decision, how to run, data, limitations |

---

## Repo Layout

```
carisurg/
├── config.yaml              # single source of truth — model type, hyperparameters, paths, seed
├── requirements.txt          # pinned library versions
├── data/
│   └── triage_cleaned_v1.csv # not committed — see data/README.md
├── src/
│   ├── data.py                # load_raw_data — loading only
│   ├── features.py            # select_features, add_arrival_ambulance, build_features
│   │                            #   + add_clinical_features, encode_demographics (documented no-op hooks)
│   ├── model.py                # build_model, evaluate, split_data, train_and_evaluate
│   └── utils.py                # load_config, set_seed, save/load_artifacts
├── scripts/
│   └── train.py                # entry point — reads config.yaml, runs the full pipeline
├── tests/
│   ├── test_data.py             # schema checks + the arrival_ambulance regression guard
│   └── test_train_smoke.py      # ~50-row synthetic end-to-end smoke test
├── records/                    # generated — final_model.joblib, final_scaler.joblib, final_metrics.json
├── notebooks/                   # exploratory work stays here; the final solution does not
└── docs/
    ├── week08_selection.md        # audit trail across Weeks 6–7, winner marked
    ├── week08_handover.md                 # one-page handover
    └── decisions/
        └── 2026-week-7-model-choice.md
```

---

## The Pinned Model

**Logistic Regression**, `class_weight="balanced"`, `max_iter=2000`, `solver="lbfgs"`, `random_state=42` — committed in `config.yaml`, not scattered across notebook cells.

**Why this one, not Random Forest or Gradient Boosting:** across all six models trained in Weeks 6–7, Logistic Regression has by far the highest ESI-1 recall (0.750) — the critical-patient metric the ED Board cares about — despite the lowest raw accuracy. Random Forest nearly doubles accuracy and still scores 0.000 ESI-1 recall, even after a recall-focused tuning pass. Full table: [`docs/model-selection.md`](docs/model-selection.md). Full reasoning: [`docs/decisions/2026-week-7-model-choice.md`](docs/decisions/2026-week-7-model-choice.md).

---

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python scripts/train.py --config config.yaml
```

## Sanity Checks

```bash
python -m pytest -v
```
Two tests, five assertions total: a data-schema check (including a regression guard for the exact `arrival_ambulance` case-mismatch bug hit in Week 5/6) and a training smoke test on ~50 synthetic rows. Neither test checks model quality — they check that the pipeline breaks loudly, not silently, when something upstream changes.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
