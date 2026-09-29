"""
Compute ‖O|‖², ‖P₁O|‖², and Λ for all blocks using the reproducing kernel method.

Key formulas:
  K_E(q,q') = (dim(τ)(n+1))/(240π²) Σ_g χ_τ(g) C_n^1(⟨gq,q'⟩)
  ‖O⁽⁰⁾|‖² = ∫∫ K_E(P,P) |cos y| dw dy
  ‖P₁O⁽⁰⁾|‖² = (1/‖ψ₁‖²) ∫∫∫∫ K_E(P,P') ψ₁(y)ψ₁(y') |cos y||cos y'| dw dy dw' dy'

For transverse sampler:
  K^{00}_E(q,q') = ∂²/∂x₀∂x'₀ K_E = C·Σ_g χ_τ(g)[C''·⟨g,q'⟩·Re(gq) + C'·Re(g)]
  On S² (x₀=0): Re(gq) = -⟨g,q⟩, so:
  K^{00}_E(q,q') = C·Σ_g χ_τ(g)[-C''·⟨g,q⟩·⟨g,q'⟩ + C'·g₀]
  where C'=dC_n^1/dx, C''=d²C_n^1/dx².
"""
import numpy as np
from core import (build_2I, all_characters, dim_of_tau, minus1_acts_as_minus,
                  make_placements, band_map, gauss_legendre_points,
                  gegenbauer_C1, gegenbauer_C2, gegenbauer_C3, left_mult_matrix,
                  BLOCKS, phi)

# ========== Setup ==========
G = build_2I()
CHARS = all_characters(G)
PLACEMENTS = make_placements()
WIDTHS = [0.25, 0.5, 1.0, 1.4]

# Quadrature settings
NY = 80   # points for y integration
NW = 60   # points for w integration

# ========== Helper functions ==========

def compute_gP_dot_P(g_matrices, P_yw):
    """Compute ⟨gP(y,w), P(y,w)⟩ for all g and all (y,w) points.
    g_matrices: (120, 4, 4) - left multiplication matrices
    P_yw: (..., 4) - band map values
    Returns: (120, ...) array
    """
    # gP = L_g @ P for each g: (120, ..., 4)
    gP = np.einsum('gij,...j->g...i', g_matrices, P_yw)
    # dot product: ⟨gP, P⟩ = sum over last axis
    return np.einsum('g...i,...i->g...', gP, P_yw)

def compute_g_dot_P(G_elts, P_yw):
    """Compute ⟨g, P⟩ = g₁P₁+g₂P₂+g₃P₃ for P on S² (x₀=0).
    G_elts: (120, 4)
    P_yw: (..., 4)
    Returns: (120, ...)
    """
    return np.einsum('gi,...i->g...', G_elts, P_yw)

def hs_norm_value_sampler(tau, n, placement_name, W):
    """Compute ‖O⁽⁰⁾|_E‖² for value sampler."""
    p, c, d = PLACEMENTS[placement_name]
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    y_nodes, y_weights = gauss_legendre_points(NY, 0, np.pi)
    w_nodes, w_weights = gauss_legendre_points(NW, -W, W)

    Y, Ww = np.meshgrid(y_nodes, w_nodes, indexing='ij')
    wy, ww = np.meshgrid(y_weights, w_weights, indexing='ij')

    P_yw = band_map(Y, Ww, p, c, d)  # (NY, NW, 4)

    # Build L_g matrices
    L_g = np.array([left_mult_matrix(G[i]) for i in range(120)])  # (120, 4, 4)

    # ⟨gP, P⟩ for each g and each (y,w)
    gP_dot_P = compute_gP_dot_P(L_g, P_yw)  # (120, NY, NW)

    # C_n^1(⟨gP,P⟩)
    Cn = gegenbauer_C1(n, gP_dot_P)  # (120, NY, NW)

    # K_E(P,P) = prefactor * Σ_g χ_τ(g) C_n^1(⟨gP,P⟩)
    K_diag = prefactor * np.einsum('g,gij->ij', chi, Cn)  # (NY, NW)

    # ‖O⁽⁰⁾|‖² = ∫∫ K_E(P,P) |cos y| dw dy
    measure = np.abs(np.cos(Y))  # |cos y|
    integrand = K_diag * measure
    result = np.sum(integrand * wy * ww)

    return result

