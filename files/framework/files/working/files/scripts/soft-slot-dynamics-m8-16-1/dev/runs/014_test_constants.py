#!/usr/bin/env python3
"""Every constant (M8.16.1's terms, THE TESTS BEFORE THE FREEZE, test 2; DRIVER_PLAN.md v2, The tests). Case: synthetic.

Usage: test_constants.py MIT_REPO TERMS_MD

It reads two texts: M8.16's governing terms, from MIT_REPO at deec830 (its SHA-256 must be 86992a5f...), and
M8.16.1's, TERMS_MD. It runs on a test FROZEN.json built by write_guard.py's own functions: the seventeen serialized
cases, frozen_values() and the pinned values file's record.

Claims, derived before the run:
  1. Forward (UA). Every numeric item of both texts' FROZEN VALUES is one of three kinds:
     (a) a literal scoring or guard constant: the value the text states equals the one the code reads, located by
         name, by a function's default, or by its occurrences on an anchored line of a named function, and FROZEN.json
         holds it, equal;
     (b) an exact or algorithmically derived value, reproduced by its calculation: a tau from its tau squared, a rounded
         root, the grid, the weights at the nominal points, the pinned script's cutoffs and digits;
     (c) an explicitly unscored reported value, on the exclusion inventory with its reason: the INFERRED tables and
         lists, and the P5 values' provenance.
  2. Coverage. Every number in both sections is claimed by exactly one item, or lies in an excluded block, or is a
     section reference after a section sign, which is not a value. Every item's anchor occurs once in its section.
  3. Reverse (UB, UA). Every numeric literal, module-level constant and default in run/'s scoring code, cases.py,
     checks.py, seeds.py and driver.py, found by a scan of the code itself, independently of the items above, outside
     the structural contexts (subscripts and slice bounds, the exponents of squares and square roots, the numbers 0
     and +-1, range bounds), is on exactly one of the test's lists, each entry with its function, its line's anchor
     and its reason, and no entry is stale. The lists: registered (a FROZEN VALUES item, or a registered point of the
     sample); case data (THE CASES, serialized into FROZEN.json's cases); a formula's own constant; a lookup or float
     guard; an unscored report; a load-time check; and v4's: the scoring constants terms v3 states outside FROZEN
     VALUES, which go into v4's FROZEN VALUES. Check 4's floor, which FROZEN.json holds and v3 does not list, is v4's
     too. The lists are printed.
Arms, each of which must turn its claim red:
  A1. FROZEN.json without D's cut, M8.16's defect: claim 1 names the missing entry (UB).
  A2. FROZEN.json without K3's axis guard, M8.16's other: claim 1 names the missing entry (UB).
  A3. FROZEN.json without check 4's floor: claim 3's v4 item for it.
  A4. a registered literal changed, AXIS_MIN to 1e-7 in a temporary copy of checks.py: claim 1, by equality.
  A5. a new scoring tolerance put into a temporary copy of checks.py, with no FROZEN VALUES entry (UA): claim 3.
"""
import ast
import copy
import hashlib
import importlib.util
import inspect
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools, linear as ln, convergence as cv, newton, branches as br  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402
import write_guard as wg  # noqa: E402

M816_TERMS = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16/run/m8_16_task_details.md'
M816_SHA = '86992a5f7a278d639042adad2576c666979fa20f3cb53071daa62c614e83d5cf'
SUP = str.maketrans('⁻⁰¹²³⁴⁵⁶⁷⁸⁹', '-0123456789')
TOKEN = re.compile(r'(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?×10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|\d+(?:\.\d+)?(?:/\d+)?%?)'
                   r'(?![A-Za-z0-9_])')
U = ln.U
out, failed = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def val(tok):
    """A token's value: 10⁻⁸, 2.22×10⁻¹⁶, 5%, 1/10, 28/143, 0.25, 40."""
    if '×10' in tok:
        m, e = tok.split('×10')
        return float(m) * 10.0 ** int(e.translate(SUP))
    if re.fullmatch(r'10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+', tok):
        return 10.0 ** int(tok[2:].translate(SUP))
    if tok.endswith('%'):
        return float(tok[:-1]) / 100
    if '/' in tok:
        a, b = tok.split('/')
        return Fr(int(a), int(b))
    return float(tok) if '.' in tok else int(tok)


def near(a, b, tol=None):
    a, b = complex(a), complex(b)
    return abs(a - b) <= (tol if tol is not None else 4 * U * max(abs(a), abs(b)))


def on_line(path, func, anchor, value):
    """How many times the numeric literal value occurs on the lines of func, in the module at path, that hold anchor."""
    src = open(path, encoding='utf-8').read()
    lines = src.splitlines()
    fn = next(n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef) and n.name == func)
    return sum(1 for n in ast.walk(fn) if isinstance(n, ast.Constant) and type(n.value) in (int, float)
               and n.value == value and anchor in lines[n.lineno - 1])


def default(fn, name):
    return inspect.signature(fn).parameters[name].default


def taus(name):
    return [m[2] for m in cs.SPECTRA[name]]


def ftaus(F, name):
    return [ck.num(m['tau']) for m in F['cases'][name]['spectrum']]


