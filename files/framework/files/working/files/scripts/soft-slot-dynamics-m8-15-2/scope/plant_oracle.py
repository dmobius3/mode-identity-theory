"""The expected outcomes REGISTER_5 registers for the coupled mock's plants, from a counts-level model of the scope memo v7's
rules 1 to 7 and 10 and decision 7 on the plants' explicit eigenvectors. It reads no record and runs no locator code.

  python3 plant_oracle.py          prints every plant's evaluated points, steps, classes and reasons

The model: the mock's structural span P = span(e0..e3) with M = I; e0 the exact zero; e1 a lift; two doubled blocks coupling
the genuine pair (e4, e5) with the lifts (e2, e3) by kappa; optionally an extra genuine eigenvalue on e7. The Hamiltonian
type change of each genuine crossing sits where L is singular, so the genuine index h jumps there; n(B|G_tol) balances, so
every clean point balances and the reading ends are the clean ends. Newton never fails, and the spectators are inert.

Three simplifications against the locator, none of which changes a registered outcome (Unit B): the branch flag reads the
bisection's points only, since every failing grid point lies outside its step's clean window; outside a branch step the
per-class checks run after the frozen identity check; and the frozen ok test on the analysed ends is skipped, since the
clean ends pass every check by construction."""
import math
import numpy as np
from scipy.optimize import linear_sum_assignment

TOL, OV, A, DL, WIDTH = 1e-9, 0.9, 0.05, 1e-5, 1e-3
N = 8                                        # e0..e7: e6 the S10 tilt partner, e7 the extra genuine eigenvalue


class Plant:
    def __init__(self, r, sigma=+1, kap=0.0, e0=None, e1=None, extra=None, tilt=None, lift_move=None, tilt_points=()):
        self.r, self.sigma, self.kap, self.tilt_points = r, sigma, kap, tuple(tilt_points)
        self.e0, self.e1 = e0, e1            # optional functions of eps for e0's and e1's eigenvalues
        self.extra = extra                   # (zero, slope): an extra genuine eigenvalue slope (eps - zero) on e7
        self.tilt = tilt                     # (eps, overlap): e1's eigenvector tilted toward e6 at that point
        self.lift_move = lift_move           # (eps_s, g0): the lifts e2, e3 move as A (eps - eps_s); the pair sits at g0

    def blocks(self, eps):
        """Each doubled block's matrix in (genuine, lift)."""
        if self.lift_move:
            es, g0 = self.lift_move
            return np.array([[g0, self.kap], [self.kap, A * (eps - es)]])
        return np.array([[self.sigma * A * (self.r - eps), self.kap], [self.kap, -DL]])

    def singular(self):
        """Where each block is singular (det = 0): its genuine index jumps there, by +1 per block in the direction it moves."""
        if self.lift_move:
            return None                      # the genuine pair does not cross: no type change
        return self.r + self.sigma * self.kap ** 2 / (A * DL)

    def point(self, eps):
        vals, vecs = np.zeros(N), np.eye(N)
        vals[0] = self.e0(eps) if self.e0 else 1e-14
        vals[1] = self.e1(eps) if self.e1 else -DL
        vals[6] = 0.05
        vals[7] = self.extra[1] * (eps - self.extra[0]) if self.extra else 0.5
        for gi, li in ((4, 2), (5, 3)):
            w, v = np.linalg.eigh(self.blocks(eps))
            for j, col in ((0, gi), (1, li)):
                vecs[:, col] = 0.0
                vecs[gi, col], vecs[li, col] = v[0, j], v[1, j]
                vals[col] = w[j]
        if self.tilt and abs(eps - self.tilt[0]) <= 1e-12:
            t = math.acos(self.tilt[1])
            b1, b6 = vecs[:, 1].copy(), vecs[:, 6].copy()
            vecs[:, 1], vecs[:, 6] = math.cos(t) * b1 + math.sin(t) * b6, -math.sin(t) * b1 + math.cos(t) * b6
        for te, tov in self.tilt_points:
            if abs(eps - te) <= 1e-12 * te:
                t = math.acos(tov)
                b0, b6 = vecs[:, 0].copy(), vecs[:, 6].copy()
                vecs[:, 0], vecs[:, 6] = math.cos(t) * b0 + math.sin(t) * b6, -math.sin(t) * b0 + math.cos(t) * b6
        ov = np.linalg.norm(vecs[:4, :], axis=0)
        st = ov >= OV
        ok = st.sum() == 4 and np.linalg.svd(vecs[:4, st], compute_uv=False).min() >= OV
        neg = vals < -TOL
        return dict(eps=eps, vals=vals, vecs=vecs, ov=ov, neg=neg, ok=bool(ok), nL=int(neg.sum()), nS=int((neg & st).sum()),
                    h=self.h(eps))

    def h(self, eps):
        h = 0
        e_nl = self.singular()
        if e_nl is not None:
            # sigma = +1: the pair falls through zero, so h goes 0 -> 2 at e_nl; sigma = -1 rises, 2 -> 0
            h += (2 if eps > e_nl else 0) if self.sigma > 0 else (2 if eps < e_nl else 0)
        if self.extra:
            z, s = self.extra
            h += (1 if eps > z else 0) if s < 0 else (1 if eps < z else 0)
        return h