def hs_norm_transverse_sampler(tau, n, placement_name, W):
    """Compute ‖O⁽¹⁾|_E‖² for transverse sampler."""
    if n == 0:
        return 0.0  # derivative of constant is 0

    p, c, d = PLACEMENTS[placement_name]
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    y_nodes, y_weights = gauss_legendre_points(NY, 0, np.pi)
    w_nodes, w_weights = gauss_legendre_points(NW, -W, W)

    Y, Ww = np.meshgrid(y_nodes, w_nodes, indexing='ij')
    wy, ww = np.meshgrid(y_weights, w_weights, indexing='ij')

    P_yw = band_map(Y, Ww, p, c, d)  # (NY, NW, 4)

    L_g = np.array([left_mult_matrix(G[i]) for i in range(120)])

    gP_dot_P = compute_gP_dot_P(L_g, P_yw)  # (120, NY, NW)
    g_dot_P = compute_g_dot_P(G, P_yw)       # (120, NY, NW)
    g0 = G[:, 0]                               # (120,)

    # Derivatives of C_n^1:
    # C_n^{1'}(x) = 2 C_{n-1}^2(x)
    # C_n^{1''}(x) = 8 C_{n-2}^3(x)
    Cp = 2 * gegenbauer_C2(n-1, gP_dot_P)  # (120, NY, NW)
    if n >= 2:
        Cpp = 8 * gegenbauer_C3(n-2, gP_dot_P)
    else:
        Cpp = np.zeros_like(gP_dot_P)

    # On S²: Re(gP) = -⟨g,P⟩
    # K^{00}_E = prefactor * Σ_g χ_τ(g) [-C''·⟨g,P⟩² + C'·g₀]
    # (using ⟨g,P⟩·(-⟨g,P⟩) = -⟨g,P⟩² and the other term is C'·g₀)

    K00 = prefactor * np.einsum('g,gij->ij', chi,
        -Cpp * g_dot_P**2 + Cp * g0[:, None, None])

    measure = np.abs(np.cos(Y))
    result = np.sum(K00 * measure * wy * ww)

    return result

