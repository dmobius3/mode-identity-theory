"""The registered controls of DESIGN.md section 8: the dry run that measures the floors, then controls 1 to 11 in
order under the design's stopping rules, and the rule of section 4. New code: every result here rests on it and on
fftcubic.py, timearm.py and fecheck.py, and every output carries their SHA-256 and the environment.

  python3 -I -B -u controls.py          the registered run, written once into record/: refused unless this folder's
                                        code is committed and unchanged and record/ is absent
  python3 -I -B -u controls.py --dev    a development run (DEVLOG.md), into dev/runs/<UTC time>/, on development
                                        seeds, N <= 12 and shorter durations: not a control, and not in the record
  python3 -I -B controls.py cost SLOT N KIND CUBIC STEPS SEED    one measurement of control 10, in its own process

Every choice the design leaves to committed code is fixed in REG before anything runs: seeds, sizes, durations,
amplitudes, schedules and normalizations. The pass lines are the design's. READINGS lists the readings of the design
that the code makes, for review; each output carries them."""
import os
import sys

for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
           'NUMEXPR_NUM_THREADS'):
    os.environ[_k] = '1'                      # one BLAS thread, set before numpy loads, as M8.15's scripts do
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import copy  # noqa: E402
import datetime  # noqa: E402
import gc  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402
import resource  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy  # noqa: E402

import fftcubic  # noqa: E402  (checks the instrument's pin first)
import timearm as ta  # noqa: E402
from instrument import basis, functional as fn, group2i, su2  # noqa: E402

REG = dict(
    seed=20261120,                 # every draw: numpy default_rng([seed, control, slot, N, draw])
    slots=('R1', 'R2', 'R3', 'R4'), rigid=('R1', 'R3'), kinds=('verlet', 'strang'),
    # the design's lines (section 8) and margin (section 5)
    cubic_tol=1e-11, ceiling=1e-10, charge_tol=1e-10, ratio=(3.5, 4.5), hw_read=0.5, drift=1e-2, quarter=0.25,
    margin=0.8, floor=10.0,
    # sizes (section 6): controls at N = 8 to 16, the FFT check to 32, the cost at 16, 24 and 32
    N1=(8, 12, 16, 24, 32), NA=(12, 16), NB=12, N10=(16, 24, 32), cost_slot='R4',
    # inputs, durations and schedules
    states1=2, dirs2=2, TA=20.0, nobsA=200,
    kappa=1.0, ladder=5, T9=2000.0, dtobs9=0.2, t5=50.0,
    T6=100.0, eps6=1e-5, rank6=1e-8, time6=2000,
    cost_steps={'fft': 20, 'dense': 3},
    fe=dict(N=12, level=2, nq=3, amp2=1e-6, T=20.0, every=100),
)
DEV = dict(REG, seed=900201, N1=(8, 12), NA=(12,), N10=(8, 12), TA=5.0, T9=100.0, T6=30.0, time6=300,
           fe=dict(REG['fe'], T=2.0))
CID = dict(dry=0, c1=1, c2=2, c3=3, c4=4, c5=5, c6=6, c7=7, c8=8, c9=9, c10=10, c11=11)
SID = {s: i + 1 for i, s in enumerate(group2i.SLOTS)}
NEW_CODE = ('controls.py', 'fecheck.py', 'fftcubic.py', 'timearm.py')
CODE = NEW_CODE + ('pin.py', 'INSTRUMENT.sha256', 'FE.sha256', 'DESIGN.md', 'SHA256SUMS')
STOPPING = ('c1', 'c2', 'c4', 'c7', 'c8', 'c9')
LINES = {
    'c1': 'The FFT cubic against the instrument\'s: normalized discrepancy at most 1e-11, absolute errors recorded; '
          'each mutation arm turns it red.',
    'c2': 'Energy and gradient: the FFT cubic is the gradient of the quartic energy of the same assembly, which equals '
          'the instrument\'s energy, each at most 1e-11 normalized.',
    'c3': 'Free modes, cubic off: Verlet at (2/h) arcsin(h w/2), the splitting at w, within the ceiling of control 4.',
    'c4': 'Reversibility: forward then backward returns within 1e-10 of |(q, p)|, the floor recorded.',
    'c5': 'The rigid standing waves in R1 and R3: each matched discrete wave within the ceiling of control 4, and the '
          'continuum-started wave converging at second order.',
    'c6': 'Theorem 3.7\'s distinct nonzero E0 frequencies read in time in R1 and R3, under step halving, for both '
          'steppers.',
    'c7': 'Charges: every applicable J_D within 1e-10 of ||D|| |q| |p|, reported against ten times the dry-run floor.',
    'c8': 'Equivariance under right SU(2), the phase, Sp(1) and, in the real slots, charge conjugation: within the '
          'ceiling of control 4.',
    'c9': 'Convergence and energy: halving ratios in [3.5, 4.5] where h w_max <= 0.5 and above the floor; the energy '
          'error at O(h^2) with its drift within 1e-2 of its largest oscillation; linear Verlet under C-bar.',
    'c10': 'Cost: complete-step time with diagnostics, and peak memory, at N = 16, 24 and 32, each stepper and cubic.',
    'c11': 'The finite-element cross-check, last and report-only.',
}
READINGS = (
    'The floors (the dry run): each is the same machinery, seeds, sizes, steps and durations with the cubic switched '
    'off, where each stepper\'s answer is exact in exact arithmetic: the splitting is then the exact linear flow, and '
    'Verlet keeps its modified energy and carries its discrete rotations. Control 9\'s "above the measured floor" reads '
    'as above ten times it, as control 7 reports against ten times its floor. A ladder with no error above ten floors '
    'where h w-bar <= 0.5 passes as at floor; one with such an error and no ratio read fails as unread.',
    'The splitting\'s matched rigid wave reads kappa = ||c||^2 where its kick reads the state, after the first half '
    'rotation (DEVLOG entry 4); Verlet\'s kicks read the step\'s ends.',
    'Control 3 takes section 5\'s step at its free-field limit, 1.6/sqrt(N(N+2)), since its cubic is off. It reads each '
    'level\'s angle per step from z_{k+1} + z_{k-1} = 2 cos(theta) z_k, which holds exactly for a stepper whose map on '
    'one mode is 2 x 2 of determinant 1, by least squares over the run, from a generic position and momentum.',
    'Controls 4, 7 and 8 read one set of runs, made at control 4: each multi-level state forward over TA and back, and '
    'each transformed state forward.',
    'Charges are normalized by ||D|| |q(0)| |p(0)|, ||D|| the spectral norm. Each input\'s charges are checked nonzero at '
    'the start, each at least 1e-6 of that normalization.',
    'Control 5\'s continuum-started convergence is read by control 9\'s ratio rule, at control 5. Control 9 then reads '
    'control 6\'s frequencies and the energy, so no quantity is read twice.',
    'Control 9\'s h w_max is read with section 5\'s bound: a ratio e(h)/e(h/2) is read where h w-bar <= 0.5, which '
    'implies h w_max <= 0.5.',
    'Control 9\'s unperturbed controls are the runs without a perturbation, read in two parts (DEVLOG entry 8). The '
    'order of the energy error is read on the multi-level states of controls 4, 7 and 8, under halving over TA: on a '
    'rigid wave the error\'s O(h^2) part is constant along the rotation, by the phase invariance, so the error there '
    'comes out O(h^4). Its secular drift is read on control 5\'s continuum-started rigid waves, at every step of the '
    'ladder over T9 = 2000, where the error oscillates at the single radial frequency: observed every 0.2 or so, below '
    'the Nyquist period of that oscillation and its harmonic, a pure oscillation at R1\'s radial frequency moves the '
    'two tenths\' means apart by at most 0.0047 of its amplitude over T9.',
    'Control 6 reads Theorem 3.7\'s frequencies on E0: 2 omega, n times, and (4 omega^2 + 2 kappa)^(1/2), with omega^2 = '
    'lambda_0 + kappa and kappa = |psi|^2 = ||phi||^2 in the normalized measure. The perturbation lies in E0, of relative '
    'size eps6, with its first-order charge removed, so it leaves the family at fixed charge and moves the frequencies '
    'only at second order. The state is demodulated at the scheme\'s own discrete rotation, and the frequencies are the '
    'arguments of the eigenvalues of the least-squares one-step map of the demodulated E0 data at its numerical rank '
    '(dynamic mode decomposition). Their moduli are an extraction diagnostic, not a growth or decay rate: the read '
    'eigenvalues sat on the unit circle to about 1e-9 in development, the zero-frequency ones fitted from weakly '
    'excited directions did not (DEVLOG entry 11), and the outputs record the two apart.',
    'The rule of section 4 compares, for each of Theorem 3.7\'s two frequencies in R1 and R3, Verlet\'s relative error '
    'at section 5\'s step h0 with the splitting\'s, measured at the step at which the splitting costs Verlet\'s '
    'wall-clock per unit of evolved time, h0 tau_s/tau_v, with tau each stepper\'s measured time per step at h0. The '
    'registered perturbation is evolved there over T6 and read as in control 6. The rule adopts the splitting only if '
    'each of its errors there is at most a quarter of Verlet\'s, that step stays below pi/w-bar, and the splitting '
    'passed controls 3 to 9.',
    'Control 10 runs in R4, the slot of the timing before the dated note, each measurement in its own process: the time '
    'per step alone, and with every diagnostic at every step, and the peak resident memory. Verlet\'s force at the end '
    'of each call is carried into the next, so every timing counts one cubic per step.',
    'Control 11 runs at ||c||^2 = 1e-6, so the nonlinearity\'s phase over its duration is about 1e-6 rad: it compares the '
    'two discretizations of the field on R4\'s lowest level, where the frozen record gives the mesh\'s lift, and reads '
    'no slow flow.',
    'The equivariance maps: the phase e^{i phi}, right translation by a random U and, in R1, R2, R6 and R8, J and a '
    'random element a + bJ of Sp(1); in the real slots, charge conjugation. Each acts on position and velocity.',
    'Control 1\'s arms (DEVLOG entry 7): the aliased grid is M = 4 max(levels), one point short of exactness for the '
    'levels present; the missing conjugation of A is planted in a basis whose intertwiners carry a complex phase per '
    'copy, against the instrument\'s cubic transformed to that basis, since the instrument\'s intertwiners are real. '
    'The FFT path on that phased basis must itself agree to 1e-11. An arm is red when its worst discrepancy over every '
    'slot, N and state exceeds 1e-11.',
    'Control 6 reads distinct frequencies: one trajectory excites one direction of each degenerate eigenspace, so '
    '2 omega, n times, reads once, and a degeneracy the scheme split would read as further values (DEVLOG entry 7).',
    'A failure of control 4, 7, 8 or 9 by the splitting alone disqualifies the splitting under the rule of section 4, '
    'and the controls go on with Verlet. A failure by Verlet, a failure of control 1 or 2, or a run past C-bar stops '
    'them.',
)


