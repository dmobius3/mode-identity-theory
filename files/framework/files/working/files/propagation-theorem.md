<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Propagation Theorem

**Type:** Result
**State:** Closed
**Status (2026-10-09):** Derived, checked by one script. If the declared carrier of light and standard rulers lies in the class below, and the effective metric is required to metricize its cone with the domain's symmetry, light sees closed, round slices. On $`S^3/2I`$, every real characteristic sheet of a linear differential operator in the class (order at most five, equivariant under the domain's transitive symmetry, with a real scalar principal symbol) is a round cone, apart from the sheet $`\xi_0 = 0`$ that odd orders carry. At order two a hyperbolic operator's cone fixes the conformal class of $`-c(t)\,dt^2 + h`$, with $`h`$ the round metric, and the scale of a metric representative needs a declared standard. The second-order statement needs only an isotropy that acts irreducibly on the tangent space, so it holds on $`S^3/2T`$ and $`S^3/2O`$ too; under the right action it fails on lens and prism spaces. Matrix symbols, order six and above, nonlocal, nonlinear or non-homogeneous laws, and a separate effective manifold lie outside it.
**Summary:** What a local, symmetric light carrier on the static domain lets light see: round characteristic cones, and so closed, round slices for any metric representative with the domain's symmetry. The first target the stress-tensor bridge named in its §X.
**Inputs:** `stress-tensor-bridge.md` (§III, §VI, §X), `molien-p1-bridge.md` §II, `missing-spatial-projection.md` §III, `scripts/propagation-theorem/propagation_check.py`
**Parent:** `stress-tensor-bridge.md`

---

RESULT, a derivation with no pre-committed pass condition. If the declared carrier of light and standard rulers lies in the class of §I, and the effective metric is required to metricize its cone with the domain's symmetry, light sees closed, round slices.
- [The stress-tensor bridge](stress-tensor-bridge.md) named this as its first target (§X, 2026-10-09), at second order. This page proves it and extends it to every order below six.
- The principal symbol fixes the cone and no more. The scale of a metric, and with it proper distances and redshifts, needs a declared standard (§III).
- The page does not say which law carries light. A carrier outside the class is not excluded, and §IV lists what lies outside.

**Related:** [The Stress-Tensor Bridge](stress-tensor-bridge.md), [The P1 Bridge](molien-p1-bridge.md), [The Missing Spatial Projection](missing-spatial-projection.md), [The Effective-Metric Floors](effective-metric-floors.md).

---

## I. The setting

**The domain.** $`M = S^3/2I`$, with the round metric $`h`$ of curvature radius $`R`$, is the quotient of $`SU(2)`$ by $`2I`$ acting on the left. Right multiplication, $`[x] \mapsto [xb]`$, is a transitive isometric action of $`SU(2)`$. The isotropy of a point is a conjugate of $`2I`$, acting on its tangent space through the image $`A_5`$ of $`2I`$ in $`SO(3)`$ ([The P1 Bridge](molien-p1-bridge.md) §II). Spacetime is $`\mathbb{R} \times M`$, with time $`t`$.

**The bundles.** A flat bundle $`E_\rho`$ has as sections the functions $`\phi : SU(2) \to V_\rho`$ with $`\phi(\gamma x) = \rho(\gamma)\,\phi(x)`$ for $`\gamma \in 2I`$; the trivial $`\rho`$ gives the functions on $`M`$.
- **The lift.** The right action lifts to sections as $`(R_b\phi)(x) = \phi(xb)`$.
- **The acting group.** Since $`\phi(-x) = \rho(-1)\,\phi(x)`$, on a spinorial bundle, where $`\rho(-1) = -1`$, the element $`-1`$ acts by $`-1`$. The acting group is $`SU(2)`$, not $`SO(3)`$.
- **The fibre.** By the same property, the isotropy $`2I`$ of the point $`[1]`$ acts on the fibre there by $`\rho`$.

**The class.** A linear differential operator $`P`$ of order $`m`$ on sections of $`E_\rho`$ over $`\mathbb{R} \times M`$ is in the class when:
- it commutes with the lifted right action, so its coefficients are homogeneous under the domain's symmetry, though they may depend on $`t`$;
- its principal symbol is real and scalar: $`\sigma_m(P)(t, x; \xi_0, \xi) = q(t, x; \xi_0, \xi)\,\mathrm{Id}`$, with $`q`$ real.

