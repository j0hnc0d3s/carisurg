## Week 5 — Data Exploration & Feasibility (update)

**Status:** Interim + final Week 5 deliverables complete. Verdict: *proceed to a Week 6 baseline,
with caveats* (see `docs/week-5-feasibility.md`).

**What's in this update:**
- `notebooks/Week5_Tutorial1_Clinical_Data_Literacy.ipynb` — dataset literacy pass: shape,
  dtypes, feature families, chief-complaint grouping, ESI/target explainer.
- `notebooks/Week5_Tutorial2_Data_Profiling.ipynb` — missingness, dtype audit, outlier
  detection (statistical vs. clinically impossible), vitals/chief-complaint correlation with
  ESI, and a full data-quality issues table.
- `notebooks/Week5_Tutorial3_Exploratory_Visualisation.ipynb` — the 6-plot data-quality
  dashboard (missingness, ESI/age, race/ethnicity, top chief complaints, vitals-by-ESI,
  correlation heatmap), saved to `docs/figs/`.
- `docs/week-5-feasibility.md` + `docs/week-5-feasibility.pdf` — the 3-part-brief feasibility
  memo for the ED Board, with the top-10 feature shortlist.
- `docs/figs/01–06_*.png` — the committed dashboard figures.

**Dataset:** `yaleemmlc_admissionprediction_triage.csv` (~55 MB) is **not committed** —
see `.gitignore`. It is 55,121 encounters × 225 columns (Yale EMMLC triage extract), used as a
stand-in pilot dataset while the Mercer General digital capture tool (Phase 1, see
`docs/Carisurg_Assignment14_Final_Documentation.pdf`) is still being built.

**Key finding carried into Week 6:** the extract is single-site, US, non-Caribbean, and has
0% missingness in structured columns — likely pre-cleaned upstream, which is itself a
documented caveat rather than an assumed strength.

**Next:** Week 6 — baseline logistic regression + decision tree on `esi`, using the top-10
shortlist as a starting feature set, informed features excluded: `disposition`, `previousdispo`
(leakage).