# ---- records -------------------------------------------------------------------------------------------------------
def sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def git(*args):
    r = subprocess.run(['git', *args], cwd=HERE, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def environment():
    return dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                platform=platform.platform(), blas_threads=1, git_head=git('rev-parse', 'HEAD'),
                uncommitted=git('status', '--porcelain', '--', *CODE),
                new_code={f: sha256(os.path.join(HERE, f)) for f in NEW_CODE},
                pins={f: sha256(os.path.join(HERE, f)) for f in ('pin.py', 'INSTRUMENT.sha256', 'FE.sha256')})


def scrub(text):
    """Text with this checkout's location replaced, so that no output carries a machine path."""
    root = git('rev-parse', '--show-toplevel') or os.path.dirname(HERE)
    return text.replace(root, '<repository>').replace(os.path.expanduser('~'), '<home>')


def scrubbed_traceback():
    import traceback
    return scrub(traceback.format_exc())


def jsonable(x):
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, np.ndarray):
        return jsonable(x.tolist())
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, (int, np.integer)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return float(x)
    if isinstance(x, (complex, np.complexfloating)):
        return [float(x.real), float(x.imag)]
    return x


class Ctx:
    def __init__(self, dev, out=None):
        self.dev, self.P = dev, (DEV if dev else REG)
        self.env = environment()
        if dev:
            stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
            self.out = out or os.path.join(HERE, 'dev', 'runs', stamp)      # a given folder, for a development test
        else:
            assert out is None, 'the registered run writes record/ only'
            if self.env['git_head'] is None:
                raise SystemExit('refused: the registered run needs a git checkout, with this folder\'s code committed')
            if self.env['uncommitted']:
                raise SystemExit('refused: the registered run needs this folder\'s code committed and unchanged:\n'
                                 + self.env['uncommitted'])
            self.out = os.path.join(HERE, 'record')
            if os.path.exists(self.out):
                raise SystemExit('refused: record/ exists, and the registered run writes it once')
        os.makedirs(self.out)
        self.cache, self.t0 = {}, time.time()
        self.runsA, self.runsB, self.c6 = {}, {}, {}

    def rng(self, control, slot, N, draw):
        return np.random.default_rng([self.P['seed'], CID[control], SID.get(slot, 0), int(N), int(draw)])

    def log(self, msg):
        line = f'[{time.time() - self.t0:9.1f} s] {msg}'
        print(line, flush=True)
        with open(os.path.join(self.out, 'run.log'), 'a', encoding='utf-8') as f:
            f.write(line + '\n')

    def save(self, name, obj):
        path = os.path.join(self.out, name + '.json')
        if os.path.exists(path):
            raise SystemExit(f'refused: {path} exists, and outputs are written once')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(jsonable(obj), f, indent=1)

    def slot(self, slot, N, dense=False):
        S = self.cache.get((slot, N))
        if S is None:
            S = self.cache[(slot, N)] = Slot(slot, N)
        if dense and S.F is None:
            S.F = fn.Functional(S.B)
        return S

    def clear(self):
        self.cache.clear()
        gc.collect()


# ---- the pieces ----------------------------------------------------------------------------------------------------
class Slot:
    def __init__(self, slot, N):
        self.slot, self.N = slot, N
        self.B = basis.Basis(slot, N)
        self.X = fftcubic.FFTCubic(self.B)
        self.F, self._D = None, None
        self.e = self.B.eig
        self.n = np.array([n for n, _, _ in self.B.index])
        self.n0 = self.B.levels[0]
        self.low = self.n == self.n0
        self.lam0 = float(self.n0 * (self.n0 + 2))
        self.quat = slot in group2i.SPINORIAL

    @property
    def D(self):
        if self._D is None:
            if self.F is None:
                self.F = fn.Functional(self.B)
            self._D = ta.Diagnostics(self.B, self.X.quartic, self.F)
        return self._D