def counts(p):
    return (p['nL'], p['nS'])


def bisect(pl, lo, hi, steps, failed=False, start=None):
    """Rules 1 to 6 of the scope memo v7, with M8.15.1's frozen split."""
    start = start or (lo['eps'], hi['eps'])
    lo_n, hi_n, lo_c, hi_c = lo, hi, lo, hi
    terminal = lo['nL'] == hi['nL']
    seen = []
    while hi_n['eps'] - lo_n['eps'] > WIDTH * lo_n['eps']:
        m = pl.point((lo_n['eps'] + hi_n['eps']) / 2)
        if not m['ok']:
            seen.append((m['eps'], 'failing', counts(m)))
            if terminal:
                steps.append(dict(start=start, status='Unresolved', reason='structural subspace', seen=seen,
                                  lo=lo_n['eps'], hi=hi_n['eps'], failed_at=m['eps'])); return
            failed = True
            if m['nL'] == lo_n['nL']: lo_n = m
            elif m['nL'] == hi_n['nL']: hi_n = m
            else:
                steps.append(dict(start=start, status='Unresolved', reason='passed midpoint matches neither end', seen=seen,
                                  lo=lo_n['eps'], hi=hi_n['eps'])); return
            continue
        if counts(m) == counts(lo_c):
            seen.append((m['eps'], 'clean, lower', counts(m))); lo_n = lo_c = m
        elif counts(m) == counts(hi_c):
            seen.append((m['eps'], 'clean, upper', counts(m))); hi_n = hi_c = m
        elif failed and m['nL'] in (lo_c['nL'], hi_c['nL']) and m['nS'] < (lo_c if m['nL'] == lo_c['nL'] else hi_c)['nS']:
            # the exchanged-lift point: n_S compared with that side's preserved clean end (UA)
            seen.append((m['eps'], 'exchanged-lift, passed', counts(m)))
            if m['nL'] == lo_n['nL']: lo_n = m
            else: hi_n = m
        elif failed:
            seen.append((m['eps'], 'clean, neither side', counts(m)))
            steps.append(dict(start=start, status='Unresolved', reason="neither side's counts after a failure", seen=seen,
                              lo=lo_n['eps'], hi=hi_n['eps'])); return
        else:
            seen.append((m['eps'], 'clean, neither end: split', counts(m)))
            bisect(pl, lo_n, m, steps, failed, start)
            bisect(pl, m, hi_n, steps, failed, start)
            return
    steps.append(analyse(pl, lo_n, hi_n, lo_c, hi_c, seen, start))


