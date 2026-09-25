<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🌁 Postulate Bridge

**Type:** Program
**State:** Active
**Status (2026-09-23):** The staged route is resolved as a split (gauge dictionary proved, Möbius channel decoupled route-specifically). The sampler reading closed negative twice over; the variational reading is recorded open. The dynamical direction is the live front. Its Tier 2 has run a first computation: the specified band is unstable, and no smooth embedded band spanning the fixed great circle attains the infimum of area. The bar now asks for a stable critical point, not a global minimum.
**Summary:** Asks whether a theorem connects the two bedrock results sitting on the two pieces of the postulate; owns the staged route and its sampler, variational, and dynamical readings.
**Gated by:** `gate:variational-independence-bar`

Resolved along the staged route, as a split. The two bedrock results sit on the two pieces of the postulate $`S^1 = \partial(\text{Möbius}) \hookrightarrow S^3`$, $`\partial S^3 = \emptyset`$. The gauge dictionary is proved: the $`E_8`$ filling carries the boundary's Galois asymmetry exactly, on $`\partial W = +\Sigma`$ ($`\Delta\rho = -8/5 = 4\,\Delta D`$, and $`k \equiv cs \bmod 1`$ in all four sectors). The Möbius coupling is refuted route-specifically: on the characteristic slot, every coefficient built on $`W`$ restricts rank-trivially, so the surface term cancels from the Galois difference in every restriction-route identity with the canonical pullback coefficient bundle. No universal independence claim is made. The naive bridge through the shared value $`2/R^2`$ remains dead (a forced curvature-scale coincidence, not a spectral link). Steps 1-4 complete ([Step 4, part two](step4-coupling.md)); the split verdict is paper-ized as the third bedrock pillar, [Galois pair](../../bedrock/files/galois-pair.md); this note is the record of the route. A dynamical direction, separating the holonomy tail, the selection reading, and a possible gravitational realization, is recorded open below and has not been run. Tier 2's totally geodesic candidate has been removed: it is topologically unavailable to a smooth Möbius band. The replacement equilibrium remains a variational problem to be defined and solved. A sampler reading of the split, naming the observation map $`f = \pi \circ i`$ that needs no descent and the sampling operator $`\mathcal O_M`$ as the open object, is recorded below (2026-08-19); its first test is closed negative, leaving the transverse-not-restrictive result as the residue. A variational reading is now recorded as program architecture over the existing Tier 2 and Tier 3 programs (2026-09-02). It consolidates the embedding, sampler, and clock-selection questions into one candidate global functional, with no ledger or engine change.

**Related:** [First eigenvalue](../../bedrock/files/first-eigenvalue.md), [Coexact gap](../../bedrock/files/coexact-gap.md), [Galois pair](../../bedrock/files/galois-pair.md), [bedrock README](../../bedrock/README.md).

---

## What exists

Two standalone spectral-geometry results, each proved, cited here by content.

**The surface.** The first positive eigenvalue of the twisted Laplacian on a constant-curvature Möbius band $`M(W) \subset S^2(R)`$ is $`2/R^2`$ in the narrow regime, stable across the Friedrichs and bridging self-adjoint extensions for $`\delta_0 > 2R/e`$. The eigenfunction is $`\sin(y/R)`$, the $`\ell = 1`$ zonal mode, on the symmetric extension-independent tower; the Friedrichs realization is unitarily equivalent to the Neumann Laplacian on a spherical lune. The framework reads $`2/R^2`$ as the surface spectral seed $`\Lambda_\text{top}`$.

**The space.** The coexact $`1`$-form gap on $`S^3/\Gamma`$ twisted by a flat bundle $`E_\tau`$ is $`q_\tau^2/R^2`$, with $`q_\tau`$ the first McKay occurrence level. For the adjoint of an irreducible flat $`\mathrm{SU}(2)`$ connection this is $`4/R^2`$ across the ADE classification, with one exception: $`36/R^2`$ for the Galois connection on $`S^3/2I`$, whose adjoint sits at McKay distance six in affine $`E_8`$. That adjoint gap is the linearized gauge-sector gap; the framework carries it into its Yang-Mills reading.

The postulate nests three objects: the temporal edge $`S^1 = \partial(\text{Möbius})`$, the Möbius surface it bounds, and the space $`S^3`$ in which the edge is anchored. The papers put operators on the surface and the space. The question is whether a theorem connects them.

---

## What was tried, and why it failed

**The arch (superseded).** An attempt to connect the two through the shared value $`2/R^2`$: the surface eigenvalue equals the Bochner/Weitzenböck Ricci floor on $`S^3`$, a coincidence special to dimension three. The grand reading does not survive. The surface eigenvalue is $`\Gamma`$-blind, the Ricci floor is the only $`\Gamma`$-independent slot in the gap, so the match is forced rather than discovered: a curvature-scale coincidence, not a spectral relationship. The corpus already half-states it (the coexact paper notes the floor is numerically the surface eigenvalue but a different operator and only a loose lower bound; the eigenvalue paper records $`2/R^2 = R_{\mathrm{sm}}`$). The modest survivor, a rigid floor across ADE plus a dimension-three realization, is true but does not connect the two operators.

**The deeper obstruction.** The band lives upstairs on a great $`S^2 \subset S^3`$; the coexact gap lives downstairs on $`S^3/\Gamma`$. No great $`S^2`$ is $`2I`$-stable (left translation by any non-central element moves the defining $`3`$-plane in $`\mathbb{R}^4`$), so the surface does not descend to the quotient as a submanifold. "Restrict to a great $`S^2`$" and "take $`2I`$-invariants" are independent operations on the $`\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R`$ content of $`S^3`$; they compose only if the surface is group-stable, and it is not.

---

## Three routes

<a id="route-1"></a>
### Route 1, spectral restriction via $`\mathbb{Z}_2`$ holonomy: closed

The idea was to link the band's orientation $`\mathbb{Z}_2`$ holonomy to a non-orientable or flat-bundle structure on the quotient. Two walls. First, $`S^3/2I`$ is orientable (an integral homology sphere), so there is no non-orientable structure downstairs to host the band's twist. Second, $`2I`$ is perfect ($`H^1(2I) = 0`$), so it has no $`\mathbb{Z}_2`$ quotient and no order-two character; the band's $`\mathbb{Z}_2`$ cannot be a $`2I`$-equivariant datum. The perfectness that makes $`2I`$ the unique gauge exception in the coexact paper is exactly what forbids the orientation bridge.

<a id="route-2"></a>
### Route 2, heat kernel: set aside

Heat traces relate a space to its covers and subspaces. The band is neither a cover nor a subspace of $`S^3/2I`$. The leading asymptotics mismatch ($`t^{-1}`$ for a surface versus $`t^{-3/2}`$ for the $`3`$-manifold), and the trace formula organizes the twisted spectrum by conjugacy classes and closed geodesics, with no slot for an embedded surface.

<a id="route-3"></a>
### Route 3, APS index theory on the $`E_8`$ plumbing: run, resolved as a split

**Why this is the route.** $`S^3/2I`$ bounds a compact oriented $`4`$-manifold $`W`$, the $`E_8`$ plumbing, whose intersection form is the $`E_8`$ lattice. This is not a second, coincidental $`E_8`$. The McKay correspondence identifies it with the one the coexact paper uses: the minimal resolution of the $`\mathbb{C}^2/2I`$ Kleinian singularity has eight exceptional $`(-2)`$-curves in bijection with the eight nontrivial irreps of $`2I`$, their intersection matrix is the negative of the finite $`E_8`$ Cartan matrix (self-intersections $`-2`$, off-diagonal $`+1`$ for $`E_8`$-adjacency), and the affine node of the McKay graph is the trivial irrep that the resolution drops. So the Galois node $`\mathrm{Sym}^2 Q'`$ at McKay distance six corresponds to a definite homology class in $`H_2(W)`$. The research question is whether the APS machinery respects that identification, not whether a map between two $`E_8`$s exists.

The boundary carries the gauge spectral data, the interior the topology. The APS index theorem relates:

- Boundary: the eta-invariant of the adjoint curl $`\ast d_\nabla`$ on $`S^3/2I`$. This is the spectral *asymmetry* of its signed first-order spectrum (eigenvalues $`\pm m/R`$), not the bottom eigenvalue. The coexact gap is the bottom of $`(\ast d_\nabla)^2 = \Delta_\tau`$, a different functional of the same operator. Both are connection-sensitive, but they are distinct features.
- Interior: signature, intersection form, characteristic classes, and the homology classes of embedded surfaces (self-intersection $`[\Sigma]^2`$, normal Euler number, $`\mathbb{Z}_2`$ class).

Fintushel-Stern is the foundational reference; Kirk-Klassen and Nasatyr compute adjoint spectral-flow and eta-invariant data on $`S^3/2I`$.

**The make-or-break question.** Does the APS index formula for the adjoint-twisted operator on $`W`$, with boundary contribution the $`Q'`$ eta-invariant, contain an interior term involving the homology class that the McKay correspondence assigns to the Galois node $`\mathrm{Sym}^2 Q'`$ (distance six)? If the boundary asymmetry distinguishing $`Q'`$ from $`Q`$ is matched in the formula by the interior class of the distance-six node, the embedding does real work and the postulate's two pieces are linked through the index. This is a computation, not a conceptual question.

