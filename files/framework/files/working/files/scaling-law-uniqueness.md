<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Scaling Law as a Separated Measurement Form on S³/2I

**Type:** Program
**State:** Active
**Status (2026-09-01):** Active, scoped to the spectral-boundary observable class. Two rows are forced; the factored form separates on a Schur+homothety+Lemma 8 argument but is not closed until the commutant theorem lands.
**Summary:** Asks whether the scaling law A/A_P = C(Θ)·(√Ω)^{-n} is forced rather than postulated, within the spectral-boundary observable class.
**Inputs:** the Sector A first-positive eigenvalue, `the-mirror.md` (Lemma 8, the character ceiling), the mass-spectrum R determination, the gauge-ladder note

ACTIVE. Scoped to the spectral-boundary observable class native to the topology: observables that are SU(2)-equivariant functionals of the first-positive boundary mode and the Hodge-Laplace spectrum. That class is a premise, not shown to exhaust the physical observables. Within it: the phase operator's sinusoidal family is forced by the anti-periodic BC and its first-positive member selected by background symmetry; the integer-depth hierarchy follows from units plus exact homothety covariance at definite weight; and the factored form *separates* on a Schur + homothety + Lemma 8 argument. The separation is argued, not closed: independent coordinates do not by themselves forbid a cross-term, so the no-cross-term step needs the commutant theorem A_obs = A_Θ ⊗ A_spec (the precise open target). Eigenvalue-side conditions: a parity-preserving cone condition and δ₀/R > 2/e (both met by the Friedrichs default), plus the narrow band W ≤ πR/2, a geometric input; past the critical width the first-positive mode crosses to a width-dependent transverse branch. Off the form: the α_W twist and the extension selection. Well assignments remain the separate next layer.

---

## The Question

Given S¹ = ∂(Möbius) ↪ S³, ∂S³ = ∅, with anti-periodic boundary conditions and the 120-domain native to S³, and given the observable class native to that topology (SU(2)-equivariant functionals of the first-positive boundary mode and the Hodge-Laplace spectrum), is there any measurement rule within that class other than

```math
\frac{A}{A_P} = C(\Theta) \cdot (\sqrt{\Omega})^{-n}
```

that produces finite, well-defined observables?

If not, the separated form is forced within that class. Whether the class exhausts the physical observables is a further premise, not part of the question. The aim is a Gleason-style rigidity (Born is the unique measure on the projection lattice); here it is reached for two of the three factors and argued, not yet closed, for the third.

---

## What's Closed

The proof splits into three structural pieces. Two close cleanly: the phase operator (anti-periodic BC for the family, background symmetry for the member) and the integer-depth hierarchy (units for the admissible dimensional form, exact homothety for the power). The third, the factored form, *separates* on a Schur + homothety argument (dimensionlessness does not supply it), but is not yet closed: the no-cross-term step needs the commutant theorem (below). The heavy machinery once aimed at the hierarchy addresses a target that dimensional analysis already settles.