def principal(A_, B_):
    qa, _ = np.linalg.qr(A_); qb, _ = np.linalg.qr(B_)
    return np.linalg.svd(qa.T @ qb, compute_uv=False)


def analyse(pl, lo_n, hi_n, lo, hi, seen, start):
    """Rule 7 between the clean ends (the reading ends, since every clean point balances), rule 10 and decision 7."""
    out = dict(start=start, lo=lo_n['eps'], hi=hi_n['eps'], clean=(lo['eps'], hi['eps']), seen=seen)
    cell = (pl.grid[-1] - pl.grid[0]) / 8
    if hi['eps'] - lo['eps'] > cell * (1 + 1e-9):
        return dict(out, status='Unresolved', reason='clean window over one grid cell')
    branch = any(lo['eps'] < e < hi['eps'] and tag in ('failing', 'exchanged-lift, passed') for e, tag, _ in seen)
    C = (lo['vecs'].T @ hi['vecs']) ** 2
    ri, ci = linear_sum_assignment(-C)
    cross = [(i, j) for i, j in zip(ri, ci) if lo['neg'][i] != hi['neg'][j]]
    signed = [+1 if hi['neg'][j] else -1 for i, j in cross]
    if sum(signed) != hi['nL'] - lo['nL']:
        return dict(out, status='Unresolved', reason='spectral coverage', branch=branch)
    classes = ['structural' if lo['ov'][i] >= OV and hi['ov'][j] >= OV else
               'genuine' if lo['ov'][i] < OV and hi['ov'][j] < OV else 'mixed' for i, j in cross]
    out.update(branch=branch, classes=classes, dnL=hi['nL'] - lo['nL'], dnS=hi['nS'] - lo['nS'], dh=hi['h'] - lo['h'])
    if not branch:
        # outside a branch step the frozen order stands: the crossing set's identity first, on the full vectors
        full_all = principal(lo['vecs'][:, [i for i, _ in cross]], hi['vecs'][:, [j for _, j in cross]]).min()
        out['full_cosine_all'] = float(full_all)
        if full_all < OV:
            return dict(out, status='Unresolved', reason='crossing identity')
    if branch and 'mixed' in classes:
        return dict(out, status='Unresolved', reason='mixed overlap')
    gen = [(i, j) for (i, j), c in zip(cross, classes) if c == 'genuine']
    if gen:
        a_ = lo['vecs'][:, [i for i, _ in gen]]; b_ = hi['vecs'][:, [j for _, j in gen]]
        full = principal(a_, b_).min()
        pa, pb = a_.copy(), b_.copy(); pa[:4, :] = 0; pb[:4, :] = 0
        outside = principal(pa, pb).min()
        out.update(full_cosine=float(full), outside_cosine=float(outside))
        if branch and outside < OV:
            return dict(out, status='Unresolved', reason='crossing identity')
        if not branch and full < OV:
            return dict(out, status='Unresolved', reason='crossing identity')
    struct = [(i, j) for (i, j), c in zip(cross, classes) if c == 'structural']
    if struct and principal(lo['vecs'][:, [i for i, _ in struct]], hi['vecs'][:, [j for _, j in struct]]).min() < OV:
        return dict(out, status='Unresolved', reason='crossing identity')
    if 'mixed' in classes:
        # in a branch step the classes are read first, so a mixed class meets the backstop before any identity test
        return dict(out, status='Unresolved', reason='mixed overlap')
    s_st = sum(s for s, c in zip(signed, classes) if c == 'structural')
    s_ge = sum(s for s, c in zip(signed, classes) if c == 'genuine')
    if out['dnS'] != s_st or out['dh'] != s_ge:
        return dict(out, status='Unresolved', reason='index bookkeeping')
    if s_st and s_ge:
        return dict(out, status='Unresolved', reason='genuine and structural crossings in one step')
    roots = []
    for i, j in cross:
        a1, b1 = lo['vals'][i], hi['vals'][j]
        t = a1 / (a1 - b1) if a1 != b1 else 0.5
        roots.append(lo['eps'] + (hi['eps'] - lo['eps']) * min(max(t, 0.0), 1.0))
    out['root'] = float(np.mean(roots))
    return dict(out, status='genuine' if s_ge else 'structural')


