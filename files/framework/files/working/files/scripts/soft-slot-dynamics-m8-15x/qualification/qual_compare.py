"""M8.15.x qualification (REGISTER_3.md v2): the comparator of the reruns against their baselines.

Two modes:
  bitwise  the closing controls (§ 3): every value equal bit for bit, except
           - the listed new fields (gauge_multipliers, N_obs, N_step, T_int), present in the new record only;
           - timing fields (seconds), skipped;
           - residual: both at or below 1e-11 and |new - old| <= sum_k |mu_k| + 1e-13, mu from the sibling
             gauge_multipliers;
  branch   the branch reruns (§ 5): categorical values and structure exact; numbers within max(1e-9 |old|, floor), the
           floor 1e-13 times the list's largest modulus for complex values ([re, im] pairs), 1e-11 for the persistence
           diagnostics at round-off, 0 otherwise; residual by the § 3 rule.
Any key added or removed outside the listed new fields fails. Iteration counts (newton_it, it) must be equal; a moved
count is reported as such, for § 3's registered rule. .npy series are compared bitwise.

  python3 qual_compare.py selftest     the mutation arms, on M8.15's baseline (a green parent first)"""
import os, sys, json, copy, math
import numpy as np

NEW_FIELDS = {'gauge_multipliers', 'N_obs', 'N_step', 'T_int'}
TIMING = {'seconds', 'seconds_L3', 'seconds_L2'}
ITER = {'newton_it', 'it'}
ROUNDOFF = {'r', 'max_dref', 'charge_drift', 'energy_drift', 'energy_secular_drift', 'max_drot', 'max_d', 'max_dperp',
            'backward_error', 'krein'}       # backward_error and krein: the amendment of REGISTER_3.md
REL, CPLX_FLOOR, CPLX_ABS, DIAG_FLOOR, RES_TOL, RES_SLACK = 1e-9, 1e-13, 1e-12, 1e-11, 1e-11, 1e-13


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def is_pair(x):
    return isinstance(x, list) and len(x) == 2 and all(is_num(v) for v in x)


def is_pair_k(x):
    """[[re, im], krein]: an eigenvalue with its Krein value."""
    return isinstance(x, list) and len(x) == 2 and is_pair(x[0]) and is_num(x[1])


def point_scale(d):
    """The largest slow modulus at a point record (genuine_all and lifted), or None outside one."""
    vals = [abs(complex(*e[0])) for e in d.get('genuine_all', []) if is_pair_k(e)]
    vals += [abs(complex(*e)) for e in d.get('lifted', []) if is_pair(e)]
    return max(vals) if vals else None


class Report:
    def __init__(self):
        self.fail, self.diff, self.floor_used, self.iter_moved, self.n = [], [], [], [], 0

    def outcome(self):
        if self.fail:
            return 'FAIL'
        return 'bit-identical' if not self.diff else 'within tolerance'


def eq_float(a, b):
    return (a == b) or (isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b))


