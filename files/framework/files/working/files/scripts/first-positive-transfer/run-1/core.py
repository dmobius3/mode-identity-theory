"""
Core infrastructure: binary icosahedral group 2I, characters, placements, band map.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

phi = (1 + np.sqrt(5)) / 2  # golden ratio

# ========== 1. Build the 120 elements of 2I ==========

def build_2I():
    """Return array of shape (120, 4) with unit quaternion coordinates (x0,x1,x2,x3)."""
    elts = []

    # 24 elements: ±1, ±i, ±j, ±k, (±1±i±j±k)/2
    for s in [+1, -1]:
        elts.append([s, 0, 0, 0])
        elts.append([0, s, 0, 0])
        elts.append([0, 0, s, 0])
        elts.append([0, 0, 0, s])
    for s0 in [+1, -1]:
        for s1 in [+1, -1]:
            for s2 in [+1, -1]:
                for s3 in [+1, -1]:
                    elts.append([s0/2, s1/2, s2/2, s3/2])

    # 96 elements: even permutations of (0, ±1, ±φ⁻¹, ±φ)/2
    base_vals = [0, 1, 1/phi, phi]  # (0, 1, φ⁻¹, φ)
    # Even permutations of 4 elements: there are 12
    even_perms = [
        (0,1,2,3), (0,2,3,1), (0,3,1,2),
        (1,0,3,2), (1,2,0,3), (1,3,2,0),
        (2,0,1,3), (2,1,3,0), (2,3,0,1),
        (3,0,2,1), (3,1,0,2), (3,2,1,0),
    ]
    for perm in even_perms:
        v = [base_vals[perm[i]] for i in range(4)]
        # all sign choices on nonzero entries
        nonzero_idx = [i for i in range(4) if v[i] != 0]
        n_nonzero = len(nonzero_idx)
        for signs in range(2**n_nonzero):
            q = list(v)
            for bit, idx in enumerate(nonzero_idx):
                if (signs >> bit) & 1:
                    q[idx] = -q[idx]
            q = [x/2 for x in q]
            elts.append(q)

    elts = np.array(elts)
    # Remove duplicates (within tolerance)
    unique = []
    for e in elts:
        is_dup = False
        for u in unique:
            if np.allclose(e, u, atol=1e-12):
                is_dup = True
                break
        if not is_dup:
            unique.append(e)
    elts = np.array(unique)
    assert elts.shape[0] == 120, f"Expected 120 elements, got {elts.shape[0]}"

    # Verify unit quaternions
    norms = np.linalg.norm(elts, axis=1)
    assert np.allclose(norms, 1.0), "Not all elements are unit quaternions"

    return elts

# ========== 2. Quaternion operations ==========

def qmul(a, b):
    """Quaternion multiplication a*b for arrays of shape (..., 4)."""
    a0, a1, a2, a3 = a[...,0], a[...,1], a[...,2], a[...,3]
    b0, b1, b2, b3 = b[...,0], b[...,1], b[...,2], b[...,3]
    return np.stack([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ], axis=-1)

def qconj(q):
    """Quaternion conjugate."""
    return q * np.array([1, -1, -1, -1])

def left_mult_matrix(g):
    """4x4 matrix for left multiplication by quaternion g."""
    g0, g1, g2, g3 = g
    return np.array([
        [g0, -g1, -g2, -g3],
        [g1,  g0, -g3,  g2],
        [g2,  g3,  g0, -g1],
        [g3, -g2,  g1,  g0],
    ])

# ========== 3. Characters of 2I ==========

def chi2(g):
    """Character χ₂ = 2·Re(g)."""
    return 2 * g[..., 0]

def chi2p(g):
    """Character χ₂' = 2·σ(Re(g)) where σ is Galois conjugation φ↔1-φ."""
    re = g[..., 0]
    # σ fixes 0, ±1, ±1/2 and swaps φ/2 ↔ -φ⁻¹/2, -φ/2 ↔ φ⁻¹/2
    out = np.copy(re)
    # Apply σ: on the real parts that occur, σ(φ/2) = (1-φ)/2 = -1/(2φ)
    # More systematically: σ sends √5 → -√5, so φ=(1+√5)/2 → (1-√5)/2 = -1/φ
    # σ(r) for r a real part of an icosian: r = (a + b√5)/c for integer a,b,c
    # The real parts that occur are: 0, ±1/2, ±1, ±φ/2, ±φ⁻¹/2
    # σ(0) = 0, σ(±1) = ±1, σ(±1/2) = ±1/2
    # σ(φ/2) = (1-φ)/2 = -φ⁻¹/2, σ(φ⁻¹/2) = (1-φ⁻¹)/2 = ...
    # φ⁻¹ = φ-1 = (-1+√5)/2, σ(φ⁻¹) = (-1-√5)/2 = -φ
    # σ(φ⁻¹/2) = -φ/2
    # Similarly σ(-φ/2) = φ⁻¹/2, σ(-φ⁻¹/2) = φ/2

    ph2 = phi / 2   # ≈ 0.809
    ip2 = 1/(2*phi)  # = (phi-1)/2 ≈ 0.309

    mask_ph2p = np.isclose(re, ph2, atol=1e-10)
    mask_ph2n = np.isclose(re, -ph2, atol=1e-10)
    mask_ip2p = np.isclose(re, ip2, atol=1e-10)
    mask_ip2n = np.isclose(re, -ip2, atol=1e-10)

    out[mask_ph2p] = -ip2
    out[mask_ph2n] = ip2
    out[mask_ip2p] = -ph2
    out[mask_ip2n] = ph2

    return 2 * out

