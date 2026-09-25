<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The sampler's first test: does the readout resolve sixty labels?

**Type:** Test
**State:** Closed
**Verdict:** Negative
**Status (2026-08-19):** Closed negative twice over: no antipodally-invariant one-boundary surface exists, and equivariance makes the scalar readout identical across all 120 deck translates. The transverse-not-restrictive structural result survives.
**Summary:** Tests whether the Möbius sampler realizes the 120→60 halving geometrically; the first test of the sampler reading.
**Parent:** `postulate-bridge.md`

Run, closed negative, doubly. The first test of the [sampler reading](postulate-bridge.md) is resolved: the sampler does not realize the $`120 \to 60`$ halving geometrically, and it fails for two independent reasons. The geometric one is elementary. No embedded compact surface in $`S^3`$ with a single boundary circle is invariant under the antipodal map (§7), so the deck element $`-1`$ never stabilizes an admissible band, $`\lvert S\rvert`$ is forced odd, and the target $`\lvert S\rvert = 2`$ is unreachable for every boundary. On a generic boundary circle $`S`$ is trivial outright and all $`120`$ lifts stay distinct. The obstruction does not depend on the boundary being a great circle, so no change of boundary curve rescues it. The second reason is independent and would have applied even had the geometry cooperated: equivariance makes the transverse sampler's scalar intensity profile identical on all $`120`$ deck translates (§8), so no invariant scalar readout distinguishes lifts at any stabilizer size, which also corrects the proxy used in §4. What survives untouched is the structural result: the natural Möbius sampler is transverse, not restrictive (§§1-2), since the pullback $`f^*E_\tau`$ is canonically trivial and only the one-sided normal direction carries the twist. Also recorded: the naive form of the intensity question is unfalsifiable, passing even for the zero operator (§3). Group facts verified exactly in [sampler-first-test.test.py](scripts/sampler-first-test.test.py). Step 3, operator separation under the sixty-lift hypothesis, is not run, its necessary geometric condition having failed.

**Related:** [Postulate bridge](postulate-bridge.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md), [Galois pair](../../bedrock/files/galois-pair.md), [engine](../../../README.md).

---

**Goal.** The sampler reading asks whether an admissible sampling operator $`\mathcal O_M`$ intertwines the central $`-1 \in 2I`$ with the Möbius sign ambiguity, so that an intensity observable factors through $`2I/\{\pm 1\} \cong I`$. Stated that way the question is not yet a computation: no $`\mathcal O_M`$ is constructed, and the property as worded is satisfied trivially. This worksheet fixes both problems, then answers the repaired question. It exhibits a canonical candidate operator, isolates the half that can fail, reduces that half to a single stabilizer condition, and proves the condition cannot be met.

**Conventions.** $`X = S^3/2I`$ with $`\pi : S^3 \to X`$ the quotient by the left action of $`2I \subset \mathrm{SU}(2) \cong S^3`$, so $`\pi_1(X) = 2I`$ and the deck group is $`2I`$. A flat bundle $`E_\tau = S^3 \times_{2I} V_\tau`$ is associated to a unitary representation $`\tau`$ of $`2I`$, and a section $`\Psi \in \Gamma(X, E_\tau)`$ is the same thing as an equivariant map $`\widetilde\Psi : S^3 \to V_\tau`$ with $`\widetilde\Psi(\gamma x) = \tau(\gamma)\widetilde\Psi(x)`$. $`M`$ is the Möbius band, $`i : M \to S^3`$ a smooth embedding from the admissible class $`\mathcal A_\gamma`$ of the [Tier 2 ground floor](postulate-bridge.md) (boundary held on a fixed round great circle $`\gamma \subset S^3(R)`$), $`f = \pi \circ i`$, and $`\mathcal L \to M`$ the orientation local system. Throughout, $`\lvert\cdot\rvert`$ on $`V_\tau`$ is a $`2I`$-invariant Hermitian metric.

---

