"""Shared pieces of the M8.15 run: per-level case setup, the frozen small-amplitude spectra, leading-order predictions,
the cross-level matching rule, and the resolution schedule."""
import numpy as np
from math import sqrt
from scipy.optimize import linear_sum_assignment
from fem import Mesh
from irreps import irreps
from standing import Standing, lowest_level
from pinned import PinnedCase, rigid_pair
from symmetry import Rotations
from continuation import Branch, ladder

G, RS = irreps()

# the frozen algebraic dimension k + r_u of each case's tracked cluster
FROZEN_DIM = {'C1': 6, 'C2a': 4, 'C2b': 6, 'C3': 8, 'T1': 4, 'T2': 8, 'T3': 8, 'T4': 6, 'T5': 10, 'C3s': 8, 'C2b_D5': 6,
              'P5': 6}       # P5: M8.15.x control 2a (REGISTER_2.md), the census zero multiplicity
LAM0 = {2: 63.0, 3: 8.0, 4: 48.0, 5: 48.0}
EPS_MAX = {4: 72.0, 5: 32.0, 2: 132.0}
D7 = 9 / 16

# small-amplitude slow spectra in R4's (or R2's) h normalization: list of (type, tau or sqrt(nu), Krein sign)
# 'i' imaginary pair at eps kappa tau; 'r' real pair at eps kappa sqrt(nu)
_T5q = (418161601, 6989958976, 28677390336)
_d = sqrt(_T5q[1] ** 2 - 4 * _T5q[0] * _T5q[2])
SPECTRA = {
    'C2a': [('i', t, +1) for t in (28 / 143, 56 / 429, 140 / 99, 112 / 39, 896 / 1287)],
    'C2b': [('i', t, +1) for t in (112 / 143, 168 / 143, 336 / 143, 504 / 143, 560 / 143)],
    'C3': [('r', sqrt(250880 / 552123), 0)] * 3,
    'T1': [('i', 56 / 1287, -1)] + [('i', t, +1) for t in (112 / 143, 112 / 117, 224 / 143, 560 / 429)],
    'T2': [('i', sqrt(5770240 / 7913763), +1)] + [('i', sqrt(19066880 / 278420571), +1)] * 2,
    'T3': [('i', sqrt(90160 / 61347), -1)] + [('i', sqrt(501760 / 552123), -1)] * 2,
    'T4': [('i', 1.01209160489, +1), ('i', 0.310692742362, -1), ('i', 0.139251832964, -1), ('i', 0.00573685922309, -1)],
    'T5': [('i', sqrt(153664 / 20449), -1), ('i', sqrt(-(-_T5q[1] + _d) / (2 * _T5q[0])), -1),
           ('i', sqrt(-(-_T5q[1] - _d) / (2 * _T5q[0])), -1)],
}
QEXACT = {('C2a', 4): 1288 / 1287, ('C2b', 2): 144 / 143, ('C3', 4): 175 / 143, ('C3s', 4): 175 / 143, ('C2b_D5', 2): 144 / 143,
          ('T1', 4): 147 / 143, ('T1', 5): 581 / 572, ('T2', 4): 5831 / 5031, ('T2', 5): 609 / 559,
          ('T3', 4): 1750 / 1287, ('T3', 5): 2751 / 2288, ('T4', 4): 1.185203461338846, ('T4', 5): 1.104176947003101,
          ('T5', 2): 22 / 13}


# M8.15.x control 2a (REGISTER_2.md): the pyramid's slow blocks from the reduced quartic at unit u
# (continuum_overlap_survey.py, |u|_G^2 = 1500); 'q' is a quartet, its first-quadrant tau complex
SPECTRA['P5'] = [('i', 93.352303643524 / 1500, -1), ('q', complex(62.602928975645, 91.375291375291) / 1500, 0),
                 ('i', 1642.778232487006 / 1500, +1)]
QEXACT[('P5', 4)] = 77 / 65
SPECTRA['C3s'] = SPECTRA['C3']
SPECTRA['C2b_D5'] = SPECTRA['C2b']


def kappa(name, slot):
    lam0 = LAM0[slot]
    return 1 / (8 * sqrt(lam0) * QEXACT[(name, slot)])


