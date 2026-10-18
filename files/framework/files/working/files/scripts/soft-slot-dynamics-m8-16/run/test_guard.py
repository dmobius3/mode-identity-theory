#!/usr/bin/env python3
"""The guard's tests (DRIVER_PLAN.md v4, § The guard's tests; UB's item 12 and UA's edited-entry test; the units on
step 3, DEVLOG 234). Case: synthetic.

Usage: test_guard.py

Every test runs on a temporary tree, a copy of instrument/ and reference/m815/ with a synthetic run/ folder, through
devtools.RUN_ROOT; the target-record tests use a synthetic git repository. No test solves anything, and no test
constructs a sealed seed: the sealed refusals are read on the name alone.

Claims, derived before the run: each case below is refused, and each green parent proceeds.
  1. A case off the allowlist; R0, also when the test FROZEN.json lists it; a sealed name placed in DRY.json.
  2. On the frozen path, as in claim 8 (UB): with devtools.GO emptied and C2a entered in branches.SEALED, C2a without
     FROZEN.json, with a FREEZE file alone present, and with a FROZEN.json whose manifest SHA-256 or terms SHA-256 is
     wrong; and a FROZEN.json with a case entry edited and its embedded hashes left intact (UA). The green parent is C2a
     admitted through a valid test FROZEN.json that lists it. P5 keeps only its refusal on the name, in claim 1.
  3. A row before the gate record shows K1 to K4 passed; a gate record whose SHA-256 differs from the logged one; the
     dry gate record (incomplete).
  4. write_guard.py with FROZEN.json present, without a go, with a manifest that differs from run/MANIFEST_PIN, and
     with a target record whose blob id differs from the named one (synthetic git repository).
  5. frozen() with a target record whose SHA-256 differs from FROZEN.json's (synthetic file).
  6. The band-edge guard: a point whose band edge lies within the gray zone reads Unresolved.
  7. At a withheld point: first_order, record, summarize, inertia and spectrum_of_L refuse, while Newton's
     hess_dense stays open.
  8. The frozen path's own green parent (UB): with devtools.GO emptied and C2a entered in branches.SEALED at its own
     slot and level, C2a is admitted by require and its seed built by seed_state through a valid test FROZEN.json
     that lists it, equal to its GO-path seed; both refuse once that file is removed.
  9. The resume (UA, UB), through driver.main in --dry mode on a temporary tree, with stand-in solvers that raise
     instead of solving. A fresh run records its tree's manifest in its log. The green parent, a clean interruption
     (completed cases that passed their checks, no gate record, the same tree), resumes and goes on to the next case.
     Refused: a resume on a changed manifest, and on a log that records none; a resume whose gate record names a stop.
     A resume whose completed control failed a check, with no gate record, stops at it as the first run would have,
     writing the gate record that names the failed check and solving nothing; a resume after that is refused.
 10. The stop's record (UB). With a control failed, the verdict is NOT QUALIFIED, naming the check; it is incomplete in a
     dry run, and at an interruption with nothing failed. The R5 rows' reason names the R5 control's failed check, or
     that it did not run. Under python -O, a real run given other cutoffs is refused, where an assert of the same form
     does not fire (the arm).
 11. python -O (UA, UB; DEVLOG 258). require refuses under -O, beside an assert that does not fire there (the arm).
     Under -O, each guard converted from an assert refuses its own mutation, beside its green parent: basis.Basis on
     R0; branches.expected_v0 on an EXPECTED_V0.md that differs from its logged version, and on a log that never logged
     it; driver.embeds on a higher basis whose leading part is reordered. log_run, in a temporary root, refuses an
     output whose kept copy exists, writing nothing, beside a green parent that writes; under -O it refuses before
     writing anything.
"""
import contextlib
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import basis, functional as fn, linear as ln, branches as br, convergence as cv, devtools  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402
import write_guard as wg  # noqa: E402

