"""M8.15.x: the angle carried along a branch, and its tests (REGISTER_1.md, amendment of 2026-10-08T23:57:20Z).

  synthetic: the carry rule (carry_solve, track_others) on analytic circles, nu = -dH/dtheta, period 2 pi;
  pyramid:   AngleBranch on P5 in R4 at level 2, ladder eps_min to 2, first point's grid from pi/10:
             1 past the basin (a kick at the third ladder step), 2 a moving coordinate, 3 both critical points;
  then the registered checks and their mutation arms.

  python3 control_carry.py      # writes control_carry.json and control_carry.log"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, time, datetime, copy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
from angle import angle_solve, carry_solve, track_others, CarryEnd, AngleBranch, N_GRID

PI = np.pi
TWO_PI = 2 * PI
W = TWO_PI / N_GRID                       # the synthetic circles' grid spacing
SYNTH_START = 0.05                        # the synthetic first grids' start: off every root (a grid point on a root
                                          # cannot be classified by the rule's interval test)
P5_P = 2 * PI / 5
SCHEDULE = (0.0, 0.05, -0.03, 0.06, -0.02, 0.04, -0.01)    # arm 2's delta_k, in periods, as registered
KICK = (2, -0.45)                         # arm 1: at ladder step k = 2 (the third), the carried angle moves by -0.45 P
LOST = 'the carried root is lost: no minimum within two grid spacings'
NOTMIN = 'the carried root is not a minimum'


class SynthCircle:
    def __init__(self, H, dH, period=TWO_PI):
        self.H, self.dH, self.period = H, dH, period
        self.ax, self.order = (0.0, 0.0, 1.0), 1
        self.offset, self.n_solves, self.last_roots = 0.0, 0, []

    def solve(self, theta, m, sigma0, start=None):
        self.n_solves += 1
        t = theta + self.offset
        return dict(theta=float(theta), nu=float(-self.dH(t, m)), mu=0.0, sigma=float(sigma0), H=float(self.H(t, m)),
                    it=0, full=0.0, res=0.0, Phi=None)

    def classes(self, mins):
        return list(range(len(mins))), {}


def synth_run(H, dH, eps_list):
    C = SynthCircle(H, dH)
    rec, _, _ = angle_solve(C, eps_list[0], 0.0, theta_start=SYNTH_START)
    roots = [r for r in C.last_roots if r['resolved']]
    s = next(r for r in roots if r['theta'] == rec['selected']['theta'])
    others = [dict(label=f'other {i}', kind='min' if r['minimum'] else 'max', theta=r['theta'], start=None, alive=True,
                   rows=[]) for i, r in enumerate(x for x in roots if x is not s and (x['minimum'] or x['maximum']))]
    pts, events, end, theta = [dict(eps=eps_list[0], theta=s['theta'], fallback=False, H=s['H'])], [], None, s['theta']
    for e in eps_list[1:]:
        try:
            r = carry_solve(C, e, 0.0, theta, kind='min')
        except CarryEnd as ce:
            end = dict(reason=ce.reason, eps=e, theta=ce.theta)
            break
        theta = r['theta']
        pts.append(dict(eps=e, theta=theta, fallback=bool(r['fallback']), H=r['H']))
        track_others(C, e, 0.0, others, r['H'], events, e)
    return dict(points=pts, events=events, end=end, n_solves=C.n_solves,
                others=[dict(label=o['label'], kind=o['kind'], alive=o['alive'], rows=o['rows']) for o in others])


SYNTH = {
    '1a': (lambda t, e: -np.cos(t - 1.5 * W * e), lambda t, e: np.sin(t - 1.5 * W * e), [0, 1, 2, 3, 4, 5]),
    '1b': (lambda t, e: -np.cos(t - 2.5 * W * e), lambda t, e: np.sin(t - 2.5 * W * e), [0, 1, 2, 3, 4, 5]),
    '2': (lambda t, e: -np.cos(t) + e * t, lambda t, e: np.sin(t) + e, [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05]),
    '3': (lambda t, e: -np.cos(2 * t) - e * np.cos(t), lambda t, e: 2 * np.sin(2 * t) + e * np.sin(t),
          [-0.5, -0.3, -0.1, 0.1, 0.3, 0.5]),
    '4': (lambda t, e: -(1 - e) * np.cos(t), lambda t, e: (1 - e) * np.sin(t), [0, 0.4, 0.8, 1.2]),
}


def mod_dist(a, b, P):
    return abs(((a - b) + P / 2) % P - P / 2)


class ArmBranch(AngleBranch):
    """AngleBranch with the controls' hooks: the moving coordinate's schedule (set at each ladder step) and arm 1's
    kick (added once to the carried coordinate at the first carry solve of its ladder step)."""
    def __init__(self, lc, schedule=None, kick=None, **kw):
        super().__init__(lc, **kw)
        self.k, self.schedule, self.kick, self.kicked = -1, schedule, kick, False
        if kick is not None:
            self.perturb = lambda br: self._kick()

    def solve_target(self, eps_k, first_step=False):
        self.k += 1
        if self.schedule is not None:
            self.C.offset = self.schedule[self.k] * self.C.period
        return super().solve_target(eps_k, first_step=first_step)

    def _kick(self):
        if self.k == self.kick[0] and not self.kicked:
            self.kicked = True
            return self.kick[1] * self.C.period
        return 0.0


def pyramid_arm(lc, **kw):
    from continuation import ladder
    t0 = time.time()
    br = ArmBranch(lc, theta_start=PI / 10, **kw)
    br.run(ladder(0.25, 2.0))
    acc = [{k: (v if not isinstance(v, (list, np.ndarray)) or k in ('nu', 'mu') else None) for k, v in r.items() if k != 'x'}
           for r in br.accepted]
    for r in acc:
        r['nu'], r['mu'] = float(r['nu'][0]), float(r['mu'][0])
    return dict(end=[br.end[0], br.end[1]], accepted=acc, k_last=br.k, kicked=br.kicked, events=br.events,
                sel_rows=br.sel_rows,
                others=[dict(label=o['label'], kind=o['kind'], alive=o['alive'], rows=o['rows']) for o in br.others],
                first_selected=br.first_grid['selected']['theta'], n_solves=br.C.n_solves,
                seconds=round(time.time() - t0, 1))


def evaluate(R):
    S, A1, A2, A3 = R['synthetic'], R['arm1'], R['arm2'], R['arm3']
    c = []
    p = S['1a']['points']
    c.append(('synthetic 1a: carried to 1.5 w eps within 1e-9, by the fallback after the first step, no end',
              S['1a']['end'] is None and len(p) == 6 and all(mod_dist(x['theta'], 1.5 * W * x['eps'], TWO_PI) <= 1e-9 for x in p)
              and all(x['fallback'] for x in p[1:])))
    c.append(('synthetic 1b: ends "lost" at eps = 1',
              S['1b']['end'] is not None and S['1b']['end']['reason'] == LOST and S['1b']['end']['eps'] == 1))
    p = S['2']['points']
    c.append(('synthetic 2: carried to -arcsin(eps) within 1e-9 through 0.9, then ends "lost" at 1.05',
              len(p) == 7 and all(mod_dist(x['theta'], -np.arcsin(x['eps']), TWO_PI) <= 1e-9 for x in p)
              and S['2']['end'] is not None and S['2']['end']['reason'] == LOST and S['2']['end']['eps'] == 1.05))
    p, ev = S['3']['points'], [e for e in S['3']['events'] if e['event'] == 'no longer the lowest minimum']
    c.append(('synthetic 3: carried at pi within 1e-9 throughout, "no longer the lowest minimum" first at 0.1',
              S['3']['end'] is None and len(p) == 6 and all(mod_dist(x['theta'], PI, TWO_PI) <= 1e-9 for x in p)
              and len(ev) == 1 and ev[0]['at'] == 0.1))
    p = S['4']['points']
    c.append(('synthetic 4: carried at 0 through 0.8, then ends "not a minimum" at 1.2',
              len(p) == 3 and all(mod_dist(x['theta'], 0.0, TWO_PI) <= 1e-9 for x in p)
              and S['4']['end'] is not None and S['4']['end']['reason'] == NOTMIN and S['4']['end']['eps'] == 1.2))
    a = A1['accepted']
    c.append(('pyramid 1: ends "not a minimum" at the kicked third ladder step, every accepted point at pi/5',
              A1['end'][0] == NOTMIN and A1['kicked'] and A1['k_last'] == KICK[0]
              and all(mod_dist(x['phys'], PI / 5, P5_P) <= 1e-7 for x in a)))
    a = A2['accepted']
    c.append(('pyramid 2: the coordinate follows pi/5 - delta_k and the physical angle stays at pi/5, within 1e-7',
              A2['end'][0] == 'eps_max' and any(x['offset'] != 0 for x in a)
              and all(mod_dist(x['phys'], PI / 5, P5_P) <= 1e-7 and mod_dist(x['theta'], PI / 5 - x['offset'], P5_P) <= 1e-7
                      for x in a)))
    c.append(('pyramid 2: |nu|, |mu| <= 1e-12 and no fallback at every accepted point',
              all(abs(x['nu']) <= 1e-12 and abs(x['mu']) <= 1e-12 and not x['fallback'] for x in a)))
    a, o, sr = A3['accepted'], A3['others'], A3['sel_rows']
    mx = [t for t in o if t['kind'] == 'max']
    rows = mx[0]['rows'] if len(mx) == 1 else []
    paired = len(rows) > 0 and [r['at'] for r in rows] == [r['at'] for r in sr[:len(rows)]]
    geometry = (len(mx) == 1 and paired and all(mod_dist(r['phys'], 0.0, P5_P) <= 1e-7 for r in rows)
                and all(mod_dist(x['phys'], PI / 5, P5_P) <= 1e-7 for x in a)
                and all(mod_dist(r['phys'], PI / 5, P5_P) <= 1e-7 for r in sr))
    no_swap = paired and all(s['H'] < r['H'] for s, r in zip(sr, rows))
    c.append(('pyramid 3: minimum at pi/5 and maximum at 0 at every ladder point, within 1e-7',
              (A3['end'][0] == 'eps_max' and len(rows) == 7 and geometry) if no_swap else geometry))
    c.append(('pyramid 3: the minimum stays below the maximum, or the swap is caught as registered',
              bool((no_swap and mx and mx[0]['alive']) or (not no_swap and A3['end'][0] == NOTMIN))))
    return c


def mutations(R):
    arms = [
        (0, 'synthetic 1a: a point moved by 2e-9', lambda r: r['synthetic']['1a']['points'][3].__setitem__('theta', r['synthetic']['1a']['points'][3]['theta'] + 2e-9)),
        (0, 'synthetic 1a: a step without the fallback', lambda r: r['synthetic']['1a']['points'][2].__setitem__('fallback', False)),
        (1, 'synthetic 1b: the end one step later', lambda r: r['synthetic']['1b']['end'].__setitem__('eps', 2)),
        (2, 'synthetic 2: the end reason changed', lambda r: r['synthetic']['2']['end'].__setitem__('reason', NOTMIN)),
        (2, 'synthetic 2: a point moved by 2e-9', lambda r: r['synthetic']['2']['points'][5].__setitem__('theta', r['synthetic']['2']['points'][5]['theta'] + 2e-9)),
        (3, 'synthetic 3: the event one step later', lambda r: [e.__setitem__('at', 0.3) for e in r['synthetic']['3']['events'] if e['event'] == 'no longer the lowest minimum']),
        (3, 'synthetic 3: a re-selection onto 0', lambda r: r['synthetic']['3']['points'][4].__setitem__('theta', 0.0)),
        (4, 'synthetic 4: ended "lost" instead', lambda r: r['synthetic']['4']['end'].__setitem__('reason', LOST)),
        (5, 'pyramid 1: reaches eps_max instead', lambda r: r['arm1']['end'].__setitem__(0, 'eps_max')),
        (5, 'pyramid 1: an accepted point at the maximum', lambda r: r['arm1']['accepted'][-1].__setitem__('phys', 0.0)),
        (6, 'pyramid 2: a coordinate off by 2e-7', lambda r: r['arm2']['accepted'][-1].__setitem__('theta', r['arm2']['accepted'][-1]['theta'] + 2e-7)),
        (6, 'pyramid 2: the coordinate never moved', lambda r: [x.__setitem__('offset', 0.0) for x in r['arm2']['accepted']]),
        (7, 'pyramid 2: nu at 2e-12', lambda r: r['arm2']['accepted'][3].__setitem__('nu', 2e-12)),
        (7, 'pyramid 2: a fallback used', lambda r: r['arm2']['accepted'][3].__setitem__('fallback', True)),
        (8, 'pyramid 3: the maximum off by 2e-7', lambda r: r['arm3']['others'][[o['kind'] for o in r['arm3']['others']].index('max')]['rows'][4].__setitem__('phys', 2e-7)),
        (9, 'pyramid 3: a swap that was not caught', lambda r: r['arm3']['others'][[o['kind'] for o in r['arm3']['others']].index('max')]['rows'][4].__setitem__('H', -1.0)),
    ]
    parent = [ok for _, ok in evaluate(R)]
    out = []
    for k, label, f in arms:
        r = copy.deepcopy(R)
        f(r)
        got = [ok for _, ok in evaluate(r)]
        out.append(dict(check=k + 1, mutation=label, verdicts=got,
                        caught=bool(parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k))))
    return parent, out


def main(tag=''):
    t0 = time.time()
    R = dict(synthetic={k: synth_run(*v) for k, v in SYNTH.items()})
    from m815_common import LevelCase
    lc = LevelCase(2, 'P5', 4)
    R['arm1'] = pyramid_arm(lc, kick=KICK)
    R['arm2'] = pyramid_arm(lc, schedule=SCHEDULE)
    R['arm3'] = pyramid_arm(lc, track=True)
    checks = evaluate(R)
    parent, muts = mutations(R)
    summary = dict(test='the carry', register='REGISTER_1.md, amendment of 2026-10-08T23:57:20Z',
                   written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                   seconds=round(time.time() - t0, 1), checks=[dict(check=c, passed=bool(ok)) for c, ok in checks],
                   all_passed=all(ok for _, ok in checks), mutations=muts,
                   all_mutations_caught=all(m['caught'] for m in muts), harness=dict(synth_start=SYNTH_START, kick=KICK,
                   schedule=SCHEDULE), **R)
    with open(os.path.join(HERE, f'control_carry{tag}.json'), 'w') as f:
        json.dump(summary, f, indent=1, default=float)
    L = [f'M8.15.x, the carry: {summary["written"]}, {summary["seconds"]} s', '']
    for k, s in R['synthetic'].items():
        L.append(f'synthetic {k}: ' + ', '.join(f'{x["eps"]:g}:{x["theta"]:.10f}{"*" if x["fallback"] else ""}' for x in s['points'])
                 + f'; end {s["end"]}; events {[(e["at"], e["track"], e["event"]) for e in s["events"]]}')
    for a in ('arm1', 'arm2', 'arm3'):
        A = R[a]
        L.append(f'pyramid {a[-1]}: end {A["end"]}, {len(A["accepted"])} accepted points, {A["n_solves"]} Newton solves, '
                 f'{A["seconds"]} s; first selected {A["first_selected"]:.12f}')
        for x in A['accepted']:
            L.append(f'    eps {x["eps"]:.6f}  coord {x["theta"]:.10f}  phys {x["phys"]:.10f}  offset {x["offset"]:+.6f}  '
                     f'nu {x["nu"]:+.2e}  mu {x["mu"]:+.2e}  H {x["H"]:.13f}  fallback {x["fallback"]}  solves {x["n_solves"]}')
        for o in A['others']:
            L.append(f'    tracked {o["label"]} ({o["kind"]}), alive {o["alive"]}: ' +
                     ', '.join(f'{r["at"]:.4g}: {r["phys"]:.10f} H {r["H"]:.13f}' for r in o['rows']))
        if A['events']:
            L.append(f'    events {A["events"]}')
    L.append('')
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {summary["all_passed"]}')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  check {m["check"]}: {m["mutation"]}' for m in muts]
    L.append(f'every mutation caught by its own check alone: {summary["all_mutations_caught"]}')
    with open(os.path.join(HERE, f'control_carry{tag}.log'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main('_' + sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--tag' else '')
