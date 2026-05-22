# 🏥 CariSurg MedTech Pathways — Week 0, Day 3
## Assignment 3: Data Visualisation
**Mercer General Hospital | Clinical AI & Innovation Unit**

---

## 📋 Overview

This notebook is the Day 3 submission for the CariSurg MedTech Pathways 2026 programme. The task was to produce clinically meaningful visualisations of the cleaned Mercer General ED triage dataset — a reduced, de-identified dataset of 2,205 patient records.

All cleaning from Days 1 and 2 is applied at the top of the notebook before any plots are generated. Group E additions at the end of the notebook focus on **MAP (Mean Arterial Pressure)**, consistent with our Day 2 column assignment.

---

## 📊 Plots Produced

### 1. Gender Distribution — Bar Plot
**Clinical question:** What is the gender breakdown of patients in this dataset?

A bar chart showing the count of Female (0) and Male (1) patients. Labels and count annotations are included.

---

### 2. GCS Score Distribution — Histogram
**Clinical question:** How are GCS scores distributed — are most patients alert, or are there many with reduced consciousness?

A histogram of Glasgow Coma Scale scores (3–15) with two clinical reference lines:
- **GCS ≤ 8** (red) — severe impairment, threshold for intubation consideration
- **GCS ≤ 14** (orange) — warrants clinical attention

The distribution is heavily skewed toward 15 (fully alert), expected for a general ED population.

---

### 3. Heart Rate (Pulse) Distribution — Histogram
**Clinical question:** How many patients present with abnormal heart rates?

A histogram of pulse readings with shaded clinical reference zones:
- **Blue zone** — Bradycardia (< 60 bpm)
- **Red zone** — Tachycardia (> 100 bpm)

---

### 4. SBP vs DBP — Scatter Plot
**Clinical question:** Is there a relationship between systolic and diastolic blood pressure?

A scatter plot of SBP against DBP with a trend reference line at `DBP ≈ 0.6 × SBP`.

---

### 5. Age vs Heart Rate — Scatter Plot
**Clinical question:** Does age affect resting heart rate in ED patients?

A scatter plot of Age against Pulse with clinical reference lines at 60 bpm (lower normal) and 100 bpm (upper normal).

---

### 6. Vital Signs Overview — Box Plots
A 2×4 grid of box plots covering all numeric vitals: `SBP`, `DBP`, `MAP`, `pulse`, `Temp`, `RR`, `GCS`, `Fio2`.

FiO2 values near 100% are intentionally preserved — 100% FiO2 is clinically valid for ventilated patients.

---

### 7. MAP Distribution — Histogram
**Clinical question:** How is MAP distributed across ED patients? How many fall below the 65 mmHg organ perfusion threshold?

Clinical reference lines:
- **65 mmHg** (red) — organ hypoperfusion threshold, key criterion in septic shock management
- **70 mmHg** (orange) — lower normal boundary
- **100 mmHg** (blue) — upper normal boundary

**Clinical interpretation:** Distribution is approximately normal, centred around 90–95 mmHg. Patients left of the 65 mmHg threshold require urgent assessment regardless of other vitals.

---

### 8. Age vs MAP — Scatter Plot
**Clinical question:** Does MAP increase with age? Older patients are more likely to be hypertensive — does the data reflect this?

**Clinical interpretation:** A slight upward trend with age is visible, consistent with known hypertension prevalence patterns. However, the spread is wide at all ages — age alone is not a reliable predictor of MAP. A small number of older patients fall below the 65 mmHg threshold, reinforcing the importance of measuring MAP directly at triage.

---

## 📁 Files

| File | Description |
|------|-------------|
| `week0_day3_visualisation.ipynb` | Main visualisation notebook |
| `EmergencyTriageDataset_Reduced_Dirty.csv` | Raw input dataset |
| `gender_distribution.png` | Bar plot output |
| `gcs_histogram.png` | GCS histogram output |
| `pulse_histogram.png` | Pulse histogram output |
| `sbp_vs_dbp.png` | SBP vs DBP scatter output |
| `age_vs_pulse.png` | Age vs Pulse scatter output |
| `vitals_boxplots.png` | Vitals box plots output |
| `age_vs_temp.png` | Age vs Temp scatter output (student challenge) |
| `map_histogram.png` | MAP histogram output (Group E) |
| `age_vs_map.png` | Age vs MAP scatter output (Group E) |

---

## ▶️ How to Run

### Option A — Google Colab
1. Upload the notebook to [colab.research.google.com](https://colab.research.google.com)
2. Upload `EmergencyTriageDataset_Reduced_Dirty.csv` via the file panel (folder icon in left sidebar)
3. Run all cells via **Runtime → Run All**

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
| Bar plot | `ax.bar(labels, values)` |
| Histogram | `ax.hist(df['col'], bins=n)` |
| Scatter plot | `ax.scatter(df['x'], df['y'])` |
| Box plot | `ax.boxplot(df['col'].dropna())` |
| Clinical reference line (vertical) | `ax.axvline(x=value)` |
| Clinical reference line (horizontal) | `ax.axhline(y=value)` |
| Shaded reference zone | `ax.axvspan(x_min, x_max, alpha=0.1)` |
| Save plot | `plt.savefig('name.png', dpi=100)` |

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
