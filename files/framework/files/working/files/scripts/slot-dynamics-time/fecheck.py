"""Control 11 of DESIGN.md section 8: the finite-element cross-check, last and report-only. New code.

M8.15.x's Verlet (its solver frozen at MIT 97a8c088, pinned in FE.sha256) runs from the same initial data as a
Galerkin Verlet run, in R4 at small amplitude, on the mesh level and with the step of M8.15.x's frozen dynamics:
level 2, and R4's step in out/dt_L2.json. Both runs take that step. The data sit on R4's lowest level, where the
frozen record gives the mesh's symmetry lift, s2 in out/freeze_numbers.json. The finite elements keep the phase and
Sp(1) but break right SU(2), so they are not an authority on the Galerkin instrument; the check has no pass line.

The map between the two. Both instruments' sections obey psi(g x) = rho(g) psi(x) under left multiplication, with
the same Hamilton product, but by different copies of 2I in SU(2): they share the 24 elements of the binary tetrahedral
group and are conjugate by the other 24 elements of the binary octahedral group (DEVLOG entry 9). With u the first
such element in a fixed order, u^{-1} G_FE u = G_Galerkin, and psi'(x) = psi(u^{-1} x) obeys psi'(g x) = rho'(g) psi'(x)
for g in G_FE, rho'(g) = rho_Galerkin(u^{-1} g u): checked here at random points. Left translation is an isometry, so
psi' evolves as psi does. The unitary S with S rho'(g) = rho_FE(g) S for all 120 g maps one fibre to the other, and the
finite element's unknowns are the values S psi(u^{-1} x) at one canonical point per node orbit. The finite element integrates over one fundamental domain of
the unit S^3 and the Galerkin norm uses the normalized measure, so Psi^H M Psi should come out near
(2 pi^2 / 120) ||c||^2; the ratio is reported.

Reported at each observation: the relative M-distance between the finite element's state and the P2 interpolant of
the Galerkin state, and each instrument's own charge drift."""
import hashlib
import itertools
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import fftcubic  # noqa: E402  (checks the instrument's pin)
import timearm as ta  # noqa: E402
from instrument import basis, group2i, su2  # noqa: E402

FE_DIR = os.path.realpath(os.path.join(HERE, '..', 'soft-slot-dynamics-m8-15x', 'm8_15x_solver'))
MODULES = ('fem', 'geometry', 'integrate', 'irreps', 'nonlinear', 'standing')
RECORDS = ('out/dt_L2.json', 'out/freeze_numbers.json')


def fe_path():
    """The finite-element folder, after its pin: the six modules this check imports and the two frozen records it
    reads must match FE.sha256, computed from git at 97a8c088, and no package, extension module or other entry of
    the folder may carry a module's name, since Python's importer would take it before the .py file."""
    with open(os.path.join(HERE, 'FE.sha256'), encoding='utf-8') as f:
        rows = [line.split(None, 1) for line in f if line.strip()]
    want = {os.path.join(FE_DIR, m + '.py') for m in MODULES} | {os.path.join(FE_DIR, r) for r in RECORDS}
    got = {}
    for digest, rel in rows:
        path = os.path.realpath(os.path.join(HERE, rel.strip()))
        if path in got:
            raise SystemExit(f'refused: {rel.strip()} is pinned twice')
        got[path] = digest
    if set(got) != want:
        raise SystemExit('refused: FE.sha256 does not pin exactly the six modules and two records this check reads')
    for path, digest in got.items():
        with open(path, 'rb') as g:
            if hashlib.sha256(g.read()).hexdigest() != digest:
                raise SystemExit(f'refused: {os.path.relpath(path, FE_DIR)} differs from its frozen SHA-256')
    for entry in os.listdir(FE_DIR):
        stem = entry.split('.', 1)[0]
        if stem in MODULES and entry != stem + '.py':
            raise SystemExit(f'refused: {entry} in the finite-element folder would shadow {stem}.py')
    return FE_DIR


def m_inner(M, a, b):
    return complex(np.vdot(a, M @ b))


