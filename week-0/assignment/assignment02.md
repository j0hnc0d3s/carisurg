# 🏥 CariSurg MedTech Pathways — Week 0, Day 2
## Group E: Blood Pressure Column Cleaning (SBP, DBP & MAP)
**Mercer General Hospital | Clinical AI & Innovation Unit**

---

## 👥 Group Members
Shari · Gabrielle · Asharah · Josiah

---

## 📋 Overview

This notebook is the Day 2 submission for Group E of the CariSurg MedTech Pathways 2026 programme. The task was to clean an assigned column from the Mercer General ED triage dataset — a reduced, de-identified dataset of 2,205 patient records containing common vital signs collected at triage.

Group E was assigned **MAP (Mean Arterial Pressure)**. However, because MAP is not directly measured but is instead *calculated* from Systolic and Diastolic Blood Pressure, we first cleaned **SBP** and **DBP** before recalculating MAP from the cleaned values.

---

## 🫀 Clinical Context

| Column | Full Name | Clinical Meaning | Valid Range | Unit |
|--------|-----------|-----------------|-------------|------|
| SBP | Systolic Blood Pressure | Peak arterial pressure during a heartbeat — the top number in a reading like 120/80 | 50–250 | mmHg |
| DBP | Diastolic Blood Pressure | Arterial pressure between heartbeats — the bottom number in a reading like 120/80 | 30–150 | mmHg |
| MAP | Mean Arterial Pressure | Average pressure driving blood to organs across a full cardiac cycle | 40–180 | mmHg |

**Key clinical thresholds:**
- SBP < 90 mmHg → hypotension
- SBP < 70 mmHg → possible shock
- MAP < 65 mmHg → organ hypoperfusion threshold; key criterion in septic shock management

**MAP formula:**

```
MAP = (SBP + 2 × DBP) / 3
```

---

## 🧹 Cleaning Approach

### Why clean SBP and DBP before MAP?
MAP is derived from SBP and DBP. If either of those columns contains errors, those errors propagate directly into MAP. Cleaning MAP in isolation would leave silently wrong values in place. The correct order is:

```
Clean SBP → Clean DBP → Recalculate MAP
```

Cross-validation confirmed this was necessary — 43 rows in the original dataset had MAP values that didn't match the formula, because MAP had been computed from dirty SBP data before cleaning.

---

### SBP Cleaning
- **Problem:** Column stored as `object` (string) dtype; 44 values of `30` or `500` present
- **Root cause:** Data entry errors, not outliers. An SBP of 30 is not survivable outside a resuscitation bay; 500 exceeds what human vasculature can generate
- **Fix:** `pd.to_numeric(..., errors='coerce')` to convert type; range filter (50–250 mmHg) to flag invalids; replaced with `NaN`
- **Imputation:** Mean (126.68 mmHg) — justified because after removing invalid values, the distribution was approximately normal (mean 126.68, median 125.00, difference of 1.68 mmHg)

---

### DBP Cleaning
- **Problem:** 3 values above 150 mmHg; 22 NaNs present
- **Fix:** Range filter (30–150 mmHg); invalid values replaced with `NaN`
- **Imputation:** Mean (77.36 mmHg) — justified because after removing invalid values, the distribution was approximately normal (mean 77.36, median 78.00, difference of 0.64 mmHg)

---

### MAP Cleaning
- **Problem:** 43 values corrupted by dirty SBP data; 22 NaNs present
- **Fix:** Recalculated entirely from cleaned SBP and DBP using the formula `(SBP + 2 × DBP) / 3` rather than filtering the existing column
- **Imputation:** Mean applied as a fallback for any rows where both SBP and DBP were simultaneously missing, leaving MAP unable to be computed from the formula
- **Edge case preserved:** One patient (ID 1762, MAP = 39.33 mmHg) falls below the physiological floor of 40 mmHg. Both their SBP (58) and DBP (30) are individually within valid ranges — this is a genuine signal of critical illness (severe hypotension), not a data error, and was preserved intentionally

---

## ✅ Final Results

| Column | Issues Found | Fix Applied | Imputation | Final Range |
|--------|-------------|-------------|------------|-------------|
| SBP | String dtype + 44 values of 30 or 500 | `pd.to_numeric()` + range filter | Mean (126.68 mmHg) | 55–250 mmHg |
| DBP | 3 values above 150 mmHg + 22 NaNs | Range filter | Mean (77.36 mmHg) | 30–150 mmHg |
| MAP | 43 values corrupted by dirty SBP | Recalculated from cleaned SBP & DBP | Mean fallback | 39–173 mmHg |

---

## 📁 Files

| File | Description |
|------|-------------|
| `week0_tutorial2_advanced_cleaning_M….ipynb` | Main notebook — full tutorial + Group E cleaning section |
| `EmergencyTriageDataset_Reduced_Dirty.csv` | Raw input dataset |
| `Emergency_Triage_Dataset_Day2_MAP — Shari, Gabrielle, Asharah, & Josiah.csv` | Cleaned output dataset |

---

## ▶️ How to Run

### Option A — Google Colab (recommended)
1. Upload the notebook to [colab.research.google.com](https://colab.research.google.com)
2. Upload `EmergencyTriageDataset_Reduced_Dirty.csv` via the file panel (folder icon in left sidebar)
3. Ensure `FILE_PATH` is set to `'EmergencyTriageDataset_Reduced_Dirty.csv'`
4. Run all cells top to bottom with **Runtime → Run All**

### Option B — VS Code (local)
1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m ipykernel install --user --name=carisurg-venv
   ```
3. Open the notebook in VS Code and select the **carisurg-venv** kernel
4. Run cells with **Shift + Enter**

---

## 📦 Dependencies

```
pandas
numpy
matplotlib
notebook
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔑 Key Concepts Used

| Concept | Code |
|---------|------|
| Convert to numeric | `pd.to_numeric(df['col'], errors='coerce')` |
| Find NaNs | `df['col'].isnull().sum()` |
| Fill NaNs with mean | `df['col'].fillna(df['col'].mean())` |
| Flag outliers | `df[(df['col'] < MIN) \| (df['col'] > MAX)]` |
| Replace outliers | `df.loc[condition, 'col'] = np.nan` |
| Recalculate derived column | `df['MAP'] = ((df['SBP'] + 2 * df['DBP']) / 3).round(2)` |

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*