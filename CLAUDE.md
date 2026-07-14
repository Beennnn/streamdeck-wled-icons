# CLAUDE.md — streamdeck-wled-icons

Project-specific rules. The global `~/.claude/CLAUDE.md` applies too (git
workflow, storage tiers, autonomy, French chat, English commits/docs).

## What this is

Two Elgato Stream Deck **icon packs** built from the WLED visual set:
- `effects/` — 216 animated effect GIFs (144×144, looping).
- `palettes/` — 111 static PNGs (72 palettes + controls + segment + nightlight
  + buttons + 11 concept tiles).

**Content repo, not a tool.** The pipeline lives in
[stream-deck-icons](https://github.com/Beennnn/stream-deck-icons) (`sdicons`);
this repo is source assets + per-pack metadata. Sibling of `stream-deck-icons`
and `streamdeck-stage-keys` (the GM/XP keyboardist pack — same pattern) in the
`music` group. Source of the icons: [openlamp/wled-assets](https://github.com/openlamp/wled-assets)
(CC0), which is where the icon *art* is authored/curated — fix visuals THERE,
then re-vendor here, never hand-edit `src/`.

## Layout

- `src/effects/*.gif`, `src/palettes/*.png` — **committed** vendored sources
  (so `bin/build.sh` runs without a wled-assets checkout).
- `effects/`, `palettes/` — pack roots: `manifest.json`, `tags.json`,
  `icon.svg` (thumbnail), `license.txt`. Generated `icons/`, `icons.json`,
  `contact-sheet.png`, `dist/` are **gitignored** (reproduce with build).
- `bin/vendor.py` — regenerates `src/` + both `tags.json` from wled-assets
  canonical data (`data/effects.json` ordered by effect id, `data/palettes.json`,
  `animations/families.json` for the motion tag). Dev-only.
- `bin/build.sh` — runs `sdicons build` on each pack → `dist/*.streamDeckIconPack`.
  Finds `sdicons` on PATH or in the sibling clone.

## Conventions & gotchas

- **Never hand-edit `src/`** — it's vendored. Edit art in wled-assets, then
  `python3 bin/vendor.py`. Hand-tuning names/tags is fine in `tags.json`
  (survives re-vendor only if you also update vendor.py's mapping).
- Static filenames are **category-prefixed** (`palette-lava`, `control-speed`,
  `concept-effects`…) so 111 icons across 6 categories keep unique paths in one
  pack. Display names stay clean ("Lava", "Speed").
- **fps warnings are expected & accepted**: WLED source GIFs run ~8 fps
  (125 ms/frame) by design, below Elgato's soft 10–20 fps guidance. Warnings,
  not errors — the packs validate. Do NOT retime to silence them; that changes
  the intended motion speed. If a pack ever needs faster playback, add a `--fps`
  retime to `sdicons`, don't fudge durations by hand.
- Two packs = two Marketplace submissions (animated vs static). Version them
  independently in each `manifest.json`.
- Commits + README + docs in **English** (public GitHub repo). Chat FR.

## Publishing

Same process as any `sdicons` pack — see
[stream-deck-icons/docs/publishing.md](https://github.com/Beennnn/stream-deck-icons/blob/main/docs/publishing.md):
`bin/build.sh` → `dist/*.streamDeckIconPack` is submit-ready; `sdicons
maker-media <pack>` generates the Maker Console upload assets. Effects submit
as **animated**, palettes as **not-animated**.
