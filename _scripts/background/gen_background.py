# Background art for the site (run from this folder: python3 gen_background.py)
# Inputs : paths.json  (billow isolines of the DNS density field + aerofoil drawing, 2-D)
# Outputs: ../../assets/img/bg_hero_{dark,light}.svg      billow interface extruded spanwise, in perspective
#          ../../assets/img/bg_aerofoil_{dark,light}.svg  wing with hump, resonator slots and TS wave, in perspective
#          ../../assets/img/bg_side_left_{dark,light}.svg  KH billows turned vertical (left margin, wide screens)
#          (right margin: bg_side_right_*.svg, stylised DNS vortices, made by dns_structures.py)
# 3-D look: each 2-D curve is extruded towards a vanishing point; every facet is shaded by
# Lambert's law for a light from the upper left, and a faint spanwise mesh is drawn on the surface.
import json, re, math

OUT = '../../assets/img/'
D = json.load(open('paths.json'))
W = 2400
THEMES = {  # colour, line opacity, facet opacity, glow strength
    'dark':  ('#5cc8e6', 0.30, 0.075, 0.9),
    'light': ('#7a1f74', 0.24, 0.055, 0.6),
}
WIDTHS = [2.6, 1.8, 1.2, 0.8]
REL_OP = [1.0, 0.8, 0.6, 0.45]
LIGHT = (-0.45, -0.89)                 # light direction in screen coordinates (y down): upper left


def fmt(P):
    return " L".join(f"{x:.0f},{y:.0f}" for x, y in P)


def lr(line):
    return line if line[0][0] < line[-1][0] else line[::-1]


def proj(p, s, vp):                    # point p moved towards the vanishing point; s = 1 front plane
    return (vp[0] + (p[0] - vp[0]) * s, vp[1] + (p[1] - vp[1]) * s)


def sheet(curve, col, fop, vp, s_back, nmesh=4, rule_every=70, line_op=0.3, closed=False):
    """Extruded surface of a 2-D curve: shaded facets, spanwise rulings, constant-depth mesh lines."""
    o, n = [], len(curve)
    segs = range(n if closed else n - 1)
    for i in segs:                     # facets
        a, b = curve[i], curve[(i + 1) % n]
        tx, ty = b[0] - a[0], b[1] - a[1]; L = math.hypot(tx, ty) or 1
        nx, ny = ty / L, -tx / L       # left normal of the curve
        lam = max(0.0, nx * LIGHT[0] + ny * LIGHT[1])
        q = [a, b, proj(b, s_back, vp), proj(a, s_back, vp)]
        o.append(f'<path fill-opacity="{fop*(0.25+1.1*lam):.3f}" d="M{fmt(q)} Z"/>')
    facets = f'<g fill="{col}" stroke="none">' + "".join(o) + '</g>'
    m = []
    for j in range(1, nmesh + 1):      # curves at constant depth
        s = 1 - (1 - s_back) * j / nmesh
        m.append(f'<path stroke-opacity="{line_op*(0.6-0.35*j/nmesh):.3f}" d="M{fmt([proj(p, s, vp) for p in curve])}{" Z" if closed else ""}"/>')
    acc = 0.0                          # spanwise rulings, equally spaced in arc length (rule_every px)
    for i in range(1, n):
        acc += math.dist(curve[i - 1], curve[i])
        if acc >= rule_every:
            acc = 0.0; p = curve[i]
            m.append(f'<path stroke-opacity="{line_op*0.35:.3f}" d="M{fmt([p, proj(p, s_back, vp)])}"/>')
    mesh = f'<g fill="none" stroke="{col}" stroke-width="0.8" stroke-linecap="round">' + "".join(m) + '</g>'
    return facets, mesh


def hfade(H, idn):                     # soft horizontal edges
    return (f'<linearGradient id="{idn}g" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            '<stop offset="0.15" stop-color="#fff"/><stop offset="0.85" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<mask id="{idn}"><rect width="{W}" height="{H}" fill="url(#{idn}g)"/></mask>')


def hero(col, op, fop, gop):
    H, DY = 640, 190
    VP, SB = (W * 0.62, -900), 0.80    # vanishing point and depth of the back plane
    L = [[(x, y + DY) for x, y in lr(l)] for l in D['billows']]
    main = L[1][::5]
    facets, mesh = sheet(main, col, fop, VP, SB, line_op=op)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>',
         '<filter id="glow" x="-5%" y="-30%" width="110%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>',
         '<filter id="far" x="-5%" y="-30%" width="110%" height="160%"><feGaussianBlur stdDeviation="4"/></filter>',
         hfade(H, 'hm'), '</defs><g mask="url(#hm)">']
    # far, defocused copy of the interface further back
    o.append(f'<g filter="url(#far)" opacity="0.4" fill="none" stroke="{col}" stroke-linecap="round">')
    for k, l in enumerate(L):
        o.append(f'<path stroke-width="{WIDTHS[k]*1.6:.1f}" stroke-opacity="{op*REL_OP[k]:.3f}" d="M{fmt([proj(p, 0.62, VP) for p in l[::3]])}"/>')
    o.append('</g>')
    # back edges of the other isolines (thin), then the shaded sheet and its mesh
    o.append(f'<g fill="none" stroke="{col}" stroke-width="0.8">')
    for k, l in enumerate(L):
        if k != 1:
            o.append(f'<path stroke-opacity="{op*REL_OP[k]*0.35:.3f}" d="M{fmt([proj(p, SB, VP) for p in l[::4]])}"/>')
    o.append('</g>')
    o += [facets, mesh]
    # front isolines: glow + sharp
    lines = "".join(f'<path stroke-width="{WIDTHS[k]}" stroke-opacity="{op*REL_OP[k]:.3f}" d="M{fmt(l[::2])}"/>' for k, l in enumerate(L))
    o.append(f'<g filter="url(#glow)" opacity="{gop}" fill="none" stroke="{col}" stroke-linecap="round">{lines}</g>')
    o.append(f'<g fill="none" stroke="{col}" stroke-linejoin="round" stroke-linecap="round">{lines}</g>')
    o.append('</g></svg>')
    return "".join(o)


