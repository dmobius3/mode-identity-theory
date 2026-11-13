"""Figure 1 of Paper 2: OpenWave's adjudicated census at its close on 2026-11-10, drawn from the committed records alone.

Reads, at MIT commit c7e3f46e: M8.17's record (§ 3, every registered point of the nine branches with its classification
and instrument; § 4, the prism's located interval in R4 and its guards), M8.18's record (O3's located interval in R5 and
its guards) and M8.15.2's record (the hexagon's two mesh-level n(L) steps in R5 and its guards). Writes census.json, what
it read with the record each value came from; figure1-census.tex, .pdf and .png, the figure in TikZ in the style of
the repository's other figures, its PDF without dates; and fig_census_log.txt. Before drawing, it
checks each row against the census's close as Table 6 states it: the window, the classified and open points, the types.
Usage: fig_census.py [MIT_CLONE [OUT_DIR]]; by default the repository this script is in, and this folder, with
the images in its figures/ folder."""
import json
import os
import re
import subprocess
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
MIT = sys.argv[1] if len(sys.argv) > 1 else subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'],
                                                           capture_output=True, text=True, check=True).stdout.strip()
OUT = sys.argv[2] if len(sys.argv) > 2 else HERE
FIGS = os.path.join(OUT, 'figures')
REV = 'c7e3f46e'
S = 'files/framework/files/working/files/scripts'
LOG = []


def note(*a):
    s = ' '.join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


def show(path):
    return subprocess.run(['git', '-C', MIT, 'show', f'{REV}:{path}'], capture_output=True, text=True,
                          check=True).stdout.replace('−', '-')


R17 = show(f'{S}/soft-slot-dynamics-m8-17/RECORD.md')
R18 = show(f'{S}/soft-slot-dynamics-m8-18/RECORD.md')
R152 = show(f'{S}/soft-slot-dynamics-m8-15-2/RECORD.md')

# --- every registered point, from M8.17's § 3 -----------------------------------------------------------------------
sec3 = R17.split('\n## 3.', 1)[1].split('\n## 4.', 1)[0]
ROWS = {}
for block in re.split(r'\n### ', sec3)[1:]:
    key = block.split(',', 1)[0]
    pts = []
    for l in block.splitlines():
        if re.match(r'^\| [0-9]', l):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            cl = c[1]
            kind = ('E' if cl == 'Elliptic' else 'H' if cl == 'Hyperbolic'
                    else 'U' if 'accounted for' in cl else 'O' if cl == 'not classified' else None)
            assert kind, (key, l[:80])
            pts.append({'eps': float(c[0]), 'eps_text': c[0], 'classification': cl, 'kind': kind, 'instrument': c[2]})
    ROWS[key] = pts
assert sorted(ROWS) == ['T1/R4', 'T1/R5', 'T2/R4', 'T2/R5', 'T3/R4', 'T3/R5', 'T4/R4', 'T4/R5', 'T5/R2'], sorted(ROWS)


def grab(pattern, text, what):
    m = re.search(pattern, text, re.S)
    assert m, what
    return m.groups()


# --- the three located intervals, each from its own record ---------------------------------------------------------------
t2 = R17.split('- **T2/R4, (16, 22.63),**', 1)[1].split('\n- **', 1)[0]
p_lo, p_hi = grab(r'The union at `N = 24` and 32: \[([\d.]+), ([\d.]+)\]', t2, 'prism union')
p_ge = grab(r'The lower guard, `δ = 0\.01`, at `ε = ([\d.]+)`, .*?: Elliptic', t2, 'prism lower guard')[0]
p_gh = grab(r'The upper guard, `δ = 0\.01`, at `ε = ([\d.]+)`, .*?: Hyperbolic', t2, 'prism upper guard')[0]
o_lo, o_hi = grab(r'The interval at `N = 24` and 32 is \[([\d.]+), ([\d.]+)\]', R18, 'O3 interval')
o_ge = grab(r'\| lower \| 0\.01 \| ([\d.]+) \|[^\n]*converged: Elliptic', R18, 'O3 lower guard')[0]
o_gh = grab(r'\| upper \| 0\.05 \| ([\d.]+) \|[^\n]*converged: Hyperbolic', R18, 'O3 upper guard')[0]
hx = R152.split('### T3/R5', 1)[1].split('\n### ', 1)[0]
h3 = grab(r'\| 3 \| genuine \| [^|]+ \| ([\d.]+) to ([\d.]+) \|', hx, 'hexagon level 3')
h2 = grab(r'\| 2 \| genuine \| [^|]+ \| ([\d.]+) to ([\d.]+) \|', hx, 'hexagon level 2')
h_ge = grab(r'\| lower \| `d = 0\.01` \| ([\d.]+) \| [\d.]+ \| Elliptic', hx, 'hexagon lower guard')[0]
h_gh = grab(r'\| upper \| `d = 0\.05` \| ([\d.]+) \| [\d.]+ \| Hyperbolic', hx, 'hexagon upper guard')[0]
BRACKETS = {
    'T2/R4': {'kind': 'harmonic', 'nL': [[p_lo, p_hi]], 'labels': ['N = 24 and 32'], 'guards': [p_ge, p_gh],
              'guard_note': '1% outside', 'source': 'M8.17 record, § 4'},
    'T3/R5': {'kind': 'finite element', 'nL': [list(h3), list(h2)], 'labels': ['mesh level 3', 'mesh level 2'],
              'guards': [h_ge, h_gh], 'guard_note': 'level 3; the upper read at 5%', 'source': 'M8.15.2 record, T3/R5'},
    'T4/R5': {'kind': 'harmonic', 'nL': [[o_lo, o_hi]], 'labels': ['N = 24 and 32'], 'guards': [o_ge, o_gh],
              'guard_note': 'the upper read at 5%, on the retry', 'source': 'M8.18 record'},
}