out, results = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def expect(label, fn_, refused=True):
    """Run fn_; record PASS when it raises PermissionError (or Withheld) as expected, or proceeds as expected."""
    try:
        fn_()
        got = False
    except (PermissionError, ck.Withheld):
        got = True
    ok = got == refused
    results.append((label, ok))
    say(f"   {'PASS' if ok else 'FAIL'}  {label}: {'refused' if got else 'proceeded'}")
    return ok


@contextlib.contextmanager
def tree(allow=('C2a',), targets=None, terms='synthetic terms\n'):
    """A temporary tree with a valid freeze: the copied instrument and controls' records, a synthetic run/ with the
    terms, the manifest pin, FROZEN.json listing `allow`, and its pin."""
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    old = devtools.RUN_ROOT
    try:
        shutil.copytree(os.path.join(ROOT, 'instrument'), os.path.join(tmp, 'instrument'),
                        ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(os.path.join(ROOT, 'reference', 'm815'), os.path.join(tmp, 'reference', 'm815'))
        os.makedirs(os.path.join(tmp, 'run'))
        with open(os.path.join(tmp, 'run', 'm8_16_task_details.md'), 'w', encoding='utf-8') as f:
            f.write(terms)
        _, msha = devtools.manifest(tmp)
        with open(os.path.join(tmp, 'run', 'MANIFEST_PIN'), 'w', encoding='utf-8') as f:
            f.write(msha + '\n')
        write_frozen(tmp, dict(allowlist=list(allow), order=list(allow), cases={}, manifest_sha256=msha,
                               terms_sha256=devtools.sha256(os.path.join(tmp, 'run', 'm8_16_task_details.md')),
                               targets=targets or [], go='test'))
        devtools.RUN_ROOT = tmp
        yield tmp
    finally:
        devtools.RUN_ROOT = old
        shutil.rmtree(tmp, ignore_errors=True)


def write_frozen(root, F, pin=True):
    text = json.dumps(F, indent=1) + '\n'
    with open(os.path.join(root, 'run', 'FROZEN.json'), 'w', encoding='utf-8') as f:
        f.write(text)
    if pin:
        with open(os.path.join(root, 'run', 'FROZEN_PIN'), 'w', encoding='utf-8') as f:
            f.write(hashlib.sha256(text.encode('utf-8')).hexdigest() + '\n')


def edit_frozen(root, change, repin=False):
    p = os.path.join(root, 'run', 'FROZEN.json')
    F = json.load(open(p, encoding='utf-8'))
    change(F)
    write_frozen(root, F, pin=repin)


def test1():
    say('1. off the allowlist, R0, and a sealed name in DRY.json:')
    with tree(allow=('C2a', 'R0')):
        expect('green parent: C2a, a GO case', lambda: devtools.require('C2a'), refused=False)
        expect('P5, off the allowlist', lambda: devtools.require('P5'))
        expect('R0, listed in the test FROZEN.json', lambda: devtools.require('R0'))
        expect('R0 as a slot-qualified name', lambda: devtools.require('T1/R0'))
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    old = dr.HERE
    try:
        D = json.load(open(os.path.join(HERE, 'DRY.json'), encoding='utf-8'))
        with open(os.path.join(tmp, 'DRY.json'), 'w', encoding='utf-8') as f:
            json.dump(D, f)
        dr.HERE = tmp
        expect('green parent: the real DRY.json', lambda: dr.load(True), refused=False)
        D['order'].append('P5')
        D['cases']['P5'] = dict(D['cases']['C2a'], admission='P5')
        with open(os.path.join(tmp, 'DRY.json'), 'w', encoding='utf-8') as f:
            json.dump(D, f)
        expect('a sealed name placed in DRY.json', lambda: dr.load(True))
    finally:
        dr.HERE = old
        shutil.rmtree(tmp, ignore_errors=True)


def test2():
    say('2. sealed admission without a valid freeze, on the frozen path (UB):')
    go, sealed = set(devtools.GO), dict(br.SEALED)
    try:
        devtools.GO.clear()
        br.SEALED['C2a'] = ('R4', 6)
        with tree(allow=('C2a',)) as t:
            expect('green parent: C2a, sealed for the test, listed in a valid test FROZEN.json (admission only; nothing'
                   ' is built)', lambda: devtools.require('C2a'), refused=False)
            os.remove(os.path.join(t, 'run', 'FROZEN.json'))
            expect('C2a without FROZEN.json', lambda: devtools.require('C2a'))
            open(os.path.join(t, 'FREEZE'), 'w').close()
            expect('C2a with a FREEZE file alone present', lambda: devtools.require('C2a'))
        with tree(allow=('C2a',)) as t:
            edit_frozen(t, lambda F: F.update(manifest_sha256='0' * 64), repin=True)
            expect('a FROZEN.json whose manifest SHA-256 is wrong', lambda: devtools.require('C2a'))
        with tree(allow=('C2a',)) as t:
            edit_frozen(t, lambda F: F.update(terms_sha256='0' * 64), repin=True)
            expect('a FROZEN.json whose terms SHA-256 is wrong', lambda: devtools.require('C2a'))
        with tree(allow=('C2a',)) as t:
            edit_frozen(t, lambda F: F['allowlist'].append('T1/R4'), repin=False)
            expect('a FROZEN.json with a case entry edited, its embedded hashes intact (UA)',
                   lambda: devtools.require('C2a'))
    finally:
        devtools.GO.clear()
        devtools.GO.update(go)
        br.SEALED.clear()
        br.SEALED.update(sealed)


def test3():
    say('3. the row gate:')
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        log = dict(completed={}, gate=None, events=[])
        expect('a row before any gate record', lambda: dr.row_gate(tmp, log))
        gate = dict(complete=True, instrument_ok=True)
        p = os.path.join(tmp, 'GATE.json')
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(gate, f)
        log['gate'] = dict(file='GATE.json', sha256=devtools.sha256(p))
        expect('green parent: a complete gate record with K1 to K4 passed', lambda: dr.row_gate(tmp, log),
               refused=False)
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(dict(gate, note='edited'), f)
        expect('a gate record whose SHA-256 differs from the logged one', lambda: dr.row_gate(tmp, log))
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(dict(complete=False, instrument_ok=None, absent=['P5']), f)
        log['gate']['sha256'] = devtools.sha256(p)
        expect('the dry gate record, incomplete', lambda: dr.row_gate(tmp, log))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def synthetic_repo():
    """A git repository holding one synthetic record, committed; returns (path, commit, file path, blob)."""
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    g = lambda *a: subprocess.run(['git', '-C', tmp, *a], check=True, capture_output=True, text=True).stdout.strip()
    g('init', '-q')
    g('config', 'user.email', 'test@example.invalid')
    g('config', 'user.name', 'guard test')
    with open(os.path.join(tmp, 'record.json'), 'w', encoding='utf-8') as f:
        f.write('{"synthetic": true}\n')
    g('add', 'record.json')
    g('commit', '-q', '-m', 'synthetic')
    commit = g('rev-parse', 'HEAD')
    blob = g('rev-parse', 'HEAD:record.json')
    return tmp, commit, 'record.json', blob


def test4():
    say('4. write_guard.py:')
    repo, commit, path, blob = synthetic_repo()
    try:
        for label, mutate, refused in (('green parent: a valid tree, the named blob', None, False),
                                       ('FROZEN.json already present', 'frozen', True),
                                       ('without a go', 'nogo', True),
                                       ('a manifest that differs from run/MANIFEST_PIN', 'manifest', True),
                                       ('a target record whose blob id differs from the named one', 'blob', True)):
            with tree() as t:
                os.remove(os.path.join(t, 'run', 'FROZEN.json'))
                os.remove(os.path.join(t, 'run', 'FROZEN_PIN'))
                rec = dict(name='SYN', path=path, commit=commit, blob='0' * 40 if mutate == 'blob' else blob,
                           file='reference/m815_targets/branch_SYN.json')
                with open(os.path.join(t, 'run', 'targets.json'), 'w', encoding='utf-8') as f:
                    json.dump(dict(records=[rec]), f)
                _, msha = devtools.manifest(t)
                with open(os.path.join(t, 'run', 'MANIFEST_PIN'), 'w', encoding='utf-8') as f:
                    f.write(msha + '\n')
                if mutate == 'frozen':
                    open(os.path.join(t, 'run', 'FROZEN.json'), 'w').close()
                if mutate == 'manifest':
                    with open(os.path.join(t, 'instrument', 'extra.py'), 'w', encoding='utf-8') as f:
                        f.write('# a file the pin did not see\n')
                go = '' if mutate == 'nogo' else 'test go'
                expect(label, lambda: wg.write(t, repo, go), refused=refused)
    finally:
        shutil.rmtree(repo, ignore_errors=True)


def test5():
    say('5. frozen() and the target records:')
    with tree() as t:
        os.makedirs(os.path.join(t, 'reference', 'm815_targets'))
        f_ = os.path.join(t, 'reference', 'm815_targets', 'branch_SYN.json')
        with open(f_, 'w', encoding='utf-8') as f:
            f.write('{"synthetic": true}\n')
        good = dict(name='SYN', file='reference/m815_targets/branch_SYN.json', sha256=devtools.sha256(f_))
        edit_frozen(t, lambda F: F.update(targets=[good]), repin=True)
        expect('green parent: a target record matching FROZEN.json', lambda: devtools.frozen(t), refused=False)
        edit_frozen(t, lambda F: F.update(targets=[dict(good, sha256='0' * 64)]), repin=True)
        expect("a target record whose SHA-256 differs from FROZEN.json's", lambda: devtools.frozen(t))


def test6():
    say('6. the band-edge guard:')
    hits = sorted(__import__('glob').glob(os.path.join(ROOT, 'dev', 'runs', '*_sep_controls_C2a_sample.json')))
    J = json.load(open(hits[-1], encoding='utf-8'))
    sums = [J[f'N{N}_eps0.5']['summary'] for N in (16, 24, 32)]
    top = J['N32_eps0.5']
    margin = top['summary']['margin']
    green = ck.reading(sums, top['eig'], top['lam'], margin, 16)
    ok_g = green['verdict'] == 'converged'
    results.append(('green parent: the saved C2a sample at eps 0.5 reads converged', ok_g))
    say(f"   {'PASS' if ok_g else 'FAIL'}  green parent: the saved C2a sample at eps 0.5 reads {green['verdict']}")
    forced = ck.reading(sums, [top['lam'] + 1e-14], top['lam'], margin, 0)
    ok_f = forced['verdict'] == 'Unresolved' and 'gray zone' in forced['reasons'][0]
    results.append(('a band edge forced into the gray zone reads Unresolved', ok_f))
    say(f"   {'PASS' if ok_f else 'FAIL'}  a band edge forced into the gray zone reads {forced['verdict']}: {forced['reasons']}")


def test7():
    say('7. the withheld point:')
    B = basis.Basis('R4', 6)
    Fn = fn.Functional(B)
    rng = np.random.default_rng(1)
    c = rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)
    calls = [('first_order', lambda: ln.first_order(None, None)), ('record', lambda: ln.record(None, None, None, None, None)),
             ('summarize', lambda: cv.summarize(None, None, None)), ('inertia', lambda: ln.inertia(np.eye(2))),
             ('spectrum_of_L', lambda: ck.spectrum_of_L(np.eye(2)))]
    with ck.withheld('test'):
        for label, call in calls:
            expect(f'{label} inside the withheld context', call)
        expect("Newton's hess_dense inside the withheld context stays open", lambda: Fn.hess_dense(c, 48.5),
               refused=False)
    expect('green parent: first_order outside it', lambda: ln.first_order(np.diag([1.0, 2.0]), 0.5), refused=False)
    expect('green parent: inertia outside it', lambda: ln.inertia(np.eye(2)), refused=False)
    expect('green parent: spectrum_of_L outside it', lambda: ck.spectrum_of_L(np.eye(2)), refused=False)


