<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Fixed Radius at Second Order

**Type:** Result
**State:** Closed
**Status (2026-10-12):** Run once on 2026-10-11 from the frozen registration, and closed. On the stress-tensor bridge's branches (a) and (c), with Einstein's equations on the static metric and a barotropic perfect fluid, no admitted first-order perturbation continues to second order with the volume radius fixed at every instant and the fluid's charge held. Under the four readings ruled on 2026-10-11, every admitted sector is NOT ABSORBED. The shape, tensor and vorticity sectors were decided before the run. The run decided the density sector at every admitted level, on $`S^3`$, $`\mathbb{RP}^3`$ and $`S^3/2I`$, with the eigenvalue kept symbolic, and reported the decided sectors again unchanged. The verdict does not rest on the charge reading: with the charge left free, the standing modes of the shape, tensor and density sectors still fail. By §4 this is an internal inconsistency in pairing the fixed radius with (a) or (c) for that source class, FATAL-class for that pairing, and not a result about MIT as a whole. Which way the framework takes is a ruling made after this record. The comparison with Losic and Unruh's integrability result is recorded beside the Results.
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

## Results

**Executed 2026-10-11, once,** from the frozen registration `09559d3`, by the instrument pinned in §5, on macOS 15.8, Python 3.13.13, SymPy 1.14.0, under hash seed 0, in 661.3 s. The run's whole record is [`run.json`](scripts/fixed-radius-second-order/run.json), committed unedited in `fd4dff0`, with SHA-256 `a1f32b486cd6aeb719f8e4901df674ed777ffb47627196043ac92221b40ad972`.
- **The gate** passed against this registration:
  - the commit is on main;
  - the page's SHA-256 is `bf2c0dd1ce3c2df44bd9bb9c1630b87564cf8ce109ea9f0d848e7f3ef8d15237`;
  - the page pins the instrument;
  - the instrument on disk is the file at that commit, with SHA-256 `71f705b686baa075b2a233040bbd3454b186ded620544dbdf6f27c51574430f9`.
- **The decided sectors** came out as §3 records them, value for value:
  - the H-ANISO cells under both charge readings, with their time-averaged diagnostics and integrability values;
  - the I-T reduction, $`P_D = 0`$ and $`Q_D = -2\langle\sigma^2\rangle`$;
  - the I-V reduction, with no integrability charge.
- **Reproduced:** a review unit reran the frozen instrument twice, on Linux with Python 3.13.16 and SymPy 1.14.0, and every computed field came out the same.
  - **The comparison:** remove `environment` and `seconds`, and write the rest as `json.dumps(r, indent=1, sort_keys=True)`. This record then hashes to `d192dc9845c6546072e1a57a57610c8875e90b4ddcf296aeac3bb35e90b11572`, and so does one rerun.
  - **The other rerun** hashes to `a3af910b22bd99dd20b8faf496743bf4e3fa56efb10f654529d3e6f52ac53df3`. That is this record's content with the gate's commit given as the full hash of `09559d3`, since the record keeps that argument as typed (Record and errata).
  - **What is not identical:** the full records. Their environment and run time differ by construction, and in one rerun so does the commit string.

**The verdict: NOT ABSORBED in every admitted sector,** under the readings of §0. No admitted first-order perturbation of a barotropic perfect fluid continues to second order on (a) or (c) with the volume radius fixed at every instant and the fluid's charge held, for any response law in T2's class. Superpositions do not escape it: under C1 every sector's residual in the averaged constraint has one sign, the same in all four sectors, and quadratic terms from different sectors fall in inequivalent representations of the round $`S^3`$'s symmetry, so they do not mix in the averages, on $`S^3`$ or its quotients. A superposition with a vortical part is read on slices that agree with each sector's own to first order, as Buchert, Mourier and Roy's scheme allows (§2). No nonzero admitted perturbation continues (DERIVED from the recorded residuals).
- **What it means (§4):** the ruling's "every order" fails for that source class. That is an internal inconsistency in pairing the fixed radius with (a) or (c), FATAL-class for that pairing: a barotropic perfect fluid, with the readings of §0.
- **What it does not reach:**
  - a non-barotropic source, or one whose homogeneous sector has degrees of freedom of its own;
  - branch (b);
  - an exact solution, or third order;
  - MIT as a whole, its topology or its quotient construction.
