<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# :jigsaw: Contribute

Mode Identity Theory has open problems you can work on without accepting its physical interpretation. Most are ordinary problems in spectral geometry, geometric analysis or computation; one is a data analysis waiting on Euclid. Each entry states what is already proved, what is open, what would count as closing it, and where the source lives.

**A negative result is a result.** Declare the class you are working in before you compute, and do not tune a functional, extension, operator, pose or threshold after seeing whether it helps the theory. A no-go theorem, or a pre-registered test that fails, closes a problem as surely as a positive answer.

**How a check runs here.** The [fixed-edge stability check](/files/framework/files/working/files/fixed-edge-check.md) is a complete example: terms frozen before the run, two blind rooms that derived the result without seeing its source, an independent maintainer, and the outcome recorded whichever way it went. It reproduced, and its record says what the check could not see.

**How to take part.** Post in [Discussions](https://github.com/dmobius3/mode-identity-theory/discussions) or open an issue, with a write-up or a script. The text here is licensed CC BY 4.0 and the code MIT, so you can build on any of it with attribution.

## :seedling: A Good First Problem

### The first self-intersection width

**Setting.** Write $`S^3`$ as the unit quaternions, with the binary icosahedral group $`2I`$ (order 120) acting by left multiplication, and let $`\Sigma`$ be the great 2-sphere of purely imaginary quaternions. Pick orthonormal $`N, e \in \Sigma`$. For $`0 < W < \pi/2`$ let $`D(W) \subset \Sigma`$ be the double lune of points within longitude $`W`$, about the poles $`\pm N`$, of the great circle through $`N`$ and $`e`$. Its quotient by $`\pm 1`$ is a Möbius band embedded in $`\mathbb{RP}^3 = S^3/\{\pm 1\}`$, pinched to a point at the image of $`\pm N`$.

**Question.** Let $`W_*(N, e)`$ be the least $`W`$ at which two points of $`D(W)`$, not related by $`\pm 1`$, lie in one $`2I`$-orbit. Compute it as a function of the pose $`(N, e)`$, exactly where possible and numerically elsewhere, and find its symmetry strata, its extrema and the poses that attain them.

**Already known.** $`W_* < \pi/2`$ at every pose. $`W_* = 0`$ exactly when the axis orthogonal to $`N`$ and $`e`$ is a rotation axis of the icosahedral group that $`2I`$ covers (there are 31); at every other pose $`W_* > 0`$. Up to symmetry the poses form a three-parameter family. No certified values are on record.

**What counts.** The function, or rigorous two-sided bounds on it, with code anyone can rerun. Exact values at special poses count too.

**Why it matters.** The quotient $`S^3/2I`$ is where the band's image is observed, and $`W_*`$ is the width at which that image first meets itself. It would limit the width only if the carrier were this band and had to embed there; the framework rules the carrier's physical domain to be $`\mathbb{RP}^3`$, where this band embeds.

**Skills:** quaternions, finite groups, numerical geometry. **Difficulty:** starter. **Source:** [The Projective Carrier](/files/framework/files/working/files/projective-carrier.md#i-the-projective-layer), Proposition 0.4, and §XI, 1f.

## :triangular_ruler: Analysis and Geometry

### Does smoothing the cone point transmit?

**Setting.** Take the band $`M(W) = D(W)/\{\pm 1\}`$ above on a sphere of radius $`R`$, with $`W < \pi R/2`$. Its one singular point $`p_c`$, the image of $`\pm N`$, is where two sectors meet at a point. Take the Laplacian on sections of its orientation line bundle, equivalently functions on $`D(W)`$ that are odd under $`x \mapsto -x`$, with the Neumann condition on the edge. At $`p_c`$ it has more than one self-adjoint realization: the Friedrichs realization, which decouples the two sectors there, and transmitting ones that couple them.

**Question.** Fill a small region about $`p_c`$ so that the two sectors join through a neck of width $`\varepsilon`$, keeping the band inside its totally geodesic $`\mathbb{RP}^2`$, with the Neumann condition on the neck's new edge arcs and the metric and boundary data unchanged elsewhere, and let $`\varepsilon \to 0`$. For which classes of necks does the Laplacian converge to the Friedrichs realization, in a generalized norm-resolvent sense with identification maps between the changing spaces, or at least in its eigenvalues? Which scalings, if any, give a transmitting limit? Capping each sector separately would disconnect them, so the question is about necks.

**Already known.** In two dimensions a point has zero capacity, which supports decoupling in shrinking-neck limits, and the source paper expects an untuned smoothing to select the Friedrichs realization, with transmission only under a resonant scaling. One smoothing of a different kind is proved. On the rectangle $`[0, \pi R] \times [-W, W]`$ that carries the band's metric $`dy^2 + \cos^2(y/R)\,dw^2`$, with the pinch at $`y = \pi R/2`$, replacing $`\cos^2(y/R)`$ by $`\cos^2(y/R) + \varepsilon^2`$ opens the collapsed fibre into a neck of width $`2\varepsilon W`$, and as $`\varepsilon \to 0`$ the Laplacian converges to the Friedrichs realization, eigenvalue by eigenvalue and in norm-resolvent sense under a fixed unitary identification. That smoothing changes the metric, not the domain, so it does not settle the necks asked about here, cut inside the totally geodesic $`\mathbb{RP}^2`$ with new Neumann edges, or other metric profiles. Such necks keep the Laplacian nonnegative, so no limit of them, in eigenvalues or in resolvent sense, can be a bridging realization at any finite $`\delta_0`$, each of which has a negative eigenvalue: a transmitting limit of necks would be a nonnegative realization (the source paper's §7). The literature on thin channels and shrinking handles bears on them directly.

**What counts.** A proof in a declared class of necks. A generic decoupling theorem confirms the realization the framework adopted; a natural transmitting limit would overturn that choice.

**Skills:** spectral theory, self-adjoint extensions, singular perturbation. **Difficulty:** research. **Source:** [The Projective Carrier](/files/framework/files/working/files/projective-carrier.md#xi-the-ruling), §XI, 1e; [the first-eigenvalue paper](/files/framework/files/bedrock/files/first-eigenvalue.md), whose Proposition 7.1 is the metric smoothing; [The Smoothed-Cone Limit](/files/framework/files/working/files/smoothed-cone-limit.md), its declaration and cross-check.

### Can a natural sampling operator produce the first positive mode?

**Setting.** A field on $`S^3/2I`$ in an irreducible representation $`\tau`$ of $`2I`$ is a section of the flat bundle $`E_\tau`$, and the band maps into $`S^3/2I`$ by a map $`f`$. A sampling operator takes such fields to sections of $`f^*E_\tau \otimes \mathcal{L}`$ on the band, where $`\mathcal{L}`$ is its orientation line bundle. In the Friedrichs realization the band's Laplacian on these sections has $`2/R^2`$ as its first positive eigenvalue, and its eigenspace carries the single profile $`\sin(y/R)`$, up to a sign that flips at the cone point, times the fiber; $`y`$ is arclength along the band's core, measured from its equator arc.

**Question.** Fix a class of sampling operators: differential of order at most $`k`$, built from the band's geometry and the field alone, one construction for every $`\tau`$. Does any nonzero operator in the class send each of the eighteen ambient harmonic blocks of [the transfer run](/files/framework/files/working/files/first-positive-transfer.md#i-the-question-as-frozen), two for each irreducible of $`2I`$, into the first positive eigenspace? If none does, prove it. For a declared $`k`$ this is finite-dimensional linear algebra.

**Already known.** No nonzero local operator can do this for every ambient eigenfield: a field supported near one point samples to a section supported near that point's preimage, and no nonzero element of the eigenspace has small support. So the question is about finitely many blocks. For those, the two natural operators, restriction and the normal derivative normalized at unit radius, both leak out of the eigenspace: in a blind run, neither kept any of the eighteen inside it.

**What does not count.** Composing a sampler with the spectral projector onto the eigenspace. That assumes the projection the question asks to derive.

**What counts.** An operator in a declared class with the property, or a no-go theorem for the class; the no-go direction is probably the more reachable.

**Why it matters.** The framework's scaling law is a conditional theorem whose weight sits on exactly this projection, which is currently an adopted premise. A positive answer would also reopen the framework's choice of sampler.

**Skills:** representation theory of finite groups, spectral geometry. **Difficulty:** research. **Source:** [the scaling law](/files/framework/files/working/files/scaling-law-uniqueness.md#whats-closed); [the transfer run](/files/framework/files/working/files/first-positive-transfer.md); [The Projective Carrier](/files/framework/files/working/files/projective-carrier.md#ii-lemma-1-the-central-sign-restricts-to-the-möbius-holonomy), §II and §XI, 1d.

### Can the band's width be selected without a new scale?

**Setting.** The band $`M(W)`$ is unbent, and its width $`W`$ is free in $`(0, \pi R/2)`$. With its edge held fixed it is a strictly stable critical point of area at every width, among variations that keep the cone point's shape: that is the check reproduced blind above. It also has the least area of any Lipschitz map of a Möbius band with the same boundary map whose core generates $`\pi_1(\mathbb{RP}^3)`$, and ties only with maps that cover it once ([Propositions 7 and 8](/files/framework/files/working/files/projective-carrier.md#ix-fixed-edge-stability)); since each width has its own edge, this selects no width either.

**Already known.** With the edge free, the standard membrane energies without spontaneous curvature, surface tension, line tension, and bending of Willmore or Canham-Helfrich type, select neither the band nor its width. Line tension opens the cone point's pinch at first order. With the pinch held and zero sheet tension, the conic bands are the least-energy unbent bands and $`W`$ is a flat direction; neither of those two conditions is derived. A boundary law can make the widths discrete: if each of the edge's two loops is mapped onto itself by a deck transformation of $`\mathbb{RP}^3 \to S^3/2I`$ other than the identity, the band is conic and its width and pose lie in a finite family ([Proposition 3.2](/files/framework/files/working/files/projective-carrier.md#iv-proposition-3-no-zero-bending-band-has-a-smooth-geodesic-edge)), but nothing on record grounds that law.

**Question.** Find an independently motivated geometric functional or boundary law with an isolated critical width, or prove that no functional in a stated natural class has one.

**Admission rule.** A functional can always be built backward to make any chosen width critical. One counts only if it is motivated independently of the result, declared with its class and parameters before its dependence on $`W`$ is computed, introduces no new fitted scale, and gives a consequence beyond $`W`$. A no-go in a stated class needs no rule.

**Skills:** geometric analysis, calculus of variations. **Difficulty:** advanced; post the proposal before computing. **Source:** [Carrier Edge Regimes](/files/framework/files/working/files/carrier-edge-regimes.md); [the bar for a variational principle](/files/framework/files/working/files/postulate-bridge.md#dynamical-direction); [The Projective Carrier](/files/framework/files/working/files/projective-carrier.md#xi-the-ruling), §XI, 1b and 1c.

## :ocean: Dynamics on OpenWave

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/m8_roadmap.md)

OpenWave's M8 column has independently reproduced or audited the results the framework's four bedrock papers name in their certification sections, within the scopes stated there, and has reproduced the conic band's fixed-edge stability blind. Its open question is whether any reasonable field dynamics on $`S^3/2I`$ realizes the McKay ladder, the representation-theoretic spectrum the framework reads its masses from. The earlier numerical route closed unresolved, on its instrument rather than on the physics. A new route starts as a proposed dynamical family and meets OpenWave's rules before any computation: pre-registration, run-before-write, and reproduction by the maintainer. The [M8 roadmap](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/m8_roadmap.md) is the place to start.

## :telescope: Data: Not Open Yet

### Score the Euclid predictions when the data arrive

Five predictions were deposited on Zenodo before Euclid's first data release, each with its scoring rule. Row IV, a ceiling on the stellar mass function at $`z \gtrsim 10`$, is the one row expected at DR1-Foundation, in November 2026; the other four read cosmology-derived products in the full DR1, in mid 2027. Both dates are tentative. DR1 can falsify the $`a_0(z)`$ evolution row and score Row IV's ceiling; Row IV's translation to galaxies runs through the standard deep-MOND relation, conditionally. Each row is scored against the latest version of the card deposited on Zenodo before the first data capable of scoring it appear. An independent scoring, including a null or a falsification, counts.

**Skills:** galaxy surveys, cosmological data analysis. **Opens:** when qualifying data are released. **Source:** [the Euclid DR1 card](/files/cosmos/files/euclid-dr1.md).

## :infinity: A Side Problem in Pure Geometry

### The spherical paper Möbius band

Take the band of points within distance $`w`$ of a geodesic segment of length $`L`$ on the unit 2-sphere, $`0 < w < \pi/2`$, and glue its two ends with a flip. A spherical paper Möbius band is a smooth isometric embedding of it in the unit 3-sphere; by the Gauss equation, its second fundamental form has zero determinant. Which $`(L, w)`$ embed? In Euclidean space the paper Möbius band embeds smoothly only when its aspect ratio exceeds $`\sqrt{3}`$ (R. E. Schwartz, *The optimal paper Moebius band*, Annals of Mathematics 201, no. 1, 2025, 291–305).

A yes would give an alternative the framework set aside a smooth realization, one that keeps the framework's original formula literally; a no would leave that alternative only conic realizations. It is here because it is a good problem.

**Source:** [The Projective Carrier](/files/framework/files/working/files/projective-carrier.md#xi-the-ruling), §XI, reading (B′).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