def test8():
    say("8. the frozen path's own green parent (UB):")
    go, sealed = set(devtools.GO), dict(br.SEALED)
    try:
        devtools.GO.clear()
        br.SEALED['C2a'] = ('R4', 6)
        B = basis.Basis('R4', 16)
        with tree(allow=('C2a',)) as t:
            expect('C2a admitted by require through a valid test FROZEN.json', lambda: devtools.require('C2a'),
                   refused=False)
            u = br.seed_state('C2a', B)
            want = np.zeros(B.m, dtype=complex)
            want[br.weight_index(B, 6, 3)] = 1.0
            ok = float(np.abs(u - want).max()) == 0.0
            results.append(("C2a's seed built by seed_state through the frozen path, equal to its GO-path seed", ok))
            say(f"   {'PASS' if ok else 'FAIL'}  C2a's seed built through the frozen path equals its GO-path seed")
            os.remove(os.path.join(t, 'run', 'FROZEN.json'))
            expect('require refuses C2a once FROZEN.json is removed', lambda: devtools.require('C2a'))
            expect('seed_state refuses C2a once FROZEN.json is removed', lambda: br.seed_state('C2a', B))
    finally:
        devtools.GO.clear()
        devtools.GO.update(go)
        br.SEALED.clear()
        br.SEALED.update(sealed)


