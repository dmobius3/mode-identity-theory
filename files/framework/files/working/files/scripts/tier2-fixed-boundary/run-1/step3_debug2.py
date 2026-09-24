"""Debug Chebyshev differentiation matrix."""
import numpy as np
from scipy.linalg import eig

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

N = 32
D, x = cheb_diffmat(N)
L = np.pi/2
t = L/2*(x + 1)  # t[0]=pi/2, t[N]=0

D_t = (2.0/L)*D

# Test 1: D_t @ sin(2t) should give 2*cos(2t)
phi_test = np.sin(2*t)
dphi_exact = 2*np.cos(2*t)
dphi_num = D_t @ phi_test
err1 = np.max(np.abs(dphi_num - dphi_exact))
print(f"Test D_t @ sin(2t): max error = {err1:.2e}")

# Test 2: D2_t @ sin(2t) should give -4*sin(2t)
D2_t = D_t @ D_t
d2phi_exact = -4*np.sin(2*t)
d2phi_num = D2_t @ phi_test
err2 = np.max(np.abs(d2phi_num - d2phi_exact))
print(f"Test D2_t @ sin(2t): max error = {err2:.2e}")

# Test 3: eigenvalues of -D2 with Dirichlet BCs on [0, pi/2]
# Should be (2n)^2 for n=1,2,3,...
A = -D2_t[1:N, 1:N]
vals = np.sort(np.linalg.eigvalsh(A))
print(f"\nEigenvalues of -D2 with Dirichlet on [0,pi/2]:")
for i in range(5):
    exact = (2*(i+1))**2
    print(f"  computed={vals[i]:.8f}, exact={(2*(i+1))**2}, diff={vals[i]-exact:.2e}")

# Now test the full operator for m=0
def f_func(t):
    return 1.0 - 0.75*np.sin(t)**2
def fp_func(t):
    return -1.5*np.sin(t)*np.cos(t)
def V_func(t, m):
    fv = f_func(t)
    return m**2/(4*fv) - 1.0/(2*fv**2) - 2.0

N = 64
D, x = cheb_diffmat(N)
t = L/2*(x + 1)
D_t = (2.0/L)*D
D2_t = D_t @ D_t

fv = f_func(t)
fpv = fp_func(t)
Vm = V_func(t, 0)

# psi_X on all points
psi_X_full = np.sin(2*t)/(4*np.sqrt(fv))

# Apply operator term by term
phi = psi_X_full
phi_prime = D_t @ phi
phi_dprime = D2_t @ phi

# -phi'' - (f'/(2f))*phi' + V_m*phi should = 0
result_full = -phi_dprime - fpv/(2*fv)*phi_prime + Vm*phi

print(f"\nFull operator applied to psi_X at all N+1 points:")
print(f"Max |residual| at interior: {np.max(np.abs(result_full[1:N])):.6e}")
print(f"|residual| at boundaries: {abs(result_full[0]):.6e}, {abs(result_full[N]):.6e}")

# The issue might be the boundary. Let's check psi_X values at boundary
print(f"\npsi_X at boundaries: t[0]={t[0]:.6f}, psi_X={psi_X_full[0]:.2e}; t[N]={t[N]:.6f}, psi_X={psi_X_full[N]:.2e}")

# Now check A @ psi_X_interior with correct boundary handling
# L_op @ phi_full = result_full at interior points
# L_op[1:N, :] @ phi_full = L_op[1:N, 1:N] @ phi_interior + L_op[1:N, 0]*phi[0] + L_op[1:N, N]*phi[N]
# Since phi[0] = phi[N] = 0 (Dirichlet), L_op[1:N, 1:N] @ phi_interior = result_full[1:N]
# But phi[0] and phi[N] are NOT exactly zero for psi_X!

print(f"\nThe boundary values of psi_X are:")
print(f"  phi[0] = psi_X(pi/2) = {psi_X_full[0]:.6e}")
print(f"  phi[N] = psi_X(0) = {psi_X_full[N]:.6e}")
print("Both are 0 (sin(pi)=0, sin(0)=0), so this shouldn't be the issue.")

# Let me check the actual matrix product
L_op = -D2_t - np.diag(fpv/(2*fv)) @ D_t + np.diag(Vm)
A = L_op[1:N, 1:N]
phi_int = psi_X_full[1:N]
res = A @ phi_int
print(f"\nA @ psi_X_interior: max |residual| = {np.max(np.abs(res)):.6e}")
print(f"norm(res)/norm(phi_int) = {np.linalg.norm(res)/np.linalg.norm(phi_int):.6e}")

# Compare with full operator
# Full: L_op @ psi_X_full (includes boundary rows)
res_full_int = (L_op @ psi_X_full)[1:N]
print(f"\n(L_op @ psi_X_full)[interior]: max |residual| = {np.max(np.abs(res_full_int)):.6e}")

# The difference would be the boundary column contributions
bndry_contrib = L_op[1:N, 0]*psi_X_full[0] + L_op[1:N, N]*psi_X_full[N]
print(f"Boundary column contributions: max = {np.max(np.abs(bndry_contrib)):.6e}")
print(f"Diff (A@phi_int - full_int): {np.max(np.abs(res - res_full_int)):.6e}")
