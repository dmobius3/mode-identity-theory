"""
Step 3: Numerical route (§4.2) for sectors m=0,1,2,3.
Corrected Chebyshev differentiation matrix.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.linalg import eig

def cheb(N):
    """Chebyshev differentiation matrix (Trefethen's cheb.m)."""
    if N == 0:
        return np.array([[0.0]]), np.array([1.0])
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

def V_func(t, m):
    fv = f_func(t)
    return m**2/(4*fv) - 1.0/(2*fv**2) - 2.0

def ode_rhs(t, y, m):
    fv = f_func(t)
    fpv = fp_func(t)
    Vm = V_func(t, m)
    return [y[1], -fpv/(2*fv)*y[1] + Vm*y[0]]

def sturm_count(m):
    if m % 2 == 0:
        y0 = [0.0, 1.0]
    else:
        y0 = [1.0, 0.0]

    t_end = np.pi/2
    t_grid_end = t_end - 1e-6

    sol = solve_ivp(ode_rhs, [0, t_end], y0, args=(m,),
                    method='DOP853', rtol=1e-12, atol=1e-14,
                    dense_output=True, t_eval=[t_end])

    N_grid = 100001
    t_grid = np.linspace(0, t_grid_end, N_grid)
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
    rho = abs(phi_end) / phi_max if phi_max > 0 else float('inf')

    return len(zeros), zeros, rho, phi_end, sol

def chebyshev_eigenvalues(m, N):
    D_x, x = cheb(N)
    L = np.pi/2
    t = L/2*(x + 1)  # t[0]=L=pi/2, t[N]=0
    D_t = (2.0/L)*D_x
    D2_t = D_t @ D_t

    fv = f_func(t)
    fpv = fp_func(t)
    Vm = V_func(t, m)

    coeff1 = fpv/(2*fv)
    L_op = -D2_t - np.diag(coeff1) @ D_t + np.diag(Vm)

    if m % 2 == 0:
        # Dirichlet at both ends: remove rows/cols 0 (t=pi/2) and N (t=0)
        A = L_op[1:N, 1:N]
        vals, vecs = eig(A)
    else:
        # Dirichlet at t=pi/2 (index 0), Neumann at t=0 (index N)
        # Remove row/col 0 (Dirichlet). Replace row N with Neumann.
        A = L_op[1:, 1:].copy()
        B = np.eye(N)
        A[-1, :] = D_t[N, 1:]
        B[-1, :] = 0.0
        vals, vecs = eig(A, B)

    mask = np.isfinite(vals) & (np.abs(vals.imag) < 1e-4)
    eigs = np.sort(vals[mask].real)
    return eigs, vecs, vals

print("="*70)
print("NUMERICAL RESULTS FOR ALL SECTORS")
print("="*70)

all_results = {}

for m in [0, 1, 2, 3]:
    print(f"\n{'='*50}")
    print(f"Sector m = {m}")
    print(f"{'='*50}")

    n_zeros, zeros, rho, phi_end, sol = sturm_count(m)
    print(f"\nSturm count: {n_zeros} interior zeros")
    for i, z in enumerate(zeros):
        print(f"  zero {i+1} at t = {z:.12f}")
    print(f"Endpoint ratio rho = {rho:.6e}")
    print(f"phi(pi/2) = {phi_end:.12e}")

    eigs64, _, _ = chebyshev_eigenvalues(m, 64)
    eigs128, vecs128, vals128 = chebyshev_eigenvalues(m, 128)

    print(f"\nChebyshev eigenvalues (mu = lambda*R^2):")
    print(f"  {'N=64':>20s}  {'N=128':>20s}  {'|diff|':>12s}  {'agree?':>8s}")

    n_report = 0
    eigenvalue_pairs = []
    for i in range(min(len(eigs64), len(eigs128))):
        mu64 = eigs64[i]
        mu128 = eigs128[i]
        diff = abs(mu64 - mu128)
        agree = "YES" if diff < 1e-8 else "NO"
        print(f"  {mu64:20.12f}  {mu128:20.12f}  {diff:12.2e}  {agree:>8s}")
        eigenvalue_pairs.append((mu64, mu128, diff))
        n_report += 1
        if mu128 > 1.0:
            break

    neg_eigs = [mu128 for mu64, mu128, d in eigenvalue_pairs if mu128 < -1e-8]
    near_zero = [mu128 for mu64, mu128, d in eigenvalue_pairs if abs(mu128) <= 1e-8]

    index_cheb = len(neg_eigs)
    has_near_zero = len(near_zero) > 0 or rho <= 1e-8

    print(f"\nIndex (Chebyshev, mu < -1e-8): {index_cheb}")
    print(f"Near-zero eigenvalues: {near_zero if near_zero else 'none'}")
    print(f"Sturm count = {n_zeros}")
    print(f"Sturm-Chebyshev agreement: {n_zeros == index_cheb}")
    print(f"Endpoint ratio rho <= 1e-8: {rho <= 1e-8}")
    if rho <= 1e-8:
        print(f"  -> NEAR-ZERO CASE from Sturm")

    all_results[m] = {
        'sturm_count': n_zeros,
        'zeros': zeros,
        'rho': rho,
        'phi_end': phi_end,
        'eigenvalue_pairs': eigenvalue_pairs,
        'index_cheb': index_cheb,
        'near_zero': near_zero,
        'has_near_zero': has_near_zero,
    }

print("\n\n" + "="*70)
print("SUMMARY")
print("="*70)
for m in [0, 1, 2, 3]:
    r = all_results[m]
    print(f"m={m}: Sturm={r['sturm_count']}, Cheb_index={r['index_cheb']}, "
          f"near_zero={r['has_near_zero']}, rho={r['rho']:.2e}")
