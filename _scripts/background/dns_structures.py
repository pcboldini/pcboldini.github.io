# Right side-panel art from the DNS of H-type breakdown (Boldini et al., JFM 2025, Movie 2 at
# https://github.com/pcboldini/DNSvisualisation/tree/main/movies).
# Usage: ffmpeg -ss 1.0 -i Movie2.mp4 -frames:v 1 f2.png ; python3 dns_structures.py f2.png
# The Q-criterion isosurfaces are separated from the plate, background, axes and colour bars;
# they are stylised with the same construction as the KH sheet (gen_background.py): shaded surface,
# mesh (lines along each tube + cross rulings), glowing front edges and a defocused far copy.
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

OUT = '../../assets/img/'
img = np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(float) / 255
side = 'right'
h, w, _ = img.shape
mx, mn = img.max(2), img.min(2)
sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
lum = img @ np.array([0.299, 0.587, 0.114])

# plate = light, unsaturated beige; its column-wise extent defines the region kept
beige = (lum > 0.8) & (sat < 0.12) & (img[..., 0] > img[..., 2])
beige = ndimage.binary_opening(beige, iterations=3)
cols = np.where(beige.sum(0) > 40)[0]
top = np.array([np.where(beige[:, c])[0].min() for c in cols])
bot = np.array([np.where(beige[:, c])[0].max() for c in cols])
# the plate is a parallelogram in the render: fit straight top and bottom edges on clean columns
ok = (bot - top) > np.percentile(bot - top, 60)
pt, pb = np.polyfit(cols[ok], top[ok], 1), np.polyfit(cols[ok], bot[ok], 1)
C = np.arange(w)
T, B = np.polyval(pt, C), np.polyval(pb, C)
inside = (np.arange(h)[:, None] > T[None, :]) & (np.arange(h)[:, None] < B[None, :])
# streamwise extent: contiguous run of columns that hold plate or structures (stops before the colour bar)
filled = (inside & (beige | (sat > 0.3))).sum(0) > 20
c_lo = cols.min()
c_hi = c_lo
while c_hi + 1 < w and (filled[c_hi + 1:c_hi + 40].any()):
    c_hi += 1
plate = inside.copy(); plate[:, :c_lo] = False; plate[:, c_hi + 1:] = False
# keep away from the edges: side-plane strip along the top edge, axis lines on the others
TOPCUT = 0.06                                  # side-plane strip along the top edge
band = (np.arange(h)[:, None] < T[None, :] + TOPCUT * h) | (np.arange(h)[:, None] > B[None, :] - 0.01 * h)
plate &= ~band; plate[:, :c_lo + 120] = False
# near the inflow the side plane bends onto the plate: trim the top edge more there
c_in = int(c_lo + 0.12 * (c_hi - c_lo))
plate[:, :c_in] &= (np.arange(h)[:, None] > T[None, :c_in] + 0.12 * h)

# structures = coloured or dark pixels on the plate (thin black axis lines removed by opening)
struct = plate & ((sat > 0.30) | (lum < 0.45))
struct = ndimage.binary_opening(struct, iterations=2)          # removes thin axis/edge lines
cyan = (img[..., 2] > 0.7) & (img[..., 0] < 0.3)          # u < 0 isosurfaces: drop
struct &= ~ndimage.binary_dilation(cyan, iterations=6)   # incl. their anti-aliased rims
# drop slivers that only hug the top edge (remains of the side plane)
lab, nlab = ndimage.label(struct)
depth = np.arange(h)[:, None] - T[None, :]
dmax = ndimage.maximum(depth, lab, index=np.arange(1, nlab + 1))
struct &= np.isin(lab, np.arange(1, nlab + 1)[dmax > 0.11 * h])
alpha = ndimage.gaussian_filter(struct.astype(float), 1.2)

# crop to the plate and rotate so the flow runs top -> bottom
rr, cc = np.where(plate)
r0, r1, c0, c1 = rr.min(), rr.max(), cc.min(), cc.max()
rot = lambda a: np.rot90(a[r0:r1, c0:c1], -1)
S = rot(struct.astype(float)); Lm = rot(lum)
k0 = int(0.03 * S.shape[0]); S, Lm = S[k0:], Lm[k0:]               # drop the axis line at the inflow end

