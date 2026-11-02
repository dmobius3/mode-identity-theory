"""What MIT's own computation solves and reads (DESIGN.md). An entry is one case on one list of amplitudes, at the ladder's
cutoffs, each cutoff on its own path from the seed. Nothing here depends on a value computed after the pin.

The grids are M8.17's windows (census_lib.WINDOWS). T5 takes added points, chosen from M8.17's stored readings alone
(dev/t5_top.out and dev/t5_laws.out, DESIGN.md): the index drop sits in (90.51, 128) at N = 24 and 32, and the
quartet's collision near 118 at N = 24 and 126 at N = 32 on the square-root law, moving up with N. They change the path
into 128 and 132, so T5's readings above 90.51 are new solves, and the stored ones are known outcomes.

The fresh points are amplitudes no record holds, next to M8.18's two failures, with pass marks stated first (PASS_MARKS;
DESIGN.md). They are read before any row. P5's pair sits between tau(32) and tau(40) for eps from about 0.230 to 0.258;
C3R/R4's D eigenvalue sits between the two gray-zone tops for eps from about 0.159 to 0.256.
"""
import json

import cases as cs
import census_lib as lib
import driver as dr

LADDER = (24, 32, 40)
W4, W5, W2 = lib.WINDOWS['R4'], lib.WINDOWS['R5'], lib.WINDOWS['R2']
T5_ADDED = (76.0, 100.0, 106.0, 112.0, 116.0, 120.0, 124.0, 126.0, 127.0, 129.0, 130.0)
T5_GRID = sorted(list(W2) + list(T5_ADDED))
ROWS = {'T1_R4': ('T1/R4', W4), 'T4_R4': ('T4/R4', W4), 'T1_R5': ('T1/R5', W5), 'T5_R2': ('T5/R2', T5_GRID),
        'T5J_R2': ('T5J/R2', W2), 'C2a_R5': ('C2a/R5', W5)}
FRESH = {'fresh_P5': ('P5', (0.24, 0.30)), 'fresh_C3R_R4': ('C3R/R4', (0.20, 0.30)), 'fresh_C2b': ('C2b', (0.30,)),
         'fresh_C2a_R5': ('C2a/R5', (0.30,))}
# M8.18's controls on their own grids: the runner's first test, against M8.18's files
CONTROLS = {'ctl_C2a': 'C2a', 'ctl_C2b': 'C2b', 'ctl_C3': 'C3', 'ctl_C2a_R5': 'C2a/R5', 'ctl_P5': 'P5',
            'ctl_C3R_R4': 'C3R/R4'}
# Each fresh point's marks, stated before any read: (as-built verdict, changed verdict, what the as-built Unresolved must
# rest on: 'link', a new link at N = 40 alone, or 'flag', D's flag at N = 40 alone), with the case's own type and indices
# at every cutoff. A control that misses a mark is diagnosed and disclosed before any row is read.
PASS_MARKS = {('fresh_P5', 0.24): ('Unresolved', 'converged', 'link'), ('fresh_P5', 0.30): ('converged', 'converged', None),
              ('fresh_C3R_R4', 0.20): ('Unresolved', 'converged', 'flag'),
              ('fresh_C3R_R4', 0.30): ('converged', 'converged', None), ('fresh_C2b', 0.30): ('converged', 'converged', None),
              ('fresh_C2a_R5', 0.30): ('converged', 'converged', None)}
# hours at N = 40 in series, from M8.17's and M8.18's records, for the runner's order alone
HOURS_40 = dict(T1_R4=8.0, T4_R4=8.9, T1_R5=11.8, T5_R2=5.6, T5J_R2=3.6, C2a_R5=12.0, fresh_P5=0.8, fresh_C3R_R4=0.8,
                fresh_C2b=0.1, fresh_C2a_R5=0.4, ctl_C2a=0.95, ctl_C2b=0.36, ctl_C3=1.31, ctl_P5=1.46, ctl_C3R_R4=1.50,
                ctl_C2a_R5=1.54)


def entry(tag):
    """(case name, amplitudes, serialized case): the case as census.Cutoff reads it, as FROZEN.json serialized it."""
    if tag in ROWS:
        name, eps = ROWS[tag]
    elif tag in FRESH:
        name, eps = FRESH[tag]
    else:
        name = CONTROLS[tag]
        eps = [p['eps'] for p in cs.CASES[name]['points']]
    case = cs.serialize(name, dict(cs.CASES[name], points=[dict(eps=e, read=True) for e in eps], cutoffs=list(LADDER)))
    return name, list(eps), json.loads(json.dumps(dr.jsonable(case)))


def hours(tag, N):
    """A job's rough length, for the order alone: M8.18's ratios between cutoffs."""
    return HOURS_40.get(tag, 1.0) / {24: 53.0, 32: 5.1, 40: 1.0}[N]


def solves():
    """Every solve of the computation, longest first."""
    jobs = [(tag, N) for tag in list(FRESH) + list(ROWS) for N in LADDER]
    return sorted(jobs, key=lambda j: -hours(*j))


def allowlist():
    return sorted({n for n, _ in ROWS.values()} | {n for n, _ in FRESH.values()} | set(CONTROLS.values()))
