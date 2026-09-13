"""Shell weights for the P1 projection of the Molien shells of S^3/2I: the normalization check.

Under P1 the temperature spectrum is  C_l = sum_N  W_N  P_R(k_N)  Delta_l(k_N)^2,  with
    W_N = 4 pi (2 pi^2 / V) g_N / k_N^3,   V = 2 pi^2 R^3 / 120,   g_N = m_N (N+1),   k_N = sqrt(N(N+2)) / R,
which reduces to  W_N = 480 pi m_N (N+1) / (N(N+2))^(3/2),  independent of R.  This script checks, with exact
integer Molien counts, that these weights reproduce the continuum measure 4 pi dln k at large N (Weyl's law),
so the shell sum tends to the continuum LambdaCDM integral.  It uses no sky data and no transfer function.
"""
import math

NMAX = 40000
FAILS = []

def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILS.append(label)

def molien_counts(nmax):
    # (1 + t^30) / ((1 - t^12)(1 - t^20))
    base = [0] * (nmax + 1)
    for a in range(nmax // 12 + 1):
        for b in range((nmax - 12 * a) // 20 + 1):
            base[12 * a + 20 * b] += 1
    return [base[n] + (base[n - 30] if n >= 30 else 0) for n in range(nmax + 1)]

def molien_counts_alt(nmax):
    # (1 - t^60) / ((1 - t^12)(1 - t^20)(1 - t^30)), an independent route to the same counts
    c = [0] * (nmax + 1)
    for a in range(nmax // 12 + 1):
        for b in range((nmax - 12 * a) // 20 + 1):
            for d in range((nmax - 12 * a - 20 * b) // 30 + 1):
                c[12 * a + 20 * b + 30 * d] += 1
    return [c[n] - (c[n - 60] if n >= 60 else 0) for n in range(nmax + 1)]

m = molien_counts(NMAX)

print("== Fixtures (step one's counts)")
check("m_N = 1 at N = 0, 12, 20, 24, 30", [m[n] for n in (0, 12, 20, 24, 30)] == [1] * 5)
check("m_N = 0 at N = 2, 4, 6, 8, 10 and at every odd N", all(m[n] == 0 for n in (2, 4, 6, 8, 10)) and all(m[n] == 0 for n in range(1, NMAX + 1, 2)))
check("m_60 = 2", m[60] == 2)
check("both closed forms agree to N = 2000", molien_counts_alt(2000) == m[:2001])

def weight(N, vol_factor=120, spin=True, scale=1.0):
    # R = 1: V = 2 pi^2 / vol_factor, so 2 pi^2 / V = vol_factor
    g = m[N] * (N + 1) if spin else m[N]
    return scale * 4 * math.pi * vol_factor * g / (N * (N + 2)) ** 1.5

def weight_s3(N):
    # the full S^3: g_N = (N+1)^2, V = 2 pi^2 R^3
    return 4 * math.pi * (N + 1) ** 2 / (N * (N + 2)) ** 1.5

def bump_ratio(wfun, u0, sig=0.25):
    # sum_N W_N f(ln k_N R) against 4 pi * integral f(u) du, for a Gaussian bump f in u = ln kR
    tot = 0.0
    for N in range(1, NMAX + 1):
        w = wfun(N)
        if w:
            u = 0.5 * math.log(N * (N + 2))
            tot += w * math.exp(-(u - u0) ** 2 / (2 * sig ** 2))
    return tot / (4 * math.pi * sig * math.sqrt(2 * math.pi))

print("\n== The first shell weights, W_N = 480 pi m_N (N+1) / (N(N+2))^(3/2)")
for N in (12, 20, 24, 30, 32, 36, 40, 42, 60):
    print(f"   N = {N:2d}  m_N = {m[N]}  g_N = {m[N]*(N+1):3d}  W_N = {weight(N):.4f}")
b = 13
print(f"   closed-space per-mode convention beta(beta^2-1) against (N(N+2))^(3/2) at N = 12: ratio {b*(b*b-1)/(12*14)**1.5:.5f}")

centres = (300, 1000, 3000, 10000)
TOL = 0.005
print(f"\n== Parent: the Molien weights reproduce 4 pi dln k (tolerance {TOL} at the two largest centres)")
ratios = {c: bump_ratio(weight, math.log(c)) for c in centres}
for c in centres:
    print(f"   bump at kR = {c:5d}: ratio = {ratios[c]:.6f}")
parent_ok = all(abs(ratios[c] - 1) < TOL for c in centres[2:])
check("Molien weights converge to the continuum measure", parent_ok)
s3 = {c: bump_ratio(weight_s3, math.log(c)) for c in centres[2:]}
print("   full S^3 weights: " + ", ".join(f"kR = {c}: {s3[c]:.6f}" for c in s3))
check("full S^3 weights converge to the same measure (second parent)", all(abs(s3[c] - 1) < TOL for c in s3))

print("\n== Mutation arms (run only on a green parent; each must fail the same tolerance)")
if parent_ok:
    arms = {
        "M1: S^3 volume with the quotient counts (the 1/120 dropped)": lambda N: weight(N, vol_factor=1),
        "M2: the free spin label dropped (g_N = m_N)": lambda N: weight(N, spin=False),
        "M3: weights halved (the slip an even-only bookkeeping error makes)": lambda N: weight(N, scale=0.5),
    }
    for label, fn in arms.items():
        r = bump_ratio(fn, math.log(10000))
        print(f"   {label}: ratio at kR = 10000 = {r:.6g}")
        check(label + " is caught", abs(r - 1) >= TOL)
else:
    print("   parent not green: arms not run")
    FAILS.append("parent")

print("\nALL PASS" if not FAILS else f"\nFAILED: {FAILS}")
