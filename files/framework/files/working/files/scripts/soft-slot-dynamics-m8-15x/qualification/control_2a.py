"""M8.15.x control 2a (REGISTER_2.md, registered 2026-10-09T01:21:48Z): the cluster rule on the pyramid.

P5 in R4, AngleBranch(track=True, theta_start=0) over the R4 ladder from 0.25 to 72, at level 3 and then level 2. At
every ladder point the verdict's slow eigenpairs are classified twice from the same eigen-data: by the 0.9 rule (the
verdict as frozen) and by the candidate rule (cluster_rule.py: the anchor, then the tracking), each with its cluster
quantities and Krein count. Then the cross-level check under the candidate rule, the refinement veto, the registered
checks of § 4 and their mutation arms.

  python3 control_2a.py [--level 3|2|eval] [--ladder-max E]
Each level writes control_2a_L<h>.json when it finishes; level 2 reads level 3's file for its anchors; 'eval' (the
default after both) writes control_2a.json and control_2a.log. --ladder-max is for a plumbing test only."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, time, datetime, copy, traceback
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
from m815_common import LevelCase, FROZEN_DIM, predicted, kappa, SPECTRA, match, ladder
from m815_branch import frozen_numbers
from linearize import Linearization
from verdict import Verdict, static_overlap, real_orthonormal, representatives
from nonlinear import to_complex
from angle import AngleBranch
from cluster_rule import anchor, track, advance, start_tracks, pcos_min, blocks_from_verdict, classify, cost

NAME, SLOT = 'P5', 4
LABELS = [('inspan', 'imag-'), ('quartet', 'quartet'), ('imagplus', 'imag+')]      # SPECTRA['P5'] order
FZ = frozen_numbers(NAME)
RF = {3: float(FZ['r_f']['3']), 2: float(FZ['r_f']['2'])}
TAU0 = {h: 10 * RF[h] for h in RF}
S2 = float(FZ['s2']['R4'])
KAP = kappa(NAME, SLOT)
TAG = ''                                  # '_plumbing' for a plumbing test (--ladder-max), never the registered run


def theorem(eps):
    return {lab: complex(l) for (lab, _), (l, _) in zip(LABELS, predicted(NAME, SLOT, eps))}


def first_resolved(level, targets):
    out = {}
    for (lab, _), (typ, t, _) in zip(LABELS, SPECTRA[NAME]):
        out[lab] = next((e for e in targets if 10 * TAU0[level] <= e * KAP * abs(complex(t))), None)
    return out


def cj(z):
    return [float(np.real(z)), float(np.imag(z))]


def point_record(level, lc, br, rec, eps_k, state, ref3, log):
    """Both classifications at one ladder point; the candidate rule's tracks live in state."""
    t0 = time.time()
    tau0 = tau_re = TAU0[level]
    Phi, sigma = to_complex(rec['x']), rec['sigma']
    lin = Linearization(lc.st, Phi, sigma)
    sl = [br.C.slice(br.C.seed(rec['phys']))]
    v = Verdict(lc.st, lc.case, lin, Phi, sigma, lc.lam0_min, lc.rot, FROZEN_DIM[NAME], rigid=lc.rigid, slices=sl,
                tau0=tau0, tau_re=tau_re)
    cls_old = np.array(v.cls)
    kr, kc, kim, rhs = v.count(tau_re)
    old = dict(cls=[str(c) for c in cls_old], dim=v.dim, closed=bool(v.closed), omega_gram=float(v.omega_gram),
               counts=[kr, kc, kim, rhs], balanced=bool(kr + 2 * kc + 2 * kim == rhs), nL=int(v.nL), nB=int(v.nB_cluster))
    old['cluster_ok'] = bool(old['dim'] == FROZEN_DIM[NAME] and old['closed'] and old['omega_gram'] >= 1e-6)
    inner = v.ps.inner
    blocks, loose, kre = blocks_from_verdict(v, tau_re, cls_old)
    tracks = state['tracks']
    step = None
    if any(t['alive'] for t in tracks) and state['prev_eps'] is not None:
        step = track(tracks, blocks, eps_k / state['prev_eps'], inner)
        advance(tracks, step, blocks, inner)
    known = {t['label'] for t in tracks}
    new = [dict(label=lab, cls=cl, mult=1) for lab, cl in LABELS
           if state['first'][lab] is not None and eps_k >= state['first'][lab] * (1 - 1e-12) and lab not in known]
    refs, no_ref = {}, []
    for m in new:
        if level == 3:
            refs[m['label']] = theorem(eps_k)[m['label']]
        else:
            r3 = ref3.get(f'{eps_k:.12g}', {}).get(m['label'])
            if r3 is None:
                no_ref.append(m)
            else:
                refs[m['label']] = complex(*r3)
    taken = {i for t in tracks if t['alive'] for i in t.get('blocks', [])}
    anchored = anchor(blocks, [m for m in new if m['label'] in refs], refs, taken) if refs else {}
    for m in no_ref:
        anchored[m['label']] = dict(ok=False, why="level 3's block is not tracked here", nearest=None)
    start_tracks(tracks, anchored, blocks, inner)
    gen = {i for t in tracks if t['alive'] for b in t['blocks'] for i in blocks[b]['idx']}
    new_cls = np.array([c if c == 'fibre' else ('genuine' if i in gen else ('rigid' if c == 'rigid' else 'lifted'))
                        for i, c in enumerate(cls_old)])
    v.reclassify(new_cls)
    kr, kc, kim, rhs = v.count(tau_re)
    cand = dict(dim=v.dim, closed=bool(v.closed), omega_gram=float(v.omega_gram), counts=[kr, kc, kim, rhs],
                balanced=bool(kr + 2 * kc + 2 * kim == rhs), nB=int(v.nB_cluster),
                genuine_all=[[*cj(l), float(k)] for l, k in v.genuine_all])
    cand['cluster_ok'] = bool(cand['dim'] == FROZEN_DIM[NAME] and cand['closed'] and cand['omega_gram'] >= 1e-6)
    # lifts in G, by kind (M8.15's points: radical if the static part lies at least half on the slice)
    Sv = real_orthonormal(np.column_stack(sl), lin.Mr)
    in_track = {b for t in tracks if t['alive'] for b in t['blocks']}
    lifts = []
    for bi, b in enumerate(blocks):
        if bi in in_track:
            continue
        o = static_overlap(v.vecs[:, b['idx'][0]], Sv, lin.Mr, v.n2)
        lifts.append(dict(block=bi, lam=cj(b['lam']), mod=abs(b['lam']), kind='radical' if o ** 2 >= 0.5 else 'paired',
                          cls=b['cls']))
    # diagnostics for the in-span block
    diag = {}
    tr = {t['label']: t for t in tracks}
    th = theorem(eps_k)
    for lab, _ in LABELS:
        t = tr.get(lab)
        d = dict(tracked=bool(t and t['alive']), why=(t or {}).get('why'))
        if t and t['alive']:
            lam = t['lam']
            d.update(lam=cj(lam), cls=t['cls'], err_theorem=cost(lam, th[lab]),
                     err_level3=(cost(lam, complex(*ref3[f'{eps_k:.12g}'][lab])) if level == 2 and
                                 ref3.get(f'{eps_k:.12g}', {}).get(lab) is not None else None))
        if step and lab in step:
            d.update(step_ok=step[lab]['ok'], overlap=step[lab].get('overlap'), runner_up=step[lab].get('runner_up'),
                     change=step[lab].get('change'), step_why=step[lab].get('why'))
        if lab in anchored:
            a = anchored[lab]
            d['anchor'] = dict(ok=a['ok'], why=a.get('why'), errors=a.get('errors'), margin=a.get('margin'),
                               nearest=a.get('nearest'))
        diag[lab] = d
    t = tr.get('inspan')
    if t and t['alive']:
        b0 = blocks[t['blocks'][0]]
        vec = v.vecs[:, b0['idx'][0]]
        R = v.Rspan
        z = sl[0] - 0.0
        zr = R @ (R.T @ (lin.Mr @ z))
        Z = real_orthonormal(zr[:, None], lin.Mr)
        XY = real_orthonormal(R - Z @ (Z.T @ (lin.Mr @ R)), lin.Mr)
        paired = [l for l in lifts if l['kind'] == 'paired']
        pb = [blocks[l['block']]['basis'] for l in paired]
        diag['inspan'].update(idx=list(b0['idx']), old_cls=[str(cls_old[i]) for i in b0['idx']],
                              ov_xy=static_overlap(vec, XY, lin.Mr, v.n2), ov_z=static_overlap(vec, Z, lin.Mr, v.n2),
                              paired_max=max((l['mod'] for l in paired), default=0.0),
                              pcos_paired=(pcos_min(b0['basis'], np.column_stack(pb), inner) if pb else None))
    paired_max = max((l['mod'] for l in lifts if l['kind'] == 'paired'), default=0.0)
    row = dict(level=level, eps=float(eps_k), eps_reached=float(rec['eps']), theta=rec['theta'], phys=rec['phys'],
               nu=rec['nu'][0], mu=rec['mu'][0], old=old, cand=cand, lifts=lifts, diag=diag, loose=len(loose),
               blocks=[dict(cls=b['cls'], lam=cj(b['lam']), complete=b['complete'], n=len(b['idx'])) for b in blocks],
               paired_lift=paired_max, paired_over_tau0=paired_max / tau0, seconds=round(time.time() - t0, 1))
    state['prev_eps'] = eps_k
    log(f'  L{level} eps {eps_k:.4g}: old dim {old["dim"]} ok={old["cluster_ok"]} counts {old["counts"]}; '
        f'candidate dim {cand["dim"]} ok={cand["cluster_ok"]} counts {cand["counts"]} balanced={cand["balanced"]}; '
        + '; '.join(f'{lab} {"tracked" if diag[lab]["tracked"] else "-"}'
                    + (f' err {diag[lab]["err_theorem"]:.4f}' if diag[lab].get('err_theorem') is not None else '')
                    for lab, _ in LABELS) + f'; paired lift / tau0 {row["paired_over_tau0"]:.2f}; {row["seconds"]} s')
    return row


