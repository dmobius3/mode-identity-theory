<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Missing Spatial Projection

**Type:** Result
**State:** Closed
**Status (2026-09-15):** Complete as a registered negative, checked by one script. The attempt was run under a work order frozen before it. It set out to construct the static-to-effective spatial projection from MIT's existing sampler, embedding and observer machinery, and found no map to flat three-space: every permitted object lands on the domain S³/2I, the Möbius band, the phase circle or a scalar readout. Two routes to a flat target are closed by theorem. No smooth pullback of fields from the domain carries a nonconstant homogeneous law to a translation-homogeneous one, since A5 isotropy ties the law's gradient covariance to the metric and the domain is curved. No translations can be inherited from the domain's isometries, whose Lie algebra has no two-dimensional abelian subalgebra. The third route, linear maps that are neither, stays open, and the existing objects supply none. The missing object must supply a flat target with its own translations, a map that does not preserve distances, linearity and positivity, and a comoving scale tie.
**Summary:** What MIT's existing machinery can and cannot supply for the spatial map from the static domain to flat effective space, the obstruction that closes the pullback route for any candidate, and the four things a new effective-metric object must provide.
**Inputs:** `stress-tensor-bridge.md` C7, C8 and §VI, `directional-transfers.md`, `radial-transfers.md`, `molien-p1-bridge.md` §II, §V, `postulate-bridge.md`, `sampler-first-test.md` §1-2, `../../../README.md`, `../../../../spectrum/files/the-waltz.md` §VI, `redshift-and-cooling.md` §I-II, `temporal-budget.md` §I-II, `friedmann-as-output.md` §I, `scripts/missing-spatial-projection/missing_projection_check.py`
**Parent:** `stress-tensor-bridge.md`

---

## I. The question, and what was fixed before it

R7 of [the Stress-Tensor Bridge](stress-tensor-bridge.md) exists to derive the spatial part of $`g_\text{static} \to g_\text{eff}`$. Its two calculations classified what such a map can do to the Molien shells, over directions ([The Shell-to-Direction Transfers](directional-transfers.md)) and over wavenumber ([The Shell-to-Radius Transfers](radial-transfers.md)). This page records the attempt to construct the map itself from what MIT already has.

> Can MIT's existing sampler, embedding and observer machinery be composed into a map from fields on the static $`S^3/2I`$ to fields on flat three-space?

A work order fixed the terms before the attempt, and nothing in it was amended.

- **Inputs.** The only corpus objects allowed:
  - from the engine page, One Shape, the Sampling Grids, the Hierarchy and the Observer, and the One Wave readings of redshift and the clock;
  - the [postulate bridge](postulate-bridge.md)'s sampler reading and its Tier 2 ground floor;
  - [the sampler first test](sampler-first-test.md) §1-2;
  - [the Waltz](../../../../spectrum/files/the-waltz.md) §VI;
  - [redshift and cooling](redshift-and-cooling.md) §I-II, [the temporal budget](temporal-budget.md) §I-II and [Friedmann as output](friedmann-as-output.md) §I;
  - [the P1 Bridge](molien-p1-bridge.md) §II.

  Standard mathematics was always allowed.
- **Exclusions.** The [variational program](variational-score-to-sample.md)'s action, functional and potential; any action, potential or metric ansatz; any rule that chooses Q, P1 or $`k_N`$ by hand.
- **What does not count as the map.** Prose; the exponential map by itself, the flat limit or a transfer law the classification pages list; a generic flattening that uses nothing beyond $`S^3/2I`$; a map built to intertwine.
- **Scoring**, in order: whether a map exists at all, then linearity, positivity and a flat power, then C8, then the directional point. The outcomes were O0 (no map), O1 (a map outside the classified family) and O2 (a map in it).
- **Expectations.** Both reviewers and the drafter predicted O0.

## II. Where the existing objects land

| existing object | lands on |
|---|---|
| the postulate and the domain (engine, One Shape) | $`X = S^3/2I`$, curved and three-dimensional; the band $`M`$, two-dimensional; the edge $`S^1`$, one-dimensional |
| the sampling grids (engine) | the $`2I`$ labels and the intensity readout, on the phase |
| the observer scale (engine, the Hierarchy and the Observer) | two numbers, $`\sqrt\Omega`$ and $`\sqrt{\ell_P R_\Lambda}`$ |
| the redshift, cooling and clock readings | functions of the phase: $`S`$, $`\Psi`$, $`1 + z`$, $`T`$, $`a_\text{eff}`$, the lapse |
| the sampler reading, the Tier 2 ground floor, the sampler first test | the band: the target type of the sampling operator, its transverse candidate, normal fluctuations as sections of the orientation system, and the named transfer into the band's eigenspaces |
| the Waltz §VI | a point of $`X`$, a point of $`S^1`$, a depth, and a projection onto a chart, which it names |
| the P1 Bridge §II | the domain's symmetry, $`SO(3)`$ acting on the right with isotropy $`A_5`$, and the source covariance shell by shell |

