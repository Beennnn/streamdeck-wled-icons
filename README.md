# WLED icons for Elgato Stream Deck

Two **Marketplace-ready icon packs** that put the [WLED](https://kno.wled.ge)
concepts — its animated effects and its colour palettes — on your Stream Deck as
key icons, so a key labelled *Fireworks* or *Lava* actually *looks* like the
thing it names. Plain drop-in icons for any key or action; no plugin required.

| Pack | Icons | Kind | Container |
|---|---|---|---|
| **WLED Effects** | 216 | animated GIF (144×144, looping) | `dist/com.beennnn.wledeffects.streamDeckIconPack` |
| **WLED Palettes & Controls** | 111 | static PNG (144×144) | `dist/com.beennnn.wledpalettescontrols.streamDeckIconPack` |

- **WLED Effects** — one looping icon per WLED effect id, from `Solid`,
  `Rainbow` and `Fire 2012` through the AudioReactive (`GEQ`, `Freqwave`), 2D
  (`Matrix`, `Octopus`, `DNA`) and Particle System (`PS Fireworks`,
  `PS Hourglass`) families. Each icon carries the effect's **motion**, not a
  colour — colour is what the palettes are for.
- **WLED Palettes & Controls** — all 72 colour palettes (`Lava`, `Aurora`,
  `April Night`…) plus segment, nightlight and button-type glyphs, the control
  strip (speed, intensity, custom sliders…) and 11 category tiles.

Two packs, not one, because the Elgato Marketplace classifies packs as
animated or static — separate listings match how people browse.

## Install

Double-click a `.streamDeckIconPack` in `dist/` to install it into the Stream
Deck app, or grab them from the Elgato Marketplace (once published). The icons
then show up in the icon picker for any key/action.

## Build from source

The packs are generated from the vendored `src/` by the
[`stream-deck-icons`](https://github.com/Beennnn/stream-deck-icons) toolkit
(`sdicons`) — this repo holds only source assets + per-pack metadata; the
rendered `icons/` and `dist/` are gitignored and reproducible.

```sh
# needs Pillow + rsvg-convert, and Beennnn/stream-deck-icons cloned as a sibling
bin/build.sh          # → both .streamDeckIconPack files in dist/
```

The animated effects are upscaled 72→144 with **nearest-neighbour** in palette
mode: an exact ×2 pixel double that keeps the LED grid crisp and preserves
each GIF's frame timing, loop, and transparency. Static palettes/controls use
lanczos.

### Re-vendoring

`src/` is copied from [`openlamp/wled-assets`](https://github.com/openlamp/wled-assets)
and committed so the build is standalone. To refresh it after wled-assets
changes:

```sh
python3 bin/vendor.py   # rebuilds src/ + each pack's tags.json from canonical WLED data
```

## Licence

Icons are derived from **wled-assets** (CC0 1.0) and are likewise released
under **[CC0 1.0](LICENSE)** — public domain, no attribution required. A nod to
[WLED](https://kno.wled.ge) is appreciated. Unofficial fan project; WLED is a
trademark of its authors.

Built with [stream-deck-icons](https://github.com/Beennnn/stream-deck-icons).
