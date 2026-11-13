"""Figures 1 to 3 of Paper 2, drawn in TikZ in the style of the repository's other figures: the slots on the affine
E8 graph, rigid and soft (section 2.1); the shape of the small-amplitude spectrum, a schematic of Theorem R(a)
(section 4.1); and the thirteen critical orbits in R4 and R5 as Majorana constellations, grouped by their
small-amplitude type (section 4.1).

Reads, at MIT commit b0e50ae3, the page standing-wave-branches.md: Table 1 (each slot's dimension and lowest level),
section 2.1's rigid and soft slots, Theorem R(a), Table 2 (the orbits' representatives, values and signatures) and
Table 4 (their slow flows and types). Reads, at MIT commit 1d11a877, the Surviving Ray's certificate file,
sr_v2_certificates.json, for the three orbits outside the census's class. Before drawing it checks: that the graph is
the McKay graph of 2I with Table 1's dimensions and that its distances from R0 are Table 1's lowest levels; each
closed-form representative's 924 r6 against Table 2, exactly; each certified orbit's against the digits Table 2
prints; and each Table 4 signature against Table 2's. It stops on any difference.

Writes theory.json, what it read; figures/figure-slots, figure-spectrum and figure-orbits, each as .tex, .pdf and .png
(300 dpi), the PDFs without dates, so a rerun gives the same bytes; and fig_theory_log.txt.
Usage: fig_theory.py [MIT_CLONE [OUT_DIR]]; by default the repository this script is in, and this folder, with the
images in its figures/ folder."""
import cmath
import json
import math
import os
import re
import subprocess
import sys
from fractions import Fraction
from math import comb

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

HERE = os.path.dirname(os.path.abspath(__file__))
MIT = sys.argv[1] if len(sys.argv) > 1 else subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'],
                                                           capture_output=True, text=True, check=True).stdout.strip()
OUT = sys.argv[2] if len(sys.argv) > 2 else HERE
FIGS = os.path.join(OUT, 'figures')
REV_PAGE, REV_CERT = 'b0e50ae3', '1d11a877'
PAGE = 'files/framework/files/dynamics/files/standing-wave-branches.md'
CERT = 'files/framework/files/bedrock/files/scripts/surviving-ray-v2/sr_v2_certificates.json'
LOG = []


def note(*a):
    s = ' '.join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


def show(rev, path):
    return subprocess.run(['git', '-C', MIT, 'show', f'{rev}:{path}'], capture_output=True, text=True,
                          check=True).stdout


def need(cond, what):
    if not cond:
        raise SystemExit(f'STOP: {what}')
    note(f'  ok: {what}')


page = show(REV_PAGE, PAGE)
cert = json.loads(show(REV_CERT, CERT))
note(f'read {PAGE} at {REV_PAGE} and {CERT} at {REV_CERT}')

# ------------------------------------------------------------------ the slots: Table 1 and section 2.1
note('\nthe slots')
T1 = {int(k): (int(d), cls, int(n)) for k, d, cls, n in re.findall(
    r'^\| \$`R_(\d)`\$ \| (\d+) \| (half-integer|integer) \| (\d+) \|$', page, re.M)}
need(sorted(T1) == list(range(1, 9)), 'Table 1 has the eight slots R1 to R8')
need("In five of the slots, $`R_1, R_3, R_6, R_7`$ and $`R_8`$, and in the control," in page
     and "the soft slots, $`R_2`$ at level 7 and $`R_4`$ and $`R_5`$ at level 6" in page,
     'section 2.1: R1, R3, R6, R7, R8 and the control rigid; R2 at level 7, R4 and R5 at level 6 soft')
