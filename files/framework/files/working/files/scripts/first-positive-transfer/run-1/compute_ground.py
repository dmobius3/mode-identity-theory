"""
Compute ground-level projections for per-level tables (§6.2).
Ground eigenfunction:
  Twisted arm Friedrichs: phi0(y) = sgn(cos y), eigenvalue 0
  Untwisted arm Friedrichs/SCTM: 1 (constant), eigenvalue 0
Both constant in w. Norm^2 = 4W.
"""
import numpy as np
import json
import time
from core import (build_2I, all_characters, dim_of_tau, minus1_acts_as_minus,
                  make_placements, gauss_legendre_points,
                  gegenbauer_C1, gegenbauer_C2, gegenbauer_C3, left_mult_matrix,
                  BLOCKS)

G = build_2I()
CHARS = all_characters(G)
PLACEMENTS = make_placements()
WIDTHS = [0.25, 0.5, 1.0, 1.4]
L_g_all = np.array([left_mult_matrix(G[i]) for i in range(120)])
NY = 30
NW = 12


def precompute_placement(placement_name):
    p, c, d = PLACEMENTS[placement_name]
    Lc = np.einsum('gab,b->ga', L_g_all, c)
    Ld = np.einsum('gab,b->ga', L_g_all, d)
    Lp = np.einsum('gab,b->ga', L_g_all, p)
    dots = {
        'cc': np.sum(Lc * c[None, :], axis=1),
        'cd': np.sum(Lc * d[None, :], axis=1),
        'cp': np.sum(Lc * p[None, :], axis=1),
        'dc': np.sum(Ld * c[None, :], axis=1),
        'dd': np.sum(Ld * d[None, :], axis=1),
        'dp': np.sum(Ld * p[None, :], axis=1),
        'pc': np.sum(Lp * c[None, :], axis=1),
        'pd': np.sum(Lp * d[None, :], axis=1),
        'pp': np.sum(Lp * p[None, :], axis=1),
    }
    g_c = np.sum(G[:, 1:] * c[None, 1:], axis=1)
    g_d = np.sum(G[:, 1:] * d[None, 1:], axis=1)
    g_p = np.sum(G[:, 1:] * p[None, 1:], axis=1)
    return dots, g_c, g_d, g_p


def compute_ground(tau, n, W, dots, g_c, g_d, g_p):
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n + 1) / (240 * np.pi**2)

    is_minus = minus1_acts_as_minus(tau)
    val_arm = 'twisted' if is_minus else 'untwisted'
    trans_arm = 'untwisted' if is_minus else 'twisted'

    y_pr, wy_pr = gauss_legendre_points(NY, 0, np.pi)
    w_pr, ww_pr = gauss_legendre_points(NW, -W, W)

    sigma_pr = np.where(y_pr <= np.pi / 2, 1.0, -1.0)
    cosy = np.cos(y_pr)
    siny = np.sin(y_pr)
    cosw = np.cos(w_pr)
    sinw = np.sin(w_pr)

    cc_ = dots['cc']; cd_ = dots['cd']; cp_ = dots['cp']
    dc_ = dots['dc']; dd_ = dots['dd']; dp_ = dots['dp']
    pc_ = dots['pc']; pd_ = dots['pd']; pp_ = dots['pp']

    psi0_norm2 = 4 * W
    results = {}

    for sampler in ['val', 'trans']:
        arm = val_arm if sampler == 'val' else trans_arm
        if arm == 'twisted':
            factor_y = cosy
        else:
            factor_y = np.abs(cosy)

        Iw_sum = np.zeros((NY, NY))

        for gb in range(0, 120, 30):
            ge = min(gb + 30, 120)

            a00 = np.outer(cosy, cosy)[None, :, :] * cc_[gb:ge, None, None]
            a01 = np.outer(cosy, sigma_pr * cosy)[None, :, :] * cd_[gb:ge, None, None]
            a02 = np.outer(cosy, siny)[None, :, :] * cp_[gb:ge, None, None]
            a10 = np.outer(sigma_pr * cosy, cosy)[None, :, :] * dc_[gb:ge, None, None]
            a11 = np.outer(sigma_pr * cosy, sigma_pr * cosy)[None, :, :] * dd_[gb:ge, None, None]
            a12 = np.outer(sigma_pr * cosy, siny)[None, :, :] * dp_[gb:ge, None, None]
            a20 = np.outer(siny, cosy)[None, :, :] * pc_[gb:ge, None, None]
            a21 = np.outer(siny, sigma_pr * cosy)[None, :, :] * pd_[gb:ge, None, None]
            a22 = np.outer(siny, siny)[None, :, :] * pp_[gb:ge, None, None]

            ck = cosw[None, None, :, None, None]
            sk = sinw[None, None, :, None, None]
            cl = cosw[None, None, None, None, :]
            sl = sinw[None, None, None, None, :]

            u = (a00[:, :, None, :, None] * ck * cl +
                 a01[:, :, None, :, None] * ck * sl +
                 a02[:, :, None, :, None] * ck +
                 a10[:, :, None, :, None] * sk * cl +
                 a11[:, :, None, :, None] * sk * sl +
                 a12[:, :, None, :, None] * sk +
                 a20[:, :, None, :, None] * cl +
                 a21[:, :, None, :, None] * sl +
                 a22[:, :, None, :, None])

            if sampler == 'val':
                Cn = gegenbauer_C1(n, u)
                Iw = np.einsum('gijkl,j,l->gik', Cn, ww_pr, ww_pr)
                Iw_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw)
            else:
                if n == 0:
                    results[f'proj0_{sampler}'] = 0.0
                    break
                gP_ik = (cosy[:, None] * cosw[None, :] * g_c[gb:ge, None, None] +
                         sigma_pr[:, None] * cosy[:, None] * sinw[None, :] * g_d[gb:ge, None, None] +
                         siny[:, None] * g_p[gb:ge, None, None])

                Cp = 2 * gegenbauer_C2(n - 1, u)
                Cpp = 8 * gegenbauer_C3(n - 2, u) if n >= 2 else np.zeros_like(u)

                g0_batch = G[gb:ge, 0]
                K00 = (-Cpp * gP_ik[:, :, :, None, None] * gP_ik[:, None, None, :, :] +
                       Cp * g0_batch[:, None, None, None, None])

                Iw_t = np.einsum('gijkl,j,l->gik', K00, ww_pr, ww_pr)
                Iw_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw_t)

        if f'proj0_{sampler}' not in results:
            outer = np.einsum('ij,i,j,i,j->', Iw_sum, factor_y, factor_y, wy_pr, wy_pr)
            results[f'proj0_{sampler}'] = prefactor * outer / psi0_norm2

    return results


if __name__ == '__main__':
    print("Ground-level projection computation")
    print("=" * 70)

    all_results = []
    t_total = time.time()

    for pname in ['generic', '2fold', '3fold', '5fold']:
        dots, g_c, g_d, g_p = precompute_placement(pname)
        print(f"\nPlacement: {pname}")

        for tau, n in BLOCKS + [('1', 0)]:
            for W in WIDTHS:
                r = compute_ground(tau, n, W, dots, g_c, g_d, g_p)
                r['tau'] = tau
                r['n'] = n
                r['placement'] = pname
                r['W'] = W
                all_results.append(r)

            pv = r.get('proj0_val', 0)
            pt = r.get('proj0_trans', 0)
            print(f"  E^{tau}_{n}: proj0_val={pv:.6e}, proj0_trans={pt:.6e}")

    for r in all_results:
        for k, v in r.items():
            if isinstance(v, np.floating):
                r[k] = float(v)

    with open('results_ground.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nTotal: {len(all_results)} results in {time.time()-t_total:.1f}s")
    print("Saved to results_ground.json")
