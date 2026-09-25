<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Effective-Metric Floors

**Type:** Result
**State:** Closed
**Status (2026-09-15):** Complete as a registered negative, checked by one script. Run under a work order frozen before it, the attempt asked whether anything in MIT constrains the missing spatial projection independently of wanting flat space, and whether any such constraint says what the projection is. Four constraints survive and none says what it is, so no candidate is written down. Every future effective-metric object inherits them as floors: the same map at every point, with only the isotropy group A5 inherited at a fixed observer unless the object declares how the domain's isometries act on the flat target's rotations; locality; no new dimensionful scale; and time dependence by the phase ratio over a static substrate. The domain has a transitive SO(3) of isometries, but MIT identifies it with the flat target's rotations only in the flat limit, a comparator, so the directional and radial classifications of the transfer family rest on an identification a candidate must earn. Without it a shell's predicted directional pattern can be any nonnegative A5-invariant function, and the conservation of each shell's power, on which the ratio table's weights rest, becomes a condition of its own. C8's intertwining and locality tests hold either way.
**Summary:** What MIT supplies, independently of wanting flat space, toward the object that would produce the spatial projection; the four floors any such object inherits; and what the missing rotation identification does to the two transfer classifications and to the ratio table.
**Inputs:** `missing-spatial-projection.md` §II, §IV, `stress-tensor-bridge.md` C3, C7-C9, §III and §VI, `directional-transfers.md` §II, §V, `radial-transfers.md` §II-III, `molien-p1-bridge.md` §II, §IV, §V, `molien-ratio-table.md`, `../../../README.md`, `../../../../spectrum/files/the-waltz.md` §VI, `redshift-and-cooling.md` §I, `temporal-budget.md` §II, `friedmann-as-output.md` §I, `postulate-bridge.md`, `sampler-first-test.md` §1-2, `variational-score-to-sample.md` §4-6, `scripts/effective-metric-floors/a5_family_check.py`
**Parent:** `stress-tensor-bridge.md`

---

## I. The question, and what was fixed before it

[The Missing Spatial Projection](missing-spatial-projection.md) found no map from the static domain to flat three-space in MIT's existing machinery, and specified what a new effective-metric object would have to supply (§IV). This page records the next question.

> Does MIT contain, or independently motivate, an object F that produces the spatial projection?

A work order fixed the terms before the question was put, and nothing in it was amended.

- **Tests, not ingredients.** The four requirements of The Missing Spatial Projection §IV score a candidate, and none may be used to build one. No mechanism was preregistered: not a coarse-graining, not a kernel, not an emergent metric.
- **Sources, tagged by what they may do.**
  - Existing definitions may motivate F: the construction attempt's inputs, the engine page's two seams as operations, and the anti-periodic Rayleigh form of [the variational page](variational-score-to-sample.md) §4.
  - Speculative machinery enters only as a named assumption: that page's two-level action architecture and schematic functional (§5-6), and the [postulate bridge](postulate-bridge.md)'s Tier 2 and Tier 3.
  - Target statements say what is wanted, so they cannot motivate: [the Stress-Tensor Bridge](stress-tensor-bridge.md)'s placement fork (§III) and its question on the effective curvature (§VI), the engine page's paragraph on placement, the Research Frontier's Dynamics problem, the operative flat-FLRW line in the routes of [the R problem](r-problem.md), and [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §V.
  - Comparators only score: C3, C7-C9, R7's three pages, and the P1 Bridge's flattenings (§V).
  - Forbidden: the variational page's frozen kinetic term and potential, and any object, action, potential or metric ansatz whose only reason is flat space, $`k_N`$, P1 or the Friedmann metric.
- **Two questions per handle.** Why would MIT contain this, if flat FLRW space were not already wanted? An answer earns at most a constraint. What does that fact say F is? Only an answer to this earns a candidate. A handle is generative if it identifies or restricts the form of F, or a definite class of forms, and constraint-only if it states a property any acceptable description owes without supplying that form.
- **The closed-destination control.** A handle passes if its source would read the same with a closed effective metric as the destination, which the bridge keeps open: "The closed alternative is not excluded" (§VI). A handle that makes sense only pointed at flat slices fails.
- **Outcomes.** E0: no independently motivated generative handle, so no candidate, with any constraint-only handles recorded as floors. E1 to E3: a candidate that fails one of the four requirements, clears them with a wrong or undetermined shell transfer, or clears them with definite C7 and C8 behavior. Classification opens only on a generative handle.
- **Expectations.** The two reviewers' and the drafter's all allowed E0, one of them beside a small class of candidates, and each named locality.

## II. What survives, and what does not