RIGID, SOFT = {1, 3, 6, 7, 8}, {2, 4, 5}
need(T1[2][2] == 7 and T1[4][2] == 6 and T1[5][2] == 6, "Table 1's lowest levels agree with section 2.1's soft slots")
EDGES = [(0, 1), (1, 3), (3, 6), (6, 7), (7, 8), (8, 4), (8, 5), (5, 2)]
DIM = {0: 1, **{k: v[0] for k, v in T1.items()}}
nbr = {k: [b for a, b in EDGES if a == k] + [a for a, b in EDGES if b == k] for k in range(9)}
need(all(2 * DIM[k] == sum(DIM[j] for j in nbr[k]) for k in range(9)),
     "the graph is the McKay graph of 2I: twice each node's dimension is its neighbours' sum, with Table 1's dimensions")
dist, front = {0: 0}, [0]
while front:
    front = [j for k in front for j in nbr[k] if j not in dist and not dist.update({j: dist[k] + 1})]
need(all(dist[k] == T1[k][2] for k in T1), "each slot's distance from R0 on the graph is Table 1's lowest level")

# ------------------------------------------------------------------ Theorem R(a) and the slow flows of Table 4
note('\nTheorem R(a) and Table 4')
need('a slow part, $`2d`$ eigenvalues $`\\varepsilon(\\chi s + o(1))`$' in page
     and 'a fast part on the imaginary axis, bounded away from 0' in page, "Theorem R(a)'s slow and fast parts")
T4 = re.findall(r'^\| (.+?) \| \((\d+), (\d+), (\d+)\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',
                page[page.index('| orbit | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow | type |'):
                     page.index('*Table 4.*')], re.M)
need(len(T4) == 13, 'Table 4 has thirteen rows')
FLOWS = {r[5].strip() for r in T4}
need(any(f.startswith('elliptic') for f in FLOWS) and 'hyperbolic, real pairs' in FLOWS
     and 'hyperbolic, a complex quartet' in FLOWS, "Table 4's slow flows include the schematic's three kinds")

# ------------------------------------------------------------------ the orbits: Table 2, Table 4 and the certificates
note('\nthe orbits')
t2 = page[page.index('| orbit | representative | $`924\\,\\hat r_6`$ | $`(n_-, n_0, n_+)`$ |'):page.index('*Table 2.*')]
T2 = re.findall(r'^\| (.+?) \| (.+?) \| (.+?) \| \((\d+), (\d+), (\d+)\) \|$', t2, re.M)  # data rows only
need(len(T2) == 13, 'Table 2 has thirteen rows')
clean = lambda s: s.replace(' †', '').replace(' (the third outside orbit)', '').strip()
sig4 = {clean(r[0]): tuple(map(int, r[1:4])) for r in T4}
typ4 = {clean(r[0]): r[6].strip() for r in T4}


def coef(s):
    c = sp.Integer(1)
    if s.startswith('i'):
        c, s = sp.I, s[1:]
    m = re.fullmatch(r'(\d*)(?:\\sqrt\{(\d+)(?:/(\d+))?\})?', s)
    if m is None:
        raise SystemExit(f'STOP: coefficient not read: {s!r}')
    if m.group(1):
        c *= int(m.group(1))
    if m.group(2):
        c *= sp.sqrt(sp.Rational(int(m.group(2)), int(m.group(3) or 1)))
    return c


def rep(s):
    """A representative, as written in Table 2, to {m: coefficient}."""
    out = {}
    for term in s.strip().strip('$`').split(' + '):
        m = re.fullmatch(r'(.*?)(?:\\,)?v_\{?(-?\d)\}?', term.strip())
        if m is None:
            raise SystemExit(f'STOP: term not read: {term!r}')
        out[int(m.group(2))] = coef(m.group(1))
    return out


def poly(W):
    """924 r6 of the state whose polynomial coefficients are W[0..6] (the Bombieri basis, w_k = sqrt(C(6,k)) c_(k-3)),
    by the certificate verifier's formula."""
    Wt = [(-1) ** (j + 1) * W[6 - j].conjugate() for j in range(7)]
    Cc = [sum(W[k] * Wt[j - k] for k in range(7) if 0 <= j - k <= 6) for j in range(13)]
    r = sum(abs(Cc[j]) ** 2 / comb(12, j) for j in range(13))
    N = sum(abs(W[k]) ** 2 / comb(6, k) for k in range(7))
    return 924 * r / N ** 2


