# Week 5 — Dataset Acquisition, Cleaning Pipeline & Feasibility Memo

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 5 is where the project moves from proposal to real data. A public Emergency Department triage dataset is acquired and put through a full cleaning pipeline, then a feasibility memo is written arguing — with real numbers, not projections — why Phase 2 (a baseline classifier) is worth building before anything more sophisticated is attempted. The ED Board's approval of this memo is what Week 6 builds on.

The emphasis this week is **defensibility of decisions, not modelling** — every cleaning choice, every excluded column, and every feature on the shortlist has to survive a "why?" from Dr. De Fretias and the Board.

---

## Assignments

> *Folder names below follow the same `docs/` / `notebooks/` convention as other weeks — confirm the exact assignment numbers against your programme portal, since this README was reconstructed from the decisions carried forward into Week 6 rather than from a Week 5 submission on file.*

| Folder | Type | Description |
|--------|------|-------------|
| `notebooks/week5_cleaning_pipeline.ipynb` | Notebook | Full cleaning pipeline: raw Yale EMMLC export → `triage_cleaned_v1.csv` |
| `docs/week-5-feasibility-memo` | Memo | Feasibility memo recommending Phase 2, with dataset profile and top-10 feature shortlist |

---

## Dataset

**Source:** Yale Emergency Medicine Machine Learning Consortium (Yale EMMLC) — one US academic hospital system's ED triage records, used as a stand-in dataset while the Phase 1 Caribbean data capture tool is still being built.
**Output file:** `triage_cleaned_v1.csv`
**Shape:** 55,121 encounters × 225 columns (25 structured fields + 200 chief-complaint flags)
**Target:** `esi` (Emergency Severity Index, 1–5)

| ESI | Label | Count | % |
|-----|-------|-------|---|
| 1 | Resuscitation (immediate) | 77 | 0.14% |
| 2 | Emergent (≤10 min) | 17,924 | 32.5% |
| 3 | Urgent (≤30 min) | 27,010 | 49.0% |
| 4 | Semi-urgent (≤60 min) | 8,896 | 16.1% |
| 5 | Non-urgent | 1,214 | 2.2% |

---

## Key Cleaning Decisions

- **Leakage exclusions (hard rule):** `disposition` and `previousdispo` are excluded — both are only known *after* the encounter ends and would leak the answer into the feature set.
- **Arrival mode encoding:** `arrivalmode` collapsed to a binary `arrival_ambulance` flag. Note: the raw value is lowercase `'ambulance'` in this dataset — a one-character miss here silently zeroes out a third of the signal.
- **Vitals cleaning:** temperature and SpO₂ values outside physiologically possible ranges are blanked before imputation, not clipped, so a single corrupted reading can't drag a real value toward a boundary.
- **Class imbalance flagged early:** ESI 1 is 77 of 55,121 encounters (0.14%). This single fact is why "accuracy" gets rejected as the primary metric before any model is even built — a model that never predicts ESI 1 already scores 99.86% accuracy.

---

## Top-10 Feature Shortlist

The memo's central technical deliverable — a defensible, clinically-reasoned shortlist rather than "throw every column at the model":

| # | Feature | Clinical reason |
|---|---------|-----------------|
| 1 | `age` | Strongest signal; reduced physiological reserve |
| 2 | `triage_vital_o2` | SpO₂ — ABCs marker; strongest vital-ESI relationship |
| 3 | `cc_chestpain` | ACS/PE rule-out; strongest complaint correlation |
| 4 | `cc_shortnessofbreath` | Respiratory distress |
| 5 | `cc_suicidal` | Safety-critical regardless of vitals |
| 6 | `cc_alcoholintoxication` | Airway/safety risk |
| 7 | `cc_alteredmentalstatus` | Neuro red flag |
| 8 | `arrival_ambulance` | Proxy for pre-hospital severity assessment |
| 9 | `triage_vital_rr` | Respiratory rate — early instability marker |
| 10 | `triage_vital_hr` | Heart rate — shock marker |

**Random seed committed for all downstream weeks:** `42`

---

## Feasibility Memo — What It Argues

1. **The dataset supports a baseline build.** 55,121 encounters is enough to attempt a defensible first model, provided class imbalance is handled explicitly rather than ignored.
2. **This is still not Caribbean data.** Every claim in the memo is scoped to "this proves feasibility on this dataset" — not "this will work at Mercer General." That distinction is what keeps the Phase 1 (local data foundation) argument alive alongside Phase 2 (modelling).
3. **Recommendation:** proceed to Phase 2 — build and evaluate simple baseline classifiers (Week 6) before considering anything more complex (Week 7).

**Outcome:** the ED Board approved Phase 2 on the strength of this memo.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
