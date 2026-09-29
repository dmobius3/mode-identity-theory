"""
Compute projections under the "same cone-trace matching" (SCTM) cone condition.
Only the untwisted arm uses SCTM. Under this condition:
  W <= pi/4: psi1 = P_2(sin y) = (3 sin^2 y - 1)/2, eigenvalue 6
  W > pi/4:  psi1 = sgn(cos y)|cos y|^alpha0 sin(pi w/(2W)), eigenvalue alpha0(alpha0+1)
             where alpha0 = pi/(2W)

The HS norms are the same as for other cone conditions (computed in compute_all.py).
Only projections differ.
"""
import numpy as np
import time
import json
from core import (build_2I, all_characters, dim_of_tau, minus1_acts_as_minus,
                  make_placements, band_map, gauss_legendre_points,
                  gegenbauer_C1, gegenbauer_C2, gegenbauer_C3, left_mult_matrix,
                  BLOCKS, phi)

G = build_2I()
CHARS = all_characters(G)
PLACEMENTS = make_placements()
WIDTHS = [0.25, 0.5, 1.0, 1.4]

L_g_all = np.array([left_mult_matrix(G[i]) for i in range(120)])

NY_proj = 30
NW_proj = 12


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


def compute_sctm_proj(tau, n, placement_name, W, dots, g_c, g_d, g_p):
    """Compute projection onto SCTM first positive eigenspace (untwisted arm only)."""
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    is_minus = minus1_acts_as_minus(tau)
    val_arm = 'twisted' if is_minus else 'untwisted'
    trans_arm = 'untwisted' if is_minus else 'twisted'

    y_pr, wy_pr = gauss_legendre_points(NY_proj, 0, np.pi)
    w_pr, ww_pr = gauss_legendre_points(NW_proj, -W, W)

    sigma_pr = np.where(y_pr <= np.pi/2, 1.0, -1.0)
    cosy_pr = np.cos(y_pr)
    siny_pr = np.sin(y_pr)
    cosw_pr = np.cos(w_pr)
    sinw_pr = np.sin(w_pr)

    cc = dots['cc']; cd = dots['cd']; cp = dots['cp']
    dc = dots['dc']; dd = dots['dd']; dp_ = dots['dp']
    pc = dots['pc']; pd = dots['pd']; pp = dots['pp']

    alpha0 = np.pi / (2*W)

    if W <= np.pi/4:
        psi1_y = 0.5 * (3 * siny_pr**2 - 1)
        psi1_w = np.ones_like(w_pr)
        psi1_norm2 = np.sum(psi1_y**2 * np.abs(cosy_pr) * wy_pr) * np.sum(psi1_w**2 * ww_pr)
    else:
        psi1_y = sigma_pr * np.abs(cosy_pr)**alpha0
        psi1_w = np.sin(np.pi * w_pr / (2*W))
        psi1_norm2 = np.sum(psi1_y**2 * np.abs(cosy_pr) * wy_pr) * np.sum(psi1_w**2 * ww_pr)

    results = {}

    for sampler in ['val', 'trans']:
        arm = val_arm if sampler == 'val' else trans_arm
        if arm != 'untwisted':
            results[f'proj_{sampler}_sctm'] = None
            results[f'lambda_{sampler}_sctm'] = None
            continue

        Iw_sum = np.zeros((NY_proj, NY_proj))

        batch_size = 30
        for gb in range(0, 120, batch_size):
            ge = min(gb + batch_size, 120)
            ng = ge - gb

            a00 = np.outer(cosy_pr, cosy_pr)[None,:,:] * cc[gb:ge, None, None]
            a01 = np.outer(cosy_pr, sigma_pr*cosy_pr)[None,:,:] * cd[gb:ge, None, None]
            a02 = np.outer(cosy_pr, siny_pr)[None,:,:] * cp[gb:ge, None, None]
            a10 = np.outer(sigma_pr*cosy_pr, cosy_pr)[None,:,:] * dc[gb:ge, None, None]
            a11 = np.outer(sigma_pr*cosy_pr, sigma_pr*cosy_pr)[None,:,:] * dd[gb:ge, None, None]
            a12 = np.outer(sigma_pr*cosy_pr, siny_pr)[None,:,:] * dp_[gb:ge, None, None]
            a20 = np.outer(siny_pr, cosy_pr)[None,:,:] * pc[gb:ge, None, None]
            a21 = np.outer(siny_pr, sigma_pr*cosy_pr)[None,:,:] * pd[gb:ge, None, None]
            a22 = np.outer(siny_pr, siny_pr)[None,:,:] * pp[gb:ge, None, None]

            ck = cosw_pr[None,None,:,None,None]
            sk = sinw_pr[None,None,:,None,None]
            cl = cosw_pr[None,None,None,None,:]
            sl = sinw_pr[None,None,None,None,:]

            u = (a00[:,:,None,:,None] * ck * cl +
                 a01[:,:,None,:,None] * ck * sl +
                 a02[:,:,None,:,None] * ck +
                 a10[:,:,None,:,None] * sk * cl +
                 a11[:,:,None,:,None] * sk * sl +
                 a12[:,:,None,:,None] * sk +
                 a20[:,:,None,:,None] * cl +
                 a21[:,:,None,:,None] * sl +
                 a22[:,:,None,:,None])

            if sampler == 'val':
                Cn = gegenbauer_C1(n, u)
                # Integrate over w, w' weighted by psi1_w(w) * psi1_w(w')
                weighted_ww1 = ww_pr * psi1_w
                weighted_ww2 = ww_pr * psi1_w
                Iw = np.einsum('gijkl,j,l->gik', Cn, weighted_ww1, weighted_ww2)
                Iw_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw)
            else:
                if n == 0:
                    break
                gP_ik = (cosy_pr[:,None] * cosw_pr[None,:] * g_c[gb:ge, None, None] +
                         sigma_pr[:,None] * cosy_pr[:,None] * sinw_pr[None,:] * g_d[gb:ge, None, None] +
                         siny_pr[:,None] * g_p[gb:ge, None, None])

                Cp = 2 * gegenbauer_C2(n-1, u)
                if n >= 2:
                    Cpp = 8 * gegenbauer_C3(n-2, u)
                else:
                    Cpp = np.zeros_like(u)

                g0_batch = G[gb:ge, 0]
                K00 = (-Cpp * gP_ik[:,:,:,None,None] * gP_ik[:,None,None,:,:] +
                       Cp * g0_batch[:, None, None, None, None])

                weighted_ww1 = ww_pr * psi1_w
                weighted_ww2 = ww_pr * psi1_w
                Iw_t = np.einsum('gijkl,j,l->gik', K00, weighted_ww1, weighted_ww2)
                Iw_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw_t)

        factor_y = psi1_y * np.abs(cosy_pr)
        outer = np.einsum('ij,i,j,i,j->', Iw_sum, factor_y, factor_y, wy_pr, wy_pr)
        proj = prefactor * outer / psi1_norm2

        hs_key = f'hs_{sampler}'
        results[f'proj_{sampler}_sctm'] = proj

    return results