def all_characters(g):
    """Compute all 9 irreducible characters at g. Returns dict."""
    t = chi2(g)
    tp = chi2p(g)
    return {
        '1':  np.ones_like(t),
        '2':  t,
        '2p': tp,
        '3':  t**2 - 1,
        '3p': tp**2 - 1,
        '4':  t * tp,
        '4p': t**3 - 2*t,
        '5':  t**4 - 3*t**2 + 1,
        '6':  t**5 - 4*t**3 + 3*t,
    }

def dim_of_tau(tau):
    dims = {'1':1, '2':2, '2p':2, '3':3, '3p':3, '4':4, '4p':4, '5':5, '6':6}
    return dims[tau]

def minus1_acts_as_minus(tau):
    """Returns True if -1 acts as -id in τ."""
    return tau in ['2', '2p', '4p', '6']

# ========== 4. Spin-n/2 character (Chebyshev) ==========

def spin_char(n, t):
    """Character of spin-n/2 rep at element with χ₂ = t.
    This is U_n(t/2) where U_n is Chebyshev of second kind."""
    return cheb_U(n, t/2)

def cheb_U(n, x):
    """Chebyshev polynomial of second kind U_n(x)."""
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 2*x
    u_prev = np.ones_like(x)
    u_curr = 2*x
    for k in range(2, n+1):
        u_next = 2*x*u_curr - u_prev
        u_prev, u_curr = u_curr, u_next
    return u_curr

# ========== 5. Gegenbauer polynomials ==========

def gegenbauer(n, alpha, x):
    """Gegenbauer polynomial C_n^alpha(x)."""
    if n == 0:
        return np.ones_like(x, dtype=float)
    elif n == 1:
        return 2*alpha*x
    c_prev = np.ones_like(x, dtype=float)
    c_curr = 2*alpha*x
    for k in range(2, n+1):
        c_next = (2*(k-1+alpha)*x*c_curr - (k-1+2*alpha-1)*c_prev) / k
        c_prev, c_curr = c_curr, c_next
    return c_curr

def gegenbauer_C1(n, x):
    """C_n^1(x) = U_n(x), Chebyshev second kind."""
    return gegenbauer(n, 1.0, x)

def gegenbauer_C2(n, x):
    """C_n^2(x)."""
    return gegenbauer(n, 2.0, x)

def gegenbauer_C3(n, x):
    """C_n^3(x)."""
    return gegenbauer(n, 3.0, x)

# ========== 6. Block table ==========

BLOCKS = [
    # (tau, n) pairs from §2
    ('1', 12), ('1', 20),
    ('3', 2), ('3', 10),
    ('3p', 6), ('3p', 10),
    ('4', 6), ('4', 8),
    ('5', 4), ('5', 8),
    ('2', 1), ('2', 11),
    ('2p', 7), ('2p', 13),
    ('4p', 3), ('4p', 9),
    ('6', 5), ('6', 7),
]

# ========== 7. Placements ==========

def make_placements():
    """Return dict of placement name -> (p, c, d) as 4-vectors with x0=0."""
    placements = {}

    # Generic
    p_v = np.array([1, 2, 3], dtype=float)
    p_v /= np.linalg.norm(p_v)
    c_v = np.array([2, -1, 0], dtype=float)
    c_v /= np.linalg.norm(c_v)
    d_v = np.cross(p_v, c_v)
    placements['generic'] = (
        np.array([0, *p_v]),
        np.array([0, *c_v]),
        np.array([0, *d_v]),
    )

    # 2-fold
    p_v = np.array([1, 0, 0], dtype=float)
    c_v = np.array([0, 1, 0], dtype=float)
    d_v = np.cross(p_v, c_v)
    placements['2fold'] = (
        np.array([0, *p_v]),
        np.array([0, *c_v]),
        np.array([0, *d_v]),
    )

    # 3-fold
    p_v = np.array([1, 1, 1], dtype=float) / np.sqrt(3)
    c_v = np.array([1, -1, 0], dtype=float) / np.sqrt(2)
    d_v = np.cross(p_v, c_v)
    placements['3fold'] = (
        np.array([0, *p_v]),
        np.array([0, *c_v]),
        np.array([0, *d_v]),
    )

    # 5-fold
    p_v = np.array([1/phi, 1, 0], dtype=float)
    p_v /= np.linalg.norm(p_v)
    c_v = np.array([0, 0, 1], dtype=float)
    d_v = np.cross(p_v, c_v)
    placements['5fold'] = (
        np.array([0, *p_v]),
        np.array([0, *c_v]),
        np.array([0, *d_v]),
    )

    # Verify orthonormality
    for name, (p, c, d) in placements.items():
        assert np.isclose(np.dot(p, p), 1), f"{name}: p not unit"
        assert np.isclose(np.dot(c, c), 1), f"{name}: c not unit"
        assert np.isclose(np.dot(d, d), 1), f"{name}: d not unit"
        assert np.isclose(np.dot(p, c), 0), f"{name}: p not ⊥ c"
        assert np.isclose(np.dot(p, d), 0), f"{name}: p not ⊥ d"
        assert np.isclose(np.dot(c, d), 0), f"{name}: c not ⊥ d"

    return placements

