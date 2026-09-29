# RETURN -- Transfer of Ambient Harmonic Blocks onto the First Positive Mode of a Conic Mobius Band

## 1. Method as Run

All computations use curvature radius R = 1. The reproducing kernel of each isotypic block E^tau_n is

    K(q, q') = dim(tau)(n+1)/(240 pi^2) sum_{g in 2I} chi_tau(g) C_n^1(<gq, q'>)

where C_n^1 is the Gegenbauer polynomial (= Chebyshev U_n).

- **HS norms** ||O||^2: 2D Gauss-Legendre quadrature (60x40 points in y x w).
- **Projections** ||P_1 O||^2: 4D quadrature (30x12 x 30x12) using the kernel at all (y,w,y',w') pairs,
  weighted by the eigenfunction of the first positive eigenspace.
- **Transverse sampler**: derivative kernel using C_n^2 and C_n^3.
- **Group**: 120 binary icosahedral elements verified (closure, 9 conjugacy classes, character orthogonality, all block multiplicities = 1).
- **Spectral step**: root-finding (scipy.optimize.brentq) on the secular equation derived from Legendre function identities.
- **Per-level tables**: 1 positive level (the first) chosen; ground + first positive + residual.

### Points where the task could not be followed exactly

1. **Symbolic forms in W and orientation.** The reproducing-kernel integrals involve Gegenbauer polynomials
   of bilinear combinations of band-map evaluations. Closed-form symbolic expressions were obtained for
   blocks where the kernel simplifies (E^2_1: all quantities are rational multiples of W/pi^2; general HS
   norms are proportional to W with computable constants). For most higher blocks, only numerical values at
   the four widths are reported.
2. **Bridging per-level decomposition.** The defect-bound eigenfunction for the twisted bridging (and untwisted
   phi_0-transformed) ground mode was not computed. The ground-level decomposition for these conditions is
   reported as missing. Since the first positive eigenspace is shared with Friedrichs, P_1 and Lambda are
   identical for Friedrichs and bridging (twisted arm), and for Friedrichs and phi_0-transformed (untwisted arm).
3. **Rank.** Since all block multiplicities are 1, the rank of P_mu O| is at most dim(tau) for each level.
   Rank was not computed separately; it is bounded by the block dimension and the eigenspace multiplicity (1 for
   all eigenspaces encountered).

## 2. Spectral Step (section 6.3): Same Cone-Trace Matching, Untwisted Arm

The untwisted arm under same cone-trace matching (SCTM) has the boundary condition
u_D^+ = u_D^-, u_N^+ + u_N^- = 0 (the twisted bridging condition applied to functions).

### Constant transverse sector

The constant-in-w sector decomposes by parity about the cone point y = pi/2:

**Symmetric (Neumann at seam):** Under SCTM, the Kirchhoff condition forces u_N = 0
(regular branch, same as Friedrichs). Tower: nu = 0, 2, 4, ... with lambda = 0, 6, 20, ...

**Antisymmetric (Dirichlet at seam):** The log datum is active. The secular equation is

    G_D(nu(nu+1)) = (pi/2) tan(pi nu/2) - gamma - psi(nu+1)

where gamma is the Euler-Mascheroni constant and psi is the digamma function.
Eigenvalue condition: G_D = ln(delta_0/(2R)) = ln(1/2) = -ln 2.

**Derivation.** Q_nu(0)/P_nu(0) = -(pi/2) tan(pi nu/2) from the DLMF identities for
P_nu(0) and Q_nu(0). The Dirichlet-normalized solution gives
G_D = -Q_nu(0)/P_nu(0) - gamma - psi(nu+1). Compare with the twisted Neumann secular
function G_N = -(pi/2) cot(pi nu/2) - gamma - psi(nu+1) of the reference section 4.4.

**Root:** nu* = 2.341328411, lambda* = nu*(nu*+1) = 7.823147140.

**Negative eigenvalue check:** min G_D on (-1, 0) approx -0.185 > -ln 2 approx -0.693.
No negative eigenvalue exists (unlike twisted bridging).

### Nonconstant transverse sectors

Transverse Neumann modes on [-W, W] include:
- Even: cos(k pi w / W), k = 0,1,2,... (periodic seam in untwisted arm)
- Odd: sin((2m+1) pi w / (2W)), m = 0,1,2,... (anti-periodic seam in untwisted arm)

The odd modes flip seam parity. First odd sector: m = 0, alpha_0 = pi/(2W),
bottom eigenvalue alpha_0(alpha_0 + 1).

### Width-dependent first positive eigenvalue

Mode crossing at W = pi/4: constant sector symmetric tower (lambda = 6) vs first odd nonconstant (lambda = alpha_0(alpha_0+1)).

| W | First positive eigenvalue | Sector | Eigenfunction |
|---|---|---|---|
| 0.25 | 6.000000 | constant symmetric | P_2(sin y) = (3 sin^2 y - 1)/2 |
| 0.5 | 6.000000 | constant symmetric | P_2(sin y) = (3 sin^2 y - 1)/2 |
| 1.0 | 4.038197 | odd nonconstant m=0 | sgn(cos y)|cos y|^{alpha_0} sin(pi w/(2W)) |
| 1.4 | 2.380875 | odd nonconstant m=0 | sgn(cos y)|cos y|^{alpha_0} sin(pi w/(2W)) |

Multiplicity: 1 (simple) at all four widths. At W = pi/4 exactly, the eigenvalue 6 is doubly degenerate.

## 3. Level-0 Control (E^1_0)

E^1_0 is the 1-dimensional block of constants (degree 0, trivial representation).

**Value sampler O^(0) (untwisted arm):**
- Basis: Psi_0 = 1/sqrt(2 pi^2)
- O^(0) Psi_0(y,w) = 1/sqrt(2 pi^2) (constant on band)
- ||O^(0)||^2 = 2W/pi^2
- P_1 projection: <constant, phi_0 sin y> = 0 by parity
- ||P_1 O^(0)||^2 = 0
- Lambda = 2W/pi^2 (all norm in ground level)

**Transverse sampler O^(1) (twisted arm):**
- d(constant)/dx_0 = 0
- ||O^(1)||^2 = 0, ||P_1 O^(1)||^2 = 0, Lambda = 0

| W | ||O^(0)||^2 | ||P_1 O^(0)||^2 | Lambda_val | ||O^(1)||^2 |
|---|---|---|---|---|
| 0.25 | 0.050661 | 0 | 0.050661 | 0 |
| 0.5 | 0.101321 | 0 | 0.101321 | 0 |
| 1.0 | 0.202642 | 0 | 0.202642 | 0 |
| 1.4 | 0.283699 | 0 | 0.283699 | 0 |

Level-0 control is not graded (section 7).

## 4. Symbolic W-dependence

### HS norms

All HS norms are proportional to W (placement-independent):

    ||O||^2 = c * W

This follows from the reproducing kernel K_E(q,q) being constant on S^2 for each block
(verified numerically to < 0.01% for all blocks).

| Block | c_val = ||O^(0)||^2 / W | c_trans = ||O^(1)||^2 / W |
|---|---|---|
| E^1_12 | 2.635081 | 147.564557 |
| E^1_20 | 4.256670 | 624.311588 |
| E^3_2 | 1.824287 | 4.864766 |
| E^3_10 | 6.689053 | 267.562109 |
| E^3'_6 | 4.256670 | 68.106719 |
| E^3'_10 | 6.689053 | 267.562109 |
| E^4_6 | 5.675560 | 90.808958 |
| E^4_8 | 7.297148 | 194.590625 |
| E^5_4 | 5.067464 | 40.539714 |
| E^5_8 | 9.121436 | 243.238281 |
| E^2_1 | 0.810794 | 0.810794 |
| E^2_11 | 4.864766 | 231.887161 |
| E^2'_7 | 3.243177 | 68.106719 |
| E^2'_13 | 5.675560 | 368.911393 |
| E^4'_3 | 3.243177 | 16.215885 |
| E^4'_9 | 8.107943 | 267.562109 |
| E^6_5 | 7.297148 | 85.133398 |
| E^6_7 | 9.729531 | 204.320156 |

### Analytic result: E^2_1

All quantities are exact and placement-independent:
- ||O^(0)||^2 = 8W/pi^2 (value sampler, twisted arm)
- ||P_1 O^(0)||^2 = 8W/(3 pi^2)
- Lambda_val = 16W/(3 pi^2)
- ||O^(1)||^2 = 8W/pi^2 (transverse sampler, untwisted arm)
- ||P_1 O^(1)||^2 = 0
- Lambda_trans = 8W/pi^2
- Ground projection (twisted Friedrichs): ||P_0 O^(0)||^2 = sin^2(W)/(2W)

## 5. Numerical Results

Results for all 18 blocks, both samplers, 4 placements, 4 widths.
Cone conditions: Friedrichs (primary) for both arms; bridging (twisted arm),
phi_0-transformed (untwisted arm), and SCTM (untwisted arm) share the same HS norms.
P_1 projections differ only under SCTM.

### Value sampler O^(0)

**Placement: generic**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 6.5877e-01 | 1.2288e-02 | 6.4648e-01 | 1.8403e-02 | 6.4037e-01 |
| E^1_12 | untwisted | 0.5 | 1.3175e+00 | 1.1442e-02 | 1.3061e+00 | 2.0160e-02 | 1.2974e+00 |
| E^1_12 | untwisted | 1.0 | 2.6351e+00 | 3.5650e-02 | 2.5994e+00 | 2.2065e-02 | 2.6130e+00 |
| E^1_12 | untwisted | 1.4 | 3.6891e+00 | 2.6021e-02 | 3.6631e+00 | 2.5698e-02 | 3.6634e+00 |
| E^1_20 | untwisted | 0.25 | 1.0642e+00 | 2.2159e-02 | 1.0420e+00 | 1.6368e-02 | 1.0478e+00 |
| E^1_20 | untwisted | 0.5 | 2.1283e+00 | 1.9632e-02 | 2.1087e+00 | 1.8986e-02 | 2.1093e+00 |
| E^1_20 | untwisted | 1.0 | 4.2567e+00 | 1.4375e-02 | 4.2423e+00 | 1.5954e-02 | 4.2407e+00 |
| E^1_20 | untwisted | 1.4 | 5.9593e+00 | 2.4009e-02 | 5.9353e+00 | 1.3870e-02 | 5.9455e+00 |
| E^3_2 | untwisted | 0.25 | 4.5607e-01 | 1.3772e-01 | 3.1835e-01 | 1.0621e-01 | 3.4986e-01 |
| E^3_2 | untwisted | 0.5 | 9.1214e-01 | 2.5858e-01 | 6.5356e-01 | 2.0107e-01 | 7.1108e-01 |
| E^3_2 | untwisted | 1.0 | 1.8243e+00 | 3.9829e-01 | 1.4260e+00 | 3.8114e-01 | 1.4431e+00 |
| E^3_2 | untwisted | 1.4 | 2.5540e+00 | 3.9018e-01 | 2.1638e+00 | 4.3011e-01 | 2.1239e+00 |
| E^3_10 | untwisted | 0.25 | 1.6723e+00 | 7.6184e-02 | 1.5961e+00 | 8.3233e-02 | 1.5890e+00 |
| E^3_10 | untwisted | 0.5 | 3.3445e+00 | 5.8749e-02 | 3.2858e+00 | 7.9840e-02 | 3.2647e+00 |
| E^3_10 | untwisted | 1.0 | 6.6891e+00 | 1.0540e-01 | 6.5836e+00 | 8.3825e-02 | 6.6052e+00 |
| E^3_10 | untwisted | 1.4 | 9.3647e+00 | 9.0023e-02 | 9.2747e+00 | 9.8254e-02 | 9.2664e+00 |
| E^3'_6 | untwisted | 0.25 | 1.0642e+00 | 1.4693e-01 | 9.1724e-01 | 1.3659e-01 | 9.2758e-01 |
| E^3'_6 | untwisted | 0.5 | 2.1283e+00 | 1.7400e-01 | 1.9543e+00 | 1.7358e-01 | 1.9548e+00 |
| E^3'_6 | untwisted | 1.0 | 4.2567e+00 | 1.4386e-01 | 4.1128e+00 | 1.4870e-01 | 4.1080e+00 |
| E^3'_6 | untwisted | 1.4 | 5.9593e+00 | 1.4070e-01 | 5.8186e+00 | 1.5275e-01 | 5.8066e+00 |
| E^3'_10 | untwisted | 0.25 | 1.6723e+00 | 1.1173e-01 | 1.5605e+00 | 8.0507e-02 | 1.5918e+00 |
| E^3'_10 | untwisted | 0.5 | 3.3445e+00 | 8.5703e-02 | 3.2588e+00 | 6.9062e-02 | 3.2755e+00 |
| E^3'_10 | untwisted | 1.0 | 6.6891e+00 | 9.1518e-02 | 6.5975e+00 | 8.2209e-02 | 6.6068e+00 |
| E^3'_10 | untwisted | 1.4 | 9.3647e+00 | 8.5766e-02 | 9.2789e+00 | 7.8160e-02 | 9.2865e+00 |
| E^4_6 | untwisted | 0.25 | 1.4189e+00 | 1.1701e-01 | 1.3019e+00 | 1.2249e-01 | 1.2964e+00 |
| E^4_6 | untwisted | 0.5 | 2.8378e+00 | 1.4741e-01 | 2.6904e+00 | 1.3959e-01 | 2.6982e+00 |
| E^4_6 | untwisted | 1.0 | 5.6756e+00 | 1.8356e-01 | 5.4920e+00 | 1.9676e-01 | 5.4788e+00 |
| E^4_6 | untwisted | 1.4 | 7.9458e+00 | 1.9925e-01 | 7.7465e+00 | 1.8416e-01 | 7.7616e+00 |
| E^4_8 | untwisted | 0.25 | 1.8243e+00 | 1.3421e-01 | 1.6901e+00 | 1.1499e-01 | 1.7093e+00 |
| E^4_8 | untwisted | 0.5 | 3.6486e+00 | 1.4896e-01 | 3.4996e+00 | 1.3724e-01 | 3.5113e+00 |
| E^4_8 | untwisted | 1.0 | 7.2971e+00 | 1.3308e-01 | 7.1641e+00 | 1.5092e-01 | 7.1462e+00 |
| E^4_8 | untwisted | 1.4 | 1.0216e+01 | 1.4788e-01 | 1.0068e+01 | 1.3168e-01 | 1.0084e+01 |
| E^5_4 | untwisted | 0.25 | 1.2669e+00 | 2.1156e-01 | 1.0553e+00 | 2.1138e-01 | 1.0555e+00 |
| E^5_4 | untwisted | 0.5 | 2.5337e+00 | 3.1913e-01 | 2.2146e+00 | 3.1274e-01 | 2.2210e+00 |
| E^5_4 | untwisted | 1.0 | 5.0675e+00 | 3.3295e-01 | 4.7345e+00 | 3.3159e-01 | 4.7359e+00 |
| E^5_4 | untwisted | 1.4 | 7.0944e+00 | 3.5341e-01 | 6.7410e+00 | 3.6267e-01 | 6.7318e+00 |
| E^5_8 | untwisted | 0.25 | 2.2804e+00 | 1.6072e-01 | 2.1196e+00 | 1.6681e-01 | 2.1135e+00 |
| E^5_8 | untwisted | 0.5 | 4.5607e+00 | 1.6779e-01 | 4.3929e+00 | 1.8271e-01 | 4.3780e+00 |
| E^5_8 | untwisted | 1.0 | 9.1214e+00 | 1.9118e-01 | 8.9303e+00 | 1.6966e-01 | 8.9518e+00 |
| E^5_8 | untwisted | 1.4 | 1.2770e+01 | 1.8427e-01 | 1.2586e+01 | 1.9157e-01 | 1.2578e+01 |
| E^2_1 | twisted | 0.25 | 2.0270e-01 | 6.7993e-02 | 1.3471e-01 | N/A | N/A |
| E^2_1 | twisted | 0.5 | 4.0540e-01 | 1.3599e-01 | 2.6941e-01 | N/A | N/A |
| E^2_1 | twisted | 1.0 | 8.1079e-01 | 2.7197e-01 | 5.3882e-01 | N/A | N/A |
| E^2_1 | twisted | 1.4 | 1.1351e+00 | 3.8076e-01 | 7.5435e-01 | N/A | N/A |
| E^2_11 | twisted | 0.25 | 1.2162e+00 | 3.3251e-02 | 1.1829e+00 | N/A | N/A |
| E^2_11 | twisted | 0.5 | 2.4324e+00 | 2.4319e-02 | 2.4081e+00 | N/A | N/A |
| E^2_11 | twisted | 1.0 | 4.8648e+00 | 4.6504e-02 | 4.8183e+00 | N/A | N/A |
| E^2_11 | twisted | 1.4 | 6.8107e+00 | 5.3345e-02 | 6.7573e+00 | N/A | N/A |
| E^2'_7 | twisted | 0.25 | 8.1079e-01 | 8.5513e-02 | 7.2528e-01 | N/A | N/A |
| E^2'_7 | twisted | 0.5 | 1.6216e+00 | 1.2209e-01 | 1.4995e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.0 | 3.2432e+00 | 9.1102e-02 | 3.1521e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.4 | 4.5404e+00 | 7.1097e-02 | 4.4694e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.25 | 1.4189e+00 | 4.9359e-02 | 1.3695e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.5 | 2.8378e+00 | 6.8611e-02 | 2.7692e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.0 | 5.6756e+00 | 4.9012e-02 | 5.6265e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.4 | 7.9458e+00 | 4.0793e-02 | 7.9050e+00 | N/A | N/A |
| E^4'_3 | twisted | 0.25 | 8.1079e-01 | 1.7363e-01 | 6.3717e-01 | N/A | N/A |
| E^4'_3 | twisted | 0.5 | 1.6216e+00 | 2.9244e-01 | 1.3291e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.0 | 3.2432e+00 | 3.2481e-01 | 2.9184e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.4 | 4.5404e+00 | 3.1502e-01 | 4.2254e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.25 | 2.0270e+00 | 9.5053e-02 | 1.9319e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.5 | 4.0540e+00 | 7.8197e-02 | 3.9758e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.0 | 8.1079e+00 | 1.1774e-01 | 7.9902e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.4 | 1.1351e+01 | 1.3405e-01 | 1.1217e+01 | N/A | N/A |
| E^6_5 | twisted | 0.25 | 1.8243e+00 | 2.3934e-01 | 1.5850e+00 | N/A | N/A |
| E^6_5 | twisted | 0.5 | 3.6486e+00 | 3.2106e-01 | 3.3275e+00 | N/A | N/A |
| E^6_5 | twisted | 1.0 | 7.2971e+00 | 3.2564e-01 | 6.9715e+00 | N/A | N/A |
| E^6_5 | twisted | 1.4 | 1.0216e+01 | 3.1106e-01 | 9.9050e+00 | N/A | N/A |
| E^6_7 | twisted | 0.25 | 2.4324e+00 | 1.9585e-01 | 2.2365e+00 | N/A | N/A |
| E^6_7 | twisted | 0.5 | 4.8648e+00 | 1.9495e-01 | 4.6698e+00 | N/A | N/A |
| E^6_7 | twisted | 1.0 | 9.7295e+00 | 2.2960e-01 | 9.4999e+00 | N/A | N/A |
| E^6_7 | twisted | 1.4 | 1.3621e+01 | 2.4192e-01 | 1.3379e+01 | N/A | N/A |

