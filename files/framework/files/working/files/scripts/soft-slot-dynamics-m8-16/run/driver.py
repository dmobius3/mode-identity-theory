#!/usr/bin/env python3
"""The registered run (registration/m8_16_task_details.md: THE RUN; DRIVER_PLAN.md v4; BOUNDARY.md's amendment 4).

Usage: driver.py [--dry] [--cutoffs N1 N2 N3]
  real:  the cases of run/FROZEN.json, admitted by devtools.frozen(); outputs under run/out/.
  --dry: the cases of run/DRY.json, GO cases only, admitted by today's GO list; outputs under run/dry/.
  --cutoffs: the dry run only, for a plumbing pass at other cutoffs, never scored; it records a stop and
             continues, so every code path runs.

The order: C1, C2a, C2b, C3, then R5's coherent branch, then the pyramid; then the rows, each refused until the gate
record shows K1 to K4 passed. Each case runs all its points at every cutoff, each cutoff on its own path from the seed,
and its checks are read once it completes. A failed check of C1 to C3 or the pyramid stops the run before the next
case, and the gate record is written then, with what ran and the failing checks named; the verdict is then NOT
QUALIFIED, naming them, while `incomplete` is kept for a dry run and for an interruption (UB). R5's control gates the
R5 rows only: if it fails, they are recorded as not qualified, with its failing check named, and are not run, and the
run continues. At a withheld point the branch is solved and accepted, and no record is computed (checks.withheld). At
the end, and at a stop, VERDICT.json and the transcript, driver.out, are written, each with its SHA-256 in the run's
log (UB). An interruption is resumed (UA, UB). The run's log records the manifest's SHA-256 when the run starts, and a
resume refuses a tree whose manifest differs, and a log whose gate record names a stop. Each completed case is loaded
with its outputs checked against the SHA-256 the log recorded, and its stop test is read again before the next case
runs. The run restarts at the first case whose outputs are incomplete, and an incomplete case's partial outputs move to
interrupted/.

The dry run's claims, derived before it runs (DRIVER_PLAN.md v2), are scored at its end. A claim that reads a case
which did not run, or a development record without the field it compares, is not evaluated, and counts as failed;
the run's entry is written either way (DEVLOG 218, 245).
  E1. K1, K2 (C2a, C2b) and K4 pass on C1 to C3, and the R5 control passes. The dry gate record shows each as passed
      on the GO controls, with the pyramid's parts and K3 marked absent, and the row gate refuses it.
  E2. Unscored code paths on the controls: K5 passes on C2a, C2b and C3 at eps = 0.25 with their frozen spectra; K3 on
      C2a at 0.25 reads 'not resolved, kernel exact', with its sentence, at (b), since C2a's slow pairs are all
      Krein-positive, with (c) and (d) computed on its smallest pair and reported (checks.k3_probe for (d)).
  E3. K6 reads C2a's six read points as agreeing with M8.15.
  E4. The withheld point, eps = 0.707, is accepted and has no record.
  E5. At 0.25, 0.5, 1 and 2, C2a's ladder segment and C2a's sample read the same type and indices, with every slow
      eigenvalue within the larger margin of the two records.
  E6. Where they overlap, the readings equal development's. The type and the indices, against the samples in dev/runs:
      C2a's (entry 170), C2b's (160), C3's (161) and R5's coherent sample (201). Every slow eigenvalue, counted with
      its multiplicity, against the samples that saved them: C2a's (170) and R5's (201), and D7's samples of C2b and C3
      (entries 70 and 71), each value read in its case's class; each within the larger margin of the two records.
      Against D7, whose margins predate section 7's calibration, the dry run record's own margin is reported beside
      it, and does not replace it (UB, UA; DEVLOG 248 and 249).
  E7. Every read point of every control, at every cutoff, carries K3(a)'s certificate, and it holds: each exact
      symmetry direction within L's cut, L's zero count equal to the chains, L's gray zone empty. Its largest tangent
      residual is reported against the cut; expected at most about 10 u, C2b's R2 tangents the largest (UB on #637).
      The scorers of the runs before it (score_dry.py, test_claims.py) read E1 to E6, the claims registered for them.
"""
import datetime
import glob
import hashlib
import json
import os
import shutil
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import basis, functional as fn, linear as ln, branches as br, convergence as cv, newton, devtools  # noqa: E402
import checks as ck  # noqa: E402

U = np.finfo(float).eps
CONTROLS = ('C1', 'C2a', 'C2b', 'C3')
out_lines = []


def say(s=''):
    print(s, flush=True)
    out_lines.append(s)


def sha(path):
    return devtools.sha256(path)


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def safe(name):
    return name.replace('/', '_').replace(':', '_')


# --- the case list ------------------------------------------------------------------------------------------------
def load(dry):
    if dry:
        with open(os.path.join(HERE, 'DRY.json'), encoding='utf-8') as f:
            D = json.load(f)
        bad = [n for n, c in D['cases'].items() if c['admission'] not in devtools.GO or n in br.SEALED]
        if bad:
            raise PermissionError(f'DRY.json lists cases outside the GO list: {bad}')
        return D['order'], D['cases'], None
    F = devtools.frozen()
    for n, c in F['cases'].items():
        rep = br.representative(n) if n != 'C1' else None
        if rep is not None:
            frozen_rep = {float(m): complex(*v) for m, v in c['representative'].items()}
            if set(frozen_rep) != {float(m) for m in rep} or any(abs(frozen_rep[float(m)] - complex(v)) > 1e-12
                                                                for m, v in rep.items()):
                raise PermissionError(f'FROZEN.json representative of {n} differs from the code')
    return F['order'], F['cases'], F


