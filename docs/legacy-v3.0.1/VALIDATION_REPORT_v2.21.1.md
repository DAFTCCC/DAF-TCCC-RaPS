# Validation Report — TCCC v2.21.1 APK

## Result
- Hardening/release checks: **59/59 PASSED**
- TCCC content validation: **PASSED**
- JavaScript syntax validation: **PASSED** for app, tiers, installations, and branding.

## Timer-access checks
- Top CUF Tourniquet quick timer is present and bound to the existing CUF tourniquet timer definition/state.
- Active Timers includes a STOP control for each valid running/paused timer.
- Active Timers uses persistent event delegation, so STOP remains functional after the live timer list redraws.
- The Active Timers card remains phase-independent/sticky, supporting a timer started in M and stopped while viewing R or later phases.
- Recovery-integrity behavior remains unchanged: recovered/interrupted timers still require VOID/RESTART and cannot be stopped as a valid timing result.

## Unchanged from v2.21.0
SHA-256 comparison against the untouched v2.21.0 baseline confirmed these files are unchanged:
- `www/tiers.js` — all Tier 1–4 clinical criteria and timer definitions
- `www/installations.js`
- `www/branding.js`
- `.github/workflows/build-test-apk.yml`
- `.github/workflows/build-release-apk.yml`
- `scripts/harden-android.mjs`
- `scripts/prepare-android.mjs`
- `scripts/apply-android-native-branding.sh`

## Environment limitation
A full Chromium interaction test could not be completed in this execution environment because localhost navigation is administratively blocked. Source-level release checks, syntax validation, timer-state wiring assertions, and baseline SHA comparisons passed.
