"""Pre-freeze expectation for step two: a Sachs-Wolfe-only estimate of C_l(P1) / C_l(LCDM).

Theory only: no data, no likelihood, no CAMB, no ISW, no Doppler, scale-invariant primordial power.
    C_l(P1) / C_l(LCDM) = l(l+1)/(2 pi) * sum_N W_N j_l(k_N chi*)^2,
    W_N = 480 pi m_N (N+1) / (N(N+2))^(3/2),   k_N chi* = sqrt(N(N+2)) chi* / R,
since the continuum Sachs-Wolfe integral is  int dx/x j_l(x)^2 = 1/(2 l(l+1)).
It also recomputes where the shells project, to check the multipole figures quoted in cmb-anomalies.
"""
import math

LMAX = 29
FAILS = []

def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILS.append(label)

def molien_counts(nmax):
    # (1 + t^30) / ((1 - t^12)(1 - t^20)) by strided prefix sums: linear in nmax
    c = [0] * (nmax + 1)
    c[0] = 1
    for step in (12, 20):
        for n in range(step, nmax + 1):
            c[n] += c[n - step]
    return [c[n] + (c[n - 30] if n >= 30 else 0) for n in range(nmax + 1)]

def molien_counts_direct(nmax):
    base = [0] * (nmax + 1)
    for a in range(nmax // 12 + 1):
        for b in range((nmax - 12 * a) // 20 + 1):
            base[12 * a + 20 * b] += 1
    return [base[n] + (base[n - 30] if n >= 30 else 0) for n in range(nmax + 1)]

def sph_jn_all(lmax, x):
    """j_0 .. j_lmax at x > 0: upward recurrence where stable (x > lmax + 5), else Miller's downward
    recurrence normalized by sum_l (2l+1) j_l(x)^2 = 1."""
    if x > lmax + 5:
        out = [math.sin(x) / x, math.sin(x) / x ** 2 - math.cos(x) / x]
        for l in range(1, lmax):
            out.append((2 * l + 1) / x * out[l] - out[l - 1])
        return out[:lmax + 1]
    L = lmax + int(x) + 60
    v = [0.0] * (L + 2)
    v[L] = 1e-30
    for l in range(L, 0, -1):
        v[l - 1] = (2 * l + 1) / x * v[l] - v[l + 1]
        if abs(v[l - 1]) > 1e100:
            for i in range(l - 1, L + 1):
                v[i] *= 1e-100
    s = 1 / math.sqrt(math.fsum((2 * l + 1) * v[l] ** 2 for l in range(L + 1)))
    if v[0] * math.sin(x) / x < 0:
        s = -s
    return [v[l] * s for l in range(lmax + 1)]

def j2(x): return (3 / x ** 2 - 1) * math.sin(x) / x - 3 * math.cos(x) / x ** 2
def j3(x): return (15 / x ** 3 - 6 / x) * math.sin(x) / x - (15 / x ** 2 - 1) * math.cos(x) / x

print("== Fixtures")
m_direct = molien_counts_direct(2000)
m = molien_counts(300000)
check("fast Molien counts equal the direct count to N = 2000, with step one's rows",
      m[:2001] == m_direct and [m[n] for n in (0, 12, 20, 24, 30, 60)] == [1, 1, 1, 1, 1, 2])
ok = all(abs(sph_jn_all(LMAX, x)[2] - j2(x)) < 1e-12 and abs(sph_jn_all(LMAX, x)[3] - j3(x)) < 1e-12
         for x in (0.7, 3.0, 9.07, 17.2, 29.7, 40.0, 500.0))
check("j_2, j_3 match closed forms in both recurrence regimes", ok)
up, down = sph_jn_all(LMAX, 60.0), sph_jn_all(80, 60.0)[:LMAX + 1]
check("upward and downward recurrences agree at x = 60 for l <= 29", max(abs(a - b) for a, b in zip(up, down)) < 1e-12)
h, cont = 0.005, {}
for l in (2, 10, 29):
    tot, x = 0.0, h
    while x < 3000:
        jl = sph_jn_all(LMAX, x)[l]
        tot += jl * jl / x * h
        x += h
    cont[l] = tot * 2 * l * (l + 1)
print("   int dx/x j_l^2 times 2l(l+1), to x = 3000: " + ", ".join(f"l = {l}: {cont[l]:.5f}" for l in cont))
check("continuum Sachs-Wolfe normalization is 1 (within 2e-3)", all(abs(cont[l] - 1) < 2e-3 for l in cont))

def ratios(R, chi, xmax, vol_factor=120):
    acc = [0.0] * (LMAX + 1)
    N = 1
    while True:
        x = math.sqrt(N * (N + 2)) * chi / R
        if x > xmax:
            break
        if m[N]:
            w = 4 * math.pi * vol_factor * m[N] * (N + 1) / (N * (N + 2)) ** 1.5
            j = sph_jn_all(LMAX, x)
            for l in range(2, LMAX + 1):
                acc[l] += w * j[l] ** 2
        N += 1
    return [l * (l + 1) / (2 * math.pi) * acc[l] if l >= 2 else 0.0 for l in range(LMAX + 1)]

CHI = 14.0
print("\n== Machinery check: at R = 200 chi* the gap sits far below l = 2, so the shell sum must return ratio 1")
big = ratios(200 * CHI, CHI, 1500.0)
worst = max(abs(big[l] - 1) for l in range(2, LMAX + 1))
print(f"   max |ratio - 1| over 2 <= l <= 29: {worst:.2e} (truncation at k chi* = 1500 alone accounts for up to 2e-4)")
check("Molien shell sum reproduces the continuum at large R (within 1e-3)", worst < 1e-3)
if worst < 1e-3:
    bad = ratios(200 * CHI, CHI, 1500.0, vol_factor=1)
    check("mutation arm (the 1/120 dropped) is caught", max(abs(bad[l] - 1) for l in range(2, LMAX + 1)) > 1e-3)

print(f"\n== Sachs-Wolfe-only ratio C_l(P1)/C_l(LCDM) at chi* = {CHI} Gpc (shells to k chi* = 6000; tail below 2e-5)")
routes = [("A 6.13", 6.13), ("B 19.7", 19.7), ("A 6.1", 6.1), ("mu-top 10.5", 10.5), ("B 20", 20.0)]
table = {name: ratios(R, CHI, 6000.0) for name, R in routes}
print("     l   " + "".join(f"{name:>13s}" for name, _ in routes))
for l in range(2, LMAX + 1):
    print(f"   {l:3d}   " + "".join(f"{table[name][l]:13.3f}" for name, _ in routes))
f2 = {2: (0.012, 0.032, 0.022), 3: (0.003, 0.021, 0.246), 4: (0.039, 0.080, 0.236), 5: (0.013, 0.126, 0.182),
      8: (0.055, 0.179, 1.68), 15: (0.379, 2.38, 1.23), 29: (1.82, 1.01, 1.02)}
print("\n   against F2's round-two table (ours / F2's), routes A 6.1, mu-top, B:")
for l, vals in f2.items():
    print(f"   l = {l:2d}: " + "   ".join(f"{table[name][l]:.3f}/{v}" for name, v in zip(("A 6.1", "mu-top 10.5", "B 20"), vals)))
for name, _ in routes:
    lo = sorted(table[name][l] for l in range(2, 21))
    top = max(range(2, LMAX + 1), key=lambda l: table[name][l])
    print(f"   {name}: over 2 <= l <= 20 the ratio runs {lo[0]:.3f} to {lo[-1]:.3f}, median {lo[len(lo)//2]:.3f};"
          f" largest ratio {table[name][top]:.2f} at l = {top}; l = 2 to 5: "
          + ", ".join(f"{table[name][l]:.3f}" for l in range(2, 6)))

print("\n== Where the shells project (l = sqrt(N(N+2)) chi*/R; r-problem.md subtracts 1/2)")
for chi in (13.9, 14.0):
    for R in (5.38, 6.1, 6.13, 10.5, 20.0):
        b10 = math.sqrt(120) * chi / R
        f12 = math.sqrt(168) * chi / R
        print(f"   chi* = {chi}  R = {R:5.2f}:  last empty shell N = 10 at {b10:5.2f} (minus 1/2: {b10 - 0.5:5.2f});"
              f"  first shell N = 12 at {f12:5.2f}")
print("\nALL PASS" if not FAILS else f"\nFAILED: {FAILS}")
