"""REGISTER_4.md v3 § 3: the real-solver controls R1 to R5 (R4b included), on orbits that are not targets.

  python3 tests/real.py r4b                    the nine Unresolved reasons on constructed pairs, with the binding arms
  python3 tests/real.py r5 TERMS               the guard's validation on a scratch copy of the instrument's folder
  python3 tests/real.py run NAME               one driver run: c2a (R1 and R4), c3 (R2 and R4), r3, r3arm, r1arm
  python3 tests/real.py evaluate QUALDIR       every expectation and arm, read from the records; QUALDIR holds the
                                               qualification's branch records (branch_C3_R4.json, branch_C2a_R4.json)
Records: out/t1_*.json from the driver; out/r4b.json, out/r5.json; out/real.json and out/real.log from evaluate."""
import os, sys, json, copy, shutil, subprocess, datetime, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import numpy as np
import locate

OUT = os.path.join(ROOT, 'out')
L = dict(e11=11.313708498984761, e16=16.0, e32=32.0, e45=45.254833995939045)
RUNS = {
    'c2a': ['C2a', '4', '--bracket3', str(L['e32']), str(L['e45']), '--bracket2', str(L['e11']), str(L['e16']),
            '--region', str(L['e11']), str(L['e45']), '--full-ladder', '--test-arm-dlev0', '--tag', '_R1R4'],
    'c3': ['C3', '4', '--bracket3', str(L['e11']), str(L['e16']), '--bracket2', str(L['e11']), str(L['e16']),
           '--region', str(L['e11']), str(L['e16']), '--full-ladder', '--test-arm-dlev0', '--tag', '_R2R4'],
    'r3': ['C2a', '4', '--bracket3', str(L['e11']), str(L['e16']), '--bracket2', str(L['e11']), str(L['e16']),
           '--region', str(L['e11']), str(L['e16']), '--test-levels', '2', '--test-maxit', '2', 'bisection', '0', '1',
           '--tag', '_R3'],
    'r3arm': ['C2a', '4', '--bracket3', str(L['e11']), str(L['e16']), '--bracket2', str(L['e11']), str(L['e16']),
              '--region', str(L['e11']), str(L['e16']), '--test-levels', '2', '--tag', '_R3arm'],
    'r1arm': ['C2a', '4', '--bracket3', str(L['e11']), str(L['e16']), '--bracket2', str(L['e11']), str(L['e16']),
              '--region', str(L['e11']), str(L['e16']), '--test-levels', '2', '--test-span-no-rotations',
              '--tag', '_R1arm'],
}


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def load(tag, case):
    return json.load(open(os.path.join(OUT, f't1_{case}_R4{tag}.json')))


