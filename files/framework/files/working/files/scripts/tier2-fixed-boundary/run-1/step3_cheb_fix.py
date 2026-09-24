"""
Fix Chebyshev implementation and redo all eigenvalue computations.
Use the standard textbook formula (Trefethen, Spectral Methods in MATLAB).
"""
import numpy as np
from scipy.linalg import eig
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def cheb(N):
    """Chebyshev differentiation matrix (Trefethen's cheb.m).
    Returns D, x where x are N+1 Chebyshev points on [-1,1]."""
    if N == 0:
        return np.array([[0.0]]), np.array([1.0])
    x = np.cos(np.pi * np.arange(N+1) / N)
    c = np.ones(N+1)
    c[0] = 2.0
    c[N] = 2.0
    c *= (-1.0)**np.arange(N+1)

    X = np.outer(x, np.ones(N+1))
    dX = X - X.T + np.eye(N+1)  # avoid 0/0 on diagonal

    D = np.outer(c, 1.0/c) / dX
    D -= np.diag(D.sum(axis=1))
    return D, x

# Verification test
N_test = 32
D_test, x_test = cheb(N_test)
# Test on [-1,1]: d/dx sin(pi*x) = pi*cos(pi*x)
f_test = np.sin(np.pi * x_test)
df_exact = np.pi * np.cos(np.pi * x_test)
df_num = D_test @ f_test
print(f"Test on [-1,1]: D @ sin(pi*x) vs pi*cos(pi*x)")
print(f"  max error = {np.max(np.abs(df_num - df_exact)):.2e}")

# Test second derivative
D2_test = D_test @ D_test
d2f_exact = -np.pi**2 * np.sin(np.pi * x_test)
d2f_num = D2_test @ f_test
print(f"  D2 @ sin(pi*x) vs -pi^2*sin(pi*x): max error = {np.max(np.abs(d2f_num - d2f_exact)):.2e}")

# Eigenvalues of -D2 on [-1,1] with Dirichlet BCs
# Should be (n*pi/2)^2 for n=1,2,... (on [-1,1], length 2)
A_test = -D2_test[1:N_test, 1:N_test]
eigs_test = np.sort(np.linalg.eigvalsh(A_test))
print(f"\n-D2 eigenvalues on [-1,1] with Dirichlet:")
for i in range(5):
    exact = ((i+1)*np.pi/2)**2
    print(f"  eig_{i+1} = {eigs_test[i]:.8f}, exact = {exact:.8f}, err = {abs(eigs_test[i]-exact):.2e}")

# Now map to [0, pi/2]
# t = L/2*(1+x) maps [-1,1] -> [0,L], L=pi/2
# d/dt = (2/L) d/dx
# But note: x[0]=1 -> t=L, x[N]=-1 -> t=0
L = np.pi/2

# Eigenvalues of -d2/dt2 on [0,L] with Dirichlet BCs: (n*pi/L)^2 = 4n^2
D_t_test = (2.0/L) * D_test
D2_t_test = D_t_test @ D_t_test
A_t_test = -D2_t_test[1:N_test, 1:N_test]

# Use eig not eigvalsh since the matrix may not be perfectly symmetric
vals_t, _ = eig(A_t_test)
eigs_t = np.sort(vals_t.real)
print(f"\n-D2 eigenvalues on [0,pi/2] with Dirichlet:")
for i in range(5):
    exact = (2*(i+1))**2
    print(f"  eig_{i+1} = {eigs_t[i]:.8f}, exact = {exact}, err = {abs(eigs_t[i]-exact):.2e}")

# Now test the actual operator
print("\n" + "="*60)
print("Testing m=0 operator on psi_X")
print("="*60)

def f_func(t):
    return 1.0 - 0.75*np.sin(t)**2
def fp_func(t):
    return -1.5*np.sin(t)*np.cos(t)
def V_func(t, m):
    fv = f_func(t)
    return m**2/(4*fv) - 1.0/(2*fv**2) - 2.0

N = 64
D_x, x = cheb(N)
t = L/2*(1+x)  # t[0]=L=pi/2, t[N]=0
D_t = (2.0/L)*D_x
D2_t = D_t @ D_t

fv = f_func(t)
fpv = fp_func(t)
Vm = V_func(t, 0)

# Apply operator to psi_X
psi_X = np.sin(2*t)/(4*np.sqrt(fv))
dpsi = D_t @ psi_X
d2psi = D2_t @ psi_X

residual = -d2psi - fpv/(2*fv)*dpsi + Vm*psi_X
print(f"psi_X values at boundaries: {psi_X[0]:.2e}, {psi_X[N]:.2e}")
print(f"Max |residual| at interior points: {np.max(np.abs(residual[1:N])):.6e}")
print(f"Max |residual| at all points: {np.max(np.abs(residual)):.6e}")

# Build L_op and get eigenvalues
L_op = -D2_t - np.diag(fpv/(2*fv)) @ D_t + np.diag(Vm)
A = L_op[1:N, 1:N]
vals, vecs = eig(A)
mask = np.abs(vals.imag) < 1e-4
eigs = np.sort(vals[mask].real)

print(f"\nChebyshev eigenvalues for m=0 (first 5):")
for i in range(min(5, len(eigs))):
    print(f"  mu_{i} = {eigs[i]:.12f}")

# Rayleigh quotient
psi_int = psi_X[1:N]
rq = np.dot(psi_int, A @ psi_int) / np.dot(psi_int, psi_int)
print(f"\nRayleigh quotient of psi_X: {rq:.12e}")
