#!/usr/bin/env bash
# Generate a clean Capacitor Android project from www/ and apply branding,
# version and hardening. Run after scripts/fetch-web.sh and scripts/bundle-web.sh.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f www/index.html ] || { echo "www/ is empty; run npm run web first"; exit 1; }
rm -rf android
npx cap add android
npx cap sync android
bash scripts/apply-android-native-branding.sh
node scripts/harden-android.mjs

M=android/app/src/main/AndroidManifest.xml
grep -q 'android:allowBackup="false"' "$M"
grep -q 'android:usesCleartextTraffic="false"' "$M"
grep -q 'android.permission.INTERNET' "$M"
test -f android/app/src/main/assets/public/index.html
echo "Android project ready"
