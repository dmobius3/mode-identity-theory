<a id="top"></a>
| **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |

---

# The Projective Carrier

**Type:** Result
**State:** Active
**Status (2026-10-05):** The premise is adopted by ruling (2026-09-27): the vacuum carrier itself is unbent, and its Möbius character is topological, the orientation holonomy around its core, not a product of extrinsic bending. The zero-bending carrier is realized through the projective layer: its core is the central element $`-I`$, and it lifts to and embeds in $`\mathbb{RP}^3 = S^3/\{\pm I\}`$, the one space form in which its totally geodesic completion embeds. Its physical domain is $`\mathbb{RP}^3`$, by ruling (2026-10-02), and $`S^3/2I`$ is its observable domain (§XI, 1f). The Λ lift's Stage-1 scalar Gauss relation needs only $`\det A = 0`$, which the conic band also meets bent, in a two-sided family in $`S^3`$ and a one-sided family in $`\mathbb{RP}^3`$; the ruling, not a derivation, sets those aside. On the placement nine further statements are derived, each with its hypotheses in its section: Lemma 1, on the central sign and the Möbius holonomy (§II); Theorem 2 with Corollary 2.1, on the Friedrichs bottom below $`2/R^2`$ (§III); Propositions 3, 3.1 and 3.2, on the edge (§IV); Lemma 4 with Proposition 4.1, on the rigid tilt, and Proposition 4.2, that under the Friedrichs realization the exact $`2/R^2`$, kept as the simple first positive level, does not force geodesic laps (§VI); Proposition 5, on the edge's lift (§VII); and Proposition 0.4, that at every pose the unbent carrier's image in $`S^3/2I`$ meets itself below the critical width (§I). The conic band is the leading carrier realization, not shown unique. The framework's two-lap sentence binds as topology only (ruling 2026-09-30), so the conic band's geodesic edge, equivalently within its class its least edge length or a rigid tilt as its $`2/R^2`$ mode, still has no framework ground: the Λ seed does not supply it, the free-edged membrane energies do not, and no framework-supplied support does ([The Carrier's Edge Regimes](carrier-edge-regimes.md)); nontrivial deck transformations keeping its loops would, but nothing grounds them (Proposition 3.2). Fixed-edge stability is derived at every embedded width for the declared class of variations, and its independent check, frozen before the run, has reproduced it blind ([The Fixed-Edge Stability Check](fixed-edge-check.md)). The fixed edge is a modeling input, adopted by ruling (2026-10-01) rather than derived, so this is fixed-edge stability, not vacuum stability. With the edge fixed, the bowtie at the cone point is locally area-minimizing (Proposition 6), and the conic band has the least area among carrier-class competitors with the edge fixed as parametrized, first for continuous finite-piecewise-smooth competitors (Proposition 7), then for Lipschitz competitors (Proposition 8), with equality only when the competitor covers it once. Condition 1's transfer has run on the conic band ([The First-Positive Transfer Run](first-positive-transfer.md)): under neither registered sampler does any of the eighteen ambient blocks run stay in the first-positive eigenspace, and under the same cone-trace matching the untwisted problem has no level at $`2/R^2`$ below the critical width. The postulate's formula now names the projective layer (§XI, 1a), the boundary map is held fixed as a modeling input (1c), the cone extension is Friedrichs in both sectors (1e), the sampler is the transverse derivative at unit radius for every block (1d), time runs on the abstract boundary circle (1g), and the physical layer is $`\mathbb{RP}^3`$ and the pose is free (1f); 1b stays open.
**Summary:** Where the Möbius carrier sits in the tower $`S^3 \to \mathbb{RP}^3 \to S^3/2I`$ under the zero-bending premise, what that placement implies for the carrier's bundles, spectrum and edge, the stability arm it opens, and the alternatives weighed against it.
**Inputs:** `../../bedrock/files/first-eigenvalue.md` (the conic band $`M(W)`$), `postulate-bridge.md` (Route 1, the sampler reading, the Tier 2 ground floor and bar), `sampler-first-test.md`, `tier2-fixed-boundary.md`, `first-positive-transfer.md`, `scaling-law-uniqueness.md` (Step C's reduction, the linear readout), `../../../../cosmos/files/cosmological-constant.md` §§II-IV, `scripts/projective-carrier/`
**Parent:** `postulate-bridge.md`
**Frozen:** 2026-09-27 §IX's terms, derivation and independent check, frozen before any run: the UTF-8 bytes from the start of the line beginning `*Registered` to the end of the Outcomes list's Unresolved item, with LF line ends, have SHA-256 `43e7165a0ba67eafd722896ce493e21b896bb1f1643aa45d6ed58c39c3612cb9`

---

This page came out of the condition-1 scope. That scope needed the sampler's transfer to run on an embedded band, which forced the question of where the band sits. The ruling of 2026-09-27 answers it by adopting the premise of §I. Apart from a paragraph in the Λ page's §III (§X) and the pointers to this page from the postulate bridge and the working index, no other page's claims change with it; the scope notes the ruling calls for are listed in §X, now [The Projective Carrier: Scope Inventory](carrier-inventory.md), and made separately. The page states what the adopted placement implies, with each result's hypotheses on its face.

## I. The projective layer

The framework's group already supplies a tower of quotients:

```math
S^3 \;\longrightarrow\; \mathbb{RP}^3 = S^3/\{\pm I\} \;\longrightarrow\; S^3/2I, \qquad 2I/\{\pm I\} \cong I .
```

$`S^3 \cong SU(2)`$ is the spin cover, $`\mathbb{RP}^3 \cong SO(3)`$ the rotation group, and the observable domain $`S^3/2I`$ is the quotient of the middle layer by the icosahedral group $`I`$. The center $`\{\pm I\}`$ already does work in the framework: integer-spin representations factor through $`I`$ and half-integer ones do not ([The Sampling Grids](../../../README.md#the-sampling-grids)), and $`-I`$ acts on the two with opposite parity ([Edges sort spin](../../../README.md#edges-sort-spin)). That is context, not a reason for the carrier to sit in the central quotient.

**The premise (ADOPTED by ruling, 2026-09-27).** The carrier itself has zero bending in its ambient space form $`S^3/\Gamma`$, the observable domain $`S^3/2I`$ included: it lies in a compact totally geodesic surface $`F`$ there, possibly immersed, and its core reverses $`F`$'s orientation, as it does automatically for a smooth band. The [Λ page](../../../../cosmos/files/cosmological-constant.md)'s Stage 1 uses $`A_{ij} = 0`$, on the covering great-$`S^2`$ band of which the carrier is a quotient. The postulate bridge's Tier 2 ground floor (2026-07-13) records that no immersed Möbius band in $`S^3`$ is totally geodesic. So in $`S^3`$ the carrier and the surface with $`A_{ij} = 0`$ are different surfaces, and the premise makes them one. That motive does not force the premise. Stage 1's scalar Gauss relation needs only $`\det A = 0`$, and the conic band meets it bent, in $`S^3`$ and in $`\mathbb{RP}^3`$ (Lemma 0.1, Propositions 0.2 and 0.3). Given the relation, zero bending adds interior minimality, $`H = 0`$ (Lemma 0.1), and the ruling adopts it for the vacuum carrier (below). The alternatives it set aside, a bent carrier in the projective layer, a bent carrier in $`S^3`$, a band in $`S^3`$ that is a different surface from the Λ lift's band, and an intrinsic model placed nowhere, stay in §XI as the decision's record.

**Lemma 0 (DERIVED).** Let a finite group $`\Gamma`$ act freely by isometries on $`S^3(R)`$. Let $`M`$ be a compact Möbius band, smooth or conic, lying in a compact surface $`F`$ with a totally geodesic immersion into $`S^3/\Gamma`$, and suppose $`M`$'s core reverses $`F`$'s orientation. Then the deck element of $`M`$'s core is $`-I`$. So $`-I \in \Gamma`$, and $`M`$ lifts to $`\mathbb{RP}^3 = S^3/\{\pm I\}`$, where its core represents the generator of $`\pi_1(\mathbb{RP}^3)`$.

*Proof.*
1. Lift the core through $`S^3 \to S^3/\Gamma`$ from a point $`x`$, carrying along the sheet of $`F`$ that contains $`M`$. That sheet is totally geodesic, so it continues inside one great sphere $`\Sigma = S^3 \cap n^\perp`$. The lift ends at $`\gamma x`$, where $`\gamma \in \Gamma`$ is the core's deck element.
2. The sheet arriving at $`\gamma x`$ and the image under $`\gamma`$ of the sheet at $`x`$ both lift the same sheet of $`F`$ through $`\gamma x`$, so they coincide. Both lie in $`\Sigma`$, so $`\gamma\Sigma = \Sigma`$. And $`\gamma`$ reverses $`\Sigma`$'s orientation because the core reverses $`F`$'s, so $`\gamma \neq I`$.
3. $`\gamma`$ is orthogonal and preserves $`n^\perp`$, so $`\gamma n = \pm n`$. If $`\gamma n = n`$, $`\gamma`$ would fix the point $`n`$ of $`S^3`$, which a free action forbids. So $`\gamma n = -n`$, $`\gamma^2`$ fixes $`n`$, and $`\gamma^2 = I`$.
4. An orthogonal involution with no fixed point on $`S^3`$ has no eigenvalue $`+1`$, so $`\gamma = -I`$. ∎

**The embedded case.** If $`F`$ is embedded, more follows. The lifts of an embedded surface are disjoint, and any two great spheres of $`S^3`$ meet, so $`F`$ lifts to the single sphere $`\Sigma`$ and every deck element preserves it. Steps 3 and 4 then apply to each element other than $`I`$, so $`\Gamma \subseteq \{\pm I\}`$. So $`\mathbb{RP}^3`$ is the one space form in which the carrier's totally geodesic completion embeds. In $`S^3/2I`$ that completion is only immersed: a left translate $`g\Sigma`$ is the great sphere orthogonal to $`gn`$, which is $`\Sigma`$ only for $`g = \pm 1`$.

**Proposition 0.4 (DERIVED).** Place the unbent conic carrier $`M(W)`$ in $`\mathbb{RP}^3`$ in any pose, and let $`W_*`$ be the least width at which its image in $`S^3/2I`$ meets itself: the infimum of the widths at which two points of $`M(W)`$ have the same image. The double lune grows with $`W`$, so above $`W_*`$ the image stays non-injective. Then $`W_* < \pi R/2`$ at every pose.

*Proof.* Identify $`S^3(R)`$ with $`R`$ times the unit quaternions, $`2I`$ acting by left multiplication. Right multiplications commute with that action, so the carrier's great sphere can be taken as $`\Sigma = S^3 \cap 1^\perp`$. Let $`\pm N`$ be the double lune's vertices and $`e`$ the point where the core crosses the lune's equator, so the core's lift lies on the great circle $`G_0`$ through $`N`$ and $`e`$. For $`x \in \Sigma \setminus \{\pm N\}`$ let $`\delta(x) \in [0, \pi/2]`$ be its longitude from $`G_0`$. Then the double lune is $`D(W) = \{\delta \le W/R\} \cup \{\pm N\}`$, and $`\Gamma = S^3 \cap \{1, e\}^\perp`$ is the set where $`\delta = \pi/2`$, with $`\pm N`$.
1. For $`g \in 2I \setminus \{\pm 1\}`$, $`g\Sigma = S^3 \cap g^\perp`$, so $`\Sigma \cap g\Sigma`$ is the great circle $`C_g = S^3 \cap \{1, g\}^\perp`$, and $`g\Gamma = S^3 \cap \{g, ge\}^\perp`$.
2. $`C_g = \Gamma`$ exactly when $`g \in \mathrm{span}\{1, e\}`$, and $`C_g = g\Gamma`$ exactly when $`1 \in \mathrm{span}\{g, ge\}`$, which is again $`g \in \mathrm{span}\{1, e\}`$, since $`\bar g`$ lies in that span when $`g`$ does. The elements of $`2I`$ in $`\mathrm{span}\{1, e\}`$ form a cyclic subgroup of order at most $`10`$, so at most $`8`$ of the $`118`$ non-central elements lie there. Take $`g`$ outside it.
3. $`C_g`$ differs from $`\Gamma`$ and from $`g\Gamma`$, so it meets their union in at most four points. Take $`x \in C_g`$ off both. Then $`x`$ and $`g^{-1}x`$ lie in $`\Sigma`$ off $`\Gamma`$, so $`\delta(x)`$ and $`\delta(g^{-1}x)`$ are below $`\pi/2`$, and both points lie in $`D(W)`$ once $`W/R`$ exceeds the larger. They are not related by $`\pm I`$, since $`2I`$ acts freely and $`g \neq \pm 1`$, so they are two points of $`M(W)`$ with one image in $`S^3/2I`$, and $`W_* \le R\max\{\delta(x), \delta(g^{-1}x)\} < \pi R/2`$. ∎

- $`W_*`$ is $`0`$ exactly when the axis orthogonal to $`N`$ and $`e`$ in the imaginary quaternions is the axis of a non-central element of $`2I`$. Such an element preserves $`G_0`$, so the image meets itself along the core at every width. Otherwise the core's translates under $`2I`$ are the other cosets of one circle subgroup, disjoint from $`G_0`$ and at positive distance from it, and $`D(W)`$, which lies within distance $`W`$ of $`G_0`$, misses them for small $`W`$. The value of $`W_*`$ at every pose, and its maximum over poses, are on [The First Self-Intersection Width](self-intersection-width.md): $`W_* \le \tfrac12\arctan(3 - \sqrt5)\,R \approx 0.326\,R`$, with equality at 30 double lunes.

**The placement (DERIVED from the premise).** By Lemma 0 no zero-bending carrier lives in $`S^3`$, and the carrier lifts to $`\mathbb{RP}^3(R)`$. There its completion is an embedded totally geodesic round $`\mathbb{RP}^2(R)`$, and its core represents the generator of $`\pi_1(\mathbb{RP}^3) \cong \mathbb Z_2`$. Everything below is stated there. Read in $`S^3/2I`$, Lemma 1 is unchanged, since it uses only the core's class. The layer does not need the premise: bent carriers lie there too (Proposition 0.3).
- For the conic band this is [first eigenvalue](../../bedrock/files/first-eigenvalue.md) Remark 2.1 read inside $`S^3`$. Take the double lune $`L \cup (-L)`$ on a great $`S^2 \subset S^3`$, with $`W < \pi R/2`$. The deck element $`-I`$ acts on that sphere as its antipodal map, so $`M(W) = (L \cup -L)/\{\pm I\}`$ is embedded in $`\mathbb{RP}^3`$.

The engine and the Λ page describe the carrier as the edge-identified quotient of a totally geodesic covering great-$`S^2`$ band. That fits this placement: Remark 2.1 realizes the same intrinsic band $`M(W)`$ as the double lune modulo the antipodal map, which is $`-I`$. It is not counted as a reason, because an abstract edge identification satisfies the wording as well as $`-I`$ does: the wording does not say where the quotient lives (§X). The bent bands of Propositions 0.2 and 0.3 satisfy it too: the quotient is taken abstractly, keeps the band's metric, and is then embedded, in $`S^3`$ or in $`\mathbb{RP}^3`$. Lemma 1's spin link is a consequence of the placement, not a reason for it.

[The sampler's first test](sampler-first-test.md) warned that the pillar's antipodal map and the ambient deck map "are antipodal maps on different spheres serving different purposes, and they must not be merged." The premise merges them: by Lemma 0, a zero-bending carrier's antipodal map is the restriction of $`-I`$. The merge is a consequence of the premise, not a further choice, and every result below is computed on the placed object.

**The premise's ground.** Stage 1 needs less than the premise gives, and the projective layer does not need the premise.

**Lemma 0.1 (DERIVED).** On the smooth locus of a surface in $`S^3/\Gamma`$ of radius $`R`$, with second fundamental form $`A`$ and mean curvature $`H = \mathrm{tr}\,A`$:
1. the Λ lift's Stage-1 scalar Gauss relation $`{}^{(3)}R = 3R_\Sigma`$ holds exactly where $`\det A = 0`$, which is where the surface's Gauss curvature is $`1/R^2`$;
2. if $`\det A = 0`$ and $`H = 0`$, then $`A = 0`$.

A carrier carries the scalar relation itself when the relation holds on it, not only on a covering band elsewhere. On such a carrier, zero bending is equivalent to interior minimality, $`H = 0`$ on the smooth locus, and to zero bending energy, $`\int H^2 = 0`$ or $`\int \lvert A\rvert^2 = 0`$. Full area-criticality also asks for a boundary condition, which depends on the boundary regime (§XI, 1c).

*Proof.* In a space form of curvature $`1/R^2`$, $`\mathrm{Ric}(\nu,\nu) = {}^{(3)}R/3 = 2/R^2`$ exactly, which is the Λ page's isotropy. The Gauss equation $`R_\Sigma = {}^{(3)}R - 2\,\mathrm{Ric}(\nu,\nu) + H^2 - \lvert A\rvert^2`$ then reads $`R_\Sigma = {}^{(3)}R/3 + 2\det A`$, since $`H^2 - \lvert A\rvert^2 = 2\det A`$. That gives 1. For 2, the principal curvatures have sum $`0`$ and product $`0`$, so both vanish. ∎

**Sidedness at the pinch.** Sidedness through $`p_c`$ is read along loops through it whose tangent planes match there. Carried once around such a loop, the normal returns either unchanged, and the carrier is two-sided along it, or reversed, and it is one-sided.

**Proposition 0.2 (DERIVED).** For every $`W < \pi R/2`$ the conic band $`M(W)`$ embeds isometrically in $`S^3(R)`$. Every isometric embedding of it there that is $`C^2`$ on the smooth locus has $`\det A = 0`$ and is bent somewhere, so $`H \neq 0`$ somewhere: none is minimal.

*Proof.* $`M(W) = (L \cup -L)/\{\pm I\}`$ is the lune $`L`$ of angle $`2W/R`$ with its vertices identified, since $`-I`$ carries $`L`$ onto $`-L`$ and $`N`$ to $`S = -N`$. Use Fermi coordinates about $`L`$'s central meridian: $`s \in [0, \pi R]`$ is arclength from $`N`$ along the meridian's great circle, and $`t`$ is the signed distance from that circle, with metric $`dt^2 + \cos^2(t/R)\,ds^2`$. There $`L`$ is $`\tan(\lvert t\rvert/R) \le \tan(W/R)\sin(s/R)`$. It has $`\lvert t\rvert \le W`$, and it meets the lines $`s = 0`$ and $`s = \pi R`$ only at $`N = (0, 0)`$ and $`S = (\pi R, 0)`$.

Let $`\Sigma' \subset S^3(R)`$ be a great sphere with unit pole $`B`$, and $`\gamma`$ a unit-speed simple closed curve in $`\Sigma'`$ of length $`\pi R`$, such as the circle of geodesic radius $`\pi R/6`$. Set

```math
\sigma(s, t) = \cos(t/R)\,\gamma(s) + R\sin(t/R)\,B .
```

1. $`\sigma`$ lies in $`S^3(R)`$. $`\sigma_t`$ has unit length, and $`\sigma_s = \cos(t/R)\,\gamma'(s)`$ is orthogonal to it, so $`\sigma`$ is isometric on $`L`$.
2. Comparing components along $`B`$ and in $`\Sigma'`$'s span, $`\sigma(s, t) = \sigma(s', t')`$ forces $`t = t'`$ and $`\gamma(s) = \gamma(s')`$. So $`\sigma`$ is injective on $`L`$, except that $`N`$ and $`S`$ both go to $`\gamma(0) = \gamma(\pi R)`$. That identification is $`M(W)`$'s own, so $`\sigma`$ embeds $`M(W)`$, pinch included.
3. The unit normal is $`\gamma`$'s normal in $`\Sigma'`$, constant along each line of constant $`s`$. The principal curvatures are $`\kappa(s)/\cos(t/R)`$ along $`\partial_s`$ and $`0`$ along $`\partial_t`$, where $`\kappa`$ is $`\gamma`$'s geodesic curvature in $`\Sigma'`$. So $`\det A = 0`$ and $`H = \kappa(s)/\cos(t/R)`$.

For any isometric embedding that is $`C^2`$ on the smooth locus, the Gauss curvature there is $`1/R^2`$, so $`\det A = 0`$ (Lemma 0.1). If it were minimal, Lemma 0.1 would make it totally geodesic. The lune would then lie in one great sphere with its meridians as great semicircles, the images of $`N`$ and $`S`$ would be antipodal, and the pinch would fail. ∎

- The embedding is not unique. Every unit-speed simple closed $`\gamma`$ of length $`\pi R`$, in any great sphere, gives one, and nothing on this page selects among them.
- It is two-sided. Its pinch is planar, so every meridian loop has matching tangent planes there, and around each the normal, $`\gamma`$'s normal, returns unchanged. The twist exists only as the pillar's label at $`p_c`$: the non-orientability the postulate names is intrinsic here, not a property of the embedding. For other isometric embeddings of $`M(W)`$ in $`S^3`$, whether a loop through the pinch has matching tangent planes there, and whether the normal ever returns reversed, is OPEN.
- Its edge passes the pinch twice, so in $`S^3`$ the edge is a closed curve through one point twice, not an embedded circle.
- As $`W \to \pi R/2`$ the pinch's two sectors close up, as the double lune does in $`\mathbb{RP}^3`$ (§V, cost 3).
- Cross-checked numerically in `scripts/projective-carrier/bent_carrier.py`.

**Proposition 0.3 (DERIVED).** For every $`W < \pi R/2`$ the conic band $`M(W)`$ also embeds isometrically in $`\mathbb{RP}^3(R)`$ bent: with $`\det A = 0`$ and $`A \neq 0`$ somewhere, its core the generator of $`\pi_1(\mathbb{RP}^3)`$, and one-sided.

*Proof.* Take $`x \in S^3(R)`$, and let $`c`$ be a unit-speed simple arc of length $`2W/R`$ in the unit sphere of $`x^\perp`$ that never meets $`-c`$, such as an arc of the circle of geodesic radius $`\pi/4`$ there. In the lune's colatitude $`\theta`$ from $`N`$ and longitude $`\lambda \in [-W/R, W/R]`$, set

```math
f(\theta, \lambda) = \cos\theta\; x + R\sin\theta\; c(\lambda) .
```

1. $`f`$ lies in $`S^3(R)`$, and its pullback metric is $`R^2(d\theta^2 + \sin^2\theta\, d\lambda^2)`$, the lune's.
2. Every meridian is a great semicircle from $`x`$ to $`-x`$, so $`N`$ and $`S`$ go to one point of $`\mathbb{RP}^3`$, and the core's deck element is $`-I`$. Away from the vertices, comparing components along $`x`$, $`f(\theta, \lambda) = \pm f(\theta', \lambda')`$ forces $`c(\lambda) = c(\lambda')`$ or $`c(\lambda) = -c(\lambda')`$, so the image in $`\mathbb{RP}^3`$ is embedded, pinch included.
3. The unit normal is $`c`$'s normal in the unit sphere of $`x^\perp`$, constant along each meridian. The principal curvatures are $`\kappa(\lambda)/(R\sin\theta)`$ along $`\partial_\lambda`$ and $`0`$ along $`\partial_\theta`$, where $`\kappa`$ is $`c`$'s geodesic curvature. So $`\det A = 0`$, and $`A \neq 0`$ unless $`c`$ is a great arc, which gives the premise's carrier.
4. Every meridian passes straight through the pinch, entering along $`-c(\lambda)`$ and leaving along $`c(\lambda)`$, with matching tangent planes there. The normal is constant along it, and the deck map $`-I`$ reverses it at the pinch, so the carrier is one-sided. ∎

- Its pinch is the vertex of the cones over $`c`$ and $`-c`$, which span all of $`T_x S^3`$ unless $`c`$ is a great arc. So it is not the planar pinch of the unbent carrier, which §IX holds fixed.
- The edge's lift is an embedded closed curve through $`x`$ and $`-x`$ once each, two great semicircles, so §VII's split holds for it as for the unbent carrier.
- The construction does not need $`W < \pi R/2`$. An arc of a circle of geodesic radius $`\rho < \pi/2`$ is simple and misses its antipode whenever $`2W/R < 2\pi\sin\rho`$, so the lune with its vertices identified embeds this way in $`\mathbb{RP}^3`$ for every $`W < \pi R`$. Under (A′) the bound $`W < \pi R/2`$ is therefore spectral, the narrow regime of first eigenvalue Theorem 1.2 with the simplicity of Corollary 6.3, not a limit of the embedding. Under (A) and (B′) it is also an embedding limit, since their planar pinch closes up there.
- Cross-checked numerically in `scripts/projective-carrier/bent_projective.py`.

**Three questions.** Lemma 0.1 and the two constructions separate the placed readings by three questions: does the carrier itself carry the scalar relation, in which layer does it lie, and is it bent? The first is intrinsic. By Lemma 0.1 the relation is the carrier's own Gauss curvature being $`1/R^2`$, so every isometric placement of $`M(W)`$ carries it, and no choice of layer or bending adds or removes it. It is 1b's question, what the carrier is, and (B) is a carrier with a different intrinsic metric. The other two are placement questions.
- Without the scalar relation on the carrier, a band in $`S^3`$ carries the postulate and the covering band carries the Λ geometry. Tier 2's run studied its minimal case, whose bands are unstable at the registered boundary.
- With it, the carrier is unbent only in the projective layer (Lemma 0), and bent carriers exist in both layers: one-sided in $`\mathbb{RP}^3`$ (Proposition 0.3) and two-sided in $`S^3`$ (Proposition 0.2).
- Lemma 0 runs one way. Zero bending forces the projective layer, but the layer does not force zero bending. What needs only the layer holds for a bent carrier there: Lemma 1, Theorem 2 and Corollary 2.1, and, with one-sidedness, §II's sampler analysis. What needs $`A = 0`$ does not: Lemma 4, the planar pinch, and §IX.

The premise is the unbent cell. The corpus pairs zero excitation with zero bending: the selection reading states that "The zero-excitation equilibrium cannot be the totally geodesic embedding" in $`S^3`$, and in the [Waltz](../../../../spectrum/files/the-waltz.md#the-surface-leads-only-the-vacuum) "Excited modes ($`m > 0`$) on the Möbius surface bend the embedding". It does not derive that a vacuum carrier must be unbent. The ruling of 2026-09-27 adopts that identification (§XI). It reads the Möbius character as global and topological, not produced by extrinsic bending; on this page that character is the orientation holonomy around the core, which for the conic band is supported at $`p_c`$ (Corollary 2.1).

## II. Lemma 1: the central sign restricts to the Möbius holonomy

**Lemma 1 (DERIVED, given the placement).** Let $`M \subset \mathbb{RP}^3`$ be a compact Möbius band, smooth or conic like $`M(W)`$, whose core represents the generator of $`\pi_1(\mathbb{RP}^3)`$. Let $`\tau`$ be an irreducible representation of $`2I`$, with flat bundle $`E_\tau = S^3 \times_{2I} V_\tau`$ over $`S^3/2I`$. Then the pullback of $`E_\tau`$ to $`M`$ is

```math
E_\tau\vert_M \;\cong\; \begin{cases} M \times V_\tau, & \tau(-I) = +\mathrm{id}, \\ \mathcal L_M \otimes V_\tau, & \tau(-I) = -\mathrm{id}, \end{cases}
```

where $`\mathcal L_M`$ is the orientation line bundle of $`M`$.

*Proof.*
1. $`M`$ deformation-retracts onto its core (for $`M(W)`$, collapse $`w \to 0`$), so $`\pi_1(M) \cong \mathbb Z`$, generated by the core.
2. The core is the nontrivial loop of $`\mathbb{RP}^3`$, so a lift of it to $`S^3`$ runs from a point $`x`$ to $`-x`$. Its class in $`\pi_1(S^3/2I) = 2I`$ is therefore $`-I`$.
3. The pulled-back flat bundle has holonomy $`\tau(-I)`$ around the core. Since $`-I`$ is central, Schur's lemma makes this $`\pm\mathrm{id}`$.
4. A flat bundle over $`M`$ is determined by its holonomy around the core, and $`\mathcal L_M`$ has holonomy $`-1`$ there because $`M`$ is a Möbius band. ∎

**The sectors.** The integer-spin irreducibles 1, 3, 3′, 4 and 5 have $`\tau(-I) = +\mathrm{id}`$. The spinorial irreducibles 2, 2′, 4′ and 6 have $`\tau(-I) = -\mathrm{id}`$.

**Consequences.**
- **The reach depends on the sampler.** The framework adopts the transverse one, normalized at unit radius (§XI, 1d).
  - *Plain restriction*, the field's value on the band, lands in $`E_\tau\vert_M`$. So the spinorial sectors reach the twisted sector, where $`\sin(y/R)`$ lives, and the integer-spin sectors reach the untwisted one.
  - *The transverse sampler* $`\partial_\nu`$ adds a factor $`\nu^* \cong \mathcal L_M`$, since $`M`$ is one-sided in $`\mathbb{RP}^3`$. That reverses the assignment.
  - The sampler reading's "transverse, not restrictive" holds for bands that lift to $`S^3`$, where the pullback is canonically trivial. On this placement the band does not lift, and plain restriction carries the twist for the spinorial sectors.
- **The linear readout.** [Condition 2's theorem](scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go) is built on the transverse sampler: every sampled state is a section of $`\mathcal L \otimes f^*E_\tau`$, and the theorem derives the sign it needs, $`-1`$ in every block's group, from the anti-periodic condition. For bands in $`S^3`$ the pullback is canonically trivial, so every block's fiber is $`V_\tau \otimes \mathcal L`$, and the theorem's table gives the trivial sector the fiber $`\mathcal L`$ itself, the one the $`\Lambda_\text{top}`$ row reads. On this placement the pullback is not trivial (Lemma 1), and each natural sampler twists one statistics class only.
  - The transverse sampler still produces sections of $`\mathcal L \otimes f^*E_\tau`$. The integer-spin blocks, the trivial one included, are twisted, as the table has them. The spinorial blocks are untwisted, since $`\mathcal L \otimes f^*E_\tau \cong V_\tau`$, so through this sampler they do not reach the twisted first mode, and their sign comes from $`\tau(-I) = -\mathrm{id}`$ through the quotient reading that condition 2's theorem adopts, instead.
  - Plain restriction produces sections of $`f^*E_\tau`$, not of $`\mathcal L \otimes f^*E_\tau`$. The spinorial blocks are twisted, and there the theorem holds: their anti-periodic sign is supplied by $`\tau(-I) = -\mathrm{id}`$, the holonomy of $`f^*E_\tau`$ around the core (Lemma 1). The integer-spin blocks are untwisted. The real trivial block then has a fixed vector, so it loses the ground for evenness, which Theorem A no longer needs. The scaling law says which block reads the $`\Lambda_\text{top}`$ row in two ways, which agree wherever the trivial block's output is twisted, through the transverse sampler on a one-sided band, in $`S^3`$, the setting the theorem was built for, or on this placement: its table gives the row the trivial block's fiber, $`\mathcal L`$ itself, and its uniformity audit gives it the surface mode $`u_0`$. Under plain restriction they split. If the row is read through the trivial block, that block is untwisted, and Theorem A, stated over nonnegative invariants, still covers it; if it is read through the twisted mode, the spinorial blocks carry it and the theorem holds. Which applies is cost 6's open dictionary. Under Friedrichs the row's value moves in neither case: the audit records it as "an exact same-mode identity", the eigenvalue $`2/R^2`$, and the untwisted problem has that level too, through $`\phi_0 u_0`$. Under bridging with the same matching an untwisted reading would not supply $`2/R^2`$, since below the critical width that problem has no level there ([The First-Positive Transfer Run](first-positive-transfer.md#iii-the-same-cone-trace-matching), §III); 1e adopts Friedrichs.
- **What the choice moves.** Under the Friedrichs extension the sampler choice decides the bookkeeping above and moves no level and no intensity profile. The untwisted problem, like the twisted one, is the Neumann problem on the lune: in the coordinates of first eigenvalue Proposition 4.2 an untwisted section is continuous across the seam's image, and the Friedrichs data at the two vertices are independent, so the identification $`N \sim S`$, where the twist sits, enters neither problem. The pillar says the same of its own operator: "the Friedrichs realization is spectrally an orientable object, a Neumann lune" (first eigenvalue §7). With $`u_0 = \sin(y/R)`$ and $`\phi_0`$ the pillar's zero mode, $`+1`$ before the cone and $`-1`$ beyond, the untwisted $`2/R^2`$ mode is $`\phi_0 u_0`$. It has the same intensity $`\sin^2(\pi\Theta)`$ and differs from $`u_0`$ only by the sign flip across the antinode (checked in `scripts/projective-carrier/identities.py`). Under bridging the answer depends on the extension declared for the untwisted sector. With the same cone-trace matching as the twisted sector, $`\phi_0 u_0`$, which jumps at the cone, leaves the domain, and below the critical width the untwisted problem then has no level at $`2/R^2`$ for any $`\delta_0`$ ([The First-Positive Transfer Run](first-positive-transfer.md#iii-the-same-cone-trace-matching), §III). With the $`\phi_0`$-transformed rule instead, the two sectors stay isospectral.
- **Route 1.** Its two walls stand: $`S^3/2I`$ is orientable, and $`2I`$ is perfect, with no order-two character. No character is constructed here; the relation runs through the inclusion $`\{\pm I\} \subset 2I`$. Route 1's closing clause, "the band's $`\mathbb{Z}_2`$ cannot be a $`2I`$-equivariant datum", holds for bands whose core maps trivially to $`2I`$, as every band in $`S^3`$ does. On this placement the core maps to $`-I`$, and in the spinorial sectors the band's $`\mathbb{Z}_2`$ is the central element's value.
- **The sampler test is intact.** Its class is compact embedded surfaces in $`S^3`$ with one boundary circle. The conic carrier's preimage in $`S^3`$ is the double lune, two lunes meeting only at $`N`$ and $`-N`$. That is not an embedded surface, and its boundary is two great circles that cross there (§VII). A smooth band on this placement, such as a tube of §III, has an annulus as its preimage, with two boundary circles. Neither is in the class.
- **Fence.** This makes the spin sign geometric on the carrier. It does not derive spin-statistics or the anticommutation of fermions. The framework's spin-statistics divide stays where [Edges sort spin](../../../README.md#edges-sort-spin) puts it: the representation split under the central $`-I`$. It also leaves the grid assignment open. Both grids use the same intensity readout, blind to the central sign, and which observable reads on which grid stays a motivated assignment (the bridge's dated note of 2026-09-25 under [A sampler reading](postulate-bridge.md#a-sampler-reading)).

## III. Theorem 2: the Friedrichs bottom lies below $`2/R^2`$

**Theorem 2 (DERIVED).** Let $`M \subset \mathbb{RP}^3(R)`$ be a compact Möbius band whose core represents the generator of $`\pi_1(\mathbb{RP}^3)`$. Suppose $`M`$ is smooth except at finitely many points, each a corner of its edge or a conic point such as $`p_c`$, and that its edge has at least one smooth point. Let $`\lambda_0(M)`$ be the bottom of the Friedrichs realization of the Laplacian of its induced metric on sections of $`\mathcal L_M`$, with the Neumann condition. Then

```math
\lambda_0(M) < \frac{2}{R^2}.
```

*Proof.*
1. The preimage $`\widetilde M \subset S^3(R)`$ is connected, because the core is nontrivial. A Möbius band has only one connected double cover, so $`\widetilde M`$ is the orientation double cover. Sections of $`\mathcal L_M`$ are the functions on $`\widetilde M`$ that are odd under $`-I`$.
2. The four coordinates $`x_0, \dots, x_3`$ of $`\mathbb R^4`$ are odd, so their restrictions are sections of $`\mathcal L_M`$. They are smooth, and corners and conic points have zero capacity (the logarithmic cutoff of first eigenvalue Lemma 4.1), so the restrictions lie in the Friedrichs form domain. Near each such point the band is a finite union of sectors, so the realization has compact resolvent, as for $`M(W)`$ (first eigenvalue Proposition 3.7), and its bottom is an eigenvalue.
3. On any surface in $`S^3(R)`$, $`\sum_i x_i^2 = R^2`$, and $`\sum_i \lvert\nabla x_i\rvert^2 = 2`$, the trace of the projection onto the tangent plane.
4. So $`\sum_i q(x_i) = 2\,\mathrm{Area}(M)`$ and $`\sum_i \lVert x_i\rVert^2 = R^2\,\mathrm{Area}(M)`$, where $`q`$ is the Dirichlet form. Since $`q(x_i) \ge \lambda_0 \lVert x_i\rVert^2`$ for each $`i`$, summing gives $`\lambda_0 \le 2/R^2`$.
5. Suppose $`\lambda_0 = 2/R^2`$. Then $`q(x_i) = \lambda_0 \lVert x_i\rVert^2`$ for every $`i`$, so every restriction $`x_i`$, the zero section included, lies in the bottom eigenspace. At a smooth point of the edge each $`x_i`$ is smooth up to the boundary, so it satisfies the Neumann condition there: $`\langle \nabla x_i, n\rangle = \langle e_i, n\rangle = 0`$ for the unit conormal $`n`$.
6. But $`\sum_i \langle e_i, n\rangle^2 = \lvert n\rvert^2 = 1`$ at that point, a contradiction. ∎

**Corollary 2.1 (DERIVED).** Under the hypotheses of Theorem 2, suppose $`M`$'s smooth locus is connected and the Friedrichs realization has $`2/R^2`$ as its first positive level. Then its bottom is $`0`$, carried by a section that is parallel on the smooth locus. So the smooth locus contains no orientation-reversing loop: it is orientable, and the twist passes through a singular point, as it does through $`p_c`$. In particular, for a band whose only singular points are corners of its edge, the Friedrichs realization never has $`2/R^2`$ as its first positive level.

*Proof.* The realization is nonnegative with compact resolvent. A positive bottom would be the first positive level, below $`2/R^2`$ by Theorem 2, so the bottom is $`0`$, an eigenvalue. A section with zero energy has $`\nabla\psi = 0`$ on the smooth locus, so it is parallel there. Being nonzero on the connected smooth locus, it trivializes $`\mathcal L`$ there. Every loop in the smooth locus then has trivial holonomy, while an orientation-reversing loop has holonomy $`-1`$. A band whose only singular points are corners of its edge contains its core in its smooth locus. ∎

**Scope.**
- The theorem covers bands on the projective placement. For a band in $`S^3`$ the coordinates are ordinary functions, not sections of $`\mathcal L`$, so the literal $`S^3`$ reading is untouched.
- The special case of domains in the round $`\mathbb{RP}^2(R)`$ uses the three coordinates of the covering $`S^2`$ in the same way.
- For a band whose only singular points are corners of its edge, the Friedrichs realization's bottom is also its first positive level: a nontrivial flat line bundle has no parallel section, so the bottom is positive.
- The conic band is covered: its Friedrichs bottom is $`0`$, and bridging's is negative ([first eigenvalue](../../bedrock/files/first-eigenvalue.md) Theorem 1.1). It keeps $`2/R^2`$ as its first positive level, so an exact $`2/R^2`$ on the conic band carries the first-positive selection with it.

**Evidence alongside it.** The canonical smooth family is the tube of half-width $`W`$ around a projective line (first eigenvalue §7). By Theorem 2 its first twisted level sits below $`2/R^2`$ at every width. At the sampled widths:

| $`W/R`$ | 0.25 | 0.50 | 1.00 | 1.40 | 1.50 |
|---|---|---|---|---|---|
| $`\lambda_0 R^2`$ | 1.0212 | 1.0891 | 1.4331 | 1.9155 | 1.9850 |

The sampled levels rise toward $`2/R^2`$ as the tube fills $`\mathbb{RP}^2`$ and its edge, of length $`2\pi R\cos(W/R)`$, shrinks to a point. They are computed by shooting (`scripts/projective-carrier/smooth_band.py`). The levels with wavenumbers $`k = \pm 1`$ along the core are degenerate at every width, since the radial problem depends only on $`k^2`$; at each sampled width that pair is the first level.

## IV. Proposition 3: no zero-bending band has a smooth geodesic edge

**Proposition 3 (DERIVED).** Let $`M`$ be a compact Möbius band that is a closed region of the round $`\mathbb{RP}^2(R)`$, with a piecewise-smooth edge whose only singular points are corners and two-sector pinches such as $`p_c`$. Then $`M`$ cannot have a smooth closed geodesic edge. If its edge is geodesic away from finitely many points, the turning at those points sums to $`-\mathrm{Area}(M)/R^2 < 0`$.

*Proof.*
1. Separate each pinch into its two sectors. The resolved surface is a region of $`\mathbb{RP}^2`$ with a piecewise-smooth boundary, and its Euler characteristic exceeds $`\chi(M) = 0`$ by one per pinch.
2. Apply Gauss-Bonnet with corners to the resolved surface, counting each pass of the edge through a pinch as a turning of its resolved corner's exterior angle minus $`\pi`$. This gives $`\int_M K\,dA + \int_{\partial M} k_g\,ds + \sum \text{turning} = 2\pi\chi(M) = 0`$, with $`K = 1/R^2`$.
3. With $`k_g = 0`$ along the geodesic arcs, the turning sums to $`-\mathrm{Area}(M)/R^2`$.
4. A smooth closed geodesic edge has no turning, which would force $`\mathrm{Area}(M) = 0`$. ∎

**Scope.**
- It covers zero-bending bands, those lying in $`\mathbb{RP}^2`$.
- The tubes of §III show the balance: their edge has geodesic curvature of magnitude $`\tan(W/R)/R`$ (first eigenvalue §7), and its integral over the edge equals the area over $`R^2`$.
- A band in $`\mathbb{RP}^3`$ that is not totally geodesic has $`K = 1/R^2 + \det A`$, which can be nonpositive; there Gauss-Bonnet forbids nothing.
- The geodesic edge comes from the regime that the Tier 2 ground floor registered for its first computation on 2026-07-13, a great-circle boundary in $`S^3`$ ([Tier 2 run](tier2-fixed-boundary.md)). It is inherited from that computation, not a framework requirement. On a zero-bending band only arcs can meet it.
- It excludes smooth geodesic edges, not geodesic arcs. Corners can balance Gauss-Bonnet: $`\mathbb{RP}^2`$ minus a convex geodesic polygon is a Möbius band whose edge is geodesic except at reflex corners, where the band's interior angle exceeds $`\pi`$. So a zero-bending band with a geodesic edge has corners; the conic band's are at $`p_c`$. For $`M(W)`$ the turning is $`-2W/R`$ at each of the edge's two passes through $`p_c`$, against $`\mathrm{Area}/R^2 = 4W/R`$. The need for a singular point comes from Corollary 2.1, not from this proposition.

**Proposition 3.1 (DERIVED).** Let $`M`$ be a compact Möbius band that is a closed region of the round $`\mathbb{RP}^2(R)`$, with a piecewise-smooth edge, whose only singular points are corners of its edge and one pinch $`p`$ formed by collapsing a transverse fibre, as $`p_c`$ is, and whose core, which passes through $`p`$, represents the generator of $`\pi_1(\mathbb{RP}^2)`$. For a pinched region that last condition is what makes it a Möbius band in the ambient sense: its preimage in $`S^2(R)`$ is connected. Then its edge has length at least $`2\pi R`$, with equality exactly when $`M`$ is a conic band $`M(W)`$, $`0 < W < \pi R/2`$, pinched at $`p`$.

*Proof.*
1. The edge passes $`p`$ twice, once at each end of the collapsed fibre, and splits there into two loops based at $`p`$.
2. Each loop is homotopic in $`M`$, with its ends held at $`p`$, to the core traversed once: in the band's rectangle, shrink the transverse coordinate to zero, and the ends stay on the collapsed fibre, which is $`p`$. So each loop represents the generator of $`\pi_1(\mathbb{RP}^2)`$ and is non-contractible there.
3. A non-contractible loop in $`\mathbb{RP}^2(R)`$ lifts to a path in $`S^2(R)`$ between antipodal points, so it has length at least $`\pi R`$, with equality only for a great semicircle, whose image is a projective line. So the edge has length at least $`2\pi R`$.
4. At equality each loop is a projective line through $`p`$. The two are distinct, since the closure of $`\mathbb{RP}^2`$ minus one line is all of $`\mathbb{RP}^2`$, which has no edge. Two lines through $`p`$ cut $`\mathbb{RP}^2`$ into two regions, the images of the two complementary double lunes on the covering $`S^2`$ with vertices over $`p`$, and $`M`$ is one of them. So $`M = M(W)`$, where $`2W/R < \pi`$ is the opening at $`p`$ of the lunes whose image it is; the other region is $`M(\pi R/2 - W)`$. Conversely, $`M(W)`$'s edge is two projective lines (Proposition 5), of total length $`2\pi R`$. ∎

**Scope.**
- It selects the family, not the member: every $`M(W)`$ has edge length $`2\pi R`$, so $`W`$ stays free (§V, cost 4).
- The pinch's type is a hypothesis. Under Corollary 2.1's hypotheses a band carries at most one fibre-collapse pinch, since two would cut the smooth locus into two pieces. Other singularities that could carry the twist are not covered.
- It needs zero bending. In $`\mathbb{RP}^3`$ the bound holds for the same reason, but equality does not force the unbent band: the bent bands of Proposition 0.3 have great-semicircle meridians, so their edges also have length $`2\pi R`$.
- Within its class, the requirement that the edge be geodesic away from the pinch is the requirement that it be as short as the class allows: a loop at $`p`$ that is geodesic away from $`p`$, non-contractible and simple is a projective line. The framework does not supply that length (§XI, 1b).

**Proposition 3.2 (DERIVED).** Let $`M`$ be as in Proposition 3.1, its $`\mathbb{RP}^2(R)`$ placed totally geodesically in $`\mathbb{RP}^3(R)`$, as the unbent carrier's is (§I), and suppose each of its edge's two loops is mapped onto itself by a deck transformation of the covering $`\mathbb{RP}^3 \to S^3/2I`$ other than the identity. Then each loop is a projective line, $`M`$ is a conic band $`M(W)`$ pinched where the two lines cross, and $`2W/R`$ is $`\theta`$ or $`\pi - \theta`$, with $`\theta`$ the angle between the two transformations' axes. So the bands that meet the hypothesis form a finite family, one for each pair of distinct icosahedral axes and choice of the angle the core bisects, up to symmetry.

*Proof.* As in Proposition 0.4's proof, write $`S^3(R)`$ as $`R`$ times the unit quaternions with $`2I`$ acting by left multiplication, and take the plane's lift to be the great sphere $`\Sigma`$ of purely imaginary quaternions.
1. A deck transformation other than the identity lifts to some $`g \in 2I`$ other than $`\pm 1`$, with axis $`a`$. Then $`\Sigma \cap g\Sigma = S^3 \cap \{1, g\}^\perp`$ (Proposition 0.4's proof, step 1), and since $`g`$ lies in the span of $`1`$ and $`a`$, this is the great circle $`G_a`$ of $`\Sigma`$ orthogonal to $`a`$.
2. The full lift of an edge loop to $`S^3(R)`$ lies in $`\Sigma`$. If the deck transformation maps the loop onto itself, $`g`$ maps that lift onto itself, so the lift lies in $`g\Sigma`$ too, hence in $`G_a`$. The loop represents the generator of $`\pi_1(\mathbb{RP}^2)`$ (Proposition 3.1's proof, step 2), so it is the whole projective line that $`G_a`$ covers.
3. Both loops are then projective lines through the pinch, so the edge has length $`2\pi R`$, and Proposition 3.1's equality case makes $`M`$ a conic band pinched where they cross. The lines are distinct, so the two axes are.
4. $`G_a`$ and $`G_b`$ cross at $`\pm(a \times b)/\lvert a \times b\rvert`$ at the angle $`\theta`$ between $`a`$ and $`b`$, and the lunes of $`M`$ open there by $`\theta`$ or by $`\pi - \theta`$. ∎

- **It selects nothing.** The hypothesis is a candidate rule for 1b and 1f, not adopted: no ground for it was located in the framework or in the literature searched. The principle of symmetric criticality (R. S. Palais, *The principle of symmetric criticality*, [Commun. Math. Phys. 69, 19–30 (1979)](https://doi.org/10.1007/BF01941322)) says that, under its hypotheses, a critical point of an invariant functional among the configurations a group fixes is a critical point outright. It does not say the carrier is such a configuration, and no nontrivial deck transformation keeps the two-loop edge. A loop kept by a nontrivial deck transformation covers an exceptional fibre, of multiplicity 2, 3 or 5, of a Seifert fibration of $`S^3/2I`$ ([the dictionary](s3-2i-oph-dictionary.md)): its lift through a point $`y`$ is $`y\,U(1)_{\bar y a y}`$, an orbit of right multiplication by a circle subgroup, which commutes with $`2I`$. Fibres of one such fibration are disjoint, and the two loops cross at the pinch.
- **What it would give.** Within Proposition 3.1's one-pinch class, whose retention is itself INFERRED (§XI, the ledger), the geodesic edge that 1b lacks would follow rather than be assumed, and the width and pose would reduce to the finite family. No member is picked, so its widths are not tabulated. One member has a second characterization: over all poses, the width at which the unbent carrier's image in the quotient first meets itself is largest at the pose of the narrower band of an adjacent three-fold and five-fold pair, where it is that band's own width ([The First Self-Intersection Width](self-intersection-width.md), Theorem 3). That grounds no rule either. Five-fold loops each cover a closed geodesic of the shortest class of $`S^3/2I`$ five times, two distinct ones; that is the class of the [Plato twist](plato-twist.md), but a loop's own holonomy is five turns of $`\pi/5`$, a half-turn, not the once-around twist that carries $`\cos(\pi/10)`$. The carrier's image in $`S^3/2I`$ meets itself along each loop, which the layer ruling allows (§XI, 1f).
- Checked in `scripts/projective-carrier/symmetric_edge.py`.

## V. The conic carrier: the leading realization

The conic band $`M(W)`$ of [first eigenvalue](../../bedrock/files/first-eigenvalue.md), placed as in §I with $`W < \pi R/2`$, keeps four things at once:
- the zero-bending projective geometry on its smooth locus;
- geodesic boundary arcs, its two meridians;
- the exact $`2/R^2`$ as its first positive twisted level (Theorem 1.2), common to Friedrichs and to bridging with $`\delta_0 > 2R/e`$;
- a simple first-positive eigenspace away from the critical width (Corollary 6.3), spanned by $`\sin(y/R)`$.

**The phase origin.** That eigenfunction has its node at the seam, $`\Theta = 0`$, and its maximum at the cone point, $`\Theta = 1/2`$. So the cone point fixes where $`\Theta = 0`$ sits. That holds for $`W < \pi R/2`$ strictly and for the extensions of Theorem 1.2. On the smooth tubes of §III the $`k = \pm 1`$ pair is degenerate at every width, and at each sampled width it is the first level, so its phase along the core is free. The simplicity is also what condition 1's reduction needs ([scaling law](scaling-law-uniqueness.md), Step C).

**Status.** Three requirements stand behind the carrier:
- zero bending, the premise of §I, adopted by the ruling;
- geodesic edge arcs, inherited from a computational regime rather than a framework requirement: Tier 2's first computation registered a great-circle boundary in $`S^3`$, a zero-bending band can meet that only with arcs (Proposition 3), and among zero-bending bands with one fibre-collapse pinch the requirement, taken as geodesic away from the pinch, is equivalent to the least edge length, $`2\pi R`$ (Proposition 3.1), and to a rigid tilt as the Friedrichs $`2/R^2`$ mode (Proposition 4.1); the projective figure-eight is a new setup, registered separately in §IX;
- the exact $`2/R^2`$ as the first positive level, the Λ page's seed.

Each forces something. Zero bending places the carrier in $`\mathbb{RP}^3`$ (Lemma 0). A geodesic edge on a zero-bending band has corners (Proposition 3). If the band's smooth locus is connected, the exact $`2/R^2`$ needs a singular point that the twist passes through, and it leaves the rest of the band orientable (Corollary 2.1). That holds for the Friedrichs realization. On the core of functions smooth up to the corner, a convex corner adds no extension parameter to it. At a reflex corner the first nonconstant Neumann sector has index $`\pi/\theta < 1`$ and is limit-circle, so the realization has other self-adjoint extensions, and taking Friedrichs there is a convention of this page's arguments. At a two-sector pinch such as $`p_c`$ the freedom left is the combination odd across the pinch, which is the pillar's choice between Friedrichs and bridging (§XI, 1e). Under the Friedrichs realization the exact $`2/R^2`$ does not force the arcs to be geodesic: near every $`M(W)`$, suitably chosen moves of one lap off its line within $`\mathbb{RP}^2`$, on an arc away from $`p_c`$, keep it exactly (Proposition 4.2). The conic band meets all three with one point, $`p_c`$, which is both its edge's corner and the pinch its twist passes through. It is the leading explicit realization presently known that simultaneously retains the projective zero-bending geometry on its smooth locus, geodesic boundary arcs, and the exact $`2/R^2`$ twisted first-positive level. It is not shown unique: $`W`$ stays free below $`\pi R/2`$, and nothing excludes other singular bands. So the necessary features are derived conditional on the requirements, and $`M(W)`$ is the leading realization of them, not uniquely selected.

**Named inputs.** These are the conic carrier's costs; item 6 is the placement's:
1. **The first-positive selection.** The bottom is $`0`$ for Friedrichs and negative for bridging, so the framework selects the first positive level.
2. **The cone condition.** $`2/R^2`$ is the first positive level for Friedrichs, or for bridging with $`\delta_0 > 2R/e`$. "The covering geometry constrains, but does not by itself fix, the extension" (first eigenvalue §3.5): it forces the regular branch in the symmetric subsector, where $`\sin(y/R)`$ lives, and leaves the antisymmetric subsector's condition free.
3. **The width.** $`W < \pi R/2`$, strictly. At the critical width the first positive level is doubly degenerate (Corollary 6.3), the pinning fails, and the double lune closes up.
4. **$`W`$ is otherwise free.**
5. **The continuation rule at the vertex.** Friedrichs imposes independent conditions at the two lune vertices; bridging matches them, encoding $`N \sim S`$ (Remark 2.1). The edge passes through $`p_c`$ twice (§VII), so the rule also bears on the edge.
6. **The sampler, under bridging.** On this placement each natural sampler twists one statistics class only, and under bridging that can move the untwisted class's $`2/R^2`$ level, depending on the extension declared for that sector (§II). Whether any observable is read through that class depends on the dictionary from observables to blocks, not yet settled, since the cosmological grid assignment has no representation-theoretic ground ([The Sampling Grids](../../../README.md#the-sampling-grids)). One sampler serves every block (§XI, 1d).

Since 1e (§XI), item 2 is fixed at Friedrichs, and so is item 5's rule for the surface operator; item 5's bearing on the edge is settled by 1g: time runs on the abstract circle, which needs no continuation rule at $`p_c`$. Item 6's case, bridging in the untwisted class, does not arise.

## VI. Lemma 4: the $`2/R^2`$ mode is the band's tilt

**Lemma 4 (DERIVED; a forced identity).** The conic band lies in the totally geodesic $`\mathbb{RP}^2`$, so its second fundamental form vanishes on the smooth locus. With $`\mathrm{Ric}(\nu,\nu) = 2/R^2`$, the area Jacobi operator is

```math
J = -\Delta_{\mathcal L} - \frac{2}{R^2}.
```

The band's $`2/R^2`$ mode, $`u_0 = \sin(y/R)`$, is its rigid tilt:
- Under the trivialization of first eigenvalue Proposition 4.2, $`u_0`$ becomes $`x_p/R`$ on the lune, where $`x_p`$ is the coordinate along the pole $`p = N`$. Its lift to the double lune is $`x_p/R`$, odd under $`-I`$.
- Along the great sphere, the rotation field of $`S^3`$ in the plane of $`p`$ and the normal $`\nu`$ is $`x_p\,\nu = R\,u_0\,\nu`$, purely normal. The rotation is a Killing field, and it tilts the great sphere about its equator. Along a minimal surface the normal part of a Killing field is a Jacobi field, so $`J u_0 = 0`$, which is the same statement as $`-\Delta_{\mathcal L} u_0 = (2/R^2)\,u_0`$.
- The field descends to $`\mathbb{RP}^3`$: it is linear in $`x`$, so it commutes with $`-I`$.

**Scope.**
- **When it is the first positive mode.** $`u_0`$ is the band's first positive mode, and a simple one, for $`W < \pi R/2`$ under Friedrichs or bridging with $`\delta_0 > 2R/e`$ (§V). For bridging with $`\delta_0 < 2R/e`$ an antisymmetric constant-sector level lies below $`2/R^2`$ (first eigenvalue §4.4). At $`\delta_0 = 2R/e`$ that level reaches $`2/R^2`$, which is then doubly degenerate within the constant sector. At $`W = \pi R/2`$ the transverse branch also reaches $`2/R^2`$ (Corollary 6.3); where the two thresholds coincide the eigenspace is three-dimensional.
- **The picture.** The $`2/R^2`$ mode is the rigid tilt of the band: the seam's equator arc stays fixed, and the cone point, the antinode, moves most.
- **Not the arch.** The identity is a statement about one operator: $`u_0`$ is a Jacobi field of the band's own area Hessian. The arch matched two operators' spectra, the surface eigenvalue against the ambient Ricci floor. The two part ways as the ambient dimension grows with the surface kept two-dimensional. For a great $`S^2`$ in $`S^n(R)`$ the Jacobi curvature term is the sum over the two tangent directions, $`2/R^2`$, in every $`n`$, so the tilt identity holds in every dimension. The ambient Ricci floor is $`(n-1)/R^2`$ and meets $`2/R^2`$ only at $`n = 3`$, the coincidence the bridge records as special to dimension three. The arch stays dead.
- **Not a second derivation.** The Killing field forces the identity, so it gives the mode a geometric meaning without deriving $`2/R^2`$ again.
- **The whole eigenspace.** On the narrow band every first positive mode is a rigid tilt. The normal parts of the ambient Killing fields along the great sphere are its three coordinate functions $`x_p`$, $`x_c`$ and $`x_d`$, and all three solve the $`2/R^2`$ equation. The Neumann arcs admit $`x_p`$ at every width, $`x_d = R\lvert\cos(y/R)\rvert\sin(w/R)`$ only at $`W = \pi R/2`$, where it is Corollary 6.3's second mode, and $`x_c`$ never. This is Theorem 1.2 and Corollary 6.3 in geometric language, not a new result. Tilts are normal fields, sections of the orientation line, so the statement is the twisted class's; the untwisted mode $`\phi_0 u_0`$ is the tilt's $`\phi_0`$-image, not a rigid motion.
- **The boundary distinction.** $`J`$ is the pillar's operator shifted by $`2/R^2`$ only as a differential expression. The pillar imposes Neumann conditions on its arcs, while fixed-edge area variations are Dirichlet. $`u_0`$ does not vanish on the arcs, so it is a moving-edge mode, a rigid isometry, and not admissible in the fixed-edge problem.
- **Area, not bending energy.** $`J`$ is the second variation of area. A bending energy of Willmore type has a fourth-order Hessian, a different object.

The identities are checked in `scripts/projective-carrier/identities.py`.

**Proposition 4.1 (DERIVED; Lemma 4's converse).** Let $`M`$ be a band in Proposition 3's class, a closed region of the round $`\mathbb{RP}^2(R)`$ with a piecewise-smooth edge whose only singular points are corners and two-sector pinches, with a connected smooth locus. Let $`e`$ be a unit vector of the three-space that holds the band's great sphere. If the tilt $`x_e = \langle x, e\rangle`$ is an eigensection of the Friedrichs realization on $`M`$, then $`M`$ is a conic band $`M(W)`$, for some $`0 < W < \pi R/2`$, with its pinch at $`[e]`$, and the eigenvalue is $`2/R^2`$. Conversely, on $`M(W)`$ the tilt $`x_p`$, with $`p`$ a lift of the pinch, is the $`2/R^2`$ mode (Lemma 4).

*Proof.* On [The Projective Carrier: Supporting Proofs](carrier-proofs.md#proposition-41).

- It needs no width bound and no pinch among its hypotheses: the pinch, and the laps' being lines, are its output. Within Proposition 3.1's class, then, three conditions coincide: laps geodesic away from the pinch, the least edge length $`2\pi R`$ (Proposition 3.1), and a rigid tilt as the Friedrichs $`2/R^2`$ mode.

**Proposition 4.2 (DERIVED; the seed does not force the laps).** Fix $`0 < W < \pi R/2`$, so that $`2/R^2`$ is $`M(W)`$'s simple first positive level (§V). Take the lune $`L`$ between two meridians through $`N`$, a lift of $`p_c`$, as $`M(W)`$'s fundamental domain on its great sphere, with $`s`$ the distance from $`N`$ and $`\phi`$ the longitude, $`\lvert\phi\rvert \le W/R`$. For a smooth profile $`V`$ supported in a closed interval $`J \subset (0, \pi R)`$, let $`M_V`$ be the band with fundamental domain

```math
D_V = \Big\{-\frac{W}{R} \le \phi \le \frac{W}{R} + \frac{V(s)}{R\sin(s/R)}\Big\},
```

one lap moved off its line within $`\mathbb{RP}^2`$ by $`V`$ along the normal, to first order, and the band unchanged near $`p_c`$. For small $`V`$, $`M_V`$ is in Proposition 3.1's class. Let $`\lambda(V)`$ be the first positive level of its Friedrichs realization. Then:
1. $`\lambda(0) = 2/R^2`$; near $`0`$, $`\lambda`$ is analytic along every finite-dimensional family of profiles, and

```math
\lambda'(0)[V] = \frac{3}{4WR^3}\int_0^{\pi R}\Big(\sin^2\frac{s}{R} - 2\cos^2\frac{s}{R}\Big)V(s)\,ds.
```

2. Take $`b`$ supported in $`J`$ with $`\lambda'(0)[b] \neq 0`$; one exists, since the density vanishes at only two points. For every profile $`a`$ supported in $`J`$ there is an analytic $`\tau(t)`$, $`\tau(0) = 0`$, with $`\lambda\big(ta + \tau(t)\,b\big) = 2/R^2`$ for small $`t`$.
3. If $`a`$ is not a multiple of $`b`$, then for small $`t \neq 0`$ the band $`M_{ta + \tau(t)b}`$ keeps the exact $`2/R^2`$ as a simple first positive level, its moved lap is not a geodesic arc, and its $`2/R^2`$ mode is not a rigid tilt.

So under the Friedrichs realization the exact $`2/R^2`$, kept as the first positive level, forces a singular point that carries the twist (Corollary 2.1) but not geodesic laps.

*Proof.* On [The Projective Carrier: Supporting Proofs](carrier-proofs.md#proposition-42), with the remark on Hadamard's formula that followed it here.

- The bands of 3 keep $`2/R^2`$ and the pinch, and their moved lap is curved, so the third of §V's requirements does not imply the second. Within Proposition 3.1's class the second is equivalent to a rigid tilt as the Friedrichs $`2/R^2`$ mode (Proposition 4.1).
- `scripts/projective-carrier/seed_laps.py` illustrates 1 to 3 by quadratic finite elements, at $`W/R = 0.3`$, $`0.6`$ and $`1.0`$, on the smooth profiles $`b_\text{mid}(s) = \beta\big((s/R - \pi/2)/0.5\big)`$ and $`b_\text{tip}(s) = \beta\big((s/R - 0.6)/0.35\big)`$, $`\beta(x) = e^{1 - 1/(1 - x^2)}`$ on $`\lvert x\rvert < 1`$. The first variations match 1's formula to $`2\times10^{-6}`$ relative. For $`t = 0.025R`$, $`0.05R`$ and $`0.1R`$ a root $`\tau(t)`$ of $`\lambda(tb_\text{mid} + \tau b_\text{tip}) = 2/R^2`$ is bracketed by a sign change at least ten times the error. At each root the level is simple with the next at least $`1/R^2`$ above it, the moved lap is curved, with geodesic curvature at least $`0.5/R`$ somewhere, and the mode lies at a relative $`L^2`$ distance of at least $`10^{-4}`$ from every tilt. The record's table gives the values: the next level at least $`1.84/R^2`$ above, the largest geodesic curvature between $`4.8/R`$ and $`15.7/R`$, and the distance at least $`3.7\times10^{-3}`$.

## VII. Proposition 5: the edge's lift

Three objects are kept distinct:
1. the abstract boundary $`\partial M \cong S^1`$;
2. its metric image, the figure-eight through $`p_c`$ (first eigenvalue §2);
3. its lift to the great $`S^2 \subset S^3`$.

**Coordinates.** Write the band as the rectangle $`[0, \pi R] \times [-W, W]`$ with the seam $`(0, w) \sim (\pi R, -w)`$. Following first eigenvalue Proposition 4.2's trivialization, map it isometrically onto the lune $`L`$, by latitude and longitude about the poles $`N`$ and $`S = -N`$:
- for $`y \le \pi R/2`$, the point $`(y, w)`$ goes to latitude $`y/R`$ and longitude $`w/R`$;
- for $`y \ge \pi R/2`$, it goes to latitude $`-(\pi R - y)/R`$ and longitude $`-w/R`$.

The seam lands on the equator arc of $`L`$. The collapsed fiber $`y = \pi R/2`$ lands on $`N`$ from one side and on $`S`$ from the other.

**The traversal.** The oriented boundary runs along $`w = +W`$ for $`y`$ from $`0`$ to $`\pi R`$, crosses the seam, and runs along $`w = -W`$ the same way, passing $`p_c`$ once on each arc. Over the carrier's smooth locus, which is simply connected, the cover $`S^3 \to \mathbb{RP}^3`$ is trivial, and $`L`$ and $`-L`$ are its two sheets. Their closures meet only at $`N`$ and $`-N`$, over the cone point, where each local sheet of the cover holds a tip of $`L`$ and a tip of $`-L`$. So the continuous lift passes from $`L`$ to $`-L`$ at each pole, following the preimage of the next half-cone, and the cover's monodromy around the core runs entirely through the cone point:

| Stretch | Lift, on the great $`S^2`$ | Piece |
|---|---|---|
| $`w = +W`$, $`0 \le y \le \pi R/2`$ | longitude $`W/R`$, equator to $`N`$ | $`L`$ |
| $`w = +W`$, $`\pi R/2 \le y \le \pi R`$ | longitude $`\pi - W/R`$, $`N`$ to equator | $`-L`$ |
| $`w = -W`$, $`0 \le y \le \pi R/2`$ | longitude $`\pi - W/R`$, equator to $`S`$ | $`-L`$ |
| $`w = -W`$, $`\pi R/2 \le y \le \pi R`$ | longitude $`W/R`$, $`S`$ to equator | $`L`$ |

**Proposition 5 (DERIVED).** The continuous lift of the oriented edge closes after one traversal. It is the boundary of the lune between longitudes $`W/R`$ and $`\pi - W/R`$, one of the two lunes complementary to the double lune, with corners at $`N`$ and $`-N`$. It passes $`N`$ once and $`-N`$ once, passing from $`L`$ to $`-L`$ at $`N`$ and back at $`-N`$. The edge's two visits to the antinode $`p_c`$ therefore lift to $`p_c`$'s two spin-cover preimages, $`N`$ and $`-N`$. The full preimage of $`\partial M`$ is this curve together with its image under $`-I`$: the two great circles through $`N`$ and $`S`$ that bound the double lune.

The traversal is traced numerically in `scripts/projective-carrier/lift_trace.py`.

**The reading allowed.** The antinode $`p_c`$ is one point of the carrier with two spin-cover preimages, $`N`$ and $`-N`$, and the edge's lift passes each once. A spinorial field takes opposite signs there, since $`\widetilde\Psi(-N) = \tau(-I)\widetilde\Psi(N) = -\widetilde\Psi(N)`$, and the intensity does not tell them apart.

**For the axiom.** On this placement the postulate as first written, $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$, holds only as a split.
- In $`\mathbb{RP}^3`$ the edge is the carrier's boundary, so $`S^1 = \partial M`$ holds there. Its metric image is the figure-eight through $`p_c`$.
- In $`S^3`$ the edge's lift is an embedded circle with two corners, so $`\hookrightarrow S^3`$ holds for the lift. That circle bounds the complementary lune, a disk. It is not the boundary of the carrier's lift, the double lune, whose boundary is the two great circles.
- The framework's language about built structure leaves a route to the split. Its postulate reads "time is the boundary of a non-orientable surface embedded in a closed three-space", and of the structure built on the smooth sphere it says "The twists and identifications live in that built structure" ([framework](../../../README.md)). Its placement prose pointed the other way, and the displayed formula named $`S^3`$, until 2026-09-28 (§X).
- On this path the non-orientability the postulate names is confined to a point. With the exact $`2/R^2`$, the rest of the carrier is orientable (Corollary 2.1), and the Friedrichs spectrum does not see the twist (§II). Whether a band in $`S^3`$ keeps $`2/R^2`$ with a non-orientable smooth locus lies outside Theorem 2; it was part of what reading (B) had to answer, and the ruling set (B) aside (§XI). The bent band of Proposition 0.2 keeps $`2/R^2`$ in $`S^3`$, since its spectrum is $`M(W)`$'s, but it is two-sided there: the non-orientability the postulate names survives only as the pillar's label at $`p_c`$.
- The ruling adopted the premise, which decides the geometric half of this: the carrier does not lie in $`S^3`$, and it is realized through the projective layer (Lemma 0). The ruling does not read the formula's shorthand as having derived $`\mathbb{RP}^3`$; it takes the projective layer as the consistent realization of the postulate's intended geometry. On 2026-09-28 the formula was rewritten to put the arrow on the band (§XI, 1a); the reach of the anti-periodic condition was decided with 1d (2026-09-29): it governs the integer-spin blocks, the trivial one included, and the spinorial blocks read the untwisted problem.

**Which edge is time.** The framework's temporal edge is the boundary circle, which traverses the strip twice ([Temporal Edge](../../../README.md#temporal-edge)), and the [Waltz](../../../../spectrum/files/the-waltz.md) reads masslessness as propagation along it. On this carrier the abstract boundary is still that circle, and its two laps are the two arcs, each of length $`\pi R`$. Its metric image passes $`p_c`$ once per lap. If the temporal edge is the abstract circle, the clock and Waltz formulas stand as written. If propagation follows the metric image, the continuation rule at the vertex (§V, cost 5) enters the edge's dynamics. §XI decides it for the abstract circle (1g).

## VIII. Fences

> **The two phases are not one variable.** $`\Theta = y/(\pi R)`$ is the sampling position at which $`C(\Theta)`$, the wells, $`a_0`$, $`H_0`$ and $`\Lambda`$ are read. The temporal boundary parameter $`t`$ is the edge phase. They belong to different eigenproblems that share sinusoidal structure. The edge's metric image passing the cone twice never makes $`\Theta = 1/2`$ two moments when $`\Lambda`$ happens. Merging the two would turn the wells into epochs, and $`a_0(z) \propto H(z)`$ depends on the positions staying fixed at every epoch.

- The geometric sign is not the statistics (§II).
- $`u_0`$ extends into $`S^3`$ as a linear coordinate, with eigenvalue $`3/R^2`$, the same 3 as $`\Lambda_\text{ref}`$. That coincidence holds only in three dimensions, where a sphere's first level $`n/R^2`$ meets the de Sitter value $`n(n-1)/(2R^2)`$. It stays out of the vacuum argument.
- The Tier 2 run's result is narrower than a claim that no band in $`S^3`$ is stable. Every minimal Möbius band spanning the registered great circle is unstable, and no immersed Möbius band in $`S^3`$ is totally geodesic. Other boundary regimes and functionals were not excluded.

<a id="ix-fixed-edge-stability"></a>
## IX. Fixed-edge stability (derived; independent check reproduced)

*Registered 2026-09-27 and frozen in the header.* Fixed-edge stability of the conic carrier is derived below at every embedded width, for the declared class of variations. What is registered and not run is its independent check, recorded when run as a Result scored against these terms, as the [variational clock arm](variational-clock-arm.md) was.

**Terms.**
- **Ambient:** $`\mathbb{RP}^3(R)`$, the layer where the carrier's completion embeds (§XI, 1f). This section makes no claim about the widths at which the image stays embedded in $`S^3/2I`$.
- **Carrier:** the conic band $`M(W)`$, the leading candidate of §V, placed as in §I, at every embedded width $`0 < W < \pi R/2`$.
- **Functional:** area.
- **Boundary:** the band's own figure-eight edge, held fixed pointwise.
- **Admissible variations:** normal graphs over the fixed conic carrier, sections of $`\nu \cong \mathcal L`$ over its smooth locus with zero trace on the edge, completed in the Dirichlet form domain, with the smooth ones as a dense core. With the edge and the carrier's conic type held fixed, this is the full normal-graph class, with no symmetry restriction. It excludes deformations that resolve the cone or change how the band meets itself at $`p_c`$.
- **The cone.** Every Dirichlet transverse sector has a nonzero angular eigenvalue $`(m\pi/2W)^2`$, $`m \ge 1`$, the same set as the pillar's nonconstant Neumann sectors. The limit-point computation of first eigenvalue Lemma 3.3 is local at $`p_c`$ and depends only on that eigenvalue. So every sector is limit-point there for $`W \le \pi R/2`$, and no cone condition is chosen.
- **The twist does not enter.** The variations vanish at $`p_c`$, the one place the twist lives (Corollary 2.1), so the twisted and untwisted Dirichlet problems coincide here.

**Derivation (DERIVED).**
1. *Second variation.* For the normal-geodesic variation with speed $`\phi`$, and $`t`$ small enough that $`\cos(t\phi/R) > 0`$, the area element of the varied surface is exactly $`\cos(t\phi/R)\sqrt{\cos^2(t\phi/R) + t^2\lvert\nabla\phi\rvert^2}\,dA`$. Its first-order term vanishes, and its second-order term is $`(\lvert\nabla\phi\rvert^2 - (2/R^2)\phi^2)/2`$ pointwise, so no boundary or vertex term enters. The second variation is the form $`q_J[\phi] = \int_M (\lvert\nabla\phi\rvert^2 - (2/R^2)\phi^2)\,dA`$, which equals $`\langle J\phi, \phi\rangle`$ for $`\phi`$ in $`J`$'s domain (checked in `scripts/projective-carrier/identities.py`).
2. *Reduction.* Multiplication by $`\phi_0`$, the unitary of first eigenvalue Proposition 4.2, preserves the energy and zero trace on the arcs. So it carries the Dirichlet form domain onto that of the lune of opening $`2W/R`$, and $`q_J`$ becomes the lune's Dirichlet form shifted by $`-2/R^2`$. This restricts the Proposition's trivialization to Dirichlet data, an adaptation made direct by every sector being limit-point.
3. *Count.* The lune's Dirichlet spectrum is $`(\nu_m + \ell)(\nu_m + \ell + 1)/R^2`$ for $`m \ge 1`$ and $`\ell \ge 0`$, with $`\nu_m = m\alpha_0`$ and $`\alpha_0 = \pi R/(2W)`$, one mode per pair, increasing in both indices. Since $`\nu_1 = \alpha_0 > 1`$ at every embedded width, the lowest level $`\alpha_0(\alpha_0 + 1)/R^2`$ exceeds $`2/R^2`$. So $`J`$'s bottom is $`(\alpha_0 - 1)(\alpha_0 + 2)/R^2 > 0`$: index 0 and nullity 0. The ground state is $`\pm\lvert\cos(y/R)\rvert^{\alpha_0}\cos(\pi w/2W)`$ in band coordinates, the sign flipping across the cone.
4. *Contrast.* Under the pillar's Neumann condition instead, $`J`$'s Friedrichs bottom is $`-2/R^2`$, attained by $`\phi_0`$, which smooth variations approximate in form norm (first eigenvalue Lemma 4.1). So the stability rests on the fixed edge. The Neumann form is a contrast, not a boundary regime: for pure area an unconstrained boundary is not well posed (the Tier 2 ground floor).

**The independent check (registered, not run).**
- **Rederivation.** The runner derives step 2's reduction and the lune's Dirichlet spectrum without taking them from this page.
- **Cross-check.** $`P_1`$ finite elements in the band's own coordinates, so that the check sees the reduction rather than assuming it. The domain is the rectangle $`[0, \pi R] \times [-W, W]`$ with the anti-periodic seam $`(0, w) \sim (\pi R, -w)`$, the area weight $`\lvert\cos(y/R)\rvert`$, and zero data on the arcs and on the collapsed fiber. Nodes are graded toward the fiber, at distance $`(\pi R/2)(k/N)^2`$ on each side. The initial mesh has $`N = 16`$ per side and 8 cells across, followed by exactly four uniform refinements. The order $`p`$ is estimated from the last three levels, and the bottom is Richardson-extrapolated from the last two; the error estimate is $`\lvert\lambda_\text{extrap} - \lambda_\text{finest}\rvert`$. Widths: $`W/R \in \{1/4, 1/2, 1, 7/5, 3/2\}`$.
- **Tolerance.** The extrapolated bottom of $`-\Delta`$ must match $`\alpha_0(\alpha_0 + 1)/R^2`$ to a relative $`10^{-3}`$. At $`W/R = 3/2`$ that is an absolute $`2 \times 10^{-3}/R^2`$, well inside $`J`$'s bottom there, about $`0.14/R^2`$.
- **Outcomes.**
  - Reproduced: the rederivation agrees, and at all five widths the cross-check converges, with both its miss and its error estimate within the tolerance.
  - Contradicted: the rederivation disagrees, or at some width a converged bottom of $`-\Delta`$ misses $`\alpha_0(\alpha_0 + 1)/R^2`$ by more than both the tolerance and ten times its error estimate. $`J`$'s sign at that width is reported with it.
  - Unresolved: anything else, such as a nonpositive $`p`$, a failure to converge, an error estimate above the tolerance, or a miss no larger than ten times the error estimate, with no refinement added afterward. The derived result then stands on the page unverified.

**The independent check, run (2026-10-01): Reproduced.** It ran blind on OpenWave as M8.14, against the terms above byte for byte, and is scored in [The Fixed-Edge Stability Check](fixed-edge-check.md). Two blind rooms each derived the reduction to the lune by its own route, which agrees under the reading M8.14 declared before the run, and the lune's Dirichlet spectrum, without taking either from this page, and the cross-check matched $`\alpha_0(\alpha_0 + 1)/R^2`$ at all five widths, with a largest miss of $`3.0 \times 10^{-7}`$ relative and every error estimate inside the tolerance. Two steps of the rederivation were asserted rather than argued in both rooms, and the check cannot see the seam's twist, which the terms already say does not enter.

**Fences.**
- The width where $`J`$'s bottom reaches $`0`$, the pillar's mode crossing and the unbent carrier's loss of embedding in $`\mathbb{RP}^3`$ are one fact: the lune's opening $`2W/R`$ reaching $`\pi`$, where $`\alpha_0 = 1`$. They are not independent confirmations.
- This is a new instance of the registered fixed-boundary regime. Its edge is the band's own figure-eight in $`\mathbb{RP}^3`$, not the registered great circle in $`S^3`$, so it rescues nothing on the $`S^3`$ arm.
- Stability is local. Least area is a separate question. For $`W > \pi R/4`$ it fails among all Möbius bands with the edge fixed as parametrized: the complementary lune, mapped as a disc, spans the same edge (Proposition 5) with area $`2\pi R^2 - 4WR < 4WR`$, and a small cross-cap glued into it gives a Möbius band of nearly that area. That band's core is contractible, so it is no carrier on this placement, whose core generates $`\pi_1(\mathbb{RP}^3)`$ (§I); with the edge fixed only as a set, the complementary conic band $`M(\pi R/2 - W)`$, whose core generates, spans it with that area (Proposition 3.1). Among continuous finite-piecewise-smooth carrier-class competitors, with the core generating and the edge fixed as parametrized, $`M(W)`$ has the least area, and a competitor ties it only by covering it once (Proposition 7); the same holds among Lipschitz ones (Proposition 8). None of this changes the positive second variation or Proposition 6's local strictness.
- **When the result counts.** Under the clarified bar, "The postulate embedding must be a critical point of the independently motivated functional whose second variation is nonnegative on every admissible variation of the declared class", and "A restriction on the admissible variations counts only when the postulate motivates it and it is declared before the computation, never because it rescues a candidate." The stability here rests on holding the edge fixed pointwise (step 4). So it counts toward the bar only if the premise, the conic realization and the fixed temporal edge are adopted (§XI, 1b and 1c), each on grounds that stand without this result, and either the fixed edge is shown to force the conic type at $`p_c`$ or that restriction is grounded too. The ruling of 2026-09-27 adopted the premise, and with it the projective layer, on the postulate's intended geometry rather than on this result. The ruling of 2026-10-01 holds the boundary map fixed as an adopted modeling input, on no postulate-level ground, so the fixed edge does not meet this condition (§XI, 1c). With $`M(W)`$'s boundary map fixed, every competitor that changes the bowtie other than by covering it once has more area, locally among Lipschitz competitors (Proposition 6) and globally among Lipschitz carrier-class ones (Propositions 7 and 8), which meets the condition on the conic type in those classes. The conic realization stays open, and its second requirement has no ground yet (§V). A later ruling on it, or a postulate-level ground for the fixed edge, cannot be blind to this result, so its independence has to come from its grounds, not its timing. Until then this is an exact fixed-edge stability theorem, not vacuum stability.
- **A family, not a selected surface.** The bar admits nullity only from exact symmetries, and here there is none: no one-parameter symmetry fixes the edge, and changing $`W`$ moves the edge. But $`W`$ stays free (§V, cost 4), so the result is one stable band per width, and the bar claims a unique universal surface "only after a further mechanism selects the realized member".
- **The rest of the bar.** The result meets the stability clause only. The bar also asks that the functional be motivated independently of the target, couple to the $`2I`$-decorated ALE/gauge sector without an arbitrary new scale, and produce content beyond the existing exchange rate.

**The cone point.** The fence on when the result counts asks that the fixed edge be shown to force the conic type at $`p_c`$, or that the restriction to it be grounded. Proposition 6 gives the local area comparison that §IX's class leaves out: among competitors that re-map the band only near $`p_c`$, the bowtie has least area, and every genuine two-dimensional resolution or bending of it costs area.

**Proposition 6 (DERIVED).** Let $`D`$ be the strip $`\lvert y - \pi R/2\rvert \le \delta`$ of the band's rectangle about the collapsed fibre, and $`F`$ the unbent carrier's map, which carries $`D`$ onto the bowtie $`B`$ at $`p_c`$, two opposite sectors of the carrier's $`\mathbb{RP}^2`$ of radius $`\delta`$. Take $`\delta < \varepsilon < \pi R/2`$, and let $`f`$ be a Lipschitz map of $`D`$ into the open ball of radius $`\varepsilon`$ about $`p_c`$ with $`f = F`$ on $`\partial D`$. Then the area of $`f`$, counted with multiplicity, is at least that of $`B`$, with equality exactly when $`f`$ covers $`B`$ once: $`f_\#[D] = F_\#[D]`$, almost every point of $`B`$ has one preimage, and the image off $`B`$ has zero area. So a genuine two-dimensional resolution of the pinch, or a bending of a sector, changes the image current and has strictly more area, while a map that only reparametrizes the strip, or sends some of it onto curves, which carry no area, does not.

*Proof.* On [The Projective Carrier: Supporting Proofs](carrier-proofs.md#proposition-6), with the remark that the twist does not enter, which followed it here.

- It is local in both senses: $`f`$ re-maps only the band's strip about $`p_c`$, and keeps it within distance $`\varepsilon < \pi R/2`$ of $`p_c`$. Coupled to changes elsewhere, the comparison survives with its strictness for continuous finite-piecewise-smooth carrier-class competitors: none has less area than $`M(W)`$, and one ties only by covering it once (Proposition 7). Proposition 8 extends the global comparison to this proposition's full Lipschitz class.
- It shows the pinch resisting local resolution. It does not ground the fixed edge itself (1c), and by itself it does not make the result count toward the bar.
- The competitors are maps of the band's own strip with the boundary map fixed, so the band's topology near $`p_c`$ is fixed; a competitor that cuts or re-glues the band there, or a mod-2 competitor, is outside the class.

**Least area with the edge fixed.** The fence on least area leaves carrier-class competitors open, and Proposition 6 compares only competitors that change the band near $`p_c`$. Integral geometry compares them all at once.

**Proposition 7 (DERIVED; least area with the edge fixed).** Let $`M'`$ be a competitor for $`M(W)`$: a continuous, finite-piecewise-smooth map of a Möbius band into $`\mathbb{RP}^3(R)`$ whose boundary map is $`M(W)`$'s edge as parametrized and whose core maps to the generator of $`\pi_1(\mathbb{RP}^3)`$. Then, with area counted with multiplicity,

```math
\mathrm{Area}(M') \ge 4WR = \mathrm{Area}(M(W)).
```

Equality holds exactly when $`M'`$ covers $`M(W)`$ once: almost every point of $`M(W)`$ has one preimage, and the image off $`M(W)`$ has zero area. Embeddedness is neither assumed nor needed, and the change from $`M(W)`$ may sit anywhere on the band, near $`p_c`$ and elsewhere together.

*Proof.* On [The Projective Carrier: Supporting Proofs](carrier-proofs.md#proposition-7), with the remark on Pu's inequality that followed it here.

- **What it settles.** With the edge fixed as parametrized and the core generating, $`M(W)`$ has the least area among continuous finite-piecewise-smooth competitors, at every width, including those that resolve the cone and change the band elsewhere. Each width has its own edge, so no width is selected.
- **Ties.** Proposition 6's strictness, more area unless a competitor covers the bowtie once, extends to coupled competitors in this class: one that changes the band near $`p_c`$ and elsewhere too has more area than $`M(W)`$ unless it covers $`M(W)`$ once. A map that reparametrizes $`M(W)`$ ties, and so does one that sends parts of the band onto curves, which carry no area, while the rest covers $`M(W)`$ once.
- **The twist does not enter.** The argument uses the edge, the core's class and area; it never orients the band.
- **Lipschitz competitors**, the class of Proposition 6 taken globally, are Proposition 8's. For finite-piecewise-smooth competitors Proposition 7 contains Proposition 6's inequality and its strictness.

**Proposition 8 (DERIVED; Lipschitz competitors).** Proposition 7 holds for Lipschitz competitors, with its equality case, at every embedded width $`0 < W < \pi R/2`$: if $`M'`$ is a Lipschitz map of a Möbius band into $`\mathbb{RP}^3(R)`$ whose boundary map is $`M(W)`$'s edge as parametrized and whose core maps to the generator of $`\pi_1(\mathbb{RP}^3)`$, then $`\mathrm{Area}(M') \ge 4WR`$, with equality exactly when $`M'`$ covers $`M(W)`$ once. The proof is in [The Lipschitz Comparison](lipschitz-comparison.md). It follows Proposition 7's route: Crofton's formula with multiplicity comes from the area formula applied to the map that sends a point and a direction to a line, the parity of the line count from local degrees, and the tie from a measure-theoretic form of step 6, with no second fundamental form.

## X. What this page does not do

This section recorded what the ruling changes on other pages and what it leaves alone: where the carrier sits, the two seams, the two signs, the sampler reading, condition 2, the cone extension, the anti-periodic condition, Tier 2, the transfer run and the readings set aside. It is now [The Projective Carrier: Scope Inventory](carrier-inventory.md), moved without change. It also carries two findings of this page, given there in full: on this placement the double lune's setwise stabilizer in $`2I`$ is $`\{\pm 1\}`$; and, independently of the ruling, under Friedrichs the holonomy selects the sector, not the level.

## XI. The ruling

**Ruled 2026-09-27: reading (A).** The framework adopts the premise: the vacuum carrier itself is unbent. The ruling reads the Möbius character as global and topological, not produced by extrinsic bending; on this page that character is the orientation holonomy around the core, supported at $`p_c`$ for the conic band. The ruling does not read the postulate's shorthand $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$ as having derived $`\mathbb{RP}^3`$; it takes the projective layer, which this page identifies, as the consistent realization of the postulate's intended geometry. So the zero-bending carrier is realized through the projective layer: it lifts to and embeds in $`\mathbb{RP}^3`$, with its core the central element $`-I`$ and the spin link of Lemma 1. Whether $`\mathbb{RP}^3`$ or $`S^3/2I`$ is its physical domain is not ruled (1f). The ruling keeps the other four readings as the alternatives the old wording admitted: the decision's record, not framework readings. The sub-decisions 1a to 1g stay open under the ruling itself, and $`M(W)`$ stays the leading realization, not uniquely selected (1b); 1a, 1c, 1d, 1e, 1f and 1g have since been decided (below).

The page's arguments use one convention of their own, the Friedrichs realization at reflex corners (§V). The rest of this section records what the ruling settled, what it set aside, and what stays open.

**Decision 1: where the carrier lives.** Five readings were weighed. Three share an intrinsic geometry that carries the Stage-1 scalar relation, and differ only in placement, by layer and bending (§I, three questions):

| | unbent, $`A = 0`$ | bent, $`\det A = 0`$, $`A \neq 0`$ |
|---|---|---|
| $`\mathbb{RP}^3`$ | (A) the premise, ruled; one-sided | (A′): Proposition 0.3's family one-sided, others open |
| $`S^3`$ | excluded (Lemma 0; the Tier 2 ground floor) | (B′): Proposition 0.2's family two-sided, others open |

- **(A) The premise, adopted.** The carrier itself has zero bending. Its core is $`-I`$, and it lifts to the projective layer (Lemma 0). Whether it is the Λ construction's own band, the quotient by $`-I`$ of the covering band, is 1b; which layer is its physical domain is 1f.
- **(A′) Bent in $`\mathbb{RP}^3`$.** The carrier lies in the projective layer with its core $`-I`$, and it is bent. What needs only the layer holds, and what needs $`A = 0`$ does not (§I, three questions). If 1b selects $`M(W)`$, Proposition 0.3 supplies a free family of such carriers, each one-sided, with a pinch that is not planar.
- **(B) Embedded in $`S^3`$.** The carrier is a Möbius band in $`S^3`$, as the postulate formula reads literally, and it does not carry the scalar relation: the covering band that carries the Λ geometry is a different surface. Tier 2's run studied its minimal case.
- **(B′) Bent in $`S^3`$.** The carrier lies in $`S^3`$ and carries the scalar relation, with $`\det A = 0`$ and $`A \neq 0`$ somewhere. If 1b selects $`M(W)`$, Proposition 0.2 supplies a free family, each two-sided, with its edge through $`p_c`$ twice. Whether a smooth carrier with the scalar relation embeds in $`S^3`$, which would keep the literal formula, is OPEN.
- **(C) An intrinsic model.** The carrier is the pillar's intrinsic surface, placed in no three-dimensional space, as the pillar presents it: "The paper's model is intrinsic, and the paper places it in no three-dimensional space" ([black-hole page](../../../../cosmos/files/black-hole.md)). The [bedrock index](../../bedrock/README.md)'s "a singular surface model" fits (C) and (A) alike.

(A) adopts the premise, and the ruling chose it. The other four each reject it in their own way: (A′) keeps the layer and gives up zero bending; (B′) gives up the layer, and with it zero bending; (B) gives the carrier a different intrinsic geometry, so the scalar relation holds only on the covering band; (C) places the carrier nowhere.

**Settled by the ruling:**
- the vacuum carrier is unbent, the premise of §I;
- the carrier cannot lie in $`S^3`$, and it lifts to $`\mathbb{RP}^3`$ (Lemma 0);
- in the spinorial sectors the central sign is the carrier's Möbius holonomy (Lemma 1).

With the exact $`2/R^2`$ kept as the first positive level of the Friedrichs realization, Corollary 2.1 adds that the twist passes through a singular point and that the rest of the band is orientable. For $`M(W)`$ that confinement is topological and holds under any extension, and the Friedrichs spectrum does not see the twist (§II).

**What stays to decide.** The sub-decisions 1a to 1g, each tagged with the readings under which it arises and each decision with the record it was made from, are on [The Projective Carrier: Decision Records](carrier-decisions.md), moved there without change, with the ledger of what each reading would gain and owe and the note on the trivial block. Their standing, in the words of that page, with *Open* for the one the ruling above does not list as decided:

| Sub-decision | Standing |
|---|---|
| 1a. The Tier-1 rows | The formula's gloss (A, A′, B′, C): Decided 2026-09-28 for (A). The anti-periodic condition's reach (A, A′, B′): Decided with 1d (2026-09-29) |
| 1b. The realization (every reading) | Open. Ruled 2026-09-30: the framework's two-lap sentence binds as topology only |
| 1c. The boundary regime (every placed reading) | Decided 2026-10-01: the temporal edge is prescribed boundary data. Note (2026-10-05), on Proposition 8 |
| 1d. The sampler (A, A′) | Decided 2026-09-29: the transverse derivative, normalized at unit radius ($`R\partial_\nu`$), for every block |
| 1e. The cone extension (twisted sector: every reading; untwisted sector: A, A′, B′) | Decided 2026-09-29: Friedrichs in both sectors |
| 1f. The physical layer, and the pose relative to $`2I`$ (A, A′) | Decided 2026-10-02: the physical layer is $`\mathbb{RP}^3`$. The carrier's physical domain is $`\mathbb{RP}^3`$, where it embeds, and $`S^3/2I`$ is its observable domain, where the sampler's target bundles live, reached through the sixty-sheeted covering. Decided 2026-10-02: the pose is free. Note (2026-11-11), on the first self-intersection width |
| 1g. Which edge is time (wherever 1b makes $`M(W)`$ the carrier: A, A′, B′, C) | Decided 2026-09-29: time runs on the abstract boundary circle |

## Files

In [`scripts/projective-carrier/`](scripts/projective-carrier/), with the SHA-256 of every other file in `SHA256SUMS`:
- `smooth_band.py`: the tube family's first twisted level by shooting, with the exact $`\mathbb{RP}^2`$ eigenfunctions checked symbolically. Its record is `smooth_band.out`.
- `identities.py`: Theorem 2's coordinate identities on a generic surface in $`S^3`$, the tubes' Gauss-Bonnet balance, Lemma 4's tilt identities and its comparison with the arch, the untwisted mode $`\phi_0 u_0`$ of §II, §IX's second-variation density, and the $`3/R^2`$ fence. Its record is `identities.out`.
- `seed_laps.py`: Proposition 4.2 on bands with one lap moved off its line, by quadratic finite elements at three widths: the level on $`M(W)`$, the first variation against the formula, a rigid turn of the lap, the bracketed roots, the level's simplicity, the moved lap's geodesic curvature, the mode's distance from every tilt and the bands' embedding, each with a planted defect that must fire. Its record is `seed_laps.out`.
- `lift_trace.py`: Proposition 5's traversal, traced through the covering and checked against the table in §VII. Its record is `lift_trace.out`.
- `bent_carrier.py`: Proposition 0.2's embedding of the conic band in $`S^3`$, cross-checked numerically for isometry, the pinch, embeddedness, $`\det A = 0`$, its mean curvature, two-sidedness and the planar pinch. Its record is `bent_carrier.out`.
- `bent_projective.py`: Proposition 0.3's embedding in $`\mathbb{RP}^3`$, cross-checked the same way, with one-sidedness through $`-I`$, the pinch that is not planar, and the edge's lift. Its record is `bent_projective.out`.
- `symmetric_edge.py`: Proposition 3.2's geometry over the 31 icosahedral axes: the circle $`\Sigma \cap g\Sigma`$ for each non-central element, the elements that keep it, the crossings and their angles, and that no non-central element keeps a two-loop edge, each with a planted defect that must fire. It prints no widths. Its record is `symmetric_edge.out`.
- `gate_page.py`: the standing gate of this page and of the three pages that hold text moved from it, [The Projective Carrier: Scope Inventory](carrier-inventory.md), [The Projective Carrier: Supporting Proofs](carrier-proofs.md) and [The Projective Carrier: Decision Records](carrier-decisions.md). On each of the four it checks hygiene, links and live anchors, the math render and budget, and every quotation verbatim and, where a link names a section, inside that section. On this page it also checks the header against metadata-lint, the tube table, the script records against their expected names, the pinned hashes, the frozen span of §IX, and the pages that point into this page: the links from the working index, the Λ page and the public pages' reworded sign and seam statements, the dated scope notes on the working-layer pages, every anchor another page links, and every quotation that another page sets beside a link to one of this page's sections, which must lie in that section unless it quotes another page the line links. Across the four it checks that each moved block has a link where it stood, that each proof pointer and each proof's link back resolve, that each statement copied to the proofs page equals its lines here, that §XI's table gives each sub-decision its label, its dated lead-ins and its standing in the decisions page's words, that each new page names this page as its parent, and that the new pages' headers are in order. Its `--arms` mode plants a defect for each check and requires it to fire.

---

| **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |
