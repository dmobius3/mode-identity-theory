"""The registered cases, as the terms state them (registration/m8_16_task_details.md: THE CASES, FROZEN VALUES and THE
RUN; BOUNDARY.md's amendment 4; DRIVER_PLAN.md v2).

For every case but C1 the expected values are derived here from the signature, (k, r_u) and the frozen slow spectrum,
as the terms' 'Where the expected columns come from' derives them:
  - V0 has dimension k + r_u, with A of rank r_u on it and A^2 = 0, and k chains;
  - n(L) = n_-; k_r, k_c and k_i^- count the real pairs, the quartets and the Krein-negative pairs, with multiplicity;
  - K = k_r + 2 k_c + 2 k_i^-, n(D) = n(L) - K, and the type is Hyperbolic exactly when k_r + k_c > 0.
C1's are Theorem D's, as D6 registered them. write_guard.py serializes CASES into run/FROZEN.json, and build_dry.py
writes the dry run's GO cases into run/DRY.json; the driver reads only those files.
"""
import math
import os
import sys
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from instrument import branches as br, certified  # noqa: E402

LAM0 = {'R2': 63.0, 'R3': 8.0, 'R4': 48.0, 'R5': 48.0}
LEVEL = {'R2': 7, 'R3': 2, 'R4': 6, 'R5': 6}
CUTOFFS = [16, 24, 32]
SAMPLE = [0.25, 0.5, 1.0, 2.0]
C1_EPS, C1_CUTOFFS = [0.5, 1.0, 2.0], [16, 24, 32, 40]
S_R5 = Fr(9, 16)
BAR = 0.05                       # the leading-order bar, K3 to K5
ORDER = ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5', 'P5', 'T1/R4', 'T1/R5', 'T4/R4', 'T4/R5', 'T2/R4', 'T2/R5', 'T3/R4',
         'T3/R5', 'T5/R2']


def _nu5():
    a, b, c = 418161601, 6989958976, 28677390336
    d = math.sqrt(b * b - 4 * a * c)
    return sorted([(-b + d) / (2 * a), (-b - d) / (2 * a)])


# The frozen slow spectra for unit u in R4's h normalization: (class, Krein sign, tau, multiplicity). An imaginary pair
# sits at +-i eps kappa s tau, a real pair at +-eps kappa s tau, a quartet at eps kappa s (+-tau, +-conj(tau)).
SPECTRA = {
    'coherent': [('imag', 1, t, 1) for t in (Fr(28, 143), Fr(56, 429), Fr(140, 99), Fr(112, 39), Fr(896, 1287))],
    'weight72': [('imag', 1, t, 1) for t in (Fr(112, 143), Fr(168, 143), Fr(336, 143), Fr(504, 143), Fr(560, 143))],
    'octahedron': [('real', None, math.sqrt(250880 / 552123), 3)],
    'pyramid': [('imag', -1, 0.0622348691, 1), ('complex', None, complex(0.0417352860, 0.0609168609), 1),
                ('imag', 1, 1.0951854883, 1)],
    'v2': [('imag', -1, Fr(56, 1287), 1)] + [('imag', 1, t, 1) for t in (Fr(112, 143), Fr(112, 117), Fr(224, 143),
                                                                         Fr(560, 429))],
    'prism': [('imag', 1, math.sqrt(5770240 / 7913763), 1), ('imag', 1, math.sqrt(19066880 / 278420571), 2)],
    'hexagon': [('imag', -1, math.sqrt(90160 / 61347), 1), ('imag', -1, math.sqrt(501760 / 552123), 2)],
    'outside3': [('imag', 1, 1.01209160489, 1), ('imag', -1, 0.310692742362, 1), ('imag', -1, 0.139251832964, 1),
                 ('imag', -1, 0.00573685922309, 1)],
    'line72_32': [('imag', -1, math.sqrt(153664 / 20449), 1)] + [('imag', -1, math.sqrt(-x), 1) for x in _nu5()],
}
Q4_T4 = 1 + float(certified.R6_924) / 1287          # Q = 1 + 924 r_6 / 1287 in R4 (dev/seed_check.py, claim 4)


def ladder(last_k, eps_max=None):
    """M8.15's grid, eps_k = 0.25 * 2^(k/2) for k = 0..last_k, with eps_max appended when it is not a grid value."""
    pts = [0.25 * 2 ** (k / 2) for k in range(last_k + 1)]
    if eps_max is not None and abs(pts[-1] - eps_max) > 1e-9 * eps_max:
        pts.append(eps_max)
    return pts


def _points(eps_list, withheld_k=()):
    return [dict(eps=e, read=k not in withheld_k) for k, e in enumerate(eps_list)]


def _derive(sig, k, r, spectrum):
    n_minus = sig[0]
    kr = sum(m for c, _, _, m in spectrum if c == 'real')
    kc = sum(m for c, _, _, m in spectrum if c == 'complex')
    ki = sum(m for c, s, _, m in spectrum if c == 'imag' and s == -1)
    K = kr + 2 * kc + 2 * ki
    return dict(dim=k + r, ranks=[r, 0], chains=k, type='Hyperbolic' if kr + kc else 'Elliptic',
                idx=[n_minus, n_minus - K, K], kr=kr, kc=kc, ki=ki)


