"""The rerun after the record fix (REGISTER_4.md, note of 2026-10-11T00:15:57Z) against the run it replaces.

The fix adds one field to each point record, 'frozen', and changes nothing the locator decides. So every driver record
of the rerun must equal its counterpart in out/run3_2026-10-10/ once these are set aside:
  - the added field 'frozen' in each locator point record, and nowhere else: the record's top-level 'frozen' block,
    the run's frozen values, is compared like everything else;
  - what records when and with which code: the start and finish times and the locator's SHA-256.
The comparison is exact, value for value, with floats compared as stored. The synthetic log is compared line for
line after its time stamp.
Two arms, each on a copy of a rerun record before anything is set aside, must fail: one number in a point record
perturbed, and one top-level frozen value changed.

  python3 compare_run3.py      prints the outcome; exit status 1 on any difference"""
import os, sys, json, glob, copy

HERE = os.path.dirname(os.path.abspath(__file__))
# the locator's folder: this script's own once it sits beside locate.py, else the bench's copy
LOCATOR = HERE if os.path.exists(os.path.join(HERE, 'locate.py')) else os.path.join(
    HERE, 't1_bench', 'scripts', 'soft-slot-dynamics-m8-15x-target1')
OUT = os.path.join(LOCATOR, 'out')
OLD = os.path.join(OUT, 'run3_2026-10-10')
VOLATILE = {'started', 'finished', 'locator_sha256'}
POINT = {'level', 'eps', 'nL', 'nB', 'nS', 'fast_search'}      # fields every locator point record carries


def strip(o, top=True):
    """Set aside the volatile top-level fields, and the 'frozen' field of locator point records only."""
    if isinstance(o, dict):
        point = not top and POINT <= set(o)
        return {k: strip(v, False) for k, v in o.items()
                if not (top and k in VOLATILE) and not (point and k == 'frozen')}
    if isinstance(o, list):
        return [strip(v, False) for v in o]
    return o


def diff(a, b, path=''):
    """The first difference between a and b, or None."""
    if type(a) != type(b):
        return f'{path}: {type(a).__name__} vs {type(b).__name__}'
    if isinstance(a, dict):
        if set(a) != set(b):
            return f'{path}: keys {sorted(set(a) ^ set(b))}'
        for k in a:
            d = diff(a[k], b[k], f'{path}.{k}')
            if d:
                return d
        return None
    if isinstance(a, list):
        if len(a) != len(b):
            return f'{path}: length {len(a)} vs {len(b)}'
        for i, (x, y) in enumerate(zip(a, b)):
            d = diff(x, y, f'{path}[{i}]')
            if d:
                return d
        return None
    return None if a == b else f'{path}: {a!r} vs {b!r}'


def first_point(rec):
    b = rec['brackets'][0]
    return b['points'][sorted(b['points'])[0]][0]


def main():
    names = sorted(os.path.basename(f) for f in glob.glob(os.path.join(OLD, 't1_*.json')))
    new_names = sorted(os.path.basename(f) for f in glob.glob(os.path.join(OUT, 't1_*.json')))
    ok = names == new_names and len(names) > 0
    print(f'  {"PASS" if ok else "FAIL"}  the same driver records: {names}' + ('' if ok else f' vs {new_names}'))
    pairs = {}
    for n in names:
        if n in new_names:
            pairs[n] = (json.load(open(os.path.join(OLD, n))), json.load(open(os.path.join(OUT, n))))
    for n, (a, b) in pairs.items():
        d = diff(strip(a), strip(b))
        ok &= d is None
        print(f'  {"PASS" if d is None else "FAIL"}  {n} equals run 3\'s' + ('' if d is None else f': {d}'))
    sl_old = open(os.path.join(OLD, 'synthetic.log')).read().splitlines()
    sl_new = open(os.path.join(OUT, 'synthetic.log')).read().splitlines()
    same = len(sl_old) == len(sl_new) > 1 and sl_old[1:] == sl_new[1:]      # the first line is the run's time stamp
    ok &= same
    print(f'  {"PASS" if same else "FAIL"}  synthetic.log equals run 3\'s, line for line after its time stamp')
    if ok and pairs:
        n, (a, b) = next(iter(pairs.items()))
        m = copy.deepcopy(b)
        p = first_point(m)
        p['near_zero'][0] = p['near_zero'][0] * (1 + 1e-12) + 1e-300
        caught = diff(strip(a), strip(m)) is not None
        ok &= caught
        print(f'  {"PASS" if caught else "FAIL"}  arm caught: one number in a point record of {n} perturbed')
        m = copy.deepcopy(b)
        m['frozen']['r_f3'] = 99.0
        caught = diff(strip(a), strip(m)) is not None
        ok &= caught
        print(f'  {"PASS" if caught else "FAIL"}  arm caught: the top-level frozen r_f3 of {n} changed to 99.0')
    print('comparison with run 3:', 'ALL PASS' if ok else 'FAIL')
    return ok


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