**The eigenvalue question, tracked open not closed.** Whether the surface eigenvalue $`2/R^2`$ enters is subtler than "it cannot." The index theorem is topological on the interior, so it sees homology classes and characteristic numbers, not Laplacian eigenvalues directly. But $`2/R^2`$ is also the scalar curvature of $`S^2(R)`$, and scalar curvature enters Gauss-Bonnet and the Pontryagin/signature integrals, so a $`2/R^2`$ can surface in the interior term. The test is therefore not "does $`2/R^2`$ appear" but "is any appearance the curvature-scale coincidence again, forced because the band's eigenvalue equals its curvature by Obata, or is it tied to the specific surface class." Any appearance must clear that check before it counts as a spectral connection.

**Why it might work.** The bounding manifold is wired to the group not by a coincidence of Dynkin diagrams but by the McKay correspondence, a proved theorem: the exceptional $`(-2)`$-curves of the resolution are the eight nontrivial $`2I`$-irreps, and their intersection form is the negative $`E_8`$ Cartan matrix. So the $`E_8`$ plumbing is the structurally correct manifold and the Galois node is a definite class in it, not a numerical match to be hoped for. The question is whether any class in $`H_2(W; \mathbb{Z}_2)`$ carries a surface whose normal twist reproduces the Möbius band's $`\mathbb{Z}_2`$ holonomy and whose topological contribution constrains the boundary coexact eta.

**On the dimensional spread.** The $`2`$-dimensional surface, $`3`$-dimensional boundary, and $`4`$-dimensional interior are not a mismatch to explain away; they are the native operating range of APS and the G-signature theorem, which exist precisely to relate data across these dimensions. The open question is not that the dimensions differ but whether the specific surface class and the specific boundary operator land in the same formula with nontrivial coefficients. A precision question, not a structural objection.

---

## Staged plan

Ordered by decisiveness, not cost: the test that can kill the program runs first.

1. **Rho comparison, $`Q`$ versus $`Q'`$ (the gatekeeper): done, gate open.** The Step-1 boundary invariant is the APS odd-signature rho invariant for $`\mathrm{ad}\,Q`$ versus $`\mathrm{ad}\,Q'`$, equivalently the coexact adjoint-curl eta asymmetry after exact-sector cancellation and acyclicity. The difference is $`8/5`$, nonzero and supported entirely on the four golden ($`\sqrt5`$) conjugacy classes, the Galois locus that produces the $`36/R^2`$ gap; an independent Chern-Simons computation confirms it mod $`\mathbb{Z}`$ and fixes the unreduced normalization. The sign is fixed in Step 2: $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$ on the resolution-boundary orientation. Full calculation: [eta-gatekeeper](eta-gatekeeper.md).
2. **Analytic setup and sign (Step 2): done.** $`W`$ is simply connected, so the flat $`Q'`$ on $`\partial W = S^3/2I`$ does not extend flatly ($`2I \to \mathrm{SU}(2)`$ cannot factor through $`\pi_1(W) = 1`$). Framework: the ALE instanton on the minimal resolution of $`\mathbb{C}^2/2I`$ (Kronheimer-Nakajima), whose tautological bundles carry the McKay classes; the orbifold cone is demoted to a consistency check, having no interior $`H_2`$. Sign: on the resolution-boundary orientation $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$, with the $`73/15`$ magnitude anchored in print (BHKK's published $`\pm 73/15`$ on $`X_{+1}=-\Sigma`$, resolved by spectral-flow integrality). Full calculation: [Step 2](step2-analytic-setup.md).
3. **Homology of $`W`$ mod $`2`$ (Step 3): done.** $`H_2(W;\mathbb{Z}_2)=\mathbb{Z}_2^8`$ with the $`E_8`$ adjacency form: alternating and nondegenerate, unique characteristic class $`0`$, $`W`$ spin. Every class carries non-orientable embedded surfaces ($`e+2\chi\equiv\mathfrak{P}\bmod 4`$ under the mod-4 refinement), and the Brown/Guillou-Marin data of the characteristic-surface route is confined to the zero class. The Galois node is the short-arm curve, mod 2 one of the $`120`$ root classes, on which the automorphism group of the mod-2/mod-4 homology acts transitively: the interior homology is Galois-blind, and the Galois selection is carried by the McKay/tautological decoration alone. Full calculation: [Step 3](step3-interior-classes.md).
4. **The coupling identity (revised by Step 3), and the $`2/R^2`$ check.** Step 3 rules out the naive form of this step: the band's $`\mathbb{Z}_2`$ data and the Galois selection do not share a class, so there is no "insert the band's class and read the coupling." The revised test is a three-ingredient identity: write the APS index on $`W`$ in Step 2's framework and determine whether the boundary rho (Galois-sensitive, Step 1), the tautological distance-six data $`\mathrm{ch}(\mathcal{R}_{d6})`$ (Step 2), and the characteristic-slot Brown/Guillou-Marin data (where the band's normal twist lives, Step 3) appear in one identity with nontrivial coefficients. A negative at this bar is a result. Any $`2/R^2`$ that surfaces here still gets the curvature-scale-coincidence check. Part one (the bookkeeping) is done: the four carried items are closed and the three ingredients compute in one exact character-sum currency, with the conversion identity $`\rho^{\mathrm{sign}}_\alpha=\dim\alpha+4(D_\alpha-\dim\alpha\,D_{\mathrm{triv}})`$ translating the boundary rho into the KN currency (gate value $`-8/5=4\,\Delta D`$ on $`+\Sigma`$), the tautological charges reproducing the Chern-Simons web mod 1, and $`\bar\mu=-1`$ locked through Ruberman-Saveliev; see [Step 4, part one](step4-bookkeeping.md). Part two is done, and it decides the question: negative, route-specifically, with the positive residue proved. The triviality lemma (every coefficient built on $`W`$ restricts rank-trivially to the characteristic slot) makes every $`F`$-localized term rank-blind, so the Möbius data cancels from the Galois difference in every restriction-route identity with the canonical pullback coefficient bundle; the complementary channels are disjoint (root classes couple but carry no canonical Guillou-Marin package; orientable characteristic surfaces carry Arf, not Möbius, data). The gauge dictionary survives as theorems. No $`2/R^2`$ appeared; the curvature-scale-coincidence check discharges vacuously. Full calculation: [Step 4, part two](step4-coupling.md).
5. **Reading.** Atiyah-Patodi-Singer (1975), Fintushel-Stern, Kirk-Klassen, Nasatyr, Rokhlin and its non-orientable generalizations, Guillou-Marin.

---

## What the framework does and does not owe this

The framework's claim is "one shape, two consequences." The shared $`S^3`$ of radius $`R`$ is already true as a geometric fact without any theorem relating the two spectra, so this bridge would be a bonus the framework is glad to have and is undamaged by lacking. The two bedrock results stand independently.

If the index computation yields a genuine connection, the result relates the gauge eta to the band's topological embedding. If it yields a negative result, that is also a result, but state it route-specifically: the interior term is topological, and any $`2/R^2`$ in it reduces to the curvature-scale coincidence (provably, since the band's eigenvalue equals its curvature by Obata) rather than a spectral link to the surface paper. That route-specific negative is provable; a universal claim that the two spectra are independent is not.