# --- R4b: the nine Unresolved reasons on constructed pairs -------------------------------------------------------------
def r4b():
    m815 = locate.import_instrument()
    from m815_branch import Point
    from verdict import representatives, Verdict
    from m815_common import LevelCase, ladder, EPS_MAX, schedule
    fz = json.load(open(os.path.join(locate.INSTRUMENT, 'out', 'freeze_numbers.json')))
    rf3 = float(fz['r_f']['3'])
    tau0_3, dlev, s2 = 10 * rf3, float(fz['delta_lev']), float(fz['s2']['R4'])
    text, h = locate.decide_source()
    full = ladder(0.25, EPS_MAX[4])
    omega = {nm: float(np.sqrt(LevelCase(2, nm, 4).lam0)) for nm in ('C2a', 'C3')}

    class CP:
        reps = Point.reps

        def __init__(self, genuine_all, nL, nB, lifted=(1e-6,), kind=('paired',), bwe=1e-12, cluster_ok=True,
                     zero_crossing=None, balanced=None):
            self.genuine_all = genuine_all
            self.genuine = representatives(genuine_all, tau0_3)
            self.nL, self.nB_cluster = nL, nB
            self.kr, self.kc, self.kim, self.rhs = Verdict.count(self, tau0_3)
            self.balanced = (self.kr + 2 * self.kc + 2 * self.kim == self.rhs) if balanced is None else balanced
            self.fast = None
            self.zero_crossing = (any(abs(l) <= tau0_3 for l, _ in self.genuine) if zero_crossing is None
                                  else zero_crossing)
            self.cluster_ok, self.bwe = cluster_ok, bwe
            self.lifted, self.kind = np.array(lifted, complex), list(kind)

    imag = lambda w: [(1j * w, 1.0), (-1j * w, -1.0)]
    real = lambda r: [(r + 0j, 0.0), (-r + 0j, 0.0)]

    def cases(name):
        rad = (name == 'C3')
        k = ('radical',) if rad else ('paired',)
        E = lambda **kw: CP(imag(0.05), 2, 2, kind=k, **kw)
        H = lambda r=0.05, **kw: CP(real(r), 3, 2, kind=k, **kw)
        out = [
            ('Elliptic pass', 1.0, E(), E(), []),
            ('Hyperbolic pass', 1.0, H(), H(), []),
            ('a mode before its first-resolved point', 0.2, E(), E(), ['a mode before its first-resolved point']),
            ('cluster check', 1.0, E(cluster_ok=False), E(), ['cluster check']),
            ('zero crossing', 1.0, E(zero_crossing=True), E(), ['zero crossing']),
            ('Krein count unbalanced', 1.0, E(balanced=False), E(), ['Krein count unbalanced']),
            ('eigenpair residual', 1.0, E(bwe=1e-9), E(), ['eigenpair residual']),
            ('cross-level disagreement', 1.0, E(), CP(imag(0.06), 2, 2, kind=k), ['cross-level disagreement']),
            ('level stability', 1.0, H(0.05), H(0.05 + 5.5e-4), ['level stability']),
        ]
        if rad:
            out.append(('radical bound', 1.0, E(lifted=(1.0,)), E(), ['radical bound']))
        else:
            out.append(('paired lifted mode above tau0', 1.0, E(lifted=(1e-3,)), E(), ['paired lifted mode above tau0']))
        return out

    def run_cases(bind):
        res = []
        for name in ('C2a', 'C3'):
            sch = schedule(name, 4, rf3, full)
            b = dict(name=name, slot=4, tau0_3=tau0_3, s2=s2, omega0=omega[name], dlev=dlev, sch=sch)
            b.update(bind.get(name, {}) if isinstance(bind, dict) and name in bind else bind.get('all', {}))
            dec = locate.bind_decide(m815, text, **b)
            for label, e, p3, p2, want in cases(name):
                typ, why, _ = dec(e, p3, p2, True)
                res.append(dict(case=name, label=label, eps=e, type=typ, why=list(why), expected=want))
        return res

    parent = run_cases({})
    ok = []
    for r in parent:
        if r['label'] == 'Elliptic pass':
            ok.append(r['type'] == 'Elliptic' and not r['why'])
        elif r['label'] == 'Hyperbolic pass':
            ok.append(r['type'] == 'Hyperbolic' and not r['why'])
        else:
            ok.append(r['type'] == 'Unresolved' and r['why'] == r['expected'])
    parent_ok = all(ok)
    arms = {}
    for key, val in (('tau0_3', tau0_3 * 1e3), ('s2', s2 * 100), ('omega0', None), ('dlev', dlev * 10), ('sch', [])):
        if key == 'omega0':
            bind = {'C2a': dict(omega0=omega['C2a'] / 100), 'C3': dict(omega0=omega['C3'] / 100)}
        else:
            bind = {'all': {key: val}}
        mut = run_cases(bind)
        changed = [m['label'] + '/' + m['case'] for m, p in zip(mut, parent) if (m['type'], m['why']) != (p['type'], p['why'])]
        arms[key] = dict(changed=changed, caught=bool(changed))
    out = dict(stamp=now(), decide_sha256=h, omega0=omega, parent=parent, parent_ok=parent_ok,
               failed=[p for p, k in zip(parent, ok) if not k], arms=arms,
               passed=bool(parent_ok and all(a['caught'] for a in arms.values())))
    json.dump(out, open(os.path.join(OUT, 'r4b.json'), 'w'), indent=1, default=str)
    print(f'R4b: parent {"ok" if parent_ok else "FAILED"}; arms ' + ', '.join(f'{k} {"caught" if v["caught"] else "NOT caught"}'
                                                                         for k, v in arms.items()))
    return out


# --- R5: the guard's validation ---------------------------------------------------------------------------------------
R5_CODE = r'''
import sys, json, argparse
sys.path.insert(0, {root!r})
import t1_branch
if {arm!r}:
    t1_branch.freeze_values_equal = lambda fz, fn: []
ns = argparse.Namespace(case='T2', slot=4, terms={terms!r}, bracket3=None, bracket2=None, region=None,
                        ladder_only=False, full_ladder=False, tag='_R5', instrument={instr!r}, test_levels=None,
                        test_maxit=None, test_span_no_rotations=False, test_arm_dlev0=False, test_stop_after_guard=True)
try:
    r = t1_branch.run(ns, log=lambda s: None)
    print(json.dumps(dict(outcome='passed the guard', result=r)))
except SystemExit as e:
    print(json.dumps(dict(outcome='refused', message=str(e))))
'''


