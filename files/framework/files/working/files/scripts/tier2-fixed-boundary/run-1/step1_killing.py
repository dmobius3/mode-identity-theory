"""
Step 1: Derive Killing field normal components for sectors m=1,3.

The four Killing fields mixing planes are X_ab(x) = x_a e_b - x_b e_a
for (a,b) in {(1,3),(1,4),(2,3),(2,4)}.

We need:
1. Compute p(s,t) components
2. Compute nu(s,t) - unit normal to B in S^3
3. Compute <X_ab, nu> for each
4. Decompose into e^{ims/2} sectors
"""
import sympy as sp

s, t, R_sym = sp.symbols('s t R', real=True)

# p(s,t) components (R factored out)
p1 = sp.cos(t) * sp.cos(s)
p2 = sp.cos(t) * sp.sin(s)
p3 = sp.sin(t) * sp.cos(s/2)
p4 = sp.sin(t) * sp.sin(s/2)

# Tangent vectors
ps = sp.Matrix([sp.diff(p1,s), sp.diff(p2,s), sp.diff(p3,s), sp.diff(p4,s)])
pt = sp.Matrix([sp.diff(p1,t), sp.diff(p2,t), sp.diff(p3,t), sp.diff(p4,t)])
p_vec = sp.Matrix([p1, p2, p3, p4])

# We need a unit normal in S^3. The tangent space of S^3 at p is orthogonal to p.
# We need n orthogonal to p, ps, pt.
# Use the 4D cross product (Hodge star of p ^ ps ^ pt)

def cross4(a, b, c):
    """4D cross product: vector orthogonal to a,b,c"""
    from sympy import Matrix
    result = []
    for i in range(4):
        # Minor: delete row i
        minor = sp.Matrix(3, 3, lambda r, col: [a,b,c][r][(col+i+1)%4 if (col+i+1)%4 < i else (col+i+1)%4] )
        # Actually let me just use the determinant formula
        pass

    # Use explicit formula
    M = sp.Matrix([a.T, b.T, c.T])  # 3x4
    result = sp.zeros(4,1)
    for i in range(4):
        # Delete column i, take 3x3 determinant
        cols = [j for j in range(4) if j != i]
        sub = M[:, cols]
        result[i] = (-1)**i * sub.det()
    return result

print("Computing cross product for normal vector...")
n_raw = cross4(p_vec, ps, pt)

# Simplify each component
print("Simplifying normal components...")
n_simp = sp.Matrix([sp.trigsimp(sp.expand_trig(c)) for c in n_raw])
print("n_raw (unnormalized):")
for i in range(4):
    print(f"  n[{i}] = {n_simp[i]}")

# Compute norm squared
n_sq = sp.trigsimp(n_simp.dot(n_simp))
print(f"\n|n|^2 = {n_sq}")
print(f"|n|^2 simplified = {sp.simplify(n_sq)}")

# Factor out to get unit normal
# nu = n_raw / |n_raw|
# But we also know f = 1 - 3/4 sin^2(t)

f = 1 - sp.Rational(3,4)*sp.sin(t)**2
print(f"\nf = {f}")

# Now compute <X_ab, nu> for each Killing field
# X_ab(x) = x_a e_b - x_b e_a
# So <X_ab, nu> = x_a * nu_b - x_b * nu_a (using R*p for x, and nu = n_raw/|n_raw|)
# = R*(p_a * nu_b - p_b * nu_a)
# But nu = n_raw / |n_raw|, so
# <X_ab, nu> = R*(p_a * n_b - p_b * n_a) / |n_raw|

# Let's compute p_a * n_b - p_b * n_a for each (a,b)
pairs = [(0,2), (0,3), (1,2), (1,3)]  # (1,3),(1,4),(2,3),(2,4) in 0-indexed
labels = ['X13', 'X14', 'X23', 'X24']

print("\nKilling field normal components (times |n_raw|/R):")
for (a,b), label in zip(pairs, labels):
    raw = p_vec[a]*n_simp[b] - p_vec[b]*n_simp[a]
    simp = sp.trigsimp(sp.expand_trig(raw))
    print(f"  <{label}, n_raw>/R = {simp}")

# Let's also try to express things in terms of e^{is/2} to identify sectors
print("\n\nNow decomposing into Fourier modes in s...")
# Use half-angle: let z = exp(i*s/2)
# cos(s) = (z^2 + z^{-2})/2, sin(s) = (z^2 - z^{-2})/(2i)
# cos(s/2) = (z + z^{-1})/2, sin(s/2) = (z - z^{-1})/(2i)

z = sp.Symbol('z')
# Substitute: express each Killing normal component in terms of z = e^{is/2}
# This is complex. Let me instead just compute the inner products directly.

# Actually, let me compute nu more carefully.
# We have n_raw = cross4(p, p_s, p_t) with the R factors.
# p has factor R, p_s has factor R, p_t has factor R
# So n_raw has factor R^3 from the 3x3 minors.
# Actually p_vec above has R factored out, so n_raw as computed is for R=1.

# Let me just compute the four quantities directly and simplify
print("\n=== Direct computation ===")
for (a,b), label in zip(pairs, labels):
    expr = p_vec[a]*n_simp[b] - p_vec[b]*n_simp[a]
    expr = sp.expand_trig(sp.expand(expr))
    expr = sp.trigsimp(expr)
    print(f"\n{label}: p[{a}]*n[{b}] - p[{b}]*n[{a}] = {expr}")

    # Try to express as sum of e^{ims/2} terms
    # Collect by cos/sin of multiples of s/2
    expr_expanded = sp.expand_trig(expr)
    # Collect terms with cos(ns/2), sin(ns/2) for various n
    for n in [1, 3]:
        cc = expr_expanded.coeff(sp.cos(n*s/2))
        cs = expr_expanded.coeff(sp.sin(n*s/2))
        if cc != 0 or cs != 0:
            print(f"  coeff of cos({n}s/2): {sp.trigsimp(cc)}")
            print(f"  coeff of sin({n}s/2): {sp.trigsimp(cs)}")
    for n in [1, 2, 3]:
        cc = expr_expanded.coeff(sp.cos(n*s))
        cs = expr_expanded.coeff(sp.sin(n*s))
        if cc != 0 or cs != 0:
            print(f"  coeff of cos({n}s): {sp.trigsimp(cc)}")
            print(f"  coeff of sin({n}s): {sp.trigsimp(cs)}")