def locate(pl, bracket=(0.8, 1.2)):
    a, b = bracket
    pl.grid = [a + (b - a) * k / 8 for k in range(9)]
    seq = [pl.point(g) for g in pl.grid]
    usable = [p for p in seq if p['ok']]
    steps = []
    for lo, hi in zip(usable[:-1], usable[1:]):
        if counts(lo) != counts(hi):
            bisect(pl, lo, hi, steps)
    return steps


SUMMARY = []


def show(label, pl):
    steps = locate(pl)
    SUMMARY.append((label, [(x['status'], x.get('reason'), x.get('branch'), x.get('classes')) for x in steps]))
    e_nl = pl.singular()
    print(f'== {label}: n(L) change {"none" if e_nl is None else f"{e_nl:.6f}"}; {len(steps)} step(s)')
    for s in steps:
        pts = '; '.join(f'{e:.6f} {tag} {c}' for e, tag, c in s['seen'])
        extra = ''
        if 'classes' in s:
            extra = (f", classes {s['classes']}, dn(L) {s['dnL']:+d}, dn_S {s['dnS']:+d}, dh {s['dh']:+d}"
                     + (f", cosines full {s['full_cosine']:.3f} outside P {s['outside_cosine']:.3f}" if 'full_cosine' in s else '')
                     + (', branch step' if s.get('branch') else ', not a branch step')
                     + (f", root {s['root']:.6f}" if 'root' in s else ''))
        clean = f", clean ends {s['clean'][0]:.6f} to {s['clean'][1]:.6f}" if 'clean' in s else ''
        print(f"   {s['status']}" + (f" ({s['reason']})" if 'reason' in s else '') + f": n(L) ends {s['lo']:.6f} to {s['hi']:.6f}"
              f"{clean}{extra}")
        print(f'      midpoints in order: {pts}')


R = {3: 1.0130, 2: 1.0181}
if __name__ == '__main__':
    for sg in (+1, -1):
        for q in (0.3, 1, 2, 2.5, 3, 4, 6):
            for lv in (3, 2):
                show(f'A1, slope sign {sg:+d}, kappa/delta {q:g}, level {lv}', Plant(R[lv], sg, q * DL))
    for lv in (3, 2):
        show(f'A27, kappa/delta 8, level {lv}', Plant(R[lv], +1, 8 * DL))
    for q in (0.3, 1, 2, 2.5, 3, 4, 6):
        show(f'A2/A28, lifts rising through zero at 1.0130 by {A} (eps - 1.0130), pair at +1e-5, kappa/delta {q:g}',
             Plant(R[3], kap=q * DL, lift_move=(1.0130, DL)))
    show('A29, S1 with the S10 tilt at 1.025 (0.85), e1 rising through zero at 1.004, an extra genuine falling at 1.006',
         Plant(R[3], +1, 0.0, e1=lambda e: 0.01 * (e - 1.004), extra=(1.006, -A), tilt=(1.025, 0.85)))
    show('A9, S1 with the S10 tilt at 1.025 (0.85), e0 falling through zero at 1.004, an extra genuine rising at 1.006',
         Plant(R[3], +1, 0.0, e0=lambda e: -0.01 * (e - 1.004), extra=(1.006, +A), tilt=(1.025, 0.85)))
    show('A3, S1 at level 3 with e1 rising through zero at 1.0127 and e0 tilted to 0.85 at 1.0140625 and 1.01328125',
         Plant(R[3], +1, 0.0, e1=lambda e: 0.01 * (e - 1.0127), tilt_points=[(1.0140625, 0.85), (1.01328125, 0.85)]))
    show('A3, S1 at level 2 with e1 rising through zero at 1.0127', Plant(R[2], +1, 0.0, e1=lambda e: 0.01 * (e - 1.0127)))
    show('A12, S1 at level 3 with e0 tilted to 0.85 at 1.0125 and 1.01328125', Plant(R[3], +1, 0.0, tilt_points=[(1.0125, 0.85), (1.01328125, 0.85)]))
    show('A12, S1 at level 2, untilted', Plant(R[2], +1, 0.0))
    for lv in (3, 2):
        show(f'A16, S1 at level {lv} with e0 tilted to 0.85 at the grid points 0.95 and 1.0 and at the midpoints 0.975 and 1.0125',
             Plant(R[lv], +1, 0.0, tilt_points=[(0.95, 0.85), (1.0, 0.85), (0.975, 0.85), (1.0125, 0.85)]))
    for lv, rr in ((3, 1.0120), (2, 1.0130)):
        show(f'A14, slope sign -1, kappa/delta 7.5, roots 1.0120 and 1.0130, level {lv}', Plant(rr, -1, 7.5 * DL))
    print('== summary, one line per plant and level: every step\'s status (reason), branch step or not, and its classes')
    for label, st in SUMMARY:
        parts = []
        for status, reason, branch, classes in st:
            parts.append(status + (f' ({reason})' if reason else '') + (', branch step' if branch else '')
                         + (f", classes {'/'.join(sorted(set(classes)))}" if classes else ''))
        print(f'   {label}: ' + '; '.join(parts))


