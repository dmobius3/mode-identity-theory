"""M8.19's driver (the terms: THE INSTRUMENT, THE GATES, THE CONTROLS, THE COHERENT ROW IN R5, and THE FREEZE, THE GUARD
AND THE RUN): M8.15.x's m815_branch.py, frozen at MIT 97a8c08, with the changes the terms list. One job per process:

  python3 -I -B -u m819_branch.py JOB --out STAGING --root OUT [bench options]

The jobs (DESIGN.md): dyn_C1, dyn_C2a, dyn_C2b, dyn_C3 and rate, M8.15's dynamics controls; p5a, control 1a's M8.15.x
arm; c3e3, C3 at eps 3; c2a_dur and c2a_long, C2a/R4 at 1 through gates 3, 5, 6 and 7; controls, gate 1;
gates_T1_R4, gates_T1_R5, gates_T4_R4, gates_T4_R5 and coherent_R5, the gates; plan; test_<stretch>; record.
Point, cross_level, bisect and slow_lineage are the frozen file's, byte for byte, and so is decide, inside run_ladder.
The frozen modules are imported in place from ../../soft-slot-dynamics-m8-15x/m8_15x_solver/, and nothing is written
there. A sealed job (T1 or T4 in either slot, C2a in R5) refuses unless FROZEN.json validates and gate 1 has passed.
A job writes only into its staging folder, which the orchestrator moves into OUT once the job exits 0; an instrument
exception writes crash.json there and exits 1, and a refusal writes refused.json and exits 3."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment: one thread, so sums are taken in a fixed order

import sys, os, json, time, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INSTRUMENT = os.path.normpath(os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x', 'm8_15x_solver'))
sys.path.insert(0, HERE)
sys.path.insert(0, INSTRUMENT)
import numpy as np
from m815_common import (LevelCase, FROZEN_DIM, predicted, classify, match, schedule, kappa, ladder, EPS_MAX, SPECTRA)
from linearize import Linearization
from verdict import Verdict, representatives
from nonlinear import to_complex
from persistence import run_test
import m819_gates as G

OUT = None                      # the job's staging folder (--out), set before the job runs
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
SEALED = {('T1', 4), ('T1', 5), ('T4', 4), ('T4', 5), ('C2a', 5)}      # the terms' targets and the coherent row in R5


def frozen_numbers(name):
    """M8.15's frozen numbers, the instrument's out/freeze_numbers.json, for every case. M8.15.x read them from there
    for its controls and from FROZEN.json, which holds every one of them unchanged, for its targets; here a sealed case
    is held by guard_sealed before any of its numbers are read."""
    with open(os.path.join(INSTRUMENT, 'out', 'freeze_numbers.json')) as f:
        return json.load(f)


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


def run_ladder(name, slot, eps_max, pts=None, log=print, levels=(3, 2), types=False):
    """M8.15.x's run_branch up to its bisection, without its lineage and persistence phases: the continuation at levels 3 and 2 along
    ladder(0.25, eps_max) from the seed, a Point at each level at the points pts (every ladder point when None), and,
    with types (the coherent row alone; no point of T1 or T4 is classified), the frozen validity check, types and
    bisection. Returns the record, both levels' points, level 2's Branch records and its LevelCase."""
    fz = frozen_numbers(name)
    rf3, rf2 = float(fz['r_f']['3']), float(fz['r_f']['2'])
    tau0_3, tau0_2 = 10 * rf3, 10 * rf2
    dlev = float(fz['delta_lev'])
    s2 = float(fz['s2'][f'R{slot}'])
    eta, T = float(fz['eta']), float(fz['T'])
    emax = eps_max
    targets = ladder(0.25, emax)
    sel = set(targets) if pts is None else set(pts)
    sch = schedule(name, slot, rf3, targets) if (types and name in SPECTRA) else []
    out = dict(case=name, slot=slot, targets=targets, schedule=sch,
               frozen=dict(r_f3=rf3, r_f2=rf2, delta_lev=dlev, s2=s2, eta=eta, T=T),
               path3=[], path2=[], points=[], level2=[], cross=[], types=[], changes=[])
    RUN.update(frozen=out['frozen'])
    # level 3: the linear record
    t0 = time.time()
    stage('level 3 setup')
    lc3 = LevelCase(levels[0], name, slot)
    out['setup3'] = setup_record(lc3)
    P3, R3 = {}, {}
    def on3(k, eps_k, rec):
        out['path3'].append(dict(eps=eps_k, eps_reached=rec['eps'], m=rec['m'], newton_it=rec['it'], residual=rec['full']))
        if eps_k not in sel:
            return
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
    reached = [d['eps'] for d in out['path3']]
    if not reached:
        # a branch end with no ladder point (M8.15.x § 4): level 2 and the gates have nothing to read
        log(f'  no level-3 ladder point: the branch ended with {out["end"][0]}; level 2 skipped')
        return out, P3, {}, {}, None
    if types:
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
    # level 2: the cross-checks and the gates' level-2 points
    stage('level 2')
    lc2 = LevelCase(levels[1], name, slot)
    out['setup2'] = setup_record(lc2)
    P2, R2 = {}, {}
    def on2(k, eps_k, rec):
        out['path2'].append(dict(eps=eps_k, eps_reached=rec['eps'], m=rec['m'], newton_it=rec['it'], residual=rec['full']))
        if eps_k not in sel:
            return
        P2[eps_k], R2[eps_k] = Point(lc2, rec, eps_k, tau0_2, tau0_2, keep_cluster=True), rec
        out['level2'].append(P2[eps_k].record())
        p = P2[eps_k]
        log(f'  L2 eps {eps_k:.4g}: cluster {p.dim}/{FROZEN_DIM[name]} ok={p.cluster_ok}; S dim {p.S_dim}, gap {p.S_gap:.3g}; '
            f'peak resident {peak_gb():.1f} GB')
    br2 = lc2.branch(reached, on2)
    out['end2'] = [str(br2.end[0]), br2.end[1]]
    omega0 = np.sqrt(lc2.lam0)
    if not types:
        return out, P3, P2, R2, lc2

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
    return out, P3, P2, R2, lc2


# --- M8.19: what the jobs read and write ------------------------------------------------------------------------------
LONG_T = G.LONG_T
REF = {'T1_R4': 'reference/m8_17/run/out/T1_R4.json', 'T1_R5': 'reference/m8_17/run/out/T1_R5.json',
       'T4_R4': 'reference/m8_17/run/out/T4_R4.json', 'T4_R5': 'reference/m8_17/run/out/T4_R5.json',
       'C2a_R5': 'reference/m8_16_1/run/out/C2a_R5.json', 'C2a_R4': 'reference/m8_16_1/run/out/C2a.json'}
ROWS = {'gates_T1_R4': ('T1', 4, 'T1_R4'), 'gates_T1_R5': ('T1', 5, 'T1_R5'), 'gates_T4_R4': ('T4', 4, 'T4_R4'),
        'gates_T4_R5': ('T4', 5, 'T4_R5'), 'coherent_R5': ('C2a', 5, 'C2a_R5')}
LABELS = {'T1_R4_1': 'T1/R4, lower', 'T1_R4_2': 'T1/R4, upper', 'T1_R5_1': 'T1/R5', 'T4_R4_1': 'T4/R4',
          'T4_R5_1': 'T4/R5', 'C2a_R5_1': 'The coherent row in R5'}
Q_R5_COHERENT = 2289 / 2288      # Q5[6] of soft-slot-branches/branches_check.py, as QEXACT[('C2a', 4)] is its Q4[6]
DYN = {'dyn_C1': 'C1', 'dyn_C2a': 'C2a', 'dyn_C2b': 'C2b', 'dyn_C3': 'C3'}
WAVE1 = ['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'rate', 'p5a', 'c3e3', 'c2a_dur']
BENCH_TESTS = {('C2a', 4, 8.0, 1000.0)}     # the stand-in's test: M8.15.x's recorded C2a/R4 test at 8, T = 1000


class Refused(Exception):
    """A guard's refusal: written as refused.json, exit 3; never a crash and never a scientific end."""


