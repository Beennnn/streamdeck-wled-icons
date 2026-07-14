#!/usr/bin/env python3
"""Vendor WLED source icons from ~/dev/music/wled-assets into src/ + write
each pack's tags.json (display names + Marketplace search tags).

Dev-only: run when wled-assets changes. src/ is committed so `bin/build.sh`
works standalone (no wled-assets checkout needed to rebuild the packs).

Two packs:
  - effects/  ← images/effects/*.gif      (animated, 1 per WLED effect id)
  - palettes/ ← images/{palettes,controls,segment,nightlight,buttons,concepts}
                (static; filenames category-prefixed so paths stay unique)

Names come from WLED's own canonical lists (data/effects.json ordered by
effect id, data/palettes.json); effect tags carry the motion family from
animations/families.json. Everything falls back to a Title-Cased filename.
"""
import json
import re
import shutil
from pathlib import Path

WLED = Path.home() / "dev/music/wled-assets"
ROOT = Path(__file__).resolve().parent.parent


def slug(s):
    s = re.sub(r"[^\w-]+", "-", s.strip().lower())
    return re.sub(r"-+", "-", s).strip("-")


def title(stem):
    return " ".join(w.capitalize() for w in stem.replace("_", "-").split("-") if w)


def _clear(d, pattern):
    for f in d.glob(pattern):
        f.unlink()


def main():
    effects = json.loads((WLED / "data/effects.json").read_text())["effects"]
    motion = json.loads((WLED / "animations/families.json").read_text())["effect_motion"]
    palettes = json.loads((WLED / "data/palettes.json").read_text())["palettes"]

    slug_to_effect = {}
    for name in effects:
        slug_to_effect.setdefault(slug(name), name)
    slug_to_motion = {slug(k): v for k, v in motion.items()}

    # --- effects pack (animated GIFs) ---
    eff_src = ROOT / "src/effects"
    eff_src.mkdir(parents=True, exist_ok=True)
    _clear(eff_src, "*.gif")
    eff_tags = {}
    for gif in sorted((WLED / "images/effects").glob("*.gif")):
        st = gif.stem
        shutil.copy(gif, eff_src / gif.name)
        name = slug_to_effect.get(st, title(st))
        tags = ["wled", "effect", "animated"]
        m = slug_to_motion.get(st) or slug_to_motion.get(slug(name))
        if m and m not in tags:
            tags.append(m)
        eff_tags[st] = {"name": name, "tags": tags}
    (ROOT / "effects/tags.json").write_text(
        json.dumps(eff_tags, indent=2, ensure_ascii=False) + "\n")

    # --- palettes pack (static, multiple categories) ---
    slug_to_palette = {}
    for name in palettes:
        slug_to_palette.setdefault(slug(name), name)
    cats = {
        "palettes":   ("palette",    ["wled", "palette", "colour", "gradient"]),
        "controls":   ("control",    ["wled", "control"]),
        "segment":    ("segment",    ["wled", "segment"]),
        "nightlight": ("nightlight", ["wled", "nightlight"]),
        "buttons":    ("button",     ["wled", "button", "input"]),
        "concepts":   ("concept",    ["wled", "concept", "category"]),
    }
    pal_src = ROOT / "src/palettes"
    pal_src.mkdir(parents=True, exist_ok=True)
    _clear(pal_src, "*.png")
    pal_tags = {}
    for cat, (prefix, base) in cats.items():
        for png in sorted((WLED / "images" / cat).glob("*.png")):
            stem = f"{prefix}-{png.stem}"
            shutil.copy(png, pal_src / f"{stem}.png")
            if cat == "palettes":
                name = slug_to_palette.get(png.stem, title(png.stem))
            else:
                name = title(png.stem)
            tokens = [t for t in slug(name).split("-") if t and t not in base]
            pal_tags[stem] = {"name": name, "tags": base + tokens}
    (ROOT / "palettes/tags.json").write_text(
        json.dumps(pal_tags, indent=2, ensure_ascii=False) + "\n")

    print(f"vendored: {len(eff_tags)} effect GIFs, {len(pal_tags)} static PNGs")


if __name__ == "__main__":
    main()