def projection_value_sampler(tau, n, placement_name, W, arm='twisted'):
    """Compute ‖P₁O⁽⁰⁾|_E‖² for value sampler.
    arm: 'twisted' -> ψ₁ = sin(y), 'untwisted' -> ψ₁ = φ₀·sin(y)
    """
    p, c, d = PLACEMENTS[placement_name]
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    y_nodes, y_weights = gauss_legendre_points(NY, 0, np.pi)
    w_nodes, w_weights = gauss_legendre_points(NW, -W, W)

    # ψ₁ norm² = 4W/3
    psi1_norm2 = 4*W/3

    # For the 4D integral, I'll compute it as:
    # Σ_g χ_τ(g) ∫∫ sin(y)sin(y')|cos y||cos y'| [∫∫ C_n^1(⟨gP(y,w),P(y',w')⟩) dw dw'] dy dy'
    #
    # Strategy: for each pair (y_i, y_j), compute the double w-integral.

    L_g = np.array([left_mult_matrix(G[i]) for i in range(120)])

    # Create grid points
    # P at y_i, w_k: (NY, NW, 4)
    Y1, W1 = np.meshgrid(y_nodes, w_nodes, indexing='ij')
    P1 = band_map(Y1, W1, p, c, d)

    # For each y_i and y_j, I need ∫∫ C_n^1(⟨gP(y_i,w), P(y_j,w')⟩) dw dw'
    # This is a (120, NY, NY) array after w-integration.

    # gP1: (120, NY, NW, 4)
    gP1 = np.einsum('gab,ijb->gija', L_g, P1)

    # For each pair of y indices (i,j), compute:
    # ⟨gP1[g,i,k,:], P1[j,l,:]⟩ = gP1[g,i,k,:] · P1[j,l,:]
    # = Σ_a gP1[g,i,k,a] * P1[j,l,a]
    # This gives (120, NY, NW, NY, NW) which is too large.

    # Instead, loop over y-pairs or use smarter decomposition.
    # Key: P1[j,l,:] = cos(y_j)cos(w_l)c + σ_j cos(y_j)sin(w_l)d + sin(y_j)p
    # gP1[g,i,k,:] is a 4-vector
    # The dot product: gP1[g,i,k,:] · P1[j,l,:] is bilinear in (cos w_k, sin w_k) and (cos w_l, sin w_l)

    # Decompose: gP1[g,i,k,a] = Σ_m A_{g,i,m,a} * f_m(w_k)
    # where f_0=cos(w), f_1=sin(w) (with sign for d), f_2=1 (for sin(y) term)

    # Actually, let me precompute the three components of gP separately.
    # P = cosy·cosw·c + σ·cosy·sinw·d + siny·p
    # So gP = cosy·cosw·(Lc) + σ·cosy·sinw·(Ld) + siny·(Lp)
    # where Lc = L_g c, etc.

    Lc = np.einsum('gab,b->ga', L_g, c)   # (120, 4)
    Ld = np.einsum('gab,b->ga', L_g, d)   # (120, 4)
    Lp = np.einsum('gab,b->ga', L_g, p)   # (120, 4)

    sigma = np.where(y_nodes <= np.pi/2, 1.0, -1.0)  # (NY,)
    cosy = np.cos(y_nodes)  # (NY,)
    siny = np.sin(y_nodes)  # (NY,)
    cosw = np.cos(w_nodes)  # (NW,)
    sinw = np.sin(w_nodes)  # (NW,)

    # gP(y_i, w_k) = cosy_i cosw_k Lc_g + sigma_i cosy_i sinw_k Ld_g + siny_i Lp_g
    # P(y_j, w_l) = cosy_j cosw_l c + sigma_j cosy_j sinw_l d + siny_j p

    # ⟨gP(i,k), P(j,l)⟩ = Σ_a gP_a P'_a
    # = cosy_i cosw_k cosy_j cosw_l (Lc·c) + cosy_i cosw_k sigma_j cosy_j sinw_l (Lc·d)
    # + cosy_i cosw_k siny_j (Lc·p) + ... (9 terms)

    # Define dot products:
    Lc_c = np.einsum('ga,a->g', Lc, c)   # (120,)
    Lc_d = np.einsum('ga,a->g', Lc, d)
    Lc_p = np.einsum('ga,a->g', Lc, p)
    Ld_c = np.einsum('ga,a->g', Ld, c)
    Ld_d = np.einsum('ga,a->g', Ld, d)
    Ld_p = np.einsum('ga,a->g', Ld, p)
    Lp_c = np.einsum('ga,a->g', Lp, c)
    Lp_d = np.einsum('ga,a->g', Lp, d)
    Lp_p = np.einsum('ga,a->g', Lp, p)

    # ⟨gP(i,k), P(j,l)⟩ =
    #   cosy_i cosw_k cosy_j cosw_l Lc_c[g]
    # + cosy_i cosw_k sigma_j cosy_j sinw_l Lc_d[g]
    # + cosy_i cosw_k siny_j Lc_p[g]
    # + sigma_i cosy_i sinw_k cosy_j cosw_l Ld_c[g]
    # + sigma_i cosy_i sinw_k sigma_j cosy_j sinw_l Ld_d[g]
    # + sigma_i cosy_i sinw_k siny_j Ld_p[g]
    # + siny_i cosy_j cosw_l Lp_c[g]
    # + siny_i sigma_j cosy_j sinw_l Lp_d[g]
    # + siny_i siny_j Lp_p[g]

    # Group by w-dependence:
    # const in w,w': (siny_i)(siny_j) Lp_p[g]
    # cosw_l only: (siny_i)(cosy_j) Lp_c[g] cosw_l
    # sinw_l only: (siny_i)(sigma_j cosy_j) Lp_d[g] sinw_l
    # cosw_k only: (sigma_i cosy_i)(siny_j) Ld_p[g]... wait this is getting messy

    # Instead, define:
    # A(g,i) = [cosy_i Lc[g], sigma_i cosy_i Ld[g], siny_i Lp[g]]  (3 4-vectors)
    # B(j) = [cosy_j c, sigma_j cosy_j d, siny_j p]
    # Then gP(i,k) = cosw_k A_0(g,i) + sinw_k A_1(g,i) + A_2(g,i)
    # P(j,l) = cosw_l B_0(j) + sinw_l B_1(j) + B_2(j)

    # ⟨gP(i,k), P(j,l)⟩ = Σ_{m,r} f_m(w_k) f_r(w_l) ⟨A_m(g,i), B_r(j)⟩
    # where f_0=cosw, f_1=sinw, f_2=1

    # Precompute M_{g,i,j,m,r} = ⟨A_m(g,i), B_r(j)⟩
    # but this is still (120, NY, NY, 3, 3) which is large

    # Better: compute the 9 dot-product coefficients as (120,) arrays
    # and form the inner product as a function of (i,j,k,l)

    # For efficiency, let's do the w-integration analytically or semi-analytically.
    # The inner product u(g,i,j,k,l) is bilinear in (cosw_k, sinw_k) and (cosw_l, sinw_l)
    # plus constant terms.

    # u = a00 cosw cosw' + a01 cosw sinw' + a02 cosw
    #   + a10 sinw cosw' + a11 sinw sinw' + a12 sinw
    #   + a20 cosw' + a21 sinw' + a22
    #
    # where a_{mr} = a_{mr}(g, i, j) are the 9 coefficients.

    # Then C_n^1(u) involves powers of u up to n.
    # ∫∫ C_n^1(u) dw dw' requires integrating each power of u.

    # For moderate n this is feasible by expanding u^k.
    # But for n=20 this means expanding u^20 in trigonometric terms, which has O(n²) terms.

    # Let me instead do the w-integration numerically but vectorize over g and (y,y').

    # Approach: for each g, compute the full (NY, NW, NY, NW) array of inner products,
    # apply C_n^1, sum over w with weights, sum over g with chi.
    # Memory: (NY, NW, NY, NW) floats = 80*60*80*60 = 23M floats = 184MB per g.
    # That's too much for 120 g values.

    # Better: process one g at a time, accumulate.

    result_sum = 0.0

    for gi in range(120):
        # Inner product coefficients
        # u(i,k,j,l) = Σ_{mr} a_{mr}(gi, i, j) * fw_m(k) * fw_r(l)

        # a_{mr}(g, i, j) depends on (i,j) through cosy, siny, sigma
        a = np.zeros((9, NY, NY))  # 9 = 3x3 for (m,r)

        a[0] = np.outer(cosy, cosy) * Lc_c[gi]          # a00 = cosy_i cosy_j Lc·c
        a[1] = np.outer(cosy, sigma*cosy) * Lc_d[gi]     # a01 = cosy_i σ_j cosy_j Lc·d
        a[2] = np.outer(cosy, siny) * Lc_p[gi]           # a02 = cosy_i siny_j Lc·p
        a[3] = np.outer(sigma*cosy, cosy) * Ld_c[gi]     # a10
        a[4] = np.outer(sigma*cosy, sigma*cosy) * Ld_d[gi]  # a11
        a[5] = np.outer(sigma*cosy, siny) * Ld_p[gi]     # a12
        a[6] = np.outer(siny, cosy) * Lp_c[gi]           # a20
        a[7] = np.outer(siny, sigma*cosy) * Lp_d[gi]     # a21
        a[8] = np.outer(siny, siny) * Lp_p[gi]           # a22

        # u(i,j,k,l) = a00 ck cl + a01 ck sl + a02 ck + a10 sk cl + a11 sk sl + a12 sk
        #            + a20 cl + a21 sl + a22
        # where ck=cosw_k, sk=sinw_k, cl=cosw_l, sl=sinw_l

        # For the w-integral: ∫∫ C_n^1(u) dw dw'
        # Do numerically: evaluate u on (NW, NW) grid for each (i,j)

        # But (NY, NY, NW, NW) is too big (80*80*60*60 ≈ 23M). Process y-pairs in chunks.

        chunk = NY  # process all y at once if memory allows

        # Build u on grid: (NY, NY, NW, NW)
        # u = a00[i,j]*ck[k]*cl[l] + a01[i,j]*ck[k]*sl[l] + ...
        ck = cosw[None, None, :, None]   # (1,1,NW,1)
        sk = sinw[None, None, :, None]
        cl = cosw[None, None, None, :]   # (1,1,1,NW)
        sl = sinw[None, None, None, :]

        u = (a[0][:,:,None,None] * ck * cl +
             a[1][:,:,None,None] * ck * sl +
             a[2][:,:,None,None] * ck +
             a[3][:,:,None,None] * sk * cl +
             a[4][:,:,None,None] * sk * sl +
             a[5][:,:,None,None] * sk +
             a[6][:,:,None,None] * cl +
             a[7][:,:,None,None] * sl +
             a[8][:,:,None,None])

        # C_n^1(u)
        Cn = gegenbauer_C1(n, u)  # (NY, NY, NW, NW)

        # Integrate over w and w'
        # ∫∫ C_n^1 dw dw' ≈ Σ_{k,l} C_n^1(u[i,j,k,l]) * ww_k * ww_l
        Iw = np.einsum('ijkl,k,l->ij', Cn, w_weights, w_weights)  # (NY, NY)

        result_sum += chi[gi] * Iw

    # Now result_sum[i,j] = Σ_g χ(g) ∫∫ C_n^1(⟨gP,P'⟩) dw dw'

    # For twisted arm: ψ₁ = sin(y)
    # For untwisted arm (Friedrichs/φ₀-trans): ψ₁ = φ₀·sin(y), but ⟨f, φ₀siny⟩ uses cos(y) instead of |cos(y)|

    if arm == 'twisted':
        # ψ₁ = sin(y), measure = |cos y|
        factor_y = siny * np.abs(cosy)  # (NY,)
    elif arm == 'untwisted':
        # ψ₁ = φ₀ sin(y), ⟨f, ψ₁⟩ = ∫ f · sin(y) · cos(y) dw dy (since φ₀|cos y| = cos y)
        factor_y = siny * cosy  # (NY,)

    # ‖P₁O|‖² = prefactor/‖ψ₁‖² · ∫∫ result_sum[i,j] · factor_y[i] · factor_y[j] dy dy'
    outer_integral = np.einsum('ij,i,j,i,j->', result_sum, factor_y, factor_y,
                               y_weights, y_weights)

    proj = prefactor * outer_integral / psi1_norm2
    return proj

