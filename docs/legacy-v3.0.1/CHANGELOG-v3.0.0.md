# Changelog — v3.0.0

## Baseline
Built from TCCC APK **v2.21.2**.

## Field-requested changes
1. Renamed Field Mode / Review Mode to segmented **OBSERVE | REVIEW**.
2. OBSERVE minimizes documentation/admin content while preserving live grading, timers, current criterion, score, unresolved count, phase navigation, and Next Unresolved.
3. REVIEW preserves detailed criterion/source information, notes, failure classification, timeline/history, sign-off, finalization, and individual exports.
4. Removed **N/O** as a selectable grading state. Blank now represents unresolved.
5. Added safe legacy N/O migration to blank/unresolved with legacy audit metadata retention.
6. Simplified failure modes to five evaluator-facing choices.
7. Renamed Primary Root Cause to **Primary Performance Contributor** and reduced contributor choices to five grouped categories.
8. Renamed user-facing root-cause analytics to **Observed Performance Contributors**.
9. Separated criterion performance-when-tested from Tested / NT exposure analytics.
10. Reorganized class exports into **Export Class Summary** + **More Exports ▾** without removing export functions.
11. Simplified startup disclosure around TRAINING USE ONLY / NO PHI-CUI / DATA STORED LOCALLY, with safeguards collapsed under View Safeguards.
12. Reorganized home navigation into **EVALUATE / MANAGE TRAINING / READINESS / PROGRAM**.
13. Increased operational typography/control sizing and added responsive three-state grading layout.
14. Added future-sync-ready local metadata only; no network/sync capability was introduced.

## Explicit non-changes
- No TCCC criterion text/order/criticality changes.
- No timer-definition changes.
- No scoring-threshold changes.
- No critical-failure-rule changes except the requested terminology/UI handling.
- No MAJCOM/base catalog changes.
- No cloud/backend/authentication/API changes.
- No removal of existing PDF/CSV/JSON exports.
- No launcher/splash branding changes.
