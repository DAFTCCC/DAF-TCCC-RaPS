# TCCC Evaluation Suite v2.21.2 — Timer Coverage Update

This is a surgical timer-only update on v2.21.1.

## Requested changes implemented

1. Added an **Overall Tactical Trauma Assessment (TTA)** timer to Tier 1 (ASM).
   - 30-minute maximum (`≤ 30:00`)
   - START TTA / STOP TTA
   - global timer behavior matches the existing CMC/CPP TTA timer
   - appears in the existing Overall TTA Clock card and Active Timers panel

2. Added the same **Overall TTA** timer to Tier 2 (CLS).
   - 30-minute maximum (`≤ 30:00`)
   - START TTA / STOP TTA
   - global timer behavior matches the existing CMC/CPP TTA timer

3. Audited timer applicability across ASM → CLS → CMC → CPP.
   - CUF tourniquet timer is present in all four tiers.
   - Wound packing/pressure timer is present in all four tiers.
   - NDC/HTS/neuro timers remain only in CMC/CPP where the corresponding timed standards exist.
   - CPP ketamine/analgesia timers remain only in CPP where the corresponding timed standards exist.
   - The v2.21.1 cross-phase Active Timers STOP control remains shared across all tiers.
   - The v2.21.1 top CUF Tourniquet quick control remains shared across all tiers and controls the same underlying timer instance as the criterion timer.

## Intentionally unchanged

No changes were made to:
- criterion wording, order, criticality, or source references,
- PASS / FAIL / NT / N/O scoring,
- RCA or remediation logic,
- MAJCOM/base/location management,
- class/program analytics,
- exports,
- PDF behavior,
- branding/icon/splash resources,
- Android build workflow behavior,
- timer definitions already present in v2.21.1 (other than adding the two requested TTA global timers).

**Version:** 2.21.2  
**Android versionCode:** 22102