# ------------------------------------------------------------------------------------------------------------ claim 1
def items(F):
    """The forward items: (section, anchor, tokens, kind, check) with check() -> (ok, detail)."""
    RS = [n for n in cs.ORDER if cs.CASES[n]['slot'] == 'R5']
    V = cs.VALUES
    w = ck.lagrange0(list(ck.NEXT_EPS))
    nominal = [abs(wi) / x ** 2 for wi, x in zip(w, ck.NEXT_EPS)]
    t5 = sorted(round(math.sqrt(-x), 4) for x in cs._nu5())
    t5j = sorted(round(math.sqrt(-x), 4) for x in cs._nu5j())
    c3r = [complex(float(g['s'][0]), float(g['s'][1])) for g in V['cases']['C3R/R4']['cutoffs']['24']['groups']]
    A, B = 'a', 'b'
    f = lambda *ks: _get(F, ks)  # noqa: E731
    return [
        ('M8.16', 'In `R5` they are multiplied by 9/16', ['9/16'], A,
         lambda: (cs.S_R5 == Fr(9, 16) and all(F['cases'][n]['s'].get('frac') == '9/16' for n in RS), cs.S_R5)),
        ('M8.16', '`τ = 28/143, 56/429, 140/99, 112/39, 896/1287`', ['28/143', '56/429', '140/99', '112/39', '896/1287'], A,
         lambda: (taus('coherent') == [Fr(28, 143), Fr(56, 429), Fr(140, 99), Fr(112, 39), Fr(896, 1287)]
                  and ftaus(F, 'C2a') == [float(t) for t in taus('coherent')], 'C2a')),
        ('M8.16', '`τ = 112/143, 168/143, 336/143, 504/143, 560/143`', ['112/143', '168/143', '336/143', '504/143', '560/143'], A,
         lambda: (taus('weight72') == [Fr(112, 143), Fr(168, 143), Fr(336, 143), Fr(504, 143), Fr(560, 143)]
                  and ftaus(F, 'C2b') == [float(t) for t in taus('weight72')], 'C2b')),
        ('M8.16', '`ν = 250880/552123`', ['250880/552123'], B,
         lambda: (near(taus('octahedron')[0] ** 2, 250880 / 552123) and ftaus(F, 'C3') == taus('octahedron'), 'C3')),
        ('M8.16', '`τ_in = 0.0622348691`, Krein −; a quartet at `τ = 0.0417352860 + 0.0609168609 i`; `τ = 1.0951854883`',
         ['0.0622348691', '0.0417352860', '0.0609168609', '1.0951854883'], A,
         lambda: (taus('pyramid') == [0.0622348691, complex(0.0417352860, 0.0609168609), 1.0951854883]
                  and ftaus(F, 'P5') == taus('pyramid'), 'P5')),
        ('M8.16', '`τ = 56/1287`, Krein −; `112/143, 112/117, 224/143, 560/429`', ['56/1287', '112/143', '112/117', '224/143',
                                                                                  '560/429'], A,
         lambda: (taus('v2') == [Fr(56, 1287), Fr(112, 143), Fr(112, 117), Fr(224, 143), Fr(560, 429)]
                  and ftaus(F, 'T1/R4') == [float(t) for t in taus('v2')], 'T1')),
        ('M8.16', '`τ² = 5770240/7913763`; `19066880/278420571` twice', ['5770240/7913763', '19066880/278420571'], B,
         lambda: (near(taus('prism')[0] ** 2, 5770240 / 7913763) and near(taus('prism')[1] ** 2, 19066880 / 278420571)
                  and ftaus(F, 'T2/R4') == taus('prism'), 'T2')),
        ('M8.16', '`τ² = 90160/61347`; `501760/552123` twice', ['90160/61347', '501760/552123'], B,
         lambda: (near(taus('hexagon')[0] ** 2, 90160 / 61347) and near(taus('hexagon')[1] ** 2, 501760 / 552123)
                  and ftaus(F, 'T3/R4') == taus('hexagon'), 'T3')),
        ('M8.16', '`τ ≈ 1.01209160489`, Krein +; `0.310692742362, 0.139251832964, 0.00573685922309`',
         ['1.01209160489', '0.310692742362', '0.139251832964', '0.00573685922309'], A,
         lambda: (taus('outside3') == [1.01209160489, 0.310692742362, 0.139251832964, 0.00573685922309]
                  and ftaus(F, 'T4/R4') == taus('outside3'), 'T4')),
        ('M8.16', '`τ² = 153664/20449`', ['153664/20449'], B,
         lambda: (near(taus('line72_32')[0] ** 2, 153664 / 20449) and ftaus(F, 'T5/R2') == taus('line72_32'), 'T5')),
        ('M8.16', '`418161601ν² + 6989958976ν + 28677390336`', ['418161601', '6989958976', '28677390336'], A,
         lambda: (all(on_line(cs.__file__, '_nu5', '_roots(', v) == 1 for v in (418161601, 6989958976, 28677390336)),
                  '_nu5')),
        ('M8.16', 'so `τ ≈ 2.6886` and `3.0802`', ['2.6886', '3.0802'], B, lambda: (t5 == [2.6886, 3.0802], t5)),
        ('M8.16', 'with `u = 2.22×10⁻¹⁶`', ['2.22×10⁻¹⁶'], A,
         lambda: (near(U, 2.22e-16, 0.005e-16) and f('values', 'calibration', 'u') == U, U)),
        ('M8.16', 'with `κ = 2` and `m₀ = 0.2`, and its gray zone from `margin/G` to `G·margin`, with `G = 3`', ['2', '0.2', '3'], A,
         lambda: ((ln.KAPPA, ln.M0, ln.GRAY) == (2, 0.2, 3) and (f('values', 'calibration', 'kappa'), f('values', 'calibration', 'm0'),
                                                              f('values', 'calibration', 'G')) == (2, 0.2, 3), (ln.KAPPA, ln.M0, ln.GRAY))),
        ('M8.16', '`κ_d = 10`', ['10'], A, lambda: (ln.KAPPA_D == 10 == f('values', 'calibration', 'kappa_d'), ln.KAPPA_D)),
        ('M8.16', '`κ_L = 200`, capped at `10⁻⁴`', ['200', '10⁻⁴'], A,
         lambda: ((ln.KAPPA_L, ln.LEAK_CAP) == (200, 1e-4) == (f('values', 'calibration', 'kappa_L'),
                                                             f('values', 'calibration', 'leak_cap')), (ln.KAPPA_L, ln.LEAK_CAP))),
        ('M8.16', '`1000 u‖L‖`, with its gray zone to `G_L = 10`', ['1000', '10'], A,
         lambda: (near(ln.L_CUT / U, 1000) and ln.G_L == 10 and near(f('values', 'calibration', 'L_cut_over_u'), 1000)
                  and f('values', 'calibration', 'G_L') == 10, (ln.L_CUT / U, ln.G_L))),
        ('M8.16', "`D`'s cut `10⁻⁸ ‖B‖`", ['10⁻⁸'], A,
         lambda: (on_line(ln.__file__, 'record', 'inertia(Dm, ', 1e-8) == 1 and f('values', 'calibration', 'D_cut') == 1e-8,
                  'linear.record')),
        ('M8.16', 'acceptance at `10⁻¹⁵`, the halving rule\'s threshold at `10⁻⁸`, the secant to `10⁻⁶` within 8 iterations, and '
                  'the seed check at `10⁻¹²`', ['10⁻¹⁵', '10⁻⁸', '10⁻⁶', '8', '10⁻¹²'], A,
         lambda: (default(newton.solve, 'accept_rel') == 1e-15 and on_line(newton.__file__, 'solve', 'if r < ', 1e-8) == 1
                  and default(br.continue_to, 'tol') == 1e-6 and default(br.continue_to, 'max_secant') == 8
                  and on_line(dr.__file__, 'run_case', 'accepted = abs(', 1e-6) == 1
                  and all(on_line(dr.__file__, fn, 'seed_ok = abs(', 1e-12) == 2 for fn in ('run_case', 'run_c1'))
                  and f('values', 'solve') == dict(accept_rel=1e-15, halving=1e-8, secant=1e-6, secant_iterations=8,
                                                  seed_check=1e-12), 'newton, branches, driver')),
        ('M8.16', '- 5% against leading order;', ['5%'], A,
         lambda: (ck.BAR == cs.BAR == 0.05 == f('values', 'checks', 'bar'), (ck.BAR, cs.BAR))),
        ('M8.16', '- the overlaps 0.9 and 0.1;', ['0.9', '0.1'], A,
         lambda: (on_line(ck.__file__, 'k3', "ov['xy'] >= ", 0.9) == 1 and on_line(ck.__file__, 'k3', "ov['xy'] >= ", 0.1) == 1
                  and (f('values', 'checks', 'overlap_xy'), f('values', 'checks', 'overlap_z')) == (0.9, 0.1), 'checks.k3')),
        ('M8.16', "the identity guard at `10⁻²`, and K3's axis guard at `10⁻⁶`", ['10⁻²', '10⁻⁶'], A,
         lambda: ((ck.IDENTITY, ck.AXIS_MIN) == (1e-2, 1e-6) == (f('values', 'checks', 'identity'),
                                                                 f('values', 'checks', 'axis')), (ck.IDENTITY, ck.AXIS_MIN))),
        ('M8.16', 'the separation factor 1/10, with the projector\'s checks: the span at `10⁻⁶`, the left residual at `10⁴ u`, the '
                  'conditioning at `10⁻²/u`, and `P X = X` at `10⁻⁶`', ['1/10', '10⁻⁶', '10⁴', '10⁻²', '10⁻⁶'], A,
         lambda: (cv.FACTOR == 0.1 and cv.SPAN_MIN == 1e-6 and near(cv.LEFT_MAX / U, 1e4) and near(cv.COND_MAX * U, 1e-2)
                  and cv.IDEM_MAX == 1e-6 and (f('values', 'checks', 'factor'), f('values', 'checks', 'span'),
                                              f('values', 'checks', 'idempotence')) == (0.1, 1e-6, 1e-6)
                  and near(f('values', 'checks', 'left'), 1e4) and near(f('values', 'checks', 'conditioning'), 1e-2),
                  'convergence')),
        ('M8.16', '`ε_k = 0.25 × 2^{k/2}`', ['0.25', '2', '2'], B,
         lambda: (cs.ladder(6) == [0.25 * 2 ** (k / 2) for k in range(7)] and cs.SAMPLE == [cs.ladder(6)[k] for k in (0, 2, 4, 6)],
                  'cases.ladder')),
        ('M8.16', '`N = 16, 24` and 32, with C1 also at 40', ['16', '24', '32', '40'], A,
         lambda: (cs.CUTOFFS == [16, 24, 32] == f('values', 'cutoffs') and cs.C1_CUTOFFS == [16, 24, 32, 40]
                  == f('values', 'c1', 'cutoffs'), cs.C1_CUTOFFS)),
        ('M8.16.1', '`τ = 0.0355667254 + 0.00986952877 i`; `τ = 0.453830235`, Krein −; `τ = 1.00180626`',
         ['0.0355667254', '0.00986952877', '0.453830235', '1.00180626'], B,
         lambda: (near(c3r[0], complex(0.0355667254, 0.00986952877), math.hypot(0.5e-10, 0.5e-11)) and near(c3r[1].imag, 0.453830235, 0.5e-9)
                  and near(c3r[2].imag, 1.00180626, 0.5e-8) and ftaus(F, 'C3R/R4') == taus('c3ray'), 'the values file')),
        ('M8.16.1', '`τ² = 15680/1859`', ['15680/1859'], B,
         lambda: (near(taus('line72_32j')[0] ** 2, 15680 / 1859) and ftaus(F, 'T5J/R2') == taus('line72_32j'), 'T5J')),
        ('M8.16.1', '`418161601ν² + 6605190592ν + 25491013632`', ['418161601', '6605190592', '25491013632'], A,
         lambda: (all(on_line(cs.__file__, '_nu5j', '_roots(', v) == 1 for v in (418161601, 6605190592, 25491013632)),
                  '_nu5j')),
        ('M8.16.1', 'so `τ ≈` 2.5899, 2.9042 and 3.0147', ['2.5899', '2.9042', '3.0147'], B,
         lambda: (sorted(t5j + [round(math.sqrt(15680 / 1859), 4)]) == [2.5899, 2.9042, 3.0147], t5j)),
        ('M8.16.1', 'check i at every case, exact where the representative is algebraic and at 50 digits at T4', ['50'], B,
         lambda: (V['environment']['dps'] == 50, V['environment']['dps'])),
        ('M8.16.1', "check vi's coincidence at 24 and 32", ['24', '32'], B,
         lambda: (V['cutoffs'] == [16, 24, 32] and all(c['checks']['D'] for c in V['cases'].values()), V['cutoffs'])),
        ('M8.16.1', 'The values at `N = 16`, and T5J\'s, come with the pinned script', ['16'], B,
         lambda: (V['cutoffs'][0] == 16 and all('16' in c['cutoffs'] for c in V['cases'].values()), V['cutoffs'][0])),
        ('M8.16.1', "- the ceiling's factors, 0.1 and 10⁻³;", ['0.1', '10⁻³'], A,
         lambda: (ck.CEILING == (0.1, 1e-3) and f('values', 'next_order', 'ceiling') == [0.1, 1e-3], ck.CEILING)),
        ('M8.16.1', "- the resolution test's tenth, with its weights", [], A,
         lambda: (ck.RESOLUTION == 0.1 == f('values', 'next_order', 'resolution'), ck.RESOLUTION)),
        ('M8.16.1', 'with its weights 128/3, 8 and 1/3;', ['128/3', '8', '1/3'], B,
         lambda: (all(near(a, b) for a, b in zip(nominal, (128 / 3, 8, 1 / 3)))
                  and f('values', 'next_order', 'nominal_weights') == nominal, nominal)),
        ('M8.16.1', "- the extrapolation's points, 0.25, 0.5 and 1.", ['0.25', '0.5', '1'], A,
         lambda: (ck.NEXT_EPS == (0.25, 0.5, 1.0) and f('values', 'next_order', 'points') == [0.25, 0.5, 1.0], ck.NEXT_EPS)),
        ('M8.16.1', 'These include the 5% bar where it still applies', ['5%'], A,
         lambda: (ck.BAR == 0.05 == f('values', 'checks', 'bar'), ck.BAR)),
    ]


