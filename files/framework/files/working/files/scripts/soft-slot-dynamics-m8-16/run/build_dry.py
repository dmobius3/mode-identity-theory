#!/usr/bin/env python3
"""Write run/DRY.json, the dry run's case list (DRIVER_PLAN.md v2): C1, C2a, C2b, C3 and R5's coherent branch, as
registered, and C2a's ladder segment to eps = 2 with eps = 0.707 withheld, for K6's path on a control. GO cases only;
the driver refuses any other name in it. The text is built before the file is opened.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cases as cs  # noqa: E402

ORDER = ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5', 'C2a:ladder']


def build():
    cases = {n: cs.serialize(n, cs.CASES[n]) for n in ORDER[:-1]}
    cases['C2a:ladder'] = cs.serialize('C2a:ladder', cs.DRY_LADDER)
    return json.dumps(dict(order=ORDER, cases=cases), indent=1) + '\n'


if __name__ == '__main__':
    text = build()
    with open(os.path.join(HERE, 'DRY.json'), 'w', encoding='utf-8') as f:
        f.write(text)
    print('DRY.json written:', ORDER)
