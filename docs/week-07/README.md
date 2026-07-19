# Week 7 — Model Optimisation & Trade-offs

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 6's baseline passed Dr. Reyes's review. Week 7 asks the harder question the ED Board and Martina Griffith (Clinical IT Lead) raised next: does a more sophisticated model actually buy anything, and is it worth the extra complexity and compute? The deliverable is not "the best model" — it is the most defensible recommendation, backed by a six-axis benchmark and an honest cost-benefit memo.

Same dataset, same top-10 feature shortlist, same 80/20 stratified split, same `random_state = 42` as Week 6 — any difference in results this week comes from the model, not the data.

---

## Assignments

> *Folder names follow the same convention as prior weeks — confirm the exact assignment number against your programme portal.*

| Folder | Type | Description |
|--------|------|-------------|
| `notebooks/week7_optimization_models.ipynb` | Notebook | Random Forest, Gradient Boosting, recall-tuned Random Forest, SHAP explanation |
| `docs/week-7-cost-benefit.md` + `.pdf` | Memo | 3-page cost-benefit memo for Dr. De Freitas, the ED Board, and Martina Griffith |
| `docs/decisions/2026-week-7-model-choice.md` | Decision journal | Context, alternatives, decision, reasoning, unknowns |
| `docs/week7_benchmark_table.csv` | Table | Six-axis benchmark, machine-readable |
| `docs/figures/` | Figures | Confusion matrices, feature importances, SHAP explanation |

---

## The Six-Axis Benchmark (plus interpretability)

| Model | Accuracy | Macro Recall | **ESI-1 Recall** | Weighted F1 | Macro F1 | Train time | Inference (per patient) | Interpretability |
|---|---|---|---|---|---|---|---|---|
| Logistic Regression (Week 6 baseline) | 0.254 | 0.417 | **0.750** | 0.327 | 0.214 | 0.34 s | 0.0002 ms | High |
| Random Forest | 0.498 | 0.282 | **0.000** | 0.492 | 0.285 | 29.1 s | 0.122 ms | Medium |
| Random Forest (tuned for recall) | 0.397 | 0.350 | **0.000** | 0.423 | 0.268 | 146.8 s | 0.029 ms | Medium |
| Gradient Boosting | 0.341 | 0.405 | **0.375** | 0.389 | 0.253 | 0.66 s | 0.006 ms | Low |

*(16 ESI-1 patients in the 11,025-patient test set — the entire critical class is 0.14% of the data.)*

---

## Verdict

**Neither complex candidate replaces the baseline.** Random Forest nearly doubles accuracy and wins on macro F1 — while missing every single ESI-1 patient in the test set. Gradient Boosting partially retains ESI-1 recall (0.375) but still recalls half of what the baseline does, and needed SHAP just to explain one prediction.

A dedicated `RandomizedSearchCV` run — scored explicitly on macro recall, not accuracy or F1 — still returned 0.000 ESI-1 recall for Random Forest. This points to a **structural** limitation (majority-vote tree ensembles averaging away an extremely rare class) rather than a hyperparameter left in the wrong position.

**Recommendation:** keep the Week 6 logistic regression baseline as the Phase 3 reference model. The right next step is not a fancier algorithm — it is more and better rare-class data, which is exactly the Caribbean data foundation Phase 1 is meant to build before Phase 2 trains a locally validated classifier.

---

## SHAP Finding Worth Remembering

One true ESI-1 patient (74 years old, near-normal vitals — SpO₂ 98%, respiratory rate 18, heart rate 78, no chest pain/SOB/altered mental status/ambulance flags) was predicted ESI 4 by Gradient Boosting. Age was the only feature pushing toward ESI 1; every vital pushed away from it. This is the "deceptively normal vitals" failure mode — the patients a tired nurse might also miss, and exactly the ones a triage model most needs to catch.

---

## LinkedIn Update

> "This week I benchmarked Random Forest and Gradient Boosting against my Week 6 baseline on a real ED triage dataset. Random Forest nearly doubled accuracy — and missed 100% of the critical patients in the test set. Gradient Boosting did better but still recalled half of what a plain logistic regression caught. Sometimes the right call isn't the fancier model — it's recognising the metric that actually matters and refusing to trade it away for a better-looking accuracy score."

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
