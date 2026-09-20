# TCCC Evaluation Suite v2.21.1 — APK

## Scope
This release intentionally changes **timer access only**. It retains the v2.21.0 clinical content, grading/scoring, RCA, remediation, MAJCOM/base management, analytics, exports, branding, and GitHub build workflows.

## Changes
1. **Cross-phase Active Timer STOP**
   - Every running or paused timer listed in **Active Timers** now has a STOP button.
   - The Active Timers card remains outside the phase-specific checklist, so a timer started in one phase can be stopped after navigating to another phase (for example, Wound Packing Pressure started in M and stopped while viewing R).
   - STOP uses the existing timer action and grading logic; no timing standards or timer definitions were changed.
   - Recovered/interrupted timers remain protected and cannot be stopped as if they were valid. They still require VOID/RESTART.

2. **Top CUF Tourniquet quick timer**
   - A duplicate CUF Tourniquet timer card is shown at the top of the evaluator before the checklist content.
   - It uses the exact same timer ID/state as the existing CUF-linked timer; it does not create a second timing record.
   - Starting/stopping/resetting from either copy updates the same timer instance.

## Version
- versionName: `2.21.1`
- versionCode: `22101`
