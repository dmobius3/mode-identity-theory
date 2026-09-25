<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Cone Point Coherence

**Type:** Program
**State:** Active
**Status (2026-09-16):** The cosmic cone point is derived; the nested-coherence reading is motivated and the galactic-scale Frobenius program is open. SPARC removed L_f as the coherence radius, so the curvature-sourcing question now stands against an unknown L_g.
**Summary:** Asks whether galactic coherence is the W-independence of a nested cone-point eigenvalue problem, and what sources the galactic-scale curvature.
**Inputs:** the first-eigenvalue paper's cone-point analysis (`../../bedrock/files/first-eigenvalue.md`), the 120-grid scale-free projection, the phase-field coherence scale (L_f SPARC-falsified, L_g open)

Working notes on the cone point as the mechanism of galactic coherence.

The cosmic cone point analysis is DERIVED (first-eigenvalue paper). The proposal that cone point identification provides the mechanism of nested coherence is MOTIVATED. The Frobenius program at galactic scale is OPEN. The curvature sourcing question (Section V) is the critical open problem. The pre-registered SPARC test ([sparc-phase-field.md](sparc-phase-field.md), run 2026-05-19) found that $`L_f = v_c^2/a_0`$ does not behave like a single galactic coherence radius: the gravitational transition lands at $`\approx 0.38\,L_f`$ and the flat onset at $`\approx 1.26\,L_f`$, and the transition radius tracks baryonic mass more tightly than $`L_f`$. This removes the empirical anchor for Reading B (the nested galactic cone point at $`L_f`$); Reading A (the cosmic cone point) and the Frobenius chain (Section VII) are untouched.

**Related:** [First Eigenvalue](../../bedrock/files/first-eigenvalue.md), [Black Double Zero's](../../../../cosmos/files/black-hole.md), [Oort Cloud project](oort-cloud-project.md), [SPARC phase field notes](sparc-phase-field.md).

---

## I. The Question

Within a galaxy, all observers measure the same $`\mathbb{R}^4`$: same $`\Lambda`$, same $`G`$, same particle masses, same coupling constants. The phase field mechanics proposed a coherence scale $`L_f = v_c^2/a_0 \approx 13`$ kpc within which the environmental phase shift $`\Theta_f`$ would be uniform. The SPARC test falsified $`L_f`$ as a single coherence radius: the gravitational transition lands at $`0.38\,L_f`$ and tracks baryonic mass ($`\rho \approx 0.68`$) more tightly than $`L_f`$ ($`\rho \approx 0.61`$). The geometric question survives: if galactic coherence has a topological origin, what sets the scale? But the target radius is no longer $`L_f`$.

On the cosmic Möbius band, the cone point at $`y = \pi R/2`$ collapses all transverse positions to a single geometric point. In the zonal sector, the first positive eigenvalue $`\lambda_1 = 2/R^2`$ is $`W`$-independent: it does not depend on the transverse width of the band. The [first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md) shows this $`W`$-independence holds for the full operator only when $`W \leq \pi R/2`$ (cone angle $`\leq \pi`$); for wider bands an azimuthal mode undercuts the zonal level. At cosmic scale the physical band sits well within the narrow regime, so the coherence argument is unaffected.

**The proposal:** galactic coherence is the $`W`$-independence of a nested eigenvalue problem, guaranteed by a cone point at galactic scale. Observers within the galaxy share the cone point of the wave, and the cone point identification is why they all measure equal $`\mathbb{R}^4`$ values.

If this is right, it must be handled with the same care as the first-eigenvalue paper: Frobenius expansion, limit-circle classification, bridging extension (not Friedrichs; see §II), excision with vanishing boundary terms. No hand-waving about transverse collapse.

---

## II. The Template

The cosmic cone point analysis establishes the following chain. Steps 1-7 are the [first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md)'s endpoint data (§§3.3-3.5 there). Steps 8-9 are this note's variational template for reaching step 10 without closed forms: the paper itself reaches the $`W`$-independent zonal level by Legendre reduction and min-max, and its one cutoff estimate (Lemma 4.1 there, $`O(1/\lvert\log\epsilon\rvert)`$) serves the opposite purpose, placing the discontinuous zero mode inside the Friedrichs domain. The excision route matters here because the galactic generalization (§VII) has no closed forms.

| Step | What it does | How |
|------|-------------|-----|
| 1 | Metric degenerates | $`\cos(y/R) \to 0`$ at $`y = \pi R/2`$ |
| 2 | Transverse interval collapses | $`[-W, W]`$ becomes a single point; cone angle $`2W/R`$ |
| 3 | Frobenius expansion | Indicial equation $`s^2 = 0`$ (double root); two local solutions |
| 4 | Regular branch | $`u_1 = a_0 + a_2\delta^2 + O(\delta^4)`$, with $`u_1' = O(\delta)`$ |
| 5 | Logarithmic branch | $`u_2 = \log\|\delta\| + \ldots`$, with $`u_2' = 1/\delta`$ |
| 6 | Limit-circle | Both branches $`L^2`$ w.r.t. weight $`\|\delta\|/R`$ |
| 7 | Bridging extension | The sector-regular bridging family $`A^{\mathrm{br}}_{\delta_0}`$ (first-eigenvalue paper, Definition 3.5) imposes continuity of the regularized value and Kirchhoff flux matching across the cone. The covering geometry (smooth pole on $`S^2`$) constrains but does not fix the extension; the operative criterion is the limit-circle classification (Remark 3.2 there). The Friedrichs extension admits a discontinuous zero mode at $`n=0`$; bridging excludes it, at the price of one cone-localized negative defect eigenvalue $`\lambda_b(\delta_0)`$. For $`n \geq 1`$ the endpoint is limit-point in the narrow band and no extension choice arises; past the critical width the first odd sector turns limit-circle, and taking its regular branch is the sector-regularity assumption. |
| 8 | Excision | $`\partial_\nu\|\nabla u\|^2 = O(\epsilon)`$, arc-length $`= O(\epsilon)`$, product $`= O(\epsilon^2) \to 0`$ |
| 9 | Rayleigh quotient | $`2W`$ appears in numerator and denominator; cancels exactly |
| 10 | $`W`$-independence | zonal first positive level $`\lambda_1 = 2/R^2`$ regardless of transverse width |

Steps 1-8 handle the singularity. Step 9 establishes the eigenvalue. Step 10 delivers coherence.

The key structural feature: the $`W`$-cancellation (step 9) works because the area element $`dA = |\cos(y/R)|\,dy\,dw`$ factors the $`w`$-integration out of both numerator and denominator. The cone point analysis (steps 1-8) is needed to make this factored integral well-defined at the singular endpoint. The extension choice moves the bottom, not the zonal level: the Friedrichs extension has bottom $`0`$, attained by the discontinuous zero mode, the bridging family replaces it with a cone-localized negative defect state, and no self-adjoint extension has a strictly positive bottom (Theorem 1.1 there). The coherence eigenvalue is therefore the first positive level, measured from zero, not a ground state. The $`W`$-cancellation delivers the zonal $`2/R^2`$ for all $`W`$, but it is the first positive level only when $`W \leq \pi R/2`$; for wider bands an azimuthal ($`n=1`$) mode with eigenvalue $`\alpha_0(\alpha_0+1)/R^2 < 2/R^2`$ ($`\alpha_0 = \pi R/2W`$) undercuts it, and the level turns width-dependent.

**Coherence is a global property ($`W`$-independence), but its proof passes through the local analysis at the cone point.**

---

## III. Two Readings

### Reading A: Shared Cosmic Cone Point

The cosmic Möbius band has one cone point at $`y = \pi R/2`$. Every meridional line (every $`w`$-position) passes through it. In the zonal sector (the $`w`$-constant first-positive mode), the eigenfunction $`u_0 = \sin(y/R)`$ takes the same value at each $`y`$ regardless of $`w`$. The cone point ($`u_0 = 1`$) is the shared maximum of all meridional lines.

Galactic observers are at different $`w`$-positions on the cosmic Möbius band but share this cone point. The first positive eigenvalue $`\lambda_1 = 2/R^2`$ is established through integration that passes through the cone point. All observers inherit the same eigenvalue because they sample the same first-positive mode on the same band.

In this reading, galactic coherence is a consequence of:
- One Möbius band (the cosmic one)
- One first-positive mode (the zonal mode)
- One cone point (at $`y = \pi R/2`$)
- $`W`$-independence (the transverse width of the galaxy doesn't matter)

The galactic gravitational field enters through the $`\Phi \to \Theta`$ mapping, which shifts the observer's phase position by $`\Theta_f \approx 2/120`$. This is a perturbation of the phase coordinate, not the transverse coordinate. The cone point structure is unaffected because the perturbation is in $`y`$ (meridional), not in $`w`$ (transverse).

**What needs to be checked:** does the $`\Theta_f`$ perturbation spoil the cone point analysis? Specifically: does the perturbed eigenfunction still belong to the bridging domain (regular branch, finite Dirichlet integral, regularized-value continuity across the apex) at the cone point? The input is the galactic potential, $`\Phi/c^2 \sim 10^{-6}`$; the environmental grid rule floors the response at the minimum bosonic step, so the displacement actually applied to the phase coordinate is $`\Theta_f \approx 2/120`$. That is small in absolute terms, and the check is owed there rather than at the potential that feeds it. But "small" is not "zero," and the cone point is a singular endpoint where small perturbations could change the qualitative character.

### Reading B: Nested Galactic Cone Point

If the 120-grid is scale-free and the Möbius structure projects at every gravitationally coherent scale, then at galactic scale there is a nested Möbius band with its own metric, its own cone point, and its own eigenvalue.

| Cosmic | Galactic (proposed) |
|--------|---------------------|
| $`ds^2 = dy^2 + \cos^2(y/R)\,dw^2`$ | $`ds^2 = dy_g^2 + f_g^2(y_g)\,dw_g^2`$ |
| Curvature $`K = 1/R^2`$ (constant) | $`K_g = ?`$ |
| Cone point at $`y = \pi R/2`$ | Cone point where $`f_g = 0`$ |
| $`\lambda_1 = 2/R^2`$ | $`\lambda_g = ?`$ |
| Coherence: all of $`S^3`$ | Coherence: $`L_g`$ (original candidate $`L_f = v_c^2/a_0 \approx 13`$ kpc, falsified by SPARC) |

In this reading, galactic coherence is the $`W_g`$-independence of the nested eigenvalue. The galactic cone point plays the same structural role at galactic scale that the cosmic cone point plays at cosmic scale.

**What needs to be derived:** the galactic metric coefficient $`f_g`$, its zeros, the Frobenius expansion at those zeros, and the full chain (steps 1-10) at galactic scale.

### Which reading?

Both may be correct at different levels. Reading A says all observers share the cosmic cone point (one band, one mode). Reading B says the structure nests (one band per scale, each with its own cone point). The Oort Cloud project's nested coherence picture (Piece B) leans toward Reading B. The question is whether Reading B requires new derivations at each scale, or whether it follows from Reading A plus the scale-free 120-grid.

---

## IV. The Budget Identity at Galactic Scale

At cosmic scale: $`u_0^2 + J^2 = 1`$, where $`u_0 = \sin(y/R)`$ and $`J = \cos(y/R)`$.

At the cone point ($`y = \pi R/2`$): $`u_0 = 1`$, $`J = 0`$. Full budget in sampling, none in transverse geometry.
At the gluing seam ($`y = 0 \equiv \pi R`$): $`u_0 = 0`$, $`J = \pm 1`$. Full budget in geometry, none in sampling.

The budget identity holds because both $`u_0`$ and $`J`$ satisfy second-order ODEs sourced by the same constant curvature $`K = 1/R^2`$, and both are trigonometric functions of $`y/R`$.

For Reading A: the budget identity holds as written. The galactic perturbation shifts the observer's $`y`$-position by $`\Theta_f`$, changing the $`u_0/J`$ balance slightly, but the identity itself is unperturbed.

For Reading B: the budget identity at galactic scale requires $`u_g^2 + J_g^2 = \text{const}`$. This holds if $`K_g`$ is constant (same trigonometric solutions). If $`K_g`$ varies, the identity takes a different form, or may not hold as a simple sum-of-squares.

| Budget | Cone point | Gluing seam | Interpretation |
|--------|-----------|----------------|----------------|
| $`u_0 = 1,\; J = 0`$ | All sampling, no extent | | Coherence maximum: transverse positions identified |
| $`u_0 = 0,\; J = \pm 1`$ | | All extent, no sampling | Coherence minimum: transverse positions maximally distinct |
| $`u_0^2 + J^2 = 1`$ | | | Fixed total: what the surface spends on extent, it loses in sampling |

At the galactic cone point (if it exists): all spatial positions within the galaxy are metrically identified. The galactic eigenfunction is at maximum. The transverse geometry has collapsed. This is the geometric content of the statement "observers within the galaxy measure equal $`\mathbb{R}^4`$ values."

---

## V. The Curvature Sourcing Problem

This is the critical open question. What sets the curvature of the galactic-scale band?

### GR tidal curvature alone does not produce a galactic cone point

The coherence domain is centered on Sagittarius A* (Sgr A*), the supermassive black hole at the galactic center ($`M \approx 4 \times 10^6\,M_\odot`$). The gravitational field has two regimes:

**Keplerian regime** ($`r \lesssim 0.7`$ pc): Sgr A* dominates. Tidal curvature $`K = 2GM/(r^3 c^2)`$ is strong and falls as $`1/r^3`$. Extrapolating the point-mass Keplerian curvature gives a match near $`r \sim 1.9`$ pc, already outside the Sgr A*-dominated regime. The Jacobi equation is oscillatory; tidal focusing can produce zeros.

**Flat-curve regime** ($`r \gtrsim 0.7`$ pc, spanning 99.99% of $`L_f`$): The tidal curvature is $`K(r) = v_c^2/(r^2 c^2)`$. The Jacobi equation becomes Euler-type:

```math
J'' + \frac{v_c^2}{r^2 c^2}\,J = 0
```

with solutions $`J \sim r^p`$ where $`p(p-1) + v_c^2/c^2 = 0`$. Since $`v_c^2/c^2 \approx 5 \times 10^{-7}`$, the exponents are $`p \approx 0`$ and $`p \approx 1`$. These are power laws, not oscillatory. **A power-law Jacobi field has no zero for $`r > 0`$.** This is not a matter of the curvature being too weak at some particular radius; the Euler-type equation is structurally non-oscillatory regardless of where it is evaluated.

### The curvature needed

If $`\pi R_g = L_g`$, then $`R_g = L_g/\pi`$ and $`K_g = \pi^2/L_g^2`$. Under the original identification $`L_g = L_f = v_c^2/a_0`$ (now falsified by SPARC):

```math
K_g = \frac{\pi^2}{L_f^2} = \frac{\pi^2\,a_0^2}{v_c^4} \approx 6.1 \times 10^{-41}\;\text{m}^{-2}
```

This is $`10^7`$ times larger than $`K_{\text{GR}}`$. It is NOT sourced by the gravitational tidal field alone.

### Where the curvature comes from

The candidate scale $`L_f = v_c^2/a_0`$ sits at the interface between gravity ($`v_c`$) and topology ($`a_0`$, derived from $`C(13/120)`$). The curvature $`K_g = \pi^2 a_0^2/v_c^4`$ lives at this interface. It is neither purely gravitational nor purely topological.

| Scale | Curvature | Source | Character |
|-------|-----------|--------|-----------|
| Cosmic | $`K = 1/R_\Lambda^2 = \Lambda_\text{ref}/3 \approx 4 \times 10^{-53}\;\text{m}^{-2}`$ | Totally geodesic $`S^2 \subset S^3`$ | Constant; oscillatory Jacobi field |
| Galactic (needed) | $`K_g \approx 6 \times 10^{-41}\;\text{m}^{-2}`$ | Topology-gravity interface ($`a_0`$, $`v_c`$) | Must be constant or oscillatory |
| Sgr A* core ($`r < 0.7`$ pc) | $`K \sim 4 \times 10^{-40}\;\text{m}^{-2}`$ at 1 pc | Keplerian tidal ($`2GM/r^3c^2`$) | Oscillatory (tidal focusing) |
| Flat-curve ($`r > 0.7`$ pc) | $`K = v_c^2/(r^2c^2) \sim 10^{-47}`$ at 8 kpc | Galactic mass distribution | **Euler-type; power-law Jacobi field; no zeros** |

The problem is not the magnitude; it is the character. The flat rotation curve produces an Euler-type Jacobi equation whose solutions are power laws. Power laws do not oscillate and do not cross zero. The Sgr A* Keplerian core does produce oscillatory behavior, but it spans only $`\sim 0.005\%`$ of $`L_f`$. The vast bulk of the coherence domain lives in the structurally non-oscillatory regime.

This is parallel to the MOND regime: $`a_0`$ marks where Newtonian gravity alone fails to account for the dynamics. Here, GR tidal curvature fails not just quantitatively but qualitatively: the Jacobi equation has the wrong character (power-law instead of oscillatory) to produce a cone point within $`L_f`$. The topology must supply the missing structure.

The [SPARC phase field notes](sparc-phase-field.md) tested $`L_f`$ empirically across the quality-filtered SPARC sample, asking whether $`L_f`$ predicts the gravitational transition radius. The SPARC correlations did not hold; the transition tracks $`M_b`$, not $`L_f`$. The curvature sourcing question remains open but its target has shifted from $`L_f`$ to whatever $`L_g`$ turns out to be.

**Assessment:** The galactic cone point (Reading B) cannot be sourced by GR curvature. It requires the topological scale $`a_0`$. If the 120-grid projects at every scale with constant curvature inherited from the Möbius structure (not from the gravitational field), then $`K_g = \pi^2/L_g^2`$ is set by the topology-gravity interface, and the cone point exists. If the curvature must be sourced purely by GR, the cone point does not exist within the galaxy, and galactic coherence must work by a different mechanism (Reading A or something else).

This is the fork. The Frobenius program (Section VII) sits on the far side of it.

---

## VI. Relation to the SPARC Result

The SPARC test ([sparc-phase-field.md](sparc-phase-field.md)) falsified $`L_f = v_c^2/a_0`$ as the galactic coherence radius. Two findings bear directly on this note.

The transition radius lands at $`r_t \approx 0.38\,L_f`$ and correlates more tightly with baryonic mass than with $`L_f`$, stable across the $`\Upsilon_\text{disk}`$ sweep. This is a directional mismatch with §V's curvature sourcing argument, which derives $`K_g`$ from $`a_0`$ and $`v_c`$. The data points toward mass distribution instead.

The mean-square velocity suppression ($`\langle v^2 \rangle_{L_f} / v_c^2 \approx 0.41`$) falls below the trigger threshold ($`\xi \approx 0.46`$). Real rotation curves are not flat over $`[0, L_f]`$, so the closure identity that guaranteed universal triggering does not hold. The numerical proximity is indicative only: the two quantities are evaluated on different radial geometries, and the mismatch biases the comparison toward the failure it illustrates. The registered SPARC verdicts do not depend on it.

Reading B (nested galactic cone point at $`L_f`$) loses its empirical anchor. Reading A (shared cosmic cone point) and the Frobenius chain (§VII) are untouched. The fork in §V sharpens: GR tidal curvature was already shown to fail; $`L_f`$ itself now fails empirically. If a galactic cone point exists, its radius must come from somewhere other than $`v_c^2/a_0`$, and whatever sets it must account for the observed $`M_b`$ dependence.

---

## VII. The Frobenius Program

If the galactic cone point exists ($`f_g`$ vanishes at some $`y_g^*`$), the following must be executed with full rigor:

### Step 1: Identify the galactic metric coefficient $`f_g(y_g)`$

Three scenarios, ordered by assumption strength:

**Scenario A (constant curvature).** If $`K_g = 1/R_g^2`$ is constant, then $`f_g = \cos(y_g/R_g)`$. The entire first-eigenvalue analysis carries over with $`R \to R_g`$. The Frobenius expansion, limit-circle classification, bridging extension (in the constant sector; the higher sectors are limit-point in the narrow band and carry no choice), and excision are identical. The eigenvalue is $`\lambda_g = 2/R_g^2 = 2\pi^2/L_g^2`$ (the original identification $`L_g = L_f`$ is no longer empirically supported). The budget identity $`u_g^2 + J_g^2 = 1`$ holds. This is the cleanest case but the strongest assumption. The width constraint applies: the zonal level is the first positive eigenvalue only when $`W_g \leq \pi R_g/2`$.

**Scenario B (variable curvature, linear zero).** If $`K_g`$ varies but $`f_g`$ still has a simple (linear) zero at $`y_g^*`$, then near the zero: $`f_g \sim |\delta_g|/R_{\text{eff}}`$ for some effective radius $`R_{\text{eff}}`$. The indicial equation is still $`s^2 = 0`$ (double root from the linear zero of the weight). Limit-circle classification still holds. The bridging extension fixes the constant sector; for $`n \geq 1`$ the endpoint is limit-point in the narrow band, so no extension choice arises. The excision terms still vanish as $`O(\epsilon^2)`$. The eigenvalue changes (no longer $`2/R_g^2`$) but the $`W_g`$-independence mechanism is preserved if the metric factors as $`ds^2 = dy_g^2 + f_g^2(y_g)\,dw_g^2`$, subject to the width constraint $`W_g \leq \pi R_{\text{eff}}/2`$.

**Scenario C (no zero, or non-linear zero).** If $`f_g`$ does not vanish, there is no cone point, and the coherence mechanism of Reading B fails. If $`f_g`$ vanishes quadratically or with higher order, the indicial exponents change and the analysis must be reworked from scratch.

### Step 2: Frobenius expansion

For Scenarios A and B, near $`\delta_g = y_g - y_g^*`$:

```math
(|\delta_g|/R_{\text{eff}} \cdot u')' + \lambda\,|\delta_g|/R_{\text{eff}} \cdot u = 0
```

Frobenius substitution $`u = |\delta_g|^s \sum a_k \delta_g^k`$. Leading balance gives $`s^2 = 0`$.

- Regular: $`u_1 = a_0 + a_2\delta_g^2 + O(\delta_g^4)`$, with $`a_2 = -\lambda a_0/4`$
- Logarithmic: $`u_2 = \log|\delta_g| + b_2\delta_g^2 + O(\delta_g^4)`$

Check: are higher-order terms in the Frobenius expansion modified by $`K_g`$ being non-constant? If $`K_g`$ varies, the $`a_2`$ coefficient acquires corrections from the curvature gradient $`K_g'`$. The leading-order structure ($`s^2 = 0`$, two branches) is unchanged because the Frobenius expansion is local and the weight vanishes linearly regardless of the curvature profile.

### Step 3: Limit-circle classification

Both branches are $`L^2`$ w.r.t. weight $`|\delta_g|/R_{\text{eff}}\,d\delta_g`$ because:
- $`u_1^2 \cdot |\delta_g| \sim |\delta_g|`$ (integrable)
- $`u_2^2 \cdot |\delta_g| \sim (\log|\delta_g|)^2 \cdot |\delta_g|`$ (integrable)

This classification depends only on the LINEAR vanishing of the weight, not on the global curvature profile. For any metric of the form $`ds^2 = dy^2 + f^2(y)\,dw^2`$ where $`f`$ has a simple zero, the cone point is limit-circle.

### Step 4: Self-adjoint extension

The Dirichlet integral distinguishes the branches:
- Regular: $`(u_1')^2 |\delta_g| \sim \delta_g^2 \cdot |\delta_g| = O(|\delta_g|^3)`$. Integrable.
- Logarithmic: $`(u_2')^2 |\delta_g| \sim \delta_g^{-2} \cdot |\delta_g| = O(|\delta_g|^{-1})`$. Divergent.

In the constant sector ($`n = 0`$) the Friedrichs extension takes the regular branch outright, while the bridging matching (regularized-value continuity plus Kirchhoff flux) forces the regular branch in the symmetric subsector, where the coherence mode lives, and deforms the antisymmetric branch onto the logarithmic solution (the defect bound state). Either way the symmetric zonal mode is regular at the apex. For $`n \geq 1`$ the endpoint is limit-point and self-adjointness is unique, with one caveat from the first-eigenvalue paper (Lemma 3.3 there): past the critical width ($`W > \pi R_{\text{eff}}/2`$, indicial exponent below 1) the first odd sector turns limit-circle too, and taking its regular branch is the sector-regularity assumption rather than forced. In the narrow band the statement holds for any simple zero of $`f`$, regardless of the curvature profile.

### Step 5: Excision estimates

For the regular-branch eigenfunctions (the symmetric zonal tower and every nonconstant sector, which is where the coherence mode lives; the logarithmic defect state is excluded and does not satisfy these estimates):
- $`u = O(1)`$, $`u' = O(\delta_g)`$, $`u'' = O(1)`$
- $`\partial_\nu|\nabla u|^2 = 2u'u'' = O(\epsilon)`$
- Arc-length of excision curve: $`|f_g| \cdot 2W_g \sim (\epsilon/R_{\text{eff}}) \cdot 2W_g = O(\epsilon)`$
- Product: $`O(\epsilon) \cdot O(\epsilon) = O(\epsilon^2) \to 0`$

This estimate depends only on the regular-branch Frobenius asymptotics and the linear vanishing of $`f_g`$. It holds for Scenarios A and B.

### Step 6: $`W_g`$-independence

The Rayleigh quotient for $`w_g`$-constant functions:

```math
\frac{\int_0^{\pi R_g}(u')^2\,|f_g|\,dy_g \cdot 2W_g}{\int_0^{\pi R_g} u^2\,|f_g|\,dy_g \cdot 2W_g}
```

$`2W_g`$ cancels if and only if the metric coefficient $`f_g`$ depends on $`y_g`$ alone (no $`w_g`$-dependence in $`f_g`$). For any metric of the factored form $`ds^2 = dy_g^2 + f_g^2(y_g)\,dw_g^2`$, the cancellation holds. This is guaranteed by the $`S^2`$-type embedding structure, which forces the metric to factor.

### Step 7: Budget identity

For constant curvature (Scenario A): $`u_g^2 + J_g^2 = 1`$ holds by the Pythagorean identity.

For variable curvature (Scenario B): the eigenfunction $`u_g`$ and Jacobi field $`J_g`$ satisfy different ODEs ($`u_g`$ has the eigenvalue $`\lambda_g`$; $`J_g`$ solves $`J'' + K_g J = 0`$). The sum $`u_g^2 + J_g^2`$ is not generally constant. A Wronskian-type conservation law may replace it, but this must be derived.

---

## VIII. What This Means for the Oort Cloud Project

### If Reading B holds (nested cone point exists):

The coherence boundary at each scale is $`2W`$ (the transverse width of that scale's Möbius band). The cone point identification guarantees $`W`$-independence of the eigenvalue, which guarantees coherence within the domain. The first-eigenvalue paper adds a constraint: the $`W`$-independence holds only when $`W \leq \pi R/2`$ (cone angle $`\leq \pi`$). For nested bands, this means $`W_g \leq \pi R_g/2`$ is required; otherwise the first positive level is azimuthal and $`W_g`$-dependent.

| Scale | $`2W`$ | Coherence domain |
|-------|------|------------------|
| Cosmic | $`2\pi R`$ (full $`\mathbb{RP}^2`$; no boundary, no deficit) | All of $`S^3`$ |
| Galactic | $`2W_g`$ | $`L_g`$ (unknown) |
| Stellar | $`2W_\odot`$ | Oort Cloud $`\approx 144{,}000`$ AU? |

At each boundary: the dominant mode's transverse identification no longer covers the observer. The observer transitions from one mode's cone point to the next. The wave is continuous through the transition (Omega Constraint), but the witness stand changes.

This reframes Gap 1 of the Oort Cloud project: instead of asking "does $`L_f = v_c^2/a_0`$ generalize?" the question becomes "what sets $`W`$ at each scale?" The mechanism is the same ($`W`$-independence from cone point analysis); only the width parameter changes.

### If Reading A holds (one cone point, perturbative):

Galactic coherence follows from all observers sampling the cosmic first-positive mode (the zonal mode), with the galactic potential introducing a small perturbation in the meridional direction. The Oort Cloud project's nested structure would need a different geometric explanation than cone point nesting.

### The Oort Cloud radius

If Reading B holds and the stellar-scale Möbius band has meridional length $`\pi R_\odot`$, the Oort Cloud radius is $`L_\odot/2 = \pi R_\odot/2`$ (half the meridional length, the stellar cone point location measured from the edge). Alternatively, $`2W_\odot`$ (the transverse width) sets the domain, and the boundary is at $`w_\odot = \pm W_\odot`$ where the dominant stellar mode's potential gives way to the galactic one.

To derive the Oort Cloud radius, one would need: the stellar analog of $`L_g`$, or equivalently, $`R_\odot`$ from the stellar potential. What plays the role of $`v_c`$ and $`a_0`$ at stellar scale?

---

## IX. Open Questions

| # | Question | Depends on | Priority |
|---|----------|-----------|----------|
| 1 | What sources $`K_g`$? GR tidal curvature in the flat-curve regime is Euler-type with power-law Jacobi solutions (no zeros at any radius); the Keplerian core near Sgr A* is oscillatory but spans $`< 0.01\%`$ of $`L_f`$. The topology-gravity interface ($`a_0`$, $`v_c`$) gives oscillatory solutions with a zero at $`L_f/2`$. What justifies constant curvature across the coherence domain? Note the empirical headwind: SPARC places the transition at $`\approx 0.38\,L_f`$ tracking $`M_b`$, not at $`L_f/2`$, so the $`L_f/2`$ zero is not observationally supported. | Curvature sourcing (§V) | CRITICAL |
| 2 | Does the 120-grid force constant curvature at every scale? If yes, the cone point exists by algebraic structure, not by gravitational focusing. | Scale-free projection (Oort §Joint 2) | HIGH |
| 3 | Reading A or B? One cone point or many? | Questions 1 and 2 | HIGH |
| 4 | Variable-curvature budget identity: what replaces $`u^2 + J^2 = 1`$ when $`K`$ is not constant? | Frobenius program, Step 7 | MEDIUM |
| 5 | What sets $`W_g`$? The meridional length is $`L_g`$ (originally identified with $`L_f = v_c^2/a_0`$, now falsified). What sets the transverse width? | Reading B | MEDIUM |
| 6 | Perturbative stability of the cosmic cone point: does the $`\Theta_f \approx 2/120`$ phase displacement spoil any step in the chain? | Reading A | Unsettled. The earlier LOW was assessed against the $`\Phi/c^2 \sim 10^{-6}`$ potential rather than the displacement the grid rule produces from it, and has not been re-derived |
| 7 | Width regime constraint: nested galactic bands (Reading B) require $`W_g \leq \pi R_g/2`$ for the zonal mode to be the first positive level. If $`W_g > \pi R_g/2`$, the first positive level is azimuthal and $`W_g`$-dependent, breaking the coherence mechanism. What constrains $`W_g`$ at galactic scale? | Width transition (first-eigenvalue paper), Reading B | HIGH |

---

## X. Falsification

| Prediction | Falsified if... |
|------------|-----------------|
| Nested cone point exists (Reading B) | Galactic-scale Jacobi field proved to have no zero from any curvature source |
| $`L_f`$ is the galactic coherence radius | Empirical support removed: SPARC finds the transition at $`\approx 0.38\,L_f`$, the flat onset at $`\approx 1.26\,L_f`$, and $`r_t`$ tracking $`M_b`$ over $`L_f`$, stable across all 27 sensitivity cells |
| Frobenius structure preserved | Indicial exponents differ from $`s^2 = 0`$ at galactic scale (requires non-linear vanishing of $`f_g`$) |
| $`W_g`$-independence | Galactic eigenvalue shown to depend on galaxy size (different-sized galaxies measure different $`\Lambda`$) |
| Width regime | Nested galactic band shown to have $`W_g > \pi R_g/2`$, placing the first positive level in the azimuthal branch where $`W`$-independence fails |
| Curvature from topology-gravity interface | $`K_g`$ shown to require fine-tuning rather than following from $`a_0`$ and $`v_c`$ |
| Omega Constraint | Cone point identification produces observer isolation at any scale; FATAL |

---

## XI. Priorities

The curvature sourcing question (§V) is the fork. Everything else sits on one side or the other.

**Before the fork:** determine whether the 120-grid projects constant curvature at every scale (Question 2). This is an algebraic question about the Möbius structure, not a dynamical calculation. If the answer is yes, the cone point exists at every scale and the full Frobenius program (§VII) runs with known tools. If the answer is no, the curvature must be sourced by the gravitational field (which fails by a factor of $`10^7`$) or by the topology-gravity interface (which needs its own derivation).

**After the fork:** run the Frobenius program at galactic scale (§VII), establish or exclude $`W_g`$-independence, and connect to the Oort Cloud project's nested coherence picture.

The fork question is coupled to Gap 1 of the Oort Cloud project (nested $`L_g`$ derivation) and to the discrete snap mechanism (working file). All three ask the same thing at different levels: how does the topological structure interface with the gravitational field at sub-cosmic scales?

---

*The cone point collapses the transverse direction. The eigenvalue survives the collapse. The observers share the survival.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
