#!/usr/bin/env python3
"""Generate site-ready logo variants from a white-background PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def remove_white_background(img: Image.Image, threshold: int) -> Image.Image:
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        if r >= threshold and g >= threshold and b >= threshold:
            new_data.append((r, g, b, 0))
        else:
            new_data.append((r, g, b, a))
    img.putdata(new_data)
    return img


def invert_for_dark(img: Image.Image, gold_tint: tuple[int, int, int] | None) -> Image.Image:
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        if a == 0:
            new_data.append((r, g, b, a))
            continue
        lum = (r + g + b) / 3
        if gold_tint and lum < 200:
            t = lum / 255
            nr = int(gold_tint[0] * t + 255 * (1 - t))
            ng = int(gold_tint[1] * t + 255 * (1 - t))
            nb = int(gold_tint[2] * t + 255 * (1 - t))
            new_data.append((nr, ng, nb, a))
        else:
            new_data.append((255 - r, 255 - g, 255 - b, a))
    img.putdata(new_data)
    return img


def resize_height(img: Image.Image, height: int) -> Image.Image:
    w, h = img.size
    ratio = height / h
    return img.resize((max(1, int(w * ratio)), height), Image.Resampling.LANCZOS)


def save_preview(img: Image.Image, bg: tuple[int, int, int], path: Path) -> None:
    canvas = Image.new("RGB", img.size, bg)
    canvas.paste(img, mask=img.split()[3])
    canvas.save(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare CISCSR logo assets")
    parser.add_argument("--input", required=True, help="Source PNG path")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--white-threshold", type=int, default=245)
    parser.add_argument("--header-height", type=int, default=50)
    parser.add_argument("--hero-height", type=int, default=118)
    args = parser.parse_args()

    src = Path(args.input)
    out = Path(args.output)
    previews = out / "previews"
    out.mkdir(parents=True, exist_ok=True)
    previews.mkdir(parents=True, exist_ok=True)

    original = Image.open(src)
    transparent = remove_white_background(original, args.white_threshold)
    on_light = transparent.copy()
    on_dark = invert_for_dark(transparent.copy(), gold_tint=(213, 183, 121))

    on_light.save(out / "logo-on-light.png")
    on_dark.save(out / "logo-on-dark.png")
    resize_height(on_light, args.header_height).save(out / "logo-header.png")
    resize_height(on_dark, args.hero_height).save(out / "logo-hero.png")
    resize_height(on_light, 32).save(out / "favicon-32.png")
    resize_height(on_light, 180).save(out / "favicon-180.png")

    save_preview(on_light, (251, 246, 234), previews / "on-paper.png")
    save_preview(on_dark, (17, 26, 42), previews / "on-navy.png")

    print(f"Generated logo assets in {out}")


if __name__ == "__main__":
    main()