# ========== 8. Band map ==========

def band_map(y, w, p, c, d):
    """
    P(y,w) = cos(y)*(cos(w)*c + sin(w)*d_y) + sin(y)*p
    where d_y = d for y<=π/2, -d for y>π/2.
    Returns 4-vectors (x0=0 since p,c,d are imaginary).
    y, w can be arrays (broadcast together).
    """
    cosy = np.cos(y)
    siny = np.sin(y)
    cosw = np.cos(w)
    sinw = np.sin(w)

    # σ = +1 for y <= π/2, -1 for y > π/2
    sigma = np.where(y <= np.pi/2, 1.0, -1.0)

    # P = cos(y)*cos(w)*c + σ*cos(y)*sin(w)*d + sin(y)*p
    # Each of p, c, d is shape (4,)
    # y, w, cosy, etc. are shape (...)
    P = (cosy * cosw)[..., None] * c[None, :] \
      + (sigma * cosy * sinw)[..., None] * d[None, :] \
      + (siny)[..., None] * p[None, :]

    return P

# ========== 9. Quadrature ==========

def gauss_legendre_points(n, a, b):
    """Gauss-Legendre quadrature on [a, b]."""
    nodes, weights = leggauss(n)
    # Transform from [-1, 1] to [a, b]
    nodes_t = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    weights_t = 0.5 * (b - a) * weights
    return nodes_t, weights_t

# ========== 10. Multiplicity computation ==========

def compute_multiplicity(tau, n, group_2I):
    """Multiplicity of irrep tau in the degree-n harmonic space's left action."""
    chars_tau = all_characters(group_2I)[tau]
    chars_spin = spin_char(n, chi2(group_2I))
    return np.sum(chars_tau * chars_spin) / 120.0

# ========== Verification ==========

if __name__ == '__main__':
    G = build_2I()
    print(f"Built 2I: {G.shape[0]} elements")

    # Check closure under multiplication
    n_fail = 0
    for i in range(120):
        for j in range(120):
            prod = qmul(G[i], G[j])
            found = False
            for k in range(120):
                if np.allclose(prod, G[k], atol=1e-10):
                    found = True
                    break
            if not found:
                n_fail += 1
    print(f"Closure check failures: {n_fail}")

    # Check conjugacy class sizes
    real_parts = np.round(G[:, 0], 10)
    unique_re = np.unique(real_parts)
    print(f"\nConjugacy classes by Re(g):")
    for r in sorted(unique_re):
        count = np.sum(np.isclose(real_parts, r, atol=1e-10))
        print(f"  Re = {r:8.5f}, count = {count}")

    # Verify character orthogonality
    chars = all_characters(G)
    print("\nCharacter inner products (should be δ_{ττ'}):")
    names = ['1', '2', '2p', '3', '3p', '4', '4p', '5', '6']
    for t1 in names:
        row = []
        for t2 in names:
            ip = np.sum(chars[t1] * chars[t2]) / 120.0
            row.append(ip)
        nonzero = [f"{names[j]}:{row[j]:.4f}" for j in range(len(names)) if abs(row[j]) > 0.001]
        print(f"  {t1:3s}: {', '.join(nonzero)}")

    # Verify multiplicities match the block table
    print("\nBlock multiplicities:")
    for tau, n in BLOCKS:
        m = compute_multiplicity(tau, n, G)
        d_tau = dim_of_tau(tau)
        D = round(m) * d_tau * (n+1)
        print(f"  E^{tau}_{n}: mult={m:.4f} (rounded={round(m)}), block dim={D}")

    # Check level 0
    m0 = compute_multiplicity('1', 0, G)
    print(f"\n  E^1_0: mult={m0:.4f}")

    # Check placements
    placements = make_placements()
    for name, (p, c, d) in placements.items():
        print(f"\n{name}: p={p}, c={c}, d={d}")