def run_level(level, ladder_max=72.0, log=print, mesh_level=None):
    t0 = time.time()
    targets = ladder(0.25, ladder_max)
    lc = LevelCase(mesh_level or level, NAME, SLOT)          # mesh_level: plumbing only (the rule of `level` on another mesh)
    log(f'level {level} setup {time.time() - t0:.0f} s')
    ref3 = {}
    if level == 2:
        L3 = json.load(open(os.path.join(HERE, f'control_2a_L3{TAG}.json'))) if os.path.exists(
            os.path.join(HERE, f'control_2a_L3{TAG}.json')) else dict(rows=[])
        for r in L3['rows']:
            ref3[f'{r["eps"]:.12g}'] = {lab: d['lam'] for lab, d in r['diag'].items() if d.get('tracked')}
    state = dict(tracks=[], prev_eps=None, first=first_resolved(level, targets))
    rows, errors = [], []
    br = AngleBranch(lc, theta_start=0.0, track=True, log=log)

    def on_point(k, eps_k, rec):
        try:
            rows.append(point_record(level, lc, br, rec, eps_k, state, ref3, log))
        except Exception as e:
            errors.append(dict(eps=float(eps_k), error=f'{type(e).__name__}: {e}', tb=traceback.format_exc()[-2000:]))
            log(f'  L{level} eps {eps_k:.4g}: CLASSIFICATION ERROR {type(e).__name__}: {e}')
    br.run(targets, on_point=on_point)
    out = dict(level=level, targets=targets, first_resolved=state['first'], end=[br.end[0], br.end[1]], rows=rows,
               errors=errors, first_grid=dict(selected=br.first_grid['selected']['theta'] if br.first_grid['selected'] else None,
               roots=[(r['theta'], r['kind']) for r in br.first_grid['roots']]),
               events=br.events, others=[dict(label=o['label'], kind=o['kind'], alive=o['alive'], n=len(o['rows'])) for o in br.others],
               sel_rows=br.sel_rows, n_solves=br.C.n_solves, seconds=round(time.time() - t0, 1),
               tracks=[dict(label=t['label'], alive=t['alive'], why=t.get('why'), cls=t.get('cls')) for t in state['tracks']])
    json.dump(out, open(os.path.join(HERE, f'control_2a_L{level}{TAG}.json'), 'w'), indent=1, default=float)
    log(f'level {level} done: end {out["end"]}, {len(rows)} ladder points, {len(errors)} errors, {out["seconds"]} s')
    return out


