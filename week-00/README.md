# Week 0 — Orientation & Data Cleaning Fundamentals

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 0 is the programme's onboarding week. The focus is environment setup, exploratory data analysis, and first clinical data cleaning tasks on a reduced, de-identified triage dataset from the Mercer General Emergency Department. All work is grounded in the ESI 5-level triage system used at Mercer.

**Dataset:** `EmergencyTriageDataset_Reduced_Dirty.csv` — 2,205 de-identified ED triage records, 11 columns (demographics + vital signs). Not committed to version control. Obtain via CariSurg programme materials.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 01 | `notebooks/assignment-01` | Notebook | Data cleaning — Gender column |
| 02 | `notebooks/assignment-02` | Notebook | Data cleaning — SBP, DBP & MAP (Group E) |
| 03 | `notebooks/assignment-03` | Notebook | Data visualisation — MAP histogram & scatter |
| 04 | `notebooks/assignment-04` | Notebook | At-risk patient pseudocode / triage algorithm |
| 05 | `docs/assignment-05` | Write-up | Vital sign description — MAP |
| 06 | `docs/assignment-06` | Write-up | Unconsidered metric — SpO2 |

---

## Key Decisions Made

**Gender cleaning (Assignment 01)**
The column contained 6 raw values from mixed data entry — casing variants and numeric codes. A `clean_gender()` function normalised everything to `Male` / `Female`. Numeric encoding assumed `0 = Female`, `1 = Male` per HL7 convention — flagged for clinical verification.

**Blood pressure cleaning (Assignment 02)**
Group E was assigned MAP. Since MAP is calculated from SBP and DBP (`MAP = (SBP + 2 × DBP) / 3`), both upstream columns were cleaned first. 44 SBP values of 30 or 500 were data entry errors, not outliers. MAP was recalculated from scratch rather than filtered — 43 rows had MAP values corrupted by dirty SBP data. Mean imputation was used for SBP and DBP after confirming approximate normality post-cleaning.

**Visualisation (Assignment 03)**
Student challenge plots focused on MAP — a histogram showing the 65 mmHg organ hypoperfusion threshold, and an Age vs MAP scatter showing the slight upward trend with age consistent with hypertension prevalence patterns.

---

## How to Run

### Google Colab
1. Upload any notebook from `notebooks/` to [colab.research.google.com](https://colab.research.google.com)
2. Upload `EmergencyTriageDataset_Reduced_Dirty.csv` via the file panel
3. Run all cells via **Runtime → Run All**

### VS Code (local)
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=carisurg-venv
```
Open any notebook, select the **carisurg-venv** kernel, run with **Shift + Enter**.

---

## Clinical Context

All cleaning decisions were made against physiologically valid ranges from the Mercer General triage reference:

| Column | Valid Range | Unit |
|--------|------------|------|
| SBP | 50–250 | mmHg |
| DBP | 30–150 | mmHg |
| MAP | 40–180 | mmHg |
| GCS | 3–15 | score |
| Pulse | 20–250 | bpm |
| Temp | 32–43 | °C |
| RR | 5–60 | breaths/min |
| FiO2 | 21–100 | % |

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*