## 1. The pullback carries no twist

The composite $`f = \pi \circ i`$ has a preferred lift to the universal cover, namely $`i`$ itself. Equivalently, $`f_* : \pi_1(M) \to \pi_1(X) = 2I`$ is the trivial homomorphism: the core loop of $`M`$ is a loop in the simply connected $`S^3`$ before it is pushed to $`X`$, so it dies there. Consequently

```math
f^*E_\tau \;=\; i^*\pi^*E_\tau \;=\; i^*(S^3 \times V_\tau) \;=\; M \times V_\tau ,
```

canonically trivialized as a flat bundle, and $`f^*\Psi`$ is the honest $`V_\tau`$-valued function $`\widetilde\Psi \circ i`$ on $`M`$.

This sharpens the second guardrail of the sampler reading. The obstruction is not only that $`\mathcal L`$ has no global nowhere-zero section: the pulled-back section data carries no twist at all, so the $`\mathcal L`$ in the target of $`\mathcal O_M`$ has to be supplied by the geometry of the realization rather than extracted from the field. Any construction that produces it by other means is inserting the twist by hand, and the insertion is the thing to scrutinize.

## 2. A canonical candidate: the twist is transverse

$`M`$ is non-orientable and $`S^3`$ is orientable, so $`M`$ is one-sided and its normal bundle $`\nu`$ is isomorphic, as a flat real line bundle with its induced normal connection, to the orientation local system $`\mathcal L`$ (Fact B of the Tier 2 ground floor). A real line bundle with $`\pm 1`$ transitions is self-dual, so $`\nu^* \cong \mathcal L`$ as well. Since $`\widetilde\Psi`$ is defined on all of $`S^3`$ and not merely on the image of $`i`$, its transverse derivative along the realization exists and is canonically $`\mathcal L`$-valued:

```math
\mathcal O^{(1)}_M(\Psi) \;:=\; \partial_\nu\bigl(\widetilde\Psi\bigr)\big\vert_{i(M)} \;\in\; \Gamma\bigl(M,\ f^*E_\tau \otimes \mathcal L\bigr).
```

The normal direction $`\nu`$ is defined only up to sign, and globally that sign cannot be fixed; the value is therefore not a function but a section of the twisted bundle, which is exactly the required target type. By contrast the plain restriction $`\mathcal O^{(0)}_M(\Psi) = \widetilde\Psi \circ i`$ lands in $`\Gamma(M, f^*E_\tau)`$ with no twist, so it does not have the right type. Combining that with §1:

```math
\boxed{\ \text{the natural Möbius sampler is transverse, not restrictive}\ }
```

The field cannot supply the twist and the restriction does not carry it, so the sampler reads how the field varies across the band rather than its value on it. This statement is independent of how the test below turns out.

$`\mathcal O^{(1)}_M`$ is *a* canonical candidate, not *the* operator. Higher normal jets, weighted combinations, and integral transforms along the transverse direction all produce the same target type, and nothing here selects among them. What $`\mathcal O^{(1)}_M`$ establishes is that the target type is attainable with no arbitrary choice, which was not previously on the record.

## 3. The trap: the naive test cannot fail

Take the question at face value: does an intensity observable factor through $`2I/\{\pm 1\}`$? For any $`\tau`$ and any $`2I`$-invariant metric,

```math
\bigl\lvert \widetilde\Psi(\gamma x)\bigr\rvert^2 \;=\; \bigl\lvert \tau(\gamma)\widetilde\Psi(x)\bigr\rvert^2 \;=\; \bigl\lvert \widetilde\Psi(x)\bigr\rvert^2 \qquad \text{for all } \gamma \in 2I,
```

and in particular at $`\gamma = -1`$, whatever the spin parity of $`\tau`$. Squaring an $`\mathcal L`$-valued section likewise kills the twist, since $`\mathcal L \otimes \mathcal L`$ is canonically trivial. So the intensity is sign-blind, and it is sign-blind for reasons that use nothing about $`M`$, about $`f`$, or about $`\mathcal O_M`$.