# --- one point's record -------------------------------------------------------------------------------------------
def groups_of(r):
    out = []
    for g in r['groups']:
        c = g['centre']
        rep = (c.imag > 0) if g['cls'] == 'imag' else ((c.real > 0) if g['cls'] == 'real' else (c.real > 0 and c.imag > 0))
        if rep:
            out.append(dict(c=[c.real, c.imag], cls=g['cls'], size=len(g['idx']), neg=g['neg'], status=g['status'],
                            idx=[int(i) for i in g['idx']]))
    return out


def record_summary(r):
    return dict(type=r['type'], nL=int(r['nL']), nD=int(r['nD']), K=int(r['K']), kr=int(r['kr']), kc=int(r['kc']),
                ki=int(r['ki']), sdim=int(r['sdim']), ranks=list(r['jordan_ranks']), blocks=int(r['blocks']),
                leak=float(r['symmetry_leak']), v0_matches=bool(r['v0_matches']), margin=float(r['margin']),
                cluster_max=float(r['cluster_max']), outside_min=float(r['outside_min']), balance=bool(r['balance']),
                separated=bool(r['separated']), gray_count=int(np.sum(r['labels'] == 'gray')),
                unresolved=list(r['unresolved']), normA=float(r['normA']),
                krein=sorted(int(g[2]) for g in r['imag_groups'] if g[2] > 0))


def k3_arrays(Fn, K, c, L, r, group):
    """The static part of the group's eigenvector, the rotation tangents, the fibre directions, the phase partner's
    static part and the axis rotation, for K3's spans (checks.k3_spans)."""
    n2 = 2 * Fn.B.m
    s = r['V'][:n2, group['idx'][0]]
    T = br.tangent_vectors(Fn, c, K)
    X = np.column_stack(T[:3])
    fib = T[3:]
    chi = np.linalg.lstsq(L, fn.to_real(c), rcond=None)[0]
    return dict(s=s, X=X, fib=np.column_stack(fib), chi=chi, z=T[2])


def read_point(Fn, K, c, lam, case, eps, want_k3):
    t0 = time.perf_counter()
    L = Fn.hess_dense(c, lam)
    A, Bm, W = ln.first_order(L, np.sqrt(lam))
    nA = np.linalg.norm(A, 2)
    m_amp = float(np.vdot(c, c).real)
    margin = ln.margin(nA, m_amp)
    T = br.tangent_vectors(Fn, c, K)
    sym = [np.concatenate([t, np.zeros(2 * Fn.B.m)]) for t in T]
    r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=dict(dim=case['dim'], ranks=case['ranks']))
    summ = cv.summarize(r, A, W)
    mu = ck.spectrum_of_L(L)
    nL = float(np.abs(mu).max())
    order = np.argsort(np.abs(mu))
    kdim = case['chains']
    point = dict(record=record_summary(r), groups=groups_of(r), summary=summ, eig=sorted(set(Fn.B.eig.tolist())),
                 lkernel=dict(lift=float(np.abs(mu[order[:kdim]]).max() / nL), genuine=float(np.abs(mu[order[kdim]]) / nL),
                              normL=nL),
                 coefficient=float(r['cluster_max'] / np.sqrt(U * nA * max(m_amp, ln.M0))))
    # K3(a)'s certificate, from L alone: each orbit tangent's ||L t|| / (||L|| ||t||), and L's zero count and gray zone
    point['kernel'] = dict(tangent=float(max((np.linalg.norm(L @ t) / (nL * np.linalg.norm(t)) for t in T),
                                             default=np.inf)),
                           dimkerL=int(r['dimkerL']), l_resolved=bool(r['l_resolved']), chains=int(case['chains']))
    arrays = None
    if want_k3:
        pick, krein_negative = ck.k3_pick(point['groups'], ck.slow_band(case, eps))
        if pick is not None:
            arrays = k3_arrays(Fn, K, c, L, r, pick)
            point['k3_overlaps'] = dict(ck.k3_overlaps(arrays), group=pick['c'], krein_negative=krein_negative)
        else:
            point['k3_overlaps'] = dict(xy=None, z=None, axis=None, why='no group lies in the slow band', group=None,
                                        krein_negative=False)
    point['seconds_record'] = time.perf_counter() - t0
    return point, arrays, r


# --- C1, Theorem D's exact branch (D6) ------------------------------------------------------------------------------
def run_c1(case):
    out = dict(cutoffs={}, readings={}, identity={})
    lad, ended = {}, None
    for N in case['cutoffs']:
        if ended is not None:
            out['cutoffs'][str(N)] = not_checked(ended)
            continue
        B = basis.Basis('R3', N)
        Fn = fn.Functional(B)
        v = br.seed_state('C1', B)
        chk = br.orbit_checks(Fn, v)
        seed_ok = abs(chk['Q'] - 1) < 1e-12 and chk['crit'] <= 1e-12 and (chk['k'], chk['r']) == (case['k'], case['r'])
        if not seed_ok:
            ended = N
            out['cutoffs'][str(N)] = dict(seed=dict(Q=chk['Q'], crit=chk['crit'], k=chk['k'], r=chk['r'], ok=False),
                                          points={})
            say(f"   C1 N = {N}: seed FAIL; the case ends here as an instrument failure, no point computed (Seeds)")
            continue
        low = np.array([n == 2 for n, _, _ in B.index])
        pts = {}
        for p in case['points']:
            t0 = time.perf_counter()
            eps = p['eps']
            c, lam = np.sqrt(eps) * v, 8.0 + eps
            cub = Fn.cubic(c)
            res = np.linalg.norm((Fn.e - lam) * c + cub)
            size = np.linalg.norm(Fn.e * c) + lam * np.linalg.norm(c) + np.linalg.norm(cub)
            off = np.linalg.norm(np.where(low, 0, cub)) / np.linalg.norm(cub)
            point, _, r = read_point(Fn, None, c, lam, case, eps, False)
            lamA = r['lam']
            up = lamA[(r['labels'] == 'imag') & (lamA.imag > 0)]          # as the record types them (D6, UA)
            omega = np.sqrt(lam)
            pred = [2 * omega, 2 * omega, np.sqrt(4 * omega ** 2 + 2 * eps)]
            used, errs = set(), []
            for q in pred:
                d = np.abs(up.imag - q) / q
                for j in np.argsort(d):
                    if j not in used:
                        used.add(j)
                        errs.append(float(d[j]))
                        break
            rec = point['record']
            ok = (res / size < 1e-15 and off < 1e-14 and len(errs) == 3 and max(errs) < 1e-10 and rec['v0_matches']
                  and rec['blocks'] == 5 and [rec['nL'], rec['nD'], rec['K']] == [0, 0, 0] and rec['type'] == 'Elliptic'
                  and not rec['unresolved'])
            point.update(accepted=True, eps_reached=eps, lam=lam, residual_rel=float(res / size), off_level=float(off),
                         lowest_errors=errs, d6_ok=bool(ok), seconds=time.perf_counter() - t0)
            lad[(N, eps)] = (rec['type'], rec['nL'], rec['K'], sorted(up.imag[list(used)]))
            pts[ck.key(eps)] = point
        out['cutoffs'][str(N)] = dict(seed=dict(Q=chk['Q'], crit=chk['crit'], k=chk['k'], r=chk['r'], ok=seed_ok),
                                      points=pts)
        say(f"   C1 N = {N}: seed {'ok' if seed_ok else 'FAIL'}; " + ', '.join(
            f"eps {p['eps']:g} {'ok' if pts[ck.key(p['eps'])]['d6_ok'] else 'FAIL'}" for p in case['points']))
    along = ended is None
    for p in (case['points'] if along else []):
        rows = [lad[(N, p['eps'])] for N in case['cutoffs']]
        same = all(x[:3] == rows[0][:3] for x in rows)
        spread = max(max(abs(a - b) / b for a, b in zip(x[3], rows[0][3])) for x in rows)
        along &= same and spread < 1e-12
    out['d6_along_ok'] = bool(along)
    return out, {}


# --- every other case -----------------------------------------------------------------------------------------------
def embeds(Ba, Bb):
    """Refuse unless the lower cutoff's basis is the leading part of the higher's, as K6's branch identity reads it;
    an explicit raise, which python -O keeps (UB)."""
    if Bb.index[:Ba.m] != Ba.index:
        raise RuntimeError(f'the N = {Ba.N} basis does not embed in the N = {Bb.N} basis')


def not_checked(ended):
    """A cutoff after the one whose seed failed: not checked, nothing solved, as the case ended there (UA)."""
    return dict(seed=dict(Q=None, crit=None, k=None, r=None, ok=False,
                          why=f'not checked: the case ended at N = {ended}, whose seed failed its check'), points={})


def run_case(name, case, dry):
    base = 'C2a' if name == 'C2a:ladder' else name
    out = dict(cutoffs={}, readings={}, identity={})
    arrays, vec, bases, fns = {}, {}, {}, {}
    k3_here = case['role'] == 'pyramid' or (dry and name in ('C2a', 'C3'))
    ended = None                  # a failed seed ends the case before any solve (the terms, Seeds; UA on #637)
    for N in case['cutoffs']:
        if ended is not None:
            out['cutoffs'][str(N)] = not_checked(ended)
            continue
        t0 = time.perf_counter()
        B = basis.Basis(case['slot'], N)
        Fn = fn.Functional(B)
        K = fn.fibre_structure_matrix(Fn)[1] if case['slot'] == 'R2' else None
        bases[N], fns[N] = B, (Fn, K)
        u = br.seed_state(base, B)
        chk = br.orbit_checks(Fn, u, K)
        Qx = ck.num(case['Q'])
        seed_ok = abs(chk['Q'] - Qx) / Qx < 1e-12 and chk['crit'] <= 1e-12 and (chk['k'], chk['r']) == (case['k'], case['r'])
        if not seed_ok:
            ended = N
            out['cutoffs'][str(N)] = dict(seed=dict(Q=chk['Q'], crit=chk['crit'], k=chk['k'], r=chk['r'], ok=False),
                                          points={}, setup_seconds=time.perf_counter() - t0)
            say(f"   {name} N = {N}: seed FAIL; the case ends here as an instrument failure, nothing solved (Seeds)")
            continue
        pts = {}
        c_prev, lam_prev, slope, acc = np.sqrt(case['points'][0]['eps'] / chk['Q']) * u, \
            case['lam0'] + case['points'][0]['eps'], 1 / chk['Q'], False
        for p in case['points']:
            eps = p['eps']
            t1 = time.perf_counter()
            res = br.continue_to(Fn, case['lam0'], eps, c_prev, lam_prev, slope, K=K, prev_accepted=acc)
            n_eval = sum(s_['evaluations'] for s_ in res['steps'])
            if not res['ok']:
                pts[ck.key(eps)] = dict(accepted=False, reason=res['reason'])
                say(f"   {name} N = {N} eps {eps:g}: FAIL {res['reason']}; this cutoff ends here")
                break
            c, lam = res['c'], res['lam']
            accepted = abs(res['eps'] - eps) <= 1e-6 and all(s_['accepted'] for s_ in res['steps'])
            if p['read']:
                point, arr, _ = read_point(Fn, K, c, lam, case, eps, k3_here and abs(eps - 0.25) < 1e-12)
                if arr is not None:
                    arrays.update({f'{k}_N{N}': v for k, v in arr.items()})
            else:
                with ck.withheld(f'{name} N = {N} eps {eps:g}'):
                    point = dict(withheld=True)
            point.update(accepted=bool(accepted), eps_reached=float(res['eps']), lam=float(lam), m=float(res['m']),
                         evaluations=n_eval, floor_rel=float(res['info']['floor_rel']), seconds=time.perf_counter() - t1)
            pts[ck.key(eps)] = point
            vec[(N, eps)] = c
            c_prev, lam_prev, slope, acc = c, lam, res['slope'], True
        out['cutoffs'][str(N)] = dict(seed=dict(Q=chk['Q'], crit=chk['crit'], k=chk['k'], r=chk['r'], ok=bool(seed_ok)),
                                      points=pts, setup_seconds=time.perf_counter() - t0)
        ok_pts = sum(1 for q in pts.values() if q.get('accepted'))
        say(f"   {name} N = {N}, m = {B.m}: seed {'ok' if seed_ok else 'FAIL'}; {ok_pts} of {len(case['points'])} points"
            f" accepted; {time.perf_counter() - t0:.0f} s")
    Ns = case['cutoffs']
    for p in case['points']:
        if not p['read']:
            continue
        e = p['eps']
        pts = [out['cutoffs'][str(N)]['points'].get(ck.key(e)) for N in Ns]
        if not all(q and 'summary' in q for q in pts):
            out['readings'][ck.key(e)] = dict(verdict='Unresolved', type=None, reasons=['a cutoff is missing'], rows=[])
            continue
        hi = pts[-1]
        out['readings'][ck.key(e)] = ck.reading([q['summary'] for q in pts], hi['eig'], hi['lam'],
                                                hi['record']['margin'], Ns[0])
        Na, Nb = Ns[-2], Ns[-1]                  # the two highest cutoffs: N = 24 and 32 in the registered run
        if (Na, e) in vec and (Nb, e) in vec:
            B24, B32 = bases[Na], bases[Nb]
            embeds(B24, B32)
            c24 = np.concatenate([vec[(Na, e)], np.zeros(B32.m - B24.m, dtype=complex)])
            Fn32, K32 = fns[Nb]
            Qb, _, _ = newton.tangent_borders(br.tangent_vectors(Fn32, c24, K32))
            dx = fn.to_real(vec[(Nb, e)]) - fn.to_real(c24)
            d_al = float(np.linalg.norm(dx - Qb @ (Qb.T @ dx)) / np.linalg.norm(fn.to_real(c24)))
            r24, r32 = pts[-2]['record'], pts[-1]['record']
            fields = ('type', 'nL', 'nD', 'K', 'krein', 'sdim', 'ranks')
            same = all(r24[f] == r32[f] for f in fields)
            out['identity'][ck.key(e)] = dict(aligned_distance=d_al, same_record=bool(same),
                                              kept=bool(d_al <= ck.IDENTITY and same))
    return out, arrays


# --- the checks of one case -----------------------------------------------------------------------------------------
def checks_of(name, case, out, m815, dry):
    role = case['role']
    if name == 'C1':
        return ck.check_c1(out, case)
    if role in ('control', 'R5gate'):
        res = ck.check_control(out, case)
        if name in ('C2a', 'C2b'):
            res['K2'] = ck.check_k2(out, case)
        if dry and role == 'control':
            res['K5_code_path'] = ck.check_row_k5(out, case)['K5']
            if name == 'C2a':
                res['K3_code_path'] = ck.k3(out, case)
                res['K3_d_probe'] = ck.k3_probe(out, case)
        return res
    if role == 'pyramid':
        res = dict(K1=ck.check_pyramid_k1(out, case))
        res['K2'] = ck.check_k2(out, case)
        res['K3'] = ck.k3(out, case)
        res.update(ck.check_pyramid_k4(out, case))
        return res
    if role == 'dryladder':
        return ck.check_row_k6(out, case, m815)
    res = ck.check_row_k5(out, case)
    if case.get('m815'):
        res.update(ck.check_row_k6(out, case, m815))
    return res


