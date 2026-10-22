#!/usr/bin/env python3
"""The guard's tests (M8.16's DRIVER_PLAN.md v4, § The guard's tests; UB's item 12 and UA's edited-entry test; the
units on step 3, its DEVLOG 234), carried into M8.16.1 and extended (M8.16.1's DRIVER_PLAN.md v2, The tests). Case:
synthetic.

Usage: test_guard.py MIT_REPO

M8.16.1's changes to M8.16's tests: M8.16's development outputs, its log and EXPECTED_V0.md (tests 6, 11, 12 and 13)
are read from M8.16's folder in MIT_REPO's history at the record's commit, 87fc643, since M8.16.1's tree does not carry
M8.16's dev/; the temporary trees hold the pinned values file, which write_guard.py now checks; test 13's reading of
E7, M8.16's dry-run claim, leaves with E7; and the script writes no development log entry. Tests 14 to 18 are new.

Every test runs on a temporary tree, a copy of instrument/ and reference/m815/ with a synthetic run/ folder, through
devtools.RUN_ROOT; the target-record tests use a synthetic git repository. No test solves anything, and no test
constructs a sealed seed: the sealed refusals are read on the name alone.

Claims, derived before the run: each case below is refused, and each green parent proceeds. Test 12 also reads entry
245's kept outputs, each checked against the SHA-256 that entry records, and M8.15's C2a record in reference/m815/.
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
 14. The two new cases on the name (M8.16.1): C3R/R4 and T5J/R2 refused by require and by seeds.seed_state with no
     FROZEN.json, and by seeds.seed_for_check outside a seedcheck process; and the driver refusing a case of the role
     ray or member before the gate record, beside its green parent, the same case as a control going on to its solve.
 15. seeds.py's own paths (M8.16.1), on C2a entered in its table at its slot and level, so no sealed seed is built:
     through a valid test FROZEN.json, seeds.seed_state builds it equal to its GO-path seed, refuses a basis of the
     wrong slot, and refuses once the file is removed; in a seedcheck process seeds.seed_for_check builds it, and
     outside one refuses it.
 16. seeds.py's guards under python -O (M8.16.1): a new seed with no freeze, seed_for_check outside a seedcheck process,
     and a basis of the wrong slot, on C2a entered in the table, so a failing guard could build no sealed seed, are each
     refused, beside the arm, an assert of the same form that does not fire.
 17. write_guard.py's values-file guard (M8.16.1), on copies of the pinned file: the file itself passes, and each is
     refused: a cases section that differs from its recorded hash; an inventory that differs from cases.py's, a
     recorded check false, and a multiple group not scalar, each with the hash recomputed; the run's own failure list
     not empty; and, each with the hash recomputed (UA), T2/R4's two groups exchanged at N = 24, their values and
     individual ties intact, and P5's quartet put outside the bar at every cutoff. cases.py's loader refuses the last
     two as well, before any scoring.
 18. The base-case rule (M8.16.1, amendment 5's ladder; UB). C2a/R5:ladder, as build_dry.py writes it, carries
     C2a/R5's admission and representative, the role dryladder and cases.R5_LADDER's points; load admits it in dry
     mode, and the seed built from its base, as run_case builds it, equals C2a/R5's. checks_of reads it with
     check_control, the R5 control's K1 and K4: on the registered C2a/R5 outputs, its bar, trend and deviations equal
     the record's, and its K1 fails where the ladder's other points are absent. Refused, for P5:ladder, T2/R5:ladder,
     C3R/R4:ladder and T5J/R2:ladder in a dry list: load, under the case's own admission; load again, with the
     admission field edited to a GO name; and the seed constructor, on its base's name. The arm: M8.16's second test,
     the full name against branches.SEALED alone, lets all four edited lists through.
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
import seeds as sd  # noqa: E402
import cases as cs  # noqa: E402
import write_guard as wg  # noqa: E402
import build_dry  # noqa: E402

REPO = sys.argv[1] if len(sys.argv) > 1 else None
RECORD = '87fc643'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
out, results = [], []


def m816(path):
    """A file of M8.16's folder, read from MIT_REPO's history at the record's commit."""
    return subprocess.run(['git', '-C', REPO, 'show', f'{RECORD}:{M816}/{path}'], check=True, capture_output=True).stdout


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
        shutil.copy(os.path.join(HERE, 'next_order_values.json'), os.path.join(tmp, 'run', 'next_order_values.json'))
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
    names = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', RECORD, f'{M816}/dev/runs/'], check=True,
                           capture_output=True, text=True).stdout.split()
    hits = sorted(n for n in names if n.endswith('_sep_controls_C2a_sample.json'))
    J = json.loads(m816(hits[-1][len(M816) + 1:]))
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
            with open(os.path.join(tmp, f_), 'wb') as f:
                f.write(m816(f_))
        call = f"from instrument import branches\nbranches.expected_v0({tmp!r})\nprint('read')"
        rc, err, so = under_O(call)
        record('green parent: expected_v0 on copies of the logged files, under -O', rc == 0 and so == 'read', so or err)
        with open(os.path.join(tmp, 'EXPECTED_V0.md'), 'a', encoding='utf-8') as f:
            f.write('\n')
        rc, err, _ = under_O(call)
        record('expected_v0 on an EXPECTED_V0.md that differs from its logged version, under -O',
               rc != 0 and 'differs from the version logged' in err, err)
        with open(os.path.join(tmp, 'EXPECTED_V0.md'), 'wb') as f:
            f.write(m816('EXPECTED_V0.md'))
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


