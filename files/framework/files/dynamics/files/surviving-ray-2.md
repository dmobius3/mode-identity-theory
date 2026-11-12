<a id="top"></a>
| **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |

---

# 🌊 Nonlinear Standing-Wave Branches and Spectral Transitions on the Poincaré Homology Sphere

**Status (2026-11-11):** Working draft. Its figures, full proofs and final bibliography are to come.

## Abstract

This paper studies standing waves of classical complex test fields on the Poincaré homology sphere $`S^3/2I`$, one in each of eight slots, the nontrivial irreducible representations of $`2I`$, on a static arena of fixed radius. The fields share one action, frozen before the finite-amplitude runs reported here without using any target outcome: the twisted wave operator, the defocusing density quartic, no mass and curvature coupling $`\xi = 0`$. The action is motivated, not derived, its density interaction a hypothesis, and every result is conditional on that action on that geometry. At every nonzero charge each slot has an orbitally stable set of ground states, in five of them an exact family whose every member is spectrally stable. Building on an earlier audited census of critical orbits within a stated class, with three more interval-certified, the paper gives small-amplitude branches and germs with their spectral types, the slow spectrum's next order, and, along branches whose existence is assumed, a Hamiltonian–Krein count with a conditional crossing classification. On pre-registered numerics adjudicated in the OpenWave project, two branches born elliptic are classified elliptic at every registered point up to their slots' spectral gaps, three changes of type are located, none identified with a crossing, and four branches end instrument-limited, no type claimed at their open points. Two slots share every small-amplitude type, their reduced quartics related by an exact scaling. On OpenWave's record they part at finite amplitude. The author's own computation, which no adjudication covers, is reported apart. Persistence tests give finite-time evidence only; the dynamics beyond them is left to a sequel. No physical matter action, particle state, relation among the slots' stable-state energies, stress tensor placed in the metric, gravity source or criterion of OpenWave's model register is claimed.

## 1. Introduction

This paper studies the standing waves of one nonlinear wave equation on the Poincaré homology sphere $`X = S^3/2I`$, with $`2I \subset SU(2)`$ the binary icosahedral group. Its fields are classical complex fields, one in each of eight slots, the nontrivial irreducible representations $`\rho`$ of $`2I`$, with the trivial one as a control, each a section of the flat bundle $`E_\rho = S^3 \times_{2I} V_\rho`$ over $`X`$, on the static arena $`\mathbb{R} \times X`$ with the curvature radius $`R`$ held fixed: they are test fields, with no backreaction on the metric (§ 2.1). The paper asks which branches of standing waves the equation carries, what can be proved about their stability, and how their linearized spectra change at finite amplitude, up to each slot's spectral gap. The arena comes from a framework, Mode Identity Theory (MIT), in which $`X`$ is the observable domain [PC, § XI, 1f]; that reading motivates the model and is evidence for nothing in the paper.

The equation comes from one action common to the eight slots, selected and frozen on 2026-10-04, before any of the finite-amplitude runs this paper reports, with no target outcome choosing any of its elements: the wave operator of the twisted Laplacian, the defocusing density quartic, no mass, and minimal curvature coupling, $`\xi = 0`$ (§ 2.2). The selection is motivated, not derived. Minimal coupling takes one side of a published disagreement, with $`\xi = 1/6`$ the named alternative, and at finite amplitude the choice matters, so the finite-amplitude results are results for $`\xi = 0`$. The density interaction is, in the words of the Surviving Ray, the paper this one follows, "a hypothesis and not a consequence" [Sh]. So every result below is a result about this action on this geometry, not a claim that nature uses it.

In the Surviving Ray, for a block state at level 6 with the density-type interaction $`\lvert\psi\rvert^2\psi`$, binary-icosahedral symmetry restricts the four-dimensional family of equivariant cubic self-maps of spin 3 to two channels, one of them radial, so that modulo the radial direction the surviving interaction is a single projective ray. Its census of the critical orbits of the reduced quartic, within a stated class [Sh, § 7.2], is an audited argument (§ 3.1), and so are its local branch germs [Sh, § 8.3], which are not a verified theorem. This paper does not say that the geometry selects the action: the action is frozen and motivated (§ 2.2), and the branches here rest on Lemmas G and G′ (§ 3.2), not on those germs.

The analytical results have two ranges. At every nonzero charge, in every slot, the minimizers of the energy at fixed charge form an orbitally stable set of standing waves (Theorem A); the proof is the constrained-minimization argument of Cazenave and Lions [CL], with Shatah's treatment of Klein–Gordon standing waves [Sha]. In the five rigid slots and the control, where every lowest-level section has constant norm, that set is the exact lowest-level family, and every member of it is spectrally stable (Theorems B and D, § 3.3). In the three soft slots the branches are born at small amplitude from the nondegenerate critical orbits of a reduced quartic on the lowest level (Lemma G, § 3.2), and along each the small-amplitude spectrum is read off that quartic (Theorem R, § 4.1); the small-amplitude spectral types of the two degenerate orbits are determined at second order (Theorem R′, § 4.2), and the slow spectrum's next order is given in closed form (Proposition N, § 4.3).

Away from small amplitude the spectrum can still be counted. On a branch along which the symmetry acts exactly, its existence at finite amplitude assumed, the Hamiltonian–Krein index theorem [KKS, Pe; KP] holds in the slot action's energy space (Theorem K, § 4.4). The count changes only where eigenvalues pass through zero, and a Krein collision leaves it unchanged; Theorem C classifies a transversal genuine crossing under its hypotheses, a definite crossing form and a regular Jordan structure of the family among them, and Corollary I says what a bracket holding one such crossing, and no other point where eigenvalues pass through zero, can contain.

Past small amplitude no theorem here decides a soft-slot branch's type, and the nondegenerate branches born elliptic are followed numerically, each to its slot's spectral gap, in a census of their finite-amplitude fates (§ 5.1). Two records are kept apart. The M8 program of the OpenWave project ran its finite-amplitude computations, each pre-registered, on two instruments, a finite-element discretization [OW15] and a harmonic Galerkin one, which OpenWave's M8.16.1 run qualified [OW16.1], each run adjudicated by the project's maintainer on a public pull request. MIT's own computation, the author's, outside that program, on the ground of OpenWave's answer that its rule against repair and rerun does not reach what MIT computes in its own repository, read the places the adjudicated record leaves open; no adjudication covers it (§ 5.3).

On OpenWave's adjudicated record two branches end elliptic throughout, classified elliptic at every registered point of their windows; three changes of type are located, each between guard readings of each type and none identified with a crossing; and four branches end instrument-limited, the census's ending that names its cause, their classified types kept and no type claimed at their open points (§ 5.2). The census closed on 2026-11-10, in the author's reading of its conditions on MIT, but the close is procedural, proving no orbital stability, and the type at each instrument-limited item stays open (§ 6.6).

The sharpest contrast is between two slots. In the reduced problem $`R_5`$ is $`R_4`$ with every $`q_J - 1`$ scaled by 9/16, so the two share their critical orbits, signatures and small-amplitude types (§ 3.1). On OpenWave's adjudicated record they part at finite amplitude: for two of the critical orbits of § 3.1, the prism and the hexagon, a change of type is located in $`R_4`$ for the prism and in $`R_5`$ for the hexagon, while the prism in $`R_5`$ and the hexagon in $`R_4`$ are elliptic at every point classified (§ 5.2). This correspondence does not establish the registered relation among the energies of stable states across the eight slots (§ 7.1).

MIT's own computation classifies one branch on both sides of a change of type that the adjudicated record leaves unlocated, but its own locator also stops without locating the change. At the top of one window its records show an index drop, then a change from elliptic to hyperbolic between consecutive points of the path at every cutoff, where a quartet appears; where that collision sits is inferred, from a fitted law, and neither of its ladders classifies those points (§ 5.3).

Persistence enters only as a bounded record. In the persistence terms' words, "a test that Persists is evidence to `T`, not beyond" [OW19]: the eight scored tests of OpenWave's M8.15 run Persist, and so does the coherent orbit's in $`R_5`$, at $`\varepsilon = 32`$ to $`T = 1000`$, while five elliptic stretches, on the branches of two orbits in $`R_4`$ and $`R_5`$, end untested, with no persistence claimed either way (§ 6.3).

The paper claims no physical matter action, particle state, step of the framework's stress-tensor bridge or gravity source, derives no law of the kind the slot relation registers for the energies of stable states across the eight slots, and fills no criterion of OpenWave's model register (§ 7.4). The dynamics of the branches, beyond those bounded tests, is left to a sequel (§ 7.3).

So three kinds of result are kept apart throughout: derived results, each at its grade, OpenWave's adjudicated record, and MIT's own computation, labelled wherever it appears, with what stays open stated beside each. Section 2 fixes the model: the arena, the action and the status of its choices, its symmetries, and what the action settles by itself. Section 3 gives the analytical branch structure: the reduced problem and its certified orbits, branch existence, and the ground states and rigid families. Section 4 treats linearized spectral stability, from small amplitude to the count and the crossing. Section 5 follows the branches born elliptic to their slots' gaps, and Section 6 says what those numerics rest on and where they stop, with the bounded record of persistence. Section 7 reads the results together, and Appendix A gives the checks behind MIT's own computation.

## 2. The frozen slot action

This section fixes the model: the arena and the fields, the action and the status of its choices, its symmetries, and what the action settles before any branch is studied. Every result in the paper is a result about this action on this geometry, not a claim that nature uses it, and a different action would need its own study.

### 2.1 The arena and the fields

Let $`2I \subset SU(2)`$ be the binary icosahedral group, of order 120, acting on the three-sphere $`S^3 \cong SU(2)`$ by left translation, and let $`X = S^3/2I`$, the Poincaré homology sphere [KS], carry the round metric of radius $`R`$. The arena is $`\mathbb{R} \times X`$ with the static metric

```math
ds^2 = -c^2\,dT^2 + R^2\,d\Omega_3^2 ,
```

and $`R`$ is held fixed: the fields below are test fields, with no backreaction on the metric. In the framework that motivates the model, $`X`$ is the observable domain [PC, § XI, 1f]; that reading motivates the choice of arena and is evidence for nothing below.

For each irreducible unitary representation $`\rho`$ of $`2I`$ on a space $`V_\rho`$, a field in the slot $`\rho`$ is a complex section $`\psi_\rho`$ of the flat bundle

```math
E_\rho = S^3 \times_{2I} V_\rho \longrightarrow X ,
```

pulled back to $`\mathbb{R} \times X`$; equivalently, a map $`\psi_\rho`$ on $`\mathbb{R} \times S^3`$, with $`S^3`$ of radius $`R`$, such that $`\psi_\rho(T, \gamma x) = \rho(\gamma)\,\psi_\rho(T, x)`$ for every $`\gamma \in 2I`$. The eight nontrivial representations, $`R_1, \ldots, R_8`$, are the slots, listed in Table 1; the trivial one, $`R_0`$, whose sections are functions on $`X`$, serves as a control.

| Slot | $`\dim V_\rho`$ | Spin class | $`\mathrm{dist}(\rho)`$ |
|---|---|---|---|
| $`R_1`$ | 2 | half-integer | 1 |
| $`R_2`$ | 2 | half-integer | 7 |
| $`R_3`$ | 3 | integer | 2 |
| $`R_4`$ | 3 | integer | 6 |
| $`R_5`$ | 4 | integer | 6 |
| $`R_6`$ | 4 | half-integer | 3 |
| $`R_7`$ | 5 | integer | 4 |
| $`R_8`$ | 6 | half-integer | 5 |

*Table 1.* The slots [SRel, § II]. The spin class is the action of the central element $`-I`$, and $`\mathrm{dist}(\rho)`$ is the lowest level at which $`\rho`$ occurs, as in the next paragraph.

On sections of $`E_\rho`$, with $`\Delta`$ the Laplacian of the flat connection, $`-\Delta`$ has the levels $`k(k+2)/R^2`$, of multiplicity $`(k+1)\,\mathrm{mult}(\rho, \mathrm{Sym}^k\mathbb{C}^2)`$ with $`\mathrm{Sym}^k\mathbb{C}^2`$ restricted to $`2I`$, and the lowest occupied level is $`k = \mathrm{dist}(\rho)`$ [Ko, Su]. No slot is carried by functions on $`X`$: every slot field lives on a twisted bundle.

In five of the slots, $`R_1, R_3, R_6, R_7`$ and $`R_8`$, and in the control, the restriction of $`\mathrm{Sym}^{\mathrm{dist}(\rho)}\mathbb{C}^2`$ to $`2I`$ is $`\rho`$ itself, and every lowest-level section has constant norm; we call these slots rigid. In the other three, the soft slots, $`R_2`$ at level 7 and $`R_4`$ and $`R_5`$ at level 6, the restriction is reducible, not every lowest-level section has constant norm, and the cubic term $`\lvert\psi\rvert^2\psi`$ of a lowest-level section need not lie in the lowest level [SA, § VI item 6; SGS, § VI].

These fields do not model physical matter: they are complex spacetime-scalar test fields carrying an internal $`2I`$ label. The slots of half-integer spin carry no Lorentz spinor index and no fermionic statistics, since their spin class records only the action of $`-I`$, and no spin-statistics relation is derived here. The action couples the fields to nothing else: to no other field, and to no dynamics of the metric [SA, § II].

### 2.2 The action

For each $`\rho`$ in $`R_0, \ldots, R_8`$, independently, the action of a section $`\psi`$ of $`E_\rho`$ over $`\mathbb{R} \times X`$ is

```math
\mathcal{S}_\rho[\psi] = -\frac{1}{2c}\int_{\mathbb{R}\times X} d^4x\,\sqrt{-g}\,\left[ g^{\mu\nu}\,(D_\mu\psi)^{\dagger} D_\nu\psi + \frac{g_4}{2}\,\lvert\psi\rvert^4 \right], \qquad g_4 = 1 ,
```

with $`D`$ the covariant derivative of the flat connection on $`E_\rho`$ and $`\lvert\cdot\rvert`$ the norm of the invariant Hermitian form on $`V_\rho`$. Its field equation is

```math
\frac{1}{c^2}\,\partial_T^2\psi \;-\; \Delta\psi \;+\; g_4\,\lvert\psi\rvert^2\psi \;=\; 0 ,
```

with the nonlinearity evaluated pointwise, $`\lvert\psi(x)\rvert^2\psi(x)`$ at each $`x \in X`$; putting the spatial integral of $`\lvert\psi\rvert^2`$ in place of $`\lvert\psi(x)\rvert^2`$ gives a different, nonlocal law. Standing waves $`\psi = e^{i\omega T}\varphi`$ solve

```math
\left(-\Delta - \frac{\omega^2}{c^2}\right)\varphi \;+\; g_4\,\lvert\varphi\rvert^2\varphi \;=\; 0 ,
```

which at $`R = 1`$ is the equation of [Sh, § 2.5] with its $`\lambda`$ equal to $`\omega^2/c^2`$; [Sh] quotients by right translation, the same structure under inversion [SA, § II, § V].

The action was selected and frozen on 2026-10-04, before any of the finite-amplitude runs this paper reports, under the rule that no target outcome, a stable branch among them, may choose any of its elements, and each element carries its own status [SA, § I, § IV]. One complex field for each slot, with no term coupling two slots, is adopted, and so is the classical scope; time is the Killing time $`T`$ of the static metric, an adopted convention; the quadratic operator is the wave operator of the twisted Laplacian, read from the slot bundles themselves; there is no mass, an adoption; for a nonzero quartic interaction, the defocusing choice $`g_4 > 0`$ keeps the energy bounded below, whereas $`g_4 < 0`$ makes it unbounded below; and $`g_4 = 1`$ is a classical normalization. Two choices are motivated rather than derived, the curvature coupling $`\xi = 0`$ and the density quartic $`(g_4/4)\lvert\psi\rvert^4`$ as the self-interaction, so the selection as a whole is motivated, not derived.

A scale-free action leaves free a dimensionless coupling $`\xi\,\mathcal{R}\,\lvert\psi\rvert^2`$ to the scalar curvature, and renormalizability requires such a term while leaving $`\xi`$ free [BC]. We take $`\xi = 0`$, minimal coupling, since the slot operator carries no curvature term. The named alternative is $`\xi = 1/6`$, the value at which the action is Weyl invariant and the one that Sonego and Faraoni derive "by applying the equivalence principle to the propagation of scalar waves" [SF], so the choice sits on one side of a published disagreement. On this arena $`\xi`$ shifts every level by $`6\xi/R^2`$, and no difference between slots depends on it at zero amplitude. At finite amplitude it matters: $`\xi = 1/6`$ puts the free frequencies on the resonant lattice $`\omega = c(k+1)/R`$, and $`\xi = 0`$ does not. The finite-amplitude results of this paper are results for $`\xi = 0`$ [SA, § IV item 4].

The density quartic is the only local quartic common to all the slots that is built from the invariant fibre metric alone, and it is the density-type interaction of [Sh], which calls it "a hypothesis and not a consequence"; that status carries over to every result below. A second local quartic, $`\lvert\psi^{T}C_\rho\psi\rvert^2`$ with $`C_\rho`$ the invariant bilinear form, vanishes identically in the quaternionic slots of § 2.3, where $`C_\rho`$ is antisymmetric, so it was never a candidate for a law common to all eight [SA, § IX, note of 2026-10-09 on the second quartic].

For any $`g_4 > 0`$ the rescaling $`\tilde\psi = \sqrt{g_4}\,\psi`$ maps the field equation to the one with $`g_4 = 1`$ and multiplies the action, the energy and the charge by $`1/g_4`$, so $`g_4`$ does not affect the classical existence and stability questions studied here [SA, § IV item 8].

### 2.3 Symmetries and conserved quantities

The Killing field $`\partial_T`$, the phase rotations $`\psi \mapsto e^{i\alpha}\psi`$ and the right translations of $`S^3`$, which commute with $`2I`$ and act on $`X`$ by isometries, give the conserved energy and charge

```math
\mathcal{E}_\rho = \int_X dV \left[ \frac{1}{2c^2}\,\lvert\partial_T\psi\rvert^2 + \frac{1}{2}\,\lvert\nabla\psi\rvert^2 + \frac{g_4}{4}\,\lvert\psi\rvert^4 \right],
\qquad
N_\rho = \frac{1}{c^2}\int_X dV\; \mathrm{Im}\left(\psi^{\dagger}\,\partial_T\psi\right),
```

and three conserved Noether charges of right $`SU(2)`$ [SA, § V].