if __name__ == '__main__':
    print("SCTM projection computation")
    print("=" * 70)

    all_results = []

    for pname in ['generic', '2fold', '3fold', '5fold']:
        t_p = time.time()
        dots, g_c, g_d, g_p = precompute_placement(pname)
        print(f"\nPlacement: {pname}")

        for tau, n in BLOCKS + [('1', 0)]:
            is_minus = minus1_acts_as_minus(tau)
            val_arm = 'twisted' if is_minus else 'untwisted'
            trans_arm = 'untwisted' if is_minus else 'twisted'

            has_untwisted = (val_arm == 'untwisted' or trans_arm == 'untwisted')
            if not has_untwisted:
                continue

            for W in WIDTHS:
                t_b = time.time()
                r = compute_sctm_proj(tau, n, pname, W, dots, g_c, g_d, g_p)
                r['tau'] = tau
                r['n'] = n
                r['placement'] = pname
                r['W'] = W
                all_results.append(r)

                if W == WIDTHS[0]:
                    pv = r.get('proj_val_sctm')
                    pt = r.get('proj_trans_sctm')
                    pv_s = f"{pv:.6e}" if pv is not None else "N/A"
                    pt_s = f"{pt:.6e}" if pt is not None else "N/A"
                    print(f"  E^{tau}_{n}: proj_val_sctm={pv_s}, proj_trans_sctm={pt_s} [{time.time()-t_b:.1f}s]")

    for r in all_results:
        for k, v in r.items():
            if isinstance(v, np.floating):
                r[k] = float(v)

    with open('results_sctm.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nTotal SCTM results: {len(all_results)}")
    print("Results saved to results_sctm.json")
