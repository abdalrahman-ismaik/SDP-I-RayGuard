"""Arrange RayGuard-App screenshots into the report walkthrough figures.

Usage (from docs/report):
  uv run --no-project --with pillow python tools/app_walkthrough_figures.py <captures>

<captures> holds the PNG files written by app_walkthrough.mjs. The output goes to
figures/private/, which Git ignores because the screenshots show dataset scans.
The sidebar is cropped from grouped panels; nothing else in a screenshot is changed.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SRC = Path(sys.argv[1])
OUT = Path(__file__).resolve().parents[1] / "figures" / "private"
FIGURES = {
    "app-steps": (2, ["1-setup", "2-loaded", "3-processing", "5-provenance", "6-review", "8-session"]),
    "app-compare": (2, ["7-demo-1488", "7-demo-2803", "7-demo-3369", "7-demo-0"]),
    "app-models": (2, ["9-device", "9-specific"]),
}
WIDTH, GAP, LABEL = 1150, 24, 46

OUT.mkdir(exist_ok=True)
image = Image.open(SRC / "4-result.png").convert("RGB")
image.resize((2000, 2000 * image.height // image.width)).save(OUT / "app-result.png", optimize=True)
font = ImageFont.load_default(size=32)
for name, (columns, shots) in FIGURES.items():
    panels = []
    for shot in shots:
        image = Image.open(SRC / f"{shot}.png").convert("RGB")
        image = image.crop((image.width * 440 // 2720, 0, image.width, image.height))
        panels.append(image.resize((WIDTH, WIDTH * image.height // image.width)))
    height = panels[0].height + LABEL
    rows = (len(panels) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * WIDTH + (columns - 1) * GAP, rows * height + (rows - 1) * GAP), "white")
    draw = ImageDraw.Draw(canvas)
    for i, panel in enumerate(panels):
        x, y = (i % columns) * (WIDTH + GAP), (i // columns) * (height + GAP)
        draw.text((x, y), f"({'abcdef'[i]})", fill="black", font=font)
        canvas.paste(panel, (x, y + LABEL))
    canvas.save(OUT / f"{name}.png", optimize=True)
    print(name, canvas.size)
