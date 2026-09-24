"""
Step 2: Verify symbolically that R^2 J_m phi_K = 0 for m=1 and m=3.

R^2 J_m phi = -1/sqrt(f) * (sqrt(f) * phi')' + V_m * phi
V_m = m^2/(4f) - 1/(2f^2) - 2
f = 1 - 3/4 sin^2(t)
"""
import sympy as sp
from sympy import sin, cos, sqrt, Rational, pi, diff, simplify, trigsimp

t = sp.Symbol('t', real=True)

f = 1 - Rational(3,4)*sin(t)**2

# phi_K profiles (up to constant - we can use numerator since sqrt(f) is common)
# m=1: phi1 = (3sin^2(t) - 2) / (4 sqrt(f))
# m=3: phi3 = (1 + cos^2(t)) / (4 sqrt(f))

phi1 = (3*sin(t)**2 - 2) / (4*sqrt(f))
phi3 = (1 + cos(t)**2) / (4*sqrt(f))

def apply_Jm(phi, m):
    """Compute R^2 J_m phi = -1/sqrt(f) * (sqrt(f)*phi')' + V_m*phi"""
    V = Rational(m**2, 4)/f - 1/(2*f**2) - 2
    term1 = -1/sqrt(f) * diff(sqrt(f) * diff(phi, t), t)
    term2 = V * phi
    return term1 + term2

print("=== Verifying J_1 phi_K^{(1)} = 0 ===")
J1_phi1 = apply_Jm(phi1, 1)
J1_simplified = trigsimp(simplify(J1_phi1))
print(f"R^2 J_1 phi1 = {J1_simplified}")

print("\n=== Verifying J_3 phi_K^{(3)} = 0 ===")
J3_phi3 = apply_Jm(phi3, 3)
J3_simplified = trigsimp(simplify(J3_phi3))
print(f"R^2 J_3 phi3 = {J3_simplified}")

# Also verify the given psi_X for m=0
print("\n=== Control: Verifying J_0 psi_X = 0 ===")
psi_X = sqrt(2)*sin(2*t) / (2*sqrt(3*cos(2*t) + 5))
# Note: 3*cos(2t)+5 = 3*(1-2sin^2 t)+5 = 8-6sin^2 t = 2*(4-3sin^2 t) = 8f
# So psi_X = sqrt(2)*sin(2t)/(2*sqrt(8f)) = sqrt(2)*sin(2t)/(4*sqrt(2)*sqrt(f))
#          = sin(2t)/(4*sqrt(f))
psi_X_alt = sin(2*t)/(4*sqrt(f))
print(f"psi_X simplified: {trigsimp(psi_X - psi_X_alt)}")

J0_psiX = apply_Jm(psi_X, 0)
J0_simplified = trigsimp(simplify(J0_psiX))
print(f"R^2 J_0 psi_X = {J0_simplified}")