# --- each row against the census's close, as Table 6 states it ------------------------------------------------------------
GAP = {'R4': 72, 'R5': 32, 'R2': 132}
NAME = {'T1': ('$v_2$', 'v2'), 'T2': ('prism', 'prism'), 'T3': ('hexagon', 'hexagon'), 'T4': (r'$\mathcal{O}_3$', 'O3'),
        'T5': ('line {7/2, −3/2}, member $i$', 'member i')}
TABLE6 = {  # (ending, Elliptic count, Hyperbolic count, open points), Table 6 of the draft, which check v16 ties to the census
    'T2/R5': ('Elliptic throughout', 15, 0, []), 'T3/R4': ('Elliptic throughout', 18, 0, []),
    'T2/R4': ('change of type bracketed', None, None, []), 'T3/R5': ('change of type bracketed', None, None, []),
    'T4/R5': ('change of type bracketed', None, None, []),
    'T1/R4': ('discretization-limited', 13, 0, ['1.41', '32', '45.25', '64', '72']),
    'T1/R5': ('discretization-limited', 14, 0, ['32']),
    'T4/R4': ('discretization-limited', None, None, ['4', '8', '11.31', '64', '72']),
    'T5/R2': ('discretization-limited', 17, 0, ['45.25', '128', '132']),
}
grid = lambda n_k, extra: [round(0.25 * 2 ** (k / 2), 6) for k in range(n_k)] + extra
GRID = {'R4': grid(17, [72.0]), 'R5': grid(15, []), 'R2': grid(19, [132.0])}
for key, pts in ROWS.items():
    slot = key.split('/')[1]
    eps = [p['eps'] for p in pts]
    assert len(eps) == len(GRID[slot]) and all(abs(a - b) <= 0.006 * b for a, b in zip(eps, GRID[slot])), key
    assert eps[-1] == GAP[slot], key
    ending, n_e, n_h, opens = TABLE6[key]
    ke = sum(p['kind'] == 'E' for p in pts)
    kh = sum(p['kind'] == 'H' for p in pts)
    ko = [p['eps_text'] for p in pts if p['kind'] == 'O']
    assert ko == opens, (key, ko, opens)
    if n_e is not None:
        assert (ke, kh) == (n_e, n_h), (key, ke, kh)
    if ending == 'change of type bracketed':
        assert key in BRACKETS and not ko, key
        kinds = [p['kind'] for p in pts if p['kind'] in 'EH']
        assert kinds == sorted(kinds), key  # Elliptic, then Hyperbolic, at the classified points
    note(f'{key}: {len(pts)} points, {ke} Elliptic, {kh} Hyperbolic, open {ko or "none"}, '
         f'undecided {[p["eps_text"] for p in pts if p["kind"] == "U"] or "none"}; {ending}')
assert [p['eps_text'] for p in ROWS['T3/R5'] if p['kind'] == 'U'] == ['16']
assert [p['eps_text'] for p in ROWS['T4/R4'] if p['kind'] == 'H'] == ['5.66', '16', '22.63', '32', '45.25']

os.makedirs(FIGS, exist_ok=True)
with open(os.path.join(OUT, 'census.json'), 'w') as f:
    json.dump({'commit': REV, 'sources': {'points': 'soft-slot-dynamics-m8-17/RECORD.md, § 3',
                                          'T2/R4': BRACKETS['T2/R4']['source'], 'T3/R5': BRACKETS['T3/R5']['source'],
                                          'T4/R5': BRACKETS['T4/R5']['source']},
               'rows': ROWS, 'brackets': BRACKETS}, f, indent=1, ensure_ascii=False)
note('wrote census.json')