This became the bedrock pillar [Galois pair](../../bedrock/files/galois-pair.md), written to that standard: no physics vocabulary, the mathematics leading, the two pillars cited by content, and the surface eigenvalue kept out of every index ingredient. The route it reports is the negative-and-positive split, not the $`\Lambda \leftrightarrow`$ mass-gap link, which the pillar does not claim.

---

## A sampler reading

**Recorded 2026-08-19.** The split verdict above closes the topological coupling on its route. This section records an interpretation under which that closure is what the architecture predicts, together with the one new mathematical object the interpretation names. Nothing in it modifies the verdict, the pillars, or the tiers below; it organizes them.

Let $`X = S^3/2I`$, let $`\pi : S^3 \to X`$ be the quotient map, and let $`i : M \to S^3`$ be a smooth Möbius realization (any member of the admissible classes of Tier 2). The deeper obstruction above rules out descent of the band to $`X`$ as a $`2I`$-stable submanifold. It does not rule out a map into the quotient: the composite

```math
f = \pi \circ i : M \to X
```

exists with no descent hypothesis at all, and every flat bundle $`E_\tau \to X`$ therefore has a canonical pullback $`f^* E_\tau \to M`$. The distinction deserves prominence:

```math
\boxed{\ \text{no descent as a submanifold} \;\neq\; \text{no sampling map}\ }
```

This opens a reading of the postulate in which the two pieces hold different jobs: the quotient carries the native spectrum ($`2I`$, $`E_8`$, the coexact gap and its Galois exception), while the Möbius geometry supplies a phase-sensitive sampling structure on that spectrum. On this reading the recorded negatives are structural, not accidents to be survived: a sampler and a substrate are different mathematical objects, so the orientation $`\mathbb{Z}_2`$ is not a $`2I`$-equivariant datum (Route 1), the band does not descend (the deeper obstruction), and the surface data cancels from the interior index route (Step 4). The failures land exactly where a readout geometry, wrongly treated as a co-resonator, would fail.

**Guardrail: the surface pillar is not demoted.** The sampler reading does not make the Möbius band spectrally passive. Its own twisted Laplacian, the extension-dependent bottom, and the stable first positive level $`2/R^2`$ remain the independent surface result ([first eigenvalue](../../bedrock/files/first-eigenvalue.md)), and the framework's cosmological reading continues to stand on it. The claim under consideration is only that the surface does not determine the native spectrum of $`X`$.

**The open object.** The interpretation names one missing object, the sampling operator

```math
\mathcal O_M : \Gamma(X, E_\tau) \longrightarrow \Gamma(M,\ f^* E_\tau \otimes \mathcal L),
```

with $`\mathcal L`$ the orientation local system of $`M`$. Only the target type is defined here; the construction is the open problem.

