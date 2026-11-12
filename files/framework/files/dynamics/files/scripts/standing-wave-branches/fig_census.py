"""Figure 1 of Paper 2: OpenWave's adjudicated census at its close on 2026-11-10, drawn from the committed records alone.

Reads, at MIT commit c7e3f46e: M8.17's record (§ 3, every registered point of the nine branches with its classification
and instrument; § 4, the prism's located interval in R4 and its guards), M8.18's record (O3's located interval in R5 and
its guards) and M8.15.2's record (the hexagon's two mesh-level n(L) steps in R5 and its guards). Writes census.json, what
it read with the record each value came from; figure1-census.pdf and .png; and fig_census_log.txt. Before drawing, it
checks each row against the census's close as Table 6 states it: the window, the classified and open points, the types.
Usage: fig_census.py [MIT_CLONE [OUT_DIR]]; by default the repository this script is in, and this folder, with
the images in its figures/ folder."""
import json
import os
import re
import subprocess
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

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
    'T2/R5': ('elliptic throughout', 15, 0, []), 'T3/R4': ('elliptic throughout', 18, 0, []),
    'T2/R4': ('change of type located', None, None, []), 'T3/R5': ('change of type located', None, None, []),
    'T4/R5': ('change of type located', None, None, []),
    'T1/R4': ('instrument-limited', 13, 0, ['1.41', '32', '45.25', '64', '72']),
    'T1/R5': ('instrument-limited', 14, 0, ['32']),
    'T4/R4': ('instrument-limited', None, None, ['4', '8', '11.31', '64', '72']),
    'T5/R2': ('instrument-limited', 17, 0, ['45.25', '128', '132']),
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
    if ending == 'change of type located':
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

# --- the figure ---------------------------------------------------------------------------------------------------------------
INK, INK2, GRIDC, SURFACE, SHADE = '#0b0b0b', '#52514e', '#e3e2dd', '#ffffff', '#f1f0ec'
ELL, HYP = '#2a78d6', '#eb6834'
plt.rcParams.update({'font.size': 8.5, 'axes.labelsize': 8.5, 'axes.edgecolor': INK2, 'axes.labelcolor': INK,
                     'xtick.color': INK2, 'ytick.color': INK2, 'axes.linewidth': 0.6, 'grid.color': GRIDC,
                     'grid.linewidth': 0.6, 'grid.linestyle': '-', 'axes.axisbelow': True, 'legend.frameon': False,
                     'legend.fontsize': 7.5, 'figure.facecolor': SURFACE, 'axes.facecolor': SURFACE,
                     'savefig.facecolor': SURFACE, 'lines.solid_capstyle': 'round', 'mathtext.fontset': 'dejavusans'})
MK = {'E': dict(marker='o', ms=5.4, color=ELL, mec=SURFACE, mew=0.8, ls='none', zorder=3),
      'H': dict(marker='s', ms=4.9, color=HYP, mec=SURFACE, mew=0.8, ls='none', zorder=3),
      'O': dict(marker='o', ms=5.4, mfc=SURFACE, mec=INK2, mew=1.0, ls='none', zorder=3),
      'U': dict(marker='|', ms=7.0, color=INK2, mew=1.2, ls='none', zorder=3)}

ORDER = [('R4', ['T1/R4', 'T2/R4', 'T3/R4', 'T4/R4']), ('R5', ['T1/R5', 'T2/R5', 'T3/R5', 'T4/R5']), ('R2', ['T5/R2'])]
HEAD = {'R4': '$R_4$, to its gap at 72', 'R5': '$R_5$, to its gap at 32', 'R2': r'$R_2$, the line {7/2, $-$3/2}, to its gap at 132'}
LABEL = {'T1': '$v_2$', 'T2': 'prism', 'T3': 'hexagon', 'T4': r'$\mathcal{O}_3$', 'T5': 'member $i$'}
ROMAN = {'T2/R4': 'i', 'T3/R5': 'ii', 'T4/R5': 'iii'}
fig = plt.figure(figsize=(7.2, 6.0))
gs = fig.add_gridspec(2, 3, height_ratios=[3.6, 1.0], left=0.11, right=0.985, top=0.885, bottom=0.075, hspace=0.42,
                      wspace=0.3)
ax = fig.add_subplot(gs[0, :])
y, ys, yt = 0.0, {}, []
for slot, keys in ORDER:
    ax.text(0.226, y + 0.62, HEAD[slot], fontsize=7.6, color=INK, ha='left', va='center')
    for key in keys:
        ys[key] = y
        yt.append((y, LABEL[key.split('/')[0]]))
        y -= 1.0
    y -= 0.75
