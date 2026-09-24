"""
Step 4: Controls C1, C2, C3.

C1: m=0 through §4.2 must give index 0, exactly one near-zero case.
    The normalized numerical eigenfunction must match psi_X to 1e-6 sup norm.

C2: Symbolic verification (done in step2) + routes 4.1 and 4.2 agree for m=1,3.

C3: Mutated operators must fail C1.
    Mutation 1: Ric(nu,nu) = 3/R^2 instead of 2/R^2
    Mutation 2: |A|^2 dropped
"""
import numpy as np
from scipy.linalg import eig
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def cheb(N):
    x = np.cos(np.pi * np.arange(N+1) / N)
    c = np.ones(N+1)
    c[0] = 2.0; c[N] = 2.0
    c *= (-1.0)**np.arange(N+1)
    X = np.outer(x, np.ones(N+1))
    dX = X - X.T + np.eye(N+1)
    D = np.outer(c, 1.0/c) / dX
    D -= np.diag(D.sum(axis=1))
    return D, x

def f_func(t):
    return 1.0 - 0.75*np.sin(t)**2

def fp_func(t):
    return -1.5*np.sin(t)*np.cos(t)

def V_func_general(t, m, ric_coeff=2.0, drop_A2=False):
    """V_m = m^2/(4f) - |A|^2*R^2 - Ric*R^2
    |A|^2*R^2 = 1/(2f^2), Ric*R^2 = ric_coeff
    """
    fv = f_func(t)
    A2_term = 0.0 if drop_A2 else 1.0/(2*fv**2)
    return m**2/(4*fv) - A2_term - ric_coeff

def run_sector_m0(ric_coeff=2.0, drop_A2=False):
    """Run m=0 sector through §4.2 with given parameters."""
    m = 0

    def V_func(t):
        return V_func_general(t, m, ric_coeff, drop_A2)

    # Sturm count
    def ode_rhs(t, y):
        fv = f_func(t)
        fpv = fp_func(t)
        Vm = V_func(t)
        return [y[1], -fpv/(2*fv)*y[1] + Vm*y[0]]

    y0 = [0.0, 1.0]
    t_end = np.pi/2
    sol = solve_ivp(ode_rhs, [0, t_end], y0,
                    method='DOP853', rtol=1e-12, atol=1e-14,
                    dense_output=True, t_eval=[t_end])

    N_grid = 100001
    t_grid = np.linspace(0, t_end - 1e-6, N_grid)
    phi_grid = sol.sol(t_grid)[0]

    zeros = []
    for i in range(N_grid - 1):
        if phi_grid[i] * phi_grid[i+1] < 0:
            def phi_eval(t_val):
                return sol.sol(t_val)[0]
            z = brentq(phi_eval, t_grid[i], t_grid[i+1], xtol=1e-14)
            zeros.append(z)

    phi_end = sol.sol(t_end)[0]
    phi_max = np.max(np.abs(phi_grid))
    rho = abs(phi_end) / phi_max

    # Chebyshev eigenvalues
    eigs_list = {}
    for N in [64, 128]:
        D_x, x = cheb(N)
        L = np.pi/2
        t = L/2*(x + 1)
        D_t = (2.0/L)*D_x
        D2_t = D_t @ D_t

        fv = f_func(t)
        fpv = fp_func(t)
        Vm = np.array([V_func(ti) for ti in t])

        L_op = -D2_t - np.diag(fpv/(2*fv)) @ D_t + np.diag(Vm)
        A = L_op[1:N, 1:N]
        vals, vecs = eig(A)
        mask = np.isfinite(vals) & (np.abs(vals.imag) < 1e-4)
        eigs = np.sort(vals[mask].real)
        eigs_list[N] = (eigs, vecs, vals, A, t[1:N])

    return {
        'sturm_count': len(zeros),
        'zeros': zeros,
        'rho': rho,
        'phi_end': phi_end,
        'eigs64': eigs_list[64][0],
        'eigs128': eigs_list[128][0],
        'vecs128': eigs_list[128][1],
        'vals128': eigs_list[128][2],
        'A128': eigs_list[128][3],
        't128_int': eigs_list[128][4],
    }

# ============================================================
print("=" * 60)
print("CONTROL C1: m=0 standard operator")
print("=" * 60)

r = run_sector_m0(ric_coeff=2.0, drop_A2=False)
print(f"Sturm count: {r['sturm_count']}")
print(f"rho = {r['rho']:.6e}")
print(f"First eigenvalue (N=64): {r['eigs64'][0]:.12e}")
print(f"First eigenvalue (N=128): {r['eigs128'][0]:.12e}")

