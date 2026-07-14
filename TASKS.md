# TASKS — streamdeck-wled-icons

- ☐ Submit both packs to maker.elgato.com (Benoît's login + Maker Agreement;
  Effects = animated, Palettes = not-animated) → **user action**. Upload
  assets: run maker-media per pack with a distinct out-dir (both default to
  `maker-media/`, so the 2nd run overwrites the 1st):
  `sdicons maker-media effects --out-dir maker-media/effects --previews rainbow,fire-2012,geq,ps-fireworks,matrix`
  and `... palettes --out-dir maker-media/palettes --previews palette-lava,palette-aurora,palette-rainbow,palette-sunset,palette-ocean`
- 🤔 Motion-family tags on effects are coarse (only the `effect_motion` type).
  Consider richer tags: audio-reactive flag, 1D/2D, Particle-System family.
- 🤔 8 fps vs Elgato's 10–20 guidance — leave as-authored (respects WLED
  motion speed) or add an `sdicons --fps` retime? Decide only if it blocks
  review.
