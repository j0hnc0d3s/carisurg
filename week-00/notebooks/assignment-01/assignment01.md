# 🏥 CariSurg MedTech Pathways — Week 0, Day 1
## Assignment 1: Data Cleaning — Gender Column
**Mercer General Hospital | Clinical AI & Innovation Unit**

---

## 📋 Overview

This notebook is the Day 1 submission for the CariSurg MedTech Pathways 2026 programme. The task was to clean the `Gender` column from the Mercer General ED triage dataset — a reduced, de-identified dataset of 2,205 patient records containing demographics and vital signs collected at triage.

---

## 🔍 The Problem

The `Gender` column contained 6 distinct raw values resulting from inconsistent data entry across different systems:

| Raw Value | Count | Problem |
|-----------|-------|---------|
| `1` | 422 | Numeric encoding — no label |
| `MALE` | 379 | Correct value, inconsistent casing |
| `Male` | 375 | Correct value, correct casing |
| `FEMALE` | 366 | Correct value, inconsistent casing |
| `Female` | 340 | Correct value, correct casing |
| `0` | 323 | Numeric encoding — no label |

This is a common real-world data quality issue — when multiple data entry points feed into the same system, the same value ends up represented in multiple formats.

---

## 🧹 Cleaning Approach

A `clean_gender()` function was written to:
1. Strip leading/trailing whitespace
2. Uppercase everything — so casing is never a factor
3. Map all known variants to a single canonical label (`Male` or `Female`)
4. Return `Unknown` for anything unrecognised — so no data is silently lost or misclassified

```python
def clean_gender(value: str) -> str:
    val = str(value).strip().upper()
    if val in ["MALE", "M", "0"]:
        return "Male"
    elif val in ["FEMALE", "F", "1"]:
        return "Female"
    else:
        return "Unknown"
```

### ⚠️ Assumption on Numeric Codes
Numeric values were mapped as `0 → Male` and `1 → Female`, following a common clinical data convention aligned with HL7/ICD coding standards.

**This assumption must be verified against the original data dictionary or EHR source before this column is used in any model training or statistical analysis.** If the encoding was reversed, the male/female counts flip entirely.

---

## ✅ Results

| Metric | Value |
|--------|-------|
| Female | 1,128 |
| Male | 1,077 |
| Unknown | 0 |
| Total rows | 2,205 |

Zero unknown or unresolved values — no data was lost in the cleaning process.

---

## 📁 Files

| File | Description |
|------|-------------|
| `week0_day1_gender_cleaning.ipynb` | Main cleaning notebook |
| `EmergencyTriageDataset_Reduced_Dirty.csv` | Raw input dataset |
| `EmergencyTriageDataset_Day1_Cleaned.csv` | Cleaned output dataset |

---

## ▶️ How to Run

### Option A — Google Colab
1. Upload the notebook to [colab.research.google.com](https://colab.research.google.com)
2. Upload `EmergencyTriageDataset_Reduced_Dirty.csv` via the file panel (folder icon in left sidebar)
3. Ensure `FILE_PATH` is set to `'EmergencyTriageDataset_Reduced_Dirty.csv'`
4. Run cells top to bottom with **Shift + Enter**

### Option B — VS Code (local)
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=carisurg-venv
```
Open the notebook in VS Code, select the **carisurg-venv** kernel, and run with **Shift + Enter**.

---

## 🔑 Key Concepts

| Concept | Code |
|---------|------|
| Apply a function to a column | `df['col'].apply(my_function)` |
| Check unique values | `df['col'].value_counts(dropna=False)` |
| Validate cleaned column | `df[~df['col'].isin(valid_values)]` |
| Export cleaned dataset | `df.to_csv('output.csv', index=False)` |

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*