for key, pts in ROWS.items():
    slot = key.split('/')[1]
    yy = ys[key]
    ax.plot([0.25, GAP[slot]], [yy, yy], color=GRIDC, lw=1.0, zorder=1)
    for kind in 'EHOU':
        xs = [p['eps'] for p in pts if p['kind'] == kind]
        if xs:
            ax.plot(xs, [yy] * len(xs), **MK[kind])
    if key in BRACKETS:
        lo, hi = (float(v) for v in BRACKETS[key]['nL'][0])
        xc = (lo * hi) ** 0.5
        ax.plot([xc], [yy + 0.36], marker='v', ms=4.6, color=INK, ls='none', zorder=4)
        ax.text(xc * 1.07, yy + 0.36, f'({ROMAN[key]})', fontsize=6.8, color=INK, va='center', ha='left')
ax.set_xscale('log')
ax.set_xlim(0.21, 175)
ax.set_xticks([0.25, 0.5, 1, 2, 4, 8, 16, 32, 72, 132], ['0.25', '0.5', '1', '2', '4', '8', '16', '32', '72', '132'])
ax.minorticks_off()
ax.set_xlabel(r'$\varepsilon$, in units of $1/R^2$, on a log scale')
ax.set_yticks([v for v, _ in yt], [t for _, t in yt])
ax.tick_params(axis='y', length=0, labelsize=8)
ax.set_ylim(y + 1.35, 1.0)
ax.grid(axis='x')
for side in ('top', 'right', 'left'):
    ax.spines[side].set_visible(False)
handles = [Line2D([], [], **{**MK['E'], 'label': 'classified Elliptic'}),
           Line2D([], [], **{**MK['H'], 'label': 'classified Hyperbolic'}),
           Line2D([], [], **{**MK['O'], 'label': 'not classified: instrument-limited'}),
           Line2D([], [], **{**MK['U'], 'label': 'undecided, inside a located interval'}),
           Line2D([], [], marker='v', ms=4.6, color=INK, ls='none', label='a located change, enlarged below')]
fig.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.55, 0.995), ncol=3, columnspacing=1.4,
           handletextpad=0.4)
fig.text(0.012, 0.885, '(a)', fontsize=9, fontweight='bold', color=INK, va='top')
fig.text(0.012, 0.215, '(b)', fontsize=9, fontweight='bold', color=INK, va='top')

# (b): the three located intervals at scale, each between its guards
TITLE = {'T2/R4': ('prism, $R_4$', 'harmonic, N = 24 and 32'), 'T3/R5': ('hexagon, $R_5$', 'finite element, two mesh levels'),
         'T4/R5': (r'$\mathcal{O}_3$, $R_5$', 'harmonic, N = 24 and 32')}
for j, key in enumerate(['T2/R4', 'T3/R5', 'T4/R5']):
    b = BRACKETS[key]
    a = fig.add_subplot(gs[1, j])
    g_e, g_h = float(b['guards'][0]), float(b['guards'][1])
    span = g_h - g_e
    a.set_xlim(g_e - 0.1 * span, g_h + 0.1 * span)
    a.plot([g_e, g_h], [1, 1], color=GRIDC, lw=1.0, zorder=1)
    a.plot([g_e], [1], **MK['E'])
    a.plot([g_h], [1], **MK['H'])
    if key == 'T3/R5':
        a.plot([16.0], [1], **MK['U'])
        a.text(16.0, 1.32, '16', fontsize=6.3, color=INK2, ha='center', va='bottom')
    for i, ((lo, hi), lab) in enumerate(zip(b['nL'], b['labels'])):
        yy = 0.25 - 0.55 * i
        a.plot([float(lo), float(hi)], [yy, yy], color=INK, lw=3.0, solid_capstyle='butt', zorder=2)
        a.text(float(hi) + 0.03 * span, yy, 'n(L) changes' + ('' if len(b['nL']) == 1 else f', {lab}'), fontsize=6.0,
               color=INK2, ha='left', va='center')
    a.set_ylim(-1.0 if len(b['nL']) > 1 else -0.45, 1.75)
    a.set_xticks([g_e, g_h], [b['guards'][0], b['guards'][1]], fontsize=6.3)
    a.set_yticks([])
    for side in ('top', 'right', 'left'):
        a.spines[side].set_visible(False)
    t1, t2 = TITLE[key]
    a.set_title(f'({ROMAN[key]}) {t1}\n{t2}', fontsize=7.0, color=INK, loc='left', linespacing=1.25)
for ext in ('pdf', 'png'):
    fig.savefig(os.path.join(FIGS, f'figure1-census.{ext}'), dpi=300 if ext == 'png' else None, bbox_inches='tight')
plt.close(fig)
note('wrote figures/figure1-census.pdf and .png')
with open(os.path.join(OUT, 'fig_census_log.txt'), 'w') as f:
    f.write('\n'.join(LOG) + '\n')
