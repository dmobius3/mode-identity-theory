"""M8.15.2's driver: one branch, its ladder rerun under the frozen continuation, and the locator v2 on its registered
primary brackets (REGISTER_5.md v3 § 1; it starts from M8.15.1 Target 1's driver at 324fde3).

  python3 t1_branch.py T2 4 --terms PATH        a target: refused, before any solve, unless M8.15.2's own guard,
                                                out/FROZEN.json in this folder, holds every value of the instrument's
                                                out/freeze_numbers.json, frozen true, the terms' SHA-256, a go, the
                                                instrument manifest's SHA-256 and the running locator's SHA-256s
  python3 t1_branch.py C2a 4 --bracket3 A B --bracket2 A B --region A B     a control (the tests)
  python3 t1_branch.py C3 4 --ladder-only       a control's full ladder (test R4)

Test options, for controls only: --tag, --test-levels 2, --test-maxit LEVEL KIND CALL MAXIT, --test-span-no-rotations,
--test-arm-dlev0, --test-stop-after-guard, and --instrument PATH (a scratch copy, test R5). Records go to out/; an
instrument exception writes a separate crash record and exits 1."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'

import sys, json, time, hashlib, argparse, datetime
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import locate

OUT = os.path.join(HERE, 'out')
GUARD = os.path.join(OUT, 'FROZEN.json')      # M8.15.2's own guard, written once at the freeze by write_guard.py
MANIFEST_SHA256 = '2b9864ab185e47f98c8572500fb2468c24de9e8346aec4e1f0fb4d077fd3e70c'                        # the instrument's out/MANIFEST.json at 97a8c08, pinned
TARGETS = {'T1', 'T2', 'T3', 'T4', 'T5'}
INSTRUMENT_FILES = ['geometry.py', 'irreps.py', 'fem.py', 'nonlinear.py', 'standing.py', 'linearize.py', 'integrate.py',
                    'symmetry.py', 'pinned.py', 'continuation.py', 'verdict.py', 'persistence.py', 'm815_common.py',
                    'm815_controls.py', 'm815_branch.py', 'm815_freeze.py', 'angle.py']
STAGE = {'stage': 'start'}
RUN = {}


def stage(s):
    STAGE['stage'] = s


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def registered_brackets(name, slot):
    """The registered primary brackets and guard regions (TARGET1_TERMS.md v7, as M8.15.1 registered them), as ladder
    values. The secondary is not run (REGISTER_5.md § 1), so the ladder runs to the primary's region end."""
    from m815_common import ladder, EPS_MAX
    L = ladder(0.25, EPS_MAX[slot])
    if (name, slot) == ('T2', 4):
        return [dict(label='primary', brackets={3: (L[12], L[13]), 2: (L[12], L[13])}, region=(L[11], L[14]))]
    if (name, slot) == ('T3', 5):
        return [dict(label='primary', brackets={3: (L[11], L[12]), 2: (L[11], L[12])}, region=(L[11], L[13]))]
    raise SystemExit(f'{name}/R{slot} has no registered bracket')


def check_instrument(instr):
    """Every instrument file's SHA-256 must equal the instrument's own manifest."""
    man = json.load(open(os.path.join(instr, 'out', 'MANIFEST.json')))
    present = sorted(f for f in os.listdir(instr) if f.endswith('.py'))
    bad = [f for f in INSTRUMENT_FILES if sha(os.path.join(instr, f)) != man['sha256'].get(f)]
    if bad or present != sorted(INSTRUMENT_FILES):
        raise SystemExit(f'refused: the instrument does not match its manifest ({bad or present})')
    return sha(os.path.join(instr, 'out', 'MANIFEST.json'))


def freeze_values_equal(fz, fn):
    """Every value of freeze_numbers.json appears unchanged in FROZEN.json."""
    return [k for k in fn if fz.get(k) != fn[k]]


def terms_match(fz, terms):
    """The guard carries the terms file's SHA-256."""
    return fz.get('terms_sha256') == sha(terms)