def kept245(name):
    """M8.16's entry 245's kept output, read from MIT's history and checked against the SHA-256 that entry records."""
    import re
    line = next(x for x in m816('DEVLOG.md').decode('utf-8').splitlines() if f'kept as `dev/runs/245_dry_{name}`' in x)
    raw = m816(f'dev/runs/245_dry_{name}')
    if hashlib.sha256(raw).hexdigest() != re.search(r'`([0-9a-f]{64})`', line).group(1):
        raise RuntimeError(f'{name} differs from the output entry 245 kept')
    return json.loads(raw.decode('utf-8'))


def test12():
    """xrodz on #637: B2, a failed seed on the pyramid's K1 and K4 and in K6; and the comment tier's reported readings.
    The pyramid's checks are read on C2a's kept output standing in, so no sealed seed or record is touched."""
    import copy
    say("12. the seeds on the pyramid and in K6, and the reported readings (xrodz on #637):")
    C2a, C2b, lad = kept245('C2a.json'), kept245('C2b.json'), kept245('C2a_ladder.json')
    with open(os.path.join(ROOT, 'reference', 'm815', 'branch_C2a_R4.json'), encoding='utf-8') as f:
        m815 = json.load(f)
    case = C2a['case']
    N0 = sorted(C2a['cutoffs'], key=int)[0]
    record("green parent: the pyramid's K1 with every seed passed", ck.check_pyramid_k1(C2a, case) is True,
           ck.check_pyramid_k1(C2a, case))
    bad = copy.deepcopy(C2a)
    bad['cutoffs'][N0]['seed']['ok'] = False
    k1b, k4b = ck.check_pyramid_k1(bad, case), ck.check_pyramid_k4(bad, case)
    record("a seed that failed its check fails the pyramid's K1 and K4", not k1b and not k4b['K4'] and not k4b['seeds'],
           (k1b, k4b['K4'], k4b['seeds']))
    st = ck.stop_checks('P5', dict(K1=k1b, K2=True, K3=dict(outcome='resolved'), K4=k4b['K4']))
    record('and the stop names K1 and K4', st == ['K1', 'K4'], st)
    k6 = ck.check_row_k6(lad, lad['case'], m815)
    record("green parent: K6 on the kept ladder with every seed passed", k6['K6'] and k6['seeds'], (k6['K6'], k6['seeds']))
    badl = copy.deepcopy(lad)
    badl['cutoffs'][sorted(badl['cutoffs'], key=int)[0]]['seed']['ok'] = False
    k6b = ck.check_row_k6(badl, badl['case'], m815)
    record('a seed that failed its check: every read point invalid, and K6 fails',
           not k6b['K6'] and k6b['rows'] and all(r['status'] == 'invalid' for r in k6b['rows']),
           (k6b['K6'], sorted({r['status'] for r in k6b['rows']})))
    rep = ck.check_row_k5(C2b, C2b['case'])['reported']
    want = [ck.key(e) for e in (0.5, 1.0, 2.0)]
    record("K5's readings at 0.5, 1 and 2 reported at every cutoff, with each mode's deviation",
           all(k in rep and all(N in rep[k] and 'modes' in rep[k][N] for N in C2b['cutoffs']) for k in want),
           sorted(rep))
    slow = [r['slow'] for r in k6['rows']]
    record("K6's slow comparison beside each read point, with M8.15's level-2 to level-3 change",
           bool(slow) and all(s.get('imag', {}).get('dev') is not None and s['imag'].get('m815_l2_vs_l3') is not None
                              for s in slow),
           [f"{s['imag']['dev']:.1e}/{s['imag']['m815_l2_vs_l3']:.1e}" for s in slow if 'imag' in s])
    Ns = sorted(C2a['cutoffs'], key=int)
    pts = [C2a['cutoffs'][N]['points'][ck.key(0.25)] for N in Ns]
    rd = ck.reading([q['summary'] for q in pts], pts[-1]['eig'], pts[-1]['lam'], pts[-1]['record']['margin'],
                    int(Ns[0]))
    tested = [r for r in rd['rows'] if r['role'] == 'tested' and 'd2' in r]
    record("the rule's relative change between the two highest cutoffs, beside it, against 1e-6",
           rd['rel_change_max'] is not None and isinstance(rd['rel_change_ok'], bool) and tested
           and all('rel_change' in r for r in tested), (rd['rel_change_max'], rd['rel_change_ok']))
    try:
        json.dumps(dr.jsonable(dict(k5=ck.check_row_k5(C2b, C2b['case']), k6=k6, k6b=k6b, reading=rd)))
        js = 'serialized'
    except (TypeError, ValueError) as e:
        js = f'{type(e).__name__}: {e}'
    record('the new records serialize as the driver writes them', js == 'serialized', js)