- **The ways out** (§4): which way the framework takes is a ruling made after this record.

**The density sector (I-S): the every-level reading held.**
- **The coefficients:** each is a polynomial in $`\lambda`$ of degree at most 3, within the bound of 5. The levels $`n = 2`$ to 8 fix it, and 9, 10 and 12 confirm it.
- **The charge shift:** under C2 its coefficient is the constant $`-4/R^2`$, so no level is exceptional.
- **The explicit checks:** at $`n = 2`$ and 12 the explicit grades agree with the reading in every configuration, under both charge readings, so every verdict is certified.

**With the charge held (C1, the graded reading): NOT ABSORBED.** That holds for standing modes, quadrature pairs and the general superposition, at every admitted level, on $`S^3`$, $`\mathbb{RP}^3`$ and $`S^3/2I`$, for every response law in T2's class. The time-averaged diagnostic reads NOT ABSORBED too.
- **Why:** with the radius and the fluid's charge fixed, the quadratic density-wave contribution leaves a nonzero averaged Hamiltonian-constraint residual, with no admissible homogeneous response available to cancel it.
- **Its form:** with $`\omega^2 = \big((\lambda - 3)c_s^2 - 1\big)/R^2`$, and per $`\epsilon^2`$ in the record's normalization of the modes, the constraint's residual is:
  - $`-2(\lambda - 3)\,\omega^2`$ for a standing mode of unit amplitude;
  - $`-4(\lambda - 3)\,\omega^2`$ for a quadrature pair of unit amplitudes;
  - $`-\tfrac52(\lambda - 3)\,\omega^2`$ for the general superposition, with amplitudes 1 and 1/2.

  It is constant in time.
- **Its sign:** one sign throughout, and nonzero at every admitted level for every law in T2's class. It vanishes only where $`\omega = 0`$, which T2's floor excludes.

**With the charge left free (C2, for comparison, not graded).** The charge shift is solved from the constraint, and the Raychaudhuri equation carries the obstruction.
- **Quadrature pairs: CONDITIONAL** on every domain. Every admitted level holds at once only at $`c_s^2 = 1/3`$ with $`p'' = 8\pi G R^2/9`$, which is $`2/\big(9(\rho_0 + p_0)\big)`$.
  - **Its scope:** that is a conditional solution of the averaged equations, not a general physical rescue. The rotating pair at $`n = 2`$ carries a nonzero charge of its own (below). That example lives on $`S^3`$ and $`\mathbb{RP}^3`$, so it establishes nothing for $`S^3/2I`$.
  - **Radiation's linear law,** $`p'' = 0`$, leaves the constant part of the pair's Raychaudhuri residual at $`-(\lambda - 3)^2/(3R^2)`$.
- **Standing modes and the general superposition: NOT ABSORBED** on every domain.
  - **Single levels:** some hold them, each at a law of its own: $`c_s^2 = 3/13`$ at $`n = 2`$, on $`S^3`$ and $`\mathbb{RP}^3`$, and $`c_s^2 = 1/111`$ at $`n = 12`$, on $`S^3/2I`$. No law holds every admitted level.
  - **At the pair's law,** the $`\cos 2\omega t`$ part of the Raychaudhuri equation is nonzero at every admitted level:
    - $`(\lambda - 6)^2(\lambda - 3)/(9R^2)`$ for a standing mode;
    - $`(\lambda - 6)^2(\lambda - 3)/(12R^2)`$ for the general superposition.
- **On time average:** all three configurations read CONDITIONAL on every domain, at the pair's law.
- **The parallel with the shape sector:** there too, with the charge left free, the pair and the time averages select $`c_s^2 = 1/3`$ (§3). The density sector adds the condition on $`p''`$.
- **So the density sector's NOT ABSORBED also holds with the charge left free,** because its standing-mode obstructions remain, as in the shape and tensor sectors. It does not rest on C1, which T7(b) declares as a restriction.

**Nothing goes to C12** (§6). No graded reading is CONDITIONAL, and the C2 law is a comparison value only.

**The remaining integrability conditions** (§4), reported beside the grades and not graded:
- **H-ANISO, I-T and I-V:** as §3 and §5 record them.
- **I-S, the zonal standing mode at $`n = 2`$:** zero against the six rotation generators. The two chiral triples are combinations of those six, so these are six independent conditions, all met.
- **I-S, a rotating pair at $`n = 2`$** (the harmonics $`X_1X_3`$ and $`X_1X_4`$), an example rather than an exhaustive test:
  - **The charge:** $`-10\sqrt{5c_s^2 - 1}`$ per $`\epsilon^2`$ at unit radius, in the record's normalization of the harmonics, against $`X_3\partial_4 - X_4\partial_3`$. That is $`-10\,\omega`$, with $`\omega`$ the pair's frequency.
  - **Its parts:** all of it is gravitational, as the comoving-orthogonal gauge places it (§4).
  - **On the chiral triples:** it shows as $`+10\,\omega`$ on the right action's generator $`q \mapsto q\,i`$, whose triple survives on $`S^3/2I`$, and as $`-10\,\omega`$ on the left action's $`q \mapsto i\,q`$. Every other generator gives zero.
  - **What it means:** within T7's variables the condition fails, so the pair is not second-order compatible, apart from its grade. A second-order rigid rotation of the fluid, which T7 does not list, could carry the charge. That is recorded as an observation and not used (§4).
  - **The radius:** the charge is the same whether $`R_V`$ is fixed or free (§4).
  - **The domains:** the pair lives on $`S^3`$ and $`\mathbb{RP}^3`$. On $`S^3/2I`$ the spatial charges are not computed: its first admitted level is $`n = 12`$, and no pair is computed there (§5).
- **The timelike condition** is the averaged constraint itself, graded above.

## The Losic and Unruh comparison

This record was written after the run, by the page's author, from `run.json` and their paper, as §5 requires. It is interpretive: the instrument computes no comparison.
- **Read from:** the arXiv version, [gr-qc/0408011](https://arxiv.org/abs/gr-qc/0408011), the preprint of the paper in Sources. Equation numbers here are the preprint's.
- **Their equation of state:** an irrotational perfect fluid given by a velocity potential, with $`p`$ proportional to $`\rho`$. So $`c_s^2 = 1/(2\alpha - 1)`$, with $`1 \le \alpha \le 3`$, and $`1/5 \le c_s^2 \le 1`$.
- **Their domain:** the Einstein static universe on $`S^3`$, with $`\Lambda`$.
- **Their gauge:** a linear change of coordinates, their (37) to (39), removes:
  - the metric perturbation's vector part;
  - the scalar part $`\delta\pi^{(Tr)}`$ of its momentum;
  - the homogeneous part of the second-order matter momentum $`\delta^2\pi_\phi`$.

  A remaining freedom in the scalar sector removes the homogeneous metric mode.
- **Their condition:** the integrability condition of the timelike Killing field. It is the second-order Hamiltonian constraint integrated over $`S^3`$, their (41) to (43).
  - **Its parts:** its inhomogeneous part $`A`$, which includes the tensor modes, is positive definite for $`\alpha \ge 1`$ and $`L \ge 2`$. The homogeneous mode's rate enters with the opposite sign.
  - **Their result:** without the homogeneous linear mode, the condition has no nontrivial solution.
  - **Its scope:** they work with this condition alone, and leave the conditions of the spatial Killing fields aside.
- **Here:** the timelike condition is the averaged constraint (13b) itself, on fluid-orthogonal slices, over the whole slice (§4). The fixed radius removes the homogeneous linear mode. Under C1 the conserved charge fixes the second-order homogeneous density.
- **The correspondence, of structure and sign:** in both, the inhomogeneous modes leave a contribution of one sign. What could cancel it is a homogeneous rate, which enters with the opposite sign.
  - **There:** their (42) sets the homogeneous mode's $`\tfrac32\,\tilde{\mathcal{A}}_{\delta\pi}^{2}\,V`$ against $`\int A`$.
  - **Here:** (13b) carries $`6(\dot a_D/a_D)^2`$ against the waves' residual, and the fixed radius sets it to zero.
- **Where the settings overlap,** the verdicts agree. The overlap is a linear law with $`1/5 < c_s^2 \le 1`$, on $`S^3`$, with no homogeneous mode.
  - **Here:** the density sector is NOT ABSORBED for every linear law, under both charge readings, since C2's every-level condition needs $`p'' \ne 0`$.
  - **There:** the condition has no nontrivial solution.
- **The differences:**
  - **The law:** theirs is linear. Here any barotropic law in T2's class is admitted, and the C1 residual carries no $`p''`$.
  - **The second-order homogeneous matter:**
    - **There:** their gauge choice removes it.
    - **Here:** the charge fixes it (C1), or it is left free (C2). Under C2 the constraint is met, and the Raychaudhuri equation carries the obstruction.
    - **Not checked:** whether their gauge-fixed term corresponds to C1's fixed charge. The agreement above does not depend on it.
  - **The tensor modes:** their integral includes them. Here the tensor sector is decided on its own, through the Raychaudhuri equation (§3).
  - **The domain:**
    - **There:** $`S^3`$.
    - **Here:** $`\mathbb{RP}^3`$ and $`S^3/2I`$ too, by restriction to their invariant modes. On $`S^3/2I`$, T2's class reaches down to $`c_s^2 > 1/165`$, below their range.
    - **The difference §5 names in advance,** a condition from the left generators, does not arise: their condition comes from the timelike Killing field, which survives on $`S^3/2I`$.
  - **The spatial conditions:** they leave them aside. Here they are reported beside the grades, with those on $`S^3/2I`$ not computed. The $`n = 2`$ pair's charge sits on both triples, so it says nothing about the right triple at $`n = 12`$.
- **What it does not establish:** an independent reproduction of their (43), or an equivalence of the two formulations. Their gauge, variables and equations differ from these.
- **An energy reading, offered and not used:**
  - **The sign convention:** the instrument writes (13b) as $`6(\dot a_D/a_D)^2 - 16\pi G\langle N^2\rho\rangle - 2\Lambda\langle N^2\rangle + Q_D + \langle N^2\,{}^3R\rangle = 0`$. So a positive energy density on the source side enters with a minus sign.
  - **The waves' part:** at fixed radius, under C1, it has that sign. It is $`-2(\lambda - 3)\,\omega^2`$ per $`\epsilon^2`$ for a unit standing mode, twice that for the pair, and 5/4 of it for amplitudes 1 and 1/2.
  - **Why read it as energy:** it scales as a quadratic wave energy does, with $`\omega^2`$ and with the summed squared amplitudes.
  - **Its standing:** they caution that, in their gauge, their integral is not the integral of the second-order Hamiltonian. So the reading is not a computed energy, and nothing above rests on it.

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

**Erratum (2026-10-12), after the run: the record's commit field.** A review unit, comparing reruns, found one description too strong.
- **The words:** the gate's docstring says the record keeps the values the gate computes, not its arguments. §5 says the record's identities are the gate's computations from the bytes, never a caller's label.
- **The fact:** `gate.commit` is the commit argument as typed. The gate checks it against main, the page's hash, the pin and the instrument at that commit, but does not resolve it to its full hash. The record's SHA-256s are computed from the bytes.
- **The consequence:** a rerun given the full hash of `09559d3` records the full hash, and that field alone differs (Results).
- **What changes:** neither the frozen instrument nor any term, grade or value. This note carries the correction.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