def validate_guard(instr, terms, manifest_sha):
    """A target's guard (REGISTER_5.md § 1): M8.15.2's own out/FROZEN.json, in this folder, exists and holds every value
    of the instrument's freeze_numbers.json unchanged, frozen true, the given terms' SHA-256, a non-empty go, the
    instrument manifest's SHA-256 as check_instrument computed it (which must equal the pin), and the SHA-256 of the
    running locate.py and t1_branch.py. The instrument's own FROZEN.json, M8.15.1's guard, is never read. Returns
    (ok, reasons), every failed check named."""
    if not os.path.exists(GUARD):
        return False, "no M8.15.2 guard (this folder's out/FROZEN.json)"
    fz = json.load(open(GUARD))
    fn = json.load(open(os.path.join(instr, 'out', 'freeze_numbers.json')))
    why = []
    diff = freeze_values_equal(fz, fn)
    if diff:
        why.append(f'the guard differs from freeze_numbers.json in {diff}')
    if not fz.get('frozen'):
        why.append('the guard is not marked frozen')
    if not terms or not os.path.exists(terms):
        why.append('no terms file given')
    elif not terms_match(fz, terms):
        why.append("the terms' SHA-256 does not match the guard")
    if not fz.get('go'):
        why.append('no go')
    if manifest_sha != MANIFEST_SHA256:
        why.append("the instrument manifest's SHA-256 is not the pinned one")
    if fz.get('instrument_manifest_sha256') != manifest_sha:
        why.append("the instrument manifest's SHA-256 does not match the guard")
    held = fz.get('locator_sha256') or {}
    for f, path in (('locate.py', locate.__file__), ('t1_branch.py', __file__)):
        if held.get(f) != sha(os.path.abspath(path)):
            why.append(f"the running {f}'s SHA-256 does not match the guard")
    return (not why), ('passed' if not why else '; '.join(why))


def compare_m815(name, slot, out, instr):
    """Any difference from M8.15's record in a type, n(L) or n(B|G_tol), at the ladder points both reached."""
    path = os.path.join(instr, '..', '..', 'soft-slot-dynamics', 'm8_15_solver', 'out', f'branch_{name}_R{slot}.json')
    if not os.path.exists(path):
        return dict(compared=False, path_missing=True)
    old = json.load(open(path))
    ot = {d['eps']: d['type'] for d in old['types']}
    op = {p['eps']: p for p in old['points'] if not p.get('bisection')}
    diffs = []
    for d in out['types']:
        e = d['eps']
        if e in ot and ot[e] != d['type']:
            diffs.append(dict(eps=e, field='type', m815=ot[e], now=d['type']))
    for p in out['points']:
        e = p['eps']
        if e in op:
            for f in ('nL', 'nB_cluster'):
                if op[e][f] != p[f]:
                    diffs.append(dict(eps=e, field=f, m815=op[e][f], now=p[f]))
    return dict(compared=True, differences=diffs)