# keep streaks -> Lambda vortices -> hairpins -> onset of breakdown; smooth into simple shapes
S = S[:int(0.58 * S.shape[0])]                                     # end with the hairpins, before the breakdown blobs
S = ndimage.gaussian_filter(S, 5) > 0.42
S = ndimage.binary_opening(S, iterations=3)
lab, nlab = ndimage.label(S)                                       # drop crumbs
sizes = ndimage.sum(S, lab, np.arange(1, nlab + 1))
S = np.isin(lab, np.arange(1, nlab + 1)[sizes > 600])
ys, xs = np.where(S); m = 40                                       # crop to the structures
S = S[max(0, ys.min()-m):ys.max()+m, max(0, xs.min()-m):xs.max()+m]
f = 2                                                              # line art at 1/2 resolution
hh, ww = S.shape[0] // f * f, S.shape[1] // f * f
Sf = ndimage.gaussian_filter(S[:hh, :ww].reshape(hh // f, f, ww // f, f).mean((1, 3)), 1.2)
D = ndimage.gaussian_filter(ndimage.distance_transform_edt(Sf > 0.5), 1.5)
Hs, Ws = Sf.shape
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
def contours(field, levs, minlen):
    fig, ax = plt.subplots(); cs = ax.contour(field, levels=levs); segs = [g for lv in cs.allsegs for g in lv]; plt.close(fig)
    return [g[::2] if len(g) > 8 else g for g in segs if len(g) > 2 and np.sum(np.hypot(*np.diff(g, axis=0).T)) >= minlen]
outline = contours(Sf, [0.5], 20)
wire = contours(D, [2.2, 4.5], 30)                                  # lines along the tubes, like the mesh on the billows
def path(g):
    return "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in g)
# fade in at the inflow, out at the breakdown end
# fade in at the inflow, out at the breakdown end
fade = ('<linearGradient id="fy" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset="0.04" stop-color="#fff"/><stop offset="0.9" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        f'<mask id="my"><rect width="{Ws}" height="{Hs}" fill="url(#fy)"/></mask>')
core = contours(D, [3.5], 20)                                       # lit core of each tube (shading)
cx, cy = Ws / 2, Hs / 2
# on screen both panels are fitted to the margin height: the KH art (2400 px tall) is shown at ~0.39x,
# this one at ~0.69x, so line widths and blur are scaled by K to give the same weight on screen
K = Hs / 2400
# strengths chosen so that, at their on-screen size, both panels have the same mean contrast and
# median/95th-percentile line contrast against the page (measured on renders at 944 px height)
for name, col, op in [('dark', '#5cc8e6', 0.204), ('light', '#7a1f74', 0.14)]:
    # same construction as the KH sheet: shaded surface + mesh + glowing front edges + defocused far copy
    L = "".join(f'<path d="{path(g)}"/>' for g in outline)
    F = "".join(f'<path d="{path(g)} Z"/>' for g in outline)
    Kc = "".join(f'<path d="{path(g)} Z"/>' for g in core)
    Wr = "".join(f'<path d="{path(g)}"/>' for g in wire)
    rul = "".join(f'<path d="M0,{y} L{Ws},{y + 0.18 * Ws:.0f}"/>' for y in range(-int(0.2 * Ws), Hs, 14))   # cross rulings, slanted like the billow mesh
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Ws}" height="{Hs}" viewBox="0 0 {Ws} {Hs}">'
           f'<defs><filter id="glow" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="{7*K:.1f}"/></filter>'
           f'<filter id="far" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="{4*K:.1f}"/></filter>'
           f'<clipPath id="cp" clip-rule="evenodd">{F}</clipPath>{fade}</defs>'
           f'<g mask="url(#my)" fill="none" stroke="{col}" stroke-linejoin="round" stroke-linecap="round">'
           f'<g filter="url(#far)" opacity="0.4" transform="translate({cx:.0f},{cy:.0f}) scale(1.35) translate({-cx - 60:.0f},{-cy + 40:.0f})" stroke-width="{2.6*1.6*K:.2f}" stroke-opacity="{op*0.6:.3f}">{L}</g>'
           f'<g fill="{col}" stroke="none" fill-rule="evenodd"><g fill-opacity="{op*0.10:.3f}">{F}</g>'
           f'<g fill-opacity="{op*0.12:.3f}" transform="translate({-1.5*K:.2f},{-1.5*K:.2f})">{Kc}</g></g>'
           f'<g stroke-width="{0.8*K:.2f}" stroke-opacity="{op*0.45:.3f}">{Wr}</g>'
           f'<g clip-path="url(#cp)" stroke-width="{0.8*K:.2f}" stroke-opacity="{op*0.35:.3f}">{rul}</g>'
           f'<g filter="url(#glow)" stroke-width="{2.6*K:.2f}" stroke-opacity="{op*0.9:.3f}">{L}</g>'
           f'<g stroke-width="{2.6*K:.2f}" stroke-opacity="{op:.3f}">{L}</g>'
           '</g></svg>')
    open(f'{OUT}bg_side_right_{name}.svg', 'w').write(svg)
    print(name, Ws, Hs, len(outline), len(wire), round(len(svg) / 1e3), 'kB')
