#!/usr/bin/env python3
"""Step 2 of the pre-freeze build: R5's coherent branch, a development control (BOUNDARY.md's amendment 3 and its note;
EXPECTED_R5.md; the units' GO, 2026-10-17). Case: C2a/R5.

Usage: r5_control.py

At N = 16, 24 and 32, each from the germ at eps = 0.25 and continued to 0.5, 1 and 2, as D7's sample and the
registration's own points (registration/m8_16_task_details.md, THE RUN). The solve and the record are D7's
(instrument/branches.py; instrument/linear.py at section 7's calibration and L's cut), on the guarded instrument
(entry 199). convergence.summarize keeps what the separation rule needs, and each cutoff's summary and level energies
are saved (UB). Then convergence.separation reads each eps from the three cutoffs, with the band edge from N = 32's
levels above N = 16.

The expectations are EXPECTED_R5.md's row, read only after the file's SHA-256 matches the one DEVLOG.md logged before
this run (UB): Q = 2289/2288; (k, r_u) = (3, 1); V0 dim 4, ranks [1, 0]; Elliptic, (n(L), n(D), K) = (0, 0, 0); five
slow pairs at eps kappa s tau, s = 9/16, kappa = 1/(8 sqrt(48) Q), tau = 28/143, 56/429, 140/99, 112/39, 896/1287, all
Krein positive.

Claims, derived before the run:
  1. The seed, at each N: Q(u) = 2289/2288 to 1e-12 relative; criticality at most 1e-12; (k, r_u) = (3, 1).
  2. Each point: the secant reaches the target within 1e-6, with every Newton solve accepted (the enforced bound); the
     record matches the row: V0 of dimension 4 with ranks [1, 0], 3 chains, and the leak of the actual tangents
     (T_a c, i c) within its bound; Elliptic, with (n(L), n(D), K) = (0, 0, 0); the balance holds; nothing unresolved.
  3. Theorem R's leading order: the slow nonzero eigenvalues (the record's own typed eigenvalues below 1) are five
     imaginary pairs, each group definite and Krein positive. Matched in order to eps kappa s tau, their largest
     relative deviation is at most 5% at eps = 0.25, the registration's bar, and smaller there than at eps = 2, at each
     N. (D7's R4 coherent branch: 1.45% at eps = 0.5 and 5.6% at 2; R5's corrections are not assumed to match R4's.)
  4. The convergence rule reads every eps converged, Elliptic, from N = 16, 24 and 32.
  5. The calibration's conditions hold in R5, as they stand (BOUNDARY.md's note: no constant is refitted on R5 unless
     one fails; a failure is preserved and returned before any adjustment, UA):
     (a) the zero cluster at least ten times below its gray zone's lower edge: its coefficient, the cluster's largest
         |lambda| over sqrt(u ||A|| max(m, m0)), at most (kappa/G)/10 = 1/15 at every point (the controls' largest,
         0.0568, in R2, R3 and R4);
     (b) L's kernel at least ten times below L's cut: its largest lift at most 100 u ||L|| (the controls': at most
         6.2 u);
     (c) L's smallest genuine eigenvalue at least ten times above L's gray zone: at least 10 G_L 1000 u ||L|| =
         1e5 u ||L|| (the controls' smallest, 1.4e-5 ||L||).
Reported, unscored: every deviation; each eps's convergence reading (the smallest ratio, its U and d); the cluster
coefficient, the lift and the smallest genuine eigenvalue at every point; the leak against its bound; and the seconds
per Newton evaluation and per point at each N, which replace the registration's R5 cost scaling.
"""
import hashlib
import json
import os
import re
import sys
import time
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, linear as ln, branches as br, convergence as cv, devtools  # noqa: E402

NAME, CASE, SLOT, LEVEL, LAM0 = 'C2a/R5', 'C2a/R5', 'R5', 6, 48.0
NS, EPS = [16, 24, 32], [0.25, 0.5, 1.0, 2.0]
U = np.finfo(float).eps
DOC = dict(Q=Fr(2289, 2288), k=3, r=1, dim=4, ranks=[1, 0], type='Elliptic', idx=(0, 0, 0), s=Fr(9, 16),
           tau=[Fr(28, 143), Fr(56, 429), Fr(140, 99), Fr(112, 39), Fr(896, 1287)])
COEF_MAX, LIFT_MAX, GENUINE_MIN = (ln.KAPPA / ln.GRAY) / 10, 100.0, 10 * ln.G_L * 1000.0
out, rec_json = [], {}


