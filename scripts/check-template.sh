#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="/tmp/copier-python-template-test"

rm -rf "$OUT_DIR"

copier copy "$ROOT_DIR" "$OUT_DIR" --trust <<EOF
demo-app
3.12
package
flat
EOF

cd "$OUT_DIR"
find . -maxdepth 4 | sort
