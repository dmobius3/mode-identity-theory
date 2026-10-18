#!/usr/bin/env python3
"""The units' counterexamples to section 7's typing (UA, UB, 2026-10-15, night), reproduced on the package as it stood
at DEVLOG 38, before any fix. Case: synthetic. It records what record() returned against what the units reported.

  UA: the collision block alone, L = diag(-1, -2) at omega^2 = omega*^2 - 1e-13, omega*^2 = (3 + 2 sqrt2)/4, where
      the pair is a quartet with real parts about 3.16e-7.
  UB c1: DL claim 4's system at omega^2 = omega*^2 - delta, with the quartet's real part 3e-6 and then 6e-6.
  UB c2: the same at real part 1.2e-5, where the quartet's two members fall in separate groups.
The collision block's quartet is computed exactly, at 50 digits, from s^4 + (4 omega^2 - 3) s^2 + 2 = 0.
"""
import os
import sys
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import linear as ln, devtools  # noqa: E402

devtools.require('synthetic')
mp.mp.dps = 50
rng = np.random.default_rng(20261019)
out = []
U = np.finfo(float).eps
KAPPAS = [0.5, 1.0, 3.0, 10.0, 100.0, 700.0, 1700.0, -3.0]
REAL_PAIR = np.diag([-5.0, 3.0])
COLL = np.diag([-1.0, -2.0])
W2 = (mp.mpf(3) + 2 * mp.sqrt(2)) / 4
TAU = 2 ** 0.25


def say(s):
    print(s)
    out.append(s)


def place(blocks):
    m = len(blocks)
    L = np.zeros((2 * m, 2 * m))
    for j, b in enumerate(blocks):
        idx = [j, m + j]
        L[np.ix_(idx, idx)] = b
    return L


def random_unitary_real(m):
    Z = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    Q, R = np.linalg.qr(Z)
    Q = Q * (np.diag(R) / np.abs(np.diag(R)))
    return np.block([[Q.real, -Q.imag], [Q.imag, Q.real]])


def margin_for(A):
    return 30.0 * np.sqrt(U * np.linalg.norm(A, 2))


def exact_re(w2):
    """The largest |Re s| of the collision block's eigenvalues at omega^2 = w2, at 50 digits."""
    b = 4 * w2 - 3
    disc = mp.sqrt(mp.mpc(b * b - 8))
    return max(abs(mp.re(mp.sqrt((-b + sg * disc) / 2))) for sg in (1, -1))


def collision_view(A, B, W, L, r):
    groups = [g for g in r['imag_groups'] if abs(g[0].imag - TAU) < 1e-3]
    lam, V = np.linalg.eig(A)
    near = np.where(np.abs(lam - 1j * TAU) < 1e-3)[0]
    forms = []
    for i in near:
        v = V[:, i] / np.linalg.norm(V[:, i])
        forms.append(float(np.real(v.conj() @ B @ v)))
    return groups, lam[near], forms


def run_block(w2):
    A, B, W = ln.first_order(COLL, float(mp.sqrt(w2)))
    r = ln.record(A, B, W, COLL, margin_for(A))
    return r, collision_view(A, B, W, COLL, r)


def run_claim4_system(w2):
    omega = float(mp.sqrt(w2))
    blocks = [np.diag([0.0, k]) for k in (5.0, -2.0)] + [np.diag([k, k]) for k in KAPPAS] + [REAL_PAIR, COLL]
    R = random_unitary_real(len(blocks))
    L = R.T @ place(blocks) @ R
    A, B, W = ln.first_order(L, omega)
    r = ln.record(A, B, W, L, margin_for(A))
    return r, collision_view(A, B, W, L, r)


def main():
    verdicts = []
    # UA
    w2 = W2 - mp.mpf('1e-13')
    r, (groups, lam, forms) = run_block(w2)
    re = float(exact_re(w2))
    ok = abs(re - 3.16e-7) < 0.01 * 3.16e-7 and r['kc'] == 0 and r['ki'] == 1 and r['K'] == 2 and not r['unresolved']
    verdicts.append(('UA', ok))
    say(f"UA, the block alone at omega^2 = omega*^2 - 1e-13: exact |Re s| {re:.3e}; margin {r['margin']:.1e};"
        f" groups at i 2^(1/4): {[(round(g[0].imag, 9), g[1], g[2], g[3]) for g in groups]};"
        f" (k_r, k_c, k_i) = ({r['kr']}, {r['kc']}, {r['ki']}), K {r['K']}, unresolved {r['unresolved']}:"
        f" {'reproduced' if ok else 'NOT reproduced'}")
    # UB c1
    for target in (3e-6, 6e-6):
        w2 = W2 - mp.mpf(target) ** 2
        r, (groups, lam, forms) = run_claim4_system(w2)
        re = float(exact_re(w2))
        ok = (len(groups) == 1 and groups[0][1] == 2 and groups[0][2] == 1 and r['K'] == 5 and not r['unresolved'])
        verdicts.append((f'UB c1 at {target:.0e}', ok))
        say(f"UB c1, claim 4's system with the quartet's real part {target:.0e} (exact {re:.3e}): margin {r['margin']:.1e};"
            f" computed |Re| {np.abs(lam.real).max():.2e}; groups at i 2^(1/4): {[(g[1], g[2], g[3]) for g in groups]};"
            f" K {r['K']}, unresolved {r['unresolved']}: {'reproduced' if ok else 'NOT reproduced'}")
    # UB c2
    target = 1.2e-5
    w2 = W2 - mp.mpf(target) ** 2
    r, (groups, lam, forms) = run_claim4_system(w2)
    re = float(exact_re(w2))
    ok = (len(groups) == 2 and all(g[1] == 1 for g in groups) and not r['unresolved']
          and max(abs(f) for f in forms) < 1e-8)
    verdicts.append(('UB c2', ok))
    say(f"UB c2, real part {target:.1e} (exact {re:.3e}): computed {np.round(lam, 9)}; groups typed imaginary:"
        f" {[(g[1], g[2], g[3]) for g in groups]}; their Krein forms on unit eigenvectors {[f'{f:+.1e}' for f in forms]};"
        f" K {r['K']}, unresolved {r['unresolved']}: {'reproduced' if ok else 'NOT reproduced'}")
    n_rep = sum(ok for _, ok in verdicts)
    say(f"{n_rep} of {len(verdicts)} findings reproduced")
    path = os.path.join(HERE, 'units_findings_r4.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"The units' counterexamples to §7's typing, on the package before any fix: {n_rep} of {len(verdicts)}"
                      f" reproduced ({', '.join(k + (': yes' if v else ': no') for k, v in verdicts)}). Nothing is scored; the"
                      ' run records the defect before the fix.'], outputs=(path,))


if __name__ == '__main__':
    main()