Mutation-testing the check confirms it is empty: replace $`M`$ by any other subset of $`S^3`$, or replace $`\mathcal O_M`$ by the zero operator, and the property still holds. A predicate that no candidate can fail is not evidence for any candidate. The "at most sixty" half of the claim is free, and it is not what the sampler reading has to earn.

The engine's own statement of the projection rests on this same sign-blindness and is untouched by anything below: the $`120`$ labels pass to the $`60`$ under $`\lvert\psi\rvert^2`$ because the anti-periodic sign is erased. That argument is sound and independent. The question here is the different one of whether the sampler *also* realizes the halving geometrically, which is what would make the reading produce structure rather than restate it.

## 4. The falsifiable core: the setwise stabilizer

What can fail is the separation half: does the sampler resolve sixty labels, rather than fewer? Make it precise through the lifts. All $`120`$ translates $`\gamma \cdot i(M)`$ have the same image in $`X`$, so they are the lifts of one sampling locus, and the number of distinct lifts is

```math
\#\{\gamma \cdot i(M) : \gamma \in 2I\} \;=\; \frac{120}{\lvert S\rvert}, \qquad S \;=\; \mathrm{Stab}_{2I}\bigl(i(M)\bigr) \ \ \text{(setwise)} .
```

Two verified facts about $`2I`$ convert this into a sharp trichotomy. First, $`2I`$ has exactly one element of order two, namely the central $`-1`$; by Cauchy's theorem every subgroup of even order therefore contains $`-1`$, and the subgroups of odd order are only the trivial group, $`\mathbb Z_3`$, and $`\mathbb Z_5`$. Hence

```math
-1 \in S \iff \lvert S\rvert \ \text{is even} .
```

Second, every element of order four in $`2I`$ squares to $`-1`$, so any $`\mathbb Z_4 \subset 2I`$ contains the centre.

What $`\lvert S\rvert`$ can be is constrained but not to three values. Any element preserving the band preserves its boundary, so $`S \subseteq H := \mathrm{Stab}_{2I}(\gamma)`$, and $`H`$ is cyclic (§6), hence $`S`$ is cyclic and $`\lvert S\rvert`$ divides $`\lvert H\rvert`$. Since the cyclic subgroup orders available in $`2I`$ are $`1, 2, 3, 4, 5, 6, 10`$, the a priori possibilities are:

| $`\lvert S\rvert`$ | lifts | reading |
|---|---|---|
| $`1`$ | $`120`$ | no geometric identification at all |
| $`2`$, so $`S = \{\pm 1\}`$ | $`60`$ | exactly the central halving: the target |
| $`3`$ or $`5`$ | $`40`$ or $`24`$ | collapse from a symmetry unrelated to the centre ($`-1 \notin S`$) |
| $`4`$, $`6`$, $`10`$ | $`30`$, $`20`$, $`12`$ | central halving plus extra symmetry: over-collapse |

The sharp statement is therefore not a three-way split but

```math
\boxed{\ \lvert S\rvert = 2 \iff \text{exactly sixty lifts}\ }
```

with every other order a distinct failure mode of the proposed geometric realization. The odd cases are worth separating from $`\lvert S\rvert = 1`$: they collapse the lift family without the centre doing the work, which would produce a label count the framework does not read and would not be a halving at all. Note also that antipodal invariance alone gives only $`\{\pm 1\} \subseteq S`$, not equality, so it is necessary and not sufficient. The predicate can fail in several distinguishable ways, which is what the naive form lacked. One caveat, established in §8 and stated here so this section is not read at face value: the lift count is a fact about the geometry, but it is not by itself a count of distinguishable *readings*, because equivariance makes the scalar intensity profile agree across all deck translates whatever $`\lvert S\rvert`$ is.

## 5. Group facts, verified