def _case(role, slot, orbit, Q, sig, k, r, points, cutoffs=None, m815=None):
    spectrum = SPECTRA[orbit]
    d = dict(role=role, slot=slot, level=LEVEL[slot], lam0=LAM0[slot], orbit=orbit, Q=Q, sig=list(sig), k=k, r=r,
             s=S_R5 if slot == 'R5' else Fr(1), spectrum=spectrum, points=points, cutoffs=cutoffs or CUTOFFS, m815=m815)
    d.update(_derive(sig, k, r, spectrum))
    if not 0 <= d['idx'][1] <= r:               # n(D) counts chains with partners: 0 <= n(D) <= r_u
        raise ValueError(f'inconsistent indices for {orbit}: {d["idx"]}')
    return d


R4_LADDER, R5_LADDER, T5_LADDER = ladder(16, 72.0), ladder(14, 32.0), ladder(17)
CASES = {
    'C1': dict(role='control', slot='R3', level=2, lam0=8.0, orbit='theoremD', Q=Fr(1), sig=None, k=4, r=2, s=Fr(1),
               spectrum=[], points=_points(C1_EPS), cutoffs=C1_CUTOFFS, m815=None, dim=6, ranks=[1, 0], chains=5,
               type='Elliptic', idx=[0, 0, 0], kr=0, kc=0, ki=0),
    'C2a': _case('control', 'R4', 'coherent', Fr(1288, 1287), (0, 0, 10), 3, 1, _points(SAMPLE)),
    'C2b': _case('control', 'R2', 'weight72', Fr(144, 143), (0, 0, 10), 5, 1, _points(SAMPLE)),
    'C3': _case('control', 'R4', 'octahedron', Fr(175, 143), (6, 0, 3), 4, 4, _points(SAMPLE)),
    'C2a/R5': _case('R5gate', 'R5', 'coherent', Fr(2289, 2288), (0, 0, 10), 3, 1, _points(SAMPLE)),
    'P5': _case('pyramid', 'R4', 'pyramid', Fr(77, 65), (5, 0, 4), 4, 2, _points(SAMPLE)),
    'T1/R4': _case('row', 'R4', 'v2', Fr(147, 143), (2, 0, 8), 3, 1, _points(SAMPLE)),
    'T1/R5': _case('row', 'R5', 'v2', Fr(581, 572), (2, 0, 8), 3, 1, _points(SAMPLE)),
    'T4/R4': _case('row', 'R4', 'outside3', Q4_T4, (7, 0, 2), 4, 2, _points(SAMPLE)),
    'T4/R5': _case('row', 'R5', 'outside3', (9 * Q4_T4 + 7) / 16, (7, 0, 2), 4, 2, _points(SAMPLE)),
    'T2/R4': _case('row', 'R4', 'prism', Fr(5831, 5031), (3, 0, 6), 4, 4, _points(R4_LADDER, (12, 13)), m815='T2_R4'),
    'T2/R5': _case('row', 'R5', 'prism', Fr(609, 559), (3, 0, 6), 4, 4, _points(R5_LADDER), m815='T2_R5'),
    'T3/R4': _case('row', 'R4', 'hexagon', Fr(1750, 1287), (9, 0, 0), 4, 4, _points(R4_LADDER, (14,)), m815='T3_R4'),
    'T3/R5': _case('row', 'R5', 'hexagon', Fr(2751, 2288), (9, 0, 0), 4, 4, _points(R5_LADDER, (12,)), m815='T3_R5'),
    'T5/R2': _case('row', 'R2', 'line72_32', Fr(22, 13), (9, 0, 0), 6, 4, _points(T5_LADDER, (15,)), m815='T5_R2'),
}
# the dry run's ladder segment on a control (DRIVER_PLAN.md v2): C2a on M8.15's grid to eps = 2, eps = 0.707 withheld
DRY_LADDER = dict(CASES['C2a'], role='dryladder', points=_points(ladder(6), (3,)), m815='C2a_R4')


def admission(name):
    """The case label the guard admits a case under: the dry ladder runs as C2a, C1 as Theorem D's R3 case."""
    return {'C1': 'theoremD:R3', 'C2a:ladder': 'C2a'}.get(name, name)


def _num(x):
    if isinstance(x, Fr):
        return dict(frac=f'{x.numerator}/{x.denominator}', value=float(x))
    if isinstance(x, complex):
        return dict(re=x.real, im=x.imag)
    return dict(value=float(x))


def serialize(name, case):
    """A case as FROZEN.json and DRY.json hold it: every expectation, its representative and its points."""
    if name == 'C1':
        rep = {1: 1.0, 0: complex(0.6, 0.3), -1: complex(0, -0.4)}      # branches.seed_state's generic member
    else:
        rep = br.representative('C2a' if name == 'C2a:ladder' else name)
    out = {k: v for k, v in case.items() if k not in ('Q', 's', 'spectrum')}
    out.update(Q=_num(case['Q']), s=_num(case['s']),
               spectrum=[dict(cls=c, sign=s_, tau=_num(t), mult=m) for c, s_, t, m in case['spectrum']],
               representative={str(m): [complex(v).real, complex(v).imag] for m, v in rep.items()},
               admission=admission(name))
    return out