# --- the figure, in TikZ, in the style of the repository's other figures ---------------------------------------------------
import math  # noqa: E402

ORDER = [('R4', ['T1/R4', 'T2/R4', 'T3/R4', 'T4/R4']), ('R5', ['T1/R5', 'T2/R5', 'T3/R5', 'T4/R5']), ('R2', ['T5/R2'])]
HEAD = {'R4': '$R_4$, to its gap at 72', 'R5': '$R_5$, to its gap at 32',
        'R2': '$R_2$, the line $\\{7/2, -3/2\\}$, to its gap at 132'}
LABEL = {'T1': '$v_2$', 'T2': 'prism', 'T3': 'hexagon', 'T4': '$\\mathcal{O}_3$', 'T5': 'member $i$'}
ROMAN = {'T2/R4': 'i', 'T3/R5': 'ii', 'T4/R5': 'iii'}
TITLE = {'T2/R4': ('prism, $R_4$', 'Galerkin, $N = 24$ and 32'),
         'T3/R5': ('hexagon, $R_5$', 'finite element, two mesh levels'),
         'T4/R5': ('$\\mathcal{O}_3$, $R_5$', 'Galerkin, $N = 24$ and 32')}
W, LO, HI = 13.0, 0.21, 175.0
TICKS = [0.25, 0.5, 1, 2, 4, 8, 16, 32, 72, 132]
X = lambda e: W * (math.log(e) - math.log(LO)) / (math.log(HI) - math.log(LO))


def mark(kind, x, y):
    if kind == 'E':
        return f'\\fill ({x:.3f},{y:.3f}) circle (1.7pt);'
    if kind == 'H':
        return f'\\fill ([shift={{(-1.55pt,-1.55pt)}}]{x:.3f},{y:.3f}) rectangle ++(3.1pt,3.1pt);'
    if kind == 'O':
        return f'\\draw[black!75, fill=white, line width=0.6pt] ({x:.3f},{y:.3f}) circle (1.7pt);'
    if kind == 'U':
        return f'\\draw[black!75, line width=0.9pt] ([yshift=-3.2pt]{x:.3f},{y:.3f}) -- ([yshift=3.2pt]{x:.3f},{y:.3f});'
    if kind == 'V':
        return f'\\fill ({x:.3f},{y:.3f}) -- ++(-2.6pt,4pt) -- ++(5.2pt,0) -- cycle;'
    raise SystemExit(f'STOP: no mark for {kind}')


s = ['\\begin{tikzpicture}[line cap=round, line join=round]']
y, ys = 0.0, {}
for slot, keys in ORDER:
    s.append(f'\\node[font=\\footnotesize, anchor=west, fill=white, inner sep=1pt] at ({X(0.25) - 0.13:.3f},{y + 0.40:.3f}) '
             f'{{{HEAD[slot]}}};')
    for key in keys:
        ys[key] = y
        s.append(f'\\node[font=\\small, anchor=east] at (-0.15,{y:.3f}) {{{LABEL[key.split("/")[0]]}}};')
        y -= 0.52
    y -= 0.40
ybot, ytop = y + 0.20, 0.62
s[1:1] = [f'\\draw[black!10] ({X(t):.3f},{ybot:.3f}) -- ({X(t):.3f},{ytop:.3f});' for t in TICKS]  # the grid, underneath
for key, pts in ROWS.items():
    slot = key.split('/')[1]
    s.append(f'\\draw[black!25, line width=0.8pt] ({X(0.25):.3f},{ys[key]:.3f}) -- ({X(GAP[slot]):.3f},{ys[key]:.3f});')
for key, pts in ROWS.items():
    for p in pts:
        s.append(mark(p['kind'], X(p['eps']), ys[key]))
    if key in BRACKETS:
        lo, hi = (float(v) for v in BRACKETS[key]['nL'][0])
        xc = X((lo * hi) ** 0.5)
        s.append(mark('V', xc, ys[key] + 0.13))
        s.append(f'\\node[font=\\scriptsize, anchor=west, fill=white, inner sep=1pt] at ({xc + 0.07:.3f},{ys[key] + 0.24:.3f}) '
                 f'{{({ROMAN[key]})}};')
s.append(f'\\draw[black!70] ({X(LO):.3f},{ybot:.3f}) -- ({X(HI):.3f},{ybot:.3f});')
for t in TICKS:
    txt = f'{t:g}'
    s.append(f'\\draw[black!70] ({X(t):.3f},{ybot:.3f}) -- ++(0,-0.08) node[below, font=\\footnotesize] {{{txt}}};')