def run(fe, rng, log=print):
    """fe: the frozen parameters (controls.py REG['fe']); rng: the control's generator. Returns the report."""
    d = fe_path()
    if d not in sys.path:
        sys.path.insert(1, d)                 # after this folder, whose module names differ from the six
    import fem, geometry, integrate, irreps, standing  # noqa: E401,E402
    import nonlinear  # noqa: E402
    for mod in (fem, geometry, integrate, irreps, nonlinear, standing):
        if os.path.dirname(os.path.realpath(mod.__file__)) != d:
            raise SystemExit(f'refused: {mod.__name__} was imported from {mod.__file__}, not the pinned folder')

    with open(os.path.join(d, 'out', 'dt_L2.json'), encoding='utf-8') as f:
        dt = float(json.load(f)['R4']['dt'])
    with open(os.path.join(d, 'out', 'freeze_numbers.json'), encoding='utf-8') as f:
        s2 = float(json.load(f)['s2']['R4'])
    log(f'  finite elements: mesh level {fe["level"]}, step {dt} (dt_L2.json), frozen lowest-level lift s2 = {s2:.3e}')
    mesh = fem.Mesh(fe['level'], nq=fe['nq'])
    G, RS = irreps.irreps()
    st = standing.Standing(mesh, RS[4])
    V = integrate.Verlet(st)
    lam_fe = standing.lowest_level(st, 7)

    # u, with u^{-1} G_FE u = G_Galerkin, the first in a fixed order of the binary octahedral group's elements
    key = lambda Q: {tuple(np.round(q, 9) + 0.0) for q in Q}
    qc = lambda q: q * np.array([1.0, -1.0, -1.0, -1.0])
    E = key(group2i.elements())
    cands = [np.array(v, float) / np.sqrt(sum(x * x for x in v)) for v in itertools.product((0, 1, -1), repeat=4)
             if sum(x * x for x in v) in (1, 2)] + [np.array(v) for v in itertools.product((0.5, -0.5), repeat=4)]
    u = next(c for c in cands if key(geometry.qmul(geometry.qmul(np.broadcast_to(qc(c), G.shape), G),
                                                   np.broadcast_to(c, G.shape))) == E)
    ui = np.broadcast_to(qc(u), G.shape)
    # the intertwiner, by averaging over 2I. Each u^{-1} g u is taken as the instrument's exact element it lands on:
    # the computed product sits about 1e-15 off it, and near the poles the instrument's spin matrices turn that into
    # 1e-8 through a square root (DEVLOG entry 9)
    Eg = group2i.elements()
    Gu = Eg[group2i.index_of(Eg, geometry.qmul(geometry.qmul(ui, G), np.broadcast_to(u, G.shape)))]
    Rg = group2i.rep('R4', Gu)
    X0 = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    S = np.einsum('gij,jk,glk->il', RS[4], X0, Rg.conj()) / 120
    gram = S.conj().T @ S
    S = S / np.sqrt(np.trace(gram).real / 3)
    s_unitary = float(np.abs(S.conj().T @ S - np.eye(3)).max())
    s_intertwines = float(max(np.abs(S @ Rg[g] - RS[4][g] @ S).max() for g in range(120)))

    B = basis.Basis('R4', fe['N'])
    X = fftcubic.FFTCubic(B)
    n = np.array([k for k, _, _ in B.index])
    low = n == B.levels[0]
    lam0 = B.levels[0] * (B.levels[0] + 2)

    # the convention: psi(g x) = rho(g) psi(x) with the finite element's own product, at random points
    xs = rng.standard_normal((5, 4))
    xs /= np.linalg.norm(xs, axis=1, keepdims=True)
    ct = rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)
    gx = geometry.qmul(np.repeat(G[None], 5, 0), np.repeat(xs[:, None], 120, 1))           # (5, 120, 4)
    at = lambda x: su2.quat_to_su2(geometry.qmul(np.broadcast_to(qc(u), x.shape), x))       # the point u^{-1} x
    psi_x = B.evaluate(at(xs)) @ ct                                                           # (5, 3)
    psi_gx = (B.evaluate(at(gx.reshape(-1, 4))) @ ct).reshape(5, 120, 3)
    conv = float(np.abs(psi_gx - np.einsum('gij,pj->pgi', Rg, psi_x)).max() / np.abs(psi_x).max())

    # the same initial data: a small state on R4's lowest level, with momenta
    c0 = np.zeros(B.m, complex)
    c0[low] = rng.standard_normal(low.sum()) + 1j * rng.standard_normal(low.sum())
    c0 *= np.sqrt(fe['amp2']) / np.linalg.norm(c0)
    v0 = np.zeros(B.m, complex)
    v0[low] = rng.standard_normal(low.sum()) + 1j * rng.standard_normal(low.sum())
    v0 *= np.sqrt(lam0 * fe['amp2']) / np.linalg.norm(v0)
    Phi = B.evaluate(at(mesh.canon))                                                          # (orbits, 3, m)
    nodal = lambda c: ((Phi @ c) @ S.T).ravel()
    Psi0, Pi0 = nodal(c0), nodal(v0)
    norm_ratio = m_inner(st.M, Psi0, Psi0).real / (2 * np.pi ** 2 / 120 * np.vdot(c0, c0).real)

    K = int(round(fe['T'] / dt))
    every = fe['every']
    H0 = 0.5 * np.vdot(v0, v0).real + 0.5 * np.sum(B.eig * np.abs(c0) ** 2) + X.quartic(c0)
    cbar = 2 * H0 / ((1 - 0.8 ** 2) * lam0)
    gal = [(0, c0.copy(), v0.copy())]
    ta.verlet(c0, v0, dt, K, B.eig, X.cubic, cbar=cbar, every=every,
              observe=lambda s, c, v: gal.append((s, c.copy(), v.copy())))
    _, _, obs = V.run(Psi0, Pi0, dt, K, every, lambda t, P_, Q_: (t, P_.copy(), Q_.copy()))
    assert len(obs) == len(gal)

    scale_fe = np.sqrt(m_inner(st.M, Psi0, Psi0).real * m_inner(st.M, Pi0, Pi0).real)
    scale_g = np.linalg.norm(c0) * np.linalg.norm(v0)
    N_fe0, N_g0 = V.charge(Psi0, Pi0), float(np.imag(np.vdot(c0, v0)))
    rows = []
    for (t, Pf, Qf), (s, cg, vg) in zip(obs, gal):
        Pg = nodal(cg)
        diff = Pf - Pg
        rows.append(dict(t=float(t), distance=float(np.sqrt(m_inner(st.M, diff, diff).real / m_inner(st.M, Pg, Pg).real)),
                         fe_charge_drift=abs(V.charge(Pf, Qf) - N_fe0) / scale_fe,
                         galerkin_charge_drift=abs(float(np.imag(np.vdot(cg, vg))) - N_g0) / scale_g))
    out = dict(mesh_level=fe['level'], nq=fe['nq'], dt=dt, steps=K, galerkin_N=fe['N'], amplitude2=fe['amp2'],
               frozen_lift_s2=s2, fe_lowest_level=dict(eigenvalues=[float(x) for x in lam_fe], exact=float(lam0),
                                                      mean_rel=float(abs(lam_fe.mean() - lam0) / lam0),
                                                      spread=float(lam_fe.max() - lam_fe.min())),
               conjugator_u=u, intertwiner=dict(unitarity=s_unitary, residual=s_intertwines), convention_residual=conv,
               norm_ratio=float(norm_ratio), observations=rows,
               max_distance=max(r['distance'] for r in rows), final_distance=rows[-1]['distance'])
    log(f'  intertwiner residual {s_intertwines:.1e}, convention residual {conv:.1e}, M-norm ratio {norm_ratio:.6f}')
    log(f'  finite-element lowest level: mean {lam_fe.mean():.6f} against {lam0}, spread {lam_fe.max() - lam_fe.min():.2e}')
    log(f'  relative M-distance at t = {rows[-1]["t"]:.2f}: {rows[-1]["distance"]:.3e} (largest {out["max_distance"]:.3e})')
    return out