There is more internal symmetry than this. Every irreducible representation of $`2I`$ has a real character, so $`\bar\rho \cong \rho`$, and a unitary $`C`$ with $`C\,\bar\rho(\gamma) = \rho(\gamma)\,C`$ for every $`\gamma \in 2I`$ makes $`\psi \mapsto C\bar\psi`$ an antilinear symmetry of the action, which reverses the sign of $`N_\rho`$. In the real slots and the control, $`R_0, R_3, R_4, R_5`$ and $`R_7`$, $`C\bar C = 1`$ and charge conjugation is a discrete $`\mathbb{Z}_2`$. In the quaternionic slots, $`R_1, R_2, R_6`$ and $`R_8`$, $`C\bar C = -1`$, so $`J\psi = C\bar\psi`$ is a quaternionic structure; with the phase it generates $`Sp(1)`$, which preserves $`\lvert\psi\rvert`$ pointwise and adds two conserved charges [SA, § IX, note of 2026-10-04 on the fibre symmetry].

A stability statement must therefore name the family it is made relative to. In $`R_2`$, a quaternionic soft slot, one $`Sp(1)`$ family holds distinct standing waves, because a standing wave selects one phase generator and the others do not commute with it. Their spectral stability need not agree, so it is assessed member by member (§ 4).

### 2.4 What the action settles by itself

The zero section is a global section of every $`E_\rho`$ and solves the field equation, so it is a background solution in every slot. About it the linearization is the free equation, and on a nontrivial $`E_\rho`$ we have $`-\Delta \ge \mathrm{dist}(\rho)(\mathrm{dist}(\rho)+2)/R^2 \ge 3/R^2`$, so no mode grows. On a nontrivial $`E_\rho`$ the conserved energy is bounded below by $`\tfrac12\int_X \left(\lvert\partial_T\psi\rvert^2/c^2 + (3/R^2)\lvert\psi\rvert^2\right) dV`$, so the zero section is also Lyapunov stable in the energy norm for as long as a solution exists [SA, § VI items 2 and 3].

In the rigid slots, with $`\pi`$ the representation of $`SU(2)`$ on $`\mathrm{Sym}^{\mathrm{dist}(\rho)}\mathbb{C}^2`$ and its restriction to $`2I`$ identified with $`\rho`$, every lowest-level section is the equivariant map $`\psi_v(x) = \pi(x/R)\,v`$ on $`S^3`$, and $`\lvert\psi_v\rvert = \lvert v\rvert`$ everywhere. The nonlinearity then acts on $`\psi_v`$ as multiplication by the constant $`g_4\lvert v\rvert^2`$, so $`\psi = e^{i\omega T}\psi_v`$ solves the field equation exactly, for every $`v`$, with

```math
\frac{\omega^2}{c^2} = \frac{\mathrm{dist}(\rho)\,\big(\mathrm{dist}(\rho)+2\big)}{R^2} + g_4\,\lvert v\rvert^2 :
```

an exact branch that keeps its profile at every amplitude [SA, § VI item 6]. Its stability is taken up in § 3.

The law has no localized standing wave in flat three-space, with or without a mass. For the flat-space reduced equation with a mass term, put $`\mu = m^2 - \omega^2/c^2`$, and call a profile localized when $`\varphi \in H^1(\mathbb{R}^3)`$ and the integrations by parts behind both identities below hold. Multiplying the equation by $`\bar\varphi`$ and integrating, and the Pohozaev identity in three dimensions, combine to

```math
\mu\int\lvert\varphi\rvert^2 + \frac{g_4}{4}\int\lvert\varphi\rvert^4 = 0,
\qquad
\int\lvert\nabla\varphi\rvert^2 = 3\mu\int\lvert\varphi\rvert^2 .
```

For $`g_4 > 0`$ the first forces $`\varphi = 0`$ when $`\mu \ge 0`$, and the second when $`\mu < 0`$ [SA, § VI item 7; § IX, note of 2026-10-09 on a mass and localized states].

On $`X`$ itself, localized states at the curvature scale are not excluded. At scales $`L`$ much smaller than $`R`$ the arena is flat to $`O(L^2/R^2)`$, so no localized state of size $`L \ll R`$ is expected; this is an inference, not a theorem [SA, § VI item 7; § VII]. Global standing waves are not particles, and no particle state is claimed.

## 3. Analytical branch structure

The rigid slots and the soft slots part at the first step. In a rigid slot the lowest-level family of § 2.4 solves the field equation exactly at every amplitude, and § 3.3 shows that it is the set of ground states at every charge. In a soft slot the cubic term of a lowest-level section need not lie in the lowest level (§ 2.1), and branches are born at small amplitude from the critical orbits of a reduced quartic: § 3.1 sets up that problem and lists the orbits in hand, § 3.2 shows that every nondegenerate orbit carries a branch, and so do two degenerate ones, and § 3.3 identifies, in $`R_4`$ and $`R_5`$ at sufficiently small charge, the ground-state sets with the stationary family of the coherent branch; in $`R_2`$ that identification stays open. The linear spectrum along the soft branches is the subject of § 4.

### 3.1 The soft slots' reduced quartic and its critical orbits

The soft slots are $`R_4`$ and $`R_5`$ at level $`n = 6`$ and $`R_2`$ at level $`n = 7`$, $`n = \mathrm{dist}(\rho)`$ as in § 2.1, with lowest eigenvalue $`\lambda_0 = n(n+2)/R^2`$ ([SSB] writes $`K`$ for the level). In each, the lowest eigenspace $`E_0`$ of $`-\Delta`$ on $`E_\rho`$ has complex dimension $`n + 1`$, and right translations act on it as the spin $`j = n/2`$ representation, so $`E_0 \cong V_j`$ isometrically, $`w \mapsto \psi_w`$. With $`V = 2\pi^2R^3/120`$ the volume of $`X`$, and with the Jensen ratio $`Q(w) = V\int_X\lvert\psi_w\rvert^4 dV/\big(\int_X\lvert\psi_w\rvert^2 dV\big)^2`$, which is 1 exactly when $`\lvert\psi_w\rvert`$ is constant, the reduced quartic is

```math
H(w) = \frac{1}{2}\int_X \lvert\psi_w\rvert^4\, dV = \frac{Q(w)\,\lVert w\rVert^4}{2V} .
```

The stationary symmetry group $`\Gamma`$ is right $`SU(2)`$ together with the fibre group of § 2.3: the phase and charge conjugation in $`R_4`$ and $`R_5`$, and $`Sp(1)`$ in $`R_2`$. It is compact, it acts orthogonally on $`E_0`$, and it leaves $`H`$ invariant [SSB, § I].

At a critical point $`u`$ of $`H`$ on the unit sphere, $`\lVert u\rVert = 1`$ and $`\nabla H(u) = 4H(u)\,u`$. Let $`K_u`$ be the tangent space of the orbit $`\Gamma u`$, which contains $`iu`$; let $`M_u = \mathrm{Hess}\,H(u) - 4H(u)`$, a symmetric real-linear map of $`E_0`$ that vanishes on $`K_u`$; and let $`N_u`$ be the orthogonal complement of $`u`$ and $`K_u`$, which $`M_u`$ preserves. The signature $`(n_-, n_0, n_+)`$ of the orbit is that of $`M_u`$ on $`N_u`$, and the orbit is nondegenerate when $`n_0 = 0`$. The slow matrix is $`S_u = iM_u`$, Hamiltonian for $`\sigma(x, y) = \mathrm{Re}\langle x, iy\rangle`$, and a nonzero frequency cluster $`\pm i\tau`$ of $`S_u`$ is Krein-definite when $`M_u`$ is definite on its real invariant subspace $`\ker(S_u^2 + \tau^2)`$; a simple pair always is [SSB, § I]. These objects carry the small-amplitude spectrum of § 4.

The two level-6 slots are one problem at leading order. The reduced quartic has a closed form [SGS, § IV]: among the spins 0 to 7 the group $`2I`$ has invariant vectors only at 0 and 6, and Schur orthogonality gives

```math
Q(w) = 1 + \beta_\rho\,\frac{\lVert (w w^{\dagger})_6 \rVert^2}{\lVert w\rVert^4},
\qquad
\beta_\rho = \frac{d\,(d-r)}{13\,r},
```

with $`(ww^{\dagger})_6`$ the spin-6 component of $`ww^{\dagger}`$ under conjugation, in the Hilbert–Schmidt norm, $`d = n + 1`$ and $`r = \dim V_\rho`$. So $`\beta_\rho`$ is 28/39 in $`R_4`$, 21/52 in $`R_5`$ and 24/13 in $`R_2`$. For spin 3 the last factor is the function $`\hat r_6(w)`$ whose critical geometry [Sh, § 7] describes, and $`Q`$ is an increasing affine function of it, so in $`R_4`$ and $`R_5`$ the critical orbits of $`H`$ on the unit sphere are those of $`\hat r_6`$ on $`\mathbb{P}(V_3)`$. Recoupled to the pairing channels, $`Q = \sum_J q_J f_J`$, with channel fractions $`f_J = \lVert[w \otimes w]_J\rVert^2/\lVert w\rVert^4`$ that sum to 1 and coefficients $`q_J`$ with $`q_J - 1`$ proportional to $`\beta_\rho`$ at a fixed block spin. Since 21/52 is 9/16 of 28/39, $`R_5`$ is $`R_4`$ with every $`q_J - 1`$ scaled by 9/16: the two slots share their critical orbits, their signatures and their small-amplitude types, with every eigenvalue of the slow matrix $`\widehat S_u`$ of § 4.1 scaled by exactly 9/16; the leading slow eigenvalues of the linearization also carry Theorem R's factor $`1/Q(u)`$ [SSB, §§ III, IV; SDC, § II].

In $`R_4`$ and $`R_5`$ the critical set is known within a stated class. A group of symmetries of $`\hat r_6`$, rotations acting together with phases, fixes a locus in $`\mathbb{P}(V_3)`$, and a critical point of $`\hat r_6`$ restricted to that locus is critical on all of $`\mathbb{P}(V_3)`$, by Palais' principle of symmetric criticality [Pa]. The orbit census of [Sh, § 7.2] takes every such locus of projective dimension at most one, six points and seven lines, finds the complete critical set on each line by elimination rather than by a numerical solver, and obtains exactly ten orbits modulo rotation and phase, each with its signature computed exactly from a characteristic polynomial. The orbit census was pre-registered by the author, reproduced blind twice, in separate runs, and graded sound under an adversarial audit [Sh, § 7.2; OW12, § 5]. We call a result an audited argument when an adversarial audit has graded its arguments sound but it is not verified as a theorem, and the orbit census stands as one. Exact arithmetic reproduces the ten orbits in value and signature [SSB, § IV]; that they are all the critical orbits of the class rests on the orbit census's elimination.

The class leaves out every orbit whose rotation stabiliser is $`C_2`$, or $`C_3`$ acting on a three-dimensional fixed space, or trivial, since the fixed loci of those groups have projective dimension two or more. Numerical searches of the critical set found three orbits outside it, $`\mathcal{O}_1, \mathcal{O}_2, \mathcal{O}_3`$ in increasing order of value, and the Surviving Ray certifies each with 60-digit interval arithmetic: inside the fixed set of its full isotropy, a Krawczyk inclusion on a box of radius $`10^{-55}`$ holds exactly one critical point, and a Gershgorin test fixes its signature [Sh, § 7.2]. Each is certified again on the full critical-point system, by a Krawczyk box of radius $`10^{-60}`$, with the same signatures, (4, 0, 5), (6, 0, 3) and (7, 0, 2) [SSB, § IV]. $`\mathcal{O}_3`$ is the third outside orbit that the orbit census's numerical probe found, and § 5 follows its branch to finite amplitude. The value of $`\mathcal{O}_2`$ lies in a certified interval that contains 28800/121, and it is not claimed to equal that fraction.

| orbit | representative | $`924\,\hat r_6`$ | $`(n_-, n_0, n_+)`$ |
|---|---|---|---|
| coherent $`v_3`$ | $`v_3`$ | 1 | (0, 0, 10) |
| $`v_2`$ | $`v_2`$ | 36 | (2, 0, 8) |
| trigonal prism | $`v_3 + \sqrt{23/10}\,v_0 + v_{-3}`$ | 8800/43 | (3, 0, 6) |
| $`v_1`$ | $`v_1`$ | 225 | (4, 2, 4) |
| D2 ray | $`v_2 + i\sqrt{6/5}\,v_0 + v_{-2}`$ | 225 | (5, 0, 4) |
| C3 ray | $`v_2 + 2v_{-1}`$ | 1188/5 | (5, 0, 4) |
| pentagonal pyramid | $`\sqrt{12}\,v_3 + \sqrt{13}\,v_{-2}`$ | 1188/5 | (5, 0, 4) |
| octahedron | $`v_2 + v_{-2}`$ | 288 | (6, 0, 3) |
| zonal $`v_0`$ | $`v_0`$ | 400 | (8, 0, 2) |
| hexagon | $`v_3 + v_{-3}`$ | 463 | (9, 0, 0) |
| $`\mathcal{O}_1`$ | interval-certified † | 215.7757925… | (4, 0, 5) |
| $`\mathcal{O}_2`$ | interval-certified † | 238.0165289… | (6, 0, 3) |
| $`\mathcal{O}_3`$ | interval-certified † | 238.3568547… | (7, 0, 2) |

*Table 2.* The thirteen critical orbits in hand in $`R_4`$ and $`R_5`$, at level 6. The first ten rows are the orbit census [Sh, § 7.2], their values and signatures exact [SSB, § IV] and their completeness within its class an audited argument; the last three are the orbits found outside that class, interval-certified [Sh, § 7.2; SSB, § IV]. Representatives are written in orthonormal Condon–Shortley components $`v_m = \lvert 3, m\rangle`$, unnormalized; the signatures are those of $`M_u`$ on $`N_u`$, the same in both slots. † No exact representative is in hand; the entry is [SSB, § IV]'s, whose rows give these values to more digits.

The identity of $`R_4`$ and $`R_5`$ is a leading-order one: at second order the pair Theorem R′(c) types at $`v_1`$ is Krein-negative in $`R_4`$ and Krein-positive in $`R_5`$, though imaginary in both (§ 4.2). At finite amplitude their fates part on the adjudicated runs of § 5: a change of type is located, between registered guard readings, for the prism in $`R_4`$ and for the hexagon in $`R_5`$, neither identified with a genuine crossing (§ 4.4), while the prism in $`R_5`$ and the hexagon in $`R_4`$ are elliptic at every point classified, up to their slots' spectral gaps [SDC, § III]. Those are OpenWave's adjudicated verdicts on its instruments, not theorems.

In $`R_2`$, at level 7, $`E_0 \cong V_{7/2}`$, and the fibre's quaternionic structure acts on $`E_0`$ as the quaternionic structure of $`V_{7/2}`$, up to a phase [SSB, § I]. The points examined are the weight states and the interior critical points of the seven cyclic fixed lines, each line spanned by two weights alone. Three of the lines, $`\lbrace 5/2, -5/2\rbrace`$, $`\lbrace 7/2, -7/2\rbrace`$ and $`\lbrace 3/2, -3/2\rbrace`$, are $`Sp(1)`$ orbits of weight states, on which $`Q`$ is constant, and Table 3 lists the weight states with the interior critical points of the other four, and their values of $`Q`$ [SSB, § IV].

| point | representative | $`Q`$ | $`(n_-, n_0, n_+)`$ |
|---|---|---|---|
| weight 7/2 | $`v_{7/2}`$ | 144/143 | (0, 0, 10) |
| weight 5/2 | $`v_{5/2}`$ | 168/143 | (4, 0, 6) |
| weight 3/2 | $`v_{3/2}`$ | 224/143 | (8, 0, 2) |
| weight 1/2 | $`v_{1/2}`$ | 168/143 | (4, 0, 6) |
| line {7/2, −5/2} | $`\sqrt{17/38}\,v_{7/2} + \sqrt{21/38}\,v_{-5/2}`$ | 369/247 | (6, 0, 3) |
| line {7/2, −3/2} | $`\sqrt{3/10}\,v_{7/2} + \sqrt{7/10}\,v_{-3/2}`$ | 22/13 | (9, 0, 0) |
| line {7/2, −1/2} | $`\sqrt{5/12}\,v_{7/2} + \sqrt{7/12}\,v_{-1/2}`$ | 193/143 | (5, 0, 4) |
| line {5/2, −3/2} | $`\sqrt{3/4}\,v_{5/2} + \sqrt{1/4}\,v_{-3/2}`$ | 161/143 | (0, 3, 6) |

*Table 3.* The points examined in $`R_2`$, at level 7 [SSB, § IV], with $`v_m = \lvert 7/2, m\rangle`$. The weight-7/2 orbit is a strict local minimum of $`Q`$ modulo its symmetry family; the point of the line {5/2, −3/2} is degenerate.

Neither critical set is known to be complete. In $`R_4`$ and $`R_5`$ the set is complete within the orbit census's class, by the audited elimination, and outside it the three orbits of Table 2 are the ones the numerical searches found; nothing says there are no others. In $`R_2`$ only the weight states and the cyclic fixed lines have been examined. Completeness of either set is open, and an orbit certified later would join the tables [SDC, § II; SSB, § V].

### 3.2 Branch existence

Every nondegenerate critical orbit carries a branch of standing waves at small amplitude. **Lemma G** [SSB, § II]. *Let $`\Gamma u`$ be a nondegenerate critical orbit and $`\kappa_u = 2H(u)`$. For small $`\varepsilon > 0`$ there are sections $`\varphi_\varepsilon \in H^2`$, smooth in $`\varepsilon`$, with $`\varphi_\varepsilon = (\varepsilon/g_4\kappa_u)^{1/2}\,(u + O(\varepsilon))`$, such that $`e^{i\omega T}\varphi_\varepsilon`$ with $`\omega^2 = c^2(\lambda_0 + \varepsilon)`$ solves the field equation. The isotropy group of $`\varphi_\varepsilon`$ in $`\Gamma`$ is exactly the isotropy group $`\Gamma_u`$ of $`u`$; near $`\Gamma u`$ the small solutions at that frequency are exactly the members of the stationary family $`\Gamma\varphi_\varepsilon`$; and the stationary operator*

```math
L_\varepsilon = -\Delta - \frac{\omega^2}{c^2} + g_4\left(\lvert\varphi_\varepsilon\rvert^2 + 2\varphi_\varepsilon\,\mathrm{Re}\left(\varphi_\varepsilon^{\dagger}\,\cdot\,\right)\right)
```

*on $`H^2`$ has kernel exactly the tangent space of that family.* How small $`\varepsilon`$ must be is not quantified.

The proof is a Lyapunov–Schmidt reduction. Since $`H^2`$ is an algebra contained in $`L^\infty`$ in three dimensions, the stationary equation is a smooth map from $`H^2`$ to $`L^2`$. With $`\omega^2/c^2 = \lambda_0 + \varepsilon`$ near $`\lambda_0`$ and $`\varphi = w + v`$, $`w \in E_0`$ and $`v`$ orthogonal to $`E_0`$, the operator $`-\Delta - \lambda_0 - \varepsilon`$ is invertible on the complement of $`E_0`$, and the implicit function theorem solves the complementary equation for a unique small $`v(w, \varepsilon)`$, $`\Gamma`$-equivariant and odd in $`w`$. The small solutions are then the critical points of the $`\Gamma`$-invariant reduced function $`f(w, \varepsilon) = -\tfrac{1}{2}\varepsilon\lVert w\rVert^2 + \tfrac{g_4}{2}H(w) + O(\lVert w\rVert^6)`$. After the scaling $`w = (\varepsilon/g_4)^{1/2}y`$, its leading part has the critical orbit through $`\kappa_u^{-1/2}u`$, with Hessian $`\kappa_u^{-1}M_u`$, nondegenerate on the normal space $`\mathbb{R}u \oplus N_u`$; the slice theorem and the implicit function theorem on a slice through that point give the branch, its isotropy and its kernel [SSB, § II].

At a degenerate orbit Lemma G does not apply, but symmetry can still pin a germ. For a critical point $`u`$ with isotropy group $`\Gamma_u`$, let $`X^u`$ be the closed subspace of sections that $`\Gamma_u`$ fixes, $`E_0^u = E_0 \cap X^u`$, a real subspace, $`\Gamma^u`$ the closed subgroup of $`\Gamma`$ that preserves $`X^u`$, and $`N_u^u`$ the orthogonal complement in $`E_0^u`$ of $`u`$ and the tangent space of $`\Gamma^u u`$. **Lemma G′** [SSB, § II]. *If $`M_u`$ is nondegenerate on $`N_u^u`$, in particular if $`N_u^u = 0`$, then for small $`\varepsilon > 0`$ there are sections $`\varphi_\varepsilon \in X^u \cap H^2`$ of Lemma G's form whose standing waves solve the field equation at $`\omega^2 = c^2(\lambda_0 + \varepsilon)`$, with isotropy group exactly $`\Gamma_u`$; near $`u`$ the small solutions in $`X^u`$ at that frequency are exactly the members of $`\Gamma^u\varphi_\varepsilon`$.* It claims nothing about solutions outside $`X^u`$, about the kernel of $`L_\varepsilon`$, or about stability. The proof is Lemma G's, run in $`X^u`$, which the field equation preserves.

Both degenerate orbits of the tables meet Lemma G′'s hypothesis in its simplest form, $`N_u^u = 0`$. In $`R_2`$, the point of the line {5/2, −3/2}, $`\sqrt{3/4}\,v_{5/2} + \sqrt{1/4}\,v_{-3/2}`$ with $`Q = 161/143`$ and signature (0, 3, 6), has an orbit of dimension $`6 = \dim\Gamma`$ and a finite isotropy group. That group contains the quarter-turn about $`z`$ and the half-turn about $`y`$, each with an element of the fibre group, and the point turned by $`\pi/4`$ about $`z`$ is fixed by the quarter-turn about $`x`$ with another, so the group also contains a quarter-turn about an axis perpendicular to $`z`$. The two quarter-turns generate the octahedral group, which no finite subgroup of $`SO(3)`$ properly contains, so the rotation part of $`\Gamma_u`$ is $`O`$. Its fixed space $`E_0^u`$ is the real line through the point, so $`N_u^u = 0`$: the slice is a point, the symmetry pins the germ, and Lemma G′ gives a branch with isotropy exactly $`\Gamma_u`$, unique in $`X^u`$ near the point. The computation is exact, over $`\mathbb{Q}(\sqrt 2, i)`$ [SSB, § II]. In $`R_4`$ and $`R_5`$, at $`v_1`$, with signature (4, 2, 4), the isotropy contains the circle $`R_z(\theta)e^{i\theta}`$, which acts on $`v_m`$ with weight $`1 - m`$, and the half-turn about $`y`$ with charge conjugation, which fixes $`v_1`$ too; so $`E_0^u = \mathbb{R}v_1`$, $`N_u^u = 0`$, and Lemma G′ gives the germ [SSB, § III].

The Surviving Ray gives local branch germs of the same kind, for the same equation on the lowest blocks of $`R_4`$ and $`R_5`$: at the six rays of [Sh, § 7.1], the coherent, zonal, octahedral and hexagonal rays, which the symmetry pins, and the pentagonal pyramid and the trigonal prism, and by the same theorem at the weight states $`v_1`$ and $`v_2`$, for sufficiently small amplitude, with no lower bound on it [Sh, § 8.3]. That theorem stands as an audited argument and, in that paper's words, "not a verified theorem". Nothing in this paper rests on it: every germ used below comes from Lemma G or Lemma G′.

### 3.3 Ground states and the rigid families

The branches above are solutions; the ground states are sets. The phase space is $`\mathcal{H} = H^1(X; E_\rho) \times L^2(X; E_\rho)`$, of pairs $`(\psi, \partial_T\psi)`$, in which solutions exist globally and conserve $`\mathcal{E}_\rho`$ and $`N_\rho`$ [SGS, § I], and for a charge $`N_0 \ne 0`$, $`G(N_0)`$ is the set of minimizers of $`\mathcal{E}_\rho`$ on $`\lbrace N_\rho = N_0\rbrace`$. **Theorem A** [SGS, § III]. *In every slot and in the control, at every charge $`N_0 \ne 0`$, the infimum of the energy is attained; every minimizer is a standing wave $`e^{i\omega T}\psi`$, with $`\omega`$ real and $`(-\Delta - \omega^2/c^2)\psi + g_4\lvert\psi\rvert^2\psi = 0`$, a ground state; and $`G(N_0)`$ is orbitally stable in $`\mathcal{H}`$: data close enough to $`G(N_0)`$ stay within any prescribed distance of it for all time.*

The proof is the constrained-minimization argument of Cazenave and Lions [CL], with Shatah's treatment of Klein–Gordon standing waves [Sha]: minimizing sequences are precompact on the compact manifold $`X`$, and the phase-space and charge steps of the Klein–Gordon setting are supplied in [SGS, § III]. Orbital stability here is a statement about the set $`G(N_0)`$, not about any one branch through it.

In the rigid slots the sets are known exactly, at every charge. **Theorem B** [SGS, § III]. *In $`R_1, R_3, R_6, R_7, R_8`$ and the control, with $`n = \mathrm{dist}(\rho)`$, $`\lambda_0 = n(n+2)/R^2`$ and $`\psi_v`$ as in § 2.4, let $`m`$ be the unique positive root of $`c^2N_0^2/m^2 = \lambda_0 + g_4m/V`$. Then*

```math
G(N_0) = \left\lbrace \left(\psi_v,\ i\omega\,\psi_v\right) \;:\; \lvert v\rvert^2 = \frac{m}{V} \right\rbrace,
\qquad
\omega = \frac{c^2N_0}{m},
\qquad
\frac{\omega^2}{c^2} = \lambda_0 + g_4\lvert v\rvert^2 ,
```

*the exact lowest-level family of § 2.4 at that frequency. It is orbitally stable as a set at every nonzero charge, and along each direction of $`v`$ it is a branch continuous in the charge.* The proof is an equality case. The energy at fixed charge is bounded below by a function of $`m = \int_X\lvert\psi\rvert^2 dV`$ alone, through Cauchy–Schwarz on the charge, the spectral bound and Jensen's inequality, and a lowest-level section of constant norm meets all three with equality. With each member the set contains the profiles that the phase, right translations and the fibre symmetry produce from it, so the claim is about the family as a set.

Their linear spectrum is as explicit. Write a member as $`e^{i\omega T}\psi_v`$, put $`\psi = e^{i\omega T}(\psi_v + \zeta)`$, and linearize the field equation in $`\zeta`$. **Theorem D** [SGS, § V]. *The whole spectrum of the linearization lies on the imaginary axis. The linearization preserves the splitting of $`\zeta`$ into its part in $`E_0`$ and the rest. On $`E_0`$ its eigenvalues are 0, with algebraic multiplicity $`2n + 2`$ and geometric multiplicity $`2n + 1`$; $`\pm 2i\omega`$, each $`n`$ times, from the complex directions orthogonal to $`v`$; and $`\pm i\left(4\omega^2 + 2g_4c^2\lvert v\rvert^2\right)^{1/2}`$, from the direction of $`v`$. Off $`E_0`$ the conserved quadratic form is positive definite, so the spectrum there consists of imaginary eigenvalues, none of them 0.* The kernel is exactly the tangent space at $`v`$ of the sphere $`\lvert v'\rvert = \lvert v\rvert`$, the members of the family at the same charge, and the one further generalized eigenvector at zero is the family's derivative in the charge. So the zero eigenvalue is not semisimple: in a fixed rotating frame the charge direction drifts linearly, and the claim is spectral stability, not bounded linearized evolution about one member at a fixed frequency. The nonlinear stability of the family is Theorem B's.

In the soft slots the ground states exist by Theorem A, and the question is what they are. In $`R_4`$ and $`R_5`$ none lies entirely in the lowest free eigenspace, at any nonzero charge: a lowest-level standing wave must have constant norm, and every symmetric-channel coefficient, the only kind that $`w \otimes w`$ meets, exceeds 1, the smallest being $`q_6`$, which is 1288/1287 in $`R_4`$ and 2289/2288 in $`R_5`$, so $`Q > 1`$ on all of $`E_0`$ [SGS, § IV, Proposition C, item 1]. At sufficiently small charge the minimizing sets are identified, though not in closed form. The coherent orbit, the first row of Table 2, is the unique minimizer of $`Q`$ on $`E_0`$, and there is an $`N_* > 0`$, depending only on the slot, $`g_4`$, $`c`$ and $`R`$, such that for $`0 < \lvert N_0\rvert \le N_*`$ every ground state concentrates on the lowest level, with its part off that level of relative order $`\lvert N_0\rvert`$, bounded above and below, and its frequency tending to $`\mathrm{sgn}(N_0)\,c\sqrt{\lambda_0}`$, the lowest free frequency with the sign of the charge, and $`G(N_0)`$ is the stationary family of the locally constructed branch of Lemma G through the coherent orbit, one orbit of $`\Gamma`$ [SGS, § IV, Proposition C, item 3]. So in $`R_4`$ and $`R_5`$ the ground-state sets at small charge form a branch, continuous in the charge. $`N_*`$ is not explicit, since the proof uses a compactness step.

At every charge the soft slots' ground states obey explicit bounds. Let $`q`$ be the value of $`Q`$ at a coherent unit vector of $`E_0`$: $`q_6`$ in $`R_4`$ and $`R_5`$, and $`q_7 = 144/143`$ in $`R_2`$. With $`m = \int_X\lvert\psi\rvert^2 dV`$, $`\varepsilon = \omega^2/c^2 - \lambda_0`$, $`\psi_\perp`$ the part of $`\psi`$ orthogonal to $`E_0`$ and $`\lambda_1`$ the next eigenvalue of $`-\Delta`$ on $`E_\rho`$, every ground state, in every soft slot and at every charge $`N_0 \ne 0`$, satisfies [SGS, § IV, Proposition C, item 4]

```math
\frac{g_4m}{V} \le \varepsilon \le \frac{q\,g_4m}{V},
\qquad
\frac{V}{m^2}\int_X\left(\lvert\psi\rvert^2 - \frac{m}{V}\right)^2 dV \le q - 1,
\qquad
\frac{\lVert\psi_\perp\rVert^2}{\lVert\psi\rVert^2} \le \frac{(q - 1)\,\varepsilon}{2(\lambda_1 - \lambda_0)} .
```

The gap $`\lambda_1 - \lambda_0`$ is $`72/R^2`$ in $`R_4`$, $`32/R^2`$ in $`R_5`$ and $`132/R^2`$ in $`R_2`$, so while $`\varepsilon`$ is at most the gap, the part off the lowest level is at most 2.0%, 1.5% and 6.0% of the norm, and its share of $`m`$ at most 0.039%, 0.022% and 0.35%. For larger $`\varepsilon`$ the last bound still holds, and grows linearly in $`\varepsilon`$. The proposition bounds the profile and the frequency only: it decides no ground-state set, orbit or branch.

What stays open is the identification beyond those limits. Beyond small charge in $`R_4`$ and $`R_5`$, and at every charge in $`R_2`$, it is open whether the ground states form branches, what their shape is, and whether each set is one orbit. In $`R_2`$ it is also open whether a ground state can lie entirely in the lowest eigenspace, which holds exactly when that eigenspace contains a section of constant norm, a unit vector $`w`$ with $`(ww^{\dagger})_6 = 0`$ and $`Q = 1`$: Proposition C, item 2 [SGS, § IV]. The smallest $`Q`$ found numerically is the weight-7/2 orbit's 144/143, and its global minimality would settle that question, since $`Q`$ would then exceed 1 on the whole block; that globality is not proved [SGS, § VII; SSB, § VI].

## 4. Linearized spectral stability

This section linearizes the field equation about the branches of § 3.2, in the frame that rotates with each branch's phase. At small amplitude the slow part of the spectrum is read off the reduced quartic: Theorem R at every nondegenerate orbit (§ 4.1), Theorem R′ at the two degenerate ones (§ 4.2), and Proposition N one order further (§ 4.3). At any amplitude, on a branch whose existence is assumed, a Hamiltonian–Krein count ties the unstable and Krein-negative eigenvalues to the negative directions of the stationary operator, and a transversal crossing of that operator splits its new kernel directions into three cases, only one of which moves pairs between real and imaginary (§ 4.4). The claim throughout is spectral stability, and orbital stability is claimed only where it is stated. Where a letter of [SSB] names another object here, the paper renames it: the slow eigenvalues' factor is $`\chi`$ (its $`\kappa`$), the Hessian's term of order $`\varepsilon`$ in Theorem R′ is $`D_u`$ (its $`D`$), and the spherical Hessian form is $`\mathsf{G}_u`$ (its $`\Gamma_u`$).

### 4.1 The small-amplitude spectrum

Fix a branch of Lemma G, with $`\omega_\varepsilon = c(\lambda_0 + \varepsilon)^{1/2}`$ and $`\omega_0 = c\sqrt{\lambda_0}`$. Writing $`\psi = e^{i\omega_\varepsilon T}(\varphi_\varepsilon + \zeta)`$, the linearized equation

```math
\frac{1}{c^2}\left(\partial_T^2\zeta + 2i\omega_\varepsilon\,\partial_T\zeta\right) + L_\varepsilon\zeta = 0
```

is a real-linear system $`\dot x = A_\varepsilon x`$ on $`\mathcal{H}`$, with $`x = (\zeta, \partial_T\zeta)`$. A standing wave is elliptic when the spectrum of $`A_\varepsilon`$ lies on the imaginary axis, and hyperbolic when it does not; a change of type is a passage between the two along a branch, and a branch is born elliptic when it is elliptic at small amplitude. It conserves $`H_2(x) = \lVert\partial_T\zeta\rVert^2/2c^2 + \tfrac{1}{2}\langle L_\varepsilon\zeta, \zeta\rangle = \tfrac{1}{2}B(x, x)`$, the second variation of $`\mathcal{E}_\rho - \omega_\varepsilon N_\rho`$ at the standing wave, and it is Hamiltonian, $`\Omega(A_\varepsilon x, y) = B(x, y)`$, for the symplectic form

```math
\Omega(x_1, x_2) = \frac{1}{c^2}\,\mathrm{Re}\left(\langle\zeta_1, \dot\zeta_2\rangle - \langle\dot\zeta_1, \zeta_2\rangle + 2\omega_\varepsilon\langle\zeta_1, i\zeta_2\rangle\right),
```

which on static vectors is $`(2\omega_\varepsilon/c^2)\,\sigma`$. The kernel of $`A_\varepsilon`$ consists of the static vectors $`(\zeta, 0)`$ with $`L_\varepsilon\zeta = 0`$: by Lemma G, the tangent space of the stationary family, of dimension $`k = \dim K_u`$. In $`R_2`$ it includes the $`Sp(1)`$ directions, which are static solutions but not symmetries of the rotating frame [SSB, § III].

**Lemma S** [SSB, § III]. *For small $`\varepsilon`$, $`\Omega`$ is nondegenerate on the spectral subspace of $`A_\varepsilon`$ inside a fixed small circle about 0, and so are the generalized kernel and the sum of the generalized eigenspaces of each nonzero cluster $`\lbrace\pm\lambda, \pm\bar\lambda\rbrace`$ within it.* The slow subspace is $`\Omega`$-orthogonal to the fast one, and $`\Omega`$ is weakly nondegenerate on $`\mathcal{H}`$, which gives the first claim. $`A_\varepsilon`$ is $`\Omega`$-skew, so generalized eigenspaces for eigenvalues $`\lambda`$ and $`\mu`$ with $`\lambda + \mu \ne 0`$ are $`\Omega`$-orthogonal, and a subspace orthogonal to its complement in a nondegenerate space is itself nondegenerate.

Theorem R uses the objects of § 3.1 in the normalization $`2VH = Q\lVert w\rVert^4`$: $`\widehat M_u = 2VM_u`$ and $`\widehat S_u = i\widehat M_u`$. Write $`r_u`$ for the dimension of the $`\sigma`$-radical of $`K_u`$, which always contains $`iu`$. At a nondegenerate orbit $`\ker\widehat S_u = K_u`$, and every radical vector has a partner, so the zero eigenvalue of $`\widehat S_u`$ has multiplicity at least $`k + r_u`$. Hypothesis (Z) is that it has multiplicity exactly $`k + r_u`$, and that the $`\Omega`$-radical of $`\ker A_\varepsilon`$ has dimension $`r_u`$ [SSB, §§ I, III].

**Theorem R** [SSB, § III]. *Let $`\Gamma u`$ be a nondegenerate critical orbit with branch $`\varphi_\varepsilon`$. There is $`\varepsilon_1 > 0`$ such that for $`0 < \varepsilon < \varepsilon_1`$: (a) the spectrum of $`A_\varepsilon`$ consists of a slow part, $`2d`$ eigenvalues $`\varepsilon(\chi s + o(1))`$, with $`s`$ running over the eigenvalues of $`\widehat S_u`$ and $`\chi = c^2/(8\omega_0 Q(u)) > 0`$, and a fast part on the imaginary axis, bounded away from 0; (b) if $`\widehat S_u`$ has an eigenvalue with positive real part, so does $`A_\varepsilon`$, and the branch is spectrally unstable; (c) if $`n_- = 0`$, the spectrum of $`A_\varepsilon`$ is imaginary, and the stationary family is orbitally stable as a set; (d) if $`n_+ = 0`$, the spectrum of $`A_\varepsilon`$ is imaginary; (e) if the nonzero eigenvalues of $`\widehat S_u`$ are imaginary and Krein-definite and (Z) holds, the spectrum of $`A_\varepsilon`$ is imaginary.* In (c) to (e) the claim is spectral stability at small amplitude, and only (c) also gives orbital stability.

