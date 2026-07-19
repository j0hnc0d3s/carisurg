# Week 3 — Stakeholder Workflow & Constraints

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 3 moves the project from literature to the actual floor of the Mercer General ED. The task is to map the existing triage workflow from door-to-disposition, identify where an AI tool could plausibly plug in, and name the three biggest constraints that would determine whether any such tool actually brings clinical value. The framing is direct: design *with* clinicians, not *at* them.

Sister Patrice Alleyne, ED Nurse-in-Charge with 20 years of experience, is the lens through which every design decision is tested. If it wouldn't survive a night shift, it doesn't belong in the proposal.

---

## Assignments

| # | Folder | Type | Description |
|---|--------|------|-------------|
| 11 | `docs/assignment-11` | Interim | Draft workflow notes + initial diagram + 3 candidate constraints |
| 12 | `docs/assignment-12` | Final Proposal | Refined proposal with diagram, constraints & stakeholders section, 11 references |

---

## Workflow Summary

The Mercer General ED follows a door-to-disposition pathway with five measured timestamps: arrival, triage, seen-by-physician, disposition decision, and exit.

| Stage | Duration | Key Data Captured |
|-------|----------|-------------------|
| Arrival | — | None yet |
| Registration | 2–3 min | Demographics, consent — paper intake form |
| Triage Assessment | 3–5 min | Vitals, chief complaint, ESI level — paper front page |
| Zone Placement | — | ESI 1–3 → bed; ESI 4–5 → fast-track waiting |
| Physician Assessment | ESI 2: ≤10 min / ESI 3: 30–60 min | History, exam, orders — deeper clinical pages |
| Investigations | 30 min – 3 hr | Labs/imaging — shared hospital resource |
| Disposition Decision | At end of workup | Admit / discharge / transfer |
| Exit | Variable | Boarding delay if admitted |

**Key information loss points:**
- The triage front page (ESI, vitals) is consistently completed; deeper clinical pages are not
- Re-triage depends entirely on a nurse visually scanning the waiting room — no structured trigger exists
- Investigations are the dominant flow bottleneck (shared with elective inpatient demand)

---

## Workflow Diagram

`docs/assignment-12/workflow_diagram.png` — rendered from the Mermaid source committed below.
`docs/assignment-11/workflow_diagram.mmd` — Mermaid source (renders automatically on GitHub).

The diagram annotates five AI plug-in points (numbered 1–5), including one explicit **non-plug-in point** at the Investigations stage — AI that increases test-ordering without addressing turnaround would worsen the queue, not relieve it.

---

## Three Constraints

**Constraint 1 — Front-Page Speed**
Any digital tool that asks for more fields than the existing paper form, or takes more time than handwriting, will be abandoned within days — regardless of how good the underlying model is. This directly shapes the interface design for the Phase 1 capture tool: it must replicate the paper form's speed, not add to it.

**Constraint 2 — Paper-to-Digital Lag at the Point of Capture**
All triage data currently exists only on paper, and even there, only the front page (ESI, vitals) is reliably completed. Before any classifier — rule-based or ML — can be trained or validated, structured digital data must exist at the moment of capture, not as a later transcription step prone to loss and delay. This is the foundational justification for the entire Phase 1 proposal.

**Constraint 3 — Shared Investigations Bottleneck**
Labs and radiology are shared hospital-wide resources with 30-minute to 3-hour turnaround, and ED workups compete directly with elective inpatient demand. This is the dominant flow bottleneck at Mercer. Any AI design that increases test-ordering volume without addressing turnaround capacity will worsen overcrowding rather than relieve it — this constraint actively rules out certain plug-in points (see the Investigations stage above) rather than just shaping their design.

---

## Glossary

`docs/GLOSSARY.md` — a standalone index of clinical, technical, and research abbreviations used across the whole proposal (not just Week 3), so any reviewer — clinical or non-clinical — can look something up without breaking flow.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
