#!/usr/bin/env python3
"""Every verdict path (M8.16.1's terms, THE TESTS BEFORE THE FREEZE, test 1; DRIVER_PLAN.md v2, The tests). Case:
synthetic.

Usage: test_verdicts.py MIT_REPO

Each registered outcome is read from a record built from M8.16's recorded outputs, read from MIT_REPO's history at the
record's commit, 87fc643, each against the SHA-256 its RUNLOG.json records, with the fields that outcome turns on
edited. Each record is scored by checks.py with M8.16.1's serialized case, and the test asserts the text the terms give
the outcome. Its parent is the same record unedited: the pyramid as recorded passes the bar, and K3 reads 'resolved'
(the record regression, score_record.py). Six mutations of the scoring code, each made in this process and undone,
turn their targeted assertions red. Nothing is solved, and no sealed case is built or read: the rows, T5's second
member and the C3 ray are read from the pyramid's record under their roles, and at the verdict from their checks alone.
Claim 1i's T5/R2 record is synthetic: its slow spectrum is the frozen next-order prediction itself, with nothing solved
and no record read (xrodz, B1 on #650).
The stops' and the resume's driver paths are test_guard.py's tests 9 and 10, which run them through this driver; here,
the verdict's text at each stop.

Claims, derived before the run:
  1. The bar, on the pyramid's two groups, the quartet and the Krein-positive pair:
     a. both pass, as recorded;
     b. Unresolved by check 1: a point not accepted (N = 24, eps = 0.5); the quartet's record group removed there;
     c. Unresolved by check 2: the quartet's projector unusable there; its residual raised so E_c exceeds its trigger;
     d. its association (UA): the Krein-positive pair's summary entry and a fast Krein-positive group's, of one class
        and Krein sign, with their index sets exchanged and their centres unchanged, reads check 2 failed on the
        inconsistency; the entry removed, and the entry duplicated, each fail check 2;
     e. fail by check 3: the quartet's values at 0.5 and 1 moved so that c2 moves and c3 does not, the spread 1.5
        ceilings, while check 4 holds;
     f. fail by check 4: the quartet's c_g(N) moved by ten ceilings at every cutoff;
     g. precedence: check 4's failure at N = 16 beside a point not accepted at N = 24 reads fail;
     h. cancellation: the quartet's spread made zero at N = 24 and its c_g set 0.05 ceilings from c3 there, between
        the spread and check 4's floor, passes.
     i. two groups of one class and sign whose next-order shifts match their separation (xrodz, B1 on #650): on a
        synthetic T5/R2 record whose slow spectrum is exactly eps kappa s_g + eps^2 c_g(N) at every cutoff and point,
        with K1, the convergence reading and a consistent summary in place, all three groups pass, its two lowest,
        2% apart at leading order, among them.
  2. K3: 'resolved' as recorded; 'not resolved, kernel exact: the diagnosis is wrong' for each mark of a merged in-span
     mode at one cutoff (N = 16, eps = 0.25): V0 not as expected, A's zero cluster not separated, the in-span group
     removed; 'instrument failure: the diagnosis is untested' for each break of L's certificate there (a tangent ten
     times the cut, L's zero count one above the chains, L's gray zone not empty, no certificate), a failed seed, a
     point not accepted, and the quartet failing the bar.
  3. K4's pyramid item: passes as recorded; fails when the quartet fails the bar, and when eps = 0.25 is not converged.
  4. K5, on the pyramid's record read as a row: passes; fails with V0 broken at eps = 0.5 at one cutoff, a point M8.16's
     K5 reported unscored; fails when a group fails the bar.
  5. The C3 ray, on the pyramid's record read as the ray, with c_g° ten ceilings from c_g: 'passed'; with c_g° equal to
     c_g: 'failed: the discrimination'; with the quartet failing the bar: 'failed: the next-order bar'.
  6. Cutoff matching: c_g(16) and c_g(24) exchanged reads fail; a record missing N = 32, and values lacking it, each
     read Unresolved.
  7. K1, K2 and the controls' K4, on C2a's record: they pass; V0 broken at a point fails K1 and K4; an extra group in
     the slow band fails K2; a mode moved 6% from leading order at eps = 0.25 fails K4.
  8. The verdict, from the checks: QUALIFIED, naming every row and member; a row failing K5, or K6, is not qualified,
     and so is a ladder row whose record has no K6 (xrodz on #650); the R5 gate failing leaves the R5 rows not qualified and every other as it was; T5J failing leaves T5/R2
     qualified, and the reverse; the C3 ray failing leaves the verdict and every row and member as they were, its
     outcome reported; a control failing K4, and the pyramid's K3 not resolved, each read NOT QUALIFIED naming the
     check, with no row or member qualified; a dry run reads incomplete.
Mutation arms, each of which must turn its assertion red:
  M1. check 4 without its floor: claim 1h reads fail.
  M2. K3(a) reading check 1 as the terms write it, with V0: claim 2's merged in-span modes read 'instrument failure'.
  M3. check 2's association by index alone, without its consistency: claim 1d's exchange passes check 2.
  M4. Unresolved taking precedence over a failure: claim 1g reads Unresolved.
  M5. check 1 pairing against the leading order, as filed at MIT 0d6beae: claim 1i's two lowest groups read fail.
  M6. a missing K6 read as passed, as filed: claim 8's ladder row without K6 qualifies.
"""
import copy
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools, linear as ln  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402