# the excluded blocks (c): (section, the first line's anchor, the last line's anchor, the reason)
EXCLUDED = [
    ('M8.16', "- **P5's values** are the continuum's", "- **P5's values** are the continuum's", "the P5 values' provenance: "
     "the overlaps of M8.15.x's survey, as its REGISTER_2.md reads them; read by no check"),
    ('M8.16', '- **The predicted modes at `ε = 0.25`', '| T5 | `R2` | 0.00931', 'INFERRED: the smallest predicted modes and '
     'their margins, read from the frozen spectra with ‖A‖ ≈ N(N+2); read by no check'),
    ('M8.16.1', '**Their smallest predicted modes**', '- T5J at 6.03×10⁻³', 'INFERRED: as M8.16\'s table; read by no check'),
    ('M8.16.1', '| case | groups, by ascending modulus', '| C3R | +0.0540938', 'INFERRED: the bench\'s preview of the pinned '
     'values; the pinned file governs, and FROZEN.json holds it'),
]


def _get(F, ks):
    for k in ks:
        F = F[k]
    return F


def section(text, head):
    i = text.index(head)
    return text[i:text.index('\n## ', i + 1)]


def claim1_2(F, texts):
    secs = {'M8.16': section(texts['M8.16'], '## FROZEN VALUES\n'),
            'M8.16.1': section(texts['M8.16.1'], '## FROZEN VALUES: WHAT IS NEW')}
    bad1, bad2, claimed = [], [], {k: [] for k in secs}
    for sec, anchor, toks, kind, check in items(F):
        s = secs[sec]
        if s.count(anchor) != 1:
            bad2.append(f'{sec}: the anchor {anchor[:50]!r} occurs {s.count(anchor)} times')
            continue
        i = s.index(anchor)
        got = [m.group(1) for m in TOKEN.finditer(anchor) if anchor[max(0, m.start() - 2):m.start()] != '§ ']
        if got != toks:
            bad2.append(f'{sec}: {anchor[:50]!r} holds {got}, not {toks}')
        claimed[sec].append((i, i + len(anchor)))
        if kind == 'c':
            continue
        try:
            ok, detail = check()
        except KeyError as e:
            ok, detail = False, f'FROZEN.json lacks {e.args[0]!r}'                # named, never a traceback (UB)
        if not ok:
            bad1.append(f'{sec} ({kind}) {anchor[:60]!r}: {detail}')
    for sec, first, last, _ in EXCLUDED:
        s = secs[sec]
        i = s.index(first)
        j = s.index(last, i)
        claimed[sec].append((i, s.index('\n', j)))
    loose = []
    for sec, s in secs.items():
        for m in TOKEN.finditer(s):
            if s[max(0, m.start() - 2):m.start()] == '§ ':
                continue
            hits = sum(a <= m.start() < b for a, b in claimed[sec])
            if hits != 1:
                loose.append(f"{sec}: {m.group(1)!r} at {s[max(0, m.start() - 30):m.start()]!r}, claimed {hits} times")
    return bad1, bad2 + loose


