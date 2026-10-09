<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Energy as Resolution Amplitude

**Type:** Note
**State:** Active
**Status (2026-09-02):** MOTIVATED, not derived. The reading is permitted by the framework; five promotion steps are named and unwalked.
**Summary:** A candidate reading of E²=(mc²)²+(pc)² as the Pythagorean theorem on the mode decomposition of the sampling operation.
**Inputs:** the standing wave $`\Psi = \cos(t/2)`$, the fermion mass formula ([engine](../../../README.md#the-mass-formula)), The Waltz §§V-VI

A candidate MIT reading of $`E^2 = (mc^2)^2 + (pc)^2`$. The framework appears to permit it; the derivation steps are specific and unwalked.

**Related:** [The Budget Map](budget-map.md), [The Waltz](../../../../spectrum/files/the-waltz.md).

---

## I. The Reframe

Standard Model reading of $`E = mc^2`$: mass is a property an object has, and that property manifests as a quantity of energy. Velocity adds kinetic energy. Total energy is the sum in quadrature: $`E^2 = (mc^2)^2 + (pc)^2`$.

The SM reading leaves $`mc^2`$ unexplained. "Mass is a property" is a definition, not a derivation. Why that property should equal an energy, converted by $`c^2`$, is asserted.

MIT candidate reading: energy is not a quantity an object carries. Energy is the amplitude of wave resolution at an observer's sampling coordinates. Rest mass energy is the amplitude resolved at a fixed sampling point. Momentum energy is the amplitude resolved along a path through $`S^3`$. Total energy is the full resolution.

Velocity does not cause energy. Velocity is a parameter of the sampling trajectory. Different trajectories extract different amplitudes from the same wave.

| SM reading | MIT candidate reading |
|---|---|
| Mass is a property objects have | Mass is the wave amplitude resolved at a fixed sampling point |
| $`mc^2`$ is the energy equivalent of mass | $`mc^2`$ is the temporal-mode content of the sampling operation |
| Velocity gives kinetic energy | Velocity is a feature of the sampling trajectory |
| $`(pc)^2`$ is kinetic energy squared | $`(pc)^2`$ is the spatial-mode content extracted along the trajectory |
| Pythagorean sum is empirical fact | Pythagorean sum is orthogonal mode decomposition of $`\Psi`$ |

## II. The Mode Decomposition

The standing wave $`\Psi(t) = \cos(t/2)`$ lives on $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$. The wave has a temporal mode (phase on $`S^1`$) and spatial modes (harmonics on $`S^3`$).

A sampling operation at a fixed geodesic position with phase advancing on $`S^1`$ extracts temporal-mode amplitude only. A sampling operation along a path through $`S^3`$ extracts both temporal-mode and spatial-mode amplitude. The two contributions are orthogonal: they come from different modes of the same wave on a bounded domain where spatial and temporal harmonics are independent.

Orthogonal contributions combine in quadrature. This is the candidate derivation of the Pythagorean form:

```math
E^2 = (\text{temporal-mode amplitude})^2 + (\text{spatial-mode amplitude})^2 = (mc^2)^2 + (pc)^2
```

The relativistic energy-momentum relation reads, in this picture, as the Pythagorean theorem on the mode decomposition of the sampling operation.

| Sampling mode | What it extracts | Contribution to $`E^2`$ |
|---|---|---|
| Fixed geodesic position, phase advancing on $`S^1`$ | Temporal-mode amplitude of $`\Psi`$ | $`(mc^2)^2`$ |
| Geodesic path through $`S^3`$, phase advancing on $`S^1`$ | Temporal mode plus spatial-mode amplitude | $`(mc^2)^2 + (pc)^2`$ |
| Null geodesic (photon) | Spatial-mode amplitude only; temporal and spatial locked by $`c`$ | $`(pc)^2`$ |

## III. The Photon Case

A photon propagates edge-only on $`S^1`$ (§V of the Waltz, masslessness as topological position). It never enters the Möbius surface and never resolves a temporal-mode amplitude at a fixed geodesic position. Its sampling is always along a null path, where temporal and spatial contributions are locked together by $`c`$.

In the mode decomposition picture: the photon's null geodesic through $`S^3`$ has geodesic distance equal to phase advance times $`c`$. The temporal and spatial modes contribute the same amplitude, which collapses the decomposition to a single term. The photon has $`E = pc`$ with no rest mass term because it has no sampling operation that extracts temporal-mode amplitude independently.

This is consistent with the Waltz's reading of masslessness as edge-only propagation. The two statements say the same thing in different languages:
- Waltz language: the photon stays on $`S^1`$, never crosses to the Möbius surface, pays no mass cost
- Mode-decomposition language: the photon samples along null paths only, has no fixed-position temporal contribution

## IV. What This Would Change

If this reframe is real, several SM framings get inverted.

**Mass-energy equivalence is structural, not conversional.** $`mc^2`$ is not "mass converted into energy." Mass and energy are the same quantity read at two manifold sectors. Mass is an $`n=1`$ edge observable; $`c^2`$ lifts it to the $`n=0`$ Planck scale where energy lives. The conversion factor is structural on $`S^1`$, the temporal edge.

**Inertia is a wave property, not an object property.** Resistance to changes in sampling trajectory comes from the wave-sampling relationship, not from the sampled object. All observers experience the same wave. The equivalence principle (gravitational mass equals inertial mass) follows immediately: both are the same feature of the same sampling operation.

**Rest frame is a sampling frame.** "At rest" means sampling at a fixed geodesic position in $`S^3`$. "In motion" means sampling along a path. There is no absolute rest, but there is a well-defined sampling operation for each observer, and the transformation between observers is a transformation between sampling operations.

**Kinetic energy is not added energy.** It is the spatial-mode content that any path-based sampling extracts. A stationary object has no kinetic energy not because it "hasn't been given any" but because a fixed-position sampling operation has no spatial-mode path to extract amplitude from.

## V. Connection to Existing MIT

The reframe does not need new postulates. It uses elements already derived or axiomatic in the framework.

| Element | Source | Role in reframe |
|---|---|---|
| $`c`$ as propagation rate on $`S^1`$ | Primitive input | Conversion factor between temporal and spatial contributions |
| Standing wave $`\Psi(t) = \cos(t/2)`$ | Axiom | The wave being resolved |
| Mass formula $`m(\rho,\sigma) = \mu_\Lambda \cdot C_\text{geom}(\rho) \cdot \ldots`$ | Engine, [mass formula](../../../README.md#the-mass-formula) | Specifies which irreps give which temporal-mode amplitudes at fixed positions |
| Masslessness as edge-only propagation | Waltz §V | Photons have no fixed-position sampling, hence no rest term |
| $`\mathbb{R}^4`$ as emergent from sampling | Waltz §VI | Removes the "moving through spacetime" framing that makes velocity primary |
| Observer coordinates: depth, position, phase | Waltz §VI | The sampling operation has structure; trajectory is a pattern in that structure |

The mass formula in particular is worth connecting. It specifies the spectrum of temporal-mode amplitudes that fixed-position sampling can resolve. The entries read against the electron, muon and tau sit at $`(R_7, \text{triv})`$, $`(R_8, \text{std})`$ and $`(R_4, \text{gal})`$. The entries and their quantum numbers come from the group-theoretic and torsion construction; which measured fermion occupies which entry is a comparison, not a prediction. In the reframe those are three temporal-mode resolutions at three different irreps and vacua. The mass formula is already in the right shape for this picture.

## VI. What Needs to Be Derived

Promotion from MOTIVATED to DERIVED requires walking the following steps.

**Step 1: The spatial-mode coupling.** The path tangent at each point of a trajectory couples to the spatial harmonics of $`\Psi`$ on $`S^3`$. The amplitude extracted depends on which spatial modes the tangent direction projects onto. The structural derivation of this coupling is the core open question. It needs to yield $`(pc)^2`$ with the correct $`c^2`$ factor from first principles.

**Step 2: Orthogonality of temporal and spatial modes.** The Pythagorean sum requires the two contributions to be orthogonal. For standing waves on bounded domains this is generically true: temporal and spatial harmonics are independent eigenmodes. But the specific wave $`\Psi`$ on $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$ needs to be shown to have this decomposition cleanly. No derivation of it is on record; it is open.

**Step 3: The $`c^2`$ factor on both terms.** $`c`$ appears in both $`mc^2`$ and $`pc`$. In MIT, $`c`$ is the propagation rate on $`S^1`$. The spatial-mode contribution $`(pc)^2`$ having $`c^2`$ factor needs to come from $`c`$ governing both the temporal advance and the null-geodesic constraint in $`S^3`$. This should fall out of the sampling operation being parameterized by phase on $`S^1`$ with $`c`$ as the universal rate.

**Step 4: Lorentz invariance as sampling symmetry.** The transformations between observers at different trajectories should form a symmetry group. That group should be (or contain) the Lorentz group. Structural plausibility: phase advance on $`S^1`$ and geodesic motion in $`S^3`$ together have a natural symmetry that includes boosts. Explicit derivation open.

**Step 5: Connection to the mass formula.** The fermion masses of the engine's [mass formula](../../../README.md#the-mass-formula) should correspond to specific temporal-mode amplitudes of $`R_7`$, $`R_8`$, and other irreps sampled at fixed geodesic positions. The mass formula already gives the right shape. What needs to be shown: the temporal-mode interpretation of $`\mu_\Lambda`$, $`C_\text{geom}`$, and the torsion factor as components of the amplitude extraction.

## VII. Status Summary

The reframe is structurally consistent with MIT's existing framework. It uses no new postulates. It recovers the SM relativistic energy-momentum relation as Pythagorean theorem on mode decomposition. The photon case checks. The mass formula sits in the right shape to be reinterpreted as temporal-mode amplitude spectrum.

None of the promotion steps are walked. The spatial-mode coupling is the core derivation needed. Lorentz recovery is the validation test.

Categorization: MOTIVATED with specific promotion paths. Not yet DERIVED. Not speculation; the framework's own structure points at this reading.

## VIII. Open Questions for the Future Paper

- Does the spatial-mode coupling yield $`(pc)^2`$ quantitatively, or only qualitatively?
- Do the Lorentz transformations fall out of sampling operation transformations, or is an additional ingredient needed?
- Where does the $`c^2`$ factor come from structurally? Is it the same $`c`$ on both terms, or two different $`c`$'s that happen to coincide?
- How does this connect to the equivalence principle derivation? If inertia is a wave property, gravity coupling should fall out the same way.
- What about quantum mechanics? The wave in MIT is classical in the sense of being a specific topological object, but the sampling operation should connect to measurement in QM. The resolution amplitude at a sampling point is suggestive of wavefunction collapse.
- Does the arrow of time live in the sampling? The standing wave is reversible and periodic, but the sampling history is not: you cannot un-sample. If irreversibility enters through the sampling rather than the wave, the arrow of time and the irreversibility of measurement are the same fact (see [Entropy as Realization Budget](entropy-as-realization-budget.md)).

## IX. What This Is Not

A claim that the SM is wrong. The SM predictions are correct at the observer scale, same as GR in Waltz §VI.

A claim that $`E = mc^2`$ needs replacement. It doesn't. It needs derivation. The SM asserts it; MIT may derive it.

A finished result. This is a research note pointing at where the framework appears to permit a deeper reading. The actual paper gets drafted after the promotion steps are walked.

---

*Velocity is not a source of energy. It is a parameter of the sampling operation.*

*What the wave yields depends on how it is sampled.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
