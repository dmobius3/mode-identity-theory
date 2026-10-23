"""Fill the M8.16.1 terms template (v7) from its sources: every hash, link, quote and number is read or computed here,
none typed. Paths are arguments, and the OpenWave revision of M8.16's terms is pinned. Refuses to overwrite its output.

  python3 -I -B build_terms_v7.py MIT_REPO RULING_1015_JSON OW_COMMIT FOLDER T5_DIR [OUT]

MIT_REPO is a checkout at origin/main; FOLDER is M8.16.1's bench folder, whose pinned values file, BOUNDARY.md,
DEVLOG.md, the ladder's kept outputs and the logged test outputs are read, each checked against its record; T5_DIR
holds t5_member_check.out; the template is read from this script's folder. v3 read the bench's preview outputs; v4
reads the pinned values file in their place. v5 takes the units' fixes to v4: the C3 ray's c_g° named as the prediction
without the off-ray part, which v4 mislabelled the spherical part, and the floor's groups counted at each cutoff. v6
cites every entry where the three tests ran, and checks that each cited entry records a test's run. v7 takes the
maintainer's B1 on #650: check 1 matched against the next-order values, and the K3(a) paragraph with it; test 1's
T5 claim, with its arms counted from its output; and the tests' citation, which gains entry 40."""
import ast
import hashlib
import json
import math
import os
import re
import subprocess as sp
import sys

REPO, RULING_1015, OW_COMMIT, FOLDER, T5DIR = sys.argv[1:6]
OUT = sys.argv[6] if len(sys.argv) > 6 else None
HERE = os.path.dirname(os.path.abspath(__file__))
assert re.fullmatch(r'[0-9a-f]{40}', OW_COMMIT), 'OW_COMMIT must be a full commit SHA'
W = 'files/framework/files/working/files'
M816 = f'{W}/scripts/soft-slot-dynamics-m8-16'
D512 = 'https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')


def git(*a):
    return sp.run(['git', *a], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(commit, path, anchor=''):
    return f'https://github.com/dmobius3/mode-identity-theory/blob/{git("rev-parse", commit + "^{commit}")}/{path}{anchor}'


def short(commit):
    return git('rev-parse', '--short=7', commit + '^{commit}')


def sci(x, d=2):
    m, e = f'{x:.{d}e}'.split('e')
    return f'{m}×10' + str(int(e)).translate(SUP)


def kappa(lam0, Q):
    return 1 / (8 * math.sqrt(lam0) * Q)


def cx(v):
    return complex(float(v[0]), float(v[1]))


def fmt(c):
    if isinstance(c, complex) and c.imag != 0:
        out = f'{c.real:+.6g} {"+" if c.imag >= 0 else "−"} {abs(c.imag):.6g} i'
    else:
        out = f'{(c.real if isinstance(c, complex) else c):+.6g}'
    return out.replace('-', '−')


def fmt3(c):
    return f'{c.real:+.3f} {"+" if c.imag >= 0 else "−"} {abs(c.imag):.3f} i'.replace('-', '−')


def folder(*p):
    return os.path.join(FOLDER, *p)


devlog = open(folder('DEVLOG.md'), encoding='utf-8').read()


def logged(path):
    """A file of the folder, read only if DEVLOG.md records its SHA-256."""
    raw = open(path, 'rb').read()
    assert sha(raw) in devlog, f'{os.path.relpath(path, FOLDER)}: its SHA-256 is not in DEVLOG.md'
    return raw


head = git('rev-parse', 'HEAD')
assert head == git('rev-parse', 'origin/main'), 'the checkout is not at origin/main'
terms = open(f'{REPO}/{M816}/run/m8_16_task_details.md', 'rb').read()
ow_terms = sp.run(['gh', 'api', '-H', 'Accept: application/vnd.github.raw', 'repos/openwave-labs/openwave/contents/openwave/xperiments/'
                   f'm8_mit/research/tasks/m8_16_task_details.md?ref={OW_COMMIT}'], capture_output=True, check=True).stdout
assert len(terms) == 48450 and ow_terms[:48450] == terms, 'the governing prefix does not match'
pin = open(f'{REPO}/{M816}/run/MANIFEST_PIN', encoding='utf-8').read().strip()
boundary = sha(open(f'{REPO}/{M816}/BOUNDARY.md', 'rb').read())
boundary_1 = sha(logged(folder('BOUNDARY.md')))

body = json.load(open(RULING_1015, encoding='utf-8'))['data']['node']['body']
sec3 = body[body.index('## 3.'):body.index('## 4.')]
quote = [l for l in sec3.splitlines() if l.startswith('> ')]
assert len(quote) == 1
quote = quote[0]
mit_quote = re.search(r'^> Admitted on #512.*?(?=\n\n)', terms.decode('utf-8'), re.M | re.S)[0]
assert ' '.join(quote.replace('>', ' ').split()) == ' '.join(mit_quote.replace('>', ' ').split()), "the boundary differs from M8.16's quote"

# --- the pinned values file -----------------------------------------------------------------------------------
V = json.loads(logged(folder('run', 'next_order_values.json')))
cases_sha = sha(json.dumps(V['cases'], sort_keys=True, separators=(',', ':')).encode('utf-8'))
assert cases_sha == V['cases_sha256'], 'the cases section differs from its recorded SHA-256'
assert not V['checks']['failed'], V['checks']


def groups(name, N):
    return sorted(V['cases'][name]['cutoffs'][N]['groups'], key=lambda g: abs(cx(g['s'])))


for name in V['cases']:
    a, b = groups(name, '24'), groups(name, '32')
    assert [g['c_over_kappa_s'] for g in a] == [g['c_over_kappa_s'] for g in b], f'{name}: N = 24 and 32 differ'

order = [('P5', 'P5'), ('T1/R4', 'T1/R4'), ('T1/R5', 'T1/R5'), ('T2/R4', 'T2/R4'), ('T2/R5', 'T2/R5'), ('T3/R4', 'T3/R4'),
         ('T3/R5', 'T3/R5'), ('T4/R4', 'T4/R4'), ('T4/R5', 'T4/R5'), ('T5/R2', 'T5/R2'), ('T5J/R2', 'T5J'), ('C3R/R4', 'C3R')]
assert {n for n, _ in order} == set(V['cases'])


def cell(name, N):
    # a quartet's c_g/(kappa s_g) is complex; a pair's is real, its stored imaginary part the 50-digit residue
    out = '; '.join(fmt(cx(g['c_over_kappa_s']) if g['cls'] == 'complex' else cx(g['c_over_kappa_s']).real)
                    + (' (double)' if int(g['mult']) == 2 else '')
                    for g in groups(name, N) if g['under_bar'] is True)
    assert all(abs(cx(g['c_over_kappa_s']).imag) < 1e-40 for g in groups(name, N) if g['cls'] != 'complex')
    assert out, f'{name}, N = {N}: no group under the bar'
    return out


WORDS = dict(enumerate(('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')))


lines = ['| case | `N = 24` and 32: `c_g/(κs_g)` | `N = 16` |', '| --- | --- | --- |']
lines += [f'| {label} | {cell(name, "24")} | {cell(name, "16")} |' for name, label in order]
preview = '\n'.join(lines)

ROWS = [n for n, _ in order if n not in ('P5', 'T5J/R2', 'C3R/R4')]
small = [(n, g) for n in ROWS for g in groups(n, '24') if abs(cx(g['c_over_kappa_s'])) < 0.01]
small16 = [(n, g) for n in ROWS for g in groups(n, '16') if abs(cx(g['c_over_kappa_s'])) < 0.01]
assert len(small) == len([g for n in ROWS for g in groups(n, '32') if abs(cx(g['c_over_kappa_s'])) < 0.01])
for N in ('16', '24', '32'):              # beyond the rows, the floor binds at the pyramid's Krein-positive pair and the C3 ray's third group
    beyond = [(n, i) for n in ('P5', 'T5J/R2', 'C3R/R4') for i, g in enumerate(groups(n, N))
              if g['under_bar'] is True and abs(cx(g['c_over_kappa_s'])) < 0.01]
    assert beyond == [('P5', 2), ('C3R/R4', 2)] and groups('P5', N)[2]['krein'] == '+', (N, beyond)
t2 = groups('T2/R5', '24')[0], groups('T2/R5', '16')[0]
assert int(t2[0]['mult']) == 2 and min(abs(cx(g['c_over_kappa_s'])) for _, g in small) == abs(cx(t2[0]['c_over_kappa_s']))
t2c, t2c16 = abs(cx(t2[0]['c_over_kappa_s'])), abs(cx(t2[1]['c_over_kappa_s']))

t4 = groups('T4/R5', '24')[0], groups('T4/R5', '16')[0]
mu = abs(cx(t4[0]['kappa_s']))
cg, cg16 = cx(t4[0]['c_over_kappa_s']).real, cx(t4[1]['c_over_kappa_s']).real
ceil4 = max(0.1 * abs(cg), 1e-3) * mu
trig = ceil4 / 10 / (128 / 3 + 8 + 1 / 3)
t4x = max(float(g['cross_check_relative_difference']) for n in ('T4/R4', 'T4/R5') for N in ('16', '24', '32')
          for g in groups(n, N))

quartet = cx(groups('P5', '24')[1]['c_over_kappa_s'])
assert groups('P5', '24')[1]['cls'] == 'complex'
c3 = groups('C3R/R4', '32')
c3q, c3m, c3p = (cx(c3[0]['s']), cx(c3[1]['s']).imag, cx(c3[2]['s']).imag)
assert c3[0]['cls'] == 'complex' and c3[1]['krein'] == '-' and c3[2]['krein'] == '+'
c3_lam = 0.25 * abs(cx(c3[0]['kappa_s']))
q24 = groups('C3R/R4', '24')[0]
c3_tot = cx(q24['c_over_kappa_s'])
c3_c0 = cx(q24['c_without_off_ray_over_kappa_s'])
ratios = []
for N in ('16', '24', '32'):
    for g in groups('C3R/R4', N):
        ks, c, c0 = cx(g['kappa_s']), cx(g['c_g']), cx(g['c_g_without_off_ray'])
        ratios.append(abs(c - c0) / (0.1 * max(0.1 * abs(c), 1e-3 * abs(ks))))

t5out = open(f'{T5DIR}/t5_member_check.out', encoding='utf-8').read()
t5i, t5j = [ast.literal_eval(x) for x in re.findall(r'tau, registered: (\[[^]]*\]); second: (\[[^]]*\])', t5out)[0]]
t5j_lam = 0.25 * kappa(63, 22 / 13) * float(t5j[0])

# --- the logged outputs: the record regression, the tests ------------------------------------------------------
rec = logged(folder('run', 'score_record.out')).decode('utf-8')
pairs = {}
for N, name, z in re.findall(r'N = (\d+), group 2, (c[23]): ([-+0-9.e]+ [-+][0-9.e+-]+j)', rec):
    pairs.setdefault(N, {})[name] = complex(z.replace(' ', ''))
spread = max(abs(p['c3'] - p['c2']) for p in pairs.values())
decades = [float(x) for x in re.findall(r', ([0-9.]+) decades, entry 8', rec)]
assert len(pairs) == 3 and len(decades) == 6
tv_text = logged(folder('run', 'test_verdicts.out')).decode('utf-8')
tv = re.search(r'^0 failed of (\d+)$', tv_text, re.M)[1]
tm = len(re.findall(r'^   PASS  M\d+\. ', tv_text, re.M))      # test 1's mutation arms, each red
assert tm and not re.search(r'^   FAIL ', tv_text, re.M)
entries = dict(re.findall(r'^## (\d+)\. (.*?)(?=^## \d+\. |\Z)', devlog, re.M | re.S))
for n in (14, 15, 16, 23, 28, 29, 30, 40):                # the tests section's citation: each entry records a test's run
    assert str(n) in entries and re.search(r'test_(?:verdicts|constants|imports)', entries[str(n)]), n
tg = re.search(r'^0 failed of (\d+)$', logged(folder('run', 'test_guard.out')).decode('utf-8'), re.M)[1]

# --- amendment 5's ladder, from its kept outputs ---------------------------------------------------------------
LAD = folder('dev', 'runs', '015_ladder')
raw = logged(os.path.join(LAD, 'C2a_R5_ladder.json'))
runlog = json.loads(logged(os.path.join(LAD, 'RUNLOG.json')))
assert next(iter(runlog['completed']['C2a/R5:ladder']['files'].values())) == sha(raw)
lad = json.loads(raw)
key = lambda e: f'{e:.12g}'  # noqa: E731
eps = [p['eps'] for p in lad['case']['points']]
accepted = sum(bool(c['points'][key(e)].get('accepted')) for c in lad['cutoffs'].values() for e in eps)


def summary_groups(N, e):
    return [(complex(*g['c']), g['cls']) for g in lad['cutoffs'][N]['points'][key(e)]['summary']['groups']]


def window(N, e):
    return sorted(z.imag for z, c in summary_groups(N, e) if c == 'imag' and 2.3 < z.imag < 2.7)


p24, p32, p16 = window('24', 32.0), window('32', 32.0), window('16', 32.0)
assert len(p24) == len(p32) == len(p16) == 2
gap = p32[1] - p32[0]
agree = max(abs(a - b) for a, b in zip(p24, p32))
assert all(abs(a - b) > gap for a, b in zip(p16, p24))
band = lad['readings'][key(32.0)]['band']


def departure(N, e):
    ref = [z for z, c in summary_groups('32', e) if abs(z) < band / 2 and z.imag >= 0]
    other = [z for z, c in summary_groups(N, e)]
    return max(min(abs(z - w) for w in other) for z in ref)


src_lin = open(folder('instrument', 'linear.py'), encoding='utf-8').read()     # condition (a)'s KAPPA / GRAY
m = re.search(r'^KAPPA, M0, GRAY, KAPPA_D, KAPPA_L, LEAK_CAP = ([0-9.]+), [0-9.]+, ([0-9.]+),', src_lin, re.M)
kg = float(m[1]) / float(m[2])
coef = {(N, e): lad['cutoffs'][N]['points'][key(e)]['coefficient'] for N in ('16', '24', '32') for e in eps}
factor = {k: kg / v for k, v in coef.items()}
over = [e for e in eps if coef[('16', e)] > 0.0568]
high = min(factor[(N, e)] for N in ('24', '32') for e in eps)


def num_list(xs):
    return ', '.join(xs[:-1]) + f' and {xs[-1]}' if len(xs) > 1 else xs[0]


def tau4(xs):
    return ', '.join(f'{float(x):.4f}' for x in xs[:-1]) + f' and {float(xs[-1]):.4f}'


fill = {
    'PR640': 'https://github.com/openwave-labs/openwave/pull/640#pullrequestreview-5575251218',
    'PR642': 'https://github.com/openwave-labs/openwave/pull/642',
    'C18955679': D512 + '18955679', 'C19071299': D512 + '19071299', 'C19076863': D512 + '19076863',
    'PROPN': short('e7652a4'), 'PROPN_URL': blob('e7652a4', f'{W}/soft-slot-branches.md', '#iii-the-small-amplitude-spectrum'),
    'ORBITS_URL': blob('e7652a4', f'{W}/soft-slot-branches.md', '#iv-the-orbits'),
    'CENSUS': short('HEAD'), 'CENSUS_URL': blob('HEAD', f'{W}/slot-dynamics-census.md', '#v-the-program'),
    'RECORD': short('87fc643'), 'RECORD_URL': blob('87fc643', f'{M816}/RECORD.md'),
    'BOUNDARY_URL': blob('HEAD', f'{M816}/BOUNDARY.md'), 'BOUNDARY': boundary[:8] + '…', 'BOUNDARY_1': boundary_1[:8] + '…',
    'M816_PIN': pin[:8] + '…', 'M816_TERMS': sha(terms)[:8] + '…',
    'OW_TERMS_URL': f'https://github.com/openwave-labs/openwave/blob/{OW_COMMIT}/openwave/xperiments/m8_mit/research/tasks/m8_16_task_details.md',
    'BOUNDARY_QUOTE': quote, 'Q_CEIL': f'{max(0.1 * abs(quartet), 1e-3):.4f}', 'Q_SPREAD': sci(spread, 1),
    'C2_MIN': f'{min(decades):.1f}', 'C2_MAX': f'{max(decades):.1f}', 'CASES_SHA': cases_sha[:8] + '…',
    'T4_MU': sci(mu), 'T4_C': f'{cg:+.3f}', 'T4_C16': f'{cg16:+.3f}', 'T4_CEIL': sci(ceil4), 'T4_TRIG': sci(trig, 1),
    'T4_X': sci(t4x, 1),
    'N_FLOOR': WORDS[len(small)], 'N_FLOOR16': WORDS[len(small16)], 'T2R5_C': sci(t2c, 1), 'T2R5_16': sci(t2c16, 1),
    'T2R5_TOL': f'{round(100 * 0.1 * 1e-3 / t2c16)}%',
    'T5I_TAU': tau4(t5i), 'T5J_TAU': tau4(t5j),
    'C3R_Q': f'{c3q.real:.9g} + {c3q.imag:.9g} i', 'C3R_M': f'{c3m:.9g}', 'C3R_P': f'{c3p:.9g}',
    'C3R_LAM': sci(c3_lam), 'C3R_MARG': f'{round((c3_lam / 4.52e-7 - 3) / 10) * 10}',
    'C3R_OFF': fmt3(c3_tot - c3_c0), 'C3R_C0': fmt3(c3_c0), 'C3R_TOT': fmt3(c3_tot),
    'C3R_RATIO': f'{math.floor(min(ratios))}',
    'T5J_LAM': sci(t5j_lam), 'T5J_MARG': f'{round((t5j_lam / 4.40e-7 - 3) / 100) * 100:,}',
    'PREVIEW': preview, 'TV_N': tv, 'TV_M': {4: 'four', 5: 'five', 6: 'six', 7: 'seven'}[tm], 'TG_N': tg,
    'LAD_POINTS': f'{accepted}', 'LAD_GAP': f'{gap:.3f}', 'LAD_AGREE': sci(agree, 1),
    'LAD_FACTOR': f'{factor[("16", 32.0)]:.1f}', 'LAD_DEP16': sci(departure('16', 32.0), 1),
    'LAD_DEP24': sci(departure('24', 32.0), 1),
    'LAD_OVER_EPS': num_list([f'{e:.3g}' for e in over]), 'LAD_OVER_F': num_list([f'{factor[("16", e)]:.1f}' for e in over]),
    'LAD_F_HIGH': f'{math.floor(high)}', 'LAD_HOURS': f'{lad["seconds"] / 3600:.2f}',
}
text = open(f'{HERE}/terms_template_v7.md', encoding='utf-8').read()
used = set(re.findall(r'«([A-Z0-9_]+)»', text))
assert used == set(fill) | {'WORDS'}, (used ^ (set(fill) | {'WORDS'}))
for k, v in fill.items():
    text = text.replace(f'«{k}»', v)
words = len(text.split())
text = text.replace('«WORDS»', f'{round(words / 100) * 100:,}')
bad = [m for m in ('—', ' – ', '«', '»', '(UA)', '(UB)') if m in text]
if 'blind' in text.lower():
    bad.append('a banned label')
table = None
for i, line in enumerate(text.splitlines(), 1):
    if line.startswith('|'):
        table = line.count('|') if table is None else table
        if line.count('|') != table:
            bad.append(f'a table row with {line.count("|")} pipes against its header\'s {table}, line {i}')
    else:
        table = None
    if line.count('`') % 2:
        bad.append(f'odd backticks on line {i}')
    if line.startswith('|') and not line.rstrip().endswith('|'):
        bad.append(f'a table row without its closing pipe, line {i}')
if bad:
    raise SystemExit('STOPPED: ' + '; '.join(bad))
out = OUT or f'{HERE}/m8_16_1_task_details.md'
open(out, 'x', encoding='utf-8').write(text)
print(f'wrote {out}: {words} words; the governing prefix and the boundary quote verified; OpenWave terms commit {OW_COMMIT[:7]}')
print(f'T4/R5: mu {mu:.4e}, c {cg:+.5f} (16: {cg16:+.5f}), ceiling {ceil4:.4e}, trigger {trig:.3e}, cross-check {t4x:.2e};'
      f' C3R lam {c3_lam:.4e}, ratio {min(ratios):.2f}; T5J lam {t5j_lam:.4e}; floor groups {len(small)}')
print(f'ladder: {accepted} accepted; pair {p16} / {p24} / {p32}, gap {gap:.4f}, agree {agree:.1e}; factor at 16/32'
      f' {factor[("16", 32.0)]:.2f}; over {over}; high {high:.1f}; departures {departure("16", 32.0):.2e}, {departure("24", 32.0):.2e}')
