"""REGISTER_5.md v3 § 3: the real-solver controls R1 to R5 (R4b included) on the locator v2, on orbits that are not
targets. R1 to R4 and R4b keep REGISTER_4.md v3 § 3's expectations and arms; each control record must also reproduce
RESULT_4's runs value for value outside § 4's fields, the new branch must never fire, and rule 11 must pass at every
step. R5 moves to M8.15.2's own guard.

  python3 tests/real.py r4b                    the nine Unresolved reasons on constructed pairs, with the binding arms
  python3 tests/real.py r5 TERMS OLD_TERMS     M8.15.2's guard on a scratch copy of this folder and of the instrument;
                                               TERMS stands in for M8.15.2's terms, OLD_TERMS is M8.15.1's
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
OLD = os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x-target1')     # M8.15.1's locator: RESULT_4's runs in out/
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


# --- R5: M8.15.2's guard (REGISTER_5.md § 3) ---------------------------------------------------------------------------
R5_CODE = r'''
import sys, json, argparse, ast, textwrap
sys.path.insert(0, {root!r})
import t1_branch
arm = {arm!r}
if arm == 'terms':
    t1_branch.terms_match = lambda fz, terms: True
elif arm == 'inherited':
    # M8.15.1's entire validate_guard predicate, from its own driver: its file path and its four checks alone
    src = open({old_driver!r}).read()
    fn = [n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == 'validate_guard']
    assert len(fn) == 1
    text = textwrap.dedent(''.join(src.splitlines(keepends=True)[fn[0].lineno - 1:fn[0].end_lineno]))
    ns = dict(vars(t1_branch))
    exec(compile(text, "M8.15.1's t1_branch.py (validate_guard)", 'exec'), ns)
    old = ns['validate_guard']
    t1_branch.validate_guard = lambda instr, terms, manifest_sha: old(instr, terms)
ns = argparse.Namespace(case='T2', slot=4, terms={terms!r}, bracket3=None, bracket2=None, region=None,
                        ladder_only=False, full_ladder=False, tag='_R5', instrument={instr!r}, test_levels=None,
                        test_maxit=None, test_span_no_rotations=False, test_arm_dlev0=False, test_stop_after_guard=True)
try:
    r = t1_branch.run(ns, log=lambda s: None)
    print(json.dumps(dict(outcome='passed the guard', result=r)))
except SystemExit as e:
    print(json.dumps(dict(outcome='refused', message=str(e))))
'''


def sha(path):
    import hashlib
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def r5(terms, old_terms):
    """M8.15.2's guard on a scratch copy of this folder and of the instrument, beside each other as on main; no real
    guard file is written. terms stands in for M8.15.2's terms; old_terms is M8.15.1's, whose SHA-256 the instrument's
    own FROZEN.json carries. The complete guard is written by the scratch copy's own write-once step."""
    work = tempfile.mkdtemp(prefix='r5_')
    here = os.path.join(work, 'soft-slot-dynamics-m8-15-2')
    os.makedirs(os.path.join(here, 'out'))
    for f in ('locate.py', 't1_branch.py', 'write_guard.py'):
        shutil.copy2(os.path.join(ROOT, f), here)
    instr = os.path.join(work, 'soft-slot-dynamics-m8-15x', 'm8_15x_solver')
    shutil.copytree(locate.INSTRUMENT, instr, ignore=shutil.ignore_patterns('__pycache__'))
    guard, inst_guard = os.path.join(here, 'out', 'FROZEN.json'), os.path.join(instr, 'out', 'FROZEN.json')
    manifest = os.path.join(instr, 'out', 'MANIFEST.json')
    old_driver = os.path.join(OLD, 't1_branch.py')
    pre = dict(instrument_guard_present=os.path.exists(inst_guard),
               instrument_guard_carries_old_terms=(os.path.exists(inst_guard)
                                                   and json.load(open(inst_guard)).get('terms_sha256') == sha(old_terms)))

    def driver(content, terms_file, arm=None):
        if os.path.exists(guard):
            os.remove(guard)
        if content is not None:
            text = json.dumps(content, indent=1)
            open(guard, 'w').write(text)
        code = R5_CODE.format(root=here, terms=terms_file, instr=instr, arm=arm, old_driver=old_driver)
        r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
        line = [x for x in r.stdout.strip().splitlines() if x.startswith('{')]
        return json.loads(line[-1]) if line else dict(outcome='error', stderr=r.stderr[-2000:])

    # the complete guard, from the write-once step, which must then refuse a second write
    w1 = subprocess.run([sys.executable, os.path.join(here, 'write_guard.py'), terms, 'a test go (R5)'],
                        capture_output=True, text=True)
    good = json.load(open(guard)) if os.path.exists(guard) else None
    w2 = subprocess.run([sys.executable, os.path.join(here, 'write_guard.py'), terms, 'a test go (R5)'],
                        capture_output=True, text=True)
    writer = dict(first=w1.returncode == 0 and good is not None, second_refused=(w2.returncode != 0
                                                                                and 'written once' in w2.stderr + w2.stdout))
    if good is None:
        shutil.rmtree(work)
        raise SystemExit(f'R5: the write-once step wrote no guard: {w1.stderr[-1000:]}')
    first = sorted(json.load(open(os.path.join(instr, 'out', 'freeze_numbers.json'))))[0]
    m1 = json.load(open(inst_guard))
    cases = [
        ("no M8.15.2 guard, the instrument's FROZEN.json present, M8.15.1's terms", None, old_terms, 'refused', []),
        ('one freeze value differing', dict(good, **{first: 'changed'}), terms, 'refused', ['freeze_numbers.json']),
        ('a terms hash that differs', dict(good, terms_sha256='0' * 64), terms, 'refused', ["terms' SHA-256"]),
        ('an empty go', dict(good, go=''), terms, 'refused', ['no go']),
        ("an instrument manifest hash that differs from the guard's", dict(good, instrument_manifest_sha256='0' * 64),
         terms, 'refused', ["manifest's SHA-256 does not match the guard"]),
        ('a locate.py hash that differs', dict(good, locator_sha256=dict(good['locator_sha256'], **{'locate.py': '0' * 64})),
         terms, 'refused', ["locate.py's SHA-256"]),
        ('a t1_branch.py hash that differs',
         dict(good, locator_sha256=dict(good['locator_sha256'], **{'t1_branch.py': '0' * 64})), terms, 'refused',
         ["t1_branch.py's SHA-256"]),
        ("M8.15.1's FROZEN.json copied to the guard's path", m1, terms, 'refused',
         ["terms' SHA-256", "manifest's SHA-256 does not match the guard", "locate.py's SHA-256", "t1_branch.py's SHA-256"]),
        ('complete and matching', good, terms, 'passed the guard', []),
    ]
    res = []
    for label, content, tf, want, words in cases:
        o = driver(content, tf)
        ok = o['outcome'] == want and all(w in o.get('message', '') for w in words)
        res.append(dict(case=label, outcome=o['outcome'], message=o.get('message'), expected=want, words=words, ok=ok))
    # the instrument's manifest itself no longer the pinned one, the guard matching it
    saved = open(manifest).read()
    man = json.loads(saved)
    text = json.dumps(dict(man, note='altered by test R5'), indent=1)
    open(manifest, 'w').write(text)
    o = driver(dict(good, instrument_manifest_sha256=sha(manifest)), terms)
    open(manifest, 'w').write(saved)
    want_words = ["manifest's SHA-256 is not the pinned one"]
    res.append(dict(case="the instrument's manifest not the pinned one", outcome=o['outcome'], message=o.get('message'),
                    expected='refused', words=want_words,
                    ok=o['outcome'] == 'refused' and all(w in o.get('message', '') for w in want_words)))
    # the arms, each after its green parent: case 3 and case 1 refused above
    a1 = driver(cases[2][1], terms, arm='terms')
    a2 = driver(None, old_terms, arm='inherited')
    arms = [dict(arm='the terms-hash check disabled, on the third case', parent_refused=res[2]['ok'],
                 outcome=a1['outcome'], message=a1.get('message'), caught=a1['outcome'] == 'passed the guard'),
            dict(arm="the inherited guard restored: M8.15.1's entire validate_guard, its file path and four checks alone, "
                     "with M8.15.1's terms and the instrument's FROZEN.json", parent_refused=res[0]['ok'],
                 outcome=a2['outcome'], message=a2.get('message'), caught=a2['outcome'] == 'passed the guard')]
    out = dict(stamp=now(), register='REGISTER_5.md v3 § 3', terms=dict(path=terms, sha256=sha(terms)),
               old_terms=dict(path=old_terms, sha256=sha(old_terms)), preconditions=pre, writer=writer, cases=res,
               arms=arms, passed=bool(all(pre.values()) and all(writer.values()) and all(r['ok'] for r in res)
                                      and all(a['parent_refused'] and a['caught'] for a in arms)),
               scratch='a temporary copy of this folder and of the instrument, removed afterwards')
    shutil.rmtree(work)
    json.dump(out, open(os.path.join(OUT, 'r5.json'), 'w'), indent=1, default=str)
    print('R5: ' + '; '.join(f'{r["case"]}: {r["outcome"]}{"" if r["ok"] else " (NOT AS EXPECTED)"}' for r in res)
          + '; arms ' + ', '.join('caught' if a['caught'] else 'NOT caught' for a in arms)
          + f'; write-once step {"as expected" if all(writer.values()) else "NOT as expected"}')
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


