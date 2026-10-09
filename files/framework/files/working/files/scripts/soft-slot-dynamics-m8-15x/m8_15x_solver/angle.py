"""The angle solve on the lifted circle (M8.15.x memo v4, § 1b and decision 1), under the frozen rule registered in
m8_15x/REGISTER_1.md (amendment of 2026-10-08T22:09:19Z).

The lifted circle of a slice case is the rotation of its representative about the pinned axis, the axis of its first
generator; for an n-fold axis its period is 2 pi / n. At angle theta the seed is the oriented germ interpolant of
D(theta) u, the slice is the rotation generator about the axis applied to that seed (as LevelCase builds it at
theta = 0), and Newton runs at fixed norm m from that seed with that slice. The slice force nu(theta) vanishes at the
discrete standing waves on the circle, and mu with it. The energy at fixed m, H = x^T K x / 2 + g V(x), picks the point
that counts: the minimum with the lowest H.

The frozen rule: N_GRID angles per period from theta_start; Brent's method on nu in every interval where nu changes
sign, to |nu| <= NU_TOL (a root that does not get there is unresolved, never used); a root is a minimum if its H lies
below H at both ends of its interval; minima carried onto each other by a mesh symmetry (normalized M-overlap at least
1 - SYM_TOL over the 120 elements of the right action) count as one; an inequivalent minimum within NEAR_FRAC of the
grid's energy range of the lowest is recorded beside the selection."""
import numpy as np
from scipy.optimize import brentq
from irreps import sym, su2
from geometry import qconj
from standing import germ_seed
from nonlinear import to_real, to_complex
from symmetry import rot3, to_quat_vec
from pinned import solve_pinned
from continuation import Branch

N_GRID = 10
NU_TOL = 1e-12
SYM_TOL = 1e-8
NEAR_FRAC = 0.1


class Circle:
    """The lifted circle of a slice case at one level (lc: a LevelCase)."""
    def __init__(self, lc):
        case = lc.case
        axes = [np.asarray(a) for a, _ in case.gens_cs]
        assert all(abs(abs(a @ axes[0]) - 1) < 1e-12 for a in axes), 'the angle solve needs a pin about one axis'
        self.lc, self.case, self.st = lc, case, lc.st
        self.ax, self.order = case.gens_cs[0]
        self.period = 2 * np.pi / self.order
        self.t = rot3(qconj(case.g0), to_quat_vec(self.ax))       # the axis in the mesh frame, as LevelCase reads it
        self.n_solves = 0
        self.offset = 0.0           # physical angle = coordinate + offset (controls only: the moving-coordinate arm)
        self.last_roots = []

    def rep(self, theta):
        """D(theta) u in Condon-Shortley components."""
        q = np.concatenate([[np.cos(theta / 2)], np.sin(theta / 2) * to_quat_vec(self.ax)])
        return sym(su2(q), self.case.j2) @ self.case.u

    def seed(self, theta):
        c = self.case
        w = sym(su2(qconj(c.g0)), c.j2) @ self.rep(theta)
        return germ_seed(c.mesh, c.R, c.j2, w, c.mesh.G)

    def slice(self, P):
        Xs = [self.lc.rot.apply(c, P) for c in 'xyz']
        t = self.t
        # quaternion coords (i, j, k) <-> Condon-Shortley (z, y, x), as LevelCase
        return to_real(t[2] * Xs[0] + t[1] * Xs[1] + t[0] * Xs[2])

    def scaled_seed(self, phys, m):
        g = self.case.P @ to_real(self.seed(phys))
        return g * np.sqrt(m / (g @ (self.st.Mr @ g)))

    def solve(self, theta, m, sigma0, start=None):
        """Newton at coordinate theta (physical angle theta + offset) and norm m. Without start it begins at the seed
        there (§ 1b); with start = (x, phys, m) of an accepted point it begins at that solution, rotated to the trial
        angle by the seed's change, with the gauges and the slice still referred to the seed there (the carry)."""
        st, c = self.st, self.case
        phys = theta + self.offset
        P = self.seed(phys)
        x = c.P @ to_real(P)
        x0 = x * np.sqrt(m / (x @ (st.Mr @ x)))
        self.n_solves += 1
        try:
            if start is None:
                Phi, sigma, info = solve_pinned(st, c, m, sigma0, slices=[self.slice(P)], x0=x0)
            else:
                xs, phys_s, m_s = start
                guess = xs * np.sqrt(m / m_s) + (x0 - self.scaled_seed(phys_s, m))
                Phi, sigma, info = solve_pinned(st, c, m, sigma0, slices=[self.slice(P)], x0=guess, xref=x0)
        except (RuntimeError, np.linalg.LinAlgError, ValueError) as e:
            return dict(theta=float(theta), failed=f'{type(e).__name__}: {e}')
        x = to_real(Phi)
        H = 0.5 * float(x @ (st.Kr @ x)) + st.g * st.q.energy(Phi)
        return dict(theta=float(theta), nu=float(info['nu'][0]), mu=float(info['mu'][0]), sigma=float(sigma), H=float(H),
                    it=int(info['it']), full=float(info['full']), res=float(info['res']), Phi=Phi)

    def classes(self, mins):
        return overlap_classes(self, mins)

    def overlap(self, Phi, x_src):
        """|<Phi, Psi>_M| / (|Phi|_M |Psi|_M) for Psi the source point's solution (a diagnostic of the fallback)."""
        M, Q = self.st.M, to_complex(x_src)
        return float(abs(np.vdot(Phi, M @ Q)) / np.sqrt(np.real(np.vdot(Phi, M @ Phi)) * np.real(np.vdot(Q, M @ Q))))


def overlap_classes(circle, mins):
    """Group minima into classes carried onto each other by a mesh symmetry; returns class labels and the best overlap
    found for every pair."""
    c, M = circle.case, circle.st.M
    n = len(mins)
    lab = list(range(n))
    best = {}
    Rs = [c.RA.matrix(h) for h in range(len(c.mesh.G))]
    nrm = [np.sqrt(np.real(np.vdot(r['Phi'], M @ r['Phi']))) for r in mins]
    for i in range(n):
        for j in range(i + 1, n):
            MPj = M @ mins[j]['Phi']
            o = max(abs(np.vdot(R @ mins[i]['Phi'], MPj)) for R in Rs) / (nrm[i] * nrm[j])
            best[(i, j)] = float(o)
            if o >= 1 - SYM_TOL:
                a, b = lab[i], lab[j]
                lab = [a if l == b else l for l in lab]
    return lab, best


H_TOL = 1e-13               # the H cross-check is decisive where both ends differ from the root's H by more than this


def kind_of(theta_r, H_r, samples, H_ends, P, convention=1.0):
    """A root's kind (REGISTER_1.md, amendment of 2026-10-09T00:42:42Z): from nu's sign at the nearest solved angles
    below and above it, modulo the period P, among those with |nu| > NU_TOL; 'min' for + below and - above, 'max' for
    the reverse, else 'unresolved'. The H cross-check: where both ends differ from the root's H by more than H_TOL, it
    must agree, or the kind is unresolved. convention = +1 is nu = -c dH/dtheta with c > 0 (control 1b's); -1 is
    for the flipped-convention check only. Returns (kind, the H test's own reading or None)."""
    up = [((t - theta_r) % P, convention * v) for t, v in samples if abs(v) > NU_TOL and (t - theta_r) % P > 0]
    dn = [((theta_r - t) % P, convention * v) for t, v in samples if abs(v) > NU_TOL and (theta_r - t) % P > 0]
    if not up or not dn:
        return 'unresolved', None
    va, vb = min(up)[1], min(dn)[1]
    k = 'min' if (vb > 0 and va < 0) else ('max' if (vb < 0 and va > 0) else 'unresolved')
    hk = None
    if len(H_ends) == 2 and all(abs(h - H_r) > H_TOL for h in H_ends):
        hk = 'min' if all(h > H_r for h in H_ends) else ('max' if all(h < H_r for h in H_ends) else 'mixed')
        if k != 'unresolved' and hk != k:
            k = 'unresolved'
    return k, hk


def angle_solve(lc, m, sigma0, theta_start=0.0, n_periods=1):
    """The frozen rule at fixed norm m, on a LevelCase's circle or on a given circle. Returns the record (grid, roots,
    classes, selection), the selected solution and the circle; the roots, with their solutions, stay on the circle."""
    C = lc if hasattr(lc, 'solve') else Circle(lc)
    cache = {}

    def at(th):
        if th not in cache:
            cache[th] = C.solve(th, m, sigma0)
        return cache[th]

    N = N_GRID * n_periods
    grid = [at(theta_start + k * C.period / N_GRID) for k in range(N + 1)]       # the last closes the interval
    roots, skipped = [], []
    isroot = lambda r: 'failed' not in r and abs(r['nu']) <= NU_TOL
    for k in range(N):
        a, b = grid[k], grid[k + 1]
        if 'failed' in a or 'failed' in b:
            skipped.append(dict(interval=[a['theta'], b['theta']], reason='Newton failure at an end'))
            continue
        if isroot(a) or isroot(b):
            continue                            # a grid point that is a root enters once, below
        if np.sign(a['nu']) == np.sign(b['nu']):
            continue

        def f(th):
            r = at(th)
            if 'failed' in r:
                raise RuntimeError(r['failed'])
            return r['nu']
        try:
            th = brentq(f, a['theta'], b['theta'], xtol=1e-13, maxiter=100)
        except RuntimeError as e:
            skipped.append(dict(interval=[a['theta'], b['theta']], reason=str(e)))
            continue
        r = at(th)
        roots.append(dict(r, interval=[a['theta'], b['theta']], ends=[a['H'], b['H']], source='interval'))
    for k in range(N):                          # grid points that are roots, each once (the last point repeats the first)
        if isroot(grid[k]):
            lo, hi = grid[k - 1] if k > 0 else grid[N - 1], grid[k + 1]
            ends = [x['H'] for x in (lo, hi) if 'failed' not in x]
            roots.append(dict(grid[k], interval=[lo['theta'], hi['theta']], ends=ends, source='grid point'))
    roots.sort(key=lambda r: r['theta'])
    samples = [(x['theta'], x['nu']) for x in cache.values() if 'failed' not in x]
    for r in roots:
        kd, hk = kind_of(r['theta'], r['H'], samples, r['ends'], C.period)
        r.update(resolved=bool(abs(r['nu']) <= NU_TOL), kind=kd, kind_H=hk, minimum=kd == 'min', maximum=kd == 'max')
    Hs = [g['H'] for g in grid if 'failed' not in g]
    H_range = max(Hs) - min(Hs)
    mins = [r for r in roots if r['resolved'] and r['minimum']]
    C.last_roots = roots
    lab, best = C.classes(mins) if mins else ([], {})
    sel = None
    if mins:
        i0 = int(np.argmin([r['H'] for r in mins]))
        sel = mins[i0]
        near = [dict(theta=r['theta'], H=r['H']) for i, r in enumerate(mins)
                if lab[i] != lab[i0] and r['H'] - sel['H'] <= NEAR_FRAC * H_range]
    strip = lambda r: {k: v for k, v in r.items() if k != 'Phi'}
    rec = dict(m=float(m), sigma0=float(sigma0), theta_start=float(theta_start), n_periods=n_periods,
               period=float(C.period), axis=[float(v) for v in C.ax], order=C.order, n_solves=C.n_solves,
               grid=[strip(g) for g in grid], roots=[strip(r) for r in roots], skipped=skipped, H_range=float(H_range),
               minima=[dict(theta=r['theta'], H=r['H'], cls=int(l)) for r, l in zip(mins, lab)],
               n_classes=len(set(lab)), pair_overlaps={f'{i},{j}': o for (i, j), o in best.items()},
               selected=(strip(sel) if sel else None), near_degenerate=(near if sel else []))
    return rec, (sel['Phi'] if sel else None), C


# --- the carry (REGISTER_1.md, amendment of 2026-10-08T23:57:20Z) --------------------------------------------------
ACCEPT_SPACINGS = 2.0       # the fallback takes a root of the tracked kind within this many grid spacings


class CarryEnd(Exception):
    """A registered end of the selected track: the carried root is not a minimum, is lost, is unresolved, or has an
    unresolved kind; with the trial angle and the trial norm."""
    def __init__(self, reason, theta, m):
        super().__init__(reason)
        self.reason, self.theta, self.m = reason, float(theta), float(m)