The proof splits the spectrum by a Riesz projection [Ka]. At $`\varepsilon = 0`$ the eigenvalue 0 is semisimple, with eigenspace $`E_0 \times \lbrace 0\rbrace`$, and $`H_2`$ is coercive on the spectral complement of that kernel; $`A_\varepsilon - A_0`$ is bounded and of size $`O(\varepsilon)`$. So the projection for a small circle about 0 has rank $`2d`$, the fast part keeps a coercive conserved form and so an imaginary spectrum, and Kato's first-order reduction carries $`A_\varepsilon`$ on the slow part to $`\varepsilon\chi\widehat S_u + o(\varepsilon)`$, with $`B`$ there equal to $`(\varepsilon/4Q(u))\langle\widehat M_u\,\cdot, \cdot\rangle + o(\varepsilon)`$. Item (b) follows by continuity; (c) and (d) from the sign of $`B`$ on the slow part, with the phase mode and its partner split off in (d); and (e) from the partners of the radical, the exact count of zeros under (Z), and a conserved definite form on each Krein-definite cluster. Orbital stability in (c) holds because the family is a compact nondegenerate critical manifold of the conserved functional $`\mathcal{E}_\rho - \omega_\varepsilon N_\rho`$, its Hessian coercive on the normal bundle [SSB, § III].

In $`R_2`$ an orbit contains its $`Sp(1)`$ family of distinct standing waves, and Theorem R applies at each member, whose slow matrix is that of $`u`$ for another complex structure, conjugated by the fibre element. Definiteness, and with it (c) and (d), holds along the whole family, uniformly by compactness, but the type of an indefinite orbit can change along it, so it is assessed member by member, as § 2.3 requires [SSB, § III].

Tables 4 and 5 give the small-amplitude type of every orbit of Tables 2 and 3. Each is computed in exact arithmetic where the orbit has an exact representative: the signature from the characteristic polynomial of $`\widehat M_u`$ by exact root counts, the type from the characteristic polynomial of $`\widehat S_u`$ in $`\nu = s^2`$, with its zero roots removed, elliptic exactly when all the remaining roots are negative reals, and Krein-definiteness from $`\widehat M_u`$ on each cluster's invariant subspace. At the three outside orbits the same steps run in interval arithmetic at their certified points [SSB, § IV]. In $`R_4`$ and $`R_5`$ the coherent orbit is a minimum, spectrally and orbitally stable; $`v_2`$, the prism and $`\mathcal{O}_3`$ meet (e), $`v_2`$ with clusters of both Krein signs and the prism Krein-positive; the hexagon is a maximum, Krein-negative; and the D2 ray, the C3 ray, the pyramid, the octahedron, the zonal ray, $`\mathcal{O}_1`$ and $`\mathcal{O}_2`$ are spectrally unstable. In $`R_2`$ the weight-7/2 orbit is a minimum along its family; the weight-5/2 and weight-3/2 orbits are elliptic at the point and hyperbolic along the family, so some of their members are unstable; the weight-1/2 orbit and the lines {7/2, −5/2} and {7/2, −1/2} are spectrally unstable; and the line {7/2, −3/2} is a maximum, Krein-negative and definite along its family [SSB, § IV; SDC, § III]. The two degenerate orbits are § 4.2's.

| orbit | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow | type |
|---|---|---|---|---|
| coherent $`v_3`$ | (0, 0, 10) | 3, 1 | elliptic, simple; Krein + | (c): spectrally and orbitally stable |
| $`v_2`$ | (2, 0, 8) | 3, 1 | elliptic, simple; Krein 4+, 1− | (e): spectrally stable |
| trigonal prism | (3, 0, 6) | 4, 4 | elliptic, one double frequency; Krein + | (e): spectrally stable |
| $`v_1`$ † | (4, 2, 4) | degenerate | not decided at first order | Theorem R′(c): spectrally stable |
| D2 ray | (5, 0, 4) | 4, 4 | hyperbolic, real pairs | (b): unstable |
| C3 ray | (5, 0, 4) | 4, 2 | hyperbolic, a complex quartet | (b): unstable |
| pentagonal pyramid | (5, 0, 4) | 4, 2 | hyperbolic, a complex quartet | (b): unstable |
| octahedron | (6, 0, 3) | 4, 4 | hyperbolic, real pairs | (b): unstable |
| zonal $`v_0`$ | (8, 0, 2) | 3, 3 | hyperbolic, real pairs | (b): unstable |
| hexagon | (9, 0, 0) | 4, 4 | elliptic, one double frequency; Krein − | (d): spectrally stable |
| $`\mathcal{O}_1`$ | (4, 0, 5) | 4, 2 | hyperbolic, one real pair | (b): spectrally unstable |
| $`\mathcal{O}_2`$ | (6, 0, 3) | 4, 2 | hyperbolic, one real pair | (b): spectrally unstable |
| $`\mathcal{O}_3`$ (the third outside orbit) | (7, 0, 2) | 4, 2 | elliptic, simple | (e): spectrally stable |

*Table 4.* The small-amplitude types in $`R_4`$ and $`R_5`$, the same in both slots [SSB, § IV; Sh, § 7.2]: the signature, the orbit's dimension $`k`$ and the radical's dimension $`r_u`$, the slow flow of $`\widehat S_u`$, with each cluster's Krein sign, the sign of $`\widehat M_u`$ on it, and the stability theorem and item that apply. The rows with exact representatives are exact; the three outside orbits are interval-certified at their certified points. † Typed at second order by Theorem R′ [SSB, § III], as § 4.2 sets out.

| point | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow at the point | along the family | type |
|---|---|---|---|---|---|
| weight 7/2 | (0, 0, 10) | 5, 1 | elliptic, simple; Krein + | definite | (c): spectrally and orbitally stable, along the family |
| weight 5/2 | (4, 0, 6) | 5, 1 | elliptic | hyperbolic | (b): unstable members |
| weight 3/2 | (8, 0, 2) | 5, 1 | elliptic | hyperbolic | (b): unstable members |
| weight 1/2 | (4, 0, 6) | 5, 1 | hyperbolic | | (b): unstable |
| line {7/2, −5/2} | (6, 0, 3) | 6, 2 | hyperbolic | | (b): unstable |
| line {7/2, −3/2} | (9, 0, 0) | 6, 4 | elliptic; Krein − | definite | (d): spectrally stable along the family |
| line {7/2, −1/2} | (5, 0, 4) | 6, 2 | hyperbolic | | (b): unstable |
| line {5/2, −3/2} † | (0, 3, 6) | degenerate | not decided at first order | | Theorem R′(b): spectrally and orbitally stable, along the family |

*Table 5.* The small-amplitude types in $`R_2`$ [SSB, § IV]. All rows are exact. The column "along the family" reads the members whose complex structure is $`j`$, $`k`$, $`(i + j)/\sqrt 2`$ or $`(i + k)/\sqrt 2`$; "definite" holds at every member. † Typed at second order by Theorem R′ [SSB, § III]; see § 4.2.

Theorem R does not give $`\varepsilon_1`$, and its size is open: whether a run's smallest registered amplitude lies below it is not known in general [SDC, § IV]. Below $`\varepsilon_1`$ the structural slow eigenvalues are exactly zero, and at an orbit meeting (e) every other slow eigenvalue is an imaginary, Krein-definite pair at a distance of order $`\varepsilon`$ from zero, so no slow mode can merge with a structural one there. For the $`v_2`$ branch, that the smallest amplitude of OpenWave's M8.15 run [OW15] lies below $`\varepsilon_1`$ is inferred, not derived: at that amplitude, the branch's four slow modes other than the Krein-negative one agree with Theorem R's prediction within 0.80% in $`R_4`$ and 1.22% in $`R_5`$ [SDC, § IV]. Section 5 reads that run's records against this.

### 4.2 The degenerate orbits

At a degenerate orbit Theorem R leaves the kernel of $`M_u`$ on $`N_u`$ undecided at order $`\varepsilon`$, and the reduced function is needed one order further. In Lemma G's scaling the reduced function is $`(\varepsilon^2/2g_4)\,\tilde f(y, \varepsilon)`$, with $`\tilde f(y, \varepsilon) = H(y) - \lVert y\rVert^2 + \varepsilon\tilde R(y, \varepsilon)`$ [SSB, § II]. **Lemma F** [SSB, § III]. *The first correction is $`\tilde R(y, 0) = \tilde R_0(y)`$, with*

```math
\tilde R_0(y) = -\big\langle L_0^{-1}P_\perp N(\psi_y),\ P_\perp N(\psi_y)\big\rangle, \qquad N(\psi) = \lvert\psi\rvert^2\psi,
```

*where $`L_0 = -\Delta - \lambda_0`$ is inverted on the complement of $`E_0`$ and $`P_\perp`$ projects onto that complement. In the soft slots, at level $`n`$ and spin $`j = n/2`$,*

```math
\tilde R_0(y) = -\frac{R^2}{s^3V^2}\sum_{J \ne j}\frac{t_J}{(2J+1)\,\mu_J}\,\big\lVert[Y_6(y)\otimes y]_J\big\rVert^2,
```

*where $`s = \dim V_\rho/(2j+1)`$, which is 3/7 in $`R_4`$, 4/7 in $`R_5`$ and 1/4 in $`R_2`$; $`Y_6(y)`$ is the spin-6 part of $`yy^{\dagger}`$ and $`[\,\cdot\,]_J`$ the part of $`V_6 \otimes V_j`$ of spin $`J`$; $`\mu_J = 2J(2J+2) - n(n+2)`$ is the gap of level $`2J`$ over level $`n`$; and the constants $`t_J`$, from the coupling of the slot projector's spin-6 part to spin $`J`$, are given in closed form there.* The nonzero $`t_J`$ fall at levels 10, 14, 16 and 18 in $`R_4`$, at 8, 12, 14, 16 and 18 in $`R_5`$, and at 13, 17 and 19 in $`R_2`$. In $`R_4`$ and $`R_5`$ the closed form reproduces exactly the values that OpenWave's M8.10 run froze beforehand: its 36 level norms, its eight values of $`\lambda_4/g^2`$, and its level sets [SSB, § III; OW10].

**Theorem R′** [SSB, § III]. *Let $`u`$ be a degenerate critical point whose germ comes from Lemma G′, with $`E_0^u \subset \mathbb{C}u`$, let $`K' = \ker M_u \cap N_u`$, and let $`\gamma_u`$ be the symmetric form $`\kappa_u^{-2}\big(\mathrm{Hess}\,\tilde R_0(u) - 6\tilde R_0(u)\big)`$ restricted to $`K'`$, taken relative to the metric. (a) At the germ, $`\mathrm{Hess}_y\tilde f(y_\varepsilon, \varepsilon) = \kappa_u^{-1}M_u + \varepsilon D_u + O(\varepsilon^2)`$, where $`y_\varepsilon`$ is the germ in Lemma G's scaling, and $`D_u`$ annihilates $`K_u`$ and is $`\gamma_u`$ on $`K'`$. (b) If $`n_- = 0`$ and $`\gamma_u`$ is positive definite, then for small $`\varepsilon > 0`$, $`L_\varepsilon \ge 0`$ with kernel exactly the tangent space of the stationary family; the spectrum of $`A_\varepsilon`$ is imaginary, and the family is orbitally stable, in $`R_2`$ along the family. (c) If $`\Gamma_u`$ contains a circle acting complex-linearly, and $`K'`$ is a whole isotypic component of it in $`E_0`$, of dimension 2 and nonzero weight, then $`\gamma_u`$ is a multiple of the metric, and that component's pair is imaginary for every small $`\varepsilon`$, at $`\pm i\varepsilon^2(c^2/4\omega_0)\,\gamma_u(1 + O(\varepsilon))`$ when $`\gamma_u \ne 0`$; if Theorem R(e)'s hypotheses hold for $`\widehat S_u`$ on the other components, the spectrum of $`A_\varepsilon`$ is imaginary.* As in Theorem R the claims are at small amplitude, and only (b) is orbital. Item (a) follows from the germ's radial correction and Lemma F; (b) and (c) then follow as Theorem R(c) and (e) do, in (c) with the circle, which commutes with $`A_\varepsilon`$, splitting off the two-dimensional component [SSB, § III].

At $`R_2`$'s degenerate point, the point of the line {5/2, −3/2}, $`K'`$ has dimension 3, and $`\Gamma_u`$, of order 24, acts on it absolutely irreducibly, so $`\gamma_u`$ is a multiple of the metric. Lemma F's sum runs over levels 13, 17 and 19 and gives $`\gamma_u = (115020/20333173)\,R^2`$, positive, with $`n_- = 0`$, so by (b) the branch is spectrally and orbitally stable at small amplitude, along its family; the computation is exact. In a finite-dimensional model of the slow problem the four eigenvalues that leave zero do so at two orders, $`\varepsilon^2`$ and $`\varepsilon^{3/2}`$, imaginary and Krein-positive. Those rates are diagnostics of the model, not derived asymptotics of the full linearization, and the type does not rest on them [SSB, § III].

At $`v_1`$, in $`R_4`$ and $`R_5`$, the component of weight 4 under the circle $`R_z(\theta)e^{i\theta}`$ is $`\mathbb{C}v_{-3}`$, which is $`K'`$, and the circle commutes with $`M_u`$ and $`i`$, so Theorem R′(c) applies: that pair is imaginary for every small $`\varepsilon`$. Its $`\gamma_u`$ is $`-(19919/6697728)\,R^2`$ in $`R_4`$, so the pair is Krein-negative, and $`(224487/41628563)\,R^2`$ in $`R_5`$, Krein-positive, both exact. On the other components $`\widehat S_u`$ has its zero of multiplicity exactly $`4 = k + r_u`$ and four simple negative roots of its slow polynomial, and the momentum of the right translations, nonzero at $`v_1`$, keeps $`r_u = 1`$ along the branch. So Theorem R(e)'s hypotheses hold there, and the branch is spectrally stable at small amplitude in both slots [SSB, § III].

Neither degenerate branch is followed to finite amplitude. Their new slow pairs are far smaller than Theorem R(a)'s, of order $`\varepsilon^2`$ at $`v_1`$, so a numerical study of either would need adequacy tests that resolve them, under a pre-registration of its own. The census of § 5 leaves both outside its program, and their finite-amplitude fate is open [SDC, § V, step 5; § VIII].

### 4.3 The next order

Theorem R(a) gives the slow eigenvalues at a nondegenerate orbit as $`\varepsilon(\chi s + o(1))`$, and says nothing of the size of the $`o(1)`$ term; Proposition N gives the next term in closed form. Fix a nondegenerate orbit with its branch. $`\tilde R_0`$ is $`\Gamma`$-invariant, so $`\nabla\tilde R_0(u)`$ lies in $`\mathbb{R}u \oplus N_u`$, where $`M_u`$ is invertible; let $`\hat z \in \mathbb{R}u \oplus N_u`$ solve $`M_u\hat z = \nabla\tilde R_0(u)`$, and put

```math
D_u = \kappa_u^{-2}\big(\mathrm{Hess}\,\tilde R_0(u) - D^3H(u)[\hat z]\big),
```

the part of order $`\varepsilon`$ of the Hessian at the germ. A slow group $`g`$ is a nonzero eigenvalue $`s_g`$ of $`\widehat S_u`$, with $`\mu_0 = \chi s_g`$, together with the slow eigenvalues of $`A_\varepsilon`$ near $`\varepsilon\mu_0`$. **Proposition N** [SSB, § III]. *For a slow group $`g`$, let*

```math
T_1 = \frac{c^2}{4\omega_0}\, iD_u - \frac{c^2}{2\omega_0^2}\,\mu_0 + \frac{\mu_0^2}{2\omega_0}\, i,
```

*and let $`r_a`$ and $`\ell_a`$ be right and left eigenvectors of $`\widehat S_u`$ for $`s_g`$, with $`\ell_a^{T}r_b = \delta_{ab}`$. (a) If $`s_g`$ is simple, then for small $`\varepsilon > 0`$, $`A_\varepsilon`$ has exactly one eigenvalue near $`\varepsilon\mu_0`$, smooth in $`\varepsilon`$, with $`\lambda_g(\varepsilon) = \varepsilon\mu_0 + \varepsilon^2c_g + O(\varepsilon^3)`$ and $`c_g = \ell^{T}T_1r`$. (b) If $`s_g`$ is semisimple of multiplicity $`m`$, and $`C_{ab} = \ell_a^{T}T_1r_b`$, the $`m`$ slow eigenvalues near $`\varepsilon\mu_0`$ are $`\varepsilon\mu_0 + \varepsilon^2c_a`$ plus remainders, with the $`c_a`$ the eigenvalues of $`C`$, counted algebraically, the remainders $`o(\varepsilon^2)`$ in general and $`O(\varepsilon^3)`$ when $`C`$ is semisimple, and their mean $`\varepsilon\mu_0 + \varepsilon^2\,\mathrm{tr}\,C/m + O(\varepsilon^3)`$.* The zero eigenvalues are not expanded, and no range of $`\varepsilon`$ is claimed in which two terms suffice. The proof reduces the eigenvalue problem to $`E_0`$ by a Schur complement, inserts the Hessian at the germ and the frequency's first shift, and applies the implicit function theorem at a simple eigenvalue, and Rouché's theorem and the argument principle at a semisimple one [SSB, § III].

Two Euler identities put the radial part of $`\hat z`$ at $`(3\tilde R_0(u)/2\kappa_u)\,u`$. With $`\hat z_{\mathrm{off}} \in N_u`$ the rest of $`\hat z`$,

```math
D_u = \mathsf{G}_u - 3\kappa_u^{-3}\tilde R_0(u)\,M_u - \kappa_u^{-2}D^3H(u)[\hat z_{\mathrm{off}}], \qquad \mathsf{G}_u = \kappa_u^{-2}\big(\mathrm{Hess}\,\tilde R_0(u) - 6\tilde R_0(u)\big),
```

so $`c_g`$ has five parts: the spherical Hessian, $`(c^2/4\omega_0)\,\ell^{T}i\mathsf{G}_ur`$; the amplitude, $`-3\kappa_u^{-2}\tilde R_0(u)\,\mu_0`$, the same relative shift for every group; the germ's off-ray shift, which is 0 when the germ stays on the ray through $`u`$; the frequency, $`-(c^2/2\omega_0^2)\,\mu_0`$; and $`\lambda^2`$, $`(\mu_0^2/2\omega_0)\,\ell^{T}ir`$. On $`K'`$ at a degenerate orbit whose germ is radial, $`D_u = \mathsf{G}_u = \gamma_u`$, Theorem R′'s form. Five cases are evaluated: the pyramid in $`R_4`$, and the coherent orbit in $`R_4`$ and in $`R_5`$, the weight-7/2 orbit in $`R_2`$ and the octahedron in $`R_4`$, the branches that OpenWave's M8.16 run used as controls [OW16]. At each, $`D_u`$ and the zero multiplicities of $`\widehat S_u`$ are exact, and (Z) holds [SSB, § III].

The coefficients' values are floating point at 50 digits, from the exact $`D_u`$, and are graded as inferred, not derived; none is fitted. At the pyramid the relative coefficient $`c_g/(\chi s_g)`$ has modulus 0.2362 for the quartet and 0.01386 for the Krein-negative pair, the pair [SSB, § III] calls in-span, a ratio of 17.04. The spherical part is of one size for both groups, and the pair's small coefficient is a near cancellation between that part and the germ's off-ray shift: without the shift the ratio would be 1.30 [SSB, § III].

With nothing fitted, Proposition N's coefficients lie within the extrapolation spread of the coefficients extrapolated from the slow eigenvalues that the M8.16 run recorded at those five branches, group by group, at the harmonic cutoffs $`N = 24`$ and 32 of § 5. The spread is the difference between a linear and a quadratic extrapolation to zero amplitude, not a certified uncertainty. At the pyramid, two terms put the quartet 5.91% from leading order at $`\varepsilon = 0.25`$, where the record reads 5.78% at $`N = 32`$. The agreement is inferred, since the record's coefficient extrapolates three finite amplitudes; the comparison is the Soft-Slot Branches page's reading of the run's data, and no adjudication covers it [SSB, § III; SDC, § V, step 4].

### 4.4 The count and the crossing

Away from small amplitude the spectrum is no longer read off the reduced quartic, but it can still be counted. Take a branch of standing waves $`e^{i\omega_\varepsilon T}\varphi_\varepsilon`$, for $`\varepsilon`$ in an interval and at any amplitude, with $`\Gamma`$ acting exactly; its existence at finite amplitude is assumed, not given. Its linearization is the system of § 4.1, whose forms need no smallness, in the energy space $`\mathcal{H}`$, where $`A_\varepsilon`$ has compact resolvent and $`L_\varepsilon`$ has finitely many negative eigenvalues and a finite-dimensional kernel. Write $`n(L_\varepsilon)`$ for the number of negative eigenvalues of $`L_\varepsilon`$, $`V_0`$ for the generalized kernel of $`A_\varepsilon`$, $`D`$ for the form $`B`$ on $`V_0`$ and $`n(D)`$ for its number of negative directions. Let $`k_r`$ count the positive real eigenvalues of $`A_\varepsilon`$, $`k_c`$ those with positive real and imaginary parts, and $`k_i^-`$ the negative directions of the Hermitian form $`B(\bar v, w)`$ on the generalized eigenspaces of the eigenvalues $`i\tau`$ with $`\tau > 0`$, their Krein-negative directions, all with multiplicity [HKI, § I]. **Theorem K** [HKI, § II]. *At every $`\varepsilon`$,*

```math
K = k_r + 2k_c + 2k_i^- = n(L_\varepsilon) - n(D).
```

This is the Hamiltonian–Krein index theorem [KKS, Pe; KP, ch. 7], here in the energy space of the slot action. The proof is a finite-dimensional reduction. Eigenvalues of large modulus are imaginary and Krein-positive; the spectral subspace outside a large disc has no negative direction of $`B`$, by that step and Pontryagin's theorem on invariant subspaces [IKL, ch. II]; and on the finite part $`B`$ adds over the generalized eigenspaces. The decomposition is $`B`$-orthogonal at every $`\varepsilon`$, so the identity holds where $`D`$ is degenerate too [HKI, § II].

$`K`$ counts the eigenvalues in the open right half-plane, plus twice the Krein-negative directions on the imaginary axis. A Krein collision at nonzero frequency trades a Krein-negative imaginary pair for a quartet, and a collision on the real axis trades a quartet for two real pairs, and neither changes $`K`$. So $`K`$ changes only where eigenvalues of $`A_\varepsilon`$ pass through zero: at a genuine crossing, where an eigenvalue of $`L_\varepsilon`$ passes through zero outside the family's kernel, or where the family's own Jordan structure degenerates, the Vakhitov–Kolokolov mechanism [VK], which is named here and not analysed [HKI, § II].

The verdict module of the finite-element instrument in § 5, which breaks the symmetry, tracks a structural cluster of near-zero eigenvalues, chosen by structure and a tolerance, with a frozen dimension $`k + r_u`$. It reads a genuine index $`h`$, $`n(L)`$ less the negative directions of $`B`$ on that cluster. In an instrument with the symmetry exact, at a regular point where the cluster is verified to span $`V_0`$, $`h = K`$. A matching dimension does not by itself show the span, which must be checked, and at a crossing $`V_0`$ is larger than the cluster, so $`h`$ is read on either side of the crossing, not at it [HKI, § II].

At a genuine crossing the type can change, and Theorem C says when. The notation is [HKI]'s but for three symbols that name other objects here: $`\sigma_\Omega`$ is $`\Omega`$ on static vectors, which § 4.1 makes $`(2\omega_\varepsilon/c^2)\,\sigma`$ and [HKI] writes $`\sigma`$; $`d_Z`$ is its $`d`$; and $`C_T`$ is its $`R_3`$. **Theorem C** [HKI, § III]. *Suppose that $`\varepsilon \mapsto \varphi_\varepsilon`$ is $`C^2`$ into $`H^2`$, and that at $`\varepsilon_*`$: $`\ker L_{\varepsilon_*} = T_* \oplus Z`$, with $`T_*`$ the stationary family's tangent space, of constant dimension nearby, and $`Z`$ of dimension $`d_Z \ge 1`$, while for $`\varepsilon \ne \varepsilon_*`$ nearby the kernel is the family's tangent; and the crossing form $`L' = P_Z(\partial_\varepsilon L_\varepsilon)P_Z`$ is definite on $`Z`$.*

*Let $`R_T`$ be the $`\sigma_\Omega`$-radical of $`T_*`$, $`\mathrm{Rad}`$ that of $`T_* \oplus Z`$, and $`C_T`$ a complement of $`R_T \cap \mathrm{Rad}`$ in $`R_T`$. Each $`s \in R_T \cap \mathrm{Rad}`$ has a partner $`p_s`$ with $`A_{\varepsilon_*}p_s = (s, 0)`$, in the family's own Jordan blocks. Suppose the family's Jordan structure is regular through $`\varepsilon_*`$: $`\sigma_\Omega`$ has constant rank on the family's tangent spaces, and the matrix $`\Pi_T`$ of the energies of the partners $`p_s`$ is nondegenerate, which makes the family's block, its tangent space less $`C_T`$ with those partners, $`\Omega`$-nondegenerate. Split $`Z`$, in the $`\Omega`$-complement of that block, as $`Z_1 \oplus Z_2 \oplus Z_3`$: $`Z_3`$ paired nondegenerately with $`C_T`$ by $`\sigma_\Omega`$, its dimension $`d_3`$ the rank of $`\sigma_\Omega`$ between $`R_T`$ and $`Z`$; $`Z_2`$ inside $`\mathrm{Rad}`$, of dimension $`d_2 = \dim\mathrm{Rad} - \dim(\mathrm{Rad} \cap T_*)`$, each $`z \in Z_2`$ with a partner $`p`$, $`A_{\varepsilon_*}p = (z, 0)`$; and $`Z_1`$ the rest, $`\sigma_\Omega`$-orthogonal to $`T_*`$, $`Z_2`$ and $`Z_3`$, of dimension $`d_1 = d_Z - d_2 - d_3`$, on which $`\sigma_\Omega`$ is nondegenerate. Suppose also that the matrix $`\Pi`$ of the energies of the partners of $`Z_2`$ is nondegenerate, and write $`W`$ for their pairing $`\Omega(z, p)`$. Then for $`\delta = \varepsilon - \varepsilon_*`$ small the family's eigenvalues stay at zero, and:*

- **Case 1, a Krein flip.** *There are $`d_1`$ eigenvalues $`\delta\mu + O(\delta^2)`$, with $`\mu`$ the eigenvalues, relative to $`\sigma_\Omega`$, of the Hamiltonian matrix of the Schur complement of $`L'`$ on $`Z_1 \oplus Z_2`$ onto $`Z_1`$, taken simple. They are imaginary on both sides, with their Krein signs reversed at $`\varepsilon_*`$, and $`K`$ changes by $`\pm d_1`$.*
- **Case 2, a change between real and imaginary.** *There are $`d_2`$ pairs with $`\lambda^2 = \delta\nu + O(\delta^{3/2})`$, with $`\nu`$ the eigenvalues, real and nonzero, of $`-L'`$ on $`Z_2`$ relative to the form $`W\Pi^{-1}W^{\mathsf T}`$, taken simple. Each pair is real on the side where $`\delta\nu > 0`$ and imaginary on the other, with the Krein sign of its partner's energy, and changes $`K`$ by $`\pm 1`$.*
- **Case 3, absorbed by the family.** *No eigenvalue from $`Z_3`$ leaves zero. Its directions change $`n(L_\varepsilon)`$ and $`n(D)`$ by $`d_3`$ each, and leave $`K`$ unchanged.*

The proof reduces to finite dimensions. Near $`\varepsilon_*`$ the Riesz projection onto the eigenvalues of $`A_\varepsilon`$ in a small disc about zero is $`C^2`$ in $`\varepsilon`$ [Ka], and its range is invariant, $`\Omega`$-nondegenerate and of fixed dimension, so the problem is a $`C^2`$ family of Hamiltonian matrices of fixed size. The family's block splits off $`\Omega`$-orthogonally, with its eigenvalues at zero, and the crossing directions are taken in its complement. On each direction of $`C_T`$ paired with its partner in $`Z_3`$ the energy is $`\mathrm{diag}(0, \delta L')`$ to leading order, so $`A_\varepsilon`$ is nilpotent there, while the partners of $`C_T`$ grow like $`1/\delta`$ and their energies change sign. On $`Z_2`$ the eigenvalues, of order $`\delta^{1/2}`$, solve a pencil with a definite form, and on $`Z_1`$ the eigenvalues, of order $`\delta`$, solve the Schur complement's Hamiltonian problem. Across $`\varepsilon_*`$, $`n(L_\varepsilon)`$ changes by $`d_Z`$ and $`n(D)`$ by $`d_3`$, so $`K`$ changes by $`d_1 + d_2`$, with the crossing's sign [HKI, § III].

The theorem is for definite crossing forms. With an indefinite one the same reduction applies, but case 1's eigenvalues need not be imaginary and case 2's $`\nu`$ need not be real. Each half of the regularity hypothesis is needed: two models on $`\mathbb{R}^3`$, one with a partner's energy vanishing at the crossing and one with $`\sigma_\Omega`$ dropping rank there, each move a second pair through zero besides case 2's [HKI, § III].

**Corollary I** [HKI, § IV]. *Suppose a bracket of $`\varepsilon`$ holds one crossing as in Theorem C and no other point where eigenvalues of $`A_\varepsilon`$ pass through zero. Then the pairs that change between real and imaginary through zero inside the bracket are case 2's $`d_2`$ pairs, all at $`\varepsilon_*`$; if $`d_2 = 0`$, a change of type inside the bracket comes from a Krein collision or a collision on the real axis, away from zero; and if $`d_2 > 0`$ and the rest of the spectrum is elliptic on the imaginary side of those pairs, the crossing is a change of type at $`\varepsilon_*`$.* So a genuine crossing at which $`h`$ changes by $`\pm 2`$ can be a Krein flip of case 1, with no change of type, and a Krein collision elsewhere in the same bracket can then give a change of type with that change of $`h`$ that does not sit at the crossing. The census's program first took, as a motivated step to be proved, that a change of type with $`h`$ changing by $`\pm 2`$ sits at the genuine crossing, and its note of 2026-10-15 records that this does not follow [SDC, § V, step 2].

The identification test is therefore Theorem C's decomposition at the crossing: $`\Omega`$ on the whole kernel, the family's directions included, with the signs of $`L'`$ and of the partners' energies, and the regularity of the family's Jordan structure. Restricting $`\Omega`$ to the crossing directions alone mistakes case 3 for case 2. The test is checked at 50 digits on two-dimensional models of each case, and on a perturbed model at $`R_2`$'s degenerate point, with that point's own kernel, forms and family and the crossing imposed by hand. There the decomposition $`(d_1, d_2, d_3)`$ is (2, 1, 0), (2, 0, 1) or (0, 2, 1) at different members of the family, so all three cases occur, and the crossing is a change of type at some members and not at others [HKI, §§ IV, V].

On the records the test needs the decomposition at the crossing, which an instrument with the symmetry broken cannot give. For the hexagon's located change in $`R_5`$, on the finite-element spectra of OpenWave's M8.15.2 run [OW15.2], the counts and spectra point one way without settling it. Elliptic below and hyperbolic above, with $`h`$ falling from 6 to 4, fits case 2 for a doublet whose partners have negative energy; on the three cleanly classified points nearest the crossing on each side, at mesh level 3, the doublet's $`\lvert\lambda\rvert^2`$ is linear in $`\varepsilon`$, imaginary and Krein-negative below and real above, and no quartet is recorded at the evaluated points between the readings, which does not exclude a collision between them. The same fit puts its zeros above each mesh level's ends for $`n(L)`$, by 0.003 to 0.006 at mesh level 3 and 0.06 to 0.11 at mesh level 2. So the reading is inferred, from the finite-element spectra with the symmetry broken, and the identification stays open [HKI, § IV].

What stays open here: whether a new branch bifurcates at a genuine crossing, and which symmetry it breaks, case 3 being where relative equilibria with momentum can branch off; crossings with an indefinite crossing form, tangential crossings, and points where the family's own Jordan structure degenerates, beyond the remarks above; and the identification of any change of type located on the instruments with a genuine crossing [HKI, §§ VI, VII].

## 5. Finite-amplitude continuation

Away from small amplitude no theorem of § 4 decides a branch's type, and the branches born elliptic are followed numerically. Two records do that, and they are kept apart throughout: § 5.2 gives OpenWave's adjudicated verdicts on its instruments, and § 5.3 gives MIT's own computation, which no adjudication covers. Neither is a theorem. Each classifies points on a pinned instrument by a registered rule, and neither identifies a located change of type with a genuine crossing of the stationary operator (§ 4.4). What each instrument was adjudicated adequate for, and where it stops, is § 6's.

### 5.1 The window, and what a classification is

Each nondegenerate branch born elliptic is followed along a ladder of registered amplitudes, from the smallest to its slot's spectral gap, 72 in $`R_4`$, 32 in $`R_5`$ and 132 in $`R_2`$ in units of $`1/R^2`$, where the census's claims stop [SDC, § II]. The gaps are derived, from Proposition C, item 4 of § 3.3; the cutoff at the gap is the census's registration. Within the window the census allows a branch four endings: elliptic throughout; each change of type located, by its $`n(L)`$ interval and its guard readings; an unresolved point, documented after it survives an adequate test, which then passes to the mathematics; or instrument-limited, its unresolved or untested points named and no type claimed. That last ending comes from the census's anti-loop rule, S6: a second instrument-limited outcome with the same cause closes the branch, with the cause named, unless a new instrument that removes the cause is admitted, and the items no admitted instrument can settle close the same way. Every elliptic stretch needs a pre-registered persistence test as well (§ 6). The census closes when these conditions hold, an unresolved point counting once it is documented; the classification of type is complete only when no unresolved point and no instrument-limited branch remains [SDC, § VI].

Two instruments carry OpenWave's verdicts. The finite-element instrument of OpenWave's M8.15 run works on one pinned mesh, with mesh levels 2 and 3 [OW15]. The harmonic Galerkin instrument, which OpenWave's M8.16.1 run qualified, works at the cutoffs $`N = 16`$, 24 and 32, and at 40 in one remedy, an instrument admitted under S6 to remove a named cause [OW16.1; OW18]. On the harmonic instrument a point is classified when, at every cutoff, it is accepted and the kernel check K1 holds, the registered convergence rule, which reads each point converged or Unresolved, reads it converged, and branch identity holds between $`N = 24`$ and 32; its type is the rule's linear type at the tested cutoffs, Hyperbolic when a group of eigenvalues lies off the imaginary axis by more than its tolerance, outside the zero cluster's gray zone, with the generalized kernel as expected, and Elliptic only when nothing is unresolved [OW16, terms], with the top cutoff's $`(n(L), n(D), K)`$ and $`k_i^-`$. On M8.15's instrument a point is classified by its adjudicated reading, and where both instruments classify a point they must agree in type, $`K`$ and $`k_i^-`$ [OW17]. K1 holds when the point is accepted, its generalized kernel has its expected dimension and ranks and contains the exact symmetry directions, and its zero cluster lies within the margin, separated from the rest of the spectrum. Branch identity holds when the solution at the lower cutoff, embedded in the higher one's basis, differs from it by at most $`10^{-2}`$ of its norm, the difference's orbit-tangent components removed, and the two records agree in type, indices, Krein counts and generalized kernel [OW16, terms].

On the harmonic instrument a change of type is located when an $`n(L)`$ interval narrower than $`10^{-3}`$ of its lower end holds it at the deciding cutoffs, $`N = 24`$ and 32, with a guard reading of each type beside it; the hexagon's location in $`R_5`$ is M8.15.2's, on the finite-element instrument under its own terms (§ 5.2). A location is an interval, not a crossing point, and its identification with the genuine crossing is not claimed [OW17].

### 5.2 OpenWave's adjudicated record

Two branches end elliptic throughout, classified elliptic at every registered point of their windows: the prism in $`R_5`$, to 32, and the hexagon in $`R_4`$, to 72, its point 32 classified on the harmonic instrument alone and 16, 45.25 and 64 on the finite-element instrument alone [OW17; SDC, § III].

The $`v_2`$ branch is elliptic wherever it is classified: at 13 of 18 points in $`R_4`$ and 14 of 15 in $`R_5`$, each to 22.63. Its open points, 1.41, 32, 45.25, 64 and 72 in $`R_4`$ and 32 in $`R_5`$, close as instrument-limited under S6, the convergence rule reading each Unresolved because a tested set's member count changes between the cutoffs, and no type is claimed at them [OW17; OW18; SDC, § V, step 5].

Where classified, $`\mathcal{O}_3`$ is elliptic to 2.83 and hyperbolic at 5.66 and from 16 to 45.25 in $`R_4`$, and elliptic to 8 and hyperbolic from 11.31 in $`R_5`$ [SDC, § III].

On the line {7/2, −3/2} in $`R_2`$, the member with complex structure $`i`$ is elliptic at 17 of 20 points to 132, and its points 45.25, 128 and 132 close as instrument-limited, with no type claimed. Its second member is not offered to the harmonic instrument again, and the other members of its $`Sp(1)`$ family are untested [SDC, § III].

Three control ladders ran under M8.15's frozen rules before any target, and they are unscored: the coherent orbit in $`R_4`$ is elliptic at all 18 points to 72, the weight-7/2 member with complex structure $`i`$ in $`R_2`$ at all 20 to 132, and the octahedron in $`R_4`$ hyperbolic at all 18 to 72 [SDC, § III]. They score nothing: the census reads them as evidence for its closed branches and as controls for any new instrument, and counts them apart from the nine branches its census run took [SDC, §§ III, VI].

