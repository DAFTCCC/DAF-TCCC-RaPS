#!/usr/bin/env bash
# Point the APK at a different RaPS web app commit.
# Usage: bash scripts/pin-web.sh <commit-sha | branch>   (default: main)
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
REF=${1:-main}
REPO=$(grep -E '^WEB_REPO=' "$ROOT/web-app.lock" | cut -d= -f2-)
if [[ "$REF" =~ ^[0-9a-f]{40}$ ]]; then
  SHA=$REF
else
  SHA=$(git ls-remote "$REPO" "refs/heads/$REF" | cut -f1)
  [ -n "$SHA" ] || { echo "Branch '$REF' not found in $REPO (use a full commit SHA otherwise)"; exit 1; }
fi
sed -i "s/^WEB_COMMIT=.*/WEB_COMMIT=$SHA/" "$ROOT/web-app.lock"
echo "web-app.lock now pins $SHA"
