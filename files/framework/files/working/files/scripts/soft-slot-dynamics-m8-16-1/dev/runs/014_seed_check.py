#!/usr/bin/env python3
"""M8.16.1's step 3: the seeds, M8.16's seed check (its dev/seed_check.py at MIT deec830, its step 1; BOUNDARY.md's
amendments 2 and 3 and their note) carried to M8.16.1's seventeen seeds (M8.16.1's terms, What development runs before
filing; DRIVER_PLAN.md v2, What the plan does not do). Case: seedcheck.

Usage: seed_check.py MIT_REPO
  MIT_REPO: a checkout of mode-identity-theory, read at the commits instrument/certified.py records.

The two new seeds, the C3 ray in R4 and T5's second member in R2, are built through run/seeds.py, since
instrument/branches.py knows only M8.16's; their exact values are section IV's rows for the C3 ray and for T5's line
{7/2, -3/2}, which T5J shares. It writes dev/seed_check.out, and dev/seed_check.json, the record the freeze block's
seeds line reads: each seed's values, and every module file under the tree that this process and its child process
loaded. It writes no development log entry: M8.16.1's are written by hand (DRIVER_PLAN.md v2, The development record).

Claims, derived before the run:
  1. The basis convention (synthetic). With J_a = gen_matrix(n, sigma_a)/2, for every n <= 32, and on every block of the
     N = 16 bases' right generators (J_a = (i/2) T_a) in R2, R3, R4 and R5: J_z e_l = ((n - 2l)/2) e_l and
     J_+ e_l = sqrt(l (n - l + 1)) e_{l-1}, each to 1e-12. So e_l is the Condon-Shortley |n/2, (n - 2l)/2>, with no
     phase (DERIVED from su2.gen_matrix's definition).
  2. The certified point. instrument/certified.py's OUTSIDE equals, string for string, the list in the Result's
     branches_check.py at the commit it records, whose SHA-256 equals the recorded one; its R6_924 equals the Soft-Slot
     Branches' section IV entry for the third outside orbit at the page commit it records.
  3. The constructors, as data. At N = 16, each seed's unit vector carries its representative's normalized
     Condon-Shortley components at the index of (n0, 0, l), l = n0/2 - m, and zeros elsewhere. T4's components equal
     M8.15's conversion of the same strings (pinned.py: w_m = sqrt((3+m)! (3-m)!) p_m, p in the order m = 3, ..., -3).
     seed_state refuses every sealed seed while no freeze exists, through seeds.seed_state for the two new ones.
  4. The check at N = 16, for all 17 seeds (C1, C2a, C2b, C3, C2a/R5 and the 12 sealed, M8.16's ten with C3R/R4 and
     T5J/R2): Q(u) within 1e-12 relative of its exact value; the lowest level's criticality residual at most 1e-12; and
     (k, r_u) as section IV gives them. Exact values, read from section IV's tables at the page commit:
       R4: Q = 1 + 924 r_6 / 1287, which must reproduce the published 1288/1287, 175/143, 77/65, 147/143, 5831/5031
           and 1750/1287, and the C3 ray's 77/65, and gives T4's from its entry;
       R5: Q = (9 Q4 + 7)/16, which must reproduce the published 581/572, 609/559, 2751/2288 and T4's
           1.104176947003101 (to 1e-15), and gives 2289/2288 for C2a/R5 (EXPECTED_R5.md);
       R2: section IV's Q column, 144/143 (C2b), and 22/13 for T5 and for T5J, on T5's line;
       C1: Q = 1 and (k, r_u) = (4, 2), the orbit's (Theorem B; D6's report).
  5. The scope (the note to amendments 2 and 3). Throughout claim 4 sentinels make newton.solve, Functional.grad,
     hess_apply, hess_parts and hess_dense, linear.first_order and linear.record, and branches.continue_to raise. None
     fires: no Newton step is taken and no Hessian, slow matrix, L or A is formed at any seed.
  6. The instrument's own guard (UB, after step 1's review). In a process that has not required seedcheck,
     sealed_seed_for_check refuses M8.16's 10 sealed seeds, and seeds.seed_for_check the two new ones, while
     linear.first_order runs, its green parent (a subprocess under case C2a). In this seedcheck process every solver path refuses with PermissionError: newton.solve,
     Functional.grad, hess_apply, hess_parts and hess_dense, linear.first_order and linear.record, and
     branches.continue_to. The arm: the same eight calls, in the C2a subprocess, never refuse on the guard.
  7. The new seeds' identity (UB). seeds.REPS equals, component for component, the representatives
     run/next_order_values.py computed C3R/R4's and T5J/R2's frozen values from. Each differs from the orbit whose Q and
     (k, r_u) it shares by its Majorana root multiplicities, read from those components: the C3 ray's double root
     against the pyramid's six simple roots, and T5J's seven simple roots against T5's double root. The Majorana
     polynomial is sum_m (-1)^(j - m) sqrt(binom(2j, j + m)) c_m z^(j + m), in which T5's reads z^7 - 7 z^2 and T5J's
     z^7 + 7i z^5 - 7 z^2 + i, as the terms' certificate gives them; a degree below 2j is a root at infinity.
     Its arms, each of which must turn it red: T5J's v_{3/2} component taken real in a copy of seeds.REPS; and T5's
     components read in T5J's place for the multiplicities.
A failed claim is recorded as failed before any correction (UA); a correction goes into a constructor, never into an
expected value.
"""
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr
from math import factorial, sqrt
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import basis, functional as fn, newton, linear, branches as br, certified, su2, devtools  # noqa: E402
import seeds as sd  # noqa: E402