| handle | source | property it imposes on a spatial map | why MIT has it independently | closed destination | kind |
|---|---|---|---|---|---|
| H1, symmetry | [the P1 Bridge](molien-p1-bridge.md) §II | the same map at every point, and, at a fixed observer, covariance under the isotropy group $`A_5`$ | the transitive right $`SO(3)`$ and its stabilizer $`A_5`$ are facts of the quotient $`S^3/2I`$ | constrains a closed projection the same way: passes | constraint-only |
| H2, local agreement | [the Waltz](../../../../spectrum/files/the-waltz.md) §VI | the effective field reproduces the correlations near the observer, which by [the radial page](radial-transfers.md) §III is locality, with root-mean-square wavenumber $`k_N`$ | observation in MIT is the wave resolving at a position | owed over any destination: passes | constraint-only |
| H3, existing scales | the engine page, One Shape and the Hierarchy and the Observer | no new dimensionful scale: shell $`N`$ lands at $`c(N, \ell_P/R, \ldots)/R`$; not currently binding, since every placement in play already has this form | $`R`$ is the domain's length, and the hierarchy's ratio is MIT's own | the same for a closed target: passes | constraint-only |
| H4, sampling in time | [redshift and cooling](redshift-and-cooling.md) §I; the Waltz §VI | lengths read at phase $`t`$ rescale by $`S(t)`$, and the domain itself does not stretch | the phase ratio is read off the standing wave | the same for a closed target: passes | constraint-only |

Each handle says why MIT has the property, and none says what the property tells us F is. The Waltz places the observer, "An observer is anywhere the wave resolves to a finite value", and reads the phase ratio as the "evolution of the sampling relationship with a fixed venue"; redshift and cooling calls it "sampling rather than stretching".

- **Rejected: the clock's exponent and the matter dilution behind it.** Their only reason is the correspondence with general relativity, "the one imported line" ([Friedmann as output](friedmann-as-output.md) §I, with [the temporal budget](temporal-budget.md) §II), which is exactly the reason the work order rejects. The FLRW scale factor $`a_\text{eff} \propto S`$ is the translation layer, a target statement, and its native content is H4.
- **The intensity readout imposes nothing.** The engine page says "the framework's intensity readout squares the wavefunction", but it says so to explain the 120-to-60 readout of the sampling grids, and no source identifies the spatial map with that readout. Positivity therefore stays the third requirement, a test the object inherits, not a property derived for it here.
  - *Added 2026-09-25: the quoted engine sentence has since been revised; the engine now reads both grids through the same intensity and states them as resolutions. The conclusion stands.*
- **The observer scale imposes nothing through the one use checked.** At $`3.2 \times 10^{-31}`$ of $`R_\Lambda`$, a Gaussian smoothing at that width changes no Molien shell through $`N = 60`$ by more than $`2 \times 10^{-58}`$ ([The Missing Spatial Projection](missing-spatial-projection.md) §II). That says nothing about other uses, and H3 keeps the scale among the data a placement may draw on.
- **Nothing else imposes anything on a spatial map:**
  - the engine page's two seams, which are operations on the domain;
  - the Rayleigh form, which is temporal only;
  - the Tier 2 ground floor, which states facts about the embedding;
  - the sampler reading and [the sampler first test](sampler-first-test.md), whose only defined operator lands on the Möbius band, so a map through it would carry two-dimensional data;
  - the Waltz's "projecting them onto a four-dimensional chart", which names the projection, and whose spatial content beyond the name is H2;
  - the speculative machinery, which gives dynamics on an observer chart it presupposes; no functional exists, since Tier 2 is "a mood".

## III. The four floors

The outcome is E0: no independently motivated generative handle, and so no candidate. Any future effective-metric object inherits four floors:

1. the same map at every point, with only the stabilizer $`A_5`$ inherited at a fixed observer, unless the object declares how the domain's isometries act on the flat target's rotations (H1);
2. locality, with root-mean-square wavenumber $`k_N`$ (H2);
3. no new dimensionful scale beyond the existing data, not currently binding (H3);
4. time dependence by the phase ratio, over a static substrate (H4).

Positivity is not among them; it remains a requirement the object is tested against. Only locality was expected, and of the other three only the first changes what earlier pages can claim.

## IV. The missing rotation identification

The domain's symmetry is global: right multiplication gives a transitive $`SO(3)`$ of isometries, and the stabilizer of a point is $`A_5`$ ([the P1 Bridge](molien-p1-bridge.md) §II). What MIT does not supply is an identification of that global action with rotations of the flat target's wave-vector sphere at the observer. The sources reach one only in the flat limit, where the Bloch sphere of the factor $`2I`$ acts on "becomes the sphere of local wave-vector directions" (the P1 Bridge §V), and that is a comparator. Without it, a map inherits only $`A_5`$ at a fixed observer.