def cgauss(rng, m):
    return (rng.standard_normal(m) + 1j * rng.standard_normal(m)) / np.sqrt(2)


def multi_level(S, rng):
    """Every coefficient's position and momentum drawn, weighted by 1/(n+1) and sqrt(n(n+2))/(n+1), then scaled to
    ||c||^2 = 1 and ||v||^2 = lambda_0."""
    c = cgauss(rng, S.B.m) / (S.n + 1)
    v = cgauss(rng, S.B.m) * np.sqrt(S.e) / (S.n + 1)
    return c / np.linalg.norm(c), v * np.sqrt(S.lam0) / np.linalg.norm(v)


def on_level(S, rng, mask, size):
    x = np.zeros(S.B.m, complex)
    x[mask] = cgauss(rng, int(mask.sum()))
    return x * size / np.linalg.norm(x)


def step5(S, H0, P):
    """Section 5: C-bar = 2 H(0) / ((1 - 0.8^2) lambda_0), w-bar^2 = N(N+2) + 3 (m/r) C-bar, h = 0.8 * 2 / w-bar."""
    cbar = 2 * H0 / ((1 - P['margin'] ** 2) * S.lam0)
    wbar = float(np.sqrt(S.N * (S.N + 2) + 3 * (S.B.m / S.B.r) * cbar))
    return P['margin'] * 2 / wbar, float(cbar), wbar


def ZERO(c):
    return np.zeros_like(c)


def evolve(kind, c, v, h, K, S, cubic, cbar, every=1, observe=None):
    f = ta.verlet if kind == 'verlet' else ta.strang
    out = f(c, v, h, K, S.e, cubic, cbar=cbar, observe=observe, every=every)
    return out[0], out[1]


def qp(c, v):
    return float(np.sqrt(np.vdot(c, c).real + np.vdot(v, v).real))


def conserved(S, kind, h, cubic_on):
    """The energy a run carries: the total energy when the cubic is on, kept to O(h^2); with the cubic off, the free
    energy under the splitting and Verlet's modified energy, each kept exactly in exact arithmetic."""
    if cubic_on:
        return S.D.energy
    if kind == 'strang':
        return lambda c, v: 0.5 * float(np.vdot(v, v).real + np.sum(S.e * np.abs(c) ** 2))
    return lambda c, v: 0.5 * float(np.vdot(v, v).real + np.sum(S.e * (1 - h * h * S.e / 4) * np.abs(c) ** 2))