| Piece | Status | Mechanism |
|---|---|---|
| Factored form C(Θ) × g(Ω, n) | SEPARATES within the class; commutant theorem pending | Dimensionlessness does not force a product (additive/mixed forms survive constraint 5). Schur + homothety + Lemma 8 make Θ and the spectral data independent coordinates, and C(Θ) is the extension-independent symmetric mode, so δ₀ never reaches it. But independent coordinates do not by themselves forbid a joint cross-term h(Θ, n); that needs the commutant theorem A_obs = A_Θ ⊗ A_spec, the open target (candidate closure: the-mirror.md character ceiling + a bridge lemma, in the [Proof](#proof-the-schur-separation)). Eigenvalue-side conditions: parity-preserving cone, δ₀/R > 2/e (Friedrichs), narrow band W ≤ πR/2. See [Proof](#proof-the-schur-separation). |
| Phase operator C(Θ) = 2sin²(πΘ) | DERIVED (family) + SELECTED (member) | The anti-periodic BC forces the sinusoidal family 2sin²((2m+1)πΘ); background symmetry (isotropy + orthogonality) selects the first-positive member m = 0. One operator across sectors: cosmology samples a single well, the mass sector samples Kostant exponent sets. |
| Integer-depth hierarchy (√Ω)^(−n) | DERIVED (units + exact homothety) | Units fix the admissible dimensional form and leave a free dimensionless function of R/ℓ_P; they do not fix the power. Exact homothety covariance at definite weight n does: $`f(\lambda x) = \lambda^{-n} f(x)`$ with $`x = 1`$ gives $`f(x) = C x^{-n}`$. Definite weight n is an admissibility condition on the class, not a theorem. |
| Coupling exponent rule: 1/\|grid\| given an assigned grid | ESTABLISHED as the framework's rule, not forced | Given a grid $`D \in \{60, 120\}`$ the ladder supplies the exponent $`1/D`$; the convergent paths and Lemma 8 support that rule for α_EM, and the representation-theoretic route below is the live attempt to force it. Two things sit outside this row: **which** grid a coupling occupies is a separate motivated assignment, and the numerical coupling claims keep the statuses their home page gives them. In the sibling vocabularies this same state is [fine-structure](../../../../spectrum/files/fine-structure.md) §III stage 5 "Provisional" and [claim-ledger](claim-ledger.md) row 5b "chosen, audited (provisional)"; the words differ, the epistemic state does not. Units stay silent here, since the couplings are dimensionless, so the ladder rule supplies the exponent that dimensions cannot. |
| α_W twist, cos(π/10) | MOTIVATED | The one injected multiplicative factor. The number is a computed invariant, the spin lift of the Levi-Civita holonomy around the shortest closed geodesic (the π/5 gluing twist, halved by the spin double cover); why it multiplies the coupling is the open link ([plato-twist](plato-twist.md)). |
| Self-adjoint extension | OPEN | Friedrichs keeps the zero mode as the m_h = 0 background. The selection rule is pending, via the smoothed-cone limit in the companion eigenvalue paper. |

The two genuinely open mechanisms, the α_W twist and the extension selection, are off the form: neither touches C(Θ) nor the separation question (which is the commutant theorem, below). (The deflation that came with the integer row, "61 orders from topology" is units, is in the closing Notes.)

---

**Note on calibration vs form.** The engine file writes the scaling law with $`\approx`$, reflecting that the kinematic identification of $`\Omega`$ with a physical quantity (e.g., $`\Omega_H = (c/(H\ell_P))^2`$ for edge modes) is approximate: the hierarchy normalization is fixed by calibrating through one measured anchor per sector ($`H_0`$ for edge modes, measured $`\Lambda`$ for surface and space modes, the mass-sector normalization for fermions).

The surface radius $`R`$ enters as the geometric parameter in the first positive eigenvalue $`\lambda = 2/R^2`$, and it is not yet fixed independently. The reason is structural, and it is the same reason the Yang-Mills gaps cannot fix it. Every observable is the single product $`C(\Theta)\cdot(\sqrt{\Omega})^{-n}`$, so one observable gives one equation, and $`R`$ reads out only as $`R`$-given-the-assumed-<i>C</i>. $`R`$ separates only when two observables share it at different powers. Same-power families return $`R`$-free ratios and nothing more: the Yang-Mills gaps live at $`1/R^2`$, $`\Lambda`$ lives at $`1/R^2`$, and within each the scale divides out. The mass spectrum is the one family carrying different powers, through the McKay elevator $`(\sqrt{\Omega_\Lambda})^{\,\mathrm{dist}/30}`$: the electron and muon sit at different McKay distances, so the same $`R`$ appears at two exponents, two equations, $`R`$ overdetermined. That is the route from calibration to an independent $`R`$ cross-read. The mass-spectrum inversion has since been executed ([r-from-mass-spectrum](r-from-mass-spectrum.md)); converting that $`R`$ to $`\Lambda_\text{ref}`$ is conditional on the reference normalization, and identifying it with the physical $`\Lambda`$ remains the Interface question.

The uniqueness question addressed here is about the *functional form* $`C(\Theta) \times g(\Omega, n)`$, separate from calibration.

---

## The Precedent: Gleason's Theorem

Gleason (1957) proved that on a Hilbert space of dimension ≥ 3, the only probability measure consistent with the lattice of projections is the Born rule: p = |⟨ψ|φ⟩|². The theorem doesn't derive Born from dynamics. It shows Born is the unique measure compatible with the structure.

The MIT analog: show that C(Θ) × (√Ω)⁻ⁿ is the unique sampling rule compatible with the bounded, closed topology of S¹ = ∂M ↪ S³, ∂S³ = ∅.

The precedent is exact for one piece only. C(Θ) is a normalized mode intensity (∫₀¹ C dΘ = 1), so a Gleason-type measure-uniqueness statement is the right tool there. The hierarchy (√Ω)⁻ⁿ is dimensional analysis (Buckingham π), not a measure; the factored form is a separation-of-variables result (the Schur separation, proved below). The three rows are three different rigidity claims of three different types, and only the phase operator is Gleason-shaped; the analogy is motivation for that one piece, not scaffolding for the whole. This note keeps them separate rather than letting one banner blur the kinds of argument or lend the open separation the standing of a measure theorem.

---

## The Constraints and What They Eliminate

| # | Constraint | Source | What it eliminates |
|---|-----------|--------|-------------------|
| 1 | Anti-periodic BC: ψ(y+L) = -ψ(y) | Möbius non-orientability (AXIOM) | Non-eigenmode primitive profiles. The anti-periodic eigenbasis of the boundary operator is the half-integer sinusoidal tower 2sin²((2m+1)πΘ); no polynomial, exponential, or rational alternative survives. The single m = 0 profile follows only after the Step 3 background selection, not from the BC alone. |
| 2 | Bounded domain: ∂S³ = ∅ | Poincaré (THEOREM) | Any hierarchy that fails to terminate. Ω is finite. The dilution is a function of a finite ratio, not an asymptotic series. |
| 3 | Discrete 120-domain: \|2I\| = 120 | S³ ≅ SU(2) (S³ itself forced by Poincaré), so finite quotients are S³/Γ, Γ ⊂ SU(2) finite (ADE, THEOREM). The selection rule, not S³ alone, forces Γ = 2I: input-minimization drops the open families (cyclic, binary dihedral, each parameterized by n); among the closed exceptional (2T, 2O, 2I) terminality takes the largest; and 2I is the unique *perfect* subgroup, the one carrying the 9× Galois coexact gap ([coexact-gap.md](../../bedrock/files/coexact-gap.md)) that the fermion generations require. So the decisive leg is a framework requirement plus a uniqueness theorem, not minimality, and \|2I\| = 120 is forced given the rule. | Continuous sampling rules and non-terminal finite-quotient grids. Phase positions are quantized to multiples of 1/120. |
| 4 | Self-dual point at √Ω | IR↔UV fixed point on bounded domain (DERIVED); the observer identification is interpretive (open) | Any other normalization point. The geometric midpoint is unique: x = Ω/x has one positive solution. Calling it the observer's scale is a physical postulate, not derived here. |
| 5 | Dimensionless output | A/Aₚ is a ratio | Leftover units only. A dimensionless output removes dimensionful candidates; it does NOT force a multiplicative split. Additive and mixed dimensionless forms (C + Ω⁻ⁿ, or C·Ω⁻ⁿ + h(Θ, Ω)) all survive this constraint. The factorization is not delivered here; it comes, if at all, from constraint 6. |
| 6 | Factorization into position and depth | Schur decoupling: Lemma 8 gives Θ ⊥ s; the link to Θ ⊥ (Ω, n) is argued, commutant theorem pending | This is the *only* source of the factored form (constraint 5 does not supply it). The homothety reduction makes (Ω, n) spectral-block data and Θ the lone positional coordinate ([Proof](#proof-the-schur-separation)); separability then needs the observable algebra to factor (the commutant theorem), which Schur and Lemma 8 motivate but do not yet prove. |

*Carried (deferred): the 2I selection above reads as a framework requirement (the fermion generations need the 9× Galois gap) plus coexact uniqueness (2I is the only perfect subgroup of SU(2)). Turning that into a formal physical-selection theorem (requirement ⇒ unique Γ) is open and not attempted here.*

---

## The Argument Shape

**Step 1:** Establish the space of candidate measurement rules.

Any rule maps (phase position Θ, manifold depth n, hierarchy Ω) to a dimensionless observable ratio. The output space is ℝ⁺. The input space is {Θ ∈ k/120} × {n ∈ ℤ or ℤ/2} × {Ω ∈ ℝ⁺, finite}.

**Step 2:** Constraint 5 narrows the output but does not factor it. A dimensionless output from dimensionless inputs need not be a product: $`f(\Theta) + g(\Omega, n)`$ and $`f(\Theta)g(\Omega, n) + h(\Theta, \Omega)`$ are equally dimensionless. The factored form

```math
\frac{A}{A_P} = f(\Theta) \cdot g(\Omega, n)
```

is supplied only by constraint 6 (Schur decoupling), and only if Θ ⊥ s extends to Θ ⊥ (Ω, n). The homothety reduction (below) delivers the independence of the coordinates, but independence is not separability: the no-cross-term step needs the commutant theorem, so at this step the factorization is a well-supported target, not a closed result.

**Step 3:** Apply constraint 1. f(Θ) satisfies the anti-periodic BC, whose eigenfunctions are trigonometric: the BC kills every polynomial, exponential, or rational candidate and admits the tower 2sin²((2m+1)πΘ). The constant zero mode is the extension-dependent background (the spatial-eigenvalue ground, distinct from the temporal harmonic ground of the cosmic wave) and carries no phase structure. The BC fixes the family but not the member; the member is selected physically. For background observables, isotropy and orthogonality exclude the higher harmonics, the same conditions that fix the cosmic background wave, leaving the lowest nonconstant mode, the first-positive eigenmode at 2/R², whose intensity is 2sin²(πΘ). So f(Θ) = C(Θ) = 2sin²(πΘ) is the first-positive-mode intensity, not the constant zero mode. This is one operator read at different positions: cosmology samples a single well, the mass sector samples Kostant exponent sets on the same mode. Two inputs enter here that the BC alone does not give: the harmonic selection (isotropy + orthogonality, for background observables) and the normalization (∫₀¹ C dΘ = 1 fixes the leading 2). Both are selection principles and should be named, not absorbed into "the BC forces it."

**Step 4:** Apply constraints 2 and 4. g(Ω, n) encodes dilution from Planck to observation on a bounded domain. Ω is the hierarchy ratio, finite by constraint 2; the self-dual point sits at √Ω by constraint 4 (its identification with the observer is the physical reading); n counts depth. Step 5 fixes the function.

**Step 5, resolved for integer depth.** Read n as the length-dimension of the observable. Λ is 1/length² (n = 2), H₀ and a₀ are 1/length (n = 1).

*What units give, and what they do not.* Units fix the admissible dimensional form: an observable normalized to its Planck value is $`(\ell_P/R)^n`$ times a dimensionless function of the one available ratio,

```math
\frac{A}{A_P} = (\sqrt{\Omega})^{-n} \cdot F(\sqrt{\Omega}).
```

Units do not fix $`F`$. Buckingham-π supplies the dimensional prefactor and leaves the dimensionless function free, which is the standard situation once a dimensionless ratio is available at all. Concretely $`(\sqrt{\Omega})^{-n}\,(1 + \epsilon \ln \sqrt{\Omega})`$ is dimensionally identical and survives constraints 2, 4 and 5. So the pure power is not a units result, and the earlier reading of this row as "form and base both follow from dimensions" quietly used the stronger premise that the observable's natural scale is exactly $`R^{-n}`$. That premise is homogeneity, not dimensional analysis.

*What fixes the power.* Exact homothety covariance, which Step B below already establishes on the spectral side: under $`R \mapsto \lambda R`$ the Hodge Laplacian scales as $`R^{-2}`$ with the unit-radius eigenspaces R-independent. An admissible observable of definite weight n satisfies $`A(\lambda R) = \lambda^{-n} A(R)`$, so with $`x = R/\ell_P`$ its normalized function obeys

```math
f(\lambda x) = \lambda^{-n} f(x) \quad \text{for all } \lambda, x > 0.
```

Setting $`x = 1`$ gives $`f(\lambda) = f(1)\,\lambda^{-n}`$ directly, hence $`f(x) = C x^{-n}`$ and $`A/A_P \propto (\sqrt{\Omega})^{-n}`$. No regularity assumption enters: the one-point substitution does the whole job, so none of the pathological solutions of the unconstrained Cauchy equation arise. The log correction dies here rather than at the units step, because rescaling generates an extra $`\epsilon \ln \lambda`$ that exact covariance forbids.

*Definite weight n is an admissibility condition, not a theorem.* The rigidity holds within the homogeneous weight-n sector, not over every conceivable observable. A non-homogeneous functional of the spectral weights, say $`\hat a(1)/R^2 + \hat a(2)^2/R^4`$, carries no single n and sits outside the statement. Dimensional analysis does not forbid such sums; the weight condition excludes them, and saying so keeps the scope of the claim visible rather than letting units appear to do more than they can.

Constraint 2 keeps Ω finite so the ratio is well-defined, and constraint 4 places the self-dual point at R/ℓ_P (read as the observer's scale by physical postulate), the same number the dimensions deliver. This closes the integer-depth case on Step B's homothety, without needing the commutant theorem.

**Scope: one scale or two.** The "R is the only scale" reading holds for surface and space modes, which dilute from the geometric curvature radius R via Ω_Λ = (R/ℓ_P)². Edge modes do not: they reference the kinematic horizon, Ω_H = (c/Hℓ_P)², so their base is c/H, not the geometric R. The two coincide only through Ω_H ≈ Ω_Λ at the present epoch, which the framework records as an observed coincidence, not a derived identity (see [calibration-structure.md](calibration-structure.md)). So units force the *form* (√Ω)⁻ⁿ in every sector, but the *identification* √Ω = R/ℓ_P is a surface/space statement; for edge modes √Ω = c/(Hℓ_P) is a separate anchor. Deriving Ω_H = Ω_Λ would collapse the two and turn Λ (n = 2) and H₀ (n = 1) into a second route to R, alongside the mass sector.

**Step 5, the coupling exponents.** A dimensionless coupling has length-dimension 0, so dimensions fix no Ω dependence. The exponent the couplings do carry, 1/60 for EM and 1/120 for the strong and weak forces, comes from the grid ladder selection rule: the carrier character sets the phase grid, the confinement target sets the exponent grid, and the exponent is one cell of that grid, 1/\|grid\|. That rule is the framework's, established as a rule but not forced; the representation-theoretic route below is the live attempt to derive it. Separately, which grid a given coupling occupies is the motivated ladder assignment. So the exponents are fixed once those two framework rules are accepted, rather than fitted to the couplings they reproduce, which is what "supplied, not open" is claiming and all it is claiming. What this paper's standard adds is lifting the ladder rule from established to forced, which is the live target for the representation-theoretic route below.

---

## Audit: n as length-dimension vs manifold index

Step 5 reads n as the observable's length-dimension; the engine's selection rule (framework/README.md, "Manifold Index") reads n as the manifold the mode lives on (edge / surface / space). These are two different rules. They agree exactly on the dimensionful dilution sector and diverge everywhere else, so the manifold rule is not redundant with dimensional analysis: it is needed for the rows units cannot reach.

| Observable | length-dimension | manifold index n | agree? | governing rule |
|---|---|---|---|---|
| H₀ | −1 (rate, via c) | 1 (edge) | yes | units = manifold |
| a₀ | −1 (acceleration, via c) | 1 (edge) | yes | units = manifold |
| Λ | −2 | 2 (surface) | yes | units = manifold |
| null dark-matter detection | −3 (number density) | 3 (space) | yes, if the observable is a 1/length³ density | units = manifold; observable to be pinned |
| G | nonzero (defines ℓ_P) | 0 (Planck floor) | NO | Planck anchor: A/A_P = 1 by construction, not by length-dimension |
| Λ_ref/Λ_top = 3/2 | 0 (ratio) | 3/2 (3 Gauss/Ricci × 1/2 de Sitter) | NO | 3/2 vacuum-reference conversion (3 Gauss/Ricci lift, 1/2 de Sitter vacuum), not a dilution exponent |
| α, α_s, α_W | 0 | fractional (1/60, 1/120) | NO | grid ladder, not units |

**Verdict.** n_(length-dim) = n_(manifold) on the dimensionful dilution observables (edge + surface + space), and only there. Three rows sit outside the identity: G is the Planck-defining anchor (ratio 1, n = 0 by construction, not because its length-dimension is 0); the 3/2 row is a vacuum-reference conversion factor (3 from the Gauss/Ricci lift, 1/2 imported from the de Sitter vacuum normalization), not a dilution; the couplings carry length-dimension 0 yet pick up fractional exponents from the ladder. The Step 5 argument, units for the dimensional form plus exact homothety for the power, therefore legitimately closes the dilution sector and only the dilution sector; the manifold and ladder rules carry the rest. This is consistent with the note's own split between Step 5 (integer depth) and the coupling exponents; the table adds G and the 3/2 conversion as the two further exceptions.

---

## Proof: the Schur Separation

*Argues constraint 6: within the observable class, the form separates. Two gaps are kept explicit. The class is a premise, not shown to exhaust the physical observables. And the no-cross-term step needs the commutant theorem, stated at Step C as the open target; what is established below is the weaker statement that Θ and the spectral data are independent coordinates.*

The factored form was the one structural row left open. Dimensionlessness does not separate Θ from (Ω, n), and Lemma 8 separates Θ only from the spectral parameter s. The gap is the step from Θ ⊥ s to Θ ⊥ (Ω, n). It closes once (Ω, n) is recognized as spectral-block data: the metric scale R entering the eigenvalues, nothing more.

**Proposition (within the observable class; conditional on the commutant theorem).** Let A be an admissible observable: a quantity built SU(2)-equivariantly from the Hodge-Laplace spectral data of S³/2I and the first-positive anti-periodic mode on the Möbius boundary S¹ (narrow band, W ≤ πR/2), under a parity-preserving self-adjoint extension with δ₀/R > 2/e (the Friedrichs default included). Then, *provided the admissible observable algebra factors as A_obs = A_Θ ⊗ A_spec* (Step C, the open commutant theorem), A/A_P = C(Θ) · g(Ω, n) with no cross-term, where C(Θ) = 2sin²(πΘ) is the boundary-phase factor and g(Ω, n) the scale-and-depth factor.

**Step A, positional reduction.** By Peter-Weyl, sections of a natural bundle split into SU(2)-isotypic blocks V_l; by Schur any admissible operator is scalar a(l) on each block (the spectral-zeta reduction, the-mirror Step 2). On the bulk S³/2I the right-SU(2) action is transitive, so no continuous bulk position survives (the S³/2I half of Lemma 8: the twisted heat kernel is constant on each fiber diagonal). The only continuous positional coordinate left in A is the Möbius boundary phase Θ.

**Step B, scale reduction.** The round metric of radius R is R² times the unit metric, so the Hodge Laplacian scales as R⁻² and a_R(l) = â(l)/R², with the unit-radius eigenspaces and their internal bases R-independent. The whole (Ω, n) dependence is therefore carried by the scalar weights a_R(l): Ω = (R/ℓ_P)² is their common scale, and n is the homothety weight, the power of R the observable carries (its length-dimension). On the spectral zeta this reads as Z(s) ↦ λ²ˢ Z(s) under R ↦ λR: a pure s-power, staying inside the spectral block, never touching the eigenspace basis where Θ lives. This is the precise sense in which the depth index rides the spectral block.

**Step C, separation (the open step).** Extract the homothety weight: A/A_P = (√Ω)⁻ⁿ · K, where K depends on Θ (positional) and on R-invariant spectral data (eigenvalue ratios, multiplicities, the bundle label n). Lemma 8 gives Θ ⊥ s for the zeta parameter, and for this equivariant family the eigenvalue-multiplicity data are fixed by the 2I character table and the Peter-Weyl decomposition (no isospectral freedom is invoked, and no claim that the spectrum fixes the geometry), so they are Θ-blind. That makes Θ and the spectral data **independent coordinates**.

Independence is necessary but not sufficient. A joint function K = C(Θ)·F(n) + h(Θ, n) is consistent with independent coordinates: nothing so far excludes the cross-term h. Excluding it is an **algebra** statement, that the admissible observable algebra factors,

```math
\mathcal{A}_\text{obs} = \mathcal{A}_\Theta \otimes \mathcal{A}_\text{spec}, \qquad \text{equivalently } \mathrm{Comm}_{SU(2)}(\mathcal{H}_\Theta \otimes \mathcal{H}_{2I}) = \mathcal{A}_\Theta \otimes \mathcal{A}_{2I},
```

with the commutant containing no operator of the form h(Θ, λ_l). Schur (scalar on each block) and Lemma 8 (no natural Θ-spectral map) motivate this factorization but do not prove it. **This commutant theorem is the open target.** A candidate closure has since appeared from the spectral side: [the-mirror.md](../../../../spectrum/files/the-mirror.md) proves the 2I character algebra is the *closed* ceiling for basis-independent bulk content (Props 1-3, Lemma 7), and Lemma 8 puts Θ outside it. That is the algebra-completeness this step lacked; Schur + homothety gave only coordinate-independence. A bridge lemma over the observable class, the first-positive boundary mode adjoined to the mirror's Definition-2 spectral constructions, would then forbid any natural h(Θ, λ) and close the separation, pending a check that the two classes compose as stated. This is a candidate, not a closure. Granted it, K splits as C(Θ)·F(n) and

```math
\frac{A}{A_P} = C(\Theta) \cdot [F(n)(\sqrt{\Omega})^{-n}] = C(\Theta) \cdot g(\Omega, n). \qquad \blacksquare \text{ (modulo the commutant theorem)}
```

**What units cannot do, the algebra must.** Constraint 5 leaves h(Θ, Ω) alive because it is dimensionless; units and Lemma 8 deliver only the setup, that Θ and the spectral data are independent coordinates. Killing the cross-term is the algebra step (the commutant theorem), not a units step, which is why the separation cannot be settled at Step 2 and is not settled by independence alone.

**Scope: dimensionful observables and couplings.** Steps B and C extract n as a length-dimension, the dimensionful case (H₀, a₀, Λ). Dimensionless couplings have n = 0, so the homothety weight is trivial and their Ω-dependence is not a length-dimension; it is the grid exponent 1/\|grid\| from the ladder rule. But that exponent is 2I representation data (the grid is the \|I\| = 60 or \|2I\| = 120 image), which is spectral-block data, and C(Θ) at the coupling wells is the same boundary phase operator. So the separation argument covers both sectors, the spectral block supplying a fractional weight for couplings: granted the commutant theorem, K splits as C(Θ) · F with F carrying Ω^(−1/\|grid\|). Only the source of the exponent differs (length-dimension for dimensionful observables, the grid for couplings); both live in the spectral block and are Θ-blind by the same block-independence argument, and the same commutant theorem closes both.

**The covariance assumption, discharged by the eigenvalue paper.** (This is the *covariance* assumption, distinct from the commutant theorem of Step C, which stays open.) Step B needs the boundary profile sin(πΘ) to be R-independent. [first-eigenvalue.md](../../bedrock/files/first-eigenvalue.md) supplies this directly, and answers the ε/R question two ways.

First, the renormalization length δ₀ (the ε of the smoothed cone) enters the spectrum only through the dimensionless ratio δ₀/R: the bridging secular condition is G(λ) = ln(δ₀/2R) with G a function of the dimensionless degree ν alone (§4.4), and the robustness threshold is δ₀ > 2R/e (Prop 4.4), both functions of δ₀/R. No absolute length enters the secular data. The one absolute-length object, the bound state λ_b ≈ −4e⁻²ᵞ/δ₀², is the antisymmetric ground state, which §7 names an extension artifact, not an intrinsic invariant.

Second, and decisively, C(Θ) does not depend on δ₀ at all. It is built from the first-positive mode, which is the *symmetric* zonal mode sin(y/R) = sin(πΘ) at 2/R² (§4.2), and the symmetric tower is shared by the parity-preserving extensions (Friedrichs and the bridging family); δ₀ deforms only the *antisymmetric* sector (Prop 4.4, Thm 5.1). So for these extensions the covariance of the phase profile is a theorem, not an assumption: sin(πΘ) is the explicit Legendre mode, manifestly R-independent, with eigenvalue 2/R² scaling as 1/R². Three conditions bound the discharge, and all are named rather than assumed: (i) the cone condition is parity-preserving, since a parity-mixing (Robin-type) condition *can* deform the symmetric subsector (Thm 5.1 claims the symmetric tower's robustness only for Friedrichs and bridging, and its proof notes a general cone condition is not claimed robust); (ii) δ₀/R > 2/e, below which the first-positive mode becomes the δ₀-dependent antisymmetric root and the profile would change; and (iii) the narrow band W ≤ πR/2, past which the first-positive level crosses to the width-dependent odd transverse branch |cos(y/R)|^α₀ sin(πw/2W) (Thm 1.2) and the profile is no longer sin(πΘ). The first two are scale-invariant extension conditions; Friedrichs, the framework's default, is parity-preserving and sits at the δ₀ → ∞ end, so it satisfies both automatically. The third is geometric: the framework takes the cosmic band as narrow, the same W ≤ πR/2 the [cosmological constant page](../../../../cosmos/files/cosmological-constant.md) records as a physical input rather than a derived fact.

**This decouples the factorization from the extension selection.** The factorization does not wait on which extension is chosen: C(Θ) is the same symmetric mode across the whole admissible regime, and the extension question governs only the ground state, which the factorization never samples. The separation's one open step is the commutant theorem (Step C), not the extension.

---

## What the Residual Requires

The integer-depth rigidity is units plus exact homothety, and the coupling exponents come from the ladder rule, so the heavy approaches below come off both. They are kept for the record, and because the representation-theoretic row is the candidate for lifting the ladder rule from established to forced.

| Approach | Idea | Status |
|----------|------|--------|
| Volume scaling | The ratio of n-dimensional volumes at scale √Ω vs scale Ω is (√Ω)⁻ⁿ. | RETIRED. Units settle the integer case. |
| Spectral | Eigenvalue spacing at depth n scales as Ω⁻ⁿ/². | RETIRED for the integer case. |
| Information-theoretic | The self-dual point at √Ω carries ½ log Ω bits per dimension; depth n gives n × ½ log Ω. | RETIRED for the integer case. |
| Representation-theoretic | The Peter-Weyl decomposition on S³/2I organizes modes by spin j; Casimir scaling under the 2I quotient sets the amplitude. | LIVE. Candidate route to lift the ladder rule from established to forced, by deriving 1/\|grid\| from the Casimir under the quotient. |
| Selberg trace formula | Eigenvalue sums equal geodesic sums, with geodesics fixed by the 9 conjugacy classes of 2I. | RETIRED for the integer case. Possibly relevant to the representation-theoretic route. See note below. |

The two open mechanisms sit outside this table. The α_W twist needs a derivation of why its spin-lifted holonomy enters the coupling as a multiplicative factor. The self-adjoint extension needs a selection rule, expected from the smoothed-cone limit.

---

## What This Paper Would Establish

Within the spectral-boundary observable class, the separated form is the unique measurement rule compatible with S¹ = ∂M ↪ S³, ∂S³ = ∅, with anti-periodic BC and the 120-domain. Two pieces reach that bar outright: the phase operator (anti-periodic family forced, first-positive member selected by isotropy + orthogonality, normalization named) and the integer-depth hierarchy (units for the dimensional form, exact homothety at definite weight for the power, on the dilution sector); for these the audit verdict moves from DECLARED to AXIOM (forced), the second within its weight-n admissibility condition. The factored structure reaches it within the class and *modulo the commutant theorem*: the separation is argued (Schur + homothety + Lemma 8), its no-cross-term step the open target. Downstream that rides the phase and hierarchy factors inherits the upgrade; downstream of the factorization inherits its conditional status.

What stays as work on the form: the commutant theorem A_obs = A_Θ ⊗ A_spec (closes the separation; candidate route via the-mirror.md character ceiling + a bridge lemma, see [Proof](#proof-the-schur-separation)), and whether the observable class exhausts the physical observables (the premise behind "within the class"). Off the form: the α_W twist mechanism and the extension selection, both stated precisely enough to attack directly. The well assignments, manifold indices, and grid types remain the next layer, the traffic rules on the bridge, with "why 13 is the exponent floor" the load-bearing item there. Lifting the ladder rule from established to forced belongs to that layer too.

---

## Note: The Selberg Merge

The spectral approach and the representation-theoretic approach may not be independent. The Selberg trace formula equates sums over eigenvalues to sums over geodesics, with geodesics fixed by conjugacy classes of the fundamental group. On S³/2I the fundamental group is 2I, with 9 conjugacy classes and geodesic lengths fixed by group structure. Peter-Weyl gives the eigenvalues; Selberg locks them to the geodesic lengths.

This was flagged as the unifying rigidity for the hierarchy. With the integer hierarchy settled by units plus exact homothety and the coupling exponents supplied by the ladder rule, the formula's possible role narrows to the representation-theoretic route, if the finite geodesic-length set turns out to fix the 1/\|grid\| scaling. That connection is unproven and speculative.

**Source:** The Selberg connection was flagged during review of Schepis, *Observer-Resonance Theory* (2026), Ch. F §3.3-3.4. Schepis identifies the Selberg trace formula as the structural analog of the Euler product for bounded manifolds and cites Connes' spectral triples matching zeta zeros at 10⁻⁵⁵ precision using primes ≤ 13. He does not apply the formula to any specific manifold. The application to S³/2I is new.

---

## A Historical Consequence: the original propagator null

On the pre-correction mass table the path-product propagator search returned no parameter-free fix, and that candidate also sat outside the separated depth-only form argued here, which made the negative unsurprising. Both halves of that reading have since weakened. The corrected torsions changed the residual landscape and formally reopened the route ([mckay-propagator-correction](mckay-propagator-correction.md)): the two remaining large residuals are d +0.51 and τ +0.44, both overshoots at Galois vacua, so the opposite-directions signature the old argument leaned on does not transfer. And the separated form is argued here rather than proved, since the factorization still awaits the commutant theorem. The old negative therefore stands as a historical result on the pre-correction table, not as a theorem that propagator corrections must fail.

---

## Relationship to Existing Papers

| Paper | What it establishes | What this paper adds |
|-------|--------------------|--------------------|
| Sector A (eigenvalue) | First positive eigenvalue 2/R² on Möbius in S³; the ground state is extension-dependent (Friedrichs: the discontinuous zero mode; bridging: a negative defect state) | That paper gives the eigenvalue. This paper argues the rule that reads it is unique within the observable class (modulo the commutant theorem). |
| Lemma 8 | Θ decouples from the spectral parameter s | The same Schur mechanism feeds constraint 6: the homothety reduction connects the depth index to the spectral block (argued here; the closing step is the commutant theorem), extending Θ ⊥ s toward Θ ⊥ (Ω, n). |
| Mass spectrum | Fermion masses via torsion × C_geom × McKay elevator | Supplies the only route to an independent R (electron and muon at different McKay distances), and hosts the R-determination open item. |
| Gauge ladder | Coupling exponents from carrier and confinement character | Supplies the 1/60 and 1/120 exponents. This paper would lift that rule from established to forced. |
| Scaling Law (this paper) | Separated form of the sampling rule (within the class; commutant theorem pending) | Completes the triad: eigenvalue, boundary, measurement. |

---

## Notes

The strongest version of this result would show the scaling law is the ONLY measurement rule within the class, not merely the simplest. Two of its pieces reach that bar outright: the phase operator and the integer hierarchy, by the anti-periodic BC (plus the member selection) and by units together with exact homothety. The factored structure is argued there (the Schur separation), not closed: the commutant theorem is the remaining step, and dimensionlessness does not stand in for it. Simplicity never entered.

The honest deflation that came with closing the integer hierarchy: the apparent miracle of "many orders of magnitude from topology" is units. R/ℓ_P is a calibrated ratio, and raising it to the observable's dimension is dimensional analysis plus the homothety weight. The genuine content sits in C(Θ), and the coupling exponents sit in the ladder rule that units do not reach. Naming this plainly is what lets the open mechanisms stand out as the real work.

---

*"The topology leaves no room for anything else" is true for the phase operator and the integer-depth hierarchy, argued within the observable class for the factorization (the Schur separation, with the commutant theorem the open step), the current framework rule for the coupling exponents, established as a rule but not forced in its derivation and conditional on the motivated grid assignment, and a precise open question for the α_W twist and the extension selection.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
