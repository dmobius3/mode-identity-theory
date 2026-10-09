"""One M8.15 branch under the frozen rules: the linear record at level 3 with its level-2 cross-checks, change-of-type
bisection, and the persistence tests at level 2.

  python3 m815_branch.py <case> <slot> [--eps-max E]

Targets (T1-T5) refuse to run unless out/FROZEN.json exists with the frozen numbers and the terms' hash; a control
name runs the same code path for testing. Every computed number is written to out/branch_<case>_R<slot>.json."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment: one thread, so sums are taken in a fixed order

import sys, os, json, time, argparse
import numpy as np
from m815_common import (LevelCase, FROZEN_DIM, predicted, classify, match, schedule, kappa, ladder, EPS_MAX, SPECTRA)
from linearize import Linearization
from verdict import Verdict, representatives
from nonlinear import to_complex
from persistence import run_test

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
HERE = os.path.dirname(os.path.abspath(__file__))
STAGE = {'stage': 'start'}      # the last stage entered, for the crash record (M8.15.x § 4)
TEST = {}                       # bench hooks for the armed controls, controls only: 'maxit', 'raise_at'
RUN = {}                        # the run's frozen block, and the freeze's terms hash and solver commit, for the crash record


def stage(name):
    STAGE['stage'] = name
    if TEST.get('raise_at') == name:
        raise RuntimeError(f'forced exception at stage {name} (armed control, controls only)')


def write_json_atomic(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=1, default=str)
    os.replace(tmp, path)
TARGETS = {'T1', 'T2', 'T3', 'T4', 'T5'}
RADICAL_ALL = {'T2', 'T3', 'T5', 'C3', 'C3s'}


def frozen_numbers(name):
    path = os.path.join(OUT, 'FROZEN.json')
    if name in TARGETS:
        if not os.path.exists(path):
            raise SystemExit(f'{name} is a target: refused, no freeze record ({path}).')
        fz = json.load(open(path))
        if not fz.get('frozen') or not fz.get('terms_sha256'):
            raise SystemExit(f'{name} is a target: refused, the freeze record is incomplete.')
        return fz
    # controls: the closing numbers if present, else bench defaults (testing only)
    alt = os.path.join(OUT, 'freeze_numbers.json')
    fz = json.load(open(alt)) if os.path.exists(alt) else {}
    fz.setdefault('r_f', {'3': 4e-6, '2': 4e-5})
    fz.setdefault('delta_lev', 1e-2)
    fz.setdefault('s2', {'R4': 6.74e-4, 'R5': 9.55e-4, 'R2': 2.14e-3})
    fz.setdefault('eta', 1e-3); fz.setdefault('T', 1000.0)
    return fz


def cj(z):
    return [float(np.real(z)), float(np.imag(z))]


def peak_gb():
    """The process's peak resident size so far (ru_maxrss: bytes on macOS, KiB on Linux)."""
    import resource
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / (2 ** 30 if sys.platform == 'darwin' else 2 ** 20)