def say(s=''):
    print(s, flush=True)
    out.append(s)


def expected_r5():
    """EXPECTED_R5.md's row, after its SHA-256 matches the one DEVLOG.md logged for it before any R5 run: the first
    entry carrying a line on `EXPECTED_R5.md` with a SHA-256."""
    path = os.path.join(ROOT, 'EXPECTED_R5.md')
    raw = open(path, 'rb').read()
    sha = hashlib.sha256(raw).hexdigest()
    log = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    logged = re.findall(r'^- `EXPECTED_R5\.md`.*SHA-256 `([0-9a-f]{64})`', log, flags=re.M)
    assert logged, 'EXPECTED_R5.md was never logged'
    assert logged[0] == sha, 'EXPECTED_R5.md differs from the version logged before the R5 control ran'
    rows = [ln_ for ln_ in raw.decode('utf-8').splitlines() if ln_.startswith('| C2a/R5 (amendment 3) |')]
    assert len(rows) == 1
    c = [x.strip() for x in rows[0].strip().strip('|').split('|')]
    m = re.fullmatch(r'dim (\d+), ranks \[([0-9, ]+)\]', c[8])
    row = dict(Q=Fr(c[3]), k=int(c[5].split(', ')[0]), r=int(c[5].split(', ')[1]), dim=int(m.group(1)),
               ranks=[int(x) for x in m.group(2).split(',')], type=c[7].split(';')[0],
               idx=tuple(int(x) for x in re.findall(r'-?\d+', c[7].split(';')[1])),
               tau=[Fr(x) for x in re.findall(r'\d+/\d+', c[6].split('τ = ')[1].split(', each')[0])],
               s=Fr(re.search(r's = (\d+/\d+)', c[6]).group(1)))
    assert row == DOC, f'EXPECTED_R5.md row {row} differs from the docstring\'s {DOC}'
    return row, sha


def record_summary(r):
    return dict(type=r['type'], nL=r['nL'], nD=r['nD'], K=r['K'], kr=r['kr'], kc=r['kc'], ki=r['ki'], sdim=r['sdim'],
                ranks=r['jordan_ranks'], blocks=r['blocks'], leak=r['symmetry_leak'], v0_matches=r['v0_matches'],
                margin=r['margin'], cluster_max=r['cluster_max'], outside_min=r['outside_min'], balance=r['balance'],
                unresolved=r['unresolved'], normA=r['normA'])


def slow_spectrum(r):
    """The slow eigenvalues as the record classifies them (UA): typed, outside the gray zone, below 1."""
    lam, lab = r['lam'], r['labels']
    typed = np.isin(lab, ('real', 'imag', 'complex')) & (np.abs(lam) < 1.0)
    vals = np.sort(lam.imag[typed & (lab == 'imag') & (lam.imag > 0)])
    groups = [g for g in r['imag_groups'] if abs(g[0]) < 1.0]
    return vals, groups, int(typed.sum())


