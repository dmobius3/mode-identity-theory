"""A stub of run/m819_branch.py for the scope test (dev/test_scope.py), never for a run: the real module, with each job that
solves or evolves replaced by one that writes, from a scenario file (M819_SCENARIO), the records its dependents read.
Gate 1, the plan, the record, the dispatch in main() and guard_long run as written; guard_sealed is a spy that logs
each call and then reads gate 1 for real, skipping only FROZEN.json, which a stub tree has not got."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import numpy as np  # noqa: E402
import m819_branch as D  # noqa: E402

SC = json.load(open(os.environ['M819_SCENARIO']))
SPY = os.environ['M819_SPY']


def spy(name, slot, root, bench):
    with open(SPY, 'a') as f:
        f.write(json.dumps(dict(case=name, slot=slot, job=sys.argv[1])) + '\n')
    if (name, slot) in D.SEALED:
        D.controls_passed(root)


def series(verdict, T=20.0, rate=None):
    """A record with the columns the frozen evaluator reads (t, d, d_perp, d_rot, d_ref, N, E): Persists, Fails, or a
    rate run's growth."""
    t = np.arange(0.0, T + 1)
    dp = np.full_like(t, 1e-3) if verdict == 'Persists' else 1e-3 * np.exp(t / 2)
    if rate is not None:
        dp = 1e-7 * np.exp(rate * t)
    E = 1.0 + 1e-7 * np.sin(t)
    return np.column_stack([t, dp, dp, 1e-6 * np.ones_like(t), 1e-12 * np.ones_like(t), np.ones_like(t), E])


def raises():
    """A scenario's job that raises on every start, as a crash does."""
    if sys.argv[1] in SC.get('raising', []):
        raise RuntimeError(f'stub: {sys.argv[1]} raises')


def dyn(name, a):
    raises()
    tag = 'C3_rate' if name == 'rate' else name
    if name == 'rate':
        rec, extra = series('Fails', T=1000.0, rate=0.01), dict(level2_rates=[[0.01, 0.0]])
    else:
        rec, extra = series(SC['dyn'].get(name, 'Persists')), {}
    D.jdump(f'dynamics_{tag}.json', dict(energy_pert=1e-3, **extra))
    np.save(os.path.join(D.OUT, f'dynamics_{tag}.npy'), rec)


def p5a(a):
    D.jdump('control_1a_arm.json', dict(control=dict(passed=SC['p5a'], rule='stub')))


def c3e3(a):
    D.jdump('dynamics_C3_eps3.json', dict(verdict='Fails' if SC['c3e3'] else 'Persists', control=dict(passed=SC['c3e3'], rule='stub')))


def c2a(a, long_T=None):
    raises()
    ok = SC['c2a_long'] if long_T is not None else SC['c2a_dur']
    D.jdump('c2a.json', dict(T=(long_T or 2750.0), control=dict(passed=ok, rule='stub')))


def gates(row, a):
    g = SC['gates'][row]
    if g == 'crash':
        raise RuntimeError('stub: a gates job that raises')
    out = dict(row=row, case=D.ROWS[row][0], slot=D.ROWS[row][1], stretches=g['stretches'], points=[], states=[])
    if row == 'coherent_R5':
        out['ladder_outcome'] = dict(established=True, stub=True, other_elliptic_runs=SC.get('other_runs', []))
    D.jdump('gates.json', out)


def test(sid, a):
    plan = json.load(open(os.path.join(D.completed(a.root, 'plan'), 'PLAN.json')))
    t = plan['tests'][sid]
    D.guard_sealed(t['case'], t['slot'], a.root, a.bench)
    D.guard_long(a.root, plan, t['T'])
    D.jdump('test.json', dict(verdict=SC['verdicts'][sid], valid=True, T=t['T'], periods=t['T'] / t['P'], max_dperp=1e-3,
                              max_drot=1e-6, max_dref=1e-12))


D.job_dyn, D.job_p5a, D.job_c3e3, D.job_c2a, D.job_gates, D.job_test = dyn, p5a, c3e3, c2a, gates, test
D.guard_sealed = spy
D.main()