def run(a, log=print):
    instr = os.path.abspath(a.instrument) if a.instrument else locate.INSTRUMENT
    stage('instrument')
    m815 = locate.import_instrument(instr)
    manifest_sha = check_instrument(instr)
    if a.case in TARGETS:
        ok, why = validate_guard(instr, a.terms, manifest_sha)
        if not ok:
            raise SystemExit(f'{a.case} is a target: refused, {why}.')
    if a.test_stop_after_guard:
        log('guard passed; stopping before any solve (test only)')
        return dict(guard='passed')
    from m815_common import LevelCase, ladder, EPS_MAX, schedule, SPECTRA
    from m815_branch import Point, write_json_atomic
    fz = m815.frozen_numbers(a.case)
    rf3, rf2 = float(fz['r_f']['3']), float(fz['r_f']['2'])
    tau0_3, tau0_2 = 10 * rf3, 10 * rf2
    dlev, s2 = float(fz['delta_lev']), float(fz['s2'][f'R{a.slot}'])
    full = ladder(0.25, EPS_MAX[a.slot])
    sch = schedule(a.case, a.slot, rf3, full) if a.case in SPECTRA else []
    text, decide_sha = locate.decide_source(instr)
    levels = tuple(int(x) for x in a.test_levels.split(',')) if a.test_levels else (3, 2)
    if a.case in TARGETS:
        entries = registered_brackets(a.case, a.slot)
    elif a.ladder_only:
        entries = []
    else:
        def snap(x):
            e = min(full, key=lambda y: abs(y - x))
            if abs(e - x) > 1e-3 * e:
                raise SystemExit(f'{x} is not a ladder point')
            return e
        b3, b2 = (a.bracket3 or a.bracket2), (a.bracket2 or a.bracket3)
        entries = [dict(label='control', brackets={3: (snap(b3[0]), snap(b3[1])), 2: (snap(b2[0]), snap(b2[1]))},
                        region=(snap(a.region[0]), snap(a.region[1])))]
    run_to = (EPS_MAX[a.slot] if (a.ladder_only or a.full_ladder or not entries)
              else max(e['region'][1] for e in entries))
    targets = [e for e in full if e <= run_to * (1 + 1e-12)]
    tag = a.tag or ''
    path = os.path.join(OUT, f't1_{a.case}_R{a.slot}{tag}.json')
    RUN.update(frozen=dict(r_f3=rf3, r_f2=rf2, delta_lev=dlev, s2=s2), decide_sha256=decide_sha,
               instrument_manifest_sha256=manifest_sha)
    out = dict(case=a.case, slot=a.slot, levels=list(levels), frozen=RUN['frozen'], decide_sha256=decide_sha,
               instrument=os.path.relpath(instr, HERE), instrument_manifest_sha256=manifest_sha,
               locator_sha256={f: sha(os.path.join(HERE, f)) for f in ('locate.py', 't1_branch.py')},
               terms_sha256=(sha(a.terms) if a.terms and os.path.exists(a.terms) else None),
               started=now(), targets=targets, points=[], level2=[], types=[], cross=[], brackets=[])
    os.makedirs(OUT, exist_ok=True)
    lcs, brs, P, R = {}, {}, {3: {}, 2: {}}, {3: {}, 2: {}}
    reached = targets
    if 3 in levels:
        stage('level 3 ladder')
        lcs[3] = LevelCase(3, a.case, a.slot)

        def on3(k, e, rec):
            P[3][e], R[3][e] = Point(lcs[3], rec, e, tau0_3, tau0_3), rec
            out['points'].append(P[3][e].record())
            log(f'  L3 eps {e:.4g}: nL {P[3][e].nL}, nB {P[3][e].nB}')
        brs[3] = lcs[3].branch(targets, on3)
        out['end'] = [str(brs[3].end[0]), brs[3].end[1]]
        reached = [e for e in targets if e in P[3]]
    stage('level 2 ladder')
    lcs[2] = LevelCase(2, a.case, a.slot)

    def on2(k, e, rec):
        P[2][e], R[2][e] = Point(lcs[2], rec, e, tau0_2, tau0_2, keep_cluster=True), rec
        out['level2'].append(P[2][e].record())
    brs[2] = lcs[2].branch(reached, on2)
    if 3 not in levels:
        out['end'] = [str(brs[2].end[0]), brs[2].end[1]]
    omega0 = float(np.sqrt(lcs[2].lam0))
    decide = locate.bind_decide(m815, text, a.case, a.slot, tau0_3, s2, omega0, dlev, sch)
    ladder_types = {}
    if 3 in levels:
        stage('types')
        decide0 = locate.bind_decide(m815, text, a.case, a.slot, tau0_3, s2, omega0, 0.0, sch) if a.test_arm_dlev0 else None
        arm = []
        for i, e in enumerate(reached):
            typ, why, cross = decide(e, P[3][e], P[2].get(e), i % 3 == 0)
            if cross:
                out['cross'].append(cross)
            out['types'].append(dict(eps=e, type=typ, why=list(why)))
            ladder_types[e] = dict(type=typ, why=list(why))
            if decide0 is not None:
                t0, w0, _ = decide0(e, P[3][e], P[2].get(e), i % 3 == 0)
                arm.append(dict(eps=e, type=t0, why=list(w0)))
            log(f'  eps {e:.4g}: {typ}' + (f' ({", ".join(why)})' if why else ''))
        if decide0 is not None:
            out['arm_dlev0_types'] = arm
        if a.case in TARGETS:
            out['m815_comparison'] = compare_m815(a.case, a.slot, out, instr)
    write_json_atomic(path, out)
    if entries:
        hooks = {}
        if a.test_maxit:
            lv, kind, call, mx = a.test_maxit
            hooks['maxit'] = dict(level=int(lv), kind=kind, call=int(call), maxit=int(mx))
        d = locate.DIM[a.case]
        ev = locate.InstrumentEvaluator(lcs, brs, {3: tau0_3, 2: tau0_2}, d, hooks)
        if a.test_span_no_rotations:
            ev.span_no_rotations = True
            ev.d = 1
        for ent in entries:
            stage(f'bracket {ent["label"]}')
            pool = {3: {}, 2: {}}
            lo_r, hi_r = ent['region']
            for lv in levels:
                for e in sorted(R[lv]):
                    if lo_r * (1 - 1e-12) <= e <= hi_r * (1 + 1e-12) or e in ent['brackets'][lv]:
                        pool[lv][e] = ev.evaluate(lv, e, R[lv][e])
            ends = {lv: (pool[lv][ent['brackets'][lv][0]], pool[lv][ent['brackets'][lv][1]]) for lv in levels}
            res = locate.locate_bracket(ev, decide, ent['brackets'], ent['region'], ent['label'], ends, ladder_types,
                                        pool, levels=levels)
            out['brackets'].append(res)
            write_json_atomic(path, out)
            for lv in pool:
                for ep in pool[lv].values():
                    ep.vecs = None
            log(f'  bracket {ent["label"]}: ' + '; '.join(n.get('name', '') for n in res['names']))
    out['finished'] = now()
    stage('record')
    write_json_atomic(path, out)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('case'); ap.add_argument('slot', type=int)
    ap.add_argument('--terms', default=None)
    ap.add_argument('--bracket3', type=float, nargs=2, default=None)
    ap.add_argument('--bracket2', type=float, nargs=2, default=None)
    ap.add_argument('--region', type=float, nargs=2, default=None)
    ap.add_argument('--ladder-only', action='store_true')
    ap.add_argument('--full-ladder', action='store_true')
    ap.add_argument('--tag', default=None)
    ap.add_argument('--instrument', default=None)
    ap.add_argument('--test-levels', default=None)
    ap.add_argument('--test-maxit', nargs=4, default=None, metavar=('LEVEL', 'KIND', 'CALL', 'MAXIT'))
    ap.add_argument('--test-span-no-rotations', action='store_true')
    ap.add_argument('--test-arm-dlev0', action='store_true')
    ap.add_argument('--test-stop-after-guard', action='store_true')
    a = ap.parse_args(argv)
    tests = (a.bracket3, a.bracket2, a.region, a.ladder_only, a.full_ladder, a.test_levels, a.test_maxit,
             a.test_span_no_rotations, a.test_arm_dlev0, a.test_stop_after_guard, a.instrument)
    if a.case in TARGETS and any(tests):
        raise SystemExit('test and bracket options are for controls only; a target runs its registered brackets')
    try:
        run(a, log=lambda s: print(s, flush=True))
    except SystemExit:
        raise
    except Exception as e:
        import traceback
        from m815_branch import write_json_atomic
        frames = [dict(file=(os.path.relpath(fr.filename, HERE) if os.path.abspath(fr.filename).startswith(HERE)
                             else os.path.basename(fr.filename)), line=fr.lineno, function=fr.name, code=fr.line)
                  for fr in traceback.extract_tb(e.__traceback__)]
        crash = dict(case=a.case, slot=a.slot, crash=True, stage=STAGE['stage'], exception=type(e).__name__,
                     message=str(e), traceback=frames, frozen=RUN.get('frozen'), decide_sha256=RUN.get('decide_sha256'),
                     instrument_manifest_sha256=RUN.get('instrument_manifest_sha256'), written=now())
        os.makedirs(OUT, exist_ok=True)
        write_json_atomic(os.path.join(OUT, f'crash_{a.case}_R{a.slot}{a.tag or ""}.json'), crash)
        print(f'INSTRUMENT EXCEPTION at stage {STAGE["stage"]}: {type(e).__name__}: {e}; crash record written', flush=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
