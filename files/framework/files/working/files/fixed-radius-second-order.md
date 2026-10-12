<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Fixed Radius at Second Order

**Type:** Result
**State:** Open
**Status (2026-10-11):** Registered and frozen 2026-10-11; not yet run. On the stress-tensor bridge's branches (a) and (c), with Einstein's equations on the static metric and a barotropic perfect fluid, can the averaged second-order equations hold with the radius fixed? Under the four readings ruled on 2026-10-11, three sectors are decided before the run. No homogeneous shape mode continues to second order with the volume radius fixed at every instant and the fluid's charge held, for any barotropic response law. Given reductions of the averaged equations that the instrument checks, no tensor mode and no vorticity mode does either. So the overall grade is NOT ABSORBED. It does not rest on the charge reading: with the charge left free, the standing modes still fail. The registered computation will map the density sector at every admitted level, with the eigenvalue kept symbolic, report the remaining integrability conditions as values, and confirm the tensor and vorticity sectors' reductions; a record written after the run will compare its results with Losic and Unruh's integrability result.
**Summary:** Whether the fixed-radius ruling, which holds "at every order", survives second order on the stress-tensor bridge's static branches, sector by sector.
**Inputs:** `postulate-bridge.md` (the fixed radius, ruled 2026-10-10), `static-domain-stability.md`, `stress-tensor-bridge.md` (C12, §IX), `first-positive-transfer.md` (the precedent for a grade decided before its run)
**Parent:** `stress-tensor-bridge.md`

---

REGISTRATION, frozen 2026-10-11 before the computation. The fixed-radius ruling says it holds at every order, and that its second-order consistency is not computed ([the postulate bridge](postulate-bridge.md#dynamical-direction)). This page registers that check. It records the four readings ruled for it on 2026-10-11, and the three sectors decided before the run.
- **What it tests:** the pairing of the fixed radius with branches (a) and (c) of [the stress-tensor bridge](stress-tensor-bridge.md), for a barotropic perfect-fluid source.
- **What it does not test:** branch (b), every source theory a candidate might bring to (a) or (c), or MIT as a whole.

**Related:** [The Postulate Bridge](postulate-bridge.md), [The Static Domain's Stability](static-domain-stability.md), [The Stress-Tensor Bridge](stress-tensor-bridge.md).

---

## 0. The question, and the rulings

The ruling leaves this open:
> The ruling holds at every order; what has been checked is its consistency with the asserted static balance, at linear order. A finite-amplitude perturbation's second-order shift of the averaged density, with no radius response to absorb it, is not computed.

**The question.** On branches (a) and (c), with Einstein's equations on the static metric and the radius held fixed: can the averaged second-order field equations be satisfied, using only the homogeneous second-order variables the ruling induces? It is asked for every admissible first-order perturbation. It asks whether the second-order averaged source can be reconciled with a fixed radius, not whether a candidate can be adjusted until it is.

**The rulings (2026-10-11).** These are readings of the fixed-radius ruling at second order. They were ruled before any computation of the open sectors, with the decided sectors' consequences written beside them.
- **T4, the radius.** The volume radius, $`R_V = \big(\lvert G\rvert\,V/(2\pi^2)\big)^{1/3}`$, with $`\lvert G\rvert`$ = 1, 2 or 120 on $`S^3`$, $`\mathbb{RP}^3`$ or $`S^3/2I`$, and $`V`$ the volume of the slice of §2. Shape and curvature may change while $`R_V`$ stays fixed.
- **T6, every instant.** $`R_V`$ is fixed at every instant.
  - A time average is reported as a diagnostic only, never as a passing grade.
  - Where the vorticity is constant, or a configuration has no common period, the time average is marked inapplicable.
- **T7(a), what is free.** The radius is fixed, Einstein's equations are unmodified, and no constraint force enters. The homogeneous second-order source is the one the field equations and conservation laws induce: solved, not chosen. The homogeneous lapse is gauge.
- **T7(b), the conserved charge (C1).** This is a declared fixed-charge restriction, a choice the fixed-radius ruling does not itself force.
  - **The charge:** every barotropic perfect fluid carries the conserved current $`\mathcal{N}^a = n(\rho)\,u^a`$, with $`dn/n = d\rho/(\rho + p)`$. It is unique up to a constant factor, and for radiation it is the entropy current.
  - **What C1 holds fixed:** the total charge $`\mathcal{N} = \int_\Sigma n\,\Gamma\,dV`$, with $`\Gamma = -u^a\nu_a`$ and $`\nu^a`$ the slice's unit normal, at its background value.
  - **The average it fixes:** on fluid-orthogonal slices $`\Gamma = 1`$ and $`\mathcal{N}/V = \langle n\rangle`$. On tilted slices $`\mathcal{N}/V = \langle n\Gamma\rangle`$.

## 1. The arena, the source and the perturbations

**The arena (T1).**
- **The background:** the static closed universe of radius $`R`$, with $`\Lambda`$ and a perfect fluid with $`\rho + p > 0`$, on (a) and (c), where $`1/R^2 = 4\pi G(\rho + p)`$ and $`\Lambda = 4\pi G(\rho + 3p)`$ ([the stability page](static-domain-stability.md) §I).
- **The modes:** harmonics of the round $`S^3`$, stated mode by mode. A quotient's result is the restriction to its invariant modes. The density sector is computed with the eigenvalue $`\lambda = n(n+2)`$ kept symbolic, so each of its readings covers every level at once (§5).
- **The quotients:** on $`\mathbb{RP}^3`$ only even $`n`$ occur, and on $`S^3/2I`$ the first scalar mode after $`n = 0`$ is $`n = 12`$. There the invariant harmonics at level $`n`$ number $`m_n(n+1)`$, with $`m_n`$ the Molien coefficient: 13 at $`n = 12`$, so pairs exist from the first level on.

**The source (T2).** A barotropic perfect fluid, $`p = p(\rho)`$, with adiabatic perturbations and $`c_s^2 = p'(\rho_0)`$ above the floor that keeps every admitted first-order mode bounded, $`(\lambda_{\min} - 3)\,c_s^2 > 1`$, read on each domain (ruled 2026-10-11). That is $`c_s^2 > 1/5`$ on $`S^3`$ and $`\mathbb{RP}^3`$, whose first admitted level is $`n = 2`$, the stability page's value, and $`c_s^2 > 1/165`$ on $`S^3/2I`$, whose first is $`n = 12`$. Above, $`c_s^2 \le 1`$ (ruled 2026-10-11): a condition above 1 is recorded beside the grade and never counted. To second order, with the averages of §2 and $`\delta\rho_1`$ the first-order part of $`\delta\rho`$,

```math
\langle p \rangle = p_0 + c_s^2\,\langle\delta\rho\rangle + \tfrac12\,p''(\rho_0)\,\langle\delta\rho_1^{\,2}\rangle + O(\epsilon^3),
```

so $`\langle p\rangle \ne p(\langle\rho\rangle)`$ unless $`p'' = 0`$.
- **Instances:** radiation, and the general law with $`c_s^2`$ and $`p''`$ symbolic.
- **Out of scope, as at linear order:** the coefficient-3 and $`\rho < 0`$ sources, which have no response law on the record, and non-barotropic sources.

**The perturbations (T3).**
- **The sectors:** the ones the ruling admits: H-ANISO, I-S ($`n \ge 2`$), I-V and I-T, each with the stability page's first-order solutions.
- **The configurations:**
  - a single standing mode;
  - a pair of degenerate modes in quadrature with equal amplitudes, which keeps the averaged quadratic terms constant;
  - the general superposition within one degenerate multiplet.
- **Superpositions across distinct harmonics:** the computation checks whether they reduce to these.
- **The quantifier:** every admissible first-order perturbation.

## 2. The averaging

**H-ANISO, I-S and I-T.** These use [Buchert's averaging](https://doi.org/10.1023/A:1012061725841) for irrotational perfect fluids, on the foliation orthogonal to the fluid, over the whole slice. Its averaged Raychaudhuri equation and constraint for the volume radius carry a kinematical backreaction $`Q_D`$ and a dynamical one $`P_D`$, from pressure gradients and the lapse, and both are kept. "The averaged density" is the volume average of $`\rho`$ over the slice.

**I-V.** Its vortical flow has no fluid-orthogonal foliation.
- **The scheme:** [Buchert, Mourier and Roy](https://doi.org/10.1007/s10714-020-02670-6)'s fluid-extrinsic averaging, their §3, whose averaged equations allow arbitrary foliations and a tilted fluid with vorticity.
  - Its volume is the slice's hypersurface volume, $`V_h = \int dV_h`$, as T4 rules.
  - Their fluid-intrinsic scheme, their §4, averages over the fluid's proper volume, $`V_b = \int \Gamma\,dV_h`$. That differs from $`V_h`$ at second order when the tilt is first order, so it is not used.
- **The slices:** slices of constant fluid proper time. They are defined by the fluid, not by coordinates.
  - The fluid clocks are synchronized to $`\tau = 0`$ on the initial slice, the background's static slice at $`t = 0`$, where the first-order data are set.
  - At first order the vortical flow is geodesic, so these slices do not hold the volume fixed by construction.
- **The charge on these slices:** $`\mathcal{N}/V_h = \langle n\Gamma\rangle`$. At fixed $`V_h`$ the second-order tilt, through $`\Gamma = 1 + \tfrac12 v^2 + \dots`$, enters that ratio and can force a shift of the averaged density. The instrument keeps it.
- **The domain:** the whole slice, transported along the fluid congruence as they transport it (their §3.2.2), so it stays the whole closed slice and holds the same fluid elements.
- **The cross-check:** the same reduction on the slices of the Poisson gauge, with its residual homogeneous time reparametrization fixed by setting the homogeneous part of the second-order lapse to zero.
- **Slicing.** Both slicings agree with the background's at first order, so the first-order vector quantities are the same on both. At second order they differ by a relabeling of time. That leaves the slice metric unchanged at this order, because the background's extrinsic curvature vanishes. It shifts the second-order lapse, which enters the averaged constraint only in combinations the static background sets to zero (§3), and it shifts the mean curvature by a divergence, whose average vanishes. So the reduced constraint that settles the I-V cell is the same on both slicings through second order. Nothing more is claimed about the full second-order equations, and beyond second order results are slicing-dependent and are reported as such.

**A caution.** The slicing must not force the answer. Maximal slices keep the volume constant by construction, since a closed slice's volume changes by $`-\int N K\,dV`$, so no maximal foliation is used.

## 3. Decided before the run

**The equations.** For a spatially homogeneous model with a non-tilted barotropic fluid, with $`\theta`$ the expansion and $`\sigma^2`$ the shear scalar:

```math
\dot\theta = -\tfrac13\theta^2 - 2\sigma^2 - 4\pi G(\rho + 3p) + \Lambda, \qquad \dot\rho = -(\rho + p)\,\theta, \qquad {}^3R + \tfrac23\theta^2 - 2\sigma^2 = 16\pi G\rho + 2\Lambda .
```

For the general superposition's rotating non-diagonal members the fluid is non-tilted through first order only: their second-order momentum constraint leaves a residual, reported below. A second-order tilt would enter these equations only at fourth order, so the cell below is unaffected.

**H-ANISO, exactly** (DERIVED).
- **The setting:** the shape modes are the left-invariant traceless deformations of the round metric (Bianchi IX).
- **The steps:**
  - fixing $`R_V`$ at every instant sets $`\theta \equiv 0`$;
  - continuity then keeps $`\rho`$ constant, and C1 holds it at its background value, since at fixed volume the homogeneous $`n = \mathcal{N}/V`$ is fixed;
  - so $`p`$ is fixed too, and Raychaudhuri requires $`2\sigma^2 = \Lambda - 4\pi G(\rho + 3p) = 0`$.
- **The cell:** no configuration with nonzero shear continues: not standing modes, not quadrature pairs, not general superpositions, and under no response law. NOT ABSORBED.
- **The constraint agrees.** With $`\beta`$ the traceless matrix of log scale factors:
  - to second order $`{}^3R = (6/R^2)\big(1 - \tfrac43\,\mathrm{Tr}\,\beta^2\big)`$, and the shape frequency is $`\omega^2 = 8/R^2`$;
  - so $`\delta\,{}^3R = -\omega^2\,\mathrm{Tr}\,\beta^2 \le 0`$;
  - at fixed $`\rho`$ the constraint requires $`\delta\,{}^3R = 2\sigma^2 \ge 0`$.
- **The domains:** the five modes are left-invariant, so they descend to $`S^3/2I`$, where $`2I`$ acts on the left, and to $`\mathbb{RP}^3`$. The cell holds on all three domains.
- **On time average** (T6, a diagnostic only): with the charge held, every configuration fails; with it left free, every configuration holds only at $`c_s^2 = 1/3`$, as the quadrature pair does at every instant.
- **The remaining integrability conditions** (§4, reported):
  - the standing and quadrature configurations, and the general superposition's diagonal members, carry no charge;
  - a rotating non-diagonal member, $`\beta = \epsilon(\cos\omega t\,A + \sin\omega t\,B)`$ with $`A`$ and $`B`$ traceless, of unit norm and not commuting, carries a constant charge, $`8\sqrt2\,\epsilon^2/R^2`$ for the pair the instrument takes, against the unit left-invariant generator along $`[A, B]`$. All of it is gravitational, since the fluid has no first-order tilt, density or pressure. The generator survives on all three domains, so within T7's variables that condition fails.

**I-T, given a reduction the instrument checks before the freeze and the run reports again** (DERIVED from that reduction).
- **The setting:** at first order, tensor modes leave the fluid at rest, with no density, pressure, lapse or expansion perturbation.
- **The reduction:** at second order Buchert's equations then reduce to $`P_D = 0`$ and $`Q_D = -2\langle\sigma^2\rangle`$.
- **The steps:**
  - with $`R_V`$ fixed, the averaged Raychaudhuri equation gives $`4\pi G\,(\delta\langle\rho\rangle + 3\,\delta\langle p\rangle) = -2\langle\sigma^2\rangle`$;
  - under C1, on fluid-orthogonal slices, $`\langle n\rangle = \mathcal{N}/V`$ is fixed, and no first-order density exists, so $`\delta\langle\rho\rangle = \delta\langle p\rangle = 0`$;
  - so $`\langle\sigma^2\rangle = 0`$.
- **The cell:** NOT ABSORBED, for every configuration and every response law.

**I-V, given a reduction the instrument checks before the freeze and the run reports again** (DERIVED from that reduction).
- **The setting:**
  - at first order, vector modes carry no density, pressure, lapse or expansion perturbation. The fluid's tilt velocity $`v^i`$ is transverse and constant in time, and the shift follows it through the momentum constraint ([the stability page](static-domain-stability.md)'s vector sector);
  - integrating that constraint against a Killing field shows the fluid carries no total angular momentum at first order, so the admitted modes are the transverse harmonics with $`n \ge 2`$;
  - no pressure gradient acts at first order, so the flow is geodesic, the slices of constant fluid proper time agree with the background's at first order, and on them $`N = \Gamma = 1 + O(\epsilon^2)`$;
  - a spatial relabeling removes the first-order vector part of the slices' metric, so the slices stay round at first order.
- **What settles the cell:** the averaged Hamiltonian constraint alone. It holds on every slice and needs no lapse. For the whole closed slice, Buchert, Mourier and Roy's form of it is their (3.33), with the global kinematical and stress-energy backreactions of their (3.54) and (3.56).
- **The reduction,** at second order with $`V_h`$ fixed:
  - the kinematical backreaction is $`\mathcal{Q}_\Sigma = -\langle\mathcal{K}_{ij}\mathcal{K}^{ij}\rangle`$, since the slices' mean curvature vanishes at first order;
  - the stress-energy backreaction is $`\mathcal{T}_\Sigma = -16\pi G(\rho_0 + p_0)\langle v^2\rangle`$;
  - the averaged curvature does not change. The slices are round at first order, and its first variation, $`-(2/R^2)\langle\mathrm{tr}\,h^{(2)}\rangle`$, vanishes at fixed volume;
  - the second-order lapse enters (3.33) only through combinations the static background sets to zero.
- **Under C1:** at fixed $`V_h`$ the charge gives $`\langle n\Gamma\rangle = n_0`$, with $`\Gamma = 1 + \tfrac12 v^2`$, so $`\delta\langle n\rangle = -\tfrac12 n_0\langle v^2\rangle`$. By T7(b)'s $`dn/n = d\rho/(\rho + p)`$, $`\delta\langle\rho\rangle = -\tfrac12(\rho_0 + p_0)\langle v^2\rangle`$.

With the radius fixed, (3.33) then reads

```math
4\pi G(\rho_0 + p_0)\,\langle v^2\rangle + \tfrac12\,\langle\mathcal{K}_{ij}\mathcal{K}^{ij}\rangle = 0 .
```

Both terms are non-negative, and the first vanishes only when $`v = 0`$. The plain averaged Hamiltonian constraint of the ADM split gives the same equation, with $`E = \rho + (\rho + p)v^2`$ the energy density the slices' normal observers measure.
- **The cell:** NOT ABSORBED, for every configuration and every response law.
- **Time:** the first-order configuration is time-independent, so "every instant" adds nothing here, and the time-averaged diagnostic is inapplicable (T6).
- **The remaining integrability conditions** (§4, reported): none. With the slices round, the lapse one and no density at first order, the second-order momentum constraint has no quadratic part in the relabeled gauge. The instrument confirms this against every generator, on both $`n = 2`$ fields, there and in a gauge with no shift.

**For comparison: the charge left free (not the ruled reading).** If the homogeneous density were free initial data, set by the constraint, then in the shape and tensor sectors:
- the standing modes would still fail, since their shear oscillates;
- the quadrature pairs would hold only at $`c_s^2 = 1/3`$, radiation's value.

They do so:
- **In H-ANISO,** directly. A quadrature pair has constant $`\sigma^2`$ with $`\delta\,{}^3R = -2\sigma^2`$, so the constraint gives $`4\pi G\,\delta\rho = -\sigma^2`$, and Raychaudhuri needs $`4\pi G(1 + 3c_s^2)\,\delta\rho = -2\sigma^2`$.
- **In I-T,** per mode, $`\delta\langle{}^3R\rangle = -\omega_n^2\langle\mathrm{Tr}\,\beta^2\rangle`$. Here $`h = 2\beta`$, $`k_n^2/R^2`$ is the mode's rough-Laplacian eigenvalue ($`k^2 = 6`$ at the lowest tensor level), and $`\omega_n^2 = (k_n^2 + 2)/R^2`$.
  - The tensor equation's quadratic Hamiltonian has that second variation as its potential. At the lowest tensor level it is the exact H-ANISO result.
  - This comparison is the computation's quadrature control (§5).

In I-V, whose first-order configuration is time-independent, (3.33) would fix the homogeneous density. Their (3.32), whose dynamical backreaction (3.55) is fourth order here, would then hold only at

```math
c_s^2 = \frac{a + 3b}{3(a + b)}, \qquad a = 4\pi G(\rho_0 + p_0)\langle v^2\rangle, \qquad b = \tfrac14\langle\mathcal{K}_{ij}\mathcal{K}^{ij}\rangle,
```

one value strictly between 1/3 and 1, set by the configuration. Here $`b > 0`$, because the momentum constraint makes $`\mathcal{K}_{ij}`$ nonzero wherever $`v`$ is.

**So the overall grade is NOT ABSORBED before the run,** since the overall grade is the weakest. What stays open is the density sector, I-S.

**Losic and Unruh** ([Phys. Rev. D 71, 044011 (2005)](https://doi.org/10.1103/PhysRevD.71.044011)) treat an irrotational perfect fluid on the Einstein static universe. They show that the homogeneous linear modes "must be present if the second order constraint equations are to be integrable".
- **How it reads against the ruling:** the ruling removes exactly those modes, so the result bears directly on I-S.
- **Where it stands here:** a record written after the run compares it; it is not assumed (§5).

## 4. The grades, and what each does

**Per sector and configuration:**
- **ABSORBED:** through second order, for small enough amplitude, the averaged constraint, Raychaudhuri and continuity equations of §2 hold with $`R_V`$ fixed. Only the variables T7 induces are used.
- **CONDITIONAL:** they hold only if the response law meets a stated condition, or only for some configurations.
- **NOT ABSORBED:** they fail at nonzero amplitude.
- **The reading:** under both charge readings, each residual's constant, $`\cos 2\omega t`$ and $`\sin 2\omega t`$ parts must vanish. Where they vanish only for some response laws, those laws are the condition. A law outside T2's class on the domain, below its floor, above 1 or not real, counts as none; a law tied to $`p''`$ counts only where some real $`p''`$ puts it inside the class.
  - **C2's charge shift** is one constant, solved and never set. It comes from the constraint's constant part when that part carries it, and otherwise from another residual in which it enters free of the response law.
  - **When nothing fixes it that way,** or the response laws where its coefficient vanishes would need excluding, the reading is withdrawn rather than guessed.
- **Over levels:** a configuration's grade on a domain is the weakest over that domain's admitted levels, with one quantifier. The condition is the set of admissible laws that satisfy every admitted level at once, $`C_D = \bigcap_{n \in A_D} C_n`$: ABSORBED when it holds every law, CONDITIONAL when it is not empty, NOT ABSORBED when it is. A condition that only looks different from level to level does not empty it.
  - **How it is computed:** every domain admits infinitely many levels, and once the charge shift is solved the conditions are polynomials in $`\lambda`$. So a law satisfies every admitted level exactly when each coefficient of each condition's polynomial in $`\lambda`$ vanishes there: a system in $`c_s^2`$ and $`p''`$ alone.
  - **Exceptional levels:** under C2 the charge shift is solved from the constraint's constant part. Where its coefficient depends on $`\lambda`$ alone, the admitted levels where it vanishes are read on their own, with the shift solved as the reading solves it, and intersected in.
  - **Where the constraint never carries the shift:** it is projected out of the other residuals through a coefficient free of $`\lambda`$ and of the response law, never set to zero. Failing that, the every-level reading is withdrawn.
  - **Withdrawal:** where the coefficient depends on the response law, or an exceptional level's reading is withdrawn, the every-level reading is withdrawn. The computed levels then carry the grade, by the same intersection taken over them alone, never by their weakest grade.

**What a grade certifies:** those averaged equations, through second order, and nothing more.
- **Reported beside each grade, ungraded:**
  - the remaining integrability conditions, which are the constraints integrated against the background's other Killing fields. Each is reported as its computed value against each generator, with its gravitational and matter parts, the domains on which the generator survives, and whether it vanishes:
    - the split between the two parts belongs to the gauge: in the density sector's comoving-orthogonal gauge the fluid moves with the slices' normal, so the whole charge sits on the gravitational side;
    - a nonzero value means the condition fails within T7's variables;
    - a second-order rigid rotation of the fluid, which T7 does not list, could carry it. That rotation enters the momentum constraint at second order and these averaged equations only at fourth. It is recorded beside the value as an observation and not used;
    - the timelike condition is the averaged constraint itself, which the grade tests;
    - the spatial conditions do not depend on whether $`R_V`$ is fixed, so they are reported, not graded. A homogeneous change of the radius at second order enters $`K`$ as a multiple of the identity, which drops out of the momentum constraint, and homogeneous changes of $`\rho`$ and $`p`$ meet first-order velocities only at third order. The instrument checks this on H-ANISO;
    - a nonzero complete charge is still a failure of full second-order compatibility under T7, apart from the grade: a configuration whose averaged equations hold is never described as second-order compatible while one of its charges is nonzero, and the rotation is never a repair;
  - the time-averaged diagnostic: the grade's own reading on the residuals' averages over one period of the first-order mode, from $`t = 0`$, with the same homogeneous variables and no others. Under C1 there are none; under C2 there is the one constant density shift, solved from the averaged constraint. No integration constant enters.
- **Not claimed by any grade:** that a first-order perturbation extends to an exact solution, or anything at third order.

**Consequences:**
- **ABSORBED in every admitted sector:** this outcome is closed by §3.
- **CONDITIONAL:** the condition joins C12's entry test for candidates on (a) or (c), and a dated note scopes the ruling's sentence to it.
- **NOT ABSORBED:** the configuration cannot be continued to second order under the declared assumptions.
  - **What it means:** the ruling's "every order" fails for that sector and source class. That is an internal inconsistency in pairing the fixed radius with (a) or (c), FATAL-class for that pairing: a barotropic perfect fluid, with the readings of §0.
  - **What it does not mean:**
    - it does not reach every source theory on those branches. A non-barotropic source, or one whose homogeneous sector has degrees of freedom of its own, lies outside the class;
    - branch (b) is untouched.
  - **The ways out:**
    - *A restriction excluding those configurations, carried as a cost.* Under the bar's full-class clause it counts only when it is motivated (by the postulate, or by a prior framework-level posit, as the ruling of 2026-10-10 reads the clause) and declared before the computation, "never because it rescues a candidate". For the cells decided in §3, declaring it now would be exactly that, so it is not available. Reading the commitment as fixing the round metric too, the reading [the stability page](static-domain-stability.md)'s §IV names, would be such a restriction. The ruling of 2026-10-10 admits the shape sector, and the engine states that the radius is fixed, not the shape.
    - *A candidate that implements the fixed radius by changing the homogeneous field equations,* which (a) and (c) assert unmodified.
    - *A radius that responds,* which the ruling excludes.
  - **Which way the framework takes** is a ruling made after the result is recorded.

## 5. The computation

**The instrument** is [`fixed_radius_check.py`](scripts/fixed-radius-second-order/fixed_radius_check.py), SHA-256 `71f705b686baa075b2a233040bbd3454b186ded620544dbdf6f27c51574430f9`. Qualification runs as `python3 fixed_radius_check.py`, and its output is [`fixed_radius_check.out`](scripts/fixed-radius-second-order/fixed_radius_check.out) beside it. The run is `python3 fixed_radius_check.py run --registration-commit <commit> --page-sha256 <SHA-256>`, given this page's commit on main and its SHA-256.

**Qualification and the run are kept apart.** A symbolic calculation is a result even with no data in it, so the open sectors' grades are computed only in the registered run.
- **Qualification,** before the freeze, computes only:
  - the instrument's algebraic identities;
  - the cells decided in §3, H-ANISO exactly;
  - the I-T reduction, $`P_D = 0`$ and $`Q_D = -2\langle\sigma^2\rangle`$ at second order;
  - the I-V reduction of §3, on both slicings of §2, derived and not assumed: from the linearized vector constraints to the vanishing first-order mean curvature and curvature change, then through the averaged constraint to the positive sum, both in Buchert, Mourier and Roy's form and in the plain ADM form;
  - the decided sectors' time-averaged diagnostics and integrability conditions;
  - the machinery the run uses, on controls alone: the symbolic form, which must reproduce the harmonic averages; the reading over levels, on synthetic forms; and the integrability routine, on H-ANISO against the class-A frame formula, on I-V in two gauges, and on the density mode's first-order constraint;
  - the controls below, each with its mutation arm;
  - a terms-to-instrument map that gives every term here a code path.
- **The run** computes the I-S grades, their time-averaged diagnostics and their integrability conditions, and reports the decided sectors again. It first verifies the frozen registration and the instrument's identity, as [the nonflat distance comparison](nonflat-distance-comparison.md)'s run did.
  - **Its record,** `run.json`, carries every grade, diagnostic, condition and integrability value, and the residual coefficients behind each grade: each level's own coefficients, their polynomials in $`\lambda`$, and every configuration's constant, cosine and sine parts, symbolic and per level. The identities in it are the ones the gate computes from the bytes, never a caller's label.
  - **A dry run** on a non-physical configuration exercises the same code path before the freeze, and its record is discarded.
  - **Repeatability:** the instrument fixes Python's hash seed, so qualification, the dry run and the run follow the same computational paths, and qualification's output repeats byte for byte in one environment.

**The density sector at every level.**
- **The coefficients:** the run computes the second-order residuals' coefficients at $`n = 2`$ to 10 and at 12, with the time dependence kept general. Each is a polynomial in $`\lambda`$ of degree at most 5:
  - every average is a quadratic integral of first-order fields, and integration by parts on the sphere of constant curvature reduces it to a polynomial in $`\lambda`$. At most 3 of the degree comes from its derivatives, which number at most six, two to each power of $`\lambda`$. At most 2 comes from its amplitudes: $`\psi`$ and $`E`$ carry none, and $`\nu`$ and $`x`$ each carry $`\lambda - 3`$;
  - the two homogeneous variables solved on the way, the volume's trace and the charge's density, come from linear equations with constant coefficients, and the averages divide only by the background volume, so no denominator in $`\lambda`$ enters;
  - the time dependence stays separate, so the frequency enters only when it is substituted, through $`\omega^2`$, a polynomial in $`\lambda`$. The sine part is divided by $`\omega`$, which T2 keeps positive at every admitted level.
- **The checks:** the levels $`n = 2`$ to 8 fix each polynomial exactly. Agreement at all ten computed levels certifies it for any degree up to 9, since a difference of degree at most 9 with ten roots vanishes. The explicit grades at $`n = 2`$ and 12 check the reading, and fail closed: if either disagrees with it, no verdict of that configuration is certified, and both values are kept.
- **The fallback:** if a check fails, or a degree exceeds the bound, the symbolic form is not established. The record then withdraws the every-level claim, and the grades cover the computed levels only, as the intersection of their law sets (§4).

**The order of operations.**
1. Build and qualify the instrument. Then freeze this page and the instrument, with the terms' SHA-256 on main before the run starts.
2. The run checks the freeze: this page's commit on main, its SHA-256, and the instrument's.
3. For each open sector and configuration, take the stability page's first-order solution, at amplitude $`\epsilon`$.
4. Compute the averaged second-order quantities in the §2 scheme.
5. Impose $`R_V`$ fixed at every instant: the averaged expansion and its time derivative vanish.
6. Solve for the variables T7 induces, and test consistency with the response law of T2. Report the charge-left-free reading beside each grade, as §3 does. Then compute the time-averaged diagnostic.
7. Grade each configuration (§4). Report the I-T and I-V reductions again under the frozen instrument.

Nothing from step 4 on changes the terms. A change after that is an erratum, with its reason. The check holds inside the perturbative regime.

**The obligations.**
- **I-T and I-V:** the reductions of §3 pass qualification before the freeze, and the run reports them again.
- **I-S:** reproduce Losic and Unruh's integrability result, or compare with it explicitly.
  - **Who and when:** the comparison is written after the run, by the page's author, from `run.json` and their paper. It is reviewed as this registration was, and the result does not close without it.
  - **What it is:** an interpretive record, not an output of the instrument, which computes no comparison.
  - **Read from the paper:** their equation of state, gauge and domain, since their abstract states none of them.
  - **One difference, named now:** on a closed space the second-order integrability conditions are the constraints integrated against the Killing fields. On $`S^3/2I`$ only $`\partial_t`$ and the three generators of the right action survive. So a condition of theirs that comes from the left generators does not transfer to the framework's domain.
- **Every sector:** report the remaining integrability conditions (§4):
  - H-ANISO: the page's configurations, and a rotating non-diagonal member of the general superposition;
  - I-V: both $`n = 2`$ fields, in two gauges;
  - I-S: the zonal standing mode, whose spatial charges vanish by symmetry, and a rotating pair at $`n = 2`$, as an example rather than an exhaustive test. Both live on $`S^3`$ and $`\mathbb{RP}^3`$. No density-sector pair is computed at $`n = 12`$, the first level $`S^3/2I`$ admits, since the spatial conditions are the same with the radius free;
  - I-T: the lowest level, from H-ANISO by orientation reversal; higher levels are not computed.

**The controls.** Each check also carries a mutation arm.
- **Positive:** an exact closed FLRW solution near the static one, with the same $`\Lambda`$ and fluid, whose radius is free to respond. Its second-order expansion must satisfy the averaged equations.
- **Negative:** the H-ANISO standing mode under T6 must fail, for every response law.
- **The quadrature cell:** with the charge left free, it must pass at $`c_s^2 = 1/3`$ and fail at every other value. Under C1 it must fail at every value.
- **The time-averaged diagnostic:** the quadrature cell, constant in time, must read on average as its grade. The standing and general configurations, averaged over a period, must read the same: this exercises the averaging itself.

## 6. After the run

- **What lands:** the results go here, under Results, with the Losic and Unruh comparison of §5 beside them; then the page closes.
- **The dated notes:**
  - the postulate bridge's ruling stands as made, and a dated note there points to this page;
  - a condition found under CONDITIONAL goes to C12 on [the stress-tensor bridge](stress-tensor-bridge.md).
- **The ways out:** which way the framework takes (§4) is a ruling made after the results are recorded.

## Sources

- T. Buchert, "On Average Properties of Inhomogeneous Fluids in General Relativity: Perfect Fluid Cosmologies", [Gen. Relativ. Gravit. 33, 1381–1405 (2001)](https://doi.org/10.1023/A:1012061725841): irrotational perfect fluids, on the foliation orthogonal to the flow.
- T. Buchert, P. Mourier and X. Roy, "On average properties of inhomogeneous fluids in general relativity III: general fluid cosmologies", [Gen. Relativ. Gravit. 52, 27 (2020)](https://doi.org/10.1007/s10714-020-02670-6): arbitrary foliations, lapse and shift, and a tilted fluid with vorticity.
- B. Losic and W. G. Unruh, "Initial value problem for second order scalar fluctuations in the Einstein static universe", [Phys. Rev. D 71, 044011 (2005)](https://doi.org/10.1103/PhysRevD.71.044011).

## Record and errata

**The qualification record** (2026-10-11), on the instrument pinned in §5:
- **Qualification:** ALL PASS, 83 lines, 41 checks and 42 mutation arms, each arm firing only after its parent passed. It runs under hash seed 0, and its output repeats byte for byte in one environment.
- **The dry run:** a non-physical configuration took the run's whole path. The two density-sector paths agree on it in every configuration at $`n = 2`$ and 12.
- **The run gate's probe:** in a throwaway clone, the gate passed a registration that pins the instrument and refused four mutations: a commit off main, a wrong page hash, a page that does not pin the instrument, and an instrument changed on disk.

No erratum.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
