"""The gates' mutation arms (M8.19's terms: THE TESTS BEFORE THE FREEZE: "each gate's mutation arm, turning it red for its
named reason on the controls at their recorded points"), on the stand-in's stored points: C2a/R4's gates.json from the
dry run, whose inputs are the frozen Points' own numbers. Arm 0 reads every stored point again unchanged and must give
its stored reading exactly; every other arm changes one input and must turn its gate red for the named reason, or, for
gate 6, move T as the rounding says. The guards' arms build a temporary run folder. Nothing is solved.

  test_gates.py GATES_JSON      prints each arm; exits 1 if any arm is not as named"""
import copy
import json
import math
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INSTRUMENT = os.path.normpath(os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x', 'm8_15x_solver'))
sys.path.insert(0, os.path.join(ROOT, 'run'))
sys.path.insert(0, INSTRUMENT)
from m815_common import classify  # noqa: E402
import m819_gates as G  # noqa: E402
import m819_branch as D  # noqa: E402

fails = []


def check(name, good, detail=''):
    print(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''))
    if not good:
        fails.append(name)


def red(name, pt, gate, why):
    ev = G.evaluate(pt, classify)
    w = ev['gates'].get(str(gate), {}).get('why') or ''
    check(name, (not ev['passed']) and ev['first_failed'] == gate and why in w,
          f"first failed {ev['first_failed']}, why {w!r}")


g = json.load(open(sys.argv[1]))
pts = g['points']
keys = ('eps', 'read', 'gates', 'first_failed', 'passed', 'T')
same = [json.loads(json.dumps(G.evaluate(p['input'], classify))) == {k: p[k] for k in keys} for p in pts]
check('arm 0: every stored point read again gives its stored reading', all(same), f'{sum(same)} of {len(pts)}')
top = G.search(pts)
check("the stand-in's search lands at 8 with T = 1000", top is not None and top['eps'] == 8.0 and top['T'] == 1000.0,
      f"{top and (top['eps'], top['T'])}")
base = top['input']
harm = next(p['input'] for p in pts if p['input']['ref']['source'] == 'harmonic' and p['passed'])
print(f"     arms at eps {base['eps']} (reference: {base['ref']['source']}) and {harm['eps']} (harmonic)")


def mut(pt, f):
    q = copy.deepcopy(pt)
    f(q)
    return q


red('gate 2: no level-2 solution', mut(base, lambda q: q.update(reached2=False)), 2, 'level 2')
red('gate 2: no level-3 solution', mut(base, lambda q: q.update(reached3=False)), 2, 'level 3')
red('gate 3: the level-3 cluster check', mut(base, lambda q: q['L3'].update(cluster_ok=False)), 3, 'level 3 cluster check')
red('gate 3: the level-2 cluster check', mut(base, lambda q: q['L2'].update(cluster_ok=False)), 3, 'level 2 cluster check')
red("gate 3: the reference's Krein sign flipped", mut(harm, lambda q: q['ref'].update(sign=-q['ref']['sign'])), 3,
    'no genuine imaginary mode with Krein sign -')
red("gate 3: the reference's count 2", mut(harm, lambda q: q['ref'].update(count=2)), 3,
    "where the reference's multiplicity is 2")


def twin(q):
    """A second Krein-positive level-2 mode at 1.02 times the slowest one's modulus."""
    c = G.candidates(q['L2'], +1, classify)[0]
    lam = c[1] * 1.02
    q['L2']['genuine'].append([[lam.real, lam.imag], c[2]])


red('gate 3: a near twin of the level-2 mode', mut(harm, twin), 3,
    'level 2: the mode is not identified: 2 candidates of Krein sign + within 5% of the slowest')
w_twin = G.evaluate(mut(harm, twin), classify)['gates']['3']['why']
c_twin = G.candidates(harm['L2'], +1, classify)[0]
check("gate 3: the near twin's refusal names both moduli",
      f'{c_twin[0]:.6g}' in w_twin and f'{abs(c_twin[1] * 1.02):.6g}' in w_twin, w_twin)


def scale_mode(q, level, s):
    c = G.candidates(q[level], q['ref'].get('sign', +1) if q['ref']['source'] == 'harmonic' else +1, classify)[0]
    for row in q[level]['genuine']:
        if complex(*row[0]) == c[1]:
            row[0] = [row[0][0] * s, row[0][1] * s]


red('gate 4: levels 2 and 3 apart by 6%', mut(base, lambda q: scale_mode(q, 'L2', 1.06)), 4, 'levels 2 and 3 differ')
red('gate 4: the harmonic reading 6% off', mut(harm, lambda q: q['ref'].update(lam=q['ref']['lam'] * 1.06)), 4,
    'differs from the harmonic reading')
red('gate 5: a share of 0.0099', mut(base, lambda q: q.update(share=0.0099)), 5, 'the slow half carries')
T = top['T']
red('gate 7: r T just above ln(1/(10 eta))', mut(base, lambda q: q.update(r=1.0001 * q['log_bound'] / T)), 7, 'exceeds')
ev = G.evaluate(mut(base, lambda q: q.update(r=0.9999 * q['log_bound'] / T)), classify)
check('gate 7: r T just below passes', ev['passed'])

# gate 6: the rounding
for P, want in ((999.9, 1000.0), (1000.0, 1000.0), (1000.1, 1250.0), (2750.0, 2750.0), (2750.0 * (1 + 1e-12), 3000.0),
                (2717.7, 2750.0)):
    lam = [0.0, 2 * math.pi / P]
    got, _ = G.test_T(lam)
    check(f'gate 6: P = {P!r} gives T = {want}', got == want, f'got {got}')