N = 16
SEALED = dict(br.SEALED, **sd.NEW)
SEEDS = ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5'] + list(SEALED)
ORBIT_ROW = {'C2a': 'coherent', 'C2a/R5': 'coherent', 'C3': 'octahedron', 'P5': 'pyramid', 'T1': 'v_2', 'T2': 'prism',
             'T3': 'hexagon', 'T4': 'third outside orbit', 'C2b': 'weight 7/2', 'T5': 'line {7/2, −3/2}',
             'C3R': 'C3 ray', 'T5J': 'line {7/2, −3/2}'}
PUBLISHED_R4 = {'C2a': Fr(1288, 1287), 'C3': Fr(175, 143), 'P5': Fr(77, 65), 'T1': Fr(147, 143), 'T2': Fr(5831, 5031),
                'T3': Fr(1750, 1287), 'C3R': Fr(77, 65)}
PUBLISHED_R5 = {'T1': Fr(581, 572), 'T2': Fr(609, 559), 'T3': Fr(2751, 2288), 'T4': 1.104176947003101}
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True, capture_output=True, text=True).stdout


def section_iv(repo):
    """The two tables of section IV at the page commit: orbit -> (value column, (k, r_u)). R4/R5 rows give 924 r_6;
    R2 rows give Q."""
    page = git(repo, 'show', f"{certified.PAGE['commit']}:{certified.PAGE['path']}")
    rows = {}
    for ln in page.splitlines():
        if not ln.startswith('| ') or ln.startswith('| ---') or ln.startswith('| orbit'):
            continue
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if len(cells) < 5 or not re.fullmatch(r'\d+, \d+', cells[4]):
            continue
        name = re.sub(r'\$`\s*([^`]*)\s*`\$', r'\1', cells[0]).replace('coherent v_3', 'coherent').strip()
        k, r = (int(x) for x in cells[4].split(', '))
        rows.setdefault(name, (cells[2], (k, r)))
    return rows


def exact(value):
    v = value.rstrip('…').strip()
    return Fr(v) if re.fullmatch(r'\d+(/\d+)?', v) else float(v)


