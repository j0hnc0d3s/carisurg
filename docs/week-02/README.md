# Week 2 — Project Setup & Documentation

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 2 is the engineering-hygiene week. The focus shifts from content to structure — version control, reference management, and repository organisation. The deliverable is an audit-ready GitHub repository that a Mercer colleague could clone and understand within 60 seconds, alongside an updated Week 1 proposal with a fully auto-generated bibliography.

No new dataset this week. All work builds on Weeks 0 and 1.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 09 | `docs/assignment-09` | Proposal | Updated Week 1 proposal — auto-generated bibliography, 7 papers (Week 1's 5 + 2 new) |

---

## What Was Done This Week

**Reference Management**
All 7 Week 1 papers imported into Zotero. Bibliography auto-generated in APA 7th edition via the Zotero Google Docs plugin. Zero manually-typed citations remain in the Week 1 proposal.

**Repository Restructure**
The `carisurg-portfolio` repo was restructured to include:
- `README.md` — portfolio-level overview
- `LICENSE` — MIT licence
- `.gitignore` — Python/Jupyter/Colab starter template
- `requirements.txt` — pinned library versions
- `week-00/notebooks/` — Week 0 Jupyter notebooks
- `week-00/docs/` — Week 0 write-ups
- `week-01/docs/` — Week 1 literature review and proposal
- `data/` — empty, with README explaining dataset provenance

**Version Control Workflow**
Feature branch `feat/week-0-refactor` created, at least 3 meaningful commits made, pull request opened and merged to `main`.

---

## New Papers Added (Week 2)

Two papers added to the Zotero library and integrated into the updated proposal:

| # | Authors | Year | Source |
|---|---------|------|--------|
| 6 | Ueareekul et al. | 2025 | Scientific Reports |
| 7 | Bhattarai et al. | 2024 | International Journal of Emergency Medicine |

**Bhattarai et al.** is the most directly relevant addition — it documents triage implementation at a Pacific Small Island Developing State hospital, providing direct precedent for building a digital triage capture tool in a paper-based resource-limited ED.

**Additional seeded paper from CariSurg:**
De Freitas, L., Goodacre, S., O'Hara, R., Thokala, P., & Hariharan, S. (2020). Qualitative exploration of patient flow in a Caribbean emergency department. *BMJ Open, 10*(12), e041422.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
