#!/usr/bin/env bash
# Build both WLED icon packs from the vendored src/ using the sdicons toolkit.
#
# Effects are animated GIFs (NEAREST upscale keeps the LED pixel grid crisp);
# palettes/controls are static PNGs (LANCZOS). Outputs land in dist/ as
# submit-ready .streamDeckIconPack files. Re-runs are idempotent — hand-tuned
# names/tags in each pack's tags.json survive.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

# Locate sdicons: PATH first (pip install -e), then the sibling clone.
if command -v sdicons >/dev/null 2>&1; then
  SDICONS=sdicons
elif [ -x "$HOME/dev/music/stream-deck-icons/bin/sdicons" ]; then
  SDICONS="$HOME/dev/music/stream-deck-icons/bin/sdicons"
else
  echo "error: sdicons not found (clone Beennnn/stream-deck-icons as a sibling," \
       "or pip install -e it)" >&2
  exit 1
fi

echo "▶ WLED Effects (216 animated GIFs, nearest upscale)"
"$SDICONS" build src/effects effects

echo
echo "▶ WLED Palettes & Controls (111 static PNGs)"
"$SDICONS" build src/palettes palettes

echo
echo "✓ done — packs in dist/:"
ls -1 dist/*.streamDeckIconPack 2>/dev/null || true
