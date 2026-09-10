<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🪜 Fine Structure

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/alpha%20banner.png?raw=true" width="100%" alt="Fine Structure">

The fine structure constant $`\alpha \approx 1/137`$ governs the strength of electromagnetic interaction. It is dimensionless: a pure number carrying no Planck units. The Standard Model takes its value as an input. Within Mode Identity Theory, the topological hierarchy behind Λ, $`H_0`$, and $`a_0`$ also governs dimensionless couplings. The result is $`\alpha = C(13/60) \cdot \Omega_\Lambda^{-1/60} = 0.00733`$, within 0.4% of the measured value, once the boundary hierarchy $`\Omega_\Lambda`$ is anchored. When $`\alpha`$ is instead what anchors $`\Omega_\Lambda`$, that 0.4% becomes a closure check and the downstream output is $`\Lambda_\text{ref}`$ (§V). The same structure extends to the strong and weak couplings.

**Results at a glance**

| Coupling | Framework value | Observed | Agreement |
|---|---|---|---|
| $`\alpha`$ | 0.00733 | 0.00730 | 0.4% |
| $`\alpha_s`$ | 0.1162 | 0.1180 | 1.5% |
| $`\alpha_W`$ | 0.0339 | 0.0338 | 0.3% |
| $`\alpha_s / \alpha_W`$ | 3.426 | 3.490 | 1.8% (pure geometry, no $`\Omega_\Lambda`$) |

## I. The Problem

Within MIT, dimensional observables scale from Planck references via the scaling law $`A/A_P = C(\Theta) \cdot (\sqrt{\Omega})^{-n}`$. Edge modes such as $`H_0`$ and $`a_0`$ reference the evolving hierarchy $`\Omega_H(z)`$, while surface/space modes reference the fixed boundary hierarchy $`\Omega_\Lambda = (R_\Lambda / \ell_P)^2 \approx 10^{122}`$. 

$`n = 1, 2, 3`$ counts manifold embedding depth. Each integer depth contributes one power of its own sector's hierarchy: edge rates take $`\sqrt{\Omega_H}`$, while surface and space quantities take $`\sqrt{\Omega_\Lambda} \approx 10^{61}`$. Depth one, the edge, gives $`H_0`$ and $`a_0`$; depth two, the surface, gives $`\Lambda_\text{top}`$; depth three, space, gives the space-sector suppression, whose observable is not yet assigned. Dimensionless couplings carry no Planck units, so manifold floors do not apply. They access the same hierarchy $`\Omega_\Lambda`$ at a different resolution: grid steps rather than manifold depth.

$`\alpha`$ couples matter (edge, $`n = 1`$) to geometry (surface, $`n = 2`$) through the photon, a boson. In the formal Planck-floor limit, the coupling becomes order unity; in the present low-energy universe, the fixed boundary hierarchy suppresses it. How it is suppressed, and by how much, is what the rest of this page constructs: which well, which grid, and which fractional power of $`\Omega_\Lambda`$.

## II. Three Ingredients

### The matter well

The well at 13/120 governs matter dynamics: it is the Fibonacci well ($`F_7 = 13`$) assigned to the MOND acceleration scale $`a_0`$. It satisfies $`\gcd(13, 120) = 1`$, making 13 the unique coprime well. That arithmetic singles out 13; its identification as the matter and acceleration seat is a diagnostic the corpus carries, not a derived selection rule.

### The bosonic grid

Photons are bosons, and the framework reads the coupling $`\alpha = g^2/4\pi`$ as an intensity-like quantity rather than a spinor amplitude. Observable intensities $`\lvert\psi\rvert^2`$ have period 1, placing them on the 60-position bosonic grid ($`\lvert I \rvert = 60`$) rather than the 120-position spinor grid ($`\lvert 2I \rvert = 120`$) where the wavefunction $`\psi`$ lives with anti-period 1.

The well label (13) stays the same. The grid denominator changes: $`120 \to 60`$. The phase operator evaluates differently at the two resolutions:

| Grid | Position | Physics |
|---|---|---|
| 60R (bosonic) | 13/60 | Matter coupling ($`\alpha`$) |
| 120 (spinor) | 13/120 | Matter dynamics ($`a_0`$) |

