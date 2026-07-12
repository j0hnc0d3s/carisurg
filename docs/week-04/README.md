# Week 4 — Ethics, Safety & Risk Awareness in Healthcare Technology

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 4 is the ethics and risk week. The framing is a regulatory consultation from the Saint Cedric Ministry of Health, which is weighing a multi-year nationwide rollout of AI-assisted triage across the public hospital network. Dr. De Fretias delegates the first draft of a risk register to the Unit.

The brief is direct: *do not flinch*. If a mitigation is weak or unproven, say so.

This week also establishes the programme's clearest stake on AI augmentation versus replacement — the position throughout this project is that AI in clinical triage is a decision support tool, never a decision replacement, and that this distinction carries measurable design consequences.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 13 | `docs/assignment-13` | Interim | Draft risk register (10 risks) + AI-harm case study (Epic Sepsis Model) |
| 14 | `docs/assignment-14` | Final Proposal | Full proposal with Risk Analysis section added; 15 references |

---

## Risk Register Summary

Ten named risks spanning four categories. Full table with mitigations and signals of success is in `docs/assignment-14`.

| Category | Risks |
|----------|-------|
| AI-technical | Distribution shift (R1), Algorithmic bias / proxy variables (R2), Silent failure / no uncertainty signal (R3) |
| Operational | Alert fatigue from over-triage (R4), Workflow friction / data-entry shortcuts (R5) |
| Ethical | Automation bias (R6), Informed consent gap (R7), Deskilling over time (R8) |
| Equity | Training data demographic skew (R9), Differential reliability across subgroups (R10) |

**Top 3 risks (plain language):**

**Alert fatigue (R4)** — if the system produces too many low-value alerts, nurses will start ignoring all of them, including the correct ones. The Epic Sepsis Model required 109 alerts per genuine case before it was reformed.

**Distribution shift (R1)** — a model trained at Mercer will reflect Mercer's population. Deploying it at a different hospital without local revalidation is exactly the failure mode that produced the Epic Sepsis Model's real-world underperformance.

**Training data demographic skew (R9)** — solving the Caribbean data gap with one urban dataset relocates the generalisability problem rather than solving it. Obermeyer et al. (2019) sharpen this further: even within a locally sourced dataset, biased proxy variables can reproduce the same inequity the project exists to avoid.

---

## AI-Harm Case Study

**Epic Sepsis Model (Epic Systems Corp., deployed 2017–present)**

A proprietary sepsis early-warning tool deployed at hundreds of US hospitals on the strength of internal validation figures, without mandatory external validation before go-live.

External validation by Wong et al. (2021) at Michigan Medicine found:
- Sensitivity: **33%** (missed 2 in 3 sepsis cases)
- Positive Predictive Value: **12%** (109 alerts per true positive)
- AUC: **0.63** (vs. Epic's reported 0.76–0.83)

Root cause: single-site training assumed to generalise everywhere; design flaw where receipt of antibiotics (already-caught sepsis) was used as a predictive input; no mandatory local revalidation gate.

Full root-cause analysis: `docs/ai-harm-case-study.md`

---

## New Papers This Week (11 → 15)

| # | Authors | Year | Why Added |
|---|---------|------|-----------|
| 12 | Obermeyer et al. | 2019 | Algorithmic bias through proxy variables (underpins R2, R9) |
| 13 | World Health Organization | 2021 | WHO ethics & governance guidance; human-in-the-loop principle (underpins R6) |
| 14 | Wong et al. | 2021 | Epic Sepsis Model external validation; primary source for harm case study |
| 15 | Habib, Lin & Grant | 2021 | Editorial on mandatory external validation before deployment |

---

## Stance on AI Augmentation vs Replacement

The position taken throughout this project:

> AI in clinical triage at Mercer is a decision *support* tool, never a decision *replacement*. The WHO (2021) guidance is clear: ultimate responsibility for clinical decisions rests with the human professional, not the system. This is not only an ethical position — it is a design requirement. Risk 6 (automation bias) is a named, monitored risk precisely because framing a tool as support while designing it to behave like a replacement will produce the same harm regardless of what the documentation says.

A near-zero override rate is not a success metric. It may indicate that nurses have stopped questioning the system — which is the opposite of a healthy human-in-the-loop relationship.

---

## Files

| File | Description |
|------|-------------|
| `docs/assignment-13/` | Interim submission — risk register and harm case study |
| `docs/assignment-14/` | Final proposal with Risk Analysis section |
| `docs/ai-harm-case-study.md` | Standalone root-cause analysis of the Epic Sepsis Model |
| `docs/risk-register.md` | Standalone risk register (also committed as `.csv` format) |

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
