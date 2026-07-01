# Week 3 — Healthcare Workflows & Systems Thinking

**CariSurg MedTech Pathways 2026 | Mercer General Hospital**

---

## Overview

Week 3 shifts from literature review to systems thinking. The task is to map the existing Mercer General ED triage workflow from door-to-disposition, identify where an AI tool could plausibly plug in, and name the three biggest constraints that would determine whether any such tool actually brings clinical value. The framing is direct: design *with* clinicians, not *at* them.

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

| # | Point | What It Does |
|---|-------|-------------|
| 1 | Registration/Triage | Digital Triage Capture Tool — THIS PROJECT, Phase 1 |
| 2 | ESI Decision | ESI Decision Support — Phase 2, future work |
| 3 | Fast-Track Waiting | Re-triage Alert — flags overdue re-checks |
| 4 | Physician Handoff | Structured Handover Prompt — auto-populates SBAR |
| 5 | Investigations | ⚠️ NOT a plug-in point — bottleneck risk |

---

## Three Workflow Constraints

**Constraint 1 — The 3–5 Minute Triage Window (Friction Budget)**
Any digital tool that takes longer than handwriting will be abandoned within days. The Phase 1 interface must replicate the paper form's speed, not add to it. Salwei et al. (2024) document exactly this failure mode in a real ED deployment.

**Constraint 2 — Paper-to-Digital Lag at the Point of Capture**
Structured digital data must exist at the moment of triage, not as a later transcription step. This is the foundational justification for the entire Phase 1 proposal.

**Constraint 3 — Shared Investigations Bottleneck**
Labs and radiology are shared hospital-wide. AI that increases test-ordering volume without addressing turnaround will worsen overcrowding — this rules out certain plug-in points entirely.

---

## Five Clinical Stakeholders

| Stakeholder | Role | Top Concern |
|-------------|------|-------------|
| Triage Nurse | Nurse | Making the right ESI call quickly; not missing a deteriorating waiting-room patient |
| ED Physician / Consultant | Consultant | Documentation burden; decision support that doesn't slow them down |
| EMS Crew | Porter/Transport | Clean SBAR handover; not waiting hours to clear their stretcher |
| Registration Clerk | Admin | Getting demographics right when the patient may be frightened or unable to communicate |
| Patient & Family | Patient Advocate | Being told what is happening, especially when activity appears slow |

---

## References Added This Week (11 total)

Poon et al. (2025), Salwei et al. (2024), and Chughtai & Blanchet (2017) added with a deployment and constraints focus.

---

*CariSurg MedTech Pathways 2026 — Building Caribbean Clinical AI Engineers*