Where rays are needed (§III), $`P`$ is also strictly hyperbolic in $`t`$: for $`\xi \neq 0`$, $`q`$ has $`m`$ distinct real roots in $`\xi_0`$.

## II. The theorem

**Theorem.** Let $`P`$ be in the class, of order $`m \le 5`$. Then

```math
q(t, x; \xi_0, \xi) = \sum_{0 \le 2k \le m} a_k(t)\, \xi_0^{\,m-2k}\, \lvert\xi\rvert_h^{2k},
```

independent of $`x`$. Every real characteristic sheet is one of two kinds:
- a round conic sheet $`\xi_0^2 = c(t)\,\lvert\xi\rvert_h^2`$ with $`c(t) > 0`$;
- or the sheet $`\xi_0 = 0`$, which every odd order carries.

If $`m = 2`$ and $`P`$ is hyperbolic, then up to an overall sign $`q = -A(t)\,\xi_0^2 + B(t)\,\lvert\xi\rvert_h^2`$ with $`A, B > 0`$. The characteristic cone is then the null cone of every metric in the conformal class

```math
\big[\, -c(t)\,dt^2 + h \,\big], \qquad c = B/A .
```

**Proof.** *Symmetry.* Equivariance makes the principal symbol equivariant.
- An element $`\gamma`$ of the isotropy at $`[1]`$ acts on covectors through $`A_5`$ and on the fibre by $`\rho(\gamma)`$. So $`q(\gamma \cdot \xi)\,\mathrm{Id} = \rho(\gamma)\, q(\xi)\, \rho(\gamma)^{-1} = q(\xi)\,\mathrm{Id}`$.
- The fibre action cancels because the symbol is scalar, so $`q(t, [1]; \xi_0, \cdot)`$ is invariant under $`A_5`$, which fixes $`\xi_0`$.
- Transitivity carries this to every point.

*Invariants.* Write $`q = \sum_j \xi_0^{\,m-j}\, P_j(\xi)`$, with each $`P_j`$ homogeneous of degree $`j`$ and invariant under $`A_5`$.
- From $`A_5`$'s characters, its invariant polynomials on $`\mathbb{R}^3`$ of degrees 0 to 6 span spaces of dimensions 1, 0, 1, 0, 1, 0 and 2; §VI checks this two ways.
- So below degree 6 they are spanned by 1, $`\lvert\xi\rvert_h^2`$ and $`\lvert\xi\rvert_h^4`$, as for $`SO(3)`$.
- Hence $`P_j`$ is a multiple of $`\lvert\xi\rvert_h^j`$ for even $`j \le 5`$, and $`P_j = 0`$ for odd $`j`$.

*Sheets.* $`q`$ is homogeneous in $`\xi_0`$ and $`\lvert\xi\rvert_h`$, with only even powers of $`\lvert\xi\rvert_h`$. So it factors over $`\mathbb{C}`$ as $`a\,\xi_0^{\varepsilon}\,\lvert\xi\rvert_h^{2\delta} \prod_r (\xi_0^2 - c_r\,\lvert\xi\rvert_h^2)`$, with $`a \neq 0`$ and every $`c_r \neq 0`$.
- $`\varepsilon`$ is odd exactly at odd orders, since $`m = \varepsilon + 2\delta + 2n`$, with $`n`$ the number of factors in the product.
- The factor $`\lvert\xi\rvert_h^{2\delta}`$, present only when the leading coefficient $`a_0`$ vanishes, is zero only at $`\xi = 0`$.
- So a real root with $`\xi \neq 0`$ is $`\xi_0 = 0`$, or $`\xi_0 = \pm\sqrt{c_r}\,\lvert\xi\rvert_h`$ with $`c_r`$ real and positive. Each real sheet is round, or is $`\xi_0 = 0`$, and no hyperbolicity has been used.
- If $`m = 2`$ and $`P`$ is hyperbolic, the single factor has $`c = B/A > 0`$. The Lorentzian metrics with this null cone are exactly the conformal multiples of $`-c\,dt^2 + h`$. ∎