def run_N(N, E, expected):
    t0 = time.perf_counter()
    B = basis.Basis(SLOT, N)
    Fn = fn.Functional(B)
    u = br.seed_state(NAME, B)
    chk = br.orbit_checks(Fn, u)
    Qx = float(E['Q'])
    ok1 = abs(chk['Q'] - Qx) / Qx < 1e-12 and chk['crit'] <= 1e-12 and (chk['k'], chk['r']) == (E['k'], E['r'])
    say(f"N = {N}, m = {B.m}: 1. the seed {'PASS' if ok1 else 'FAIL'}  Q(u) {chk['Q']:.15f} against {Qx:.15f},"
        f" criticality {chk['crit']:.1e}, (k, r_u) = ({chk['k']}, {chk['r']}); setup {time.perf_counter() - t0:.1f} s,"
        f" cached {Fn.cached}")
    fails = int(not ok1)
    kappa = 1 / (8 * np.sqrt(LAM0) * Qx)
    pts = {}
    c_prev, lam_prev, slope, acc = np.sqrt(EPS[0] / chk['Q']) * u, LAM0 + EPS[0], 1 / chk['Q'], False
    for eps in EPS:
        t1 = time.perf_counter()
        res = br.continue_to(Fn, LAM0, eps, c_prev, lam_prev, slope, prev_accepted=acc)
        t_solve = time.perf_counter() - t1
        n_eval = sum(s['evaluations'] for s in res['steps'])
        if not res['ok']:
            fails += 1
            say(f"   eps {eps}: FAIL  {res['reason']}; the ladder at N = {N} ends here")
            rec_json[f'N{N}_eps{eps}'] = dict(ok=False, reason=res['reason'], steps=res['steps'])
            break
        c, lam = res['c'], res['lam']
        m_amp = float(np.vdot(c, c).real)
        t2 = time.perf_counter()
        L = Fn.hess_dense(c, lam)
        t_hess = time.perf_counter() - t2
        A, Bm, W = ln.first_order(L, np.sqrt(lam))
        normA = np.linalg.norm(A, 2)
        margin = ln.margin(normA, m_amp)
        sym = [np.concatenate([t, np.zeros(2 * B.m)]) for t in br.tangent_vectors(Fn, c)]
        t3 = time.perf_counter()
        r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
        t_rec = time.perf_counter() - t3
        s = cv.summarize(r, A, W)
        mu = np.linalg.eigvalsh(L)
        nL = float(np.abs(mu).max())
        order = np.argsort(np.abs(mu))
        lift = float(np.abs(mu[order[:E['k']]]).max() / nL)
        genuine = float(np.abs(mu[order[E['k']]]) / nL)
        coef = r['cluster_max'] / np.sqrt(U * normA * max(m_amp, ln.M0))
        accepted = abs(res['eps'] - eps) <= 1e-6 and all(st['accepted'] for st in res['steps'])
        ok2 = (accepted and r['v0_matches'] and r['blocks'] == E['k'] and r['type'] == E['type']
               and (r['nL'], r['nD'], r['K']) == E['idx'] and r['balance'] and not r['unresolved'])
        vals, groups, ntyped = slow_spectrum(r)
        pred = np.sort([eps * kappa * float(E['s']) * float(t) for t in E['tau']])
        count_ok = len(vals) == len(pred) and ntyped == 2 * len(pred)
        krein_ok = all(g[4] == 'definite' and g[2] == 0 for g in groups) and len(groups) == len(set(np.round(vals, 9)))
        dev = (np.abs(vals - pred) / pred).tolist() if count_ok else []
        fails += not (ok2 and count_ok and krein_ok)
        secs = time.perf_counter() - t1
        pts[eps] = dict(sum=s, lam=lam, eig=B.eig, dev=max(dev) if dev else np.inf, coef=coef, lift=lift,
                        genuine=genuine, ok=ok2 and count_ok and krein_ok)
        rec_json[f'N{N}_eps{eps}'] = dict(ok=True, eps=res['eps'], lam=lam, m=res['m'], steps=res['steps'],
                                          evaluations=n_eval, seconds_solve=t_solve, seconds_hessian=t_hess,
                                          seconds_record=t_rec, seconds=secs, record=record_summary(r), summary=s,
                                          eig=sorted(set(B.eig)), slow=vals.tolist(), predicted=pred.tolist(),
                                          deviations=dev, cluster_coefficient=coef, lift_over_normL=lift,
                                          genuine_over_normL=genuine, normL=nL,
                                          slow_groups=[(complex(g[0]).imag, g[1], g[2], g[4]) for g in groups])
        say(f"   eps {eps:6.3f}: 2. {'PASS' if ok2 else 'FAIL'}, slow {'PASS' if count_ok and krein_ok else 'FAIL'}"
            f"  reached {res['eps']:.9f}, {len(res['steps'])} solves, {n_eval} evaluations, floor {res['info']['floor_rel']:.1e};"
            f" V0 dim {r['sdim']}, ranks {r['jordan_ranks']}, {r['blocks']} chains, leak {r['symmetry_leak']:.1e};"
            f" ({r['nL']}, {r['nD']}, {r['K']}); {r['type']}, unresolved {r['unresolved']}; {len(vals)} slow of {len(pred)},"
            f" largest deviation {pts[eps]['dev']:.2e}; coefficient {coef:.4f}, lift {lift / U:.1f} u, genuine"
            f" {genuine:.1e}; {t_solve / max(n_eval, 1):.1f} s per evaluation, Hessian {t_hess:.1f} s, record"
            f" {t_rec:.1f} s, point {secs:.1f} s")
        c_prev, lam_prev, slope, acc = c, lam, res['slope'], True
    return pts, fails