def energy_stats(E, E0):
    r = (np.asarray(E) - E0) / E0
    m = max(1, len(r) // 10)
    return dict(max=float(np.abs(r).max()), drift=float(abs(r[-m:].mean() - r[:m].mean())), n_obs=len(r))


def maps(S, rng):
    phi = 2 * np.pi * rng.random()
    q = rng.standard_normal(4)
    R = fn.right_rotation(S.B, su2.quat_to_su2(q / np.linalg.norm(q)))
    K = S.D.K
    out = {'phase': lambda c: np.exp(1j * phi) * c, 'right_su2': lambda c: R @ c}
    if S.quat:
        ab = cgauss(rng, 2)
        a, b = ab / np.linalg.norm(ab)
        out['sp1_J'] = lambda c: K @ np.conj(c)
        out['sp1_element'] = lambda c: a * c + b * (K @ np.conj(c))
    else:
        out['conjugation'] = lambda c: K @ np.conj(c)
    return out


def setup_A(ctx, slot, N):
    """The multi-level state of controls 4, 7 and 8 (and their floors), its step, schedule and maps."""
    P = ctx.P
    S = ctx.slot(slot, N)
    c0, v0 = multi_level(S, ctx.rng('c4', slot, N, 0))
    D = S.D
    h, cbar, wbar = step5(S, D.energy(c0, v0), P)
    K = int(np.ceil(P['TA'] / h))
    Q0, scale = D.charges(c0, v0), np.linalg.norm(c0) * np.linalg.norm(v0)
    q0 = {k: Q0[k] / (D.norms[k] * scale) for k in Q0}
    if min(abs(x) for x in q0.values()) < 1e-6:
        raise SystemExit(f'input check: a charge of the {slot} N = {N} state is not nonzero at the start: {q0}')
    return dict(S=S, c0=c0, v0=v0, h=h, cbar=cbar, wbar=wbar, K=K, every=max(1, K // P['nobsA']), q0=q0,
                G=maps(S, ctx.rng('c8', slot, N, 0)), levels=len(S.B.levels))


def run_A(A, kind, cubic_on):
    S, c0, v0, h, K, cbar = A['S'], A['c0'], A['v0'], A['h'], A['K'], A['cbar']
    cubic = S.X.cubic if cubic_on else ZERO
    D, en = S.D, conserved(S, kind, h, cubic_on)
    Q0, E0 = D.charges(c0, v0), en(c0, v0)
    Qs, Es, top = [Q0], [E0], [np.vdot(c0, c0).real]

    def obs(s, c, v):
        Qs.append(D.charges(c, v))
        Es.append(en(c, v))
        top.append(np.vdot(c, c).real)

    c1, v1 = evolve(kind, c0, v0, h, K, S, cubic, cbar, A['every'], obs)
    cb, vb = evolve(kind, c1, v1, -h, K, S, cubic, cbar)
    scale = np.linalg.norm(c0) * np.linalg.norm(v0)
    out = dict(rev=qp(cb - c0, vb - v0) / qp(c0, v0),
               charge={k: max(abs(Q[k] - Q0[k]) for Q in Qs) / (D.norms[k] * scale) for k in Q0},
               energy=energy_stats(Es, E0), cmax_over_cbar=max(top) / cbar, equiv={})
    for name, g in A['G'].items():
        cg, vg = evolve(kind, g(c0), g(v0), h, K, S, cubic, cbar)
        out['equiv'][name] = qp(cg - g(c1), vg - g(v1)) / qp(c1, v1)
    return out


def energy_ladder(A, kind, cubic_on, P):
    """A multi-level state's relative energy error at each step h/2^j of the ladder over TA: its largest value over
    the observations, at times common to every step. With the cubic off, the energy each stepper keeps exactly."""
    S, out = A['S'], []
    for j in range(P['ladder']):
        h, K, every = A['h'] / 2 ** j, A['K'] * 2 ** j, A['every'] * 2 ** j
        en = conserved(S, kind, h, cubic_on)
        E0 = en(A['c0'], A['v0'])
        Es = [E0]
        evolve(kind, A['c0'], A['v0'], h, K, S, S.X.cubic if cubic_on else ZERO, A['cbar'], every,
               lambda s, c, v: Es.append(en(c, v)))
        out.append(energy_stats(Es, E0)['max'])
    return out


def omega_estimate(S, c, rng, iters=60):
    """Power iteration on the instrument's hess_apply at lambda = 0. It approaches w_max from below, so it reports
    the margin and never sets h (section 5)."""
    S.D
    d = cgauss(rng, S.B.m)
    d /= np.linalg.norm(d)
    lam = 0.0
    for _ in range(iters):
        w = S.F.hess_apply(c, 0.0, d)
        lam = float(np.vdot(d, w).real)
        d = w / np.linalg.norm(w)
    return float(np.sqrt(max(lam, 0.0)))


def setup_B(ctx, slot):
    """The rigid member of controls 5 and 6, at kappa = ||phi||^2 on E0, its step ladder and schedules, and control 6's
    perturbation, drawn once."""
    P = ctx.P
    N = P['NB']
    S = ctx.slot(slot, N)
    kappa = P['kappa']
    phi = on_level(S, ctx.rng('c5', slot, N, 0), S.low, np.sqrt(kappa))
    Om = float(np.sqrt(S.lam0 + kappa))
    h0, cbar, wbar = step5(S, S.D.energy(phi, 1j * Om * phi), P)
    every0 = max(1, int(round(P['dtobs9'] / h0)))
    rng6 = ctx.rng('c6', slot, N, 0)
    return dict(S=S, slot=slot, phi=phi, Om=Om, kappa=kappa, h0=h0, cbar=cbar, wbar=wbar,
                hs=[h0 / 2 ** j for j in range(P['ladder'])], every0=every0,
                K0=int(np.ceil(P['T9'] / (every0 * h0))) * every0, i5=int(round(P['t5'] / (every0 * h0))),
                K6=int(np.ceil(P['T6'] / h0)), dpert=(on_level(S, rng6, S.low, 1.0), on_level(S, rng6, S.low, 1.0)))


def matched_run(R, kind, j, cubic_on):
    """The matched discrete wave at ladder step j over T9: its error against the exact discrete rotation."""
    S, phi = R['S'], R['phi']
    h, every, K = R['hs'][j], R['every0'] * 2 ** j, R['K0'] * 2 ** j
    z0, dz0, th = ta.matched(kind, h, S.lam0, R['kappa'] if cubic_on else 0.0)
    c0, v0 = z0 * phi, dz0 * phi
    scale, errs, top = qp(c0, v0), [0.0], [np.vdot(c0, c0).real]

    def obs(s, c, v):
        ph = np.exp(1j * s * th)
        errs.append(qp(c - ph * c0, v - ph * v0) / scale)
        top.append(np.vdot(c, c).real)

    evolve(kind, c0, v0, h, K, S, S.X.cubic if cubic_on else ZERO, R['cbar'], every, obs)
    return dict(t5=errs[R['i5']], max=max(errs), theta=th, z0_abs2=abs(z0) ** 2, steps=K,
                cmax_over_cbar=max(top) / R['cbar'])


def continuum_run(R, kind, j, cubic_on):
    """The wave started from the continuum's (phi, i Omega phi) at ladder step j over T9: its state error at t5 against
    the continuum's e^{i Omega t} phi, and its energy over the run."""
    S, phi = R['S'], R['phi']
    W = R['Om'] if cubic_on else float(np.sqrt(S.lam0))
    h, every, K = R['hs'][j], R['every0'] * 2 ** j, R['K0'] * 2 ** j
    en = conserved(S, kind, h, cubic_on)
    c0, v0 = phi, 1j * W * phi
    E0, scale = en(c0, v0), qp(c0, v0)
    Es, errs, top = [E0], [0.0], [np.vdot(c0, c0).real]

    def obs(s, c, v):
        ph = np.exp(1j * W * s * h)
        errs.append(qp(c - ph * phi, v - 1j * W * ph * phi) / scale)
        Es.append(en(c, v))
        top.append(np.vdot(c, c).real)

    evolve(kind, c0, v0, h, K, S, S.X.cubic if cubic_on else ZERO, R['cbar'], every, obs)
    return dict(t5=errs[R['i5']], t=R['i5'] * R['every0'] * R['h0'], energy=energy_stats(Es, E0), steps=K,
                cmax_over_cbar=max(top) / R['cbar'])


def dmd(X, h, rank_rel):
    """The arguments per unit time of the eigenvalues of the least-squares one-step map of the columns of X, at the
    data's numerical rank."""
    X0, X1 = X[:, :-1], X[:, 1:]
    U, s, Vh = np.linalg.svd(X0, full_matrices=False)
    r = int(np.sum(s > rank_rel * s[0]))
    A = (U[:, :r].T @ X1 @ Vh[:r].T) / s[:r]
    nu = np.linalg.eigvals(A)
    return np.angle(nu) / h, nu, r


def perturbed_run(R, kind, h, K, cubic_on, P):
    """Control 6 at step h over K steps: the matched member, perturbed in E0 at relative size eps6 with its
    first-order charge removed, demodulated at the scheme's own rotation and read by dmd. With the cubic off the member
    is the free wave, and every positive frequency is the scheme's exact 2 theta / h. The moduli of the fitted map's
    eigenvalues are recorded as an extraction diagnostic, the read ones apart from the rest."""
    S, phi = R['S'], R['phi']
    kappa = R['kappa'] if cubic_on else 0.0
    z0, dz0, th = ta.matched(kind, h, S.lam0, kappa)
    c0, v0 = z0 * phi, dz0 * phi
    dc, dv = R['dpert']
    dN = float(np.imag(np.vdot(dc, v0) + np.vdot(c0, dv)))
    dv = dv - 1j * c0 * dN / np.vdot(c0, c0).real
    sc = P['eps6'] * qp(c0, v0) / qp(dc, dv)
    dc, dv = sc * dc, sc * dv
    low, snaps, off, top = S.low, [], [0.0], []

    def obs(s, c, v):
        ph = np.exp(-1j * s * th)
        zc, zv = ph * c[low] - c0[low], ph * v[low] - v0[low]
        snaps.append(np.concatenate([zc.real, zc.imag, zv.real, zv.imag]))
        off.append(qp(c[~low], v[~low]))
        top.append(np.vdot(c, c).real)

    obs(0, c0 + dc, v0 + dv)
    evolve(kind, c0 + dc, v0 + dv, h, K, S, S.X.cubic if cubic_on else ZERO, R['cbar'], 1, obs)
    mu, nu, rank = dmd(np.array(snaps).T, h, P['rank6'])
    n1 = int(low.sum())
    # the distinct values: one trajectory excites one direction of each degenerate eigenspace, so 2 omega, n times,
    # reads once, and a degeneracy that the scheme split would read as further values
    if cubic_on:
        expect = np.array(([2 * R['Om']] if n1 > 1 else []) + [np.sqrt(4 * R['Om'] ** 2 + 2 * kappa)])
    else:
        expect = np.array([2 * th / h])
    cut = 0.25 * expect.min()
    pos = np.sort(mu[mu > cut])
    dev = np.abs(np.abs(nu) - 1)
    rd = np.abs(mu) > cut
    out = dict(h=h, steps=K, rank=rank, frequencies=pos, expected=expect, off_E0=max(off) / qp(c0, v0),
               extraction_moduli=dict(read=float(dev[rd].max()) if rd.any() else float('nan'),
                                      rest=float(dev[~rd].max()) if (~rd).any() else float('nan')),
               cmax_over_cbar=max(top) / R['cbar'], read=len(pos) == len(expect))
    if out['read']:
        rel = np.abs(pos - expect) / expect
        out['errors'] = {'2omega': float(rel[0]) if len(expect) > 1 else float('nan'), 'radial': float(rel[-1]),
                         'all': float(rel.max())}
    else:
        out['errors'] = {'2omega': float('nan'), 'radial': float('nan'), 'all': float('nan')}
    return out


def time_per_step(R, kind, steps):
    """The wall-clock per step at h0, after 20 warm-up steps, with Verlet's force carried from them, so that each
    stepper counts one cubic per step."""
    S, h = R['S'], R['h0']
    z0, dz0, _ = ta.matched(kind, h, S.lam0, R['kappa'])
    c, v = z0 * R['phi'], dz0 * R['phi']
    if kind == 'verlet':
        c, v, a = ta.verlet(c, v, h, 20, S.e, S.X.cubic, cbar=R['cbar'])
        t = time.perf_counter()
        ta.verlet(c, v, h, steps, S.e, S.X.cubic, a=a, cbar=R['cbar'])
    else:
        c, v = ta.strang(c, v, h, 20, S.e, S.X.cubic, cbar=R['cbar'])
        t = time.perf_counter()
        ta.strang(c, v, h, steps, S.e, S.X.cubic, cbar=R['cbar'])
    return (time.perf_counter() - t) / steps


def ratios(errs, floors, hs, wbar, P):
    """Halving ratios e(h)/e(h/2), each read only where h w-bar <= hw_read and both errors exceed floor times their
    floors. 'ok' when every read ratio lies in the window and one at least is read; 'at floor' when no step with
    h w-bar <= hw_read has an error above floor times its floor; otherwise 'unread', or 'out of window'."""
    lo, hi = P['ratio']
    F = P['floor']
    rows = []
    for j in range(len(hs) - 1):
        r = errs[j] / errs[j + 1] if errs[j + 1] > 0 else float('inf')
        read = hs[j] * wbar <= P['hw_read'] and errs[j] > F * floors[j] and errs[j + 1] > F * floors[j + 1]
        rows.append(dict(h=hs[j], hw=hs[j] * wbar, ratio=r, read=bool(read), in_window=bool(lo <= r <= hi)))
    read = [x for x in rows if x['read']]
    asym = [j for j in range(len(hs)) if hs[j] * wbar <= P['hw_read']]
    if read:
        status = 'ok' if all(x['in_window'] for x in read) else 'out of window'
    elif all(errs[j] <= F * floors[j] for j in asym):
        status = 'at floor'
    else:
        status = 'unread'
    return dict(errors=list(errs), floors=list(floors), rows=rows, status=status, passed=status in ('ok', 'at floor'))


def sci(xs):
    return '[' + ', '.join(f'{x:.2e}' for x in xs) + ']'


def by_kind(P, rows, key='ok'):
    return {k: all(r[key] for r in rows if r['kind'] == k) for k in P['kinds']}


# ---- the dry run and the controls ----------------------------------------------------------------------------------
def dry(ctx):
    P = ctx.P
    out = dict(A={}, B={}, cubic={})
    ctx.log('dry run: every floor, the cubic off')
    for slot in P['slots']:
        for N in P['NA']:
            A = setup_A(ctx, slot, N)
            for kind in P['kinds']:
                r = run_A(A, kind, cubic_on=False)
                out['A'][f'{slot}/{N}/{kind}'] = dict(rev=r['rev'], charge=max(r['charge'].values()),
                                                     equiv=max(r['equiv'].values()), energy=r['energy']['max'],
                                                     energy_ladder=energy_ladder(A, kind, False, P))
                ctx.log(f'  {slot} N={N} {kind}: {out["A"][f"{slot}/{N}/{kind}"]}')
        ctx.clear()
    for slot in P['rigid']:
        R = setup_B(ctx, slot)
        for kind in P['kinds']:
            for j in range(P['ladder']):
                m = matched_run(R, kind, j, cubic_on=False)
                c = continuum_run(R, kind, j, cubic_on=False)
                f = perturbed_run(R, kind, R['hs'][j], R['K6'] * 2 ** j, False, P)
                out['B'][f'{slot}/{kind}/{j}'] = dict(state_t5=m['t5'], state_max=m['max'], energy=c['energy']['max'],
                                                     freq=f['errors']['all'], freq_read=f['read'])
                ctx.log(f'  {slot} {kind} h0/{2 ** j}: {out["B"][f"{slot}/{kind}/{j}"]}')
        ctx.clear()
    for slot in P['slots']:
        for N in P['N1']:
            S = ctx.slot(slot, N, dense=True)
            c = c1_states(ctx, S)[0]
            rng = ctx.rng('dry', slot, N, 0)
            ph = np.exp(2j * np.pi * rng.random())
            q = rng.standard_normal(4)
            Rm = fn.right_rotation(S.B, su2.quat_to_su2(q / np.linalg.norm(q)))
            G0 = S.F.cubic(c)
            nG = np.linalg.norm(G0)
            out['cubic'][f'{slot}/{N}'] = dict(
                phase=float(np.linalg.norm(np.conj(ph) * S.F.cubic(ph * c) - G0) / nG),
                right_su2=float(np.linalg.norm(Rm.conj().T @ S.F.cubic(Rm @ c) - G0) / nG))
            ctx.log(f'  dense cubic floor {slot} N={N}: {out["cubic"][f"{slot}/{N}"]}')
            ctx.clear()
    return out


def c1_states(ctx, S):
    out = []
    for k in range(ctx.P['states1']):
        c = cgauss(ctx.rng('c1', S.slot, S.N, k), S.B.m)
        out.append(c / np.linalg.norm(c))
    out.append(on_level(S, ctx.rng('c1', S.slot, S.N, 99), S.low, 1.0))
    return out


def phased(S, rng):
    """A copy of the basis whose intertwiners carry a complex phase per copy, and the phase of each coefficient: the
    instrument's intertwiners are real, so the missing conjugation of A can bite only here."""
    chi = {n: rng.uniform(0, 2 * np.pi, len(S.B.A[n])) for n in S.B.levels}
    B2 = copy.copy(S.B)
    B2.A = {n: [np.exp(1j * x) * a for x, a in zip(chi[n], S.B.A[n])] for n in S.B.levels}
    return B2, np.concatenate([np.repeat(np.exp(1j * chi[n]), n + 1) for n in S.B.levels])


def c1(ctx, floors):
    P = ctx.P
    rows, arms = [], {m: 0.0 for m in fftcubic.MUTATIONS[1:]}
    plain_conj, phased_ok = 0.0, 0.0
    for slot in P['slots']:
        for N in P['N1']:
            S = ctx.slot(slot, N, dense=True)
            muts = {m: fftcubic.FFTCubic(S.B, mutation=m) for m in arms if m != 'unconjugated_A'}
            B2, ph = phased(S, ctx.rng('c1', slot, N, 98))
            X2, X2m = fftcubic.FFTCubic(B2), fftcubic.FFTCubic(B2, mutation='unconjugated_A')
            Xplain = fftcubic.FFTCubic(S.B, mutation='unconjugated_A')
            for k, c in enumerate(c1_states(ctx, S)):
                Gd, Gx = S.F.cubic(c), S.X.cubic(c)
                nd = np.linalg.norm(Gd)
                rows.append(dict(slot=slot, N=N, state='lowest' if k == P['states1'] else k, levels=len(S.B.levels),
                                 m=S.B.m, normalized=float(np.linalg.norm(Gx - Gd) / nd),
                                 absolute=float(np.linalg.norm(Gx - Gd)), max_abs=float(np.abs(Gx - Gd).max())))
                for m, Xm in muts.items():
                    arms[m] = max(arms[m], float(np.linalg.norm(Xm.cubic(c) - Gd) / nd))
                plain_conj = max(plain_conj, float(np.linalg.norm(Xplain.cubic(c) - Gd) / nd))
                ref = np.conj(ph) * S.F.cubic(ph * c)
                nr = np.linalg.norm(ref)
                phased_ok = max(phased_ok, float(np.linalg.norm(X2.cubic(c) - ref) / nr))
                arms['unconjugated_A'] = max(arms['unconjugated_A'], float(np.linalg.norm(X2m.cubic(c) - ref) / nr))
            ctx.log(f'  {slot} N={N}: worst {max(r["normalized"] for r in rows if r["slot"] == slot and r["N"] == N):.2e}')
            ctx.clear()
    worst = max(r['normalized'] for r in rows)
    red = {m: v > P['cubic_tol'] for m, v in arms.items()}
    return dict(passed=bool(worst <= P['cubic_tol'] and phased_ok <= P['cubic_tol'] and all(red.values())),
                worst=worst, phased_basis_worst=phased_ok, rows=rows,
                arms={m: dict(worst=arms[m], red=red[m]) for m in arms},
                unconjugated_A_in_the_real_basis=plain_conj, floors=floors['cubic'])


def c2(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['slots']:
        for N in P['N1']:
            S = ctx.slot(slot, N, dense=True)
            for k, c in enumerate(c1_states(ctx, S)):
                Vd = S.F.energy(c, 0.0) - 0.5 * np.sum(S.e * np.abs(c) ** 2)
                G = S.X.cubic(c)
                grads = []
                for j in range(P['dirs2']):
                    d = cgauss(ctx.rng('c2', slot, N, 10 * k + j), S.B.m)
                    d /= np.linalg.norm(d)
                    s = 0.5
                    V = [S.X.quartic(c + t * s * d) for t in (-2, -1, 1, 2)]
                    g5 = (V[0] - 8 * V[1] + 8 * V[2] - V[3]) / (12 * s)
                    grads.append(abs(g5 - float(np.vdot(G, d).real)) / np.linalg.norm(G))
                rows.append(dict(slot=slot, N=N, state='lowest' if k == P['states1'] else k,
                                 energy=float(abs(S.X.quartic(c) - Vd) / abs(Vd)), gradient=float(max(grads))))
            ctx.log(f'  {slot} N={N}: energy {max(r["energy"] for r in rows[-3:]):.2e}, '
                    f'gradient {max(r["gradient"] for r in rows[-3:]):.2e}')
            ctx.clear()
    we, wg = max(r['energy'] for r in rows), max(r['gradient'] for r in rows)
    return dict(passed=bool(we <= P['cubic_tol'] and wg <= P['cubic_tol']), worst_energy=we, worst_gradient=wg,
                rows=rows, stencil='five-point, exact for the quartic polynomial V(c + s d), s = 0.5')


def linear_exact(kind, h, w, K, c0, v0):
    if kind == 'strang':
        a = K * h * w
        return np.cos(a) * c0 + np.sin(a) / w * v0, -w * np.sin(a) * c0 + np.cos(a) * v0
    th = 2 * np.arcsin(h * w / 2)
    s = np.sin(K * th) / np.sin(th)
    return (np.cos(K * th) * c0 + h * s * v0,
            -h * w * w * (1 - h * h * w * w / 4) * s * c0 + np.cos(K * th) * v0)


def c3(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['slots']:
        for N in P['NA']:
            S = ctx.slot(slot, N)
            h = P['margin'] * 2 / np.sqrt(N * (N + 2))
            K = int(np.ceil(P['TA'] / h))
            for n in S.B.levels:
                if slot == 'R4' and n == S.n0:
                    continue                  # R4's free modes sit off its lowest level (section 8)
                lv, w = S.n == n, float(np.sqrt(n * (n + 2)))
                rng = ctx.rng('c3', slot, N, n)
                c0, v0 = on_level(S, rng, lv, 1.0), on_level(S, rng, lv, w)
                for kind in P['kinds']:
                    Z = [c0[lv]]
                    cK, vK = evolve(kind, c0, v0, h, K, S, ZERO, None, 1, lambda s, c, v: Z.append(c[lv].copy()))
                    Z = np.array(Z)
                    num = np.sum((np.conj(Z[1:-1]) * (2 * Z[1:-1] - Z[2:] - Z[:-2])).real)
                    th = 2 * np.arcsin(np.sqrt(num / (4 * np.sum(np.abs(Z[1:-1]) ** 2))))
                    th_exp = 2 * np.arcsin(h * w / 2) if kind == 'verlet' else h * w
                    ce, ve = linear_exact(kind, h, w, K, c0, v0)
                    rel = abs(th - th_exp) / th_exp
                    rows.append(dict(slot=slot, N=N, level=n, kind=kind, h=h, steps=K, frequency=th / h,
                                     expected=th_exp / h, rel=float(rel), state=qp(cK - ce, vK - ve) / qp(c0, v0),
                                     ok=bool(rel <= P['ceiling'])))
            ctx.log(f'  {slot} N={N}: worst {max(r["rel"] for r in rows if r["slot"] == slot and r["N"] == N):.2e}')
        ctx.clear()
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, worst=max(r['rel'] for r in rows), rows=rows)


def c4(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['slots']:
        for N in P['NA']:
            A = setup_A(ctx, slot, N)
            west = omega_estimate(A['S'], A['c0'], ctx.rng('c4', slot, N, 1))
            for kind in P['kinds']:
                key = f'{slot}/{N}/{kind}'
                r = run_A(A, kind, cubic_on=True)
                ctx.runsA[key] = dict(r, slot=slot, N=N, kind=kind, q0=A['q0'], levels=A['levels'])
                rows.append(dict(key=key, kind=kind, levels=A['levels'], h=A['h'], steps=A['K'], wbar=A['wbar'],
                                 cbar=A['cbar'], omega_estimate=west, h_omega_estimate=A['h'] * west,
                                 cmax_over_cbar=r['cmax_over_cbar'], rev=r['rev'],
                                 floor=floors['A'][key]['rev'], ok=bool(r['rev'] <= P['ceiling'])))
                ctx.log(f'  {key}: reversibility {r["rev"]:.2e} (floor {floors["A"][key]["rev"]:.1e})')
        ctx.clear()
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, worst=max(r['rev'] for r in rows), rows=rows)


def c5(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['rigid']:
        R = setup_B(ctx, slot)
        for kind in P['kinds']:
            m = matched_run(R, kind, 0, cubic_on=True)
            cont = [continuum_run(R, kind, j, cubic_on=True) for j in range(P['ladder'])]
            fl = [floors['B'][f'{slot}/{kind}/{j}']['state_t5'] for j in range(P['ladder'])]
            conv = ratios([c['t5'] for c in cont], fl, R['hs'], R['wbar'], P)
            ctx.runsB[(slot, kind)] = dict(energy=[c['energy'] for c in cont], hs=R['hs'], wbar=R['wbar'])
            ok = m['max'] <= P['ceiling'] and conv['passed']
            rows.append(dict(slot=slot, kind=kind, h0=R['h0'], wbar=R['wbar'], cbar=R['cbar'], matched=m,
                             matched_floor=floors['B'][f'{slot}/{kind}/0']['state_max'], continuum=cont,
                             convergence=conv, ok=bool(ok)))
            ctx.log(f'  {slot} {kind}: matched {m["max"]:.2e}; continuum at t5 {sci(c["t5"] for c in cont)} '
                    f'({conv["status"]})')
        ctx.clear()
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, rows=rows)


def c6(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['rigid']:
        R = setup_B(ctx, slot)
        tau = {k: [] for k in P['kinds']}
        for _ in range(3):
            for kind in P['kinds']:
                tau[kind].append(time_per_step(R, kind, P['time6']))
        tau = {k: min(v) for k, v in tau.items()}
        ctx.c6[slot] = dict(h0=R['h0'], wbar=R['wbar'], hs=R['hs'], tau=tau)
        for kind in P['kinds']:
            reads = [perturbed_run(R, kind, R['hs'][j], R['K6'] * 2 ** j, True, P) for j in range(P['ladder'])]
            ctx.c6[slot][kind] = reads
            rows.append(dict(slot=slot, kind=kind, h0=R['h0'], wbar=R['wbar'], tau=tau[kind], reads=reads,
                             ok=all(r['read'] for r in reads)))
            ctx.log(f'  {slot} {kind}: errors 2w {sci(r["errors"]["2omega"] for r in reads)}, '
                    f'radial {sci(r["errors"]["radial"] for r in reads)}; {tau[kind] * 1e3:.2f} ms per step')
        ctx.clear()
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, rows=rows)


def c7(ctx, floors):
    P = ctx.P
    rows = []
    for key, r in ctx.runsA.items():
        fl = floors['A'][key]['charge']
        for D, drift in r['charge'].items():
            rows.append(dict(key=key, kind=r['kind'], charge=D, initial=r['q0'][D], drift=drift, floor=fl,
                             vs_ten_floors=drift / (10 * fl) if fl > 0 else float('inf'),
                             ok=bool(drift <= P['charge_tol'])))
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, worst=max(r['drift'] for r in rows), rows=rows)


def c8(ctx, floors):
    P = ctx.P
    rows = []
    for key, r in ctx.runsA.items():
        for g, err in r['equiv'].items():
            rows.append(dict(key=key, kind=r['kind'], map=g, error=err, floor=floors['A'][key]['equiv'],
                             ok=bool(err <= P['ceiling'])))
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, worst=max(r['error'] for r in rows), rows=rows,
                energy_diagnostic={k: r['energy'] for k, r in ctx.runsA.items()})


def c9(ctx, floors):
    P = ctx.P
    rows = []
    for slot in P['rigid']:
        d = ctx.c6[slot]
        for kind in P['kinds']:
            fl = [floors['B'][f'{slot}/{kind}/{j}']['freq'] for j in range(P['ladder'])]
            for f in ('2omega', 'radial'):
                errs = [r['errors'][f] for r in d[kind]]
                q = ratios(errs, fl, d['hs'], d['wbar'], P)
                rows.append(dict(part='frequency', slot=slot, kind=kind, quantity=f, **q, ok=q['passed']))
            e = ctx.runsB[(slot, kind)]
            efl = [floors['B'][f'{slot}/{kind}/{j}']['energy'] for j in range(P['ladder'])]
            drift = [dict(h=e['hs'][j], drift=x['drift'], largest=x['max'], read=bool(x['max'] > P['floor'] * efl[j]),
                          ok=bool(x['max'] <= P['floor'] * efl[j] or x['drift'] <= P['drift'] * x['max']))
                     for j, x in enumerate(e['energy'])]
            rows.append(dict(part='energy drift', slot=slot, kind=kind, energy=[x['max'] for x in e['energy']],
                             floors=efl, drift=drift, ok=all(x['ok'] for x in drift)))
            ctx.log(f'  {slot} {kind}: rigid-wave energy {sci(x["max"] for x in e["energy"])}; drift '
                    f'{sci(x["drift"] / max(x["largest"], 1e-300) for x in drift)} of the largest oscillation')
    for slot in P['slots']:
        for N in P['NA']:
            A = setup_A(ctx, slot, N)
            for kind in P['kinds']:
                key = f'{slot}/{N}/{kind}'
                errs = energy_ladder(A, kind, True, P)
                q = ratios(errs, floors['A'][key]['energy_ladder'], [A['h'] / 2 ** j for j in range(P['ladder'])],
                           A['wbar'], P)
                rows.append(dict(part='energy order', key=key, kind=kind, **q, ok=q['passed']))
                ctx.log(f'  {key}: energy {sci(errs)} ({q["status"]})')
            top = [np.vdot(A['c0'], A['c0']).real]
            evolve('verlet', A['c0'], A['v0'], A['h'], A['K'], A['S'], ZERO, None, 1,
                   lambda s, c, v: top.append(np.vdot(c, c).real))
            rows.append(dict(part='C-bar', slot=slot, N=N, kind='verlet', max_norm2=max(top), cbar=A['cbar'],
                             ok=bool(max(top) <= A['cbar'])))
        ctx.clear()
    bk = by_kind(P, rows)
    return dict(passed=all(bk.values()), by_kind=bk, rows=rows)


def c10(ctx, floors):
    P = ctx.P
    rows = []
    for N in P['N10']:
        for cubic in ('fft', 'dense'):
            for kind in P['kinds']:
                cmd = [sys.executable, '-I', '-B', os.path.abspath(__file__), 'cost', P['cost_slot'], str(N), kind,
                       cubic, str(P['cost_steps'][cubic]), str(P['seed'])]
                r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
                if r.returncode != 0:
                    raise RuntimeError(f'cost run {cmd[4:]} failed:\n{scrub(r.stderr[-2000:])}')
                rows.append(json.loads(r.stdout.strip().splitlines()[-1]))
                ctx.log(f'  N={N} {cubic} {kind}: {rows[-1]["step"]:.4f} s per step, {rows[-1]["step_with_diagnostics"]:.4f}'
                        f' s with diagnostics, peak {rows[-1]["peak_rss_gb"]:.2f} GB')
    return dict(passed=None, rows=rows)


def cost_child(slot, N, kind, cubic, steps, seed):
    t0 = time.perf_counter()
    B = basis.Basis(slot, N)
    if cubic == 'fft':
        X = fftcubic.FFTCubic(B)
        force, quartic = X.cubic, X.quartic
    else:
        F = fn.Functional(B)
        force = F.cubic
        quartic = lambda c: F.energy(c, 0.0) - 0.5 * np.sum(B.eig * np.abs(c) ** 2)  # noqa: E731
    D = ta.Diagnostics(B, quartic, None)       # R4 is real: the phase and right-SU(2) charges
    build = time.perf_counter() - t0
    n = np.array([k for k, _, _ in B.index])
    lam0 = B.levels[0] * (B.levels[0] + 2)
    rng = np.random.default_rng([seed, CID['c10'], SID[slot], N, 0])
    c = cgauss(rng, B.m) / (n + 1)
    v = cgauss(rng, B.m) * np.sqrt(B.eig) / (n + 1)
    c, v = c / np.linalg.norm(c), v * np.sqrt(lam0) / np.linalg.norm(v)
    margin = REG['margin']
    cbar = 2 * D.energy(c, v) / ((1 - margin ** 2) * lam0)
    h = margin * 2 / np.sqrt(N * (N + 2) + 3 * (B.m / B.r) * cbar)
    if kind == 'verlet':                       # the force at a call's end is carried into the next call
        run = lambda c, v, n, a, **kw: ta.verlet(c, v, h, n, B.eig, force, a=a, cbar=cbar, **kw)  # noqa: E731
    else:
        run = lambda c, v, n, a, **kw: ta.strang(c, v, h, n, B.eig, force, cbar=cbar, **kw) + (None,)  # noqa: E731
    c, v, a = run(c, v, 1, None)
    t = time.perf_counter()
    c, v, a = run(c, v, steps, a)
    alone = (time.perf_counter() - t) / steps

    def diagnose(s, c, v):
        D.energy(c, v), D.charges(c, v), D.level_energy(c, v)

    t = time.perf_counter()
    run(c, v, steps, a, observe=diagnose, every=1)
    both = (time.perf_counter() - t) / steps
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)
    print(json.dumps(dict(slot=slot, N=N, kind=kind, cubic=cubic, m=B.m, build=build, h=h, steps=steps, step=alone,
                          step_with_diagnostics=both, hours_T1000=both * 1000 / h / 3600, peak_rss_gb=peak / 1e9)))