def record(label, ok, detail):
    results.append((label, ok))
    say(f"   {'PASS' if ok else 'FAIL'}  {label}: {detail}")


class Solved(Exception):
    """Raised by the stand-in solvers: the run went on to solve a case."""


def stand_in_case(name, case, dry):
    raise Solved(name)


def stand_in_c1(case):
    raise Solved('C1')


@contextlib.contextmanager
def dry_tree():
    """A temporary tree (tree()) whose run/ holds the real DRY.json, with driver.main pointed at it in --dry mode, the
    stand-in solvers in place, and the dry claims' own log entry captured, not written."""
    saved = (dr.HERE, dr.run_case, dr.run_c1, devtools.log_run, list(sys.argv))
    with tree() as t:
        shutil.copy(os.path.join(HERE, 'DRY.json'), os.path.join(t, 'run', 'DRY.json'))
        try:
            dr.HERE = os.path.join(t, 'run')
            dr.run_case, dr.run_c1 = stand_in_case, stand_in_c1
            devtools.log_run = lambda *a, **k: None
            sys.argv[:] = ['driver.py', '--dry']
            yield t
        finally:
            dr.HERE, dr.run_case, dr.run_c1, devtools.log_run = saved[:4]
            sys.argv[:] = saved[4]


def seed_log(t, completed, manifest=True, stop=None):
    """A synthetic interrupted dry run on the tree t: each completed case's output (its DRY.json entry with the given
    checks), and RUNLOG.json recording them, the tree's manifest unless manifest is False, and a gate record naming
    `stop` if one is given."""
    outdir = os.path.join(t, 'run', 'dry')
    os.makedirs(outdir)
    D = json.load(open(os.path.join(t, 'run', 'DRY.json'), encoding='utf-8'))
    log = dict(completed={}, gate=None, events=[dict(t='test', event='dry run started')])
    for name, checks in completed.items():
        p = os.path.join(outdir, dr.safe(name) + '.json')
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(dict(case=D['cases'][name], checks=checks), f)
        log['completed'][name] = dict(files={os.path.basename(p): devtools.sha256(p)}, t='test')
    if manifest:
        log['manifest_sha256'] = devtools.manifest(t)[1]
    if stop:
        p = os.path.join(outdir, 'GATE.json')
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(dict(stop=stop, complete=False, instrument_ok=None), f)
        log['gate'] = dict(file='GATE.json', sha256=devtools.sha256(p), written='test')
    with open(os.path.join(outdir, 'RUNLOG.json'), 'w', encoding='utf-8') as f:
        json.dump(log, f)
    return outdir


def resumed():
    """driver.main in --dry mode: ('proceeded', the case it went on to solve), ('refused', why) or ('stopped', None)."""
    try:
        dr.main()
    except Solved as e:
        return 'proceeded', str(e)
    except PermissionError as e:
        return 'refused', str(e)
    return 'stopped', None


def test9():
    say('9. the resume (UA, UB):')
    C1, C2A = dict(K1=True, K4=True), dict(K1=True, K2=True, K4=True)
    with dry_tree() as t:
        got = resumed()
        log = json.load(open(os.path.join(t, 'run', 'dry', 'RUNLOG.json'), encoding='utf-8'))
        record("a fresh run records its tree's manifest in its log, then goes on to C1",
               got == ('proceeded', 'C1') and log.get('manifest_sha256') == devtools.manifest(t)[1], got)
    with dry_tree() as t:
        seed_log(t, {'C1': C1, 'C2a': C2A})
        got = resumed()
        record('green parent: a clean interruption, on the same tree, resumes and goes on to C2b',
               got == ('proceeded', 'C2b'), got)
    with dry_tree() as t:
        seed_log(t, {'C1': C1, 'C2a': C2A})
        with open(os.path.join(t, 'instrument', 'extra.py'), 'w', encoding='utf-8') as f:
            f.write('# a file the run did not start with\n')
        got = resumed()
        record('a resume on a changed manifest', got[0] == 'refused', got)
    with dry_tree() as t:
        seed_log(t, {'C1': C1, 'C2a': C2A}, manifest=False)
        got = resumed()
        record('a resume on a log that records no manifest', got[0] == 'refused', got)
    with dry_tree() as t:
        seed_log(t, {'C1': C1, 'C2a': C2A}, stop='C2a failed K4')
        got = resumed()
        record('a resume whose gate record names a stop', got[0] == 'refused', got)
    with dry_tree() as t:
        outdir = seed_log(t, {'C1': C1, 'C2a': dict(C2A, K4=False)})
        got = resumed()
        gate = json.load(open(os.path.join(outdir, 'GATE.json'), encoding='utf-8'))
        v = json.load(open(os.path.join(outdir, 'VERDICT.json'), encoding='utf-8'))
        record('a resume whose completed control failed a check, with no gate record, stops at it, solving nothing',
               got == ('stopped', None) and gate.get('stop') == 'C2a failed K4' and v['verdict'] == 'incomplete'
               and v['failed'] == ['C2a: K4'], (got, gate.get('stop'), v['verdict'], v['failed']))
        again = resumed()
        record('a resume after that stop', again[0] == 'refused', again)


