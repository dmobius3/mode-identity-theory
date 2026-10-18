#!/usr/bin/env python3
"""Step 1 of the pre-freeze build: the seeds (registration/m8_16_task_details.md, BEFORE THE FREEZE; BOUNDARY.md's
amendments 2 and 3 and their note). Case: seedcheck.

Usage: seed_check.py MIT_REPO
  MIT_REPO: a checkout of mode-identity-theory, read at the commits instrument/certified.py records.

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
     seed_state refuses every sealed seed while no freeze exists.
  4. The check at N = 16, for all 15 seeds (C1, C2a, C2b, C3, C2a/R5 and the 10 sealed): Q(u) within 1e-12 relative of
     its exact value; the lowest level's criticality residual at most 1e-12; and (k, r_u) as section IV gives them.
     Exact values, read from section IV's tables at the page commit:
       R4: Q = 1 + 924 r_6 / 1287, which must reproduce the published 1288/1287, 175/143, 77/65, 147/143, 5831/5031
           and 1750/1287, and gives T4's from its entry;
       R5: Q = (9 Q4 + 7)/16, which must reproduce the published 581/572, 609/559, 2751/2288 and T4's
           1.104176947003101 (to 1e-15), and gives 2289/2288 for C2a/R5 (EXPECTED_R5.md);
       R2: section IV's Q column, 144/143 (C2b) and 22/13 (T5);
       C1: Q = 1 and (k, r_u) = (4, 2), the orbit's (Theorem B; D6's report).
  5. The scope (the note to amendments 2 and 3). Throughout claim 4 sentinels make newton.solve, Functional.grad,
     hess_apply, hess_parts and hess_dense, linear.first_order and linear.record, and branches.continue_to raise. None
     fires: no Newton step is taken and no Hessian, slow matrix, L or A is formed at any seed.
  6. The instrument's own guard (UB, after step 1's review). In a process that has not required seedcheck,
     sealed_seed_for_check refuses all 10 sealed seeds while linear.first_order runs, its green parent (a subprocess
     under case C2a). In this seedcheck process every solver path refuses with PermissionError: newton.solve,
     Functional.grad, hess_apply, hess_parts and hess_dense, linear.first_order and linear.record, and
     branches.continue_to. The arm: the same eight calls, in the C2a subprocess, never refuse on the guard.
A failed claim is recorded as failed before any correction (UA); a correction goes into a constructor, never into an
expected value.
"""
import ast
import hashlib
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
from instrument import basis, functional as fn, newton, linear, branches as br, certified, su2, devtools  # noqa: E402

N = 16
SEEDS = ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5'] + list(br.SEALED)
ORBIT_ROW = {'C2a': 'coherent', 'C2a/R5': 'coherent', 'C3': 'octahedron', 'P5': 'pyramid', 'T1': 'v_2', 'T2': 'prism',
             'T3': 'hexagon', 'T4': 'third outside orbit', 'C2b': 'weight 7/2', 'T5': 'line {7/2, −3/2}'}