def expected(repo):
    rows = section_iv(repo)
    exp, fails = {}, []
    for name in SEEDS:
        if name == 'C1':
            exp[name] = (Fr(1), (4, 2))
            continue
        orbit = name.split('/')[0]
        slot = SEALED[name][0] if name in SEALED else br.CASES[name][1]
        val, kr = rows[ORBIT_ROW[orbit]]
        if slot == 'R2':
            q = exact(val)
        else:
            q4 = 1 + exact(val) / 1287
            if orbit in PUBLISHED_R4 and q4 != PUBLISHED_R4[orbit]:
                fails.append(f'{name}: 1 + 924 r_6/1287 = {q4} against the published {PUBLISHED_R4[orbit]}')
            q = q4 if slot == 'R4' else (9 * q4 + 7) / 16
            if slot == 'R5' and orbit in PUBLISHED_R5:
                pub = PUBLISHED_R5[orbit]
                ok = q == pub if isinstance(pub, Fr) else abs(float(q) - pub) <= 1e-15
                if not ok:
                    fails.append(f'{name}: (9 Q4 + 7)/16 = {float(q)!r} against the published {pub}')
        exp[name] = (q, kr)
    if exp['C2a/R5'][0] != Fr(2289, 2288):
        fails.append(f"C2a/R5: Q = {exp['C2a/R5'][0]} against EXPECTED_R5.md's 2289/2288")
    return exp, fails


def claim1():
    worst = 0.0
    def check(Jx, Jy, Jz, n):
        nonlocal worst
        l = np.arange(n + 1)
        Jp = Jx + 1j * Jy
        want_p = np.zeros((n + 1, n + 1))
        for ll in range(1, n + 1):
            want_p[ll - 1, ll] = sqrt(ll * (n - ll + 1))
        worst = max(worst, np.abs(Jz - np.diag((n - 2 * l) / 2)).max(), np.abs(Jp - want_p).max())
    for n in range(33):
        check(*(su2.gen_matrix(n, S) / 2 for S in (su2.SX, su2.SY, su2.SZ)), n)
    blocks = 0
    for slot in ('R2', 'R3', 'R4', 'R5'):
        B = basis.Basis(slot, N)
        T = fn.right_generators(B)
        col = 0
        for n in B.levels:
            for _ in B.A[n]:
                sl = slice(col, col + n + 1)
                check(*((0.5j) * T[a][sl, sl] for a in range(3)), n)
                col += n + 1
                blocks += 1
    return worst <= 1e-12, worst, blocks


def claim2(repo):
    src = git(repo, 'show', f"{certified.SOURCE['commit']}:{certified.SOURCE['path']}")
    sha_ok = hashlib.sha256(src.encode('utf-8')).hexdigest() == certified.SOURCE['sha256']
    i0 = src.index('OUTSIDE = [')
    i1 = src.index(']', i0) + 1
    strings_ok = ast.literal_eval(src[i0 + len('OUTSIDE = '):i1]) == certified.OUTSIDE
    rows = section_iv(repo)
    r_ok = rows['third outside orbit'][0].rstrip('…').strip() == certified.R6_924
    return sha_ok and strings_ok and r_ok, (sha_ok, strings_ok, r_ok)


def claim3():
    worst, refused, problems = 0.0, 0, []
    x = [float(s) for s in certified.OUTSIDE]
    p = [complex(x[a], x[7 + a]) for a in range(7)]
    m815 = {3 - a: sqrt(factorial(3 + (3 - a)) * factorial(3 - (3 - a))) * p[a] for a in range(7)}
    t4 = br.representative('T4/R4')
    worst = max(worst, max(abs(t4[m] - m815[m]) for m in m815))
    for name in SEEDS:
        if name == 'C1':
            continue
        slot = SEALED[name][0] if name in SEALED else br.CASES[name][1]
        n0 = SEALED[name][1] if name in SEALED else br.CASES[name][2]
        B = basis.Basis(slot, N)
        u = sd.seed_for_check(name, B) if name in SEALED else br.seed_state(name, B)
        comps = sd.representative(name)
        norm = sqrt(sum(abs(c) ** 2 for c in comps.values()))
        want = np.zeros(B.m, dtype=complex)
        for m, c in comps.items():
            l = n0 / 2 - m
            hits = [j for j, (nn, i, kk) in enumerate(B.index) if nn == n0 and i == 0 and kk == int(round(l))]
            assert len(hits) == 1 and abs(l - round(l)) < 1e-12
            want[hits[0]] = c / norm
        worst = max(worst, np.abs(u - want).max())
        if name in SEALED:
            try:
                sd.seed_state(name, B)
                problems.append(f'{name}: seed_state did not refuse it')
            except PermissionError:
                refused += 1
    return worst <= 1e-15 and refused == len(SEALED) and not problems, worst, refused, problems


