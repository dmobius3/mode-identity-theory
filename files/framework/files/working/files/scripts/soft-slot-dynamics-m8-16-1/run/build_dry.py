#!/usr/bin/env python3
"""Write run/DRY.json, a dry run's case list, from one of two lists, by name.

Usage: build_dry.py [plumbing|ladder]
  plumbing, the default: the plumbing pass's list (M8.16.1's DRIVER_PLAN.md v2, The development runs in this step,
            3): C1, C2a, C2b, C3 and R5's coherent branch, as registered.
  ladder:   amendment 5's (BOUNDARY.md; LADDER_PLAN.md v2): one case, C2a/R5:ladder, R5's coherent branch along
            cases.R5_LADDER, every point read, with the role dryladder.
GO cases only; the driver refuses any other name in it, and any case whose base is sealed. M8.16's dry list also held
C2a's ladder segment, for its E3 to E5, which M8.16.1 does not carry. The text is built before the file is opened.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cases as cs  # noqa: E402

ORDER = ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5']
LADDER = 'C2a/R5:ladder'


def lists(which):
    """The order and the serialized cases of the named list."""
    if which == 'plumbing':
        return ORDER, {n: cs.serialize(n, cs.CASES[n]) for n in ORDER}
    if which == 'ladder':
        case = dict(cs.CASES['C2a/R5'], role='dryladder', points=cs._points(cs.R5_LADDER))
        return [LADDER], {LADDER: cs.serialize(LADDER, case)}
    raise SystemExit(f'build_dry.py: no list {which!r}; the lists are plumbing and ladder')


def build(which='plumbing'):
    order, cases = lists(which)
    return json.dumps(dict(order=order, cases=cases), indent=1) + '\n'


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'plumbing'
    text = build(which)
    with open(os.path.join(HERE, 'DRY.json'), 'w', encoding='utf-8') as f:
        f.write(text)
    print('DRY.json written:', json.loads(text)['order'])