# ------------------------------------------------------------------------------------------------------------ claim 3
REG, CASE, FORM, LOOK, UNSC, LOAD, V4 = ('registered', 'case data', "a formula's own constant", 'a lookup or float guard',
                                         'an unscored report', 'a load-time check', "v4's FROZEN VALUES")
LISTS = [
    # (module, function, the line's anchor, value or None for every literal on the line, list, reason)
    ('cases', '<module>', 'LAM0 = {', None, CASE, "each slot's lam0, THE CASES"),
    ('cases', '<module>', 'LEVEL = {', None, CASE, "each slot's lowest level, THE CASES"),
    ('cases', '<module>', 'CUTOFFS = [16, 24, 32]', None, REG, 'the cutoffs'),
    ('cases', '<module>', 'SAMPLE = [0.25, 0.5, 1.0, 2.0]', None, REG, 'the sample, the grid at k = 0, 2, 4 and 6'),
    ('cases', '<module>', 'C1_EPS, C1_CUTOFFS = ', None, REG, "C1's points and cutoffs, with C1 also at 40"),
    ('cases', '<module>', 'S_R5 = Fr(9, 16)', None, REG, 'the R5 factor, 9/16'),
    ('cases', '<module>', 'BAR = 0.05', None, REG, 'the leading-order bar'),
    ('cases', '_roots', 'd = math.sqrt(b * b - 4 * a * c)', None, FORM, 'the quadratic formula'),
    ('cases', '_roots', 'return sorted([(-b + d) / (2 * a)', None, FORM, 'the quadratic formula'),
    ('cases', '_nu5', 'return _roots(', None, REG, "T5's slow polynomial"),
    ('cases', '_nu5j', 'return _roots(', None, REG, "T5J's slow polynomial"),
    ('cases', '<module>', "    'coherent': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'weight72': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'octahedron': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'pyramid': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "                ('imag', 1, 1.0951854883, 1)],", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'v2': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "Fr(560, 429))],", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'prism': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'hexagon': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'outside3': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "('imag', -1, 0.00573685922309, 1)],", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'line72_32': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', "    'line72_32j': [", None, REG, 'the frozen spectra'),
    ('cases', '<module>', 'Q4_T4 = 1 + float(certified.R6_924) / 1287', None, CASE, "T4's Q in R4, THE CASES"),
    ('cases', 'ladder', 'pts = [0.25 * 2 ** (k / 2)', None, REG, 'the grid'),
    ('cases', 'ladder', '> 1e-9 * eps_max', None, LOOK, 'whether eps_max is already a grid value'),
    ('cases', '_derive', 'K = kr + 2 * kc + 2 * ki', None, FORM, 'K counts each quartet and Krein-negative pair twice'),
    ('cases', '<module>', 'R4_LADDER, R5_LADDER, T5_LADDER = ', None, CASE, "the ladders' last k and eps_max, THE CASES"),
    ('cases', '<module>', "    'C1': dict(", None, CASE, "C1's columns, THE CASES"),
    ('cases', '<module>', 'spectrum=[], points=_points(C1_EPS)', None, CASE, "C1's columns, THE CASES"),
    ('cases', '<module>', ': _case(', None, CASE, "each case's columns, THE CASES"),
    ('cases', '_written', '>= 16:', None, LOAD, 'the tie: a literal printed to 16 digits is a floating-point value'),
    ('cases', '_written', 'return 0.5 * 10 ** -len(', None, LOAD, "the tie: half a unit in a literal's last digit"),
    ('cases', '_tie', "z = tc * (1j if cls == 'imag' else 1) * fac", None, FORM, 'the imaginary unit'),
    ('cases', '_tie', '+ 4 * EPS * abs(s)', None, LOAD, "the tie: a few units of double precision"),
    ('cases', 'serialize', 'rep = {1: 1.0, 0: complex(0.6, 0.3)', None, CASE, "C1's generic member, branches.seed_state's"),
    ('checks', '<module>', 'BAR = 0.05', None, REG, 'the leading-order bar'),
    ('checks', '<module>', 'IDENTITY = 1e-2', None, REG, 'the identity guard'),
    ('checks', '<module>', 'AXIS_MIN = 1e-6', None, REG, "K3's axis guard"),
    ('checks', '<module>', 'FRACTION = 1e-6', None, UNSC, "the rule's retired fraction, reported beside it"),
    ('checks', '<module>', 'NEXT_EPS = (0.25, 0.5, 1.0)', None, REG, "the extrapolation's points"),
    ('checks', '<module>', 'CEILING = (0.1, 1e-3)', None, REG, "the ceiling's factors"),
    ('checks', '<module>', 'RESOLUTION = 0.1', None, REG, "check 2's tenth"),
    ('checks', '<module>', 'FLOOR = 0.1', None, V4, "check 4's floor: FROZEN.json holds it, and terms v3 does not list it"),
    ('checks', '<module>', 'TWO_TERM = 0.01', None, UNSC, 'the two-term residual is reported beside 1%'),
    ('checks', 'predicted', 'kappa = 1 / (8 * math.sqrt', None, FORM, 'kappa = 1/(8 sqrt(lam0) Q), the Result\'s'),
    ('checks', 'predicted', 'lam = 1j * eps * kappa', None, FORM, 'the imaginary unit'),
    ('checks', 'slow_band', 'return 2 * max(', None, V4, "K2's slow band, twice the largest predicted mode, THE CHECKS"),
    ('checks', 'reading', 'if not band / 2 > ln.GRAY', None, V4, "the band-edge guard's half, THE CONVERGENCE RULE"),
    ('checks', 'real_orthonormal', 'def real_orthonormal(V, rel=1e-6)', None, V4, "K3's spans: the orthonormal cut"),
    ('checks', 'real_orthonormal', 'C = (C + C.T) / 2', None, FORM, "a matrix's symmetric part"),
    ('checks', 'check_control', 'p25, p2 = ', None, REG, "K4's points, in the sample"),
    ('checks', 'check_control', 'ok25, w25, _ = leading(', None, REG, "K4's points, in the sample"),
    ('checks', 'check_control', '_, w2, _ = leading(', None, REG, "K4's points, in the sample"),
    ('checks', 'k3', 'eps = 0.25', None, REG, "K3's point, in the sample"),
    ('checks', 'k3', "ov['xy'] >= 0.9", None, REG, 'the overlaps'),
    ('checks', 'k3_probe', 'eps = 0.25', None, REG, "the probe's point, in the sample"),
    ('checks', 'check_pyramid_k4', 'converged(case_out, 0.25', None, REG, "K4's point, in the sample"),
    ('checks', 'check_pyramid_k4', 'key(0.25)', None, REG, "K4's point, in the sample"),
    ('checks', 'check_pyramid_k4', 'leading(p, case, 0.25', None, REG, "K4's point, in the sample"),
    ('checks', 'check_row_k5', 'key(0.25)', None, REG, "K5's point, in the sample"),
    ('checks', 'check_row_k5', 'for e in (0.5, 1.0, 2.0):', None, REG, "K5's reported points, in the sample"),
    ('checks', 'check_row_k5', 'converged(case_out, 0.25', None, REG, "K5's point, in the sample"),
    ('checks', '_classed', '< 1e-9', None, UNSC, "classing M8.15's values for K6's reported comparison"),
    ('checks', 'slow_compare', "abs(p['eps'] - eps) < 1e-9", None, LOOK, "M8.15's point at the same grid value"),
    ('checks', 'm815_point', "abs(p['eps'] - eps) < 1e-9", None, LOOK, "M8.15's point at the same grid value"),
    ('checks', 'm815_point', "abs(t['eps'] - eps) < 1e-9", None, LOOK, "M8.15's type at the same grid value"),
    ('checks', 'check_row_k6', 'if e <= 2 + 1e-12', 2, V4, "K6's agreement at every read point with eps at most 2, THE CHECKS"),
    ('checks', 'check_row_k6', 'if e <= 2 + 1e-12', 1e-12, LOOK, "a float guard on K6's boundary at 2"),
    ('checks', 'check_row_k6', "r['eps'] > 2 for r in rows", None, UNSC, 'the agreements above 2, reported'),
    ('seeds', '<module>', 'NEW = {', None, CASE, "the new seeds' slots and levels, THE CASES: WHAT IS ADDED"),
    ('seeds', '<module>', "REPS = {'C3R/R4':", None, CASE, "the C3 ray's representative, THE CASES: WHAT IS ADDED"),
    ('seeds', '<module>', "'T5J/R2': {3.5:", None, CASE, "T5J's representative, T5'S SECOND MEMBER"),
    ('driver', 'load', '> 1e-12', None, LOOK, "FROZEN.json's representative against the code's, the same numbers"),
    ('driver', 'k3_arrays', 'n2 = 2 * Fn.B.m', None, FORM, "a state's real and imaginary halves"),
    ('driver', 'read_point', 'np.zeros(2 * Fn.B.m)', None, FORM, "a state's real and imaginary halves"),
    ('driver', 'read_point', 'nA = np.linalg.norm(A, 2)', None, FORM, 'the spectral norm, of order 2'),
    ('driver', 'run_c1', 'abs(chk[\'Q\'] - 1) < 1e-12', None, REG, 'the seed check'),
    ('driver', 'run_c1', 'low = np.array([n == 2', None, CASE, "C1's lowest level, 2"),
    ('driver', 'run_c1', 'c, lam = np.sqrt(eps) * v, 8.0 + eps', None, CASE, "C1's lam0 in R3"),
    ('driver', 'run_c1', 'pred = [2 * omega, 2 * omega, np.sqrt(4 * omega', None, FORM, "Theorem D's frequencies, THE CHECKS"),
    ('driver', 'run_c1', 'ok = (res / size < 1e-15', 1e-15, V4, "C1's residual bound, THE CHECKS"),
    ('driver', 'run_c1', 'ok = (res / size < 1e-15', 1e-14, V4, "C1's off-level bound, THE CHECKS"),
    ('driver', 'run_c1', 'ok = (res / size < 1e-15', 3, FORM, "Theorem D's three frequencies"),
    ('driver', 'run_c1', 'ok = (res / size < 1e-15', 1e-10, V4, "C1's spectrum to 1e-10, THE CHECKS"),
    ('driver', 'run_c1', "and rec['blocks'] == 5", None, CASE, "C1's five chains, THE CHECKS"),
    ('driver', 'run_c1', 'along &= same and spread < 1e-12', None, V4, "C1's readings unchanged in N to 1e-12, THE CHECKS"),
    ('driver', 'run_case', "abs(chk['Q'] - Qx) / Qx < 1e-12", None, REG, 'the seed check'),
    ('driver', 'run_case', 'accepted = abs(res', None, REG, "the secant's 1e-6, the point's acceptance"),
    ('driver', 'run_case', 'abs(eps - 0.25) < 1e-12', 0.25, REG, "K3's point, in the sample"),
    ('driver', 'run_case', 'abs(eps - 0.25) < 1e-12', 1e-12, LOOK, "K3's point among the read points"),
    ('driver', 'main', 'sys.argv[i + 1:i + 4]', None, FORM, "the three cutoffs' arguments"),
]
SCORING = ('cases', 'checks', 'seeds', 'driver')


