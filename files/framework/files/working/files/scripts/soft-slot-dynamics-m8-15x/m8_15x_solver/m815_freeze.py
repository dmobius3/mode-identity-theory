"""The M8.15 freeze bundle (setup only; no target is solved).

  python3 m815_freeze.py orientations     every case's orientation g0, pinned subgroup (2I indices), fibre maps, and seed
                                          Q, at levels 2 and 3 -> out/orientations.json
  python3 m815_freeze.py manifest         SHA-256 of every solver script, the outside-orbit check with its imports, point
                                          copy and output, and the frozen numbers -> out/MANIFEST.json

The guard file out/FROZEN.json, which m815_branch.py requires before any target runs, is written only at the freeze,
after the maintainer's go and with the frozen terms' SHA-256 already on main."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment: one thread, so sums are taken in a fixed order

import sys, os, json, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
SCRIPTS = ['geometry.py', 'irreps.py', 'fem.py', 'nonlinear.py', 'standing.py', 'linearize.py', 'integrate.py',
           'symmetry.py', 'pinned.py', 'continuation.py', 'verdict.py', 'persistence.py', 'm815_common.py',
           'm815_controls.py', 'm815_branch.py', 'm815_freeze.py']
CHECK = os.path.join(HERE, '..', 'm8_15_math', 'outside3_krein.py')
CHECK_OUT = os.path.join(HERE, '..', 'm8_15_math', 'outside3_krein.out')
CHECK_DEPS = ['analyse.py', 'core.py', 'outside3_p.npy']      # the check's imports and its copy of the certified point
CASES = [('C1', 3), ('C2a', 4), ('C2b', 2), ('C3', 4), ('T1', 4), ('T1', 5), ('T2', 4), ('T2', 5), ('T3', 4), ('T3', 5),
         ('T4', 4), ('T4', 5), ('T5', 2)]


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def orientations():
    from fem import Mesh
    from irreps import irreps
    from standing import Standing
    from pinned import PinnedCase
    G, Rs = irreps()
    out = {}
    for level in (2, 3):
        mesh = Mesh(level, nq=3)
        vol = 120 * mesh.vol.sum()
        for name, slot in CASES:
            case = PinnedCase(mesh, Rs, name, slot=slot)
            st = Standing(mesh, case.R, quaternionic=case.quaternionic)
            P = case.seed
            Q = vol * 4 * st.q.energy(P) * 120 / (120 * np.real(np.vdot(P, st.M @ P))) ** 2
            out[f'{name}/R{slot}/L{level}'] = dict(
                g0=[float(x) for x in case.g0], H=[int(h) for h in case.H],
                fibre=[[[float(np.real(a)), float(np.imag(a))], [float(np.real(b)), float(np.imag(b))]] for a, b in case.fib],
                fibre_fit=float(case.fibre_residual), seed_in_fixed_space=float(case.seed_in_fixed),
                fixed_dim=int(case.Br.shape[1]), seed_Q=float(Q),
                generators_cs=[[list(map(float, ax)), int(order)] for ax, order in case.gens_cs])
            print(f'  L{level} {name}/R{slot}: |H| {len(case.H)}, fixed dim {case.Br.shape[1]}, fit {case.fibre_residual:.1e}, seed Q {Q:.7f}', flush=True)
    with open(os.path.join(OUT, 'orientations.json'), 'w') as f:
        json.dump(out, f, indent=1)


def manifest():
    files = {s: sha(os.path.join(HERE, s)) for s in SCRIPTS}
    files['m8_15_math/outside3_krein.py'] = sha(CHECK)
    files['m8_15_math/outside3_krein.out'] = sha(CHECK_OUT)
    for f in CHECK_DEPS:
        files['m8_15_math/' + f] = sha(os.path.join(os.path.dirname(CHECK), f))
    for extra in ('freeze_numbers.json', 'orientations.json'):
        p = os.path.join(OUT, extra)
        if os.path.exists(p):
            files['out/' + extra] = sha(p)
    import platform, scipy
    env = dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
               machine=platform.machine(), processor=platform.processor(),
               threads={k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
                                                      'MKL_NUM_THREADS')})
    try:
        env['numpy_config'] = np.show_config(mode='dicts')
        env['scipy_config'] = scipy.show_config(mode='dicts')
    except TypeError:
        pass
    with open(os.path.join(OUT, 'MANIFEST.json'), 'w') as f:
        json.dump(dict(sha256=files, seed=20261006, arpack_v0_seed=271828, levels=dict(linear=3, dynamics=2),
                       environment=env, determinism='deterministic under the frozen environment'), f, indent=1,
                  default=str)
    print(json.dumps(files, indent=1))


if __name__ == '__main__':
    {'orientations': orientations, 'manifest': manifest}[sys.argv[1]]()
