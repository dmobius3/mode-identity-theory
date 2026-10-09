<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The First-Positive Transfer Run

**Type:** Result
**State:** Closed
**Status (2026-09-29):** Run blind against terms frozen before it, and reviewed. On the conic band $`M(W)`$ neither registered sampler, value or transverse, carries the output of any of the eighteen ambient blocks run into the band's first-positive eigenspace, in either class of output, under any registered cone condition, at any registered placement or width; the lowest blocks settle this at every pose and width without numerics. Condition 1 of the scaling law therefore carries the first-positive projection as an adopted premise, as registered before the run, and nothing is falsified. The run's spectral step at $`\delta_0 = R`$, corrected in review for one missed level, and a theorem the review adds for every $`\delta_0`$ show that under the same cone-trace matching the untwisted problem has no level at $`2/R^2`$ below the critical width, so with the premise, uniformity fails for untwisted blocks read under that rule.
**Summary:** Condition 1's first transfer computation: how much of each ambient block's sampled output reaches the conic band's first positive mode, run blind on the projective placement.
**Inputs:** `scaling-law-uniqueness.md` (Step C's reduction), `projective-carrier.md` (§II, the two classes of output), `../../bedrock/files/first-eigenvalue.md` (the band and its operator), `scripts/first-positive-transfer/`
**Parent:** `scaling-law-uniqueness.md`

---

RESULT, a registered negative whose grade was decidable before the run. The [scaling law](scaling-law-uniqueness.md)'s Step C reduces its shared boundary mode to the first-positive projection: if each block's sampled state is the projection of its sampler output onto a simple first-positive eigenspace, every block carries the same profile. This run asked whether either registered sampler makes that projection automatic on the conic band $`M(W)`$ of the [first-eigenvalue paper](../../bedrock/files/first-eigenvalue.md), placed through the projective layer as [The Projective Carrier](projective-carrier.md) places it. Neither does. The output of each of eighteen ambient harmonic blocks, two for every irreducible of $`2I`$, leaks out of the first-positive eigenspace, under the value and the transverse sampler, in the twisted and the untwisted class, under every registered cone condition, at four placements and four widths. The two lowest blocks decide every column at every pose and width by a rank count (§II), so the run's numbers confirm a grade that follows from the terms without them; what the run adds is each block's first-positive weight and the same-trace spectrum. As registered, condition 1 returns to the projection as an adopted premise, and nothing is falsified. The same-trace spectrum settles what the terms left open: the untwisted problem then has no level at $`2/R^2`$ below the critical width, so under that matching the holonomy separates the level, and an untwisted block read under it cannot share the twisted profile (§III).

**Related:** [Scaling law](scaling-law-uniqueness.md), [The Projective Carrier](projective-carrier.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md).

---

## I. The question, as frozen

The terms were frozen on 2026-09-28, before the run, and are published unchanged as [`FREEZE.md`](scripts/first-positive-transfer/setup/FREEZE.md), SHA-256 `f824ccad7d5819c89991b0b792a68c7c0c717393ab786a12f75ada1ee97d1f52`. Main stated the work order and its scope before the run, in [The Projective Carrier §X as of commit 739d799](https://github.com/dmobius3/mode-identity-theory/blob/739d7995804da59d3e95dba3bbfd95767d4dafd3/files/framework/files/working/files/projective-carrier.md#x-what-this-page-does-not-do), pushed on 2026-09-28 twelve minutes before the first attempt started. The terms use $`M(W)`$ as the declared calculational realization of the projective placement, so the run decides none of the carrier's open sub-decisions ([The Projective Carrier](projective-carrier.md) §XI).

**The band.** $`M(W)`$ is the rectangle $`[0, \pi R] \times [-W, W]`$ with $`(0, w) \sim (\pi R, -w)`$ and metric $`dy^2 + \cos^2(y/R)\,dw^2`$, for $`0 < W < \pi R/2`$. It is placed in a great $`S^2`$ of $`S^3`$ by

```math
P(y, w) = R\big[\cos(y/R)\big(\cos(w/R)\,c + \sin(w/R)\,d_y\big) + \sin(y/R)\,p\big],
```

with pole $`p`$, azimuth $`c`$ and $`d = p \times c`$, where $`d_y = d`$ before the pinch $`y = \pi R/2`$ and $`d_y = -d`$ beyond it, so that $`-I`$ pairs $`(0, w)`$ with $`(\pi R, -w)`$, the band's seam.

- **The blocks.** For each irreducible $`\tau`$ of $`2I`$, the block $`E^\tau_n`$ is the $`\tau`$-isotypic part, under left multiplication, of the degree-$`n`$ harmonics on $`S^3`$. The run takes the first two degrees $`n \ge 1`$ at which each $`\tau`$ occurs: 12 and 20 for $`1`$, 2 and 10 for $`3`$, 6 and 10 for $`3'`$, 6 and 8 for $`4`$, 4 and 8 for $`5`$, 1 and 11 for $`2`$, 7 and 13 for $`2'`$, 3 and 9 for $`4'`$, 5 and 7 for $`6`$. The constants are an ungraded control.
- **The samplers and the two classes.** The value sampler $`O^{(0)}\Psi = \Psi \circ P`$ and the transverse sampler $`O^{(1)}\Psi = \partial_\nu \Psi \circ P`$, the derivative along the great sphere's normal; neither is primary. Under $`O^{(0)}`$ a block's output is a section of the band's orientation line, the twisted class, exactly when $`\tau(-I) = -\mathrm{id}`$, and under $`O^{(1)}`$ exactly when $`\tau(-I) = +\mathrm{id}`$ ([The Projective Carrier](projective-carrier.md) §II). Each output is graded in its own class.
- **The target operators.** The band's Laplacian, with Neumann arcs and the regular branch in every nonconstant transverse sector. In the constant sector the twisted class takes the Friedrichs extension or bridging at $`\delta_0 = R`$, which share the first positive level $`2/R^2`$, spanned by $`\sin(y/R)`$ ([first eigenvalue](../../bedrock/files/first-eigenvalue.md), Theorem 1.2). The untwisted class takes Friedrichs, or the $`\phi_0`$-transformed bridging rule, both with $`2/R^2`$ spanned by $`\phi_0\sin(y/R)`$, or the same cone-trace matching at $`\delta_0 = R`$, whose first positive level the run computed first.
- **The measure.** For a block $`E`$, a sampler $`O`$ and a cone condition, the leakage is $`\Lambda = \lVert O|_E\rVert^2_{HS} - \lVert P_1 O|_E\rVert^2_{HS}`$, with $`P_1`$ the projection onto that class's first-positive eigenspace in $`L^2`$ of the band's area measure. A block that the geometry selects has $`\Lambda = 0`$.
- **Placements and widths.** A generic pole and azimuth, and one on each kind of $`2I`$ axis, 2-fold, 3-fold and 5-fold. At the 2-fold placement $`\pm k`$ preserve the core, which was disclosed in advance. The widths are $`W/R \in \{1/4, 1/2, 1, 7/5\}`$.
- **The grades, fixed before the numbers.** Selection: $`\Lambda = 0`$ for every width and orientation. Partial: $`\Lambda = 0`$ at every placement. Leakage: $`\Lambda > 0`$ at some placement, a no-go for deriving the projection from that sampler's geometry in that class. If every admissible sampler leaks, condition 1 returns to the projection as an explicit physical premise, and it is not falsified.

## II. The blind result

Every column grades leakage, at every placement and every width.

| Class | Sampler | Cone condition | Grade |
| --- | --- | --- | --- |
| twisted | value | Friedrichs, bridging | leakage |
| twisted | transverse | Friedrichs, bridging | leakage |
| untwisted | value | Friedrichs, $`\phi_0`$-transformed, same matching | leakage |
| untwisted | transverse | Friedrichs, $`\phi_0`$-transformed, same matching | leakage |

The grade does not rest on the numerics. $`\Lambda = 0`$ needs a block's sampled image to lie inside the first-positive eigenspace, a single line except at the untwisted crossing $`W = \pi R/4`$ under the same matching, where it is a plane. Every column receives some of the five full blocks, $`E^2_1`$, $`E^3_2`$, $`E^{4'}_3`$, $`E^5_4`$ and $`E^6_5`$: each is the whole degree-$`n`$ harmonic space, invariant under all of $`SO(4)`$, so its output does not depend on the pose. In the twisted columns, $`E^2_1`$ under the value sampler and $`E^3_2`$ under the transverse sampler return the great sphere's three coordinate functions on the band, and only $`\sin(y/R)`$ among them is first-positive. It carries exactly a third of the norm, so their leakage fraction is exactly two thirds at every pose and width. In the untwisted columns, $`E^2_1`$'s transverse output is the constant, orthogonal to every untwisted first positive mode, and $`E^3_2`$'s value output is the quadratics on the great sphere, a six-dimensional image. So every column leaks at every pose and width (DERIVED). The other blocks leak at every registered placement; whether an unregistered pose confines one of them is not tested.

The numbers agree. Over the 864 graded values the smallest leakage fraction is the lowest blocks' exact two thirds, which the run's quadrature gives as 0.665; the next block leaks 0.70 of its norm. Under Friedrichs most of each block's norm lies above the first positive level, a median of 82 to 94 percent by sampler and class, and the ground mode's share is small, a median of 3 to 10 percent, except for $`E^2_1`$'s transverse output, which is all ground. That spread is what restriction predicts: a degree-$`n`$ harmonic restricts to the great sphere with components up to degree $`n`$.

Under the premise, what the run supplies is each block's first-positive weight $`\lVert P_1 O|_E\rVert^2_{HS}`$, which uniformity's fixed spectral weight reads for that block. The full blocks' weights do not depend on the pose; the others' do, by up to a factor of 2.6 across the four placements. Only $`E^2_1`$'s transverse weight is zero at every placement.

## III. The same cone-trace matching

Under the same cone-trace matching the terms gave nothing about the untwisted spectrum, and the run computed it first. In the constant transverse sector the untwisted problem splits into parts even and odd across the seam. The even part is forced regular, with levels $`0, 6, 20, \dots`$ in units of $`1/R^2`$. The odd part has Dirichlet at the seam and the regularized condition $`\tilde u_D = 0`$ at the cone, and in the first-eigenvalue paper's trace convention its levels $`\lambda = \nu(\nu+1)/R^2`$ solve

```math
\frac{\pi}{2}\tan\frac{\pi\nu}{2} - \gamma - \psi(\nu+1) = \ln\frac{\delta_0}{2R}.
```

At $`\delta_0 = R`$ its positive root is $`\nu = 2.341328411`$, a level at $`7.823147140/R^2`$. The first positive level is therefore $`6/R^2`$, spanned by $`(3\sin^2(y/R) - 1)/2`$, for $`W \le \pi R/4`$, and beyond that width the transverse branch $`\alpha_0(\alpha_0+1)/R^2`$ with $`\alpha_0 = \pi R/(2W)`$. It is simple except at $`W = \pi R/4`$, where the two cross, a width the run did not tabulate.

**One level missed, corrected in review.** The return states that this problem has no negative level. Its search stopped at $`\lambda = -1/(4R^2)`$, below which $`\nu = -\tfrac12 + i\kappa`$ is complex. There the left side of the condition is real and falls without bound, and at $`\delta_0 = R`$ it meets the right side at $`\lambda = -1.34520728/R^2`$, a cone-bound state odd across the seam, confirmed by direct integration of the radial equation. The condition's ground state is therefore a defect state, not the constant the return names. The grades use only the first positive level, which is unchanged, so no grade moves.

**No level at $`2/R^2`$ (DERIVED).** For $`W < \pi R/2`$ and every $`\delta_0 > 0`$, the untwisted problem under the same cone-trace matching has no level at $`2/R^2`$. The even constant part is regular, with levels $`\ell(\ell+1)/R^2`$ for even $`\ell`$. At $`2/R^2`$ the odd constant part has, up to scale, the single solution $`\phi_0 \sin(y/R)`$, which is regular with $`\tilde u_D^\pm = \mp 1`$, so the matching excludes it. Every nonconstant sector starts at $`\alpha(\alpha+1)/R^2 > 2/R^2`$. What replaces the level depends on $`\delta_0`$: below $`\delta_0 = 2R`$ the problem has a negative level and its first positive level lies above $`2/R^2`$; at $`2R`$ zero is a double level; above $`2R`$ a level lies in $`(0, 2/R^2)`$. So under this matching the holonomy separates $`2/R^2`$ from the untwisted spectrum, and an untwisted block does not share the twisted class's first-positive profile.

## IV. Audit, review and conformance

- **Blind.** A fresh solver ran the terms in a contained environment. It received a transcription of the frozen terms with the framework context left out, a brief, and the first-eigenvalue paper with its navigation, figures, citation and certification removed. The audit of its record found that it read nothing else: its nine flags are reads of its own background-task outputs and one string in a print statement, and no access was refused. A first attempt ended at an output limit before computing anything; a second completed the run with the terms unchanged.
- **Review.** Each check can fail, and each has a planted defect that trips it. The sampled norms are exact: at $`R = 1`$, $`\lVert O^{(0)}|_E\rVert^2_{HS} = 2\dim(E)\,W/\pi^2`$ and $`\lVert O^{(1)}|_E\rVert^2_{HS} = 2n(n+2)\dim(E)\,W/(3\pi^2)`$, since a block's kernel has a constant diagonal on $`S^3`$ and an isotropic first-derivative density there. All 304 rows meet these within $`2.8 \times 10^{-4}`$, the run's quadrature error. Six placement-dependent rows, recomputed by a different method, agree within $`4.8 \times 10^{-4}`$ of each block's norm. Every output lies in the class that $`\tau(-I)`$ and its sampler assign. Direct integration checks the same-trace roots; as a separate control it reproduces the paper's twisted-bridging threshold, $`\delta_0 = 2R/e`$.
- **Conformance.** The per-level rows whose ground state is a defect state are missing, as the return declares: twisted bridging and the $`\phi_0`$-transformed rule, and, after the correction above, the same matching. The ranks are not stated but are determined, since every level used is simple at the tabulated widths. The grade is symbolic in $`W`$ and in the pose (§II); the weights are numerical, at the four widths and placements. The zero rule's relative tolerance, $`10^{-12}`$, lies far below the run's precision, and no value comes within three orders of magnitude of zero. None of these bears on the grade, which needs $`\Lambda > 0`$ at one placement.

## V. What it decides

The reading was fixed before the numbers. Neither registered sampler supplies the first-positive projection on $`M(W)`$, in either class, so condition 1 of the [scaling law](scaling-law-uniqueness.md) returns to it as an explicit physical premise, which the scaling law carries as adopted: the observer reads the sampler through the band's first positive mode. The premise is uniformity's first requirement restated at the operator level, not a weaker ground for it; the run removes one candidate derivation, from the samplers' geometry. It is not falsified. Under Friedrichs, the registered channel reading places most of the leakage in the samplers' geometry rather than in the conic defect; for the other extensions the per-level rows it would need are missing (§IV).

The run decides none of the carrier's open sub-decisions ([The Projective Carrier](projective-carrier.md) §XI): whether $`M(W)`$ is the carrier (1b), the sampler (1d), the extension and the untwisted rule (1e), or the layer (1f). It adds a consequence to one option of 1e: with the premise, uniformity fails for any contributing block read through the untwisted class under the same cone-trace matching (§III). And while the pose is open (1f), the first-positive weights of the blocks that are not full depend on it.

*Added 2026-09-29: 1e and 1d have since been ruled: Friedrichs in both sectors, and the transverse sampler, normalized at unit radius, for every block ([The Projective Carrier](projective-carrier.md) §XI). The run selected neither. The value column stays the registered alternative, and the verdict holds for both samplers.*

*Added 2026-10-02: 1f has since been ruled: the carrier's physical layer is $`\mathbb{RP}^3`$ and its pose is free ([The Projective Carrier](projective-carrier.md) §XI). The run selected neither, and with the pose free the first-positive weights of the blocks that are not full stay pose-dependent.*

## VI. Guards

- Which blocks land in which class is fixed by $`\tau(-I)`$ and the sampler, known before the run, and gets no physical reading. In particular it is not read as the $`60R`$ projection.
- The results get no spin-statistics reading ([The Projective Carrier](projective-carrier.md) §II).
- Nothing here selects $`M(W)`$ as the physical carrier, a sampler, an extension, an untwisted rule or a layer.

## Files

In [`scripts/first-positive-transfer/`](scripts/first-positive-transfer/), with the SHA-256 of every other file in `SHA256SUMS`:
- `setup/`: the frozen terms, `FREEZE.md`, and the two checks they name under `tools/`, byte for byte, each with its record. `axes.py` checks the convention and the placements' axes exactly; `g4_terms.py` checks the characters and $`\tau(-I)`$, the blocks' degrees, the classes, the placements' symmetries and the seam, each with a planted defect.
- `run-1/`: the solver's two input files, its return (SHA-256 `eb776a5c19890d5d56fa04772975158b8e518730acec88c12c035fbac8241361`), its scripts and its result records, as returned. The paper it received is the bedrock page with navigation, figures, citation and certification removed.
- `review/`: `numbers_check.py`, built on `transfer_kernel.py`, checks the norms, the classes, six rows and the margin; `same_trace_check.py` checks the same-trace spectrum. Both come with their records.