def structural(n, parents):
    """The scan's structural contexts: a subscript or slice; the exponent 2 or 0.5 of a power; 0 and +-1; range bounds."""
    p, v, me = parents.get(n), n.value, n
    if isinstance(p, ast.UnaryOp) and isinstance(p.op, ast.USub):
        me, p, v = p, parents.get(p), -v
    if isinstance(p, (ast.Subscript, ast.Slice)) or (isinstance(p, ast.Tuple) and isinstance(parents.get(p), ast.Subscript)):
        return True
    if isinstance(p, ast.BinOp) and isinstance(p.op, ast.Pow) and p.right is me and v in (2, 0.5):
        return True
    if v in (0, 1, -1):
        return True
    return isinstance(p, ast.Call) and getattr(p.func, 'id', None) == 'range'


def literals(path):
    """(function, value, line) for every numeric literal of the module outside the structural contexts."""
    src = open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    parents = {c: n for n in ast.walk(tree) for c in ast.iter_child_nodes(n)}

    def func_of(n):
        while n in parents:
            n = parents[n]
            if isinstance(n, ast.FunctionDef):
                return n.name
        return '<module>'
    lines = src.splitlines()
    return [(func_of(n), (-1 if isinstance(parents.get(n), ast.UnaryOp) and isinstance(parents[n].op, ast.USub) else 1) * n.value,
             lines[n.lineno - 1]) for n in ast.walk(tree) if isinstance(n, ast.Constant) and type(n.value) in (int, float, complex)
            and not structural(n, parents)]


