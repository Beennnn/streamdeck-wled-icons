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

## Notes / open decisions

- **fps**: effects run ~8 fps (WLED source cadence) — below Elgato's soft
  10–20 fps guidance. Validates fine (warnings only). Leave as-authored unless
  review flags it.
- Presented as standalone WLED-*concept* icons — no plugin/controller link for
  now (deliberate).