In $`R_5`$ the coherent orbit's control on the harmonic instrument is elliptic at four points, to 2, its checks passing [OW16.1]; its ladder above 2 ran in OpenWave's M8.19 run [OW19], on the finite-element instrument under the persistence test's terms, elliptic at all 15 points to 32 and recorded apart, with how the census counts those types not ruled (§ 6).

M8.16.1's verdict on the second member of the line {7/2, −3/2} stands: not qualified, and not offered to that instrument again [OW16.1; SDC, § V, step 4].

Twelve points, fixed before M8.18's go for its reading at $`N = 40`$, stay unclassified on OpenWave's record: the $`v_2`$ branch's six open points, $`\mathcal{O}_3`$'s at 4, 8, 11.31, 64 and 72 in $`R_4`$, and the member $`i`$'s at 45.25. M8.17 classified none of them, and the reading at $`N = 40`$ in OpenWave's M8.18 run ended at its control gate before it read any. Each closes as instrument-limited, its cause named, with no type claimed [OW18; SDC, § V, step 5].

Three changes of type are located, and none is identified with a crossing. The hexagon's in $`R_5`$ is located by OpenWave's M8.15.2 run, under the third clause of its frozen ceiling, between the guard readings, elliptic at 15.6356 and hyperbolic at 16.5832 at mesh level 3 [OW15.2]. Its adjudicated name, and beside it, as the terms require, the limit of its continuity check, read in the terms' words [SSB, § VI]:

> A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only.
>
> The solution-continuity check does not certify which solution branch the step lies on, least of all where two branches share `m`.

The prism's change of type in $`R_4`$ is located by OpenWave's M8.17 run: $`n(L)`$ changes by +2 within [16.271828, 16.278300] at $`N = 24`$ and 32, between the guard readings, elliptic at 16.109109 and hyperbolic at 16.441083 [OW17].

$`\mathcal{O}_3`$'s change of type in $`R_5`$ is located by M8.18: $`n(L)`$ changes by −1 within [8.720990, 8.724874] at $`N = 24`$ and 32, between the guard readings, elliptic at 8.633781 and, on the retry, hyperbolic at 9.161117. The location rests on one designed midpoint, 8.720990, to which M8.18 moved the midpoint 8.721638 that K1 had refused [OW18; SDC, § V, step 5].

In $`R_4`$, $`\mathcal{O}_3`$'s change of type, across its unclassified point 4, is not located, and it closes with that point, as instrument-limited under S6 [SDC, § V, step 5].

On the member $`i`$ of the line {7/2, −3/2}, the points 45.25, 128 and 132 stay Unresolved on both instruments and close as instrument-limited under S6, with no cause claimed as shared between the instruments. At 128 and 132 the finite-element instrument's mesh level 3 shows one complex quartet near the top of the window, where its two mesh levels disagree [SDC, §§ IV, V].

Which crossing, if any, each located interval holds is open. Corollary I's test needs Theorem C's decomposition at the crossing (§ 4.4), and no record gives it, so the paper states no count that Theorem C would allow at these intervals and adds no crossing case [HKI, § IV].

### 5.3 MIT's own computation

MIT computed the census's open items on its own side, outside OpenWave's M8 program, on the ground of OpenWave's answer on #512: the condition that nothing is repaired and rerun "binds M8's registrations and what the census counts under S6", and "does not reach what you compute in your own repository" [SDC, § V, step 5]. Its code is changed off M8.16.1's pin, so neither that qualification nor any adjudication carries to it; its values are no M8 outcome, and no closure of § 5.2 changes with them [MC, design § 1]. Everything in this subsection is MIT's, and § 6 and Appendix A say how it was checked.

The computation is M8.18's instrument with two changes to its reader. Change A reads a set by its eigenvalues rather than by its groups' centres, and change B narrows the gray zone of $`n(D)`$ to a factor of 10 above its cut, as $`L`$'s is. Each point reports both verdicts, as built and changed; where they agree, the point rests on no changed code, and no solve uses either change [MC, design §§ 2, 3]. On the ladder of cutoffs $`N = 24`$, 32 and 40, each cutoff on its own path from the seed, the $`v_2`$ branch is elliptic (2, 0, 2) at all 18 points to 72 in $`R_4`$ and at all 15 to 32 in $`R_5`$ [MC, record § 4].

The coherent orbit in $`R_5`$ is elliptic (0, 0, 0) at all 15 points to 32 [MC, record § 4].

On the line {7/2, −3/2}, the member $`i`$ is elliptic (9, 3, 6) wherever it is classified, at 20 of 31 points, and not classified at 11.31, 16 and 116 to 132; the second member is elliptic (9, 3, 6) at 15 of 20 points as built and 16 changed, and not classified at 4, 5.66, 128 and 132, and at 0.354 as built [MC, record § 4]. Table 6 gives the computation's chart.

