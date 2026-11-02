"""A preview on saved readings, outside any run: the rule as built must reproduce every stored verdict; candidate A
compares a set's members, at every cutoff, at the top cutoff's linking distance; candidate B lifts n(D)'s gray zone."""
import copy, glob, json, os, sys, types
import numpy as np
ROOT, M817, M1 = sys.argv[1:4]
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import convergence as cv, linear as ln
import checks as ck

src = open(os.path.join(ROOT, 'instrument', 'convergence.py'), encoding='utf-8').read()
a = "        pts = [[_c(g) for _, g in lev for _ in range(g['size'])] for lev in members]\n"
assert src.count(a) == 1
src2 = src.replace(a, a + "        if kind == 'set' and 'same_resolution' in arms:\n            pts = [_blur(p, hi) for p in pts]\n")
b = "ARMS = ('factor_one', "
assert src2.count(b) == 1
src2 = src2.replace(b, "ARMS = ('same_resolution', 'factor_one', ")
c = "def _chain(levels, i):"
assert src2.count(c) == 1
src2 = src2.replace(c, '''def _blur(p, hi):
    """Each member of a set at the mean of the members linked to it at the top cutoff's linking distance."""
    from instrument import linear as ln_
    vals = np.array(p, dtype=complex)
    tol = np.maximum(hi['margin'], ln_.KAPPA_D * np.sqrt(U * hi['normA'] * np.abs(vals)))
    out = vals.copy()
    for g in ln_.group(vals, tol):
        out[g] = vals[g].mean()
    return list(out)


''' + c)
cv2 = types.ModuleType('convergence_fix')
cv2.__package__ = 'instrument'
exec(compile(src2, 'convergence_fix.py', 'exec'), cv2.__dict__)
NDG = 'n(D): an eigenvalue of D lies in its gray zone'


def verdict(sums, eig, lam, marg, n_lo, mod, arms=()):
    band = cv.band_edge(eig, n_lo, lam)
    if not band / 2 > ln.GRAY * marg:
        return dict(verdict='Unresolved', reasons=['the band edge lies within the gray zone (UA)'])
    r = mod.separation(sums, band=band, arms=arms)
    return dict(verdict=r['verdict'], reasons=list(r['reasons']))


def lifted(sums):
    s2 = copy.deepcopy(sums)
    for s in s2:
        s['unresolved'] = [x for x in s['unresolved'] if x != NDG]
    return s2


def reads(path):
    d = json.load(open(path, encoding='utf-8'))
    cuts = sorted(d['cutoffs'], key=int)
    name = os.path.basename(path)[:-5]
    for e, rd in d['readings'].items():
        pts = [d['cutoffs'][N]['points'].get(e) for N in cuts]
        if not rd or not all(q and 'summary' in q for q in pts):
            continue
        yield name, e, cuts, [q['summary'] for q in pts], pts[-1]['eig'], pts[-1]['lam'], pts[-1]['record']['margin'], rd


SETS = [('M8.18 controls', sorted(glob.glob(os.path.join(ROOT, 'run/out/*.json')))),
        ('M8.16.1 controls', sorted(glob.glob(os.path.join(M1, '*.json')))),
        ('M8.17 rows', sorted(glob.glob(os.path.join(M817, 'T*_R*.json'))))]
tot, mis, nd_hits = 0, 0, 0
chg = []
for label, files in SETS:
    n, conv = 0, 0
    for f in files:
        if not any(k in json.load(open(f, encoding='utf-8')) for k in ('readings',)):
            continue
        for name, e, cuts, sums, eig, lam, marg, rd in reads(f):
            n_lo = 16
            built = verdict(sums, eig, lam, marg, n_lo, cv)
            ok = built['verdict'] == rd['verdict'] and built['reasons'] == rd['reasons']
            tot += 1
            mis += not ok
            if not ok:
                print('  AS-BUILT DIFFERS', label, name, e, built['verdict'], rd['verdict'])
            n += 1
            conv += rd['verdict'] == 'converged'
            nd_hits += sum(NDG in s['unresolved'] for s in sums)
            A = verdict(sums, eig, lam, marg, n_lo, cv2, ('same_resolution',))
            AB = verdict(lifted(sums), eig, lam, marg, n_lo, cv2, ('same_resolution',))
            if A['verdict'] != rd['verdict'] or AB['verdict'] != rd['verdict'] or A['reasons'] != rd['reasons']:
                chg.append((label, name, e, cuts, rd['verdict'], A['verdict'], AB['verdict'], len(rd['reasons']), len(A['reasons']), len(AB['reasons'])))
    print(f'{label}: {n} readings, {conv} stored converged')
print('total', tot, 'as-built differences', mis, "records holding n(D)'s gray-zone line", nd_hits)
print('changed under the candidates:')
for x in chg:
    print('  ', x)

# does candidate A still catch real motion?
d = json.load(open(os.path.join(ROOT, 'run/out/P5.json'), encoding='utf-8'))
pts = [d['cutoffs'][N]['points']['0.25'] for N in ('24', '32', '40')]
sums = [q['summary'] for q in pts]
base = verdict(sums, pts[-1]['eig'], pts[-1]['lam'], pts[-1]['record']['margin'], 16, cv2, ('same_resolution',))
print('P5 at 0.25 under A:', base)
for shift in (3e-6, 1e-6):
    s2 = copy.deepcopy(sums)
    g = [x for x in s2[-1]['groups'] if x['size'] == 2 and abs(complex(*x['c']).imag - 4.02029) < 1e-5][0]
    g['c'][1] += shift
    r = verdict(s2, pts[-1]['eig'], pts[-1]['lam'], pts[-1]['record']['margin'], 16, cv2, ('same_resolution',))
    print(f'  the merged group moved by {shift:g} at N = 40:', r['verdict'], r['reasons'][:1])
s2 = copy.deepcopy(sums)
for lvl, sh in ((0, 2 * 3e-6), (1, 3e-6)):      # members moving together, slower than the top step: contracting, must pass
    pass
print('pair means:', [f"{np.mean([complex(*x['c']).imag for x in s['groups'] if abs(complex(*x['c']).imag - 4.02029) < 1.5e-5 for _ in range(x['size'])]):.15f}" for s in sums])
print('P5, imaginary groups under 4.03 at N = 32:')
for e in ('0.25', '0.5', '1'):
    g = sorted(complex(*x['c']).imag for x in d['cutoffs']['32']['points'][e]['summary']['groups'] if x['cls'] == 'imag' and 3.9 < complex(*x['c']).imag < 4.2)
    gaps = np.diff(g)
    print(' ', e, 'n', len(g), 'smallest gaps', np.array2string(np.sort(gaps)[:4], precision=3))
