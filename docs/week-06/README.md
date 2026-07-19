# Week 6 — Building a Baseline Model

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 6 is the second half of the Weeks 5–6 modelling block. The Week 5 feasibility memo was accepted — the ED Board approved Phase 2. This week builds two simple classifiers on the triage dataset, evaluates them with clinically justified metrics, and produces a defensible baseline before anyone talks about more complex models.

The emphasis is defensibility, not sophistication. Dr. Marcus Reyes, a sceptical Consultant Emergency Physician, will review the baseline. He will not care about the F1 score until he understands why recall for ESI Level 1 matters more than overall accuracy.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 16 | `notebooks/week6_baseline_models.ipynb` | Notebook | Two baseline models + evaluation + metric justification |
| 16 | `docs/Assignment16_Week6_Report.docx` | Report | Final report (≤3 pages) with real results, metric justification, failure-mode reflection |

---

## Dataset

**File:** `triage_cleaned_v1.csv` — the canonical Week 5 pipeline output
**Source:** Yale Emergency Medicine Machine Learning Consortium (one US academic hospital system)
**Shape:** 55,121 encounters × 225 columns (25 structured + 200 chief-complaint flags)
**Target:** `esi` (Emergency Severity Index, 1–5)

| ESI | Label | Count | % |
|-----|-------|-------|---|
| 1 | Resuscitation (immediate) | 77 | 0.14% |
| 2 | Emergent (≤10 min) | 17,924 | 32.5% |
| 3 | Urgent (≤30 min) | 27,010 | 49.0% |
| 4 | Semi-urgent (≤60 min) | 8,896 | 16.1% |
| 5 | Non-urgent | 1,214 | 2.2% |

**Random seed:** 42 | **Split:** 80/20 stratified | **Train:** 44,096 | **Test:** 11,025

---

## Features Used (Top-10 from Week 5 Memo)

| Feature | Clinical reason |
|---------|----------------|
| `age` | Strongest signal (r = −0.24); reduced physiological reserve |
| `triage_vital_o2` | SpO₂ — ABCs marker; strongest vital-ESI relationship |
| `cc_chestpain` | ACS/PE rule-out; strongest complaint correlation |
| `cc_shortnessofbreath` | Respiratory distress |
| `cc_suicidal` | Safety-critical regardless of vitals |
| `cc_alcoholintoxication` | Airway/safety risk |
| `cc_alteredmentalstatus` | Neuro red flag |
| `arrival_ambulance` | Binary flag from `arrivalmode == 'ambulance'` (lowercase) |
| `triage_vital_rr` | Respiratory rate — early instability marker |
| `triage_vital_hr` | Heart rate — shock marker |

**Excluded:** `disposition`, `previousdispo` — outcome leakage (hard rule, not judgment call)

---

## Primary Metric Justification

**Primary metric: ESI-1 recall. Summary metric: macro recall.**

ESI 1 = cardiac arrest, major trauma, anaphylaxis, shock — immediate resuscitation required. A false negative sends that patient to wait. In cardiac arrest, survival drops roughly 10% per minute without intervention.

ESI 1 is 0.14% of encounters. A model predicting ESI 1 zero times achieves 99.86% accuracy. Accuracy is therefore clinically meaningless as a headline number here.

**Macro vs weighted F1:** weighted F1 is dominated by ESI 3 (49% of data) — a model that ignores ESI 1 entirely can still score a high weighted F1. Macro F1 gives every class equal weight, so an ESI-1 failure is visible rather than buried.

---

## Results

### Head-to-Head

| Model | Accuracy | Macro Recall | **ESI-1 Recall** | Weighted F1 | Macro F1 |
|-------|----------|-------------|-----------------|-------------|----------|
| Dummy (stratified) | 0.375 | 0.204 | ~0.14 | 0.375 | 0.204 |
| Logistic Regression | 0.254 | 0.417 | **0.750** | 0.327 | 0.214 |
| Decision Tree (depth=5) | 0.255 | 0.386 | **0.563** | 0.302 | 0.170 |

**Logistic regression is the stronger baseline on the primary metric.** It caught 12 of 16 ESI-1 patients in the test set. Random guessing caught approximately 2.

### Failure Mode

- **Most worried about:** 4 of 16 ESI-1 patients missed by logistic regression (25% false negative rate). In deployment, those patients wait in the wrong queue.
- **Second concern:** ESI-2 recall = 0.31 for LR. Missed ESI-2 patients have strokes, sepsis, ACS — all with 10-minute physician targets. The `balanced` weighting trades ESI-2 precision for ESI-1 and ESI-5 recall — a trade worth naming explicitly, not hiding.
- **Decision tree ESI-4 failure:** the tree predicts ESI 4 zero times in the test set — worth flagging in writing since Dr. Reyes will notice it.

---

## Clinical Explainer Script (for Dr. Reyes)

*~55 seconds at normal pace. No ML jargon.*

"Dr. Reyes — we have two ways to measure whether this system is any good. How often it's right overall, and how often it catches every patient who genuinely needs the resuscitation bay. These are not the same thing. Cardiac arrests are less than one in a thousand patients coming through the door, so a model that never once calls a Level 1 can still be right 99.86% of the time. That number is useless to you. What matters is: of the patients who truly needed the resuscitation bay, how many did we catch? Today's model caught 12 of 16. That's the number I'm asking you to judge us on."

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
