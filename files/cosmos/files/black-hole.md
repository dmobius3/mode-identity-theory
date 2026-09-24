<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🎸 Black Holes

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/black%20holes%20banner.png?raw=true" width="100%" alt="Black Holes">

Where Θ hits the wall, and Ω may collapse with it. *A working supplement to Mode Identity Theory.*

**Status:** Sections I-V derived or motivated from the scaling law, with one central exception flagged up front: $`\Theta \to 0`$ and $`C(\Theta) \to 0`$ are DERIVED consequences of the near-horizon mapping (§VIII.1); $`\Omega_\Psi \to 0`$ is CONJECTURED, not derived, its dependence on an unspecified observer's proper time is open (§II); and the scaling law's actual joint limit, $`C(\Theta)\cdot\Omega_\Psi^{-n/2}`$, is an unresolved $`0\times\infty`$ until $`\Omega_\Psi(\Theta)`$ is known (§II; frozen as its own question in [Ω_Ψ derivation](../../framework/files/working/files/omega-h-derivation.md)). "Black Double Zero" names the conjectured mechanism, not an established result. Section II.A connects to spectral geometry results from the RH program. The $`\Phi \to \Theta`$ mapping (§VIII.1) derives the near-horizon exponent; the coefficient and the global form beyond it are the minimal extension, a choice, not a further derivation. Hawking temperature: eigenfunction-gradient $`1/M`$ dependence derived under that same minimal choice, temperature normalization and thermal character inherited (§V, §VIII.4); minimum mass is a conditional estimate under the minimal mapping and an imposed Planck-length cutoff, not a derived physical bound (§VIII.2); area entropy is motivated but the 1/4 factor remains open (§III). The domain is topologically closed (§VI). $`\Lambda`$ and the horizon are opposite critical points of $`C(\Theta)`$ (§VIII.6); whether either dynamically attracts $`\Theta`$ is open pending an evolution law. The horizon-exterior mapping does not extend to $`r<r_s`$: the interior and the classical singularity are not modeled here (§I, §VII).

---

## I. What is it?

A Black Hole, in this framework, is presently a statement about the *exterior* geometry only: a region where enough wave content on the Möbius surface is enclosed that the phase position $`\Theta`$ reaches the boundary of its domain, driving the sampling amplitude $`C(\Theta) = 2\sin^2(\pi\Theta)`$ to zero as $`r \to r_s`$. That much, $`\Theta \to 0`$ and $`C(\Theta) \to 0`$ at the horizon, is DERIVED from the near-horizon mapping (§VIII.1), specifically for the exterior stationary observer congruence that mapping is built on (it is paired with the Schwarzschild lapse, §VIII.1). A freely falling observer crossing the horizon is not shown to experience any such vanishing, and in GR remains locally regular there; "observation ceases" throughout this page means the exterior stationary channel closes, not that observation ceases for every observer. A second, independent quantity, the local scale hierarchy $`\Omega_\Psi`$, is *conjectured* to collapse toward zero over the same approach; whether it does, for which observer's proper time, and how it relates to $`\Theta`$, is open (§II). Nothing here currently maps past the horizon: the interior and the classical singularity at $`r = 0`$ are not modeled by this construction (§VII).

General Relativity sits at the 3/2 conversion interface (the 3 a Gauss/Ricci lift, the 1/2 the de Sitter vacuum normalization), between the temporal edge ($`n = 1`$) and the Möbius surface ($`n = 2`$). That 3/2 coincides numerically with face over edge, $`Z_3/Z_2`$, the stabilizer orders of the icosahedron; the framework marks that identity open. At the horizon, GR is squeezed from one side that is derived and one that is conjectured: the surface mode it reads has vanished ($`\Theta`$ at its boundary, so $`C = 0`$, DERIVED), and the edge hierarchy it converts through is conjectured to collapse ($`\Omega_\Psi \to 0`$, OPEN). The wave persists through the node. MIT reads the information as unsampled rather than destroyed; whether it is recoverable is open (§IV).

| GR says | MIT says |
|---|---|
| Singularity ($`r = 0`$): geodesic incompleteness, curvature divergence | Not modeled: the $`\Phi \to \Theta`$ mapping requires $`C/C_0 = 1 - r_s/r \geq 0`$, impossible for $`r < r_s`$. Says nothing about the interior or $`r = 0`$. |
| Event horizon ($`r = r_s`$): point of no return | Radius where enclosed $`n = 2`$ content closes the exterior stationary sampling channel; $`\Theta \to 0`$, $`C \to 0`$ (DERIVED, §VIII.1, for that congruence specifically) |
| Information destroyed | Information unsampled at the horizon. Wave persists through the node. Whether the exterior evolution is unitary and information is recoverable is a separate, OPEN question (§IV). |
| Entropy scales with area | Surface ($`n = 2`$) is fundamental. Area scaling is motivated; the factor 1/4 is open. |

**On time specifically.** GR tells two stories depending on who is asked: time slows without limit for a distant observer watching infall, while an infalling observer's proper time continues normally past the horizon. What is established on the MIT side is narrower than "one story for every observer": $`\Theta \to 0`$ drives $`C(\Theta) \to 0`$ at the horizon, derived from the near-horizon mapping. The $`\Omega_\Psi`$ construction in §II is built on a proper-time derivative, and proper time is observer-dependent (static vs. infalling give different answers in GR); whether $`\Omega_\Psi`$'s collapse is well-defined independent of that choice is exactly the open question below, not yet settled.

---

## II. The Double Zero

The scaling law has two visible factors:

```math
A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}
```

$`C(\Theta)`$ is where on the mode spectrum. $`(\sqrt{\Omega})^{-n}`$ is which level of the hierarchy. Near the horizon, two things are claimed to happen at once, but they are not on equal footing:

| Quantity | Status | Character |
|---|---|---|
| $`\Theta \to 0`$ | DERIVED (§VIII.1) | Phase position reaches the domain boundary as $`r \to r_s`$ |
| $`C(\Theta) \to 0`$ | DERIVED, consequence of the above | Sampling amplitude vanishes: observation can no longer read the wave there |
| $`\Omega_\Psi \to 0`$ | CONJECTURED / OPEN | Proposed local-hierarchy collapse; observer-dependence and relation to $`\Theta`$ not established |

**Definition.** $`\Omega_\Psi \equiv (\ell_\text{phase}/\ell_P)^2`$, the local phase-gradient hierarchy, distinct from the cosmological rate ledger $`\Omega_H = (c/H\ell_P)^2`$ the [framework page](../../framework/README.md) uses and related to it by $`\Omega_\Psi/\Omega_H = (\Psi/S)^4`$, where $`\ell_\text{phase} = c/\kappa_\text{phase}`$ and $`\kappa_\text{phase} = |d\ln\Psi/d\tau|`$. Far from gravitating masses, the phase gradient is taken to relax to the global cosmological clock, giving $`\Omega_\Psi \approx \Omega_\Lambda \approx 10^{122}`$; that asymptotic normalization is a boundary hypothesis of this branch rather than an identity inherited from the cosmological ledger; that limit is well-defined because there is a preferred cosmological $`\tau`$. Near a horizon there is not: $`\tau`$ could mean a static exterior observer's proper time, a freely falling observer's proper time, an invariant norm of $`\nabla\ln\Psi`$, or a preferred MIT clock distinct from either GR family, and these are physically inequivalent choices. A static observer's proper time runs increasingly slow approaching $`r_s`$ (and no static observer exists at the horizon itself), which could drive $`\kappa_\text{phase}`$ to diverge and $`\ell_\text{phase}\to0`$ for that congruence specifically, while a freely falling observer's proper time is regular there and might not show the same collapse. Which congruence, if any, $`\Omega_\Psi`$ is built on is not yet specified. The claim "$`\Omega_\Psi\to0`$ at the horizon" is therefore a conjecture about a currently unstated observer choice, not a derived, observer-independent fact. This is frozen as its own question in [Ω_Ψ derivation](../../framework/files/working/files/omega-h-derivation.md).

Even granting $`\Omega_\Psi\to0`$ for some choice of observer, the scaling law does not thereby acquire a "double zero." $`C(\Theta)`$ enters directly and vanishes; $`\Omega_\Psi`$ enters as $`\Omega_\Psi^{-n/2}`$, an *inverse* power, which *diverges* as $`\Omega_\Psi\to0`$. The product is the indeterminate form $`0\times\infty`$, resolved only by the relative rate at which each limit is approached, i.e. by $`\Omega_\Psi(\Theta)`$, which is not presently derived. If $`\Omega_\Psi\sim\Theta^p`$ near the horizon, the scaling-law output goes as $`\Theta^{2-pn/2}`$: it vanishes, stays finite, or diverges depending on $`p`$ and $`n`$. Until $`p`$ is derived, the joint limit is open.

The phase operator $`C(\Theta) = 2\sin^2(\pi\Theta)`$ vanishes at the boundaries ($`\Theta = 0`$ and $`\Theta = 1`$). At these zero-crossings, the standing wave is there; observation cannot reach it. Think of a node on a guitar string: the string is still there, the wave passes through, the displacement at that point is zero. The position on the string ($`\Theta`$) identifies which node. The vanishing displacement ($`C`$) is what you measure.

The vanishing is quadratic: $`C(\Theta) \approx 2\pi^2\Theta^2`$ near $`\Theta = 0`$. The first derivative $`C'(0) = 0`$. The leading nonvanishing order is the curvature $`C''(0) = 4\pi^2`$. The logarithmic slope $`d\ln C / d\Theta = 2\pi\cot(\pi\Theta)`$ diverges as $`1/\Theta`$.

What is genuinely established: $`\Theta\to0`$ produces a geometrically selected zero of $`C`$ within this metric and twisted sector (§IV.A). What is not established: that this is a topological invariant immune to any perturbation preserving only the topology, or that a second, independent zero in $`\Omega_\Psi`$ joins it to produce a protected "double zero" in the scaling law itself. Both stronger claims are open; "double zero" is retained as the label for the conjectured mechanism this document is named for, not as an announcement that either has been shown.

### II.A The Spectral Mirror

The $`\Theta \to 0`$ zero of $`C`$ has an exact structural analog in the spectral geometry of $`S^3/2I`$; $`\Omega_\Psi`$'s conjectured, separate zero (§II) has no established analog here.

The twisted spectral zeta function $`Z_\sigma(s) = \sum_l N_l(\sigma)\lambda_l^{-s}`$ on the Poincaré homology sphere satisfies $`Z_\sigma(0) = 0`$ for every nontrivial twist $`\sigma`$. The scalar eigenvalues are $`\lambda_l = l(l+2) = (l+1)^2 - 1`$, and the curvature shift "-1" generates a Pochhammer expansion:

```math
Z_{0,\sigma}(s) = \sum_{k \geq 0} \frac{(s)_k}{k!} \cdot \widetilde{H}_k(s)
```

At $`s = 0`$, the Pochhammer symbol $`(0)_k = 0`$ for $`k \geq 1`$ eliminates every term with $`k \geq 1`$, leaving $`Z_{0,\sigma}(0) = \widetilde{H}_0(0)`$ exactly: the tower collapses to its single surviving term, it does not by itself force that survivor to vanish. The base fact, $`Z_\sigma(0) = 0`$ for every nontrivial twist, hence $`\widetilde H_0(0) = 0`$, is established in [The Mirror](../../spectrum/files/the-mirror.md) (Lemma 1, the identical Pochhammer construction on $`S^3/2I`$, via Dowker's cancellation formula), imported here, not independently re-derived in this page. Status: tower collapse DERIVED, directly from the Pochhammer symbol; survivor vanishing IMPORTED from that construction. This is a tower collapse plus an imported vanishing survivor, not one mechanism producing the zero on its own, and not two independent zeros.

| Scaling side ($`\Theta \to 0`$) | Spectral side ($`s \to 0`$) |
|---|---|
| $`\Theta \to 0`$ drives $`C(0) = 0`$ (DERIVED) | $`Z_\sigma(0) = 0`$ |
| $`\Omega_\Psi \to 0`$ conjectured to collapse hierarchy (OPEN, §II) | $`(s)_k = 0`$ for $`k \geq 1`$ collapses the Pochhammer tower to its $`k=0`$ survivor; that survivor must separately vanish for $`Z_\sigma(0)=0`$ |
| Parallel in structure, not a proven joint limit: $`\Theta \to 0`$ is derived, $`\Omega_\Psi \to 0`$ is conjectured | Tower collapse plus a vanishing survivor, one structure not two |
| Survivor: $`C(\Theta) \approx 2\pi^2\Theta^2`$ (quadratic in the position) | Survivor: $`Z'_\sigma(0) = \log T^2`$ (torsion) |
| The curvature of $`C`$ at the node | The derivative of $`Z`$ at the zero |
| Hawking radiation: residual sampling at the node | Torsion: L-function special values at the zero |

The physics lives in the first nonvanishing order at each zero. The $`\Theta \to 0`$ zero of $`C`$ is a spectral-geometric consequence of the selected eigenfunction within this fixed great-$`S^2`$ geometry and twisted sector (§IV.A); whether it survives perturbations that preserve only the topology, not this specific metric, is not established. The derivative at the zero carries the content.

**The zero is a filter.** At $`s = 0`$, the Pochhammer collapse kills everything except leading order. The $`E_8`$ McKay symmetries of $`S^3/2I`$ then kill 12 of 16 Dirichlet characters mod 60, leaving exactly four survivors encoding the structural constants of the manifold: $`\{\log 2, \log 3, \log 5, \log\varphi\}`$. The primes dividing $`|2I| = 120`$ and the golden ratio from the character field of $`2I`$. Away from $`s = 0`$, the Dirac operator's spectral zeta carries 28 to 32 of 32 characters. The zero selects. The interior floods.

These surviving primes are the stabilizer triple of the icosahedron: $`Z_2`$ (edge, order 2), $`Z_3`$ (face, order 3), $`Z_5`$ (vertex, order 5). In the companion mass spectrum analysis, the same triple assigns particle identity: $`Z_3`$ encodes color charge, $`Z_4`$ (the $`Z_2`$ lift to the double cover) encodes the domain size, and $`Z_5`$ encodes the electroweak interface through the Möbius twist. The horizon filter selects the same arithmetic that the stabilizer decomposition uses to distinguish quarks from leptons, fermions from bosons, and the three gauge forces from each other. The zero at the boundary strips everything except the identity mechanism.

This is the same mechanism by which the horizon is sharp: the sampling boundary is a geometrically selected node of $`C(\Theta)`$ (not established as topologically forced, §II), and only the leading order leaks through. On the spectral side, the "leakage" is the torsion. On the scaling side, the "leakage" is Hawking radiation. Both are residual signals at the first nonvanishing order of their respective zero.

**What this connection is.** It is a structural parallel between the scaling law (Tool 5) and the spectral geometry (Tool 3). Both the horizon and $`s = 0`$ are special points organized around a zero: on the scaling side, $`\Theta \to 0`$ (derived) with $`\Omega_\Psi \to 0`$ conjectured alongside it; on the spectral side, the Pochhammer collapse produces $`Z_\sigma(0) = 0`$ directly, one mechanism, not two independent zeros. In both cases the physics is carried by the derivative at that point. Both are filters: the zero kills everything except the essential structure.

**Three descriptions, two events, one pattern.** The scaling and eigenfunction zeros describe the same physical event ($`C = 2u_0^2`$). The spectral zero is a structurally parallel but independent event in a different parameter space ($`s`$, not $`\Theta`$), proved independent by Lemma 8. All three share the same mathematical structure: value vanishes, derivative carries content through.

| Domain | Value vanishes | Derivative survives |
|--------|---------------|-------------------|
| Scaling | $`C(\Theta) \to 0`$ (quadratic: $`C \approx 2\pi^2\Theta^2`$) | $`C''(0) = 4\pi^2`$ |
| Spectral | $`Z_\sigma(0) = 0`$ for nontrivial $`\sigma`$ | $`Z'_\sigma(0) = \log T^2`$ (torsion) |
| Eigenfunction | $`u_0(0) = 0`$ | $`u_0'(0) = 1/R`$ (slope through node) |

$`C=2u_0^2`$ means the scaling and eigenfunction descriptions are two representations of one geometrically selected node, not two zeros. The spectral zero is a structurally parallel, independent event in its own domain (§II.A above).

**What this connection is not.** It is not a derivation of Hawking radiation from spectral geometry, or of torsion from the scaling law. The $`\Phi \to \Theta`$ mapping (§VIII.1) is derived at leading order; the spectral-to-physical bridge (§VIII.5) remains open. The $`s \leftrightarrow \Theta`$ bridge is proved not to exist by Lemma 8 (The Mirror), established by four independent approaches on $`S^1`$ (heat kernel, theta function, Poisson summation, direct decomposition). The non-existence has two distinct mechanisms: on $`S^1`$, every eigenspace with anti-periodic BC is 2-dimensional (sin and cos), and the spectral zeta sees only eigenvalues and multiplicities, blind to the sin/cos choice that defines $`C(\Theta)`$; on $`S^3/2I`$, right-<i>SU(2)</i> homogeneity acts transitively, forcing the twisted heat kernel constant on each fiber diagonal so that continuous geometric position drops out structurally. The parallel is exact at the level of structure. The physical $`\Phi \to \Theta`$ mapping avoids the spectral obstruction: the gravitational potential provides the discrete localization that spectral geometry lacks, because mass at a specific location breaks the right-<i>SU(2)</i> isometry.

---

## III. Area Scaling

Bekenstein-Hawking entropy $`S \propto A`$ is motivated by surface primacy. The specific coefficient $`S = A/(4\ell_P^2)`$ is not yet derived.

| Step | Content | Status |
|---|---|---|
| 1 | The Möbius surface ($`n = 2`$) carries the boundary condition | AXIOM |
| 2 | $`S^3`$ volume ($`n = 3`$) carries the deepest dilution, $`(\sqrt{\Omega})^{-3}`$, and no assigned observable ([Manifold Index](../../framework/README.md#manifold-index)) | MOTIVATED |
| 3 | Degrees of freedom of a bounded region are counted by the surface, not the volume | MOTIVATED by 1 + 2 |
| 4 | $`S \propto A`$ (area, not volume) | MOTIVATED |
| 5 | $`S = A/(4\ell_P^2)`$ with the factor 1/4 | OPEN |

*Whether the volume carries independent gauge degrees of freedom is not settled here: the [coexact gap](../../framework/files/bedrock/files/coexact-gap.md) computes gauge fluctuations on the three-dimensional quotient, and its relation to the surface count of step 3 awaits reconciliation.*

In standard physics, area scaling is a deep question: why area rather than volume? In MIT, the volume layer ($`n = 3`$) carries the deepest dilution and no assigned observable, which motivates counting at the surface. Entropy lives on the surface because the surface carries the boundary condition. The horizon area is the natural count of $`n = 2`$ degrees of freedom at the sampling boundary.

What remains open is the coefficient. Since $`r_k = \rho_k r_s`$ for a fixed dimensionless $`\rho_k`$ depending only on $`k`$ (§VIII.3), the shell areas scale exactly like horizon area, $`A_k = \rho_k^2 A_H`$, and the sum over the 33 finite shells is finite, not divergent: $`\sum_{k=1}^{33}\rho_k^2 \approx 891`$ for the full grid, $`\approx 219`$ for the bosonic even-$`k`$ subgrid ($`k=2,4,\ldots,32`$, 16 finite addresses). It does not reproduce $`S_{BH}`$ either way: it gives a large, mapping-dependent multiple of $`A_H`$ with no established interpretation as entropy or a microstate count. That the sum scales with area at all is close to automatic, a consequence of every $`r_k`$ being proportional to $`r_s`$, not a nontrivial structural result; the real open problem is the weighting or state-count rule that would turn the raw coefficient ($`\approx891`$ or $`\approx219`$) into $`1/4`$, not whether area scaling holds in the first place. Including the $`k=34`$ reference point, which is $`r\to\infty`$ exactly (§VIII.3), would make the sum infinite; that point is the asymptotic reference, not a physical shell, and does not belong in it. The factor 1/4 is not produced by the 3/2 vacuum-reference conversion, by the structural coefficient $`\sin(\pi\Theta_0)`$, or by any evident combination of current framework quantities. A microstate counting rule, a spectral degeneracy law, or a topological partition function on the horizon would be needed.

**The 1/4 flag.** The structural ratio $`\Delta S_\text{phase}/\Delta S_\text{min} = 1/4`$ (one spatial grid step carries 1/4 of one temporal chronon action) matches the Bekenstein-Hawking factor numerically. These are different objects at different levels: the spatial/temporal ratio is topology-native (no $`G`$, no $`M`$); the entropy factor involves $`G`$ through $`\ell_P`$. Whether they connect through a derivation or coincide by accident is OPEN. Flagged, not forced.

---

## IV. Information

| Step | Content | Status |
|---|---|---|
| 1 | The wave persists at all $`\Theta`$ | AXIOM (wave identity) |
| 2 | $`C(\Theta) \to 0`$ means observation stops, not that the wave stops | Follows from 1 |
| 3 | The wave carries full mode structure through the node | Follows from 1 |
| 4 | The postulate supplies an information-preserving ontology | Output |
| 5 | Unitary evolution and information recovery in the outgoing radiation | OPEN |

Wave persistence is an ontological claim: the information still exists, globally, in the wave. That is not the same claim as unitary recoverability, that the exterior/outgoing density matrix is pure, or reproduces a Page curve. A hidden global wave can preserve information in this ontological sense while the exterior state an observer actually has access to remains exactly thermal forever. Resolving the paradox in the technical sense (unitary S-matrix, information recoverable from Hawking radiation) requires saying something about that quantum-state evolution specifically, which is not attempted here.

Every other approach to the information paradox introduces its own new physics or structure: firewalls, complementarity, remnants, ER=EPR. MIT is not an exception to that in kind, it introduces its own new ontology and sampling structure; the comparison is about which new structure, not whether one is needed.

A guitar string at a node: the string is still there, the wave passes through, the displacement at that point is zero. The string has not become something else. You just cannot read it there.

The spectral mirror (§II.A) reinforces the ontological point: at $`s = 0`$, the spectral zeta value vanishes ($`Z_\sigma(0) = 0`$; the zeta-regularized determinant is $`\exp(-Z'_\sigma(0))`$, built from the derivative, not this value), but the L-function structure persists in that derivative ($`Z'_\sigma(0) = \log T^2`$). The information encoded in the spectrum is not lost at the zero; it is carried by the first nonvanishing order. The wave on $`S^3`$ does not stop at the spectral zero any more than the standing wave stops at the node, an ontological parallel, not a demonstration of unitarity.

### IV.A The Geometric Complement

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/bh-budget.png?raw=true" width="80%" alt="The budget identity on the Moebius band. Top: the intrinsic quotient [0, pi R] x [-W, W] / (0, w) ~ (pi R, -w), drawn with width |J| and not as an embedding. The gluing seam at y = 0 ~ pi R is a transverse arc with flip arrows, ending on the longitudinal edges w = +W and w = -W, which join into the boundary. The dashed core w = 0, the phase circle, crosses the seam at one point, Theta = 0 = 1, and runs through the pinch at the cone point y = pi R/2. On the seam u0 = 0, J = +1 or -1, C = 0; at the cone point u0 = 1, J = 0, C = 2. Bottom: u0 squared, J squared and their constant sum 1 against y from 0 to pi R, the signed J falling from +1 to -1, and C = 2 u0 squared on a second axis">

The [Sector A eigenvalue problem](../../framework/files/bedrock/files/first-eigenvalue.md) gives the first positive eigenfunction and the metric coefficient on a band of the totally geodesic great $`S^2 \subset S^3`$, whose edge-identified quotient is the Möbius band:

```math
u_0(y) = \sin(y/R), \qquad J(y) = \cos(y/R)
```

$`u_0`$ is the first positive eigenfunction of the twisted Laplacian, with eigenvalue $`2/R^2`$. $`J`$ is the Jacobi field: the transverse scale factor measuring the geometric width of the surface at each meridional position $`y`$. The phase coordinate is $`\Theta = y/(\pi R)`$, so the phase operator is $`C(\Theta) = 2\sin^2(\pi\Theta) = 2u_0^2`$.

The two quantities satisfy:

```math
u_0^2 + J^2 = 1
```

Equivalently: $`C/2 + J^2 = 1`$. Observation amplitude and transverse geometry are complementary on the meridian. The surface has a fixed budget: what it spends on geometric extent, it loses in spectral amplitude.

| Location | $`y`$ | $`\lvert J\rvert`$ (surface width) | $`u_0`$ (eigenfunction) | $`C`$ (observation) | Reading |
|---|---|---|---|---|---|
| Gluing seam | 0 or $`\pi R`$ (identified) | 1 (full width) | 0 (zero) | 0 | Surface at maximum extent. Observation silent. |
| Antinode (cone point) | $`\pi R/2`$ | 0 (collapsed to a point) | 1 (maximum) | 2 | Surface collapsed. Observation peaks. |
| Fibonacci wells | intermediate | intermediate | intermediate | 0.22 to 1.97 | Where sampling reads finite observables. |

$`J(y) = \cos(y/R)`$ is signed: $`J(0) = 1`$ but $`J(\pi R) = -1`$. The table above lists $`\lvert J\rvert`$, the transverse extent, which is what "surface width" means physically; the budget identity itself is stated in $`J^2`$ ($`u_0^2 + J^2 = 1`$), so the sign is immaterial there. Retain the signed $`J`$ when discussing the Jacobi field as such.

**Where the zeros live.** The Möbius identification $`(0, w) \sim (\pi R, -w)`$ glues the transverse arcs $`y = 0`$ and $`y = \pi R`$ into one transverse arc, the gluing seam, parametrized by $`w \in [-W, W]`$. The twist acts across it. The boundary $`\partial M = S^1`$ consists of the longitudinal edges $`w = \pm W`$, which the same identification joins into a single loop running in the $`y`$-direction; it carries all values of $`u_0`$ from 0 to 1. The $`C = 0`$ locus is the gluing seam: it crosses the band's core, the closed curve $`w = 0`$ along which $`\Theta`$ runs once from 0 to 1, at a single point, and meets the temporal edge $`\partial M`$ at its two ends.

**Why sin, why there.** On the flat strip, the anti-periodic BC admits both $`\sin(y/R)`$ and $`\cos(y/R)`$ as lowest flat-strip modes at the same eigenvalue $`1/R^2`$: a degenerate pair. Cosine has no zeros at $`y = 0, \pi R`$. The curvature of $`S^3`$ breaks this degeneracy. The $`\tan(y/R)`$ term in the curved Laplacian ($`\Delta u = u'' - R^{-1}\tan(y/R)\,u'`$) eliminates cosine as a solution entirely. Only $`\sin(y/R)`$ survives, and the eigenvalue is simple (Sector $`\mathcal{A}`$, §7, Sturm-Liouville). The same curvature that lifts the eigenvalue from $`1/R^2`$ to $`2/R^2`$ selects the eigenfunction that vanishes on the gluing seam. The zeros are placed by the curvature, through the selection of sin over cos.

At the $`C = 0`$ locus, the surface is at its most geometrically intact. The Möbius band is wide open. The transverse direction has full extent ($`\lvert J\rvert = 1`$). The wave has maximum room. The eigenfunction vanishes because the curvature of the embedding uniquely selects a first positive mode whose zeros land on the gluing seam. The surface is healthy. Sampling is what fails.

This complementarity is created by the curvature of $`S^3`$. On the flat strip, $`J = 1`$ everywhere, sin and cos are equally valid lowest modes, and there is no trade-off between geometry and observation. The totally geodesic great $`S^2 \subset S^3`$ on which the band lies curves $`J`$ into $`\cos(y/R)`$, breaks the eigenfunction degeneracy in favor of $`\sin(y/R)`$, and couples the two through a shared curvature $`K = 1/R^2`$. The complementarity and the zero placement are both consequences of the great-$`S^2`$ geometry.

**Status:** DERIVED. Follows from the Sector $`\mathcal{A}`$ eigenfunction, the Jacobi equation on $`S^2 \subset S^3`$, and the Pythagorean identity. The complementarity is forced by the totally geodesic great-$`S^2`$ geometry the band inherits; any other ambient geometry would break it.

**Local flatness at the node, precisely.** At $`y = 0`$ (on the gluing seam), the curvature term's coefficient in the surface's Laplace-Beltrami operator ($`\Delta u = u'' - \tfrac1R\tan(y/R)\,u'`$) vanishes, so the first-order drift term drops out there and the operator coincides pointwise with the flat-strip operator ($`u''`$); the principal symbol, from $`u''`$ alone, is the same everywhere and was never in question. This is a pointwise coincidence, not a neighborhood one: expanding $`\tfrac1R\tan(y/R) \approx \tfrac{y}{R^2} + \tfrac{y^3}{3R^4} + O(y^5/R^6)`$ shows the curvature term reappears at next order immediately off the point, the same way Christoffel symbols vanish at a point in Riemann normal coordinates without curvature disappearing nearby. The eigenvalue $`\lambda_0 = 2/R^2`$ remains a global property of the whole surface throughout.

---

## V. Size, Temperature, Mergers

Black holes span over ten orders of magnitude in mass. MIT accommodates the full range from a single mechanism, more enclosed $`n = 2`$ content pushes $`\Theta`$ further toward the domain boundary, extending the $`C = 0`$ surface outward, without explaining the observed astrophysical mass distribution itself.

### Size

| Property | Stellar (~10 M☉) | Supermassive (~10⁹ M☉) | MIT reading |
|---|---|---|---|
| $`R_s`$ | ~30 km | ~10⁹ km | Radius where enclosed surface content closes sampling |
| Area (Planck units) | ~4×10⁷⁹ | ~4×10⁹⁵ | Surface degrees of freedom at the sampling boundary |

The size of a black hole is the amount of wave content enclosed behind the sampling boundary. The horizon radius is where that content generates enough curvature to push $`\Theta`$ to its boundary, zeroing $`C`$.

### Temperature

The transition from $`C > 0`$ to $`C \approx 0`$ is compressed into a smaller region for smaller black holes. Steeper gradient means more residual sampling leaks through.

| Black hole | $`C`$ gradient at boundary | Hawking $`T`$ |
|---|---|---|
| Stellar | Steep (short transition) | ~10⁻⁸ K |
| Supermassive | Gentle (long transition) | ~10⁻¹⁷ K |

The wave is still there at the boundary. The surface is still real. The gradient of $`C`$ near the zero controls how much mode structure leaks through, an eigenfunction-gradient structure, paired with, not yet derived as, the mechanism behind Hawking radiation. The spectral analog (§II.A): at $`s = 0`$, the torsion $`Z'_\sigma(0)`$ carries L-function content through the spectral zero, with the amount of content controlled by the derivative.

**Recovery of $`T_H`$.** The $`\Phi \to \Theta`$ mapping (§VIII.1) establishes that $`C/C_0 \sim A(1-r_s/r)`$ as $`r\to r_s`$, with the exponent on $`(1-r_s/r)`$ uniquely forced to 1 by the requirement that the eigenfunction slope $`u_0'(0) = 1/R`$ remain finite and nonzero in proper distance coordinates at the horizon; the leading coefficient $`A`$ is not fixed by that argument. The resulting chain, writing $`x=1-r_s/r`$ and $`u_0 = \sin(\pi\Theta_0)\sqrt{Ax}`$:

```math
u_0'(0) = \frac{1}{R} \;\longrightarrow\; \frac{du_0}{d\Theta}\bigg\vert_0 = \pi \;\longrightarrow\; \frac{du_0}{d\ell}\bigg\vert_H = \sqrt{A}\,\kappa_\text{geom}\sin(\pi\Theta_0)
```

where $`\kappa_\text{geom} = 1/(2r_s) = c^2/(4GM)`$ has units of inverse length, matching $`du_0/d\ell`$ (using $`\sqrt{x}\sim\ell/2r_s`$ near the horizon). The physical surface gravity $`\kappa_\text{phys} = c^2\kappa_\text{geom} = c^4/(4GM)`$ carries units of acceleration; the two are related by a factor of $`c^2`$, not equal, and "$`\kappa`$" alone is ambiguous between them. The $`1/M`$ dependence of $`du_0/d\ell|_H`$ is robust as long as $`A`$ is mass-independent, carried entirely by $`\kappa_\text{geom}`$. The specific numerical coefficient $`\sin(\pi\Theta_0) \approx 0.777`$ is obtained only after additionally setting $`A=1`$, the normalized minimal choice ($`C/C_0 = 1-r_s/r`$ exactly, not merely proportional to it near the horizon), which belongs to the minimal global extension (§VIII.1), not to the exponent-uniqueness argument. The thermal spectrum itself, $`T_H = \hbar\kappa_\text{phys}/(2\pi c k_B) = \hbar c^3/(8\pi GMk_B)`$ (Planck distribution), is a further, separate claim: inherited through pairing $`C/C_0`$ with the Schwarzschild lapse $`N^2=1-r_s/r`$ (the convention-independent, manifestly non-negative object; bare $`g_{tt}`$ carries a sign that depends on metric-signature convention) and GR's Euclidean periodicity, not independently recovered from the eigenfunction slope, and $`\sin(\pi\Theta_0)`$ does not appear in it. Both are tied to the exterior stationary observer congruence (§I). Status: near-horizon linear exponent DERIVED; eigenfunction-gradient $`1/M`$ scaling obtained under a mass-independent leading coefficient; the numerical coefficient $`\sin(\pi\Theta_0)`$ obtained under the normalized minimal choice $`A=1`$; Hawking-temperature normalization and thermal character INHERITED through the minimal lapse pairing.

### Mergers

Two $`\Theta = 0`$ ($`C = 0`$) regions combine. Total enclosed content adds. New boundary area exceeds the sum of parent areas. This provides the MIT reading of the area theorem (Hawking 1971: horizon area never decreases), matching §VIII.4's MOTIVATED status rather than deriving it: you cannot extract $`n = 2`$ wave content through a zero-sampling boundary, so content can enter but not leave, and the boundary grows or holds. This reading is scoped to classical merger dynamics with no radiation; it is not a claim that area can never decrease under any process, the next subsection (Evaporation) describes exactly that, via Hawking radiation carrying content away. A general proof for dynamical, radiating horizons is not established here.

### Evaporation

Under the inherited Hawking law, decreasing $`M`$ raises $`T_H\propto1/M`$ and accelerates mass loss: smaller black holes radiate faster and shrink faster, a runaway. The divergence of $`d\ln C/d\Theta = 2\pi\cot(\pi\Theta)`$ as $`\Theta\to0`$ is a structural analogy expressing sampling sensitivity near the node, $`C`$ responding more and more sharply to a given $`\Theta`$-change, not the evaporation dynamics itself; it is not the source of the runaway. Quantitative recovery of the evaporation rate from the framework's own variables is MOTIVATED at best.

**Minimum mass (conditional estimate).** The 120-grid maps 33 finite radial addresses in the exterior plus the asymptotic reference point (§VIII.2, §VIII.3). Setting the proper distance to the innermost shell equal to the Planck length gives $`M_\text{min} \approx 7.4\,m_P`$ (full grid) or $`\approx 3.7\,m_P`$ (bosonic grid), *conditional* on the minimal-extension coefficient ($`A=1`$ above) and on the $`\ell_\text{innermost}=\ell_P`$ cutoff, which is imposed, not derived from any instability or exclusion principle. The framework's own action bound ($`\Delta S_\text{min} = \hbar\pi/30`$) produces no mass threshold: the action per grid step at the horizon is mass-independent ($`\Delta S_\text{phase}/\Delta S_\text{min} = 1/4`$, a structural ratio). The minimum mass is a property of the interface ($`G`$, which produces $`\ell_P`$), while the topology treats every horizon with equal fidelity.

### Local dynamics and the merger problem

MIT leaves Einstein's field equations unchanged, and a merger is local dynamics: the inspiral, the waveform, and the ringdown are inherited from general relativity, which already matches LIGO. That inheritance is by design, not an omission. Static here is a cosmological claim: it fixes the topology and the global scale of $`S^3`$, not the local metric. The $`C \to 0`$ boundary is not a defect pinned to a coordinate on $`S^3`$; it is the local field configuration the mass sources, represented by the Schwarzschild lapse through the minimal pairing $`C/C_0 = N^2 = 1-r_s/r`$ (§VIII.1), localized because the mass breaks the homogeneity of the right SU(2) action. It travels with its mass: two orbiting black holes are two $`C \to 0`$ regions carried under their mutual gravity, exactly as two Schwarzschild horizons move through the fixed coordinate background of a numerical-relativity simulation.

What the framework has not yet done is restate that motion in its own language. The $`\Phi \to \Theta`$ mapping of §VIII.1 is derived only at leading order and only for a horizon at rest, pairing $`C/C_0`$ with the lapse $`N^2`$ for a single static black hole. The dynamical version, two $`C \to 0`$ regions moving, radiating, and combining, written in the sampling variables rather than inherited from the metric, is open: §VIII.1 already flags the global corrections and the Kerr generalization as untested. This is an incomplete re-description, not a missing mechanism. General relativity supplies the physics of the merger and the framework keeps it in full; what is outstanding is the translation of that physics into the $`C(\Theta)`$ picture, the next order of the same mapping that is leading-order everywhere gravity meets the grid.

---

## VI. The Phase Walk and the Closed Domain

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/bh-closed-domain.png?raw=true" width="85%" alt="The phase operator C(Theta) over the closed domain: the bosonic domain [0, 60/120] shaded up to its wall at the antinode, Lambda; the H0 well at 34/120 and the one-step displacement toward 36/120 that the Hubble-tension correspondence would need; the horizon walking continuously from the well down to the node at Theta = 0; and Theta = 0 and Theta = 1 joined as one node with two coordinate addresses">

The [phase field](../../framework/README.md#the-phase-field) and the black hole case both move $`\Theta`$ on the same phase operator $`C(\Theta)`$, but not by the same mechanism. The phase-field shift would be a discrete environmental step (2/120). The trigger proposed to realize it is withdrawn: the pre-registered SPARC coherence test falsified it, and a separate exploratory check did not detect the two-cluster $`H_0`$ structure it predicted, so that correspondence has no active mechanism ([Hubble Tension](hubble-tension.md), §III and §V). The black hole case is a different, continuous mechanism: the Schwarzschild response $`C/C_0 = 1 - r_s/r`$ (§VIII.1), which in an ordinary galactic potential gives a smooth shift orders of magnitude below one bosonic step (§VIII.1, weak-field decoupling). They share the operator, not the response law, and the two numbers should not be expected to agree.

### The bosonic domain has a wall

The full 120-grid comes from $`|2I| = 120`$. Observation squares the wavefunction, projecting $`2I \to I`$, giving the 60R bosonic grid. This projection traces to the edge stabilizer $`Z_4 \subset 2I`$: integer-spin irreps carry only real $`Z_4`$ content ($`D = 60`$), half-integer carry only complex pairs ($`D = 120`$). For photon-mediated observables, the effective domain is $`[0, 60/120]`$. The antinode at 60/120 is the boundary of the bosonic domain. Bosonic sampling reaches $`\Lambda`$ and stops.

### The two nodes are one point

The eigenfunction $`u_0 = \sin(y/R)`$ vanishes at $`y = 0`$ and $`y = \pi R`$. The Möbius identification $`(y + \pi R, w) \sim (y, -w)`$ glues these two ends into one transverse arc, the gluing seam of §IV.A. The anti-periodic boundary condition gives $`u_0(\pi R) = -u_0(0) = 0`$. On the phase circle, the band's core, $`\Theta = 0`$ and $`\Theta = 1`$ are two coordinate addresses for one point; on the band, the node is the whole gluing seam through that point.

The Hubble-tension step (from 34/120 to 36/120) would move toward the antinode, away from the node, were a mechanism to realize it. The black hole horizon (walking from 34/120 toward 0/120) moves toward the node where $`C`$ vanishes. Both are shifts on the same closed domain, one away from the zero, one toward it.

One arch, one node (with two coordinate addresses), one antinode.

### The spectral mirror

The spectral side exhibits the same structure. Moving away from $`s = 0`$ opens the Pochhammer tower (factorization breaks, 28-32 of 32 characters contribute). Moving toward $`s = 0`$ collapses it (4 of 16 characters survive). The "clean" direction is toward the zero. The "messy" direction is away from it. This matches: the horizon (toward $`\Theta = 0`$, where $`C`$ vanishes) is where structure simplifies; the interior of the domain (away from both zeros) is where everything participates.

---

## VII. Near the Planck Floor (Speculative; Not Reached by the Derived Mapping)

This section is not covered by the $`\Phi \to \Theta`$ mapping (§VIII.1), which is derived only for $`r \geq r_s`$ and does not extend to the interior or to $`r = 0`$ (§I). What follows is a separate, more speculative discussion of what "no scale separation" would mean in this framework's own terms, not a statement about black hole interiors specifically.

By definition, $`\Omega_\Psi \equiv (\ell_\text{phase}/\ell_P)^2`$. Equal phase and Planck scales, $`\ell_\text{phase} = \ell_P`$, correspond to $`\Omega_\Psi = 1`$, not $`\Omega_\Psi \to 0`$: that is the point where the distinction between edge ($`n = 1`$) and surface ($`n = 2`$) would lose operational meaning, a dissolution of the hierarchy that distinguishes them, not a conversion of one into the other. $`\Omega_\Psi \to 0`$ would instead mean the phase-gradient length shrinks *below* the Planck length, which this framework does not currently interpret; if that limit is physically meaningful at all, it needs its own justification, not an equation with $`\Omega_\Psi = 1`$.

If the wave content persists at $`\Omega_\Psi = 1`$, as the postulate would suggest, it cannot be sorted into "surface" and "edge" categories there, because the hierarchy that makes that distinction meaningful has collapsed to unity. Whether this has anything to do with the interior of an actual black hole is exactly what is not established here.

---

## VIII. Open Derivations

### VIII.1 The Φ → Θ Mapping (Priority 1)

**Status: DERIVED (leading order near the horizon); the global form below is the minimal extension of that result, not independently forced.**

The mapping pairs the framework's sampling amplitude with the GR redshift factor:

```math
\frac{C(\Theta)}{C(\Theta_0)} = 1 - \frac{r_s}{r}
```

Equivalently: $`\sin(\pi\Theta) = \sin(\pi\Theta_0) \cdot (1 - r_s/r)^{1/2}`$, with $`\Theta_0 = 34/120`$. Write $`x = 1-r_s/r`$: what the argument below actually forces is the leading behavior $`C/C_0 \sim x`$ as $`x\to0`$ (the horizon). Taking $`C/C_0=x`$ at all $`r`$ is the minimal global extension consistent with that limit and with $`C/C_0\to1`$ as $`r\to\infty`$; it is a choice, not a further derivation, and the weak-field result below, which lives at $`x\to1`$, rests on that choice rather than on the horizon argument alone.

The power $`\beta = 1`$ is uniquely forced by the requirement that the eigenfunction slope $`u_0'(0) = 1/R`$ (a geometric property established by two independent paths in the Sector $`\mathcal{A}`$ paper) remain finite and nonzero in proper distance coordinates at the horizon. For $`\beta < 1`$, the slope diverges; for $`\beta > 1`$, it vanishes. Only $`\beta = 1`$ preserves the geometric property.

**Sketch of uniqueness.** The proper distance from the horizon, $`\ell \propto (r - r_s)^{1/2}`$ near $`r = r_s`$, is measured on a Schwarzschild $`t = \text{const}`$ exterior slice, the same static/exterior construction flagged throughout (§I). Under $`C/C_0 = (1 - r_s/r)^\beta`$, the eigenfunction $`u_0 = (C/2)^{1/2} \propto (r - r_s)^{\beta/2}`$. The slope in proper distance is $`du_0/d\ell \propto (r - r_s)^{(\beta - 1)/2}`$. For $`\beta < 1`$: diverges. For $`\beta > 1`$: vanishes. For $`\beta = 1`$: finite and nonzero, matching $`u_0'(0) = 1/R`$ from the Sector $`\mathcal{A}`$ eigenvalue problem.

**Verified properties:**

| Property | Result |
|----------|--------|
| Weak-field behavior, under the minimal global extension | For $`C/C_0=1-r_s/r`$, the smooth shift at $`r/r_s=10^6`$ is $`2\times10^{-7}`$, far below one bosonic step (2/120): the Schwarzschild response does not reach, and does not explain, the separate phase-field step, whose proposed trigger is withdrawn (§VI). Not protected by the near-horizon uniqueness proof, which constrains only $`f(x)\sim x`$ as $`x\to0`$; a different global $`f`$ with the same horizon limit could give a different weak-field derivative $`f'(1)`$ |
| Near-horizon slope | $`du_0/d\ell\vert_H = \sqrt{A}\,\sin(\pi\Theta_0) \cdot \kappa_\text{geom}`$, finite and nonzero for mass-independent $`A`$, proportional to surface gravity; $`\sin(\pi\Theta_0)`$ alone requires the further choice $`A=1`$ (§V) |
| Uniqueness of $`\beta = 1`$ | Only value giving finite nonzero slope; all other $`\beta`$ fail |
| Identity under the minimal extension | $`C(\Theta)/C(\Theta_0) \div (1 - r_s/r) = 1`$ exactly at all radii, by construction of the minimal choice, not an independent check |

**What remains open:** Global corrections (functions $`f(x)`$ with $`f(x) \sim x`$ near $`x = 0`$ but $`f(x) \neq x`$ globally) are constrained to preserve the horizon asymptotics by construction, but nothing forces $`f'(1) = 1`$: they can alter the weak-field/galactic regime ($`x\to1`$) freely, since that regime is not what the uniqueness argument constrains. Recovering the weak-field result above specifically requires either the minimal choice $`f(x)=x`$ or an independent argument fixing $`f'(1)=1`$; neither is presently derived. A Kerr generalization is untested, and pairing $`C/C_0`$ with bare $`g_{tt}`$ is not even the right target to test: in Kerr, $`g_{tt}=0`$ defines the stationary-limit surface (the ergosurface), not the event horizon, except in the non-rotating limit where the two coincide. The horizon itself is where the norm of the horizon-generating Killing field $`\chi^\mu=(\partial_t)^\mu+\Omega_H(\partial_\phi)^\mu`$ vanishes, $`\chi^\mu\chi_\mu=0`$; any rotating extension of this mapping should be built on that norm, not on $`g_{tt}`$.

Lemma 8 (The Mirror) proved that the direct map $`s \leftrightarrow \Theta`$ does not exist on the spectral side. The physical $`\Phi \to \Theta`$ mapping avoids this obstruction: a gravitational potential breaks the right-<i>SU(2)</i> homogeneity that forces continuous position out of spectral data (mass at a specific location breaks the isometry).

### VIII.2 Minimum Black Hole Mass (Priority 2)

**Status: CONDITIONAL ESTIMATE, under the minimal-extension coefficient ($`A=1`$, §V) and an imposed Planck-length cutoff. Not a derived physical bound: no instability, exclusion principle, or formation argument is given for why lighter masses cannot exist.**

The 120-grid maps 33 finite radial addresses between the horizon and the $`H_0`$-well reference point ($`\Theta_0 = 34/120`$, which this mapping's normalization treats as the asymptotic $`r\to\infty`$ limit; the 34th grid position is that limit itself, not an address, §VIII.3). Each shell sits at $`r_k/r_s = 1/(1 - C(k/120)/C_0)`$. In proper distance, the shells are nearly uniformly spaced near the horizon (increments of ~$`0.067\,r_s`$ to ~$`0.081\,r_s`$ for the first 10 shells); at $`k=30`$ the proper distance is $`\approx 6.81\,r_s`$, not the previously stated $`5.67\,r_s`$ (§VIII.3).

Setting the proper distance to the innermost grid point equal to the Planck length, an imposed cutoff, not a derived one:

| Grid | Innermost point | $`M_\text{min}`$ (conditional) |
|------|----------------|----------|
| Full 120 | $`\Theta = 1/120`$ | $`\approx 7.42\,m_P`$ |
| Bosonic 60 | $`\Theta = 2/120`$ | $`\approx 3.70\,m_P`$ |

Both are deep in the quantum gravity regime (~$`10^{38}`$ times smaller than any astrophysical black hole), conditional on the assumptions above. The framework's own action bound ($`\Delta S_\text{min} = \hbar\pi/30`$) produces no mass threshold: the action per grid step at the horizon is mass-independent ($`r_s`$ in the proper distance cancels $`r_s`$ in the surface gravity). Whichever cutoff and coefficient are used, the minimum mass is a property of the interface ($`G`$, which produces $`\ell_P`$), not of the topology, which treats every horizon with equal fidelity.

### VIII.3 Discrete Horizon Structure (Priority 3)

**Status: CONDITIONAL RADIAL-ADDRESS MAP under the minimal global mapping (§VIII.1), not an established shell structure. The 33 addresses are read off a relation already established to be continuous (§VI); nothing here forces the metric itself to be discontinuous at these radii.**

Under the minimal global mapping, the 120-grid selects 33 finite radial addresses between the horizon and the $`k=34`$ reference point, which is $`r\to\infty`$ exactly (§VIII.2): at $`k=34`$, $`C(k/120)/C_0=1`$ by definition of $`C_0\equiv C(\Theta_0)`$, giving $`r_{34}/r_s\to\infty`$, not a 34th finite address. Each shell $`k=1,\ldots,33`$ sits at coordinate radius $`r_k`$ where $`C(k/120)/C_0 = 1 - r_s/r_k`$, giving $`r_k/r_s = 1/(1 - C(k/120)/C_0)`$. The proper distance from the horizon to $`r_k`$ is $`\ell_k = \int_{r_s}^{r_k} (1 - r_s/r')^{-1/2}\,dr'`$. The shell structure:

| $`k`$ | $`r_k/r_s`$ | $`\ell_k/r_s`$ (proper distance from horizon) |
|-----|-----------|------|
| 1 | 1.001 | 0.067 |
| 5 | 1.029 | 0.342 |
| 10 | 1.125 | 0.721 |
| 20 | 1.706 | 1.86 |
| 30 | 5.810 | 6.81 |

**What the shells are, unresolved.** The innermost spacing is $`\ell_1 \approx 0.067\,r_s`$: for a $`10\,M_\odot`$ hole this is kilometers, for a supermassive hole, astronomical, not a Planck-scale correction at either end; by $`k=33`$ the shells already sit at $`\approx 23\,r_s`$, well into the exterior rather than clustered at the horizon. §VI calls the underlying Schwarzschild response continuous, and the mapping bears that out: $`\Theta(r)`$ is smooth and monotonic, so every value between $`0`$ and $`\Theta_0`$ is reached by some $`r`$, not only the integers $`k`$ this section restricts to. That restriction, imported from the same 120-grid used elsewhere in the framework, is what produces 33 addresses; the $`r`$-$`\Theta`$ relation itself does not single them out. This makes the readings asymmetric, not four peers: (2) discrete sampling addresses on a continuous metric and (3) bookkeeping need nothing beyond what is already stated here; (1) physical layers in the geometry needs a pinning or quantization rule that nothing in this framework currently supplies, and a fourth, unspecified alternative is not excluded either. Absent such a rule, (1) is the reading that owes new physics, not a peer of (2)/(3).

Given that asymmetry, only reading (1) changes what a ringdown could actually see: a genuine layer in the geometry perturbs the effective potential a ringdown probes, a claim a measurement bears on. Reading (2) leaves the metric and its wave equation untouched by construction, so the radiated signal is exactly GR's, though not necessarily silent everywhere: this framework treats sampling itself as physically doing something, not merely reading a value that was already there (§IV), so a discretized sampling process could in principle still show up in emission or detection channels without touching the metric; nothing here specifies such a mechanism, though. Reading (3) predicts nothing observable by definition. A null ringdown result would therefore constrain reading (1)'s specific parameters (amplitude, location, coupling to the relevant modes), not rule out physical layers as a class, and would say nothing about (2) or (3); no frozen test is registered against any of this yet.

Potential observational signatures (all require detailed modeling, and depend on which of the above the shells are). Integer-spin (bosonic) channels, gravitational-wave ringdown and photon emission alike, should use the bosonic subgrid, $`k=2,4,\ldots,32`$, 16 finite addresses; fermionic emission channels, where energetically accessible, would use the full $`1/120`$ resolution instead:
- Hawking spectrum: deviations from perfect Planck blackbody, set by lattice geometry
- Quasi-normal modes: discrete structure in gravitational wave ringdown frequencies

These are speculative pending the ontology question above, not an established prediction to test against LIGO/LISA ringdown data.

### VIII.4 Black Hole Thermodynamics (Priority 4)

| Law | GR statement | MIT target | Status |
|---|---|---|---|
| Zeroth | $`\kappa`$ constant on horizon | Uniformity of the surface-gravity analogue ($`\kappa_\text{geom}`$, i.e. $`du_0/d\ell\vert_H`$) across the horizon's 2-sphere; not the trivially-uniform value $`C=0`$ itself, which says nothing about $`\kappa`$ | OPEN |
| First | $`dM = (\kappa/8\pi)dA + \Omega\,dJ + \Phi\,dQ`$ | Energy balance from mode accounting | OPEN |
| Second | $`dA \geq 0`$ | Wave content behind $`\Theta = 0`$ boundary cannot decrease | MOTIVATED |
| Temperature | $`T_H = \hbar c^3/(8\pi G M k_B)`$ | Eigenfunction slope: $`du_0/d\ell\vert_H = \sqrt{A}\,\sin(\pi\Theta_0) \cdot \kappa_\text{geom} \propto 1/M`$ for mass-independent $`A`$ (§V). Thermal spectrum inherited through pairing $`C/C_0`$ with the lapse $`N^2=1-r_s/r`$. | Near-horizon exponent DERIVED; $`1/M`$ scaling and $`\sin(\pi\Theta_0)`$ coefficient obtained under the minimal choice $`A=1`$ (§V); temperature normalization and thermal character INHERITED |

The GR third law (extremal horizons, $`\kappa = 0`$, cannot be reached in finite physical operations) has no established correspondence here: a Schwarzschild horizon at $`\Theta = 0`$ has nonzero surface gravity, and $`\Theta = 0`$ is itself grid position $`k=0`$, one finite step from $`k=1`$, on the same lattice used elsewhere in this section. A phase-operator analogue of extremality, if one exists, would need a Kerr or charged-black-hole extension to identify a separate configuration; none is given here.

### VIII.5 Spectral-Physical Bridge (Priority 5)

The structural parallel between the scaling-side zero ($`\Theta \to 0`$ driving $`C \to 0`$, DERIVED, with $`\Omega_\Psi \to 0`$ conjectured alongside it, §II) and the spectral zero ($`Z_\sigma(0) = 0`$, driven by the Pochhammer collapse $`(s)_k = 0`$) is established (§II.A). The $`s \leftrightarrow \Theta`$ map on the spectral side is proved not to exist by Lemma 8 (The Mirror): the spectral and scaling sides are structurally parallel but cannot be connected by a natural map. The open question is whether the torsion survivor $`Z'_\sigma(0) = \log T^2`$ can be connected to the physical survivor (Hawking radiation gradient) through a route other than the direct spectral-to-phase bridge. The $`\Phi \to \Theta`$ mapping provides the discrete localization that spectral geometry lacks (mass breaks the right-SU(2) isometry). If the torsion values $`\{\log 2, \log 3, \log 5, \log\varphi\}`$ constrain the horizon structure through the same arithmetic that constrains the fermion mass spectrum ([mass spectrum](../../spectrum/files/mass-spectrum.md) §II.4), the spectral and physical sides of the double zero would be unified. This would close the loop between Tools 3 and 5 at the boundary of the domain. Status: OPEN.

### VIII.6 The Directional Problem: Critical-Point Geometry

**Status: Critical-point identification DERIVED; dynamical interpretation OPEN (no evolution law for $`\Theta`$ is given anywhere in this framework).**

The Hubble-tension correspondence would walk $`\Theta`$ away from $`0`$ toward the antinode ($`C`$ increases), though no active mechanism realizes it (§VI); the horizon requires $`\Theta \to 0`$ (toward the node, $`C`$ decreases). These look like opposite directions on the domain coordinate, but coordinate direction is not the relevant variable; proximity to a critical point of $`C`$ is.

```math
\frac{dC}{d\Theta} = 2\pi\sin(2\pi\Theta)
```

vanishes at exactly three points:

| Position | $`C`$ | $`dC/d\Theta`$ | Type |
|---|---|---|---|
| $`\Theta = 0`$ | 0 | 0 | Node (minimum) |
| $`\Theta = 1/2`$ (60/120) | 2 | 0 | Antinode (maximum) |
| $`\Theta = 1`$ | 0 | 0 | Node (minimum) |

$`\Lambda`$ sits at the maximum, the horizon at the minimum, opposite critical points of the same function. That $`C(\Theta) = 2\sin^2(\pi\Theta)`$ has critical points exactly at $`\Theta = 0, 1/2, 1`$ is DERIVED directly from its form; that $`\Lambda`$ specifically occupies the antinode and the horizon specifically occupies the node is the physical identification established elsewhere (the antinode assignment for $`\Lambda`$; the $`\Phi\to\Theta`$ mapping, §VIII.1, for the horizon), not something the bare function proves by itself.

**What this does not establish.** $`dC/d\Theta = 0`$ at a point means the *observable* $`C`$ has no first-order response to a small change in $`\Theta`$ there, a statement about $`C`$'s sensitivity, not about whether $`\Theta`$ itself is dynamically stable or attracted to that point. That would require an evolution law for $`\Theta`$ (e.g. $`\dot\Theta = F(\Theta)`$), which is not written down anywhere in the framework. Likewise, the log slope

```math
\frac{d\ln C}{d\Theta} = 2\pi\cot(\pi\Theta)
```

diverges as $`\Theta \to 0`$ and vanishes at $`\Theta = 1/2`$: this says $`C`$ is extremely sensitive to $`\Theta`$ near the node and insensitive to it near the antinode (the first-order-insensitivity argument used for $`\Lambda`$ elsewhere in the framework), not that $`\Theta`$ moves faster near the node. That the black hole horizon has $`\Theta \to 0`$, and that infall past it is one-way, is inherited from GR, not derived from the log-slope of $`C`$.

**A numerical check worth recording.** $`\Theta_0 = 34/120`$, the Hubble-tension well, is not near the antinode plateau: $`C'(34/120) \approx 6.15`$, within 2.2% of the arch's maximum possible slope $`2\pi \approx 6.28`$, and 26 grid steps from $`60/120`$. It sits near the steepest part of the arch, not a flat region. Whatever protects $`\Lambda`$ (whose own well sits exactly at the true zero-slope antinode) does not extend to 34/120.

**Connection to the complementarity.** The two critical points of $`C`$ are the two poles of $`u_0^2 + J^2 = 1`$ (§IV.A): antinode ($`u_0 = 1`$, $`J = 0`$, cone point, curvature dominates) and node ($`u_0 = 0`$, $`J = \pm 1`$, gluing seam, geometry dominates).

---

## Quick Reference

| Quantity | Value | Source |
|---|---|---|
| $`\Theta = 0`$ and $`\Theta = 1`$ | One point of the phase circle (the core); on the band, the gluing seam | Möbius identification; both are zeros of $`C`$; domain is closed |
| $`C(0) = C(1)`$ | 0 | Phase operator at boundary ($`\Theta`$ at the wall drives $`C`$ to zero) |
| $`C'(0) = C'(1)`$ | 0 | Quadratic vanishing |
| $`C''(0)`$ | $`4\pi^2`$ | Leading nonvanishing order |
| $`C(60/120)`$ | 2.00 | Antinode ($`\Lambda`$) |
| $`\Phi_N/c^2`$ at Schwarzschild horizon | -1/2 | Schwarzschild-radius identity using Newtonian $`\Phi_N=-GM/r`$; the exact GR object is $`g_{tt}`$, not $`\Phi_N`$ |
| $`\Phi \to \Theta`$ mapping | near-horizon exponent $`\beta = 1`$ forced; $`C/C_0 = 1-r_s/r`$ globally is the minimal extension | DERIVED (exponent only); global form and coefficient are a choice |
| Bosonic domain | $`[0, 60/120]`$ | $`\lvert I \rvert = 60`$ from squaring |
| Bosonic step | $`2/120 = 1/60`$ | Minimum observable shift |
| Full domain | $`[0, 120/120]`$ | $`\lvert 2I \rvert = 120`$ |
| Fermionic step | 1/120 | Full lattice resolution |
| Bekenstein-Hawking entropy | $`S = A/(4\ell_P^2)`$ | Observed; MIT: motivated by surface primacy ($`n = 2`$); 1/4 factor OPEN |
| Hawking temperature | $`T = \hbar c^3/(8\pi G M k_B)`$ | $`du_0/d\ell\vert_H = \sqrt{A}\sin(\pi\Theta_0) \cdot \kappa_\text{geom}`$; $`1/M`$ scaling DERIVED for mass-independent $`A`$; $`\sin(\pi\Theta_0)`$ under the minimal choice $`A=1`$; temperature normalization and thermal character INHERITED |
| Minimum mass | $`\approx 7.4\,m_P`$ (full grid) or $`\approx 3.7\,m_P`$ (bosonic grid) | CONDITIONAL ESTIMATE (§VIII.2): minimal-extension coefficient + imposed $`\ell_P`$ cutoff, not a derived bound |
| $`Z_\sigma(0)`$ | 0 | Spectral zeta value at boundary (nontrivial $`\sigma`$); the determinant is $`\exp(-Z'_\sigma(0))`$, from the derivative below |
| $`Z'_\sigma(0)`$ | $`\log T^2(\sigma)`$ | Torsion: L-function special values |
| Torsion survivors | $`\{\log 2, \log 3, \log 5, \log\varphi\}`$ | 4 of 16 characters, $`E_8`$ selected; conductors are the stabilizer primes of the icosahedron |

---

*The topology holds. The wave persists. The observer goes silent.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