def cross_and_veto(L3, L2):
    r3 = {f'{r["eps"]:.12g}': r for r in L3['rows']}
    out = []
    for r2 in L2['rows']:
        key = f'{r2["eps"]:.12g}'
        r = r3.get(key)
        if r is None:
            continue
        tau_re = TAU0[3]
        reps = lambda row: [(complex(a, b), classify(complex(a, b), k, tau_re))
                            for a, b, k in row['cand']['genuine_all'] if a >= -tau_re and b >= -tau_re]
        pairs = match(reps(r), reps(r2))
        if pairs is None:
            cross = dict(ok=False, why='class counts differ')
        else:
            omega0 = np.sqrt(48.0)
            worst = max((abs(a - b) / (0.01 * max(abs(a), abs(b)) + S2 / omega0) for a, b, c in pairs), default=0.0)
            cross = dict(ok=bool(worst <= 1.0), why=f'worst ratio to tolerance {worst:.3f}')
        veto = dict(applies=bool(r['cand']['dim'] == FROZEN_DIM[NAME] and r2['cand']['dim'] == FROZEN_DIM[NAME]))
        if veto['applies']:
            ok, pairs_v = True, []
            for kind in ('paired', 'radical'):
                a = sorted(l['mod'] for l in r['lifts'] if l['kind'] == kind)
                b = sorted(l['mod'] for l in r2['lifts'] if l['kind'] == kind)
                if len(a) != len(b):
                    ok = False
                    pairs_v.append(dict(kind=kind, why='unequal counts', l3=a, l2=b))
                    continue
                for x3, x2 in zip(a, b):
                    if x3 >= RF[3]:
                        ratio = x2 / x3
                        pairs_v.append(dict(kind=kind, l3=x3, l2=x2, ratio=ratio))
                        ok &= ratio >= 2.0
            veto.update(ok=bool(ok), pairs=pairs_v)
        out.append(dict(eps=r2['eps'], cross=cross, veto=veto))
    return out