Computed exactly in [sampler-first-test.test.py](scripts/sampler-first-test.test.py), which builds $`2I`$ by closing a generating pair of unit quaternions and checks the closure is a group of order $`120`$ with nine conjugacy classes before asserting anything else.

| Fact | Value |
|---|---|
| Conjugacy classes of $`2I`$ | $`9`$, of sizes $`1, 1, 12, 12, 12, 12, 20, 20, 30`$ |
| Classes closed under $`g \mapsto -g`$ | exactly one, the order-four class of size $`30`$ |
| Behaviour of the rest | the other eight classes are swapped in four pairs |
| Elements of order two | exactly one, the central $`-1`$ |
| Element orders present | $`1, 2, 3, 4, 5, 6, 10`$ (no element of order $`15`$) |
| Squares of order-four elements | all equal $`-1`$ |
| Odd cyclic subgroup orders | $`1, 3, 5`$ |
| Subgroup-circle stabilizers $`2I \cap C`$ | $`C_4`$ on $`15`$ axes, $`C_6`$ on $`10`$, $`C_{10}`$ on $`6`$, $`\{\pm 1\}`$ otherwise |

The last row is the boundary computation of §6, done here because it is pure group theory. Every element of $`2I`$ other than $`\pm 1`$ lies on a unique subgroup circle, indexed by its rotation axis up to sign; grouping the $`118`$ non-central elements by axis gives $`31`$ occupied axes, carrying $`2`$, $`4`$, and $`8`$ non-central elements respectively, so the circle through each contains $`4`$, $`6`$, or $`10`$ elements of $`2I`$ once $`\pm 1`$ are counted. These are the icosahedral symmetry axes: $`15`$ two-fold (edge), $`10`$ three-fold (face), $`6`$ five-fold (vertex), and $`15 + 10 + 6 = 31`$. Every other axis carries no element of $`2I`$ beyond the centre, so its circle has $`2I \cap C = \{\pm 1\}`$.

The first two rows are recorded because they are easy to over-read. Negation acts on $`\mathrm{SU}(2)`$ conjugacy classes by $`\varphi \mapsto \pi - \varphi`$ on the rotation angle, so the order-four class ($`\varphi = \pi/2`$, trace $`0`$) is the unique fixed one. This says something about conjugacy, not about the stabilizer question of §4, and it does not by itself select $`\mathbb Z_4`$ as the band's stabilizer. It is listed because the framework separately names a $`\mathbb Z_4`$ edge stabilizer in the mass sector, and the coincidence of the symbol $`\mathbb Z_4`$ across two different questions is exactly the kind of thing that invites a false identification. The mass-sector $`\mathbb Z_4`$ is about representation content restricted to a cyclic subgroup; the $`S`$ of §4 is a setwise stabilizer of an embedded band. Whether they meet is a question, not a given.

## 6. The computation, in order (as run)

**Step 1, the stabilizer of the boundary: done, and it governs the rest.** For a one-parameter-subgroup circle $`C = \{\exp(tZ)\}`$, left translation gives $`\gamma C = C`$ exactly when $`\gamma \in C`$, because $`1 \in C`$ forces $`\gamma \in \gamma C`$. So $`H = \mathrm{Stab}_{2I}(C) = 2I \cap C`$, a finite subgroup of a circle group and therefore cyclic, which is what makes $`S`$ cyclic in §4. Every such circle contains $`-1`$, since $`\exp(\pi Z) = -1`$ for unit $`Z \in \mathfrak{su}(2)`$, so $`\lvert H\rvert`$ is always even. By §5, $`H`$ is $`C_4`$, $`C_6`$, or $`C_{10}`$ when the axis is one of the $`31`$ icosahedral axes and $`\{\pm 1\}`$ otherwise. The admissible possibilities for $`S`$ follow at once.