Both transfer classifications take the full identification in their first step: covariance under every rotation makes $`E_N(\hat z)`$ commute with the $`U(1)`$ of rotations about the pole, and so makes it diagonal ([the directional page](directional-transfers.md) §II, and [the radial page](radial-transfers.md) §II at each wavenumber). Under $`A_5`$ alone the stabilizer of a direction is cyclic of order 5, 3 or 2 on the 62 symmetry directions and trivial everywhere else, so $`E_N`$ is constrained only on those 62 directions, and elsewhere only related across each orbit of 60. The directional simplex, and the radial page's classification of the full transfer family, are therefore conditional on the identification. C8's intertwining and locality tests are not: intertwining acts on the Laplacian's eigenvalue alone, and the radial page's locality argument (§III) holds for any function on a shell, "isotropic or not".

What this does to the prediction, at $`N = 12`$:

- **P1 keeps its prediction.** Under $`A_5`$ alone a constant transfer need only commute with $`2I`$ on $`\mathrm{Sym}^N`$, and at $`N = 12`$ such transfers form a four-dimensional cone, since $`\mathrm{Sym}^{12}`$ is $`1 + 3 + 4 + 5`$ under $`A_5`$ (the P1 Bridge §IV). But below $`N = 60`$ the realized source on a shell is its invariant state (the directional page §V), which lies in the trivial summand, so every such transfer that conserves the shell's power predicts what P1 predicts.
- **The direction-dependent family becomes infinite-dimensional.** The predicted pattern on the realized source can be any nonnegative $`A_5`$-invariant function of direction, scaled to the shell's power, while the classified family's patterns span exactly four dimensions at $`N = 12`$ (the directional page §V). The record builds one from the part of $`\sum_v (\hat n \cdot v)^{20}`$, over the twelve five-fold directions $`v`$, that lies outside that span: the transfer is positive on every sampled direction and covariant to $`4 \times 10^{-13}`$, and its pattern sits at a relative residual of 0.289 from the span on the record's grid.

## V. What it touches in the ratio table

Across the classified family, normalization fixes each shell's angle-averaged power, by Schur's lemma: on the invariant state it is $`\sum_m t_m/(N+1) = 1/(N+1)`$ for every normalized $`t`$. Under $`A_5`$ alone a trace-normalized transfer delivers instead its weight on the trivial summand, which nothing constrains. [The ratio table](molien-ratio-table.md) reads only each shell's angle-averaged power, since its $`C_\ell`$ is an average over $`m`$, which by the addition theorem sees nothing else, and its weights rest on each shell's power being conserved. P1 conserves it, so every recorded number stands, for P1 and for every transfer that conserves each shell's power. What changes is the reason: conservation follows from full rotation covariance, and without it a candidate must show it on its own.

## VI. A pattern

Three findings now share one shape: the corpus names an object, states requirements on it, and supplies nothing that determines it. They concern two objects, not three: the variational route's functional, whose page records "no functional fixed", and the spatial projection twice, once when the construction attempt found no map among the existing objects and once here, where no source gives an independent handle on a new one.

## VII. What this leaves

MIT constrains a future effective-metric object in four ways, and does not say what that object is; even the full rotation covariance the two transfer classifications use is something the object must earn. [The Stress-Tensor Bridge](stress-tensor-bridge.md) carries that as C10: a candidate must declare how the domain's isometries act on the flat target's rotations. A declaration of the full rotation group brings the two classifications and the power conservation with it. A declaration of $`A_5`$ alone leaves both to be supplied, the larger family classified before any scoring and each shell's power shown to be conserved. C8's intertwining and locality tests apply either way.

Not computed: the classification of the $`A_5`$-covariant family, which would have opened only on a generative handle; and anything from $`N = 60`$, where a shell's invariant space has more than one dimension. **(Pointer added 2026-09-15.)** [The Spatial Carriers](spatial-carriers.md) takes up the field-level question this page leaves open, and classifies which $`A_5`$ spectra a shell can carry.

## VIII. Checks

[`a5_family_check.py`](scripts/effective-metric-floors/a5_family_check.py) needs numpy and scipy, and its record [`a5_family_check.out`](scripts/effective-metric-floors/a5_family_check.out) reproduces byte for byte from it. At $`N = 12`$ it checks:
- $`2I`$ as 120 unit quaternions, closed, with $`\rho_j`$ a representation paired with the rotations in the standard way;
- the invariant counts through $`N = 30`$, the decomposition $`1 + 3 + 4 + 5`$ with its four-dimensional commutant, and the invariant state in the trivial summand;
- constant $`2I`$-commuting transfers agreeing on the invariant state and differing on a generic one;
- the invariant state's averaged power, $`1/(N+1)`$ across the classified family to $`3 \times 10^{-17}`$, and not fixed across the constant $`A_5`$ family;
- the two direction-dependent transfers, their covariance, and their patterns against the classified span.

Each check carries a control that must come out the other way, and all five do.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