def test10():
    say("10. the stop's record (UB):")
    R = {'C1': dict(case=dict(role='control', slot='R3'), checks=dict(K1=True, K4=True)),
         'C2a': dict(case=dict(role='control', slot='R4'), checks=dict(K1=True, K2=True, K4=False))}
    v = ck.verdict(R)
    record('a control failed in a real run: NOT QUALIFIED, naming the check',
           v['verdict'] == 'NOT QUALIFIED' and v['failing'] == ['K4'] and v['failed'] == ['C2a: K4'],
           (v['verdict'], v.get('failing'), v['failed']))
    v = ck.verdict(R, dry=True)
    record('the same in a dry run: incomplete', v['verdict'] == 'incomplete' and v['failed'] == ['C2a: K4'],
           (v['verdict'], v['failed']))
    R2 = dict(R, C2a=dict(R['C2a'], checks=dict(K1=True, K2=True, K4=True)))
    v = ck.verdict(R2)
    record('an interruption with nothing failed: incomplete', v['verdict'] == 'incomplete' and v['failed'] == [],
           (v['verdict'], v['failed']))
    f5 = ck.r5_failed(dict(R2, **{'C2a/R5': dict(case=dict(role='R5gate', slot='R5'), checks=dict(K1=True, K4=False))}))
    record("the R5 rows' reason names the R5 control's failed check", f5 == ['K4'], f5)
    f0 = ck.r5_failed(R2)
    record("or that it did not run", f0 == ['not run'], f0)
    p = subprocess.run([sys.executable, '-O', '-I', '-B', os.path.join(HERE, 'driver.py'), '--cutoffs', '12', '16',
                        '20'], capture_output=True, text=True)
    record('under python -O, a real run given other cutoffs is refused',
           p.returncode != 0 and 'refused: other cutoffs are for a dry plumbing pass only' in p.stderr,
           (p.returncode, p.stderr.strip().splitlines()[-1:]))
    arm = "dry = False\nassert dry, 'other cutoffs are for a dry plumbing pass only'\nprint('proceeded')"
    a = subprocess.run([sys.executable, '-O', '-I', '-B', '-c', arm], capture_output=True, text=True)
    record('the arm: under python -O, an assert of the same form does not fire',
           a.returncode == 0 and a.stdout.strip() == 'proceeded', a.stdout.strip())


def under_O(code):
    """A snippet under python -O -I -B with the bench on its path: (exit status, the last line of stderr, stdout)."""
    head = f'import sys\nsys.path.insert(0, {ROOT!r})\nsys.path.insert(0, {HERE!r})\n'
    p = subprocess.run([sys.executable, '-O', '-I', '-B', '-c', head + code], capture_output=True, text=True)
    return p.returncode, (p.stderr.strip().splitlines() or [''])[-1], p.stdout.strip()


def log_root():
    """A temporary root for log_run: a copy of instrument/, a two-entry DEVLOG.md and an empty dev/runs/."""
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    shutil.copytree(os.path.join(ROOT, 'instrument'), os.path.join(tmp, 'instrument'),
                    ignore=shutil.ignore_patterns('__pycache__'))
    os.makedirs(os.path.join(tmp, 'dev', 'runs'))
    with open(os.path.join(tmp, 'DEVLOG.md'), 'w', encoding='utf-8') as f:
        f.write('# test\n\n## 0. a\n\n## 1. b\n')
    with open(os.path.join(tmp, 'probe.out'), 'w', encoding='utf-8') as f:
        f.write('a new output\n')
    return tmp


def test11():
    say('11. python -O (UA, UB):')
    rc, err, _ = under_O("from instrument import devtools\ndevtools.require('synthetic')")
    record('require refuses under python -O', rc != 0 and 'refused under python -O' in err, err)
    rc, _, so = under_O("dry = False\nassert dry, 'other cutoffs are for a dry plumbing pass only'\nprint('proceeded')")
    record('the arm: an assert under python -O does not fire', rc == 0 and so == 'proceeded', so)
    rc, err, so = under_O("from instrument import basis\nbasis.Basis('R4', 8)\nprint('built')")
    record("green parent: basis.Basis('R4', 8) builds under -O", rc == 0 and so == 'built', so or err)
    rc, err, _ = under_O("from instrument import basis\nbasis.Basis('R0', 8)")
    record("basis.Basis('R0', 8) under -O", rc != 0 and 'R0 never runs' in err, err)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        for f_ in ('DEVLOG.md', 'EXPECTED_V0.md'):
            shutil.copy(os.path.join(ROOT, f_), tmp)
        call = f"from instrument import branches\nbranches.expected_v0({tmp!r})\nprint('read')"
        rc, err, so = under_O(call)
        record('green parent: expected_v0 on copies of the logged files, under -O', rc == 0 and so == 'read', so or err)
        with open(os.path.join(tmp, 'EXPECTED_V0.md'), 'a', encoding='utf-8') as f:
            f.write('\n')
        rc, err, _ = under_O(call)
        record('expected_v0 on an EXPECTED_V0.md that differs from its logged version, under -O',
               rc != 0 and 'differs from the version logged' in err, err)
        shutil.copy(os.path.join(ROOT, 'EXPECTED_V0.md'), tmp)
        with open(os.path.join(tmp, 'DEVLOG.md'), 'w', encoding='utf-8') as f:
            f.write('# a log that never logged it\n')
        rc, err, _ = under_O(call)
        record('expected_v0 on a log that never logged it, under -O', rc != 0 and 'was never logged' in err, err)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    code = ("import driver\nfrom instrument import basis\nBa, Bb = basis.Basis('R4', 8), basis.Basis('R4', 12)\n"
            "driver.embeds(Ba, Bb)\nprint('embeds')\n")
    rc, err, so = under_O(code)
    record('green parent: the N = 8 basis embeds in the N = 12 one, under -O', rc == 0 and so == 'embeds', so or err)
    rc, err, _ = under_O(code.replace("driver.embeds(Ba, Bb)", "Bb.index[0], Bb.index[1] = Bb.index[1], Bb.index[0]\n"
                                                                "driver.embeds(Ba, Bb)"))
    record('a higher basis whose leading part is reordered, under -O', rc != 0 and 'does not embed' in err, err)
    tmp = log_root()
    old = devtools.ROOT
    try:
        devtools.ROOT = tmp
        before = open(os.path.join(tmp, 'DEVLOG.md'), encoding='utf-8').read()
        expect('green parent: log_run in a temporary root writes its entry and keeps the output',
               lambda: devtools.log_run(os.path.abspath(__file__), 'synthetic', ['a test entry'],
                                        outputs=(os.path.join(tmp, 'probe.out'),)), refused=False)
        wrote = open(os.path.join(tmp, 'DEVLOG.md'), encoding='utf-8').read()
        kept_ = os.path.join(tmp, 'dev', 'runs', '002_probe.out')
        record('   its entry and its kept copy are there', wrote != before and os.path.exists(kept_), sorted(os.listdir(
            os.path.join(tmp, 'dev', 'runs'))))
        with open(kept_, 'w', encoding='utf-8') as f:
            f.write('a kept output\n')
        os.replace(os.path.join(tmp, 'DEVLOG.md'), os.path.join(tmp, 'DEVLOG.md.x'))
        with open(os.path.join(tmp, 'DEVLOG.md'), 'w', encoding='utf-8') as f:
            f.write(before)
        expect('log_run where the kept copy exists', lambda: devtools.log_run(
            os.path.abspath(__file__), 'synthetic', ['a test entry'], outputs=(os.path.join(tmp, 'probe.out'),)))
        same = (open(os.path.join(tmp, 'DEVLOG.md'), encoding='utf-8').read() == before
                and open(kept_, encoding='utf-8').read() == 'a kept output\n')
        record('   nothing written: the log and the kept copy as they were', same, same)
        rc, err, _ = under_O(f"from instrument import devtools\ndevtools.ROOT = {tmp!r}\n"
                             f"devtools.log_run({os.path.abspath(__file__)!r}, 'synthetic', ['x'],"
                             f" outputs=({os.path.join(tmp, 'probe.out')!r},))")
        same = (open(os.path.join(tmp, 'DEVLOG.md'), encoding='utf-8').read() == before
                and open(kept_, encoding='utf-8').read() == 'a kept output\n')
        record('log_run under -O, writing nothing', rc != 0 and 'refused under python -O' in err and same, err)
    finally:
        devtools.ROOT = old
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    devtools.require('synthetic')
    assert not os.path.exists(os.path.join(ROOT, 'run', 'FROZEN.json')), 'a freeze exists'
    say("The guard's tests (DRIVER_PLAN.md v4), on temporary trees; nothing solved, no sealed seed built.")
    for t in (test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11):
        t()
    failed = sum(not ok for _, ok in results)
    say(f'{failed} failed of {len(results)}')
    path = os.path.join(HERE, 'test_guard.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"The guard's tests: {'PASS' if not failed else 'FAIL'}, {len(results) - failed} of {len(results)}.",
                      'Each outcome derived before the run (the script\'s docstring); temporary trees only, nothing solved,'
                      ' no sealed seed built, no sealed record opened.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