class _Failed(Exception):
    pass


class _Root(Exception):
    def __init__(self, theta):
        self.theta = theta


def wrap_near(t, c, P):
    """t moved by whole periods to lie within half a period of c."""
    return c + (((t - c) + P / 2) % P - P / 2)


def carry_solve(C, m, sigma0, theta_c, start=None, kind='min'):
    """The carry rule at norm m from the carried coordinate theta_c: a local Brent solve on [theta_c - w, theta_c + w]
    when nu changes sign across it, the kind check, and otherwise the full rule from theta_c as the fallback, taking the
    nearest root of the tracked kind within two spacings. Returns the root (with Phi), None on a Newton failure, or
    raises CarryEnd."""
    w = C.period / N_GRID
    cache = {}

    def at(th):
        if th not in cache:
            cache[th] = C.solve(th, m, sigma0, start=start)
        return cache[th]

    lo, hi = at(theta_c - w), at(theta_c + w)
    if 'failed' in lo or 'failed' in hi:
        return None
    if abs(lo['nu']) > NU_TOL and abs(hi['nu']) > NU_TOL and np.sign(lo['nu']) != np.sign(hi['nu']):
        def f(th):
            r = at(th)
            if 'failed' in r:
                raise _Failed
            if abs(r['nu']) <= NU_TOL:
                raise _Root(th)                 # Brent stops at the registered bar (amendment of 00:42:42Z)
            return r['nu']
        try:
            th = brentq(f, theta_c - w, theta_c + w, xtol=1e-13, maxiter=100)
        except _Failed:
            return None
        except _Root as e:
            th = e.theta
        r = at(th)
        if abs(r['nu']) > NU_TOL:
            raise CarryEnd('the carried root is unresolved', th, m)
        samples = [(x['theta'], x['nu']) for x in cache.values() if 'failed' not in x]
        kd, hk = kind_of(th, r['H'], samples, [lo['H'], hi['H']], C.period)
        if kd == 'unresolved':
            raise CarryEnd("the carried root's kind is unresolved", th, m)
        if kd != kind:
            raise CarryEnd(f'the carried root is not a {kind}imum', th, m)
        return dict(r, kind=kd, kind_H=hk, fallback=False, n_solves=len(cache))
    n0 = C.n_solves
    rec, _, _ = angle_solve(C, m, sigma0, theta_start=theta_c)
    P = C.period
    cands = [r for r in C.last_roots if r['resolved'] and r['kind'] == kind]
    if cands:
        best = min(cands, key=lambda r: abs(wrap_near(r['theta'], theta_c, P) - theta_c))
        th = wrap_near(best['theta'], theta_c, P)
        if abs(th - theta_c) <= ACCEPT_SPACINGS * w:
            ov = (C.overlap(best['Phi'], start[0]) if start is not None and best['Phi'] is not None
                  and hasattr(C, 'overlap') else None)
            return dict(best, theta=float(th), fallback=True, n_solves=len(cache) + C.n_solves - n0, source_overlap=ov)
    raise CarryEnd(f'the carried root is lost: no {kind}imum within two grid spacings', theta_c, m)


def track_others(C, m, sigma0, others, sel_H, events, label):
    """Carry every live other critical point one ladder point on, and record what the registered rule records: a lost
    or wrong-kind track stops, and a carried minimum below the selected one is 'no longer the lowest minimum' (once).
    others: dicts with kind, theta, start (x, phys, m) or None, alive, rows."""
    for o in others:
        if not o['alive']:
            continue
        try:
            r = carry_solve(C, m, sigma0, o['theta'], start=o['start'], kind=o['kind'])
        except CarryEnd as e:
            o['alive'] = False
            events.append(dict(at=label, track=o['label'], event=e.reason, theta=e.theta))
            continue
        if r is None:
            o['alive'] = False
            events.append(dict(at=label, track=o['label'], event='Newton failure'))
            continue
        o['theta'] = r['theta']
        if r['Phi'] is not None:
            o['start'] = (to_real(r['Phi']), r['theta'] + C.offset, m)
        o['rows'].append(dict(at=label, theta=r['theta'], phys=r['theta'] + C.offset, H=r['H'], nu=r['nu'],
                              fallback=r['fallback']))
    lower = [o for o in others if o['alive'] and o['kind'] == 'min' and o['rows'] and o['rows'][-1]['H'] < sel_H]
    if lower and not any(e['event'] == 'no longer the lowest minimum' for e in events):
        events.append(dict(at=label, track='selected', event='no longer the lowest minimum',
                           below=[o['label'] for o in lower]))


