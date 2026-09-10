<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 📐 Framework

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/geometric%20code%20banner.png?raw=true" width="100%" alt="The Geometric Code: Mode Identity Theory">

Mode Identity Theory is a boundary-condition framework. It leaves Einstein's field equations governing local gravitational dynamics and the Standard Model particle content unchanged, and supplies one new thing: a global topological domain for them to live on.

Picture it before the formal names arrive: twist a strip into a Möbius band, scale its single edge up to the size of the universe, and set the whole thing inside the three-sphere, the one closed three-dimensional space that is simply connected, finite, with no boundary and no holes. That single edge is the theory's temporal edge, where time is carried as phase. The space it sits in closes on itself, so there is no outside to ask about.

That geometric setup is where the whole theory starts. The particles, the forces, and the constants are not added to it as separate ingredients; they are read from the structure itself, as modes, positions, and relations on the domain.

The shape has two layers: the smooth three-sphere underneath, and the structure built on it where the physics is resolved. The twists and identifications live in that built structure; the covering space underneath stays smooth and simply connected.

The postulate itself is one sentence: **time is the boundary of a non-orientable surface embedded in a closed three-space.**

The observable domain is not that smooth covering space itself but its quotient by the binary icosahedral group, a symmetry group of order 120: fold the space down by that symmetry, and the result is the Poincaré homology sphere. Together, the embedded Möbius band and the 2I quotient fix what is rigid: the boundary condition, the mode domain, the stabilizers, and the McKay graph. What is read off that structure ranges in firmness, from the dimensionless ratios that need no anchor at all to the well positions, grids, and exponents whose selection rule the theory is still working to state; measured anchors set only the absolute scales.

---
<a id="table-of-contents"></a>
### -Table of Contents-

<table>
<tr>
<td valign="top">

**[The Firing Order](#the-firing-order)**
  - The ontological chain

**[One Shape](#one-shape)**
  - Space, Surface, Temporal Edge
  - Why $`S^3/2I`$
  - The Sampling Grids
  - The Chronon

**[One Wave](#one-wave)**
  - Redshift and Cooling
  - The Waltz Clock
  - The Present Epoch

**[One Equation](#one-equation)**
  - What the ratio means
  - The Phase Operator
  - Fibonacci Wells
  - The Hierarchy and the Observer
  - Manifold Index
  - The Phase Field
  - The Assembled Engine

**[One Identity](#one-identity)**
  - The particle address
  - Faces sort color
  - Edges sort spin
  - Vertices set electroweak address

</td>
<td valign="top">

**[One Ladder](#one-ladder)**
  - The Gauge Ladder
  - Supersymmetry

**[One Formula](#one-formula)**
  - The Gauge Gap
  - Three Generations
  - The Mass Formula

**[One Interface](#one-interface)**
  - The two seams
  - Gravity is what crosses

**[Inputs and Calibration](#inputs-and-calibration)**
  - The Ω ledger
  - Unit constants
  - The dimensionless core
  - Three readings of one hierarchy
  - Sector anchors
  - Predicted and calibrated

**[Research Frontier](#research-frontier)**
  - The three problems
  - Recorded nulls
  - Forward tests

</td>
</tr>
</table>

>📗 marks a **canonical paper**: the standalone treatment where the point at hand is worked out in full.

>📒 marks a **working note**: research in progress on the point at hand, not yet settled.

---
<a id="the-firing-order"></a>
## ⚙️ The Firing Order

*In what order does the theory have to be built?*

Mode Identity Theory is built upon a specific order of operation. Each step depends on the one before, and nothing later in the sequence exists independently from what came prior.

- Topology sets what is possible.
- Embedding defines the structure.
- The Cosmic Wave expresses the boundary.
- Time is phase of the wave.
- Sampling resolves position in the domain.
- Meaning arises only after realization.

>[![One Shape](https://img.youtube.com/vi/U3VtY8GZox8/mqdefault.jpg)](https://www.youtube.com/watch?v=U3VtY8GZox8)
>
>*Video: [The Perfect Shape](https://www.youtube.com/watch?v=U3VtY8GZox8)*

[↑ Table of Contents](#table-of-contents)

---
<a id="one-shape"></a>
## 🏟️ One Shape

*What space is this, and why must it be this one?*

```math
\Large {S^1 = \partial(\text{Möbius}) \hookrightarrow S^3, \quad \partial S^3 = \emptyset}
```

A temporal edge bounds a non-orientable surface embedded in a closed space, and the space has no boundary. The manifold triad is pinned by a theorem and a minimality choice: surface classification with minimality selects the Möbius strip, the minimal non-orientable surface with one boundary, and the simply connected closed cover is $`S^3`$ by the Poincaré theorem. The observable domain is its quotient $`S^3/2I`$, selected on the grounds given below. Together these choices define the canonical realization the framework carries.

### Space

$`S^3`$ is the only simply connected closed 3-manifold (Poincaré). It is diffeomorphic to SU(2) and admits a spin structure, and the framework equips it with the round metric of curvature radius $`R_\Lambda`$. The space has no boundary:

```math
\Large {\partial S^3 = \emptyset}
```

The hierarchy terminates here. "What's outside?" is malformed; there is no boundary from which to observe.

### Surface

A Möbius strip has one side and one edge. Carry the normal once around the Möbius core and it returns reversed. That sign is the holonomy of the orientation line bundle; MIT reads the resulting anti-periodic sector as the topological origin of fermionic character. The Möbius strip is also the simplest surface that carries such a bundle: by the classification of compact surfaces, a connected non-orientable surface with one boundary component is a disk removed from a connected sum of $`k`$ crosscaps, and the Möbius strip is the minimal case ($`k = 1`$), the one minimality selects. Non-orientability produces three consequences:

| Consequence | Mechanism |
|---|---|
| Anti-periodic BC | Sections of the orientation bundle acquire a sign flip: $`\psi(y + \pi R_\Lambda) = -\psi(y)`$ |
| Half-integer spectrum | Mode numbers $`\nu = 1/2, 3/2, 5/2, \ldots`$; the constant mode is forbidden |
| $`Z_2`$ holonomy | The normal direction reverses under one traversal |

For an orientable surface the orientation bundle is trivial, so none of the three follows.

The eigenvalue problem $`-\partial_y^2 \psi = \lambda \psi`$ under the anti-periodic condition requires $`e^{ik\pi R_\Lambda} = -1`$, so $`k = (2m+1)/R_\Lambda`$; with the mode number $`\nu = kR_\Lambda/2`$ the allowed values are the half-integers $`\nu = 1/2, 3/2, 5/2, \ldots`$, and the constant mode ($`k = 0`$) is forbidden. This is the lifted phase-lap spectrum, not the full surface Laplacian: on the constant-curvature Möbius model the ground state depends on the cone extension, the choice of self-adjoint boundary behaviour at the cone point, and no extension has a strictly positive bottom, while the first positive surface level is stable at $`2/R_\Lambda^2`$ in the first-eigenvalue paper's regime, the level MIT later reads as $`\Lambda_{\text{top}}`$.

>**📗 [First Eigenvalue](files/bedrock/files/first-eigenvalue.md):** the twisted Möbius Laplacian in full, fixing the first positive surface level at $`2/R_\Lambda^2`$ that MIT reads as $`\Lambda_\text{top}`$.

>**📒 [Cone Point Coherence](files/working/files/cone-point-coherence.md):** whether the cone-point coherence scale sources galactic curvature, the working program behind the galactic-curvature gate.

### Temporal Edge

$`S^1`$ is the boundary of the Möbius surface. The strip has longitudinal period $`L = \pi R_\Lambda`$ (one lap), and the boundary $`S^1`$ traverses the strip twice before closing, giving geometric circumference $`2L = 2\pi R_\Lambda`$. The anti-periodic flip acts per lap, $`\psi(y + \pi R_\Lambda) = -\psi(y)`$, on the one-lap lift of the orientation-twisting core loop, not on the closed edge itself; over two laps the field returns to $`+\psi`$, so the closed edge is globally periodic with trivial total orientation holonomy, while the $`4\pi`$ wave period lives on the lifted phase coordinate. This is where time advances and where the observer is anchored. The $`S^1`$ here is the phase cycle of the standing wave, not a closed timelike coordinate of the Lorentzian metric; proper time along an observer history is monotone over the epoch.

The chronon and the standing-wave period operate in the phase parameter $`t \in [0, 4\pi]`$, not in geometric length. The factor $`4\pi`$ is the anti-periodic wave period, two sign-flip laps of the strip, dimensionless.

### Why $`S^3/2I`$

The observable domain is $`S^3/2I`$: the hypersphere modulo the binary icosahedral group $`2I`$, with $`\lvert 2I\rvert = 120`$. The discrete subgroups of SU(2) $`\cong S^3`$ are classified into open families (cyclic $`Z_n`$ and binary dihedral $`2D_n`$, parameterized by $`n`$) and three closed exceptional groups (binary tetrahedral $`\lvert 2T\rvert = 24`$, binary octahedral $`\lvert 2O\rvert = 48`$, binary icosahedral $`\lvert 2I\rvert = 120`$).

Open families require an external choice of $`n`$ and fall to the framework's input-minimization. Among the closed exceptional cases $`2I`$ is terminal, largest in order and maximal under the McKay correspondence, where it identifies with $`E_8`$, the largest exceptional Lie algebra.

$`2I`$ is the unique nontrivial perfect finite subgroup of SU(2), equal to its own commutator subgroup, so its only one-dimensional character is the trivial one. With no nontrivial character to twist by, the standard connection $`Q`$ and its Galois conjugate $`Q'`$ stay distinct under every twist, two genuinely different flat vacua rather than one dressed up as another. That split has a spectral consequence which selects the domain a second time: the Galois vacuum's gap is the unique exception across the whole ADE classification of finite subgroups of SU(2), proved in the coexact-gap paper and derived where it is used, in [One Formula](#one-formula). Counting the flat connections on the quotient closes the list at three: the trivial one, the standard $`Q`$, and the Galois conjugate $`Q'`$. That count is what later sections range a vacuum label over; its isolation and its reading as the three generations are [One Formula](#one-formula). Terminality and perfectness are two independent grounds converging on one domain; the theorem folding them into one proof, framework requirement $`\Rightarrow 2I`$, is open.

>**📒 [The Postulate Bridge](files/working/files/postulate-bridge.md):** the staged route from the postulate to the derivations, and the terminality-and-perfectness theorem the domain selection still needs.

### The Sampling Grids

The full $`2I`$ sampling resolution carries 120 sign-sensitive labels. Fermions access all 120, while the framework's intensity readout squares the wavefunction: $`\lvert\psi(\Theta+1)\rvert^2 = \lvert\psi(\Theta)\rvert^2`$ erases the central sign, passing from the $`2I`$ labels to the $`I`$ labels ($`\lvert I\rvert = 60`$) and reducing the bosonic readout to the 60R projection. The 60R grid is the central-sign quotient $`2I \to I`$, what survives that projection, while the full 120 grid retains the sign-sensitive representation data. That two resolutions exist is the representation theory; which observable reads on which is a separate step, and reading photon-mediated quantities onto 60R is a motivated grid assignment, not a derivation. That halving is the squaring itself, a fact about the representation rather than a geometric move: the Möbius sign flip and the central $`-I`$ of $`2I`$ are two distinct $`Z_2`$'s, and the natural sampler built from the Möbius geometry does not carry one onto the other.

The sampling dictionary uses those two resolutions as follows:

| Grid | Labels | Minimum step | Observables |
|---|---|---|---|
| Full $`2I`$ resolution | 120 | 1/120 | $`a_0`$ (dynamical) |
| Bosonic projection | 60 | 2/120 | $`H_0`$, $`\Lambda`$, $`\alpha`$ (photon-mediated) |

The 120 is the order of $`2I`$, not a feature of the smooth $`S^3`$ beneath it. Two questions about these grids are answered elsewhere and are not repeated here: what the order's prime factorization means, and why the central sign sorts the two representation classes, are [One Identity](#one-identity); which positions on the grids the framework samples is [One Equation](#one-equation).

### The Chronon

On the framework's 120-step phase resolution, the smallest registrable advance is:

```math
\Delta t_{\min} = \frac{4\pi}{120} = \frac{\pi}{30}
```

MIT associates that phase increment with the action step $`\Delta\mathcal{S}_{\min} = \hbar\pi/30`$. Within the 120-step sampling dictionary the increment $`\pi/30`$ is a pure number set by the topology rather than a coordinate choice, and $`\hbar`$ is invariant, so the associated action phase $`\mathcal{S}/\hbar`$ is frame-independent.

[↑ Table of Contents](#table-of-contents)

---
<a id="one-wave"></a>
## Ψ One Wave

*What is waving, and what makes it time?*

The domain is static; its temporal edge carries a standing wave, and what is read as cosmic time is the observer's phase along it. On the one-lap lift of that edge the Möbius identification is anti-periodic, the same sign flip that gives matter its fermionic character: one traversal flips the wave, the closed edge restores it after the second, and the fundamental phase period is $`4\pi`$ rather than $`2\pi`$. It opens at full amplitude, holds its selected fundamental mode, and where the observer samples it, matter appears.

Anti-periodicity, the initial-maximum condition ($`\Psi(0) = +1`$), and selection of the fundamental temporal mode ($`m = 0`$) together fix:

```math
\Large {\Psi = \cos(t/2)}
```
<br>

| Condition | Selects | Why |
|---|---|---|
| Anti-periodic BC | Period $`4\pi`$ | Sign flips per lap; two laps to restore it |
| $`\Psi(0) = +1`$ | Cosine over sine | $`t = 0`$ at amplitude maximum; $`\partial_t\Psi\big\vert_{t=0} = 0`$ |
| Lowest admissible harmonic $`m = 0`$ | The fundamental, no overtones | Isotropy ($`10^{-5}`$) and orthogonality (Gpc integration) select it |

The cosine has a complement. Write $`S = \sin(t/2)`$; then $`\Psi^2 + S^2 = 1`$ partitions the total amplitude into two shares at every phase. MIT reads the two shares as standing-wave content and realized-mode content: cosmic evolution is their bounded transfer, weight moving $`\Psi^2 \to S^2`$ as the phase advances and the resolved fraction grows. That single state variable $`S`$ is what the cosmological observables read.

**MIT does not posit expansion of the underlying $`S^3`$.** Its radius is fixed; cosmological expansion is represented through an effective, phase-based description, and completing that description dynamically is open. What that description reads is the single state variable $`S`$, through the dictionary and the clock below.

>**📗 [Dark Energy](../cosmos/files/dark-energy.md):** the effective, phase-based expansion history in full, where what evolves is not $`\Lambda`$ but perception.

### Redshift and Cooling

Redshift is a phase ratio, $`1 + z = S(t_\text{obs})/S(t_\text{emit})`$, the observer reading the wave from farther along it rather than space carrying source and observer apart. The effective distance relation carries a scale factor $`a_\text{eff} \propto S`$, and in that effective metric the phase ratio is the ordinary null-geodesic result, so the standard FLRW distance relation is recovered as the translation layer for comparison with observations.

Cooling applies the same ratio to the bath: every wavelength rescales by $`S`$, photon number density by $`S^{-3}`$ at conserved photon count, radiation energy density by $`S^{-4}`$, and the Planck blackbody is preserved at $`T \propto 1/S`$. The fixed quantity is the spectral radius, not the effective volume; where the redshifted photon energy goes is left to the same stress-energy accounting still under construction.

>**📒 [Redshift and Cooling](files/working/files/redshift-and-cooling.md):** redshift as phase-sampling and cooling as the same ratio on the bath, worked from the standing wave.

### The Waltz Clock

The Waltz clock advances budget phase, the argument $`t`$ of $`\Psi = \cos(t/2)`$, in two steps set by $`a_\text{eff} \propto S`$. The registered interface tick, the measure that accumulates one unit per act of realization, accumulates as $`d\mu_{\text{tick}} = S^{3/2}\,dt`$, and dividing by the scale factor gives the Hubble clock $`d\tau_H = S^{1/2}\,dt`$ the distance model runs on, with $`dt/d\tau_H = S^{-1/2}`$. The fitted rate reads $`H = (1/S)\,dS/d\tau_H \propto \Psi/S^{3/2}`$. That $`-1/2`$ exponent enters through the GR correspondence: matter dilution supplies the three-dimensional factor $`S^{-3}`$, the Friedmann relation reads its square root, and the clock keeps the $`S^{-1/2}`$ power. With the vacuum-reference $`\Lambda`$ supplying the constant term, that clock fits Pantheon+ and DESI DR2 BAO at $`\Delta\chi^2 = +0.11`$ versus flat ΛCDM at the same parameter count, three fitted on each side ($`s_0`$, $`H_0 r_d`$, $`M_B`$) with the vacuum fraction held at the named anchor rather than fitted (temporal budget), while integer-power alternatives miss those distances by wide margins. Read as an expansion history in the ΛCDM way, that is the familiar shift from the matter-only $`q_0 = +0.5`$ to the observed $`q_0 \approx -0.55`$, a translation of the distance relation rather than a motion of the domain; the budget map keeps the full accounting.

>**📒 [The Budget Map](files/working/files/budget-map.md):** the inventory of what is a budget and what is read off one, pinning temperature and entropy as readings of the single state $`S`$.

>**📒 [Temporal Budget Identity](files/working/files/temporal-budget.md):** the $`\Psi^2 + S^2 = 1`$ budget and the Λcos clock fit to Pantheon+ and DESI DR2 BAO.

Two things about the clock are not closed, and they are one problem rather than two. The $`-1/2`$ exponent enters through the GR correspondence rather than from the postulate layer, and the map from the static geometry to the effective metric the distance model runs on has no derived source. The stress-tensor bridge carries the arithmetic, including why the native machinery and the anchored vacuum term are demonstrably not both carried by one fixed metric under the original clock, which is why $`\Lambda`$ enters as its own object rather than falling out of the budget. [One Interface](#one-interface) poses the same gap as gravity's open construction, and the [Research Frontier](#research-frontier) states it as the Dynamics problem.

>**📒 [Variational Score-to-Sample](files/working/files/variational-score-to-sample.md):** the variational route to the clock exponent, a global score-to-sample principle sought independently of the target power.

>**📒 [Friedmann as Output](files/working/files/friedmann-as-output.md):** the half-power clock, deriving the $`S^{-1/2}`$ exponent and the Friedmann relation as an output rather than an import.

### The Present Epoch

Two phase parameterizations meet at the present epoch. The engine phase $`\Phi = 4\pi\, T/T_\text{cycle}`$ is linear in the Hubble-clock age $`T`$, with $`\Phi_\text{now}`$ under re-derivation; the budget phase $`t`$, the argument of $`\Psi = \cos(t/2)`$, is nonlinear in it through that same clock, and distance data pin $`s_0 = \sin(t_\text{now}/2) < 0.19`$ (95% CL). The mapping $`t(\Phi)`$ between them is still open, and until it closes the present age is read only after the clock is calibrated, so the familiar 13.8 Gyr is carried over from ΛCDM rather than recovered here. The distance-redshift relation is written in the budget phase $`t`$; the engine phase $`\Phi`$ refers to the same cycle, but with $`t(\Phi)`$ still to be derived $`\Phi_\text{now}`$ is bookkeeping, not an independent cosmological clock. The $`4\pi`$ anti-periodic period is topology-native; the 120-step chronon is the framework's sampling resolution on that period, independent of which parameterization labels it.

>[![Time](https://img.youtube.com/vi/9N6g-kDgUDc/mqdefault.jpg)](https://www.youtube.com/watch?v=9N6g-kDgUDc)
>
>*Video: [The Machinery of Time](https://www.youtube.com/watch?v=9N6g-kDgUDc)*

[↑ Table of Contents](#table-of-contents)

---
<a id="one-equation"></a>
## ⚖️ One Equation

*Why does a constant have the size it has?*

```math
\Large {\frac{A}{A_P} \approx C(\Theta) \cdot (\sqrt{\Omega})^{-n}}
```

Each quantity the law addresses is one kind of thing, sampled at one position and one depth. The scaling law reads: **how big is this thing compared to the natural Planck unit for its kind,** $`A/A_P`$, equals **where it sits on the wave,** $`C(\Theta)`$, times **how far the geometry has diluted it from the Planck scale,** $`(\sqrt{\Omega})^{-n}`$.

The law reads as one line, but four claims sit inside it at different strengths. The phase profile $`C(\Theta)`$ is fixed within the spectral-boundary class, family forced and member selected. The integer-depth power is fixed by exact homothety at definite weight. Their separation into a pure position factor and a pure spectral factor still awaits the commutant theorem $`\mathcal{A}_\text{obs} = \mathcal{A}_\Theta \otimes \mathcal{A}_\text{spec}`$: independent coordinates do not by themselves forbid a mixed term, and closing that is the law's open keystone. The wells the law is sampled at, and the assignment of an observable to each, are the selection layer that follows. Run together the law looks more derived than it is; kept apart, each is exactly as strong as its own argument.

>**📒 [Scaling Law Uniqueness](files/working/files/scaling-law-uniqueness.md):** the scaling law read as a separated measurement form, and the admissibility conditions the separation still requires.

### What the ratio means

$`A_P`$ is the Planck reference: the natural scale for that *kind* of quantity, built from nothing but $`G`$, $`\hbar`$, and $`c`$.

| Planck unit | Value | What it sets |
|---|---|---|
| $`\ell_P \approx 1.6 \times 10^{-35}`$ m | length | the quantum-gravity length scale |
| $`t_P \approx 5.4 \times 10^{-44}`$ s | time | the light-crossing time of $`\ell_P`$ |
| $`m_P \approx 2.2 \times 10^{-8}`$ kg | mass | where gravity and quantum mechanics meet |

So $`A/A_P`$ just asks how big the measured thing is in those units. For the Hubble rate the reference is $`t_P^{-1}`$, and $`H_0 / t_P^{-1} \approx 10^{-61}`$: the Hubble rate is about $`10^{61}`$ times slower than the Planck rate. For the cosmological constant the reference is $`\ell_P^{-2}`$ (a curvature), and $`\Lambda / \ell_P^{-2} \approx 10^{-122}`$: the vacuum curves space about $`10^{122}`$ times more weakly than the Planck scale would suggest.

**The classical mystery is why these ratios are so absurdly small.** MIT reads that smallness as the hierarchy factor $`(\sqrt{\Omega})^{-n}`$, the price of living on the edge ($`n = 1`$) or the surface ($`n = 2`$) of the geometry instead of at the Planck floor. What the index accounts for is the *form* of the suppression, one power per geometric layer, and the fixed ratio between layers. It does not account for the hierarchy's own size: $`\Omega`$ is read from an anchor, not derived, as [Inputs and Calibration](#inputs-and-calibration) states. That factor sets the orders of magnitude; the position factor $`C(\Theta)`$ sets the leading digits. Once the single-ratio monomial form is granted, each sector supplies one hierarchy ratio; that the class carries a definite weight is an admissibility condition the uniqueness argument names, not a theorem the law proves.

**The sample occurs at** $`(t, \Theta)`$: a moment in the wave's phase, at a position on the grid.

### The Phase Operator

$`C(\Theta)`$ is fixed within the spectral-boundary class in two steps. The anti-periodic boundary condition (the Möbius sign flip) forces the sinusoidal family: the eigenbasis is the half-integer tower, with no polynomial, exponential, or rational profile surviving (the uniqueness argument carries the detail). Background symmetry then selects the member: isotropy and orthogonality pick the lowest harmonic, the first-positive mode, and the boundary node picks sine over cosine, giving $`\psi_1(\Theta) = \sin(\pi\Theta)`$, zero at the two boundaries and peaking at the antinode. An observer registers intensity, the squared amplitude, so the weight is $`\lvert\psi_1\rvert^2 = \sin^2(\pi\Theta)`$, normalized to unit mean over the domain, the normalization being the second selection principle the boundary condition does not supply and the one that fixes the leading 2:

```math
\Large C(\Theta) = 2\sin^2(\pi\Theta)
```

The temporal anti-periodic tower and this positional profile are distinct eigenproblems sharing the sinusoidal form: the tower lives on the lifted phase lap of the temporal edge, while $`C(\Theta)`$ here is the first-positive intensity read across the sampling interval. One operator, read at every position, the same across all sectors (cosmology reads it at a single well, the mass sector across Kostant-exponent sets, the exponents attached to an irrep by the Coxeter element). For the dimensional constants the powers of ten are units, and the dimensionless physics is the value of $`C(\Theta)`$.

| Position | $`C(\Theta)`$ | Slope $`d\ln C/d\Theta`$ | Significance |
|---|---|---|---|
| $`\Theta = 0`$ (boundary) | 0 | $`\to \infty`$ | No observable amplitude |
| $`\Theta = 1/2`$ (antinode) | 2 | 0 | Maximum amplitude; stationary to first order |
| $`\Theta = 1`$ (boundary) | 0 | $`\to -\infty`$ | No observable amplitude |

$`\Lambda_\text{top}`$ sits at the antinode: slope exactly zero.

The boundary zeros are physical: in the black-hole reading the exterior stationary horizon maps to this $`C \to 0`$ node, closing that sampling channel.

>**📗 [Black Holes](../cosmos/files/black-hole.md):** black holes as topological nodes of the wave, where the exterior horizon maps to the $`C \to 0`$ boundary node.

### Fibonacci Wells

The first-positive wave shape is selected, but not every position on it is a place the framework samples. The candidate sampling positions continue a sequence the domain already carries. The icosahedral branch orders $`(2,3,5)`$, the stabilizer orders of the edges, faces, and vertices of the rotation group beneath $`2I`$ and what [One Identity](#one-identity) reads as the stabilizer primes, are already consecutive Fibonacci terms obeying $`2+3=5`$, and running that same recurrence forward on the fixed 120-grid gives the well sequence. The terms that resolve it are exactly the Fibonacci divisors of 120, namely $`\{1,2,3,5,8\}`$, whose least common multiple is 120; these tile the grid rather than mark new sampling positions. The first Fibonacci term that is not a divisor is $`F_7 = 13`$, the seam between the divisor block that closes at the domain order and the Fibonacci structure that lives on it. The upper end is the wave's own reflection symmetry, $`C(\Theta) = C(1 - \Theta)`$, about the antinode, so no new intensity well appears beyond $`\Theta = 1/2`$. The wells therefore fall between the seam and the antinode at $`13, 21, 34, 55`$, with spacings $`8, 13, 21`$, again consecutive Fibonacci. The golden ratio behind this recurrence is not imported from outside; it is already present in the binary icosahedral character field $`\mathbb{Q}(\sqrt5)`$, the same $`\sqrt5`$ that fixes the exact torsion ratio $`\varphi^{-4}`$ between the Galois-paired vacua.

>**📒 [Fibonacci Wells](files/working/files/fibonacci-wells.md):** the forcing worksheet for why the sampling wells land at $`\{13, 21, 34, 55\}`$, with the variational route ruled out.

That the realized positions continue the recurrence is where this level stops being a theorem. A variational origin was searched for with a signed anti-periodic sweep over eight boundary-mode functionals designed to make the observed set extremal; all eight returned uniform or clustered minimizers, never the wells. So $`\{13, 21, 34, 55\}`$ is a structural label the recurrence carries, not a derived extremum. The golden field is native either way, so the recurrence is the domain's own arithmetic rather than a sampling dynamics imported from outside. Why the realized positions continue it, on the edge where the mirror locates the interference, is open.

>**📗 [The Mirror](../spectrum/files/the-mirror.md):** the curvature duality of primes and matter, and where on the edge the well interference is located.

### The Hierarchy and the Observer

The hierarchy base is sector-specific, one ledger per sector:

```math
\Omega_\Lambda = \left(\frac{R_\Lambda}{\ell_P}\right)^2 \quad \text{(surface, space)},
\qquad
\Omega_H = \left(\frac{c}{H\ell_P}\right)^2 \quad \text{(temporal edge)}
```

$`\Omega_\Lambda`$ is epoch-independent, since $`R_\Lambda`$ is fixed. Its absolute value is not a further output of the law: it is read from one surface anchor, and three candidate anchors exist whose readings do not yet agree, which [Inputs and Calibration](#inputs-and-calibration) states in full. What the law needs here is the ledger and its epoch behaviour, not the choice among those anchors. For the dimensionless couplings the same hierarchy enters as a fractional power that is itself the content: $`\alpha`$ is one grid step of it.

The phase-gradient scale changes with epoch:

```math
\Omega_\Psi(u,x) \equiv \left(\frac{c}{\ell_P\,\kappa_\Psi}\right)^2, \qquad \kappa_\Psi = \lvert u^\mu\nabla_\mu\ln\lvert\Psi\rvert\rvert
```

$`\Omega_\Psi`$ is a second, local hierarchy and is **not** $`\Omega_H`$. It reads the gradient of the standing-wave share where $`\Omega_H`$ reads the rate of the realized one, and no choice of clock closes that gap: for any lapse $`d\tau = N\,dt`$ the factor $`N`$ cancels from the ratio of the two logarithmic gradients, leaving $`(S/\Psi)^2`$. Their ratio is closed-form and fixed by the phase alone,

```math
\frac{\Omega_\Psi}{\Omega_H} = \left(\frac{\Psi}{S}\right)^4 = \frac{(1-S^2)^2}{S^4},
```

which is $`1`$ exactly at budget equipartition $`\Psi^2 = S^2 = 1/2`$ and nowhere else, an identity of the two definitions rather than a result. The present epoch sits far on the $`\Psi`$-dominated side of that crossing, so the two run about $`3 \times 10^4`$ apart at the posterior median. What is open is not the relation but what the second scale is for: which observables read the $`\Psi`$ gradient rather than the $`S`$ rate, and whether the horizon branch needs a length running as $`(\Psi/S)^2`$ against the Hubble radius. It is also observer-dependent, so no observer-independent $`\Omega_\Psi`$ exists until a preferred clock field is supplied; that is the frozen question on [Ω_H(Θ)](files/working/files/omega-h-derivation.md), whose historical $`\Omega_H`$ denotes what this page now calls $`\Omega_\Psi`$.

Everything downstream of this section uses $`\Omega_H`$, the rate ledger. At the present epoch it and $`\Omega_\Lambda`$ are numerically close, both of order $`10^{122}`$. In the current calibration structure this coincidence is observed, not derived: $`\Omega_H`$ is anchored by the measured Hubble rate, $`\Omega_\Lambda`$ by measured $`\Lambda`$.

The domain runs from the Planck floor ($`\Omega = 1`$) up to the cosmic ceiling ($`\Omega \approx 10^{122}`$). Ask where the observer sits, and the geometry answers with its own midpoint: the self-dual point $`x = \Omega/x`$, where the climb to the ceiling equals the drop to the floor.

```math
\Large x = \sqrt{\Omega} \approx 10^{61}
```

MIT identifies that fixed point with the observer scale: in $`\Omega`$ it sits at $`\sqrt{\Omega} = 10^{61}`$, 61 orders from the floor and 61 from the ceiling. This is where observation resolves.

In physical units the same center is a length, the geometric mean of the Planck length and the curvature radius:

```math
\sqrt{\ell_P \, R_\Lambda} \approx 50\ \mu\text{m}.
```

Because $`\Omega = (R_\Lambda/\ell_P)^2`$, distances in length are half those in $`\Omega`$: 50 μm sits about 30 orders of magnitude above the Planck length and 30 below the curvature radius. The geometric mean of these two reference lengths is bound to land somewhere macroscopic; the content here is the specific value, the scale of a living cell. Why observers should sit at the center rather than anywhere else is an open question, not something the framework derives.

### Manifold Index

Mode intensity dilutes as $`(\sqrt{\Omega})^{-n}`$. The manifold index $`n`$ specifies which scale governs the mode being sampled.

| $`n`$ | Manifold | $`\Omega`$ | $`(\sqrt{\Omega})^{-n}`$ | Observables |
|---|---|---|---|---|
| 0 | Planck floor | 1 | 1 | $`G`$ |
| 1 | Temporal edge $`S^1`$ | $`\Omega_H`$ (the rate ledger, not $`\Omega_\Psi`$) | $`10^{-61}`$ | $`H_0`$, $`a_0`$ |
| 2 | Möbius surface | $`\Omega_\Lambda`$ | $`10^{-122}`$ | $`\Lambda_\text{top}`$ |
| 3 | Space $`S^3`$ | $`\Omega_\Lambda`$ | $`10^{-183}`$ | space-sector density suppression; observable not yet assigned |

**The scale selection rule.** The index $`n`$ is read from where the quantity lives and whether it evolves with epoch: edge rates take $`n = 1`$ on the evolving $`\Omega_H`$, surface and space quantities take $`n = 2`$ and $`n = 3`$ on the fixed $`\Omega_\Lambda`$. Dimensionless couplings sit outside that index and use the separate grid-ladder exponents $`1/60`$ and $`1/120`$.

The index $`n`$ has two compatible readings in the dilution sector: the length-dimension of the observable, and the geometric layer on which the mode lives. They agree for the edge, surface, and space rows. Two things sit outside the table on purpose. The $`3/2`$ vacuum factor is not a manifold index at all; it is the separate Gauss/Ricci × de Sitter reference conversion described in One Interface. And the dimensionless couplings dilute at fractional powers that are grid-ladder exponents, not fractional manifold dimension.

Three constraints then narrow the observable assignments, though not all to a single answer. The manifold index separates edge modes ($`n = 1`$, epoch-dependent: $`H_0`$, $`a_0`$) from surface modes ($`n = 2`$, epoch-independent: $`\Lambda_\text{top}`$); the bosonic projection sends photon-mediated observables to the 60R-grid (even numerators survive $`2I \to I`$) and dynamical ones to the full 120; and $`\Lambda_\text{top}`$ sits at the antinode $`60/120`$ by eigenvalue identity. Under these, $`H_0 \to 34`$ is forced, the unique even-numerator edge well. The forcing is within the dictionary, not above it: it is exact once the photon-mediated-to-60R assignment above is granted, and that assignment is motivated rather than derived. The matter index 13 is singled arithmetically, the unique coprime well, and $`\alpha`$ and $`a_0`$ take its 60R and full-120 images; but the step from "coprime well" to "the dynamical-acceleration seat" is a diagnostic the corpus carries, not a derived rule. Wells 21 and 55 carry no observable.

### The Phase Field

The phase position decomposes as $`\Theta = \Theta_0 + \Theta_f`$, where $`\Theta_0`$ is the Fibonacci well, fixed by the recurrence above, and $`\Theta_f`$ is a local environmental shift. The decomposition is what makes a well's slope meaningful: $`C'(\Theta_0)`$ sets how sharply an observable answers to displacement. $`\Lambda_\text{top}`$ sits at the antinode where the derivative vanishes and is stationary to first order; $`H_0`$ sits on a moderate slope; $`a_0`$ sits on the steepest of the three.

What the engine takes from this is the decomposition and those slopes. The rest is application and is owned where it is tested: the finite-step arithmetic at each well, the 8.4% displacement that would carry $`67.4`$ to $`73.04`$ km/s/Mpc, the sublattice and orientation conditions it rests on, and the two tests that closed it are all on the Hubble tension page. The trigger that would have realized the shift is withdrawn: the pre-registered SPARC coherence test falsified the binary mechanism, and a separate exploratory check found the $`H_0`$ distribution unimodal rather than two-clustered. So the correspondence has no active mechanism, and a large derivative at $`a_0`$ produces a sensitive continuous response rather than a threshold.

>**📗 [Hubble Tension](../cosmos/files/hubble-tension.md):** $`H_0`$ as an edge mode and the 8.4% lattice step, with the sublattice conditions and the two tests that closed the mechanism.

The forward content that survives the null is the epoch relation $`a_0(z) \propto H(z)`$ and the sign-fixed $`(1+z)^1`$ term it ties to, carried in the [Research Frontier](#research-frontier)'s forward tests and registered on the Euclid card.

### The Assembled Engine

Evaluating the scaling law at each well:

| Observable | $`F_n`$ | Grid | $`\Theta`$ | $`C`$ | $`n`$ | $`A_P`$ | $`A/A_P`$ | Role |
|---|---|---|---|---|---|---|---|---|
| [α](../spectrum/files/fine-structure.md) | $`F_7`$ | 60R | 13/60 | 0.792 | 1/30 | 1 | $`7.33 \times 10^{-3}`$ | Λ-anchored comparison / α-route anchor |
| [a₀](../cosmos/files/early-galaxies.md) | $`F_7`$ | 120 | 13/120 | 0.223 | 1 | $`a_P`$ | $`2.2 \times 10^{-62}`$ | edge-ratio comparison |
| — | $`F_8`$ | 120 | 21/120 | 0.55 | — | — | — | unassigned |
| [H₀](../cosmos/files/hubble-tension.md) | $`F_9`$ | 60R | 34/120 | 1.208 | 1 | $`t_P^{-1}`$ | $`1.2 \times 10^{-61}`$ | calibration anchor |
| — | $`F_{10}`$ | 120 | 55/120 | 1.97 | — | — | — | unassigned |
| [Λ_top](../cosmos/files/cosmological-constant.md) | — | 60R | 60/120 | 2.00 | 2 | $`\ell_P^{-2}`$ | $`\approx 1.9 \times 10^{-122}`$ * | surface spectral seed |

> * The scaling law returns the surface spectral seed $`\Lambda_\text{top} = 2\,\Omega_\Lambda^{-1}\,\ell_P^{-2} = 2/R_\Lambda^2`$ ($`C = 2`$ at the antinode, $`n = 2`$), computed directly on the curved totally geodesic metric $`ds^2 = dy^2 + \cos^2(y/R_\Lambda)\,dw^2`$ and confirmed from below by the Bochner identity; equality is unique. The vacuum-reference value carries the lift $`\Lambda_\text{ref} = (3/2)\,\Lambda_\text{top} = 3/R_\Lambda^2 \approx 2.85 \times 10^{-122}\,\ell_P^{-2}`$, under three conditions: totally geodesic embedding of the underlying great-$`S^2`$ band ($`K_{ij} = 0`$), isotropy (CMB-verified to $`10^{-5}`$), and a de Sitter vacuum reference. That lift, and whether its coefficient is the physical constant of a static domain, is the stress-tensor question One Interface poses, so the number is a surface-sector calibration rather than an independent prediction. The first-eigenvalue paper establishes the geometric side, worked through on the cosmological constant page.

The Grid column is the readout class, the $`\Theta`$ column the coordinate. They differ because the well sequence is generated on the 120-step parent grid while the even numerators over 120 are exactly the points surviving $`2I \to I`$: $`34/120 = 17/60`$ and $`60/120 = 30/60`$ are 60R positions written in the parent coordinate. The odd-numerator wells, $`a_0`$ at 13/120 among them, have no 60R image and stay on the full resolution.

>**📗 [Cosmological Constant](../cosmos/files/cosmological-constant.md):** the surface spectral seed behind $`\Lambda`$, the full working of $`\Lambda_\text{top} = 2/R_\Lambda^2`$ and its $`3/2`$ lift.

**Calibration structure.** $`H_0`$ is the measured edge anchor: it defines the edge normalization $`N = H_0 t_P / C(34/120)`$, so the $`H_0`$ row fixes the ruler rather than testing the law against it, which is the calibration-versus-prediction split [Inputs and Calibration](#inputs-and-calibration) separates ledger by ledger. The other edge observables follow from $`N`$; the falsifiable content is any ratio of two edge-mode $`C`$ factors, in which $`N`$ cancels, the sharpest being $`a_0/(cH_0) = C(13/120)/C(34/120)`$. The $`\approx`$ in the scaling law marks the sector calibration, one anchor per sector.

$`\alpha`$ and $`a_0`$ share the Fibonacci index 13 but live on different grids, reference different scales ($`\Omega_\Lambda`$ vs $`\Omega_H`$), and carry different exponents. The shared index reflects Fibonacci stability operating at the topological level for both.

The $`a_0/(cH_0)`$ ratio is locked by well positions: $`C(13/120)/C(34/120) = 0.184`$. Because both are edge modes sharing the same calibrated normalization $`N`$, the ratio holds at every epoch: $`a_0(z) \propto H(z)`$.


[↑ Table of Contents](#table-of-contents)

---

<a id="one-identity"></a>
## 🔺 One Identity

*What tells one particle from another?*

```math
\Large {\lvert 2I\rvert = 120 = 2^3 \cdot 3 \cdot 5}
```

The order of the binary icosahedral group factors into exactly three primes, and the factorization is not bookkeeping. The stabilizer orders 2, 3, 5 belong to the edges, faces, and vertices of the icosahedral rotation group beneath it; in the binary lift the edge $`Z_2`$ becomes $`Z_4 \subset 2I`$, containing the central element $`-I`$. Restricting an irrep to each stabilizer gives a clean representation-theoretic decomposition, and MIT reads each decomposition as one axis of physical identity. The arithmetic is forced; the physical assignment is the reading.

### The particle address

A resolved particle address is the pair $`(\rho, \sigma)`$, with $`\rho`$ an irrep of $`2I`$, the representation seat, and $`\sigma`$ the flat-vacuum label [One Shape](#one-shape) closed at three. The propagating mode is read on $`\rho \otimes \sigma`$, and the three restrictions below are what give that address its physical content. [One Ladder](#one-ladder) and [One Formula](#one-formula) both consume it.

### Faces sort color

Restrict the propagating mode $`\rho \otimes \sigma`$ to the three-fold face stabilizer $`Z_3`$, and it decomposes into trivial characters and conjugate nontrivial character pairs. MIT reads the trivial channels as color singlets and the nontrivial pairs as color triplet and anti-triplet channels. The decomposition determines which color channels are available; the full $`(\rho, \sigma)`$ address determines which one a particle occupies. The face structure is vacuum-independent, so on this reading color is generation-independent.

### Edges sort spin

The four-fold edge stabilizer $`Z_4`$ contains the central element $`-I`$, which acts with opposite parity on integer- and half-integer-spin irreps. In the $`Z_4`$ restriction this becomes an exact binary: integer-spin irreps carry real $`Z_4`$ content and use the $`D = 60`$ grid, while half-integer irreps carry complex pairs and use $`D = 120`$. MIT reads that representation split as the boson-fermion, spin-statistics divide. This $`-I`$ is the central sign of $`2I`$, the same sign the scaling law's 60R and 120 grids are sorted by, and it is not the Möbius orientation sign of One Shape: two distinct $`Z_2`$'s, kept apart here as they are in the gauge ladder.

### Vertices set the electroweak address

The five-fold vertex decomposition makes the Galois distinction explicit: $`R_1`$ and $`R_2`$ occupy complementary fifth-root sectors exchanged by $`\sqrt5 \mapsto -\sqrt5`$, writing $`R_n`$ for the eight nontrivial irreps of $`2I`$ in their McKay ordering. MIT reads that distinction as the electroweak address, and it feeds the Coxeter-Galois gate: weak isospin $`T_3`$ is assigned by that gate from spectral parity, the sign the eta invariant carries on the irrep, together with the Galois structure, with a separate eta-sign gate constraining the electric-charge slot, so the isospin is the gate's output and not furnished by $`Z_5`$ alone. This is the same $`T_3`$ gate One Formula's mass table leans on, and it is the identification doing the most work in the section: representation theory distinguishes the pair, and the framework's dictionary gives the distinction its electroweak meaning.

The same stabilizers give two further entries that are not primes but corrections, each tying back to a section of its own.

| Combination | Value | Role | Mechanism |
|---|---|---|---|
| Face / base-edge stabilizer | 3/2 | gravity correspondence | ratio of the $`Z_3`$ face order to the base $`Z_2`$ edge order, matched to the vacuum-reference 3/2; the geometric conversion is derived separately in One Interface |
| Vertex $`\times`$ twist | $`\cos(\pi/10)`$ | weak coupling correction | the $`\pi/5`$ gluing twist of the shortest closed geodesic, a five-fold axis, whose spin lift has half-trace $`\cos(\pi/10)`$; its entry into the coupling is open |

The 3/2 entry is the conjectural one and is not this section's to adjudicate: it is the raw stabilizer ratio, and the fence separating it from the vacuum conversion and the clock exponent is kept in [One Interface](#one-interface), which owns the geometric derivation. The $`\cos(\pi/10)`$ entry is stated where it is used, in the gauge ladder: the number is a computed holonomy invariant, and its entry into the weak coupling is motivated, not derived. Its halving comes from the spin double cover, the same integer-versus-half-integer split the central $`-I`$ sorts, not from the Möbius orientation $`Z_2`$, which stays a distinct sign.

The stabilizers determine the decompositions and MIT's dictionary gives them their physical reading, all from the same topology. What leaves this section is what the rest of the page samples: the two grids, and the address $`(\rho, \sigma)`$ with its color, spin and electroweak content fixed. The observable law that reads them is already in hand; which entry lands on which measured fermion is decided later, by the masses rather than the topology.

[↑ Table of Contents](#table-of-contents)

---
<a id="one-ladder"></a>
## 🪜 One Ladder

*Where do the forces sit, and why is one rung empty?*

The same sampling engine resolves the coupling sector as a discrete ladder of phase positions and representation channels. Every ingredient it uses is already in hand: the two grids from [One Shape](#one-shape) and [One Identity](#one-identity), and the phase weight, the wells and the hierarchy from [One Equation](#one-equation).

### The Gauge Ladder

Everything in this sector lives at two phase slots, the Fibonacci well 13 and its $`E_8`$ Coxeter conjugate 17, the Coxeter complement $`30 - 13`$ rather than a Fibonacci well of its own. The Coxeter pair $`(13, 17)`$ sums to the Coxeter number of $`E_8`$: $`13 + 17 = 30 = h(E_8)`$. The McKay correspondence ties $`2I`$ directly to $`E_8`$, so the domain's natural arithmetic runs modulo 30, and 13 and 17 are the conjugate exponents that pair across it.

One coincidence belongs on the record here rather than left for a reader to find. The strong seat $`17/60`$ and the Hubble well $`34/120`$ are the same phase position, both giving $`C = 1.208`$, reached by two different routes: $`H_0`$ by the Fibonacci sequence forcing well 34 and projecting it through $`2I \to I`$, the strong coupling by the Coxeter complement $`30 - 13`$ taken directly on 60R. They stay distinguishable by everything except position: different sectors, different ledgers, different depths, $`n = 1`$ on the evolving $`\Omega_H`$ against the dimensionless $`\Omega_\Lambda^{-1/120}`$. Whether that is two derivations meeting as a consistency check or an identification that would cost the Coxeter pair its independence from the well sequence is not settled here, and no identification between the two seats is claimed. The weak seat at $`17/120`$ is a different point and is unaffected.

**The framework's assignments:**

| Well | Grid | Observable | What it represents |
|---|---|---|---|
| 13/60 | 60R | $`\alpha`$ | electromagnetic coupling; photon-mediated, bosonic |
| 13/120 | 120 | $`a_0`$ | matter acceleration scale; dynamical, full domain |
| 17/60 | 60R | strong coupling | bosonic carrier, confined fermions |
| 17/120 | 120 | weak coupling | fermion-changing carrier, flavor transitions |

**13 is where matter and electromagnetism anchor.** Of the two rows above it, the 60R version is what the photon sees and the 120 version is what matter dynamics sees; why one index carries both is [The Assembled Engine](#the-assembled-engine)'s.

**17 is where the short-range forces anchor.** Strong and weak both take 17 as their phase slot; the grid difference between them, identity-preserving versus fermion-changing action, is what separates confinement from flavor-changing transitions. Here the 120 grid labels the action on the full orientation-sensitive fermion domain, not the spin of the mediator: the $`W`$ and $`Z`$ remain spin-1 bosons, their 120 assignment coming from that action, a motivated selection rule rather than a derived one.

**Why the two resolutions are available.** The gauge ladder reuses the two grids defined in [The Sampling Grids](#the-sampling-grids) as a carrier/target dictionary: intensity-like roles take 60R, full wavefunction-like roles take 120. The Möbius orientation $`Z_2`$ is a separate structure, and the framework does not identify the two signs geometrically. So 13 connects to what propagates freely through the domain, and 17 to what binds or transforms within it.

The couplings then follow one assignment rule: the phase slot inherits the grid of the carrier, the exponent slot the grid of the confinement target.

| Force | Phase grid | Exponent grid | Formula | Framework value | Observed | Agreement |
|---|---|---|---|---|---|---|
| EM ($`\alpha`$) | 60R (bosonic carrier) | 60R (bosonic current) | $`C(13/60) \cdot \Omega_\Lambda^{-1/60}`$ | 0.00733 | 0.00730 | 0.4% |
| Strong ($`\alpha_s`$) | 60R (bosonic carrier) | 120 (confined fermions) | $`C(17/60) \cdot \Omega_\Lambda^{-1/120}`$ | 0.1162 | 0.1180 | 1.5% |
| Weak ($`\alpha_W`$) | 120 (fermion-changing action) | 120 (fermion transitions) | $`C(17/120) \cdot \Omega_\Lambda^{-1/120} \cdot \cos(\pi/10)`$ | 0.0339 | 0.0338 | 0.3% |
| Vacant 120/60 pairing (SUSY reading) | 120 (fermionic carrier) | 60R (bosonic target) | none: would change fermion/boson class | — | no superpartners | vacant (ladder rule) |

The $`\cos(\pi/10)`$ factor on the weak coupling is a motivated correction, not a derived one: the number occurs as the spin-lifted Levi-Civita holonomy around the shortest closed geodesic, and why the coupling carries it is open.

**Reference scale.** The displayed values compare $`\alpha`$ at low energy with $`\alpha_s`$ and $`\alpha_W`$ in their conventional $`Z`$-mass normalizations; run to the $`Z`$ mass, $`\alpha`$ itself is about 6% from the grid value. The grid returns base assignments; reconciling the reference scales, or deriving the running from the topology, remains open.

**Anchor discipline.** Under the $`\Lambda`$-anchored reading these percent-level agreements are conditional outputs of the selected ladder: with $`\Omega_\Lambda`$ fixed by a surface anchor, the three couplings are comparisons of the selected ladder, not independent forward predictions. When a coupling is instead the anchor that fixes $`\Omega_\Lambda`$ (the best-conditioned route, since $`\alpha`$ is the most precisely measured input), its own 0.4% becomes a consistency check rather than an independent prediction, and the genuine output of that route is $`\Lambda_\text{ref}`$ to 23% ($`\alpha \to \Omega_\Lambda \to \Lambda_\text{ref}`$). The alternative anchors are laid out under [Inputs and Calibration](#inputs-and-calibration).

**The Coxeter pair** $`(13, 17)`$ under $`h(E_8) = 30`$ is exceptional but not forced. Within the restricted conjugate-pair comparison, $`(13, 17)`$ stands alone: the three alternatives miss the coupling targets by 15% to 156% across the nine comparisons. The broad control is consistent with its local-density baseline, so it does not establish uniqueness. The restriction is therefore where the selection content lives. The three forces exhaust the grid ladder, monotone in fermionic content: there are only four ways to pair a carrier grid with a target grid, and the table shows three of them filled.

>**📗 [Fine Structure](../spectrum/files/fine-structure.md):** $`\alpha`$ as the first realized grid step of the hierarchy, with the Coxeter-pair $`(13,17)`$ selection scan in full.

### Supersymmetry

The vacant fourth rung has a SUSY reading. The one missing pairing would turn a fermion into a boson, exactly the move a superpartner symmetry asks for, and MIT reads the standard supersymmetric gaugino-scalar gauge sector as the natural occupant of that vacant pairing. Every real gauge rung acts within a statistics class: EM, strong, and weak change phase, charge, or representation but leave the fermion or boson character of what they act on intact. A superpartner rung would instead identify the fermionic 120-grid (the section $`\psi`$) with the bosonic 60R-grid (the intensity $`\lvert\psi\rvert^2`$), the split that the central element $`-I`$ carries, and no gauge rung crosses it. The obstruction is the ladder's own rule, not a spin-statistics prohibition (ordinary quantum field theory permits fermionic mediators), and not an attempted inverse of $`\psi \to \lvert\psi\rvert^2`$: that projection is well-defined but non-invertible, the measurement-level reason the two grids stay distinct. So within the grid-action reading the missing superpartner force is not an unreached energy scale but the empty fourth chair in a four-rung ladder: a conditional structural prediction of the ladder, not a spin-statistics theorem and not a claim that supersymmetry is impossible at every scale.

[↑ Table of Contents](#table-of-contents)

---

<a id="one-formula"></a>
## ⚛️ One Formula

*What fixes the masses, and where do three generations come from?*

The mass spectrum assembles in three moves, each set by the same topology: the curvature gap on the coexact gauge modes, the three flat vacua MIT reads as the generations, and the four-factor formula that ranks the fermions.

### The Gauge Gap

Confinement is usually told as a story about energy: the cost keeps climbing until the field snaps. What the topology supplies here is not that story but a curvature-induced gap on the coexact gauge modes, a structural ingredient on the confinement side of the mass construction rather than a derivation of the confinement scale. Positive Ricci curvature forces a positive gap on the coexact gauge fluctuations around a flat connection, and the twisted harmonic 1-forms vanish ($`H^1 = 0`$), so every mode is lifted off zero. The value is read from the coexact form spectrum through the McKay distance, the number of steps from an irrep to the trivial node on the affine $`E_8`$ McKay graph: the adjoint-valued gap is $`4/R_\Lambda^2`$ at the trivial and standard vacua, with the Galois vacuum the single exception below. It is a spectral gap on a compact curved background, fixed by curvature rather than tuned into the dynamics, and it is not the flat-space confinement scale $`\Lambda_\text{QCD}`$, which stays a separate open problem.

>**📗 [Yang-Mills](../spectrum/files/yang-mills.md):** the linearized gauge gap and the three flat vacua on $`S^3/2I`$, worked out in full.

### Three Generations

Why three, and not two or seven? Because the space has exactly three ways to hold a flat field still, with no path from one to another. Flat $`\text{SU}(2)`$ connections on $`S^3/2I`$ are classified by conjugacy classes of homomorphisms $`2I \to \text{SU}(2)`$, and exactly three exist: the trivial map, the standard connection $`Q`$, and its Galois conjugate $`Q'`$. Each is isolated ($`H^1 = 0`$), with no continuous moduli and no Goldstone mode bridging the families.

| Vacuum | Mass gap | Source |
|---|---|---|
| Trivial | $`4/R_\Lambda^2`$ | flat connection |
| Standard | $`4/R_\Lambda^2`$ | irreducible connection |
| Galois | $`36/R_\Lambda^2`$ ($`9\times`$) | Galois-conjugate connection |

The count of three flat vacua is forced; their identification with the three particle generations is MIT's reading, and the specific vacuum-to-generation mapping is open. Trivial and Standard sit together at the floor, while Galois clears it by a ninefold enhancement resting on two independent facts: $`2I`$'s perfectness, which keeps $`Q`$ and $`Q'`$ distinct under every twist so the Galois vacuum is a genuine third connection and not a decoration of the standard one, and the McKay distance, which sets the Galois adjoint at six against the standard adjoint's two, so the gap runs $`36/4 = (6/2)^2 = 9`$.

The coexact gap paper establishes the spectral side: across the whole ADE classification of finite subgroups of $`\text{SU}(2)`$ the adjoint coexact gap is uniformly $`4/R_\Lambda^2`$, with a single break, the Galois connection on $`S^3/2I`$ at $`36/R_\Lambda^2`$. MIT reads that exception as selection evidence, converging with the input-minimization argument that independently terminates on $`2I`$, so $`S^3/2I`$ is taken as the physical quotient on two grounds rather than one. The galois-pair paper supplies the boundary side, carrying the standard-versus-Galois asymmetry through the tautological bundles on the $`E_8`$ ALE filling of $`S^3/2I`$; it establishes that filling structure without yet identifying the gauge decoration with the standing-wave sector, so the Möbius-to-ALE bridge stays open.

>**📗 [Coexact Gap](files/bedrock/files/coexact-gap.md):** the adjoint coexact gap uniform at $`4/R_\Lambda^2`$ across the whole ADE classification, with the single Galois break to $`36/R_\Lambda^2`$ on $`S^3/2I`$.

### The Mass Formula

For the particle address $`(\rho, \sigma)`$ defined in [One Identity](#one-identity), the mass law reads left to right as one motion: start at the floor, choose a seat, ride the elevator, turn the dial.

```math
\Large m(\rho, \sigma) = \mu_\Lambda \cdot C_\text{geom}(\rho) \cdot (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)
```

It reads as one line, but like the scaling law its four factors do not stand at one strength, and they are worth keeping apart.

**The neutrino floor** $`\mu_\Lambda`$ is the mass sector's anchor, not an output of the formula: $`\mu_\Lambda = \rho_\Lambda^{1/4} \approx 2.25`$ meV, the fourth root of the vacuum energy density, the lowest energy the geometry can resolve and the scale every other mass is built up from.

**The Kostant sunflower** $`C_\text{geom}(\rho)`$ is the same phase weight $`C(\Theta)`$ the scaling law uses, read now as the geometric mean of $`C(e/D)`$ over the Kostant exponents of the irrep $`\rho`$: derived once and reused, not reintroduced. Each irrep takes its own seat on that discrete sunflower.

**The McKay elevator** $`(\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30}`$ raises the seat through orders of magnitude, one fixed factor per step along the McKay graph, with the denominator the Coxeter number $`h(E_8) = 30`$ of the same McKay geometry attached to $`2I`$. That exponent is reached by more than one convergent route but not yet from a single principle, so it is a structural rule the geometry carries rather than a closed derivation.

**The torsion dial** $`T^2(\rho \otimes \sigma)`$ is the fine adjustment within a shell, the one factor that changes across the three vacua, and the most exactly known of the four. Every irrep carries a closed form in $`\mathbb{Q}(\varphi)`$: the Galois-paired vacua satisfy $`T^2(R_3)/T^2(R_4) = \varphi^{-4}`$ and $`T^2(R_1)/T^2(R_2) = \varphi^{-8}`$, and the two spin-parity sector products, $`4`$ and $`1/4`$, are exact inverses.

**Two paths to the torsion.** The eight nontrivial values are computed within the framework analytically, from a Ray-Singer spectral-zeta combination. They have since been computed a second time from the based cellular chain complex of $`S^3/2I`$ and its twisted boundary maps, as a Reidemeister torsion. Both routes take the same topological input, the same space form and the same representation; what the second uses nowhere in its evaluation is spectral machinery, no eigenvalues, no zeta function, no heat kernel. Their equality is guaranteed in advance by the Cheeger-Müller theorem for acyclic unitary flat bundles, and what the second run covers is the closed forms themselves: all eight nontrivial values agree exactly in $`\mathbb{Q}(\varphi)`$, both Galois ratios follow, and both sector products follow as exact inverses, with the one free convention, the global direction of the torsion, fixed once at a single reference row ([the torsion algebra and its reproduction](files/working/files/torsion-correction.md)). The twenty-four products are built from those values downstream and were not part of that run, and two of them, the non-acyclic diagonal entries, sit outside the theorem's acyclic hypothesis and take a canonical integral-cohomology normalization instead.

What that buys is narrower than it first looks. With the model and invariant fixed, neither route has numerical freedom: the values are topological invariants of the supplied data, and the first computation was as bound to them as the second. What the second route certifies is the arithmetic, and that is a live risk rather than a formality. The analytic route was once run as a coexact-only truncation, and adding the scalar term revised twelve of the twenty-four products. A second evaluation sharing no spectral machinery turns an error of that kind from a silent one into a cross-method disagreement. The built-backward objection fenced elsewhere, at the wells sweep and at the postulate bridge's Tier 2, is therefore answered here for the computation, and stands unchanged at three places the reproduction does not reach: the choice of model, the entry rule that selects $`T^2`$ rather than $`T`$ and pairs it with the Kostant seat, and the assignment of entries to measured masses.

Applied to the eight nontrivial irreps across three vacua, the formula produces twenty-four entries across the fermion band. Lined up against the measured fermions, with $`m_e`$ taken as the benchmark rather than a counted hit, five of the remaining eight charged fermions land within a factor of three of a quantum-number-compatible entry, four of them surviving a sector-first adjudication. The dispositions are specific: the down quark is assigned but outside the factor-of-three window; the up quark is unassigned; charm is excluded by quantum numbers rather than distance, its nearest entries sitting on the Galois adjoint at weak isospin $`-1/2`$ where charm carries $`+1/2`$; the bottom quark's nearest compatible entry falls outside its own sector and stays uncounted; and the muon and strange share one entry at rank fifteen. That is a comparison, not a prediction, and it is helped by density: wherever the charged entries cluster, the factor-of-three window is wider than the gaps between them, so a measured mass sits near some entry largely by counting.

Whether the specific torsion values add fit beyond that quantum-number-constrained density was the open question, and a pre-registered null test, its design and seed fixed before the run ([`mass-null-v1.1`](files/working/files/mass-null-test.md)), has answered it. Reassigning the torsions at random across the fixed slots reproduced or exceeded the observed coverage in 69% of draws ($`p_A = 0.690`$), with the null distribution centered on the observed count: the factor-of-three scorecard is uninformative about whether the specific torsion values sit in the right slots. That removes the scorecard as evidence for the assignment. The table's evidential weight rests where it did: on the twenty-four-entry construction, the $`T_3`$ gate evaluations, the closed-form torsion algebra now reproduced, and the falsifiable outliers. The null tests where the values sit, not what they are for the specified topological data.

The correction also reopens one selection question the [Research Frontier](#research-frontier) carries: whether a parameter-free propagator correction tracks the residuals at high McKay distance, since the earlier elimination was computed on the pre-correction torsions and does not carry over.

The gauge gap above and this mass spectrum share the McKay structure and little else: the gap is proved, the spectrum is the comparison, and neither lends the other its standing.

>**📗 [Mass Spectrum](../spectrum/files/mass-spectrum.md):** fermion mass as positions on the McKay lattice, the four-factor formula and the maintained scorecard in full.

[↑ Table of Contents](#table-of-contents)

---
<a id="one-interface"></a>
## 🪡 One Interface

*What is gravity, and why does it not sit on the grid with the rest?*

All of it, the wells, the spectrum, the stabilizer sorting, lives on a smooth space that knows none of it. The last question is how that discrete structure sits on the $`S^3`$ underneath, and what gravity is across the seam. The answer is not one operation but two.

Underneath everything is $`S^3`$: smooth, continuous, every point equivalent, with uniform Ricci curvature. It knows nothing about 120. The discrete structure is built on top of it, in two distinct ways.

### The two seams

| Seam | Operation | Produces | Carries |
|---|---|---|---|
| Möbius $`\hookrightarrow S^3`$ | totally geodesic covering great-$`S^2`$ band; Möbius by edge identification | the vacuum spectral seed $`\Lambda_\text{top} = 2/R_\Lambda^2`$ | factor 3 from the isotropic Ricci trace, factor 1/2 from the de Sitter reference normalization |
| $`S^3 \to S^3/2I`$ | quotient (point identification) | the 120-label representation domain, McKay graph, and spectral sectors | the matter-side discrete dictionary |

These are different operations doing different jobs. The same division runs through the Waltz construction: the Möbius sector supplies the vacuum-side geometry, the $`2I`$ quotient the matter-side representation structure. The two seams are separate, and the one attempt to couple them, to make the Möbius standing-wave sector drive the $`2I`$ spectrum through an index-theoretic identity, is refuted on that route: the surface term cancels from the Galois difference. That construction fails; it does not establish universal independence. The equivariant-lift and restricted-connection channels remain untried, and the galois-pair filling carries the boundary asymmetry any such coupling would have to move.

>**📗 [Galois Pair](files/bedrock/files/galois-pair.md):** the $`E_8`$ ALE filling and the tautological charge, carrying the standard-versus-Galois boundary asymmetry.

The 3/2 belongs to the vacuum seam. It is the cost of converting the Möbius surface's curvature into the spatial curvature of $`S^3`$: the numerator 3 is the Gauss factor, derived geometry from the totally geodesic great-$`S^2`$ band, in an isotropic $`S^3`$; the denominator 2 is the de Sitter normalization, imported from general relativity. The cosmological constant page keeps that derived-versus-imported split explicit. The grid carries no such factor.

**The three 3/2's are fenced apart.** [One Identity](#one-identity)'s face-over-base-edge stabilizer ratio is 3/2, the vacuum conversion just derived is 3/2, and the clock carries a third, the registered interface tick $`d\mu_{\text{tick}} = S^{3/2}\,dt`$ [One Wave](#one-wave) names, the arithmetic midpoint of the amplitude and intensity measures. The [Manifold Index](#manifold-index) keeps the same 3/2 out of its dilution column. The tempting move is to let one face-over-edge ratio be the vacuum conversion and then, by arithmetic, the clock's half-power; but numerical equality is not a mechanism, and the framework does not merge the three until an operator-level bridge from stabilizer order to clock exponent is derived.

### Gravity is what crosses

Gravity belongs to the interface. The grid carries particle identity; the smooth substrate carries geometry. Gravity is therefore not a vacant grid position and not a fourth gauge force waiting for its rung: MIT reads it as the conversion between the two descriptions, the one interaction that translates between the smooth substrate and every discrete structuring of it. On the grid seam it pays nothing special, only the ordinary stress-energy coupling at $`8\pi G`$. Einstein's field equations themselves stay unchanged; what remains open is their placement. They may source the static domain from its mode content, or govern the effective metric the distance dictionary runs on; the coefficient constraint two paragraphs below constrains the first placement, and the projection requirement the stress-tensor bridge states constrains the second. The present distance construction uses the effective-metric placement; deriving or rejecting that placement from the mode content is part of the bridge. On the vacuum seam the conversion carries the geometric 3/2 relation, reading the surface eigenvalue $`\Lambda_\text{top} = 2/R_\Lambda^2`$ up to the reference value $`\Lambda_\text{ref} = 3/R_\Lambda^2`$.

The remaining problem is the source, and it is already sharply posed. No map from the realized wave variables to $`g_\text{eff}`$ or $`T_\text{eff}`$, and no action generating one, has yet been derived; the stress-tensor bridge is the program that would build it, and it meets there the same two-part metric-definition problem the cosmological side runs into, spatial-curvature placement and the vacuum dressing of the clock. The coefficient itself is at stake on the static-source branch: there a homogeneous perfect fluid gives $`\Lambda R_\Lambda^2 = 3`$ only in the pure-pressure limit $`\rho = 0`$, which violates the dominant energy condition, so either the domain's content lies outside that class or the coefficient moves off 3. The effective-metric placement remains the alternative. The 3/2 is thus a vacuum-reference reading whose physical realization waits on that source, not a settled field equation.

>**📒 [The Stress-Tensor Bridge](files/working/files/stress-tensor-bridge.md):** the program for the ledger's $`E(S)`$, the missing map from the realized budget to a stress tensor with a declared metric placement.

Within MIT, this interface structure is why gravity is not assigned another gauge quantum on the 120-domain. The two sides source different things: $`\Lambda_\text{top}`$ is the first positive eigenvalue of a smooth constant-curvature surface, so discretizing the substrate would remove what sources it, while the spectrum, the mass gap, and the three vacua come from the finite quotient, so continualizing the 120-domain would remove what sources them. A quantum completion of gravity has to keep both, and MIT does not yet supply one that does. The claim is about this construction, not a general no-go: it says what closing this interface requires, not that no quantization can.

>**📗 [The Waltz](../spectrum/files/the-waltz.md):** the gravity between surface and space, the Möbius vacuum sector and the $`2I`$ matter sector as one construction.

[↑ Table of Contents](#table-of-contents)

---
<a id="inputs-and-calibration"></a>
## 🎛️ Inputs and Calibration

*What is measured, and what follows from it?*

The scaling law uses one hierarchy ledger at a time: $`\Omega_H`$ on the temporal edge, $`\Omega_\Lambda`$ in the surface and space sectors. Each sector needs one absolute anchor, and the relations that survive between anchors are the physics. Invert one observable to fix that sector's $`\Omega`$ and the rest of the sector follows; which observable you invert is calibration. This section separates the two, ledger by ledger.

### The Ω ledger

The symbol $`\Omega`$ is a hierarchy ledger, not by itself a prediction: its status depends on the sector row.

| Sector | Hierarchy | How $`\Omega`$ is fixed | What is tested |
|---|---|---|---|
| Edge | $`\Omega_H = (c/H_0\ell_P)^2 = (H_0 t_P)^{-2}`$ | read from measured $`H_0`$ | the well ratio $`a_0/(cH_0) = C(13/120)/C(34/120)`$ |
| Surface, space | $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$ | one surface anchor: measured $`\Lambda`$, or read from $`\alpha`$ or the mass spectrum | cross-read consistency, and the downstream mass and coupling structure |
| Couplings | powers $`\Omega_\Lambda^{-1/60}`$, $`\Omega_\Lambda^{-1/120}`$ | inherited from the surface hierarchy | grid relations and same-depth ratios |
| Masses | powers $`(\sqrt{\Omega_\Lambda})^{\text{dist}/30}`$ | inherited from the surface hierarchy, plus one mass-sector normalization | McKay distances and ratios |

At an anchor row, substituting that row's own definition of $`\Omega`$ back into the scaling law returns the anchor identity: calibration, not prediction. The content is in reading the same $`\Omega`$ ledger at different wells, depths, and sectors. In the edge sector $`\Omega_H = (H_0 t_P)^{-2}`$ is read from measured $`H_0`$, fixing the edge reference at the $`34/120`$ row, and the anchor-independent comparison is the acceleration ratio $`a_0/(cH_0) = C(13/120)/C(34/120) = 0.184`$.

### Unit constants

| Constant | Value | Role |
|---|---|---|
| $`c`$ | 299,792,458 m/s | propagation rate on the temporal boundary |
| $`\hbar`$ | $`1.055 \times 10^{-34}`$ J s | converts dimensionless mode structure into physical action and energy |
| $`G`$ | $`6.67430 \times 10^{-11}`$ m³ kg⁻¹ s⁻² | measured gravitational coupling; with $`c`$ and $`\hbar`$ it sets the Planck units |

None is predicted by MIT. $`c`$ and $`\hbar`$ are exact in the SI definition; $`G`$ remains measured. Together they define the Planck references the framework builds on.

### The dimensionless core

In a ratio of two observables at the same depth, $`\Omega_\Lambda`$ cancels: no anchor enters and the number is parameter-free. These hold under every choice of anchor below; cross-depth or cross-grid comparisons are the levers that read the hierarchy.

| Quantity | Value | Status |
|---|---|---|
| flat-vacuum count | 3 | exact; the generation identification is the reading |
| force count | 3 | the count is structural; identifying the rungs with EM, strong, and weak is the reading |
| $`T_3`$ gate evaluations | 11 featured (5 assigned + 2 neutrino-proxy + 4 structural) | exact given One Identity's Coxeter-Galois gate; agreement with the Standard Model assignments is a comparison |
| Galois torsion ratios | $`\varphi^{-4}`$, $`\varphi^{-8}`$ | exact ($`T^2(R_3)/T^2(R_4)`$, $`T^2(R_1)/T^2(R_2)`$); the closed forms reproduced by an independent combinatorial route, which certifies the arithmetic and not the assignment |
| torsion sector products | $`4`$, $`1/4`$ | exact inverses |
| $`\alpha_s/\alpha_W`$ | 3.43 | comparison (1.8%), $`\Omega`$ cancels |
| $`a_0/(cH_0)`$ | 0.184 | comparison (<1%), normalization cancels |

### Three readings of one hierarchy

To attach a scale you invert one observable for $`\Omega_\Lambda`$. Three are independent, so $`\Omega_\Lambda`$ is over-determined, and whether the three readings agree is then a real test rather than a bookkeeping check. They do not land the same scale.

| Anchor | Determines | $`\Lambda_\text{ref}`$ | $`\alpha`$ | Role |
|---|---|---|---|---|
| measured $`\Lambda`$, under $`\Lambda_\text{ref} = 3/R_\Lambda^2`$ | $`\Omega_\Lambda`$ from $`R_\Lambda`$ | circular | 0.4% | current default |
| measured $`\alpha`$ | $`\Omega_\Lambda`$ from the coupling | 23% | circular | best-conditioned |
| mass spectrum ($`m_\mu/m_e`$) | $`\Omega_\Lambda`$ from the mass ratio | ~13.4× off | ~few % | independent cross-check |

**The named anchor.** For the $`\Lambda`$-anchored default this repository uses Planck 2018 base-ΛCDM, TT,TE,EE+lowE+lensing: $`H_0 = 67.36`$ km s⁻¹ Mpc⁻¹ and the vacuum density fraction $`f_\Lambda = 0.6847`$ (notation), giving $`\Lambda\,\ell_P^2 = 2.845 \times 10^{-122}`$, hence $`\Omega_\Lambda = 1.054 \times 10^{122}`$ and $`R_\Lambda = 5.38`$ Gpc. Working prose rounds that row to $`H_0 = 67.4`$ and $`0.685`$, which returns the same $`2.85 \times 10^{-122}`$ to three figures. That agreement is specific to $`\Lambda`$, which rounds to $`2.85`$ from either pair. $`R_\Lambda`$ does not: the two straddle a boundary at 5.375 Gpc (5.3787 named against 5.3740 working), so a radius derived from the rounded pair would print 5.37. Everything absolute in the corpus derives from this named row, $`R_\Lambda = 5.38`$ Gpc included; other Planck combinations, +BAO in particular, are comparison datasets and not silent replacements for the anchor. One documented exception is the published mass ladder: its pinned inputs, $`\mu_\Lambda = 2.25`$ meV and $`\sqrt{\Omega_\Lambda} = 1.019 \times 10^{61}`$, encode the Planck 2018 +BAO row rather than the named row, which would print about $`2.24`$ meV and $`1.027 \times 10^{61}`$. Those two are mutually derivable and pinned to the table they generated, so retargeting either alone corrupts that table rather than updating it; the split is recorded in the mass spectrum's calibration note and enforced by its regression guard.

>**📒 [Calibration Structure](files/working/files/calibration-structure.md):** the engine reframed as one measured anchor per sector, localizing the R problem to a single demotion.

The $`\alpha`$ route is the cleanest non-circular inversion. From one measured coupling, with no $`R_\Lambda`$ and no further calibration, the non-circular chain is $`\alpha \to R_\Lambda \to \Lambda_\text{ref} = 3/R_\Lambda^2`$, landing the observed cosmological value to about 23%; whether that reference coefficient is the static domain's physical $`\Lambda`$ is the Interface question, not a calibration result. The 0.4% match on $`\alpha`$ itself is a closure test, not a prediction, because $`\alpha`$ is also what calibrates $`R_\Lambda`$ on this route: input and output on one line, the reading the gauge ladder's note already states. The 122 orders of magnitude are not predicted here; they enter through $`\Omega_\Lambda`$, read from $`\alpha`$.

The mass route misses, and the disagreement is the framework's largest internal tension. All three routes read $`\Omega_\Lambda`$ through the same steep 60-fold lever ($`\Lambda_\text{ref}\ell_P^2 \propto \alpha^{60}`$): against the measured $`R_\Lambda \approx 5.4`$ Gpc the mass-spectrum route puts the master length at $`\approx 20`$ Gpc, about a factor of 3.7, and the ~13.4× miss in $`\Lambda_\text{ref}`$ the table above records. Sharper still is the disagreement between the two non-circular readings themselves: the coupling route gives $`R_\Lambda \approx 6.1`$ Gpc against the mass route's $`\approx 20`$, a factor of 3.2 in $`R_\Lambda`$ and 10.5 in $`\Lambda_\text{ref}`$. The 60-fold inversion amplifies small input residuals, but that amplification does not by itself explain the disagreement; the present machinery does not distinguish conditioning from structural inconsistency. Until one route is established as the correct determination of $`R_\Lambda`$, every absolute prediction flowing through it inherits the ambiguity. Reconciling the two is open.

>**📒 [The R Problem](files/working/files/r-problem.md):** every route to an independent curvature radius $`R_\Lambda`$ and where each stands, the tracker behind the calibration tension.

The mass route is an independent cross-check because the electron and muon sit at different McKay distances: a same-depth ratio would cancel $`R_\Lambda`$, but theirs keeps a net power of $`\sqrt{\Omega_\Lambda}`$ through the elevator and reads the scale rather than dividing it out.

### Sector anchors

| Sector | Anchor | Role |
|---|---|---|
| Edge | measured $`H_0`$ | fixes the present edge hierarchy $`\Omega_H = (c/H_0\ell_P)^2`$ |
| Surface / space | any one of $`\Lambda`$, $`\alpha`$, or the mass ratio | fixes $`\Omega_\Lambda`$; the three do not yet agree, above |
| Mass | normalization tied to $`m_e = 0.511`$ MeV | fixes the absolute mass scale once ratios are known |
| Phase clock | $`s_0`$ from distance data | locates the current observer phase |

Edge observables reference the evolving $`\Omega_H(z)`$; surface and space observables reference the fixed $`\Omega_\Lambda`$. The mass sector inherits $`\mu_\Lambda = \rho_\Lambda^{1/4}`$ from $`\Omega_\Lambda`$, with $`m_e`$ the benchmark rather than a second floor. Compute $`m_e`$ from $`\Lambda`$ instead, carrying both the $`\mu_\Lambda`$ scale and the hierarchy feedback ($`m_e \propto \Lambda^{11/60}`$), and it lands within 2%; inverting, that 2% is about 11% in $`\Lambda`$. The closure is one loop run from either end, the web holding whichever quantity you pick as the input.

One number the distance fit uses is not an input at all: the matter fraction $`\Omega_m = 0.315`$, a density fraction rather than one of the hierarchy ledgers above, is the flat-closure complement $`1 - f_\Lambda`$ of the vacuum fraction and is not read off the fit.

### Predicted and calibrated

| Quantity | Status |
|---|---|
| dimensionless ratios ($`a_0/cH_0`$, $`\alpha_s/\alpha_W`$) | anchor-independent once the well and grid assignments are granted, and only where the two share an exponent grid: $`\alpha_s/\alpha`$ keeps $`\Omega_\Lambda^{1/120}`$ because 13 and 17 sit at different depths |
| counts and $`T_3`$ evaluations | exact given the group structure and the Coxeter-Galois gate |
| $`\Omega_\Lambda`$ | over-determined by three readings that do not yet agree |
| $`\Lambda_\text{ref}`$ (absolute) | conditional output of the $`\alpha`$ reading (23%) or the mass reading (~13.4× off); circular from the $`\Lambda`$ reading; its identification with the physical $`\Lambda`$ is the Interface question |
| $`\alpha`$, $`\alpha_s`$, $`\alpha_W`$ (absolute) | $`\Lambda`$-anchored conditional comparisons (0.4% for $`\alpha`$); the anchor when $`\alpha`$ is the input |
| first positive eigenvalue $`2/R_\Lambda^2`$ | surface spectral result |
| torsion mass-ratio structure | exact torsion ratios; the map to measured fermion mass ratios is the mass comparison, read against data |
| absolute fermion masses | set by the $`m_e`$ benchmark |
| three flat vacua and the Yang-Mills gap | structural results on $`S^3/2I`$; the generation identification is the reading |

[↑ Table of Contents](#table-of-contents)

---
<a id="research-frontier"></a>
## 🌅 Research Frontier

*What is still open, and what would settle it?*

The body is the theory as it stands; this is the theory as a program. The largest open items are not scattered: three problems carry what the framework has spent and most of what it still bets. They are not the whole debt. Smaller opens stay in their home sections and are named there, among them $`\Lambda_\text{QCD}`$, the running of the couplings, the Möbius-to-ALE bridge, and the step that carries the $`\cos(\pi/10)`$ correction into the weak coupling. The full apparatus, the controls, and the dates live in the claim ledger and the [working register](files/working/README.md); the Frontier names the three problems and points to where each already lives.

>**📒 [Claim Ledger](files/working/files/claim-ledger.md):** the skeptical audit of every quantitative claim, the eight-cycle calibration web, and the two live internal tensions.

### The three problems

**Dynamics: how does the wave content source geometry?** Not yet by any derived map. The gap is one object accounting for two symptoms that read as separate problems: gravity's open construction in [One Interface](#one-interface) and the clock exponent in [One Wave](#one-wave), and until it is built the two placements the coefficient constraint leaves open stay undecided. [One Interface](#one-interface) poses the problem; the stress-tensor bridge is the program that would close it. This is the framework's largest structural debt: several pages are waiting on one bridge.

**Selection: why these sectors and not others?** Topology fixes the family; Selection must fix the realized member. The scaling law's factored form still awaits the commutant theorem $`\mathcal{A}_\text{obs} = \mathcal{A}_\Theta \otimes \mathcal{A}_\text{spec}`$ that One Equation names as its keystone; the Fibonacci wells continue a recurrence with no derived sampling rule; the McKay elevator's $`\text{dist}/30`$ has no single-principle derivation, and the propagator route One Formula reopened is still to run; and the vacuum-to-generation assignment, the charm slot with no home, and the neutrino placements are the same question in the mass sector. The domain itself sits here too: terminality and perfectness both point at $`2I`$, but the single theorem folding them into one proof is One Shape's open problem.

**Calibration closure: do the independent scale-fixings agree?** No, and this is the framework's largest internal tension. Three anchors fix the surface hierarchy and two of them are non-circular, so their disagreement is a real result rather than a bookkeeping check; until one is established as the correct determination of $`R_\Lambda`$, every absolute scale flowing through it inherits the ambiguity. [Inputs and Calibration](#inputs-and-calibration) carries the three readings, the numbers and the conditioning question.

>**📒 [Energy as Resolution Amplitude](files/working/files/energy-as-resolution-amplitude.md):** energy read as the standing-wave resolution amplitude, a working note toward the stress-energy accounting.

>**📒 [Entropy as Realization Budget](files/working/files/entropy-as-realization-budget.md):** entropy as the count of realized modes, tied to the Molien shell-unlock map that sets the accessible mode count.

### Recorded nulls

The framework spent these to find where the three problems actually sit, and each is a result rather than a gap. A coherence trigger for the $`H_0`$ shift was pre-registered and falsified on SPARC rotation curves, and a separate check found the $`H_0`$ distribution unimodal where a discrete shift would have split it. A variational origin for the wells was searched across eight boundary-mode functionals and never returned them. The torsion null test ($`p_A = 0.690`$) removed the factor-of-three proximity count as evidence for the torsion dial. The index-theoretic route from the Möbius sector to the $`2I`$ quotient was run and refuted on its own terms, the surface contribution cancelling from the Galois difference, which is the negative behind [One Interface](#one-interface)'s account of what the two seams do not share. And the original McKay-propagator search returned no parameter-free correction on the pre-correction mass table, a negative the corrected torsions have since reopened rather than confirmed. Each is recorded once in its home section and consolidated, with the rest, in the claim ledger; together they are the credibility core, the places the theory has already told itself no.

### Forward tests

The exams are thin by design. The phase-clock relation is read through correlated channels rather than counted as separate bets: the epoch relation $`a_0(z) \propto H(z)`$ and the sign-fixed $`(1+z)^1`$ term of the phase-clock $`H^2(z)`$ are two faces of it, the second an identity of the construction rather than a fitted amplitude. Alongside them sit a vacuum-sector test, a flat dark-energy history $`\Omega_\text{DE}(z)`$, and a high-redshift galaxy-abundance test riding on the $`a_0(z)`$ enhancement. Euclid DR1 is the next registered observational gate, with the channels, thresholds, and falsification conditions on the pre-registration card; the release date lives there, not on this page. Because the clock channels are one relation, a single release can take them down together, which is the point of setting them that way.

>**📗 [CMB Anomalies](../cosmos/files/cmb-anomalies.md):** the low-ℓ suppression read as the Molien shell gap, a standing CMB signature with parity and alignment still open.

>**📗 [Early Galaxies](../cosmos/files/early-galaxies.md):** early massive galaxies in a static geometry, the high-redshift abundance test riding on the $`a_0(z)`$ enhancement.

>**📗 [Euclid DR1 Showdown](../cosmos/files/euclid-dr1.md):** the pre-registration card, the next registered observational gate and the framework's falsification test.

[↑ Table of Contents](#table-of-contents)

---

>[![Resonant Universe](https://img.youtube.com/vi/I3AOKh-RRTA/mqdefault.jpg)](https://www.youtube.com/watch?v=I3AOKh-RRTA)
>
>*Audio Podcast: [Resonant Universe](https://www.youtube.com/watch?v=I3AOKh-RRTA)*

*Topology holds. Wave is. Particle samples.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