**Guardrail: a canonical candidate $`\mathcal O^{(1)}_M`$ exists, but nothing selects it as the sampler operator.** The $`\mathcal L`$-twist cannot be produced by choosing a global nowhere-zero section of $`\mathcal L`$: no such section exists, and its nonexistence is the topology being retained, not an inconvenience to be normalized away. Any local construction carries a sign ambiguity valued in exactly the $`\mathbb{Z}_2`$ that intensity forgets, which is why the intensity level is the first place a well-defined observable can live.

**The first bounded test.** Route 1 proves the Möbius orientation holonomy cannot be identified with any $`2I`$-datum: $`2I`$ is perfect and has no order-two character. The bounded question is therefore not identification but intertwining after sign-forgetting, in exactly the quotient where the distinction disappears:

```math
\boxed{\begin{array}{c}
\text{Does an admissible } \mathcal O_M \text{ intertwine the central } -1 \in 2I \text{ with the Möbius sign ambiguity,} \\
\text{so that an intensity observable factors through } 2I/\{\pm 1\} \cong I\ ?
\end{array}}
```

The [engine](../../../README.md) records the intensity projection (the 120 labels passing to the 60 under $`\lvert\psi\rvert^2`$) as the mechanism of the 60R grid; a positive answer here would derive it within a specified operator framework, the first structure the sampler reading produces rather than explains. A negative answer, stated for a specified admissible class, would close this reading's first route the same way Steps 1-4 closed the topological one.

The test has been run and is [closed negative](sampler-first-test.md). No compact embedded surface in $`S^3`$ with a single boundary circle is invariant under the antipodal map: the quotient would be a compact surface in $`\mathbb{RP}^3`$ whose boundary is the nontrivial class of $`H_1(\mathbb{RP}^3;\mathbb F_2)`$, which a mod-$`2`$ fundamental class forbids. So the deck element $`-1`$ never stabilizes an admissible band, $`\lvert S\rvert`$ is forced odd, the target $`\lvert S\rvert = 2`$ is unreachable for every boundary, and no change of boundary curve rescues it. The sampler does not realize the $`120 \to 60`$ halving geometrically. This leaves the engine's projection exactly where it was, resting on $`\lvert\psi\rvert^2`$ alone, and it sharpens the architecture: Route 1 showed the two $`\mathbb Z_2`$'s cannot be identified algebraically, and this shows they cannot be identified through antipodal symmetry of the sampler either.

*Added 2026-09-25: the engine no longer names the intensity projection as the 60R grid's mechanism. Both grids use the same readout, the intensity ([linear readout](scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go)), blind to the central sign in every sector, so squaring cannot sort observables between them; the grids differ in resolution, and which observable takes which is a motivated assignment ([engine](../../../README.md#the-sampling-grids)).*

What survives, independent of the test, is the reading's one structural result:

```math
\boxed{\ \text{the natural Möbius sampler is transverse, not restrictive}\ }
```

The pullback $`f^*E_\tau`$ is canonically trivial, since $`f = \pi \circ i`$ has the preferred lift $`i`$, so the field cannot supply the twist; the plain restriction does not carry it; and $`\nu \cong \mathcal L`$ makes the transverse derivative carry it for free.