# --- rule 11 on the continuity plants: an evaluation log, the m path, the spans and the comparisons ----------------------
M2, TAU = 3.4601e-4, 3.4601e-3       # the default path's curvature (the controls' largest statistic) and the tolerance (recon v8)
LADDER = (0.6, 0.8, 1.2, 1.4)


class Run(Plant):
    """A Plant whose every evaluation is logged with its m and reached eps. Options: lift_line (eps_s, slope) moves the lifts
    e2, e3 (S2's structural crossing) with no coupling; switch (lo, hi, J) puts targets in (lo, hi) on a second path, m + J;
    slack alternates the reached eps by 1e-6, relative, in evaluation order; reeval_J puts a re-evaluation of an
    already-evaluated target on a second path; region is the guard region whose ladder points seed the pool."""
    def __init__(self, r, sigma=+1, kap=0.0, lift_line=None, switch=None, slack=False, reeval_J=0.0, region=(0.6, 1.4), **kw):
        super().__init__(r, sigma, kap, **kw)
        self.lift_line, self.switch, self.slack, self.reeval_J, self.region = lift_line, switch, slack, reeval_J, region
        self.log = []

    def blocks(self, eps):
        if self.lift_line:
            es, sl = self.lift_line
            return np.array([[self.sigma * A * (self.r - eps), 0.0], [0.0, sl * (eps - es)]])
        return super().blocks(eps)

    def evaluate(self, eps):
        p = Plant.point(self, eps)
        again = any(abs(q['target'] - eps) <= 1e-9 * eps for q in self.log)
        reached = eps * (1 + (1e-6 if len(self.log) % 2 == 0 else -1e-6)) if self.slack else eps
        x = reached - 1.0
        m = 1.0 + 0.15 * x + 0.5 * M2 * x * x
        if self.switch and self.switch[0] < eps < self.switch[1]:
            m += self.switch[2]
        if again:
            m += self.reeval_J
        self.log.append(dict(target=eps, reached=reached, m=m, ok=p['ok']))
        return p


