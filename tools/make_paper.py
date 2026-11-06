"""Makes the photocopied textures for home/: the attic-rafters background and two small ink tiles."""
import os
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "home")
rng = np.random.default_rng(7)
W, H = 1600, 1000

# The scene: rafters running up to a ridge, a collar beam, and darkness in the corners.
scene = Image.new("L", (W, H), 150)
d = ImageDraw.Draw(scene)
peak = (W * 0.5, -60)
for x in (-900, -420, 80, 520, 1080, 1520, 2020, 2500):
    d.line([peak, (x, H + 200)], fill=38, width=74)
d.line([(0, H * 0.34), (W, H * 0.30)], fill=30, width=64)
d.line([(0, H * 0.86), (W, H * 0.90)], fill=26, width=92)
d.polygon([(0, 0), (W * 0.2, 0), (0, H * 0.5)], fill=30)
d.polygon([(W, 0), (W * 0.8, 0), (W, H * 0.5)], fill=30)
a = np.asarray(scene, dtype=float) / 255
a = gaussian_filter(a, 26)
a += gaussian_filter(rng.standard_normal((H, W)), 70) * 1.5     # uneven toner
fine = gaussian_filter(rng.standard_normal((H, W)), 0.95)
fine /= fine.std()
out = (a + fine * 0.2) > 0.34
Image.fromarray((out * 255).astype("uint8")).convert("1").save(os.path.join(OUT, "paper.png"), optimize=True)

# Tiles wrap at the edges, so they repeat without a seam.
S = 320
blot = gaussian_filter(rng.standard_normal((S, S)), 1.0, mode="wrap")
patch = gaussian_filter(rng.standard_normal((S, S)), 26, mode="wrap")
blot /= blot.std()
patch /= patch.std()

def tile(name, keep):
    rgba = np.zeros((S, S, 4), "uint8")
    rgba[..., :3] = 255
    rgba[..., 3] = keep * 255
    Image.fromarray(rgba).save(os.path.join(OUT, name), optimize=True)

tile("ink.png", (blot + patch * 0.7) < 1.75)     # mask: worn holes in the ink
tile("speck.png", (blot + patch * 0.8) > 1.35)   # overlay: pale mottling on a flat colour