def evaluate(R):
    L3, L2, X = R['L3'], R['L2'], R['cross']
    e0 = lambda L: next((r for r in L['rows'] if abs(r['eps'] - 0.25) < 1e-12), None)
    p = e0(L3)
    checks = []
    # 1. the 0.9 rule fails at eps_min, level 3
    ok1 = False
    if p and p['diag']['inspan'].get('tracked'):
        ok1 = (p['old']['dim'] == 8 and not p['old']['cluster_ok']
               and all(c != 'genuine' for c in p['diag']['inspan']['old_cls']))
    checks.append(('1. the 0.9 rule puts the in-span block in G_tol at eps_min, level 3: dimension 8 against 6', ok1))
    checks.append(('2. the selected track reaches eps = 72 at both levels',
                   L3['end'][0] == 'eps_max' and L2['end'][0] == 'eps_max'))
    a3 = p['diag'] if p else {}
    ok3 = bool(p) and all(a3[lab].get('anchor', {}).get('ok') for lab, _ in LABELS)
    checks.append(('3. the three blocks anchored within 0.10, uniquely, at eps_min, level 3', ok3))
    # 4. the in-span block tracked and genuine wherever resolved, from its first resolved point at each level
    def held(L, start):
        rows = [r for r in L['rows'] if r['eps'] >= start - 1e-12]
        if not rows or abs(rows[0]['eps'] - start) > 1e-9 or not rows[0]['diag']['inspan'].get('tracked'):
            return False, start                            # it must be tracked at its first resolved point
        for r in rows:
            d = r['diag']['inspan']
            if not d.get('tracked'):
                return False, r['eps']
            if abs(complex(*d['lam'])) < 10 * TAU0[L['level']]:
                return True, r['eps']                      # left the resolved band: the check ends here
        return True, None
    h3, h2 = held(L3, 0.25), held(L2, L2['first_resolved']['inspan'])
    checks.append(('4. the in-span block tracked and genuine at every resolved point, level 3 from 0.25 and level 2 from 5.66',
                   h3[0] and h2[0] and L2['first_resolved']['inspan'] is not None))
    d = a3.get('inspan', {})
    checks.append(('5. identity at eps_min: overlap >= 0.9 with span(X_x, X_y), <= 0.1 with X_z, |lambda| >= 10 x the paired lift',
                   bool(d.get('tracked')) and d.get('ov_xy', 0) >= 0.9 and d.get('ov_z', 1) <= 0.1
                   and abs(complex(*d['lam'])) >= 10 * d.get('paired_max', np.inf)))
    all3 = lambda r: all(r['diag'][lab].get('tracked') for lab, _ in LABELS)
    ok6 = all(r['cand']['dim'] == 6 for r in L3['rows'] if all3(r))
    for r in L2['rows']:
        want = 12 if r['eps'] < 4 - 1e-9 else (8 if r['eps'] < 5.656854 - 1e-6 else (6 if all3(r) else None))
        if want is not None and r['cand']['dim'] != want:
            ok6 = False
    checks.append(("6. the candidate rule's cluster dimension: 6 at level 3; 12, 8, then 6 at level 2", ok6))
    checks.append(('7. the Krein count balances at eps_min, level 3, with k_c = 1, k_i- = 1, k_r = 0',
                   bool(p) and p['cand']['balanced'] and p['cand']['counts'][:3] == [0, 1, 1]))
    checks.append(('8. the veto passes wherever it applies', all(x['veto']['ok'] for x in X if x['veto']['applies'])))
    checks.append(('9. the cross-level points below 5.66 read Unresolved, from unequal class counts',
                   all((not x['cross']['ok']) and x['cross']['why'] == 'class counts differ' for x in X if x['eps'] < 5.656854 - 1e-6)))
    return checks