| $`H`$ | $`\lvert S\rvert`$ possible | over-collapse reachable |
|---|---|---|
| $`\{\pm 1\}`$ (generic axis) | $`1, 2`$ | no |
| $`C_4`$ (15 edge axes) | $`1, 2, 4`$ | yes |
| $`C_6`$ (10 face axes) | $`1, 2, 3, 6`$ | yes |
| $`C_{10}`$ (6 vertex axes) | $`1, 2, 5, 10`$ | yes |

A generic boundary circle is therefore the clean case: $`S \subseteq \{\pm 1\}`$ leaves only $`\lvert S\rvert \in \{1, 2\}`$, so over-collapse and the odd unrelated-symmetry cases are excluded before any geometry is attempted, and the test becomes binary. Which circle the postulate's boundary actually is remains a choice to record explicitly, not an assumption to make quietly; if it sits on one of the $`31`$ special axes, symmetry-breaking becomes part of the construction problem.

**Step 2, the single existence question.** With the boundary fixed, everything reduces to

```math
\exists\, i(M) \in \mathcal A_\gamma \ \ \text{with} \ \ \mathrm{Stab}_{2I}\bigl(i(M)\bigr) = \{\pm 1\}\ ?
```

This one equality carries both halves: $`-1 \in S`$ is antipodal invariance of the whole band, not merely of its boundary curve, and $`S \subseteq \{\pm 1\}`$ is the exclusion of extra symmetry. On a generic boundary the second half is automatic, so the question collapses further to whether an antipodally invariant admissible band exists at all. Section 7 shows it does not.

**Step 3, the operator, not run.** Under the sixty-lift hypothesis one would ask whether $`\mathcal O^{(1)}_M`$ separates the sixty lifts. Step 2 is a necessary condition for that hypothesis and it fails, so this step is not reached.

## 7. The obstruction

> **Proposition.** Let $`\Sigma \subset S^3`$ be a compact embedded surface with exactly one boundary circle. Then $`\Sigma`$ is not invariant under the antipodal map $`a(x) = -x`$.

*Proof.* Suppose $`a(\Sigma) = \Sigma`$. The antipodal map is free on $`S^3`$, hence free on $`\Sigma`$, so the quotient $`N = \Sigma/\langle a\rangle`$ is a compact surface embedded in $`S^3/\langle a\rangle = \mathbb{RP}^3`$, with $`\partial N = (\partial\Sigma)/\langle a\rangle`$.

Since $`a`$ preserves $`\Sigma`$ it preserves $`\partial\Sigma`$, which by hypothesis is a single circle. So $`\partial\Sigma \to \partial N`$ is a connected double cover of a circle by a circle, and a lift of the loop $`\partial N`$ to $`S^3`$ is a path from a point to its antipode rather than a closed loop. Hence $`\partial N`$ represents the nontrivial element of $`\pi_1(\mathbb{RP}^3) = \mathbb Z/2`$, and

```math
[\partial N] \neq 0 \quad \text{in } H_1(\mathbb{RP}^3; \mathbb F_2) \cong \mathbb F_2 .
```

On the other hand $`N`$ is a compact surface, so it carries a mod-$`2`$ fundamental class $`[N, \partial N] \in H_2(N, \partial N; \mathbb F_2)`$ whether or not it is orientable, which is why $`\mathbb F_2`$ is the right coefficient ring here. Exactness of the pair sequence

```math
H_2(N, \partial N; \mathbb F_2) \xrightarrow{\ \partial\ } H_1(\partial N; \mathbb F_2) \xrightarrow{\ \iota_*\ } H_1(N; \mathbb F_2)
```

gives $`\iota_*[\partial N] = 0`$, and pushing forward along $`N \hookrightarrow \mathbb{RP}^3`$ gives $`[\partial N] = 0`$ in $`H_1(\mathbb{RP}^3; \mathbb F_2)`$. That contradicts the previous display. $`\square`$