PUBLISHED_R4 = {'C2a': Fr(1288, 1287), 'C3': Fr(175, 143), 'P5': Fr(77, 65), 'T1': Fr(147, 143), 'T2': Fr(5831, 5031),
                'T3': Fr(1750, 1287)}
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
        slot = br.SEALED[name][0] if name in br.SEALED else br.CASES[name][1]
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
        slot = br.SEALED[name][0] if name in br.SEALED else br.CASES[name][1]
        n0 = br.SEALED[name][1] if name in br.SEALED else br.CASES[name][2]
        B = basis.Basis(slot, N)
        u = br.sealed_seed_for_check(name, B) if name in br.SEALED else br.seed_state(name, B)
        comps = br.representative(name)
        norm = sqrt(sum(abs(c) ** 2 for c in comps.values()))
        want = np.zeros(B.m, dtype=complex)
        for m, c in comps.items():
            l = n0 / 2 - m
            hits = [j for j, (nn, i, kk) in enumerate(B.index) if nn == n0 and i == 0 and kk == int(round(l))]
            assert len(hits) == 1 and abs(l - round(l)) < 1e-12
            want[hits[0]] = c / norm
        worst = max(worst, np.abs(u - want).max())
        if name in br.SEALED:
            try:
                br.seed_state(name, B)
                problems.append(f'{name}: seed_state did not refuse it')
            except PermissionError:
                refused += 1
    return worst <= 1e-15 and refused == len(br.SEALED) and not problems, worst, refused, problems


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
            names = [s for s in SEEDS if (br.SEALED[s][0] if s in br.SEALED else br.CASES[s][1]) == slot]
            if not names:
                continue
            B = basis.Basis(slot, N)
            Fn = fn.Functional(B)
            K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
            saved = install_sentinels()
            for name in names:
                u = br.sealed_seed_for_check(name, B) if name in br.SEALED else br.seed_state(name, B)
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
import sys
sys.path.insert(0, ROOT)
import numpy as np
from instrument import basis, branches as br, functional as fn, linear as ln, newton, devtools
devtools.require('C2a')
refused = 0
for name, (slot, n0) in br.SEALED.items():
    try:
        br.sealed_seed_for_check(name, basis.Basis(slot, 16))
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
'''


def claim6():
    import inspect
    src = 'ROOT = %r\n' % ROOT + inspect.getsource(guarded_calls).replace('def guarded_calls', 'def GUARDED_CALLS') + SUB
    p = subprocess.run([sys.executable, '-I', '-B', '-c', src], capture_output=True, text=True)
    fields = p.stdout.split()
    sub_ok = p.returncode == 0 and fields[:4] == [str(len(br.SEALED)), '4', '0', 'False']
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
    return sub_ok and here_ok, dict(subprocess=fields or p.stderr[-300:], here=here)


def main():
    repo = sys.argv[1]
    devtools.require('seedcheck')
    assert not os.path.exists(os.path.join(devtools.RUN_ROOT, 'run', 'FROZEN.json')), 'a freeze exists: this is the pre-freeze check'
    say(f'Step 1, the seeds, at N = {N}: {len(SEEDS)} seeds, {len(br.SEALED)} of them sealed; certified point from '
        f"{certified.SOURCE['commit'][:7]}, section IV from {certified.PAGE['commit'][:7]}")
    failed = 0
    ok1, w1, blocks = claim1()
    say(f'1. the basis convention: {"PASS" if ok1 else "FAIL"}  largest deviation {w1:.1e}, on n <= 32 and {blocks} blocks')
    ok2, parts = claim2(repo)
    say(f'2. the certified point: {"PASS" if ok2 else "FAIL"}  (source SHA-256, OUTSIDE strings, 924 r_6) = {parts}')
    ok3, w3, refused, problems = claim3()
    say(f'3. the constructors as data: {"PASS" if ok3 else "FAIL"}  largest deviation {w3:.1e}; seed_state refused '
        f'{refused} of {len(br.SEALED)} sealed seeds{"; " + "; ".join(problems) if problems else ""}')
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
        f' refused {sub[0] if sub else "?"} of {len(br.SEALED)}, first_order ran (size {sub[1] if len(sub) > 1 else "?"}),'
        f' guard refusals {sub[2] if len(sub) > 2 else "?"} of {len(GUARDED)} (the arm: none expected);'
        f' in this seedcheck process: {sum(v == "refused" for _, v in detail["here"])} of {len(GUARDED)} paths refused')
    if not ok6:
        say(f'   detail: {detail}')
    failed = sum(not x for x in (ok1, ok2, ok3, ok4, ok5, ok6))
    say(f'{failed} failed')
    path = os.path.join(HERE, 'seed_check.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'seedcheck',
                     [f"Step 1, the seeds: {'PASS' if not failed else 'FAIL'} ({failed} failed); {len(SEEDS)} seeds at N = {N},"
                      f" {len(br.SEALED)} sealed, each evaluated only for Q(u), criticality and (k, r_u).",
                      'Each outcome derived before the run (the script\'s docstring); expected values read from the Soft-Slot'
                      ' Branches\' section IV at the page commit instrument/certified.py records.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
