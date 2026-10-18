#!/usr/bin/env python3
"""The separation rule re-read from saved summaries (UB's re-read, as a logged run). Cases: C2a, C2b.

Usage: sep_reread.py CONTROL

convergence.separation is applied to the summaries that dev/sep_controls.py saved under the set rule (the runs in
dev/runs/ whose points carry a saved summary), with each point's band edge from its saved basis levels and lam, exactly
as the driver read them. Nothing is solved and no record is built: the instrument's code is read again, at its current
hashes, on saved data. It is the logged check that the shipped verdicts stand under the instrument as it now is.

Claims, derived before the run:
  1. Every re-read verdict and type equals the shipped one, except where the merged closure of DEVLOG 219 changes
     it, which is named in CHANGED: C2a's ladders at eps = 32, shipped Unresolved, read converged, Elliptic, since two
     closures that share a group at N = 24 are read as one set (DEVLOG 219; DEVLOG 220 read it so). C2a: its sample,
     3 of 3 as shipped, and its ladders, 17 of 18 as shipped and that one as changed; C2b: its ladders, 20 of 20.
  2. Under the arm 'one_way_set', the sets as built when those runs shipped, every verdict and type equals the shipped
     one: the rule's code changed only in how it forms and reads sets.
"""
import glob
import json
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import convergence as cv, devtools  # noqa: E402

out = []
CHANGED = {('C2a', 'ladders', 32.0): ('converged', 'Elliptic')}     # by the merged closure (DEVLOG 219)


def say(s=''):
    print(s, flush=True)
    out.append(s)


def saved_runs(name):
    """The logged control runs of this control whose points carry saved summaries, by mode."""
    runs = {}
    for path in sorted(glob.glob(os.path.join(HERE, 'runs', f'*_sep_controls_{name}_*.json'))):
        J = json.load(open(path, encoding='utf-8'))
        if any(k.startswith('N') and 'summary' in v for k, v in J.items()):
            runs[path.rsplit('_', 1)[1][:-5]] = (os.path.basename(path), J)
    return runs


def main():
    name = sys.argv[1]
    assert name in ('C2a', 'C2b')
    devtools.require(name)
    runs = saved_runs(name)
    say(f"The separation rule re-read on {name}'s saved summaries, under convergence.py as it now is: {sorted(runs)}")
    total, same, changed, arm_same = 0, 0, 0, 0
    for mode, (fname, J) in sorted(runs.items()):
        Ns = sorted({int(k[1:].split('_')[0]) for k in J if k.startswith('N')})
        eps_keys = sorted((k[len('rule_eps'):] for k in J if k.startswith('rule_eps')), key=float)
        ok_mode, ch_mode, arm_mode = 0, 0, 0
        for e in eps_keys:
            sums = [J[f'N{N}_eps{e}']['summary'] for N in Ns]
            top = J[f'N{Ns[-1]}_eps{e}']
            band = cv.band_edge(top['eig'], Ns[0], top['lam'])
            res = cv.separation(sums, band=band)
            arm = cv.separation(sums, band=band, arms=('one_way_set',))
            shipped = (J[f'rule_eps{e}']['verdict'], J[f'rule_eps{e}']['type'])
            want = CHANGED.get((name, mode, float(e)))
            got = (res['verdict'], res['type'])
            if want is None:
                ok_mode += got == shipped
            else:
                ch_mode += got == want and shipped != want
            arm_mode += (arm['verdict'], arm['type']) == shipped
            if got != (want or shipped):
                say(f"   {mode} eps {float(e):g}: MISMATCH  re-read {got[0]} {got[1]}, expected {(want or shipped)[0]}"
                    f" {(want or shipped)[1]}, shipped {shipped[0]} {shipped[1]}")
            elif want is not None:
                say(f"   {mode} eps {float(e):g}: changed as named, shipped {shipped[0]} {shipped[1]}, re-read {got[0]}"
                    f" {got[1]}")
        n_changed = sum(1 for (c, m, _) in CHANGED if (c, m) == (name, mode))
        total += len(eps_keys)
        same += ok_mode
        changed += ch_mode
        arm_same += arm_mode
        say(f"{mode} ({fname}): {ok_mode} of {len(eps_keys) - n_changed} verdicts as shipped and {ch_mode} of {n_changed}"
            f" as changed, at N = {Ns}; under the arm, {arm_mode} of {len(eps_keys)} as shipped")
    n_all = sum(1 for (c, _, _) in CHANGED if c == name)
    ok1 = total > 0 and same == total - n_all and changed == n_all
    ok2 = total > 0 and arm_same == total
    failed = int(not ok1) + int(not ok2)
    say(f"1. {'PASS' if ok1 else 'FAIL'}: {same} of {total - n_all} re-read verdicts equal the shipped ones, and {changed}"
        f" of {n_all} changed as named")
    say(f"2. {'PASS' if ok2 else 'FAIL'}: under the arm, {arm_same} of {total} equal the shipped ones")
    path = os.path.join(HERE, f'sep_reread_{name}.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), name,
                     [f"The separation rule re-read on {name}'s saved summaries: {'PASS' if not failed else 'FAIL'}, {same} of"
                      f" {total - n_all} verdicts as shipped and {changed} of {n_all} changed as named; under the arm,"
                      f" {arm_same} of {total} as shipped; under the instrument as hashed above. No solve.",
                      'Derived before the run (the script\'s docstring): the rule changed only in how it forms and reads'
                      ' sets.'],
                     outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