### The fractional exponent

For dimensional observables, $`n = 1, 2, 3`$ counts whole manifold embeddings. Edge rates suppress by $`\sqrt{\Omega_H}`$; surface and space quantities suppress by $`\sqrt{\Omega_\Lambda}`$. Dimensional observables count whole floors because they carry Planck dimensions (powers of $`\ell_P`$, $`t_P`$) requiring whole-manifold dilution. Dimensionless couplings carry no Planck dimensions; they resolve at the grid level. 

The bosonic grid has 60 positions, so the minimum resolved step is $`1/60 = 1/\lvert I \rvert`$, and one grid step of the hierarchy gives $`\Omega_\Lambda^{-1/60}`$. The exponent is motivated by two convergent paths (McKay packetization, dimensionless dilution rule). The McKay mass spectrum independently repeats the same $`\text{dist}/30`$ hierarchy; its within-factor-3 match rate for the charged fermions is not significant under the registered null ($`p_A = 0.690`$, $`m_e`$ the benchmark), so the companion supports the recurrence of the hierarchy, not an empirical hit rate.

## III. The formula

The scaling law for a dimensionless coupling ($`A_P = 1`$) is:

```math
\alpha = C(\Theta) \cdot \Omega_\Lambda^{-1/60}
```

with $`\Theta = 13/60`$ (matter well on bosonic grid) and $`\Omega_\Lambda = (R_\Lambda / \ell_P)^2 = 1.054 \times 10^{122}`$, fixed from the Planck 2018 Λ inference.

**Phase factor.** The phase operator $`C(\Theta) = 2\sin^2(\pi\Theta)`$ evaluated at $`\Theta = 13/60`$:

```math
C(13/60) = 2\sin^2\left(\pi \cdot \frac{13}{60}\right) = 2 \times (0.6293)^2 = 0.7921
```

**Hierarchy suppression.** One grid step of the vacuum hierarchy:

```math
\Omega_\Lambda^{-1/60} = \left(1.054 \times 10^{122}\right)^{-1/60} = 0.009253
```

**Product:**

```math
\alpha = 0.7921 \times 0.009253 = 0.007329
```

Observed: $`\alpha = 0.007297`$. Agreement: 0.4%.

At the Planck floor ($`\Omega_\Lambda \to 1`$), the suppression vanishes and $`\alpha \to C(13/60) = 0.792`$: order unity, as expected for a coupling at the scale where the hierarchy collapses.

### The derivation chain

These three ingredients (matter well, bosonic grid, fractional exponent) map onto the following chain from topology to output:

| # | Input | Output | Status |
|---|---|---|---|
| 1 | $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3,\ \partial S^3 = \emptyset`$ | Anti-periodic BC | Derived |
| 2 | $`F_7 = 13`$, $`\gcd(13, 120) = 1`$; EM couples matter | Matter well 13 | Motivated |
| 3 | $`\lvert\psi\rvert^2`$ (bosonic) | 60R-grid; $`\Theta = 13/60`$ | Motivated grid assignment |
| 4 | $`\alpha`$ epoch-independent | Reference $`\Omega_\Lambda`$ | Framework selection rule |
| 5 | Minimum grid step: $`1/\lvert I \rvert = 1/60`$ | $`\Omega_\Lambda^{-1/60}`$ | Provisional |
| 6 | $`C(13/60) \times \Omega_\Lambda^{-1/60}`$ | $`\alpha = 0.00733`$ | Output |

One derivation, two motivated assignments, one framework selection rule, one provisional structural step, one arithmetic output. The grid-hierarchy exponent (stage 5) is supported by two convergent arguments (McKay packetization, dimensionless dilution rule); the restricted scan in Section IV checks its identifiability within the framework's own rule set.

## IV. Identifiability

Accuracy alone cannot distinguish the formula from numerology. A scan of all combinations $`C(\Theta) \times \Omega_\Lambda^{-1/d}`$ across grid positions and candidate denominators tests whether the MIT formula is structurally selected or merely lucky.

| Scan | Combinations | Hits < 0.5% | Local-density baseline |
|---|---|---|---|
| Broad (half-domain positions × all denominators) | 7,200 | 9 | ~7.6 |
| Restricted (MIT constraints only) | 24 | 1 | — |

The broad control runs the non-redundant half-domain, $`\Theta = k/120`$ for $`k = 1 \ldots 60`$, against exponent denominators $`d = 1 \ldots 120`$; positions above the antinode are omitted because $`C(\Theta) = C(1 - \Theta)`$ makes them mirrors carrying no new value. The restricted class is the formula's own three choice slots, the four realized wells across both grids at the three admitted group depths. Both enumerations and every count in the table are reproduced by [alpha-scan.test.py](../../framework/files/working/files/scripts/alpha-scan.test.py).

In the broad scan, the hit count is consistent with the baseline: the local-density estimate gives about 7.6 hits and 9 are found. Accuracy alone selects nothing. In the restricted scan (MIT structural constraints only), the formula is uniquely selected: of 24 candidates, exactly one lands within 0.5% of $`\alpha`$, the matter well at the minimum realized step. That is identifiability within the framework's own rule set: the constraints, taken together, pick the formula out uniquely.

### The best competitor

The most accurate alternative is $`C(34/120) \times \Omega_\Lambda^{-1/55}`$, achieving 0.06% error (seven times better than MIT). In the unreduced 120-grid notation used by the broad scan, its structural comparison with the MIT formula is:

| Test | MIT formula | Competitor |
|---|---|---|
| Grid type | Bosonic (60R): photon is boson | Spinor (120): violates the bosonic-grid assignment |
| Well | 13 (matter / $`a_0`$): EM couples matter | 34 ($`H_0`$): phase clock, not coupling |
| Exponent denominator | $`60 = \lvert I \rvert`$ (group order) | $`55 = F_{10}`$ (Fibonacci, not group) |

Because $`34/120 = 17/60`$, the first two rows depend partly on how the same phase point is represented. On the reduced 60R-grid, the competitor uses the coprime Kostant seat 17: it satisfies the bosonic-grid condition, but it still fails the electromagnetic matter-seat assignment (13), and its denominator $`d = 55`$ is not one of the admitted group depths $`\{30, 60, 120\}`$. At $`d = 60`$, the corresponding restricted candidate gives $`C(17/60) \cdot \Omega_\Lambda^{-1/60} = 0.0112`$, a 53% miss. The runner-up is the conjugate seat off its menu: it reaches α only by leaving the rule set.

### Structural checklist

Only the MIT formula passes all five constraints. The exponent denominator carries two readings of one condition ($`1/\lvert I \rvert = 1/60 = 1/2h(E_8)`$: group order and Coxeter depth), counted once:

| # | Constraint | Rationale |
|---|---|---|
| 1 | Bosonic grid ($`60 = \lvert I \rvert`$) | Photons are bosons |
| 2 | Matter well ($`F_7 = 13`$) | EM couples matter |
| 3 | Coprime: $`\gcd(13, 60) = 1`$ | Unique coprime realized well |
| 4 | Group-depth exponent: $`1/\lvert I \rvert = 1/2h(E_8)`$ | Icosahedral order; equivalently Coxeter depth of $`E_8`$ |
| 5 | Epoch-independent: $`\Omega_\Lambda`$ | $`\alpha`$ is constant |

Accuracy alone is inconclusive. Within the restricted rule set, structure selects the MIT formula uniquely.

## V. The Gauge Ladder

The $`\alpha`$ derivation uses two structural choices: a phase well (which Kostant exponent) and a grid resolution (60R or 120). For the electromagnetic coupling, both slots are bosonic. A single principle extends this to all three gauge forces: each formula slot inherits the grid matching the interaction character of its participant. The phase slot tracks the carrier. The exponent slot tracks what the force confines.

### The Coxeter pair

The $`E_8`$ root system has Coxeter number $`h = 30`$. Its exponents are the integers coprime to $`h`$: $`\{1, 7, 11, 13, 17, 19, 23, 29\}`$. These pair under conjugation $`e \leftrightarrow h - e`$. The electromagnetic coupling uses the Kostant exponent 13. Its conjugate is arithmetic: $`30 - 13 = 17`$. That the conjugate governs the strong and weak couplings is the ladder's working hypothesis. Among the four conjugate pairs $`(13, 17)`$ is exceptional within the restricted class: the three alternatives miss the measured couplings by 15% to 156% across the nine comparisons. That restricted comparison singles the pair out; it does not force the assignment, and the broad control of Section IV does not establish uniqueness.

The same exponent 17 governs both the strong and weak couplings. What differs is the grid.

### Grid ladder selection rule

The domain sizes $`60 = |I|`$ and $`120 = |2I|`$ trace to the edge stabilizer $`Z_4 \subset 2I`$: integer-spin irreps carry only real $`Z_4`$ content (domain $`D = 60`$), half-integer carry only complex pairs ($`D = 120`$). That $`-I`$ spin sort fixes the $`60/120`$ split for the mass irreps. The gauge-carrier ladder below reuses those two domains under a distinct criterion, identity-preserving (60R) versus fermion-changing (120) action, not the mediator's own spin; the two uses of the split should not be conflated.

Each gauge force occupies a rung of the carrier/target grid ladder. Each coupling formula has two slots: one for the force carrier (photon, gluon, or W/Z) and one for what the force acts on or confines. Each slot is assigned to the 60R-grid when the role is bosonic (intensity-like) or to the 120-grid when the role is spinorial (wavefunction-like). The three observed gauge forces occupy three of the four possible pairings, with spinorial content increasing monotonically:

| Force | Carrier character | Phase grid | Confinement target | Exponent grid | Spinorial slots |
|---|---|---|---|---|---|
| EM | Bosonic (photon preserves identity) | 60R | Bosonic (current, no confinement) | 60R | 0 of 2 |
| Strong | Bosonic (gluon rotates color) | 60R | Spinorial (confined fermions) | 120 | 1 of 2 |
| Weak | Chiral charged currents ($`W^\pm`$ changes flavor; $`Z`$ flavor-diagonal at tree level) | 120 | Spinorial (fermion transitions) | 120 | 2 of 2 |

The three forces exhaust the lower triangle of the grid matrix. There are no gaps and no unused rungs. The color reading the strong-force rung uses traces to the face stabilizer $`Z_3 \subset 2I`$: restricting a propagating mode to it exposes trivial characters and conjugate nontrivial pairs, which MIT reads as the available color singlet and triplet/anti-triplet channels, as set out in the companion mass spectrum analysis. The grid distinction traces to the edge stabilizer $`Z_4`$. The gauge ladder is the stabilizer structure of the icosahedron expressed through the force sector.

### $`\alpha_s`$: the strong coupling

The gluon is a boson (phase grid = 60R), but it confines fermions (exponent grid = 120). Kostant exponent 17 on the 60R phase grid, with one step of $`\Omega_\Lambda`$ on the 120 domain:

```math
\alpha_s = C(17/60) \times \Omega_\Lambda^{-1/120} = 0.1162
```

Observed: 0.1180. Agreement: 1.5%.

### $`\alpha_W`$: the weak coupling and the Plato twist

The quantity here is the $`SU(2)_L`$ gauge coupling, $`\alpha_W \equiv \hat{g}^2/4\pi = \hat\alpha(M_Z)/\hat{s}_Z^2`$. The weak interaction is the chiral, parity-violating sector: its charged-current $`W^\pm`$ vertices change fermion flavor, while the neutral $`Z`$ current is flavor-diagonal at tree level. Both slots sit on the 120 fermion domain (phase grid = 120, exponent grid = 120). The $`W^\pm`$ remain spin-1 bosons; the 120 assignment reads their action, not their spin, and it is a proposed selection rule rather than a derived one. The $`Z`$, an electroweak mixture, plays no role in the carrier classification. Kostant exponent 17 on the 120 phase grid:

```math
\alpha_W = C(17/120) \times \Omega_\Lambda^{-1/120} \times \cos(\pi/10) = 0.0339
```

Observed: 0.0338. Agreement: 0.3%.

**The Plato twist.** The correction $`\cos(\pi/10) \approx 0.951`$ was first motivated through the dodecahedral geometry of $`S^3/2I`$: the dodecahedron (dual to the icosahedron) has angular defect $`\pi/5`$ at each vertex, the Möbius $`Z_2`$ holonomy was taken to halve it to $`\pi/10`$, and in that stabilizer reading the vertex geometry ($`Z_5`$) meets the Möbius twist while color ($`Z_3`$) transmits cleanly through the surface, the reading's account of why the strong and electromagnetic forces carry no twist. No computation stands behind that route.

The number does occur as a computed geometric invariant, by a different route. The shortest closed geodesics of $`S^3/2I`$ run along its five-fold axes, and a frame carried once around one by the Levi-Civita connection returns rotated by $`\pi/5`$, the gluing twist of the dodecahedral space. The spin lift of that rotation has half-trace $`\cos(\pi/10)`$. On the same loop the flat holonomy of $`2I`$ gives $`\cos(\pi/5)`$, and the spin lift takes its half-angle, $`\cos(\pi/10) = \sqrt{(1+\cos(\pi/5))/2} = \sqrt{(2+\varphi)}/2`$: the golden ratio comes with the five-fold axis, and the halving is the spin double cover rather than the Möbius twist. The calculation, with the nearby constructions that fail, is recorded in [The Plato Twist](../../framework/files/working/files/plato-twist.md).

What remains underived is the insertion: why the weak coupling carries that factor, at the first power, and alone. The weak force is the only Standard Model interaction that violates parity, but the factor cannot encode that: it is even in the twist's orientation, so if chirality is what singles out the weak row, it enters elsewhere. The factor is a discrete geometric quantity rather than a continuously adjustable coefficient, and until the insertion is derived the correction remains an ansatz.

Numerically, the correction is selective: it uniquely improves $`\alpha_W`$ (from 5.5% to 0.3%), and uniquely degrades both $`\alpha`$ (from 0.4% to 4.5%) and $`\alpha_s`$ (from 1.5% to 6.4%) if misapplied. That selectivity is specific to the weak row; deriving why is what the ladder still owes.

### $`\alpha_s / \alpha_W`$: pure geometry

The ratio of the strong to weak coupling cancels all $`\Omega_\Lambda`$ dependence:

```math
\frac{\alpha_s}{\alpha_W} = \frac{C(17/60)}{C(17/120) \times \cos(\pi/10)} = 3.426
```

Observed: 3.490. Agreement: 1.8%. Same Kostant exponent, different grids, one twist correction. The ladder reads the strong-to-weak ratio as geometry of the domain.

### The scorecard

| Coupling | Formula | Framework value | Observed | Agreement | Status |
|---|---|---|---|---|---|
| $`\alpha`$ | $`C(13/60) \cdot \Omega_\Lambda^{-1/60}`$ | 0.00733 | 0.00730 | 0.4% | Conditional (Λ-anchored); exponent provisional |
| $`\alpha_s`$ | $`C(17/60) \cdot \Omega_\Lambda^{-1/120}`$ | 0.1162 | 0.1180 | 1.5% | Conjectural |
| $`\alpha_W`$ | $`C(17/120) \cdot \Omega_\Lambda^{-1/120} \cdot \cos(\pi/10)`$ | 0.0339 | 0.0338 | 0.3% | Conjectural (Plato-twist ansatz) |
| $`\alpha_s/\alpha_W`$ | $`C(17/60) / [C(17/120) \cdot \cos(\pi/10)]`$ | 3.426 | 3.490 | 1.8% | Conjectural |

The percentages are convention-pinned, and the conventions carry weight. The α row is a $`q^2 = 0`$ statement: at $`M_Z`$ the same framework value misses $`\hat\alpha(M_Z)`$ by ≈6%. The 0.3% weak residual is specific to the $`\overline{\text{MS}}`$ convention at $`M_Z`$ ($`\alpha_W = \hat\alpha(M_Z)/\hat{s}_Z^2`$); substituting the on-shell mixing angle shifts the target by ≈3.5%. And the ladder has not yet seated hypercharge: above electroweak symmetry breaking, α is built from the $`U(1)_Y`$ and $`SU(2)_L`$ couplings, so a complete ladder would seat $`g_1`$ and derive $`\sin^2\theta_W`$. That future seat is already overdetermined: with $`\alpha`$ and $`\alpha_W`$ both seated, $`1/\hat\alpha = 1/\alpha_Y + 1/\alpha_W`$ fixes $`\alpha_Y = \hat\alpha/(1 - \hat\alpha/\alpha_W)`$, so a $`U(1)_Y`$ geometry must reproduce that value without a new fit parameter, and a seat that introduces one to land it has fitted rather than derived. Computing $`\sin^2\theta_W = \hat\alpha(M_Z)/\alpha_W`$ is correspondingly not a third comparison: from the tabulated targets it returns $`\hat{s}_Z^2`$ identically, since that is how $`\alpha_W`$ is defined here, and from the two framework values it returns their residuals as a ratio. Scale matching is the open problem (see Section VIII).

Under the Λ-anchored reading, the α row is a conditional comparison. The 0.4% holds when $`\Omega_\Lambda`$ is fixed externally, from the Planck Λ inference. When α is instead the best-conditioned anchor that fixes $`\Omega_\Lambda`$, its own 0.4% is a consistency check, not an independent prediction, and the genuine output of that route is $`\Lambda_\text{ref} = 3/R^2`$ to 23%. The surface sector is over-determined: you anchor on one of Λ, α, or the mass ratio and the others become conditional outputs, never all at once (see [Three readings of one hierarchy](../../framework/README.md#three-readings-of-one-hierarchy)).

Those anchors do not presently close on one value. Substituting the mass-spectrum $`R_\Lambda`$ for the coupling-route $`R_\Lambda`$ moves $`\Omega_\Lambda`$ by about a factor of ten, which the $`-1/60`$ exponent damps to roughly 4% in the conditional $`\alpha`$ value: small in absolute terms, but an order above the 0.4% quoted here, so the mass and coupling calibrations cannot both preserve the percent-level gauge match. This is the same $`R_\Lambda`$-route tension carried under [Inputs and Calibration](../../framework/README.md#inputs-and-calibration), and it is an internal alternative calibration rather than a revised external Λ of the kind the core-consistency condition in Section VIII speaks to.

## VI. The α-Λ Connection

Both the cosmological constant and the fine structure constant reference the same hierarchy $`\Omega_\Lambda`$. The difference is how much of it they use.

```math
\Lambda_\text{top} \cdot \ell_P^2 = \Omega_\Lambda^{-1} \cdot C(60/120) = 2\,\Omega_\Lambda^{-1}
```

```math
\alpha = \Omega_\Lambda^{-1/60} \cdot C(13/60)
```

$`\Lambda_\text{top}`$ sits at the antinode: $`C(60/120) = C(30/60) = 2`$. This is the bare surface eigenvalue; the Gauss/de Sitter conversion $`3/2`$ carries it to the vacuum-reference value $`\Lambda_\text{ref} \cdot \ell_P^2 = 3\,\Omega_\Lambda^{-1}`$ (see the [cosmological constant](../../cosmos/files/cosmological-constant.md)). Grid choice is invisible at the antinode. $`\alpha`$ sits away from the antinode, where the grid matters: $`C(13/60) = 0.79`$ on the bosonic grid vs $`C(13/120) = 0.22`$ on the spinor grid.

$`\Lambda_\text{top}`$ uses the full hierarchy (exponent 1). $`\alpha`$ uses 1/60-th: one grid step. The ratio of log-scalings confirms the relationship:

```math
\frac{\log_{10}\alpha}{\log_{10}(\Lambda_\text{top} \cdot \ell_P^2)} \approx \frac{-2.13}{-121.7} \approx \frac{1}{57}
```

Close to 1/60; the offset comes from $`C(13/60) \neq C(60/120)`$. The coupling constant measures how much hierarchy one quantum of exchange crosses. $`\Lambda_\text{top}`$ is the full surface spectral seed. $`\alpha`$ is one resolved interaction step within the same hierarchy.

### Planck-floor limit and scale matching

The formula gives a fixed value of the electromagnetic coupling:

```math
\alpha = C(13/60)\,\Omega_\Lambda^{-1/60}
```

$`\Omega_\Lambda`$ is fixed by the cosmological boundary scale. The formula's argument is a boundary condition, not an energy scale. Under the Λ-anchored reading this is a base-value comparison, not a theory of energy-dependent running. The agreement is with the low-energy value of $`\alpha`$, not with $`\alpha(M_Z)`$.

The Planck-floor limit is still meaningful. If the hierarchy were collapsed to $`\Omega_\Lambda \to 1`$:

```math
\alpha \to C(13/60) = 0.792
```

Order unity. This is a structural limit of the formula: in a Planck-scale bounded domain, the hierarchy suppression disappears. It is not the same as saying that $`\Omega_\Lambda`$ varies locally with scattering energy in our universe.

Standard QED running remains a perturbative field-theory effect layered on top of the infrared coupling. Connecting the MIT base value to $`\alpha(q^2)`$ requires an additional derivation: either identifying the formula with $`\alpha(q^2 = 0)`$ and leaving conventional vacuum-polarization running unchanged, or deriving a scale-dependent effective hierarchy from MIT. That second step is open.

This gives a geometric version of the usual unification intuition: when the hierarchy suppression is removed, the couplings become order unity. Whether this can be promoted to an energy-dependent unification mechanism requires the open scale-matching step above.

## VII. The Vacant Rung

*Beyond the v2 deposit: the deposited paper stops at the vacant fourth pairing and defers its interpretation until the grid rule is derived. This section and the extension tests in Section VIII are the live framework's stronger reading.*

The grid ladder in Section V assigns two structural properties to each gauge force: the character of its carrier (phase grid) and the character of what it confines (exponent grid). Each slot resolves as bosonic (60R, intensity $`|\psi|^2`$, period 1) or spinorial (120, wavefunction $`\psi`$, anti-period 1). Two binary choices across two formula slots yield four possible rungs, three occupied.

| Phase grid (carrier) | Exponent grid (target) | Physical reading | Force |
|---|---|---|---|
| 60R | 60R | Bosonic carrier, bosonic current | EM |
| 60R | 120 | Bosonic carrier, confined fermions | Strong |
| 120 | 120 | Flavor-changing charged-current carrier, fermion transitions | Weak |
| 120 | 60R | Fermionic carrier, bosonic target | — |

Three rungs are occupied; the upper off-diagonal entry, 120/60, is empty, and structurally so: a gauge rung preserves the fermion or boson character of what it acts on, so the 120/60 rung, a fermionic carrier acting on a bosonic target, has no realization among gauge forces. The firing order (topology $`\to`$ wave $`\to`$ observable) runs one direction, and the mechanism is the obstruction below.

In the stabilizer framework, the three occupied rungs exhaust the monotone sequence in spinorial content:

| Rung | Spinorial slots | Stabilizer interface | Force |
|---|---|---|---|
| 60R / 60R | 0 of 2 | Pure $`Z_4`$ real sector | EM |
| 60R / 120 | 1 of 2 | $`Z_3`$ color (face) confining $`Z_4`$ complex sector | Strong |
| 120 / 120 | 2 of 2 | $`Z_5`$ vertex through $`Z_2`$ twist | Weak |

Spinorial content increases. The reverse move (from 2 spinorial slots to 1 bosonic target) would break monotonicity. The ladder climbs; it does not descend.

### What the vacant rung describes

In the language of particle physics, the 120/60 entry requires:

1. A **fermionic force carrier** (spinorial phase grid). All known mediators (photon, gluons, W, Z) are spin-1 bosons.
2. A **bosonic confinement target** (bosonic exponent grid). The force would bind or confine integer-spin matter.

This is the structure of supersymmetric gauge interaction. Gauginos (spin-1/2 superpartners of gauge bosons) mediate forces between scalar partners of fermions (squarks, sleptons). The SUSY force sector is the natural occupant of the 120/60 rung: spinorial (gaugino) carriers acting on bosonic (scalar) matter.

### The obstruction

The vacancy is a rule of the ladder, not a spin-statistics theorem. Every gauge rung here acts within a statistics class: it changes phase, charge, or representation but preserves the fermion-or-boson character of what it acts on, and the three occupied rungs climb monotonically in spinorial content. The weak rung is the test case: its charged-current action swaps one fermion for another, so the target stays a fermion and the carrier stays a spin-1 boson. The 120/60 cell reverses that climb, sending the full-domain action into a bosonic target, so it falls outside the pattern the three forces trace; the cell that would sit there needs a fermionic (gaugino) carrier binding bosonic matter, which no observed gauge force provides. Ordinary quantum field theory does permit fermionic mediators between fermions and bosons, so the obstruction here is the ladder's own rule, not a spin-statistics prohibition. Underneath, the anti-periodic boundary condition makes $`\psi`$ the fundamental object and $`|\psi|^2`$ its square: that projection is well-defined but non-invertible, which is the measurement-level reason the 120 and 60R grids stay distinct.

### The prediction

Within the grid-action reading, the three observed gauge forces exhaust the three realized rungs. A fourth fundamental force would require the 120/60 rung, which the ladder does not generate. The empty rung is therefore a conditional structural prediction of the ladder, not a theorem that no fourth force can exist.

Supersymmetric partners, in their standard formulation as gaugino-mediated interactions between scalar matter, are the natural occupant of that ungenerated rung. The prediction is not that superpartners are heavy. It is that the gaugino-mediated SUSY force sector does not appear as a realized fundamental interaction, as intrinsic to the framework's picture as the Möbius strip having a single edge.

The grid ladder was constructed to derive coupling constants. It was not designed to count forces. That it produces exactly three occupied rungs matching exactly three observed gauge interactions, with the vacancy mapping onto exactly the sector that decades of collider searches have failed to populate, is a conditional structural output of the selected ladder rather than an input to it.

## VIII. Falsification

**Failure conditions (deposited v2)**, prospective and named before the fact:

| Condition | Fails if | Scope |
|---|---|---|
| Internal failure | A derivation of the grid rule or the Plato-twist factor, once constructed, yields a different grid assignment or a different correction | Ladder |
| Convention stability | Common-scale, common-scheme updates move $`\alpha_s`$ or $`\alpha_W`$ outside a 5% tolerance under the stated $`M_Z`$, $`\overline{\text{MS}}`$ convention | Ladder |
| Core consistency | A revised Λ moves the conditional α prediction outside 2% | α core |

**Working-extension tests** (beyond the deposit, contact with observation):

| Test | Kills the extension if | Sharpness |
|---|---|---|
| Force count | A fourth fundamental force occupies the 120/60 rung | Decisive |
| SUSY vacancy | Gaugino-mediated interactions observed at any energy scale | Decisive |
| Scale consistency / running | The three coupling values cannot be assigned to consistent reference scales, or MIT cannot connect the infrared $`\alpha`$ value to conventional $`\alpha(q^2)`$ running | Open |
| $`\alpha`$ – $`\Lambda`$ correlation | Refined Λ pushes predicted $`\alpha`$ further from CODATA | Weak (sensitivity suppressed by 1/60) |

The deposited conditions name in advance what would kill the construction. The extension tests are where the working framework meets data: the force count and SUSY vacancy are tested by every collider run. The open question spanning both is scale consistency: the three values sit at different energy scales ($`\alpha`$ at $`q^2 = 0`$, $`\alpha_s`$ and $`\alpha_W`$ at $`M_Z`$), and deriving RG running from the MIT hierarchy structure remains open.

---

One Coxeter pair $`(13, 17)`$, its conjugation forced by $`E_8`$ arithmetic, its assignment the ladder's hypothesis. One selected grid ladder occupied by three forces. One twist correction, on the parity-violating row alone. Three gauge-coupling values from that ladder, at 0.4%, 1.5%, and 0.3%. Their ratio at 1.8% with no $`\Omega_\Lambda`$ input at all. $`\Lambda_\text{top}`$ uses the full vacuum hierarchy. $`\alpha`$ uses one-sixtieth of it. The strong and weak forces fill the remaining rungs.

*The fine structure constant is the fine structure of the cosmological constant: the vacuum hierarchy resolved at its first step.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