def compare(new, old, mode, path='', rep=None, parent_new=None, key=None, S=None):
    rep = rep or Report()
    if isinstance(old, dict):
        if mode == 'branch' and ('genuine_all' in old or 'lifted' in old):
            S = point_scale(old)
        if not isinstance(new, dict):
            rep.fail.append((path, 'type changed'))
            return rep
        extra = set(new) - set(old) - NEW_FIELDS
        missing = set(old) - set(new)
        for k in sorted(extra):
            rep.fail.append((f'{path}/{k}', 'key added'))
        for k in sorted(missing):
            rep.fail.append((f'{path}/{k}', 'key removed'))
        for k in old:
            if k in new and k not in TIMING:
                compare(new[k], old[k], mode, f'{path}/{k}', rep, parent_new=new, key=k, S=S)
        return rep
    if key == 'residual' and is_num(old) and is_num(new):
        rep.n += 1
        mu = (parent_new or {}).get('gauge_multipliers')
        if mu is None:
            rep.fail.append((path, 'residual without gauge_multipliers beside it'))
            return rep
        bound = sum(abs(m) for m in mu) + RES_SLACK
        if not (new <= RES_TOL and old <= RES_TOL and abs(new - old) <= bound):
            rep.fail.append((path, f'residual {new!r} against {old!r}, bound {bound:.2e}'))
        elif new != old:
            rep.diff.append((path, f'residual moved by {abs(new - old):.2e} (bound {bound:.2e})'))
        return rep
    if isinstance(old, list):
        if not isinstance(new, list) or len(new) != len(old):
            rep.fail.append((path, f'list length {len(new) if isinstance(new, list) else "?"} against {len(old)}'))
            return rep
        pairs = mode == 'branch' and old and all(is_pair(x) for x in old) and all(is_pair(x) for x in new)
        pairs_k = mode == 'branch' and old and all(is_pair_k(x) for x in old) and all(is_pair_k(x) for x in new)
        if pairs or pairs_k:
            cz = (lambda x: complex(*x)) if pairs else (lambda x: complex(*x[0]))
            scale = S if S is not None else max(abs(cz(x)) for x in old)
            for i, (a, b) in enumerate(zip(new, old)):
                if pairs_k:
                    compare(a[1], b[1], mode, f'{path}[{i}][1]', rep, parent_new=parent_new, key='krein', S=S)
                rep.n += 1
                d = abs(cz(a) - cz(b))
                if d == 0:
                    continue
                tol = max(REL * abs(cz(b)), CPLX_FLOOR * scale, CPLX_ABS)
                if d <= tol:
                    rep.diff.append((f'{path}[{i}]', f'complex moved by {d:.2e}'))
                    if d > REL * abs(cz(b)):
                        rep.floor_used.append(f'{path}[{i}]')
                else:
                    rep.fail.append((f'{path}[{i}]', f'complex moved by {d:.2e}, tolerance {tol:.2e}'))
            return rep
        for i, (a, b) in enumerate(zip(new, old)):
            compare(a, b, mode, f'{path}[{i}]', rep, parent_new=parent_new, key=key, S=S)
        return rep
    rep.n += 1
    if key in ITER and new != old:
        rep.iter_moved.append((path, new, old))
        rep.fail.append((path, f'iteration count {new} against {old}'))
        return rep
    if isinstance(old, bool) or isinstance(new, bool) or not (is_num(old) and is_num(new)):
        if new != old:
            rep.fail.append((path, f'{new!r} against {old!r}'))
        return rep
    if eq_float(new, old):
        return rep
    if mode == 'bitwise':
        rep.fail.append((path, f'{new!r} against {old!r}'))
        return rep
    floor = DIAG_FLOOR if key in ROUNDOFF else 0.0
    d = abs(new - old)
    tol = max(REL * abs(old), floor)
    if d <= tol:
        rep.diff.append((path, f'moved by {d:.2e}'))
        if d > REL * abs(old):
            rep.floor_used.append(path)
    else:
        rep.fail.append((path, f'{new!r} against {old!r}, tolerance {tol:.2e}'))
    return rep


def compare_npy(new_path, old_path):
    a, b = np.load(new_path), np.load(old_path)
    return bool(a.shape == b.shape and np.array_equal(a, b, equal_nan=True))


def add_new_fields(rec):
    """A baseline record dressed with the listed new fields, as a revised run writes them (the green parent)."""
    r = copy.deepcopy(rec)

    def walk(o):
        if isinstance(o, dict):
            if 'residual' in o and 'gauge_multipliers' not in o:
                o['gauge_multipliers'] = [0.0]
            if 'verdict' in o and 'dt' in o and 'N_obs' not in o:
                o.update(N_obs=int(round(1 / o['dt'])), N_step=int(round(1000.0 / o['dt'])), T_int=0.0)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(r)
    return r