def test13():
    """UA on #637: a failed seed ends the case before any solve. With the seed check made to fail and a sentinel in
    place of the solver, the sentinel never fires and the failure is recorded; with the seed passing, the sentinel
    fires, so it is live. C1 the same, its sentinel on the record. M8.16's reading of E7 leaves with E7."""
    say("13. a failed seed ends the case before any solve (UA on #637):")
    real_checks, real_continue, real_read = br.orbit_checks, br.continue_to, dr.read_point

    def failing(*a, **k):
        chk = dict(real_checks(*a, **k))
        chk['crit'] = 1.0
        return chk

    def sentinel(*a, **k):
        raise Solved('the solver')

    C2a, C1 = kept245('C2a.json'), kept245('C1.json')
    for name, case, run, attr in (('C2a', C2a['case'], lambda c: dr.run_case('C2a', c, True), 'continue_to'),
                                  ('C1', C1['case'], lambda c: dr.run_c1(c), 'read_point')):
        mod = br if attr == 'continue_to' else dr
        try:
            setattr(mod, attr, sentinel)
            try:
                run(case)
                live = False
            except Solved:
                live = True
            record(f"{name}, green parent: with the seed passing, the sentinel in place of {attr} fires", live, live)
            br.orbit_checks = failing
            try:
                out, _ = run(case)
                fired = False
            except Solved:
                out, fired = None, True
        finally:
            br.orbit_checks, br.continue_to, dr.read_point = real_checks, real_continue, real_read
        Ns = [str(N) for N in case['cutoffs']]
        shape = (out is not None and sorted(out['cutoffs'], key=int) == Ns
                 and out['cutoffs'][Ns[0]]['seed']['ok'] is False and out['cutoffs'][Ns[0]]['seed']['Q'] is not None
                 and all(out['cutoffs'][N]['seed'].get('why', '').startswith('not checked') for N in Ns[1:])
                 and all(not out['cutoffs'][N]['points'] for N in Ns))
        record(f"{name}: with the seed failing, the sentinel never fires, and every cutoff is recorded with no point",
               not fired and shape, (fired, shape))
        try:
            chk = dr.checks_of(name, case, out, None, True) if out is not None else {}
            st = ck.stop_checks(name, chk)
            ok_ = chk.get('K1') is False and chk.get('K4') is False and 'K1' in st and 'K4' in st
            got = (chk.get('K1'), chk.get('K4'), st)
        except Exception as e:                                   # the checks must report it, never raise
            ok_, got = False, f'{type(e).__name__}: {e}'
        record(f"{name}: its checks report the failure without an exception, and the stop names it", ok_, got)



