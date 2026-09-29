"""
Optimized computation of ‖O|‖², ‖P₁O|‖², Λ for all blocks.
Uses reduced quadrature for 4D projection integrals.
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

# Pre-compute L_g matrices
L_g_all = np.array([left_mult_matrix(G[i]) for i in range(120)])  # (120, 4, 4)

# Quadrature for HS norm (2D)
NY_hs = 60
NW_hs = 40

# Quadrature for projection (4D) — reduced for speed
NY_proj = 30
NW_proj = 12


def precompute_placement(placement_name):
    """Precompute dot-product coefficients for a placement (independent of W)."""
    p, c, d = PLACEMENTS[placement_name]

    Lc = np.einsum('gab,b->ga', L_g_all, c)   # (120, 4)
    Ld = np.einsum('gab,b->ga', L_g_all, d)
    Lp = np.einsum('gab,b->ga', L_g_all, p)

    # 9 dot products per g
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

    # For transverse sampler: ⟨g, P⟩ = g·(R³ components of P)
    g_c = np.sum(G[:, 1:] * c[None, 1:], axis=1)
    g_d = np.sum(G[:, 1:] * d[None, 1:], axis=1)
    g_p = np.sum(G[:, 1:] * p[None, 1:], axis=1)

    return dots, g_c, g_d, g_p


def compute_u_4d(dots, y_nodes_1, w_nodes_1, y_nodes_2, w_nodes_2):
    """Compute inner product u(g, y, w, y', w') = ⟨gP(y,w), P(y',w')⟩.
    Returns: (120, NY1, NW1, NY2, NW2) or processes in batches.
    """
    sigma1 = np.where(y_nodes_1 <= np.pi/2, 1.0, -1.0)
    sigma2 = np.where(y_nodes_2 <= np.pi/2, 1.0, -1.0)
    cosy1 = np.cos(y_nodes_1)
    siny1 = np.sin(y_nodes_1)
    cosy2 = np.cos(y_nodes_2)
    siny2 = np.sin(y_nodes_2)
    cosw1 = np.cos(w_nodes_1)
    sinw1 = np.sin(w_nodes_1)
    cosw2 = np.cos(w_nodes_2)
    sinw2 = np.sin(w_nodes_2)

    NY1, NW1, NY2, NW2 = len(y_nodes_1), len(w_nodes_1), len(y_nodes_2), len(w_nodes_2)

    # Build coefficient arrays
    # a_{mr}(g, i, j) where m,r ∈ {0,1,2} for (cosw, sinw, 1)
    # u(g,i,k,j,l) = Σ_{mr} a_{mr}(g,i,j) f_m(w_k) f_r(w'_l)

    # a00[g,i,j] = cosy_i * cosy_j * dots['cc'][g]
    # etc.

    cc = dots['cc']  # (120,)
    cd = dots['cd']
    cp = dots['cp']
    dc = dots['dc']
    dd = dots['dd']
    dp = dots['dp']
    pc = dots['pc']
    pd = dots['pd']
    pp = dots['pp']

    # Compute u for all g at once — memory: 120 * NY1 * NW1 * NY2 * NW2
    # For (50, 20, 50, 20): 120 * 50 * 20 * 50 * 20 = 120M entries → ~960 MB
    # Process in batches of g

    batch_size = 10  # process 10 g values at a time
    u_all = np.zeros((120, NY1, NW1, NY2, NW2))

    for gb in range(0, 120, batch_size):
        ge = min(gb + batch_size, 120)
        ng = ge - gb

        # Shape: (ng, NY1, NY2)
        a00 = np.outer(cosy1, cosy2)[None,:,:] * cc[gb:ge, None, None]
        a01 = np.outer(cosy1, sigma2*cosy2)[None,:,:] * cd[gb:ge, None, None]
        a02 = np.outer(cosy1, siny2)[None,:,:] * cp[gb:ge, None, None]
        a10 = np.outer(sigma1*cosy1, cosy2)[None,:,:] * dc[gb:ge, None, None]
        a11 = np.outer(sigma1*cosy1, sigma2*cosy2)[None,:,:] * dd[gb:ge, None, None]
        a12 = np.outer(sigma1*cosy1, siny2)[None,:,:] * dp[gb:ge, None, None]
        a20 = np.outer(siny1, cosy2)[None,:,:] * pc[gb:ge, None, None]
        a21 = np.outer(siny1, sigma2*cosy2)[None,:,:] * pd[gb:ge, None, None]
        a22 = np.outer(siny1, siny2)[None,:,:] * pp[gb:ge, None, None]

        # u = a00*ck*cl + a01*ck*sl + a02*ck + a10*sk*cl + a11*sk*sl + a12*sk
        #   + a20*cl + a21*sl + a22
        # Shape: (ng, NY1, NW1, NY2, NW2)
        u_all[gb:ge] = (
            a00[:,:,None,:,None] * cosw1[None,None,:,None,None] * cosw2[None,None,None,None,:] +
            a01[:,:,None,:,None] * cosw1[None,None,:,None,None] * sinw2[None,None,None,None,:] +
            a02[:,:,None,:,None] * cosw1[None,None,:,None,None] +
            a10[:,:,None,:,None] * sinw1[None,None,:,None,None] * cosw2[None,None,None,None,:] +
            a11[:,:,None,:,None] * sinw1[None,None,:,None,None] * sinw2[None,None,None,None,:] +
            a12[:,:,None,:,None] * sinw1[None,None,:,None,None] +
            a20[:,:,None,:,None] * cosw2[None,None,None,None,:] +
            a21[:,:,None,:,None] * sinw2[None,None,None,None,:] +
            a22[:,:,None,:,None]
        )

    return u_all


def compute_block(tau, n, placement_name, W, dots, g_c, g_d, g_p):
    """Compute all quantities for one block at one placement and width.
    Returns dict with hs_val, hs_trans, proj_val, proj_trans, lambda_val, lambda_trans.
    """
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    is_minus = minus1_acts_as_minus(tau)
    # Value sampler arm: twisted if -1 acts as -id
    val_arm = 'twisted' if is_minus else 'untwisted'
    # Transverse sampler arm: opposite
    trans_arm = 'untwisted' if is_minus else 'twisted'

    psi1_norm2 = 4*W/3

    # ===== HS NORMS (2D integrals) =====
    p, c, d = PLACEMENTS[placement_name]

    y_hs, wy_hs = gauss_legendre_points(NY_hs, 0, np.pi)
    w_hs, ww_hs = gauss_legendre_points(NW_hs, -W, W)
    Y_hs, W_hs = np.meshgrid(y_hs, w_hs, indexing='ij')
    P_hs = band_map(Y_hs, W_hs, p, c, d)  # (NY_hs, NW_hs, 4)

    # gP = L_g @ P, dot product = gP · P
    gP = np.einsum('gij,abj->gabi', L_g_all, P_hs)  # (120, NY_hs, NW_hs, 4)
    gP_dot_P = np.einsum('gabi,abi->gab', gP, P_hs)  # (120, NY_hs, NW_hs)

    measure_hs = np.abs(np.cos(Y_hs))  # (NY_hs, NW_hs)
    wy2d = np.outer(wy_hs, ww_hs)  # (NY_hs, NW_hs)

    # Value sampler HS norm
    Cn_diag = gegenbauer_C1(n, gP_dot_P)
    K_diag = prefactor * np.einsum('g,gij->ij', chi, Cn_diag)
    hs_val = np.sum(K_diag * measure_hs * wy2d)

    # Transverse sampler HS norm
    if n == 0:
        hs_trans = 0.0
    else:
        g_dot_P = np.einsum('gi,abi->gab', G, P_hs)  # (120, NY_hs, NW_hs)
        g0 = G[:, 0]

        Cp_diag = 2 * gegenbauer_C2(n-1, gP_dot_P)
        if n >= 2:
            Cpp_diag = 8 * gegenbauer_C3(n-2, gP_dot_P)
        else:
            Cpp_diag = np.zeros_like(gP_dot_P)

        K00_diag = prefactor * np.einsum('g,gij->ij', chi,
            -Cpp_diag * g_dot_P**2 + Cp_diag * g0[:, None, None])
        hs_trans = np.sum(K00_diag * measure_hs * wy2d)

    # ===== PROJECTIONS (4D integrals) =====
    y_pr, wy_pr = gauss_legendre_points(NY_proj, 0, np.pi)
    w_pr, ww_pr = gauss_legendre_points(NW_proj, -W, W)

    sigma_pr = np.where(y_pr <= np.pi/2, 1.0, -1.0)
    cosy_pr = np.cos(y_pr)
    siny_pr = np.sin(y_pr)
    cosw_pr = np.cos(w_pr)
    sinw_pr = np.sin(w_pr)

    # Value sampler projection
    # Process g in batches to avoid memory issues
    Iw_val_sum = np.zeros((NY_proj, NY_proj))
    Iw_trans_sum = np.zeros((NY_proj, NY_proj))

    cc = dots['cc']; cd = dots['cd']; cp = dots['cp']
    dc = dots['dc']; dd = dots['dd']; dp_ = dots['dp']
    pc = dots['pc']; pd = dots['pd']; pp = dots['pp']

    batch_size = 30  # g values per batch
    for gb in range(0, 120, batch_size):
        ge = min(gb + batch_size, 120)
        ng = ge - gb

        # Build 9 coefficient arrays: (ng, NY, NY)
        a00 = np.outer(cosy_pr, cosy_pr)[None,:,:] * cc[gb:ge, None, None]
        a01 = np.outer(cosy_pr, sigma_pr*cosy_pr)[None,:,:] * cd[gb:ge, None, None]
        a02 = np.outer(cosy_pr, siny_pr)[None,:,:] * cp[gb:ge, None, None]
        a10 = np.outer(sigma_pr*cosy_pr, cosy_pr)[None,:,:] * dc[gb:ge, None, None]
        a11 = np.outer(sigma_pr*cosy_pr, sigma_pr*cosy_pr)[None,:,:] * dd[gb:ge, None, None]
        a12 = np.outer(sigma_pr*cosy_pr, siny_pr)[None,:,:] * dp_[gb:ge, None, None]
        a20 = np.outer(siny_pr, cosy_pr)[None,:,:] * pc[gb:ge, None, None]
        a21 = np.outer(siny_pr, sigma_pr*cosy_pr)[None,:,:] * pd[gb:ge, None, None]
        a22 = np.outer(siny_pr, siny_pr)[None,:,:] * pp[gb:ge, None, None]

        # u: (ng, NY, NW, NY, NW)
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

        # Value sampler: C_n^1(u)
        Cn = gegenbauer_C1(n, u)  # (ng, NY, NW, NY, NW)

        # Integrate over w, w'
        Iw = np.einsum('gijkl,j,l->gik', Cn, ww_pr, ww_pr)  # (ng, NY, NY)
        Iw_val_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw)

        # Transverse sampler projection
        if n > 0:
            # ⟨g, P(y,w)⟩ for each g in batch
            gP_ik = (cosy_pr[:,None] * cosw_pr[None,:] * g_c[gb:ge, None, None] +
                     sigma_pr[:,None] * cosy_pr[:,None] * sinw_pr[None,:] * g_d[gb:ge, None, None] +
                     siny_pr[:,None] * g_p[gb:ge, None, None])  # (ng, NY, NW)
            gP_jl = gP_ik  # same formula, will broadcast

            Cp = 2 * gegenbauer_C2(n-1, u)
            if n >= 2:
                Cpp = 8 * gegenbauer_C3(n-2, u)
            else:
                Cpp = np.zeros_like(u)

            g0_batch = G[gb:ge, 0]
            K00 = (-Cpp * gP_ik[:,:,:,None,None] * gP_jl[:,None,None,:,:] +
                   Cp * g0_batch[:, None, None, None, None])

            Iw_t = np.einsum('gijkl,j,l->gik', K00, ww_pr, ww_pr)
            Iw_trans_sum += np.einsum('g,gij->ij', chi[gb:ge], Iw_t)

    # Value sampler projection
    if val_arm == 'twisted':
        factor_y = siny_pr * np.abs(cosy_pr)
    else:
        factor_y = siny_pr * cosy_pr

    outer_val = np.einsum('ij,i,j,i,j->', Iw_val_sum, factor_y, factor_y,
                          wy_pr, wy_pr)
    proj_val = prefactor * outer_val / psi1_norm2

    # Transverse sampler projection
    if n == 0:
        proj_trans = 0.0
    else:
        if trans_arm == 'twisted':
            factor_y_t = siny_pr * np.abs(cosy_pr)
        else:
            factor_y_t = siny_pr * cosy_pr

        outer_trans = np.einsum('ij,i,j,i,j->', Iw_trans_sum, factor_y_t, factor_y_t,
                               wy_pr, wy_pr)
        proj_trans = prefactor * outer_trans / psi1_norm2

    lambda_val = hs_val - proj_val
    lambda_trans = hs_trans - proj_trans

    return {
        'tau': tau, 'n': n, 'placement': placement_name, 'W': W,
        'val_arm': val_arm, 'trans_arm': trans_arm,
        'hs_val': hs_val, 'hs_trans': hs_trans,
        'proj_val': proj_val, 'proj_trans': proj_trans,
        'lambda_val': lambda_val, 'lambda_trans': lambda_trans,
    }


if __name__ == '__main__':
    # Quick validation
    print("=" * 80)
    print("Validation: E^2_1, generic, W=1")
    t0 = time.time()
    dots, g_c, g_d, g_p = precompute_placement('generic')
    r = compute_block('2', 1, 'generic', 1.0, dots, g_c, g_d, g_p)
    print(f"  hs_val = {r['hs_val']:.10f} (expect {8/np.pi**2:.10f})")
    print(f"  hs_trans = {r['hs_trans']:.10f} (expect {8/np.pi**2:.10f})")
    print(f"  proj_val = {r['proj_val']:.10f} (expect {8/(3*np.pi**2):.10f})")
    print(f"  proj_trans = {r['proj_trans']:.10f} (expect 0)")
    print(f"  lambda_val = {r['lambda_val']:.10f} (expect {16/(3*np.pi**2):.10f})")
    print(f"  Time: {time.time()-t0:.1f}s")

    # Full computation
    print("\n" + "=" * 80)
    print("Full computation")
    print("=" * 80)

    all_results = []

    for pname in ['generic', '2fold', '3fold', '5fold']:
        t_p = time.time()
        dots, g_c, g_d, g_p = precompute_placement(pname)
        print(f"\nPlacement: {pname} (precompute: {time.time()-t_p:.1f}s)")

        for tau, n in BLOCKS + [('1', 0)]:
            for W in WIDTHS:
                t_b = time.time()
                r = compute_block(tau, n, pname, W, dots, g_c, g_d, g_p)
                all_results.append(r)
                elapsed = time.time() - t_b

                if W == WIDTHS[0]:  # print once per block per placement
                    print(f"  E^{tau}_{n}, W={W}: "
                          f"hs_v={r['hs_val']:.6e}, proj_v={r['proj_val']:.6e}, Λ_v={r['lambda_val']:.6e} | "
                          f"hs_t={r['hs_trans']:.6e}, proj_t={r['proj_trans']:.6e}, Λ_t={r['lambda_trans']:.6e} "
                          f"[{elapsed:.1f}s]")

    # Save results
    # Convert to serializable format
    for r in all_results:
        for k, v in r.items():
            if isinstance(v, np.floating):
                r[k] = float(v)

    with open('results.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nTotal results: {len(all_results)}")
    print("Results saved to results.json")