def projection_transverse_sampler(tau, n, placement_name, W, arm='twisted'):
    """Compute ‖P₁O⁽¹⁾|_E‖² for transverse sampler."""
    if n == 0:
        return 0.0

    p, c, d = PLACEMENTS[placement_name]
    chi = CHARS[tau]
    dtau = dim_of_tau(tau)
    prefactor = dtau * (n+1) / (240 * np.pi**2)

    y_nodes, y_weights = gauss_legendre_points(NY, 0, np.pi)
    w_nodes, w_weights = gauss_legendre_points(NW, -W, W)

    psi1_norm2 = 4*W/3

    L_g = np.array([left_mult_matrix(G[i]) for i in range(120)])

    Lc = np.einsum('gab,b->ga', L_g, c)
    Ld = np.einsum('gab,b->ga', L_g, d)
    Lp = np.einsum('gab,b->ga', L_g, p)

    sigma = np.where(y_nodes <= np.pi/2, 1.0, -1.0)
    cosy = np.cos(y_nodes)
    siny = np.sin(y_nodes)
    cosw = np.cos(w_nodes)
    sinw = np.sin(w_nodes)

    # Need K^{00}_E(P(y,w), P(y',w')) = prefactor * Σ_g χ(g) [-C''(u)·⟨g,P⟩·⟨g,P'⟩ + C'(u)·g₀]
    # where u = ⟨gP, P'⟩

    # ⟨g, P(y,w)⟩ = g₁P₁+g₂P₂+g₃P₃ (since P₀=0)
    # = cosy cosw (g·c) + σ cosy sinw (g·d) + siny (g·p)
    # where g·c = g₁c₁+g₂c₂+g₃c₃ etc. (R³ components only)

    g_c = np.sum(G[:, 1:] * c[None, 1:], axis=1)   # (120,)
    g_d = np.sum(G[:, 1:] * d[None, 1:], axis=1)
    g_p = np.sum(G[:, 1:] * p[None, 1:], axis=1)
    g0 = G[:, 0]

    # Dot product coefficients (same as value sampler)
    Lc_c_arr = np.sum(Lc * c[None, :], axis=1)
    Lc_d_arr = np.sum(Lc * d[None, :], axis=1)
    Lc_p_arr = np.sum(Lc * p[None, :], axis=1)
    Ld_c_arr = np.sum(Ld * c[None, :], axis=1)
    Ld_d_arr = np.sum(Ld * d[None, :], axis=1)
    Ld_p_arr = np.sum(Ld * p[None, :], axis=1)
    Lp_c_arr = np.sum(Lp * c[None, :], axis=1)
    Lp_d_arr = np.sum(Lp * d[None, :], axis=1)
    Lp_p_arr = np.sum(Lp * p[None, :], axis=1)

    result_sum = np.zeros((NY, NY))

    for gi in range(120):
        # Build u(i,j,k,l) as before
        a = np.zeros((9, NY, NY))
        a[0] = np.outer(cosy, cosy) * Lc_c_arr[gi]
        a[1] = np.outer(cosy, sigma*cosy) * Lc_d_arr[gi]
        a[2] = np.outer(cosy, siny) * Lc_p_arr[gi]
        a[3] = np.outer(sigma*cosy, cosy) * Ld_c_arr[gi]
        a[4] = np.outer(sigma*cosy, sigma*cosy) * Ld_d_arr[gi]
        a[5] = np.outer(sigma*cosy, siny) * Ld_p_arr[gi]
        a[6] = np.outer(siny, cosy) * Lp_c_arr[gi]
        a[7] = np.outer(siny, sigma*cosy) * Lp_d_arr[gi]
        a[8] = np.outer(siny, siny) * Lp_p_arr[gi]

        ck = cosw[None, None, :, None]
        sk = sinw[None, None, :, None]
        cl = cosw[None, None, None, :]
        sl = sinw[None, None, None, :]

        u = (a[0][:,:,None,None] * ck * cl +
             a[1][:,:,None,None] * ck * sl +
             a[2][:,:,None,None] * ck +
             a[3][:,:,None,None] * sk * cl +
             a[4][:,:,None,None] * sk * sl +
             a[5][:,:,None,None] * sk +
             a[6][:,:,None,None] * cl +
             a[7][:,:,None,None] * sl +
             a[8][:,:,None,None])

        # ⟨g, P(y_i, w_k)⟩ = cosy_i cosw_k g_c + sigma_i cosy_i sinw_k g_d + siny_i g_p
        gP_ik = (cosy[:,None] * cosw[None,:] * g_c[gi] +
                 sigma[:,None] * cosy[:,None] * sinw[None,:] * g_d[gi] +
                 siny[:,None] * g_p[gi])  # (NY, NW)

        gP_jl = (cosy[:,None] * cosw[None,:] * g_c[gi] +
                 sigma[:,None] * cosy[:,None] * sinw[None,:] * g_d[gi] +
                 siny[:,None] * g_p[gi])  # (NY, NW) - same formula

        # C'_n(u) = 2 C_{n-1}^2(u), C''_n(u) = 8 C_{n-2}^3(u)
        Cp = 2 * gegenbauer_C2(n-1, u)
        if n >= 2:
            Cpp = 8 * gegenbauer_C3(n-2, u)
        else:
            Cpp = np.zeros_like(u)

        # K^{00} kernel: -C''·⟨g,P⟩·⟨g,P'⟩ + C'·g₀
        K00 = (-Cpp * gP_ik[:, None, :, None] * gP_jl[None, :, None, :] +
               Cp * g0[gi])  # (NY, NY, NW, NW)

        # Integrate over w, w'
        Iw = np.einsum('ijkl,k,l->ij', K00, w_weights, w_weights)

        result_sum += chi[gi] * Iw

    if arm == 'twisted':
        factor_y = siny * np.abs(cosy)
    elif arm == 'untwisted':
        factor_y = siny * cosy

    outer_integral = np.einsum('ij,i,j,i,j->', result_sum, factor_y, factor_y,
                               y_weights, y_weights)

    proj = prefactor * outer_integral / psi1_norm2
    return proj