def predicted(name, slot, eps):
    """Leading-order slow eigenvalue representatives (Re >= 0, Im >= 0) with Krein signs, for the branch's own kappa;
    R5 scales tau by 9/16."""
    k = kappa(name, slot)
    sc = D7 if slot == 5 else 1.0
    out = []
    for typ, t, sgn in SPECTRA[name]:
        if typ == 'q':                          # a quartet's first-quadrant representative (control 2a)
            out.append((eps * k * sc * complex(t), sgn))
            continue
        lam = eps * k * sc * t
        out.append((complex(lam, 0) if typ == 'r' else complex(0, lam), sgn))
    return out


def schedule(name, slot, r_f3, targets):
    """The pre-registered resolution schedule: for each frozen mode, the first ladder point where tau0 = 10 r_f3 is at
    most eps kappa tau / 10."""
    tau0 = 10 * r_f3
    out = []
    for (lam1, sgn), (typ, t, _) in zip(predicted(name, slot, 1.0), SPECTRA[name]):
        mod = abs(lam1)
        first = next((e for e in targets if tau0 <= e * mod / 10), None)
        out.append(dict(type=typ, tau=t, krein=sgn, first_resolved=first))
    return out


def match(A, B):
    """The frozen cross-level matching: representatives matched one-to-one within each class (imaginary pairs by Krein
    sign, real pairs, quartets) by minimum total distance. A, B: lists of (lambda, class). Returns pairs or None when a
    class has unequal counts."""
    pairs = []
    classes = set(c for _, c in A) | set(c for _, c in B)
    for c in classes:
        a = [l for l, cc in A if cc == c]
        b = [l for l, cc in B if cc == c]
        if len(a) != len(b):
            return None
        if not a:
            continue
        C = np.abs(np.subtract.outer(np.array(a), np.array(b)))
        r, s = linear_sum_assignment(C)
        pairs += [(a[i], b[j], c) for i, j in zip(r, s)]
    return pairs


def classify(lam, krein, tau_re):
    if lam.real > tau_re and abs(lam.imag) <= tau_re:
        return 'real'
    if lam.real > tau_re:
        return 'quartet'
    return 'imag+' if krein > 0 else 'imag-'


class LevelCase:
    """A case at one mesh level, with everything a ladder point needs."""
    def __init__(self, level, name, slot=None, meshes={}):
        if level not in meshes:
            meshes[level] = Mesh(level, nq=3)
        self.mesh = mesh = meshes[level]
        self.level = level
        self.vol = 120 * mesh.vol.sum()
        self.case = PinnedCase(mesh, RS, name, slot=slot)
        self.name, self.slot = name, self.case.slot
        self.st = Standing(mesh, self.case.R, quaternionic=self.case.quaternionic)
        self.rot = Rotations(mesh, self.case.R, self.st.M)
        n0 = self.case.j2 + 1
        lam = lowest_level(self.st, n0)
        self.lam0, self.lam0_min, self.spread = lam.mean(), lam.min(), lam.max() - lam.min()
        P = self.case.seed
        self.Q = self.vol * 4 * self.st.q.energy(P) * 120 / (120 * np.real(np.vdot(P, self.st.M @ P))) ** 2
        self.rigid = rigid_pair(self.case, mesh, G) if name == 'C1' else None
        self.slices = []
        from pinned import CASES
        if CASES[name].get('slice_axis'):
            from nonlinear import to_real
            ax = self.case.gens_cs[0][0]
            # the slice: the rotation about the pinned 2-fold axis, in the mesh frame
            from symmetry import rot3, to_quat_vec
            from geometry import qconj
            t = rot3(qconj(self.case.g0), to_quat_vec(ax))         # the axis after orientation (quaternion coords)
            Xs = [self.rot.apply(c, P) for c in 'xyz']
            # quaternion coords (i, j, k) <-> Condon-Shortley (z, y, x)
            v = t[2] * Xs[0] + t[1] * Xs[1] + t[0] * Xs[2]
            self.slices = [to_real(v)]

    def branch(self, targets, on_point, log=lambda s: None):
        return Branch(self.st, self.case, self.lam0, self.Q, self.vol, slices=self.slices, log=log).run(targets, on_point=on_point)
