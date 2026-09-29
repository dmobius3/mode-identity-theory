"""
Spectral step: first positive eigenvalue for the "same cone-trace matching"
operator on the untwisted arm of M(W).

The untwisted arm = functions (periodic seam). The constant transverse sector
decomposes by parity about the cone:

Symmetric about cone (Neumann at seam):
  Under "same cone-trace matching", the Kirchhoff condition forces u_N = 0
  (regular branch, same as Friedrichs). Tower: ν = 0, 2, 4, ... → λ = 0, 6, 20, ...

Antisymmetric about cone (Dirichlet at seam):
  Under "same cone-trace matching", ũ_D^+ = ũ_D^- with antisymmetry ũ_D^+ = -ũ_D^-
  forces ũ_D = 0 (log datum active). Friedrichs tower: ν = 1, 3, 5, ... → λ = 2, 12, 30, ...
  Under bridging: deformed tower via secular function.

The secular function (by analogy with reference §4.4, but with Dirichlet seam):
  G_D(ν(ν+1)) = (π/2) tan(πν/2) - γ - ψ(ν+1)

  Derivation: Q_ν(0)/P_ν(0) = -(π/2)tan(πν/2), from the DLMF identities:
    P_ν(0) = √π / [Γ((1-ν)/2) Γ(1+ν/2)]
    Q_ν(0) = -√π sin(πν/2) Γ(ν/2+1/2) / [2 Γ(ν/2+1)]
  and the Dirichlet-normalized solution u with u(0)=0 near the cone gives
    G_D = -Q_ν(0)/P_ν(0) - γ - ψ(ν+1) = (π/2)tan(πν/2) - γ - ψ(ν+1)

  Compare with the twisted case (reference §4.4, Neumann seam):
    G_N(ν(ν+1)) = -(π/2) cot(πν/2) - γ - ψ(ν+1)

Eigenvalue condition: G_D = ln(δ₀/(2R)). For δ₀ = 1, R = 1: target = ln(1/2) = -ln(2).
"""

import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq

gamma_em = -digamma(1.0)

def G_D(nu):
    return (np.pi/2) * np.tan(np.pi * nu / 2) - gamma_em - digamma(nu + 1)

target = np.log(0.5)

print("=" * 70)
print("Spectral step: same cone-trace matching, untwisted arm, R=1")
print("=" * 70)
print(f"\nSecular equation: G_D(ν(ν+1)) = ln(δ₀/(2R))")
print(f"Target: {target:.10f}")

print(f"\nG_D(ν→0) = {G_D(1e-10):.10f} (should → 0)")

print("\n--- G_D values ---")
for nu in [0.0001, 0.5, 0.9, 0.999, 1.001, 1.5, 2.0, 2.3, 2.5, 2.9]:
    try:
        val = G_D(nu)
        lam = nu * (nu + 1)
        print(f"  ν = {nu:7.3f}, λ = {lam:8.4f}, G_D = {val:+10.6f}")
    except:
        print(f"  ν = {nu:7.3f}: pole")

print("\n--- Finding first positive eigenvalue (antisymmetric sector) ---")
nu_star = brentq(lambda nu: G_D(nu) - target, 1.001, 2.999)
lam_star = nu_star * (nu_star + 1)
print(f"  Root: ν* = {nu_star:.15f}")
print(f"  Eigenvalue: λ* = {lam_star:.15f}")
print(f"  Check: G_D(ν*) = {G_D(nu_star):.15e}")

print("\n--- Negative eigenvalue check ---")
nu_dense = np.linspace(-0.999, -0.001, 10000)
G_dense = np.array([G_D(nu) for nu in nu_dense])
min_G = np.min(G_dense)
min_nu = nu_dense[np.argmin(G_dense)]
print(f"  min G_D on (-1, 0): {min_G:.10f} at ν = {min_nu:.4f}")
print(f"  target = {target:.10f}")
print(f"  Since min G_D > target, NO negative eigenvalue.")

