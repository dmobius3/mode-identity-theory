"""volume_cap_check.py -- the arithmetic of The Volume Cap (volume-cap.md).

The theorem is one line (the page's §II); this script checks the numbers the page carries:
  1. the caps: a Euclidean ball of radius r fits the round space S^3/G of radius R by volume only
     if (4/3) pi r^3 <= 2 pi^2 R^3 / |G|, so r <= (3 pi / (2 |G|))^(1/3) R; |G| = 120 for 2I, 1 for S^3;
  2. the flat comoving radius to z = 2.33 under the published Λcos rate (Ω_Λ = 0.685, s0 = 0.001),
     by adaptive quadrature and by the pipeline's own numerics (4000-point trapezoid), which must agree;
  3. the ratio of that ball's volume to the domain's at the three readings, in both H0 rows;
  4. the bound the cap puts on the domain's radius in today's units, r / 0.3399.
Each check has a mutation arm that must turn it red, run after its parent passes.
Needs numpy and scipy. Its record is volume_cap_check.out, which it reproduces byte for byte.
"""
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid

C_LIGHT = 299792.458                         # km/s
OMEGA_L, S0 = 0.685, 0.001                   # the published Λcos fit
Z_DEEPEST = 2.33                             # DESI DR2's deepest BAO point
H0_ROWS = {"anchor": 67.36, "SH0ES": 73.04}  # km/s/Mpc
READINGS = {"A": 6.13, "C": 10.5, "B": 19.7}  # Gpc
ORDER = {"2I": 120, "S3": 1}

def E(z, ol=OMEGA_L):
    return np.sqrt((1 - ol) / (1 - S0**2) * ((1 + z)**3 - S0**2 * (1 + z)) + ol)

def integral_quad(z, ol=OMEGA_L):
    return quad(lambda x: 1 / E(x, ol), 0, z, epsabs=1e-13, epsrel=1e-13)[0]

def integral_pipeline(z, n=4000, ol=OMEGA_L):
    g = np.linspace(0, 2.5, n)
    return float(np.interp(z, g, cumulative_trapezoid(1 / E(g, ol), g, initial=0)))

def cap_factor(order):
    return (3 * np.pi / (2 * order)) ** (1 / 3)

def radius(H0, I):
    return C_LIGHT / H0 * I / 1000.0          # Gpc

def ratio(r, R, order):
    return (4 / 3 * np.pi * r**3) / (2 * np.pi**2 * R**3 / order)

# ---- the checks; each returns (passed, detail) ----
def check_caps(order_2i=120):
    a, b = cap_factor(order_2i), cap_factor(ORDER["S3"])
    ok = abs(a - (np.pi / 80) ** (1 / 3)) < 1e-15 and abs(b - (1.5 * np.pi) ** (1 / 3)) < 1e-15
    return ok, f"caps: {a:.4f} R on S^3/2I, {b:.4f} R on S^3"

def check_integral(n=4000):
    q, p = integral_quad(Z_DEEPEST), integral_pipeline(Z_DEEPEST, n)
    return abs(p / q - 1) < 1e-6, f"I(2.33): quadrature {q:.6f}, pipeline {p:.6f}, relative difference {abs(p / q - 1):.1e}"

def check_ratios(readings=READINGS):
    I = integral_quad(Z_DEEPEST)
    rows, ok = [], True
    for lab, R in readings.items():
        for row, H0 in H0_ROWS.items():
            r = radius(H0, I)
            q, s = ratio(r, R, ORDER["2I"]), ratio(r, R, ORDER["S3"])
            rows.append((lab, R, row, r, q, s))
            ok &= (q > 1) == (lab in ("A", "C")) and s < 1
    return ok, rows

def check_bound(factor=None):
    factor = factor or cap_factor(ORDER["2I"])
    I = integral_quad(Z_DEEPEST)
    bounds = {row: radius(H0, I) / factor for row, H0 in H0_ROWS.items()}
    ok = all((READINGS[lab] < b) == (lab in ("A", "C")) for lab in READINGS for b in bounds.values())
    return ok, bounds

if __name__ == "__main__":
    out = []
    p1, d1 = check_caps(); out.append(f"[{'PASS' if p1 else 'FAIL'}] {d1}")
    p2, d2 = check_integral(); out.append(f"[{'PASS' if p2 else 'FAIL'}] {d2}")
    I = integral_quad(Z_DEEPEST)
    for row, H0 in H0_ROWS.items():
        out.append(f"       flat comoving radius to z = 2.33 at H0 = {H0}: {radius(H0, I):.3f} Gpc")
    p3, rows = check_ratios()
    out.append(f"[{'PASS' if p3 else 'FAIL'}] ball volume / domain volume (A and C exceed S^3/2I in both rows, B does not; all fit S^3):")
    for lab, R, row, r, q, s in rows:
        out.append(f"       {lab} R = {R:5.2f} Gpc, {row:<6}: cap on S^3/2I {cap_factor(120) * R:5.2f} Gpc, ratio {q:6.2f}; on S^3 {s:5.3f}")
    p4, bounds = check_bound()
    out.append(f"[{'PASS' if p4 else 'FAIL'}] the bound on the domain's radius in today's units: "
               + ", ".join(f"{b:.2f} Gpc ({row})" for row, b in bounds.items()))
    arms = {
        "caps with |G| = 60": not check_caps(60)[0],
        "pipeline grid cut to 40 points": not check_integral(40)[0],
        "readings A and B swapped": not check_ratios({"A": 19.7, "C": 10.5, "B": 6.13})[0],
        "the bound with the S^3 factor": not check_bound(cap_factor(1))[0],
    }
    parents = p1 and p2 and p3 and p4
    for name, fired in arms.items():
        out.append(f"[{'PASS' if (fired and parents) else 'FAIL'}] arm turns its check red: {name}")
    out.append("ALL PASS" if parents and all(arms.values()) else "SOME FAIL")
    print("\n".join(out))