class Point:
    """The verdict data at one eps on one level, reduced to what the rules read."""
    def __init__(self, lc, rec, eps_k, tau0, tau_re, keep_cluster=False):
        Phi, sigma = to_complex(rec['x']), rec['sigma']
        lin = Linearization(lc.st, Phi, sigma)
        v = Verdict(lc.st, lc.case, lin, Phi, sigma, lc.lam0_min, lc.rot, FROZEN_DIM[lc.name], rigid=lc.rigid,
                    slices=lc.slices, tau0=tau0, tau_re=tau_re)
        self.eps, self.eps_reached, self.sigma, self.m = eps_k, rec['eps'], sigma, rec['m']
        self.dim, self.closed, self.omega_gram = v.dim, bool(v.closed), float(v.omega_gram)
        self.cluster_ok = (v.dim == v.frozen_dim) and self.closed and self.omega_gram >= 1e-6
        lab = (v.cls == 'lifted') | (v.cls == 'rigid')
        self.lifted = v.vals[lab]
        # which lifted modes are radical: all of them where every rotation direction is radical; in T4 only the
        # rotation about the pinned 2-fold axis (the slice direction), by the larger static overlap
        from verdict import static_overlap, real_orthonormal
        kind = []
        for vec in v.vecs[:, lab].T:
            if lc.name in RADICAL_ALL:
                kind.append('radical')
            elif lc.slices:
                S = real_orthonormal(np.column_stack(lc.slices), lc.st.Mr)
                o = static_overlap(vec, S, lc.st.Mr, v.n2)
                kind.append('radical' if o ** 2 >= 0.5 else 'paired')
            else:
                kind.append('paired')
        self.kind = kind
        self.genuine_all = list(v.genuine_all)
        self.genuine = [(l, k) for l, k in v.genuine]
        kr, kc, kim, rhs = v.count(tau_re)
        self.kr, self.kc, self.kim, self.rhs = kr, kc, kim, rhs
        self.balanced = (kr + 2 * kc + 2 * kim == rhs)
        self.fast = None
        if not self.balanced:
            fast = v.fast_search(np.sqrt(sigma), tau_re)
            kr2 = kr + sum(1 for l, k in fast if l.real > tau_re and abs(l.imag) <= tau_re)
            kc2 = kc + sum(1 for l, k in fast if l.real > tau_re and abs(l.imag) > tau_re)
            ki2 = kim + sum(1 for l, k in fast if l.real <= tau_re and k < 0)
            self.fast = dict(found=[[cj(l), k] for l, k in fast], counts=[kr2, kc2, ki2],
                             balanced=(kr2 + 2 * kc2 + 2 * ki2 == rhs))
        self.nL, self.nB = v.nL, v.nB_cluster
        self.bwe = float(v.bwe.max())
        self.zero_crossing = any(abs(l) <= tau0 for l, _ in self.genuine)
        self.residual = rec['full']
        self.slice_force = [float(x) for x in rec['nu']]
        self.gauge_multipliers = [float(x) for x in rec['mu']]
        if keep_cluster:
            self.v, self.Phi = v, Phi
            # the slow subspace S: G_tol plus the genuine modes among the 2 nE0 slowest, with its gap ratio
            self.S = v.slow_basis()
            gen = np.abs(v.vals[v.cls == 'genuine'])
            self.S_gap = (float(v.gap[1] / gen.max()) if len(gen) else np.inf)
            self.S_dim = int(self.S.shape[1])
            self.nslow = int(len(v.vals))

    def reps(self, tau_re):
        """The representatives and their classes, both read at tau_re (the cross-level check reads both levels at
        level 3's)."""
        return [(l, classify(l, k, tau_re)) for l, k in representatives(self.genuine_all, tau_re)]

    def record(self):
        return dict(eps=self.eps, eps_reached=self.eps_reached, sigma=self.sigma, m=self.m, dim=self.dim,
                    closed=self.closed, omega_gram=self.omega_gram, cluster_ok=self.cluster_ok,
                    lifted=[cj(l) for l in self.lifted], lifted_kind=self.kind, genuine=[[cj(l), float(k)] for l, k in self.genuine],
                    genuine_all=[[cj(l), float(k)] for l, k in self.genuine_all],
                    kr=self.kr, kc=self.kc, ki_minus=self.kim, nL=self.nL, nB_cluster=self.nB, balanced=self.balanced,
                    zero_crossing=self.zero_crossing, backward_error=self.bwe, residual=self.residual,
                    slice_force=self.slice_force, gauge_multipliers=self.gauge_multipliers, fast_search=self.fast)


def cross_level(p3, p2, tau_re, s2, omega0):
    """The frozen cross-level check: matching within classes, then |l3 - l2| <= 0.01 max(|l3|, |l2|) + s2/omega0."""
    pairs = match(p3.reps(tau_re), p2.reps(tau_re))
    if pairs is None:
        return False, 'class counts differ'
    worst = 0.0
    for a, b, c in pairs:
        tol = 0.01 * max(abs(a), abs(b)) + s2 / omega0
        worst = max(worst, abs(a - b) / tol)
    return bool(worst <= 1.0), f'worst ratio to tolerance {worst:.3f}'


def bisect(lo, hi, ta, tb, state, step, typer, tol=0.02):
    """Change-of-type bisection to tol relative in eps. step(mid, state) -> the new state or None; typer(mid, state)
    -> (type, why). Returns (lo, hi, note, trail)."""
    note, trail = 'located', []
    while (hi - lo) / lo > tol:
        mid = (lo + hi) / 2
        new = step(mid, state)
        if new is None:
            note = 'continuation failed inside the bracket'
            break
        tm, why = typer(mid, new)
        trail.append((mid, tm))
        if tm == ta:
            lo, state = mid, new
        elif tm == tb:
            hi = mid
        else:
            note = f'Unresolved inside the bracket at {mid:.6g} ({", ".join(why)})'
            break
    return lo, hi, note, trail


def slow_lineage(reached, P2, nslow, start_ok):
    """S tracked along the level-2 ladder: the frozen dimension 2 nE0, a gap |lambda_next| >= 2 max over S minus G of
    |lambda|, and continuity: every principal cosine with the previous S at least 0.9 (at eps_min, the start test
    start_ok instead). The first failure ends the lineage; there is no re-entry. Returns (valid points, records)."""
    valid, recs, prev = [], [], None
    for e in reached:
        p = P2.get(e)
        if p is None:
            break
        ok_dim = p.S_dim == nslow
        ok_gap = p.S_gap >= 2.0
        if prev is None:
            cos, ok_cont = None, bool(start_ok)
        else:
            C = p.v.ps.inner(prev.S, p.S)
            cos = float(np.linalg.svd(C, compute_uv=False).min()) if C.size else 1.0
            ok_cont = cos >= 0.9 and prev.S_dim == p.S_dim
        recs.append(dict(eps=e, dim=p.S_dim, gap=p.S_gap, min_cosine=cos, ok=bool(ok_dim and ok_gap and ok_cont)))
        if not (ok_dim and ok_gap and ok_cont):
            break
        valid.append(e)
        prev = p
    return valid, recs