**What the proof uses.** At $`m = 2`$ it uses only that the isotropy acts irreducibly on the tangent space. Then no covector is invariant, so there is no $`\xi_0\,\xi`$ term, and by Schur's lemma only one quadratic form is, so the spatial part is round.
- **Where else it holds.** It holds on $`S^3/2T`$ and $`S^3/2O`$ as well. On $`S^3`$ and $`\mathbb{RP}^3`$, under the full isometry group, whose isotropy is $`SO(3)`$, it holds at every order: the standard representation of $`SO(3)`$ is irreducible, and its invariants are the powers of $`\lvert\xi\rvert^2`$ in every degree.
- **Where it fails, under the right action.** There the symmetry no longer forces roundness, and non-round symbols in the class exist:
  - on the lens space $`L(5,1)`$, whose isotropy leaves a covector and two quadratic forms invariant;
  - on the prism space of the binary dihedral group of order 20, whose isotropy leaves two quadratic forms invariant;
  - on $`S^3`$ or $`\mathbb{RP}^3`$ under the right action alone, whose isotropy acts trivially.
- **Higher orders.** From $`m = 3`$ on, the statement uses $`A_5`$'s invariants. $`2T`$ has a cubic invariant and $`2O`$ a second quartic one, so on those quotients the statement stops at orders 2 and 3 respectively.

## III. Rays and distances