A second obstruction, independent of the geometric one, is recorded with it: equivariance gives $`\mathcal O^{(1)}_{gM}(\Psi)(gx) = \tau(g)\,\mathcal O^{(1)}_M(\Psi)(x)`$, so the scalar intensity profile is identical on all $`120`$ deck translates and no invariant scalar readout distinguishes lifts at any stabilizer size. The translates are symmetry-related presentations of the same quotient data. The two negatives are therefore best named as non-identification by obstruction, algebraic (Route 1: $`\mathcal L`$'s $`\mathbb Z_2`$ is not a $`2I`$ character) and geometric (no antipodally invariant one-boundary sampler), both saying $`\mathbb Z_2^{\text{Möbius}} \neq \mathbb Z_2^{\text{centre}}`$ as identified structures while leaving open that both participate in one mechanism. No universal independence is claimed, here or anywhere on this program.

The successor question is accordingly not what distinguishes the lifts but what the sampler transfers: the operator $`T^{(\tau)}_{\mu\lambda} = P_\mu \circ \mathcal O^{(1)}_M\vert_{E^\tau_\lambda}`$ from ambient eigenspaces into twisted Möbius ones, studied through its rank or Hilbert-Schmidt norm, with selection rules or a dependence on $`2I`$ and $`E_8`$ representation data as the informative outcomes. It is not set up, and it carries two guards: it must not re-assert the dead $`2/R^2`$ arch (a coupling matrix element is not an equality of spectra), and its Möbius eigenspaces must belong to a named operator on the embedded band's induced metric rather than being imported from the intrinsic conic pillar.

**Relation to the tiers.** This reading is an organizing interpretation over the existing programs, not a fourth tier. Tier 1 asks what such sampling detects in holonomy; Tier 2 asks whether the sampler configuration is dynamically selected ($`\delta\mathcal{S}/\delta i`$ choosing $`i`$ among admissible realizations); Tier 3 asks whether the ambient metric responds to the realized sampled state ($`\delta\mathcal{S}/\delta g`$). None of these is established by the reading, and the bar below is unchanged: the reading becomes structure only when a specified $`\mathcal O_M`$ clears it.

---

<a id="dynamical-direction"></a>
## A dynamical direction (candidate; Tier 2's first computation run)

The three routes above are index-theoretic and therefore topological on the interior by construction: they see homology classes and characteristic numbers, but are structurally blind to stress, extrinsic curvature, local action density, and variation of the metric. Their route-specific negative constrains the *topological* reading of the temporal edge and says nothing about a dynamical one. A dynamical reading is a different direction, not a rephrasing, and is no more owed by the framework than the topological bridge was. It is recorded here at three tiers of decreasing tractability and decreasing warrant.

**Tier 1, the holonomy tail (bounded, open, already flagged).** Definition 7.3 of [Galois pair](../../bedrock/files/galois-pair.md) closes its negative to the restriction route and explicitly excludes "the holonomy of the restricted connection." Holonomy is finer than the Chern character: two connections sharing all characteristic classes can still differ in holonomy. The paper already shows the tautological restriction can be nontrivial on the root class of the distance-six (Galois) node in $`H_2(W;\mathbb{Z}_2)`$, so a surface representing that class couples to the decoration, while the Guillou-Marin enhancement that might convert such a coupling into an eta contribution is unavailable away from the characteristic class. The open question is whether the holonomy of the tautological connection, evaluated on a surface representing that decorated homology class, detects the same Galois distinction whose boundary character-sum difference is supported on the four golden conjugacy classes of $`2I`$. This is a computation on objects that already exist: the fixed ALE metric and the fixed tautological connection; [Galois pair]'s Directions name the broader opening, pointing to the equivariant refinements of instanton theory. A positive result would show that a finer invariant of an *already-fixed* configuration carries the asymmetry. It is not the dynamical claim and is kept separate from it: nothing about this computation requires or supports energy as a constituent of the temporal edge.

**Tier 2, the selection reading (a direction, currently a mood).** The postulate specifies an *admissible* configuration: a circle as the edge of a Möbius band embedded in $`S^3`$. The stronger reading is that the realized embedding is a critical point of a coupled action, $`\delta\mathcal{S}[g, i, \text{fields}] = 0`$, so the embedded edge solves an Euler-Lagrange matching equation in intrinsic and extrinsic curvature, surface and edge tension, and ambient geometry, rather than being assumed as an inclusion by hand. In that reading $`G`$ appears first as a coefficient in the equation that makes surface and space fit, and only afterward as the exchange rate the [Waltz](../../../../spectrum/files/the-waltz.md) reads off. The zero-excitation equilibrium cannot be the totally geodesic embedding: for a totally geodesic surface the normal line is parallel in $`\mathbb R^4`$, so a connected such surface lies in a great $`S^2`$, and any surface immersed in an orientable surface is orientable, so no Möbius band in $`S^3`$ has $`A_{ij}\equiv 0`$. The topology excludes the zero-bending configuration: every smooth immersed realization in $`S^3`$ carries extrinsic curvature somewhere. Whether a specified area or bending functional has a uniform positive lower bound over an admissible class, and whether a least-energy representative exists to serve as the equilibrium, are the first variational questions of this tier, still open. This is the interesting version of the "gravity upstream" idea, but it remains a mood until there is a functional whose critical point realizes the postulate embedding and produces content beyond the $`G`$ ratio already in hand. Words that already carry technical jobs in the papers, instanton, action, Ricci-flat, do not transfer to this reading for free. A cautionary precedent sits in the corpus. The signed well-functional sweep tested a structurally similar hope, whether a distinguished structure is secretly the extremum of a natural functional, and found none across an eight-functional menu (a recorded null). The searches differ in kind and size: the wells sweep ranges over a handful of arithmetic positions, where eight functionals cover real ground, whereas a functional over embeddings ranges over an entire function space, the kind of search that has landed before (minimal surfaces, Willmore surfaces, brane actions). So the null lowers the prior on an obvious low-complexity extremization discovered after the answer is known, but it is not a data point about the embedding case itself: it is the methodological instance of the built-backward caveat, not a forecast that Tier 2 fails.

**Tier 2 ground floor (recorded 2026-07-13; facts only, computation not run).** Two standard facts give this tier a concrete starting point. First, the obstruction above: no immersed Möbius band in $`S^3`$ is totally geodesic, so every smooth immersed realization has $`A\not\equiv 0`$; a uniform positive energy floor over an admissible class, and a least-energy equilibrium, are open variational questions, not consequences. Second, the normal bundle of a one-sided surface in an orientable 3-manifold, with its induced normal connection, is isomorphic as a flat real line bundle to the orientation local system ($`w_1(\nu\Sigma)=w_1(T\Sigma)`$, locally constant $`\pm1`$ transitions), so normal fluctuations are sections of $`\mathcal L`$ with its $`\mathbb Z_2`$ holonomy; at an area-critical (minimal) immersion the interior second-variation operator is the twisted connection Laplacian with curvature potential, $`-\Delta_{\mathcal L}-(|A|^2+\mathrm{Ric}(\nu,\nu))`$, and the full Hessian adds the boundary contribution fixed by the boundary regime. The [first-eigenvalue pillar](../../bedrock/files/first-eigenvalue.md) solves the bare $`-\Delta_{\mathcal L}`$, the kinetic term alone, exactly, over its own intrinsic conic geometry. What the two settings share is that the usual scalar positivity theorem is unavailable, the eigensections living in a nontrivial line bundle; this shared obstruction identifies neither the operators nor the spectra, and the pillar's extension-dependent bottom requires its conic defect analysis, which nothing here reproduces. The first bounded computation is the fixed-boundary area branch on an explicit class of embeddings: fix a round great circle $`\gamma\subset S^3(R)`$ and the admissible class $`\mathcal A_\gamma`$ of smooth Möbius-band embeddings $`f`$ with $`f|_{\partial M}=\gamma`$; extremize area, derive the minimal-surface equation, and compute the second variation on $`\Gamma(\mathcal L)`$ with Dirichlet condition $`\psi|_{\partial M}=0`$ (dependence on the representative within the unknot class is later work). The resulting Dirichlet problem versus the pillar's Neumann condition is an informative contrast, not a defect: it makes precise that the pillar is the intrinsic model of the bundle and holonomy, not the Hessian of the embedded problem. Supported-boundary and line-tension regimes are the successor problems: in closed $`S^3`$ an unconstrained boundary is not a well-posed regime for pure area (the boundary term cannot vanish for arbitrary displacement without a support constraint or an edge functional, and the unconstrained infimum is zero), and a pure line-tension term is inert under a pointwise-fixed boundary, becoming live only in the movable-boundary regimes. Willmore and Canham-Helfrich are independently established fourth-order alternatives; the postulate does not yet select among these frameworks or fix their coefficients and boundary conditions. Honesty limits: the pillar's surface is intrinsic, with no embedding in $`S^3`$ asserted in that paper, and the embedded surface will carry whatever metric its variational problem produces; nothing here couples to the $`2I`$/Galois side, so this is the surface half of the postulate only. The tier's bar stands unchanged below.

**Tier 2 first computation (run 2026-09-23).** The ground floor above is its registration, kept as recorded. The fixed-boundary area branch has run once, blind, on one specified critical band: [The Tier 2 Fixed-Boundary Run](tier2-fixed-boundary.md). That band is Lawson's Möbius band, half of his Klein bottle $`\tau_{2,1}`$. It is unstable, with Dirichlet index 2 and nullity 1. The index was already stated in the literature; the nullity follows by reflection from a published computation on Lawson's Klein bottle, and a standalone statement of it was not located. The review adds that every minimal Möbius band spanning $`\gamma`$ has Dirichlet index at least 2, so no member of $`\mathcal A_\gamma`$ attains the infimum of area. With a pointwise-fixed great-circle boundary, then, area has no least-area member of $`\mathcal A_\gamma`$. The least-area minimal band that does exist (Bernstein and Ketover) is unstable, with index 2. So this regime cannot supply a stable least-area equilibrium. The infimum's value stays open, and so do the supported-boundary, line-tension and fourth-order regimes.

**Tier 3, the gravitational realization (untried program).** The Route 3 filling is an ALE gravitational instanton: hyperkähler and Ricci-flat, with finite $`L^2`$-curvature. The proved Galois asymmetry, however, lives in the tautological gauge decoration on that background, not demonstrably in the pure gravitational metric. Making gravity load-bearing would require showing that varying or constraining the gravitational geometry couples nontrivially to that decoration, for example through an effective action obtained by integrating out the twisted field, whose metric variation produces a stress tensor and whose embedding variation produces a force on the surface or its edge. The proposed escape, that topology fixes the edge energy, is only partly available: for a gravitational instanton the relevant action depends on the chosen functional, boundary terms, and normalization, and ALE spaces carry geometric moduli, so at most a dimensionless charge is topologically fixed while the physical scale still awaits metric normalization. The defensible target is therefore a BPS-like coupled gravitational-gauge extremum with a topologically fixed dimensionless charge, not a fully quantized edge energy.

**The bar.** This direction earns promotion from mood to claim only by meeting the standard used throughout this note: an actual functional over embeddings, explicitly varied, with the postulate embedding emerging as a solution whose vacuum critical point is the least-area (least-bending) equilibrium, coupling to the $`2I`$-decorated ALE/gauge sector without an arbitrary new scale, producing content beyond the existing exchange rate, and motivated independently of the target, since a functional can always be built backward to make any chosen configuration its critical point. Until then, "$`G`$ is upstream" changes how the sentence reads, not what has been shown.

**The bar, clarified (2026-09-23).** After the first Tier 2 computation, "vacuum critical point" above is read as a stable critical point, and stability is kept separate from global least energy.
- **Stable.** The postulate embedding must be a critical point of the independently motivated functional whose second variation is nonnegative on every admissible variation of the declared class: index zero. Nullity may come only from the problem's exact symmetries or gauge redundancies. Any other zero modes are vacuum moduli. They must be declared, and a unique universal surface is claimed only after a further mechanism selects the realized member.
- **The full class.** Stability is tested on every admissible variation: interior and boundary variations for a movable boundary, the coupled area-and-edge Hessian for line tension, and the full fourth-order second variation, with its boundary conditions, for bending. A restriction on the admissible variations counts only when the postulate motivates it and it is declared before the computation, never because it rescues a candidate. The Lawson band shows why: it has index zero in its screw-symmetric sector and index 2 overall.
- **Global least energy** is a stronger result, required only of a route that claims absolute vacuum selection rather than a stable or metastable vacuum. For such a claim the "least-area" wording above stands; for a stable-vacuum claim, stability is what is required.
- **Tier 3.** For a Lorentzian action, the analogue of stability is the absence of growing physical modes once constraints and gauge are removed, not a positive Hessian.
- **In short:** criticality gives a solution, stability an equilibrium, and uniqueness modulo symmetry a selector. Global minimality is extra strength.
- **Consequence.** Under this bar the fixed-boundary area branch fails outright, since every minimal Möbius band spanning a fixed great circle has Dirichlet index at least 2 ([The Tier 2 Fixed-Boundary Run](tier2-fixed-boundary.md)).

---

<a id="variational-reading"></a>
## A variational reading (candidate, not run)

**Recorded 2026-09-02. Status: MOTIVATED. Ledger effect: none. Engine effect: none.**

The current dynamics problem is better framed as a variational principle for the global score-to-sample relation than as a search for a conventional $`L(q,\dot q,t)`$ that makes the framework move.

The corpus phase $`t`$ remains fundamental. Observer time is reconstructed from it through a lapse,

```math
d\tau_H = N(t)\,dt,
```

so the descriptive chain is

```math
t \longrightarrow \tau_H(t) \longrightarrow q(\tau_H).
```

Time is phase advance; motion is change of resolved state under that advance.

The intended two-level structure is

```math
\mathcal{S}_{\text{MIT}}
\;\longrightarrow\;
\text{descent / integration of sampled degrees of freedom}
\;\longrightarrow\;
\mathcal{S}_{\text{eff}}.
```

$`\mathcal{S}_{\text{eff}}`$ descends from $`\mathcal{S}_{\text{MIT}}`$. This is an organizing interpretation over the existing programs, not a fourth tier. Tier 2 remains the embedding variation problem, schematically $`\delta\mathcal{S}/\delta i`$; Tier 3 remains the metric-response problem, schematically $`\delta\mathcal{S}/\delta g`$.

The Möbius phase convention is fixed as follows. One lap has phase length $`2\pi`$ and flips the sign,

```math
\Psi(t+2\pi)=-\Psi(t).
```

The closed edge traverses two laps, has phase length $`4\pi`$, and returns $`\Psi`$ to itself. Quadratic quantities such as $`\lvert\Psi\rvert^2`$ have period $`2\pi`$, so a quadratic functional on the closed edge descends to the single lap and forgets the Möbius orientation sign.

That loss of sign is the Möbius orientation $`\mathbb{Z}_2`$. The $`120 \to 60`$ halving belongs instead to the central $`-I`$ of $`2I`$, whose parity on integer- and half-integer-spin representations separates the two resolutions. Squaring erases both signs by the same algebraic operation but does not choose the grid, and the two $`\mathbb{Z}_2`$ structures remain distinct.

The promotion gate is the observer clock. The global functional should treat $`N(t)`$ as a variable and ask whether its own lapse equation,

```math
\frac{\delta \mathcal{S}_{\text{MIT}}}{\delta N}=0,
```

forces

```math
N(t)=S(t)^{1/2}
```

without inserting the exponent by hand.

The identity

```math
\Psi^2+S^2=1
```

may enter only as an on-shell constraint relation, with $`S`$ varied as the realized-mode share rather than substituted as $`\sin(t/2)`$ at the start.

A stabilizer-based route to the exponent earns promotion only if the operator-level bridge among the currently unmerged $`3/2`$ structures is supplied with it. A non-stabilizer derivation of the lapse stands on its own.

Until this gate is passed, the variational reading remains program architecture.

Full working program: [Variational Score-to-Sample](variational-score-to-sample.md).

---

*The computation has been run. The dictionary is proved, the coupling is refuted on its route, and the question outside that route stays open.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
