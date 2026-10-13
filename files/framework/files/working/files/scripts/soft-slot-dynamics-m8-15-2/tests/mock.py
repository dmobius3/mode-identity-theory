"""The mock evaluator of REGISTER_4.md v3 § 2: planted spectra, read by the locator through the frozen functions. It
stays the default for every S test; REGISTER_5.md § 1 adds the hooks of M8.15.2's plants, each off by default.

The static spectrum lives in 80 dimensions with M = I: basis e0..e3 span the structural span P (e0 an exact zero, e1..e3
lifts at -1e-5), e4 and e5 the genuine doubled crossing pair s_h(eps) = a (r_h - eps), e6..e79 the 74 inert positive
spectators 0.05 * 40^(k/73). The Hamiltonian genuine set holds the crossing pair, lambda_h^2 = c (eps - r_h), doubled,
and another imaginary pair at 0.0745 i eps; each field decide reads is derived by the frozen functions.

M8.15.2's additions: every point carries the solution norm m and a reached eps (by default the target, with
m = 1 + 0.15 (eps - 1) + 0.5 * 3.4601e-4 (eps - 1)^2 at the reached eps, so rule 11's statistic reads 3.4601e-4
exactly); the coupling of the genuine pair (e4, e5) to the lifts (e2, e3) in two blocks [[g, kappa], [kappa, -delta]],
g = sigma a (r - eps), whose Hamiltonian type change sits where each block is singular, r + sigma kappa^2 / (a delta);
and the plant hooks REGISTER_5.md § 1 lists."""
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
M2 = 3.4601e-4                          # the default m path's curvature: the controls' largest rule-11 statistic


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
        # M8.15.2's hooks (REGISTER_5.md § 1), each off by default
        self.kappa = None                   # the coupling of (e4, e5) to the lifts (e2, e3), in blocks [[g, kappa],
        self.sigma = +1                     #   [kappa, -delta]], g = sigma a (r - eps): sigma the slope sign
        self.delta = 1e-5
        self.lift_line = None               # (eps_s, b): the coupled lifts follow b (eps - eps_s) (A2, A28)
        self.hold = None                    # the genuine pair held at this value in the blocks (A2, A28)
        self.e0_line = None                 # (zero, slope): e0's eigenvalue slope (eps - zero) (A9)
        self.e1_line = None                 # (zero, slope): e1's eigenvalue slope (eps - zero) (A3, A29)
        self.extra = None                   # (zero, slope): an extra genuine eigenvalue on e7, with its own type change
        self.glitch = None                  # (level, eps, value): e7's eigenvalue at one point, an extra negative one (A4)
        self.turn_out = None                # degrees: the genuine pair turned toward e8 and e9 from the root up (A5)
        self.gate_fail = None               # (level, eps): the span's gate fails there (A7)
        self.cover_fail = None              # (level, eps): spectral coverage fails there at every k_L (A7)
        self.m_jump = None                  # (lo, hi, J): targets in (lo, hi) on a second path, m + J (A20, A21, A24)
        self.slack = False                  # the reached eps alternating by +-1e-6, relative, in evaluation order (A22)
        self.reeval_J = 0.0                 # a re-evaluation of an evaluated target on a second path, m + J (A25)
        self.region = REGION                # the guard region: only its ladder points seed the pool (A26)
        self.a17 = None                     # (level, cos alpha, degrees): A17's construction
        self.a18 = None                     # A18's second genuine doublet on e10 and e11, held at this value
        self.nB_at = []                     # [(level, eps, dn)]: n(B|G) too high by dn at that point (A11(b))
        self.__dict__.update(kw)


class MockPoint:
    """The fields decide reads, derived from the plant by the frozen rules (Point's and Verdict's)."""
    reps = m815_branch.Point.reps

    def __init__(self, genuine_all, nL, nB, bwe, tau_re=TAU0, tau0=TAU0, m=None, eps_reached=None):
        self.m, self.eps_reached = m, eps_reached           # what rule 11 reads, as from the frozen Point
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
        self.count, self.seen = {}, {}      # evaluations per level, and their targets (the slack and reeval_J hooks)

    def block(self, level, eps):
        """One coupled block in (genuine, lift): [[g, kappa], [kappa, -delta]], or with the hold and the lift line."""
        pl = self.pl
        g = pl.hold if pl.hold is not None else pl.sigma * pl.a * (pl.r[level] - eps)
        lift = pl.lift_line[1] * (eps - pl.lift_line[0]) if pl.lift_line is not None else -pl.delta
        return np.array([[g, pl.kappa], [pl.kappa, lift]])

    def pair(self, lam):
        """The Hamiltonian pair of a genuine static eigenvalue lam, lambda^2 = c |lam| / a: imaginary with Krein sign +
        where lam > 0, real where lam <= 0."""
        w = np.sqrt(self.pl.c * abs(lam) / self.pl.a)
        return [(1j * w, 1.0), (-1j * w, -1.0)] if lam > 0 else [(w + 0j, 0.0), (-w + 0j, 0.0)]

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
        # M8.15.2's eigenvalue hooks
        if pl.e0_line is not None:
            vals[0] = pl.e0_line[1] * (eps - pl.e0_line[0])
        if pl.e1_line is not None:
            vals[1] = pl.e1_line[1] * (eps - pl.e1_line[0])
        if pl.extra is not None:
            vals[7] = pl.extra[1] * (eps - pl.extra[0])
        if pl.glitch is not None and pl.glitch[0] == level and close(eps, pl.glitch[1]):
            vals[7] = pl.glitch[2]
        if pl.a18 is not None and level == pl.a17[0]:
            vals[10] = vals[11] = pl.a18
        # the coupled blocks: column 4 (5) holds each block's lower eigenpair, column 2 (3) its upper
        if pl.kappa is not None:
            for gi, li in ((4, 2), (5, 3)):
                w, v = np.linalg.eigh(self.block(level, eps))
                for j, col in ((0, gi), (1, li)):
                    B[:, col] = 0.0
                    B[gi, col], B[li, col] = v[0, j], v[1, j]
                    vals[col] = w[j]
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
        # M8.15.2's eigenvector hooks
        if pl.cover_fail is not None and pl.cover_fail[0] == level and close(eps, pl.cover_fail[1]):
            rot2(B, 3, 79, np.pi / 2)           # e3's direction moves to the largest spectator, outside every k_L
        if pl.turn_out is not None and eps >= pl.r[level]:
            t = np.radians(pl.turn_out)
            rot2(B, 4, 8, t)
            rot2(B, 5, 9, t)
        if pl.a17 is not None and level == pl.a17[0]:
            # the lift e1 tilted out of P by alpha toward u, the genuine pair's first vector g orthogonal to it; columns
            # 1, 4, 8 and 9 carry the tilted lift, g, w and e4, so the eigenvectors stay orthonormal
            E = np.eye(DIM)
            al = np.arccos(pl.a17[1])
            phi = np.radians(pl.a17[2]) if eps >= pl.r[level] else 0.0
            u = np.cos(phi) * E[:, 8] + np.sin(phi) * E[:, 9]
            B[:, 1] = np.cos(al) * E[:, 1] + np.sin(al) * u
            B[:, 4] = -np.sin(al) * E[:, 1] + np.cos(al) * u
            B[:, 8] = -np.sin(phi) * E[:, 8] + np.cos(phi) * E[:, 9]
            B[:, 9] = E[:, 4]
            if pl.a18 is not None and eps >= pl.r[level]:
                # from the root up the crossing doublet's first vector is e10, the second doublet's the turned g
                B[:, 10], B[:, 4] = B[:, 4].copy(), E[:, 10]
        return vals, B

    def hamiltonian(self, level, eps):
        pl = self.pl
        g = []
        r = pl.r[level]
        if pl.kappa is not None and pl.hold is None:
            r = r + pl.sigma * pl.kappa ** 2 / (pl.a * pl.delta)      # where each coupled block is singular
        swap = any(lv == level and close(eps, e) for lv, e in pl.swap_at)

        def crossing(root, sign=+1):
            # sign -1: the pair is real below the root and imaginary above it (slope sign -1)
            out = []
            if (eps < root) if sign > 0 else (eps > root):
                w = np.sqrt(pl.c * abs(root - eps))
                out += [(1j * w, 1.0), (-1j * w, -1.0)] * 2
            elif swap:
                w = np.sqrt(pl.c * abs(eps - root))
                out += [(1j * w, -1.0), (-1j * w, 1.0)]
            elif pl.one_real and root == r:
                rr = np.sqrt(pl.c * abs(eps - root))
                out += [(rr + 0j, 0.0), (-rr + 0j, 0.0), (1j * rr, 1.0), (-1j * rr, -1.0)]
            else:
                rr = np.sqrt(pl.c * abs(eps - root))
                out += [(rr + 0j, 0.0), (-rr + 0j, 0.0)] * 2
            return out
        if pl.hold is not None:
            g += self.pair(pl.hold) * 2                 # the genuine pair held: no type change
        elif pl.genuine_crossing:
            g += crossing(r, pl.sigma)
        if pl.second_root is not None:
            g += crossing(pl.second_root)
        if pl.extra is not None:
            g += self.pair(pl.extra[1] * (eps - pl.extra[0]))
        if pl.a18 is not None and level == pl.a17[0]:
            g += self.pair(pl.a18) * 2
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
        gens = np.eye(DIM)[:, :NSTRUCT]
        if pl.gate_fail is not None and pl.gate_fail[0] == level and close(eps, pl.gate_fail[1]):
            # a fifth generator near e3: the span's gap gate fails (sigma_5 / sigma_1 = 0.147 > 0.05), P stays near e0..e3
            gens = np.column_stack([gens, np.eye(DIM)[:, 3] + 0.3 * np.eye(DIM)[:, 6]])
        P, rel, gate = locate.structural_span(gens, NSTRUCT, inner)

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
        nB += sum(dn for lv, e, dn in pl.nB_at if lv == level and close(eps, e))
        bwe =1e-9 if any(lv == level and close(eps, e) for lv, e in pl.bwe_at) else 1e-12
        # rule 11's fields: the reached eps and m on the default path, with the slack, second-path and re-evaluation hooks
        n = self.count.get(level, 0)
        self.count[level] = n + 1
        reached = eps * (1 + (1e-6 if n % 2 == 0 else -1e-6)) if pl.slack else eps
        x = reached - 1.0
        m = 1.0 + 0.15 * x + 0.5 * M2 * x * x
        if pl.m_jump is not None and pl.m_jump[0] < eps < pl.m_jump[1]:
            m += pl.m_jump[2]
        if any(abs(e - eps) <= 1e-9 * eps for e in self.seen.get(level, [])):
            m += pl.reeval_J
        self.seen.setdefault(level, []).append(eps)
        p = MockPoint(g, nL, nB, bwe, m=m, eps_reached=reached)
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
    region = plant.region
    seeded = [e for e in LADDER if region[0] * (1 - 1e-12) <= e <= region[1] * (1 + 1e-12)]   # the region's points
    pool = {3: {}, 2: {}}
    for e in seeded:
        for lv in (3, 2):
            pool[lv][e] = ev.evaluate(lv, e, dict(eps=e, full=1e-12, x=None, sigma=48.0))
    ladder_types = {}
    for e, i in LADDER.items():
        if e in seeded:
            typ, why, cross = decide(e, pool[3][e].p, pool[2][e].p, i % 3 == 0)
            ladder_types[e] = dict(type=typ, why=list(why))
    ends = {lv: (pool[lv][BRACKET[0]], pool[lv][BRACKET[1]]) for lv in (3, 2)}
    res = locate.locate_bracket(ev, decide, {3: BRACKET, 2: BRACKET}, region, label, ends, ladder_types, pool)
    res['decide_sha256'] = h
    return res
