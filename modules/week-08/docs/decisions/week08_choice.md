# Decision Journal — Week 7: Model Choice

**Date:** 2026-07-18
**Project:** CariSurg MedTech Pathways — ESI Triage Classifier

## Context

- The ED Board and Martina Griffith (Clinical IT) asked whether a more sophisticated model than the Week 6 logistic regression baseline is worth the added complexity and compute cost before Phase 3.
- Two candidates — Random Forest and Gradient Boosting — were built on the identical Week 6 feature set, split, and seed, so any difference in results is attributable to the model choice alone.

## Alternatives considered

- **Random Forest (default and recall-tuned):** highest accuracy and macro F1 of anything tried this week, but 0.000 recall on ESI 1 in both the default and the recall-optimised configuration — it misses every critical patient in the test set.
- **Gradient Boosting (`HistGradientBoostingClassifier`):** partially retains ESI-1 recall (0.375) and is far cheaper to train and run than Random Forest, but still recalls less than half of what the baseline does on the critical class, and needed SHAP just to produce a per-patient explanation.
- **Keep the Week 6 logistic regression baseline:** lowest accuracy and macro F1 of the four, but by a wide margin the highest ESI-1 recall (0.750), the fastest, and the easiest to explain to a clinician without extra tooling.

## Decision

Keep the Week 6 logistic regression baseline as the reference model for Phase 3; do not promote Random Forest or Gradient Boosting on this week's evidence.

## Reasoning

- Aggregate metrics (accuracy, macro F1) actively mislead here: Random Forest looks like the best model on both, while missing 100% of the patients the whole system exists to protect.
- The ESI-1 miss was tested directly for fixability — a `RandomizedSearchCV` run scored explicitly on macro recall still returned 0.000 ESI-1 recall on test — which points to a structural limitation of majority-vote tree ensembles on an extremely rare class (77 of 55,121 encounters), not a hyperparameter that was set wrong.
- One SHAP-explained case illustrates the failure mode concretely: a 74-year-old patient truly triaged ESI 1 had near-normal vitals (SpO₂ 98%, respiratory rate 18, heart rate 78, no chest pain/SOB/altered mental status/ambulance arrival flags). Gradient Boosting predicted ESI 4. Age was the only feature pushing toward ESI 1; every vital sign pushed away from it. This is exactly the "deceptively normal vitals" danger pattern flagged in Tutorial 4 — the patients a tired nurse might also miss, and the ones a triage model most needs to catch.

## Things I do not yet know

- Whether a different rare-class strategy (oversampling ESI-1 specifically, a two-stage model that screens for ESI-1 first and defers everything else to a second classifier, or cost-sensitive thresholding rather than `class_weight="balanced"`) would recover ESI-1 recall without sacrificing the baseline's simplicity — not yet tested.
- Whether this result replicates on Caribbean ED data once Phase 1 delivers it, since all of this week's numbers are still on the Yale-derived dataset.
