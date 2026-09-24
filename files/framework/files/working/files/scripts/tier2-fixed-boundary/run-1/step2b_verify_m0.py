"""
Verify J_0 psi_X = 0 more carefully with better simplification.
"""
import sympy as sp
from sympy import sin, cos, sqrt, Rational, pi, diff, simplify, trigsimp, expand

t = sp.Symbol('t', real=True)

f = 1 - Rational(3,4)*sin(t)**2

# psi_X = sin(2t) / (4*sqrt(f))  (R is a constant factor, drops out of J)
phi = sin(2*t) / (4*sqrt(f))

# V_0 = -1/(2f^2) - 2
V0 = -1/(2*f**2) - 2

# R^2 J_0 phi = -(1/sqrt(f)) * (sqrt(f)*phi')' + V0*phi
sqf = sqrt(f)
phi_prime = diff(phi, t)
inner = sqf * phi_prime
inner_simplified = sp.cancel(inner)
print(f"sqrt(f)*phi' = {inner_simplified}")

inner_deriv = diff(inner_simplified, t)
print(f"(sqrt(f)*phi')' = ... (computing)")

term1 = -inner_deriv / sqf
term1_cancel = sp.cancel(term1)

term2 = V0 * phi
term2_cancel = sp.cancel(term2)

result = sp.cancel(term1_cancel + term2_cancel)
print(f"\nR^2 J_0 phi (cancelled) = {result}")

# Try a different approach: substitute u = sin^2(t) or work numerically first
import numpy as np

def eval_J0_numeric(t_val):
    fv = 1 - 0.75*np.sin(t_val)**2
    phi_v = np.sin(2*t_val)/(4*np.sqrt(fv))

    dt = 1e-7
    phi_p = np.sin(2*(t_val+dt))/(4*np.sqrt(1-0.75*np.sin(t_val+dt)**2))
    phi_m = np.sin(2*(t_val-dt))/(4*np.sqrt(1-0.75*np.sin(t_val-dt)**2))

    sqf_v = np.sqrt(fv)
    sqf_p = np.sqrt(1-0.75*np.sin(t_val+dt)**2)
    sqf_m = np.sqrt(1-0.75*np.sin(t_val-dt)**2)

    phi_prime_v = (phi_p - phi_m)/(2*dt)

    g_p = sqf_p * (np.sin(2*(t_val+2*dt))/(4*np.sqrt(1-0.75*np.sin(t_val+2*dt)**2)) - phi_p)/(dt)
    g_m = sqf_m * (phi_m - np.sin(2*(t_val-2*dt))/(4*np.sqrt(1-0.75*np.sin(t_val-2*dt)**2)))/(dt)
    # Actually let me use a simpler approach

    h = 1e-5
    def phi_func(tv):
        return np.sin(2*tv)/(4*np.sqrt(1-0.75*np.sin(tv)**2))
    def sqf_func(tv):
        return np.sqrt(1-0.75*np.sin(tv)**2)

    # (sqrt(f)*phi')' at t_val using finite differences
    def sqf_phip(tv):
        return sqf_func(tv) * (phi_func(tv+h) - phi_func(tv-h))/(2*h)

    d_sqf_phip = (sqf_phip(t_val+h) - sqf_phip(t_val-h))/(2*h)

    term1 = -d_sqf_phip / sqf_func(t_val)
    V0v = -1/(2*fv**2) - 2
    term2 = V0v * phi_func(t_val)

    return term1 + term2

print("\nNumerical check of J_0 psi_X at several points:")
for tv in [0.3, 0.5, 0.7, 1.0, 1.2]:
    print(f"  t={tv}: J_0 phi = {eval_J0_numeric(tv):.2e}")

# Let me try the full symbolic with expand and collect
print("\nTrying full symbolic expansion...")
# Substitute c2t = cos(2t), rewrite everything
c = sp.Symbol('c')  # c = cos(2t)
# f = 1 - 3/4*(1-cos(2t))/2 = 1 - 3/8 + 3cos(2t)/8 = 5/8 + 3cos(2t)/8 = (5+3cos(2t))/8
# sin(2t) = sqrt(1-c^2)
# But this introduces square roots. Let me just try harder with sympy.

phi_v2 = sin(2*t) / (4*sqrt(f))
inner_v2 = sqrt(f) * diff(phi_v2, t)
# Simplify the inner product
inner_v2 = sp.radsimp(inner_v2)
print(f"sqrt(f)*phi' radsimp = {inner_v2}")

# Derivative
d_inner = diff(inner_v2, t)
d_inner = sp.radsimp(d_inner)

result_v2 = sp.radsimp(-d_inner/sqrt(f) + V0 * phi_v2)
print(f"Result radsimp = {result_v2}")

# Try with full expansion and simplify
result_v3 = sp.nsimplify(result_v2, rational=False)
print(f"Result nsimplify = {result_v3}")

# Factor approach: multiply through by 4*sqrt(f) * (2f^2) to clear denominators
# and check if numerator is 0
numer = sp.numer(sp.together(result_v2))
print(f"Numerator of together = {trigsimp(expand(numer))}")