def selftest(base):
    """The comparator's mutation arms on M8.15's own records: each must be flagged, after a green parent."""
    lin = json.load(open(os.path.join(base, 'controls_first_2026-10-07', 'linear_L3.json')))
    dyn = json.load(open(os.path.join(base, 'controls_first_2026-10-07', 'dynamics_C2a.json')))
    br = json.load(open(os.path.join(base, 'branch_C3_R4.json')))
    out = []

    def arm(label, old, mode, mutate, expect_flag=True):
        new = add_new_fields(old)
        if mutate:
            mutate(new)
        rep = compare(new, old, mode)
        flagged = rep.outcome() == 'FAIL'
        out.append(dict(arm=label, outcome=rep.outcome(), ok=bool(flagged == expect_flag),
                        first=(rep.fail[:1] or rep.diff[:1])))

    pt = lambda r: r['C2a']['points'][0]
    arm('parent: linear_L3 with the new fields, bitwise', lin, 'bitwise', None, expect_flag=False)
    arm('parent: dynamics_C2a with the new fields, bitwise', dyn, 'bitwise', None, expect_flag=False)
    arm('parent: branch_C3_R4 with the new fields, branch mode', br, 'branch', None, expect_flag=False)
    arm('a sigma moved by one ulp (bitwise)', lin, 'bitwise', lambda r: pt(r).__setitem__('sigma', np.nextafter(pt(r)['sigma'], np.inf)))
    arm('an unlisted key added', lin, 'bitwise', lambda r: pt(r).__setitem__('extra_field', 1))
    arm('a key removed', lin, 'bitwise', lambda r: pt(r).pop('omega_gram'))
    arm('an iteration count moved', lin, 'bitwise', lambda r: pt(r).__setitem__('newton_it', pt(r)['newton_it'] + 1))
    arm('a residual past its bound', lin, 'bitwise', lambda r: pt(r).__setitem__('residual', pt(r)['residual'] + 3e-13))
    arm('an eigenvalue component moved by one ulp (bitwise)', lin, 'bitwise',
        lambda r: pt(r)['all_slow'][3].__setitem__(1, float(np.nextafter(pt(r)['all_slow'][3][1], np.inf))))
    arm('a persistence diagnostic moved by one ulp (bitwise)', dyn, 'bitwise', lambda r: r.__setitem__('max_dref', float(np.nextafter(r['max_dref'], np.inf))))
    arm('a categorical value changed', dyn, 'bitwise', lambda r: r.__setitem__('verdict', 'Fails'))
    p3 = lambda r: r['points'][2]
    arm('branch: sigma moved by 2e-9 relative', br, 'branch', lambda r: p3(r).__setitem__('sigma', p3(r)['sigma'] * (1 + 2e-9)))
    arm('branch: sigma moved by 0.5e-9 relative (within)', br, 'branch', lambda r: p3(r).__setitem__('sigma', p3(r)['sigma'] * (1 + 0.5e-9)), expect_flag=False)
    arm('branch: a complex value moved past its floor', br, 'branch',
        lambda r: p3(r)['genuine_all'][0][0].__setitem__(0, p3(r)['genuine_all'][0][0][0] + 1e-3))
    arm('branch: a type changed', br, 'branch', lambda r: r['types'][0].__setitem__('type', 'Elliptic') if r.get('types') else None)
    arm('branch: a lifted eigenvalue moved by 5e-13 (within the absolute floor)', br, 'branch',
        lambda r: p3(r)['lifted'][0].__setitem__(0, p3(r)['lifted'][0][0] + 5e-13), expect_flag=False)
    arm('branch: a lifted eigenvalue moved by 5e-12 (past the floor)', br, 'branch',
        lambda r: p3(r)['lifted'][0].__setitem__(0, p3(r)['lifted'][0][0] + 5e-12))
    arm('branch: a round-off Krein value moved by 5e-12 (within its floor)', br, 'branch',
        lambda r: p3(r)['genuine_all'][0].__setitem__(1, p3(r)['genuine_all'][0][1] + 5e-12), expect_flag=False)
    arm('branch: a Krein value moved by 2e-11 (past its floor)', br, 'branch',
        lambda r: p3(r)['genuine_all'][0].__setitem__(1, p3(r)['genuine_all'][0][1] + 2e-11))
    arm('branch: backward_error moved by 5e-12 (within its floor)', br, 'branch',
        lambda r: p3(r).__setitem__('backward_error', p3(r)['backward_error'] + 5e-12), expect_flag=False)
    arm('branch: backward_error moved by 2e-11 (past its floor)', br, 'branch',
        lambda r: p3(r).__setitem__('backward_error', p3(r)['backward_error'] + 2e-11))
    return out


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(here, 'qual_2026-10-09', 'baseline')
    if sys.argv[1:] == ['selftest']:
        res = selftest(base)
        for r in res:
            print(f"  {'ok ' if r['ok'] else 'BAD'}  {r['arm']}: {r['outcome']}  {r['first']}")
        print('comparator self-test:', 'PASS' if all(r['ok'] for r in res) else 'FAIL')
