"""Regression gate for the carry edit (REGISTER_1.md, amendment of 2026-10-08T23:57:20Z): solve_pinned gained a
reference argument and angle.py a carry path. Control 1a's bench arm and control 1b's angle solve must reproduce
their records exactly; 1b's roots gained one field, 'maximum', which is set aside in the comparison."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, subprocess, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))


def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if k != 'maximum'}
    if isinstance(o, list):
        return [strip(v) for v in o]
    return o


if __name__ == '__main__':
    out = []
    p = os.path.join(HERE, 'regress_1a_bench.json')
    subprocess.run([sys.executable, os.path.join(HERE, 'control_1a.py'), '--arm', 'bench', p], check=True)
    new = json.load(open(p)); os.remove(p)
    old = json.load(open(os.path.join(HERE, 'control_1a_amended.json')))['arms']['bench']
    same1a = new['iterations'] == old['iterations'] and new['accepted'] == old['accepted']
    out.append(f'1a bench arm, iterations and accepted point identical to the amended run: {same1a}')
    from m815_common import LevelCase
    from angle import angle_solve
    lc = LevelCase(2, 'P5', 4)
    m0 = 0.25 / (lc.Q / lc.vol) / 120
    ref = json.load(open(os.path.join(HERE, 'control_1b.json')))
    ok = True
    for n, key in ((1, 'one_period'), (2, 'two_periods')):
        rec, _, _ = angle_solve(lc, m0, lc.lam0 + 0.25, theta_start=math.pi / 10, n_periods=n)
        rec = json.loads(json.dumps(rec, default=float))
        same = strip(rec) == strip(ref[key])
        ok &= same
        out.append(f'1b angle solve, {key}: identical to the record except the new field: {same}')
    out.append(f'gate passes: {same1a and ok}')
    open(os.path.join(HERE, 'regress_carry_edit.log'), 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))
