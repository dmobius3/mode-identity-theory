<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🌊 Dynamics

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/Unified_Slot_Action.png?raw=true" width="100%" alt="Bedrock">

Dynamics is one problem with two halves: how the wave content moves, and how that motion sources geometry. The first half now stands on a fixed geometry, as an effective theory rather than the framework's matter action: on $`\mathbb{R} \times S^3/2I`$, fields carrying the eight nontrivial representations of $`2I`$, its McKay slots, move under one common action whose self-interaction is the Surviving Ray's density interaction. The pages below follow those fields from that interaction to their lowest-energy states, and to the branches of standing waves that grow out of the interaction's critical orbits. The second half is the [Research Frontier](../../README.md#research-frontier)'s Dynamics question, and it has no derived map yet; it is the framework's largest structural debt, and the last entry below is its program. The equilibrium of the Möbius carrier itself is a separate question, and it stays with the embedding on the [Postulate Bridge](../working/files/postulate-bridge.md).

---

## [Surviving Ray](../bedrock/files/surviving-ray.md)

**The Interaction:** The spin-3 representation carries a four-channel family of scattering self-interactions. On the Poincaré homology sphere, for a block state at level 6 with the density interaction, binary-icosahedral symmetry restricts that family to two channels, one of them radial; modulo the radial part, the surviving self-interaction is forced onto a single projective ray. In the coordinates of the spin-3 condensate literature that ray is one coupling point, and the paper maps the critical geometry of the governing quartic there: ten critical orbits within a stated symmetry class, three more certified outside it, and the extremes of the top multipole, $`1/924`$ on the coherent states and $`463/924`$ on the hexagon. Back on the quotient, the first correction at the four symmetry-pinned rays is exact and was reproduced blind on OpenWave, and local branch germs exist at eight critical rays for sufficiently small amplitude, an argument audited there. Those critical orbits return below, where each nondegenerate one starts a branch of the slot fields' standing waves.

---

## [Slot Action](../working/files/slot-action.md)

**The Action:** One action for all eight slot fields, chosen without using any outcome it would be tested against and frozen before the runs that test it. Each field is a section of its flat bundle over $`\mathbb{R} \times S^3/2I`$ and moves by the wave equation of that bundle's Laplacian, and its self-interaction is the density quartic, the only quartic common to the slots that is built from the fibre metric alone. The choice is motivated rather than derived. It is the effective theory the OpenWave runs use, and it settles the lowest-level branches of five of the slots without a run.

---

## [Slot Ground States](../working/files/slot-ground-states.md)

**The Ground States:** Under that action every slot field has lowest-energy states at each fixed nonzero charge; each is a standing wave, and the set of them is orbitally stable. In the five rigid slots these are exactly the lowest-level family, stable at every charge, with the whole linear spectrum about each member on the imaginary axis. In the three soft slots the ground states keep a nearly uniform density at every charge, and in two of them, at small charge, they concentrate on the lowest level and form the branch through the coherent orbit.

---

## [Soft-Slot Branches](../working/files/soft-slot-branches.md)

**The Branches:** In the three soft slots, every critical orbit of the reduced quartic that is nondegenerate up to its symmetry continues to a branch of standing waves at small amplitude, and the branch's small-amplitude spectrum is read off the quartic. Hyperbolic slow motion makes a branch unstable; a nondegenerate minimum gives a stable branch and a maximum a spectrally stable one; and an indefinite orbit gives a spectrally stable branch when its slow motion is elliptic with Krein-definite frequencies and its zero modes are accounted for exactly. The page classifies the orbits it treats in exact or interval arithmetic, the Surviving Ray's census among them. A continuation run filed with OpenWave, under terms frozen before any target ran, then followed the branches at five of these orbits to finite amplitude on one fixed mesh. At three of the orbits it reached verdicts on five branches: three stayed elliptic wherever it could decide, two turned hyperbolic at amplitudes it bracketed but could not locate, and every persistence test that ran held. At the other two it gave no verdict in either slot: one failed the run's validity check at its smallest amplitude, and the other produced no point at all. These are numerical verdicts, so finite amplitude is still open as mathematics.

---

## [Stress-Tensor Bridge](../working/files/stress-tensor-bridge.md)

**The Sourcing:** The open half. The framework's one missing map runs from the realized wave content to a stress tensor with a declared placement, the metric whose Einstein equations it sources. The same gap sits behind gravity's open construction and behind the [clock exponent](../working/files/friedmann-as-output.md) the Waltz still takes from general relativity. Nothing on the map is derived, and no candidate matter action exists yet; a [variational route](../working/files/variational-score-to-sample.md) is preferred for building one, and the action it seeks could serve the slot fields too, provided its matter fields carry the slots. The slot action above defines a stress tensor of its own, but as an effective theory it is not a candidate matter action, so the bridge stays open. A matter action that carried the slot fields and supplied the missing source would join the two halves.

---

## 🏄‍♂️ Collaboration on OpenWave

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/m8_roadmap.md)

The runs these pages cite are filed with [OpenWave](https://github.com/openwave-labs/openwave), an open-source physics simulator, in M8, MIT's column there. They follow the project's rules: each run is pre-registered and frozen before it goes, nothing is written up until it has run, and the maintainer reproduces or adjudicates the result in public review. The column's open question is whether any reasonable action on $`S^3/2I`$ carries a common finite-amplitude branch or stability structure across the eight McKay slots; placing fields on the slots is kinematic, and the framework files no relation among their energies. The [M8 roadmap](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/m8_roadmap.md) is the place to start, and [CONTRIBUTING](/CONTRIBUTING.md#dynamics-on-openwave) says how to propose a route.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