def rule(ctx, res):
    P = ctx.P
    split_ok = all(res[c]['by_kind']['strang'] for c in ('c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'))
    rows, runs = [], {}
    for slot in P['rigid']:
        d = ctx.c6[slot]
        ratio = d['tau']['strang'] / d['tau']['verlet']
        R = setup_B(ctx, slot)
        hs = R['h0'] * ratio                  # the splitting's step at Verlet's wall-clock per unit of evolved time
        guard = bool(hs * R['wbar'] < np.pi)
        read = perturbed_run(R, 'strang', hs, int(np.ceil(P['T6'] / hs)), True, P) if guard else None
        runs[slot] = read
        for f in ('2omega', 'radial'):
            ev = d['verlet'][0]['errors'][f]
            es = read['errors'][f] if read is not None and read['read'] else float('nan')
            rows.append(dict(slot=slot, frequency=f, verlet_at_h0=ev, splitting_at_equal_cost=es, tau_ratio=ratio,
                             h0=R['h0'], h_equal_cost=hs, h_wbar_equal_cost=hs * R['wbar'],
                             ok=bool(guard and read is not None and read['read'] and es <= P['quarter'] * ev)))
        ctx.log(f'  {slot}: tau ratio {ratio:.3f}, equal-cost step {hs:.5f}; ' + ', '.join(
            f'{r["frequency"]} {r["splitting_at_equal_cost"]:.2e} against {r["verlet_at_h0"]:.2e}' for r in rows[-2:]))
        ctx.clear()
    adopted = split_ok and all(r['ok'] for r in rows)
    return dict(passed=None, splitting_passed_3_to_9=split_ok, rows=rows, equal_cost_reads=runs,
                production='splitting' if adopted else 'verlet')


def main(dev):
    ctx = Ctx(dev)
    ctx.log(('DEVELOPMENT run, not a control' if dev else 'REGISTERED run') + f', into {os.path.relpath(ctx.out, HERE)}/')
    ctx.log(json.dumps(ctx.env))
    common = dict(env=ctx.env, params=ctx.P, readings=READINGS, rests_on_new_code=NEW_CODE)
    floors = dry(ctx)
    ctx.save('00_dry', dict(control='the dry run: the floors', floors=floors, **common))
    res, stopped, error = {}, None, None
    order = (('c1', c1), ('c2', c2), ('c3', c3), ('c4', c4), ('c5', c5), ('c6', c6), ('c7', c7), ('c8', c8),
             ('c9', c9), ('c10', c10))
    for name, f in order:
        ctx.log(f'control {CID[name]}: {LINES[name]}')
        try:
            r = f(ctx, floors)
        except ta.Ceiling as e:
            r = dict(passed=False, ceiling=str(e))
        except Exception:
            error = dict(control=name, traceback=scrubbed_traceback())
            ctx.log(error['traceback'])
            break
        res[name] = r
        ctx.save(f'{CID[name]:02d}_{name}', dict(control=CID[name], line=LINES[name], result=r, **common))
        ctx.log(f'control {CID[name]}: ' + ('report' if r.get('passed') is None else
                                            ('pass' if r['passed'] else 'FAIL')))
        if name in STOPPING and r.get('passed') is False and r.get('by_kind', {}).get('verlet') is True:
            ctx.log(f'  the splitting alone failed control {CID[name]}: it is disqualified under the rule of section 4, '
                    'and the controls go on with Verlet')
        elif name in STOPPING and r.get('passed') is False:
            if ctx.dev:
                ctx.log('  development run: continuing past a stopping failure, so that every part of the harness runs')
                continue
            stopped = name
            break
    finish(ctx, res, stopped, error, common)