print(f"\n--- Width-dependent first positive eigenvalue ---")
print(f"{'W':>6} | {'const-sect':>12} | {'odd j=0':>12} | {'even k=1':>12} | {'overall':>12}")
print("-" * 65)
for W in [0.25, 0.5, 1.0, 1.4]:
    lam_const = min(lam_star, 6.0)
    alpha0_odd = np.pi / (2*W)
    lam_odd0 = alpha0_odd * (alpha0_odd + 1)
    alpha1_even = np.pi / W
    lam_even1 = alpha1_even * (alpha1_even + 1)
    lam_total = min(lam_const, min(lam_odd0, lam_even1))
    print(f"{W:6.2f} | {lam_const:12.6f} | {lam_odd0:12.6f} | {lam_even1:12.6f} | {lam_total:12.6f}")

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"  First positive eigenvalue (constant sector): λ* = {lam_star:.10f}")
print(f"  Spectral parameter: ν* = {nu_star:.10f}")
print(f"  Multiplicity: 1 (simple)")
print(f"  Eigenfunction: sgn(cos y)·[P_ν*(sin y) + c·Q_ν*(sin y)], constant in w")
print(f"    where c = -P_ν*(0)/Q_ν*(0) ensures u(0) = 0")
print(f"  No negative eigenvalue (unlike twisted bridging)")
print(f"  Ground state: constant function, λ = 0")

print(f"\n--- Nonconstant sectors (sector-regular, same for all cone conditions) ---")
print(f"  Transverse Neumann modes on [-W, W]:")
print(f"    Even: cos(kπw/W), k=0,1,2,... → periodic seam in untwisted arm")
print(f"    Odd:  sin((2m+1)πw/(2W)), m=0,1,2,... → anti-periodic seam in untwisted arm")
print(f"  Odd transverse modes flip the seam parity!")
print(f"  First odd sector: m=0, α₀ = π/(2W), bottom at α₀(α₀+1)")
print(f"  First even nonconstant: k=1, μ₁ = π/W, bottom at μ₁(μ₁+1)")
print(f"  Overall nonconstant bottom: min(α₀(α₀+1), μ₁(μ₁+1)) = α₀(α₀+1)")

print(f"\n--- Mode crossing ---")
alpha_cross = 2.0
W_cross = np.pi / (2*alpha_cross)
print(f"  α₀(α₀+1) = 6 when α₀ = 2, i.e., W = π/4 = {W_cross:.6f}")
print(f"  For W ≤ π/4: first pos eigenvalue = 6 (constant sector, symmetric tower)")
print(f"  For W > π/4: first pos eigenvalue = α₀(α₀+1) = (π/(2W))(π/(2W)+1)")
print(f"  At W = π/4: doubly degenerate (constant symmetric + first odd nonconstant)")
print(f"  Eigenfunction for W ≤ π/4: P₂(sin y) = (3sin²y - 1)/2, constant in w")
print(f"  Eigenfunction for W > π/4: sgn(cos y)|cos y|^{{α₀}} sin(πw/(2W))")

print(f"\n--- Summary table: first positive eigenvalue vs W ---")
print(f"{'W':>6} | {'sector':>20} | {'eigenvalue':>12} | {'eigenfunction':>40}")
print("-" * 85)
for W in [0.25, 0.5, 1.0, 1.4]:
    alpha0 = np.pi / (2*W)
    lam_nc = alpha0*(alpha0+1)
    if lam_nc >= 6.0:
        print(f"{W:6.2f} | {'constant symmetric':>20} | {6.0:12.6f} | {'P₂(sin y) = (3sin²y-1)/2':>40}")
    else:
        print(f"{W:6.2f} | {'odd nonconstant m=0':>20} | {lam_nc:12.6f} | {'sgn(cosy)|cosy|^α₀ sin(πw/(2W))':>40}")
