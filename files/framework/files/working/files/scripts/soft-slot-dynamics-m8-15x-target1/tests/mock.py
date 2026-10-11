"""The mock evaluator of REGISTER_4.md v3 § 2: planted spectra, read by the locator through the frozen functions.

The static spectrum lives in 80 dimensions with M = I: basis e0..e3 span the structural span P (e0 an exact zero, e1..e3
lifts at -1e-5), e4 and e5 the genuine doubled crossing pair s_h(eps) = a (r_h - eps), e6..e79 the 74 inert positive
spectators 0.05 * 40^(k/73). The Hamiltonian genuine set holds the crossing pair, lambda_h^2 = c (eps - r_h), doubled,
and another imaginary pair at 0.0745 i eps; each field decide reads is derived by the frozen functions."""
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import locate

m815_branch = locate.import_instrument()
from verdict import representatives, Verdict

DIM, NSTRUCT = 80, 4
TOL_L = 1e-9
TAU0 = 1.040e-5                         # R4's tau0 = tau_Re at level 3, used at both levels by the mock
S2_R4, OMEGA0, DLEV = 6.739e-4, np.sqrt(48.0), 1e-2
LADDER = {0.6: 11, 0.8: 12, 1.2: 13, 1.4: 14}      # the mock's ladder points and their indices
BRACKET, REGION = (0.8, 1.2), (0.6, 1.4)
SPECTATORS = [0.05 * 40 ** (k / 73) for k in range(74)]


def close(a, b):
    return abs(a - b) <= 1e-12 * max(1.0, abs(b))


class Plant:
    """The baseline plant; each test changes only what it names."""
    def __init__(self, **kw):
        self.r = {3: 1.0130, 2: 1.0181}
        self.a, self.c = 0.05, 0.01
        self.genuine_crossing = True
        self.struct_cross = None            # S2: two lifts follow 0.01 (eps - eps0), n(B|G) falling with them
        self.second_root = None             # S16: a second genuine doubled crossing
        self.newton_fail = None             # S7: (level, kind, call)
        self.quartet_at = None              # S6: (level, eps)
        self.bwe_at = []                    # S4, S16: [(level, eps)] with backward error 1e-9
        self.slow_at = None                 # S11: (level, eps, overlap)
        self.swap_at = []                   # S5: [(level, eps)] where the real pairs become one Krein-negative pair
        self.nB_wrong = False               # S9: n(B|G) planted so the genuine change is +1
        self.turn = None                    # S8: (level, overlap below the root, overlap above the root)
        self.tilt_at = None                 # S10: (level, eps, overlap)
        self.tilt_lifts = None              # S2 and S3 arms: overlap of the two crossing lifts, everywhere
        self.rotate = False                 # S17
        self.near_spectators = False        # S15
        self.nB_lag = None                  # S18: n(B|G) falls this much later than n(L)
        self.one_real = False               # S9: two L eigenvalues cross, but the genuine set gains one real pair
        self.tilt_points = []               # S18b: [(level, eps, overlap)] where the exact zero's eigenvector is tilted
                                            # out of P: the structural subspace check fails and n_S is unchanged
        self.nB_offset_all = 0              # S18c: n(B|G) too high by this at every point
        self.__dict__.update(kw)


class MockPoint:
    """The fields decide reads, derived from the plant by the frozen rules (Point's and Verdict's)."""
    reps = m815_branch.Point.reps

    def __init__(self, genuine_all, nL, nB, bwe, tau_re=TAU0, tau0=TAU0):
        self.genuine_all = genuine_all
        self.genuine = representatives(genuine_all, tau_re)
        self.nL, self.nB_cluster, self.nB = nL, nB, nB
        self.kr, self.kc, self.kim, self.rhs = Verdict.count(self, tau_re)
        self.balanced = (self.kr + 2 * self.kc + 2 * self.kim == self.rhs)
        self.fast = None if self.balanced else dict(found=[], counts=[self.kr, self.kc, self.kim], balanced=False)
        self.zero_crossing = any(abs(l) <= tau0 for l, _ in self.genuine)
        self.dim, self.closed, self.omega_gram = 8, True, 1.0
        self.cluster_ok = True
        self.lifted = np.array([1e-6 + 0j, 1e-6 + 0j])
        self.kind = ['paired', 'paired']
        self.bwe = bwe
        self.sigma = 48.0


def rot2(B, i, j, t):
    """Rotate basis columns i and j by angle t (in their plane)."""
    c, s = np.cos(t), np.sin(t)
    bi, bj = B[:, i].copy(), B[:, j].copy()
    B[:, i], B[:, j] = c * bi + s * bj, -s * bi + c * bj


class MockEvaluator:
    def __init__(self, plant):
        self.pl = plant
        self.calls = {}

    def inner(self, level, A, B):
        return A.T @ B

    def goto(self, level, eps, start, kind='grid'):
        n = self.calls.get((level, kind), 0)
        self.calls[(level, kind)] = n + 1
        nf = self.pl.newton_fail
        if nf is not None and nf == (level, kind, n):
            hist = [[dict(it=0, res=1e-3, full=1e-3), dict(it=1, res=2e-6, full=2e-6)]]
            return None, hist
        return dict(eps=eps, full=1e-12, x=None, sigma=48.0), None

    def static(self, level, eps):
        """The planted static spectrum: (values, orthonormal eigenvectors as columns)."""
        pl = self.pl
        vals = np.zeros(DIM)
        B = np.eye(DIM)
        vals[0] = 1e-14
        vals[1:4] = -1e-5
        if pl.struct_cross is not None:
            vals[2] = vals[3] = 0.01 * (eps - pl.struct_cross)
        if pl.genuine_crossing:
            vals[4] = vals[5] = pl.a * (pl.r[level] - eps)
        else:
            vals[4] = vals[5] = 0.02
        sp = list(SPECTATORS)
        if pl.near_spectators:
            sp = sp[:58] + [1e-7 * k for k in range(1, 17)]
        vals[6:] = sp
        if pl.second_root is not None:
            vals[78] = vals[79] = pl.a * (pl.second_root - eps)
        # eigenvector shapes
        if pl.tilt_lifts is not None:
            t = np.arccos(pl.tilt_lifts)
            rot2(B, 2, 6, t)
            rot2(B, 3, 7, t)
        if pl.tilt_at is not None and pl.tilt_at[0] == level and close(eps, pl.tilt_at[1]):
            rot2(B, 1, 6, np.arccos(pl.tilt_at[2]))
        for lv, e, ov in pl.tilt_points:
            if lv == level and close(eps, e):
                rot2(B, 0, 6, np.arccos(ov))
        if pl.turn is not None and pl.turn[0] == level:
            ovl = pl.turn[1] if eps < pl.r[level] else pl.turn[2]
            rot2(B, 4, 3, np.arcsin(ovl))       # e4 turns toward p3; the lift on p3 is displaced
        if pl.rotate:
            rot2(B, 4, 5, 2 * np.pi * eps / 0.01)
        return vals, B

    def hamiltonian(self, level, eps):
        pl = self.pl
        g = []
        r = pl.r[level]
        swap = any(lv == level and close(eps, e) for lv, e in pl.swap_at)

        def crossing(root):
            out = []
            if eps < root:
                w = np.sqrt(pl.c * (root - eps))
                out += [(1j * w, 1.0), (-1j * w, -1.0)] * 2
            elif swap:
                w = np.sqrt(pl.c * (eps - root))
                out += [(1j * w, -1.0), (-1j * w, 1.0)]
            elif pl.one_real and root == r:
                rr = np.sqrt(pl.c * (eps - root))
                out += [(rr + 0j, 0.0), (-rr + 0j, 0.0), (1j * rr, 1.0), (-1j * rr, -1.0)]
            else:
                rr = np.sqrt(pl.c * (eps - root))
                out += [(rr + 0j, 0.0), (-rr + 0j, 0.0)] * 2
            return out
        if pl.genuine_crossing:
            g += crossing(r)
        if pl.second_root is not None:
            g += crossing(pl.second_root)
        w = 0.0745 * eps
        g += [(1j * w, 1.0), (-1j * w, -1.0)]
        quartet = pl.quartet_at is not None and pl.quartet_at[0] == level and close(eps, pl.quartet_at[1])
        if quartet:
            g += [(0.01 + 0.02j, 0.0), (0.01 - 0.02j, 0.0), (-0.01 + 0.02j, 0.0), (-0.01 - 0.02j, 0.0)]
        return g, quartet

    def evaluate(self, level, eps, rec, full=False):
        pl = self.pl
        vals, B = self.static(level, eps)
        inner = lambda X, Y: X.T @ Y
        P, rel, gate = locate.structural_span(np.eye(DIM)[:, :NSTRUCT], NSTRUCT, inner)

        def eigs(k):
            order = np.argsort(np.abs(vals - locate.SHIFT))[:k]
            return vals[order], B[:, order]
        v, vecs, nz, k = locate.near_zero_loop(eigs, P, inner, TOL_L, NSTRUCT)
        nL = int((vals < -TOL_L).sum())
        g, quartet = self.hamiltonian(level, eps)
        # n(B|G) planted so the count balances (consistent), except S9
        tmp = MockPoint(g, nL, 0, 1e-12)
        nB = nL - (tmp.kr + 2 * tmp.kc + 2 * tmp.kim)
        if pl.nB_wrong and eps > pl.r[level]:
            nB += 1
        if pl.nB_lag is not None and pl.struct_cross < eps < pl.struct_cross + pl.nB_lag:
            nB += 2
        nB += pl.nB_offset_all
        bwe = 1e-9 if any(lv == level and close(eps, e) for lv, e in pl.bwe_at) else 1e-12
        p = MockPoint(g, nL, nB, bwe)
        slow = 0.1
        if pl.slow_at is not None and pl.slow_at[0] == level and close(eps, pl.slow_at[1]):
            slow = pl.slow_at[2]
        ep = locate.EvalPoint(level, eps, rec, p, nL, nB, p.kc, v, vecs, nz, k, rel, gate, slow, 1e-12, TOL_L,
                              ctx=dict(P=P, fast_skipped=not full))
        ep._full = (vals, B)
        return ep

    def enlarge(self, ep, k):
        vals, B = ep._full
        order = np.argsort(np.abs(vals - locate.SHIFT))[:k]
        inner = lambda X, Y: X.T @ Y
        nz = locate.near_zero_data(vals[order], B[:, order], ep.ctx['P'], inner, TOL_L, NSTRUCT)
        new = locate.EvalPoint(ep.level, ep.eps, ep.rec, ep.p, ep.nL, ep.nB, ep.kc, vals[order], B[:, order], nz, k,
                               ep.gate_rel, ep.gate_ok, ep.slow_overlap, ep.residual, ep.tolL, ctx=ep.ctx)
        new._full = ep._full
        return new


def mock_decide():
    text, h = locate.decide_source()
    return locate.bind_decide(m815_branch, text, name='MOCK', slot=4, tau0_3=TAU0, s2=S2_R4, omega0=OMEGA0,
                              dlev=DLEV, sch=[]), h


def run(plant, label='primary'):
    """The locator on the mock's bracket, with the ladder's region-end verdicts read as the ladder reads them."""
    ev = MockEvaluator(plant)
    decide, h = mock_decide()
    pool = {3: {}, 2: {}}
    for e in LADDER:
        for lv in (3, 2):
            pool[lv][e] = ev.evaluate(lv, e, dict(eps=e, full=1e-12, x=None, sigma=48.0))
    ladder_types = {}
    for e, i in LADDER.items():
        typ, why, cross = decide(e, pool[3][e].p, pool[2][e].p, i % 3 == 0)
        ladder_types[e] = dict(type=typ, why=list(why))
    ends = {lv: (pool[lv][BRACKET[0]], pool[lv][BRACKET[1]]) for lv in (3, 2)}
    res = locate.locate_bracket(ev, decide, {3: BRACKET, 2: BRACKET}, REGION, label, ends, ladder_types, pool)
    res['decide_sha256'] = h
    return res
