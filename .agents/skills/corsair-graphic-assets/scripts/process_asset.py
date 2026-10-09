#!/usr/bin/env python3
"""
Corsair Graphic Asset Processing Pipeline.

Turns raw AI-generated assets on white into transparent RGBA PNG text containers:
1. Keys out solid white backgrounds while preserving anti-aliased edge alpha.
2. Removes white fringe halos from edge pixels.
3. Locks the deep interior to a uniform flat color for high-contrast text overlay.
4. Autocrops transparent margins to the true bounding box.
5. Computes safe inner padding insets (top, right, bottom, left) for CSS layouts.
"""

import argparse
import os
import sys
from PIL import Image, ImageChops, ImageFilter


def alpha_from_white(rgb: Image.Image, lo: int = 12, hi: int = 60) -> Image.Image:
    """Extract true RGBA alpha channel from a pure white (#FFFFFF) background."""
    r, g, b = rgb.split()
    mn = ImageChops.darker(ImageChops.darker(r, g), b)
    k = 255.0 / max(1, (hi - lo))
    return mn.point(lambda v: max(0, min(255, int(((255 - v) - lo) * k))))


def median_color(rgb: Image.Image, mask: Image.Image) -> tuple[int, int, int]:
    """Sample median RGB color from the deep interior."""
    w, h = rgb.size
    px, mp = rgb.load(), mask.load()
    rs, gs, bs = [], [], []
    for y in range(0, h, 4):
        for x in range(0, w, 4):
            if mp[x, y] > 250:
                p = px[x, y]
                rs.append(p[0])
                gs.append(p[1])
                bs.append(p[2])
    if not rs:
        return (18, 24, 32)
    rs.sort()
    gs.sort()
    bs.sort()
    m = len(rs) // 2
    return (rs[m], gs[m], bs[m])


