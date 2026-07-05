Week 5 — AI-Assisted Triage: Data Exploration (Part 1 of 2)
CariSurg MedTech Pathways 2026 | Mercer General Hospital

Overview
Week 5 opens the combined Week 5–6 triage-modelling block. The ED Board's ask: is this dataset
good enough to build a triage model from? Week 5 answers that through profiling, cleaning, and
visualisation, ending in a feasibility memo with a verdict the Board can act on. Week 6 (Part 2)
builds the first baseline model on the same dataset. All work is grounded in the ESI 5-level
triage system (1 = most urgent, 5 = non-urgent).

Dataset: yaleemmlc_admissionprediction_triage.csv — 55,121 de-identified ED encounters, 225
columns (25 structured: demographics, triage vitals, arrival/admin fields, outcomes; 200
chief-complaint flags). Used as a stand-in pilot dataset while the Mercer General digital
capture tool (Phase 1) is still being built. Not committed to version control — see .gitignore.

Assignments
# 	Folder 	Type 	Description
01 	notebooks/week05_tut1_clinical_data_literacy 	Notebook 	Dataset literacy — shape, dtypes, feature families, chief-complaint grouping, ESI/target explainer
02 	notebooks/week05_tut2_data_profiling 	Notebook 	Data profiling — missingness, dtype audit, outlier detection, vitals/complaint correlation with ESI, data-quality issues table
03 	notebooks/week05_tut3_exploratory_visualisation 	Notebook 	Cleaning pipeline (clean_triage()) + 6-plot data-quality dashboard
04 	docs/week-5-feasibility 	Write-up 	3-page feasibility memo for the ED Board, verdict + top-10 feature shortlist

Key Decisions Made
Cleaning pipeline (Tutorial 3) clean_triage() drops rows with no ESI label, coerces vitals
(and age) to numeric, flags physiologically impossible values as NaN rather than capping them
(4 respiratory-rate and 25 glucose readings caught), median-imputes vitals, fills chief-complaint
and administrative blanks with 0 / "Unknown", and rounds ESI to a clean integer 1–5. Every step
is logged so an auditor can re-run it end-to-end from the raw CSV.

Missingness (Tutorial 2) This extract is 100% complete across all structured columns — no
missing ESI labels, no missing vitals anywhere. Rather than treat this as a strength, it's
flagged as a caveat: the completeness likely reflects cleaning already done by the dataset's
original publisher, so it doesn't demonstrate how a live Mercer capture tool would behave when
a nurse skips a field under time pressure.

Outcome leakage (Tutorial 2) disposition and previousdispo record the admit/discharge outcome,
known only after the visit concludes. Both are excluded from every feature list and from the
top-10 shortlist on purpose — using them as inputs would leak the answer.

Feature shortlist (feasibility memo) Ranked by combining clinical intuition with simple
correlation against ESI. age (r = −0.24) was the strongest single signal found — ahead of every
vital — followed by SpO2 (r = +0.18), and cc_chestpain (r = −0.16). Notably, triage_vital_sbp
barely correlates with ESI at all (r ≈ 0.001) despite being a textbook shock marker, flagged for
a closer look in Week 6 rather than assumed to be a strong feature by default.

How to Run
Google Colab
Upload any notebook from notebooks/ to colab.research.google.com
Upload yaleemmlc_admissionprediction_triage.csv via the file panel
Run all cells via Runtime → Run All

VS Code (local)
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=carisurg-venv
Open any notebook, select the carisurg-venv kernel, Run All (Restart first if cells were run
out of order — clean_triage() and classify_columns() must run before any cell that calls them).

Clinical Context
All cleaning decisions were made against physiologically valid ranges (adult general triage):
Column 	Valid Range 	Unit
HR (Pulse) 	20–250 	bpm
SBP 	50–300 	mmHg
DBP 	20–200 	mmHg
RR 	4–60 	breaths/min
SpO2 	50–100 	%
Temp 	86–110 	°F
Glucose 	20–800 	mg/dL
Age 	0–120 	years
ESI 	1–5 	score

Note: temperature in this extract is recorded in °F, not °C — convert before comparing to
Celsius-based thresholds elsewhere in the programme.

CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers
