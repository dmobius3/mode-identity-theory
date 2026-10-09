<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Static Domain's Stability

**Type:** Result
**State:** Closed
**Status (2026-10-05):** Derived, checked by one script. On the stress-tensor bridge's branches (a) and (c), where Einstein's equations hold on the static metric, the static closed domain's linear perturbations split into four sectors. For every perfect-fluid source with $`\rho + p > 0`$, the homogeneous shape modes and the vector and tensor modes oscillate without growing. The radius mode and the density modes turn on the source's response law: for a barotropic law with sound speed $`c_s^2`$, the radius grows unless $`c_s^2 < -1/3`$ and the density modes grow unless $`c_s^2 > 1/5`$, so with both admitted no barotropic source keeps both quiet. Holding the radius fixed removes the radius mode only together with the source's homogeneous perturbation, a restriction on the dynamics rather than stability. The coefficient-3 source and the sources the record's readings of R require have no response law on the record, so those cells stay open. On branch (b) the test does not apply. The result adds C12 to the bridge's entry test.
**Summary:** Which linear perturbations of the static closed domain grow, on each branch of the stress-tensor bridge's placement fork, and what a candidate source must declare as a result.
**Inputs:** `stress-tensor-bridge.md` (C1, C2, §III, §IX), `../../../../cosmos/files/cosmological-constant.md` §IV, §VI, `temporal-budget.md` §IX, `../../../README.md`, `scripts/static-domain-stability/stability_check.py`
**Parent:** `stress-tensor-bridge.md`

---

RESULT, a derivation with no pre-committed pass condition. [The Λ page](../../../../cosmos/files/cosmological-constant.md) leaves "the dynamical stability of the cosmology" open (§VI), and in general relativity the conventional perfect-fluid Einstein static universe is the classic unstable case: Eddington showed it unstable to homogeneous isotropic perturbations. This page asks what classical general relativity says about the static domain's linear stability on each branch of [the stress-tensor bridge](stress-tensor-bridge.md)'s placement fork, sector by sector, and what a candidate source must declare as a result. It selects no branch and no source.

**Related:** [The Stress-Tensor Bridge](stress-tensor-bridge.md), [Cosmological Constant](../../../../cosmos/files/cosmological-constant.md), [The Missing Spatial Projection](missing-spatial-projection.md), [The Effective-Metric Floors](effective-metric-floors.md).

## I. The setting

The background is the static closed universe of radius $`R`$, with cosmological constant $`\Lambda`$ and a perfect fluid $`(\rho, p)`$. At $`\dot a = \ddot a = 0`$ the Friedmann and Raychaudhuri equations give

```math
\frac{1}{R^2} = 4\pi G(\rho + p), \qquad \Lambda = 4\pi G(\rho + 3p), \qquad \Lambda R^2 = 3 - \frac{2}{1 + w},
```

as on the Λ page (§IV), so a static radius needs $`\rho + p > 0`$.

- **The response law.** Adiabatic perturbations of a barotropic fluid have $`\delta p = c_s^2\,\delta\rho`$, with $`c_s^2 = dp/d\rho`$ at the background. It equals $`w = p/\rho`$ only for the linear law $`p = w\rho`$, and $`\Lambda R^2`$ does not fix it.
- **Harmonics.** On the unit $`S^3`$, scalar harmonics have $`\nabla^2 Q = -k^2 Q`$ with $`k^2 = n(n+2)`$.
- **The four sectors.**
  - H-ISO: the homogeneous isotropic mode, the radius itself.
  - H-ANISO: the homogeneous anisotropic modes, of Bianchi type IX.
  - I-S: inhomogeneous scalar density modes.
  - I-V/T: inhomogeneous vector and tensor modes.
- **The verdicts.**
  - STABLE: perturbations decay.
  - NEUTRALLY STABLE: they stay bounded without decaying, with undamped oscillations, so the static solution is not an attractor.
  - UNSTABLE: some perturbation grows.
  - NOT ADMITTED: the sector is removed from the admissible phase space, for instance by holding the radius fixed. This records a restriction on the dynamics and is never STABLE.
  - NOT APPLICABLE: the branch's equations do not govern the static metric.
  - OPEN, SOURCE DYNAMICS MISSING: the source has no declared linear response law.

  On a static background nothing decays, so no cell below reads STABLE.
- **Scope.** Linear perturbations only. The static closed universe has compact slices and many Killing symmetries, so a linearized solution is tangent to a true one only where higher-order constraints hold, the linearization instability that Barrow and Yamamoto note in their §1. The verdicts are for the linearized problem.

## II. The four sectors

### H-ISO, the radius

Perturb $`a = R(1 + \epsilon)`$. Continuity gives $`\delta\rho = -3(\rho + p)\,\epsilon`$, and the Raychaudhuri equation, $`\ddot a/a = -\tfrac{4\pi G}{3}(\rho + 3p) + \Lambda/3`$, then gives

```math
\ddot\epsilon = -\frac{4\pi G}{3}\left(1 + 3c_s^2\right)\delta\rho = \frac{1 + 3c_s^2}{R^2}\,\epsilon .
```

The Friedmann constraint holds identically at first order. The radius grows exponentially for $`c_s^2 > -1/3`$ and linearly at $`c_s^2 = -1/3`$, both UNSTABLE, and oscillates for $`c_s^2 < -1/3`$, NEUTRALLY STABLE. For the linear law this is Eddington's instability for $`w > -1/3`$.

### H-ANISO, the shape

Take the diagonal Bianchi IX metric $`-dt^2 + \sum_i a_i^2 \sigma_i^2`$, with $`d\sigma_1 = \sigma_2 \wedge \sigma_3`$ and cyclic. Its round case $`a_i = A`$ is the $`S^3`$ of radius $`R = 2A`$. With a perfect fluid at rest and $`\Lambda`$, linearize $`a_i = A(1 + \beta_i)`$. Once the static conditions hold, the traceless combinations obey

```math
\frac{d^2}{dt^2}\left(\beta_i - \beta_j\right) = -\frac{8}{R^2}\left(\beta_i - \beta_j\right),
```

with no dependence on $`\rho`$, $`p`$ or $`c_s^2`$: NEUTRALLY STABLE for every perfect fluid with $`\rho + p > 0`$. The trace, $`\beta_i = \epsilon`$, returns H-ISO's equation. The left-invariant traceless tensors are transverse-traceless on the round $`S^3`$, with rough Laplacian $`-6/R^2`$, and the tensor equation below gives them the same frequency, $`8/R^2`$.

The later full analysis agrees. Barrow and Yamamoto's Bianchi IX linearization, for $`p = (\gamma - 1)\rho`$, has one real pair of eigenvalues, $`\pm\sqrt{3\gamma - 2}`$, which is the volume or FLRW mode and which they identify with the mode found in the 2003 analysis. The anisotropic curvature gives two purely imaginary pairs, $`\pm 2\sqrt2\,i`$. With $`\gamma = 1 + w`$, their squared ratio, $`8/(1 + 3w)`$, is the ratio of this sector's $`8/R^2`$ to H-ISO's $`(1 + 3w)/R^2`$ under the linear law. So the homogeneous Bianchi IX instability that Barrow, Ellis, Maartens and Tsagas report is the growth of their mean scale factor (their eq. 42), the radius mode, while the shape modes oscillate. That section's printed coefficients do not all agree with its own background equations: its eq. (41) gives six times the density perturbation its conservation law (39) gives. No coefficient here is taken from it.

### I-S, density inhomogeneities

In longitudinal gauge, $`-(1 + 2\Phi)\,dt^2 + R^2(1 - 2\Psi)\,\gamma`$ with $`\gamma`$ the unit-sphere metric, a perfect fluid has no anisotropic stress, so $`\Phi = \Psi`$. The 00 equation and the trace of the spatial equations give

```math
\frac{3 - k^2}{R^2}\,\Psi = 4\pi G\,\delta\rho, \qquad \ddot\Psi - \frac{\Psi}{R^2} = 4\pi G\,c_s^2\,\delta\rho, \qquad \text{so} \qquad \ddot\Psi = \frac{1 - c_s^2\left(k^2 - 3\right)}{R^2}\,\Psi .
```

- **The homogeneous mode,** $`n = 0`$, returns H-ISO.
- **The next mode,** $`n = 1`$, has $`\delta\rho = 0`$ by the 00 equation, so it carries no density perturbation.
- **The physical modes,** $`n \ge 2`$, have $`k^2 - 3 \ge 5`$, so every one oscillates exactly when $`c_s^2 > 1/5`$, with $`n = 2`$ binding. At $`c_s^2 = 1/5`$ the $`n = 2`$ mode grows linearly, and for $`c_s^2 < 0`$ every mode with $`n \ge 2`$ grows. Verdict: NEUTRALLY STABLE for $`c_s^2 > 1/5`$, UNSTABLE otherwise.

This is Barrow, Ellis, Maartens and Tsagas's eq. (15), with their condition $`(k^2 - 3)c_s^2 > 1`$ (eq. 16) and $`c_s^2 > 1/5`$ (eq. 17). The derivation here uses no range of $`w`$, only $`\rho + p > 0`$ and the barotropic law. Under the linear law it gives the radiation and dust results they attribute to Harrison: radiation, $`c_s^2 = 1/3`$, neutral; dust, $`c_s^2 = 0`$, unstable.

### I-V/T, vorticity and gravitational waves

- **Vector.** For a perfect fluid on the static background, the linearized Euler equation, $`(\rho + p)\,\partial_t u_i + \partial_i\,\delta p + (\rho + p)\,\partial_i\Phi = 0`$, loses both gradients under the curl. So the vorticity is constant in time (Barrow et al., eq. 21), and the vector metric perturbation follows it through the momentum constraint. Verdict: NEUTRALLY STABLE for every perfect fluid with $`\rho + p > 0`$, whatever its response law.
- **Tensor.** Transverse-traceless perturbations with no anisotropic stress obey $`\ddot h + (k^2 + 2)\,h/R^2 = 0`$ (their eq. 23, with $`4\pi G(1 + w)\rho_0 = 1/R^2`$). Here $`-\nabla^2 h = k^2 h/R^2`$, and the rough Laplacian is non-positive on the compact $`S^3`$, so $`k^2 \ge 0`$ and the squared frequency is at least $`2/R^2`$. Verdict: NEUTRALLY STABLE for every perfect fluid with $`\rho + p > 0`$.

## III. The cells

On branches (a) and (c), where Einstein's equations hold on the static metric. Branch (a) with coefficient 3 is the $`\rho = 0`$ row; branch (c) is every other row.

| Source | $`\Lambda R^2`$ | H-ISO | H-ANISO | I-S | I-V/T |
| --- | --- | --- | --- | --- | --- |
| Barotropic, $`-1/3 < w \le 1`$ | $`(0, 2]`$ | UNSTABLE if $`c_s^2 \ge -1/3`$, which includes the linear law; NEUTRALLY STABLE if $`c_s^2 < -1/3`$ | NEUTRALLY STABLE | NEUTRALLY STABLE if $`c_s^2 > 1/5`$ (linear law: radiation yes, dust no); UNSTABLE otherwise | NEUTRALLY STABLE |
| Barotropic, $`w > 1`$ | $`(2, 3)`$ | the same rule; the linear law is UNSTABLE | NEUTRALLY STABLE | the same rule; the linear law is NEUTRALLY STABLE, for a source that violates the dominant energy condition ($`p > \rho`$) and, under the linear law, is superluminal ($`c_s^2 = w > 1`$) | NEUTRALLY STABLE |
| Perfect fluid, $`\rho = 0`$, $`p > 0`$ (coefficient 3) | $`3`$ | OPEN, SOURCE DYNAMICS MISSING | NEUTRALLY STABLE | OPEN, SOURCE DYNAMICS MISSING | NEUTRALLY STABLE |
| Perfect fluid, $`\rho < 0`$, $`p > -\rho`$ (the record's readings of R) | above $`3`$ | OPEN, SOURCE DYNAMICS MISSING | NEUTRALLY STABLE | OPEN, SOURCE DYNAMICS MISSING | NEUTRALLY STABLE |
| Any row above, with the radius held fixed | | NOT ADMITTED, with the source's homogeneous perturbation removed as well (§IV) | as in its row | as in its row | as in its row |

**The disjointness.** For any barotropic law, H-ISO is quiet only for $`c_s^2 < -1/3`$ and I-S only for $`c_s^2 > 1/5`$. So with both sectors admitted, every barotropic perfect-fluid source on (a) or (c) has an UNSTABLE sector, whatever its $`w`$ and whatever the sign of $`\rho`$, subject to the static condition $`\rho + p > 0`$. Only NOT ADMITTED in H-ISO escapes it.

**The open cells.** No response law for the coefficient-3 source or for the $`\rho < 0`$ sources is on the record.
- A barotropic law would fall under the disjointness. For the $`\rho < 0`$ sources under the linear law, $`w < -1`$ and $`c_s^2 = w`$, so H-ISO is NEUTRALLY STABLE and I-S is UNSTABLE.
- Non-barotropic sources are not covered. One example: with a ghost scalar field, whose energy density is negative, and radiation, Barrow and Tsagas find the static universe free of linear growth. Its radius oscillates, its density perturbations stay constant, its vortical distortions vanish, and its gravitational waves oscillate at constant amplitude.
- Sources whose constituents lie outside the perfect-fluid class still sum to a perfect fluid on the exact static metric, so C2's balance holds for their total, and their perturbation sectors stay OPEN, SOURCE DYNAMICS MISSING.

## IV. Holding the radius fixed

Set $`\epsilon \equiv 0`$ in the homogeneous sector. The first-order Friedmann constraint, $`0 = \tfrac{8\pi G}{3}\,\delta\rho + 2\epsilon/R^2`$, then gives $`\delta\rho = 0`$, and the Raychaudhuri equation gives $`\delta p = 0`$. So on (a) and (c) the radius can be held fixed only with the source's homogeneous perturbation removed too: H-ISO is NOT ADMITTED, for metric and source together, a restriction carried as a cost. A source whose homogeneous sector stays dynamical while the radius is fixed would suspend those two equations, which (a) and (c) assert.

The framework fixes the radius of the static $`S^3`$ ([the engine](../../../README.md): "Its radius is fixed"). Paired with (a) or (c), that costs exactly this removal and no more. If the commitment fixed the round metric as well, the traceless shape modes would be NOT ADMITTED too, and neither reading gives growth.

For a barotropic perfect-fluid source, after the removal the admitted sectors are free of linear growth exactly when $`c_s^2 > 1/5`$, since H-ANISO and I-V/T are neutral. Such a candidate on (a) or (c) owes two things: a frozen homogeneous source sector, stated as a cost, and a response law with $`c_s^2 > 1/5`$. A non-barotropic source carries degrees of freedom the scalar equation does not classify, and its cells stay OPEN.

## V. Branch (b)

By the branch's own definition, the static metric is substrate and solves no Einstein equation with matter. So all four sectors are NOT APPLICABLE to the Einstein-static test, and a substrate dynamics supplied later is analyzed under its own equations. Two things are left elsewhere.
- **The substrate's stability** belongs to whatever substrate dynamics or $`g_\text{static} \to g_\text{eff}`$ construction arrives, and C12 requires such a candidate to state that dynamics. A radius fixed by stipulation, with no substrate dynamics, removes degrees of freedom; it is not a stability result.
- **The effective metric** is an evolving metric rather than a static equilibrium, and its perturbations pass through the missing map. C7, C8 and C10 already require a candidate to declare the fluctuation map it induces. The record touches that sector through the linear-growth check against DESI DR1 ([Temporal Budget](temporal-budget.md) §IX). No verdict is stated there.

## VI. What it settles, and what it does not

- **What it settles.** On (a) and (c):
  - H-ANISO and I-V/T are neutral for every perfect fluid;
  - H-ISO and I-S are governed by the response law, and the disjointness holds;
  - the radius is held fixed only at the stated cost.

  The Λ page's open question is answered branch by branch, as far as the record's sources allow.
- **What it adds.** C12, on [the stress-tensor bridge](stress-tensor-bridge.md#ii-the-constraint-set-already-in-hand).
- **What it does not settle.**
  - the branch, the dictionary, the clock, flatness or the coefficient;
  - the response law of the coefficient-3 source and of the sources the record's readings of R require;
  - anything nonlinear.

## VII. Checks

[`stability_check.py`](scripts/static-domain-stability/stability_check.py) needs sympy, and its record [`stability_check.out`](scripts/static-domain-stability/stability_check.out) reproduces byte for byte from it. It computes each sector from the Einstein tensor of the perturbed metric:
- H-ISO from the Raychaudhuri equation;
- I-S in longitudinal gauge, at $`n = 0, 2, 3, 4`$;
- H-ANISO from the Bianchi IX metric in Euler angles, with its trace and its 00 constraint;
- the trace, divergence and rough Laplacian of the left-invariant traceless tensors;
- what holding the radius fixed forces on the homogeneous source.

Five mutation arms, one per claim, each turn it red.

## References

- A. S. Eddington, "On the Instability of Einstein's Spherical World", [Mon. Not. R. Astron. Soc. 90, 668–678 (1930)](https://doi.org/10.1093/mnras/90.7.668).
- E. R. Harrison, "Normal Modes of Vibrations of the Universe", [Rev. Mod. Phys. 39, 862–882 (1967)](https://doi.org/10.1103/RevModPhys.39.862).
- J. D. Barrow, G. F. R. Ellis, R. Maartens and C. G. Tsagas, "On the stability of the Einstein static universe", [Class. Quantum Grav. 20, L155–L164 (2003)](https://doi.org/10.1088/0264-9381/20/11/102).
- J. D. Barrow and C. G. Tsagas, "On the stability of static ghost cosmologies", [Class. Quantum Grav. 26, 195003 (2009)](https://doi.org/10.1088/0264-9381/26/19/195003).
- J. D. Barrow and K. Yamamoto, "Instabilities of Bianchi type IX Einstein static universes", [Phys. Rev. D 85, 083505 (2012)](https://doi.org/10.1103/PhysRevD.85.083505).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
