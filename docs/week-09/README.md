# Week 9 — Designing & Prototyping a Human-Centred System

CariSurg MedTech Pathways 2026 · Mercer General Emergency Department

Deployment planning for the triage classification model (logistic regression baseline,
`class_weight='balanced'`, top-10 features, ESI-1 recall 0.750 on the Yale EMMLC dataset)
across two candidate settings:

- **Setting A** — ED Triage Desk (HCI, screen-based)
- **Setting B** — Observation Unit kiosk (HRI, physically co-present with the patient)

## Mock-ups

**Setting A — `In Figma`**
One frame showing the triage desk screen: three patients at different acuity levels
(red / amber / green), each carrying colour + icon + text label so acuity never rides on
colour alone, plus a visible, logged override control on the highest-acuity card.

**Setting B — `In TinkerCAD`**
Front view and top-down floor placement of the Observation Unit kiosk: sensor array,
status display (active/idle/fault), fixed base, and the hardware-enforced proximity
guard, shown relative to the existing vitals station and patient bed.

**Tool note:** both mock-ups were produced as annotated SVG/PNG rather than native Figma
or TinkerCAD files. They cover the same content the tutorial's minimum bar asks for —
three-patient triage queue with colour+shape alert states and a visible override for
Setting A; footprint, height, and major components (screen, sensor array, base,
proximity guard) with front/top views for Setting B — but are **not** `.fig` or `.stl`
files. If the rubric checks for those specific formats, these need to be rebuilt
natively in Figma and TinkerCAD before final submission.

**View-access link:** _not applicable — no Figma/Canva file was created for this pass.
Add a view-only link here if/when the mock-ups are rebuilt natively._

## Co-design canvas, requirements & safety

`assignment-22.docx` contains, for both settings:

- Canvases 01–06 (Problem Space, Ethical Considerations, Guidelines, Robot Design MVP,
  Environment, Form), reproducing the grid structure of the
  [Social Robot Co-Design Canvases](https://github.com/minjaaxelsson/social_robot_co-design_canvases)
  (Axelsson et al., 2021), CC BY-SA 4.0 — see Attribution below.
- System requirements (functional / non-functional / integration)
- Safety considerations (3 HCI + 3 HRI, Concern/Context/Mitigation/Residual Risk format)
- Failure-mode table (power loss, connectivity loss, sensor failure, user error, low
  model confidence)
- Two-minute walk-through video script outline

**Known gap:** Canvas 03 (Guidelines) field labels could not be verified against the raw
template PDF — the content follows the tutorial's description of that canvas's purpose
rather than the literal printed layout used for the other five canvases.

## Submission checklist (per Tutorial 5)

- [ ] Canvas PDFs committed (export the .docx canvases to PDF)
- [x] Mock-up files committed (SVG/PNG — confirm if native Figma/TinkerCAD required)
- [x] System requirements document
- [x] Safety one-pager
- [ ] 2-minute walk-through video recorded and posted to Discord (#week9-submissions) and LinkedIn
- [ ] All files pushed to `carisurg-portfolio/week9/` before Tuesday 11:59 p.m. AST

## Attribution

Canvases 01–06 in `assignment-22.docx` reproduce the grid structure
of the **Social Robot Co-Design Canvases (SoRoCo Canvases)**, free version, by Minja
Axelsson, licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), sponsored by Futurice.

Cite as: Axelsson, M., Oliveira, R., Racca, M., & Kyrki, V. (2021). Social robot
co-design canvases: A participatory design framework. *ACM Transactions on Human-Robot
Interaction (THRI)*, 11(1), 1–39.

Original canvases: <https://osf.io/jg2t8/> and
<https://github.com/minjaaxelsson/social_robot_co-design_canvases>.