def locate_run(pl, bracket=(0.8, 1.2)):
    a, b = bracket
    pl.grid = [a + (b - a) * k / 8 for k in range(9)]
    seeded = {e: pl.evaluate(e) for e in LADDER if pl.region[0] * (1 - 1e-12) <= e <= pl.region[1] * (1 + 1e-12)}
    seq = [seeded[g] if g in seeded else pl.evaluate(g) for g in pl.grid]
    usable = [p for p in seq if p['ok']]
    steps = []
    orig = pl.point
    pl.point = pl.evaluate                        # the bisection's midpoints are logged too
    try:
        for lo, hi in zip(usable[:-1], usable[1:]):
            if counts(lo) != counts(hi):
                bisect(pl, lo, hi, steps)
    finally:
        pl.point = orig
    return steps


def stat11(a, b, c):
    h1, h2 = b['reached'] - a['reached'], c['reached'] - b['reached']
    if not (h1 > 1e-9 * c['reached'] and h2 > 1e-9 * c['reached']):
        return None, None
    miss = abs(c['m'] - b['m'] - (b['m'] - a['m']) * h2 / h1)
    return miss / (h2 * (h1 + h2) / 2), miss


def rule11(pl, s, mode='registered'):
    """mode: 'registered'; 'bare' (the bare miss against a tolerance that clears a grid cell); 'target' (the target eps as
    abscissa); 'evaluation' (each point's predictors are the two points evaluated just before it); 'subinterval' (the span
    restricted to the step's final sub-interval); 'latest' (a re-evaluated target keeps only its latest record);
    'skip' (a degenerate comparison is skipped)."""
    log = [dict(q) for q in pl.log]
    if mode == 'target':
        for q in log:
            q['reached'] = q['target']
    if mode == 'latest':
        keep = {}
        for q in log:
            keep[round(q['target'], 9)] = q
        log = list(keep.values())
    pool = sorted(log, key=lambda q: q['reached'])
    dups = [(p_['target'], q_['target'], abs(p_['m'] - q_['m'])) for p_, q_ in zip(pool, pool[1:])
            if abs(q_['target'] - p_['target']) <= 1e-9 * q_['target']]
    lo, hi = s['start']
    if 'clean' in s:
        lo, hi = min(lo, s['clean'][0]), max(hi, s['clean'][1])
    if mode == 'subinterval':
        lo, hi = s['lo'], s['hi']
    idx = [i for i, q in enumerate(pool) if lo * (1 - 1e-12) <= q['target'] <= hi * (1 + 1e-12)]
    comps = []
    if mode == 'evaluation':
        order = [q for q in log if lo * (1 - 1e-12) <= q['target'] <= hi * (1 + 1e-12)]
        for k in range(2, len(order)):
            comps.append((order[k]['target'],) + stat11(order[k - 2], order[k - 1], order[k]))
    else:
        for i in idx[1:]:
            comps.append((pool[i]['target'],) + (stat11(pool[i - 2], pool[i - 1], pool[i]) if i >= 2 else (None, None)))
        if 'clean' in s:
            il = next(i for i, q in enumerate(pool) if abs(q['target'] - s['clean'][0]) <= 1e-9 * q['target'])
            iu = next(i for i, q in enumerate(pool) if abs(q['target'] - s['clean'][1]) <= 1e-9 * q['target'])
            comps.append((pool[iu]['target'],) + (stat11(pool[il - 1], pool[il], pool[iu]) if il >= 1 else (None, None)))
    in_span = [d for d in dups if lo * (1 - 1e-12) <= d[0] <= hi * (1 + 1e-12)]
    if mode == 'bare':
        bad = [c for c in comps if c[2] is not None and c[2] > TAU * 0.05 ** 2]
    elif mode == 'skip':
        bad = [c for c in comps if c[1] is not None and c[1] > TAU]
    else:
        bad = [c for c in comps if c[1] is None or c[1] > TAU]
    if in_span and mode != 'latest':
        verdict = 'Unresolved (solution continuity, duplicate target)'
    else:
        verdict = 'Unresolved (solution continuity)' if bad else 'passes'
    worst = max((c for c in comps if c[1] is not None), key=lambda c: c[1], default=None)
    return verdict, worst, bad[:3], in_span