**Rays.** Let $`P`$ also be strictly hyperbolic. Then $`\partial q/\partial\xi_0 \neq 0`$ on each real sheet, so each sheet is of real principal type.
- **The scalar case.** For scalar operators of real principal type, wavefront sets propagate along the bicharacteristics ([Duistermaat and Hörmander](https://doi.org/10.1007/BF02392165)).
- **The bundle-valued case.** With a scalar principal symbol, Dencker's theorem for systems of real principal type gives the corresponding propagation of polarization sets along the same flow ([Dencker](https://doi.org/10.1016/0022-1236%2882%2990051-9)). The flow depends on the principal symbol alone.
- **A round sheet.** $`\xi_0^2 = c(t)\,\lvert\xi\rvert_h^2`$ is the null cone of $`-c(t)\,dt^2 + h = -d\eta^2 + h`$, with $`d\eta = \sqrt{c}\,dt`$. Its rays therefore run along geodesics of $`h`$, the images of great circles, and cover the arclength $`\chi = \int \sqrt{c}\,dt`$.
- **Several sheets.** At orders 4 and 5, each propagating sheet has its own $`c_r`$, so its rays have their own $`\chi`$, and no single metric carries them all.
- **The sheet $`\xi_0 = 0`$.** Strict hyperbolicity allows it only at odd orders, where it is simple. Its Hamilton flow runs in the time direction alone, so its singularities are spatially stationary.

**What the cone fixes.** The principal symbol fixes the cone, and so at second order it fixes only the conformal class.
- **No scale from propagation.** Multiplying $`P`$ by a nowhere-zero $`f(t)`$ leaves its solutions and its cone unchanged and rescales $`A`$ and $`B`$ together. So the propagation law fixes the ray paths and $`\chi`$, and no metric scale.
- **Symmetric representatives.** A metric representative invariant under the domain's symmetry has the form $`\Omega(t)^2\,[-c(t)\,dt^2 + h]`$, whose slices are closed and round, of curvature radius $`\Omega R`$.
- **Flat representatives.** The round sphere is conformally flat, so representatives with flat slices exist, but only on an open patch, where they break the transitive symmetry ([the stress-tensor bridge](stress-tensor-bridge.md) §III).
- **Fixing the scale.** Fixing $`\Omega`$, and with it proper sizes and redshifts, needs a declared standard. One instance is a mass term held constant in a fixed normalization, since the lower-order terms carry the scale.

**Distances, per image.**
- **On the cover.** On $`S^3`$, along a unit-speed geodesic of $`h`$ from the observer, a transverse Jacobi field solves $`f'' = -f/R^2`$ with $`f(0) = 0`$ and $`f'(0) = 1`$. So the transverse factor is $`R\sin(\chi/R)`$.
- **On the quotient.** An image on the quotient arrives along a lifted geodesic and inherits that factor.
- **Several images.** The shortest translation in $`2I`$ is by $`\pi/5`$, so the injectivity radius is $`\pi R/10`$. Beyond it, geodesics from the observer need not be unique, and a source can have several images, each with its own $`\chi`$.
- **Comoving terms.** In comoving terms, which the propagation law fixes, an object of $`h`$-size $`\ell_h`$ subtends $`\ell_h/(R\sin(\chi/R))`$, which a statistically isotropic ruler reads through angles.
- **With a declared representative.** $`D_A = \Omega(t_e)\,R\sin(\chi/R)`$ and $`D_M = \Omega_0\,R\sin(\chi/R)`$, where $`\Omega_0`$ is $`\Omega`$ at observation. Setting $`\Omega_0 = 1`$ makes $`R`$ the curvature radius there.

## IV. What it does not close

The theorem closes its class and nothing beyond it. Outside lie:
- matrix principal symbols, as for operators on the larger slot bundles whose symbol is not a multiple of the identity: the named open case;
- order six and above, where $`A_5`$ has a second sextic invariant;
- operators that break the domain's homogeneity;
- nonlinear propagation;
- nonlocal laws, including pseudodifferential operators, whose invariant symbols need not be polynomials;
- laws without real principal type, for rays: non-hyperbolic laws with no finite speed;
- propagation on a separate effective manifold.

## V. Bearing on the bridge

The theorem establishes two things for a carrier in the class:
- every real characteristic sheet, apart from $`\xi_0 = 0`$ at odd orders, is a round cone over the closed domain;
- at second order, the cone fixes the conformal class of $`-c(t)\,dt^2 + h`$.

[The stress-tensor bridge](stress-tensor-bridge.md) adopts flat effective slices (§VI), and types branch (b) as needing an effective propagation that admits a metric (§III). It also records that the closed domain carries no flat metric at all.

Suppose branch (b)'s $`g_\text{eff}`$ is required to metricize the cone of a declared carrier in this class, and to share the domain's symmetry. Then its slices are closed and round, and in comoving terms its distance relation is $`D_M = R\sin(\chi/R)`$ at $`\Omega_0 = 1`$. So a flat $`g_\text{eff}`$ needs one of three things:
- a carrier outside the class;
- a representative that gives up the domain's symmetry on an open patch;
- or giving up that metricization.

A closed $`g_\text{eff}`$ owes the comparison with the nonflat distance relation, which §VI says accepting it would require. (DERIVED, given the declarations of §I.)

## VI. Checks

[`propagation_check.py`](scripts/propagation-theorem/propagation_check.py) needs numpy and sympy, and its record [`propagation_check.out`](scripts/propagation-theorem/propagation_check.out) reproduces byte for byte from it. It is a floating-point cross-check of the proof, not a replacement for it. It builds $`2I`$, $`2O`$ and $`2T`$ as quaternions and checks that each is closed, then checks:
- the isotropy: $`A_5`$ leaves no covector and one quadratic form invariant, and so do the images of $`2O`$ and $`2T`$;
- the invariants of $`A_5`$ by degree, from 0 to 16 from characters, and from 0 to 6 again from the rank of the Reynolds average at random points;
- on the two-dimensional slot bundle, that $`\phi(x) = x\,v`$ is a section and that the right action of $`-1`$ acts on it by $`-1`$;
- distances: the round $`S^3`$ of radius $`R`$, with its metric induced from the embedding in $`\mathbb{R}^4`$, satisfies $`\mathrm{Ric} = 2g/R^2`$, so its curvature is $`1/R^2`$. Its transverse Jacobi field along a unit-speed geodesic is $`R\sin(\chi/R)`$, the metric's own transverse factor;
- the shortest translation in $`2I`$.

Five mutation arms, one per claim, each turn it red:
- the lens space $`L(5,1)`$, the prism space of order 20 and trivial isotropy each leave more than one quadratic form;
- $`2T`$ has a cubic invariant and $`2O`$ a second quartic one;
- on the adjoint bundle, $`-1`$ acts by $`+1`$;
- the flat $`\mathbb{R}^3`$, embedded the same way, has curvature 0 and Jacobi factor $`\chi`$;
- $`2O`$'s shortest translation is $`\pi/4`$.

## References

- J. J. Duistermaat and L. Hörmander, "Fourier integral operators. II", [Acta Math. 128, 183–269 (1972)](https://doi.org/10.1007/BF02392165).
- N. Dencker, "On the propagation of polarization sets for systems of real principal type", [J. Funct. Anal. 46, 351–372 (1982)](https://doi.org/10.1016/0022-1236%2882%2990051-9).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