The homology used is the standard cellular computation: $`\mathbb{RP}^3`$ has one cell in each dimension with vanishing mod-$`2`$ boundary maps, so $`H_1(\mathbb{RP}^3; \mathbb F_2) \cong \mathbb F_2`$ generated by the projective line $`\mathbb{RP}^1`$. When $`\gamma`$ is a great circle, $`\gamma`$ is the intersection of $`S^3`$ with a $`2`$-plane through the origin, that plane is preserved by $`a`$, and $`\gamma/\langle a\rangle`$ is exactly that $`\mathbb{RP}^1`$.

**Scope, and why no boundary curve rescues it.** The proof uses only that $`\partial\Sigma`$ is a single connected circle, which the Möbius band forces, and never that it is a great circle. Changing the boundary curve therefore cannot help. What the argument does not cover, correctly, is surfaces with two or more boundary circles: there $`a`$ may swap components, $`\partial N`$ can carry the trivial class, and no contradiction arises. Closed invariant surfaces are likewise untouched, as they must be, since the great $`2`$-sphere is antipodally invariant with quotient $`\mathbb{RP}^2 \subset \mathbb{RP}^3`$.

**Consequence for the stabilizer.** No admissible band is antipodally invariant, so $`-1 \notin S`$ always. By the verified equivalence of §4 ($`-1 \in S`$ if and only if $`\lvert S\rvert`$ is even), $`\lvert S\rvert`$ is odd, so $`S`$ is an odd-order subgroup of $`H`$. The taxonomy collapses to:

| $`H`$ | surviving $`S`$ | lifts |
|---|---|---|
| $`\{\pm 1\}`$ (generic axis) | $`1`$ | $`120`$ |
| $`C_4`$ (15 edge axes) | $`1`$ | $`120`$ |
| $`C_6`$ (10 face axes) | $`1`$ or $`C_3`$ | $`120`$ or $`40`$ |
| $`C_{10}`$ (6 vertex axes) | $`1`$ or $`C_5`$ | $`120`$ or $`24`$ |

The target $`\lvert S\rvert = 2`$ is unreachable for every boundary. On a generic axis, the case §6 called clean because it excluded over-collapse, $`S`$ is forced trivial and all $`120`$ lifts remain distinct. The only surviving collapses are the odd ones, $`40`$ or $`24`$ lifts on special axes, and those are precisely the failure mode in which the centre does no work at all: a collapse driven by a symmetry unrelated to the $`\mathbb Z_2`$ the reading is about.

A caution carried from the corpus bears directly on the proof above, which turns on the antipodal map of the ambient $`S^3`$. The first-eigenvalue pillar also has an antipodal quotient in its construction, the double lune on the covering $`S^2(R)`$ whose antipodal quotient is the band. These are antipodal maps on different spheres serving different purposes, and they must not be merged. The pillar's is intrinsic to the band's own covering geometry; the one here is the deck action on the ambient $`S^3`$. Any statement that slides between them is the failure mode already recorded on this program, a number computed on a valid object and narrated on an invalid one.

## 8. The second obstruction: equivariance

The geometric obstruction is not the only one, and the other is independent of it. Write $`L_g(x) = gx`$ for the deck action. Equivariance $`\widetilde\Psi \circ L_g = \tau(g)\widetilde\Psi`$ differentiates to

```math
d\widetilde\Psi_{gx}\bigl(dL_g\, v\bigr) = \tau(g)\, d\widetilde\Psi_x(v),
```

since $`\tau(g)`$ is a constant linear map. If $`v = \nu_x`$ is normal to $`M`$ at $`x`$ then $`dL_g\nu_x`$ is normal to $`gM`$ at $`gx`$, and because $`L_g`$ is an isometry of the round $`S^3`$ it carries unit normals to unit normals, which is what makes the following exact rather than true up to scale:

```math
\boxed{\ \mathcal O^{(1)}_{gM}(\Psi)(gx) \;=\; \tau(g)\,\mathcal O^{(1)}_M(\Psi)(x)\ }
```

Since $`\tau`$ is unitary, $`\bigl\lvert\mathcal O^{(1)}_{gM}(\Psi)(gx)\bigr\rvert^2 = \bigl\lvert\mathcal O^{(1)}_M(\Psi)(x)\bigr\rvert^2`$ pointwise, and since $`L_g`$ preserves volume, $`\int_{gM}\lvert\mathcal O^{(1)}_{gM}\Psi\rvert^2 = \int_M \lvert\mathcal O^{(1)}_M\Psi\rvert^2`$. The scalar intensity profile is therefore the same on every deck translate, transported.

**This corrects §4 as well as reinforcing §7.** Section 4 used the number of distinct lifts, $`120/\lvert S\rvert`$, as the proxy for the number of distinguishable readings. The lemma says the readings coincide across translates whatever $`\lvert S\rvert`$ is, so even had $`S = \{\pm 1\}`$ been achievable, the sixty lifts would have carried identical intensity profiles and nothing would have been resolved at sixty either. The lift count is a real fact about the geometry, but it was never observable through the scalar readout that the test named. So the first test was obstructed twice over, and independently: the geometry cannot produce $`S = \{\pm 1\}`$, and an invariant scalar readout cannot distinguish deck translates in any case.

Recording this matters more than the redundancy suggests. Without it, a successor program can quietly rebuild the same unfalsifiable test in another form, asking again which deck copy is being observed. The $`120`$ translated bands are symmetry-related presentations of the same quotient data, and no invariant scalar observable will ever tell them apart.

## 9. What the negative does and does not say

**What is closed.** The central $`2I`$ halving cannot be implemented as setwise antipodal symmetry of a one-boundary sampler. That is a route-specific theorem in the same spirit as the restriction-route negative of Steps 1 to 4 on the [bridge](postulate-bridge.md): a definite mechanism is excluded by a definite argument, with the scope stated. The proposal that the geometry of the lift family explains $`120 \to 60`$ is dead, and it should not be rescued by modifying the band, since the obstruction is insensitive to the boundary curve.

**What is untouched.** The engine's projection stands exactly as it stood. It never rested on the sampler: the $`120`$ labels pass to the $`60`$ under $`\lvert\psi\rvert^2`$ because the anti-periodic sign is erased, an argument in the representation theory alone (§3). This worksheet asked whether the sampler *additionally* realizes that halving geometrically, and the answer is no. Nothing about the label count itself is disturbed.

*Added 2026-09-25: the engine's statement of the projection has since changed. Both grids use the same readout, the intensity ([linear readout](scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go)), sign-blind in every sector as §3 shows, so sign-blindness cannot sort observables between the 120 and 60R grids; the engine now states the grids as resolutions, with the assignment of observables to them motivated ([engine](../../../README.md#the-sampling-grids)). This worksheet's result is unaffected.*

**What survives as the result.** The structural observation of §§1-2 does not depend on the test at all. The pullback $`f^*E_\tau`$ is canonically trivial, so the field cannot supply the twist, while $`\nu \cong \mathcal L`$ makes the transverse direction supply it for free. The sampler is transverse, not restrictive. That is the durable output of this worksheet, and it is a sharper statement of what a Möbius readout is than the reading began with.

**What the negative sharpens.** Route 1 already showed the two $`\mathbb Z_2`$'s cannot be identified algebraically, since $`2I`$ is perfect and has no order-two character. This adds that they cannot be identified through setwise antipodal symmetry of the sampler either. The central $`2I`$ sign and the Möbius normal sign are independent structures, and the architecture is better for saying so plainly than it would be with a coincidence to defend.

**The pattern, named carefully.** Two obstructions of the same conceptual shape now sit on this reading, and neither is a universal independence claim, which the corpus rightly refuses. The safer name is non-identification by obstruction:

| | statement |
|---|---|
| Algebraic non-identification | $`\mathcal L`$'s $`\mathbb Z_2`$ cannot be a $`2I`$ character (Route 1: $`2I`$ is perfect) |
| Geometric non-identification | $`\mathcal L`$'s sign cannot be realized by antipodal setwise symmetry of a one-boundary sampler (§7) |