def test14():
    say('14. the two new cases on the name, and before the gate record (M8.16.1):')
    with tree(allow=('C2a',)) as t:
        os.remove(os.path.join(t, 'run', 'FROZEN.json'))
        for name, B in (('C3R/R4', basis.Basis('R4', 16)), ('T5J/R2', basis.Basis('R2', 16))):
            expect(f'{name} by require, with no FROZEN.json', lambda n=name: devtools.require(n))
            expect(f'{name} by seeds.seed_state, with no FROZEN.json', lambda n=name, b=B: sd.seed_state(n, b))
            expect(f'{name} by seeds.seed_for_check, outside a seedcheck process', lambda n=name, b=B: sd.seed_for_check(n, b))
    for role in ('ray', 'member'):
        with dry_tree() as t:
            p = os.path.join(t, 'run', 'DRY.json')
            D = json.load(open(p, encoding='utf-8'))
            D['cases']['C1'] = dict(D['cases']['C1'], role=role)
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(D, f)
            got = resumed()
            record(f'the driver refuses a case of the role {role} before the gate record',
                   got[0] == 'refused' and 'gate record' in got[1], got)
    with dry_tree() as t:
        got = resumed()
        record('green parent: the same first case, as a control, goes on to its solve', got == ('proceeded', 'C1'), got)


def test15():
    say("15. seeds.py's own paths, on C2a entered in its table (M8.16.1):")
    go, new, reps = set(devtools.GO), dict(sd.NEW), dict(sd.REPS)
    B = basis.Basis('R4', 16)
    want = np.zeros(B.m, dtype=complex)
    want[br.weight_index(B, 6, 3)] = 1.0
    try:
        devtools.GO.clear()
        sd.NEW['C2a'], sd.REPS['C2a'] = ('R4', 6), {3: 1.0}
        with tree(allow=('C2a',)) as t:
            u = sd.seed_state('C2a', B)
            ok = float(np.abs(u - want).max()) == 0.0
            record('through a valid test FROZEN.json, seeds.seed_state builds it equal to its GO-path seed', ok, ok)
            expect('seeds.seed_state on a basis of the wrong slot', lambda: sd.seed_state('C2a', basis.Basis('R2', 16)))
            expect('seeds.seed_for_check outside a seedcheck process', lambda: sd.seed_for_check('C2a', B))
            os.remove(os.path.join(t, 'run', 'FROZEN.json'))
            expect('seeds.seed_state once FROZEN.json is removed', lambda: sd.seed_state('C2a', B))
    finally:
        devtools.GO.clear()
        devtools.GO.update(go)
        sd.NEW.clear()
        sd.NEW.update(new)
        sd.REPS.clear()
        sd.REPS.update(reps)
    code = (f"import sys\nsys.path.insert(0, {ROOT!r})\nsys.path.insert(0, {HERE!r})\nimport numpy as np\n"
            "from instrument import basis, devtools\nimport seeds as sd\ndevtools.require('seedcheck')\n"
            "sd.NEW['C2a'], sd.REPS['C2a'] = ('R4', 6), {3: 1.0}\n"
            "u = sd.seed_for_check('C2a', basis.Basis('R4', 16))\nprint('built', round(float(np.linalg.norm(u)), 12))")
    q = subprocess.run([sys.executable, '-I', '-B', '-c', code], capture_output=True, text=True)
    record('green parent: in a seedcheck process, seeds.seed_for_check builds it',
           q.returncode == 0 and q.stdout.strip() == 'built 1.0', q.stdout.strip() or q.stderr.strip()[-200:])