s.append(f'\\node[font=\\small] at ({W / 2:.3f},{ybot - 0.78:.3f}) {{$\\varepsilon$, in units of $1/R^2$, on a log scale}};')
LEG = [('E', 'classified Elliptic'), ('H', 'classified Hyperbolic'), ('O', 'not classified: discretization-limited'),
       ('U', 'unclassified, inside a bracketing interval'), ('V', 'a bracketed change, enlarged in (b)')]
LPOS = [(0.2, 0), (4.1, 0), (8.0, 0), (0.2, 1), (6.35, 1)]
for (k, txt), (lx, row) in zip(LEG, LPOS):
    ly = ytop + 0.95 - 0.42 * row
    s.append(mark(k, lx, ly - (0.07 if k == 'V' else 0)))
    s.append(f'\\node[font=\\footnotesize, anchor=west] at ({lx + 0.14:.3f},{ly:.3f}) {{{txt}}};')
s.append(f'\\node[font=\\small\\bfseries, anchor=west] at (-1.75,{ytop + 0.25:.3f}) {{(a)}};')

# (b): the three located intervals at scale, each between its guards
yb = ybot - 2.05
s.append(f'\\node[font=\\small\\bfseries, anchor=west] at (-1.75,{yb + 0.75:.3f}) {{(b)}};')
for j, key in enumerate(['T2/R4', 'T3/R5', 'T4/R5']):
    b = BRACKETS[key]
    x0, w = 0.0 + 4.6 * j, 3.7
    g_e, g_h = float(b['guards'][0]), float(b['guards'][1])
    span = g_h - g_e
    a0, a1 = g_e - 0.1 * span, g_h + 0.1 * span
    xb = lambda v: x0 + w * (v - a0) / (a1 - a0)
    t1, t2 = TITLE[key]
    s.append(f'\\node[font=\\footnotesize, anchor=south west, align=left, inner sep=0pt] at ({x0:.3f},{yb + 0.38:.3f}) '
             f'{{({ROMAN[key]}) {t1}\\\\ {t2}}};')
    s.append(f'\\draw[black!25, line width=0.8pt] ({xb(g_e):.3f},{yb:.3f}) -- ({xb(g_h):.3f},{yb:.3f});')
    s.append(mark('E', xb(g_e), yb))
    s.append(mark('H', xb(g_h), yb))
    if key == 'T3/R5':
        s.append(mark('U', xb(16.0), yb))
        s.append(f'\\node[font=\\scriptsize, above, inner sep=2pt] at ({xb(16.0):.3f},{yb + 0.08:.3f}) {{16}};')
    for i, ((lo, hi), lab) in enumerate(zip(b['nL'], b['labels'])):
        yy = yb - 0.36 - 0.30 * i
        s.append(f'\\draw[line width=2.4pt, line cap=butt] ({xb(float(lo)):.4f},{yy:.3f}) -- ({xb(float(hi)):.4f},{yy:.3f});')
        txt = '$n(L)$ changes' + ('' if len(b['nL']) == 1 else f', {lab}')
        s.append(f'\\node[font=\\scriptsize, anchor=west, inner sep=1pt] at ({xb(float(hi)) + 0.08:.3f},{yy:.3f}) {{{txt}}};')
    ya = yb - 0.36 - 0.30 * max(len(c['nL']) for c in BRACKETS.values()) - 0.05
    s.append(f'\\draw[black!70] ({x0:.3f},{ya:.3f}) -- ({x0 + w:.3f},{ya:.3f});')
    for g in b['guards']:
        s.append(f'\\draw[black!70] ({xb(float(g)):.3f},{ya:.3f}) -- ++(0,-0.08) node[below, font=\\scriptsize] {{{g}}};')
s.append('\\end{tikzpicture}')

PREAMBLE = ('\\pdfinfoomitdate=1\n\\pdftrailerid{}\n\\pdfsuppressptexinfo=-1\n'
            '\\documentclass[border=6pt]{standalone}\n\\usepackage{amsmath,amssymb}\n\\usepackage{tikz}\n'
            '\\begin{document}\n')
NAME = 'figure1-census'
with open(os.path.join(FIGS, NAME + '.tex'), 'w') as f:
    f.write(PREAMBLE + '\n'.join(s) + '\n\\end{document}\n')
r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', NAME + '.tex'], cwd=FIGS,
                   capture_output=True, text=True)
if r.returncode:
    raise SystemExit('pdflatex failed:\n' + r.stdout[-1500:])
subprocess.run(['pdftocairo', '-png', '-r', '300', '-singlefile', NAME + '.pdf', NAME], cwd=FIGS, check=True)
for ext in ('aux', 'log'):
    os.remove(os.path.join(FIGS, f'{NAME}.{ext}'))
note(f'wrote figures/{NAME}.tex, .pdf and .png')
with open(os.path.join(OUT, 'fig_census_log.txt'), 'w') as f:
    f.write('\n'.join(LOG) + '\n')
