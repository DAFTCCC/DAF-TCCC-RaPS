# Validation Report — TCCC v2.21.2 APK

**Scope:** Timer-only update requested from v2.21.1.

## Release checks

- `scripts/validate_hardening.py`: **65/65 passed**
- `scripts/validate-content.mjs`: **passed**
- `node --check www/app.js`: **passed**
- `node --check www/tiers.js`: **passed**
- Android hardening dry-run produced **versionName 2.21.2 / versionCode 22102**, disabled backups/cleartext, and removed INTERNET permission.

## Surgical-diff verification

- Tier 1–4 criterion sections identical to v2.21.1: **TRUE**
- Existing v2.21.1 timer definitions unchanged: **TRUE**
- Only new runtime timer definitions: `asm_overall` and `cls_overall`.

- `www/app.js` unchanged: **TRUE**
- `www/index.html` unchanged: **TRUE**
- `www/styles.css` unchanged: **TRUE**
- `www/installations.js` unchanged: **TRUE**
- `www/branding.js` unchanged: **TRUE**
- `.github/workflows/build-test-apk.yml` unchanged: **TRUE**
- `.github/workflows/build-release-apk.yml` unchanged: **TRUE**
- `scripts/harden-android.mjs` unchanged: **TRUE**
- `scripts/apply-android-native-branding.sh` unchanged: **TRUE**

## Timer applicability audit

| Tier | Timer | Standard | Linked criterion | Section |
|---|---|---:|---|---|
| ASM | Overall Tactical Trauma Assessment | ≤ 30:00 | — | GLOBAL |
| ASM | CUF Tourniquet — Bleeding Control | ≤ 1:00 | ASM-009 | ASM |
| ASM | Wound Packing Pressure | ≥ 3:00 | ASM-017 | ASM |
| CLS | Overall Tactical Trauma Assessment | ≤ 30:00 | — | GLOBAL |
| CLS | CUF Tourniquet — Bleeding Control | ≤ 1:00 | CLS-001G | CUF |
| CLS | Wound Packing / Hemostatic Dressing Pressure | ≥ 3:00 | CLS-004C | M |
| CMC | Overall Tactical Trauma Assessment | ≤ 30:00 | — | GLOBAL |
| CMC | CUF Tourniquet — Bleeding Control | ≤ 1:00 | CMC-005 | CUF |
| CMC | Wound Packing Pressure | ≥ 3:00 | CMC-014 | M |
| CMC | NDC Catheter Hold | 5–10 sec | CMC-034 | R |
| CMC | Hypertonic Saline Administration | ≥ 10:00 | CMC-080 | H2 |
| CMC | HTS Repeat Interval — if no response | ≥ 20:00 | CMC-081 | H2 |
| CMC | Neurologic Reassessment Interval | 5–10 min | CMC-084 | H2 |
| CPP | Overall Tactical Trauma Assessment | ≤ 30:00 | — | GLOBAL |
| CPP | CUF Tourniquet — Bleeding Control | ≤ 1:00 | CPP-005 | CUF |
| CPP | Wound Packing Pressure | ≥ 3:00 | CPP-013 | M |
| CPP | NDC Catheter Hold | 5–10 sec | CPP-034 | R |
| CPP | Hypertonic Saline Administration | ≥ 10:00 | CPP-079 | H2 |
| CPP | HTS Repeat Interval — if no response | ≥ 20:00 | CPP-080 | H2 |
| CPP | Neurologic Reassessment Interval | 5–10 min | CPP-083 | H2 |
| CPP | Ketamine IV/IO Administration — when IV/IO option used | ≥ 1:00 | CPP-095 | P |
| CPP | Analgesia Repeat Interval — PRN | ≥ 30:00 | CPP-096 | P |

## Requested behavior verification

- **ASM Overall TTA:** added as a 30-minute global timer (`asm_overall`).
- **CLS Overall TTA:** added as a 30-minute global timer (`cls_overall`).
- **CMC Overall TTA:** retained unchanged (`cmc_overall`).
- **CPP Overall TTA:** retained unchanged (`cpp_overall`).
- **Top CUF Tourniquet quick control:** shared renderer finds the CUF tourniquet timer by label, so it applies to ASM, CLS, CMC, and CPP.
- **Cross-phase STOP:** Active Timers is generated from any running/paused timer in the current tier, independent of the selected CUF→EVAC phase; the STOP action uses the shared timer ID.
- **Advanced CMC/CPP timers:** retained only where the corresponding timed criteria exist; no NDC/HTS/neuro/analgesia timer was invented for ASM/CLS.

## No-change boundary

No functional changes were made to scoring, RCA, remediation, MAJCOM/base management, analytics, exports, PDF behavior, clinical criterion wording, branding, installation data, or GitHub APK workflows.