# the search: the top point failing moves the test down to the next point that passes
evs = copy.deepcopy(pts)
i = max(range(len(evs)), key=lambda k: evs[k]['eps'])
evs[i] = dict(G.evaluate(mut(evs[i]['input'], lambda q: q.update(share=0.0)), classify))
nxt = G.search(evs)
lower = max(p['eps'] for p in pts if p['passed'] and p['eps'] < 8.0)
check('the search: the top point red moves the test down one point', nxt is not None and nxt['eps'] == lower,
      f"{nxt and nxt['eps']} against {lower}")

# the duration control reads gates 2, 3, 5, 6 and 7: a gate-4 failure does not turn it red
ev = G.evaluate(mut(base, lambda q: (scale_mode(q, 'L2', 1.06), q.update(read=[2, 3, 5, 6, 7]))), classify)
check("the duration control: gate 4 is not read", ev['passed'] and '4' not in ev['gates'])

# the stretches and the coherent row's stretch
R = {e: dict(type='Elliptic', verdict='converged', lam=1.0, sign=1, count=1) for e in (0.25, 0.5, 1.0, 2.0, 4.0)}
R[1.0] = dict(type=None, verdict='Unresolved', lam=None, sign=None, count=None)
check('stretches: an unclassified point splits a stretch', G.stretches(R) == [[0.25, 0.5], [2.0, 4.0]], str(G.stretches(R)))
L = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0]
ty = {e: 'Elliptic' for e in L}
check('the coherent stretch: all Elliptic, the whole ladder', G.coherent_stretch(ty, L, [0.25, 0.5, 1.0, 2.0], True) == (L, 'ladder'))
ty2 = dict(ty)
ty2[0.5] = 'Unresolved'
check('the coherent stretch: the run through 2', G.coherent_stretch(ty2, L, [0.25, 0.5, 1.0, 2.0], True) == ([1.0, 2.0, 4.0, 8.0], 'ladder'))
check('the coherent stretch: not established, the record',
      G.coherent_stretch(ty, L, [0.25, 0.5, 1.0, 2.0], False) == ([0.25, 0.5, 1.0, 2.0], 'record'))
ty3 = dict(ty)
ty3[4.0] = 'Hyperbolic'
st3, _ = G.coherent_stretch(ty3, L, [0.25, 0.5, 1.0, 2.0], True)
check('the coherent row: an Elliptic run above a gap is named apart', st3 == [0.25, 0.5, 1.0, 2.0]
      and G.other_elliptic_runs(ty3, L, st3, True) == [[8.0]], str(G.other_elliptic_runs(ty3, L, st3, True)))
check('the coherent row: none apart when the whole ladder is the stretch', G.other_elliptic_runs(ty, L, L, True) == [])
check('the coherent row: none apart on a ladder not established',
      G.other_elliptic_runs(ty3, L, [0.25, 0.5, 1.0, 2.0], False) == [])

# the guards, on a temporary run folder
tmp = tempfile.mkdtemp()
try:
    def runlog(completed):
        with open(os.path.join(tmp, 'RUNLOG.json'), 'w') as f:
            json.dump(dict(completed=completed, ended={}, not_run={}, events=[]), f)

    def controls(passed):
        os.makedirs(os.path.join(tmp, 'controls'), exist_ok=True)
        p = os.path.join(tmp, 'controls', 'CONTROLS.json')
        with open(p, 'w') as f:
            json.dump(dict(all_passed=passed, controls={}), f)
        return D.sha(p)

    def refused(name, f, why):
        try:
            f()
        except D.Refused as e:
            check(name, why in str(e), str(e))
            return
        check(name, False, 'not refused')

    runlog({})
    refused('guard: gate 1 not run', lambda: D.controls_passed(tmp), 'has not completed')
    h = controls(False)
    runlog({'controls': dict(files={'CONTROLS.json': h})})
    refused('guard: gate 1 failed', lambda: D.controls_passed(tmp), 'gate 1 did not pass')
    controls(True)
    refused('guard: CONTROLS.json changed after it completed', lambda: D.controls_passed(tmp), 'differs from the SHA-256')
    refused('guard: a sealed job on the bench', lambda: D.guard_sealed('T4', 5, tmp, True), 'sealed')
    if not os.path.exists(os.path.join(D.HERE, 'FROZEN.json')):
        refused('guard: a sealed job with no FROZEN.json', lambda: D.guard_sealed('T1', 4, tmp, False), 'no FROZEN.json')
    check('guard: a control is not sealed', D.guard_sealed('C2a', 4, tmp, False) is None)
    plan = dict(T_max=3000.0)
    refused('guard: a test longer than 2750 before the longest control', lambda: D.guard_long(tmp, plan, 3000.0),
            'c2a_long has not completed')
    os.makedirs(os.path.join(tmp, 'c2a_long'))
    p = os.path.join(tmp, 'c2a_long', 'c2a.json')
    with open(p, 'w') as f:
        json.dump(dict(T=3000.0, control=dict(passed=False)), f)
    runlog({'c2a_long': dict(files={'c2a.json': D.sha(p)})})
    refused('guard: the longest control did not Persist', lambda: D.guard_long(tmp, plan, 3000.0), 'waits for the longest')
    with open(p, 'w') as f:
        json.dump(dict(T=3000.0, control=dict(passed=True)), f)
    runlog({'c2a_long': dict(files={'c2a.json': D.sha(p)})})
    check('guard: a test longer than 2750 after the longest control Persisted', D.guard_long(tmp, plan, 3000.0) is None)
    check('guard: a test of 2750 or less waits for nothing', D.guard_long(tempfile.gettempdir(), plan, 2750.0) is None)
finally:
    shutil.rmtree(tmp)
print('PASS' if not fails else f'FAIL: {fails}')
raise SystemExit(1 if fails else 0)
