# Marketplace submission — WLED icon packs

Everything is prepared. The **final submit on
[maker.elgato.com](https://maker.elgato.com) needs Benoît's Elgato login** (+ the
Maker Agreement on first use) — that step is yours. Full process detail lives in
[stream-deck-icons/docs/publishing.md](https://github.com/Beennnn/stream-deck-icons/blob/main/docs/publishing.md);
this file is the pack-specific cheat sheet.

## Build the artifacts

```sh
bin/build.sh                                   # → dist/*.streamDeckIconPack (both packs)
# per-pack Maker Console media (thumbnail 1920×960, 5 previews 144×144, gallery):
sdicons maker-media effects  --out-dir maker-media/effects \
  --title "WLED Effects" --subtitle "216 animated effects for Stream Deck" \
  --previews rainbow,fire-2012,geq,ps-fireworks,matrix
sdicons maker-media palettes --out-dir maker-media/palettes \
  --title "WLED Palettes & Controls" --subtitle "111 palette & control icons" \
  --previews palette-lava,palette-aurora,palette-rainbow,palette-sunset,palette-ocean
```

`dist/` and `maker-media/` are gitignored — regenerate any time.

## Two submissions (one per pack)

| | WLED Effects | WLED Palettes & Controls |
|---|---|---|
| Package | `dist/com.beennnn.wledeffects.streamDeckIconPack` | `dist/com.beennnn.wledpalettescontrols.streamDeckIconPack` |
| Icons | 216 animated GIF | 111 static PNG |
| **Animated?** | **Yes** | **No** |
| Style | Illustrated | Illustrated |
| Media | `maker-media/effects/` | `maker-media/palettes/` |
| Price | Free | Free |

## Wizard checklist (per pack)

1. **Details** — Name/Description from `manifest.json`. Set **Animated = yes**
   for Effects, **no** for Palettes. Style = Illustrated. Type/Theme/Colour
   multi-selects are flaky — persist. Free (locked after submit).
   - **AI-content disclosure**: the art is programmatically generated (SVG
     stencils + scripted GIFs from wled-assets), Claude-assisted. Decide whether
     that counts as AI-generated for Elgato's checkbox and tick accordingly.
2. **Upload media** — drag from `maker-media/<pack>/`: thumbnail
   (`thumbnail-1920x960.png`), the 5 `preview-*.png`, and ≥3 `gallery-*.png`.
   Native Finder→page drops — must be done by hand.
3. **Submit for review** — release notes required (e.g. "Initial release —
   the complete WLED effect / palette set as Stream Deck icons"). Auto-publish
   toggle optional. **Submit is your final click.**

## Re-submit after the 2026-07-14 v1 rejection (both packs)

Both packs were rejected the same day: *"ensure there was no cropping of
information, please ensure all media for Marketplace is 1920×960."* Root cause:
the gallery generator packed 3 rows of 6 into the 960 px canvas with tiles too
tall, so each `gallery-N.png` had its **bottom row sliced** (the file was 1920×960,
but the content overflowed). Fixed in `sdicons/makermedia.py` (tile 250→220,
y0 250→190 → 3 full rows fit: 190 + 3·220 + 2·24 = 898 ≤ 960). Media regenerated.

To clear it: **Media tab → replace every gallery image** with the freshly
regenerated `maker-media/<pack>/gallery-*.png` (12 for effects, 7 for palettes),
re-check the thumbnail, then **Versions → Submit for review** again. Nothing else
changed (description, previews, package all already accepted).

## Notes / open decisions

- **fps**: effects run ~8 fps (WLED source cadence) — below Elgato's soft
  10–20 fps guidance. Validates fine (warnings only). Leave as-authored unless
  review flags it.
- Presented as standalone WLED-*concept* icons — no plugin/controller link for
  now (deliberate).