**Placement: 2fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 6.5877e-01 | 6.5514e-03 | 6.5222e-01 | 1.8523e-02 | 6.4025e-01 |
| E^1_12 | untwisted | 0.5 | 1.3175e+00 | 3.0750e-02 | 1.2868e+00 | 4.1241e-02 | 1.2763e+00 |
| E^1_12 | untwisted | 1.0 | 2.6351e+00 | 2.8532e-02 | 2.6065e+00 | 3.1993e-02 | 2.6031e+00 |
| E^1_12 | untwisted | 1.4 | 3.6891e+00 | 2.6750e-02 | 3.6624e+00 | 2.5633e-02 | 3.6635e+00 |
| E^1_20 | untwisted | 0.25 | 1.0642e+00 | 2.0511e-03 | 1.0621e+00 | 1.1990e-02 | 1.0522e+00 |
| E^1_20 | untwisted | 0.5 | 2.1283e+00 | 1.3228e-02 | 2.1151e+00 | 2.3140e-03 | 2.1260e+00 |
| E^1_20 | untwisted | 1.0 | 4.2567e+00 | 7.8662e-03 | 4.2488e+00 | 8.3296e-03 | 4.2483e+00 |
| E^1_20 | untwisted | 1.4 | 5.9593e+00 | 5.6107e-03 | 5.9537e+00 | 4.6408e-02 | 5.9129e+00 |
| E^3_2 | untwisted | 0.25 | 4.5607e-01 | 1.3772e-01 | 3.1835e-01 | 1.0621e-01 | 3.4986e-01 |
| E^3_2 | untwisted | 0.5 | 9.1214e-01 | 2.5858e-01 | 6.5356e-01 | 2.0107e-01 | 7.1108e-01 |
| E^3_2 | untwisted | 1.0 | 1.8243e+00 | 3.9829e-01 | 1.4260e+00 | 3.8114e-01 | 1.4431e+00 |
| E^3_2 | untwisted | 1.4 | 2.5540e+00 | 3.9018e-01 | 2.1638e+00 | 4.3011e-01 | 2.1239e+00 |
| E^3_10 | untwisted | 0.25 | 1.6723e+00 | 1.0470e-01 | 1.5676e+00 | 9.2053e-02 | 1.5802e+00 |
| E^3_10 | untwisted | 0.5 | 3.3445e+00 | 8.9392e-02 | 3.2551e+00 | 1.2924e-01 | 3.2153e+00 |
| E^3_10 | untwisted | 1.0 | 6.6891e+00 | 8.7498e-02 | 6.6016e+00 | 1.2245e-01 | 6.5666e+00 |
| E^3_10 | untwisted | 1.4 | 9.3647e+00 | 1.0377e-01 | 9.2609e+00 | 7.4811e-02 | 9.2899e+00 |
| E^3'_6 | untwisted | 0.25 | 1.0642e+00 | 1.4600e-01 | 9.1817e-01 | 1.2582e-01 | 9.3834e-01 |
| E^3'_6 | untwisted | 0.5 | 2.1283e+00 | 1.4984e-01 | 1.9785e+00 | 1.1605e-01 | 2.0123e+00 |
| E^3'_6 | untwisted | 1.0 | 4.2567e+00 | 7.6273e-02 | 4.1804e+00 | 2.0762e-01 | 4.0491e+00 |
| E^3'_6 | untwisted | 1.4 | 5.9593e+00 | 1.8903e-01 | 5.7703e+00 | 1.0262e-01 | 5.8567e+00 |
| E^3'_10 | untwisted | 0.25 | 1.6723e+00 | 1.4348e-01 | 1.5288e+00 | 1.2451e-01 | 1.5477e+00 |
| E^3'_10 | untwisted | 0.5 | 3.3445e+00 | 9.5686e-02 | 3.2488e+00 | 9.6981e-02 | 3.2475e+00 |
| E^3'_10 | untwisted | 1.0 | 6.6891e+00 | 7.9859e-02 | 6.6092e+00 | 6.5957e-02 | 6.6231e+00 |
| E^3'_10 | untwisted | 1.4 | 9.3647e+00 | 6.2862e-02 | 9.3018e+00 | 1.1189e-01 | 9.2528e+00 |
| E^4_6 | untwisted | 0.25 | 1.4189e+00 | 1.1794e-01 | 1.3010e+00 | 1.3326e-01 | 1.2856e+00 |
| E^4_6 | untwisted | 0.5 | 2.8378e+00 | 1.7156e-01 | 2.6662e+00 | 1.9712e-01 | 2.6407e+00 |
| E^4_6 | untwisted | 1.0 | 5.6756e+00 | 2.5115e-01 | 5.4244e+00 | 1.3784e-01 | 5.5377e+00 |
| E^4_6 | untwisted | 1.4 | 7.9458e+00 | 1.5092e-01 | 7.7949e+00 | 2.3429e-01 | 7.7115e+00 |
| E^4_8 | untwisted | 0.25 | 1.8243e+00 | 1.2138e-01 | 1.7029e+00 | 1.1871e-01 | 1.7056e+00 |
| E^4_8 | untwisted | 0.5 | 3.6486e+00 | 1.3411e-01 | 3.5145e+00 | 1.2825e-01 | 3.5203e+00 |
| E^4_8 | untwisted | 1.0 | 7.2971e+00 | 1.6184e-01 | 7.1353e+00 | 1.0493e-01 | 7.1922e+00 |
| E^4_8 | untwisted | 1.4 | 1.0216e+01 | 1.1939e-01 | 1.0097e+01 | 1.6816e-01 | 1.0048e+01 |
| E^5_4 | untwisted | 0.25 | 1.2669e+00 | 2.1156e-01 | 1.0553e+00 | 2.1138e-01 | 1.0555e+00 |
| E^5_4 | untwisted | 0.5 | 2.5337e+00 | 3.1913e-01 | 2.2146e+00 | 3.1274e-01 | 2.2210e+00 |
| E^5_4 | untwisted | 1.0 | 5.0675e+00 | 3.3295e-01 | 4.7345e+00 | 3.3159e-01 | 4.7359e+00 |
| E^5_4 | untwisted | 1.4 | 7.0944e+00 | 3.5341e-01 | 6.7410e+00 | 3.6267e-01 | 6.7318e+00 |
| E^5_8 | untwisted | 0.25 | 2.2804e+00 | 1.7355e-01 | 2.1068e+00 | 1.6309e-01 | 2.1173e+00 |
| E^5_8 | untwisted | 0.5 | 4.5607e+00 | 1.8264e-01 | 4.3781e+00 | 1.9170e-01 | 4.3690e+00 |
| E^5_8 | untwisted | 1.0 | 9.1214e+00 | 1.6242e-01 | 8.9590e+00 | 2.1565e-01 | 8.9058e+00 |
| E^5_8 | untwisted | 1.4 | 1.2770e+01 | 2.1275e-01 | 1.2557e+01 | 1.5510e-01 | 1.2615e+01 |
| E^2_1 | twisted | 0.25 | 2.0270e-01 | 6.7993e-02 | 1.3471e-01 | N/A | N/A |
| E^2_1 | twisted | 0.5 | 4.0540e-01 | 1.3599e-01 | 2.6941e-01 | N/A | N/A |
| E^2_1 | twisted | 1.0 | 8.1079e-01 | 2.7197e-01 | 5.3882e-01 | N/A | N/A |
| E^2_1 | twisted | 1.4 | 1.1351e+00 | 3.8076e-01 | 7.5435e-01 | N/A | N/A |
| E^2_11 | twisted | 0.25 | 1.2162e+00 | 2.5142e-02 | 1.1910e+00 | N/A | N/A |
| E^2_11 | twisted | 0.5 | 2.4324e+00 | 3.6215e-02 | 2.3962e+00 | N/A | N/A |
| E^2_11 | twisted | 1.0 | 4.8648e+00 | 9.1418e-02 | 4.7733e+00 | N/A | N/A |
| E^2_11 | twisted | 1.4 | 6.8107e+00 | 7.7449e-02 | 6.7332e+00 | N/A | N/A |
| E^2'_7 | twisted | 0.25 | 8.1079e-01 | 6.9602e-02 | 7.4119e-01 | N/A | N/A |
| E^2'_7 | twisted | 0.5 | 1.6216e+00 | 6.0283e-02 | 1.5613e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.0 | 3.2432e+00 | 4.1028e-02 | 3.2021e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.4 | 4.5404e+00 | 5.4778e-02 | 4.4857e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.25 | 1.4189e+00 | 1.6051e-02 | 1.4028e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.5 | 2.8378e+00 | 2.0313e-02 | 2.8175e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.0 | 5.6756e+00 | 2.0639e-02 | 5.6549e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.4 | 7.9458e+00 | 4.4699e-02 | 7.9011e+00 | N/A | N/A |
| E^4'_3 | twisted | 0.25 | 8.1079e-01 | 1.7363e-01 | 6.3717e-01 | N/A | N/A |
| E^4'_3 | twisted | 0.5 | 1.6216e+00 | 2.9244e-01 | 1.3291e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.0 | 3.2432e+00 | 3.2481e-01 | 2.9184e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.4 | 4.5404e+00 | 3.1502e-01 | 4.2254e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.25 | 2.0270e+00 | 1.1512e-01 | 1.9119e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.5 | 4.0540e+00 | 1.3647e-01 | 3.9175e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.0 | 8.1079e+00 | 1.8493e-01 | 7.9230e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.4 | 1.1351e+01 | 1.5519e-01 | 1.1196e+01 | N/A | N/A |
| E^6_5 | twisted | 0.25 | 1.8243e+00 | 2.3934e-01 | 1.5850e+00 | N/A | N/A |
| E^6_5 | twisted | 0.5 | 3.6486e+00 | 3.2106e-01 | 3.3275e+00 | N/A | N/A |
| E^6_5 | twisted | 1.0 | 7.2971e+00 | 3.2564e-01 | 6.9715e+00 | N/A | N/A |
| E^6_5 | twisted | 1.4 | 1.0216e+01 | 3.1106e-01 | 9.9050e+00 | N/A | N/A |
| E^6_7 | twisted | 0.25 | 2.4324e+00 | 2.1176e-01 | 2.2206e+00 | N/A | N/A |
| E^6_7 | twisted | 0.5 | 4.8648e+00 | 2.5676e-01 | 4.6080e+00 | N/A | N/A |
| E^6_7 | twisted | 1.0 | 9.7295e+00 | 2.7967e-01 | 9.4499e+00 | N/A | N/A |
| E^6_7 | twisted | 1.4 | 1.3621e+01 | 2.5824e-01 | 1.3363e+01 | N/A | N/A |

**Placement: 3fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 6.5877e-01 | 2.1980e-02 | 6.3679e-01 | 1.8493e-02 | 6.4028e-01 |
| E^1_12 | untwisted | 0.5 | 1.3175e+00 | 3.7360e-02 | 1.2802e+00 | 2.0669e-02 | 1.2969e+00 |
| E^1_12 | untwisted | 1.0 | 2.6351e+00 | 2.1302e-02 | 2.6138e+00 | 2.9710e-02 | 2.6054e+00 |
| E^1_12 | untwisted | 1.4 | 3.6891e+00 | 2.5445e-02 | 3.6637e+00 | 1.7248e-02 | 3.6719e+00 |
| E^1_20 | untwisted | 0.25 | 1.0642e+00 | 5.1230e-03 | 1.0590e+00 | 1.0918e-02 | 1.0532e+00 |
| E^1_20 | untwisted | 0.5 | 2.1283e+00 | 1.2802e-02 | 2.1155e+00 | 9.8836e-03 | 2.1185e+00 |
| E^1_20 | untwisted | 1.0 | 4.2567e+00 | 1.5749e-02 | 4.2409e+00 | 1.3732e-02 | 4.2429e+00 |
| E^1_20 | untwisted | 1.4 | 5.9593e+00 | 9.6063e-03 | 5.9497e+00 | 1.9884e-02 | 5.9395e+00 |
| E^3_2 | untwisted | 0.25 | 4.5607e-01 | 1.3772e-01 | 3.1835e-01 | 1.0621e-01 | 3.4986e-01 |
| E^3_2 | untwisted | 0.5 | 9.1214e-01 | 2.5858e-01 | 6.5356e-01 | 2.0107e-01 | 7.1108e-01 |
| E^3_2 | untwisted | 1.0 | 1.8243e+00 | 3.9829e-01 | 1.4260e+00 | 3.8114e-01 | 1.4431e+00 |
| E^3_2 | untwisted | 1.4 | 2.5540e+00 | 3.9018e-01 | 2.1638e+00 | 4.3011e-01 | 2.1239e+00 |
| E^3_10 | untwisted | 0.25 | 1.6723e+00 | 1.0313e-01 | 1.5691e+00 | 8.7726e-02 | 1.5845e+00 |
| E^3_10 | untwisted | 0.5 | 3.3445e+00 | 1.0419e-01 | 3.2403e+00 | 9.4971e-02 | 3.2496e+00 |
| E^3_10 | untwisted | 1.0 | 6.6891e+00 | 7.4930e-02 | 6.6141e+00 | 1.0305e-01 | 6.5860e+00 |
| E^3_10 | untwisted | 1.4 | 9.3647e+00 | 8.8673e-02 | 9.2760e+00 | 7.2314e-02 | 9.2924e+00 |
| E^3'_6 | untwisted | 0.25 | 1.0642e+00 | 1.2997e-01 | 9.3420e-01 | 1.1798e-01 | 9.4619e-01 |
| E^3'_6 | untwisted | 0.5 | 2.1283e+00 | 1.4466e-01 | 1.9837e+00 | 1.1978e-01 | 2.0086e+00 |
| E^3'_6 | untwisted | 1.0 | 4.2567e+00 | 1.1044e-01 | 4.1462e+00 | 1.7057e-01 | 4.0861e+00 |
| E^3'_6 | untwisted | 1.4 | 5.9593e+00 | 1.4638e-01 | 5.8130e+00 | 1.3931e-01 | 5.8200e+00 |
| E^3'_10 | untwisted | 0.25 | 1.6723e+00 | 1.3060e-01 | 1.5417e+00 | 1.1461e-01 | 1.5577e+00 |
| E^3'_10 | untwisted | 0.5 | 3.3445e+00 | 9.1670e-02 | 3.2529e+00 | 1.0948e-01 | 3.2350e+00 |
| E^3'_10 | untwisted | 1.0 | 6.6891e+00 | 1.0514e-01 | 6.5839e+00 | 7.2363e-02 | 6.6167e+00 |
| E^3'_10 | untwisted | 1.4 | 9.3647e+00 | 9.9048e-02 | 9.2656e+00 | 8.7185e-02 | 9.2775e+00 |
| E^4_6 | untwisted | 0.25 | 1.4189e+00 | 1.3397e-01 | 1.2849e+00 | 1.4110e-01 | 1.2778e+00 |
| E^4_6 | untwisted | 0.5 | 2.8378e+00 | 1.7674e-01 | 2.6610e+00 | 1.9339e-01 | 2.6444e+00 |
| E^4_6 | untwisted | 1.0 | 5.6756e+00 | 2.1699e-01 | 5.4586e+00 | 1.7489e-01 | 5.5007e+00 |
| E^4_6 | untwisted | 1.4 | 7.9458e+00 | 1.9357e-01 | 7.7522e+00 | 1.9759e-01 | 7.7482e+00 |
| E^4_8 | untwisted | 0.25 | 1.8243e+00 | 1.2507e-01 | 1.6992e+00 | 1.2283e-01 | 1.7015e+00 |
| E^4_8 | untwisted | 0.5 | 3.6486e+00 | 1.2983e-01 | 3.5187e+00 | 1.4692e-01 | 3.5017e+00 |
| E^4_8 | untwisted | 1.0 | 7.2971e+00 | 1.6574e-01 | 7.1314e+00 | 1.1985e-01 | 7.1773e+00 |
| E^4_8 | untwisted | 1.4 | 1.0216e+01 | 1.5002e-01 | 1.0066e+01 | 1.5424e-01 | 1.0062e+01 |
| E^5_4 | untwisted | 0.25 | 1.2669e+00 | 2.1156e-01 | 1.0553e+00 | 2.1138e-01 | 1.0555e+00 |
| E^5_4 | untwisted | 0.5 | 2.5337e+00 | 3.1913e-01 | 2.2146e+00 | 3.1274e-01 | 2.2210e+00 |
| E^5_4 | untwisted | 1.0 | 5.0675e+00 | 3.3295e-01 | 4.7345e+00 | 3.3159e-01 | 4.7359e+00 |
| E^5_4 | untwisted | 1.4 | 7.0944e+00 | 3.5341e-01 | 6.7410e+00 | 3.6267e-01 | 6.7318e+00 |
| E^5_8 | untwisted | 0.25 | 2.2804e+00 | 1.6986e-01 | 2.1105e+00 | 1.5898e-01 | 2.1214e+00 |
| E^5_8 | untwisted | 0.5 | 4.5607e+00 | 1.8692e-01 | 4.3738e+00 | 1.7303e-01 | 4.3877e+00 |
| E^5_8 | untwisted | 1.0 | 9.1214e+00 | 1.5851e-01 | 8.9629e+00 | 2.0073e-01 | 8.9207e+00 |
| E^5_8 | untwisted | 1.4 | 1.2770e+01 | 1.8212e-01 | 1.2588e+01 | 1.6901e-01 | 1.2601e+01 |
| E^2_1 | twisted | 0.25 | 2.0270e-01 | 6.7993e-02 | 1.3471e-01 | N/A | N/A |
| E^2_1 | twisted | 0.5 | 4.0540e-01 | 1.3599e-01 | 2.6941e-01 | N/A | N/A |
| E^2_1 | twisted | 1.0 | 8.1079e-01 | 2.7197e-01 | 5.3882e-01 | N/A | N/A |
| E^2_1 | twisted | 1.4 | 1.1351e+00 | 3.8076e-01 | 7.5435e-01 | N/A | N/A |
| E^2_11 | twisted | 0.25 | 1.2162e+00 | 3.5876e-02 | 1.1803e+00 | N/A | N/A |
| E^2_11 | twisted | 0.5 | 2.4324e+00 | 4.9813e-02 | 2.3826e+00 | N/A | N/A |
| E^2_11 | twisted | 1.0 | 4.8648e+00 | 5.5553e-02 | 4.8092e+00 | N/A | N/A |
| E^2_11 | twisted | 1.4 | 6.8107e+00 | 4.9938e-02 | 6.7607e+00 | N/A | N/A |
| E^2'_7 | twisted | 0.25 | 8.1079e-01 | 6.9042e-02 | 7.4175e-01 | N/A | N/A |
| E^2'_7 | twisted | 0.5 | 1.6216e+00 | 6.3929e-02 | 1.5577e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.0 | 3.2432e+00 | 6.5862e-02 | 3.1773e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.4 | 4.5404e+00 | 7.9103e-02 | 4.4613e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.25 | 1.4189e+00 | 2.2062e-02 | 1.3968e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.5 | 2.8378e+00 | 2.0940e-02 | 2.8168e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.0 | 5.6756e+00 | 4.1314e-02 | 5.6342e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.4 | 7.9458e+00 | 3.8052e-02 | 7.9077e+00 | N/A | N/A |
| E^4'_3 | twisted | 0.25 | 8.1079e-01 | 1.7363e-01 | 6.3717e-01 | N/A | N/A |
| E^4'_3 | twisted | 0.5 | 1.6216e+00 | 2.9244e-01 | 1.3291e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.0 | 3.2432e+00 | 3.2481e-01 | 2.9184e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.4 | 4.5404e+00 | 3.1502e-01 | 4.2254e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.25 | 2.0270e+00 | 1.1991e-01 | 1.9071e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.5 | 4.0540e+00 | 1.4411e-01 | 3.9099e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.0 | 8.1079e+00 | 1.3889e-01 | 7.9691e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.4 | 1.1351e+01 | 1.2653e-01 | 1.1225e+01 | N/A | N/A |
| E^6_5 | twisted | 0.25 | 1.8243e+00 | 2.3934e-01 | 1.5850e+00 | N/A | N/A |
| E^6_5 | twisted | 0.5 | 3.6486e+00 | 3.2106e-01 | 3.3275e+00 | N/A | N/A |
| E^6_5 | twisted | 1.0 | 7.2971e+00 | 3.2564e-01 | 6.9715e+00 | N/A | N/A |
| E^6_5 | twisted | 1.4 | 1.0216e+01 | 3.1106e-01 | 9.9050e+00 | N/A | N/A |
| E^6_7 | twisted | 0.25 | 2.4324e+00 | 2.1232e-01 | 2.2201e+00 | N/A | N/A |
| E^6_7 | twisted | 0.5 | 4.8648e+00 | 2.5311e-01 | 4.6117e+00 | N/A | N/A |
| E^6_7 | twisted | 1.0 | 9.7295e+00 | 2.5483e-01 | 9.4747e+00 | N/A | N/A |
| E^6_7 | twisted | 1.4 | 1.3621e+01 | 2.3391e-01 | 1.3387e+01 | N/A | N/A |