def readings(R):
    """The registered readings that are not pass or fail: the in-span anchor error's outcome, validity, and where
    the 0.9 rule fails beyond eps_min."""
    p = next((r for r in R['L3']['rows'] if abs(r['eps'] - 0.25) < 1e-12), None)
    e = p['diag']['inspan'].get('err_theorem') if p else None
    errs = [p['diag'][lab].get('err_theorem') for lab, _ in LABELS] if p else []
    outcome = (None if e is None else ('within 5%: validity and the anchor pass' if e <= 0.05 else
               ('5% to 10%: INVALID under the 5% bar, the anchor passes' if e <= 0.10 else 'above 10%: the anchor fails')))
    return dict(inspan_error=e, outcome=outcome, validity_eps_min=bool(errs and all(x is not None and x <= 0.05 for x in errs)),
                errors_eps_min=errs, old_rule_fails_at=[r['eps'] for r in R['L3']['rows'] if not r['old']['cluster_ok']])


def mutations(R):
    def first(L):
        return next(r for r in L['rows'] if abs(r['eps'] - 0.25) < 1e-12)
    arms = [
        (0, 'the 0.9 rule keeping the in-span mode genuine', lambda r: first(r['L3'])['old'].update(dim=6, cluster_ok=True)),
        (1, 'level 2 ending early', lambda r: r['L2'].__setitem__('end', ['the carried root is lost: no minimum within two grid spacings', None])),
        (2, 'the quartet unanchored', lambda r: first(r['L3'])['diag']['quartet']['anchor'].__setitem__('ok', False)),
        (3, 'the in-span track lost at level 3', lambda r: r['L3']['rows'][3]['diag']['inspan'].__setitem__('tracked', False)),
        (4, 'the in-span block on the radical lift', lambda r: first(r['L3'])['diag']['inspan'].__setitem__('ov_z', 0.5)),
        (5, 'a level-3 cluster dimension of 8', lambda r: r['L3']['rows'][2]['cand'].__setitem__('dim', 8)),
        (6, 'the Krein count unbalanced', lambda r: first(r['L3'])['cand'].__setitem__('balanced', False)),
        (7, 'a veto failure', lambda r: [x['veto'].update(ok=False) for x in r['cross'] if x['veto']['applies']][:1]),
        (8, 'a cross-level point below 5.66 passing', lambda r: [x['cross'].update(ok=True, why='worst ratio 0.1') for x in r['cross'] if x['eps'] < 5.6][:1]),
    ]
    parent = [ok for _, ok in evaluate(R)]
    out = []
    for k, label, f in arms:
        r = copy.deepcopy(R)
        try:
            f(r)
            got = [ok for _, ok in evaluate(r)]
        except Exception as e:
            out.append(dict(check=k + 1, mutation=label, caught=False, error=str(e)))
            continue
        out.append(dict(check=k + 1, mutation=label,
                        caught=bool(parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k)),
                        parent_passed=bool(parent[k])))
    return out


