# Changelog — WLED icon packs

Two packs live in this repo and are versioned together: **WLED Effects**
(216 animated GIF) and **WLED Palettes & Controls** (111 static PNG).

## v1 — resubmission (2026-07-14)

Both packs were **rejected** on their first Maker Console submission (2026-07-14):
> *"We'd like to see the media for the product page updated to ensure there was
> no cropping of information, please ensure all media for Marketplace is 1920×960."*

### Fixed
- **Gallery banners no longer crop their bottom row.** The product-page gallery
  packed 3 rows of 6 icon tiles into the 1920×960 canvas with tiles too tall, so
  each banner's bottom row was sliced off (~100 px past the 960 px edge). The
  files *were* 1920×960 — the content overflowed. Retuned the tile size and top
  margin so all three rows fit inside the frame (`190 + 3·220 + 2·24 = 898 ≤ 960`).
  Root cause + fix live in the `sdicons` tool
  ([Beennnn/stream-deck-icons@5633513](https://github.com/Beennnn/stream-deck-icons/commit/5633513)).
- **Regenerated every product-page asset** at exact Maker Console dimensions:
  - WLED Effects — thumbnail (1920×960), 5 icon previews (144×144), 12 gallery
    banners (1920×960), and 1 animated gallery video
    (`gallery-animated.mp4`, 1920×1080 H.264 + AAC, ~862 KB) for the Video slot.
  - WLED Palettes & Controls — thumbnail, 5 icon previews, 7 gallery banners.

### Unchanged (accepted as-is on the first review)
- The icons themselves: 216 animated GIF effects / 111 static palette & control PNG.
- Product descriptions, icon previews, and the packages
  (`dist/*.streamDeckIconPack`).

### Known, non-blocking
- Effect GIFs run ~8 fps (matching the WLED source cadence), below Elgato's soft
  10–20 fps guidance — `sdicons validate` reports these as warnings only; left
  as-authored on purpose.

### To publish (manual, Benoît's Elgato account)
1. **Media tab** — replace all gallery banners with the regenerated
   `maker-media/<pack>/gallery-*.png`; add `gallery-animated.mp4` to the Effects
   Video slot.
2. **Versions → 1 → Revise → Submit for review** (keep version 1). Submit is the
   final click.