def flatten_interior(
    rgb: Image.Image,
    alpha: Image.Image,
    erode_small: int = 10,
    tol: int = 55
) -> tuple[Image.Image, tuple[int, int, int]]:
    """Force the deep interior to one flat color so text sits on an unobstructed surface."""
    w, h = rgb.size
    solid = alpha.point(lambda v: 255 if v > 128 else 0)
    small = solid.resize((max(1, w // 4), max(1, h // 4)), Image.Resampling.NEAREST)
    eroded = small.filter(ImageFilter.MinFilter(2 * erode_small + 1))
    deep = eroded.resize((w, h), Image.Resampling.BILINEAR).filter(ImageFilter.GaussianBlur(5))
    flat = median_color(rgb, deep.point(lambda v: 255 if v > 250 else 0))
    flat_img = Image.new("RGB", (w, h), flat)
    d = ImageChops.difference(rgb, flat_img)
    dr, dg, db = d.split()
    dmax = ImageChops.lighter(ImageChops.lighter(dr, dg), db)
    sim = dmax.point(lambda v: 255 if v <= tol else 0).filter(ImageFilter.GaussianBlur(1.2))
    weight = ImageChops.multiply(deep, sim)
    return Image.composite(flat_img, rgb, weight), flat


def defringe(rgb: Image.Image, alpha: Image.Image) -> Image.Image:
    """Remove the white halo that anti-aliasing leaves on edge pixels."""
    px = list(rgb.getdata())
    al = list(alpha.getdata())
    out = []
    for (r, g, b), a in zip(px, al):
        if 0 < a < 255:
            f = a / 255.0
            r = max(0, min(255, int((r - 255 * (1 - f)) / f)))
            g = max(0, min(255, int((g - 255 * (1 - f)) / f)))
            b = max(0, min(255, int((b - 255 * (1 - f)) / f)))
        out.append((r, g, b))
    res = Image.new("RGB", rgb.size)
    res.putdata(out)
    return res


def autocrop(rgba: Image.Image) -> Image.Image:
    """Trim transparent margins to the visual bounding box."""
    bbox = rgba.split()[3].point(lambda v: 255 if v > 16 else 0).getbbox()
    return rgba.crop(bbox) if bbox else rgba


def safe_rect(rgba: Image.Image) -> tuple[int, int, int, int]:
    """Calculate safe text body padding insets (top, right, bottom, left) in px."""
    a = rgba.split()[3]
    w, h = a.size
    px = a.load()

    def run_x(y):
        cx = w // 2
        if px[cx, y] <= 128:
            return None
        l = cx
        while l > 0 and px[l - 1, y] > 128:
            l -= 1
        r = cx
        while r < w - 1 and px[r + 1, y] > 128:
            r += 1
        return l, r

    def run_y(x):
        cy = h // 2
        if px[x, cy] <= 128:
            return None
        t = cy
        while t > 0 and px[x, t - 1] > 128:
            t -= 1
        b = cy
        while b < h - 1 and px[x, b + 1] > 128:
            b += 1
        return t, b

    ls, rs, ts, bs = [], [], [], []
    for f in (0.3, 0.4, 0.5, 0.6, 0.7):
        rx = run_x(int(h * f))
        if rx:
            ls.append(rx[0])
            rs.append(rx[1])
        ry = run_y(int(w * f))
        if ry:
            ts.append(ry[0])
            bs.append(ry[1])

    if not ls or not rs or not ts or not bs:
        return (40, 40, 40, 40)

    pad_left = max(ls)
    pad_right = w - min(rs)
    pad_top = max(ts)
    pad_bottom = h - min(bs)
    return (pad_top, pad_right, pad_bottom, pad_left)


def process_asset(
    input_path: str,
    output_path: str,
    flatten: bool = True,
    lo: int = 12,
    hi: int = 60,
    tol: int = 55,
    erode: int = 10,
    preview_path: str | None = None
) -> None:
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loading raw asset: {input_path}")
    img = Image.open(input_path).convert("RGB")
    alpha = alpha_from_white(img, lo=lo, hi=hi)

    flat_color = None
    if flatten:
        img, flat_color = flatten_interior(img, alpha, erode_small=erode, tol=tol)

    img = defringe(img, alpha)
    rgba = img.convert("RGBA")
    rgba.putalpha(alpha)
    rgba = autocrop(rgba)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    rgba.save(output_path, optimize=True)

    w, h = rgba.size
    top, right, bottom, left = safe_rect(rgba)

    print(f"\nAsset processed successfully -> {output_path}")
    print(f"  Dimensions : {w}x{h} px")
    if flat_color:
        hex_col = f"#{flat_color[0]:02x}{flat_color[1]:02x}{flat_color[2]:02x}"
        print(f"  Interior   : {hex_col} (RGB {flat_color})")
    print(f"  Safe Insets: top={top}px, right={right}px, bottom={bottom}px, left={left}px")
    print("\n  Recommended CSS:")
    print(f"    background-image: url('{os.path.basename(output_path)}');")
    print(f"    background-size: 100% 100%;")
    print(f"    padding: {top}px {right}px {bottom}px {left}px;")

    if preview_path:
        os.makedirs(os.path.dirname(os.path.abspath(preview_path)), exist_ok=True)
        prev = Image.new("RGB", (w + 60, h + 60), (248, 250, 252))
        prev.paste(rgba, (30, 30), rgba)
        prev.save(preview_path)
        print(f"  Preview    : {preview_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Process raw AI-generated assets into transparent RGBA text containers."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to input image file.")
    parser.add_argument("--output", "-o", required=True, help="Path to output PNG file.")
    parser.add_argument("--no-flatten", action="store_true", help="Skip deep interior color flattening.")
    parser.add_argument("--lo", type=int, default=12, help="Low alpha threshold (default: 12).")
    parser.add_argument("--hi", type=int, default=60, help="High alpha threshold (default: 60).")
    parser.add_argument("--tol", type=int, default=55, help="Interior flattening color tolerance (default: 55).")
    parser.add_argument("--erode", type=int, default=10, help="Interior erosion radius in px (default: 10).")
    parser.add_argument("--preview", "-p", help="Optional path to save preview on light paper.")

    args = parser.parse_args()
    process_asset(
        input_path=args.input,
        output_path=args.output,
        flatten=not args.no_flatten,
        lo=args.lo,
        hi=args.hi,
        tol=args.tol,
        erode=args.erode,
        preview_path=args.preview
    )


if __name__ == "__main__":
    main()