def main_eval():
    L3 = json.load(open(os.path.join(HERE, 'control_2a_L3.json')))
    L2 = json.load(open(os.path.join(HERE, 'control_2a_L2.json')))
    R = dict(L3=L3, L2=L2)
    R['cross'] = cross_and_veto(L3, L2)
    checks = evaluate(R)
    rd = readings(R)
    muts = mutations(R)
    S = dict(control='2a', register='REGISTER_2.md, registered 2026-10-09T01:21:48Z',
             written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             checks=[dict(check=c, passed=bool(ok)) for c, ok in checks], all_passed=all(ok for _, ok in checks),
             readings=rd, mutations=muts, cross=R['cross'],
             summary=dict(L3_end=L3['end'], L2_end=L2['end'], L3_seconds=L3['seconds'], L2_seconds=L2['seconds'],
                          L3_errors=L3['errors'], L2_errors=L2['errors']))
    json.dump(S, open(os.path.join(HERE, 'control_2a.json'), 'w'), indent=1, default=float)
    L = [f'M8.15.x control 2a: {S["written"]}', f'readings: {rd}', '']
    for x in R['cross']:
        L.append(f'  cross eps {x["eps"]:.4g}: {x["cross"]}; veto {x["veto"]}')
    L.append('')
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {S["all_passed"]}')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  check {m["check"]}: {m["mutation"]}' for m in muts]
    open(os.path.join(HERE, 'control_2a.log'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    args = sys.argv[1:]
    level = args[args.index('--level') + 1] if '--level' in args else 'all'
    emax = float(args[args.index('--ladder-max') + 1]) if '--ladder-max' in args else 72.0
    if emax != 72.0:
        TAG = '_plumbing'
    lg = lambda s: print(s, flush=True)
    if '--plumbing-mesh' in args:
        TAG = '_plumbing_mesh'
        run_level(3, emax, lg, mesh_level=int(args[args.index('--plumbing-mesh') + 1]))
        sys.exit(0)
    if level in ('3', 'all'):
        run_level(3, emax, lg)
    if level in ('2', 'all'):
        run_level(2, emax, lg)
    if level in ('eval', 'all'):
        main_eval()