ORB = []
for name, repr_s, value_s, a, b, c in T2:
    name = clean(name)
    sig = (int(a), int(b), int(c))
    need(sig4.get(name) == sig, f'{name}: Table 4 signature {sig4.get(name)} equals Table 2\'s {sig}')
    if 'interval-certified' in repr_s:
        key = {'$`\\mathcal{O}_1`$': 'T1', '$`\\mathcal{O}_2`$': 'T2', '$`\\mathcal{O}_3`$': 'T3'}[name]
        o = cert['orbits'][key]
        mp.mp.dps = 50
        B = [[Fraction(q) for q in row] for row in o['basis_14xd']]
        y = [mp.mpf(s) for s in o['centre'][:len(B[0])]]
        x = [mp.fsum(mp.mpf(Bij.numerator) / Bij.denominator * yj for Bij, yj in zip(row, y)) for row in B]
        W = [mp.mpc(x[k], x[7 + k]) for k in range(7)]
        v = poly(W)
        digits = value_s.replace('…', '')
        need(mp.nstr(v.real, 20).startswith(digits) and abs(v.imag) < mp.mpf('1e-40'),
             f'{name} ({key}): 924 r6 at the certified centre is {mp.nstr(v.real, 12)}…, Table 2 prints {value_s}')
        Wc = [complex(w) for w in W]
        ORB.append(dict(name=name, sig=sig, value=value_s, source=f'{CERT} at {REV_CERT}, orbit {key}', W=Wc))
    else:
        R = rep(repr_s)
        W = [sp.sqrt(comb(6, k)) * R.get(k - 3, 0) for k in range(7)]
        v = sp.nsimplify(sp.simplify(poly([sp.nsimplify(w) for w in W])))
        need(v == sp.Rational(value_s), f'{name}: 924 r6 of {repr_s.strip("$`")} is {v}, Table 2 gives {value_s}')
        ORB.append(dict(name=name, sig=sig, value=value_s, source='Table 2', rep=repr_s.strip('$`'),
                        W=[complex(sp.N(w, 30)) for w in W]))
for O in ORB:
    O['type'] = typ4[O['name']]
    O['stable'] = 'unstable' not in O['type']
    O['v'] = float(sp.Rational(O['value'])) if '…' not in O['value'] else float(O['value'].replace('…', ''))
need(sum(O['stable'] for O in ORB) == 6, "six orbits spectrally stable, seven spectrally unstable, as Table 4 types them")

# ------------------------------------------------------------------ Majorana stars and the drawing
SIN_A = 0.324 / 1.050  # the Surviving Ray's figure: the equator's half-height over the sphere's radius
COS_A = math.sqrt(1 - SIN_A ** 2)


def stars(W):
    """The Majorana points of the polynomial sum W_k z^k on the unit sphere, z = tan(theta/2) e^(i phi); a missing top
    degree puts its roots at the south pole. Returns (unit vectors, multiplicities)."""
    c = list(W)
    while abs(c[-1]) < 1e-12:
        c.pop()
    roots = list(np.roots(c[::-1])) if len(c) > 1 else []
    pts = [(0.0, 0.0, -1.0)] * (6 - (len(c) - 1))
    for z in roots:
        th, ph = 2 * math.atan(abs(z)), cmath.phase(z)
        pts.append((math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)))
    uniq, mult = [], []
    for p in pts:
        for i, q in enumerate(uniq):
            if math.dist(p, q) < 1e-6:
                mult[i] += 1
                break
        else:
            uniq.append(p)
            mult.append(1)
    return uniq, mult


def view(p, beta):
    x, y, z = p
    xr, yr = x * math.cos(beta) - y * math.sin(beta), x * math.sin(beta) + y * math.cos(beta)
    return xr, yr * SIN_A + z * COS_A, -yr * COS_A + z * SIN_A > 1e-9  # screen x, screen y, in front


