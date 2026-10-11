"""M8.15.x: the amendment of 2026-10-09T00:42:42Z (REGISTER_1.md): a root's kind from nu's sign, and the carry's record
and wiring. Checks (a) to (f) as registered, with their mutation arms; (d) reruns the carry's tests as
control_carry_kind.*, so the first run's record stays as it is. Writes control_kind.json and control_kind.log."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, time, datetime, copy, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
sys.path.insert(0, HERE)
from angle import angle_solve, kind_of, AngleBranch, NU_TOL
from control_carry import SynthCircle, mod_dist, NOTMIN

PI = np.pi
P5_P = 2 * PI / 5
NEW = ('maximum', 'minimum', 'kind', 'kind_H', 'ends', 'source')


def strip(o, keys=NEW):
    if isinstance(o, dict):
        return {k: strip(v, keys) for k, v in o.items() if k not in keys}
    if isinstance(o, list):
        return [strip(v, keys) for v in o]
    return o


def roots_view(rec):
    return [dict(theta=r['theta'], kind=r['kind'], kind_H=r['kind_H'], source=r['source'], H=r['H'], nu=r['nu'])
            for r in rec['roots']]


def main():
    t0 = time.time()
    R = {}
    ref = json.load(open(os.path.join(HERE, 'control_1b.json')))
    from m815_common import LevelCase
    lc = LevelCase(2, 'P5', 4)
    m0 = 0.25 / (lc.Q / lc.vol) / 120
    # (a) the pyramid's full rule at theta_start = 0
    rec, _, _ = angle_solve(lc, m0, lc.lam0 + 0.25, theta_start=0.0)
    R['a'] = dict(roots=roots_view(rec), selected=rec['selected'] and dict(theta=rec['selected']['theta'],
                  H=rec['selected']['H'], sigma=rec['selected']['sigma']), ref_selected=dict(
                  H=ref['one_period']['selected']['H'], sigma=ref['one_period']['selected']['sigma']),
                  grid=[dict(theta=g['theta'], nu=g['nu'], H=g['H']) for g in rec['grid']])
    # (b) synthetic -cos theta, grid from 0
    C = SynthCircle(lambda t, e: -np.cos(t), lambda t, e: np.sin(t))
    recb, _, _ = angle_solve(C, 0.0, 0.0, theta_start=0.0)
    R['b'] = dict(roots=roots_view(recb))
    # (c) a flipped convention on control 1b's recorded grid
    g = ref['one_period']['grid']
    samples = [(x['theta'], x['nu']) for x in g]
    gH = {round(x['theta'], 12): x['H'] for x in g}
    rows = []
    for r in ref['one_period']['roots']:
        ends = [gH[round(t, 12)] for t in r['interval']]
        rows.append(dict(theta=r['theta'], H=r['H'], ends=ends,
                         plain=kind_of(r['theta'], r['H'], samples, ends, P5_P)[0],
                         flipped=kind_of(r['theta'], r['H'], samples, ends, P5_P, convention=-1.0)[0],
                         flipped_no_H=kind_of(r['theta'], r['H'], samples, [], P5_P, convention=-1.0)[0]))
    R['c'] = dict(roots=rows)
    # (d) part 1: section 1b's angle solve against control 1b's record
    same = {}
    for n, key in ((1, 'one_period'), (2, 'two_periods')):
        r1, _, _ = angle_solve(lc, m0, lc.lam0 + 0.25, theta_start=PI / 10, n_periods=n)
        r1 = json.loads(json.dumps(r1, default=float))
        gHk = {round(x['theta'], 12): x['H'] for x in ref[key]['grid']}
        old_kind = lambda x, e: 'min' if all(x['H'] < h for h in e) else ('max' if all(x['H'] > h for h in e) else '-')
        kinds_old = [old_kind(x, [gHk[round(t, 12)] for t in x['interval']]) for x in ref[key]['roots']]
        kinds_new = [x['kind'] if x['kind'] in ('min', 'max') else '-' for x in r1['roots']]
        same[key] = dict(identical_but_new_fields=strip(r1) == strip(ref[key]), kinds_old=kinds_old, kinds_new=kinds_new,
                         selected_same=r1['selected']['theta'] == ref[key]['selected']['theta'])
    R['d1b'] = same
    # (e) an end inside a bisection: a kicked carry inside goto
    from continuation import ladder
    br = AngleBranch(lc, theta_start=PI / 10)
    br.run(ladder(0.25, 0.3536))
    before = [id(x) for x in br.accepted]
    n_before = len(br.accepted)
    kicked = []
    br.perturb = lambda b: (kicked.append(1) or -0.45 * P5_P) if not kicked else 0.0
    got = br.goto(0.5, br.accepted[-1])
    R['e'] = dict(returned=None if got is None else 'a point', events=br.events, accepted_unchanged=(
        [id(x) for x in br.accepted] == before and len(br.accepted) == n_before), end=list(br.end) if br.end else None,
        n_accepted=n_before)
    # (d) part 2 and (f): the carry's tests rerun under the amendment
    subprocess.run([sys.executable, os.path.join(HERE, 'control_carry.py'), '--tag', 'kind'], check=True)
    new = json.load(open(os.path.join(HERE, 'control_carry_kind.json')))
    old = json.load(open(os.path.join(HERE, 'control_carry.json')))
    R['d_carry'] = dict(
        checks=[c['passed'] for c in new['checks']], ends_old={k: old['synthetic'][k]['end'] and old['synthetic'][k]['end']['reason']
        for k in old['synthetic']} | {a: old[a]['end'][0] for a in ('arm1', 'arm2', 'arm3')},
        ends_new={k: new['synthetic'][k]['end'] and new['synthetic'][k]['end']['reason'] for k in new['synthetic']}
        | {a: new[a]['end'][0] for a in ('arm1', 'arm2', 'arm3')},
        sel_old={a: [round(x['phys'], 6) for x in old[a]['accepted']] for a in ('arm1', 'arm2', 'arm3')},
        sel_new={a: [round(x['phys'], 6) for x in new[a]['accepted']] for a in ('arm1', 'arm2', 'arm3')},
        max_dtheta={a: (max(abs(x['phys'] - y['phys']) for x, y in zip(old[a]['accepted'], new[a]['accepted']))
                        if len(old[a]['accepted']) == len(new[a]['accepted']) else float('inf')) for a in ('arm1', 'arm2', 'arm3')},
        solves_old={a: old[a]['n_solves'] for a in ('arm1', 'arm2', 'arm3')},
        solves_new={a: new[a]['n_solves'] for a in ('arm1', 'arm2', 'arm3')},
        others_kinds_new=[(o['kind'], o['alive']) for o in new['arm3']['others']])
    R['f'] = dict(end=new['arm1']['end'])
    checks = evaluate(R)
    muts = mutations(R)
    summary = dict(test='the kind rule and the carry record (REGISTER_1.md, amendment of 2026-10-09T00:42:42Z)',
                   written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                   seconds=round(time.time() - t0, 1), checks=[dict(check=c, passed=bool(ok)) for c, ok in checks],
                   all_passed=all(ok for _, ok in checks), mutations=muts,
                   all_mutations_caught=all(m['caught'] for m in muts), **R)
    json.dump(summary, open(os.path.join(HERE, 'control_kind.json'), 'w'), indent=1, default=float)
    L = [f'M8.15.x, the kind rule and the carry record: {summary["written"]}, {summary["seconds"]} s', '']
    L.append('(a) pyramid, theta_start = 0: ' + '; '.join(f'{r["theta"]:.12f} {r["kind"]} (H test {r["kind_H"]}, {r["source"]})'
                                                     for r in R['a']['roots'])
             + f'; selected {R["a"]["selected"]}')
    L.append('(b) synthetic -cos, grid from 0: ' + '; '.join(f'{r["theta"]:.12f} {r["kind"]} ({r["source"]})' for r in R['b']['roots']))
    L.append('(c) 1b grid: ' + '; '.join(f'{r["theta"]:.9f} plain {r["plain"]}, flipped {r["flipped"]}, flipped without H {r["flipped_no_H"]}'
                                       for r in R['c']['roots']))
    L.append(f'(d) 1b angle solve: {R["d1b"]}')
    L.append(f'(d) carry rerun: checks {R["d_carry"]["checks"]}; ends {R["d_carry"]["ends_new"]}; max change in the physical '
             f'angle {R["d_carry"]["max_dtheta"]}; Newton solves {R["d_carry"]["solves_old"]} -> {R["d_carry"]["solves_new"]}')
    L.append(f'(e) goto with a kick: returned {R["e"]["returned"]}; events {R["e"]["events"]}; accepted unchanged {R["e"]["accepted_unchanged"]}')
    L.append(f'(f) arm 1 end: {R["f"]["end"]}')
    L.append('')
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {summary["all_passed"]}')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  check {m["check"]}: {m["mutation"]}' for m in muts]
    L.append(f'every mutation caught by its own check alone: {summary["all_mutations_caught"]}')
    open(os.path.join(HERE, 'control_kind.log'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))


def evaluate(R):
    a = R['a']
    mx = [r for r in a['roots'] if r['kind'] == 'max']
    mn = [r for r in a['roots'] if r['kind'] == 'min']
    rel = lambda x, y: abs(x - y) / abs(y)
    ok_a = (len(a['roots']) == 2 and len(mx) == 1 and len(mn) == 1 and mod_dist(mx[0]['theta'], 0.0, P5_P) <= 1e-9
            and mod_dist(mn[0]['theta'], PI / 5, P5_P) <= 1e-9 and a['selected'] is not None
            and mod_dist(a['selected']['theta'], PI / 5, P5_P) <= 1e-9
            and rel(a['selected']['H'], a['ref_selected']['H']) <= 1e-12 and rel(a['selected']['sigma'], a['ref_selected']['sigma']) <= 1e-12)
    b = R['b']['roots']
    ok_b = (len(b) == 2 and [r['kind'] for r in sorted(b, key=lambda r: r['theta'] % (2 * PI))] == ['min', 'max']
            and mod_dist(sorted(b, key=lambda r: r['theta'] % (2 * PI))[0]['theta'], 0.0, 2 * PI) <= 1e-12
            and mod_dist(sorted(b, key=lambda r: r['theta'] % (2 * PI))[1]['theta'], PI, 2 * PI) <= 1e-12)
    c = R['c']['roots']
    ok_c = len(c) == 2 and all(r['flipped'] == 'unresolved' for r in c) and sorted(r['plain'] for r in c) == ['max', 'min']
    d = R['d1b']
    ok_d1 = all(v['identical_but_new_fields'] and v['kinds_old'] == v['kinds_new'] and v['selected_same'] for v in d.values())
    dc = R['d_carry']
    ok_d2 = (all(dc['checks']) and len(dc['checks']) == 10 and dc['ends_old'] == dc['ends_new']
             and all(v <= 1e-7 for v in dc['max_dtheta'].values()))
    e = R['e']
    ok_e = (e['returned'] is None and e['accepted_unchanged'] and len(e['events']) == 1 and e['events'][0]['event'] == NOTMIN)
    f = R['f']['end']
    ok_f = isinstance(f[1], dict) and 'm_tried' in f[1] and f[1]['m_tried'] > f[1]['m']
    return [('(a) the pyramid at theta_start = 0: 0 a maximum and pi/5 a minimum, each once; pi/5 selected, matching 1b', ok_a),
            ('(b) synthetic -cos from 0: a minimum at 0 and a maximum at pi, each once', ok_b),
            ('(c) a flipped convention on 1b\'s grid leaves both roots unresolved', ok_c),
            ('(d) 1b\'s angle solve reproduces its roots, kinds and selection', ok_d1),
            ('(d) the carry\'s ten checks pass again, with the same ends and angles within 1e-7', ok_d2),
            ('(e) an end inside goto returns no point, is recorded, and leaves the accepted points', ok_e),
            ('(f) arm 1\'s end records a trial norm above the last accepted one', ok_f)]


def mutations(R):
    def old_rule_a(r):
        # the H-only rule on the same samples: each grid-point root's interval has the root itself as one end
        for x in r['a']['roots']:
            x['kind'] = 'min' if x['H'] < x['H'] else ('max' if x['H'] > x['H'] else 'unresolved')
        r['a']['selected'] = None
    arms = [
        (0, '(a) the H-only rule, which classifies neither grid-point root', old_rule_a),
        (1, '(b) a grid-point root entered twice', lambda r: r['b']['roots'].append(dict(r['b']['roots'][0]))),
        (1, '(b) reversed neighbour signs', lambda r: [x.__setitem__('kind', {'min': 'max', 'max': 'min'}[x['kind']]) for x in r['b']['roots']]),
        (2, '(c) no H cross-check, so the flipped convention classifies', lambda r: [x.__setitem__('flipped', x['flipped_no_H']) for x in r['c']['roots']]),
        (3, '(d) a kind changed in the 1b regression', lambda r: r['d1b']['one_period']['kinds_new'].reverse()),
        (4, '(d) one of the carry\'s checks failing', lambda r: r['d_carry']['checks'].__setitem__(6, False)),
        (4, '(d) an end reason changed', lambda r: r['d_carry']['ends_new'].__setitem__('arm1', 'eps_max')),
        (5, '(e) the bisection step returning a point', lambda r: r['e'].__setitem__('returned', 'a point')),
        (5, '(e) the accepted points changed', lambda r: r['e'].__setitem__('accepted_unchanged', False)),
        (6, '(f) no trial norm', lambda r: r['f']['end'][1].pop('m_tried')),
    ]
    parent = [ok for _, ok in evaluate(R)]
    out = []
    for k, label, fn in arms:
        r = copy.deepcopy(R)
        fn(r)
        got = [ok for _, ok in evaluate(r)]
        out.append(dict(check=k + 1, mutation=label, verdicts=got,
                        caught=bool(parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k))))
    return out


if __name__ == '__main__':
    main()