def run_branch(name, slot, eps_max=None, log=print, levels=(3, 2), T_override=None):
    fz = frozen_numbers(name)
    rf3, rf2 = float(fz['r_f']['3']), float(fz['r_f']['2'])
    tau0_3, tau0_2 = 10 * rf3, 10 * rf2
    dlev = float(fz['delta_lev'])
    s2 = float(fz['s2'][f'R{slot}'])
    eta, T = float(fz['eta']), float(T_override or fz['T'])
    emax = eps_max or EPS_MAX[slot]
    targets = ladder(0.25, emax)
    sch = schedule(name, slot, rf3, targets) if name in SPECTRA else []
    out = dict(case=name, slot=slot, targets=targets, schedule=sch,
               frozen=dict(r_f3=rf3, r_f2=rf2, delta_lev=dlev, s2=s2, eta=eta, T=T),
               points=[], level2=[], cross=[], types=[], changes=[], persistence=[])
    RUN.update(frozen=out['frozen'], **{k: fz[k] for k in ('terms_sha256', 'solver_commit') if k in fz})
    # level 3: the linear record
    t0 = time.time()
    stage('level 3 setup')
    lc3 = LevelCase(levels[0], name, slot)
    P3, R3 = {}, {}
    def on3(k, eps_k, rec):
        p = Point(lc3, rec, eps_k, tau0_3, tau0_3)
        P3[eps_k], R3[eps_k] = p, rec
        out['points'].append(p.record())
        log(f'  L3 eps {eps_k:.4g}: cluster {p.dim}/{FROZEN_DIM[name]} ok={p.cluster_ok}; Krein {p.kr},{p.kc},{p.kim} vs {p.rhs} '
            f'{"balanced" if p.balanced else "UNBALANCED"}; zero-crossing {p.zero_crossing}; lifted max {max(abs(p.lifted), default=0):.2e}; '
            f'peak resident {peak_gb():.1f} GB')
    stage('level 3 ladder')
    if TEST.get('maxit') is not None:
        from continuation import Branch
        br3 = Branch(lc3.st, lc3.case, lc3.lam0, lc3.Q, lc3.vol, slices=lc3.slices, maxit=TEST['maxit'],
                     log=lambda s: None).run(targets, on_point=on3)
    else:
        br3 = lc3.branch(targets, on3)
    out['end'] = [str(br3.end[0]), br3.end[1]]
    out['seconds_L3'] = time.time() - t0
    reached = [e for e in targets if e in P3]
    tag = '' if tuple(levels) == (3, 2) else f'_test{levels[0]}{levels[1]}'
    if not reached:
        # a branch end with no ladder point (M8.15.x § 4): the level-2 phase and persistence have nothing to do
        stage('record')
        log(f'  no level-3 ladder point: the branch ended with {out["end"][0]}; level 2 and persistence skipped')
        write_json_atomic(os.path.join(OUT, f'branch_{name}_R{slot}{tag}.json'), out)
        return out
    stage('validity')
    # validity at eps_min: every resolved mode within 5% of the leading order, types and Krein signs exactly
    if name in SPECTRA and 0.25 in P3:
        from scipy.optimize import linear_sum_assignment
        p = P3[0.25]
        pred = predicted(name, slot, 0.25)
        res_modes = [(l, sg) for (l, sg), sc in zip(pred, sch) if sc['first_resolved'] == 0.25]
        comp = [(l, 'r' if abs(l.imag) <= tau0_3 else ('i+' if k > 0 else 'i-')) for l, k in p.genuine]
        want = [(l, 'r' if l.imag == 0 else ('i+' if sg > 0 else 'i-')) for l, sg in res_modes]
        okv, worst = True, 0.0
        for cls in set(c for _, c in want):
            a = [abs(l) for l, c in want if c == cls]
            b = sorted([abs(l) for l, c in comp if c == cls])
            if len(b) < len(a):
                okv = False
                continue
            Cm = np.abs(np.subtract.outer(np.array(a), np.array(b)) / np.array(a)[:, None])
            r, cc = linear_sum_assignment(Cm)
            worst = max(worst, Cm[r, cc].max())
        okv = okv and worst <= 0.05
        out['validity_eps_min'] = dict(ok=bool(okv), worst_relative=float(worst))
        log(f'  validity at eps_min: {"pass" if okv else "INVALID BRANCH"} (worst {worst:.3%})')
    # level 2: the cross-checks and the persistence clusters
    stage('level 2')
    lc2 = LevelCase(levels[1], name, slot)
    P2, R2 = {}, {}
    def on2(k, eps_k, rec):
        P2[eps_k], R2[eps_k] = Point(lc2, rec, eps_k, tau0_2, tau0_2, keep_cluster=True), rec
        out['level2'].append(P2[eps_k].record())
        p = P2[eps_k]
        log(f'  L2 eps {eps_k:.4g}: cluster {p.dim}/{FROZEN_DIM[name]} ok={p.cluster_ok}; S dim {p.S_dim}, gap {p.S_gap:.3g}; '
            f'peak resident {peak_gb():.1f} GB')
    br2 = lc2.branch(reached, on2)
    omega0 = np.sqrt(lc2.lam0)

    def decide(e, p3, p2, third):
        why = []
        if any((sc['first_resolved'] is None or sc['first_resolved'] > e) for sc in sch):
            why.append('a mode before its first-resolved point')
        if not p3.cluster_ok:
            why.append('cluster check')
        if p3.zero_crossing:
            why.append('zero crossing')
        if not p3.balanced and not (p3.fast and p3.fast['balanced']):
            why.append('Krein count unbalanced')
        if name in SPECTRA:
            bound = 0.5 * max(abs(l) for l, _ in predicted(name, slot, e))
            for l, kd in zip(p3.lifted, p3.kind):
                if kd == 'radical' and abs(l) >= bound:
                    why.append('radical bound'); break
                if kd == 'paired' and abs(l) > tau0_3:
                    why.append('paired lifted mode above tau0'); break
        if p3.bwe > 1e-10:
            why.append('eigenpair residual')
        counts = p3.fast['counts'] if (p3.fast and p3.fast['balanced']) else [p3.kr, p3.kc, p3.kim]
        cand = counts[0] + counts[1] > 0
        cross = None
        if (third or cand) and p2 is not None:
            ok, msg = cross_level(p3, p2, tau0_3, s2, omega0)
            cross = dict(eps=e, ok=ok, msg=msg)
            if not ok:
                why.append('cross-level disagreement')
        if cand and p2 is not None:
            r3 = max((l.real for l, _ in p3.genuine), default=0.0)
            r2 = max((l.real for l, _ in p2.genuine), default=0.0)
            if not (abs(r2 - r3) <= dlev * abs(r3)):
                why.append('level stability')
        typ = 'Unresolved' if why else ('Hyperbolic' if cand else 'Elliptic')
        return typ, why, cross

    stage('types')
    for i, e in enumerate(reached):
        typ, why, cross = decide(e, P3[e], P2.get(e), i % 3 == 0)
        if cross:
            out['cross'].append(cross)
        out['types'].append(dict(eps=e, type=typ, why=why))
        log(f'  eps {e:.4g}: {typ}' + (f' ({", ".join(why)})' if why else ''))
    stage('bisection')
    # changes of type: bisection to 2% in eps between ladder points of different decided types
    T_ = {d['eps']: d['type'] for d in out['types']}
    for a, b in zip(reached[:-1], reached[1:]):
        ta, tb = T_[a], T_[b]
        if ta == tb or 'Unresolved' in (ta, tb) or a not in R2:
            continue
        def step(mid, st):
            r3 = br3.goto(mid, st[0])
            r2 = br2.goto(mid, st[1])
            return None if (r3 is None or r2 is None) else (r3, r2)
        def typer(mid, st):
            p3, p2 = Point(lc3, st[0], mid, tau0_3, tau0_3), Point(lc2, st[1], mid, tau0_2, tau0_2)
            tm, why, cross = decide(mid, p3, p2, True)
            out['points'].append(dict(p3.record(), bisection=True))
            return tm, why
        lo, hi, note, trail = bisect(a, b, ta, tb, (R3[a], R2[a]), step, typer)
        out['changes'].append(dict(from_type=ta, to_type=tb, bracket=[lo, hi], note=note))
        log(f'  change {ta} -> {tb} in [{lo:.6g}, {hi:.6g}]: {note}')
    lc3 = None
    stage('lineage')
    # the slow subspace's lineage along the level-2 ladder (starts at eps_min with validity and the cross-level check)
    nslow = 2 * (lc2.case.j2 + 1)
    start_ok = out.get('validity_eps_min', {}).get('ok', True) and all(c['ok'] for c in out['cross'] if c['eps'] == reached[0])
    S_valid, S_recs = slow_lineage(reached, P2, nslow, start_ok)
    out['slow_lineage'] = S_recs
    stage('persistence')
    # persistence at level 2: a scheduled point moves down to the last accepted elliptic ladder point below it that
    # meets the drift margin and lies inside the slow subspace's lineage
    sched_pts = []
    for frac in (1 / 8, 1 / 2):
        tgt = emax * frac
        sched_pts.append(min(targets, key=lambda e: abs(e - tgt)))
    done = set()
    for sp in sched_pts:
        cands = [e for e in reached if e <= sp and T_.get(e) == 'Elliptic' and e > 0.25 + 1e-12]
        inS = [e for e in cands if e in S_valid]
        chosen = None
        for e in sorted(inS, reverse=True):
            lv = P2[e].lifted
            r = float(np.max(lv.real)) if len(lv) else 0.0
            if r * T <= np.log(1 / (10 * eta)):
                chosen = e
                break
        if chosen is None:
            verdict = ('Not reached' if not cands else
                       ('Not run (slow subspace unresolved)' if not inS else 'Not run (floor)'))
            out['persistence'].append(dict(scheduled=sp, ran_at=None, verdict=verdict))
            log(f'  persistence scheduled {sp:.4g}: {verdict}')
            continue
        if chosen in done:
            out['persistence'].append(dict(scheduled=sp, ran_at=chosen, verdict='(same point as the other test)'))
            continue
        done.add(chosen)
        p2 = P2[chosen]
        res = run_test(lc2.st, p2.Phi, p2.sigma, p2.v.ps, p2.v.G, lc2.rot, lc2.case, p2.lifted, eta=eta, T=T,
                       log=log, progress=100, S=p2.S, mode='split')
        rec = res.pop('rec', None)
        if rec is not None:
            np.save(os.path.join(OUT, f'persist_{name}_R{slot}_{chosen:.4g}.npy'), rec)
        out['persistence'].append(dict(scheduled=sp, ran_at=chosen, **{k: (v if not isinstance(v, np.generic) else float(v)) for k, v in res.items()}))
        log(f'  persistence at eps {chosen:.4g} (scheduled {sp:.4g}): {res["verdict"]}')
    stage('record')
    write_json_atomic(os.path.join(OUT, f'branch_{name}_R{slot}{tag}.json'), out)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('case'); ap.add_argument('slot', type=int); ap.add_argument('--eps-max', type=float, default=None)
    ap.add_argument('--test-levels', default=None, help='bench only: e.g. 2,1 (controls only)')
    ap.add_argument('--T', type=float, default=None, help='bench only: shorter persistence runs (controls only)')
    ap.add_argument('--test-newton-maxit', type=int, default=None, help='armed control only: cap the seed Newton')
    ap.add_argument('--test-raise-at', default=None, help='armed control only: raise at this stage')
    a = ap.parse_args()
    levels = (3, 2)
    if a.test_newton_maxit is not None or a.test_raise_at:
        if a.case in TARGETS:
            raise SystemExit('test options are for controls only')
        TEST.update(maxit=a.test_newton_maxit, raise_at=a.test_raise_at)
    if a.test_levels or a.T:
        if a.case in TARGETS:
            raise SystemExit('test options are for controls only')
        if a.test_levels:
            levels = tuple(int(x) for x in a.test_levels.split(','))
    try:
        run_branch(a.case, a.slot, a.eps_max, log=lambda s: print(s, flush=True), levels=levels, T_override=a.T)
    except Exception as e:
        # an instrument exception, never a scientific branch end (M8.15.x § 4): a separate crash record, nonzero exit
        import traceback, datetime
        frames = [dict(file=(os.path.relpath(fr.filename, HERE) if os.path.abspath(fr.filename).startswith(HERE)
                             else os.path.basename(fr.filename)), line=fr.lineno, function=fr.name, code=fr.line)
                  for fr in traceback.extract_tb(e.__traceback__)]
        tag = '' if tuple(levels) == (3, 2) else f'_test{levels[0]}{levels[1]}'
        crash = dict(case=a.case, slot=a.slot, crash=True, stage=STAGE['stage'], exception=type(e).__name__,
                     message=str(e), traceback=frames, frozen=RUN.get('frozen'),
                     **{k: RUN[k] for k in ('terms_sha256', 'solver_commit') if k in RUN},
                     written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
        write_json_atomic(os.path.join(OUT, f'crash_{a.case}_R{a.slot}{tag}.json'), crash)
        print(f'INSTRUMENT EXCEPTION at stage {STAGE["stage"]}: {type(e).__name__}: {e}; crash record written', flush=True)
        sys.exit(1)
