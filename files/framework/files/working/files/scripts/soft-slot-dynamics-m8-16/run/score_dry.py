#!/usr/bin/env python3
"""The dry run's claims scored from entry 245's kept outputs (UB, UA; DEVLOG 248 and 249). Case: dryrun.

Usage: score_dry.py

The rerun of entry 245 computed every case, and its claims code crashed at E6. Here driver.dry_claims, with E6's
reader as the units ruled it, is applied to the outputs that entry kept, after each is checked against the SHA-256 that
entry and the run's own log record. Nothing is solved. The gate record is copied to a temporary directory, and the
claims' own log entry is captured, not written; this script's entry records the outcome.

Claims, derived before the run:
  1. Every output entry 245 kept equals the SHA-256 that entry records; and every case output, the gate record, the
     verdict and the transcript equal the SHA-256s in the run's log.
  2. Every reference E6 reads equals the output its own entry logged.
  3. The claims code raises nothing, and E1 to E5 read as the run scored them: each line equals the run's own line in
     its driver.log, character for character, so the edit reached E6 alone.
  4. E6 is evaluated. Its outcome is the dry run's E6, reported as it falls: the dry run passes if E1 to E6 all hold.
  5. The arm (UB, UA): with C2b's D7 reference copied and its slow eigenvalues removed at N = 32, eps = 2, E6 reads not
     evaluated and counts as failed, the claims' entry reads FAIL, and nothing raises.
"""
import ast
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import driver  # noqa: E402

E = 245
OUTS = ['driver.log', 'driver.out', 'RUNLOG.json', 'GATE.json', 'VERDICT.json', 'C1.json', 'C2a.json', 'C2a.npz',
        'C2b.json', 'C3.json', 'C3.npz', 'C2a_R5.json', 'C2a_ladder.json']
CASES = {'C1': 'C1.json', 'C2a': 'C2a.json', 'C2b': 'C2b.json', 'C3': 'C3.json', 'C2a/R5': 'C2a_R5.json',
         'C2a:ladder': 'C2a_ladder.json'}
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def kept(f):
    return os.path.join(ROOT, 'dev', 'runs', f'{E:03d}_dry_{f}')


def logged(path):
    """The SHA-256 DEVLOG.md records for a kept file, from its 'kept as' line, or None."""
    with open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8') as f:
        for line in f:
            if f'kept as `{path}`' in line:
                return re.search(r'`([0-9a-f]{64})`', line).group(1)
    return None


def score(results, log, refs=None):
    """driver.dry_claims on the kept outputs: (its lines, the captured entry's first line, an exception or None)."""
    captured, real, saved = [], devtools.log_run, dict(driver.E6_REFS)
    start = len(driver.out_lines)
    devtools.log_run = lambda script, case, lines, outputs=(): captured.append(lines)
    driver.E6_REFS.update(refs or {})
    err = None
    try:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(kept('GATE.json'), os.path.join(tmp, 'GATE.json'))
            driver.dry_claims(tmp, results, log, None)
    except Exception as e:                 # noqa: BLE001, the claim is that none is raised
        err = repr(e)
    finally:
        devtools.log_run = real
        driver.E6_REFS.clear()
        driver.E6_REFS.update(saved)
    return driver.out_lines[start:], (captured[0][0] if captured else ''), err


def claims_of(entry):
    """The claims' outcomes from the captured entry's line, as dry_claims writes them."""
    m = re.search(r'(\{.*\})\.$', entry)
    return ast.literal_eval(m.group(1)) if m else None


def main():
    devtools.require('dryrun')
    say(f"The dry run's claims scored from entry {E}'s kept outputs; nothing solved.")
    with open(kept('RUNLOG.json'), encoding='utf-8') as f:
        L = json.load(f)
    bad = [f for f in OUTS if logged(f'dev/runs/{E:03d}_dry_{f}') != sha(kept(f))]
    bad += [fn for rec in L['completed'].values() for fn, h in rec['files'].items() if sha(kept(fn)) != h]
    bad += [k for k, fn in (('gate', 'GATE.json'), ('verdict', 'VERDICT.json'), ('transcript', 'driver.out'))
            if L[k]['sha256'] != sha(kept(fn))]
    ok1 = not bad
    say(f"1. {'PASS' if ok1 else 'FAIL'}: {len(OUTS)} kept outputs against entry {E}, and the run's log's hashes"
        f"{'' if ok1 else '; differ: ' + str(bad)}")
    paths = sorted({p for v in driver.E6_REFS.values() for p in v[:2]})
    badr = [p for p in paths if logged(p) != sha(os.path.join(ROOT, p))]
    ok2 = not badr
    say(f"2. {'PASS' if ok2 else 'FAIL'}: {len(paths)} references equal the outputs their entries logged: {paths}"
        f"{'' if ok2 else '; differ: ' + str(badr)}")
    results = {}
    for name, fn in CASES.items():
        with open(kept(fn), encoding='utf-8') as f:
            results[name] = json.load(f)
    lines, entry, err = score(results, L)
    with open(kept('driver.log'), encoding='utf-8') as f:
        ran = f.read().split('\n')
    first = lambda ls, t: next((x for x in ls if x.startswith(f'{t}. ')), None)    # noqa: E731
    same = {t: first(lines, t) is not None and first(lines, t) == first(ran, t) for t in ('E1', 'E2', 'E3', 'E4', 'E5')}
    ok3 = err is None and all(same.values())
    say(f"3. {'PASS' if ok3 else 'FAIL'}: {'no exception' if err is None else err}; E1 to E5 as the run scored them:"
        f" {same}")
    C = claims_of(entry) or {}
    ok4 = C.get('E6') in (True, False)
    passed = all(C.get(t) is True for t in ('E1', 'E2', 'E3', 'E4', 'E5', 'E6'))
    say(f"4. {'PASS' if ok4 else 'FAIL'}: E6 evaluated: {C.get('E6')}. {first(lines, 'E6')}")
    say(f"   The dry run's claims: {C}: {'PASS' if passed else 'FAIL'}")
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ipath, epath, how = driver.E6_REFS['C2b']
        with open(os.path.join(ROOT, epath), encoding='utf-8') as f:
            J = json.load(f)
        del J['N32_eps2.0']['slow']
        cut = os.path.join(tmp, os.path.basename(epath))
        with open(cut, 'w', encoding='utf-8') as f:
            json.dump(J, f)
        a_lines, a_entry, a_err = score(results, L, refs={'C2b': (ipath, cut, how)})
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    A = claims_of(a_entry) or {}
    ok5 = a_err is None and A.get('E6', 'absent') is None and "FAIL" in a_entry
    reads = a_entry.split(':')[1].split('(')[0].strip() if ':' in a_entry else repr(a_entry)
    say(f"5. {'PASS' if ok5 else 'FAIL'}: the arm, C2b's D7 slow eigenvalues removed at N = 32, eps = 2:"
        f" {first(a_lines, 'E6')}; the entry reads {reads}; {'no exception' if a_err is None else a_err}")
    failed = sum(not x for x in (ok1, ok2, ok3, ok4, ok5))
    say(f'{failed} failed')
    say()
    say("The claims' lines, as dry_claims wrote them on the kept outputs:")
    for x in lines:
        say('   ' + x)
    path = os.path.join(HERE, 'score_dry.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'dryrun',
                     [f"The dry run's claims scored from entry {E}'s kept outputs, no solve: the scoring's checks"
                      f" {'PASS' if not failed else 'FAIL'} ({failed} failed); the dry run's claims {C}:"
                      f" {'PASS' if passed else 'FAIL'}.",
                      'Each claim derived before the run (the script\'s docstring).'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