def edges(P):
    """The polyhedron's edges: the convex hull's, coplanar triangles merged; a planar set's polygon; none for fewer
    than three distinct points."""
    if len(P) < 3:
        return []
    A = np.array(P)
    try:
        h = ConvexHull(A)
    except Exception:
        n = np.cross(A[1] - A[0], A[2] - A[0])
        n /= np.linalg.norm(n)
        c0 = A.mean(axis=0)
        u = A[0] - c0
        u /= np.linalg.norm(u)
        w = np.cross(n, u)
        order = sorted(range(len(P)), key=lambda i: math.atan2((A[i] - c0) @ w, (A[i] - c0) @ u))
        return [(order[i], order[(i + 1) % len(order)]) for i in range(len(order))]
    count = {}
    for s, eq in zip(h.simplices, h.equations):
        for i in range(3):
            e = tuple(sorted((int(s[i]), int(s[(i + 1) % 3]))))
            count.setdefault(e, []).append(tuple(np.round(eq, 6)))
    return [e for e, fs in count.items() if len(fs) == 1 or fs[0] != fs[1]]


def best_beta(P):
    best = None
    for deg in range(0, 120, 3):
        b = math.radians(deg + 10)
        S = [view(p, b)[:2] for p in P]
        dmin = min((math.dist(S[i], S[j]) for i in range(len(S)) for j in range(i)), default=9.0)
        if best is None or dmin > best[0] + 1e-9:
            best = (dmin, b)
    return best[1]


def constellation(O, cx, cy, R):
    P, mult = stars(O['W'])
    beta = best_beta(P)
    out = [f'\\draw[black!35] ({cx:.3f},{cy:.3f}) circle ({R:.3f});',
           f'\\draw[black!30, dashed] ({cx + R:.3f},{cy:.3f}) arc[start angle=0, end angle=180, x radius={R:.3f}, '
           f'y radius={R * SIN_A:.3f}];',
           f'\\draw[black!35] ({cx + R:.3f},{cy:.3f}) arc[start angle=0, end angle=-180, x radius={R:.3f}, '
           f'y radius={R * SIN_A:.3f}];']
    V = [view(p, beta) for p in P]
    XY = [(cx + R * a, cy + R * b) for a, b, _ in V]
    E = edges(P)
    for i, j in E:
        if not V[i][2] and not V[j][2]:
            out.append(f'\\draw[black!45, dashed, thin] ({XY[i][0]:.3f},{XY[i][1]:.3f}) -- ({XY[j][0]:.3f},{XY[j][1]:.3f});')
    for i, j in E:
        if V[i][2] or V[j][2]:
            out.append(f'\\draw[black, thin] ({XY[i][0]:.3f},{XY[i][1]:.3f}) -- ({XY[j][0]:.3f},{XY[j][1]:.3f});')
    for (x, y), (_, _, fr), m in zip(XY, V, mult):
        out.append(f'\\fill ({x:.3f},{y:.3f}) circle (1.7pt);' if fr else
                   f'\\draw[black!55, fill=white] ({x:.3f},{y:.3f}) circle (1.7pt);')
        if m > 1:
            out.append(f'\\node[font=\\scriptsize, anchor=west, inner sep=1pt] at ({x + 0.07:.3f},{y:.3f}) {{$\\times {m}$}};')
    label = O['name'].replace('$`', '$').replace('`$', '$')
    out.append(f'\\node[font=\\footnotesize, align=center] at ({cx:.3f},{cy - R - 0.42:.3f}) '
               f'{{{label}\\\\ $({O["sig"][0]}, {O["sig"][1]}, {O["sig"][2]})$}};')
    O['stars'] = [dict(point=[round(c, 6) for c in p], multiplicity=m) for p, m in zip(P, mult)]
    O['edges'] = len(E)
    return out


PREAMBLE = ('\\pdfinfoomitdate=1\n\\pdftrailerid{}\n\\pdfsuppressptexinfo=-1\n'
            '\\documentclass[border=6pt]{standalone}\n\\usepackage{amsmath,amssymb}\n\\usepackage{tikz}\n'
            '\\usetikzlibrary{arrows.meta,decorations.pathreplacing,positioning}\n\\begin{document}\n')


def build(name, body):
    os.makedirs(FIGS, exist_ok=True)
    tex = PREAMBLE + body + '\n\\end{document}\n'
    with open(os.path.join(FIGS, name + '.tex'), 'w') as f:
        f.write(tex)
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', name + '.tex'], cwd=FIGS,
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f'STOP: pdflatex failed on {name}:\n' + r.stdout[-1500:])
    subprocess.run(['pdftocairo', '-png', '-r', '300', '-singlefile', name + '.pdf', name], cwd=FIGS, check=True)
    for ext in ('aux', 'log'):
        os.remove(os.path.join(FIGS, f'{name}.{ext}'))
    note(f'wrote figures/{name}.tex, .pdf and .png')


# Figure 1: the slots
POS = {0: (0.0, 0.0), 1: (1.9, 0.0), 3: (3.8, 0.0), 6: (5.7, 0.0), 7: (7.6, 0.0), 8: (9.5, 0.0),
       4: (11.2, 1.3), 5: (11.2, -1.3), 2: (13.1, -1.3)}
WHERE = {0: 'below', 1: 'above', 3: 'below', 6: 'above', 7: 'below', 8: 'above left=5pt and -2pt of', 4: 'above',
         5: 'below', 2: 'below'}
s = ['\\begin{tikzpicture}[line cap=round, line join=round,',
     '  soft/.style={circle, draw, line width=1.3pt, fill=white, minimum size=10pt, inner sep=0pt},',
     '  rigid/.style={circle, fill, minimum size=6pt, inner sep=0pt}]']
for k, (x, y) in POS.items():
    s.append(f'\\node[{"soft" if k in SOFT else "rigid"}] (R{k}) at ({x:.2f},{y:.2f}) {{}};')
for a, b in EDGES:
    s.append(f'\\draw[semithick] (R{a}) -- (R{b});')
for k in POS:
    w = WHERE[k]
    w = w if ' of' in w else f'{w}=5pt of'
    s.append(f'\\node[{w} R{k}, font=\\small, inner sep=1pt] {{$R_{k}$ \\ ({dist[k]})}};')
s.append('\\node[font=\\footnotesize, anchor=north] at (0,-0.95) {control};')
s.append('\\draw[decorate, decoration={brace, amplitude=5pt, mirror}, black!60] (1.70,-1.05) -- (9.70,-1.05);')
s.append('\\node[font=\\footnotesize, align=center, anchor=north] at (5.70,-1.30) '
         '{rigid: $\\mathrm{Sym}^{n}\\mathbb{C}^2$ restricts to the slot itself,\\\\ and every lowest-level section has constant norm};')
s.append('\\node[font=\\footnotesize, align=center, anchor=west] at (12.0,1.30) '
         '{soft: the restriction is reducible,\\\\ and a reduced quartic types the branches};')
s.append('\\node[font=\\footnotesize, anchor=west] at (0.2,-2.55) {$(n)$: the lowest level, $k(k+2)/R^2$ at $k = n$, '
         'which is the distance from $R_0$};')
s.append('\\end{tikzpicture}')
build('figure-slots', '\n'.join(s))

# Figure 2: the shape of the small-amplitude spectrum, a schematic
def plane(x0, title, slow):
    o = [f'\\draw[->, black!70] ({x0 - 1.45:.2f},0) -- ({x0 + 1.55:.2f},0) node[right, font=\\scriptsize] {{Re}};',
         f'\\draw[->, black!70] ({x0:.2f},-2.05) -- ({x0:.2f},2.15) node[above, font=\\scriptsize] {{Im}};',
         f'\\draw[black!40, dashed] ({x0:.2f},0) circle (0.62);']
    for yv in (1.10, 1.42, 1.78, -1.10, -1.42, -1.78):
        o.append(f'\\fill ({x0:.2f},{yv:.2f}) circle (1.5pt);')
    o.append(f'\\draw ({x0:.2f},0) circle (2.3pt); \\fill ({x0:.2f},0) circle (1.2pt);')
    o += slow
    o.append(f'\\node[font=\\footnotesize, align=center, anchor=north] at ({x0:.2f},-2.35) {{{title}}};')
    return o


s = ['\\begin{tikzpicture}[line cap=round, line join=round]']
s += plane(0.0, '(a) elliptic: imaginary,\\\\ each pair with a Krein sign',
           ['\\fill (0,0.24) circle (1.5pt); \\fill (0,-0.24) circle (1.5pt);',
            '\\fill (0,0.44) circle (1.5pt); \\fill (0,-0.44) circle (1.5pt);',
            '\\node[font=\\scriptsize, anchor=west] at (0.07,0.24) {$+$};',
            '\\node[font=\\scriptsize, anchor=west] at (0.07,0.44) {$-$};'])
s += plane(4.3, '(b) hyperbolic:\\\\ a real pair',
           ['\\fill (3.92,0) circle (1.5pt); \\fill (4.68,0) circle (1.5pt);'])
s += plane(8.6, '(c) hyperbolic:\\\\ a complex quartet',
           ['\\fill (8.28,0.26) circle (1.5pt); \\fill (8.92,0.26) circle (1.5pt);',
            '\\fill (8.28,-0.26) circle (1.5pt); \\fill (8.92,-0.26) circle (1.5pt);'])
s.append('\\draw[decorate, decoration={brace, amplitude=4pt}, black!60] (-0.18,1.00) -- (-0.18,1.88);')
s.append('\\node[font=\\scriptsize, anchor=east, align=right] at (-0.32,1.44) {fast part,\\\\ imaginary};')
s.append('\\draw[black!60] (-0.44,-0.44) -- (-0.95,-0.95) node[anchor=north east, font=\\scriptsize, align=right, '
         'inner sep=1pt] {slow part,\\\\ within $O(\\varepsilon)$ of 0};')
s.append('\\draw[black!60] (0.10,-0.06) -- (0.55,-0.95) node[anchor=north west, font=\\scriptsize, align=left, '
         'inner sep=1pt] {zeros forced\\\\ by symmetry};')
s.append('\\end{tikzpicture}')
build('figure-spectrum', '\n'.join(s))

# Figure 3: the orbits, by type, each row in the order of 924 r6
R0_, DX, ROWY = 0.85, 2.40, (0.0, -3.55)
rows = [sorted([O for O in ORB if O['stable']], key=lambda O: O['v']),
        sorted([O for O in ORB if not O['stable']], key=lambda O: O['v'])]
s = ['\\begin{tikzpicture}[line cap=round]']
for (title, row), yrow in zip((('spectrally stable at small amplitude', rows[0]),
                               ('spectrally unstable at small amplitude', rows[1])), ROWY):
    s.append(f'\\node[font=\\small\\itshape, anchor=west] at ({-R0_:.2f},{yrow + R0_ + 0.42:.2f}) {{{title}}};')
    for i, O in enumerate(row):
        s += constellation(O, i * DX, yrow, R0_)
s.append('\\end{tikzpicture}')
build('figure-orbits', '\n'.join(s))
for O in ORB:
    note(f"  {O['name']}: {O['type']}; {len(O['stars'])} distinct stars, multiplicities "
         f"{[st['multiplicity'] for st in O['stars']]}, {O['edges']} edges")

with open(os.path.join(OUT, 'theory.json'), 'w') as f:
    json.dump({'commits': {'page': REV_PAGE, 'certificates': REV_CERT},
               'slots': {f'R{k}': dict(dim=DIM[k], level=dist[k], kind='control' if k == 0 else
                                       'soft' if k in SOFT else 'rigid') for k in range(9)},
               'orbits': [{k: (v if k != 'W' else [[round(w.real, 12), round(w.imag, 12)] for w in v])
                           for k, v in O.items() if k not in ('v',)} for O in ORB]}, f, indent=1, ensure_ascii=False)
    f.write('\n')
with open(os.path.join(OUT, 'fig_theory_log.txt'), 'w') as f:
    f.write('\n'.join(LOG) + '\n')
print('done')