def floor_held(F):
    """Check 4's floor, v4's item: FROZEN.json must hold it, equal to the code's."""
    return F['values']['next_order'].get('floor') == ck.FLOOR


def claim3(paths):
    """(unlisted, stale, by list): every literal on exactly one entry; every entry used."""
    used, unlisted, by, outside = {i: 0 for i in range(len(LISTS))}, [], {}, []
    for mod in SCORING:
        for fn, v, line in literals(paths[mod]):
            hits = [i for i, (m, f, a, x, _, _) in enumerate(LISTS) if m == mod and f == fn and a in line
                    and (x is None or x == v)]
            if len(hits) != 1:
                unlisted.append(f'{mod}.{fn}: {v!r} on {line.strip()[:70]!r} ({len(hits)} entries)')
                continue
            used[hits[0]] += 1
            by.setdefault(LISTS[hits[0]][4], []).append((mod, fn, v))
            if 'in the sample' in LISTS[hits[0]][5] and v not in cs.SAMPLE:
                outside.append(f'{mod}.{fn}: {v!r} is registered as a point in the sample, and is not in it')
    stale = [f'{LISTS[i][0]}.{LISTS[i][1]} {LISTS[i][2]!r}' for i, k in used.items() if k == 0]
    return unlisted, stale + outside, by


