<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Lipschitz Comparison

**Type:** Result
**State:** Closed
**Status (2026-10-05):** Derived. With the edge fixed as parametrized and the core generating, the unbent conic carrier $`M(W)`$ has the least area among Lipschitz carrier-class competitors at every embedded width, and a competitor ties it only by covering it once. This is Proposition 8 of the projective carrier, extending its Proposition 7 from finite-piecewise-smooth competitors. The proof follows Proposition 7's route. Crofton's formula with multiplicity comes from the area formula applied to the map that sends a point and a direction to a line, and the parity of the line count from local degrees. The tie comes from a measure-theoretic form of Proposition 7's step 6, which needs no second fundamental form. The result completes the fixed-edge area comparison for the natural competitor class. It grounds neither the conic realization (1b) nor the fixed edge (1c), and it selects no width.
**Summary:** Whether the conic carrier's least area with its edge fixed, proved for finite-piecewise-smooth competitors, holds for Lipschitz ones, the regularity class of Proposition 6, and with what equality case.
**Inputs:** `projective-carrier.md` (§IX, Propositions 5, 6 and 7, §XI 1b and 1c), `postulate-bridge.md` (the bar)
**Parent:** `projective-carrier.md`

---

RESULT, a derivation with no pre-committed pass condition. [The projective carrier](projective-carrier.md)'s Proposition 7 compares $`M(W)`$ by Crofton's formula with every continuous finite-piecewise-smooth carrier-class competitor at once, and it leaves Lipschitz competitors, Proposition 6's regularity class taken globally, unclaimed. This page proves the comparison, with its equality case, for Lipschitz competitors; there it is Proposition 8. Nothing here selects the carrier, its edge or its width.

**Related:** [The Projective Carrier](projective-carrier.md), [The Fixed-Edge Stability Check](fixed-edge-check.md), [The Carrier's Edge Regimes](carrier-edge-regimes.md), [The Postulate Bridge](postulate-bridge.md).

## I. The Statement

**Proposition 8 (DERIVED; Lipschitz competitors).** Fix an embedded width, $`0 < W < \pi R/2`$, and let $`M'`$ be a Lipschitz map of a Möbius band into $`\mathbb{RP}^3(R)`$ whose boundary map is $`M(W)`$'s edge as parametrized and whose core maps to the generator of $`\pi_1(\mathbb{RP}^3)`$. Then, with area counted with multiplicity,

```math
\mathrm{Area}(M') \ge 4WR = \mathrm{Area}(M(W)).
```

Equality holds exactly when $`M'`$ covers $`M(W)`$ once: almost every point of $`M(W)`$ has one preimage, and the image off $`M(W)`$ has zero area.

The area of a Lipschitz map $`f`$ is $`\int J\,dA`$, with $`J`$ its two-dimensional Jacobian, defined almost everywhere by Rademacher's theorem. By the area formula it equals $`\int N(f, y)\,dH^2(y)`$, where $`N(f, y)`$ counts preimages.

## II. The Setting

- **The glued surface.** Proposition 7's step 1 glues the complementary lune to $`M'`$ along the edge. The result is a Lipschitz map $`f`$ of a projective plane $`\Sigma`$ into $`\mathbb{RP}^3`$, with $`\mathrm{Area}(f) = \mathrm{Area}(M') + 2\pi R^2 - 4WR`$. $`\Sigma`$ carries a smooth structure through a collar of the seam.
- **Its class.** Step 2's argument is for continuous maps, so $`f_*[\Sigma]`$ is the nonzero class of $`H_2(\mathbb{RP}^3; \mathbb Z_2)`$.
- **Notation.**
  - $`\mathcal L`$ is the space of projective lines, with its invariant measure $`d\ell`$.
  - $`n_f(\ell)`$ is the number of points of $`\Sigma`$ that $`f`$ sends into $`\ell`$.
  - $`\Sigma^+`$ is the set where $`f`$ is differentiable with $`J > 0`$, and $`m = J\,dA`$ on it, so $`m(\Sigma^+) = \mathrm{Area}(f)`$.
  - For $`x \in \Sigma^+`$, $`P_x`$ is the projective plane through $`f(x)`$ tangent to $`Df_x(T_x\Sigma)`$.

## III. Three Lemmas

**Lemma A (Crofton with multiplicity).** $`\int_{\mathcal L} n_f\,d\ell = \kappa\,\mathrm{Area}(f)`$, where $`\kappa`$ is Proposition 7's constant, fixed by a projective plane.

*Proof.* Use the homogeneous, Lie-group structure of round $`\mathbb{RP}^3 \cong SO(3)`$ to identify unoriented tangent directions at every point with one $`\mathbb{RP}^2`$. Let $`G(x, \theta)`$ be the line through $`f(x)`$ in direction $`\theta`$.
- **The area formula.** $`G`$ is Lipschitz from the four-dimensional $`\Sigma \times \mathbb{RP}^2`$ to the four-dimensional $`\mathcal L`$. Each point of $`f^{-1}(\ell)`$ gives exactly one preimage of $`\ell`$ under $`G`$. So the area formula gives $`\int J_G = \int n_f\,d\ell`$.
- **The Jacobian.** Where $`f`$ is differentiable, write the invariant density of lines in its local product form: the area element of a plane perpendicular to the line, times the density of directions (Santaló). Moving $`x`$ moves the line's foot in that plane by the projection along $`\theta`$ of $`Df_x\,dx`$. So $`J_G(x, \theta) = c_0\,J(x)\,\lvert\langle \nu_x, \theta\rangle\rvert`$. Here $`\nu_x`$ is the unit normal to $`Df_x(T_x\Sigma)`$, and $`c_0 > 0`$ is a universal constant set by the measures' normalization.
- **The directions.** By rotational invariance, the integral over directions is $`\kappa J(x)`$, with $`\kappa`$ independent of $`\nu_x`$. A projective plane calibrates $`\kappa`$, and nothing depends on $`c_0`$. ∎

This is Santaló's derivation of Crofton's formula, with the area formula supplying the change of variables that a Lipschitz parametrization needs. Crofton's formula for rectifiable sets, a separate theorem, is not needed for a parametrized surface.

**Lemma B (parity).** For almost every line $`\ell`$, $`n_f(\ell)`$ is finite and odd. At each point $`x`$ of $`f^{-1}(\ell)`$, $`f`$ is differentiable, $`Df_x`$ is injective, and $`\ell`$ is transverse to $`Df_x(T_x\Sigma)`$.

*Proof.*
1. *Finite.* This follows from Lemma A.
2. *Good meetings.* Three sets of lines are null.
   - $`f`$ is differentiable off a null set, whose image is $`H^2`$-null. The lines meeting an $`H^2`$-null set form a null set: cover it by balls with $`\sum r_i^2`$ small, and note that the lines meeting a ball of radius $`r`$ have measure at most $`Cr^2`$.
   - The image of $`\lbrace J = 0\rbrace`$ is $`H^2`$-null, by the area formula, so the lines meeting it form a null set too.
   - The pairs $`(x, \theta)`$ with $`\theta`$ tangent to $`Df_x(T_x\Sigma)`$ have $`J_G = 0`$. So, by the area formula, the lines through them form a null set.
3. *Local index.* At a good meeting $`x`$, take a tubular chart about $`\ell`$, and let $`h`$ be $`f`$ followed by projection onto the normal disc, so $`h(x) = 0`$.
   - Transversality makes $`A = Dh(x)`$ invertible, and $`h(x + u) = Au + o(\lvert u\rvert)`$.
   - Take $`r`$ small enough that $`\lvert h(x + u) - Au\rvert < \tfrac12\sigma_{\min}(A)\,r`$ on the circle $`\lvert u\rvert = r`$. Then the straight-line homotopy from $`h`$ to $`A`$ avoids $`0`$ there.
   - So $`h`$ winds $`\mathrm{sgn}\det A = \pm 1`$ times on that circle. No local injectivity is needed.
4. *Parity.*
   - **The approximants.** Choose smooth maps $`f_k \to f`$ uniformly, by Whitney approximation. Once $`f_k`$ is close to $`f`$, the pointwise minimizing geodesics give a homotopy, so $`f_k`$ carries the same nonzero class.
   - **What is imported.** The $`f_k`$ are maps of the closed surface, not carrier competitors. What this step takes from Proposition 7 is step 2's mod-2 intersection argument, which needs only that class: for a line transverse to $`f_k`$, it makes $`n_{f_k}(\ell)`$ odd.
   - **The line.** Fix $`\ell`$ good for $`f`$ and transverse to every $`f_k`$, in the sense of Proposition 7's step 2. The conditions are countably many, so this still leaves almost every line.
   - **The discs.** Take disjoint small discs $`U_i`$ about the points of $`f^{-1}(\ell)`$, on whose boundaries $`h`$ winds $`\pm 1`$ and outside which $`f`$ stays a distance $`\delta`$ from $`\ell`$.
   - **The count.** For large $`k`$, $`f_k^{-1}(\ell)`$ lies in the union of the $`U_i`$. On each $`\partial U_i`$ the projection of $`f_k`$ winds as $`h`$ does, by a homotopy that avoids the center. So each $`U_i`$ holds an odd number of $`f_k`$'s transverse preimages.
   - **Conclusion.** $`n_{f_k}(\ell)`$ and $`n_f(\ell)`$ agree mod 2, so $`n_f(\ell)`$ is odd. ∎

**Lemma C (one plane, covered once).** If $`n_f(\ell) = 1`$ for almost every line, then $`f(\Sigma)`$ lies in one projective plane $`P`$ up to an $`H^2`$-null set, and almost every point of $`P`$ has exactly one preimage.

*Proof.*
1. *Pairs.*
   - Let $`\Psi(x, x')`$ be the line through $`f(x)`$ and $`f(x')`$. It is Lipschitz on each set $`E_j`$ where $`f(x)`$ and $`f(x')`$ lie at least $`1/j`$ apart, but not across the coincidence locus.
   - Almost every line has one preimage under $`f`$, hence none under $`\Psi`$. So the area formula on each $`E_j`$ makes $`J_\Psi = 0`$ almost everywhere, and the union over $`j`$ covers every pair with distinct images.
   - The coincidences form an $`(m \times m)`$-null set: for each $`x`$, the area formula gives $`f^{-1}(f(x)) \cap \Sigma^+`$ no $`m`$-measure.
2. *The secant map's Jacobian.* Take lifts $`p, q \in S^3`$ of $`f(x), f(x')`$, and let $`L = \mathrm{span}(p, q)`$. The tangent space of the space of lines at $`L`$ is $`\mathrm{Hom}(L, \mathbb R^4/L)`$.
   - **The two columns.** A variation $`\dot p`$ at $`p`$ changes only the first generator, giving the homomorphism that sends $`p`$ to $`[\dot p]`$ and $`q`$ to $`0`$. A variation at $`q`$ gives the other column.
   - **When it is invertible.** So $`D\Psi`$ is an isomorphism exactly when both projections, of $`Df_x(T_x\Sigma)`$ and of $`Df_{x'}(T_{x'}\Sigma)`$ into $`\mathbb R^4/L`$, are.
   - **The kernels.** Since $`\dot p \perp p`$, the first projection's kernel is $`Df_x(T_x\Sigma) \cap L`$. That is the line's tangent direction at $`p`$ when the line is tangent to the image there, and zero otherwise; likewise at $`q`$. In $`\mathbb{RP}^3`$ two distinct points lie on exactly one line, so there is no antipodal exception.
   - **The sets A and B.** At pairs in $`\Sigma^+ \times \Sigma^+`$ with distinct images, $`J_\Psi = 0`$ exactly when $`f(x') \in P_x`$ or $`f(x) \in P_{x'}`$. Write $`A`$ for the pairs with $`f(x') \in P_x`$ and $`B`$ for those with $`f(x) \in P_{x'}`$. Then $`A \cup B`$ covers $`\Sigma^+ \times \Sigma^+`$ up to a null set.
3. *A plane.* $`B`$ is $`A`$ with its factors swapped, so $`(m \times m)(A) \ge \mathrm{Area}(f)^2/2`$. So some $`x_0`$ has $`m(\Sigma^+ \cap f^{-1}(P_{x_0})) > 0`$. Set $`P = P_{x_0}`$ and $`\Sigma_P = \Sigma^+ \cap f^{-1}(P)`$.
4. *P at its own points.*
   - $`m(\Sigma_P) > 0`$, and $`J > 0`$ on $`\Sigma^+`$, so $`\Sigma_P`$ has positive area.
   - Almost every point $`x`$ of $`\Sigma_P`$ is a Lebesgue density point of it at which $`f`$ is differentiable with $`J > 0`$. At such a point every cone of directions contains points of $`\Sigma_P`$, whose images lie in $`P`$.
   - So $`Df_x`$ maps $`T_x\Sigma`$ into, hence onto, $`T_{f(x)}P`$, and $`P_x = P`$.
5. *Nothing outside P.*
   - **The section.** Fubini makes the section of $`A \cup B`$ at $`x'`$ $`m`$-full, for $`m`$-almost every $`x' \in \Sigma^+ \setminus f^{-1}(P)`$. So for $`m`$-almost every $`x \in \Sigma_P`$, the pair lies in $`A`$ or $`B`$.
   - **Not in A.** The pair is not in $`A`$, since $`f(x') \notin P = P_x`$. So $`f(x) \in P_{x'}`$.
   - **A second plane.** Then $`P \cap P_{x'}`$ contains the image of a set of positive $`m`$-measure, which has positive area by the area formula. Two distinct projective planes meet in a line, which has no area, so $`P_{x'} = P`$ and $`f(x') \in P`$, a contradiction.
   - **Conclusion.** $`\Sigma^+ \setminus f^{-1}(P)`$ is $`m`$-null, so its image is $`H^2`$-null by the area formula, and so is $`f(\Sigma \setminus \Sigma^+)`$, as in Lemma B. So $`f(\Sigma)`$ lies in $`P`$ up to an $`H^2`$-null set.
6. *Once.* Almost every line meets $`P`$ in one point $`y_\ell`$ and misses $`f(\Sigma) \setminus P`$. So $`n_f(\ell)`$ is the number of preimages of $`y_\ell`$, which is $`1`$. The map $`\ell \mapsto y_\ell`$ carries $`d\ell`$ to a smooth positive density on $`P`$, so almost every point of $`P`$ has exactly one preimage. ∎

## IV. The Proof of Proposition 8

*The inequality.* By Lemmas A and B, $`\mathrm{Area}(f) = \kappa^{-1}\int n_f\,d\ell \ge \kappa^{-1}\int d\ell = 2\pi R^2`$, since almost every line meets a projective plane once. So $`\mathrm{Area}(M') \ge 4WR`$.

*The tie.*
- $`\mathrm{Area}(M') = 4WR`$ exactly when $`\mathrm{Area}(f) = 2\pi R^2`$. Since $`n_f`$ is odd, Lemmas A and B make that the case exactly when $`n_f(\ell) = 1`$ for almost every line.
- Lemma C then gives one plane, covered once. The lune lies in the carrier's $`\mathbb{RP}^2`$ with positive area, so the plane is the carrier's.
- The lune covers its own region once, so $`M'`$ covers $`M(W)`$ once, and its image off $`M(W)`$ has zero area.
- The count is of all preimages, without sign, so in a tie no sheets cancel and none is in excess. Since $`f(\Sigma \setminus \Sigma^+)`$ is $`H^2`$-null, almost every point of $`M(W)`$ has its one preimage in $`\Sigma^+`$, where $`J > 0`$.

Conversely, a map that covers $`M(W)`$ once has area $`4WR`$, by the area formula. ∎

## V. What It Settles, and What It Does Not

- **What it settles.** With the edge fixed as parametrized and the core generating, $`M(W)`$ has the least area among Lipschitz carrier-class competitors at every embedded width, and a competitor ties it only by covering it once. This contains Proposition 6's inequality and strictness, which are local, and Proposition 7's, which are for finite-piecewise-smooth competitors.
- **The route.** The parity count and Crofton's formula hold for Lipschitz maps, and the tie needs no second fundamental form. Proposition 7's own proof stands for its class.
- **What it does not settle.**
  - It does not select the carrier (1b), ground the fixed edge (1c), or select the width.
  - Stability with the edge free stays as [The Carrier's Edge Regimes](carrier-edge-regimes.md) leaves it.
  - The bar's coupling and content clauses are untouched.
  - It is a fixed-edge theorem, not vacuum selection.
- **Beyond Lipschitz.** Competitors of lower regularity are not treated.

## References

- L. A. Santaló, *Integral Geometry and Geometric Probability*, [2nd ed., Cambridge University Press, 2004](https://doi.org/10.1017/CBO9780511617331): the invariant density of lines and Crofton's formula.
- H. Federer, *Geometric Measure Theory*, [Springer, Classics in Mathematics, 1996](https://doi.org/10.1007/978-3-642-62010-2): the area formula for Lipschitz maps and Rademacher's theorem.
- J. M. Lee, *Introduction to Smooth Manifolds*, [Springer, Graduate Texts in Mathematics, 2012](https://doi.org/10.1007/978-1-4419-9982-5): the Whitney approximation theorem for maps into manifolds.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