def m815_record(case, F):
    if not case.get('m815'):
        return None
    if F is None:
        path = os.path.join(ROOT, 'reference', 'm815', f"branch_{case['m815']}.json")
    else:
        t = next(t for t in F['targets'] if t['name'] == case['m815'])
        path = os.path.join(ROOT, t['file'])
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# --- outputs, the run log, the gate --------------------------------------------------------------------------------
def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, complex):
        return [o.real, o.imag]
    if isinstance(o, np.ndarray):
        return jsonable(o.tolist())
    return o


def load_log(outdir):
    p = os.path.join(outdir, 'RUNLOG.json')
    if not os.path.exists(p):
        return dict(completed={}, gate=None, events=[])
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def save_log(outdir, log):
    with open(os.path.join(outdir, 'RUNLOG.json'), 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=1)


def resume(outdir, log, order):
    """Before a run that started earlier loads any completed case (UA, UB): the tree's manifest must equal the one its
    log recorded at the start; a run whose gate record names a stop does not resume; and each completed case's outputs
    must match the SHA-256 the log recorded. An incomplete case's partial outputs move aside."""
    if log['completed'] or log['events']:
        if log.get('manifest_sha256') != devtools.manifest()[1]:
            raise PermissionError('the run does not resume: its log records '
                                  + ("no manifest" if 'manifest_sha256' not in log else "another tree's manifest"))
        if log.get('gate'):
            p = os.path.join(outdir, log['gate']['file'])
            if not os.path.exists(p) or sha(p) != log['gate']['sha256']:
                raise PermissionError('the gate record differs from the SHA-256 the run logged')
            with open(p, encoding='utf-8') as f:
                stop = json.load(f).get('stop')
            if stop:
                raise PermissionError(f'the run stopped ({stop}): a stopped run does not resume')
    for name, rec in log['completed'].items():
        for fname, h in rec['files'].items():
            if sha(os.path.join(outdir, fname)) != h:
                raise PermissionError(f'the completed case {name}: {fname} differs from the SHA-256 the run logged')
    for name in order:
        if name in log['completed']:
            continue
        partial = glob.glob(os.path.join(outdir, safe(name) + '.*'))
        if partial:
            dest = os.path.join(outdir, 'interrupted', now().replace(':', ''))
            os.makedirs(dest, exist_ok=True)
            for f_ in partial:
                shutil.move(f_, dest)
            log['events'].append(dict(t=now(), event=f'{name}: partial outputs moved to {os.path.relpath(dest, outdir)}'))