The machinery reads out from the space onto its temporal structure, the band and its edge, and onto scalars. No object maps fields on the domain to fields on another three-dimensional space.

Flat space enters only as the effective metric the readings rest on: $`a_\text{eff} \propto S`$ "carries the volume", and the FLRW distance relation is "recovered as the translation layer". The engine page says so directly: "the map from the static geometry to the effective metric the distance model runs on has no derived source". The Waltz names the step, "projecting them onto a four-dimensional chart", without defining it.

The one arrow into a flat three-space the inputs reach is standard geometry: the exponential map at the observer's point, a comparator. The observer data neither selects nor alters it. The domain is homogeneous, so the observer's position is not a parameter, and at $`3.2 \times 10^{-31}`$ of $`R_\Lambda`$ the observer scale leaves every Molien shell through $`N = 60`$ unchanged, to $`2 \times 10^{-58}`$.

The outcome is O0.

## III. Three routes to a flat target

For the registered construction, the routes now on the table split three ways. Two are closed by theorem; the third remains open but is uninstantiated in the frozen corpus.

**Smooth pullbacks are closed.** At every point of $`X`$, the gradient covariance $`E[\nabla f \otimes \nabla f]`$ of a homogeneous law is invariant under the isotropy group $`A_5`$ (the P1 Bridge §II). Under $`A_5`$ the symmetric square of the tangent space is $`1 + 5`$, so the only invariant symmetric 2-tensor is the metric. The gradient covariance is therefore $`c\,g`$, with $`c`$ constant by homogeneity and $`c > 0`$ for a nonconstant law.

Pull such a law back along a smooth $`\phi: \mathbb{R}^3 \to X`$. Its gradient covariance becomes $`c\,\phi^* g`$, so a translation-homogeneous pullback needs $`\phi^* g`$ constant, hence flat. Where $`\phi^* g`$ is non-degenerate, $`\phi`$ is a local isometry onto the round $`X`$, whose curvature is $`1/R^2`$. Where it is degenerate, the pulled-back field is constant along its kernel. So no smooth pullback carries a nonconstant homogeneous law on $`X`$ to a non-degenerate translation-homogeneous field on flat space.

This holds for every candidate, not only the exponential map. For the exponential map at the observer the failure is measured:
- translating a pair by up to $`0.1R`$ changes its pulled-back distance by up to $`4.8 \times 10^{-4} R`$;
- the $`N = 12`$ shell's pulled-back correlation changes by up to 0.008 at $`0.15R`$;
- the flat controls stay below $`10^{-12}`$.

**Inherited translations are closed.** A construction that takes its translations from the domain's isometries needs an abelian group of them acting transitively. The isometries are $`SO(3)`$, and the bracket of $`\mathfrak{so}(3)`$ is the cross product, so two generators commute only when they are parallel. Every abelian group of isometries therefore has orbits of dimension at most one.

**Linear maps that are neither remain open.** These are smearing kernels and maps defined through the spectrum, and the existing objects supply none of either. The transfer laws of the two classification pages reach translation homogeneity through the spectrum, by assigning each shell a wavenumber, and C8 excludes that when it is built in. The flat limit reaches it only as $`R`$ grows, where the isometries contract to the Euclidean group.

## IV. What the missing object must supply

The arrow the corpus names and does not construct must supply four things:

1. a flat three-dimensional target with its own translations, not a subgroup of the domain's isometries;
2. a map from the domain's fields to fields on that target that does not preserve distances and is not a smooth pullback, which §III now forces rather than prefers, defined by its action on the space rather than through the shell decomposition;
3. linearity and positivity, so that it lands in the classified family, where C8 and the directional page can score it;
4. a comoving tie between the target's scale and the domain's, which $`a_\text{eff}`$ moves in time but does not set.

The corpus names this object twice, in the Stress-Tensor Bridge's question for "a genuine projection or coarse-graining that explains flat effective slices over a closed substrate" and in the Waltz's projection onto a chart. It is a new effective-metric object, not a further reading of the existing machinery, and the Stress-Tensor Bridge now carries its second requirement as C9. **(Pointer added 2026-09-15.)** [The Effective-Metric Floors](effective-metric-floors.md) asks whether MIT contains or independently motivates that object, and finds four floors on any candidate but nothing that says what it is.

## V. Checks

[`missing_projection_check.py`](scripts/missing-spatial-projection/missing_projection_check.py) needs numpy, and its record [`missing_projection_check.out`](scripts/missing-spatial-projection/missing_projection_check.out) reproduces byte for byte from it. It checks five things:
- the pullback failures above, against flat controls;
- the $`\mathfrak{so}(3)`$ bracket;
- the observer scale's effect on the shells;
- the single $`A_5`$ invariant among symmetric 2-tensors, counted over the 60 rotations built from $`2I`$ and checked closed.

Five mutation arms, one per claim, each turn it red.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
