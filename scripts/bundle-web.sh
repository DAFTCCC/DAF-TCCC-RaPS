#!/usr/bin/env bash
# Copy exactly the files the web app ships from .web-src/ into www/.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
SRC="$ROOT/.web-src"
OUT="$ROOT/www"
[ -f "$SRC/index.html" ] || { echo "Run scripts/fetch-web.sh first"; exit 1; }

rm -rf "$OUT" && mkdir -p "$OUT"
cp "$SRC/index.html" "$SRC/styles.css" "$SRC/manifest.webmanifest" "$OUT/"
for f in "$SRC"/*.js; do cp "$f" "$OUT/"; done
cp -r "$SRC/assets" "$SRC/vendor" "$OUT/"
[ -d "$SRC/briefing" ] && cp -r "$SRC/briefing" "$OUT/"
git -C "$SRC" rev-parse HEAD > "$OUT/web-commit.txt"

# Capacitor injects its native bridge as an inline script into the page. Allow
# inline scripts in the Android bundle only; the APK serves just these local
# files, and the web deployment keeps the strict script-src 'self' policy.
grep -q "script-src 'self';" "$OUT/index.html" || { echo "Expected CSP not found in index.html"; exit 1; }
sed -i "s/script-src 'self';/script-src 'self' 'unsafe-inline';/" "$OUT/index.html"

# Every script the page loads must be present in the bundle.
missing=0
for src in $(grep -o 'src="[^"]*\.js' "$OUT/index.html" | sed 's/src="//; s/\?.*//'); do
  [ -f "$OUT/$src" ] || { echo "MISSING from bundle: $src"; missing=1; }
done
[ $missing -eq 0 ] || exit 1
for f in "$OUT"/*.js; do node --check "$f"; done
echo "Web bundle ready: $(find "$OUT" -type f | wc -l) files, RaPS $(grep -o "versionName: '[^']*'" "$OUT/version.js" | cut -d"'" -f2)"