def main():
    devtools.require('synthetic')
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    repo, terms = sys.argv[1:3]
    raw = subprocess.run(['git', '-C', repo, 'show', f'deec830:{M816_TERMS}'], check=True, capture_output=True).stdout
    texts = {'M8.16': raw.decode('utf-8'), 'M8.16.1': open(terms, encoding='utf-8').read()}
    say("Every constant (M8.16.1's DRIVER_PLAN.md v2): both FROZEN VALUES against the code and a test FROZEN.json.")
    say(f"   M8.16's terms {hashlib.sha256(raw).hexdigest()}; M8.16.1's {devtools.sha256(terms)}")
    if hashlib.sha256(raw).hexdigest() != M816_SHA:
        raise SystemExit("M8.16's terms differ from its governing text")
    F = json.loads(json.dumps(dr.jsonable(dict(cases={n: cs.serialize(n, cs.CASES[n]) for n in cs.ORDER},
                                               values=wg.frozen_values(), next_order=wg.next_order_values(ROOT)))))
    paths = {m: os.path.join(HERE, f'{m}.py') for m in SCORING}
    bad1, bad2 = claim1_2(F, texts)
    n_items = len(items(F))
    say(f"1. {'PASS' if not bad1 else 'FAIL'}: the forward items, {n_items}, of kinds (a), (b) and (c)" +
        ''.join(f'\n      {b}' for b in bad1))
    say(f"2. {'PASS' if not bad2 else 'FAIL'}: coverage: every number in both sections claimed once" +
        ''.join(f'\n      {b}' for b in bad2[:12]))
    for sec, first, _, why in EXCLUDED:
        say(f'      excluded, {sec}: {first[:40]!r}: {why}')
    unlisted, stale, by = claim3(paths)
    v4 = sorted({(m, f, v) for m, f, v in by.get(V4, [])}, key=str)
    floor_in = floor_held(F)
    ok3 = not unlisted and not stale and floor_in
    say(f"3. {'PASS' if ok3 else 'FAIL'}: the reverse scan of {', '.join(SCORING)}: every literal on exactly one list, "
        f"no entry stale" + ''.join(f'\n      unlisted: {u}' for u in unlisted) + ''.join(f'\n      stale: {s}' for s in stale))
    for k in (REG, CASE, FORM, LOOK, UNSC, LOAD, V4):
        say(f'      {k}: {len(by.get(k, []))} literals')
    say("      for v4's FROZEN VALUES, the scoring constants terms v3 states outside it:")
    for m, f, v in v4:
        why = next(r for (mm, ff, _, x, lst, r) in LISTS if (mm, ff) == (m, f) and lst == V4 and (x is None or x == v))
        say(f'        {m}.{f}: {v!r}: {why}')
    say('      the non-FROZEN-VALUES lists, each with its reason:')
    for m, f, a, x, lst, why in LISTS:
        if lst not in (REG, V4):
            say(f"        [{lst}] {m}.{f} {a.strip()[:44]!r}{'' if x is None else f' {x!r}'}: {why}")

    say('arms, each of which must turn its claim red:')
    arms = []
    for label, path in (("A1. FROZEN.json without D's cut", ('values', 'calibration', 'D_cut')),
                        ("A2. FROZEN.json without K3's axis guard", ('values', 'checks', 'axis'))):
        G = copy.deepcopy(F)
        del _get(G, path[:-1])[path[-1]]
        lines = claim1_2(G, texts)[0]
        arms.append((label + f": claim 1 names it, {[b for b in lines if f'lacks {path[-1]!r}' in b][:1]}",
                     any(f'FROZEN.json lacks {path[-1]!r}' in b for b in lines)))
    G = copy.deepcopy(F)
    del G['values']['next_order']['floor']
    arms.append(("A3. FROZEN.json without check 4's floor", not floor_held(G)))
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        src = open(paths['checks'], encoding='utf-8').read()
        p4 = os.path.join(tmp, 'checks_a4.py')
        with open(p4, 'w', encoding='utf-8') as f_:
            f_.write(src.replace('AXIS_MIN = 1e-6 ', 'AXIS_MIN = 1e-7 ', 1))
        spec = importlib.util.spec_from_file_location('checks_a4', p4)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        saved = ck.AXIS_MIN
        ck.AXIS_MIN = mod.AXIS_MIN
        try:
            arms.append(('A4. AXIS_MIN changed to 1e-7 in a copy of checks.py', bool(claim1_2(F, texts)[0])))
        finally:
            ck.AXIS_MIN = saved
        p5 = os.path.join(tmp, 'checks.py')
        anchor = "            fails = abs(off - x['c3hat']) > tol\n"
        if src.count(anchor) != 1:
            raise SystemExit('the A5 anchor moved')
        with open(p5, 'w', encoding='utf-8') as f_:
            f_.write(src.replace(anchor, "            fails = abs(off - x['c3hat']) > 1.07 * tol\n", 1))
        arms.append(('A5. a new scoring tolerance, 1.07, in a copy of checks.py', bool(claim3(dict(paths, checks=p5))[0])))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for label, red in arms:
        say(f"   {label}: {'RED' if red else 'GREEN'}")
    n_fail = bool(bad1) + bool(bad2) + (not ok3) + sum(not red for _, red in arms)
    say(f'{n_fail} failed')
    with open(os.path.join(HERE, 'test_constants.out'), 'w', encoding='utf-8') as f_:
        f_.write('\n'.join(out) + '\n')
    if n_fail:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
