"""Regression gate for Verdict's reclassify refactor (control 2a): the Point record at one level-2 point of P5 (pi/5,
eps_min norm) and of C2a (the seed solve) must be identical before and after. Usage: python3 regress_verdict_refactor.py
before|after; 'after' compares against the saved 'before'."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
from m815_common import LevelCase
from m815_branch import Point
from angle import Circle
from continuation import Branch
from nonlinear import to_real


def records():
    out = {}
    lc = LevelCase(2, 'P5', 4)
    m0 = 0.25 / (lc.Q / lc.vol) / 120
    r = Circle(lc).solve(math.pi / 5, m0, lc.lam0 + 0.25)
    rec = dict(m=m0, eps=r['sigma'] - lc.lam0, sigma=r['sigma'], x=to_real(r['Phi']), it=r['it'], full=r['full'],
               nu=[r['nu']], mu=[r['mu']])
    out['P5'] = Point(lc, rec, 0.25, 3.97e-4, 3.97e-4, keep_cluster=True).record()
    lc = LevelCase(2, 'C2a', 4)
    br = Branch(lc.st, lc.case, lc.lam0, lc.Q, lc.vol, log=lambda s: None)
    assert br.first(0.25)
    out['C2a'] = Point(lc, br.accepted[0], 0.25, 3.97e-4, 3.97e-4, keep_cluster=True).record()
    return json.loads(json.dumps(out, default=float))


if __name__ == '__main__':
    path = os.path.join(HERE, 'regress_verdict_before.json')
    if sys.argv[1] == 'before':
        json.dump(records(), open(path, 'w'))
        print('saved')
    else:
        same = records() == json.load(open(path))
        open(os.path.join(HERE, 'regress_verdict_refactor.log'), 'w').write(f'Point records identical before and after the refactor: {same}\n')
        print('identical:', same)
