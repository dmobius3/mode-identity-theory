"""Mutation arms for control 1a's registered checks: each arm alters the recorded arms just past one check's threshold,
and that check must fail while every other keeps its parent verdict. Reads control_1a.json; writes
control_1a_mutations.log."""
import os, json, copy, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from control_1a import evaluate


def last(a):
    return a['iterations'][-1]


ARMS = [
    (0, 'a middle frozen iteration falls below 1e-11', lambda fr, be: fr['iterations'][20].update(res=0.9e-11)),
    (0, 'the frozen solve stops at 39 iterations', lambda fr, be: fr['iterations'].pop()),
    (0, 'the frozen seed solve converges', lambda fr, be: fr.update(ok=True)),
    (1, 'the plateau misses its prediction by 2e-3', lambda fr, be: last(fr).update(full=last(fr)['plateau_pred'] * (1 + 2e-3))),
    (2, 'the plateau is 0.9e-8', lambda fr, be: last(fr).update(res=0.9e-8)),
    (3, 'the bench test ends at 2e-11', lambda fr, be: last(be).update(res=2e-11)),
    (3, 'the bench seed solve fails', lambda fr, be: be.update(ok=False)),
    (4, 'sigma differs by 2e-12 relative', lambda fr, be: last(be).update(sigma=last(fr)['sigma'] * (1 + 2e-12))),
    (5, '|nu| is 0.9e-8', lambda fr, be: last(be).update(nu=0.9e-8)),
    (6, 'mu misses its relation by 2e-6', lambda fr, be: last(be).update(mu=last(be)['mu_pred'] * (1 + 2e-6))),
]

if __name__ == '__main__':
    with open(os.path.join(HERE, 'control_1a.json')) as f:
        rec = json.load(f)
    fr0, be0 = rec['arms']['frozen'], rec['arms']['bench']
    parent = [ok for _, ok in evaluate(fr0, be0)[0]]
    L = [f'parent: {parent}']
    good = True
    for k, label, mut in ARMS:
        fr, be = copy.deepcopy(fr0), copy.deepcopy(be0)
        mut(fr, be)
        got = [ok for _, ok in evaluate(fr, be)[0]]
        others = all(got[j] == parent[j] for j in range(len(parent)) if j != k)
        fired = (not got[k]) and parent[k] and others
        good &= fired
        L.append(f'  {"caught" if fired else "MISSED"}  check {k + 1}: {label}  (verdicts {got})')
    L.append(f'every mutation caught by its own check alone: {good}' + ('' if all(parent) else
             '; the parent is not green, so a check that already fails cannot be mutation-tested'))
    with open(os.path.join(HERE, 'control_1a_mutations.log'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))