class Sentinel(Exception):
    pass


def install_sentinels():
    targets = [(newton, 'solve'), (fn.Functional, 'grad'), (fn.Functional, 'hess_apply'), (fn.Functional, 'hess_parts'),
               (fn.Functional, 'hess_dense'), (linear, 'first_order'), (linear, 'record'), (br, 'continue_to')]
    saved = []
    for obj, attr in targets:
        saved.append((obj, attr, getattr(obj, attr)))
        label = f'{getattr(obj, "__name__", obj)}.{attr}'

        def raiser(*a, _label=label, **k):
            raise Sentinel(f'{_label} was called inside the seed check')
        setattr(obj, attr, raiser)
    return saved


def claim4(exp):
    rows, fails = [], 0
    saved = None
    try:
        for slot in ('R3', 'R4', 'R5', 'R2'):
            names = [s for s in SEEDS if (SEALED[s][0] if s in SEALED else br.CASES[s][1]) == slot]
            if not names:
                continue
            B = basis.Basis(slot, N)
            Fn = fn.Functional(B)
            K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
            saved = install_sentinels()
            for name in names:
                u = sd.seed_for_check(name, B) if name in SEALED else br.seed_state(name, B)
                chk = br.orbit_checks(Fn, u, K)
                q_exact, kr = exp[name]
                rel = abs(chk['Q'] - float(q_exact)) / float(q_exact)
                ok = rel <= 1e-12 and chk['crit'] <= 1e-12 and (chk['k'], chk['r']) == kr
                fails += not ok
                rows.append((name, slot, chk['Q'], q_exact, rel, chk['crit'], (chk['k'], chk['r']), kr, ok))
            for obj, attr, f in saved:
                setattr(obj, attr, f)
            saved = None
    finally:
        if saved:
            for obj, attr, f in saved:
                setattr(obj, attr, f)
    return fails == 0, rows


GUARDED = ['newton.solve', 'Functional.grad', 'Functional.hess_apply', 'Functional.hess_parts', 'Functional.hess_dense',
           'linear.first_order', 'linear.record', 'branches.continue_to']


def guarded_calls(newton_, fn_, linear_, br_):
    """Each guarded path, called with placeholder arguments: the guard is its first statement, so in a seedcheck
    process each raises PermissionError before reading them; elsewhere each fails on the placeholders instead."""
    return [lambda: newton_.solve(None, None, None, None, None), lambda: fn_.Functional.grad(None, None, None),
            lambda: fn_.Functional.hess_apply(None, None, None, None), lambda: fn_.Functional.hess_parts(None, None, None),
            lambda: fn_.Functional.hess_dense(None, None, None), lambda: linear_.first_order(None, None),
            lambda: linear_.record(None, None, None, None, None), lambda: br_.continue_to(None, None, None, None, None, None)]


SUB = r'''
import json, os, sys
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import numpy as np
from instrument import basis, branches as br, functional as fn, linear as ln, newton, devtools
import seeds as sd
devtools.require('C2a')
refused = 0
for name, (slot, n0) in br.SEALED.items():
    try:
        br.sealed_seed_for_check(name, basis.Basis(slot, 16))
    except PermissionError:
        refused += 1
for name, (slot, n0) in sd.NEW.items():
    try:
        sd.seed_for_check(name, basis.Basis(slot, 16))
    except PermissionError:
        refused += 1
A, Bm, W = ln.first_order(np.diag([1.0, 2.0]), 0.5)
guard_refusals = 0
for call in GUARDED_CALLS(newton, fn, ln, br):
    try:
        call()
    except PermissionError:
        guard_refusals += 1
    except Exception:
        pass
print(refused, A.shape[0], guard_refusals, devtools.SEEDCHECK)
r = os.path.realpath(ROOT) + os.sep
print(json.dumps(sorted({os.path.relpath(os.path.realpath(m.__file__), r) for m in list(sys.modules.values())
                         if getattr(m, '__file__', None) and os.path.realpath(m.__file__).startswith(r)})))
'''


def claim6():
    import inspect
    src = 'ROOT = %r\n' % ROOT + inspect.getsource(guarded_calls).replace('def guarded_calls', 'def GUARDED_CALLS') + SUB
    p = subprocess.run([sys.executable, '-I', '-B', '-c', src], capture_output=True, text=True)
    lines = p.stdout.strip().splitlines()
    fields = lines[0].split() if lines else []
    children = json.loads(lines[1]) if len(lines) > 1 else []
    sub_ok = p.returncode == 0 and fields[:4] == [str(len(SEALED)), '4', '0', 'False']
    here = []
    for label, call in zip(GUARDED, guarded_calls(newton, fn, linear, br)):
        try:
            call()
            here.append((label, 'ran'))
        except PermissionError:
            here.append((label, 'refused'))
        except Exception as e:
            here.append((label, f'{type(e).__name__}'))
    here_ok = all(v == 'refused' for _, v in here) and devtools.SEEDCHECK
    return sub_ok and here_ok, dict(subprocess=fields or p.stderr[-300:], here=here, children=children)


def claim7(arm=None):
    """Claim 7 (the module docstring): (holds, the new seeds' agreement with the pinned script, the multiplicities).
    arm 'real' takes T5J's v_{3/2} component real in a copy of seeds.REPS; arm 'swap' reads T5's components in T5J's
    place for the multiplicities."""
    import sympy as sp
    src = open(os.path.join(ROOT, 'run', 'next_order_values.py'), encoding='utf-8').read()
    node = next(n.value for n in ast.parse(src).body if isinstance(n, ast.Assign)
                and any(getattr(t, 'id', None) == 'ALGEBRAIC' for t in n.targets))
    ns = {'sqrt': sp.sqrt, 'R': sp.Rational, 'I': sp.I}
    reps = {e.elts[0].value: eval(compile(ast.Expression(e.elts[2]), 'next_order_values.py', 'eval'), {'__builtins__': {}}, ns)
            for e in node.elts}
    same = {}
    for name in sd.NEW:
        theirs = {float(m): complex(sp.N(c, 30)) for m, c in reps[name].items()}
        mine = dict(sd.REPS[name])
        if arm == 'real' and name == 'T5J/R2':
            mine[1.5] = abs(mine[1.5])
        tol = 4 * np.finfo(float).eps * max(abs(x) for x in theirs.values())
        same[name] = (set(theirs) == {float(m) for m in mine}
                      and all(abs(complex(mine[m]) - theirs[float(m)]) <= tol for m in mine))
    z = sp.symbols('z')

    def multiplicities(comps, j2):
        j = sp.Rational(j2, 2)
        P = sp.Poly(sp.expand(sum((-1) ** int(j - sp.Rational(m)) * sp.sqrt(sp.binomial(j2, j + sp.Rational(m))) * c
                                  * z ** int(j + sp.Rational(m)) for m, c in comps.items())), z, extension=True)
        out = [k for f, k in P.sqf_list()[1] for _ in range(f.degree())] + ([j2 - P.degree()] if j2 > P.degree() else [])
        return sorted(out, reverse=True)
    mult = {name: multiplicities(reps['T5/R2' if arm == 'swap' and name == 'T5J/R2' else name], j2)
            for name, j2 in (('C3R/R4', 6), ('P5', 6), ('T5J/R2', 7), ('T5/R2', 7))}
    want = {'C3R/R4': [2, 1, 1, 1, 1], 'P5': [1] * 6, 'T5J/R2': [1] * 7, 'T5/R2': [2, 1, 1, 1, 1, 1]}
    return all(same.values()) and mult == want, same, mult


def main():
    repo = sys.argv[1]
    devtools.require('seedcheck')
    assert not os.path.exists(os.path.join(devtools.RUN_ROOT, 'run', 'FROZEN.json')), 'a freeze exists: this is the pre-freeze check'
    say(f"M8.16.1's step 3, the seeds, at N = {N}: {len(SEEDS)} seeds, {len(SEALED)} of them sealed; certified point "
        f"from {certified.SOURCE['commit'][:7]}, section IV from {certified.PAGE['commit'][:7]}")
    failed = 0
    ok1, w1, blocks = claim1()
    say(f'1. the basis convention: {"PASS" if ok1 else "FAIL"}  largest deviation {w1:.1e}, on n <= 32 and {blocks} blocks')
    ok2, parts = claim2(repo)
    say(f'2. the certified point: {"PASS" if ok2 else "FAIL"}  (source SHA-256, OUTSIDE strings, 924 r_6) = {parts}')
    ok3, w3, refused, problems = claim3()
    say(f'3. the constructors as data: {"PASS" if ok3 else "FAIL"}  largest deviation {w3:.1e}; seed_state refused '
        f'{refused} of {len(SEALED)} sealed seeds{"; " + "; ".join(problems) if problems else ""}')
    exp, exp_fails = expected(repo)
    for f in exp_fails:
        say(f'   expectation: {f}')
    try:
        ok4, rows = claim4(exp)
        ok5 = True
        sentinel = None
    except Sentinel as e:
        ok4, rows, ok5, sentinel = False, [], False, str(e)
    ok4 = ok4 and not exp_fails
    say(f'4. the check: {"PASS" if ok4 else "FAIL"}')
    for name, slot, q, qx, rel, crit, kr, krx, ok in rows:
        say(f"   {name:7s} {slot}: Q {q:.15f} against {qx if isinstance(qx, Fr) else repr(qx)} (rel {rel:.1e}); criticality"
            f" {crit:.1e}; (k, r_u) {kr} against {krx}: {'PASS' if ok else 'FAIL'}")
    say(f'5. the scope: {"PASS" if ok5 else "FAIL"}  {"no sentinel fired" if ok5 else sentinel}')
    ok6, detail = claim6()
    sub = detail['subprocess']
    say(f'6. the instrument\'s guard: {"PASS" if ok6 else "FAIL"}  outside seedcheck (case C2a): sealed_seed_for_check'
        f' refused {sub[0] if sub else "?"} of {len(SEALED)}, first_order ran (size {sub[1] if len(sub) > 1 else "?"}),'
        f' guard refusals {sub[2] if len(sub) > 2 else "?"} of {len(GUARDED)} (the arm: none expected);'
        f' in this seedcheck process: {sum(v == "refused" for _, v in detail["here"])} of {len(GUARDED)} paths refused')
    if not ok6:
        say(f'   detail: {detail}')
    ok7, same, mult = claim7()
    say(f"7. the new seeds' identity: {'PASS' if ok7 else 'FAIL'}  seeds.REPS against run/next_order_values.py's "
        f"representatives {same}; the Majorana root multiplicities: C3R/R4 {mult['C3R/R4']} against P5's {mult['P5']},"
        f" T5J/R2 {mult['T5J/R2']} against T5/R2's {mult['T5/R2']}")
    arms7 = {a: not claim7(a)[0] for a in ('real', 'swap')}
    ok7 = ok7 and all(arms7.values())
    say(f"   its arms: T5J's v_3/2 component taken real {'RED' if arms7['real'] else 'GREEN'}; T5's components in T5J's"
        f" place {'RED' if arms7['swap'] else 'GREEN'}")
    failed = sum(not x for x in (ok1, ok2, ok3, ok4, ok5, ok6, ok7))
    root = os.path.realpath(ROOT) + os.sep
    loaded = sorted({os.path.relpath(os.path.realpath(m.__file__), root) for m in list(sys.modules.values())
                     if getattr(m, '__file__', None) and os.path.realpath(m.__file__).startswith(root)
                     and m is not sys.modules['__main__']})                 # the script itself is the record's 'script'
    record = dict(script=dict(path=os.path.relpath(os.path.abspath(__file__), ROOT),
                              sha256=hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()),
                  N=N, failed=failed, identity=dict(representatives=same, multiplicities=mult),
                  seeds=[dict(name=name, slot=slot, Q=q, Q_exact=str(qx), crit=crit, k=kr[0], r=kr[1], ok=ok)
                         for name, slot, q, qx, rel, crit, kr, krx, ok in rows],
                  loaded=loaded, children=detail['children'])
    say(f"the record: {len(loaded)} files loaded here and {len(detail['children'])} in the child process, under the tree")
    say(f'{failed} failed')
    path = os.path.join(HERE, 'seed_check.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(os.path.join(HERE, 'seed_check.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(record, indent=1) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
