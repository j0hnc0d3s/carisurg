# AI-Harm Case Study: The Epic Sepsis Model

**CariSurg MedTech Pathways 2026 | Week 4**
**Prepared by:** Josiah-John Green

---

## What Happened

The Epic Sepsis Model (ESM) is a proprietary, AI-driven early-warning tool embedded in the Epic electronic health record system, designed to alert clinicians when a hospitalised patient may be developing sepsis. It was deployed at hundreds of US hospitals on the strength of internal validation figures Epic had reported, without mandatory independent external validation before clinical use.

In June 2021, Wong et al. published an external validation of the ESM in *JAMA Internal Medicine*, examining 38,455 hospitalisations at Michigan Medicine between December 2018 and October 2019. The results fell sharply short of Epic's internal claims: a sensitivity of only 33% (the model missed two-thirds of actual sepsis cases), a positive predictive value of just 12%, and an area under the curve (AUC) of 0.63 — well below the 0.76–0.83 range Epic had cited internally. The clinical burden was severe: clinicians needed to investigate roughly 109 alerts to find one genuine sepsis case. A second, independent study across two county-hospital emergency departments later replicated this failure pattern, finding the model missed sepsis in over half of encounters and offered little to no time advantage over standard clinical recognition.

## Why It Happened — Root Cause

The core failure was not a single bug but a generalisability gap baked into the model's design and deployment process. The ESM was developed and tuned on data from one set of hospital systems, then deployed broadly under the assumption that its performance would transfer unchanged to any hospital running Epic — different patient populations, different disease prevalence, different documentation habits and all. STAT News investigations later surfaced an additional design flaw: the model used whether a patient had already received antibiotics as a predictive input, meaning it was partly learning to detect sepsis that clinicians had *already caught and treated*, rather than predicting it ahead of time. This produced a model that looked statistically respectable in aggregate but performed poorly at the one task that actually mattered clinically: catching sepsis before a human would.

Critically, the system was deployed at scale without a mandatory requirement for local validation. Hospitals were trusting Epic's internal performance figures rather than testing the tool against their own patient population before going live.

## What the System Failed to Anticipate

The model's developers failed to anticipate that statistical performance on a training population does not guarantee performance on a different population — the exact distribution-shift risk named as Risk 1 in this project's register. They also failed to anticipate the operational consequence of a high false-positive rate: a 109:1 alert-to-true-positive ratio is not a minor inconvenience, it is a near-guarantee of alert fatigue, where clinicians begin reflexively dismissing alerts, including correct ones.

## What Would Have Caught It

Mandatory external validation at each deploying hospital, before clinical go-live, would have surfaced this gap immediately — Michigan Medicine's own data showed the problem the moment someone looked. A requirement to report sensitivity, specificity, and PPV by deploying site rather than relying on a single internal benchmark would have made the risk visible long before hundreds of hospitals had already adopted the tool. This is precisely the mitigation proposed for Risks 1 and 9 in this register: no deployment to a new site without local revalidation first.

## Relevance to This Project

This case is a close analogue to the Phase 2 ambition of this proposal — an early-warning, decision-support tool sitting inside a clinical workflow, prioritising patients by risk. The lesson transfers directly: any classifier trained on Mercer's eventual dataset must be locally validated before being assumed to work elsewhere, and alert volume must be tuned conservatively from the start rather than corrected after clinicians have already learned to ignore it.

---

**Sources:**

Wong, A., Otles, E., Donnelly, J. P., Krumm, A., McCullough, J., DeTroyer-Cooley, O., Pestrue, J., Phillips, M., Konye, J., Penoza, C., Ghous, M., & Singh, K. (2021). External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. *JAMA Internal Medicine, 181*(8), 1065–1070. https://doi.org/10.1001/jamainternmed.2021.2626

Habib, A. R., Lin, A. L., & Grant, R. W. (2021). The Epic Sepsis Model Falls Short — The Importance of External Validation. *JAMA Internal Medicine, 181*(8), 1040–1041. https://doi.org/10.1001/jamainternmed.2021.3333

*(Second independent validation, two-site county ED study, JAMIA Open, 2024 — confirms the pattern persisted post-overhaul.)*

---

*CariSurg MedTech Pathways 2026 — Week 4 Interim Submission*