class AngleBranch(Branch):
    """A slice case's branch with the angle an unknown at every continuation solve: the full rule of § 1b at the first
    point selects the minimum, which is then carried from each accepted point by carry_solve; the circle's other
    critical points found there are carried beside it at every ladder point. A registered end of the selected track
    ends the branch, never followed by a re-selection."""
    def __init__(self, lc, circle=None, theta_start=0.0, track=False, log=lambda s: None, **kw):
        super().__init__(lc.st, lc.case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=log, **kw)
        self.C = circle if circle is not None else Circle(lc)
        self.theta_start, self.track = theta_start, track
        self.perturb = None         # controls only: f(branch) -> offset added to the next carried coordinate
        self.others, self.events, self.first_grid, self.sel_rows = [], [], None, []

    def _rec(self, r, m):
        return dict(m=m, eps=r['sigma'] - self.lam0, sigma=r['sigma'], x=to_real(r['Phi']), it=r['it'], full=r['full'],
                    nu=[r['nu']], mu=[r['mu']], H=r['H'], theta=r['theta'], phys=r['theta'] + self.C.offset,
                    offset=self.C.offset, fallback=r.get('fallback', False), n_solves=r.get('n_solves'))

    def first(self, eps0):
        m0 = eps0 / (self.Q / self.vol) / 120
        rec, _, _ = angle_solve(self.C, m0, self.lam0 + eps0, theta_start=self.theta_start)
        self.first_grid = rec
        if rec['selected'] is None:
            self.end = ('no minimum on the circle at the seed', None)
            return False
        roots = [r for r in self.C.last_roots if r['resolved']]
        sel = next(r for r in roots if r['theta'] == rec['selected']['theta'])
        self.accept(self._rec(sel, m0))
        if self.track:
            c0 = next(q['cls'] for q in rec['minima'] if q['theta'] == sel['theta'])
            same = {q['theta'] for q in rec['minima'] if q['cls'] == c0}       # the selected minimum and its copies
            for i, r in enumerate(x for x in roots if x['theta'] not in same and (x['minimum'] or x['maximum'])):
                self.others.append(dict(label=f'other {i}', kind='min' if r['minimum'] else 'max', theta=r['theta'],
                                        start=(to_real(r['Phi']), r['theta'] + self.C.offset, m0), alive=True, rows=[]))
        return True

    def newton(self, m, x_from, m_from, eps_guess):
        src = next(r for r in reversed(self.accepted) if r['x'] is x_from)
        theta_c = src['theta'] + (self.perturb(self) if self.perturb is not None else 0.0)
        r = carry_solve(self.C, m, self.lam0 + eps_guess, theta_c, start=(src['x'], src['phys'], src['m']))
        return None if r is None else self._rec(r, m)

    def run(self, targets, on_point=None):
        def hook(k, eps_k, rec):
            self.sel_rows.append(dict(at=float(eps_k), theta=rec['theta'], phys=rec['phys'], H=rec['H']))
            if self.track:
                track_others(self.C, rec['m'], rec['sigma'], self.others, rec['H'], self.events, float(eps_k))
            if on_point is not None:
                on_point(k, eps_k, rec)
        try:
            return super().run(targets, on_point=hook)
        except CarryEnd as e:
            last = self.accepted[-1]
            self.end = (e.reason, dict(m=last['m'], eps=last['eps'], theta_tried=e.theta, m_tried=e.m))
            self.log(f'    branch ends: {e.reason} (tried {e.theta:.6f})')
            return self

    def goto(self, eps_target, start):
        """Branch.goto for the change-of-type bisection: an end of the selected track there fails that bisection step,
        as a Newton failure does, and is recorded; the branch stays as it is."""
        try:
            return super().goto(eps_target, start)
        except CarryEnd as e:
            self.events.append(dict(at=float(eps_target), track='selected', event=e.reason, theta=e.theta, m=e.m))
            return None
