# DAF-TCCC-RaPS — Android app

This repository builds the **RaPS Android app (APK)**. The app is the RaPS web
app from [DAF-TCCC-RaPS-WEB](https://github.com/DAFTCCC/DAF-TCCC-RaPS-WEB)
packaged with Capacitor: same grading logic, same server, same sign-in.

The web code is **not copied** here. `web-app.lock` pins the exact web app
commit each APK ships, and the build downloads it. The web repository stays
web-only, and there is one copy of the grading logic.

| | |
|---|---|
| App ID | `org.daftccc.raps` |
| Ships | RaPS web app at the commit in `web-app.lock` |
| Version | RaPS version name (e.g. `3.4.13-web.5`); versionCode = RaPS versionCode × 100 + web number |
| Builds | GitHub Actions: test APK on every pull request; signed APK + GitHub Release on `main` |

## Releasing a new web version as an APK

1. Merge the web change in DAF-TCCC-RaPS-WEB.
2. Here, on a branch: `bash scripts/pin-web.sh main` (or a full commit SHA).
3. Open a pull request. CI attaches a test APK to the run.
4. Merge. CI publishes `android-v<version>` on the Releases page.

Each RaPS version is released once; bump the web version before re-releasing.

## Layout

| Path | Purpose |
|---|---|
| `web-app.lock` | Web repo URL and pinned commit |
| `scripts/fetch-web.sh` | Downloads the pinned web app into `.web-src/` |
| `scripts/bundle-web.sh` | Copies the shipped files into `www/`, allows Capacitor's inline bridge in the APK's CSP only, checks every script is present |
| `scripts/prepare-android.sh` | Generates the Android project, applies branding, version and hardening |
| `scripts/harden-android.mjs` | Version, backups off, cleartext off, INTERNET kept for sync |
| `native-android-res/` | Launcher icon and splash screen |
| `.github/workflows/android.yml` | CI build and release |
| `docs/ANDROID-APP.md` | Installing, signing key setup, how the build works |
| `docs/legacy-v3.0.1/` | Notes from the earlier offline-only TCCC Evaluation Suite APK (v3.0.1) |

`www/`, `.web-src/` and `android/` are generated and not committed.

## Earlier offline-only app (v3.0.1)

Before this change, this repository held the standalone, offline-only
**TCCC Evaluation Suite** (app ID `org.tccc.evaluationsuite`). Its source is in
the git history (commit `11a4eac`). The RaPS app has a different app ID, so it
installs **alongside** the old app and never overwrites records stored in it.

## Local build

Requires Node 20+, JDK 21 and the Android SDK.

```bash
npm install
npm run android:debug   # APK at android/app/build/outputs/apk/debug/
```