def finish(ctx, res, stopped, error, common):
    """The rule of section 4, control 11 and the summary, after the controls. A run past C-bar in the rule's
    equal-cost runs stops the controls at the rule, as reading 16 says, with 12_rule.json recording it; any other
    failure there is a harness error. Either way control 11 does not run, and the summary is written."""
    if stopped is None and error is None:
        try:
            res['rule'] = rule(ctx, res)
        except ta.Ceiling as e:
            res['rule'] = dict(passed=False, ceiling=str(e))
            stopped = 'rule'
        except Exception:
            error = dict(control='rule', traceback=scrubbed_traceback())
            ctx.log(error['traceback'])
        if 'rule' in res:
            ctx.save('12_rule', dict(control='the rule of section 4', result=res['rule'], **common))
            ctx.log('the rule of section 4: ' + (f'production stepper {res["rule"]["production"]}' if stopped is None
                                                  else f'stopped, {res["rule"]["ceiling"]}'))
    if stopped is None and error is None:
        ctx.log(f'control 11: {LINES["c11"]}')
        try:
            import fecheck
            res['c11'] = dict(passed=None, report=fecheck.run(ctx.P['fe'], ctx.rng('c11', 'R4', ctx.P['fe']['N'], 0),
                                                              ctx.log))
        except BaseException as e:            # a refused pin raises SystemExit: recorded, and the summary still written
            error = dict(control='c11', traceback=scrubbed_traceback(), exception=repr(e)[:500])
            ctx.log(error['traceback'])
            res['c11'] = dict(passed=None, error=error)
        ctx.save('11_c11', dict(control=11, line=LINES['c11'], result=res['c11'], **common))
    summary = dict(stopped_after=stopped, error=error,
                   fft_adopted=bool(res.get('c1', {}).get('passed') and res.get('c2', {}).get('passed')),
                   production=res.get('rule', {}).get('production'),
                   controls={k: (v.get('passed'), v.get('by_kind')) for k, v in res.items()}, **common)
    ctx.save('SUMMARY', summary)
    ctx.log('done: ' + (f'harness error in {error["control"]}' if error else
                        f'stopped after {stopped}' if stopped else 'every control ran'))
    return stopped, error

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'cost':
        a = sys.argv[2:]
        cost_child(a[0], int(a[1]), a[2], a[3], int(a[4]), int(a[5]))
    else:
        main('--dev' in sys.argv[1:])