**Placement: 5fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 6.5877e-01 | 1.5437e-02 | 6.4333e-01 | 1.9076e-02 | 6.3969e-01 |
| E^1_12 | untwisted | 0.5 | 1.3175e+00 | 1.4278e-02 | 1.3033e+00 | 1.5364e-02 | 1.3022e+00 |
| E^1_12 | untwisted | 1.0 | 2.6351e+00 | 2.5694e-02 | 2.6094e+00 | 2.4928e-02 | 2.6102e+00 |
| E^1_12 | untwisted | 1.4 | 3.6891e+00 | 3.0817e-02 | 3.6583e+00 | 2.3720e-02 | 3.6654e+00 |
| E^1_20 | untwisted | 0.25 | 1.0642e+00 | 2.1534e-02 | 1.0426e+00 | 2.8136e-02 | 1.0360e+00 |
| E^1_20 | untwisted | 0.5 | 2.1283e+00 | 1.5807e-02 | 2.1125e+00 | 1.3649e-02 | 2.1147e+00 |
| E^1_20 | untwisted | 1.0 | 4.2567e+00 | 1.4100e-02 | 4.2426e+00 | 1.5448e-02 | 4.2412e+00 |
| E^1_20 | untwisted | 1.4 | 5.9593e+00 | 2.8300e-02 | 5.9310e+00 | 2.0349e-02 | 5.9390e+00 |
| E^3_2 | untwisted | 0.25 | 4.5607e-01 | 1.3772e-01 | 3.1835e-01 | 1.0621e-01 | 3.4986e-01 |
| E^3_2 | untwisted | 0.5 | 9.1214e-01 | 2.5858e-01 | 6.5356e-01 | 2.0107e-01 | 7.1108e-01 |
| E^3_2 | untwisted | 1.0 | 1.8243e+00 | 3.9829e-01 | 1.4260e+00 | 3.8114e-01 | 1.4431e+00 |
| E^3_2 | untwisted | 1.4 | 2.5540e+00 | 3.9018e-01 | 2.1638e+00 | 4.3011e-01 | 2.1239e+00 |
| E^3_10 | untwisted | 0.25 | 1.6723e+00 | 6.4588e-02 | 1.6077e+00 | 7.7015e-02 | 1.5952e+00 |
| E^3_10 | untwisted | 0.5 | 3.3445e+00 | 9.0559e-02 | 3.2540e+00 | 8.7033e-02 | 3.2575e+00 |
| E^3_10 | untwisted | 1.0 | 6.6891e+00 | 1.0418e-01 | 6.5849e+00 | 8.3167e-02 | 6.6059e+00 |
| E^3_10 | untwisted | 1.4 | 9.3647e+00 | 1.0248e-01 | 9.2622e+00 | 8.1039e-02 | 9.2836e+00 |
| E^3'_6 | untwisted | 0.25 | 1.0642e+00 | 1.4871e-01 | 9.1546e-01 | 1.3642e-01 | 9.2775e-01 |
| E^3'_6 | untwisted | 0.5 | 2.1283e+00 | 1.7762e-01 | 1.9507e+00 | 1.6555e-01 | 1.9628e+00 |
| E^3'_6 | untwisted | 1.0 | 4.2567e+00 | 1.6027e-01 | 4.0964e+00 | 1.3504e-01 | 4.1216e+00 |
| E^3'_6 | untwisted | 1.4 | 5.9593e+00 | 1.7167e-01 | 5.7877e+00 | 1.2202e-01 | 5.8373e+00 |
| E^3'_10 | untwisted | 0.25 | 1.6723e+00 | 7.1653e-02 | 1.6006e+00 | 7.9171e-02 | 1.5931e+00 |
| E^3'_10 | untwisted | 0.5 | 3.3445e+00 | 1.1188e-01 | 3.2326e+00 | 1.2573e-01 | 3.2188e+00 |
| E^3'_10 | untwisted | 1.0 | 6.6891e+00 | 7.2881e-02 | 6.6162e+00 | 9.2021e-02 | 6.5970e+00 |
| E^3'_10 | untwisted | 1.4 | 9.3647e+00 | 8.2497e-02 | 9.2822e+00 | 9.0733e-02 | 9.2739e+00 |
| E^4_6 | untwisted | 0.25 | 1.4189e+00 | 1.1523e-01 | 1.3037e+00 | 1.2266e-01 | 1.2962e+00 |
| E^4_6 | untwisted | 0.5 | 2.8378e+00 | 1.4379e-01 | 2.6940e+00 | 1.4762e-01 | 2.6902e+00 |
| E^4_6 | untwisted | 1.0 | 5.6756e+00 | 1.6715e-01 | 5.5084e+00 | 2.1042e-01 | 5.4651e+00 |
| E^4_6 | untwisted | 1.4 | 7.9458e+00 | 1.6828e-01 | 7.7775e+00 | 2.1489e-01 | 7.7309e+00 |
| E^4_8 | untwisted | 0.25 | 1.8243e+00 | 1.3190e-01 | 1.6924e+00 | 1.1664e-01 | 1.7076e+00 |
| E^4_8 | untwisted | 0.5 | 3.6486e+00 | 1.3643e-01 | 3.5121e+00 | 1.5251e-01 | 3.4961e+00 |
| E^4_8 | untwisted | 1.0 | 7.2971e+00 | 1.2424e-01 | 7.1729e+00 | 1.5300e-01 | 7.1442e+00 |
| E^4_8 | untwisted | 1.4 | 1.0216e+01 | 1.3008e-01 | 1.0086e+01 | 1.5402e-01 | 1.0062e+01 |
| E^5_4 | untwisted | 0.25 | 1.2669e+00 | 2.1156e-01 | 1.0553e+00 | 2.1138e-01 | 1.0555e+00 |
| E^5_4 | untwisted | 0.5 | 2.5337e+00 | 3.1913e-01 | 2.2146e+00 | 3.1274e-01 | 2.2210e+00 |
| E^5_4 | untwisted | 1.0 | 5.0675e+00 | 3.3295e-01 | 4.7345e+00 | 3.3159e-01 | 4.7359e+00 |
| E^5_4 | untwisted | 1.4 | 7.0944e+00 | 3.5341e-01 | 6.7410e+00 | 3.6267e-01 | 6.7318e+00 |
| E^5_8 | untwisted | 0.25 | 2.2804e+00 | 1.6303e-01 | 2.1173e+00 | 1.6516e-01 | 2.1152e+00 |
| E^5_8 | untwisted | 0.5 | 4.5607e+00 | 1.8032e-01 | 4.3804e+00 | 1.6744e-01 | 4.3933e+00 |
| E^5_8 | untwisted | 1.0 | 9.1214e+00 | 2.0001e-01 | 8.9214e+00 | 1.6758e-01 | 8.9539e+00 |
| E^5_8 | untwisted | 1.4 | 1.2770e+01 | 2.0206e-01 | 1.2568e+01 | 1.6924e-01 | 1.2601e+01 |
| E^2_1 | twisted | 0.25 | 2.0270e-01 | 6.7993e-02 | 1.3471e-01 | N/A | N/A |
| E^2_1 | twisted | 0.5 | 4.0540e-01 | 1.3599e-01 | 2.6941e-01 | N/A | N/A |
| E^2_1 | twisted | 1.0 | 8.1079e-01 | 2.7197e-01 | 5.3882e-01 | N/A | N/A |
| E^2_1 | twisted | 1.4 | 1.1351e+00 | 3.8076e-01 | 7.5435e-01 | N/A | N/A |
| E^2_11 | twisted | 0.25 | 1.2162e+00 | 3.1815e-02 | 1.1844e+00 | N/A | N/A |
| E^2_11 | twisted | 0.5 | 2.4324e+00 | 2.6250e-02 | 2.4061e+00 | N/A | N/A |
| E^2_11 | twisted | 1.0 | 4.8648e+00 | 3.8279e-02 | 4.8265e+00 | N/A | N/A |
| E^2_11 | twisted | 1.4 | 6.8107e+00 | 4.9574e-02 | 6.7611e+00 | N/A | N/A |
| E^2'_7 | twisted | 0.25 | 8.1079e-01 | 8.4138e-02 | 7.2666e-01 | N/A | N/A |
| E^2'_7 | twisted | 0.5 | 1.6216e+00 | 1.1338e-01 | 1.5082e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.0 | 3.2432e+00 | 1.0184e-01 | 3.1413e+00 | N/A | N/A |
| E^2'_7 | twisted | 1.4 | 4.5404e+00 | 8.0762e-02 | 4.4597e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.25 | 1.4189e+00 | 4.7910e-02 | 1.3710e+00 | N/A | N/A |
| E^2'_13 | twisted | 0.5 | 2.8378e+00 | 3.2297e-02 | 2.8055e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.0 | 5.6756e+00 | 4.1760e-02 | 5.6338e+00 | N/A | N/A |
| E^2'_13 | twisted | 1.4 | 7.9458e+00 | 4.7458e-02 | 7.8983e+00 | N/A | N/A |
| E^4'_3 | twisted | 0.25 | 8.1079e-01 | 1.7363e-01 | 6.3717e-01 | N/A | N/A |
| E^4'_3 | twisted | 0.5 | 1.6216e+00 | 2.9244e-01 | 1.3291e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.0 | 3.2432e+00 | 3.2481e-01 | 2.9184e+00 | N/A | N/A |
| E^4'_3 | twisted | 1.4 | 4.5404e+00 | 3.1502e-01 | 4.2254e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.25 | 2.0270e+00 | 9.7731e-02 | 1.9293e+00 | N/A | N/A |
| E^4'_9 | twisted | 0.5 | 4.0540e+00 | 9.5524e-02 | 3.9584e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.0 | 8.1079e+00 | 1.0892e-01 | 7.9990e+00 | N/A | N/A |
| E^4'_9 | twisted | 1.4 | 1.1351e+01 | 1.2221e-01 | 1.1229e+01 | N/A | N/A |
| E^6_5 | twisted | 0.25 | 1.8243e+00 | 2.3934e-01 | 1.5850e+00 | N/A | N/A |
| E^6_5 | twisted | 0.5 | 3.6486e+00 | 3.2106e-01 | 3.3275e+00 | N/A | N/A |
| E^6_5 | twisted | 1.0 | 7.2971e+00 | 3.2564e-01 | 6.9715e+00 | N/A | N/A |
| E^6_5 | twisted | 1.4 | 1.0216e+01 | 3.1106e-01 | 9.9050e+00 | N/A | N/A |
| E^6_7 | twisted | 0.25 | 2.4324e+00 | 1.9723e-01 | 2.2352e+00 | N/A | N/A |
| E^6_7 | twisted | 0.5 | 4.8648e+00 | 2.0366e-01 | 4.6611e+00 | N/A | N/A |
| E^6_7 | twisted | 1.0 | 9.7295e+00 | 2.1886e-01 | 9.5107e+00 | N/A | N/A |
| E^6_7 | twisted | 1.4 | 1.3621e+01 | 2.3225e-01 | 1.3389e+01 | N/A | N/A |

### Transverse sampler O^(1)

**Placement: generic**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 3.6891e+01 | 1.9282e+00 | 3.4963e+01 | N/A | N/A |
| E^1_12 | twisted | 0.5 | 7.3782e+01 | 1.2179e+00 | 7.2564e+01 | N/A | N/A |
| E^1_12 | twisted | 1.0 | 1.4756e+02 | 3.2907e+00 | 1.4427e+02 | N/A | N/A |
| E^1_12 | twisted | 1.4 | 2.0659e+02 | 3.8516e+00 | 2.0274e+02 | N/A | N/A |
| E^1_20 | twisted | 0.25 | 1.5608e+02 | 1.0714e+01 | 1.4536e+02 | N/A | N/A |
| E^1_20 | twisted | 0.5 | 3.1216e+02 | 1.0032e+01 | 3.0212e+02 | N/A | N/A |
| E^1_20 | twisted | 1.0 | 6.2431e+02 | 7.0316e+00 | 6.1728e+02 | N/A | N/A |
| E^1_20 | twisted | 1.4 | 8.7404e+02 | 5.2303e+00 | 8.6881e+02 | N/A | N/A |
| E^3_2 | twisted | 0.25 | 1.2162e+00 | 4.0796e-01 | 8.0823e-01 | N/A | N/A |
| E^3_2 | twisted | 0.5 | 2.4324e+00 | 8.1592e-01 | 1.6165e+00 | N/A | N/A |
| E^3_2 | twisted | 1.0 | 4.8648e+00 | 1.6318e+00 | 3.2329e+00 | N/A | N/A |
| E^3_2 | twisted | 1.4 | 6.8107e+00 | 2.2846e+00 | 4.5261e+00 | N/A | N/A |
| E^3_10 | twisted | 0.25 | 6.6891e+01 | 4.7853e+00 | 6.2105e+01 | N/A | N/A |
| E^3_10 | twisted | 0.5 | 1.3378e+02 | 4.2548e+00 | 1.2953e+02 | N/A | N/A |
| E^3_10 | twisted | 1.0 | 2.6756e+02 | 8.4867e+00 | 2.5908e+02 | N/A | N/A |
| E^3_10 | twisted | 1.4 | 3.7459e+02 | 1.0465e+01 | 3.6412e+02 | N/A | N/A |
| E^3'_6 | twisted | 0.25 | 1.7027e+01 | 1.7523e+00 | 1.5274e+01 | N/A | N/A |
| E^3'_6 | twisted | 0.5 | 3.4053e+01 | 3.2190e+00 | 3.0834e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.0 | 6.8107e+01 | 5.5560e+00 | 6.2551e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.4 | 9.5349e+01 | 6.1538e+00 | 8.9196e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.25 | 6.6891e+01 | 9.6486e+00 | 5.7242e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.5 | 1.3378e+02 | 1.1241e+01 | 1.2254e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.0 | 2.6756e+02 | 9.9441e+00 | 2.5762e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.4 | 3.7459e+02 | 9.1614e+00 | 3.6543e+02 | N/A | N/A |
| E^4_6 | twisted | 0.25 | 2.2702e+01 | 4.9811e+00 | 1.7721e+01 | N/A | N/A |
| E^4_6 | twisted | 0.5 | 4.5404e+01 | 7.2738e+00 | 3.8131e+01 | N/A | N/A |
| E^4_6 | twisted | 1.0 | 9.0809e+01 | 7.3579e+00 | 8.3451e+01 | N/A | N/A |
| E^4_6 | twisted | 1.4 | 1.2713e+02 | 7.9419e+00 | 1.1919e+02 | N/A | N/A |
| E^4_8 | twisted | 0.25 | 4.8648e+01 | 7.6095e+00 | 4.1038e+01 | N/A | N/A |
| E^4_8 | twisted | 0.5 | 9.7295e+01 | 1.1325e+01 | 8.5970e+01 | N/A | N/A |
| E^4_8 | twisted | 1.0 | 1.9459e+02 | 1.0510e+01 | 1.8408e+02 | N/A | N/A |
| E^4_8 | twisted | 1.4 | 2.7243e+02 | 1.0077e+01 | 2.6235e+02 | N/A | N/A |
| E^5_4 | twisted | 0.25 | 1.0135e+01 | 2.4162e+00 | 7.7187e+00 | N/A | N/A |
| E^5_4 | twisted | 0.5 | 2.0270e+01 | 4.2843e+00 | 1.5986e+01 | N/A | N/A |
| E^5_4 | twisted | 1.0 | 4.0540e+01 | 5.9678e+00 | 3.4572e+01 | N/A | N/A |
| E^5_4 | twisted | 1.4 | 5.6756e+01 | 6.9578e+00 | 4.9798e+01 | N/A | N/A |
| E^5_8 | twisted | 0.25 | 6.0810e+01 | 6.1123e+00 | 5.4697e+01 | N/A | N/A |
| E^5_8 | twisted | 0.5 | 1.2162e+02 | 7.8722e+00 | 1.1375e+02 | N/A | N/A |
| E^5_8 | twisted | 1.0 | 2.4324e+02 | 1.1866e+01 | 2.3137e+02 | N/A | N/A |
| E^5_8 | twisted | 1.4 | 3.4053e+02 | 1.3681e+01 | 3.2685e+02 | N/A | N/A |
| E^2_1 | untwisted | 0.25 | 2.0270e-01 | 0 | 2.0270e-01 | 1.2198e-06 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0540e-01 | 0 | 4.0540e-01 | 2.4395e-06 | 4.0539e-01 |
| E^2_1 | untwisted | 1.0 | 8.1079e-01 | 0 | 8.1079e-01 | 0 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1351e+00 | 0 | 1.1351e+00 | 0 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 5.7972e+01 | 3.6877e+00 | 5.4284e+01 | 5.3956e+00 | 5.2576e+01 |
| E^2_11 | untwisted | 0.5 | 1.1594e+02 | 3.6349e+00 | 1.1231e+02 | 5.4863e+00 | 1.1046e+02 |
| E^2_11 | untwisted | 1.0 | 2.3189e+02 | 8.1540e+00 | 2.2373e+02 | 6.1347e+00 | 2.2575e+02 |
| E^2_11 | untwisted | 1.4 | 3.2464e+02 | 7.1915e+00 | 3.1745e+02 | 8.2195e+00 | 3.1642e+02 |
| E^2'_7 | untwisted | 0.25 | 1.7027e+01 | 2.1354e+00 | 1.4891e+01 | 2.6161e+00 | 1.4411e+01 |
| E^2'_7 | untwisted | 0.5 | 3.4053e+01 | 3.1678e+00 | 3.0886e+01 | 3.0164e+00 | 3.1037e+01 |
| E^2'_7 | untwisted | 1.0 | 6.8107e+01 | 4.2156e+00 | 6.3891e+01 | 4.5208e+00 | 6.3586e+01 |
| E^2'_7 | untwisted | 1.4 | 9.5349e+01 | 4.0122e+00 | 9.1337e+01 | 3.9432e+00 | 9.1406e+01 |
| E^2'_13 | untwisted | 0.25 | 9.2228e+01 | 7.9515e+00 | 8.4276e+01 | 7.2438e+00 | 8.4984e+01 |
| E^2'_13 | untwisted | 0.5 | 1.8446e+02 | 8.6748e+00 | 1.7578e+02 | 7.8414e+00 | 1.7661e+02 |
| E^2'_13 | untwisted | 1.0 | 3.6891e+02 | 8.2435e+00 | 3.6067e+02 | 7.8930e+00 | 3.6102e+02 |
| E^2'_13 | untwisted | 1.4 | 5.1648e+02 | 6.8333e+00 | 5.0964e+02 | 7.2748e+00 | 5.0920e+02 |
| E^4'_3 | untwisted | 0.25 | 4.0540e+00 | 1.1018e+00 | 2.9522e+00 | 8.4970e-01 | 3.2043e+00 |
| E^4'_3 | untwisted | 0.5 | 8.1079e+00 | 2.0686e+00 | 6.0393e+00 | 1.6085e+00 | 6.4994e+00 |
| E^4'_3 | untwisted | 1.0 | 1.6216e+01 | 3.1863e+00 | 1.3030e+01 | 3.0491e+00 | 1.3167e+01 |
| E^4'_3 | untwisted | 1.4 | 2.2702e+01 | 3.1214e+00 | 1.9581e+01 | 3.4409e+00 | 1.9261e+01 |
| E^4'_9 | untwisted | 0.25 | 6.6891e+01 | 6.7981e+00 | 6.0092e+01 | 6.7437e+00 | 6.0147e+01 |
| E^4'_9 | untwisted | 0.5 | 1.3378e+02 | 8.6423e+00 | 1.2514e+02 | 9.3583e+00 | 1.2442e+02 |
| E^4'_9 | untwisted | 1.0 | 2.6756e+02 | 1.1677e+01 | 2.5588e+02 | 1.0304e+01 | 2.5726e+02 |
| E^4'_9 | untwisted | 1.4 | 3.7459e+02 | 1.1945e+01 | 3.6264e+02 | 1.2845e+01 | 3.6174e+02 |
| E^6_5 | untwisted | 0.25 | 2.1283e+01 | 4.1914e+00 | 1.7092e+01 | 3.8111e+00 | 1.7472e+01 |
| E^6_5 | untwisted | 0.5 | 4.2567e+01 | 6.9325e+00 | 3.5634e+01 | 6.1657e+00 | 3.6401e+01 |
| E^6_5 | untwisted | 1.0 | 8.5133e+01 | 8.7749e+00 | 7.6359e+01 | 8.5528e+00 | 7.6581e+01 |
| E^6_5 | untwisted | 1.4 | 1.1919e+02 | 8.9231e+00 | 1.1026e+02 | 9.5134e+00 | 1.0967e+02 |
| E^6_7 | untwisted | 0.25 | 5.1080e+01 | 7.6762e+00 | 4.3404e+01 | 6.6106e+00 | 4.4469e+01 |
| E^6_7 | untwisted | 0.5 | 1.0216e+02 | 1.1218e+01 | 9.0942e+01 | 1.0215e+01 | 9.1945e+01 |
| E^6_7 | untwisted | 1.0 | 2.0432e+02 | 1.2723e+01 | 1.9160e+02 | 1.2410e+01 | 1.9191e+02 |
| E^6_7 | untwisted | 1.4 | 2.8605e+02 | 1.3324e+01 | 2.7272e+02 | 1.4132e+01 | 2.7192e+02 |

**Placement: 2fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 3.6891e+01 | 1.6680e-01 | 3.6724e+01 | N/A | N/A |
| E^1_12 | twisted | 0.5 | 7.3782e+01 | 2.7146e+00 | 7.1068e+01 | N/A | N/A |
| E^1_12 | twisted | 1.0 | 1.4756e+02 | 6.8569e+00 | 1.4071e+02 | N/A | N/A |
| E^1_12 | twisted | 1.4 | 2.0659e+02 | 6.0253e+00 | 2.0057e+02 | N/A | N/A |
| E^1_20 | twisted | 0.25 | 1.5608e+02 | 5.6399e+00 | 1.5044e+02 | N/A | N/A |
| E^1_20 | twisted | 0.5 | 3.1216e+02 | 6.9170e+00 | 3.0524e+02 | N/A | N/A |
| E^1_20 | twisted | 1.0 | 6.2431e+02 | 3.7791e+00 | 6.2053e+02 | N/A | N/A |
| E^1_20 | twisted | 1.4 | 8.7404e+02 | 6.1295e+00 | 8.6791e+02 | N/A | N/A |
| E^3_2 | twisted | 0.25 | 1.2162e+00 | 4.0796e-01 | 8.0823e-01 | N/A | N/A |
| E^3_2 | twisted | 0.5 | 2.4324e+00 | 8.1592e-01 | 1.6165e+00 | N/A | N/A |
| E^3_2 | twisted | 1.0 | 4.8648e+00 | 1.6318e+00 | 3.2329e+00 | N/A | N/A |
| E^3_2 | twisted | 1.4 | 6.8107e+00 | 2.2846e+00 | 4.5261e+00 | N/A | N/A |
| E^3_10 | twisted | 0.25 | 6.6891e+01 | 5.3786e+00 | 6.1512e+01 | N/A | N/A |
| E^3_10 | twisted | 0.5 | 1.3378e+02 | 8.5934e+00 | 1.2519e+02 | N/A | N/A |
| E^3_10 | twisted | 1.0 | 2.6756e+02 | 1.4424e+01 | 2.5314e+02 | N/A | N/A |
| E^3_10 | twisted | 1.4 | 3.7459e+02 | 1.2541e+01 | 3.6205e+02 | N/A | N/A |
| E^3'_6 | twisted | 0.25 | 1.7027e+01 | 4.6411e+00 | 1.2386e+01 | N/A | N/A |
| E^3'_6 | twisted | 0.5 | 3.4053e+01 | 6.4397e+00 | 2.7614e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.0 | 6.8107e+01 | 5.9021e+00 | 6.2205e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.4 | 9.5349e+01 | 6.3613e+00 | 8.8988e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.25 | 6.6891e+01 | 4.0475e+00 | 6.2843e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.5 | 1.3378e+02 | 8.2278e+00 | 1.2555e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.0 | 2.6756e+02 | 6.2993e+00 | 2.6126e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.4 | 3.7459e+02 | 8.6466e+00 | 3.6594e+02 | N/A | N/A |
| E^4_6 | twisted | 0.25 | 2.2702e+01 | 2.0922e+00 | 2.0610e+01 | N/A | N/A |
| E^4_6 | twisted | 0.5 | 4.5404e+01 | 4.0532e+00 | 4.1351e+01 | N/A | N/A |
| E^4_6 | twisted | 1.0 | 9.0809e+01 | 7.0118e+00 | 8.3797e+01 | N/A | N/A |
| E^4_6 | twisted | 1.4 | 1.2713e+02 | 7.7344e+00 | 1.1940e+02 | N/A | N/A |
| E^4_8 | twisted | 0.25 | 4.8648e+01 | 5.1705e+00 | 4.3477e+01 | N/A | N/A |
| E^4_8 | twisted | 0.5 | 9.7295e+01 | 7.3570e+00 | 8.9938e+01 | N/A | N/A |
| E^4_8 | twisted | 1.0 | 1.9459e+02 | 7.0468e+00 | 1.8754e+02 | N/A | N/A |
| E^4_8 | twisted | 1.4 | 2.7243e+02 | 8.9784e+00 | 2.6345e+02 | N/A | N/A |
| E^5_4 | twisted | 0.25 | 1.0135e+01 | 2.4162e+00 | 7.7187e+00 | N/A | N/A |
| E^5_4 | twisted | 0.5 | 2.0270e+01 | 4.2843e+00 | 1.5986e+01 | N/A | N/A |
| E^5_4 | twisted | 1.0 | 4.0540e+01 | 5.9678e+00 | 3.4572e+01 | N/A | N/A |
| E^5_4 | twisted | 1.4 | 5.6756e+01 | 6.9578e+00 | 4.9798e+01 | N/A | N/A |
| E^5_8 | twisted | 0.25 | 6.0810e+01 | 8.5513e+00 | 5.2258e+01 | N/A | N/A |
| E^5_8 | twisted | 0.5 | 1.2162e+02 | 1.1841e+01 | 1.0978e+02 | N/A | N/A |
| E^5_8 | twisted | 1.0 | 2.4324e+02 | 1.5329e+01 | 2.2791e+02 | N/A | N/A |
| E^5_8 | twisted | 1.4 | 3.4053e+02 | 1.4779e+01 | 3.2575e+02 | N/A | N/A |
| E^2_1 | untwisted | 0.25 | 2.0270e-01 | 0 | 2.0270e-01 | 1.2198e-06 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0540e-01 | 0 | 4.0540e-01 | 2.4395e-06 | 4.0539e-01 |
| E^2_1 | untwisted | 1.0 | 8.1079e-01 | 0 | 8.1079e-01 | 0 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1351e+00 | 0 | 1.1351e+00 | 0 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 5.7972e+01 | 4.6228e+00 | 5.3349e+01 | 5.9029e+00 | 5.2069e+01 |
| E^2_11 | untwisted | 0.5 | 1.1594e+02 | 4.5142e+00 | 1.1143e+02 | 1.1221e+01 | 1.0472e+02 |
| E^2_11 | untwisted | 1.0 | 2.3189e+02 | 7.4501e+00 | 2.2444e+02 | 9.4831e+00 | 2.2240e+02 |
| E^2_11 | untwisted | 1.4 | 3.2464e+02 | 8.7737e+00 | 3.1587e+02 | 6.0583e+00 | 3.1858e+02 |
| E^2'_7 | untwisted | 0.25 | 1.7027e+01 | 2.4276e+00 | 1.4599e+01 | 7.2593e-01 | 1.6301e+01 |
| E^2'_7 | untwisted | 0.5 | 3.4053e+01 | 4.5838e+00 | 2.9470e+01 | 1.2922e+00 | 3.2761e+01 |
| E^2'_7 | untwisted | 1.0 | 6.8107e+01 | 5.0512e+00 | 6.3056e+01 | 2.3976e+00 | 6.5709e+01 |
| E^2'_7 | untwisted | 1.4 | 9.5349e+01 | 2.7978e+00 | 9.2552e+01 | 5.4635e+00 | 8.9886e+01 |
| E^2'_13 | untwisted | 0.25 | 9.2228e+01 | 8.7797e+00 | 8.3448e+01 | 6.9450e+00 | 8.5283e+01 |
| E^2'_13 | untwisted | 0.5 | 1.8446e+02 | 9.3924e+00 | 1.7506e+02 | 3.2752e+00 | 1.8118e+02 |
| E^2'_13 | untwisted | 1.0 | 3.6891e+02 | 5.1652e+00 | 3.6375e+02 | 6.3365e+00 | 3.6257e+02 |
| E^2'_13 | untwisted | 1.4 | 5.1648e+02 | 7.0418e+00 | 5.0943e+02 | 1.0349e+01 | 5.0613e+02 |
| E^4'_3 | untwisted | 0.25 | 4.0540e+00 | 1.1018e+00 | 2.9522e+00 | 8.4970e-01 | 3.2043e+00 |
| E^4'_3 | untwisted | 0.5 | 8.1079e+00 | 2.0686e+00 | 6.0393e+00 | 1.6085e+00 | 6.4994e+00 |
| E^4'_3 | untwisted | 1.0 | 1.6216e+01 | 3.1863e+00 | 1.3030e+01 | 3.0491e+00 | 1.3167e+01 |
| E^4'_3 | untwisted | 1.4 | 2.2702e+01 | 3.1214e+00 | 1.9581e+01 | 3.4409e+00 | 1.9261e+01 |
| E^4'_9 | untwisted | 0.25 | 6.6891e+01 | 6.6589e+00 | 6.0232e+01 | 8.5426e+00 | 5.8348e+01 |
| E^4'_9 | untwisted | 0.5 | 1.3378e+02 | 7.9039e+00 | 1.2588e+02 | 1.3065e+01 | 1.2072e+02 |
| E^4'_9 | untwisted | 1.0 | 2.6756e+02 | 1.1125e+01 | 2.5644e+02 | 1.4020e+01 | 2.5354e+02 |
| E^4'_9 | untwisted | 1.4 | 3.7459e+02 | 1.3875e+01 | 3.6071e+02 | 9.9389e+00 | 3.6465e+02 |
| E^6_5 | untwisted | 0.25 | 2.1283e+01 | 4.1914e+00 | 1.7092e+01 | 3.8111e+00 | 1.7472e+01 |
| E^6_5 | untwisted | 0.5 | 4.2567e+01 | 6.9325e+00 | 3.5634e+01 | 6.1657e+00 | 3.6401e+01 |
| E^6_5 | untwisted | 1.0 | 8.5133e+01 | 8.7749e+00 | 7.6359e+01 | 8.5528e+00 | 7.6581e+01 |
| E^6_5 | untwisted | 1.4 | 1.1919e+02 | 8.9231e+00 | 1.1026e+02 | 9.5134e+00 | 1.0967e+02 |
| E^6_7 | untwisted | 0.25 | 5.1080e+01 | 7.3840e+00 | 4.3696e+01 | 8.5008e+00 | 4.2579e+01 |
| E^6_7 | untwisted | 0.5 | 1.0216e+02 | 9.8020e+00 | 9.2358e+01 | 1.1939e+01 | 9.0221e+01 |
| E^6_7 | untwisted | 1.0 | 2.0432e+02 | 1.1887e+01 | 1.9243e+02 | 1.4533e+01 | 1.8979e+02 |
| E^6_7 | untwisted | 1.4 | 2.8605e+02 | 1.4539e+01 | 2.7151e+02 | 1.2611e+01 | 2.7344e+02 |

**Placement: 3fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 3.6891e+01 | 1.8307e+00 | 3.5060e+01 | N/A | N/A |
| E^1_12 | twisted | 0.5 | 7.3782e+01 | 2.5762e+00 | 7.1206e+01 | N/A | N/A |
| E^1_12 | twisted | 1.0 | 1.4756e+02 | 3.8277e+00 | 1.4374e+02 | N/A | N/A |
| E^1_12 | twisted | 1.4 | 2.0659e+02 | 3.5524e+00 | 2.0304e+02 | N/A | N/A |
| E^1_20 | twisted | 0.25 | 1.5608e+02 | 5.6941e+00 | 1.5038e+02 | N/A | N/A |
| E^1_20 | twisted | 0.5 | 3.1216e+02 | 4.4472e+00 | 3.0771e+02 | N/A | N/A |
| E^1_20 | twisted | 1.0 | 6.2431e+02 | 5.9649e+00 | 6.1835e+02 | N/A | N/A |
| E^1_20 | twisted | 1.4 | 8.7404e+02 | 6.1927e+00 | 8.6784e+02 | N/A | N/A |
| E^3_2 | twisted | 0.25 | 1.2162e+00 | 4.0796e-01 | 8.0823e-01 | N/A | N/A |
| E^3_2 | twisted | 0.5 | 2.4324e+00 | 8.1592e-01 | 1.6165e+00 | N/A | N/A |
| E^3_2 | twisted | 1.0 | 4.8648e+00 | 1.6318e+00 | 3.2329e+00 | N/A | N/A |
| E^3_2 | twisted | 1.4 | 6.8107e+00 | 2.2846e+00 | 4.5261e+00 | N/A | N/A |
| E^3_10 | twisted | 0.25 | 6.6891e+01 | 6.0254e+00 | 6.0865e+01 | N/A | N/A |
| E^3_10 | twisted | 0.5 | 1.3378e+02 | 9.3879e+00 | 1.2439e+02 | N/A | N/A |
| E^3_10 | twisted | 1.0 | 2.6756e+02 | 9.9111e+00 | 2.5765e+02 | N/A | N/A |
| E^3_10 | twisted | 1.4 | 3.7459e+02 | 9.6729e+00 | 3.6491e+02 | N/A | N/A |
| E^3'_6 | twisted | 0.25 | 1.7027e+01 | 3.9233e+00 | 1.3103e+01 | N/A | N/A |
| E^3'_6 | twisted | 0.5 | 3.4053e+01 | 5.6441e+00 | 2.8409e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.0 | 6.8107e+01 | 5.6546e+00 | 6.2452e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.4 | 9.5349e+01 | 6.0457e+00 | 8.9304e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.25 | 6.6891e+01 | 4.3290e+00 | 6.2562e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.5 | 1.3378e+02 | 6.5604e+00 | 1.2722e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.0 | 2.6756e+02 | 8.2929e+00 | 2.5927e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.4 | 3.7459e+02 | 9.5689e+00 | 3.6502e+02 | N/A | N/A |
| E^4_6 | twisted | 0.25 | 2.2702e+01 | 2.8101e+00 | 1.9892e+01 | N/A | N/A |
| E^4_6 | twisted | 0.5 | 4.5404e+01 | 4.8487e+00 | 4.0556e+01 | N/A | N/A |
| E^4_6 | twisted | 1.0 | 9.0809e+01 | 7.2593e+00 | 8.3550e+01 | N/A | N/A |
| E^4_6 | twisted | 1.4 | 1.2713e+02 | 8.0499e+00 | 1.1908e+02 | N/A | N/A |
| E^4_8 | twisted | 0.25 | 4.8648e+01 | 5.4114e+00 | 4.3236e+01 | N/A | N/A |
| E^4_8 | twisted | 0.5 | 9.7295e+01 | 7.2894e+00 | 9.0006e+01 | N/A | N/A |
| E^4_8 | twisted | 1.0 | 1.9459e+02 | 9.3236e+00 | 1.8527e+02 | N/A | N/A |
| E^4_8 | twisted | 1.4 | 2.7243e+02 | 1.0604e+01 | 2.6182e+02 | N/A | N/A |
| E^5_4 | twisted | 0.25 | 1.0135e+01 | 2.4162e+00 | 7.7187e+00 | N/A | N/A |
| E^5_4 | twisted | 0.5 | 2.0270e+01 | 4.2843e+00 | 1.5986e+01 | N/A | N/A |
| E^5_4 | twisted | 1.0 | 4.0540e+01 | 5.9678e+00 | 3.4572e+01 | N/A | N/A |
| E^5_4 | twisted | 1.4 | 5.6756e+01 | 6.9578e+00 | 4.9798e+01 | N/A | N/A |
| E^5_8 | twisted | 0.25 | 6.0810e+01 | 8.3104e+00 | 5.2499e+01 | N/A | N/A |
| E^5_8 | twisted | 0.5 | 1.2162e+02 | 1.1908e+01 | 1.0971e+02 | N/A | N/A |
| E^5_8 | twisted | 1.0 | 2.4324e+02 | 1.3052e+01 | 2.3019e+02 | N/A | N/A |
| E^5_8 | twisted | 1.4 | 3.4053e+02 | 1.3153e+01 | 3.2738e+02 | N/A | N/A |
| E^2_1 | untwisted | 0.25 | 2.0270e-01 | 0 | 2.0270e-01 | 1.2198e-06 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0540e-01 | 0 | 4.0540e-01 | 2.4395e-06 | 4.0539e-01 |
| E^2_1 | untwisted | 1.0 | 8.1079e-01 | 0 | 8.1079e-01 | 0 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1351e+00 | 0 | 1.1351e+00 | 0 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 5.7972e+01 | 5.5581e+00 | 5.2414e+01 | 4.6037e+00 | 5.3368e+01 |
| E^2_11 | untwisted | 0.5 | 1.1594e+02 | 7.0206e+00 | 1.0892e+02 | 6.3104e+00 | 1.0963e+02 |
| E^2_11 | untwisted | 1.0 | 2.3189e+02 | 6.1153e+00 | 2.2577e+02 | 8.3627e+00 | 2.2352e+02 |
| E^2_11 | untwisted | 1.4 | 3.2464e+02 | 6.5204e+00 | 3.1812e+02 | 5.6274e+00 | 3.1901e+02 |
| E^2'_7 | untwisted | 0.25 | 1.7027e+01 | 2.4030e+00 | 1.4624e+01 | 1.4895e+00 | 1.5537e+01 |
| E^2'_7 | untwisted | 0.5 | 3.4053e+01 | 3.8781e+00 | 3.0175e+01 | 2.7308e+00 | 3.1323e+01 |
| E^2'_7 | untwisted | 1.0 | 6.8107e+01 | 4.8812e+00 | 6.3226e+01 | 3.4902e+00 | 6.4617e+01 |
| E^2'_7 | untwisted | 1.4 | 9.5349e+01 | 4.7714e+00 | 9.0578e+01 | 5.0426e+00 | 9.0307e+01 |
| E^2'_13 | untwisted | 0.25 | 9.2228e+01 | 7.3251e+00 | 8.4903e+01 | 6.2966e+00 | 8.5931e+01 |
| E^2'_13 | untwisted | 0.5 | 1.8446e+02 | 7.4758e+00 | 1.7698e+02 | 6.7534e+00 | 1.7770e+02 |
| E^2'_13 | untwisted | 1.0 | 3.6891e+02 | 9.6991e+00 | 3.5921e+02 | 7.1275e+00 | 3.6178e+02 |
| E^2'_13 | untwisted | 1.4 | 5.1648e+02 | 9.0363e+00 | 5.0744e+02 | 8.9412e+00 | 5.0753e+02 |
| E^4'_3 | untwisted | 0.25 | 4.0540e+00 | 1.1018e+00 | 2.9522e+00 | 8.4970e-01 | 3.2043e+00 |
| E^4'_3 | untwisted | 0.5 | 8.1079e+00 | 2.0686e+00 | 6.0393e+00 | 1.6085e+00 | 6.4994e+00 |
| E^4'_3 | untwisted | 1.0 | 1.6216e+01 | 3.1863e+00 | 1.3030e+01 | 3.0491e+00 | 1.3167e+01 |
| E^4'_3 | untwisted | 1.4 | 2.2702e+01 | 3.1214e+00 | 1.9581e+01 | 3.4409e+00 | 1.9261e+01 |
| E^4'_9 | untwisted | 0.25 | 6.6891e+01 | 7.1536e+00 | 5.9737e+01 | 7.5154e+00 | 5.9375e+01 |
| E^4'_9 | untwisted | 0.5 | 1.3378e+02 | 9.7091e+00 | 1.2407e+02 | 9.6971e+00 | 1.2408e+02 |
| E^4'_9 | untwisted | 1.0 | 2.6756e+02 | 9.7560e+00 | 2.5781e+02 | 1.2724e+01 | 2.5484e+02 |
| E^4'_9 | untwisted | 1.4 | 3.7459e+02 | 1.0528e+01 | 3.6406e+02 | 1.0445e+01 | 3.6414e+02 |
| E^6_5 | untwisted | 0.25 | 2.1283e+01 | 4.1914e+00 | 1.7092e+01 | 3.8111e+00 | 1.7472e+01 |
| E^6_5 | untwisted | 0.5 | 4.2567e+01 | 6.9325e+00 | 3.5634e+01 | 6.1657e+00 | 3.6401e+01 |
| E^6_5 | untwisted | 1.0 | 8.5133e+01 | 8.7749e+00 | 7.6359e+01 | 8.5528e+00 | 7.6581e+01 |
| E^6_5 | untwisted | 1.4 | 1.1919e+02 | 8.9231e+00 | 1.1026e+02 | 9.5134e+00 | 1.0967e+02 |
| E^6_7 | untwisted | 0.25 | 5.1080e+01 | 7.4086e+00 | 4.3671e+01 | 7.7373e+00 | 4.3343e+01 |
| E^6_7 | untwisted | 0.5 | 1.0216e+02 | 1.0508e+01 | 9.1652e+01 | 1.0501e+01 | 9.1659e+01 |
| E^6_7 | untwisted | 1.0 | 2.0432e+02 | 1.2057e+01 | 1.9226e+02 | 1.3441e+01 | 1.9088e+02 |
| E^6_7 | untwisted | 1.4 | 2.8605e+02 | 1.2565e+01 | 2.7348e+02 | 1.3032e+01 | 2.7302e+02 |

**Placement: 5fold**

| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |
|---|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 3.6891e+01 | 1.8724e+00 | 3.5019e+01 | N/A | N/A |
| E^1_12 | twisted | 0.5 | 7.3782e+01 | 1.9174e+00 | 7.1865e+01 | N/A | N/A |
| E^1_12 | twisted | 1.0 | 1.4756e+02 | 2.8516e+00 | 1.4471e+02 | N/A | N/A |
| E^1_12 | twisted | 1.4 | 2.0659e+02 | 3.7196e+00 | 2.0287e+02 | N/A | N/A |
| E^1_20 | twisted | 0.25 | 1.5608e+02 | 3.2902e+00 | 1.5279e+02 | N/A | N/A |
| E^1_20 | twisted | 0.5 | 3.1216e+02 | 6.3578e+00 | 3.0580e+02 | N/A | N/A |
| E^1_20 | twisted | 1.0 | 6.2431e+02 | 6.0803e+00 | 6.1823e+02 | N/A | N/A |
| E^1_20 | twisted | 1.4 | 8.7404e+02 | 6.1061e+00 | 8.6793e+02 | N/A | N/A |
| E^3_2 | twisted | 0.25 | 1.2162e+00 | 4.0796e-01 | 8.0823e-01 | N/A | N/A |
| E^3_2 | twisted | 0.5 | 2.4324e+00 | 8.1592e-01 | 1.6165e+00 | N/A | N/A |
| E^3_2 | twisted | 1.0 | 4.8648e+00 | 1.6318e+00 | 3.2329e+00 | N/A | N/A |
| E^3_2 | twisted | 1.4 | 6.8107e+00 | 2.2846e+00 | 4.5261e+00 | N/A | N/A |
| E^3_10 | twisted | 0.25 | 6.6891e+01 | 3.8513e+00 | 6.3039e+01 | N/A | N/A |
| E^3_10 | twisted | 0.5 | 1.3378e+02 | 5.8899e+00 | 1.2789e+02 | N/A | N/A |
| E^3_10 | twisted | 1.0 | 2.6756e+02 | 7.6911e+00 | 2.5987e+02 | N/A | N/A |
| E^3_10 | twisted | 1.4 | 3.7459e+02 | 9.5323e+00 | 3.6505e+02 | N/A | N/A |
| E^3'_6 | twisted | 0.25 | 1.7027e+01 | 2.0047e+00 | 1.5022e+01 | N/A | N/A |
| E^3'_6 | twisted | 0.5 | 3.4053e+01 | 3.3676e+00 | 3.0686e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.0 | 6.8107e+01 | 4.8977e+00 | 6.3209e+01 | N/A | N/A |
| E^3'_6 | twisted | 1.4 | 9.5349e+01 | 5.9401e+00 | 8.9409e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.25 | 6.6891e+01 | 4.8592e+00 | 6.2031e+01 | N/A | N/A |
| E^3'_10 | twisted | 0.5 | 1.3378e+02 | 9.5165e+00 | 1.2426e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.0 | 2.6756e+02 | 9.6639e+00 | 2.5790e+02 | N/A | N/A |
| E^3'_10 | twisted | 1.4 | 3.7459e+02 | 1.0107e+01 | 3.6448e+02 | N/A | N/A |
| E^4_6 | twisted | 0.25 | 2.2702e+01 | 4.7287e+00 | 1.7974e+01 | N/A | N/A |
| E^4_6 | twisted | 0.5 | 4.5404e+01 | 7.1253e+00 | 3.8279e+01 | N/A | N/A |
| E^4_6 | twisted | 1.0 | 9.0809e+01 | 8.0162e+00 | 8.2793e+01 | N/A | N/A |
| E^4_6 | twisted | 1.4 | 1.2713e+02 | 8.1555e+00 | 1.1898e+02 | N/A | N/A |
| E^4_8 | twisted | 0.25 | 4.8648e+01 | 7.1930e+00 | 4.1455e+01 | N/A | N/A |
| E^4_8 | twisted | 0.5 | 9.7295e+01 | 1.0405e+01 | 8.6890e+01 | N/A | N/A |
| E^4_8 | twisted | 1.0 | 1.9459e+02 | 1.1166e+01 | 1.8343e+02 | N/A | N/A |
| E^4_8 | twisted | 1.4 | 2.7243e+02 | 1.0760e+01 | 2.6167e+02 | N/A | N/A |
| E^5_4 | twisted | 0.25 | 1.0135e+01 | 2.4162e+00 | 7.7187e+00 | N/A | N/A |
| E^5_4 | twisted | 0.5 | 2.0270e+01 | 4.2843e+00 | 1.5986e+01 | N/A | N/A |
| E^5_4 | twisted | 1.0 | 4.0540e+01 | 5.9678e+00 | 3.4572e+01 | N/A | N/A |
| E^5_4 | twisted | 1.4 | 5.6756e+01 | 6.9578e+00 | 4.9798e+01 | N/A | N/A |
| E^5_8 | twisted | 0.25 | 6.0810e+01 | 6.5287e+00 | 5.4281e+01 | N/A | N/A |
| E^5_8 | twisted | 0.5 | 1.2162e+02 | 8.7922e+00 | 1.1283e+02 | N/A | N/A |
| E^5_8 | twisted | 1.0 | 2.4324e+02 | 1.1210e+01 | 2.3203e+02 | N/A | N/A |
| E^5_8 | twisted | 1.4 | 3.4053e+02 | 1.2997e+01 | 3.2754e+02 | N/A | N/A |
| E^2_1 | untwisted | 0.25 | 2.0270e-01 | 0 | 2.0270e-01 | 1.2198e-06 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0540e-01 | 0 | 4.0540e-01 | 2.4395e-06 | 4.0539e-01 |
| E^2_1 | untwisted | 1.0 | 8.1079e-01 | 0 | 8.1079e-01 | 0 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1351e+00 | 0 | 1.1351e+00 | 0 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 5.7972e+01 | 4.2674e+00 | 5.3704e+01 | 2.9316e+00 | 5.5040e+01 |
| E^2_11 | untwisted | 0.5 | 1.1594e+02 | 6.6016e+00 | 1.0934e+02 | 5.3535e+00 | 1.1059e+02 |
| E^2_11 | untwisted | 1.0 | 2.3189e+02 | 8.7139e+00 | 2.2317e+02 | 6.8676e+00 | 2.2502e+02 |
| E^2_11 | untwisted | 1.4 | 3.2464e+02 | 8.5915e+00 | 3.1605e+02 | 6.8101e+00 | 3.1783e+02 |
| E^2'_7 | untwisted | 0.25 | 1.7027e+01 | 2.0153e+00 | 1.5011e+01 | 2.6321e+00 | 1.4395e+01 |
| E^2'_7 | untwisted | 0.5 | 3.4053e+01 | 2.6707e+00 | 3.1383e+01 | 3.7449e+00 | 3.0308e+01 |
| E^2'_7 | untwisted | 1.0 | 6.8107e+01 | 3.3417e+00 | 6.4765e+01 | 4.2807e+00 | 6.3826e+01 |
| E^2'_7 | untwisted | 1.4 | 9.5349e+01 | 3.3295e+00 | 9.2020e+01 | 4.8822e+00 | 9.0467e+01 |
| E^2'_13 | untwisted | 0.25 | 9.2228e+01 | 7.3188e+00 | 8.4909e+01 | 3.4184e+00 | 8.8809e+01 |
| E^2'_13 | untwisted | 0.5 | 1.8446e+02 | 9.6341e+00 | 1.7482e+02 | 7.7571e+00 | 1.7670e+02 |
| E^2'_13 | untwisted | 1.0 | 3.6891e+02 | 7.5729e+00 | 3.6134e+02 | 8.2230e+00 | 3.6069e+02 |
| E^2'_13 | untwisted | 1.4 | 5.1648e+02 | 8.0476e+00 | 5.0843e+02 | 9.1015e+00 | 5.0737e+02 |
| E^4'_3 | untwisted | 0.25 | 4.0540e+00 | 1.1018e+00 | 2.9522e+00 | 8.4970e-01 | 3.2043e+00 |
| E^4'_3 | untwisted | 0.5 | 8.1079e+00 | 2.0686e+00 | 6.0393e+00 | 1.6085e+00 | 6.4994e+00 |
| E^4'_3 | untwisted | 1.0 | 1.6216e+01 | 3.1863e+00 | 1.3030e+01 | 3.0491e+00 | 1.3167e+01 |
| E^4'_3 | untwisted | 1.4 | 2.2702e+01 | 3.1214e+00 | 1.9581e+01 | 3.4409e+00 | 1.9261e+01 |
| E^4'_9 | untwisted | 0.25 | 6.6891e+01 | 7.2457e+00 | 5.9645e+01 | 6.3435e+00 | 6.0547e+01 |
| E^4'_9 | untwisted | 0.5 | 1.3378e+02 | 1.0164e+01 | 1.2362e+02 | 8.0834e+00 | 1.2570e+02 |
| E^4'_9 | untwisted | 1.0 | 2.6756e+02 | 1.3028e+01 | 2.5453e+02 | 1.0745e+01 | 2.5682e+02 |
| E^4'_9 | untwisted | 1.4 | 3.7459e+02 | 1.2997e+01 | 3.6159e+02 | 1.1100e+01 | 3.6349e+02 |
| E^6_5 | untwisted | 0.25 | 2.1283e+01 | 4.1914e+00 | 1.7092e+01 | 3.8111e+00 | 1.7472e+01 |
| E^6_5 | untwisted | 0.5 | 4.2567e+01 | 6.9325e+00 | 3.5634e+01 | 6.1657e+00 | 3.6401e+01 |
| E^6_5 | untwisted | 1.0 | 8.5133e+01 | 8.7749e+00 | 7.6359e+01 | 8.5528e+00 | 7.6581e+01 |
| E^6_5 | untwisted | 1.4 | 1.1919e+02 | 8.9231e+00 | 1.1026e+02 | 9.5134e+00 | 1.0967e+02 |
| E^6_7 | untwisted | 0.25 | 5.1080e+01 | 7.7963e+00 | 4.3284e+01 | 6.5947e+00 | 4.4485e+01 |
| E^6_7 | untwisted | 0.5 | 1.0216e+02 | 1.1715e+01 | 9.0445e+01 | 9.4867e+00 | 9.2673e+01 |
| E^6_7 | untwisted | 1.0 | 2.0432e+02 | 1.3597e+01 | 1.9072e+02 | 1.2650e+01 | 1.9167e+02 |
| E^6_7 | untwisted | 1.4 | 2.8605e+02 | 1.4007e+01 | 2.7204e+02 | 1.3193e+01 | 2.7286e+02 |

## 6. Per-level Tables

Decomposition: ||O||^2 = ||P_0 O||^2 + ||P_1 O||^2 + Residual.
One positive level chosen (the first). Residual = Lambda - ||P_0 O||^2.

Ground eigenfunction under Friedrichs:
- Twisted arm: phi_0(y) = sgn(cos y), eigenvalue 0
- Untwisted arm: 1 (constant), eigenvalue 0

Under bridging (twisted) and phi_0-transformed (untwisted): ground mode is the
defect-bound state; per-level decomposition not computed for those conditions.
Under SCTM: ground is the constant function (same as untwisted Friedrichs).

Note: residuals near zero may show as small negative values (order 10^{-4}) due to
quadrature error between the HS norm (60x40 grid) and projection (30x12 grid) computations.
These indicate that the true residual is 0.

### Value sampler O^(0) -- Friedrichs per-level

**Placement: generic**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 2.2390e-02 | 1.2288e-02 | 6.2409e-01 | 6.5877e-01 |
| E^1_12 | untwisted | 0.5 | 2.1597e-02 | 1.1442e-02 | 1.2845e+00 | 1.3175e+00 |
| E^1_12 | untwisted | 1.0 | 2.2735e-02 | 3.5650e-02 | 2.5767e+00 | 2.6351e+00 |
| E^1_12 | untwisted | 1.4 | 2.3189e-02 | 2.6021e-02 | 3.6399e+00 | 3.6891e+00 |
| E^1_20 | untwisted | 0.25 | 1.9832e-02 | 2.2159e-02 | 1.0222e+00 | 1.0642e+00 |
| E^1_20 | untwisted | 0.5 | 2.1953e-02 | 1.9632e-02 | 2.0867e+00 | 2.1283e+00 |
| E^1_20 | untwisted | 1.0 | 1.6242e-02 | 1.4375e-02 | 4.2261e+00 | 4.2567e+00 |
| E^1_20 | untwisted | 1.4 | 6.5125e-02 | 2.4009e-02 | 5.8702e+00 | 5.9593e+00 |
| E^3_2 | untwisted | 0.25 | 1.7498e-01 | 1.3772e-01 | 1.4338e-01 | 4.5607e-01 |
| E^3_2 | untwisted | 0.5 | 2.9286e-01 | 2.5858e-01 | 3.6071e-01 | 9.1214e-01 |
| E^3_2 | untwisted | 1.0 | 3.1479e-01 | 3.9829e-01 | 1.1112e+00 | 1.8243e+00 |
| E^3_2 | untwisted | 1.4 | 2.9515e-01 | 3.9018e-01 | 1.8687e+00 | 2.5540e+00 |
| E^3_10 | untwisted | 0.25 | 6.8646e-02 | 7.6184e-02 | 1.5274e+00 | 1.6723e+00 |
| E^3_10 | untwisted | 0.5 | 7.4095e-02 | 5.8749e-02 | 3.2117e+00 | 3.3445e+00 |
| E^3_10 | untwisted | 1.0 | 7.9727e-02 | 1.0540e-01 | 6.5039e+00 | 6.6891e+00 |
| E^3_10 | untwisted | 1.4 | 9.0552e-02 | 9.0023e-02 | 9.1841e+00 | 9.3647e+00 |
| E^3'_6 | untwisted | 0.25 | 9.3017e-02 | 1.4693e-01 | 8.2422e-01 | 1.0642e+00 |
| E^3'_6 | untwisted | 0.5 | 9.2284e-02 | 1.7400e-01 | 1.8621e+00 | 2.1283e+00 |
| E^3'_6 | untwisted | 1.0 | 1.2266e-01 | 1.4386e-01 | 3.9902e+00 | 4.2567e+00 |
| E^3'_6 | untwisted | 1.4 | 1.4714e-01 | 1.4070e-01 | 5.6715e+00 | 5.9593e+00 |
| E^3'_10 | untwisted | 0.25 | 8.1265e-02 | 1.1173e-01 | 1.4793e+00 | 1.6723e+00 |
| E^3'_10 | untwisted | 0.5 | 1.2110e-01 | 8.5703e-02 | 3.1377e+00 | 3.3445e+00 |
| E^3'_10 | untwisted | 1.0 | 8.4599e-02 | 9.1518e-02 | 6.5129e+00 | 6.6891e+00 |
| E^3'_10 | untwisted | 1.4 | 7.5140e-02 | 8.5766e-02 | 9.2038e+00 | 9.3647e+00 |
| E^4_6 | untwisted | 0.25 | 2.1539e-01 | 1.1701e-01 | 1.0865e+00 | 1.4189e+00 |
| E^4_6 | untwisted | 0.5 | 2.1936e-01 | 1.4741e-01 | 2.4710e+00 | 2.8378e+00 |
| E^4_6 | untwisted | 1.0 | 1.9148e-01 | 1.8356e-01 | 5.3005e+00 | 5.6756e+00 |
| E^4_6 | untwisted | 1.4 | 1.6374e-01 | 1.9925e-01 | 7.5828e+00 | 7.9458e+00 |
| E^4_8 | untwisted | 0.25 | 1.7035e-01 | 1.3421e-01 | 1.5197e+00 | 1.8243e+00 |
| E^4_8 | untwisted | 0.5 | 1.5969e-01 | 1.4896e-01 | 3.3399e+00 | 3.6486e+00 |
| E^4_8 | untwisted | 1.0 | 1.4611e-01 | 1.3308e-01 | 7.0180e+00 | 7.2971e+00 |
| E^4_8 | untwisted | 1.4 | 1.3108e-01 | 1.4788e-01 | 9.9370e+00 | 1.0216e+01 |
| E^5_4 | untwisted | 0.25 | 2.6045e-01 | 2.1156e-01 | 7.9486e-01 | 1.2669e+00 |
| E^5_4 | untwisted | 0.5 | 3.2692e-01 | 3.1913e-01 | 1.8877e+00 | 2.5337e+00 |
| E^5_4 | untwisted | 1.0 | 3.2053e-01 | 3.3295e-01 | 4.4140e+00 | 5.0675e+00 |
| E^5_4 | untwisted | 1.4 | 3.0397e-01 | 3.5341e-01 | 6.4371e+00 | 7.0944e+00 |
| E^5_8 | untwisted | 0.25 | 1.5427e-01 | 1.6072e-01 | 1.9654e+00 | 2.2804e+00 |
| E^5_8 | untwisted | 0.5 | 1.5489e-01 | 1.6779e-01 | 4.2380e+00 | 4.5607e+00 |
| E^5_8 | untwisted | 1.0 | 1.7338e-01 | 1.9118e-01 | 8.7569e+00 | 9.1214e+00 |
| E^5_8 | untwisted | 1.4 | 1.8460e-01 | 1.8427e-01 | 1.2401e+01 | 1.2770e+01 |
| E^2_1 | twisted | 0.25 | 1.2242e-01 | 6.7993e-02 | 1.2288e-02 | 2.0270e-01 |
| E^2_1 | twisted | 0.5 | 2.2985e-01 | 1.3599e-01 | 3.9562e-02 | 4.0540e-01 |
| E^2_1 | twisted | 1.0 | 3.5404e-01 | 2.7197e-01 | 1.8479e-01 | 8.1079e-01 |
| E^2_1 | twisted | 1.4 | 3.4683e-01 | 3.8076e-01 | 4.0753e-01 | 1.1351e+00 |
| E^2_11 | twisted | 0.25 | 4.2624e-02 | 3.3251e-02 | 1.1403e+00 | 1.2162e+00 |
| E^2_11 | twisted | 0.5 | 4.6559e-02 | 2.4319e-02 | 2.3615e+00 | 2.4324e+00 |
| E^2_11 | twisted | 1.0 | 5.8895e-02 | 4.6504e-02 | 4.7594e+00 | 4.8648e+00 |
| E^2_11 | twisted | 1.4 | 5.4715e-02 | 5.3345e-02 | 6.7026e+00 | 6.8107e+00 |
| E^2'_7 | twisted | 0.25 | 9.7897e-02 | 8.5513e-02 | 6.2738e-01 | 8.1079e-01 |
| E^2'_7 | twisted | 0.5 | 7.8495e-02 | 1.2209e-01 | 1.4210e+00 | 1.6216e+00 |
| E^2'_7 | twisted | 1.0 | 8.1062e-02 | 9.1102e-02 | 3.0710e+00 | 3.2432e+00 |
| E^2'_7 | twisted | 1.4 | 7.6838e-02 | 7.1097e-02 | 4.3925e+00 | 4.5404e+00 |
| E^2'_13 | twisted | 0.25 | 3.5674e-02 | 4.9359e-02 | 1.3339e+00 | 1.4189e+00 |
| E^2'_13 | twisted | 0.5 | 5.6839e-02 | 6.8611e-02 | 2.7123e+00 | 2.8378e+00 |
| E^2'_13 | twisted | 1.0 | 4.6244e-02 | 4.9012e-02 | 5.5803e+00 | 5.6756e+00 |
| E^2'_13 | twisted | 1.4 | 4.0059e-02 | 4.0793e-02 | 7.8649e+00 | 7.9458e+00 |
| E^4'_3 | twisted | 0.25 | 2.2327e-01 | 1.7363e-01 | 4.1390e-01 | 8.1079e-01 |
| E^4'_3 | twisted | 0.5 | 3.2549e-01 | 2.9244e-01 | 1.0037e+00 | 1.6216e+00 |
| E^4'_3 | twisted | 1.0 | 3.1103e-01 | 3.2481e-01 | 2.6073e+00 | 3.2432e+00 |
| E^4'_3 | twisted | 1.4 | 3.3738e-01 | 3.1502e-01 | 3.8880e+00 | 4.5404e+00 |
| E^4'_9 | twisted | 0.25 | 1.1519e-01 | 9.5053e-02 | 1.8167e+00 | 2.0270e+00 |
| E^4'_9 | twisted | 0.5 | 1.1774e-01 | 7.8197e-02 | 3.8580e+00 | 4.0540e+00 |
| E^4'_9 | twisted | 1.0 | 1.2989e-01 | 1.1774e-01 | 7.8603e+00 | 8.1079e+00 |
| E^4'_9 | twisted | 1.4 | 1.3379e-01 | 1.3405e-01 | 1.1083e+01 | 1.1351e+01 |
| E^6_5 | twisted | 0.25 | 2.8936e-01 | 2.3934e-01 | 1.2956e+00 | 1.8243e+00 |
| E^6_5 | twisted | 0.5 | 3.1955e-01 | 3.2106e-01 | 3.0080e+00 | 3.6486e+00 |
| E^6_5 | twisted | 1.0 | 3.2136e-01 | 3.2564e-01 | 6.6502e+00 | 7.2971e+00 |
| E^6_5 | twisted | 1.4 | 3.2953e-01 | 3.1106e-01 | 9.5754e+00 | 1.0216e+01 |
| E^6_7 | twisted | 0.25 | 2.2204e-01 | 1.9585e-01 | 2.0145e+00 | 2.4324e+00 |
| E^6_7 | twisted | 0.5 | 2.3259e-01 | 1.9495e-01 | 4.4372e+00 | 4.8648e+00 |
| E^6_7 | twisted | 1.0 | 2.3876e-01 | 2.2960e-01 | 9.2612e+00 | 9.7295e+00 |
| E^6_7 | twisted | 1.4 | 2.4686e-01 | 2.4192e-01 | 1.3133e+01 | 1.3621e+01 |

**Placement: 2fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 3.7444e-03 | 6.5514e-03 | 6.4847e-01 | 6.5877e-01 |
| E^1_12 | untwisted | 0.5 | 8.0032e-03 | 3.0750e-02 | 1.2788e+00 | 1.3175e+00 |
| E^1_12 | untwisted | 1.0 | 3.2935e-02 | 2.8532e-02 | 2.5736e+00 | 2.6351e+00 |
| E^1_12 | untwisted | 1.4 | 2.9383e-02 | 2.6750e-02 | 3.6330e+00 | 3.6891e+00 |
| E^1_20 | untwisted | 0.25 | 3.1794e-02 | 2.0511e-03 | 1.0303e+00 | 1.0642e+00 |
| E^1_20 | untwisted | 0.5 | 1.7085e-02 | 1.3228e-02 | 2.0980e+00 | 2.1283e+00 |
| E^1_20 | untwisted | 1.0 | 1.2125e-02 | 7.8662e-03 | 4.2367e+00 | 4.2567e+00 |
| E^1_20 | untwisted | 1.4 | 2.9781e-02 | 5.6107e-03 | 5.9239e+00 | 5.9593e+00 |
| E^3_2 | untwisted | 0.25 | 1.7498e-01 | 1.3772e-01 | 1.4338e-01 | 4.5607e-01 |
| E^3_2 | untwisted | 0.5 | 2.9286e-01 | 2.5858e-01 | 3.6071e-01 | 9.1214e-01 |
| E^3_2 | untwisted | 1.0 | 3.1479e-01 | 3.9829e-01 | 1.1112e+00 | 1.8243e+00 |
| E^3_2 | untwisted | 1.4 | 2.9515e-01 | 3.9018e-01 | 1.8687e+00 | 2.5540e+00 |
| E^3_10 | untwisted | 0.25 | 1.6480e-02 | 1.0470e-01 | 1.5511e+00 | 1.6723e+00 |
| E^3_10 | untwisted | 0.5 | 7.8343e-02 | 8.9392e-02 | 3.1768e+00 | 3.3445e+00 |
| E^3_10 | untwisted | 1.0 | 1.1545e-01 | 8.7498e-02 | 6.4861e+00 | 6.6891e+00 |
| E^3_10 | untwisted | 1.4 | 9.2191e-02 | 1.0377e-01 | 9.1687e+00 | 9.3647e+00 |
| E^3'_6 | untwisted | 0.25 | 9.4935e-02 | 1.4600e-01 | 8.2323e-01 | 1.0642e+00 |
| E^3'_6 | untwisted | 0.5 | 1.2964e-01 | 1.4984e-01 | 1.8489e+00 | 2.1283e+00 |
| E^3'_6 | untwisted | 1.0 | 1.8305e-01 | 7.6273e-02 | 3.9973e+00 | 4.2567e+00 |
| E^3'_6 | untwisted | 1.4 | 1.3118e-01 | 1.8903e-01 | 5.6391e+00 | 5.9593e+00 |
| E^3'_10 | untwisted | 0.25 | 6.0022e-02 | 1.4348e-01 | 1.4688e+00 | 1.6723e+00 |
| E^3'_10 | untwisted | 0.5 | 7.3932e-02 | 9.5686e-02 | 3.1749e+00 | 3.3445e+00 |
| E^3'_10 | untwisted | 1.0 | 7.0851e-02 | 7.9859e-02 | 6.5383e+00 | 6.6891e+00 |
| E^3'_10 | untwisted | 1.4 | 1.0356e-01 | 6.2862e-02 | 9.1983e+00 | 9.3647e+00 |
| E^4_6 | untwisted | 0.25 | 2.1348e-01 | 1.1794e-01 | 1.0875e+00 | 1.4189e+00 |
| E^4_6 | untwisted | 0.5 | 1.8201e-01 | 1.7156e-01 | 2.4842e+00 | 2.8378e+00 |
| E^4_6 | untwisted | 1.0 | 1.3109e-01 | 2.5115e-01 | 5.2933e+00 | 5.6756e+00 |
| E^4_6 | untwisted | 1.4 | 1.7970e-01 | 1.5092e-01 | 7.6152e+00 | 7.9458e+00 |
| E^4_8 | untwisted | 0.25 | 1.9137e-01 | 1.2138e-01 | 1.5115e+00 | 1.8243e+00 |
| E^4_8 | untwisted | 0.5 | 1.4263e-01 | 1.3411e-01 | 3.3718e+00 | 3.6486e+00 |
| E^4_8 | untwisted | 1.0 | 1.0351e-01 | 1.6184e-01 | 7.0318e+00 | 7.2971e+00 |
| E^4_8 | untwisted | 1.4 | 1.4209e-01 | 1.1939e-01 | 9.9545e+00 | 1.0216e+01 |
| E^5_4 | untwisted | 0.25 | 2.6045e-01 | 2.1156e-01 | 7.9486e-01 | 1.2669e+00 |
| E^5_4 | untwisted | 0.5 | 3.2692e-01 | 3.1913e-01 | 1.8877e+00 | 2.5337e+00 |
| E^5_4 | untwisted | 1.0 | 3.2053e-01 | 3.3295e-01 | 4.4140e+00 | 5.0675e+00 |
| E^5_4 | untwisted | 1.4 | 3.0397e-01 | 3.5341e-01 | 6.4371e+00 | 7.0944e+00 |
| E^5_8 | untwisted | 0.25 | 1.3325e-01 | 1.7355e-01 | 1.9736e+00 | 2.2804e+00 |
| E^5_8 | untwisted | 0.5 | 1.7195e-01 | 1.8264e-01 | 4.2061e+00 | 4.5607e+00 |
| E^5_8 | untwisted | 1.0 | 2.1599e-01 | 1.6242e-01 | 8.7430e+00 | 9.1214e+00 |
| E^5_8 | untwisted | 1.4 | 1.7360e-01 | 2.1275e-01 | 1.2384e+01 | 1.2770e+01 |
| E^2_1 | twisted | 0.25 | 1.2242e-01 | 6.7993e-02 | 1.2288e-02 | 2.0270e-01 |
| E^2_1 | twisted | 0.5 | 2.2985e-01 | 1.3599e-01 | 3.9562e-02 | 4.0540e-01 |
| E^2_1 | twisted | 1.0 | 3.5404e-01 | 2.7197e-01 | 1.8479e-01 | 8.1079e-01 |
| E^2_1 | twisted | 1.4 | 3.4683e-01 | 3.8076e-01 | 4.0753e-01 | 1.1351e+00 |
| E^2_11 | twisted | 0.25 | 7.7956e-03 | 2.5142e-02 | 1.1833e+00 | 1.2162e+00 |
| E^2_11 | twisted | 0.5 | 4.8025e-02 | 3.6215e-02 | 2.3481e+00 | 2.4324e+00 |
| E^2_11 | twisted | 1.0 | 5.9953e-02 | 9.1418e-02 | 4.7134e+00 | 4.8648e+00 |
| E^2_11 | twisted | 1.4 | 5.6149e-02 | 7.7449e-02 | 6.6771e+00 | 6.8107e+00 |
| E^2'_7 | twisted | 0.25 | 1.1000e-01 | 6.9602e-02 | 6.3120e-01 | 8.1079e-01 |
| E^2'_7 | twisted | 0.5 | 8.6794e-02 | 6.0283e-02 | 1.4745e+00 | 1.6216e+00 |
| E^2'_7 | twisted | 1.0 | 7.9401e-02 | 4.1028e-02 | 3.1227e+00 | 3.2432e+00 |
| E^2'_7 | twisted | 1.4 | 7.8706e-02 | 5.4778e-02 | 4.4070e+00 | 4.5404e+00 |
| E^2'_13 | twisted | 0.25 | 4.8449e-02 | 1.6051e-02 | 1.3544e+00 | 1.4189e+00 |
| E^2'_13 | twisted | 0.5 | 5.1397e-02 | 2.0313e-02 | 2.7661e+00 | 2.8378e+00 |
| E^2'_13 | twisted | 1.0 | 3.8197e-02 | 2.0639e-02 | 5.6167e+00 | 5.6756e+00 |
| E^2'_13 | twisted | 1.4 | 5.0867e-02 | 4.4699e-02 | 7.8502e+00 | 7.9458e+00 |
| E^4'_3 | twisted | 0.25 | 2.2327e-01 | 1.7363e-01 | 4.1390e-01 | 8.1079e-01 |
| E^4'_3 | twisted | 0.5 | 3.2549e-01 | 2.9244e-01 | 1.0037e+00 | 1.6216e+00 |
| E^4'_3 | twisted | 1.0 | 3.1103e-01 | 3.2481e-01 | 2.6073e+00 | 3.2432e+00 |
| E^4'_3 | twisted | 1.4 | 3.3738e-01 | 3.1502e-01 | 3.8880e+00 | 4.5404e+00 |
| E^4'_9 | twisted | 0.25 | 8.1939e-02 | 1.1512e-01 | 1.8299e+00 | 2.0270e+00 |
| E^4'_9 | twisted | 0.5 | 1.2341e-01 | 1.3647e-01 | 3.7941e+00 | 4.0540e+00 |
| E^4'_9 | twisted | 1.0 | 1.4029e-01 | 1.8493e-01 | 7.7827e+00 | 8.1079e+00 |
| E^4'_9 | twisted | 1.4 | 1.3034e-01 | 1.5519e-01 | 1.1066e+01 | 1.1351e+01 |
| E^6_5 | twisted | 0.25 | 2.8936e-01 | 2.3934e-01 | 1.2956e+00 | 1.8243e+00 |
| E^6_5 | twisted | 0.5 | 3.1955e-01 | 3.2106e-01 | 3.0080e+00 | 3.6486e+00 |
| E^6_5 | twisted | 1.0 | 3.2136e-01 | 3.2564e-01 | 6.6502e+00 | 7.2971e+00 |
| E^6_5 | twisted | 1.4 | 3.2953e-01 | 3.1106e-01 | 9.5754e+00 | 1.0216e+01 |
| E^6_7 | twisted | 0.25 | 2.0994e-01 | 2.1176e-01 | 2.0107e+00 | 2.4324e+00 |
| E^6_7 | twisted | 0.5 | 2.2429e-01 | 2.5676e-01 | 4.3837e+00 | 4.8648e+00 |
| E^6_7 | twisted | 1.0 | 2.4042e-01 | 2.7967e-01 | 9.2094e+00 | 9.7295e+00 |
| E^6_7 | twisted | 1.4 | 2.4499e-01 | 2.5824e-01 | 1.3118e+01 | 1.3621e+01 |

**Placement: 3fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 4.9164e-03 | 2.1980e-02 | 6.3187e-01 | 6.5877e-01 |
| E^1_12 | untwisted | 0.5 | 1.7240e-02 | 3.7360e-02 | 1.2629e+00 | 1.3175e+00 |
| E^1_12 | untwisted | 1.0 | 2.5322e-02 | 2.1302e-02 | 2.5885e+00 | 2.6351e+00 |
| E^1_12 | untwisted | 1.4 | 2.1125e-02 | 2.5445e-02 | 3.6425e+00 | 3.6891e+00 |
| E^1_20 | untwisted | 0.25 | 2.3695e-02 | 5.1230e-03 | 1.0353e+00 | 1.0642e+00 |
| E^1_20 | untwisted | 0.5 | 1.4817e-02 | 1.2802e-02 | 2.1007e+00 | 2.1283e+00 |
| E^1_20 | untwisted | 1.0 | 1.5143e-02 | 1.5749e-02 | 4.2258e+00 | 4.2567e+00 |
| E^1_20 | untwisted | 1.4 | 1.6485e-02 | 9.6063e-03 | 5.9332e+00 | 5.9593e+00 |
| E^3_2 | untwisted | 0.25 | 1.7498e-01 | 1.3772e-01 | 1.4338e-01 | 4.5607e-01 |
| E^3_2 | untwisted | 0.5 | 2.9286e-01 | 2.5858e-01 | 3.6071e-01 | 9.1214e-01 |
| E^3_2 | untwisted | 1.0 | 3.1479e-01 | 3.9829e-01 | 1.1112e+00 | 1.8243e+00 |
| E^3_2 | untwisted | 1.4 | 2.9515e-01 | 3.9018e-01 | 1.8687e+00 | 2.5540e+00 |
| E^3_10 | untwisted | 0.25 | 4.2265e-02 | 1.0313e-01 | 1.5269e+00 | 1.6723e+00 |
| E^3_10 | untwisted | 0.5 | 8.3762e-02 | 1.0419e-01 | 3.1566e+00 | 3.3445e+00 |
| E^3_10 | untwisted | 1.0 | 9.2769e-02 | 7.4930e-02 | 6.5214e+00 | 6.6891e+00 |
| E^3_10 | untwisted | 1.4 | 7.9347e-02 | 8.8673e-02 | 9.1967e+00 | 9.3647e+00 |
| E^3'_6 | untwisted | 0.25 | 1.1317e-01 | 1.2997e-01 | 8.2103e-01 | 1.0642e+00 |
| E^3'_6 | untwisted | 0.5 | 1.3244e-01 | 1.4466e-01 | 1.8512e+00 | 2.1283e+00 |
| E^3'_6 | untwisted | 1.0 | 1.6209e-01 | 1.1044e-01 | 3.9841e+00 | 4.2567e+00 |
| E^3'_6 | untwisted | 1.4 | 1.2195e-01 | 1.4638e-01 | 5.6910e+00 | 5.9593e+00 |
| E^3'_10 | untwisted | 0.25 | 5.7946e-02 | 1.3060e-01 | 1.4837e+00 | 1.6723e+00 |
| E^3'_10 | untwisted | 0.5 | 6.9121e-02 | 9.1670e-02 | 3.1837e+00 | 3.3445e+00 |
| E^3'_10 | untwisted | 1.0 | 7.2548e-02 | 1.0514e-01 | 6.5114e+00 | 6.6891e+00 |
| E^3'_10 | untwisted | 1.4 | 8.3168e-02 | 9.9048e-02 | 9.1825e+00 | 9.3647e+00 |
| E^4_6 | untwisted | 0.25 | 1.9524e-01 | 1.3397e-01 | 1.0897e+00 | 1.4189e+00 |
| E^4_6 | untwisted | 0.5 | 1.7920e-01 | 1.7674e-01 | 2.4818e+00 | 2.8378e+00 |
| E^4_6 | untwisted | 1.0 | 1.5205e-01 | 2.1699e-01 | 5.3065e+00 | 5.6756e+00 |
| E^4_6 | untwisted | 1.4 | 1.8893e-01 | 1.9357e-01 | 7.5633e+00 | 7.9458e+00 |
| E^4_8 | untwisted | 0.25 | 1.6966e-01 | 1.2507e-01 | 1.5296e+00 | 1.8243e+00 |
| E^4_8 | untwisted | 0.5 | 1.4063e-01 | 1.2983e-01 | 3.3781e+00 | 3.6486e+00 |
| E^4_8 | untwisted | 1.0 | 1.2826e-01 | 1.6574e-01 | 7.0031e+00 | 7.2971e+00 |
| E^4_8 | untwisted | 1.4 | 1.4742e-01 | 1.5002e-01 | 9.9186e+00 | 1.0216e+01 |
| E^5_4 | untwisted | 0.25 | 2.6045e-01 | 2.1156e-01 | 7.9486e-01 | 1.2669e+00 |
| E^5_4 | untwisted | 0.5 | 3.2692e-01 | 3.1913e-01 | 1.8877e+00 | 2.5337e+00 |
| E^5_4 | untwisted | 1.0 | 3.2053e-01 | 3.3295e-01 | 4.4140e+00 | 5.0675e+00 |
| E^5_4 | untwisted | 1.4 | 3.0397e-01 | 3.5341e-01 | 6.4371e+00 | 7.0944e+00 |
| E^5_8 | untwisted | 0.25 | 1.5496e-01 | 1.6986e-01 | 1.9555e+00 | 2.2804e+00 |
| E^5_8 | untwisted | 0.5 | 1.7395e-01 | 1.8692e-01 | 4.1998e+00 | 4.5607e+00 |
| E^5_8 | untwisted | 1.0 | 1.9123e-01 | 1.5851e-01 | 8.7717e+00 | 9.1214e+00 |
| E^5_8 | untwisted | 1.4 | 1.6826e-01 | 1.8212e-01 | 1.2420e+01 | 1.2770e+01 |
| E^2_1 | twisted | 0.25 | 1.2242e-01 | 6.7993e-02 | 1.2288e-02 | 2.0270e-01 |
| E^2_1 | twisted | 0.5 | 2.2985e-01 | 1.3599e-01 | 3.9562e-02 | 4.0540e-01 |
| E^2_1 | twisted | 1.0 | 3.5404e-01 | 2.7197e-01 | 1.8479e-01 | 8.1079e-01 |
| E^2_1 | twisted | 1.4 | 3.4683e-01 | 3.8076e-01 | 4.0753e-01 | 1.1351e+00 |
| E^2_11 | twisted | 0.25 | 2.4549e-02 | 3.5876e-02 | 1.1558e+00 | 1.2162e+00 |
| E^2_11 | twisted | 0.5 | 5.6971e-02 | 4.9813e-02 | 2.3256e+00 | 2.4324e+00 |
| E^2_11 | twisted | 1.0 | 5.3714e-02 | 5.5553e-02 | 4.7555e+00 | 4.8648e+00 |
| E^2_11 | twisted | 1.4 | 4.8613e-02 | 4.9938e-02 | 6.7121e+00 | 6.8107e+00 |
| E^2'_7 | twisted | 0.25 | 9.6024e-02 | 6.9042e-02 | 6.4573e-01 | 8.1079e-01 |
| E^2'_7 | twisted | 0.5 | 8.3202e-02 | 6.3929e-02 | 1.4745e+00 | 1.6216e+00 |
| E^2'_7 | twisted | 1.0 | 7.8630e-02 | 6.5862e-02 | 3.0987e+00 | 3.2432e+00 |
| E^2'_7 | twisted | 1.4 | 8.5148e-02 | 7.9103e-02 | 4.3762e+00 | 4.5404e+00 |
| E^2'_13 | twisted | 0.25 | 4.7337e-02 | 2.2062e-02 | 1.3495e+00 | 1.4189e+00 |
| E^2'_13 | twisted | 0.5 | 4.5192e-02 | 2.0940e-02 | 2.7716e+00 | 2.8378e+00 |
| E^2'_13 | twisted | 1.0 | 4.5423e-02 | 4.1314e-02 | 5.5888e+00 | 5.6756e+00 |
| E^2'_13 | twisted | 1.4 | 4.6683e-02 | 3.8052e-02 | 7.8610e+00 | 7.9458e+00 |
| E^4'_3 | twisted | 0.25 | 2.2327e-01 | 1.7363e-01 | 4.1390e-01 | 8.1079e-01 |
| E^4'_3 | twisted | 0.5 | 3.2549e-01 | 2.9244e-01 | 1.0037e+00 | 1.6216e+00 |
| E^4'_3 | twisted | 1.0 | 3.1103e-01 | 3.2481e-01 | 2.6073e+00 | 3.2432e+00 |
| E^4'_3 | twisted | 1.4 | 3.3738e-01 | 3.1502e-01 | 3.8880e+00 | 4.5404e+00 |
| E^4'_9 | twisted | 0.25 | 1.0329e-01 | 1.1991e-01 | 1.8038e+00 | 2.0270e+00 |
| E^4'_9 | twisted | 0.5 | 1.2736e-01 | 1.4411e-01 | 3.7825e+00 | 4.0540e+00 |
| E^4'_9 | twisted | 1.0 | 1.2731e-01 | 1.3889e-01 | 7.8417e+00 | 8.1079e+00 |
| E^4'_9 | twisted | 1.4 | 1.2195e-01 | 1.2653e-01 | 1.1103e+01 | 1.1351e+01 |
| E^6_5 | twisted | 0.25 | 2.8936e-01 | 2.3934e-01 | 1.2956e+00 | 1.8243e+00 |
| E^6_5 | twisted | 0.5 | 3.1955e-01 | 3.2106e-01 | 3.0080e+00 | 3.6486e+00 |
| E^6_5 | twisted | 1.0 | 3.2136e-01 | 3.2564e-01 | 6.6502e+00 | 7.2971e+00 |
| E^6_5 | twisted | 1.4 | 3.2953e-01 | 3.1106e-01 | 9.5754e+00 | 1.0216e+01 |
| E^6_7 | twisted | 0.25 | 2.2391e-01 | 2.1232e-01 | 1.9962e+00 | 2.4324e+00 |
| E^6_7 | twisted | 0.5 | 2.2789e-01 | 2.5311e-01 | 4.3838e+00 | 4.8648e+00 |
| E^6_7 | twisted | 1.0 | 2.4119e-01 | 2.5483e-01 | 9.2335e+00 | 9.7295e+00 |
| E^6_7 | twisted | 1.4 | 2.3855e-01 | 2.3391e-01 | 1.3149e+01 | 1.3621e+01 |

**Placement: 5fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | untwisted | 0.25 | 2.4154e-02 | 1.5437e-02 | 6.1918e-01 | 6.5877e-01 |
| E^1_12 | untwisted | 0.5 | 1.8643e-02 | 1.4278e-02 | 1.2846e+00 | 1.3175e+00 |
| E^1_12 | untwisted | 1.0 | 2.1914e-02 | 2.5694e-02 | 2.5875e+00 | 2.6351e+00 |
| E^1_12 | untwisted | 1.4 | 2.4213e-02 | 3.0817e-02 | 3.6341e+00 | 3.6891e+00 |
| E^1_20 | untwisted | 0.25 | 8.4031e-03 | 2.1534e-02 | 1.0342e+00 | 1.0642e+00 |
| E^1_20 | untwisted | 0.5 | 1.6462e-02 | 1.5807e-02 | 2.0961e+00 | 2.1283e+00 |
| E^1_20 | untwisted | 1.0 | 1.4172e-02 | 1.4100e-02 | 4.2284e+00 | 4.2567e+00 |
| E^1_20 | untwisted | 1.4 | 3.9274e-02 | 2.8300e-02 | 5.8918e+00 | 5.9593e+00 |
| E^3_2 | untwisted | 0.25 | 1.7498e-01 | 1.3772e-01 | 1.4338e-01 | 4.5607e-01 |
| E^3_2 | untwisted | 0.5 | 2.9286e-01 | 2.5858e-01 | 3.6071e-01 | 9.1214e-01 |
| E^3_2 | untwisted | 1.0 | 3.1479e-01 | 3.9829e-01 | 1.1112e+00 | 1.8243e+00 |
| E^3_2 | untwisted | 1.4 | 2.9515e-01 | 3.9018e-01 | 1.8687e+00 | 2.5540e+00 |
| E^3_10 | untwisted | 0.25 | 7.5231e-02 | 6.4588e-02 | 1.5324e+00 | 1.6723e+00 |
| E^3_10 | untwisted | 0.5 | 6.0695e-02 | 9.0559e-02 | 3.1933e+00 | 3.3445e+00 |
| E^3_10 | untwisted | 1.0 | 7.5842e-02 | 1.0418e-01 | 6.5090e+00 | 6.6891e+00 |
| E^3_10 | untwisted | 1.4 | 8.5107e-02 | 1.0248e-01 | 9.1771e+00 | 9.3647e+00 |
| E^3'_6 | untwisted | 0.25 | 9.1142e-02 | 1.4871e-01 | 8.2431e-01 | 1.0642e+00 |
| E^3'_6 | untwisted | 0.5 | 9.1768e-02 | 1.7762e-01 | 1.8590e+00 | 2.1283e+00 |
| E^3'_6 | untwisted | 1.0 | 1.1230e-01 | 1.6027e-01 | 3.9841e+00 | 4.2567e+00 |
| E^3'_6 | untwisted | 1.4 | 1.2814e-01 | 1.7167e-01 | 5.6595e+00 | 5.9593e+00 |
| E^3'_10 | untwisted | 0.25 | 1.1818e-01 | 7.1653e-02 | 1.4824e+00 | 1.6723e+00 |
| E^3'_10 | untwisted | 0.5 | 6.9604e-02 | 1.1188e-01 | 3.1630e+00 | 3.3445e+00 |
| E^3'_10 | untwisted | 1.0 | 8.8510e-02 | 7.2881e-02 | 6.5277e+00 | 6.6891e+00 |
| E^3'_10 | untwisted | 1.4 | 9.4378e-02 | 8.2497e-02 | 9.1878e+00 | 9.3647e+00 |
| E^4_6 | untwisted | 0.25 | 2.1727e-01 | 1.1523e-01 | 1.0864e+00 | 1.4189e+00 |
| E^4_6 | untwisted | 0.5 | 2.1988e-01 | 1.4379e-01 | 2.4741e+00 | 2.8378e+00 |
| E^4_6 | untwisted | 1.0 | 2.0183e-01 | 1.6715e-01 | 5.3066e+00 | 5.6756e+00 |
| E^4_6 | untwisted | 1.4 | 1.8274e-01 | 1.6828e-01 | 7.5948e+00 | 7.9458e+00 |
| E^4_8 | untwisted | 0.25 | 1.7466e-01 | 1.3190e-01 | 1.5177e+00 | 1.8243e+00 |
| E^4_8 | untwisted | 0.5 | 1.5960e-01 | 1.3643e-01 | 3.3525e+00 | 3.6486e+00 |
| E^4_8 | untwisted | 1.0 | 1.5470e-01 | 1.2424e-01 | 7.0182e+00 | 7.2971e+00 |
| E^4_8 | untwisted | 1.4 | 1.4490e-01 | 1.3008e-01 | 9.9410e+00 | 1.0216e+01 |
| E^5_4 | untwisted | 0.25 | 2.6045e-01 | 2.1156e-01 | 7.9486e-01 | 1.2669e+00 |
| E^5_4 | untwisted | 0.5 | 3.2692e-01 | 3.1913e-01 | 1.8877e+00 | 2.5337e+00 |
| E^5_4 | untwisted | 1.0 | 3.2053e-01 | 3.3295e-01 | 4.4140e+00 | 5.0675e+00 |
| E^5_4 | untwisted | 1.4 | 3.0397e-01 | 3.5341e-01 | 6.4371e+00 | 7.0944e+00 |
| E^5_8 | untwisted | 0.25 | 1.4996e-01 | 1.6303e-01 | 1.9674e+00 | 2.2804e+00 |
| E^5_8 | untwisted | 0.5 | 1.5498e-01 | 1.8032e-01 | 4.2254e+00 | 4.5607e+00 |
| E^5_8 | untwisted | 1.0 | 1.6479e-01 | 2.0001e-01 | 8.7566e+00 | 9.1214e+00 |
| E^5_8 | untwisted | 1.4 | 1.7079e-01 | 2.0206e-01 | 1.2397e+01 | 1.2770e+01 |
| E^2_1 | twisted | 0.25 | 1.2242e-01 | 6.7993e-02 | 1.2288e-02 | 2.0270e-01 |
| E^2_1 | twisted | 0.5 | 2.2985e-01 | 1.3599e-01 | 3.9562e-02 | 4.0540e-01 |
| E^2_1 | twisted | 1.0 | 3.5404e-01 | 2.7197e-01 | 1.8479e-01 | 8.1079e-01 |
| E^2_1 | twisted | 1.4 | 3.4683e-01 | 3.8076e-01 | 4.0753e-01 | 1.1351e+00 |
| E^2_11 | twisted | 0.25 | 5.0383e-02 | 3.1815e-02 | 1.1340e+00 | 1.2162e+00 |
| E^2_11 | twisted | 0.5 | 4.0377e-02 | 2.6250e-02 | 2.3658e+00 | 2.4324e+00 |
| E^2_11 | twisted | 1.0 | 5.3260e-02 | 3.8279e-02 | 4.7732e+00 | 4.8648e+00 |
| E^2_11 | twisted | 1.4 | 5.6984e-02 | 4.9574e-02 | 6.7041e+00 | 6.8107e+00 |
| E^2'_7 | twisted | 0.25 | 1.0038e-01 | 8.4138e-02 | 6.2628e-01 | 8.1079e-01 |
| E^2'_7 | twisted | 0.5 | 8.0234e-02 | 1.1338e-01 | 1.4280e+00 | 1.6216e+00 |
| E^2'_7 | twisted | 1.0 | 8.0257e-02 | 1.0184e-01 | 3.0611e+00 | 3.2432e+00 |
| E^2'_7 | twisted | 1.4 | 7.8501e-02 | 8.0762e-02 | 4.3812e+00 | 4.5404e+00 |
| E^2'_13 | twisted | 0.25 | 6.1698e-02 | 4.7910e-02 | 1.3093e+00 | 1.4189e+00 |
| E^2'_13 | twisted | 0.5 | 3.8848e-02 | 3.2297e-02 | 2.7666e+00 | 2.8378e+00 |
| E^2'_13 | twisted | 1.0 | 4.2280e-02 | 4.1760e-02 | 5.5915e+00 | 5.6756e+00 |
| E^2'_13 | twisted | 1.4 | 4.9888e-02 | 4.7458e-02 | 7.8484e+00 | 7.9458e+00 |
| E^4'_3 | twisted | 0.25 | 2.2327e-01 | 1.7363e-01 | 4.1390e-01 | 8.1079e-01 |
| E^4'_3 | twisted | 0.5 | 3.2549e-01 | 2.9244e-01 | 1.0037e+00 | 1.6216e+00 |
| E^4'_3 | twisted | 1.0 | 3.1103e-01 | 3.2481e-01 | 2.6073e+00 | 3.2432e+00 |
| E^4'_3 | twisted | 1.4 | 3.3738e-01 | 3.1502e-01 | 3.8880e+00 | 4.5404e+00 |
| E^4'_9 | twisted | 0.25 | 1.0957e-01 | 9.7731e-02 | 1.8197e+00 | 2.0270e+00 |
| E^4'_9 | twisted | 0.5 | 1.2027e-01 | 9.5524e-02 | 3.8382e+00 | 4.0540e+00 |
| E^4'_9 | twisted | 1.0 | 1.3092e-01 | 1.0892e-01 | 7.8681e+00 | 8.1079e+00 |
| E^4'_9 | twisted | 1.4 | 1.3108e-01 | 1.2221e-01 | 1.1098e+01 | 1.1351e+01 |
| E^6_5 | twisted | 0.25 | 2.8936e-01 | 2.3934e-01 | 1.2956e+00 | 1.8243e+00 |
| E^6_5 | twisted | 0.5 | 3.1955e-01 | 3.2106e-01 | 3.0080e+00 | 3.6486e+00 |
| E^6_5 | twisted | 1.0 | 3.2136e-01 | 3.2564e-01 | 6.6502e+00 | 7.2971e+00 |
| E^6_5 | twisted | 1.4 | 3.2953e-01 | 3.1106e-01 | 9.5754e+00 | 1.0216e+01 |
| E^6_7 | twisted | 0.25 | 2.1955e-01 | 1.9723e-01 | 2.0156e+00 | 2.4324e+00 |
| E^6_7 | twisted | 0.5 | 2.3085e-01 | 2.0366e-01 | 4.4303e+00 | 4.8648e+00 |
| E^6_7 | twisted | 1.0 | 2.3956e-01 | 2.1886e-01 | 9.2711e+00 | 9.7295e+00 |
| E^6_7 | twisted | 1.4 | 2.4519e-01 | 2.3225e-01 | 1.3144e+01 | 1.3621e+01 |

### Transverse sampler O^(1) -- Friedrichs per-level

**Placement: generic**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 2.3167e+00 | 1.9282e+00 | 3.2646e+01 | 3.6891e+01 |
| E^1_12 | twisted | 0.5 | 3.4325e+00 | 1.2179e+00 | 6.9132e+01 | 7.3782e+01 |
| E^1_12 | twisted | 1.0 | 4.3613e+00 | 3.2907e+00 | 1.3991e+02 | 1.4756e+02 |
| E^1_12 | twisted | 1.4 | 4.1045e+00 | 3.8516e+00 | 1.9863e+02 | 2.0659e+02 |
| E^1_20 | twisted | 0.25 | 3.9551e+00 | 1.0714e+01 | 1.4141e+02 | 1.5608e+02 |
| E^1_20 | twisted | 0.5 | 8.0040e+00 | 1.0032e+01 | 2.9412e+02 | 3.1216e+02 |
| E^1_20 | twisted | 1.0 | 6.6154e+00 | 7.0316e+00 | 6.1066e+02 | 6.2431e+02 |
| E^1_20 | twisted | 1.4 | 7.6264e+00 | 5.2303e+00 | 8.6118e+02 | 8.7404e+02 |
| E^3_2 | twisted | 0.25 | 7.3450e-01 | 4.0796e-01 | 7.3728e-02 | 1.2162e+00 |
| E^3_2 | twisted | 0.5 | 1.3791e+00 | 8.1592e-01 | 2.3737e-01 | 2.4324e+00 |
| E^3_2 | twisted | 1.0 | 2.1242e+00 | 1.6318e+00 | 1.1087e+00 | 4.8648e+00 |
| E^3_2 | twisted | 1.4 | 2.0810e+00 | 2.2846e+00 | 2.4452e+00 | 6.8107e+00 |
| E^3_10 | twisted | 0.25 | 7.2774e+00 | 4.7853e+00 | 5.4828e+01 | 6.6891e+01 |
| E^3_10 | twisted | 0.5 | 8.3915e+00 | 4.2548e+00 | 1.2113e+02 | 1.3378e+02 |
| E^3_10 | twisted | 1.0 | 9.8007e+00 | 8.4867e+00 | 2.4927e+02 | 2.6756e+02 |
| E^3_10 | twisted | 1.4 | 1.0561e+01 | 1.0465e+01 | 3.5356e+02 | 3.7459e+02 |
| E^3'_6 | twisted | 0.25 | 4.6212e+00 | 1.7523e+00 | 1.0653e+01 | 1.7027e+01 |
| E^3'_6 | twisted | 0.5 | 5.7716e+00 | 3.2190e+00 | 2.5063e+01 | 3.4053e+01 |
| E^3'_6 | twisted | 1.0 | 5.5219e+00 | 5.5560e+00 | 5.7029e+01 | 6.8107e+01 |
| E^3'_6 | twisted | 1.4 | 6.6033e+00 | 6.1538e+00 | 8.2592e+01 | 9.5349e+01 |
| E^3'_10 | twisted | 0.25 | 5.8723e+00 | 9.6486e+00 | 5.1370e+01 | 6.6891e+01 |
| E^3'_10 | twisted | 0.5 | 9.6708e+00 | 1.1241e+01 | 1.1287e+02 | 1.3378e+02 |
| E^3'_10 | twisted | 1.0 | 9.8536e+00 | 9.9441e+00 | 2.4776e+02 | 2.6756e+02 |
| E^3'_10 | twisted | 1.4 | 8.9242e+00 | 9.1614e+00 | 3.5650e+02 | 3.7459e+02 |
| E^4_6 | twisted | 0.25 | 4.2695e+00 | 4.9811e+00 | 1.3452e+01 | 2.2702e+01 |
| E^4_6 | twisted | 0.5 | 6.4769e+00 | 7.2738e+00 | 3.1654e+01 | 4.5404e+01 |
| E^4_6 | twisted | 1.0 | 8.2880e+00 | 7.3579e+00 | 7.5163e+01 | 9.0809e+01 |
| E^4_6 | twisted | 1.4 | 7.5892e+00 | 7.9419e+00 | 1.1160e+02 | 1.2713e+02 |
| E^4_8 | twisted | 0.25 | 7.2004e+00 | 7.6095e+00 | 3.3838e+01 | 4.8648e+01 |
| E^4_8 | twisted | 0.5 | 9.5677e+00 | 1.1325e+01 | 7.6402e+01 | 9.7295e+01 |
| E^4_8 | twisted | 1.0 | 1.0676e+01 | 1.0510e+01 | 1.7341e+02 | 1.9459e+02 |
| E^4_8 | twisted | 1.4 | 1.0032e+01 | 1.0077e+01 | 2.5232e+02 | 2.7243e+02 |
| E^5_4 | twisted | 0.25 | 3.4569e+00 | 2.4162e+00 | 4.2618e+00 | 1.0135e+01 |
| E^5_4 | twisted | 0.5 | 5.5534e+00 | 4.2843e+00 | 1.0432e+01 | 2.0270e+01 |
| E^5_4 | twisted | 1.0 | 6.6506e+00 | 5.9678e+00 | 2.7921e+01 | 4.0540e+01 |
| E^5_4 | twisted | 1.4 | 6.8421e+00 | 6.9578e+00 | 4.2956e+01 | 5.6756e+01 |
| E^5_8 | twisted | 0.25 | 9.9893e+00 | 6.1123e+00 | 4.4708e+01 | 6.0810e+01 |
| E^5_8 | twisted | 0.5 | 1.1780e+01 | 7.8722e+00 | 1.0197e+02 | 1.2162e+02 |
| E^5_8 | twisted | 1.0 | 1.2837e+01 | 1.1866e+01 | 2.1854e+02 | 2.4324e+02 |
| E^5_8 | twisted | 1.4 | 1.4042e+01 | 1.3681e+01 | 3.1281e+02 | 3.4053e+02 |
| E^2_1 | untwisted | 0.25 | 2.0309e-01 | 0 | -3.8688e-04 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0617e-01 | 0 | -7.7376e-04 | 4.0540e-01 |
| E^2_1 | untwisted | 1.0 | 8.1234e-01 | 0 | -1.5475e-03 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1373e+00 | 0 | -2.1665e-03 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 4.8586e+00 | 3.6877e+00 | 4.9425e+01 | 5.7972e+01 |
| E^2_11 | untwisted | 0.5 | 5.8006e+00 | 3.6349e+00 | 1.0651e+02 | 1.1594e+02 |
| E^2_11 | untwisted | 1.0 | 6.5887e+00 | 8.1540e+00 | 2.1714e+02 | 2.3189e+02 |
| E^2_11 | untwisted | 1.4 | 7.6908e+00 | 7.1915e+00 | 3.0976e+02 | 3.2464e+02 |
| E^2'_7 | untwisted | 0.25 | 3.2728e+00 | 2.1354e+00 | 1.1618e+01 | 1.7027e+01 |
| E^2'_7 | untwisted | 0.5 | 4.9521e+00 | 3.1678e+00 | 2.5933e+01 | 3.4053e+01 |
| E^2'_7 | untwisted | 1.0 | 4.9782e+00 | 4.2156e+00 | 5.8913e+01 | 6.8107e+01 |
| E^2'_7 | untwisted | 1.4 | 4.3416e+00 | 4.0122e+00 | 8.6996e+01 | 9.5349e+01 |
| E^2'_13 | untwisted | 0.25 | 4.9939e+00 | 7.9515e+00 | 7.9282e+01 | 9.2228e+01 |
| E^2'_13 | untwisted | 0.5 | 1.0254e+01 | 8.6748e+00 | 1.6553e+02 | 1.8446e+02 |
| E^2'_13 | untwisted | 1.0 | 8.6428e+00 | 8.2435e+00 | 3.5203e+02 | 3.6891e+02 |
| E^2'_13 | untwisted | 1.4 | 7.6784e+00 | 6.8333e+00 | 5.0196e+02 | 5.1648e+02 |
| E^4'_3 | untwisted | 0.25 | 1.8060e+00 | 1.1018e+00 | 1.1462e+00 | 4.0540e+00 |
| E^4'_3 | untwisted | 0.5 | 3.1552e+00 | 2.0686e+00 | 2.8841e+00 | 8.1079e+00 |
| E^4'_3 | untwisted | 1.0 | 4.1430e+00 | 3.1863e+00 | 8.8866e+00 | 1.6216e+01 |
| E^4'_3 | untwisted | 1.4 | 4.6358e+00 | 3.1214e+00 | 1.4945e+01 | 2.2702e+01 |
| E^4'_9 | untwisted | 0.25 | 8.7011e+00 | 6.7981e+00 | 5.1391e+01 | 6.6891e+01 |
| E^4'_9 | untwisted | 0.5 | 9.3669e+00 | 8.6423e+00 | 1.1577e+02 | 1.3378e+02 |
| E^4'_9 | untwisted | 1.0 | 1.1227e+01 | 1.1677e+01 | 2.4466e+02 | 2.6756e+02 |
| E^4'_9 | untwisted | 1.4 | 1.2883e+01 | 1.1945e+01 | 3.4976e+02 | 3.7459e+02 |
| E^6_5 | untwisted | 0.25 | 5.8343e+00 | 4.1914e+00 | 1.1258e+01 | 2.1283e+01 |
| E^6_5 | untwisted | 0.5 | 8.6558e+00 | 6.9325e+00 | 2.6978e+01 | 4.2567e+01 |
| E^6_5 | untwisted | 1.0 | 1.0061e+01 | 8.7749e+00 | 6.6298e+01 | 8.5133e+01 |
| E^6_5 | untwisted | 1.4 | 1.0601e+01 | 8.9231e+00 | 9.9662e+01 | 1.1919e+02 |
| E^6_7 | untwisted | 0.25 | 9.4409e+00 | 7.6762e+00 | 3.3963e+01 | 5.1080e+01 |
| E^6_7 | untwisted | 0.5 | 1.1575e+01 | 1.1218e+01 | 7.9367e+01 | 1.0216e+02 |
| E^6_7 | untwisted | 1.0 | 1.3462e+01 | 1.2723e+01 | 1.7813e+02 | 2.0432e+02 |
| E^6_7 | untwisted | 1.4 | 1.4767e+01 | 1.3324e+01 | 2.5796e+02 | 2.8605e+02 |

**Placement: 2fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 2.0317e-01 | 1.6680e-01 | 3.6521e+01 | 3.6891e+01 |
| E^1_12 | twisted | 0.5 | 1.0425e+00 | 2.7146e+00 | 7.0025e+01 | 7.3782e+01 |
| E^1_12 | twisted | 1.0 | 4.5506e+00 | 6.8569e+00 | 1.3616e+02 | 1.4756e+02 |
| E^1_12 | twisted | 1.4 | 4.1532e+00 | 6.0253e+00 | 1.9641e+02 | 2.0659e+02 |
| E^1_20 | twisted | 0.25 | 8.6988e+00 | 5.6399e+00 | 1.4174e+02 | 1.5608e+02 |
| E^1_20 | twisted | 0.5 | 5.0321e+00 | 6.9170e+00 | 3.0021e+02 | 3.1216e+02 |
| E^1_20 | twisted | 1.0 | 4.6144e+00 | 3.7791e+00 | 6.1592e+02 | 6.2431e+02 |
| E^1_20 | twisted | 1.4 | 7.8412e+00 | 6.1295e+00 | 8.6007e+02 | 8.7404e+02 |
| E^3_2 | twisted | 0.25 | 7.3450e-01 | 4.0796e-01 | 7.3728e-02 | 1.2162e+00 |
| E^3_2 | twisted | 0.5 | 1.3791e+00 | 8.1592e-01 | 2.3737e-01 | 2.4324e+00 |
| E^3_2 | twisted | 1.0 | 2.1242e+00 | 1.6318e+00 | 1.1087e+00 | 4.8648e+00 |
| E^3_2 | twisted | 1.4 | 2.0810e+00 | 2.2846e+00 | 2.4452e+00 | 6.8107e+00 |
| E^3_10 | twisted | 0.25 | 3.0183e+00 | 5.3786e+00 | 5.8494e+01 | 6.6891e+01 |
| E^3_10 | twisted | 0.5 | 6.0608e+00 | 8.5934e+00 | 1.1913e+02 | 1.3378e+02 |
| E^3_10 | twisted | 1.0 | 1.1036e+01 | 1.4424e+01 | 2.4210e+02 | 2.6756e+02 |
| E^3_10 | twisted | 1.4 | 1.0408e+01 | 1.2541e+01 | 3.5164e+02 | 3.7459e+02 |
| E^3'_6 | twisted | 0.25 | 1.8657e+00 | 4.6411e+00 | 1.0520e+01 | 1.7027e+01 |
| E^3'_6 | twisted | 0.5 | 3.3643e+00 | 6.4397e+00 | 2.4249e+01 | 3.4053e+01 |
| E^3'_6 | twisted | 1.0 | 6.2223e+00 | 5.9021e+00 | 5.5982e+01 | 6.8107e+01 |
| E^3'_6 | twisted | 1.4 | 6.5314e+00 | 6.3613e+00 | 8.2457e+01 | 9.5349e+01 |
| E^3'_10 | twisted | 0.25 | 1.2173e+01 | 4.0475e+00 | 5.0670e+01 | 6.6891e+01 |
| E^3'_10 | twisted | 0.5 | 9.5311e+00 | 8.2278e+00 | 1.1602e+02 | 1.3378e+02 |
| E^3'_10 | twisted | 1.0 | 8.4876e+00 | 6.2993e+00 | 2.5278e+02 | 2.6756e+02 |
| E^3'_10 | twisted | 1.4 | 9.8117e+00 | 8.6466e+00 | 3.5613e+02 | 3.7459e+02 |
| E^4_6 | twisted | 0.25 | 7.0250e+00 | 2.0922e+00 | 1.3585e+01 | 2.2702e+01 |
| E^4_6 | twisted | 0.5 | 8.8842e+00 | 4.0532e+00 | 3.2467e+01 | 4.5404e+01 |
| E^4_6 | twisted | 1.0 | 7.5876e+00 | 7.0118e+00 | 7.6210e+01 | 9.0809e+01 |
| E^4_6 | twisted | 1.4 | 7.6610e+00 | 7.7344e+00 | 1.1174e+02 | 1.2713e+02 |
| E^4_8 | twisted | 0.25 | 1.1168e+01 | 5.1705e+00 | 3.2310e+01 | 4.8648e+01 |
| E^4_8 | twisted | 0.5 | 1.1677e+01 | 7.3570e+00 | 7.8262e+01 | 9.7295e+01 |
| E^4_8 | twisted | 1.0 | 9.6543e+00 | 7.0468e+00 | 1.7789e+02 | 1.9459e+02 |
| E^4_8 | twisted | 1.4 | 1.0255e+01 | 8.9784e+00 | 2.5319e+02 | 2.7243e+02 |
| E^5_4 | twisted | 0.25 | 3.4569e+00 | 2.4162e+00 | 4.2618e+00 | 1.0135e+01 |
| E^5_4 | twisted | 0.5 | 5.5534e+00 | 4.2843e+00 | 1.0432e+01 | 2.0270e+01 |
| E^5_4 | twisted | 1.0 | 6.6506e+00 | 5.9678e+00 | 2.7921e+01 | 4.0540e+01 |
| E^5_4 | twisted | 1.4 | 6.8421e+00 | 6.9578e+00 | 4.2956e+01 | 5.6756e+01 |
| E^5_8 | twisted | 0.25 | 6.0220e+00 | 8.5513e+00 | 4.6236e+01 | 6.0810e+01 |
| E^5_8 | twisted | 0.5 | 9.6709e+00 | 1.1841e+01 | 1.0011e+02 | 1.2162e+02 |
| E^5_8 | twisted | 1.0 | 1.3858e+01 | 1.5329e+01 | 2.1405e+02 | 2.4324e+02 |
| E^5_8 | twisted | 1.4 | 1.3819e+01 | 1.4779e+01 | 3.1194e+02 | 3.4053e+02 |
| E^2_1 | untwisted | 0.25 | 2.0309e-01 | 0 | -3.8688e-04 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0617e-01 | 0 | -7.7376e-04 | 4.0540e-01 |
| E^2_1 | untwisted | 1.0 | 8.1234e-01 | 0 | -1.5475e-03 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1373e+00 | 0 | -2.1665e-03 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 1.4905e-01 | 4.6228e+00 | 5.3200e+01 | 5.7972e+01 |
| E^2_11 | untwisted | 0.5 | 4.0569e+00 | 4.5142e+00 | 1.0737e+02 | 1.1594e+02 |
| E^2_11 | untwisted | 1.0 | 9.7616e+00 | 7.4501e+00 | 2.1468e+02 | 2.3189e+02 |
| E^2_11 | untwisted | 1.4 | 8.0630e+00 | 8.7737e+00 | 3.0781e+02 | 3.2464e+02 |
| E^2'_7 | untwisted | 0.25 | 4.9804e+00 | 2.4276e+00 | 9.6186e+00 | 1.7027e+01 |
| E^2'_7 | untwisted | 0.5 | 4.7985e+00 | 4.5838e+00 | 2.4671e+01 | 3.4053e+01 |
| E^2'_7 | untwisted | 1.0 | 3.2386e+00 | 5.0512e+00 | 5.9817e+01 | 6.8107e+01 |
| E^2'_7 | untwisted | 1.4 | 4.6769e+00 | 2.7978e+00 | 8.7875e+01 | 9.5349e+01 |
| E^2'_13 | untwisted | 0.25 | 6.6194e+00 | 8.7797e+00 | 7.6829e+01 | 9.2228e+01 |
| E^2'_13 | untwisted | 0.5 | 7.8603e+00 | 9.3924e+00 | 1.6720e+02 | 1.8446e+02 |
| E^2'_13 | untwisted | 1.0 | 6.3363e+00 | 5.1652e+00 | 3.5741e+02 | 3.6891e+02 |
| E^2'_13 | untwisted | 1.4 | 9.5674e+00 | 7.0418e+00 | 4.9987e+02 | 5.1648e+02 |
| E^4'_3 | untwisted | 0.25 | 1.8060e+00 | 1.1018e+00 | 1.1462e+00 | 4.0540e+00 |
| E^4'_3 | untwisted | 0.5 | 3.1552e+00 | 2.0686e+00 | 2.8841e+00 | 8.1079e+00 |
| E^4'_3 | untwisted | 1.0 | 4.1430e+00 | 3.1863e+00 | 8.8866e+00 | 1.6216e+01 |
| E^4'_3 | untwisted | 1.4 | 4.6358e+00 | 3.1214e+00 | 1.4945e+01 | 2.2702e+01 |
| E^4'_9 | untwisted | 0.25 | 4.7814e+00 | 6.6589e+00 | 5.5450e+01 | 6.6891e+01 |
| E^4'_9 | untwisted | 0.5 | 9.2950e+00 | 7.9039e+00 | 1.1658e+02 | 1.3378e+02 |
| E^4'_9 | untwisted | 1.0 | 1.4630e+01 | 1.1125e+01 | 2.4181e+02 | 2.6756e+02 |
| E^4'_9 | untwisted | 1.4 | 1.2282e+01 | 1.3875e+01 | 3.4843e+02 | 3.7459e+02 |
| E^6_5 | untwisted | 0.25 | 5.8343e+00 | 4.1914e+00 | 1.1258e+01 | 2.1283e+01 |
| E^6_5 | untwisted | 0.5 | 8.6558e+00 | 6.9325e+00 | 2.6978e+01 | 4.2567e+01 |
| E^6_5 | untwisted | 1.0 | 1.0061e+01 | 8.7749e+00 | 6.6298e+01 | 8.5133e+01 |
| E^6_5 | untwisted | 1.4 | 1.0601e+01 | 8.9231e+00 | 9.9662e+01 | 1.1919e+02 |
| E^6_7 | untwisted | 0.25 | 7.7332e+00 | 7.3840e+00 | 3.5963e+01 | 5.1080e+01 |
| E^6_7 | untwisted | 0.5 | 1.1729e+01 | 9.8020e+00 | 8.0629e+01 | 1.0216e+02 |
| E^6_7 | untwisted | 1.0 | 1.5202e+01 | 1.1887e+01 | 1.7723e+02 | 2.0432e+02 |
| E^6_7 | untwisted | 1.4 | 1.4432e+01 | 1.4539e+01 | 2.5708e+02 | 2.8605e+02 |

**Placement: 3fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 1.1753e+00 | 1.8307e+00 | 3.3885e+01 | 3.6891e+01 |
| E^1_12 | twisted | 0.5 | 3.7056e+00 | 2.5762e+00 | 6.7500e+01 | 7.3782e+01 |
| E^1_12 | twisted | 1.0 | 4.1405e+00 | 3.8277e+00 | 1.3960e+02 | 1.4756e+02 |
| E^1_12 | twisted | 1.4 | 3.5669e+00 | 3.5524e+00 | 1.9947e+02 | 2.0659e+02 |
| E^1_20 | twisted | 0.25 | 6.2495e+00 | 5.6941e+00 | 1.4413e+02 | 1.5608e+02 |
| E^1_20 | twisted | 0.5 | 6.4394e+00 | 4.4472e+00 | 3.0127e+02 | 3.1216e+02 |
| E^1_20 | twisted | 1.0 | 6.1619e+00 | 5.9649e+00 | 6.1218e+02 | 6.2431e+02 |
| E^1_20 | twisted | 1.4 | 5.8095e+00 | 6.1927e+00 | 8.6203e+02 | 8.7404e+02 |
| E^3_2 | twisted | 0.25 | 7.3450e-01 | 4.0796e-01 | 7.3728e-02 | 1.2162e+00 |
| E^3_2 | twisted | 0.5 | 1.3791e+00 | 8.1592e-01 | 2.3737e-01 | 2.4324e+00 |
| E^3_2 | twisted | 1.0 | 2.1242e+00 | 1.6318e+00 | 1.1087e+00 | 4.8648e+00 |
| E^3_2 | twisted | 1.4 | 2.0810e+00 | 2.2846e+00 | 2.4452e+00 | 6.8107e+00 |
| E^3_10 | twisted | 0.25 | 5.1579e+00 | 6.0254e+00 | 5.5707e+01 | 6.6891e+01 |
| E^3_10 | twisted | 0.5 | 8.1741e+00 | 9.3879e+00 | 1.1622e+02 | 1.3378e+02 |
| E^3_10 | twisted | 1.0 | 1.0124e+01 | 9.9111e+00 | 2.4753e+02 | 2.6756e+02 |
| E^3_10 | twisted | 1.4 | 9.1304e+00 | 9.6729e+00 | 3.5578e+02 | 3.7459e+02 |
| E^3'_6 | twisted | 0.25 | 2.6971e+00 | 3.9233e+00 | 1.0406e+01 | 1.7027e+01 |
| E^3'_6 | twisted | 0.5 | 4.2736e+00 | 5.6441e+00 | 2.4136e+01 | 3.4053e+01 |
| E^3'_6 | twisted | 1.0 | 6.1577e+00 | 5.6546e+00 | 5.6294e+01 | 6.8107e+01 |
| E^3'_6 | twisted | 1.4 | 5.5431e+00 | 6.0457e+00 | 8.3761e+01 | 9.5349e+01 |
| E^3'_10 | twisted | 0.25 | 1.0570e+01 | 4.3290e+00 | 5.1992e+01 | 6.6891e+01 |
| E^3'_10 | twisted | 0.5 | 9.6968e+00 | 6.5604e+00 | 1.1752e+02 | 1.3378e+02 |
| E^3'_10 | twisted | 1.0 | 1.0140e+01 | 8.2929e+00 | 2.4913e+02 | 2.6756e+02 |
| E^3'_10 | twisted | 1.4 | 1.0573e+01 | 9.5689e+00 | 3.5444e+02 | 3.7459e+02 |
| E^4_6 | twisted | 0.25 | 6.1936e+00 | 2.8101e+00 | 1.3699e+01 | 2.2702e+01 |
| E^4_6 | twisted | 0.5 | 7.9749e+00 | 4.8487e+00 | 3.2581e+01 | 4.5404e+01 |
| E^4_6 | twisted | 1.0 | 7.6522e+00 | 7.2593e+00 | 7.5897e+01 | 9.0809e+01 |
| E^4_6 | twisted | 1.4 | 8.6493e+00 | 8.0499e+00 | 1.1043e+02 | 1.2713e+02 |
| E^4_8 | twisted | 0.25 | 9.6405e+00 | 5.4114e+00 | 3.3596e+01 | 4.8648e+01 |
| E^4_8 | twisted | 0.5 | 1.0508e+01 | 7.2894e+00 | 7.9498e+01 | 9.7295e+01 |
| E^4_8 | twisted | 1.0 | 1.0255e+01 | 9.3236e+00 | 1.7501e+02 | 1.9459e+02 |
| E^4_8 | twisted | 1.4 | 1.1393e+01 | 1.0604e+01 | 2.5043e+02 | 2.7243e+02 |
| E^5_4 | twisted | 0.25 | 3.4569e+00 | 2.4162e+00 | 4.2618e+00 | 1.0135e+01 |
| E^5_4 | twisted | 0.5 | 5.5534e+00 | 4.2843e+00 | 1.0432e+01 | 2.0270e+01 |
| E^5_4 | twisted | 1.0 | 6.6506e+00 | 5.9678e+00 | 2.7921e+01 | 4.0540e+01 |
| E^5_4 | twisted | 1.4 | 6.8421e+00 | 6.9578e+00 | 4.2956e+01 | 5.6756e+01 |
| E^5_8 | twisted | 0.25 | 7.5491e+00 | 8.3104e+00 | 4.4950e+01 | 6.0810e+01 |
| E^5_8 | twisted | 0.5 | 1.0840e+01 | 1.1908e+01 | 9.8871e+01 | 1.2162e+02 |
| E^5_8 | twisted | 1.0 | 1.3257e+01 | 1.3052e+01 | 2.1693e+02 | 2.4324e+02 |
| E^5_8 | twisted | 1.4 | 1.2681e+01 | 1.3153e+01 | 3.1470e+02 | 3.4053e+02 |
| E^2_1 | untwisted | 0.25 | 2.0309e-01 | 0 | -3.8688e-04 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0617e-01 | 0 | -7.7376e-04 | 4.0540e-01 |
| E^2_1 | untwisted | 1.0 | 8.1234e-01 | 0 | -1.5475e-03 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1373e+00 | 0 | -2.1665e-03 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 2.3247e+00 | 5.5581e+00 | 5.0089e+01 | 5.7972e+01 |
| E^2_11 | untwisted | 0.5 | 5.6480e+00 | 7.0206e+00 | 1.0327e+02 | 1.1594e+02 |
| E^2_11 | untwisted | 1.0 | 7.8097e+00 | 6.1153e+00 | 2.1796e+02 | 2.3189e+02 |
| E^2_11 | untwisted | 1.4 | 6.5257e+00 | 6.5204e+00 | 3.1160e+02 | 3.2464e+02 |
| E^2'_7 | untwisted | 0.25 | 4.1852e+00 | 2.4030e+00 | 1.0439e+01 | 1.7027e+01 |
| E^2'_7 | untwisted | 0.5 | 4.4158e+00 | 3.8781e+00 | 2.5759e+01 | 3.4053e+01 |
| E^2'_7 | untwisted | 1.0 | 3.9406e+00 | 4.8812e+00 | 5.9285e+01 | 6.8107e+01 |
| E^2'_7 | untwisted | 1.4 | 5.1406e+00 | 4.7714e+00 | 8.5437e+01 | 9.5349e+01 |
| E^2'_13 | untwisted | 0.25 | 6.8203e+00 | 7.3251e+00 | 7.8082e+01 | 9.2228e+01 |
| E^2'_13 | untwisted | 0.5 | 6.8844e+00 | 7.4758e+00 | 1.7010e+02 | 1.8446e+02 |
| E^2'_13 | untwisted | 1.0 | 7.7633e+00 | 9.6991e+00 | 3.5145e+02 | 3.6891e+02 |
| E^2'_13 | untwisted | 1.4 | 8.4588e+00 | 9.0363e+00 | 4.9898e+02 | 5.1648e+02 |
| E^4'_3 | untwisted | 0.25 | 1.8060e+00 | 1.1018e+00 | 1.1462e+00 | 4.0540e+00 |
| E^4'_3 | untwisted | 0.5 | 3.1552e+00 | 2.0686e+00 | 2.8841e+00 | 8.1079e+00 |
| E^4'_3 | untwisted | 1.0 | 4.1430e+00 | 3.1863e+00 | 8.8866e+00 | 1.6216e+01 |
| E^4'_3 | untwisted | 1.4 | 4.6358e+00 | 3.1214e+00 | 1.4945e+01 | 2.2702e+01 |
| E^4'_9 | untwisted | 0.25 | 6.6019e+00 | 7.1536e+00 | 5.3135e+01 | 6.6891e+01 |
| E^4'_9 | untwisted | 0.5 | 1.0301e+01 | 9.7091e+00 | 1.1377e+02 | 1.3378e+02 |
| E^4'_9 | untwisted | 1.0 | 1.2749e+01 | 9.7560e+00 | 2.4506e+02 | 2.6756e+02 |
| E^4'_9 | untwisted | 1.4 | 1.1427e+01 | 1.0528e+01 | 3.5263e+02 | 3.7459e+02 |
| E^6_5 | untwisted | 0.25 | 5.8343e+00 | 4.1914e+00 | 1.1258e+01 | 2.1283e+01 |
| E^6_5 | untwisted | 0.5 | 8.6558e+00 | 6.9325e+00 | 2.6978e+01 | 4.2567e+01 |
| E^6_5 | untwisted | 1.0 | 1.0061e+01 | 8.7749e+00 | 6.6298e+01 | 8.5133e+01 |
| E^6_5 | untwisted | 1.4 | 1.0601e+01 | 8.9231e+00 | 9.9662e+01 | 1.1919e+02 |
| E^6_7 | untwisted | 0.25 | 8.5285e+00 | 7.4086e+00 | 3.5143e+01 | 5.1080e+01 |
| E^6_7 | untwisted | 0.5 | 1.2112e+01 | 1.0508e+01 | 7.9541e+01 | 1.0216e+02 |
| E^6_7 | untwisted | 1.0 | 1.4500e+01 | 1.2057e+01 | 1.7776e+02 | 2.0432e+02 |
| E^6_7 | untwisted | 1.4 | 1.3968e+01 | 1.2565e+01 | 2.5951e+02 | 2.8605e+02 |

**Placement: 5fold**

| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |
|---|---|---|---|---|---|---|
| E^1_12 | twisted | 0.25 | 3.2768e+00 | 1.8724e+00 | 3.1742e+01 | 3.6891e+01 |
| E^1_12 | twisted | 0.5 | 2.8689e+00 | 1.9174e+00 | 6.8996e+01 | 7.3782e+01 |
| E^1_12 | twisted | 1.0 | 3.9800e+00 | 2.8516e+00 | 1.4073e+02 | 1.4756e+02 |
| E^1_12 | twisted | 1.4 | 4.3155e+00 | 3.7196e+00 | 1.9856e+02 | 2.0659e+02 |
| E^1_20 | twisted | 0.25 | 5.8599e+00 | 3.2902e+00 | 1.4693e+02 | 1.5608e+02 |
| E^1_20 | twisted | 0.5 | 6.7469e+00 | 6.3578e+00 | 2.9905e+02 | 3.1216e+02 |
| E^1_20 | twisted | 1.0 | 6.0570e+00 | 6.0803e+00 | 6.1217e+02 | 6.2431e+02 |
| E^1_20 | twisted | 1.4 | 6.2727e+00 | 6.1061e+00 | 8.6166e+02 | 8.7404e+02 |
| E^3_2 | twisted | 0.25 | 7.3450e-01 | 4.0796e-01 | 7.3728e-02 | 1.2162e+00 |
| E^3_2 | twisted | 0.5 | 1.3791e+00 | 8.1592e-01 | 2.3737e-01 | 2.4324e+00 |
| E^3_2 | twisted | 1.0 | 2.1242e+00 | 1.6318e+00 | 1.1087e+00 | 4.8648e+00 |
| E^3_2 | twisted | 1.4 | 2.0810e+00 | 2.2846e+00 | 2.4452e+00 | 6.8107e+00 |
| E^3_10 | twisted | 0.25 | 8.1829e+00 | 3.8513e+00 | 5.4856e+01 | 6.6891e+01 |
| E^3_10 | twisted | 0.5 | 8.8081e+00 | 5.8899e+00 | 1.1908e+02 | 1.3378e+02 |
| E^3_10 | twisted | 1.0 | 1.0584e+01 | 7.6911e+00 | 2.4929e+02 | 2.6756e+02 |
| E^3_10 | twisted | 1.4 | 1.0533e+01 | 9.5323e+00 | 3.5452e+02 | 3.7459e+02 |
| E^3'_6 | twisted | 0.25 | 4.4076e+00 | 2.0047e+00 | 1.0614e+01 | 1.7027e+01 |
| E^3'_6 | twisted | 0.5 | 5.8894e+00 | 3.3676e+00 | 2.4796e+01 | 3.4053e+01 |
| E^3'_6 | twisted | 1.0 | 6.2101e+00 | 4.8977e+00 | 5.6999e+01 | 6.8107e+01 |
| E^3'_6 | twisted | 1.4 | 6.4727e+00 | 5.9401e+00 | 8.2937e+01 | 9.5349e+01 |
| E^3'_10 | twisted | 0.25 | 1.0290e+01 | 4.8592e+00 | 5.1742e+01 | 6.6891e+01 |
| E^3'_10 | twisted | 0.5 | 8.8513e+00 | 9.5165e+00 | 1.1541e+02 | 1.3378e+02 |
| E^3'_10 | twisted | 1.0 | 9.8062e+00 | 9.6639e+00 | 2.4809e+02 | 2.6756e+02 |
| E^3'_10 | twisted | 1.4 | 9.9177e+00 | 1.0107e+01 | 3.5456e+02 | 3.7459e+02 |
| E^4_6 | twisted | 0.25 | 4.4831e+00 | 4.7287e+00 | 1.3490e+01 | 2.2702e+01 |
| E^4_6 | twisted | 0.5 | 6.3591e+00 | 7.1253e+00 | 3.1920e+01 | 4.5404e+01 |
| E^4_6 | twisted | 1.0 | 7.5998e+00 | 8.0162e+00 | 7.5193e+01 | 9.0809e+01 |
| E^4_6 | twisted | 1.4 | 7.7197e+00 | 8.1555e+00 | 1.1126e+02 | 1.2713e+02 |
| E^4_8 | twisted | 0.25 | 7.6130e+00 | 7.1930e+00 | 3.3842e+01 | 4.8648e+01 |
| E^4_8 | twisted | 0.5 | 9.3061e+00 | 1.0405e+01 | 7.7584e+01 | 9.7295e+01 |
| E^4_8 | twisted | 1.0 | 9.9863e+00 | 1.1166e+01 | 1.7344e+02 | 1.9459e+02 |
| E^4_8 | twisted | 1.4 | 1.0259e+01 | 1.0760e+01 | 2.5141e+02 | 2.7243e+02 |
| E^5_4 | twisted | 0.25 | 3.4569e+00 | 2.4162e+00 | 4.2618e+00 | 1.0135e+01 |
| E^5_4 | twisted | 0.5 | 5.5534e+00 | 4.2843e+00 | 1.0432e+01 | 2.0270e+01 |
| E^5_4 | twisted | 1.0 | 6.6506e+00 | 5.9678e+00 | 2.7921e+01 | 4.0540e+01 |
| E^5_4 | twisted | 1.4 | 6.8421e+00 | 6.9578e+00 | 4.2956e+01 | 5.6756e+01 |
| E^5_8 | twisted | 0.25 | 9.5766e+00 | 6.5287e+00 | 4.4704e+01 | 6.0810e+01 |
| E^5_8 | twisted | 0.5 | 1.2042e+01 | 8.7922e+00 | 1.0079e+02 | 1.2162e+02 |
| E^5_8 | twisted | 1.0 | 1.3526e+01 | 1.1210e+01 | 2.1850e+02 | 2.4324e+02 |
| E^5_8 | twisted | 1.4 | 1.3815e+01 | 1.2997e+01 | 3.1372e+02 | 3.4053e+02 |
| E^2_1 | untwisted | 0.25 | 2.0309e-01 | 0 | -3.8688e-04 | 2.0270e-01 |
| E^2_1 | untwisted | 0.5 | 4.0617e-01 | 0 | -7.7376e-04 | 4.0540e-01 |
| E^2_1 | untwisted | 1.0 | 8.1234e-01 | 0 | -1.5475e-03 | 8.1079e-01 |
| E^2_1 | untwisted | 1.4 | 1.1373e+00 | 0 | -2.1665e-03 | 1.1351e+00 |
| E^2_11 | untwisted | 0.25 | 5.8833e+00 | 4.2674e+00 | 4.7821e+01 | 5.7972e+01 |
| E^2_11 | untwisted | 0.5 | 4.8436e+00 | 6.6016e+00 | 1.0450e+02 | 1.1594e+02 |
| E^2_11 | untwisted | 1.0 | 6.4667e+00 | 8.7139e+00 | 2.1671e+02 | 2.3189e+02 |
| E^2_11 | untwisted | 1.4 | 7.3842e+00 | 8.5915e+00 | 3.0867e+02 | 3.2464e+02 |
| E^2'_7 | untwisted | 0.25 | 3.4670e+00 | 2.0153e+00 | 1.1544e+01 | 1.7027e+01 |
| E^2'_7 | untwisted | 0.5 | 4.8467e+00 | 2.6707e+00 | 2.6536e+01 | 3.4053e+01 |
| E^2'_7 | untwisted | 1.0 | 5.0584e+00 | 3.3417e+00 | 5.9707e+01 | 6.8107e+01 |
| E^2'_7 | untwisted | 1.4 | 4.8291e+00 | 3.3295e+00 | 8.7191e+01 | 9.5349e+01 |
| E^2'_13 | untwisted | 0.25 | 9.9931e+00 | 7.3188e+00 | 7.4916e+01 | 9.2228e+01 |
| E^2'_13 | untwisted | 0.5 | 5.5560e+00 | 9.6341e+00 | 1.6927e+02 | 1.8446e+02 |
| E^2'_13 | untwisted | 1.0 | 8.1884e+00 | 7.5729e+00 | 3.5315e+02 | 3.6891e+02 |
| E^2'_13 | untwisted | 1.4 | 9.2444e+00 | 8.0476e+00 | 4.9918e+02 | 5.1648e+02 |
| E^4'_3 | untwisted | 0.25 | 1.8060e+00 | 1.1018e+00 | 1.1462e+00 | 4.0540e+00 |
| E^4'_3 | untwisted | 0.5 | 3.1552e+00 | 2.0686e+00 | 2.8841e+00 | 8.1079e+00 |
| E^4'_3 | untwisted | 1.0 | 4.1430e+00 | 3.1863e+00 | 8.8866e+00 | 1.6216e+01 |
| E^4'_3 | untwisted | 1.4 | 4.6358e+00 | 3.1214e+00 | 1.4945e+01 | 2.2702e+01 |
| E^4'_9 | untwisted | 0.25 | 8.1960e+00 | 7.2457e+00 | 5.1449e+01 | 6.6891e+01 |
| E^4'_9 | untwisted | 0.5 | 9.7688e+00 | 1.0164e+01 | 1.1385e+02 | 1.3378e+02 |
| E^4'_9 | untwisted | 1.0 | 1.1131e+01 | 1.3028e+01 | 2.4340e+02 | 2.6756e+02 |
| E^4'_9 | untwisted | 1.4 | 1.1950e+01 | 1.2997e+01 | 3.4964e+02 | 3.7459e+02 |
| E^6_5 | untwisted | 0.25 | 5.8343e+00 | 4.1914e+00 | 1.1258e+01 | 2.1283e+01 |
| E^6_5 | untwisted | 0.5 | 8.6558e+00 | 6.9325e+00 | 2.6978e+01 | 4.2567e+01 |
| E^6_5 | untwisted | 1.0 | 1.0061e+01 | 8.7749e+00 | 6.6298e+01 | 8.5133e+01 |
| E^6_5 | untwisted | 1.4 | 1.0601e+01 | 8.9231e+00 | 9.9662e+01 | 1.1919e+02 |
| E^6_7 | untwisted | 0.25 | 9.2467e+00 | 7.7963e+00 | 3.4037e+01 | 5.1080e+01 |
| E^6_7 | untwisted | 0.5 | 1.1681e+01 | 1.1715e+01 | 7.8764e+01 | 1.0216e+02 |
| E^6_7 | untwisted | 1.0 | 1.3382e+01 | 1.3597e+01 | 1.7734e+02 | 2.0432e+02 |
| E^6_7 | untwisted | 1.4 | 1.4280e+01 | 1.4007e+01 | 2.5776e+02 | 2.8605e+02 |

## 7. Outcome Classes

### Methodology

For each block, sampler, and cone condition, Lambda = ||O||^2 - ||P_1 O||^2 was
checked at all 4 placements and 4 widths. A value is zero if below 10^{-12}
relative to ||O||^2 (section 7 zero rule).

### Results

**All blocks have Lambda > 0 at all placements for all samplers and all cone conditions.**

Specifically, no block satisfies Lambda = 0 at any placement for any W in {1/4, 1/2, 1, 7/5}.
This means the outcome class is **N (leakage)** for every arm/sampler/cone condition.

| Arm | Sampler | Cone condition | Outcome class |
|---|---|---|---|
| twisted | O^(0) | Friedrichs | N |
| twisted | O^(0) | bridging | N (same Lambda as Friedrichs) |
| twisted | O^(1) | Friedrichs | N |
| twisted | O^(1) | bridging | N (same Lambda as Friedrichs) |
| untwisted | O^(0) | Friedrichs | N |
| untwisted | O^(0) | phi_0-transformed | N (same Lambda as Friedrichs) |
| untwisted | O^(0) | SCTM | N |
| untwisted | O^(1) | Friedrichs | N |
| untwisted | O^(1) | phi_0-transformed | N (same Lambda as Friedrichs) |
| untwisted | O^(1) | SCTM | N |

### Placement-independent blocks

The following blocks have HS norms, P_1 projections, and Lambda identical across all placements
(to < 1% relative variation):

- Value sampler: E^3_2, E^5_4, E^2_1, E^4'_3, E^6_5
- Transverse sampler: E^3_2, E^5_4, E^2_1, E^4'_3, E^6_5

### 2-fold symmetric probe

At the 2-fold placement (p = i, c = j), left multiplication by +/-k preserves the core
circle. No zero of Lambda at the 2-fold placement was found for any block.

## 8. Files

- `core.py` -- 2I group construction, characters, placements, band map, Gegenbauer polynomials
- `compute_all.py` -- main computation: HS norms, first-positive projections, leakage for Friedrichs
- `compute_sctm.py` -- SCTM first-positive projections
- `compute_ground.py` -- ground-level projections for per-level tables
- `spectral_step.py` -- spectral step: secular equation, root-finding, mode-crossing analysis
- `compile_return.py` -- assembles results into RETURN.md
- `validate.py` -- quick validation of E^2_1 block (analytic cross-check)
- `process_results.py` -- summary tables and W-linearity check
- `results.json` -- 304 numerical results (HS norms, projections, leakage)
- `results_sctm.json` -- 304 SCTM projection results
- `results_ground.json` -- 304 ground-level projection results

## 9. Consulted Material

- `TASK.md` -- task specification (sections 1-8)
- `REFERENCE.md` -- the paper on the conic Mobius band and its operator
- `BRIEF.md` -- instructions file

## 10. Underdetermined Points

1. **Same cone-trace matching spectrum for general W.** The task asks to grade leakage against the SCTM
   first positive eigenspace for every W. The spectral step was computed for all four tabulated widths
   and the mode-crossing at W = pi/4 was identified. For W in (0, pi/4], the first positive eigenvalue
   is 6 (constant symmetric sector). For W in (pi/4, pi/2), it is alpha_0(alpha_0+1) = (pi/(2W))(pi/(2W)+1)
   (odd nonconstant sector). These formulas hold for all W in (0, pi/2), so the spectral step covers
   the full range.

2. **Symbolic forms in orientation.** The HS norms are placement-independent (proven by the constancy
   of K_E(q,q) on S^2). For projections, some blocks (E^3_2, E^5_4, E^2_1, E^4'_3, E^6_5) are
   placement-independent; others depend on placement. A closed-form polynomial in the frame entries
   was not computed.

3. **Bridging ground mode.** The defect-bound eigenfunction of twisted bridging (and hence the untwisted
   phi_0-transformed ground) was not computed explicitly. The per-level decomposition for these conditions
   is reported as missing at the ground level.

4. **Number of positive levels.** One positive level was chosen for the per-level table. The eigenspaces
   at higher levels involve mode crossings and sector-dependent eigenfunctions that were not tabulated.