# ========== Main computation ==========

if __name__ == '__main__':
    import time

    print("=" * 80)
    print("Computing ‖O|‖², ‖P₁O|‖², Λ for all blocks")
    print("=" * 80)

    # First do a quick test with E^2_1 at W=1 generic placement
    print("\n--- Quick test: E^2_1, generic, W=1 ---")
    t0 = time.time()
    hs = hs_norm_value_sampler('2', 1, 'generic', 1.0)
    print(f"  ‖O⁽⁰⁾|‖² = {hs:.10f} (expected 8/(π²) = {8/np.pi**2:.10f})")
    # Expected: 8W/π² = 8/π² for W=1

    hs_t = hs_norm_transverse_sampler('2', 1, 'generic', 1.0)
    print(f"  ‖O⁽¹⁾|‖² = {hs_t:.10f} (expected 8/π² = {8/np.pi**2:.10f})")

    proj = projection_value_sampler('2', 1, 'generic', 1.0, arm='twisted')
    print(f"  ‖P₁O⁽⁰⁾|‖² = {proj:.10f} (expected 8/(3π²) = {8/(3*np.pi**2):.10f})")

    lam = hs - proj
    print(f"  Λ = {lam:.10f} (expected 16/(3π²) = {16/(3*np.pi**2):.10f})")

    proj_t = projection_transverse_sampler('2', 1, 'generic', 1.0, arm='untwisted')
    print(f"  ‖P₁O⁽¹⁾|‖² = {proj_t:.10f} (expected 0)")
    print(f"  Time: {time.time()-t0:.1f}s")

    # Check W-independence of ‖O|‖²/W for this block
    print("\n--- W-scaling test for E^2_1 ---")
    for W in WIDTHS:
        hs = hs_norm_value_sampler('2', 1, 'generic', W)
        print(f"  W={W}: ‖O⁽⁰⁾|‖²/W = {hs/W:.10f} (should be 8/π² = {8/np.pi**2:.10f})")