| branch | points | classified, as built / changed | wherever classified | not classified |
|---|---|---|---|---|
| $`v_2`$ in $`R_4`$ (T1) | 18, 0.25 to 72 | 18 / 18 | Elliptic (2, 0, 2) | none |
| $`\mathcal{O}_3`$ in $`R_4`$ (T4) | 18, 0.25 to 72 | 18 / 18 | Elliptic (7, 1, 6) from 0.25 to 4, Hyperbolic (6, 1, 5) from 5.66 to 72 | none; the change of type between 4 and 5.66 is not located † |
| $`v_2`$ in $`R_5`$ (T1) | 15, 0.25 to 32 | 15 / 15 | Elliptic (2, 0, 2) | none |
| coherent $`v_3`$ in $`R_5`$ (the coherent row) | 15, 0.25 to 32 | 15 / 15 | Elliptic (0, 0, 0) | none |
| line {7/2, −3/2} in $`R_2`$, member $`i`$ (T5) | 31, 0.25 to 132 | 20 / 20 | Elliptic (9, 3, 6) | 11.31, 16, 116 to 132 |
| line {7/2, −3/2} in $`R_2`$, second member (T5's second member) | 20, 0.25 to 132 | 15 / 16 | Elliptic (9, 3, 6) | 0.354 as built, 4, 5.66, 128, 132 |

*Table 6.* MIT's own computation, its chart on the ladder $`N = 24`$, 32 and 40 [MC, record, the chart]. Every entry is MIT's, outside M8, and no OpenWave adjudication covers it. A point is classified when it is accepted with K1 at every cutoff, the rule reads it converged with a type, and branch identity holds on both pairs of cutoffs; the type is the rule's, with $`N = 40`$'s indices $`(n(L), n(D), K)`$. "As built / changed" counts the points each reader classifies. In parentheses, the record's names for the branches. † The record's cell points to its own § 5; the bracket is read below.

The twelve points that M8.18 did not read keep M8.17's stored type and indices at $`N = 40`$, classified both ways [MC, record § 3]. On OpenWave's record they stay unclassified (§ 5.2): a type this computation classifies is its own, not the census's.

Before it read $`\mathcal{O}_3`$'s bracket in $`R_4`$, MIT's locator ran M8.18's location of $`\mathcal{O}_3`$ in $`R_5`$ again on its own tree: 0 differences from M8.18's record, and 0 of 146 arrays unequal [MC, record § 1].

$`\mathcal{O}_3`$ in $`R_4`$ is elliptic (7, 1, 6) from 0.25 to 4 and hyperbolic (6, 1, 5) from 5.66 to 72, all 18 points classified, with one real pair from 5.66 and, at 72, a quartet beside it [MC, record § 4].

On the bracket (4, 5.66), $`n(L)`$ changes from 7 to 6 inside [5.588897, 5.592133] at $`N = 24`$, 32 and 40, and the change of type is not located: K1 stopped the bisection at 5.590515, and at the moved point 5.590192, at every cutoff. The interval's width is 0.000579 of its lower end, where completing asks below 0.0005, and it is not identified with the genuine crossing [MC, record § 5; locator terms].

Outside the locator's rule, and deciding nothing, the record adds an inferred reading. $`L`$'s eigenvalue that changes sign, on a straight line through the accepted midpoints near the interval, crosses zero near 5.590415 at $`N = 24`$ and 5.590470 at 32 and 40. K1 cannot hold where the eigenvalue of $`A_\varepsilon`$ on that mode lies within three margins of zero, a neighbourhood $`9.3\times10^{-4}`$, $`1.7\times10^{-3}`$ and $`2.6\times10^{-3}`$ wide around that zero at $`N = 24`$, 32 and 40, where a completed interval must be narrower than $`2.8\times10^{-3}`$, and both refused points lie inside it at every cutoff [MC, record § 5].

*Figure 2 (to come).* $`\mathcal{O}_3`$ across its bracket in $`R_4`$, in MIT's register: not located, and not identified with a crossing.

At the top of the member $`i`$'s window, 116 to 132 are not classified on the first ladder. Branch identity fails between $`N = 24`$ and 32 at every one of them; at 116, 120 and 124 the records also differ along the ladder, and a tested set's count changes between cutoffs; and at 126 a tested group's error exceeds a tenth of its distance to the imaginary axis [MC, record § 4].

A second ladder, $`N = 32`$, 40 and 48, ran under terms fixed before any solve there [MC, top terms]. Its raw readings: 116 and 120 converged, elliptic (9, 3, 6); 124 converged, elliptic (4, 0, 4); 126 Unresolved; 127 to 132 converged, hyperbolic (4, 0, 4). None is classified, because the rule does not read 100 and 106, the classified points below them that serve as controls in the row, converged on that ladder: their records keep elliptic (9, 3, 6), but one Krein-negative group's step stops shrinking, and why is open. The first ladder's verdict, not classified, stays the record [MC, record head, § 6].

The index drop: at $`N = 32`$, 40 and 48 the records go from elliptic (9, 3, 6) at 120 to elliptic (4, 0, 4) at 124, and neither point is classified on either ladder [MC, record §§ 4, 6]. Before the reads, an elliptic stretch with $`K = 4`$ was stated to come before the quartet, since a collision moves no index and the three low pairs at 90.51 are all Krein-negative, so that one has to pass through zero before two can leave the axis [MC, design § 6]. The stretch is in the records; that the index drop and the collision are separate events stays inferred [MC, record § 7].

The collision: each cutoff's records change type, from elliptic to hyperbolic, between 126 and 127 at $`N = 48`$, between 124 and 126 at $`N = 32`$ and 40, and between 116 and 120 at $`N = 24`$. These are raw transitions, since none of those points is classified on either ladder [MC, record §§ 4, 6].

On the collision law, the real part squared linear in $`\varepsilon`$ over the hyperbolic points above 64, the collision sits at 118.078, 125.752, 125.969 and 126.001 at $`N = 24`$, 32, 40 and 48, with a limit of about 126.01 on the last three. The fit is inferred, and its rate is not shown [MC, record § 6].

The quartet's real part at $`N = 48`$ runs from 0.0634 at 127 to 0.1560 at 132, falling at every step from $`N = 24`$ to 48, its step from 40 to 48 between 0.216 and 0.227 of its step from 32 to 40 [MC, record § 6].

On that ratio its limit would be about 0.0629 at 127 and 0.1558 at 132, an inference, since three cutoffs cannot show the rate [MC, record § 6].

*Figure 3 (to come).* The low imaginary eigenvalues of the member $`i`$, with their Krein signs, from 100 to 132, through the index drop and the collision, in MIT's register; no point from 116 up is classified on either ladder.

*Figure 4 (to come).* The quartet's real part against $`\varepsilon`$, in MIT's register.

Statements were made before the reads, from known outcomes, and none was a classification [MC, design § 6; top terms § 5]. These missed: the quartet's real part at $`N = 40`$ and at 48 on every stated law, its step from 40 to 48, the collision's place at $`N = 40`$ and 48, and branch identity's range on the cutoffs 40 and 48. These held: the twelve, 132 off the axis, the stretch with $`K = 4`$, no new link at $`N = 40`$ alone at a stored point of the branches in the tested set, the tolerances at 48, and the types and the branch at 48, but at 126. The one new link at $`N = 40`$ alone is the second member's at 0.354, which no earlier record held. The misses are kept as stated [MC, record § 7].

## 6. Verification and limits

This section says what the numerics of § 5 rest on and where they stop: what is derived about the instruments (§ 6.1), what each was adjudicated adequate for (§ 6.2), the bounded record of persistence (§ 6.3), the orbital stability supplied by the theorems of §§ 3 and 4 (§ 6.4), where each instrument stops (§ 6.5), and what stays open (§ 6.6).

### 6.1 What is derived about the instruments

The harmonic instrument expands the sections in the twisted harmonics, by complete $`SU(2)`$ levels up to a cutoff. Its kernel holds under three conditions: the truncated space is invariant under right $`SU(2)`$ and the fibre group, which complete levels give by construction; the scheme is variational Galerkin, with the quartic evaluated exactly, not by collocation; and the solver's slices and gauges act only in the Newton solve, never in the operator whose spectrum is read. Under them, differentiating the energy's invariance twice at a critical point puts the orbit tangent in the Hessian's kernel exactly [SDC, § V, step 3].

In a variational discretization that keeps the symmetry exactly, the stationary operator is self-adjoint, and its eigenvectors for nonzero eigenvalues are orthogonal to its exact kernel. So away from a genuine crossing the mixing of lifted structural modes with genuine ones is absent in exact arithmetic; that does not by itself make every check of the structural subspace pass in finite precision [SDC, § IV].

In the continuum, on the $`v_2`$ branch below $`\varepsilon_1`$, every slow eigenvalue but the structural zeros is an imaginary, Krein-definite pair at a distance of order $`\varepsilon`$ from zero, by Theorem R(a) and (e), so the merger with a structural mode that the finite-element instrument met there cannot occur (§ 4.1) [SDC, § IV].

### 6.2 The instruments, and what each was adjudicated adequate for

M8.15, on one pinned finite-element discretization with mesh levels 2 and 3, found the prism in $`R_5`$ elliptic at all 15 points to 32, the hexagon in $`R_4`$ at 17 of 18 to 72, and the member $`i`$ of the line {7/2, −3/2} at 17 of 20 to 132; the prism in $`R_4`$ hyperbolic from 32 and the hexagon in $`R_5`$ from 22.63, neither change located; the $`v_2`$ branch INVALID at its smallest amplitude in both slots, in $`R_4`$ on the instrument's 0.9 overlap classification alone; and $`\mathcal{O}_3`$ with no ladder point in either slot [OW15; SSB, § VI].

M8.15.1 located no change of type [OW15.1]. M8.15.2 located the hexagon's in $`R_5`$, under the third clause of its frozen ceiling, and not the prism's in $`R_4`$, where its two mesh levels disagree [OW15.2; SSB, § VI].

Whether the lifting of the structural zero modes caused the finite-element instrument's failures near zero is open. The census calls its account "a diagnosis, not an established cause", and M8.16.1's check K3, which certifies the kernel from the Hessian alone, registered to show that account wrong, did not, a known outcome read as inferred [SDC, §§ IV, V].

M8.16 was not qualified: the pyramid control's quartet lay 5.76% to 5.78% from Theorem R's leading order at $`\varepsilon = 0.25`$, against a bar of 5%, so the diagnosis stayed untested and no branch ran [OW16; SDC, § V, step 4].

Proposition N's two terms put that quartet 5.91% from leading order at 0.25, where the record reads 5.78%, so the departure over the bar is consistent with the quartet's own next-order term (§ 4.3); that reading is an inference [SDC, § V, step 4].

OpenWave admitted the harmonic instrument on #512 on 2026-10-15, as a stationary continuation and linear-spectrum record of named branches under the frozen action, with a law it derives and pins itself, and nothing from the design inputs of M8.5-C, OpenWave's earlier spectral route, closed on #506, or from the room of that route's C2 protocol. Outside the admission are time integration in a harmonic basis, any use as a route to the two criteria of OpenWave's model register that are gated on field dynamics, and the census's persistence tests [SDC, § V, step 3].

M8.16.1 qualified the instrument and nine branches, each mode scored against Proposition N's next-order term. The check registered to show the diagnosis wrong did not, and the quartet's pass and K3's resolution are known outcomes, read as inferred, neither of them a test of Proposition N. The second member of the line {7/2, −3/2} is not qualified, and not offered to the instrument again. A qualification is not a classification [OW16.1; SDC, § V, step 4].

M8.17 stands as recorded: of its 56 first-time readings, 42 are classified, and no point that both instruments classify disagrees [OW17].

M8.18 stands as recorded: $`\mathcal{O}_3`$ in $`R_5`$ is located; its reading at $`N = 40`$ ended at its control gate, with none of the twelve read; and S6 is applied item by item [OW18].

OpenWave's answer on #512, which MIT's own computation stands on, is quoted in § 5.3 [SDC, § V, step 5].

### 6.3 Persistence: a bounded record

The census's persistence condition, S5, asks that every elliptic stretch have at least one pre-registered persistence test [SDC, § VI]; a ruling set out below lets a stretch that no adequate test can reach end untested instead. The tests lie outside the harmonic instrument's admission and need a pre-registration of their own [SDC, § V, step 5]. Every scored test on the record is bounded: one frozen perturbation draw at $`\eta = 10^{-3}`$, at mesh level 2, over a finite time $`T`$, 1000 in M8.15's tests and, in M8.19's, at least one period of the mode a test probes, never under 1000 and rounded up to a multiple of 250. M8.15's control test on the coherent orbit in $`R_4`$ at $`\varepsilon = 1`$, at $`T = 1000`$, spanned 0.37 of that mode's slowest period, 2740. The controls also include the octahedron control's separate rate run, at $`\eta = 10^{-7}`$, which is no scored test. In M8.19's terms' words, "a test that Persists is evidence to `T`, not beyond" [OW19].

M8.15 ran eight persistence tests at mesh level 2, with $`\eta = 10^{-3}`$ and $`T = 1000`$, on the prism and the hexagon in both slots and on the member $`i`$: all eight Persist, each for its one registered direction. The control ladders of the coherent orbit in $`R_4`$ and of the weight-7/2 member in $`R_2`$ carry two each, and all four Persist [OW15; SDC, § III].

OpenWave's #512 ruling of 2026-11-07 fixed how S5 ends a stretch it cannot test. A stretch whose instrument cannot be shown adequate, under tests fixed before any target evolves, ends untested, as S6 ends an item, with its cause named and no persistence claimed either way; its classified type stands as adjudicated, and S5 counts it for the census's close. The ending closes a condition of the census, not the question of persistence, which stays open at the stretch [SDC, § V, step 5].

M8.19's terms, merged on OpenWave #698, give every elliptic stretch on OpenWave's record that has no persistence test, each unclassified point splitting a stretch, one test where adequacy gates fixed before any target evolves pass, on M8.15.x's frozen finite-element solver outside the harmonic admission; a stretch that fails a gate ends untested, with its cause. The coherent orbit's ladder in $`R_5`$ above $`\varepsilon = 2`$ runs and is recorded on its own, and no outcome claims orbital stability or instability [OW19].

The terms count M8.15's eight tests at the amplitudes they ran: the prism's at 5.66 in $`R_4`$ and at 4 and 16 in $`R_5`$; the hexagon's at 2.83 in $`R_4`$ and at 4 and 11.31 in $`R_5`$; and the member $`i`$'s at 16 and 64, one on each side of its unclassified point 45.25. The four control tests stay apart from the scored targets [OW19].

M8.19 ran on 2026-11-10 in one launch, and OpenWave adjudicated it on #705 the same day, "approve and merge, no findings, no maintainer edits", the record standing as filed. Gate 1 passed: every control gave the verdict the terms ask, and no target evolved before it [OW19].

Five stretches end untested under S5: the $`v_2`$ branch in $`R_4`$ from 0.25 to 1 and from 2 to 22.63, in $`R_5`$ from 0.25 to 22.63, and $`\mathcal{O}_3`$ in $`R_4`$ from 0.25 to 2.83 and in $`R_5`$ from 0.25 to 8. The cause is gate 3, the level-3 cluster check failing at every one of their 46 points. No persistence is claimed either way, their types stand as adjudicated, and S5 counts each of them for the census's close [OW19; SDC, § V, step 5].

The coherent orbit in $`R_5`$ has its test, as S5 asks: at $`\varepsilon = 32`$, with $`T = 1000`$, 3.33 periods, it Persists, valid. In the adjudication's words, "That is evidence to `T`, from one draw at one `η`, and not beyond" [OW19].

There "valid" is the frozen persistence rule's word. Beside it, M8.15's persistence code computes a second energy rule, `valid_under_v6_energy_rule`, charge drift at most $`10^{-10}`$ and energy drift at most $`10^{-6}`$ of the total energy, recorded and not scored. It is false on every test the frozen rule reads valid, and true only on C3's rate run, at $`\eta = 10^{-7}`$, which the frozen rule reads invalid. M8.19's terms disclosed it before the run, and the frozen rule governs, so the second rule scores nothing and moves no verdict; no stronger claim about conservation in the runs rests on the record [OW19].

Its ladder in $`R_5`$ is established, elliptic at all 15 points from 0.25 to 32, and its outcome is recorded apart. The terms put the test on the stretch the ladder establishes, here 0.25 to 32, and how the census counts the ladder's types above 2 is not ruled [OW19].

Three findings after the run score nothing: accepted numerical stationary solutions on the finite-element instrument at mesh levels 3 and 2 at all 19 points of $`\mathcal{O}_3`$'s two stretches, where M8.15's Newton failed at the seed; the Krein count at mesh level 2, which does not balance at 8 of those 19 points; and the frozen search of the fast spectrum, which did not restore the balance. No gate reads the count or the search, and none of the three is a continuum result [OW19; SDC, § V, step 5].

### 6.4 Orbital stability on the record

The slot action names an orbital-stability theorem as the alternative to a persistence test [SA, § VII]. One is supplied for the rigid families at every charge, by Theorem B, and for the soft minima at small amplitude, by Theorem R(c) [SA, § IX; SSB, § V]; whether it counts on OpenWave's M8.2 success ladder is a filing's to adjudicate.

$`R_2`$'s degenerate point is orbitally stable at small amplitude, along its family, by Theorem R′(b) (§ 4.2) [SSB, §§ III, VI].

Orbital stability at the maxima and the saddles is open: there Theorems R(d), R(e) and R′(c) give spectral stability only [SDC, § VIII; SSB, § V].

### 6.5 Where the instruments stop

The finite-element instrument's mesh breaks the continuous symmetry of right $`SU(2)`$ and lifts the structural zero modes off zero, 7 to 11 times the frozen floor at mesh level 3 on the pyramid control; the lifted pair can merge, at small amplitude, with a genuine slow mode that lies nearly in the structural plane; and a finer mesh level is likely beyond the machine that ran the instrument. That account is inferred, from the qualification's measurements [SDC, § IV].

The finite-element instrument's two mesh levels disagree near the prism's change of type in $`R_4`$, and at the member $`i`$'s points 45.25, 128 and 132 [OW15; SSB, § VI].

The harmonic instrument, as qualified, leaves a point unclassified where a tested set's member count changes between cutoffs or a group does not contract: at the open points of the $`v_2`$ branch and of $`\mathcal{O}_3`$, and at the member $`i`$'s 45.25. K1 refused the midpoint 8.721638 of $`\mathcal{O}_3`$'s bracket in $`R_5`$ at $`N = 24`$ and 32 [OW17; SDC, § V, step 5].

At $`N = 40`$ the remedy's control gate stopped it: the kernel passed on all seven controls, the pyramid control and the C3 ray's control in $`R_4`$ read Unresolved at 0.25, and none of the twelve was solved [OW18].

The record's diagnostic, made after the run, scores nothing: in both controls a tolerance that grows with the cutoff reaches a value that does not move, at $`N = 40`$ alone [OW18].

Time integration in a harmonic basis lies outside the harmonic instrument's admission (§ 6.2), so no persistence test runs on it.

MIT's own computation stops, as built and changed alike, at $`\mathcal{O}_3`$'s unlocated change of type in $`R_4`$, where K1 refuses both midpoints, and at the top of the member $`i`$'s window: on the first ladder, where branch identity fails between $`N = 24`$ and 32, and on the second, where the in-row controls at 100 and 106 read Unresolved, one Krein-negative group's step from 40 to 48 not shrinking, above the floor [MC, record §§ 5, 6, 8; locator terms]. Its own checks run beside it: six fresh control points, their marks fixed before any read, hold every mark on both ladders; the stored reads were read again before any read at $`N = 48`$, and found equal; M8.18's location was reproduced (§ 5.3); and the record recomputes each point's classification from its reading file [MC, record head, §§ 1, 2]. Appendix A gives these checks in full.

Why the steps at 100 and 106 stop shrinking on the second ladder is open [MC, record §§ 6, 8].

On the member $`i`$'s finer path, MIT's, with eleven points added from 76 to 130, the solve fields show no sign that the stored, coarser path stepped onto another solution, an inference; a proof that it did not is open [SDC, § V, step 5].

Bitwise agreement on another machine is not claimed: MIT's computation agrees with itself bit for bit on its own machine, and elsewhere its comparisons agree to round-off [MC, record § 10].

### 6.6 What stays open

With S5 holding, the census's conditions hold and it closed on 2026-11-10, but the close is procedural, proving no orbital stability, and the classification of type is not complete: the $`v_2`$ branch in both slots, $`\mathcal{O}_3`$ in $`R_4`$ and the member $`i`$ end instrument-limited under S6 [SDC, Status; § VI]. That reading of the close is the author's, on MIT. The type at every item closed as instrument-limited stays open, and so does persistence on the stretches of the $`v_2`$ branch and $`\mathcal{O}_3`$ that end untested [SDC, § VIII].

Completeness of both critical sets is open (§ 3.1) [SDC, § VIII].

Whether $`R_2`$'s lowest eigenspace contains a section of constant norm, the question Proposition C, item 2, leaves, and whether the coherent branch is the ground-state set beyond small charge in $`R_4`$ and $`R_5`$, are open (§ 3.3) [SDC, § VIII].

Outside the census, and open: whether branches born hyperbolic re-stabilize, amplitudes beyond the gap, and branches that start at higher levels [SDC, § II].

The soft-slot branches past small amplitude are open as mathematics: their continuation, spectral type and stability through the windows rest on numerics alone, while the ground-state results of § 3.3 at every charge stand apart [SSB, §§ V, VI; HKI, § VI].

The members of the line {7/2, −3/2}'s $`Sp(1)`$ family other than the member $`i`$ and the second member are untested on OpenWave's record, and their type is open [SDC, § III].

The member $`i`$'s index drop between 120 and 124, at $`N = 32`$, 40 and 48, is open: no locator ran on it, and no record says which eigenvalues move there, or whether they do so through a genuine crossing of $`L_\varepsilon`$ or a degeneration of the family's own Jordan structure, the two ways § 4.4 allows [MC, record §§ 6, 8; design § 6].

How the census counts the coherent orbit's types in $`R_5`$ above $`\varepsilon = 2`$ is open: no ruling has settled it [SDC, § VIII]. The earlier sections state the rest of what stays open: the size of $`\varepsilon_1`$ (§ 4.1), the degenerate branches at finite amplitude (§ 4.2), branching and the other crossings Theorem C leaves aside (§ 4.4), and what each located interval holds (§ 5.2).

## 7. Discussion and the sequel

This section reads the results together: what in the problem is generic and what the geometry adds (§ 7.1), what the finite-amplitude numerics add to the theorems (§ 7.2), what the open questions would need, with the sequel's program (§ 7.3), what the paper does not claim (§ 7.4), and what it establishes (§ 7.5). Each result keeps the standing it has where it is stated: a derived result at its grade, OpenWave's adjudicated record, or MIT's own computation, with what stays open beside it.

### 7.1 What is generic, and what the geometry adds

The mechanism behind the ground states' stability is generic. Theorem A holds for a defocusing quartic on any compact manifold of dimension at most three; Theorem B applies wherever the whole lowest eigenspace consists of sections of constant norm; and Theorem D needs that property and nothing more [SGS, § VI]. What is specific to $`2I`$ is which slots are rigid, the coherent orbit that minimizes the reduced quartic in $`R_4`$ and $`R_5`$ and carries their ground states at small charge, and the reduced quartic's closed form [SGS, §§ IV, VI].

The representation theory of $`2I`$ decides which slots are rigid. In $`R_1, R_3, R_6, R_7, R_8`$ and the control, every lowest-level section has constant norm, so each one starts an exact branch whose profile never changes (§ 2.4); those families are the ground-state sets, orbitally stable as sets at every nonzero charge, and every member of them is spectrally stable, its whole linearized spectrum on the imaginary axis (§ 3.3). In the soft slots, $`R_2`$ at level 7 and $`R_4`$ and $`R_5`$ at level 6, not every lowest section has constant norm, and the cubic term of a lowest-level section need not lie in the lowest level [SA, § VI; SGS, § VI].

In the soft slots the branches start at the critical orbits of the reduced quartic on the lowest level, each nondegenerate orbit continuing to a branch (§ 3.2). In $`R_4`$ and $`R_5`$ the critical points on the fixed loci of projective dimension at most one make exactly ten orbits modulo rotation and phase, by an audited argument, the ten reproduced in value and signature in exact arithmetic, and three orbits outside that class are interval-certified (§ 3.1). Whether either critical set is complete is open [SDC, § VIII].

The sharpest contrast is between $`R_4`$ and $`R_5`$. In the reduced problem $`R_5`$ is $`R_4`$ with every $`q_J - 1`$ scaled by 9/16, so the two share their critical orbits, their signatures and their small-amplitude types, with every eigenvalue of the slow matrix $`\widehat S_u`$ scaled by exactly 9/16; the leading slow eigenvalues of the linearization also carry Theorem R's factor $`1/Q(u)`$ (§§ 3.1, 4.1). At finite amplitude, on OpenWave's adjudicated record, they part: a change of type is located for the prism in $`R_4`$ and for the hexagon in $`R_5`$, neither identified with a crossing, while the prism in $`R_5`$ and the hexagon in $`R_4`$ are elliptic at every point classified [SDC, § III]. This correspondence between the reduced problems does not establish the separately registered relation among the energies of stable states across the eight slots, which stays open [SRel].

In the quaternionic slots charge conjugation generates $`Sp(1)`$ with the phase, so a stability claim names the family it is made relative to. In $`R_2`$ one family holds distinct standing waves whose spectral stability need not agree, and at small amplitude definiteness holds along a whole family, while an indefinite orbit's type can change along it (§§ 2.3, 4.1).

### 7.2 What the numerics add to the theorems

The analytical results have two ranges: the ground-state sets and the rigid families at every nonzero charge (§ 3.3), and the soft-slot branches at sufficiently small amplitude (§§ 3.2, 4.1). How small is open: the size of $`\varepsilon_1`$ is not derived, nor whether a registered smallest amplitude lies below it (§ 4.1). Past small amplitude the soft-slot branches are open as mathematics: their continuation, spectral type and stability through the windows rest on numerics alone [SSB, §§ V, VI; HKI, § VI].

What the numerics add is the branches' spectral history through those windows, read at registered points on registered continuation paths. On OpenWave's adjudicated record two branches end elliptic throughout, classified elliptic at every registered point of their windows, the prism in $`R_5`$ and the hexagon in $`R_4`$; and three changes of type are located, each between guard readings of each type: the hexagon's in $`R_5`$, under the third clause of its run's frozen ceiling, with the limits its adjudicated name states, the prism's in $`R_4`$, and $`\mathcal{O}_3`$'s in $`R_5`$ (§ 5.2). A type is read at those points and at the tested cutoffs, not between the points and not in the continuum (§ 5.1).

MIT's own computation, which no adjudication covers, reads two places that OpenWave's record leaves open. It classifies $`\mathcal{O}_3`$ in $`R_4`$ at all 18 points, elliptic to 4 and hyperbolic from 5.66, its change of type bracketed and not located; and at the top of the member $`i`$'s window its records show an index drop and, between consecutive points at every cutoff, a change to hyperbolic where a quartet appears; where that collision sits is inferred, from a fitted law, and neither of its ladders classifies those points (§ 5.3).

Neither record identifies a located change with a crossing. Theorem K counts the spectrum at any amplitude, and its count changes only where eigenvalues pass through zero, at a genuine crossing or where the family's own Jordan structure degenerates; a Krein collision leaves it unchanged (§ 4.4). Which crossing, if any, each located interval holds is open: Corollary I's test needs Theorem C's decomposition at the crossing, and no record gives it.

### 7.3 What the open questions need, and the sequel

Some of the questions that stay open (§ 6.6) are mathematical: orbital stability at the maxima and the saddles, where Theorems R(d), R(e) and R′(c) give spectral stability only (§ 6.4), and the soft-slot branches past small amplitude, whose continuation, type and stability rest on numerics alone (§ 7.2). The identification of a located change asks for a computation the theory specifies: Theorem C's decomposition at the crossing, taken on the whole kernel with the family's directions included, since restricting it to the crossing directions mistakes case 3 for case 2 (§ 4.4).

Others need an instrument. Persistence on the stretches of the $`v_2`$ branch and $`\mathcal{O}_3`$ that end untested is open, and so is the type at every item closed as instrument-limited (§ 6.6). At the $`v_2`$ branch and $`\mathcal{O}_3`$ the census's leading account of the finite-element instrument's failures is that its mesh breaks the continuous symmetry and lifts the structural zero modes off zero; that account is inferred, from the qualification's measurements, and a finer mesh level is likely beyond the machine that ran the instrument (§ 6.5). Whether the lift caused the failures is open [SDC, § IV]. In a variational discretization that keeps the symmetry exactly, the mixing of lifted structural modes with genuine ones is absent in exact arithmetic away from a genuine crossing, though that alone does not make every check pass in finite precision, and the harmonic instrument keeps the symmetry under the three conditions of § 6.1. Its admission excludes time integration (§ 6.2).

Two places in MIT's computation need a location. No locator ran on the member $`i`$'s index drop, so which eigenvalues move there, and whether through a genuine crossing or a degeneration of the family's Jordan structure, is open. On $`\mathcal{O}_3`$'s bracket in $`R_4`$ the registered locator ran, and K1 stopped its bisection at every cutoff, so the change of type there is not located (§ 5.3).

The paper reports the registered finite-time tests of § 6.3 and claims no persistence beyond each test's time $`T`$; it undertakes no dynamics program of its own. The sequel's program is the response to perturbation over several directions, amplitudes and durations, with refinement; dynamics that keeps the continuous symmetry at the $`v_2`$ branch and $`\mathcal{O}_3`$, where the census's leading diagnosis, an inferred one, is the mesh's breaking of it; evolution near the located changes of type, near $`\mathcal{O}_3`$'s unlocated change in $`R_4`$ and at the top of the member $`i`$'s window; and the line between finite-time persistence, spectral stability and orbital stability. It needs an instrument first. The harmonic admission excludes time integration, and a point the census run did not classify is not offered to that instrument again without a ruling on #512 [SDC, § V, steps 4 and 5]. So the sequel runs under a new ruling there, or as MIT's own computation outside OpenWave's M8 program, labelled as such.

### 7.4 What the paper does not claim

Nothing here holds for another action. A different curvature coupling, quartic or mass, or a term coupling two sectors, would be a new selection, frozen on its own page, and a different action would need its own census [SA, § VIII; SDC, § VII]. Nor does the paper fill a criterion of OpenWave's model register. The structure common to the eight slots meets the letter of what OpenWave's M8.4 pre-registration names as earning more, "a common finite-amplitude branch or stability structure across the eight under one action", not its intent, and the label stays M8.4's "nonlinear persistence of the installed free structure" [SA, § VII; SDC, § VII; SGS, § VI].

Nor does the paper make a physical claim. It derives no law for the energies of stable states across the eight slots, of the kind the slot relation registers and reports open [SRel]; it gives no physical particle state, since global standing waves are not particles; and it takes no step of the framework's stress-tensor bridge, its program toward a stress tensor with a declared place in the metric [SA, § VII; SDC, § VII; STB]. This law has no localized standing wave in flat three-space, with or without a mass (§ 2.4). Whether localized states exist on $`X`$ at the curvature scale is open [SA, § VII]. The action is covariant, but the static compact arena has a global rest frame, so no Lorentz invariance is claimed without that qualification [SA, § VII]. The next physics question, a bridge from the standing waves to a derived physical matter action, a matter sector or a gravity source, is outside this paper.

Two limits run through the mathematics and the numerics. No orbital stability is claimed where only spectral stability is proved, and no imaginary spectrum is read off a truncation: a numerical type is the registered rule's linear type at the tested cutoffs (§ 5.1). No type is claimed at an instrument-limited item, and no located change of type is identified with a crossing (§§ 5.2, 7.2).

### 7.5 What the paper establishes

For the frozen action on $`X`$, the paper establishes by proof: a branch of standing waves at small amplitude at every nondegenerate critical orbit of the reduced quartic, and germs at the two degenerate orbits of Tables 2 and 3 (Lemmas G and G′); in every slot and at every nonzero charge an orbitally stable set of ground states, and in the rigid slots families known exactly, orbitally and spectrally stable (Theorems A, B and D); the small-amplitude spectral type of every nondegenerate orbit of Tables 2 and 3, computed in exact arithmetic and, at three orbits, in interval arithmetic (Theorem R), and of both degenerate orbits at second order (Theorem R′); the next order of the slow spectrum (Proposition N); and, at any amplitude on a branch whose existence is assumed, with its symmetry acting exactly, the Hamiltonian–Krein count (Theorem K), with the classification of a transversal genuine crossing under Theorem C's hypotheses, among them a definite crossing form, a regular Jordan structure of the family and a nondegenerate energy matrix of the partners (Theorem C, Corollary I).

On OpenWave's adjudicated record, the nondegenerate branches born elliptic are followed through their windows on registered continuation paths and typed at the points classified: two are classified elliptic at every registered point of their windows; the $`v_2`$ branch and the member $`i`$ are elliptic wherever classified, and $`\mathcal{O}_3`$ elliptic and then hyperbolic; three changes of type are located, none identified with a crossing; and every item the instruments could not classify closes as instrument-limited, with no type claimed (§ 5.2). Persistence stands as a bounded record: M8.15's eight scored tests Persist, and so does the coherent orbit's in $`R_5`$, each evidence to its time $`T`$ and not beyond, and five stretches end untested (§ 6.3). The record is of registered paths, classified points and bounded tests, not of spectral stability through a whole interval.

As MIT's own computation, outside every adjudication, the paper reports $`\mathcal{O}_3`$ in $`R_4`$ classified at all 18 points, its change of type bracketed and not located, and the top of the member $`i`$'s window, where the records show an index drop and then a quartet, at points neither ladder classifies, the collision's place inferred from a fitted law (§ 5.3).

Every one of these is a result about one frozen action on one geometry. The paper establishes what that action does on the Poincaré homology sphere, not that nature uses it, and a different action would need its own study.

## Appendix A. The verification of MIT's own computation

This appendix gives the checks behind MIT's own computation of § 5.3, which § 6.5 summarizes: what its code is, what it was tested on before it ran, how its runs were kept, what its fresh controls showed, and how its record is rebuilt. They show that the computation ran as its design fixed it, and no more. Its code is off M8.16.1's pin, so neither that qualification nor any of OpenWave's adjudications carries to it, and its values are no M8 outcome [MC, design § 1].

### A.1 The code, and what it was tested on

The computation is M8.18's instrument byte for byte, every file of the instrument and the run that M8.18's run used, but for one arm of the convergence rule, which is change A of § 5.3. The files it adds, change B and the changed reading, the grid and its pass marks, the fresh controls' test, the jobs and the pins, are imported by no part of the solver [MC, design § 2].

The solves do not touch the changes. The solver's modules import neither the linear reader nor the convergence rule, and a solve runs where every path that writes a record refuses, so no solve rests on either change, and no spectrum exists until a read makes one [MC, design § 2].

Before the first pin, the code was tested at the run's own setting. M8.18's six controls at $`N = 24`$ and 32, solved again, equal its files in all 336 solve fields and 11,048 array entries; its stored solutions at all three cutoffs, read again, equal its records at all 72 points, the readings and both identities among them; and the changed reading is converged at all 24 control points, moving exactly the pyramid control and the C3 ray's control in $`R_4`$ at 0.25 [MC, design § 2]. Separately, the convergence rule alone was tested on all 262 published readings [MC, design § 2]. The reading tests ran again on the change A that ran, which replaced the first pin's, before the reads and beside the solves rather than at the run's setting, with the same results, apart from the eigenvalues a read now keeps beside the record [MC, development log, entries 7, 8].

Both changes were chosen knowing M8.18's control-gate failure, its 24 control readings and M8.17's stored readings at the twelve points, so readings already on record are not new evidence for the changed code. Each point reports both verdicts, as built and changed, and where they agree it rests on no changed code [MC, design § 3].

### A.2 Custody and order

The computation ran in 21 launches from 2026-11-02 to 2026-11-07, 125 jobs in five stages, each stage on its own manifest pin. Each read refuses until it is given the commit of the dated note on the census page that names its pin, and refuses a path whose job record names a manifest the solves did not run under, or whose files differ. Every job completed, none failed or was resumed, and the 162 files the job records logged match their SHA-256. Before each note, the solves were checked at their solve fields alone, which hold no spectrum [MC, record head, § 1].

The design was written before any of the run's solves and revised before any read of them, and it fixed the order: the pin; the solves, with no spectral read, diagnostic preview or grid change from a result before the note; the review of the design and the changed code, with the solves running, each change after the pin by its own dated commit, and one to the run's files or the instrument only after the last solve; the dated note on the census page, naming the pin current on its date and the one the solves ran under; the reads, the fresh controls and their pass first; the locator on $`\mathcal{O}_3`$'s bracket and the member $`i`$'s top, each by its own dated commit; and the record [MC, design head, §§ 4, 7]. After the review, the first pin's change A, which compared a set's members at the top cutoff's linking distance, was replaced before any read by the one of § 5.3, which reads a set by its eigenvalues. The change landed after the last solve at $`N = 24`$, 32 and 40, so those solves ran under the first pin and their reads under the next, one dated note naming both [MC, design § 3; record § 1]. What the design stated before the reads, and what the reads found, are in § 5.3.

The record names no deviation in the runs: each stage ran from its pinned tree, in its terms' order, and every job completed once. The computation's looks beyond its terms decide nothing. Between the two pins at $`N = 48`$, where the top terms allow checks on each seed's check and each point's acceptance alone, the solve checks also set each point's reached amplitude against its record at $`N = 40`$, and say so. After the reads come the zero of $`L`$'s eigenvalue that changes sign in $`\mathcal{O}_3`$'s bracket in $`R_4`$, with the neighbourhood around it where K1 cannot hold, and the limit of the quartet's real part at the member $`i`$'s top, on the ratio of its last two steps, each inferred (§ 5.3). What was stated before the reads stands as stated, its misses kept [MC, record § 9].

### A.3 The fresh controls

Before any branch was read, six control points ran at amplitudes no earlier record holds, beside M8.18's two failures, each with marks fixed before any read on its ladder: the case's own type and indices, K1 and branch identity at every cutoff, and the two verdicts, those of Table 7 on the first ladder. No branch was read until a pass for the first ladder's marks was on record, and no point of the member $`i`$'s top at $`N = 48`$ until a pass for the second ladder's, which the top terms fixed. Every point holds every mark set for it, on both ladders [MC, record § 2; design § 5; top terms § 4].

| Control | $`\varepsilon`$ | As built | Changed | Marked, as built / changed |
|---|---|---|---|---|
| the pyramid control (P5) | 0.24 | Unresolved | converged | Unresolved, by a new link at `N = 40` alone / converged |
| the pyramid control (P5) | 0.30 | converged | converged | converged / converged |
| the C3 ray's control in $`R_4`$ (C3R/R4) | 0.20 | Unresolved | converged | Unresolved, by D's flag at `N = 40` alone, B clearing it / converged |
| the C3 ray's control in $`R_4`$ (C3R/R4) | 0.30 | converged | converged | converged / converged |
| the weight-7/2 member $`i`$ in $`R_2`$ (C2b) | 0.30 | converged | converged | converged / converged |
| the coherent orbit in $`R_5`$ (C2a/R5) | 0.30 | converged | converged | converged / converged |

*Table 7.* MIT's fresh controls on the ladder $`N = 24`$, 32 and 40: each point's verdict as built and as changed, and the verdicts marked for it before the read, as built / changed [MC, record § 2]. In parentheses, the record's names for the controls. On the second ladder, $`N = 32`$, 40 and 48, every changed verdict is marked converged, and three as-built marks differ from these: the pyramid control at 0.24 is reported, not marked, and reads converged; the C3 ray's control in $`R_4`$ is marked Unresolved, by D's flag at $`N = 40`$ and 48 alone at 0.20, and at $`N = 48`$ alone at 0.30, B clearing it at both [MC, record § 2; top terms § 4]. D's flag is the gray-zone flag of $`n(D)`$, and B is change B (§ 5.3).

A pass shows that these points hold their marks on this code, and no more. It does not show that a pair is stable at any other point: the points at 0.30 show only that nothing moved there, and the C3 ray's control at 0.20 is hyperbolic, so it does not exercise the changed test of branch identity [MC, design § 5].

### A.4 Reading again, reproducing, rebuilding

Before any read at $`N = 48`$, the stored reads at $`N = 32`$ and 40, at every point the second ladder reads, were read again on the run's machine: 36 point-reads, each equal to its stored read field for field, in value and type, timings aside [MC, record § 1].

The locator's reproduction of M8.18's location, before its read of $`\mathcal{O}_3`$'s bracket in $`R_4`$, is in § 5.3. The record recomputes each point's classification, as built and changed, from its reading file, 141 points on the two ladders, and finds every one equal to the file's [MC, record head, § 1]. The check on the member $`i`$'s finer path is in § 6.5.

### A.5 The machine, and reproduction

The run's machine ran Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate, under macOS 15.8.2, on one Apple M3, four jobs at a time with M8.18's thread setting, kept because one thread, leaving a solve unchanged, moves one record field at $`N = 24`$ in its round-off [MC, record § 1; design § 4]. The solutions come with the record. The read and reading files stay on the author's bench, outside the repository, each named by its SHA-256 in the job record that wrote it, and can be read again from the solutions on the pinned trees [MC, record head]. A checkout of the folder, `files/framework/files/working/files/scripts/soft-slot-dynamics-mit/`, holds the solutions but not those files, so reproduction runs on a copy whose `run/out/` also holds them: it checks the SHA-256 sums and the manifest against its pin, rebuilds the record and recomputes every classification with `python3 -I -B tools/build_record.py MIT_REPO --check`, `MIT_REPO` being a clone of MIT's repository, and reads the development runs from the same files [MC, record § 10]. Bitwise agreement on another machine is not claimed: the computation's comparisons are bit for bit on its own machine, and elsewhere they agree to round-off [MC, record § 10].

## References

- **[BC]** L. S. Brown and J. C. Collins, Dimensional renormalization of scalar field theory in curved space-time. *Ann. Phys.* **130** (1980), 215–248; [doi:10.1016/0003-4916(80)90232-8](https://doi.org/10.1016/0003-4916(80)90232-8).
- **[CL]** T. Cazenave and P.-L. Lions, Orbital stability of standing waves for some nonlinear Schrödinger equations. *Commun. Math. Phys.* **85** (1982), 549–561; [doi:10.1007/BF01403504](https://doi.org/10.1007/BF01403504).
- **[HKI]** The Hamiltonian–Krein Identification, an MIT working page at `fb84a81d`: [`hamiltonian-krein-identification.md`](../../working/files/hamiltonian-krein-identification.md).
- **[IKL]** I. S. Iohvidov, M. G. Krein and H. Langer, *Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*. Akademie-Verlag, Berlin, 1982, Mathematical Research 9; [doi:10.1515/9783112735992](https://doi.org/10.1515/9783112735992).
- **[Ka]** T. Kato, *Perturbation Theory for Linear Operators*. Classics in Mathematics, Springer, Berlin, 1995; [doi:10.1007/978-3-642-66282-9](https://doi.org/10.1007/978-3-642-66282-9).
- **[KKS]** T. Kapitula, P. G. Kevrekidis and B. Sandstede, Counting eigenvalues via the Krein signature in infinite-dimensional Hamiltonian systems. *Physica D* **195** (2004), 263–282; [doi:10.1016/j.physd.2004.03.018](https://doi.org/10.1016/j.physd.2004.03.018); with a note under the same title, *Physica D* **201** (2005), 199–201; [doi:10.1016/j.physd.2004.11.015](https://doi.org/10.1016/j.physd.2004.11.015).
- **[Ko]** B. Kostant, The Coxeter element and the branching law for the finite subgroups of SU(2) (2004); [arXiv:math/0411142](https://arxiv.org/abs/math/0411142).
- **[KP]** T. Kapitula and K. Promislow, *Spectral and Dynamical Stability of Nonlinear Waves*. Applied Mathematical Sciences, Springer, New York, 2013; [doi:10.1007/978-1-4614-6995-7](https://doi.org/10.1007/978-1-4614-6995-7).
- **[KS]** R. C. Kirby and M. G. Scharlemann, Eight faces of the Poincaré homology 3-sphere. In *Geometric Topology* (Athens, GA, 1977), J. C. Cantrell, ed., Academic Press, New York, 1979, 113–146; [doi:10.1016/B978-0-12-158860-1.50015-0](https://doi.org/10.1016/B978-0-12-158860-1.50015-0).
- **[MC]** MIT's own computation of the census's open items, outside M8: its [record](../../working/files/scripts/soft-slot-dynamics-mit/RECORD.md), [design](../../working/files/scripts/soft-slot-dynamics-mit/run/DESIGN.md), [locator terms](../../working/files/scripts/soft-slot-dynamics-mit/run/LOCATOR.md), [top terms](../../working/files/scripts/soft-slot-dynamics-mit/run/TOP48.md) and [development log](../../working/files/scripts/soft-slot-dynamics-mit/DEVLOG.md), MIT pages at `fb84a81d`.
- **[OW10]** OpenWave M8 track, M8.10: first correction at the level-6 critical rays. Its [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_10_method_note.md), at OpenWave commit b0b07867, 2026.
- **[OW12]** OpenWave M8 track, M8.12: the reduced Morse census of the level-6 quartic. Its [method note](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md), at OpenWave commit b0b07867, 2026.
- **[OW15]** OpenWave M8 track, M8.15: the continuation and persistence run on the soft-slot branches, adjudicated on OpenWave [#620](https://github.com/openwave-labs/openwave/pull/620). Its record, an MIT page at `fb84a81d`: [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics/RECORD.md).
- **[OW15.1]** OpenWave M8 track, M8.15.1: the location of the two index changes M8.15 bracketed, adjudicated on OpenWave [#625](https://github.com/openwave-labs/openwave/pull/625#pullrequestreview-5492753760). Its record, an MIT page at `fb84a81d`: [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-15x-target1/RECORD.md).
- **[OW15.2]** OpenWave M8 track, M8.15.2: the location of two index changes through the structural-subspace failure, adjudicated on OpenWave [#632](https://github.com/openwave-labs/openwave/pull/632#pullrequestreview-5511519208). Its record, an MIT page at `fb84a81d`: [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-15-2/RECORD.md).
- **[OW16]** OpenWave M8 track, M8.16: a qualification of the harmonic Galerkin instrument at a pyramid control and five other controls, adjudicated not qualified on OpenWave [#640](https://github.com/openwave-labs/openwave/pull/640#pullrequestreview-5575251218). Its terms and record, MIT pages at `fb84a81d`: [`m8_16_task_details.md`](../../working/files/scripts/soft-slot-dynamics-m8-16/run/m8_16_task_details.md) and [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-16/RECORD.md).
- **[OW16.1]** OpenWave M8 track, M8.16.1: a second qualification of the harmonic Galerkin instrument, qualified with nine branches, adjudicated on OpenWave [#653](https://github.com/openwave-labs/openwave/pull/653#pullrequestreview-5646373760). Its record, an MIT page at `fb84a81d`: [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-16-1/RECORD.md).
- **[OW17]** OpenWave M8 track, M8.17: the slot dynamics census run, on the nine branches M8.16.1 qualified, adjudicated on OpenWave [#676](https://github.com/openwave-labs/openwave/pull/676#pullrequestreview-5691493287). Its terms and record, MIT pages at `fb84a81d`: [`m8_16_task_details.md`](../../working/files/scripts/soft-slot-dynamics-m8-17/run/m8_16_task_details.md) and [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-17/RECORD.md).
- **[OW18]** OpenWave M8 track, M8.18: the two remedies after M8.17, adjudicated on OpenWave [#692](https://github.com/openwave-labs/openwave/pull/692#pullrequestreview-5730646319). Its record, an MIT page at `fb84a81d`: [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-18/RECORD.md).
- **[OW19]** OpenWave M8 track, M8.19: the census's persistence tests, adjudicated on OpenWave [#705](https://github.com/openwave-labs/openwave/pull/705#pullrequestreview-5849541157). Its terms and record, MIT pages at `fb84a81d`: [`m8_19_task_details.md`](../../working/files/scripts/soft-slot-dynamics-m8-19/run/m8_19_task_details.md) and [`RECORD.md`](../../working/files/scripts/soft-slot-dynamics-m8-19/RECORD.md).
- **[Pa]** R. S. Palais, The principle of symmetric criticality. *Commun. Math. Phys.* **69** (1979), 19–30; [doi:10.1007/BF01941322](https://doi.org/10.1007/BF01941322).
- **[PC]** The Projective Carrier, an MIT working page at `fb84a81d`: [`projective-carrier.md`](../../working/files/projective-carrier.md).
- **[Pe]** D. E. Pelinovsky, Inertia law for spectral stability of solitary waves in coupled nonlinear Schrödinger equations. *Proc. R. Soc. A* **461** (2005), 783–812; [doi:10.1098/rspa.2004.1345](https://doi.org/10.1098/rspa.2004.1345).
- **[SA]** The Slot Action, an MIT working page at `fb84a81d`: [`slot-action.md`](../../working/files/slot-action.md).
- **[SDC]** The Slot Dynamics Census, an MIT working page at `fb84a81d`: [`slot-dynamics-census.md`](../../working/files/slot-dynamics-census.md).
- **[SF]** S. Sonego and V. Faraoni, Coupling to the curvature for a scalar field from the equivalence principle. *Class. Quantum Grav.* **10** (1993), 1185–1187; [doi:10.1088/0264-9381/10/6/015](https://doi.org/10.1088/0264-9381/10/6/015).
- **[SGS]** The Slot Ground States, an MIT working page at `fb84a81d`: [`slot-ground-states.md`](../../working/files/slot-ground-states.md).
- **[Sh]** B. Shatto, The Surviving Ray: the spin-3 coupling point that $`S^3/2I`$ selects, and its critical geometry. *Zenodo* (2026), [doi:10.5281/zenodo.22681501](https://doi.org/10.5281/zenodo.22681501). Its sections are cited as numbered in its second version, [doi:10.5281/zenodo.24145098](https://doi.org/10.5281/zenodo.24145098); the living text is the repository page at `fb84a81d`, [`surviving-ray.md`](../../bedrock/files/surviving-ray.md), whose numbering differs in places.
- **[Sha]** J. Shatah, Stable standing waves of nonlinear Klein-Gordon equations. *Commun. Math. Phys.* **91** (1983), 313–327; [doi:10.1007/BF01208779](https://doi.org/10.1007/BF01208779).
- **[SRel]** The Slot Relation, an MIT working page at `fb84a81d`: [`slot-relation.md`](../../working/files/slot-relation.md).
- **[SSB]** The Soft-Slot Branches, an MIT working page at `fb84a81d`: [`soft-slot-branches.md`](../../working/files/soft-slot-branches.md).
- **[STB]** The Stress-Tensor Bridge, an MIT working page at `fb84a81d`: [`stress-tensor-bridge.md`](../../working/files/stress-tensor-bridge.md).
- **[Su]** R. Suter, Quantum affine Cartan matrices, Poincaré series of binary polyhedral groups, and reflection representations. *Manuscripta Math.* **122** (2007), 1–21; [doi:10.1007/s00229-006-0055-1](https://doi.org/10.1007/s00229-006-0055-1).
- **[VK]** N. G. Vakhitov and A. A. Kolokolov, Stationary solutions of the wave equation in a medium with nonlinearity saturation. *Radiophys. Quantum Electron.* **16** (1973), 783–789; [doi:10.1007/BF01031343](https://doi.org/10.1007/BF01031343).

---

| **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |
