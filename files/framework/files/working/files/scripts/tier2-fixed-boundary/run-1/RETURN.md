# Results: Dirichlet Jacobi spectrum of a minimal Mobius band in S^3

## Per-sector results

### Sector m = 0

- **Index:** 0. Decided by §4.2 (Sturm count = 0, Chebyshev index = 0).
- **Nullity:** 1. Decided by §4.4: psi_X is exhibited as an exact zero eigenfunction satisfying both boundary conditions. The near-zero numerical eigenvalue (mu ~ -1.4e-12) is resolved as nullity.
- **Sturm count:** 0 interior zeros.
- **Endpoint ratio:** rho = 4.778534e-12 (near-zero case).
- **Chebyshev eigenvalues (mu = lambda R^2):**

| N=64 | N=128 | |diff| |
|------|-------|--------|
| -7.298375679700e-14 | -1.403562511105e-12 | 1.33e-12 |
| 1.165988590218e+01 | 1.165988590217e+01 | 1.28e-12 |

- **C1 eigenfunction check:** sup-norm difference between normalized numerical eigenfunction and normalized psi_X = 1.33e-13. Passes the 1e-6 threshold.

### Sector m = 1

- **Index:** 1. Decided by §4.1 (one zero of phi_K in (0, pi/2)), confirmed by §4.2 (Sturm count = 1, Chebyshev index = 1).
- **Nullity:** 0. Decided by §4.1: phi_K(pi/2) = 1/2 != 0. No near-zero case in §4.2.
- **Closed form of phi_K:**
$$\varphi_K(t) = \frac{3\sin^2 t - 2}{2\sqrt{4 - 3\sin^2 t}}$$
  (equivalently: (3 sin^2 t - 2) / (4 sqrt(f)), where f = 1 - 3 sin^2(t)/4).
  This is the t-profile of the normal component of the Killing combination (X_13 + X_24), which is sector-pure for |m| = 1.
- **Zeros in (0, pi/2):** Exactly one, at t* = arcsin(sqrt(2/3)) = 0.955316618125... Verified by symbolic root isolation: phi_K = 0 iff 3 sin^2(t) = 2, i.e. sin^2(t) = 2/3. Since 0 < sqrt(2/3) < 1, there is exactly one solution in (0, pi/2). Cross-checked by Sturm shooting zero at t = 0.955316618125.
- **Sturm count:** 1 interior zero at t = 0.955316618125.
- **Endpoint ratio:** rho = 1.000000e+00.
- **Chebyshev eigenvalues:**

| N=64 | N=128 | |diff| |
|------|-------|--------|
| -1.999999999998e+00 | -1.999999999952e+00 | 4.54e-11 |
| 5.245448707917e+00 | 5.245448707880e+00 | 3.69e-11 |

### Sector m = 2

- **Index:** 0. Decided by §4.2 (Sturm count = 0, Chebyshev index = 0).
- **Nullity:** 0. No near-zero case (smallest mu > 1, rho = 0.74).
- **Sturm count:** 0 interior zeros.
- **Endpoint ratio:** rho = 7.380306e-01.
- **Chebyshev eigenvalues:**

| N=64 | N=128 | |diff| |
|------|-------|--------|
| 1.849413336656e+00 | 1.849413336655e+00 | 1.24e-12 |

### Sector m = 3

- **Index:** 0. Decided by §4.1 (no zeros of phi_K in (0, pi/2)), confirmed by §4.2 (Sturm count = 0, Chebyshev index = 0).
- **Nullity:** 0. Decided by §4.1: phi_K(pi/2) = 1/2 != 0. No near-zero case in §4.2.
- **Closed form of phi_K:**
$$\varphi_K(t) = \frac{1 + \cos^2 t}{2\sqrt{4 - 3\sin^2 t}}$$
  (equivalently: (1 + cos^2 t) / (4 sqrt(f))).
  This is the t-profile of the normal component of the Killing combination (X_13 - X_24), which is sector-pure for |m| = 3.
- **Zeros in (0, pi/2):** None. phi_K(t) = (1 + cos^2 t)/(4 sqrt(f)) > 0 for all t, since 1 + cos^2(t) >= 1 and f > 0.
- **Sturm count:** 0 interior zeros.
- **Endpoint ratio:** rho = 1.000000e+00.
- **Chebyshev eigenvalues:**

| N=64 | N=128 | |diff| |
|------|-------|--------|
| 6.916191422806e-01 | 6.916191422377e-01 | 4.33e-11 |
| 9.122935239526e+00 | 9.122935239500e+00 | 2.59e-11 |

## Totals

Each sector |m| >= 1 counts twice (for +m and -m); sector m = 0 counts once.

- **Total index I = 2.** Contributions: m = 0 contributes 0; m = +/-1 contributes 2 x 1 = 2; m = +/-2 contributes 0; m = +/-3 contributes 0; |m| >= 4 contributes 0 (given).
- **Total nullity N = 1.** Contributions: m = 0 contributes 1; all other sectors contribute 0.

## Outcome class

**O2: I >= 1.** I = 2, carried by sectors m = +/-1.

## Controls

### C1: m = 0 standard operator
**PASS.** Sector m = 0 via §4.2 gives index = 0 and exactly one near-zero case (mu ~ -1.4e-12, rho ~ 4.8e-12). Resolved as nullity = 1 by exhibiting psi_X (§4.4). The normalized numerical eigenfunction matches psi_X to 1.33e-13 in sup norm, well within the 1e-6 threshold.

### C2: Symbolic verification and route agreement
**PASS.** R^2 J_1 phi_K = 0 verified symbolically (sympy simplification yields exactly 0). R^2 J_3 phi_K = 0 verified symbolically (sympy simplification yields exactly 0). R^2 J_0 psi_X = 0 verified symbolically (numerator of the combined expression equals 0 after trigsimp+expand). Routes §4.1 and §4.2 agree: m = 1 has index 1, m = 3 has index 0.

### C3: Mutated operators
**PASS.** Both mutations cause C1 to fail:
- Mutation 1 (Ric = 3/R^2): Sturm count = 1, Chebyshev first eigenvalue = -1.0. Index becomes 1 instead of 0. C1 fails.
- Mutation 2 (|A|^2 dropped): Sturm count = 0, Chebyshev first eigenvalue = 1.855. No near-zero case. C1 fails (no near-zero eigenvalue where one is expected).

## Method as run

Section 4 was followed exactly. No deviations were necessary.

- §4.1: The four Killing fields X_13, X_14, X_23, X_24 were computed as functions on the annulus. Their normal components were decomposed into Fourier modes in s/2 using product-to-sum identities. Sector-pure combinations: (X_13 + X_24) and (X_14 - X_23) for |m| = 1; (X_13 - X_24) and -(X_14 + X_23) for |m| = 3.
- §4.2: Sturm count by solve_ivp with DOP853 (rtol=1e-12, atol=1e-14), 100001-point grid, Brent refinement. Chebyshev collocation at N=64 and N=128, using scipy.linalg.eig. All compared eigenvalue pairs agree to better than 1e-8 in absolute value.
- §4.3-4.4: Controls run as specified. Near-zero cases resolved only where exact solutions are exhibited.

## Files

- `step1_killing.py` — Computes unit normal and Killing field normal components.
- `step1b_sectors.py` — Fourier decomposition into sectors; identifies phi_K; counts zeros.
- `step2_verify_jacobi.py` — Symbolic verification that J_m phi_K = 0 for m = 0, 1, 3.
- `step2b_verify_m0.py` — Extended symbolic verification for m = 0 (psi_X).
- `step3_numerical.py` — Sturm count and Chebyshev eigenvalue computation for all sectors.
- `step3_cheb_fix.py` — Debugging and verification of Chebyshev differentiation matrix.
- `step3_debug_m0.py`, `step3_debug2.py` — Intermediate debugging scripts.
- `step4_controls.py` — All three controls C1, C2, C3.

All output records are in the terminal output of the above scripts.

## Consulted material

- `BRIEF.md` — Instructions and scope.
- `TASK.md` — Full problem statement with sections 1-5.

No other files were read.

## Underdetermined points

None identified. All computations reached definite values and all controls passed.
