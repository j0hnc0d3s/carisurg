# Model Selection — Audit Trail (Weeks 6–7)

Every model trained across Weeks 6–7, same dataset (`triage_cleaned_v1.csv`), same top-10 feature shortlist, same 80/20 stratified split, `random_state = 42` throughout. Differences in the numbers below come from the model, not the data.

Full reasoning behind the winning model: [`docs/decisions/2026-week-7-model-choice.md`](decisions/2026-week-7-model-choice.md).

| Model | Week | Key hyperparameters | Accuracy | Macro Precision | Macro Recall | **ESI-1 Recall** | Weighted F1 | Macro F1 | Train time | Inference (per patient) |
|---|---|---|---|---|---|---|---|---|---|---|
| Dummy (stratified) | 6 | — | 0.375 | — | 0.204 | ~0.14 | 0.375 | 0.204 | — | — |
| Decision Tree | 6 | `max_depth=5`, `class_weight=balanced` | 0.255 | — | 0.386 | 0.563 | 0.302 | 0.170 | <0.1 s | ~0 ms |
| **Logistic Regression** ✅ **WINNER** | 6 | `class_weight=balanced`, `max_iter=2000`, `solver=lbfgs` | 0.254 | 0.315 | 0.417 | **0.750** | 0.327 | 0.214 | 0.25 s | 0.00009 ms |
| Random Forest | 7 | `n_estimators=300`, `class_weight=balanced` | 0.498 | — | 0.282 | **0.000** | 0.492 | 0.285 | 29.1 s | 0.122 ms |
| Random Forest (tuned) | 7 | `RandomizedSearchCV`, scored on `recall_macro` | 0.397 | — | 0.350 | **0.000** | 0.423 | 0.268 | 146.8 s | 0.029 ms |
| Gradient Boosting | 7 | `HistGradientBoostingClassifier`, `max_depth=6`, `max_iter=300` | 0.341 | — | 0.405 | **0.375** | 0.389 | 0.253 | 0.66 s | 0.006 ms |

## Winner: Logistic Regression

**Pinned in `config.yaml`.** Not the highest accuracy or macro F1 of the six models tried — Random Forest beats it on both. It wins on the metric the ED Board and Dr. Reyes actually care about: **ESI-1 recall**, the fraction of the most critical patients correctly flagged. Random Forest scores 0.000 on this axis in both its default and recall-tuned configurations — it misses every single ESI-1 patient in the test set, despite nearly doubling overall accuracy. That is disqualifying for a triage system, regardless of how good the aggregate numbers look.

Full reasoning, including why tuning did not fix Random Forest's ESI-1 blind spot, and the SHAP case that shows the failure mode concretely, is in the linked decision journal entry above — this table is the audit trail; that file is the argument.
