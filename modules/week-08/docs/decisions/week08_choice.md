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

---

## Addendum — 2026-07-25 (Week 8): responding to Dr. De Freitas's objection

**Objection raised:** is a 0.75 ESI-1 recall worth having only 0.254 overall accuracy? Framed as "assign every patient's ESI level," 0.254 accuracy means the model is wrong on roughly 3 of every 4 patients across ESI 2–5 — the 98.86% of volume that isn't ESI-1. That has real costs the original decision above didn't weigh: nurses losing trust in a tool that's visibly wrong most of the time (and abandoning it before it ever catches an ESI-1), and under-triage errors on the common classes (ESI-2 strokes, sepsis) being spread across a much larger population than the 77 ESI-1 encounters this whole argument was built around.

**This is a fair objection, and it exposes a real gap: the original decision above answered "which model" without answering "what is this model actually for."** Comparing four classifiers on accuracy vs. ESI-1 recall implicitly assumed all four were candidates to autonomously assign ESI end-to-end. At 0.254 accuracy, the logistic regression baseline cannot defensibly be deployed that way — Dr. De Freitas is right about that.

**Resolution — reframe the model's role, not the model itself:**

The pinned logistic regression does not change. What changes is what it's for: a **high-recall ESI-1 screening flag that runs alongside normal triage**, not a replacement for it. A nurse still assigns ESI 2–5 exactly as before; the model's only job is to ask "is this one you might be missing?" on the rare, high-consequence class it was actually built and evaluated for. Under that framing, 0.254 overall accuracy is no longer the relevant number, because the tool was never the source of truth for ESI 2–5 in the first place — and the objection above stops applying to a use case that was never proposed.

**Logged as future work, not this week's deliverable** (Week 8 is reproducibility/handover, not modelling — this is deliberately not new model-shopping):
- A two-stage/hierarchical architecture: a cheap, high-recall-only ESI-1 screen, with a separately accuracy-optimised model or ordinary nursing judgement handling ESI 2–5.
- Whether that screen should be this same logistic regression, or something purpose-built for a screening threshold (e.g. tuned on precision-recall trade-off rather than `class_weight="balanced"`).

See `docs/HANDOVER.md` for the updated final-model-decision line and known limitations reflecting this reframing.