def aerofoil_geometry():
    g = D['aerofoil_group']; out = {'stream': [], 'ts': None, 'body': None, 'res': []}
    for m in re.finditer(r'<path stroke-width="([0-9.]+)" stroke-opacity="([0-9.]+)" d="M([^"]+)"', g):
        w, o, d = m.groups()
        P = [tuple(map(float, p.split(','))) for p in d.rstrip('Z').replace(' L', ' ').split()]
        if d.endswith('Z'): out['body'] = P
        elif w == '1.7': out['ts'] = P
        elif w == '1.6': out['res'].append(P)
        else: out['stream'].append((float(w), float(o), P))
    return out


def aerofoil(col, op, fop, gop):
    H, DY = 520, 120
    G = aerofoil_geometry()
    for k in ('body', 'ts'): G[k] = [(x, y + DY) for x, y in G[k]]
    G['res'] = [[(x, y + DY) for x, y in R] for R in G['res']]
    G['stream'] = [(w, oo, [(x, y + DY) for x, y in P]) for w, oo, P in G['stream']]
    VP, SB = (W * 0.95, -500), 0.84
    body = G['body'][::3]
    # orient the outline so its left normal points outwards (clockwise on screen with y down)
    area = sum(body[i][0] * body[(i+1) % len(body)][1] - body[(i+1) % len(body)][0] * body[i][1] for i in range(len(body)))
    if area > 0: body = body[::-1]
    facets, mesh = sheet(body, col, fop * 1.6, VP, SB, nmesh=3, rule_every=45, line_op=op, closed=True)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>',
         '<filter id="glow" x="-5%" y="-30%" width="110%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>',
         hfade(H, 'am'), '</defs><g mask="url(#am)" stroke-linecap="round" stroke-linejoin="round">']
    # streamlines (mid-span plane)
    o.append(f'<g fill="none" stroke="{col}">' + "".join(
        f'<path stroke-width="{w}" stroke-opacity="{oo*op:.3f}" d="M{fmt(P[::2])}"/>' for w, oo, P in G['stream']) + '</g>')
    # TS wave: spanwise-uniform crests drawn as a translucent ribbon over the span
    ts = G['ts'][::2]
    tsf, tsm = sheet(ts, col, fop * 0.5, VP, SB, nmesh=2, rule_every=1e9, line_op=op)
    o += [facets, mesh, tsm]              # TS crests: copies across the span, no ribbon fill
    # resonator slots: necks repeated along the span
    slots = []
    for R in G['res']:
        neck = ((R[0][0] + R[-1][0]) / 2, (R[0][1] + R[-1][1]) / 2)
        slots.append(f'<path stroke-opacity="{op*0.8:.3f}" stroke-width="1.4" d="M{fmt([neck, proj(neck, SB, VP)])}"/>')
    o.append(f'<g fill="none" stroke="{col}">' + "".join(slots) + '</g>')
    front = (f'<path stroke-width="2.4" stroke-opacity="{op:.3f}" fill="none" d="M{fmt(G["body"][::3])} Z"/>'
             f'<path stroke-width="1.7" stroke-opacity="{op:.3f}" fill="none" d="M{fmt(G["ts"][::2])}"/>'
             + "".join(f'<path stroke-width="1.6" stroke-opacity="{op:.3f}" fill="none" d="M{fmt(R)}"/>' for R in G['res']))
    o.append(f'<g filter="url(#glow)" opacity="{gop}" stroke="{col}">{front}</g><g stroke="{col}">{front}</g>')
    o.append('</g></svg>')
    return "".join(o)


def vertical(build, args, H, turn):
    """Rotate a piece by -90 degrees (turn='left') or +90; the light is pre-rotated so it still comes from the upper left on screen."""
    global LIGHT
    keep = LIGHT
    LIGHT = (0.89, -0.45) if turn == 'left' else (-0.89, 0.45)
    svg = build(*args); LIGHT = keep
    inner = svg[svg.index('>') + 1:svg.rindex('</svg>')]
    tr = f'translate(0,{W}) rotate(-90)' if turn == 'left' else f'translate({H},0) rotate(90)'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{H}" height="{W}" viewBox="0 0 {H} {W}"><g transform="{tr}">{inner}</g></svg>'


for name, (col, op, fop, gop) in THEMES.items():
    open(f'{OUT}bg_hero_{name}.svg', 'w').write(hero(col, op, fop, gop))
    open(f'{OUT}bg_aerofoil_{name}.svg', 'w').write(aerofoil(col, op, fop, gop))
    open(f'{OUT}bg_side_left_{name}.svg', 'w').write(vertical(hero, (col, op, fop, gop), 640, 'left'))
    print(name, 'written')