Both say $`\mathbb Z_2^{\text{Möbius}} \neq \mathbb Z_2^{\text{centre}}`$ as *identified* structures, while leaving open that both may participate in one eventual observation mechanism. That distinction is the whole content, and it should not be compressed into a claim of independence.

**The successor question.** Not whether the band turns $`120`$ lifts into $`60`$: §8 shows no invariant scalar readout can address that at all. The question is what spectral information the sampler transfers:

```math
\boxed{\ \text{what does } \mathcal O^{(1)}_M \text{ transfer from the ambient mode space into the twisted Möbius channel?}\ }
```

Concretely, for an ambient eigenspace $`E^\tau_\lambda`$ and a twisted Möbius eigenspace $`F_\mu`$ with projector $`P_\mu`$, study the transfer operator $`T^{(\tau)}_{\mu\lambda} = P_\mu \circ \mathcal O^{(1)}_M\big\vert_{E^\tau_\lambda}`$ through $`\mathrm{rank}\,T^{(\tau)}_{\mu\lambda}`$ or $`\lVert T^{(\tau)}_{\mu\lambda}\rVert^2_{\mathrm{HS}}`$. The failure modes are real ones: $`T = 0`$ means the channel does not couple those modes; $`T \neq 0`$ but representation-blind means the sampler works mathematically and explains none of the discrete structure; nontrivial selection rules would mean it filters latent modes; and a distinguished dependence on the existing $`2I`$ and $`E_8`$ representation data would connect the sectors without identifying their $`\mathbb Z_2`$'s. The canonical trivialization of §1 keeps the bookkeeping clean, since $`f^*E_\tau \otimes \mathcal L \cong (M \times V_\tau) \otimes \mathcal L`$ splits the target into $`\Gamma(M,\mathcal L) \otimes V_\tau`$.

Two guards belong on that question before it is opened. First, it must not resurrect the dead $`2/R^2`$ arch: projecting onto a known twisted Möbius mode measures a coupling matrix element $`\langle \phi_{\text{Möb}}, \mathcal O^{(1)}_M\Psi\rangle`$, which asserts nothing about equality of the surface and ambient spectra. Second, and this is where the corpus has been burned before, the eigenspaces $`F_\mu`$ must be those of a named operator on the *embedded* band's induced metric. The [first-eigenvalue pillar](../../bedrock/files/first-eigenvalue.md) solves an intrinsic conic geometry with no embedding in $`S^3`$ asserted, so its eigenvalues may not be imported here without a derivation. Importing them silently would be the recorded failure of computing on a valid object and narrating on an invalid one. None of this is set up here.

## 10. Scope and non-claims

The negative is route-specific and is not a universal independence claim: it excludes setwise antipodal symmetry of a one-boundary sampler as the mechanism, not every conceivable relation between the two $`\mathbb Z_2`$'s. Nothing here asserts that $`\mathcal O^{(1)}_M`$ is the right operator, only that it is canonical and has the correct target type; the negative concerns the geometry of the lift family and does not evaluate the operator, which was Step 3 and is not reached. Nothing here couples to the $`2I`$-decorated gauge sector: this is the sampling half of the postulate, and the Galois side is untouched, exactly as the Tier 2 ground floor is the surface half only. Nothing here is dynamical; which admissible band is realized is Tier 2's question, and this worksheet takes the band as given. The surface pillar is not in play: its twisted spectrum and its $`2/R^2`$ first positive level are an independent result about the band's own intrinsic geometry, and no eigenvalue of that problem enters any statement above. The bar of the [postulate bridge](postulate-bridge.md) is unchanged and unmet.

---

*The sampler is transverse, not restrictive. The lift family is not what halves the labels: the geometry cannot arrange it, and equivariance would have hidden it anyway. What a Möbius readout does is transfer modes, not name copies.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