def show11(label, pl, modes=('registered',)):
    steps = locate_run(pl)
    print(f'== {label}: {len(steps)} step(s)')
    for s in steps:
        head = f"   {s['status']}" + (f" ({s['reason']})" if 'reason' in s else '') + f": start {s['start'][0]:.6f} to {s['start'][1]:.6f}"
        print(head + (f", clean ends {s['clean'][0]:.6f} to {s['clean'][1]:.6f}" if 'clean' in s else ''))
        for mode in modes:
            v, worst, bad, dups = rule11(pl, s, mode)
            w = f'worst {worst[1]:.2e} at {worst[0]:.6f}' if worst else 'no comparison'
            b = '; '.join(f"{c[0]:.6f} {'degenerate' if c[1] is None else f'{c[1]:.2e}'}" for c in bad)
            d = '; '.join(f'duplicate {x[0]:.6f}, records {"agree" if x[2] == 0 else "differ by " + format(x[2], ".1e")}' for x in dups)
            print(f'      rule 11 ({mode}): {v}; {w}' + (f'; over the tolerance: {b}' if b else '') + (f'; {d}' if d else ''))


if __name__ == '__main__':
    print(f'== rule 11 plants: tolerance {TAU:.4e}; the default path m = 1 + 0.15 (e - 1) + 0.5 {M2:.4e} (e - 1)^2, against the reached eps')
    show11('S1, level 3, the default path', Run(R[3]))
    show11('A20, S1 level 3, targets above 1.0150 on a second path, m + 1e-6', Run(R[3], switch=(1.0150, 9.0, 1e-6)), ('registered', 'bare'))
    show11('A21, S1 level 3 with e0 tilted to 0.85 at 1.0125, targets above 1.0050 on a second path, m + 1e-5',
           Run(R[3], tilt_points=[(1.0125, 0.85)], switch=(1.0050, 9.0, 1e-5)))
    show11('A22, A1 slope +1, kappa/delta 2.5, level 3, reached eps alternating by 1e-6', Run(R[3], +1, 2.5 * DL, slack=True), ('registered', 'target'))
    show11('A22, level 2', Run(R[2], +1, 2.5 * DL, slack=True), ('registered', 'target'))
    show11('A23, S3 with its structural crossing at 1.005, level 3', Run(R[3], lift_line=(1.005, 0.01)), ('registered', 'evaluation'))
    show11('A23, level 2', Run(R[2], lift_line=(1.005, 0.01)), ('registered', 'evaluation'))
    show11('A24, A23 level 3 with targets in (1.0025, 1.0058) on a second path, m + 1e-5',
           Run(R[3], lift_line=(1.005, 0.01), switch=(1.0025, 1.0058, 1e-5)), ('registered', 'subinterval'))
    show11('A24, level 2', Run(R[2], lift_line=(1.005, 0.01), switch=(1.0025, 1.0058, 1e-5)), ('registered', 'subinterval'))
    show11('A25, A10 at level 3 with the re-evaluation on a second path, m + 1e-5',
           Run(R[3], tilt_points=[(1.0, 0.85)], reeval_J=1e-5), ('registered', 'latest'))
    show11('A25, level 2', Run(R[2], tilt_points=[(1.0, 0.85)], reeval_J=1e-5), ('registered', 'latest'))
    show11('A26, guard region 0.8 to 1.4, root 0.82, level 3', Run(0.82, region=(0.8, 1.4)), ('registered', 'skip'))
    show11('A26, level 2, root 0.8241', Run(0.8241, region=(0.8, 1.4)), ('registered', 'skip'))
    show11('A10, S1 level 3 with e0 tilted to 0.85 at the grid point 1.0', Run(R[3], tilt_points=[(1.0, 0.85)]), ('registered', 'latest'))
    show11('A10, level 2', Run(R[2], tilt_points=[(1.0, 0.85)]), ('registered', 'latest'))
