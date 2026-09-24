"""Debug m=0 Chebyshev: the zero eigenvalue (psi_X) should appear."""
import numpy as np
from scipy.linalg import eig

def f_func(t):
    return 1.0 - 0.75*np.sin(t)**2

def fp_func(t):
    return -1.5*np.sin(t)*np.cos(t)

def V_func(t, m):
    fv = f_func(t)
    return m**2/(4*fv) - 1.0/(2*fv**2) - 2.0

def cheb_diffmat(N):
    j = np.arange(N+1)
    x = np.cos(np.pi*j/N)
    c = np.ones(N+1)
    c[0] = 2.0; c[N] = 2.0
    c *= (-1.0)**j
    X = np.tile(x, (N+1, 1))
    dX = X - X.T + np.eye(N+1)
    D = np.outer(c, 1.0/c) / dX
    for i in range(N+1):
        D[i,i] = 0
        D[i,i] = -np.sum(D[i,:])
    return D, x

N = 64
m = 0
D, x = cheb_diffmat(N)
L = np.pi/2
t = L/2*(x + 1)

D_t = (2.0/L)*D
D2_t = D_t @ D_t

fv = f_func(t)
fpv = fp_func(t)
Vm = V_func(t, m)

coeff1 = fpv/(2*fv)
L_op = -D2_t - np.diag(coeff1) @ D_t + np.diag(Vm)

# For Dirichlet-Dirichlet: remove rows/cols 0 and N
A = L_op[1:N, 1:N]

vals_all, vecs_all = eig(A)
print(f"Total eigenvalues: {len(vals_all)}")
print(f"Max |imag|: {np.max(np.abs(vals_all.imag)):.2e}")

# Sort by real part
idx = np.argsort(vals_all.real)
vals_sorted = vals_all[idx]

print("\nFirst 10 eigenvalues (sorted by real part):")
for i in range(10):
    print(f"  mu_{i} = {vals_sorted[i].real:.12f} + {vals_sorted[i].imag:.2e}i")

# Check: evaluate psi_X on interior Chebyshev points
t_int = t[1:N]
psi_X = np.sin(2*t_int)/(4*np.sqrt(f_func(t_int)))
psi_X_norm = psi_X / np.linalg.norm(psi_X)

# Apply L_op to psi_X (zero-extended to include boundary values)
psi_full = np.zeros(N+1)
psi_full[1:N] = psi_X  # boundary values are 0

residual = L_op[1:N, :] @ psi_full
print(f"\n||L_op @ psi_X|| = {np.linalg.norm(residual):.6e}")
print(f"||psi_X|| = {np.linalg.norm(psi_X):.6e}")
print(f"Rayleigh quotient = {np.dot(psi_X, residual)/np.dot(psi_X, psi_X):.12e}")

# Check psi_X at boundaries
print(f"\npsi_X at boundary points:")
print(f"  psi_X(t=0) should be 0: {np.sin(0)/(4*np.sqrt(f_func(0)))}")
print(f"  psi_X(t=pi/2) should be 0: {np.sin(np.pi)/(4*np.sqrt(f_func(np.pi/2)))}")

# Also check: what does the smallest eigenvector look like?
vecs_sorted = vecs_all[:, idx]
ev0 = vecs_sorted[:, 0].real
ev0 /= np.max(np.abs(ev0))
print(f"\nSmallest eigenvector (normalized) at a few points:")
for i in [0, N//4, N//2, 3*N//4, N-2]:
    if i < len(t_int):
        print(f"  t={t_int[i]:.4f}: ev={ev0[i]:.6f}, psi_X={psi_X_norm[i]:.6f}")
