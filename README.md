### CariSurg MedTech Pathways 2026 — Clinical AI Engineering Portfolio
**Josiah John-Green | University of the West Indies, Mona**

---

## 👤 About Me

I'm a final-year Software Engineering student at the University of the West Indies, Mona. This repository documents my 13-week journey through the CariSurg MedTech Pathways 2026 programme, where I'm training as a Clinical AI Engineer embedded in the Emergency Department at Mercer General Hospital.

---

## 🧭 About the Programme

CariSurg MedTech Pathways is a 13-week intensive programme building a pipeline of Caribbean clinical AI engineers — professionals who understand both global healthcare technology and the regional health-system realities it must serve.

The programme is run by [CariSurg](https://carisurg.com), a partnership between the University of the West Indies and the University of Leeds' STORM Lab. It combines clinical data science, AI/ML, and human-computer interaction, with a focus on building tools that actually work in resource-constrained Caribbean healthcare settings.

**Clinical setting:** Mercer General Hospital Emergency Department — a 24/7 regional ED serving ~80,000 residents, running on paper triage records and a shared lab/radiology setup.

---

## 📁 Repository Structure

```
carisurg-portfolio/
├── week-01/
│   ├── assignment-01/
│   │   ├── week0_day1_gender_cleaning.ipynb
│   │   └── assignment01.md
│   └── assignment-02/
│   │   ├── week0_day1_gender_cleaning.ipynb
│   │   └── assignment01.md
│   └── assignment-03/
│   │   ├── age_vs_map.png
│   │   └── age_vs_pulse.png
│   │   └── age_vs_temp.png
│   │   └── assignment-03.pdf
│   │   └── gcs_histogram.png
│   │   └── gender_distribution.png
│   │   └── map_histogram.png
│   │   └── pulse_histogram.png
│   │   └── sbp_vs_dbp.png
│   │   └── vitals_boxplots.png
│   │   └── week0_day3_visualisation.ipynb
│   └── assignment-04/
│   │   └── assignment-04.pdf
│   └── assignment-05/
│   │   └── assignment-05.pdf
│   └── assignment-06/
│       └── assignment-06.pdf
├── week-02/
│   ├── assignment-07/
│   │   └── assignment-07.pdf
│   └── assignment-08/
│       └── assignment-08.pdf
├── week-3/          # Coming soon
│   ...
├── week-12/         # Coming soon
├── requirements.txt
└── README.md
└── EmergencyTriageDataset_Reduced_Dirty.csv
```

---

## 📅 Weekly Progress

### ✅ Week 0 — Orientation & Data Cleaning Fundamentals
> *Environment setup, exploratory data analysis, and first clinical data cleaning tasks on the Mercer General ED triage dataset.*

| # | Assignment | Status |
|---|-----------|--------|
| 1 | Data Cleaning — Gender Column | ✅ Complete |
| 2 | Data Cleaning — Assigned Column (MAP) | ✅ Complete |
| 3 | Data Visualization | ✅ Completes |
| 4 | Vital Sign Description | ✅ Complete |
| 5 | Unconsidered Metrics | ✅ Complete |
| 6 | Triage Pseudocode | ✅ Complete |
| 7 | Final Submission | ✅ Complete |

**Dataset:** `EmergencyTriageDataset_Reduced_Dirty.csv` — 2,205 de-identified ED triage records with 11 columns (demographics + vital signs).

**Key work this week:**
- Cleaned the `Gender` column — resolved mixed casing and numeric encoding (`0/1`) across 6 distinct raw values
- Cleaned `SBP`, `DBP`, and recalculated `MAP` from scratch — identified 44 data entry errors in SBP and cross-validated MAP against its formula `(SBP + 2×DBP) / 3`, finding 43 corrupted rows
- Justified imputation choices (mean vs median) based on distribution analysis

---

### ✅ Week 1 — Research Fundamentals (Academic Papers & Preliminary Proposal)
> *Research metholodology, and principles*

| # | Assignment | Status |
|---|-----------|--------|
| 1 | Intermim Submission | ✅ Complete |
| 2 | Final Submission | ✅ Complete |

**Key work this week:**
- Learned how to use Zotoro to reference publication/articles.
- Refined research principles, and writing.

---

### ✅ Week 2 — Project Setup & Documentation
> *Research metholodology, and principles, Git fundamentals*

| # | Assignment | Status |
|---|-----------|--------|
| 1 | Intermim Submission | 🔄 In-Progress |
| 2 | Final Submission | 🔄 In-Progress |
| 3 | Career Challenge | 🔄 In-Progress |

**Key work this week:**
- Learned how to use Zotoro to reference publication/articles.
- Refined research principles, and writing.

---

### 🔜 Week 3–12 — Coming Soon
Weeks 3–12 will cover progressively advanced clinical AI topics including feature engineering, model building, evaluation, and deployment considerations for low-resource Caribbean health settings. This section will be updated weekly.

---

## 🛠️ Setup & Running the Notebooks

### Option A — Google Colab (no installation needed)
1. Open [colab.research.google.com](https://colab.research.google.com)
2. Upload the `.ipynb` file via **File → Upload notebook**
3. Upload the CSV via the file panel (folder icon in left sidebar)
4. Run cells with **Shift + Enter**

### Option B — Local (VS Code)

```bash
# Clone the repo
git clone https://github.com/j0hnc0d3s/carisurg-portfolio.git
cd carisurg-portfolio/week0

# Create and activate virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
python -m ipykernel install --user --name=carisurg-venv
```

Then open any `.ipynb` in VS Code and select the **carisurg-venv** kernel.

---

## 📦 Dependencies

```
pandas
numpy
matplotlib
notebook
```

---

## 🏥 Clinical Context

All work in this portfolio is grounded in the operational realities of the Mercer General ED:

- **Triage system:** ESI 5-level (Emergency Severity Index)
- **Data capture:** Paper-based triage records — the programme's goal is to build the digital foundation that makes future AI tooling possible
- **Staffing:** Minimum 2 house officers per shift, 1 registrar, 1 consultant on call
- **Key constraint:** Lab and radiology are shared with the rest of the hospital — any tool that increases test ordering without addressing turnaround worsens the queue

> *"A project that does nothing more than digitise the existing triage form into a queryable, de-identified database is genuinely valuable on its own — and it is the foundation any later predictive or improvement work has to stand on."*
> — Dr. Loren De Freitias, Director of Emergency Medicine, Mercer General

---

## 📬 Contact

**Josiah John-Green**
- GitHub: [@j0hnc0d3s](https://github.com/j0hnc0d3s)
- LinkedIn: [linkedin.com/in/josiah-john-green](https://linkedin.com/in/josiah-john-green)
- Portfolio: [Portfolio](https://j0hnc0d3s.github.io/portfolio/)

---

*Built as part of CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