def main():
    devtools.require(CASE)
    E, sha = expected_r5()
    expected = dict(dim=E['dim'], ranks=E['ranks'])
    say(f"Step 2, R5's coherent branch ({NAME}, level {LEVEL}): N = {NS}, eps = {EPS}; EXPECTED_R5.md SHA-256 {sha},"
        f" as logged before the run; factor {cv.FACTOR:g}")
    t0 = time.perf_counter()
    runs, failed = {}, 0
    for N in NS:
        runs[N], f = run_N(N, E, expected)
        failed += f
    common = [e for e in EPS if all(e in runs[N] for N in NS)]
    # claim 3's trend and bar, at each N
    ok3 = True
    for N in NS:
        if 0.25 in runs[N] and 2.0 in runs[N]:
            d25, d2 = runs[N][0.25]['dev'], runs[N][2.0]['dev']
            ok = d25 <= 0.05 and d25 < d2
            ok3 &= ok
            say(f"3. N = {N}: the largest deviation at eps 0.25, {d25:.2e} (bar 5%), against eps 2, {d2:.2e}:"
                f" {'PASS' if ok else 'FAIL'}")
        else:
            ok3 = False
    # claim 4, the separation rule from three cutoffs
    ok4 = len(common) == len(EPS)
    for eps in common:
        sums = [runs[N][eps]['sum'] for N in NS]
        band = cv.band_edge(runs[NS[-1]][eps]['eig'], NS[0], runs[NS[-1]][eps]['lam'])
        res = cv.separation(sums, band=band)
        good = res['verdict'] == 'converged' and res['type'] == DOC['type']
        ok4 &= good
        tested = [r_ for r_ in res['rows'] if 'U' in r_]
        worst = min(tested, key=lambda r_: r_['ratio']) if tested else None
        line = f"4. eps {eps:6.3f}: {res['verdict']}" + (f" {res['type']}" if res['type'] else '') + f"; band edge {band:.3g}"
        if worst:
            line += (f"; the smallest ratio {worst['ratio']:.3g} at {cv.row_centre(worst):.6g} ({worst['event']}):"
                     f" U {worst['U']:.2e}, d {worst['d']:.2e}")
        if res['reasons']:
            line += f"; {res['reasons'][:2]}"
        say(line)
        rec_json[f'rule_eps{eps}'] = dict(verdict=res['verdict'], type=res['type'], band=band, reasons=res['reasons'],
                                          rows=res['rows'])
    # claim 5, the calibration's conditions as they stand
    allpts = [p for N in NS for p in runs[N].values()]
    cmax = max(p['coef'] for p in allpts) if allpts else np.inf
    lmax = max(p['lift'] for p in allpts) / U if allpts else np.inf
    gmin = min(p['genuine'] for p in allpts) / U if allpts else 0.0
    ok5a, ok5b, ok5c = cmax <= COEF_MAX, lmax <= LIFT_MAX, gmin >= GENUINE_MIN
    say(f"5. the calibration's conditions: (a) the cluster coefficient, largest {cmax:.4f} against {COEF_MAX:.4f}:"
        f" {'PASS' if ok5a else 'FAIL'}; (b) L's kernel lift, largest {lmax:.1f} u against {LIFT_MAX:.0f} u:"
        f" {'PASS' if ok5b else 'FAIL'}; (c) L's smallest genuine eigenvalue, {gmin:.2e} u against {GENUINE_MIN:.0e} u"
        f" ({gmin * U:.1e} ||L||): {'PASS' if ok5c else 'FAIL'}")
    claims_failed = int(failed > 0) + (not ok3) + (not ok4) + (not ok5a) + (not ok5b) + (not ok5c)
    say(f"1 and 2: {'PASS' if failed == 0 else 'FAIL'} ({failed} failures among the seeds and points)")
    say(f"{claims_failed} failed; {time.perf_counter() - t0:.0f} s")
    for N in NS:
        secs = [rec_json[f'N{N}_eps{e}']['seconds'] for e in EPS if f'N{N}_eps{e}' in rec_json and rec_json[f'N{N}_eps{e}']['ok']]
        if secs:
            say(f"   cost at N = {N}: {sum(secs) / len(secs):.0f} s per point on average, {sum(secs):.0f} s in all")
    path, jpath = os.path.join(HERE, 'r5_control.out'), os.path.join(HERE, 'r5_control.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(rec_json, f, indent=1, default=lambda o: float(o) if np.isscalar(o) else str(o))
    devtools.log_run(os.path.abspath(__file__), CASE,
                     [f"Step 2, R5's coherent branch: {'PASS' if not claims_failed else 'FAIL'} ({claims_failed} failed);"
                      f" N = {NS}, eps = {EPS}.",
                      f'EXPECTED_R5.md SHA-256 {sha}, as logged before the run. Each outcome derived before the run (the'
                      ' script\'s docstring); no constant refitted.'], outputs=(path, jpath))
    if claims_failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
