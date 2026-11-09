"""The dry run's bit-for-bit comparisons (M8.19's terms: THE TESTS BEFORE THE FREEZE), against M8.15.x's own records from
its qualification run on the frozen bytes, qualification/solver/m8_15_solver/out/ and qual_2026-10-09/controls/.

  compare_qual.py p5a RUNDIR        control 1a's arm against control_1a_rerun.json's M8.15.x arm
  compare_qual.py standin RUNDIR    the stand-in's points at 0.25 to 8, both levels, and its test at 8, against
                                    branch_C2a_R4.json and persist_C2a_R4_8.npy
  compare_qual.py dyn RUNDIR        M8.15's dynamics controls against the qualification's dynamics_*.json and .npy

RUNDIR holds the job folders. Every leaf is compared exactly, with only the fields named as timings left out. Prints each
comparison and its differing leaves; exits 1 on any difference or missing record."""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
QUAL = os.path.normpath(os.path.join(HERE, '..', '..', 'soft-slot-dynamics-m8-15x', 'qualification'))
QOUT = os.path.join(QUAL, 'solver', 'm8_15_solver', 'out')
TEST_FIELDS = ['verdict', 'valid', 'valid_under_v6_energy_rule', 'read_until', 'max_d', 'max_dperp', 'max_drot',
               'max_dref', 'charge_drift', 'energy_drift', 'energy_pert', 'energy_dev_vs_pert', 'energy_secular_drift',
               't_fail', 'drot_at_fail', 'r', 'dt', 'direction', 'initial_energy_norm', 'N_obs', 'N_step', 'T_int']
fails = []


def diff(a, b, path=''):
    out = []
    if type(a) != type(b):
        return [(path, a, b)]
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append((f'{path}/{k}', a.get(k, '<absent>'), b.get(k, '<absent>')))
            else:
                out += diff(a[k], b[k], f'{path}/{k}')
    elif isinstance(a, list):
        if len(a) != len(b):
            return [(path, f'{len(a)} entries', f'{len(b)} entries')]
        for i, (u, v) in enumerate(zip(a, b)):
            out += diff(u, v, f'{path}[{i}]')
    elif a != b:
        out.append((path, a, b))
    return out


def report(what, d, n=None):
    print(f"{'same' if not d else 'DIFFERS'}  {what}" + (f' ({n} leaves)' if n is not None else ''))
    for x in d[:12]:
        print('        ', x)
    if d:
        fails.append(what)


def leaves(o):
    if isinstance(o, dict):
        return sum(leaves(v) for v in o.values())
    if isinstance(o, list):
        return sum(leaves(v) for v in o)
    return 1


def load(p):
    with open(p) as f:
        return json.load(f)


def arrays(a_path, b_path, what):
    a, b = np.load(a_path), np.load(b_path)
    same = a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()
    print(f"{'same' if same else 'DIFFERS'}  {what}: {a.shape} against {b.shape}, bytes {'equal' if same else 'differ'}")
    if not same:
        fails.append(what)
        if a.shape == b.shape:
            k = np.argwhere(a != b)
            print('         first differing entries', k[:5].tolist(), 'max |a - b|', float(np.max(np.abs(a - b))))


def p5a(run):
    new = load(os.path.join(run, 'p5a', 'control_1a_arm.json'))
    old = load(os.path.join(QUAL, 'qual_2026-10-09', 'controls', 'control_1a_rerun.json'))['arms']['bench']
    for d in (new, old):
        d.pop('solve_seconds', None)
        d.pop('control', None)
        d['diagnostics'].pop('setup_seconds', None)
    report("control 1a's M8.15.x arm, all but its two timings", diff(new, old), leaves(old))


def standin(run):
    g = load(os.path.join(run, 'gates_C2a_R4', 'gates.json'))
    q = load(os.path.join(QOUT, 'branch_C2a_R4.json'))
    for key, label in (('points', 'level 3'), ('level2', 'level 2')):
        old = [p for p in q[key] if not p.get('bisection') and p['eps'] <= 8.0]
        new = g['ladder'][key]
        report(f'{label}: the points at 0.25 to 8 ({len(old)} on record)', diff(new, old), leaves(old))
    if g['ladder'].get('types'):
        # the coherent row's path: M8.15's frozen types, cross-checks and validity, against the same record's
        for key in ('types', 'cross'):
            old = [d for d in q[key] if d['eps'] <= 8.0]
            report(f'the {key} at 0.25 to 8 ({len(old)} on record)', diff(g['ladder'][key], old), leaves(old))
        report('the validity check at 0.25', diff(g['ladder']['validity_eps_min'], q['validity_eps_min']), 2)
        report('the changes of type at 0.25 to 8', diff(g['ladder']['changes'],
                                                         [c for c in q['changes'] if c['bracket'][1] <= 8.0]))
    tdir = os.path.join(run, 'test_C2a_R4_standin_1')
    if not os.path.isdir(tdir):
        print('(no test folder yet)')
        return
    t = load(os.path.join(tdir, 'test.json'))
    old = next(p for p in q['persistence'] if p.get('ran_at') == 8.0)
    report('the test at 8: every field run_test returns', diff({k: t[k] for k in TEST_FIELDS}, {k: old[k] for k in TEST_FIELDS}),
           len(TEST_FIELDS))
    arrays(os.path.join(tdir, 'test.npy'), os.path.join(QOUT, 'persist_C2a_R4_8.npy'), "the test's series at 8")


def dyn(run):
    for job, tag in (('dyn_C1', 'C1'), ('dyn_C2a', 'C2a'), ('dyn_C2b', 'C2b'), ('dyn_C3', 'C3'), ('rate', 'C3_rate')):
        d = os.path.join(run, job)
        if not os.path.isdir(d):
            print(f'MISSING  {job}')
            fails.append(job)
            continue
        new, old = load(os.path.join(d, f'dynamics_{tag}.json')), load(os.path.join(QOUT, f'dynamics_{tag}.json'))
        for x in (new, old):
            x.pop('seconds', None)
        report(f'{tag}: the record, all but its time', diff(new, old), leaves(old))
        arrays(os.path.join(d, f'dynamics_{tag}.npy'), os.path.join(QOUT, f'dynamics_{tag}.npy'), f'{tag}: the series')


if __name__ == '__main__':
    {'p5a': p5a, 'standin': standin, 'dyn': dyn}[sys.argv[1]](os.path.abspath(sys.argv[2]))
    print('PASS' if not fails else f'FAIL: {fails}')
    raise SystemExit(1 if fails else 0)