NEW_FIELDS = {'start', 'nL_ends', 'clean_ends', 'midpoints', 'branch_step', 'branch_points', 'continuity',
              'identity_cosines_genuine', 'identity_cosines_structural', 'clause3_trigger'}
TOP_FIELDS = {'locator_sha256', 'started', 'finished'}


def strip_new(x, top=True):
    """A record with REGISTER_5.md § 4's fields set aside: § 1 item 4's step fields and item 5's trigger, wherever they
    sit, and at the top the locator's SHA-256 and the start and finish times. None of these names occurs in RESULT_4's
    records."""
    if isinstance(x, dict):
        return {k: strip_new(v, False) for k, v in x.items() if k not in NEW_FIELDS and not (top and k in TOP_FIELDS)}
    if isinstance(x, list):
        return [strip_new(v, False) for v in x]
    return x


def differences(a, b, path='', out=None):
    """Every path at which two JSON values differ."""
    out = [] if out is None else out
    if type(a) != type(b):
        out.append(f'{path}: {type(a).__name__} against {type(b).__name__}')
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f'{path}/{k}: only in {"RESULT_4" if k in a else "this run"}')
            else:
                differences(a[k], b[k], f'{path}/{k}', out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(f'{path}: {len(a)} entries against {len(b)}')
        for i, (p, q) in enumerate(zip(a, b)):
            differences(p, q, f'{path}[{i}]', out)
    elif a != b:
        out.append(f'{path}: {a!r} against {b!r}')
    return out


def control_steps(rec):
    return [s for b in rec['brackets'] for L in b['levels'].values() for s in L['steps']]


def evaluate(qualdir):
    lines, out = [f'REGISTER_5.md § 3, the real-solver controls on the locator v2, evaluated {now()}'], {}

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
                 + '; arms ' + ', '.join('caught' if a['caught'] else 'NOT caught' for a in r5_['arms'])
                 + f'; write-once step {"as expected" if all(r5_["writer"].values()) else "NOT as expected"}')
    # REGISTER_5.md § 3: what every control record also carries
    recs = dict(c2a=c2a, c3=c3, r3=r3, r3arm=r3arm, r1arm=r1arm)
    tags = dict(c2a=('_R1R4', 'C2a'), c3=('_R2R4', 'C3'), r3=('_R3', 'C2a'), r3arm=('_R3arm', 'C2a'), r1arm=('_R1arm', 'C2a'))
    diffs = {k: differences(strip_new(json.load(open(os.path.join(OLD, 'out', f't1_{tags[k][1]}_R4{tags[k][0]}.json')))),
                            strip_new(v)) for k, v in recs.items()}
    verdict('RESULT_4 reproduced', [(f"{k}: value for value outside § 4's fields ({len(d)} differences)", not d)
                                     for k, d in diffs.items()])
    out['RESULT_4 reproduced']['differences'] = {k: d[:20] for k, d in diffs.items()}
    verdict('the new branch never fires', [(f'{k}: no midpoint passed, exchanged or ending a step, and no branch step',
                                            all(not s.get('midpoints') and s.get('branch_step') is False
                                                for s in control_steps(v))) for k, v in recs.items()])
    largest = [s['continuity']['largest'] for s in control_steps(c2a) if s.get('continuity', {}).get('largest') is not None]
    verdict('rule 11 on the controls', [(f'{k}: rule 11 passes at every step', all(
        s.get('continuity', {}).get('verdict') == 'passes' for s in control_steps(v))) for k, v in recs.items()]
            + [("C2a's steps: the statistic at most 2.6e-6 (recon_numbers.py v5)", bool(largest)
                and max(largest) <= 2.65e-6), ('C3: no step', not control_steps(c3))])
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
        sys.exit(0 if r5(sys.argv[2], sys.argv[3])['passed'] else 1)
    if cmd == 'run':
        sys.exit(run(sys.argv[2]))
    if cmd == 'evaluate':
        sys.exit(0 if evaluate(sys.argv[2]) else 1)
    raise SystemExit(__doc__)
