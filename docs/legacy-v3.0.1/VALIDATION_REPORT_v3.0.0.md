# Validation Report — TCCC Evaluation Suite v3.0.0

## Result
**PASS — source/package validation complete.**

## Automated release validation
- `scripts/validate-content.mjs`: PASS
- `scripts/validate_hardening.py`: **59/59 PASS**
- JavaScript syntax validation: PASS

### Tier content counts
- Tier 1 ASM: 33 criteria / 17 critical / 3 timers
- Tier 2 CLS: 71 criteria / 16 critical / 3 timers
- Tier 3 CMC: 124 criteria / 28 critical / 7 timers
- Tier 4 CPP: 124 criteria / 30 critical / 9 timers

Total: **352 criteria / 22 timers**.

## Non-regression comparison vs v2.21.2
Programmatic comparison confirmed:
- all Tier 1–4 `sections` are identical,
- all timer definitions are identical,
- all instant-event definitions are identical,
- `installations.js` is byte-identical,
- `branding.js` is byte-identical,
- APK GitHub build workflows are unchanged.

The intentional Tier metadata changes are limited to removal of the N/O rating option and corresponding instruction/pass-rule wording.

## Legacy record migration / reopen test
A runtime VM smoke test loaded a representative legacy v2.x database containing an `N/O` criterion and verified:
- database schema migration succeeds,
- legacy N/O becomes blank/unresolved,
- original legacy value is retained under `legacyRatings`,
- saved tier snapshot no longer exposes N/O,
- OBSERVE mode defaults correctly,
- stable class/student/attempt IDs are retained,
- class/participant/attempt linkage is populated,
- device ID remains stable across a simulated application reopen,
- created/modified/version/content/sync metadata is present,
- `syncStatus` remains `LOCAL`.

## Responsive layout test
Representative v3 operational UI was rendered headlessly at:
- 320 × 640 — small phone
- 390 × 844 — typical Android phone
- 768 × 1024 — tablet
- 1366 × 768 — desktop/browser-width reference

After the final typography correction:
- no horizontal document overflow,
- no tested control text clipping,
- no tested badge/button vertical clipping,
- no tested operational control below the 12 px target,
- no tested button exceeded 76 px height.

This was a representative rendered-layout test using the production stylesheet and operational markup. The execution environment blocks direct browser navigation to localhost/file URLs, so this is not represented as a full end-to-end browser navigation test.

## Offline/static dependency validation
- All local `src`/`href`/CSS asset references resolve.
- No external web resource is required by the evaluator shell.
- App Content Security Policy retains `connect-src 'none'`.
- No `fetch()` or `XMLHttpRequest` network transport exists in evaluator app logic.

## Android preparation smoke test
The native branding and Android hardening scripts were run against a generated-like Android tree and verified:
- launcher/splash resources applied,
- `versionName "3.0.0"`,
- `versionCode 30000`,
- `android:allowBackup="false"`,
- `android:usesCleartextTraffic="false"`,
- INTERNET permission removed.

## Limitation
A complete Gradle/Android APK build was not executed inside this container. The GitHub workflow remains the authoritative end-to-end Android build environment.