REPO = sys.argv[1] if len(sys.argv) > 1 else None
RECORD = '87fc643'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
WRONG, UNTESTED = 'not resolved, kernel exact: the diagnosis is wrong', 'instrument failure: the diagnosis is untested'
out, results = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def record(label, ok, detail=''):
    results.append((label, bool(ok)))
    say(f"   {'PASS' if ok else 'FAIL'}  {label}{': ' + str(detail) if detail != '' else ''}")


def show(path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{RECORD}:{M816}/{path}'], check=True, capture_output=True).stdout


def case(name, **over):
    return dict(json.loads(json.dumps(dr.jsonable(cs.serialize(name, cs.CASES[name])))), **over)


def recorded(names):
    log = json.loads(show('run/out/RUNLOG.json'))
    files = {f: h for r in log['completed'].values() for f, h in r['files'].items()}
    recs = {}
    for n in names:
        f = n.replace('/', '_') + '.json'
        raw = show(f'run/out/{f}')
        if hashlib.sha256(raw).hexdigest() != files[f]:
            raise RuntimeError(f'{f} differs from the SHA-256 its RUNLOG.json records')
        recs[n] = json.loads(raw)
    return recs


def pt(o, N, e):
    return o['cutoffs'][N]['points'][ck.key(e)]


def index_of(c, cls, krein):
    return next(i for i, g in enumerate(c['next_order']['24']) if (g['cls'], g['krein']) == (cls, krein))


def holder(o, c, N, e, gi):
    """The record group holding the frozen group gi's value at (N, e), and its convergence-summary entry."""
    _, _, groups, _ = ck.mode_values(pt(o, N, e), c, e, c['next_order'][N][gi]['spectrum_index'], N)
    g = groups[0]
    return g, next(x for x in pt(o, N, e)['summary']['groups'] if sorted(x['idx']) == sorted(g['idx']))


def shift(o, c, N, e, gi, delta):
    """Moves the group's centre by delta, in the record's group and its summary entry alike."""
    g, s = holder(o, c, N, e, gi)
    z = complex(*g['c']) + delta
    g['c'] = s['c'] = [z.real, z.imag]


def set_value(c, N, gi, key, z):
    c['next_order'][N][gi][key] = [repr(z.real), repr(z.imag)]


def move_c2(o, c, N, gi, target):
    """Moves the values at eps = 0.5 and 1 so that c2 becomes target while c3 stays: delta h = (0, a, b) with
    w3 . delta h = 0, at the reached amplitudes."""
    r = ck.bar_cutoff(o, c, int(N), c['next_order'][N][gi])
    x = r['x']
    w2, w3 = ck.lagrange0(x[:2]), ck.lagrange0(x)
    a = (target - r['c2hat']) / w2[1]
    b = -w3[1] * a / w3[2]
    shift(o, c, N, 0.5, gi, a * x[1] ** 2)
    shift(o, c, N, 1.0, gi, b * x[2] ** 2)
    return r


def readings(o, c, form='full'):
    return {gi: r['reading'] for gi, r in ck.bar(o, c, form).items()}


def exact_t5():
    """Claim 1i's record: T5/R2's slow spectrum at exactly eps kappa s_g + eps^2 c_g(N), one group per frozen entry at
    every cutoff and point, with K1, the convergence reading and a consistent summary in place. Nothing is solved and
    no record is read."""
    c = case('T5/R2')
    o = dict(cutoffs={}, readings={ck.key(e): dict(verdict='converged', type=c['type']) for e in ck.NEXT_EPS})
    for N in c['next_order']:
        pts = {}
        for e in ck.NEXT_EPS:
            groups, k = [], 0
            for j, modes in enumerate(ck.predicted_next(c, e, N)):
                m, lam = c['spectrum'][j], modes[0][2]
                groups.append(dict(c=[lam.real, lam.imag], cls=m['cls'], status='definite', size=m['mult'],
                                   neg=m['mult'] if m['sign'] == -1 else 0, idx=list(range(k, k + m['mult']))))
                k += m['mult']
            summary = dict(normA=1.0, groups=[dict(g, ok=True, pnorm=1.0, resid=0.0, why=None) for g in groups])
            rec = dict(v0_matches=True, blocks=c['chains'], separated=True, gray_count=0, nL=c['idx'][0],
                       nD=c['idx'][1], K=c['idx'][2])
            pts[ck.key(e)] = dict(accepted=True, eps_reached=e, groups=groups, summary=summary, record=rec)
        o['cutoffs'][N] = dict(seed=dict(ok=True), points=pts)
    return o, c


def main():
    devtools.require('synthetic')
    if not REPO:
        raise SystemExit(__doc__)
    say("Every verdict path (M8.16.1's DRIVER_PLAN.md v2), on records built from M8.16's; nothing solved.")
    recs = recorded(('P5', 'C2a'))
    P0, PC = recs['P5'], case('P5')
    Q, KP = index_of(PC, 'complex', None), index_of(PC, 'imag', '+')
    ceil = {N: ck.bar_cutoff(P0, PC, int(N), PC['next_order'][N][Q])['ceiling'] for N in PC['next_order']}

    say('1. the bar:')
    r = readings(P0, PC)
    record('a. both groups pass, as recorded', r == {Q: 'pass', KP: 'pass'}, r)
    o = copy.deepcopy(P0)
    pt(o, '24', 0.5)['accepted'] = False
    r = ck.bar(o, PC)
    record('b. a point not accepted: Unresolved by check 1', all(x['reading'] == 'Unresolved' for x in r.values())
           and all('check 1 at N = 24, eps = 0.5' in x['why'] for x in r.values()), {g: x['reading'] for g, x in r.items()})
    o = copy.deepcopy(P0)
    pt(o, '24', 0.5)['groups'] = [g for g in pt(o, '24', 0.5)['groups'] if g['cls'] != 'complex']
    r = ck.bar(o, PC)
    record("b. the quartet's record group removed: Unresolved by check 1", r[Q]['reading'] == 'Unresolved'
           and 'check 1 at N = 24, eps = 0.5' in r[Q]['why'], r[Q]['why'][:1])
    o = copy.deepcopy(P0)
    holder(o, PC, '24', 0.5, Q)[1]['ok'] = False
    r = readings(o, PC)
    record("c. the quartet's projector unusable: Unresolved by check 2, the pair passing", r == {Q: 'Unresolved', KP: 'pass'},
           ck.bar(o, PC)[Q]['why'][:1])
    o = copy.deepcopy(P0)
    holder(o, PC, '24', 0.5, Q)[1]['resid'] = 1e-3
    r = ck.bar(o, PC)
    record('c. its residual raised: E_c over its trigger, Unresolved by check 2', r[Q]['reading'] == 'Unresolved'
           and any('E_c' in w for w in r[Q]['why']), r[Q]['why'][:1])

    def exchanged():
        o = copy.deepcopy(P0)
        g, s = holder(o, PC, '24', 0.5, KP)
        fast = next(x for x in pt(o, '24', 0.5)['summary']['groups'] if x['cls'] == 'imag' and x['neg'] == s['neg']
                    and x['size'] == s['size'] and sorted(x['idx']) != sorted(s['idx']))
        s['idx'], fast['idx'] = fast['idx'], s['idx']
        return o
    r = ck.bar(exchanged(), PC)
    d_ok = r[KP]['reading'] == 'Unresolved' and any('disagrees with its record group' in w for w in r[KP]['why'])
    record("d. the pair's entry and a fast one's index sets exchanged: check 2 reads the inconsistency", d_ok,
           r[KP]['why'][:1])
    o = copy.deepcopy(P0)
    g, s = holder(o, PC, '24', 0.5, KP)
    pt(o, '24', 0.5)['summary']['groups'].remove(s)
    r = ck.bar(o, PC)
    record("d. the pair's entry removed: check 2 fails", r[KP]['reading'] == 'Unresolved'
           and any('no summary entry' in w for w in r[KP]['why']), r[KP]['why'][:1])
    o = copy.deepcopy(P0)
    g, s = holder(o, PC, '24', 0.5, KP)
    pt(o, '24', 0.5)['summary']['groups'].append(copy.deepcopy(s))
    r = ck.bar(o, PC)
    record("d. the pair's entry duplicated: check 2 fails", r[KP]['reading'] == 'Unresolved'
           and any('2 summary entries' in w for w in r[KP]['why']), r[KP]['why'][:1])

    o = copy.deepcopy(P0)
    base = ck.bar_cutoff(o, PC, 24, PC['next_order']['24'][Q])
    move_c2(o, PC, '24', Q, base['c3hat'] - 1.5 * ceil['24'])
    x = ck.bar_cutoff(o, PC, 24, PC['next_order']['24'][Q])
    r = ck.bar(o, PC)
    record('e. the spread 1.5 ceilings, c3 unmoved: fail by check 3, check 4 holding',
           r[Q]['reading'] == 'fail' and x['c3'] is False and x['c4'] is True and abs(x['c3hat'] - base['c3hat']) < 1e-12 * ceil['24'],
           f"spread/ceiling {x['spread'] / x['ceiling']:.3f}; c3 moved {abs(x['c3hat'] - base['c3hat']):.1e}")
    PF = copy.deepcopy(PC)
    for N in PF['next_order']:
        set_value(PF, N, Q, 'c_g', ck._c(PF['next_order'][N][Q]['c_g']) + 10 * ceil[N])
    r = ck.bar(P0, PF)
    record('f. c_g moved ten ceilings at every cutoff: fail by check 4', r[Q]['reading'] == 'fail'
           and all(not x['c4'] and x['c3'] for x in r[Q]['per_N'].values()), r[Q]['why'][:1])

    def precedence():
        P16 = copy.deepcopy(PC)
        set_value(P16, '16', Q, 'c_g', ck._c(P16['next_order']['16'][Q]['c_g']) + 10 * ceil['16'])
        o = copy.deepcopy(P0)
        pt(o, '24', 0.5)['accepted'] = False
        return ck.bar(o, P16)[Q]['reading']
    g_read = precedence()
    record('g. check 4 failing at N = 16, a point not accepted at N = 24: fail', g_read == 'fail', g_read)

    def cancellation():
        o, c = copy.deepcopy(P0), copy.deepcopy(PC)
        base = ck.bar_cutoff(o, c, 24, c['next_order']['24'][Q])
        move_c2(o, c, '24', Q, base['c3hat'])
        set_value(c, '24', Q, 'c_g', base['c3hat'] + 0.05 * ceil['24'])
        x = ck.bar_cutoff(o, c, 24, c['next_order']['24'][Q])
        return ck.bar(o, c)[Q]['reading'], x
    h_read, x = cancellation()
    record('h. the spread zero and c_g 0.05 ceilings from c3: pass', h_read == 'pass'
           and x['spread'] < 1e-9 * x['ceiling'] < abs(x['c_g'] - x['c3hat']) < ck.FLOOR * x['ceiling'],
           f"spread/ceiling {x['spread'] / x['ceiling']:.1e}, |c_g - c3|/ceiling {abs(x['c_g'] - x['c3hat']) / x['ceiling']:.3f}")
    T5O, T5C = exact_t5()
    lows = sorted(T5C['next_order']['24'], key=lambda g: abs(ck._c(g['kappa_s'])))[:2]
    lows = [T5C['next_order']['24'].index(g) for g in lows]
    r = readings(T5O, T5C)
    record("i. T5/R2's spectrum exactly at the next order, its two lowest groups 2% apart: all three pass",
           len(r) == 3 and all(x == 'pass' for x in r.values()), r)

    say('2. K3:')
    record("as recorded: 'resolved'", ck.k3(P0, PC)['outcome'] == 'resolved', ck.k3(P0, PC)['outcome'])

    def marked(change):
        o = copy.deepcopy(P0)
        change(o, pt(o, '16', 0.25))
        return ck.k3(o, PC)['outcome']
    merged = [('V0 not as expected', lambda o, p: p['record'].__setitem__('v0_matches', False)),
              ("A's zero cluster not separated", lambda o, p: p['record'].__setitem__('separated', False)),
              ('the in-span group removed', lambda o, p: p.__setitem__('groups', [g for g in p['groups'] if not (
                  g['cls'] == 'imag' and g['status'] == 'definite' and g['neg'] == g['size']
                  and abs(complex(*g['c'])) <= ck.slow_band(PC, 0.25))]))]
    for label, change in merged:
        got = marked(change)
        record(f'a merged in-span mode, {label}: the diagnosis is wrong', got == WRONG, got)
    breaks = [('a tangent ten times the cut', lambda o, p: p['kernel'].__setitem__('tangent', 10 * ln.L_CUT)),
              ("L's zero count one above the chains", lambda o, p: p['kernel'].__setitem__('dimkerL', PC['chains'] + 1)),
              ("L's gray zone not empty", lambda o, p: p['kernel'].__setitem__('l_resolved', False)),
              ('no certificate', lambda o, p: p.pop('kernel')),
              ('a failed seed', lambda o, p: o['cutoffs']['16']['seed'].__setitem__('ok', False)),
              ('a point not accepted', lambda o, p: p.__setitem__('accepted', False))]
    for label, change in breaks:
        got = marked(change)
        record(f'{label}: the diagnosis is untested', got == UNTESTED, got)
    got = ck.k3(P0, PF)['outcome']
    record('the quartet failing the bar: the diagnosis is untested', got == UNTESTED, got)

    say("3. K4's pyramid item:")
    record('as recorded: passes', ck.check_pyramid_k4(P0, PC)['K4'] is True)
    record('the quartet failing the bar: fails', ck.check_pyramid_k4(P0, PF)['K4'] is False)
    o = copy.deepcopy(P0)
    o['readings'][ck.key(0.25)]['verdict'] = 'Unresolved'
    record('eps = 0.25 not converged: fails', ck.check_pyramid_k4(o, PC)['K4'] is False)

    say("4. K5, on the pyramid's record read as a row:")
    RC = dict(PC, role='row')
    record('passes', ck.check_row_k5(P0, RC)['K5'] is True)
    o = copy.deepcopy(P0)
    pt(o, '24', 0.5)['record']['v0_matches'] = False
    k5 = ck.check_row_k5(o, RC)
    record('V0 broken at eps = 0.5 at one cutoff: fails, check 1 scoring the point', k5['K5'] is False
           and all(x['reading'] == 'Unresolved' for x in k5['next_order'].values()))
    record('a group failing the bar: fails', ck.check_row_k5(P0, dict(PF, role='row'))['K5'] is False)

    say("5. the C3 ray, on the pyramid's record read as the ray:")

    def ray(c, off):
        c = copy.deepcopy(dict(c, role='ray'))
        for N in c['next_order']:
            for gi, g in enumerate(c['next_order'][N]):
                set_value(c, N, gi, 'c_g_off', ck._c(g['c_g']) + off * ceil[N])
        return ck.check_ray(P0, c)['outcome']
    for label, c, off, want in (('c_g° ten ceilings from c_g', PC, 10, 'passed'),
                                ('c_g° equal to c_g', PC, 0, 'failed: the discrimination'),
                                ('the quartet failing the bar', PF, 10, 'failed: the next-order bar')):
        got = ray(c, off)
        record(f"{label}: '{want}'", got == want, got)

    say('6. cutoff matching:')
    PS = copy.deepcopy(PC)
    for gi in (Q, KP):
        a, b = PS['next_order']['16'][gi]['c_g'], PS['next_order']['24'][gi]['c_g']
        PS['next_order']['16'][gi]['c_g'], PS['next_order']['24'][gi]['c_g'] = b, a
    r = readings(P0, PS)
    record('c_g(16) and c_g(24) exchanged: fail', r == {Q: 'fail', KP: 'fail'}, r)
    o = copy.deepcopy(P0)
    o['cutoffs'].pop('32')
    r = readings(o, PC)
    record('a record missing N = 32: Unresolved', r == {Q: 'Unresolved', KP: 'Unresolved'}, r)
    PM = copy.deepcopy(PC)
    PM['next_order'].pop('32')
    r = readings(P0, PM)
    record('values lacking N = 32: Unresolved', r == {Q: 'Unresolved', KP: 'Unresolved'}, r)

    say("7. K1, K2 and the controls' K4, on C2a's record:")
    C0, CC = recs['C2a'], case('C2a')
    c = ck.check_control(C0, CC)
    record('they pass', c['K1'] and c['K4'] and ck.check_k2(C0, CC), (c['K1'], c['K4']))
    o = copy.deepcopy(C0)
    pt(o, '24', 0.5)['record']['v0_matches'] = False
    c = ck.check_control(o, CC)
    record('V0 broken at a point: K1 and K4 fail', not c['K1'] and not c['K4'], (c['K1'], c['K4']))
    o = copy.deepcopy(C0)
    band = ck.slow_band(CC, 0.5)
    pt(o, '24', 0.5)['groups'].append(dict(c=[0.0, band / 3], cls='imag', size=1, neg=0, status='definite', idx=[10 ** 6]))
    record('an extra group in the slow band: K2 fails', ck.check_k2(o, CC) is False)
    o = copy.deepcopy(C0)
    p = pt(o, '24', 0.25)
    g = min((g for g in p['groups'] if g['cls'] == 'imag' and abs(complex(*g['c'])) <= ck.slow_band(CC, 0.25)),
            key=lambda g: abs(complex(*g['c'])))
    g['c'] = [g['c'][0], g['c'][1] * 1.06]
    c = ck.check_control(o, CC)
    record('a mode moved 6% from leading order at 0.25: K4 fails', not c['K4'] and not c['bar'], (c['K4'], c['bar']))

    say('8. the verdict, from the checks:')
    rows = [n for n in cs.ORDER if cs.CASES[n]['role'] == 'row']

    def results_with(changes=None):
        R = {}
        for n in cs.ORDER:
            cn = case(n)
            role = cn['role']
            if role == 'pyramid':
                chk = dict(K1=True, K2=True, K3=dict(outcome='resolved'), K4=True)
            elif role == 'ray':
                chk = dict(outcome='passed')
            elif role in ('row', 'member'):
                chk = dict(K5=True, **(dict(K6=True) if cn.get('m815') else {}))
            else:
                chk = dict(K1=True, K4=True, **(dict(K2=True) if n in ('C2a', 'C2b') else {}))
            R[n] = dict(case=cn, checks=chk)
        for n, upd in (changes or {}).items():
            R[n]['checks'].update(upd)
        return R
    v0 = ck.verdict(results_with())
    record('every check passed: QUALIFIED, naming every row and member', v0['verdict'] == 'QUALIFIED'
           and sorted(v0['qualified']) == sorted(rows + ['T5J/R2']) and v0['c3_ray'] == {'C3R/R4': 'passed'},
           f"{v0['verdict']}, {len(v0['qualified'])} qualified")
    v = ck.verdict(results_with({'T1/R4': dict(K5=False)}))
    record('a row failing K5: not qualified, the verdict QUALIFIED', v['verdict'] == 'QUALIFIED' and not v['rows']['T1/R4']
           and 'T1/R4' not in v['qualified'])
    v = ck.verdict(results_with({'T2/R4': dict(K6=False)}))
    record('a row failing K6: not qualified', not v['rows']['T2/R4'] and v['rows']['T2/R5'])

    def without_k6():
        R = results_with()
        R['T2/R4']['checks'].pop('K6')
        return ck.verdict(R)
    v = without_k6()
    record('a ladder row whose record has no K6: not qualified', not v['rows']['T2/R4'] and v['rows']['T2/R5'])
    v = ck.verdict(results_with({'C2a/R5': dict(K4=False)}))
    r5 = [n for n in rows if cs.CASES[n]['slot'] == 'R5']
    record('the R5 gate failing: the R5 rows not qualified, every other as it was', v['verdict'] == 'QUALIFIED'
           and not v['r5_gate'] and not any(v['rows'][n] for n in r5)
           and all(v['rows'][n] for n in rows if n not in r5) and v['members']['T5J/R2'], sorted(r5))
    v = ck.verdict(results_with({'T5J/R2': dict(K5=False)}))
    record('T5J failing: T5/R2 still qualified', not v['members']['T5J/R2'] and v['rows']['T5/R2'])
    v = ck.verdict(results_with({'T5/R2': dict(K5=False)}))
    record('T5/R2 failing: T5J still qualified', v['members']['T5J/R2'] and not v['rows']['T5/R2'])
    v = ck.verdict(results_with({'C3R/R4': dict(outcome='failed: the discrimination')}))
    same = {k: x for k, x in v.items() if k != 'c3_ray'} == {k: x for k, x in v0.items() if k != 'c3_ray'}
    record('the C3 ray failing: the verdict, rows and members as they were, its outcome reported',
           same and v['c3_ray'] == {'C3R/R4': 'failed: the discrimination'}, v['c3_ray'])
    v = ck.verdict(results_with({'C3': dict(K4=False)}))
    record('a control failing K4: NOT QUALIFIED, naming it, nothing qualified', v['verdict'] == 'NOT QUALIFIED'
           and v['failing'] == ['K4'] and 'C3: K4' in v['failed'] and not v['qualified'], (v['failing'], v['failed']))
    v = ck.verdict(results_with({'P5': dict(K3=dict(outcome=WRONG))}))
    record("the pyramid's K3 not resolved: NOT QUALIFIED, naming K3, nothing qualified", v['verdict'] == 'NOT QUALIFIED'
           and v['failing'] == ['K3'] and 'P5: K3' in v['failed'] and not v['qualified'], (v['failing'], v['failed']))
    v = ck.verdict(results_with(), dry=True)
    record('a dry run: incomplete', v['verdict'] == 'incomplete')

    say('mutation arms, each of which must turn its assertion red:')
    saved = (ck.FLOOR, ck.bar, ck.association, ck.bar_group, ck.predicted_next, ck.k6_holds)
    try:
        ck.FLOOR = 0.0
        m1 = cancellation()[0]
        ck.FLOOR = saved[0]
        record('M1. check 4 without its floor: claim 1h no longer passes', m1 != 'pass', m1)
        ck.bar = lambda o, c, form='full': saved[1](o, c, 'full')
        m2 = [marked(change) for _, change in merged]
        ck.bar = saved[1]
        record("M2. K3(a) reading check 1 with V0: the merged in-span modes read 'instrument failure'",
               all(x == UNTESTED for x in m2), m2)

        def by_index_only(point, groups):
            entries, nA = point['summary']['groups'], point['summary']['normA']
            Es = [e['pnorm'] * max(e['resid'], ln.U * nA) for g in groups for e in entries
                  if sorted(e['idx']) == sorted(g['idx'])]
            return bool(Es), max(Es) if Es else None, None
        ck.association = by_index_only
        m3 = ck.bar(exchanged(), PC)[KP]['reading']
        ck.association = saved[2]
        record("M3. check 2's association by index alone: claim 1d's exchange passes unseen", m3 == 'pass', m3)

        def unresolved_first(case_out, c, gi, form='full'):
            res = saved[3](case_out, c, gi, form)
            if any(not (x['c1'] and x['c2']) for x in res['per_N'].values()):
                res = dict(res, reading='Unresolved')
            return res
        ck.bar_group = unresolved_first
        m4 = precedence()
        ck.bar_group = saved[3]
        record('M4. Unresolved taking precedence: claim 1g reads Unresolved', m4 == 'Unresolved', m4)

        def leading_order(c, e, N):
            return [[(m['cls'], m['sign'], ck.predicted(dict(c, spectrum=[m]), e)[0][2])] * m['mult']
                    for m in c['spectrum']]
        ck.predicted_next = leading_order
        m5 = readings(T5O, T5C)
        ck.predicted_next = saved[4]
        record("M5. check 1 paired against the leading order, as filed: claim 1i's two lowest groups read fail",
               [m5[gi] for gi in lows] == ['fail', 'fail'], m5)
        ck.k6_holds = lambda r: r['checks'].get('K6', True)
        m6 = without_k6()['rows']['T2/R4']
        ck.k6_holds = saved[5]
        record("M6. a missing K6 read as passed, as filed: claim 8's ladder row without K6 qualifies", m6 is True, m6)
    finally:
        ck.FLOOR, ck.bar, ck.association, ck.bar_group, ck.predicted_next, ck.k6_holds = saved
    failed = sum(not ok for _, ok in results)
    say(f'{failed} failed of {len(results)}')
    with open(os.path.join(HERE, 'test_verdicts.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