def test16():
    say("16. seeds.py's guards under python -O (M8.16.1):")
    rc, err, _ = under_O("from instrument import basis\nimport seeds as sd\nsd.seed_state('C3R/R4', basis.Basis('R4', 8))")
    record('a new seed with no freeze, under -O', rc != 0 and 'no valid frozen allowlist lists it' in err, err)
    rc, err, _ = under_O("from instrument import basis\nimport seeds as sd\nsd.seed_for_check('T5J/R2', basis.Basis('R2', 8))")
    record('seed_for_check outside a seedcheck process, under -O', rc != 0 and 'only in a seedcheck process' in err, err)
    rc, err, _ = under_O("from instrument import basis, devtools\nimport seeds as sd\ndevtools.admitted = lambda *a, **k: True\n"
                         "sd.NEW['C2a'], sd.REPS['C2a'] = ('R4', 6), {3: 1.0}\nsd.seed_state('C2a', basis.Basis('R2', 8))")
    record('a basis of the wrong slot, on C2a entered in the table, under -O', rc != 0 and 'not R4 from level 6' in err, err)
    rc, _, so = under_O("slot = 'R2'\nassert slot == 'R4', 'the basis is not R4'\nprint('proceeded')")
    record('the arm: an assert of the same form does not fire under -O', rc == 0 and so == 'proceeded', so)


def test17():
    say("17. write_guard.py's values-file guard (M8.16.1):")
    src = os.path.join(HERE, 'next_order_values.json')

    def rehash(V):
        V['cases_sha256'] = hashlib.sha256(json.dumps(V['cases'], sort_keys=True, separators=(',', ':'),
                                                      ensure_ascii=False).encode('utf-8')).hexdigest()

    def guard_on(change):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            os.makedirs(os.path.join(tmp, 'run'))
            V = json.load(open(src, encoding='utf-8'))
            change(V)
            with open(os.path.join(tmp, 'run', 'next_order_values.json'), 'w', encoding='utf-8') as f:
                json.dump(V, f, indent=1, ensure_ascii=False)
            return wg.next_order_values(tmp)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def group(V, n, i):
        return V['cases'][n]['cutoffs']['24']['groups'][i]
    expect('green parent: the pinned values file', lambda: guard_on(lambda V: None), refused=False)
    expect('a cases section that differs from its recorded hash',
           lambda: guard_on(lambda V: group(V, 'P5', 1).update(c_g=['0', '0'])))
    expect("an inventory that differs from cases.py's, its hash recomputed",
           lambda: guard_on(lambda V: (group(V, 'T1/R4', 0).update(krein='+'), rehash(V))))
    expect('a recorded check false, its hash recomputed',
           lambda: guard_on(lambda V: (V['cases']['T4/R5']['checks'].update(X=False), rehash(V))))
    expect('a multiple group not scalar, its hash recomputed',
           lambda: guard_on(lambda V: (group(V, 'T2/R4', 0).update(scalar=False), rehash(V))))
    expect("the run's own failure list not empty", lambda: guard_on(lambda V: V['checks'].update(failed=['an arm'])))

    def exchanged(V):
        gs = V['cases']['T2/R4']['cutoffs']['24']['groups']
        gs[0], gs[1] = gs[1], gs[0]
        rehash(V)

    def quartet_out(V):
        for x in V['cases']['P5']['cutoffs'].values():
            next(g for g in x['groups'] if g['cls'] == 'complex')['under_bar'] = False
        rehash(V)
    for label, change, name in (("T2/R4's two groups exchanged at N = 24, their ties intact (UA)", exchanged, 'T2/R4'),
                                ("P5's quartet outside the bar at every cutoff (UA)", quartet_out, 'P5')):
        expect(f'{label}, its hash recomputed', lambda c=change: guard_on(c))
        V = json.load(open(src, encoding='utf-8'))
        change(V)
        try:
            cs._next_order(name, cs.CASES[name], V)
            why = None
        except ValueError as e:
            why = str(e)
        record(f"   cases.py's loader refuses it before any scoring", why is not None, why)


