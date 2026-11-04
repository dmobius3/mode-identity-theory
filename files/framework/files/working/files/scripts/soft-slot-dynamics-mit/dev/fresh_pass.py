#!/usr/bin/env python3
"""The fresh controls against their pass marks, by hand: run/fresh.py holds the marks' test, and the job `fresh` writes the
record the rows need. This prints each point, and tests the marks' test.

Usage: fresh_pass.py OUT                    the marks in run/grid.py, on OUT's reading files
       fresh_pass.py --test OUT             the same code on M8.18's controls, read again in dev/runs: their marks are on
                                            record, and each wrong mark, its verdict or its cause, must be reported as a miss
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import fresh  # noqa: E402
import grid  # noqa: E402

KNOWN = {('ctl_P5', 0.25): ('Unresolved', 'converged', 'link'), ('ctl_P5', 0.5): ('converged', 'converged', None),
         ('ctl_C3R_R4', 0.25): ('Unresolved', 'converged', 'flag'), ('ctl_C3R_R4', 0.5): ('converged', 'converged', None),
         ('ctl_C2b', 0.25): ('converged', 'converged', None), ('ctl_C2a_R5', 0.25): ('converged', 'converged', None)}
WRONG = (('ctl_P5', 0.25, ('converged', 'converged', None)), ('ctl_P5', 0.25, ('Unresolved', 'converged', 'flag')),
         ('ctl_C3R_R4', 0.25, ('Unresolved', 'converged', 'link')))


def main():
    test = '--test' in sys.argv
    out = sys.argv[-1]
    marks = KNOWN if test else grid.PASS_MARKS
    bad = 0
    for (tag, e), m in marks.items():
        got = fresh.misses(out, tag, e, m)
        bad += bool(got)
        print(f"{tag} {e:g}: {'pass' if not got else 'MISS: ' + '; '.join(got)}", flush=True)
    if test:
        for tag, e, m in WRONG:
            wrong = fresh.misses(out, tag, e, m)
            print(f"a wrong mark, {tag} {e:g} {m}, is reported: {wrong[:1]}")
            bad += not wrong
    print(f'{bad} missed')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
