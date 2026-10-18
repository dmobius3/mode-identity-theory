#!/usr/bin/env python3
"""The dry run's claims on a stopped run (DEVLOG 218). Case: dryrun.

Usage: test_claims.py

driver.dry_claims is read on the outputs that DEVLOG 218's dry run kept. That run stopped after C1 and C2a, and its
claims code raised KeyError on C2b. The gate record is copied to a temporary directory, and the claims' own log entry
is captured, not written. Nothing is solved.

Claims, derived before the run:
  1. No exception.
  2. Every claim is not evaluated, naming what did not run: E1 and E6 name C2b, C3 and C2a/R5; E2 names C2b and C3;
     E3, E4 and E5 name C2a's ladder segment, C2a:ladder.
  3. 6 of 6 claims count as failed, and the captured entry reads FAIL.
"""
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import driver  # noqa: E402

out = []
WANT = {'E1': 'C2b, C3, C2a/R5', 'E2': 'C2b, C3', 'E3': 'C2a:ladder', 'E4': 'C2a:ladder', 'E5': 'C2a:ladder',
        'E6': 'C2b, C3, C2a/R5'}


def say(s=''):
    print(s, flush=True)
    out.append(s)


def kept(name):
    """Entry 218's kept output, by name: the stopped run, not the newest kept dry run (DEVLOG 253)."""
    return os.path.join(ROOT, 'dev', 'runs', f'{218:03d}_dry_{name}')


def main():
    devtools.require('dryrun')
    results = {}
    for n in ('C1', 'C2a'):
        with open(kept(f'{n}.json'), encoding='utf-8') as f:
            results[n] = json.load(f)
    with open(kept('RUNLOG.json'), encoding='utf-8') as f:
        log = json.load(f)
    say(f"The dry run's claims on the stopped run's kept outputs: {sorted(results)} ran"
        f" ({os.path.basename(kept('C2a.json'))}).")
    captured, real, crashed = [], devtools.log_run, None
    devtools.log_run = lambda script, case, lines, outputs=(): captured.append((case, lines))
    try:
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(kept('GATE.json'), os.path.join(tmp, 'GATE.json'))
            driver.dry_claims(tmp, results, log, None)
    except Exception as e:                 # noqa: BLE001, the claim is that none is raised
        crashed = repr(e)
    finally:
        devtools.log_run = real
    lines = list(driver.out_lines)
    ok1 = crashed is None
    say(f"1. {'PASS' if ok1 else 'FAIL'}: {'no exception' if ok1 else crashed}")
    seen = {t: next((ln for ln in lines if ln.startswith(f'{t}. ')), None) for t in WANT}
    ok2 = all(seen[t] == f'{t}. not evaluated: {w} did not run' for t, w in WANT.items())
    say(f"2. {'PASS' if ok2 else 'FAIL'}: " + '; '.join(f'{seen[t]!r}' for t in WANT))
    entry = captured[0][1][0] if captured else ''
    ok3 = 'FAIL (6 of 6' in entry and any(ln == "6 of the dry run's claims failed or were not evaluated" for ln in lines)
    say(f"3. {'PASS' if ok3 else 'FAIL'}: the captured entry reads {entry!r}")
    failed = sum(not x for x in (ok1, ok2, ok3))
    say(f'{failed} failed')
    path = os.path.join(HERE, 'test_claims.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'dryrun',
                     [f"The dry run's claims on a stopped run: {'PASS' if not failed else 'FAIL'} ({failed} failed). No"
                      ' solve; the claims\' own entry captured, not written.',
                      'Each claim derived before the run (the script\'s docstring).'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
