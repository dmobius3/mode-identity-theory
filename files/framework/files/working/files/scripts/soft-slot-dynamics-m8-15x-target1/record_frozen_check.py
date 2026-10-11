"""The locator's point records carry the frozen point data (REGISTER_4.md, note of 2026-10-11T00:15:57Z).

Reads every driver record out/t1_*.json of the locator and checks each evaluated point, guards' points included:
  - it carries 'frozen', the frozen point's own record;
  - that record is the same point's: n(L), n(B|G_tol), k_c and the slow balance agree with the locator's fields;
  - its fast-spectrum result is present exactly where the search ran: a dict (found, counts, balanced) at a point
    recorded 'run', and None at one recorded 'not needed' or 'skipped'.
Then three mutation arms, each on a copy of the records, each of which must fail: a point without 'frozen'; a search
result at a point recorded 'not needed'; a frozen n(L) off by one. The parent must pass before the arms run.

No control reaches a full point that does not balance, so no record holds the state 'run'. The code path is therefore
also checked directly: EvalPoint.record on stub points in all three states, then on a copy of locate.py without the
line that drops the stand-in's output at a skipped point, which must fail.

  python3 record_frozen_check.py      prints the outcome; exit status 1 on any failure"""
import os, sys, json, glob, copy, types
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# the locator's folder: this script's own once it sits beside locate.py, else the bench's copy
LOCATOR = HERE if os.path.exists(os.path.join(HERE, 'locate.py')) else os.path.join(
    HERE, 't1_bench', 'scripts', 'soft-slot-dynamics-m8-15x-target1')
OUT = os.path.join(LOCATOR, 'out')
DROP = "                out['frozen']['fast_search'] = None"


def locate_module(mutant=False):
    path = os.path.join(LOCATOR, 'locate.py')
    src = open(path).read()
    if mutant:
        assert src.count(DROP) == 1, 'the line the arm removes is not in locate.py once'
        src = src.replace(DROP, '                pass')
    mod = types.ModuleType('locate_mutant' if mutant else 'locate_checked')
    mod.__file__ = path
    exec(compile(src, path, 'exec'), mod.__dict__)
    return mod


def stub_problems(mod):
    """EvalPoint.record on stub points: not needed (balanced), skipped (the stand-in's dict on the point) and run (the
    search's dict on the point). The frozen record carries a search result exactly at 'run'."""
    class Stub:
        def __init__(self, balanced):
            self.balanced = balanced
            self.fast = None if balanced else dict(found=[[1e-2, 0.0]], counts=[1, 0, 0], balanced=True)

        def record(self):
            return dict(nL=2, nB_cluster=2, kc=0, balanced=self.balanced, fast_search=self.fast)
    nz = dict(neg=[], ov=[], struct=[], nS=0, cover=[1.0], sub=[1.0], coverage_ok=True, subspace_ok=True)
    bad = []
    for state, balanced, skipped in (('not needed', True, False), ('skipped', False, True), ('run', False, False)):
        ep = mod.EvalPoint(3, 1.0, {}, Stub(balanced), 2, 2, 0, np.zeros(0), np.zeros((0, 0)), nz, 16, [1.0], True,
                           None, None, 1e-9, ctx=dict(fast_skipped=skipped))
        r = ep.record()
        fs = r.get('frozen', {}).get('fast_search', 'absent')
        if r['fast_search'] != state:
            bad.append(f'{state}: recorded as {r["fast_search"]}')
        if state == 'run' and not isinstance(fs, dict):
            bad.append('run: no search result')
        if state != 'run' and fs is not None:
            bad.append(f'{state}: a search result {fs}')
    return bad


def points(rec):
    """Every evaluated point record in a driver record: the brackets' points and the guards' two points."""
    for b in rec.get('brackets', []):
        for lv, pts in b.get('points', {}).items():
            for p in pts:
                yield f'level {lv} eps {p["eps"]:.6g}', p
        for sn in b.get('steps_named', []):
            for g in sn.get('guards', []):
                for k in ('point3', 'point2'):
                    if isinstance(g.get(k), dict):
                        yield f'guard {g["side"]} d {g.get("d")} {k}', g[k]


def problems(recs):
    bad, n = [], 0
    for name, rec in recs.items():
        for where, p in points(rec):
            n += 1
            f = p.get('frozen')
            if not isinstance(f, dict):
                bad.append(f'{name} {where}: no frozen record')
                continue
            for mine, theirs in (('nL', 'nL'), ('nB', 'nB_cluster'), ('kc', 'kc'), ('balanced', 'balanced')):
                if p[mine] != f.get(theirs):
                    bad.append(f'{name} {where}: {mine} {p[mine]} but frozen {theirs} {f.get(theirs)}')
            fs = f.get('fast_search', 'absent')
            if p['fast_search'] == 'run':
                if not (isinstance(fs, dict) and {'found', 'counts', 'balanced'} <= set(fs)):
                    bad.append(f'{name} {where}: recorded run, but no search result')
            elif fs is not None:
                bad.append(f'{name} {where}: recorded {p["fast_search"]}, but a search result {str(fs)[:40]}')
    return n, bad


def first_point(recs):
    for name, rec in recs.items():
        for where, p in points(rec):
            return p
    raise SystemExit('no point records to mutate')


def main():
    files = sorted(glob.glob(os.path.join(OUT, 't1_*.json')))
    recs = {os.path.basename(f): json.load(open(f)) for f in files}
    n, bad = problems(recs)
    by_state = {}
    for name, rec in recs.items():
        for where, p in points(rec):
            by_state[p['fast_search']] = by_state.get(p['fast_search'], 0) + 1
    print(f'records: {len(recs)} ({", ".join(recs)})')
    print(f'points: {n}; by fast-spectrum state: {by_state}')
    ok = n > 0 and not bad
    print(f'  {"PASS" if ok else "FAIL"}  every point carries its own frozen record' + ('' if ok else f': {bad[:5]}'))
    if not ok:
        return False
    arms = []
    m = copy.deepcopy(recs); del first_point(m)['frozen']
    arms.append(('a point without its frozen record', m))
    m = copy.deepcopy(recs); p = first_point(m); p['fast_search'] = 'not needed'
    p['frozen']['fast_search'] = dict(found=[], counts=[0, 0, 0], balanced=True)
    arms.append(('a search result at a point recorded not needed', m))
    m = copy.deepcopy(recs); first_point(m)['frozen']['nL'] += 1
    arms.append(('a frozen n(L) off by one', m))
    allok = True
    for label, m in arms:
        caught = bool(problems(m)[1])
        allok &= caught
        print(f'  {"PASS" if caught else "FAIL"}  arm caught: {label}')
    sb = stub_problems(locate_module())
    print(f'  {"PASS" if not sb else "FAIL"}  the code path on stub points, all three states' + ('' if not sb else f': {sb}'))
    allok &= not sb
    if not sb:
        caught = bool(stub_problems(locate_module(mutant=True)))
        allok &= caught
        print(f'  {"PASS" if caught else "FAIL"}  arm caught: locate.py without the line that drops the stand-in\'s output')
    print('record check:', 'ALL PASS' if allok else 'FAIL')
    return allok


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