def r5(terms):
    import hashlib
    work = tempfile.mkdtemp(prefix='r5_')
    src = locate.INSTRUMENT
    instr = os.path.join(work, 'soft-slot-dynamics-m8-15x', 'm8_15x_solver')
    shutil.copytree(src, instr, ignore=shutil.ignore_patterns('__pycache__'))
    fn = json.load(open(os.path.join(instr, 'out', 'freeze_numbers.json')))
    th = hashlib.sha256(open(terms, 'rb').read()).hexdigest()
    good = dict(fn, frozen=True, terms_sha256=th, go='a test go (R5)', terms='R5 test terms')
    first = sorted(fn)[0]
    cases = [
        ('no FROZEN.json', None, 'refused'),
        ('one value differing', dict(good, **{first: 'changed'}), 'refused'),
        ('a terms hash that differs', dict(good, terms_sha256='0' * 64), 'refused'),
        ('an empty go', dict(good, go=''), 'refused'),
        ('complete and matching', good, 'passed the guard'),
    ]

    def run_case(content, arm=False):
        p = os.path.join(instr, 'out', 'FROZEN.json')
        if os.path.exists(p):
            os.remove(p)
        if content is not None:
            json.dump(content, open(p, 'w'), indent=1)
        code = R5_CODE.format(root=ROOT, terms=terms, instr=instr, arm=arm)
        r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
        line = [x for x in r.stdout.strip().splitlines() if x.startswith('{')]
        return json.loads(line[-1]) if line else dict(outcome='error', stderr=r.stderr[-2000:])

    res = []
    for label, content, want in cases:
        o = run_case(content)
        res.append(dict(case=label, outcome=o['outcome'], message=o.get('message'), expected=want, ok=o['outcome'] == want))
    arm = run_case(cases[1][1], arm=True)
    arm_caught = arm['outcome'] != 'refused'
    out = dict(stamp=now(), cases=res, arm=dict(case='one value differing, equality check disabled', outcome=arm['outcome'],
                                                caught=arm_caught),
               passed=bool(all(r['ok'] for r in res) and arm_caught), scratch='a temporary copy, removed afterwards')
    shutil.rmtree(work)
    json.dump(out, open(os.path.join(OUT, 'r5.json'), 'w'), indent=1, default=str)
    print('R5: ' + '; '.join(f'{r["case"]}: {r["outcome"]}' for r in res) + f'; arm {"caught" if arm_caught else "NOT caught"}')
    return out


def run(name):
    cmd = [sys.executable, os.path.join(ROOT, 't1_branch.py')] + RUNS[name]
    log = open(os.path.join(OUT, f'run_{name}.log'), 'w')
    r = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT)
    print(f'{name}: exit {r.returncode}')
    return r.returncode


# --- evaluate ----------------------------------------------------------------------------------------------------------
def br(rec, i=0):
    return rec['brackets'][i]


def r1_expect(rec, levels=(3, 2)):
    b = br(rec)
    c = []
    for lv in levels:
        st = b['levels'][str(lv)]['steps']
        c.append((f'one step at level {lv}', len(st) == 1))
        s = st[0] if st else {}
        c.append((f'structural, dnL = dnS = -2 at level {lv}', s.get('status') == 'structural' and s.get('dnL') == -2
                  and s.get('dnS') == -2 and s.get('dh') == 0))
        c.append((f'crossing eigenvectors structural at both ends, level {lv}', bool(s.get('crossings')) and all(
            x['lo_overlap'] >= 0.9 and x['hi_overlap'] >= 0.9 for x in s.get('crossings', []))))
        pts = b['points'][str(lv)]
        c.append((f'every point passes the gate (d = 3), coverage and the subspace, level {lv}',
                  all(not p['checks'] and len(p['span_singular_values']) >= 4 and p['span_singular_values'][2] >= 0.1
                      and p['span_singular_values'][3] <= 0.05 for p in pts)))
        c.append((f'named "no genuine crossing detected at level {lv}"',
                  any(n.get('name') == f'no genuine crossing detected at level {lv}' for n in b['names'])))
    return c


def r2_expect(rec):
    b = br(rec)
    c = []
    for lv in (3, 2):
        c.append((f'no step at level {lv}', len(b['levels'][str(lv)]['steps']) == 0))
        pts = b['points'][str(lv)]
        c.append((f'n(L) = 9 at every point, level {lv}', all(p['nL'] == 9 for p in pts)))
        c.append((f'every point passes the gate (d = 4), coverage and the subspace, level {lv}',
                  all(not p['checks'] and p['span_singular_values'][3] >= 0.1 for p in pts)))
        c.append((f'named "no genuine crossing detected at level {lv}"',
                  any(n.get('name') == f'no genuine crossing detected at level {lv}' for n in b['names'])))
    return c


def r3_expect(rec):
    b = br(rec)
    st = b['levels']['2']['steps']
    s = [x for x in st if x['status'] == 'Unresolved' and x.get('reason') == 'Newton failure']
    return [('a step Unresolved (Newton failure) at the first bisection midpoint', len(s) == 1),
            ('its residual history recorded, every attempt', bool(s) and len(s[0].get('history') or []) >= 1
             and all(len(x) >= 1 for x in s[0]['history'])),
            ('a record written, finished', bool(rec.get('finished')))]


def r4_expect(rec, qual):
    c = []
    q = json.load(open(qual))
    c.append(('types and reasons equal', [(d['eps'], d['type'], d['why']) for d in rec['types']]
              == [(d['eps'], d['type'], d['why']) for d in q['types']]))
    c.append(('cross-level records equal', rec['cross'] == q['cross']))
    for grp in ('points', 'level2'):
        qa = [p for p in q[grp] if not p.get('bisection')]
        ra = rec[grp]
        same = len(qa) == len(ra) and all(all(k in r and r[k] == p[k] for k in p) for r, p in zip(ra, qa))
        c.append((f'{grp}: every frozen field bit for bit', same))
    return c


def r4_arm(rec):
    arm = rec.get('arm_dlev0_types', [])
    return [('the arm: every C3 point Unresolved (level stability)', bool(arm) and all(
        a['type'] == 'Unresolved' and 'level stability' in a['why'] for a in arm))]


def evaluate(qualdir):
    lines, out = [f'REGISTER_4.md § 3, the real-solver controls, evaluated {now()}'], {}

    def verdict(name, conds, arm_conds=None, arm_should_fail=True):
        ok = all(v for _, v in conds)
        caught = None
        if arm_conds is not None:
            arm_ok = all(v for _, v in arm_conds)
            caught = (not arm_ok) if arm_should_fail else arm_ok
        out[name] = dict(passed=bool(ok and (caught is None or caught)), checks=[[k, bool(v)] for k, v in conds],
                         arm=(None if arm_conds is None else dict(caught=caught, checks=[[k, bool(v)] for k, v in arm_conds])))
        lines.append(f'  {"PASS" if out[name]["passed"] else "FAIL"}  {name}: ' + ('all checks hold' if ok else
                     'failed: ' + str([k for k, v in conds if not v])) + ('' if caught is None else
                     f'; arm {"caught" if caught else "NOT caught"}'))

    c2a, c3 = load('_R1R4', 'C2a'), load('_R2R4', 'C3')
    r1arm, r3, r3arm = load('_R1arm', 'C2a'), load('_R3', 'C2a'), load('_R3arm', 'C2a')
    verdict('R1', r1_expect(c2a), r1_expect(r1arm, levels=(2,)))
    verdict('R2', r2_expect(c3), r2_expect(c2a))
    verdict('R3', r3_expect(r3), r3_expect(r3arm))
    verdict('R4 (C3)', r4_expect(c3, os.path.join(qualdir, 'branch_C3_R4.json')), r4_arm(c3), arm_should_fail=False)
    verdict('R4 (C2a)', r4_expect(c2a, os.path.join(qualdir, 'branch_C2a_R4.json')))
    r4b_ = json.load(open(os.path.join(OUT, 'r4b.json')))
    out['R4b'] = dict(passed=r4b_['passed'], arms={k: v['caught'] for k, v in r4b_['arms'].items()})
    lines.append(f'  {"PASS" if r4b_["passed"] else "FAIL"}  R4b: the nine reasons and two passes '
                 f'{"as expected" if r4b_["parent_ok"] else "NOT as expected"}; arms ' +
                 ', '.join(f'{k} {"caught" if v["caught"] else "NOT caught"}' for k, v in r4b_['arms'].items()))
    r5_ = json.load(open(os.path.join(OUT, 'r5.json')))
    out['R5'] = dict(passed=r5_['passed'])
    lines.append(f'  {"PASS" if r5_["passed"] else "FAIL"}  R5: ' + '; '.join(f'{c["case"]}: {c["outcome"]}' for c in r5_['cases'])
                 + f'; arm {"caught" if r5_["arm"]["caught"] else "NOT caught"}')
    n = sum(v['passed'] for v in out.values())
    lines.append(f'real-solver controls: {n} of {len(out)} pass' + (', each arm caught' if n == len(out) else ''))
    json.dump(dict(stamp=now(), results=out), open(os.path.join(OUT, 'real.json'), 'w'), indent=1, default=str)
    open(os.path.join(OUT, 'real.log'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    return n == len(out)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    cmd = sys.argv[1]
    if cmd == 'r4b':
        sys.exit(0 if r4b()['passed'] else 1)
    if cmd == 'r5':
        sys.exit(0 if r5(sys.argv[2])['passed'] else 1)
    if cmd == 'run':
        sys.exit(run(sys.argv[2]))
    if cmd == 'evaluate':
        sys.exit(0 if evaluate(sys.argv[2]) else 1)
    raise SystemExit(__doc__)