def sha(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def jdump(name, obj):
    write_json_atomic(os.path.join(OUT, name), obj)


def setup_record(lc):
    """The case as set up at a level: the seed's Q against the exact one, the fixed space, the lowest level."""
    from m815_common import QEXACT
    q = QEXACT.get((lc.name, lc.slot))
    return dict(level=lc.level, Q=float(lc.Q), Q_exact=q, Q_rel=(float(lc.Q / q - 1) if q else None),
                lam0=float(lc.lam0), lam0_min=float(lc.lam0_min), spread=float(lc.spread),
                fixed_dim=int(lc.case.Br.shape[1]), H=len(lc.case.H), slices=len(lc.slices))


def inject_coherent_R5():
    """C2a's case in R5 (the coherent row): PinnedCase takes the slot; FROZEN_DIM and SPECTRA are C2a's, and predicted
    scales by 9/16 in R5 as for every row. The one constant added is the exact Q."""
    import m815_common
    key = ('C2a', 5)
    if key in m815_common.QEXACT and m815_common.QEXACT[key] != Q_R5_COHERENT:
        raise RuntimeError('QEXACT already holds another value for the coherent row in R5')
    m815_common.QEXACT[key] = Q_R5_COHERENT


# --- the guards ---------------------------------------------------------------------------------------------------
def runlog(root):
    with open(os.path.join(root, 'RUNLOG.json')) as f:
        return json.load(f)


def completed(root, job):
    """A completed job's folder, every file at the SHA-256 the orchestrator logged; refused otherwise."""
    rec = runlog(root)['completed'].get(job)
    if rec is None:
        raise Refused(f'{job} has not completed')
    d = os.path.join(root, job)
    for f, h in rec['files'].items():
        if sha(os.path.join(d, f)) != h:
            raise Refused(f'{job}/{f} differs from the SHA-256 the run logged')
    return d


def validate_frozen():
    """run/FROZEN.json: frozen, a go, the terms' SHA-256, every file under run/ and reference/ at its pin and none
    unpinned, the instrument's files at its manifest and the manifest at its pin, and M8.15's frozen numbers."""
    path = os.path.join(HERE, 'FROZEN.json')
    if not os.path.exists(path):
        raise Refused('no FROZEN.json')
    pin = os.path.join(HERE, 'FROZEN_PIN')
    if not os.path.exists(pin) or open(pin).read().strip() != sha(path):
        raise Refused('FROZEN.json is not at its pin, FROZEN_PIN')
    with open(path) as f:
        F = json.load(f)
    if not F.get('frozen') or not F.get('go'):
        raise Refused('FROZEN.json is not marked frozen with a go')
    for rel, h in F['pins'].items():
        if not os.path.exists(os.path.join(ROOT, rel)) or sha(os.path.join(ROOT, rel)) != h:
            raise Refused(f'{rel} differs from its pin')
    if sorted(F['pins']) != sorted(pinned_files()):
        raise Refused('the files under run/ and reference/ are not the pinned set')
    if sha(os.path.join(HERE, 'm8_19_task_details.md')) != F['terms_sha256']:
        raise Refused("the terms' SHA-256 differs")
    man = json.load(open(os.path.join(INSTRUMENT, 'out', 'MANIFEST.json')))
    bad = [f for f in sorted(os.listdir(INSTRUMENT)) if f.endswith('.py') and man['sha256'].get(f) != sha(os.path.join(INSTRUMENT, f))]
    if bad or sha(os.path.join(INSTRUMENT, 'out', 'MANIFEST.json')) != F['instrument_manifest_sha256']:
        raise Refused(f'the instrument differs from its manifest ({bad})')
    if frozen_numbers('C1') != F['freeze_numbers']:
        raise Refused("M8.15's frozen numbers differ from FROZEN.json's")
    return F


def pinned_files():
    """Every file the freeze pins, relative to this task's folder: run/ but out/ and the freeze's own files, and
    reference/."""
    out = []
    for top in ('run', 'reference'):
        for dp, dn, fn in os.walk(os.path.join(ROOT, top)):
            rel = os.path.relpath(dp, ROOT)
            dn[:] = sorted(d for d in dn if not (rel == 'run' and d == 'out') and d != '__pycache__')
            for f in sorted(fn):
                r = os.path.join(rel, f)
                if r not in ('run/FROZEN.json', 'run/FROZEN_PIN') and f != '.DS_Store':
                    out.append(r)
    return sorted(out)


def controls_passed(root):
    d = completed(root, 'controls')
    with open(os.path.join(d, 'CONTROLS.json')) as f:
        c = json.load(f)
    if not c['all_passed']:
        raise Refused('gate 1 did not pass')
    return c


def guard_long(root, plan, T):
    """A test longer than 2750 runs only after C2a/R4 at 1 has Persisted, valid, at the longest T the gates set."""
    if T <= LONG_T:
        return
    c = json.load(open(os.path.join(completed(root, 'c2a_long'), 'c2a.json')))
    if not (c['control']['passed'] and c['T'] == plan['T_max'] and T <= plan['T_max']):
        raise Refused('a test longer than 2750 waits for the longest control to Persist, valid')


def guard_sealed(name, slot, root, bench):
    if (name, slot) not in SEALED:
        return None
    if bench:
        raise Refused(f'{name}/R{slot} is sealed: no bench run touches it')
    F = validate_frozen()
    controls_passed(root)
    RUN.update(go=F['go'], terms_sha256=F['terms_sha256'])
    return F


# --- gate 5 and the reading of a point -------------------------------------------------------------------------------
def excitation(lc2, p2, lam, eta):
    """Gate 5 at level 2: the perturbation drawn exactly as persistence.direction draws it, its slow half
    v_s = (P_S - P_G) v, and B the real span of the identified mode's eigenvectors and their Hamiltonian partners;
    returns ||P_B v_s||^2 / ||v_s||^2 in the energy norm direction() scales in, with what it read."""
    from persistence import SEED, omega_projector, energy_norm, direction
    from nonlinear import to_real
    v, ps, Mr = p2.v, p2.v.ps, lc2.st.Mr
    n = len(p2.Phi)
    rng = np.random.default_rng(SEED)
    re = rng.standard_normal(n)
    im = rng.standard_normal(n)
    vec = np.concatenate([to_real(re + 1j * im), np.zeros(2 * n)])
    PG = omega_projector(ps, v.G)
    PS = omega_projector(ps, p2.S)
    pv = PS(vec)
    fast = vec - pv
    slow = pv - PG(vec)
    tol = 1e-6 * abs(lam) + 1e-7                    # the frozen closure tolerance
    gm = v.cls == 'genuine'
    gvals, gvecs = v.vals[gm], v.vecs[:, gm]
    sel = [i for i, l in enumerate(gvals) if min(abs(l - t) for t in (lam, -lam, np.conj(lam), -np.conj(lam))) <= tol]
    Bc = np.column_stack([np.real(gvecs[:, sel]), np.imag(gvecs[:, sel])])
    Cb = ps.inner(Bc, Bc)
    Cb = (Cb + Cb.T) / 2
    ev, U = np.linalg.eigh(Cb)
    keep = ev > 1e-12 * ev.max()
    B = Bc @ (U[:, keep] / np.sqrt(ev[keep]))
    pb = omega_projector(ps, B)(slow)
    share = float((energy_norm(pb, Mr, 2 * n) / energy_norm(slow, Mr, 2 * n)) ** 2)
    # the job's v_s is the test's: direction() must return exactly the scaled halves
    nP = np.sqrt(to_real(p2.Phi) @ (Mr @ to_real(p2.Phi)))
    a = (eta / np.sqrt(2)) * nP
    same = bool(p2.S.shape[1] > v.G.shape[1] and np.array_equal(
        direction(n, eta, p2.Phi, ps, v.G, Mr, S=p2.S, mode='split'),
        slow * (a / energy_norm(slow, Mr, 2 * n)) + fast * (a / energy_norm(fast, Mr, 2 * n))))
    if not same:
        raise RuntimeError("gate 5's slow half is not the one direction() applies")
    return share, dict(B_dim=int(B.shape[1]), eigenvectors=len(sel), direction_reproduced=same)


def level_data(p, tau_re):
    return dict(cluster_ok=bool(p.cluster_ok), tau_re=float(tau_re), genuine=[[cj(l), float(k)] for l, k in p.genuine])


def read_points(name, slot, P3, P2, lc2, pts, refs, read=G.GATES):
    """Gates 2 to 7 (or those read) at each point, from the frozen points; gate 7 also by persistence.margin_ok."""
    from persistence import margin_ok
    fz = frozen_numbers(name)
    tau0_3, tau0_2, eta = 10 * float(fz['r_f']['3']), 10 * float(fz['r_f']['2']), float(fz['eta'])
    log_bound = float(np.log(1 / (10 * eta)))
    res = []
    for e in pts:
        p3, p2 = P3.get(e), P2.get(e)
        r = refs.get(e)
        ref = dict(source='harmonic', lam=r['lam'], sign=r['sign'], count=r['count']) if (r and r['lam']) else dict(source='level3')
        pt = dict(eps=e, reached3=p3 is not None, reached2=p2 is not None, read=list(read), ref=ref,
                  L3=level_data(p3, tau0_3) if p3 is not None else None,
                  L2=level_data(p2, tau0_2) if p2 is not None else None, share=None, r=None, log_bound=log_bound)
        extra = {}
        if p2 is not None:
            lv = p2.lifted
            pt['r'] = float(np.max(lv.real)) if len(lv) else 0.0
        if p3 is not None and p2 is not None:
            _, _, m2, _ = G.mode_at(pt, classify)
            if m2 is not None:
                pt['share'], extra = excitation(lc2, p2, G.C(m2['lam']), eta)
        ev = G.evaluate(pt, classify)
        if ev['T'] is not None and '7' in ev['gates']:
            okm, rm = margin_ok(p2.lifted, ev['T'], eta)
            if bool(okm) != ev['gates']['7']['passed'] or float(rm) != pt['r']:
                raise RuntimeError('gate 7 disagrees with persistence.margin_ok')
        res.append(dict(ev, input=pt, excitation=extra))
    return res


def store_states(path, P2, R2, pts):
    """The level-2 standing wave (the continuation's accepted record) and spectrum at each point, exactly."""
    arrays, index = {}, []
    for i, e in enumerate(e for e in pts if e in R2):
        rec, p = R2[e], P2[e]
        arrays[f'x_{i}'] = rec['x']
        arrays[f'vals_{i}'] = p.v.vals
        arrays[f'cls_{i}'] = np.array([str(c) for c in p.v.cls])
        index.append(dict(i=i, eps=e, m=float(rec['m']), eps_reached=float(rec['eps']), sigma=float(rec['sigma']),
                          it=int(rec['it']), full=float(rec['full']), nu=[float(x) for x in rec['nu']],
                          mu=[float(x) for x in rec['mu']]))
    np.savez(path, **arrays)
    return index


def stretch_tests(row, strs, evs):
    """Each stretch's search: its points' gates, the test point and its T, or untested with every point's cause."""
    by = {d['eps']: d for d in evs}
    out = {}
    for i, s in enumerate(strs, 1):
        sid = f'{row}_{i}'
        pe = [by[e] for e in s]
        top = G.search(pe)
        out[sid] = dict(label=LABELS.get(sid, sid), points=s, test=(dict(eps=top['eps'], T=top['T'],
                        P=top['gates']['6']['P']) if top else None),
                        causes={str(d['eps']): (None if d['passed'] else d['first_failed']) for d in pe})
    return out


# --- the jobs -------------------------------------------------------------------------------------------------------
def job_dyn(name, a):
    """M8.15's dynamics control, its own code: m815_controls.dynamics with its output folder moved to the job's."""
    import m815_controls as MC
    MC.OUT = OUT
    T = 1000.0 if a.T is None else a.T
    stage('dynamics')
    if name == 'rate':
        MC.dynamics('C3', eta=1e-7, T=T, tag='C3_rate')
    else:
        MC.dynamics(name, T=T)


def job_p5a(a):
    """Control 1a's M8.15.x arm (qualification/control_1a.py, arm 'bench'): P5a in R4 at level 2, the seed solve that
    Branch.first makes at eps_min = 0.25, its stopping test read by a trace; the solve itself is untouched."""
    import inspect
    from math import sqrt
    import pinned
    from continuation import Branch
    from nonlinear import to_real
    sp = dict(slot=4, j2=6, u={3: sqrt(12 / 25), -2: sqrt(13 / 25) * np.exp(5j * np.pi / 10)}, gens=[('z', 5)],
              slice_axis='z')
    b = pinned.CASES['P5a']
    assert {k: v for k, v in b.items() if k != 'u'} == {k: v for k, v in sp.items() if k != 'u'}
    assert b['u'].keys() == sp['u'].keys() and all(b['u'][m] == sp['u'][m] for m in sp['u'])
    stage('p5a setup')
    t0 = time.time()
    lc = LevelCase(2, 'P5a', 4)
    t_setup = time.time() - t0
    case, st = lc.case, lc.st
    s = lc.slices[0]
    S0 = st.Mr @ s
    Br = case.Br
    seed = case.P @ to_real(case.seed)
    p_seed = to_real(1j * to_complex(seed))
    diag = dict(orientation=case.orientation_report(), lam0=float(lc.lam0), Q=float(lc.Q), vol=float(lc.vol),
                slice_outside_fixed=float(np.linalg.norm(case.P @ s - s) / np.linalg.norm(s)),
                Mslice_outside_fixed=float(np.linalg.norm(S0 - Br @ (Br.T @ S0)) / np.linalg.norm(S0)),
                slice_phase_cosine=float((s @ (st.Mr @ p_seed)) / np.sqrt((s @ S0) * (p_seed @ (st.Mr @ p_seed)))),
                setup_seconds=round(t_setup, 1))
    code = pinned.solve_pinned.__code__
    lines, start = inspect.getsourcelines(pinned.solve_pinned)
    hits = [start + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
    assert len(hits) == 1
    LINE = hits[0]
    its = []

    def local(frame, event, arg):
        if event == 'line' and frame.f_lineno == LINE:
            L = frame.f_locals
            x, F, Mx, mu, nu, T, S = L['x'], L['F'], L['Mx'], L['mu'], L['nu'], L['T'], L['S']
            assert len(T) == 1 and len(S) == 1
            nMx = np.linalg.norm(Mx)
            p = to_real(1j * to_complex(x))
            its.append(dict(
                it=int(L['it']), res=float(L['res']), full=float(L['full']), sigma=float(L['sigma']),
                mu=float(mu[0]), nu=float(nu[0]),
                new_form=float(np.linalg.norm(F) / nMx),
                old_form=float(np.linalg.norm(F - mu[0] * T[0]) / nMx),
                projected=float(np.linalg.norm(L['Br'].T @ F) / nMx),
                norm_constraint=float(abs(L['c'][0]) / L['m']), gauge_constraint=float(L['c'][1]),
                slice_constraint=float(L['c'][2]),
                mu_pred=float(-nu[0] * (p @ S[0]) / (p @ T[0])),
                plateau_pred=float(abs(mu[0]) * np.linalg.norm(T[0]) / nMx)))
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    stage('p5a solve')
    br = Branch(st, case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
    t1 = time.time()
    sys.settrace(glob)
    try:
        ok = br.first(0.25)
    finally:
        sys.settrace(None)
    out = dict(arm='bench', ok=bool(ok), end=br.end, iterations=its, diagnostics=diag,
               solve_seconds=round(time.time() - t1, 1))
    if ok:
        r = br.accepted[0]
        out['accepted'] = dict(it=r['it'], full=float(r['full']), sigma=float(r['sigma']), eps=float(r['eps']),
                               m=float(r['m']), nu=[float(v) for v in r['nu']],
                               mu=[float(v) for v in r.get('mu', [])])
    out = json.loads(json.dumps(out, default=str))
    out['control'] = dict(passed=bool(out['ok'] and its and its[-1]['res'] < 1e-11),
                          rule='the seed solve stops under the repaired test below 1e-11')
    jdump('control_1a_arm.json', out)


def pre_evolution(st, Phi, sigma, ps, Gc, case, lifted_vals, eta, T, S, mode='split', dt_factor=0.8):
    """run_test up to its first step (persistence.py, lines 94 to 113): the margin, the step, the perturbation and its
    energy E_eta. Nothing evolves; the bench reads a fresh control's gates with it."""
    from persistence import margin_ok, direction, energy_norm
    from integrate import Verlet, omega_max
    from nonlinear import to_real
    Mr = st.Mr
    n = len(Phi)
    ok, r = margin_ok(lifted_vals, T, eta)
    V = Verlet(st)
    dt = dt_factor * 2 / omega_max(st)
    theta = 2 * np.arcsin(dt * np.sqrt(sigma) / 2)
    c0 = (np.exp(1j * theta) - 1 + 0.5 * dt ** 2 * sigma) / dt
    v = direction(n, eta, Phi, ps, Gc, Mr, S=S, mode=mode)
    delta, p = to_complex(v[:2 * n]), to_complex(v[2 * n:])
    X0 = (Phi + delta, c0 * (Phi + delta) + p)
    Y0 = (Phi.copy(), c0 * Phi)
    E0, Eref = V.energy(*X0), V.energy(*Y0)
    nP = np.sqrt(to_real(Phi) @ (Mr @ to_real(Phi)))
    return dict(margin_ok=bool(ok), r=float(r), dt=float(dt), E_eta=float(E0 - Eref), energy_pert=float((E0 - Eref) / E0),
                initial_energy_norm=float(energy_norm(v, Mr, 2 * n) / nP), T=float(T))


def job_c3e3(a):
    """C3 at eps = 3, which must Fail (the terms: THE CONTROLS): m815_controls.dynamics with the amplitude the terms
    name, the same seed, T = 1000. With --no-evolve (the bench) it stops before the first step."""
    import m815_controls as MC
    eps, name, eta, T = 3.0, 'C3', 1e-3, 1000.0
    stage('c3e3 ladder')
    lc = LevelCase(2, name)
    hold = {}
    lc.branch(ladder(0.25, eps), lambda k, e, r: hold.__setitem__('rec', r) if abs(e - eps) < 1e-9 else None)
    if 'rec' not in hold:
        jdump('dynamics_C3_eps3.json', dict(eps=eps, verdict='Not reached', control=dict(passed=False)))
        return
    rec = hold['rec']
    Phi, sigma = to_complex(rec['x']), rec['sigma']
    stage('c3e3 verdict')
    lin = Linearization(lc.st, Phi, sigma)
    v = Verdict(lc.st, lc.case, lin, Phi, sigma, lc.lam0_min, lc.rot, FROZEN_DIM[name], rigid=lc.rigid,
                tau_re=MC.tau_re(2))
    lifted = v.vals[(v.cls == 'lifted') | (v.cls == 'rigid')]
    cluster = dict(dim=int(v.dim), frozen_dim=int(v.frozen_dim), closed=bool(v.closed), omega_gram=float(v.omega_gram),
                   ok=bool(v.dim == v.frozen_dim and v.closed and v.omega_gram >= 1e-6))
    base = dict(eps=eps, eps_reached=float(rec['eps']), residual=float(rec['full']), cluster=cluster,
                level2_rates=[cj(l) for l, _ in v.genuine])
    if a.no_evolve:
        jdump('dynamics_C3_eps3_gates.json', dict(base, pre_evolution=pre_evolution(
            lc.st, Phi, sigma, v.ps, v.G, lc.case, lifted, eta, T, v.slow_basis())))
        return
    stage('c3e3 evolution')
    t0 = time.time()
    res = run_test(lc.st, Phi, sigma, v.ps, v.G, lc.rot, lc.case, lifted, eta=eta, T=T, log=lambda s: print(s, flush=True),
                   progress=100, S=v.slow_basis(), mode='split')
    recarr = res.pop('rec', None)
    res['seconds'] = time.time() - t0
    res.update(base)
    res['control'] = dict(passed=res['verdict'] == 'Fails', rule='must Fail')
    jdump('dynamics_C3_eps3.json', res)
    if recarr is not None:
        np.save(os.path.join(OUT, 'dynamics_C3_eps3.npy'), recarr)


def job_c2a(a, long_T=None):
    """C2a/R4 at 1, read through gates 3, 5, 6 and 7 as a target is (the terms: THE CONTROLS), with gate 2's solution at
    both levels; then the test at gate 6's T (c2a_dur, which must give 2750) or at the longest T (c2a_long)."""
    name, slot, eps = 'C2a', 4, 1.0
    refs = G.references(G.load_readings(os.path.join(ROOT, REF['C2a_R4'])), ladder(0.25, EPS_MAX[slot]))
    out, P3, P2, R2, lc2 = run_ladder(name, slot, eps, pts=[eps])
    ev = read_points(name, slot, P3, P2, lc2, [eps], refs, read=(2, 3, 5, 6, 7))[0]
    T = ev['T'] if long_T is None else long_T
    rec = dict(ladder=out, gates=ev, T=T, T_gate6=ev['T'])
    if long_T is not None and ev['passed']:
        from persistence import margin_ok
        okm, _ = margin_ok(P2[eps].lifted, long_T, float(frozen_numbers(name)['eta']))
        rec['margin_at_T'] = bool(okm)
    stage('c2a test')
    if a.no_evolve or not ev['passed'] or (long_T is not None and not rec.get('margin_at_T')):
        rec['test'] = None
    else:
        if a.T is not None:
            T = a.T
        p2 = P2[eps]
        t0 = time.time()
        res = run_test(lc2.st, p2.Phi, p2.sigma, p2.v.ps, p2.v.G, lc2.rot, lc2.case, p2.lifted, eta=1e-3, T=T,
                       log=lambda s: print(s, flush=True), progress=100, S=p2.S, mode='split')
        arr = res.pop('rec', None)
        res['seconds'] = time.time() - t0
        rec['test'] = dict(res, T=T)
        if arr is not None:
            np.save(os.path.join(OUT, 'test.npy'), arr)
    want = (ev['passed'] and rec['test'] is not None and rec['test']['verdict'] == 'Persists' and rec['test']['valid']
            and (long_T is not None or ev['T'] == LONG_T))
    rec['control'] = dict(passed=bool(want), rule=('Persists, valid, at T = 2750 by gate 6' if long_T is None
                                                   else f'Persists, valid, at the longest T, {long_T}'))
    jdump('c2a.json', rec)


def job_controls(a):
    """Gate 1 (the terms: THE CONTROLS) on the wave-1 records: M8.15's dynamics gate re-read as m815_controls.summarize
    reads it, control 1a's rule, C3 at 3 Failing, and C2a/R4's duration control Persisting, valid, at T = 2750."""
    from persistence import evaluate
    L = runlog(a.root)
    res = {}

    def folder(job):
        if job not in L['completed']:
            return None
        return completed(a.root, job)

    want = {'dyn_C1': 'Persists', 'dyn_C2a': 'Persists', 'dyn_C2b': 'Persists', 'dyn_C3': 'Fails'}
    for job, verdict_wanted in want.items():
        d = folder(job)
        if d is None:
            res[job] = dict(passed=False, why='not completed')
            continue
        nm = DYN[job]
        rec = np.load(os.path.join(d, f'dynamics_{nm}.npy'))
        dj = json.load(open(os.path.join(d, f'dynamics_{nm}.json')))
        Eref = rec[0, 6] * (1 - dj['energy_pert'])
        ev = evaluate(rec, 1e-3, Eref)
        res[job] = dict(passed=bool(ev['verdict'] == verdict_wanted and ev['valid']), verdict=ev['verdict'],
                        wanted=verdict_wanted, max_dperp=ev['max_dperp'], t_fail=ev['t_fail'])
    d = folder('rate')
    if d is None:
        res['rate'] = dict(passed=False, why='not completed')
    else:
        rr = json.load(open(os.path.join(d, 'dynamics_C3_rate.json')))
        rec = np.load(os.path.join(d, 'dynamics_C3_rate.npy'))
        t, dp = rec[:, 0], rec[:, 2]
        eta7 = 1e-7
        sel = (dp >= 10 * eta7) & (dp <= 1e4 * eta7)
        rate = np.polyfit(t[sel], np.log(dp[sel]), 1)[0]
        lin2 = max(abs(complex(z[0], z[1])) for z in rr['level2_rates'])
        res['rate'] = dict(passed=bool(abs(rate / lin2 - 1) <= 0.05), fitted=float(rate), linear_L2=float(lin2),
                           points=int(sel.sum()))
    for job, fname in (('p5a', 'control_1a_arm.json'), ('c3e3', 'dynamics_C3_eps3.json'), ('c2a_dur', 'c2a.json')):
        d = folder(job)
        if d is None:
            res[job] = dict(passed=False, why='not completed')
            continue
        if not os.path.exists(os.path.join(d, fname)):
            res[job] = dict(passed=False, why=f'no {fname}: the job did not evolve')
            continue
        c = json.load(open(os.path.join(d, fname)))
        res[job] = dict(c['control'], **({'verdict': c.get('verdict')} if job == 'c3e3' else {}))
    out = dict(controls=res, all_passed=all(r['passed'] for r in res.values()) and len(res) == len(WAVE1))
    jdump('CONTROLS.json', out)


def job_gates(row, a):
    """A row's gates (wave 2): the continuation at levels 3 and 2 to its highest classified point, gates 2 to 7 at each
    classified point, each stretch's search; the level-2 standing wave and spectrum stored at each point."""
    name, slot, ref = ROWS[row] if row in ROWS else ('C2a', 4, 'C2a_R4')
    L = ladder(0.25, EPS_MAX[slot])
    refs = G.references(G.load_readings(os.path.join(ROOT, REF[ref])), L)
    strs = G.stretches(refs)
    if a.standin:
        # the bench's stand-in (DESIGN.md, the dry run): the coherent row's own job on C2a/R4, with its ladder to 8 and
        # M8.16.1's C2a readings at 0.25, 0.5, 1 and 2 as its record
        return job_coherent(a, refs, strs, L, slot=4, eps_max=8.0, row='C2a_R4_standin')
    if row == 'coherent_R5':
        return job_coherent(a, refs, strs, L)
    pts = sorted(set(e for s in strs for e in s))
    out, P3, P2, R2, lc2 = run_ladder(name, slot, max(pts), pts=pts)
    stage('gates')
    evs = read_points(name, slot, P3, P2, lc2, pts, refs)
    index = store_states(os.path.join(OUT, 'states_L2.npz'), P2, R2, pts)
    rid = f'{name}_R{slot}' + ('_standin' if a.standin else '')
    jdump('gates.json', dict(row=rid, case=name, slot=slot, ladder=out, points=evs, stretches=stretch_tests(rid, strs, evs),
                             states=index))


def job_coherent(a, refs, strs, L, slot=5, eps_max=32.0, row='C2a_R5'):
    """The coherent row in R5 (the terms: THE COHERENT ROW IN R5): C2a's case in R5 along ladder(0.25, 32), M8.15's
    frozen types at level 3 cross-checked at level 2; the ladder's outcome; then the gates on its stretch. The bench's
    stand-in runs it on C2a/R4 to 8."""
    record_pts = strs[0]
    out, P3, P2, R2, lc2 = run_ladder('C2a', slot, eps_max, pts=None, types=True)
    types = {d['eps']: d['type'] for d in out['types']}
    why = []
    if not out.get('validity_eps_min', {}).get('ok', False):
        why.append('the validity check at 0.25')
    why += [f'the type at {e:g} is {types.get(e)}, M8.16.1 Elliptic' for e in record_pts if types.get(e) != 'Elliptic']
    established = not why
    reached = [d['eps'] for d in out['path3']]
    stretch, source = G.coherent_stretch(types, reached, record_pts, established)
    stage('gates')
    evs = read_points('C2a', slot, P3, P2, lc2, stretch, refs)
    index = store_states(os.path.join(OUT, 'states_L2.npz'), P2, R2, stretch)
    outcome = dict(established=established, why=why, types=out['types'], changes=out['changes'], end=out['end'],
                   end2=out.get('end2'), validity_eps_min=out.get('validity_eps_min'), stretch=stretch, stretch_from=source,
                   other_elliptic_runs=G.other_elliptic_runs(types, reached, stretch, established))
    jdump('gates.json', dict(row=row, case='C2a', slot=slot, ladder=out, ladder_outcome=outcome, points=evs,
                             stretches=stretch_tests(row, [stretch], evs), states=index))


def job_plan(a):
    """Each stretch's test point and T from the gates' records, and the longest T (the terms: THE FREEZE, THE GUARD AND
    THE RUN, waves 3 and 4)."""
    L = runlog(a.root)
    tests, untested, missing = {}, {}, []
    for job in (['gates_C2a_R4'] if a.standin else list(ROWS)):
        if job not in L['completed']:
            missing.append(job)
            continue
        g = json.load(open(os.path.join(completed(a.root, job), 'gates.json')))
        for sid, s in g['stretches'].items():
            if s['test']:
                tests[sid] = dict(job=job, case=g['case'], slot=g['slot'], **s['test'])
            else:
                untested[sid] = s['causes']
    T_max = max((t['T'] for t in tests.values()), default=None)
    jdump('PLAN.json', dict(tests=tests, untested=untested, gates_not_completed=missing, T_max=T_max,
                            long_control=(T_max is not None and T_max > LONG_T)))


def job_test(sid, a):
    """One stretch's test (wave 4): the stored level-2 state reloaded, its Point rebuilt and checked equal to the
    stored one, gates 3 (level 2), 5, 6 and 7 read again and equal, then the frozen run_test at gate 6's T."""
    plan = json.load(open(os.path.join(completed(a.root, 'plan'), 'PLAN.json')))
    t = plan['tests'][sid]
    name, slot, eps, T = t['case'], t['slot'], t['eps'], t['T']
    guard_sealed(name, slot, a.root, a.bench)
    if a.bench and (name, slot, eps, T) not in BENCH_TESTS:
        raise Refused(f'the bench evolves recorded states only: {name}/R{slot} at {eps} with T = {T} is not one')
    if not a.bench:
        guard_long(a.root, plan, T)
    gdir = completed(a.root, t['job'])
    g = json.load(open(os.path.join(gdir, 'gates.json')))
    st = np.load(os.path.join(gdir, 'states_L2.npz'))
    ix = next(d for d in g['states'] if d['eps'] == eps)
    stored = next(d for d in g['ladder']['level2'] if d['eps'] == eps)
    gpt = next(d for d in g['points'] if d['eps'] == eps)
    if name == 'C2a' and slot == 5:
        inject_coherent_R5()
    fz = frozen_numbers(name)
    tau0_2, eta = 10 * float(fz['r_f']['2']), float(fz['eta'])
    stage('test setup')
    lc2 = LevelCase(2, name, slot)
    rec = dict(m=ix['m'], eps=ix['eps_reached'], sigma=ix['sigma'], x=st[f'x_{ix["i"]}'], it=ix['it'], full=ix['full'],
               nu=np.array(ix['nu']), mu=np.array(ix['mu']))
    p2 = Point(lc2, rec, eps, tau0_2, tau0_2, keep_cluster=True)
    same = (json.loads(json.dumps(p2.record(), default=str)) == stored and np.array_equal(p2.v.vals, st[f'vals_{ix["i"]}'])
            and [str(c) for c in p2.v.cls] == [str(c) for c in st[f'cls_{ix["i"]}']])
    if not same:
        raise RuntimeError('the rebuilt level-2 point differs from the stored one')
    pt = dict(gpt['input'], L2=level_data(p2, tau0_2), r=(float(np.max(p2.lifted.real)) if len(p2.lifted) else 0.0))
    _, _, m2, _ = G.mode_at(pt, classify)
    pt['share'], extra = excitation(lc2, p2, G.C(m2['lam']), eta)
    ev = G.evaluate(pt, classify)
    if json.loads(json.dumps(ev)) != {k: gpt[k] for k in ev} or ev['T'] != T:
        raise RuntimeError("the gates read again differ from the gates' record")
    stage('test evolution')
    t0 = time.time()
    res = run_test(lc2.st, p2.Phi, p2.sigma, p2.v.ps, p2.v.G, lc2.rot, lc2.case, p2.lifted, eta=eta, T=T,
                   log=lambda s: print(s, flush=True), progress=100, S=p2.S, mode='split')
    arr = res.pop('rec', None)
    res['seconds'] = time.time() - t0
    jdump('test.json', dict(res, stretch=sid, case=name, slot=slot, eps=eps, T=T, P=t['P'], periods=T / t['P']))
    if arr is not None:
        np.save(os.path.join(OUT, 'test.npy'), arr)


def job_record(a):
    """The record (wave 5, the terms: THE OUTCOMES): per stretch, with no aggregate, the frozen evaluator's verdict at its
    test point with T, the periods spanned, max d_perp, max d_rot and the reference floor; or untested with each point's
    cause; or, where a job ended its part of the run or gate 1 failed, that cause, for the maintainer's adjudication.
    The coherent row's ladder is recorded apart, or, if its job did not complete, that job's cause, for adjudication;
    and any other Elliptic run its established ladder reads is named apart from the terms' stretches, as a newly
    identified Elliptic stretch with no test fixed (DESIGN.md, reading 3). Read from the completed jobs' folders and the
    log alone."""
    L = runlog(a.root)
    rec = dict(controls=None, stretches={}, coherent_ladder=None, newly_identified={}, ended=L['ended'],
               not_run=L['not_run'])
    if 'controls' in L['completed']:
        rec['controls'] = json.load(open(os.path.join(completed(a.root, 'controls'), 'CONTROLS.json')))
    for job in ROWS:
        name, slot, ref = ROWS[job]
        if job not in L['completed']:
            why = L['ended'].get(job, {}).get('cause') or L['not_run'].get(job, {}).get('why') or 'not run'
            for sid, lab in LABELS.items():
                if sid.startswith(ref + '_'):
                    rec['stretches'][sid] = dict(label=lab, outcome='for adjudication', why=f'{job}: {why}')
            if job == 'coherent_R5':
                rec['coherent_ladder'] = dict(outcome='for adjudication', why=f'{job}: {why}')
            continue
        g = json.load(open(os.path.join(completed(a.root, job), 'gates.json')))
        if job == 'coherent_R5':
            rec['coherent_ladder'] = g['ladder_outcome']
            for k, run in enumerate(g['ladder_outcome']['other_elliptic_runs'], 1):
                at = f'at {run[0]:g}' if len(run) == 1 else f'from {run[0]:g} to {run[-1]:g}'
                rec['newly_identified'][f'{ref}_new_{k}'] = dict(
                    label=f'The coherent row in R5, Elliptic {at}', points=run, outcome='no test fixed',
                    why=('a newly identified Elliptic stretch, apart from the one its ladder establishes: these terms fix no '
                         'test for it, so S5 stays open for it, for the maintainer'))
        for sid, s in g['stretches'].items():
            entry = dict(label=s['label'], points=s['points'], causes=s['causes'])
            if not s['test']:
                entry.update(outcome='Untested', why='no point passes gates 2 to 7')
            else:
                tj = f'test_{sid}'
                entry.update(test_point=s['test'])
                if tj in L['completed']:
                    t = json.load(open(os.path.join(completed(a.root, tj), 'test.json')))
                    v = t['verdict']
                    entry.update(verdict=v, T=t['T'], periods=t['periods'], max_dperp=t.get('max_dperp'),
                                 max_drot=t.get('max_drot'), max_dref=t.get('max_dref'), valid=t.get('valid'),
                                 outcome=('tested' if v in ('Persists', 'Fails') else
                                          'tested, Unresolved (the terms ask the maintainer to confirm the reading)'
                                          if v == 'Unresolved' else
                                          "Invalid: S5's untested ending on the terms' reading, for the maintainer to confirm"
                                          if v.startswith('Invalid') else v))
                else:
                    why = L['ended'].get(tj, {}).get('cause') or L['not_run'].get(tj, {}).get('why') or 'not run'
                    entry.update(outcome='for adjudication', why=f'{tj}: {why}')
            rec['stretches'][sid] = entry
    jdump('RECORD.json', rec)


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument('job')
    ap.add_argument('--out', required=True, help="the job's staging folder")
    ap.add_argument('--root', required=True, help="the run's out/ folder, with RUNLOG.json and the completed jobs")
    ap.add_argument('--T', type=float, default=None, help='bench only: a shorter T, controls only')
    ap.add_argument('--long-T', type=float, default=None, help="c2a_long's T, from the plan")
    ap.add_argument('--no-evolve', action='store_true', help='bench only: stop before the first step')
    ap.add_argument('--standin', action='store_true', help="bench only: the stand-in's test stretch")
    ap.add_argument('--bench', action='store_true', help='a bench run: sealed jobs refuse')
    ap.add_argument('--test-raise-at', default=None, help='armed control only: raise at this stage')
    a = ap.parse_args()
    OUT = a.out
    os.makedirs(OUT, exist_ok=True)
    try:
        if (a.T is not None or a.no_evolve or a.standin or a.test_raise_at) and not a.bench:
            raise Refused('bench options need --bench')
        job = a.job
        sealed_job = job in ('gates_T1_R4', 'gates_T1_R5', 'gates_T4_R4', 'gates_T4_R5', 'coherent_R5') or job.startswith('test_')
        if a.test_raise_at:
            if sealed_job:
                raise Refused('test hooks are for controls only')
            TEST.update(raise_at=a.test_raise_at)
        stage('start')
        if job in DYN or job == 'rate':
            job_dyn(DYN.get(job, 'rate'), a)
        elif job == 'p5a':
            job_p5a(a)
        elif job == 'c3e3':
            job_c3e3(a)
        elif job == 'c2a_dur':
            job_c2a(a)
        elif job == 'c2a_long':
            job_c2a(a, long_T=a.long_T)
        elif job == 'controls':
            job_controls(a)
        elif job in ROWS or (a.standin and job == 'gates_C2a_R4'):
            if job in ROWS:
                name, slot, _ = ROWS[job]
                guard_sealed(name, slot, a.root, a.bench)
                if job == 'coherent_R5':
                    inject_coherent_R5()
            job_gates(job, a)
        elif job == 'plan':
            job_plan(a)
        elif job.startswith('test_'):
            job_test(job[len('test_'):], a)
        elif job == 'record':
            job_record(a)
        else:
            raise Refused(f'no job {job}')
    except Refused as e:
        write_json_atomic(os.path.join(OUT, 'refused.json'), dict(job=a.job, refused=str(e)))
        print(f'REFUSED: {e}', flush=True)
        sys.exit(3)
    except Exception as e:
        # an instrument exception, never a scientific end (M8.15.x § 4): a crash record, nonzero exit
        import traceback, datetime
        frames = [dict(file=(os.path.relpath(fr.filename, INSTRUMENT) if os.path.abspath(fr.filename).startswith(INSTRUMENT)
                             else os.path.basename(fr.filename)), line=fr.lineno, function=fr.name, code=fr.line)
                  for fr in traceback.extract_tb(e.__traceback__)]
        crash = dict(job=a.job, crash=True, stage=STAGE['stage'], exception=type(e).__name__, message=str(e),
                     traceback=frames, frozen=RUN.get('frozen'),
                     written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
        write_json_atomic(os.path.join(OUT, 'crash.json'), crash)
        print(f'INSTRUMENT EXCEPTION at stage {STAGE["stage"]}: {type(e).__name__}: {e}; crash record written', flush=True)
        sys.exit(1)
    jdump('job.json', dict(job=a.job, peak_gb=peak_gb(), bench=a.bench))


if __name__ == '__main__':
    main()
