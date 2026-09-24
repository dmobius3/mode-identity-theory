"""
Step 1b: Decompose Killing normal components into e^{ims/2} sectors.

From step1: nu = n_raw / sqrt(f), and <X_ab, nu> = R*(p_a*n_b - p_b*n_a)/sqrt(f).

Product-to-sum decomposition to extract |m|=1 and |m|=3 modes.
"""
import sympy as sp
from sympy import sin, cos, sqrt, Rational, pi, trigsimp, simplify, expand_trig

s, t = sp.symbols('s t', real=True)

f = 1 - Rational(3,4)*sin(t)**2

# From step1, the raw expressions (times sqrt(f)/R):
X13_raw = sin(s/2)*cos(s)*cos(t)**2 + sin(s)*cos(s/2)*sin(t)**2/2
X14_raw = sin(s/2)*sin(s)*sin(t)**2/2 - cos(s/2)*cos(s)*cos(t)**2
X23_raw = sin(s/2)*sin(s)*cos(t)**2 - cos(s/2)*cos(s)*sin(t)**2/2
X24_raw = -sin(s/2)*cos(s)*sin(t)**2/2 - sin(s)*cos(s/2)*cos(t)**2

# Use product-to-sum identities
# sin(s/2)*cos(s) = [sin(3s/2) - sin(s/2)]/2
# sin(s)*cos(s/2) = [sin(3s/2) + sin(s/2)]/2
# cos(s/2)*cos(s) = [cos(3s/2) + cos(s/2)]/2  (wait: cos(A)cos(B) = [cos(A-B)+cos(A+B)]/2)
#   cos(s/2)*cos(s) = [cos(s/2) + cos(3s/2)]/2
# sin(s/2)*sin(s) = [cos(s/2) - cos(3s/2)]/2

# Define t-dependent coefficients
A = (1 + cos(t)**2)/4   # = (2 - sin^2 t)/4
B_coeff = (-2 + 3*sin(t)**2)/4  # coefficient for |m|=1

print("A(t) =", A, "=", trigsimp(A))
print("B(t) =", B_coeff, "=", trigsimp(B_coeff))
print()

# Verify decomposition by expanding
X13_decomp = sin(Rational(3,1)*s/2)*A + sin(s/2)*B_coeff
X14_decomp = -cos(Rational(3,1)*s/2)*A + cos(s/2)*B_coeff
X23_decomp = -cos(Rational(3,1)*s/2)*A - cos(s/2)*B_coeff
X24_decomp = -sin(Rational(3,1)*s/2)*A + sin(s/2)*B_coeff

for label, raw, decomp in [('X13', X13_raw, X13_decomp),
                            ('X14', X14_raw, X14_decomp),
                            ('X23', X23_raw, X23_decomp),
                            ('X24', X24_raw, X24_decomp)]:
    diff = trigsimp(expand_trig(raw - decomp))
    print(f"{label}: raw - decomp = {diff}")

print()
# Sector-pure combinations:
print("=== Sector-pure combinations ===")
print("For |m|=1 (sin(s/2) mode):")
print("  X13 + X24 = 2*sin(s/2)*B(t)")
combo1 = trigsimp(expand_trig(X13_raw + X24_raw))
print(f"  Direct: {combo1}")
print(f"  Expected: {trigsimp(2*sin(s/2)*B_coeff)}")
print(f"  Match: {trigsimp(combo1 - 2*sin(s/2)*B_coeff) == 0}")

print("\nFor |m|=1 (cos(s/2) mode):")
print("  X14 - X23 = 2*cos(s/2)*B(t)")
combo2 = trigsimp(expand_trig(X14_raw - X23_raw))
print(f"  Direct: {combo2}")
print(f"  Match: {trigsimp(combo2 - 2*cos(s/2)*B_coeff) == 0}")

print("\nFor |m|=3 (sin(3s/2) mode):")
print("  X13 - X24 = 2*sin(3s/2)*A(t)")
combo3 = trigsimp(expand_trig(X13_raw - X24_raw))
print(f"  Direct: {combo3}")
print(f"  Match: {trigsimp(combo3 - 2*sin(Rational(3,1)*s/2)*A) == 0}")

print("\nFor |m|=3 (cos(3s/2) mode):")
print("  -(X14 + X23) = 2*cos(3s/2)*A(t)")
combo4 = trigsimp(expand_trig(-(X14_raw + X23_raw)))
print(f"  Direct: {combo4}")
print(f"  Match: {trigsimp(combo4 - 2*cos(Rational(3,1)*s/2)*A) == 0}")

# The t-profile for the Jacobi solution in each sector
# <K, nu> = R * (raw) / sqrt(f), and the s-dependence is e^{ims/2}
# So phi_K(t) = coefficient / sqrt(f)

print("\n=== t-profiles phi_K(t) ===")
phi1 = B_coeff / sqrt(f)
phi3 = A / sqrt(f)

phi1_simplified = trigsimp(phi1)
phi3_simplified = trigsimp(phi3)

print(f"phi_K for |m|=1: {phi1_simplified}")
print(f"phi_K for |m|=3: {phi3_simplified}")

# Values at endpoints
print(f"\nphi1(0) = {phi1.subs(t, 0)}")
print(f"phi1(pi/2) = {phi1.subs(t, pi/2)}")
print(f"phi3(0) = {phi3.subs(t, 0)}")
print(f"phi3(pi/2) = {phi3.subs(t, pi/2)}")

# Zeros of phi1 in (0, pi/2)
# phi1 = 0 iff B_coeff = 0 iff -2 + 3*sin^2(t) = 0 iff sin^2(t) = 2/3
print(f"\nZeros of phi1: B(t) = 0 when sin^2(t) = 2/3")
t_zero = sp.asin(sqrt(Rational(2,3)))
print(f"  t* = arcsin(sqrt(2/3)) = {t_zero}")
print(f"  Numerical: {float(t_zero):.10f}")
print(f"  pi/2 = {float(pi/2):.10f}")
print(f"  t* < pi/2: {float(t_zero) < float(pi/2)}")
print(f"  t* > 0: {float(t_zero) > 0}")
print(f"  So exactly 1 zero in (0, pi/2) for m=1 sector")

# Zeros of phi3 in (0, pi/2)
print(f"\nZeros of phi3: A(t) = (1+cos^2(t))/4 >= 1/4 > 0 always")
print(f"  A(0) = {A.subs(t, 0)}, A(pi/2) = {A.subs(t, pi/2)}")
print(f"  No zeros in (0, pi/2) for m=3 sector")

print("\n=== Summary ===")
print("m=1: index = 1 (one zero), nullity = 0 (phi_K(pi/2) != 0)")
print("m=3: index = 0 (no zeros), nullity = 0 (phi_K(pi/2) != 0)")
