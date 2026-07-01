# Risk Register — Mercer General ED Digital Triage Capture Tool

**CariSurg MedTech Pathways 2026 | Week 4**
**Prepared for:** Saint Cedric Ministry of Health regulatory consultation (via Dr. De Fretias, Mercer General Clinical AI & Innovation Unit)
**Prepared by:** Josiah-John Green

---

## Purpose

This register identifies 10 named risks spanning the AI-technical, operational, ethical, and equity dimensions of a phased AI-assisted triage rollout, modelled on the Phase 1 (digital capture) / Phase 2 (rule-based and ML classifier) approach proposed for Mercer General ED. Each risk includes likelihood, impact, a proposed mitigation, and a measurable signal that the mitigation is actually working — not just present on paper.

Dr. De Fretias's instruction: *do not flinch*. Where a mitigation is weak or unproven, that is stated plainly rather than smoothed over.

---

## Risk Register

| # | Risk | Category | Likelihood | Impact | Mitigation | Signal of Success |
|---|------|----------|:----------:|:------:|------------|--------------------|
| 1 | **Distribution shift / single-site overfitting.** A model trained on Mercer's patient population performs poorly when deployed at a different hospital with a different demographic and disease mix. | AI-technical | High | High | Mandate site-specific external validation before any new deployment; no "train once, deploy everywhere" rollout. | AUC/sensitivity tracked per site quarterly; deployment paused if performance drops below a pre-agreed local threshold. |
| 2 | **Algorithmic bias from non-representative training data.** No Caribbean ED triage dataset currently exists; any model bootstrapped from non-Caribbean data risks encoding assumptions that don't hold locally. | AI-technical | High | High | Phase 1 deliverable is exclusively Caribbean-sourced data; no transfer learning from non-Caribbean models without full local revalidation. | Published demographic audit comparing training set composition against the ED's actual catchment population. |
| 3 | **Silent failure — no uncertainty signal on ESI suggestions.** A rule-based or ML classifier outputs a triage suggestion with no indication of how confident or borderline that suggestion is. | AI-technical | Medium | High | Every suggestion must surface the triggering rule or confidence score alongside the ESI level — never a bare number. | 100% of system-generated suggestions are paired with an explainable trigger or confidence indicator (audited at code review, not self-reported). |
| 4 | **Alert fatigue from over-triage.** High false-positive volume causes nurses to start ignoring or dismissing alerts reflexively, including true positives. | Operational | High | High | Conservative initial alert thresholds; minimum locally-validated positive predictive value required before go-live; nurse-tunable thresholds post-deployment. | Alerts-per-true-positive ratio tracked monthly; target materially better than the 109:1 ratio documented in the Epic Sepsis Model case (see harm case study). |
| 5 | **Workflow friction causing data-entry shortcuts.** Nurses copy-paste from the previous patient or skip fields if the digital tool takes longer than the paper form. | Operational | High | Medium | Phase 1 fields are capped at what the existing paper form already captures — no additional fields; usability testing confirms ≤5 minute completion time. | Field completion audit; target >95% of entries are genuine (non-default, non-duplicated) values. |
| 6 | **Automation bias.** Nurses defer to the system's suggested ESI level even when it contradicts their own clinical judgment, particularly under time pressure. | Ethical | Medium | High | System is framed explicitly as decision *support*, never decision *maker*; any override requires the nurse to document a one-line reason. | Override rate tracked over time. **Honest caveat: a near-zero override rate is not success — it may indicate automation bias rather than agreement.** This signal needs a paired qualitative audit, not just the number alone. |
| 7 | **Informed consent gap.** Patients are triaged and their data feeds a digital/AI system without being meaningfully informed this is happening. | Ethical | Medium | Medium | Visible signage and a short verbal consent disclosure at registration; an opt-out pathway that does not delay or downgrade care. | Spot-check audit of registration encounters confirming disclosure was given. |
| 8 | **Deskilling — erosion of independent triage judgment over time.** Long-term reliance on system suggestions could degrade nurses' own unaided triage accuracy. | Ethical | Low–Medium (long-term) | High | Periodic "blind" triage audits where nurses triage without system input, to confirm skill retention against baseline. | Blind-audit ESI accuracy held stable over time relative to pre-deployment baseline. |
| 9 | **Training data demographic skew.** Mercer's data is from one urban Caribbean ED; a model trained on it may not generalise to rural EDs or other island contexts with different patient profiles. | Equity | High | High | Deployment scope explicitly limited to validated sites; any new site requires local revalidation before go-live — directly mirroring the corrective step Epic itself was forced to adopt after the Wong et al. findings (see harm case study). | Site-specific validation report is a hard gate before any new deployment — not a recommendation, a requirement. |
| 10 | **Differential reliability across patient subgroups.** Aggregate accuracy can mask poor performance for specific groups — e.g. paediatric patients, elderly patients with atypical presentations, or free-text complaint capture across different dialects/accents. | Equity | Medium | High | Performance is reported by subgroup (age band, presentation type), never aggregate-only. | Subgroup-level sensitivity/specificity published alongside overall figures in every validation report. |

---

## Risk Memo — Top 3 Risks, Explained Simply

### 1. Alert Fatigue (Risk 4)
If the system cries wolf too often, nurses stop listening — including when it's right. This is not a hypothetical: it is the single most consistent failure mode found in the deployed clinical AI literature reviewed this week, most starkly in the Epic Sepsis Model, where clinicians had to investigate 109 alerts to find one genuine sepsis case. A Mercer system that floods triage nurses with low-value flags will be tuned out within days, regardless of how good the underlying logic is — and once nurses learn to ignore it, even a correct alert is at risk of being dismissed.

### 2. Distribution Shift / Single-Site Overfitting (Risk 1)
A model is only as good as the population it was trained on. Mercer's eventual dataset will reflect one hospital, in one part of the Caribbean, over one stretch of time. If that model is later assumed to work identically at a different hospital — different demographics, different disease burden, different staffing — it can quietly fail in ways nobody notices until patients are harmed. This is exactly what happened with the Epic Sepsis Model: a tool validated in one context was deployed at hundreds of hospitals with wildly different patient populations, and its real-world performance fell far short of what internal testing had suggested.

### 3. Training Data Demographic Skew (Risk 9)
This is the equity risk underneath the entire project's justification. The whole premise of the Phase 1 proposal is that AI triage tools built on North American and European data don't transfer to the Caribbean — but that same logic applies *within* the Caribbean too. A model trained only on Mercer's urban catchment will not automatically work for a rural clinic in a different territory with a different patient mix. Solving the "Caribbean data gap" with a single urban dataset risks just relocating the same generalisability problem to a smaller scale, rather than actually solving it.

---

*CariSurg MedTech Pathways 2026 — Week 4 Interim Submission*