def write_gate(outdir, log, results, stop=None, dry=False):
    gate = dict(written=now(), stop=stop, cases={n: results[n]['checks'] for n in results if
                                                 results[n]['case']['role'] in ('control', 'R5gate', 'pyramid')})
    v = ck.verdict({n: r for n, r in results.items() if r['case']['role'] != 'dryladder'}, dry=dry)
    gate.update(complete=all(n in results for n in ('C1', 'C2a', 'C2b', 'C3', 'P5')), instrument_ok=v['instrument'],
                r5_gate=v.get('r5_gate'), absent=[n for n in ('C1', 'C2a', 'C2b', 'C3', 'C2a/R5', 'P5') if n not in results])
    path = os.path.join(outdir, 'GATE.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(jsonable(gate), f, indent=1)
    log['gate'] = dict(file='GATE.json', sha256=sha(path), written=gate['written'])
    log['events'].append(dict(t=now(), event=f"gate record written, SHA-256 {log['gate']['sha256']}"))
    save_log(outdir, log)
    return gate


def row_gate(outdir, log):
    """A row runs only on a gate record whose SHA-256 equals the logged one, complete, with K1 to K4 passed."""
    path = os.path.join(outdir, 'GATE.json')
    if not log.get('gate') or not os.path.exists(path):
        raise PermissionError('no gate record: the rows wait for K1 to K4')
    if sha(path) != log['gate']['sha256']:
        raise PermissionError('the gate record differs from the SHA-256 the run logged')
    with open(path, encoding='utf-8') as f:
        gate = json.load(f)
    if not (gate['complete'] and gate['instrument_ok']):
        raise PermissionError('the gate record does not show K1 to K4 passed on every control and the pyramid')
    return gate


# --- the run -------------------------------------------------------------------------------------------------------
def main():
    dry = '--dry' in sys.argv
    cut = None
    if '--cutoffs' in sys.argv:
        if not dry:
            raise SystemExit('refused: other cutoffs are for a dry plumbing pass only')
        i = sys.argv.index('--cutoffs')
        cut = [int(x) for x in sys.argv[i + 1:i + 4]]
    if dry:
        devtools.require('dryrun')
    order, cases, F = load(dry)
    outdir = (os.path.join(HERE, 'dry') if cut is None else os.path.join(HERE, 'dry', 'plumbing')) if dry else \
        os.path.join(HERE, 'out')
    os.makedirs(outdir, exist_ok=True)
    log = load_log(outdir)
    resume(outdir, log, order)
    if 'manifest_sha256' not in log:
        log['manifest_sha256'] = devtools.manifest()[1]           # the tree the run starts on (UA, UB)
    log['events'].append(dict(t=now(), event=f"{'dry run' if dry else 'run'} started; cases {order}"))
    save_log(outdir, log)
    say(f"M8.16 {'dry run' if dry else 'registered run'}: {len(order)} cases; outputs in {os.path.relpath(outdir, ROOT)}")
    results, t_all = {}, time.perf_counter()
    for name in order:
        case = dict(cases[name])
        if cut is not None:
            case['cutoffs'] = cut
        devtools.require(case['admission'])
        if name in log['completed']:
            with open(os.path.join(outdir, safe(name) + '.json'), encoding='utf-8') as f:
                results[name] = json.load(f)
            say(f"{name}: completed earlier, outputs checked against the log; its stop test is read again")
        else:
            if case['role'] == 'row':
                row_gate(outdir, log)
                if case['slot'] == 'R5' and ck.r5_failed(results):
                    why = f"the R5 control failed {', '.join(ck.r5_failed(results))} (amendment 4)"
                    results[name] = dict(case=case, checks=dict(K5=False, not_run=why))
                    say(f"{name}: not run, {why}")
                    continue
            t0 = time.perf_counter()
            say(f"{name} ({case['role']}, {case['slot']}):")
            run = run_c1 if name == 'C1' else (lambda c: run_case(name, c, dry))
            out, arrays = run(case)
            m815 = m815_record(case, F)
            out['checks'] = checks_of(name, case, out, m815, dry)
            out['case'] = case
            out['seconds'] = time.perf_counter() - t0
            jpath = os.path.join(outdir, safe(name) + '.json')
            with open(jpath, 'w', encoding='utf-8') as f:
                json.dump(jsonable(out), f, indent=1)
            files = {os.path.basename(jpath): sha(jpath)}
            if arrays:
                npath = os.path.join(outdir, safe(name) + '.npz')
                np.savez(npath, **arrays)
                files[os.path.basename(npath)] = sha(npath)
            log['completed'][name] = dict(files=files, t=now())
            log['events'].append(dict(t=now(), event=f'{name} completed'))
            save_log(outdir, log)
            with open(jpath, encoding='utf-8') as f:
                results[name] = json.load(f)
            chk = results[name]['checks']
            say(f"   checks: { {k: v for k, v in chk.items() if not isinstance(v, (dict, list))} };"
                f" {out['seconds']:.0f} s")
        if name in CONTROLS + ('P5',):
            failed = ck.stop_checks(name, results[name]['checks'])
            if failed:
                stop = f"{name} failed {', '.join(failed)}"
                if cut is not None:
                    say(f"   (plumbing pass: {stop}, which stops a real or dry run here; continuing)")
                else:
                    write_gate(outdir, log, results, stop=stop, dry=dry)
                    say(f"STOP: {stop}; the gate record is written")
                    break
        if (name == 'P5' or (dry and name == 'C2a/R5')) and not log.get('gate'):
            write_gate(outdir, log, results, dry=dry)
    if not log.get('gate'):
        write_gate(outdir, log, results, dry=dry)
    v = ck.verdict({n: r for n, r in results.items() if r['case']['role'] != 'dryladder'}, dry=dry)
    vpath, tpath = os.path.join(outdir, 'VERDICT.json'), os.path.join(outdir, 'driver.out')
    with open(vpath, 'w', encoding='utf-8') as f:
        json.dump(jsonable(v), f, indent=1)
    say(f"verdict: {v}; {time.perf_counter() - t_all:.0f} s")
    with open(tpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')
    log['verdict'] = dict(file='VERDICT.json', sha256=sha(vpath), written=now())       # UB
    log['transcript'] = dict(file='driver.out', sha256=sha(tpath), written=now())
    log['events'].append(dict(t=now(), event=f"verdict ({v['verdict']}) and transcript written"))
    save_log(outdir, log)
    if dry:
        dry_claims(outdir, results, log, cut)


# --- the dry run's claims -------------------------------------------------------------------------------------------
def slow_centres(point, band):
    return sorted((complex(*g['c']) for g in point['groups'] if np.hypot(*g['c']) <= band), key=abs)


def same_reading(pa, pb, case, eps):
    """The same type and indices, and every slow eigenvalue within the larger margin of the two records."""
    ra, rb = pa['record'], pb['record']
    if (ra['type'], ra['nL'], ra['nD'], ra['K']) != (rb['type'], rb['nL'], rb['nD'], rb['K']):
        return False
    band = ck.slow_band(case, eps)
    a, b = slow_centres(pa, band), slow_centres(pb, band)
    tol = max(ra['margin'], rb['margin'])
    return len(a) == len(b) and all(abs(x - y) <= tol for x, y in zip(a, b))


# E6's references (UB, UA; DEVLOG 248 and 249): for each control, the development record read for the type and
# the indices, the one read for the slow eigenvalues, and how those are read.
E6_REFS = {
    'C2a': ('dev/runs/170_sep_controls_C2a_sample.json', 'dev/runs/170_sep_controls_C2a_sample.json', 'groups'),
    'C2b': ('dev/runs/160_sep_controls_C2b_sample.json', 'dev/runs/070_d7_C2b_N16_24_32.json', 'imag'),
    'C3': ('dev/runs/161_sep_controls_C3_sample.json', 'dev/runs/071_d7_C3_N16_24_32.json', 'real'),
    'C2a/R5': ('dev/runs/201_r5_control.json', 'dev/runs/201_r5_control.json', 'imag'),
}


def ref_points(path):
    """A development run's saved points, (N, eps) -> the point as saved, from its logged JSON."""
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        J = json.load(f)
    out = {}
    for k, v in J.items():
        if k.startswith('N') and '_eps' in k and isinstance(v, dict) and v.get('accepted', v.get('ok', True)):
            N, e = k[1:].split('_eps')
            out[(int(N), float(e))] = v
    return out


def with_multiplicity(groups, band):
    """Each group's centre below the band, once for each eigenvalue the group holds, smallest first."""
    return sorted((complex(*g['c']) for g in groups for _ in range(g['size']) if np.hypot(*g['c']) <= band), key=abs)


def ref_slow(v, how, band):
    """A development point's slow eigenvalues below the band, with multiplicity, read in its case's class, and its
    record's margin. A KeyError where the point saved no such field."""
    if how == 'groups':
        return with_multiplicity(v['summary']['groups'], band), v['summary']['margin']
    vals = [1j * x if how == 'imag' else complex(x, 0.0) for x in v['slow']]
    return sorted((z for z in vals if abs(z) <= band), key=abs), v['margin'] if 'margin' in v else v['record']['margin']


def e6(results):
    """E6 (the module docstring) at every point the dry run shares with a reference: (verdict, rows, missing). The
    verdict is None where a reference lacks a field the claim compares: not evaluated, never an exception (UB, UA)."""
    rows, missing = [], []
    for name, (ipath, epath, how) in E6_REFS.items():
        R = results[name]
        I, E = ref_points(ipath), ref_points(epath)
        for (N, e), v in sorted(I.items()):
            p = R['cutoffs'].get(str(N), {}).get('points', {}).get(ck.key(e))
            if not p or 'record' not in p:
                continue
            r, band = p['record'], ck.slow_band(R['case'], e)
            try:
                d = v['record'] if 'record' in v else v
                idx = (d['type'], d['nL'], d['nD'], d['K'])
                theirs, m_ref = ref_slow(E[(N, e)], how, band)
            except KeyError as err:
                missing.append(f'{name} at N = {N}, eps = {e:g}: {err}')
                continue
            mine = with_multiplicity(p['summary']['groups'], band)
            dist = max((abs(x - y) for x, y in zip(mine, theirs)), default=0.0)
            rows.append(dict(case=name, N=N, eps=e, same=(r['type'], r['nL'], r['nD'], r['K']) == idx,
                             count=(len(mine), len(theirs)), d=dist, tol=max(r['margin'], m_ref), own=r['margin'],
                             d7=epath != ipath))
    if missing or not rows:
        return None, rows, missing
    return all(x['same'] and x['count'][0] == x['count'][1] and x['d'] <= x['tol'] for x in rows), rows, missing


def e7(results):
    """E7 (the module docstring): (verdict, largest tangent residual over u, missing). The verdict is None where a read
    point lacks the certificate: not evaluated, never an exception."""
    worst, missing, held = 0.0, [], True
    for n in CONTROLS + ('C2a/R5',):
        R = results[n]
        for N, c in R['cutoffs'].items():
            for e, p in c['points'].items():
                if 'record' not in p:
                    continue
                if 'kernel' not in p:
                    missing.append(f'{n} at N = {N}, eps = {e}')
                    continue
                held &= ck.kernel_exact(p, R['case'])
                worst = max(worst, p['kernel']['tangent'] / ck.ln.U)
    return (None if missing else bool(held)), worst, missing


def dry_claims(outdir, results, log, cut, e7_claim=True):
    say('The dry run\'s claims, derived before it ran (the module docstring):')
    ok = {}
    gate_path = os.path.join(outdir, 'GATE.json')
    with open(gate_path, encoding='utf-8') as f:
        gate = json.load(f)
    c = {n: results[n]['checks'] for n in results}

    def ran(tag, names):
        """Whether every case the claim reads ran; if one did not, the run having stopped, the claim is not evaluated
        and counts as failed (DEVLOG 218)."""
        missing = [n for n in names if n not in results]
        if missing:
            ok[tag] = None
            say(f"{tag}. not evaluated: {', '.join(missing)} did not run")
        return not missing

    if ran('E1', CONTROLS + ('C2a/R5',)):
        e1 = (all(c[n]['K1'] and c[n]['K4'] for n in CONTROLS) and c['C2a']['K2'] and c['C2b']['K2']
              and c['C2a/R5']['K1'] and c['C2a/R5']['K4'] and not gate['complete'] and 'P5' in gate['absent'])
        try:
            row_gate(outdir, log)
            refused = False
        except PermissionError:
            refused = True
        ok['E1'] = e1 and refused
        say(f"E1. the controls and the R5 control pass, and the row gate refuses the dry gate record: {ok['E1']}")
    if ran('E2', ('C2a', 'C2b', 'C3')):
        k3c = c['C2a'].get('K3_code_path', {})
        ok['E2'] = (all(c[n].get('K5_code_path') for n in ('C2a', 'C2b', 'C3'))
                    and str(k3c.get('outcome')).split(':')[0] == 'not resolved, kernel exact'
                    and not any(v['b'] for v in k3c.get('per_N', {}).values()))
        ov = {N: v.get('overlaps') for N, v in k3c.get('per_N', {}).items()}
        say(f"E2. K5 passes on C2a, C2b and C3 at 0.25; K3 on C2a reads {k3c.get('outcome')!r} at (b): {ok['E2']};"
            f" (c) on C2a's smallest pair, reported: {ov}")
        if 'K3_d_probe' in c['C2a']:
            say(f"    (d) on that pair, reported: {c['C2a']['K3_d_probe']}")
    if ran('E3', ('C2a:ladder',)):
        lad = c['C2a:ladder']
        agree = [r['eps'] for r in lad.get('rows', []) if r['status'] == 'agrees']
        ok['E3'] = len(agree) == 6 and lad.get('accepted', False)
        say(f"E3. K6 on C2a's ladder segment: {len(agree)} of {len(lad.get('rows', []))} read points agree with M8.15:"
            f" {ok['E3']}")
    L = results.get('C2a:ladder', {}).get('cutoffs', {})
    if ran('E4', ('C2a:ladder',)):
        wh = [L[N]['points'].get(ck.key(0.25 * 2 ** 1.5)) for N in L]
        ok['E4'] = bool(wh) and all(p and p.get('accepted') and 'record' not in p and p.get('withheld') for p in wh)
        say(f"E4. the withheld point is accepted at every cutoff and has no record: {ok['E4']}")
    if ran('E5', ('C2a', 'C2a:ladder')):
        case = results['C2a']['case']
        e5 = True
        for e in (0.25, 0.5, 1.0, 2.0):
            for N in results['C2a']['cutoffs']:
                pa = results['C2a']['cutoffs'][N]['points'].get(ck.key(e))
                pb = L.get(N, {}).get('points', {}).get(ck.key(e))
                e5 &= bool(pa and pb and 'record' in pa and 'record' in pb and same_reading(pa, pb, case, e))
        ok['E5'] = e5
        say(f"E5. C2a's ladder segment and sample read the same at 0.25, 0.5, 1 and 2: {ok['E5']}")
    if ran('E6', ('C2a', 'C2b', 'C3', 'C2a/R5')):
        if cut is not None:
            ok['E6'] = True
            say('E6. not read in a plumbing pass')
        else:
            v6, rows, missing = e6(results)
            ok['E6'] = v6
            if v6 is None:
                say(f"E6. not evaluated: a development record lacks a field the claim compares: "
                    f"{'; '.join(missing[:4]) or 'no overlapping point'}")
            else:
                held = lambda x, tol: x['count'][0] == x['count'][1] and x['d'] <= tol      # noqa: E731
                d7 = [x for x in rows if x['d7']]
                say(f"E6. the readings equal development's at {len(rows)} overlapping points: the type and the indices"
                    f" at {sum(x['same'] for x in rows)}, every slow eigenvalue within the larger margin of the two"
                    f" records at {sum(held(x, x['tol']) for x in rows)}: {v6}; the largest difference"
                    f" {max(x['d'] for x in rows):.1e}. Reported beside it, against D7: within the dry run record's own"
                    f" margin at {sum(held(x, x['own']) for x in d7)} of {len(d7)}")
    if e7_claim and ran('E7', CONTROLS + ('C2a/R5',)):
        v7, worst, miss7 = e7(results)
        ok['E7'] = v7
        if v7 is None:
            say(f"E7. not evaluated: a read point lacks K3(a)'s certificate: {'; '.join(miss7[:4])}")
        else:
            say(f"E7. K3(a)'s certificate at every read point of every control: {v7}; the largest tangent residual"
                f" {worst:.2g} u, against the cut's {ck.ln.L_CUT / ck.ln.U:.0f} u")
    failed = sum(v is not True for v in ok.values())
    say(f"{failed} of the dry run's claims failed or were not evaluated" +
        (' (plumbing pass, unscored)' if cut is not None else ''))
    path = os.path.join(outdir, 'driver_dry.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines) + '\n')
    outputs = [path, os.path.join(outdir, 'driver.out'), gate_path, os.path.join(outdir, 'VERDICT.json'),
               os.path.join(outdir, 'RUNLOG.json')]
    devtools.log_run(os.path.abspath(__file__), 'dryrun',
                     [f"Step 3's dry run{' (a plumbing pass at cutoffs ' + str(cut) + ', unscored)' if cut else ''}:"
                      f" {'PASS' if not failed else 'FAIL'} ({failed} of {len(ok)} claims failed or not evaluated):"
                      f" {ok}.",
                      'The claims were derived before the run (the driver\'s docstring; DRIVER_PLAN.md v2). The run\'s'
                      ' per-case outputs and their SHA-256 are in its RUNLOG.json.'], outputs=outputs)


if __name__ == '__main__':
    main()