def test18():
    say("18. the base-case rule, amendment 5's ladder (M8.16.1; UB):")
    D = json.loads(build_dry.build('ladder'))
    lad = D['cases'].get(build_dry.LADDER, {})
    plumbing = json.loads(build_dry.build())['cases']['C2a/R5']
    ok = (D['order'] == ['C2a/R5:ladder'] and lad.get('admission') == 'C2a/R5' and lad.get('role') == 'dryladder'
          and [p['eps'] for p in lad.get('points', [])] == cs.R5_LADDER and all(p['read'] for p in lad['points'])
          and lad.get('representative') == plumbing['representative'])
    record("the ladder's list: C2a/R5's admission and representative, the role dryladder, cases.R5_LADDER's points,"
           ' all read', ok, f"{D['order']}, {lad.get('admission')}, {lad.get('role')}, {len(lad.get('points', []))} points")
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    old = dr.HERE

    def put(order, cases):
        with open(os.path.join(tmp, 'DRY.json'), 'w', encoding='utf-8') as f:
            json.dump(dict(order=order, cases=cases), f)
    try:
        dr.HERE = tmp
        put(D['order'], D['cases'])
        expect('green parent: C2a/R5:ladder admitted by load in dry mode', lambda: dr.load(True), refused=False)
        B5 = basis.Basis('R5', 8)
        u, v = sd.seed_state(sd.base('C2a/R5:ladder'), B5), sd.seed_state('C2a/R5', B5)
        same = float(np.abs(u - v).max()) == 0.0
        record("its seed, built from its base as run_case builds it, equals C2a/R5's", same, same)
        reg = json.loads(m816('run/out/C2a_R5.json'))
        chk = dr.checks_of(build_dry.LADDER, lad, reg, None, True)
        ok = (set(chk) == {'K1', 'K4', 'converged', 'bar', 'trend', 'deviations'} and chk['bar'] and chk['trend']
              and json.loads(json.dumps(dr.jsonable(chk['deviations']))) == reg['checks']['deviations']
              and not chk['K1'] and not chk['K4'])
        record("checks_of reads it with check_control: on the registered outputs, the record's bar, trend and deviations,"
               " and K1 failing where the ladder's other points are absent", ok,
               {k: v for k, v in chk.items() if k != 'deviations'})
        names = [f'{x}:ladder' for x in ('P5', 'T2/R5', 'C3R/R4', 'T5J/R2')]
        slots = {'P5:ladder': 'R4', 'T2/R5:ladder': 'R5', 'C3R/R4:ladder': 'R4', 'T5J/R2:ladder': 'R2'}
        for n in names:
            c = dict(lad, admission=cs.admission(n))
            put([n], {n: c})
            expect(f"{n} in a dry list, under its own admission {cs.admission(n)}", lambda: dr.load(True))
            put([n], {n: dict(c, admission='C2a/R5')})
            expect(f'{n}, its admission field edited to a GO name, by load', lambda: dr.load(True))
            expect(f'{n}: its base, {sd.base(n)}, by the seed constructor, on the name',
                   lambda b=sd.base(n), sl=slots[n]: sd.seed_state(b, basis.Basis(sl, 8)))
        through = [n for n in names if not ('C2a/R5' not in devtools.GO or n in br.SEALED)]
        record("the arm: M8.16's second test, the full name against branches.SEALED alone, lets all four edited lists"
               ' through', through == names, through)
    finally:
        dr.HERE = old
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    devtools.require('synthetic')
    if not REPO:
        raise SystemExit(__doc__)
    assert not os.path.exists(os.path.join(ROOT, 'run', 'FROZEN.json')), 'a freeze exists'
    say("The guard's tests (M8.16.1's DRIVER_PLAN.md v2), on temporary trees; nothing solved, no sealed seed built.")
    for t in (test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14,
              test15, test16, test17, test18):
        t()
    failed = sum(not ok for _, ok in results)
    say(f'{failed} failed of {len(results)}')
    path = os.path.join(HERE, 'test_guard.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if failed:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