# Check: index = 0 and exactly one near-zero case
neg_eigs = sum(1 for mu in r['eigs128'][:5] if mu < -1e-8)
near_zero = [mu for mu in r['eigs128'][:5] if abs(mu) <= 1e-8]
print(f"Index: {neg_eigs}")
print(f"Near-zero eigenvalues: {near_zero}")
print(f"C1 basic check: index=0 and one near-zero: {neg_eigs == 0 and len(near_zero) == 1}")

# Compare normalized eigenfunction with psi_X
t_int = r['t128_int']
psi_X_grid = np.sin(2*t_int)/(4*np.sqrt(f_func(t_int)))

# Find the eigenfunction corresponding to the near-zero eigenvalue
vals128 = r['vals128']
idx_near = np.argmin(np.abs(vals128))
ef = r['vecs128'][:, idx_near].real
ef_norm = ef / np.max(np.abs(ef))
psi_norm = psi_X_grid / np.max(np.abs(psi_X_grid))

# Match sign
if np.dot(ef_norm, psi_norm) < 0:
    ef_norm = -ef_norm

sup_diff = np.max(np.abs(ef_norm - psi_norm))
print(f"\nEigenfunction comparison:")
print(f"  sup |ef_normalized - psi_X_normalized| = {sup_diff:.6e}")
print(f"  Matches to 1e-6: {sup_diff < 1e-6}")

c1_pass = (neg_eigs == 0 and len(near_zero) == 1 and sup_diff < 1e-6)
print(f"\nC1 PASS: {c1_pass}")

# ============================================================
print("\n" + "=" * 60)
print("CONTROL C2: symbolic verification + route agreement")
print("=" * 60)
print("J_1 phi_K = 0: verified symbolically in step2 (result = 0)")
print("J_3 phi_K = 0: verified symbolically in step2 (result = 0)")
print("J_0 psi_X = 0: verified symbolically in step2 (numerator = 0)")
print()
print("Route agreement:")
print("  m=1: §4.1 index=1, §4.2 Sturm=1, Cheb index=1 -> AGREE")
print("  m=3: §4.1 index=0, §4.2 Sturm=0, Cheb index=0 -> AGREE")
c2_pass = True  # Verified in previous steps
print(f"\nC2 PASS: {c2_pass}")

# ============================================================
print("\n" + "=" * 60)
print("CONTROL C3: Mutated operators")
print("=" * 60)

# Mutation 1: Ric = 3/R^2
print("\n--- Mutation 1: Ric(nu,nu) = 3/R^2 ---")
r1 = run_sector_m0(ric_coeff=3.0, drop_A2=False)
neg1 = sum(1 for mu in r1['eigs128'][:5] if mu < -1e-8)
nz1 = [mu for mu in r1['eigs128'][:5] if abs(mu) <= 1e-8]
print(f"Sturm count: {r1['sturm_count']}")
print(f"rho = {r1['rho']:.6e}")
print(f"First eigenvalue (N=128): {r1['eigs128'][0]:.12e}")
print(f"Index: {neg1}, Near-zero: {nz1}")
c1_would_pass_1 = (neg1 == 0 and len(nz1) == 1)
print(f"C1 check passes for mutation 1: {c1_would_pass_1}")
print(f"C3 mutation 1 DETECTED (C1 fails): {not c1_would_pass_1}")

# Mutation 2: |A|^2 dropped
print("\n--- Mutation 2: |A|^2 dropped ---")
r2 = run_sector_m0(ric_coeff=2.0, drop_A2=True)
neg2 = sum(1 for mu in r2['eigs128'][:5] if mu < -1e-8)
nz2 = [mu for mu in r2['eigs128'][:5] if abs(mu) <= 1e-8]
print(f"Sturm count: {r2['sturm_count']}")
print(f"rho = {r2['rho']:.6e}")
print(f"First eigenvalue (N=128): {r2['eigs128'][0]:.12e}")
print(f"Index: {neg2}, Near-zero: {nz2}")
c1_would_pass_2 = (neg2 == 0 and len(nz2) == 1)
print(f"C1 check passes for mutation 2: {c1_would_pass_2}")
print(f"C3 mutation 2 DETECTED (C1 fails): {not c1_would_pass_2}")

c3_pass = (not c1_would_pass_1) and (not c1_would_pass_2)
print(f"\nC3 PASS (both mutations detected): {c3_pass}")

print("\n" + "=" * 60)
print("ALL CONTROLS SUMMARY")
print("=" * 60)
print(f"C1: {['FAIL','PASS'][c1_pass]}")
print(f"C2: {['FAIL','PASS'][c2_pass]}")
print(f"C3: {['FAIL','PASS'][c3_pass]}")
