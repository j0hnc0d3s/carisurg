# Week 1 — Research Fundamentals

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 1 shifts from data cleaning to research literacy. The deliverable is a preliminary proposal for a 12-week pilot project, written for Dr. De Fretias and the Mercer General ED Board — not for a journal. Short, scannable, referenced.

The core argument: Caribbean EDs like Mercer General run on paper triage forms, generating no structured data. Before any AI triage tool can be built or validated locally, a digital data foundation must exist first.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 07 | `docs/assignment-07` | Write-up | Paper summaries — 7 papers on AI-assisted triage |
| 08 | `docs/assignment-08` | Proposal | Preliminary proposal — problem statement, previous work, proposed solution, references |

---

## Problem Statement

> *Emergency departments in resource-constrained Caribbean settings like Mercer General Hospital operate on paper-based triage systems that generate no structured, queryable data. Without a digital foundation, locally validated AI triage tools cannot be built, and globally trained models — developed predominantly on North American and European patient populations — cannot be reliably applied. This project proposes to establish a structured digital triage dataset from the Mercer General ED as the necessary first step toward a clinically credible, regionally relevant AI-assisted triage classifier.*

---

## Two Gaps Identified

**Gap 1 — Caribbean and small-island developing state representation**
Virtually no validated AI triage studies exist from Caribbean or SIDS contexts. Most reviews restrict to US, European, or East Asian datasets. This is not a gap of absence — it is a gap of exclusion. Tools have been tried and validated elsewhere; the question of whether they transfer to the Caribbean has simply not been asked.

**Gap 2 — Infrastructure assumption mismatch**
Most AI triage systems assume EHR infrastructure, stable power, and internet connectivity. These assumptions do not hold at paper-based EDs like Mercer. The models exist; the preconditions for deploying them do not. A system built for Mercer must be designed around the constraints of the setting, not retrofitted from a high-resource context.

---

## Papers Reviewed

| # | Authors | Year | Source |
|---|---------|------|--------|
| 1 | Tyler et al. | 2024 | Cureus |
| 2 | Da'Costa et al. | 2025 | International Journal of Medical Informatics |
| 3 | Araouchi & Adda | 2024 | Procedia Computer Science |
| 4 | Yi, Baik & Baek | 2025 | Journal of Nursing Scholarship |
| 5 | Abdalhalim et al. | 2025 | ResearchSquare (Preprint) |
| 6 | Ueareekul et al. | 2025 | Scientific Reports |
| 7 | Bhattarai et al. | 2024 | International Journal of Emergency Medicine |

References managed in Zotero. Bibliography auto-generated in APA 7th edition.

---

## Proposed Solution

**Phase 1 (12-week pilot):** Design and validate a structured digital triage capture tool aligned with the existing Mercer General paper triage form. Deliverable is a clean, de-identified, queryable dataset from real ED encounters — not an AI model.

**Phase 2 (beyond this programme):** Use the Phase 1 dataset to train and locally validate a rule-based ESI classifier, iterating toward a machine learning model as data volume grows.

The Phase 1 deliverable is the foundation. The AI comes second.

---

## Additional Paper — Dr. De Fretias (Week 2)

De Freitas, L., Goodacre, S., O'Hara, R., Thokala, P., & Hariharan, S. (2020). Qualitative exploration of patient flow in a Caribbean emergency department. *BMJ Open, 10*(12), e041422. https://doi.org/10.1136/bmjopen-2020-041422

This paper, written by the programme's Clinical Sponsor, documents patient flow patterns at a Caribbean ED and directly informs the operational constraints the proposed digital tool must respect.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*