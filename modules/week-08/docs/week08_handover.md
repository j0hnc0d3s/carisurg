# Handover Document

**Project:** ESI Triage Classifier — Phase 3 Baseline
**Prepared for:** Martina Griffith (Clinical IT Lead), Dr. De Freitas
**Prepared by:** Josiah-John Green, CariSurg MedTech Pathways 2026
**Date:** Week 8

---

## Project Summary

This repo trains and evaluates a machine-learning classifier that predicts a patient's Emergency Severity Index (ESI 1–5) from ten triage-time features (age, vitals, chief-complaint flags, arrival mode). It was built on a public Yale EMMLC dataset (55,121 encounters) as a proof of feasibility while the Phase 1 Caribbean data-capture tool is developed in parallel; it has **not** been validated on Mercer General data and is not cleared for clinical use.

## The Final Model Decision

**Logistic Regression**, `class_weight="balanced"`, pinned in `config.yaml`.

**Why:** across six models tried in Weeks 6–7 (Dummy, Decision Tree, Logistic Regression, Random Forest, tuned Random Forest, Gradient Boosting), Logistic Regression has the lowest accuracy but by far the highest recall on ESI-1 — the most critical patient class (0.750, versus 0.000 for Random Forest and 0.375 for Gradient Boosting). For a triage system, missing critical patients is a worse failure than a lower overall accuracy score. Full comparison: [`docs/model-selection.md`](model-selection.md). Full reasoning: [`docs/decisions/2026-week-7-model-choice.md`](decisions/2026-week-7-model-choice.md).

## How to Run

```bash
git clone https://github.com/j0hnc0d3s/carisurg.git
cd carisurg
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# place triage_cleaned_v1.csv in data/ (see "Where the Data Lives" below)

python scripts/train.py --config config.yaml
```

Expect console output ending in a metrics block (accuracy, ESI-1 recall, etc.) and three new files under `records/`: `final_model.joblib`, `final_scaler.joblib`, `final_metrics.json`.

To confirm the pipeline itself is healthy before trusting any of that:
```bash
python -m pytest -v
```
Both tests should pass in a few seconds. They check the data schema and run a training smoke test on synthetic data — they do not check model quality.

## Where the Data Lives

- **Source:** Yale Emergency Medicine Machine Learning Consortium (Yale EMMLC), a US academic hospital's de-identified ED triage export.
- **File expected at:** `data/triage_cleaned_v1.csv` — **git-ignored, not committed to this repo.** See `data/README.md` for provenance and how to obtain it.
- **Access:** limited to CariSurg MedTech Pathways programme participants and tutors. Do not redistribute the CSV outside the programme, upload it to any third-party service, or commit it (or any copy/derivative of it, including model artifacts trained on it) to a public repository.
- **Governance status:** external, de-identified, public research dataset — **not Mercer General patient data**, and no IRB/ethics approval has been sought or is required for it. De-identified does not mean ungoverned: the access restriction above still applies. Any future work using real Mercer General patient data will require separate ethics review before this pipeline (or any successor) touches it.

## Known Limitations

- **ESI-1 recall is measured on only 16 test patients** (77 of 55,121 encounters overall). Every recall number in `docs/model-selection.md` should be read as a consistent pattern across models, not a precise estimate — a single patient's outcome shifts the ESI-1 recall figure by more than 6 percentage points.
- **This is not Caribbean data.** No result in this repo says anything about performance at Mercer General until validated against local ED data collected under Phase 1. Single-site data of any kind carries a real risk of distribution shift when applied elsewhere.
- **The pinned model uses only 10 features, and demographics are excluded by design, not oversight.** No race, ethnicity, or other demographic column is in the feature set — this was a deliberate fairness choice from the Week 5 memo, not a gap to fill in later. It does mean the model draws on far less than a clinician's full judgement, which caps how good it can realistically get.

## Who to Ask

| Question about | Contact |
|---|---|
| Model choice / hyperparameters | Josiah-John Green (author) |
| Dataset access / data governance | Martina Griffith (Clinical IT Lead) |
| Clinical validity of ESI predictions, triage workflow | Dr. Marcus Reyes (Consultant EP) / Dr. De Freitas (Clinical Sponsor) |
| Programme process / submission logistics | CariSurg tutor team — `#ask-a-tutor` |
