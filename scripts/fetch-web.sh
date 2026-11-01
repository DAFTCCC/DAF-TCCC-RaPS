#!/usr/bin/env bash
# Download the pinned RaPS web app (web-app.lock) into .web-src/.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
# shellcheck source=/dev/null
source <(grep -E '^WEB_(REPO|COMMIT)=' "$ROOT/web-app.lock")
: "${WEB_REPO:?WEB_REPO missing from web-app.lock}"
: "${WEB_COMMIT:?WEB_COMMIT missing from web-app.lock}"
[[ "$WEB_COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "WEB_COMMIT must be a full 40-character commit SHA"; exit 1; }

SRC="$ROOT/.web-src"
rm -rf "$SRC" && mkdir -p "$SRC"
git -C "$SRC" init -q
git -C "$SRC" remote add origin "$WEB_REPO"
git -C "$SRC" fetch -q --depth 1 origin "$WEB_COMMIT"
git -C "$SRC" checkout -q FETCH_HEAD
GOT=$(git -C "$SRC" rev-parse HEAD)
[ "$GOT" = "$WEB_COMMIT" ] || { echo "Fetched $GOT, expected $WEB_COMMIT"; exit 1; }
echo "RaPS web app fetched at ${WEB_COMMIT:0:7}"
