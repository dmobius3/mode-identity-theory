<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# ❸ Coexact Gap

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/Coeaxact%20Gap.png" width="100%" alt="Coexact Gap">

On the round three-sphere and its quotients by finite groups of rotations, the Hodge Laplacian on twisted coexact $`1`$-forms has a lowest nonzero eigenvalue, the spectral gap $`q_\tau^2/R^2`$, where $`q_\tau \ge 2`$ is the lowest coexact level carrying a constituent of the twisting representation $`\tau`$. A constituent at McKay distance $`d`$ enters at level $`d`$ for $`d \ge 2`$ and at level $`2`$ for $`d = 0`$, for any finite $`\Gamma`$; when $`-I \in \Gamma`$, equivalently when the McKay graph is bipartite, a distance-one constituent enters at level $`3`$. Here $`q_\tau`$ is the minimum of these entry levels over the constituents of $`\tau`$, so in particular the gap is $`d_\tau^2/R^2`$ whenever $`d_\tau \ge 2`$.

The adjoint bundle of an irreducible flat $`\mathrm{SU}(2)`$ connection, the coefficient system gauge theory asks for, always has $`d_\tau \ge 2`$, so its gap is the squared adjoint distance. Across the ADE classification of finite subgroups of $`\mathrm{SU}(2)`$ this gap is $`4/R^2`$ for every irreducible flat connection, with one exception: the Galois-conjugate connection on the Poincaré homology sphere $`S^3/2I`$ gives $`36/R^2`$. The exception reflects two related features of $`2I`$, the unique nontrivial perfect finite subgroup of $`\mathrm{SU}(2)`$: its perfectness prevents $`Q^\prime`$ from being a character twist of $`Q`$, while the distinct adjoint $`\mathrm{Sym}^2 Q^\prime`$ separately occupies the $`3`$-dimensional node at distance six in affine $`E_8`$, on the short branch; every other adjoint has its nearest constituent at distance two. The ingredients are classical: the form spectra of Ikeda and Taniguchi, the representation-theoretic descent of Lauret, Miatello and Rossetti, and the McKay correspondence.

---

## 1. Introduction

On a homogeneous spherical space form $`S^3/\Gamma`$ of radius $`R`$, the coexact spectral gap of a flat bundle is a McKay-graph quantity: whenever the nearest constituent of the twisting representation lies at graph distance at least two from the trivial node of the affine ADE diagram of $`\Gamma`$, the gap is the square of that distance divided by $`R^2`$. The Poincaré homology sphere $`\Sigma(2,3,5) = S^3/2I`$ holds a distinguished place in gauge theory. Among spherical space forms with nontrivial fundamental group it is the unique integral homology sphere, singled out on that account by Fintushel and Stern [FintushelStern] in the instanton-Floer setting. Adjoint-coefficient spectral-flow computations for it appear in Nasatyr [Nasatyr1992] and Kirk and Klassen [KirkKlassen], with the binary polyhedral character and flat-connection data recorded by Helle [Helle]. Gauge theory typically compares flat connections through global invariants of such adjoint operators, such as spectral flow along a path between them; the question here is intrinsic to each connection separately, and simpler: for $`X = S^3/\Gamma`$, the quotient of the round three-sphere by a finite subgroup $`\Gamma \subset \mathrm{SU}(2)`$ acting by left translation, and the flat bundle $`E_\tau`$ determined by a finite-dimensional representation $`\tau`$ of $`\Gamma`$, what is the lowest nonzero eigenvalue of the Hodge Laplacian on coexact $`E_\tau`$-valued $`1`$-forms, and how does it depend on $`\tau`$? In the adjoint case that eigenvalue is also the bottom of the gauge-fixed Laplacian on the Coulomb slice at the connection: the slice is cut out by the coclosedness condition $`d_\nabla^* a = 0`$, and coclosed $`1`$-forms coincide with coexact ones on these spaces (Lemma 2.1).

The answer is representation-theoretic. For an arbitrary twist the gap is $`q_\tau^2/R^2`$ for an integer $`q_\tau`$, the first level of the round sphere's coexact spectrum at which a constituent of $`\tau`$ appears, and it is likewise the square of the smallest absolute eigenvalue of the natural curl-type operator on the same forms. The spectral question therefore reduces to a first-occurrence problem in representation theory. For the adjoint bundle of an irreducible flat $`\mathrm{SU}(2)`$ connection, the coefficient system of the gauge-theoretic deformation problem, the answer is uniform across the ADE classification of finite subgroups of $`\mathrm{SU}(2)`$, with exactly one exception.

> **Theorem 1.1.** Let $`X = S^3/\Gamma`$ be the homogeneous spherical space form of a finite subgroup $`\Gamma \subset \mathrm{SU}(2)`$ acting by left translation on the round three-sphere of curvature $`1/R^2`$, and let $`\rho \colon \Gamma \to \mathrm{SU}(2)`$ be an irreducible representation, equivalently an irreducible flat $`\mathrm{SU}(2)`$ connection on $`X`$. The bottom of the spectrum of the Hodge Laplacian on coexact $`1`$-forms valued in the adjoint bundle of $`\rho`$ is $`4/R^2`$, with a single exception over all pairs $`(\Gamma, \rho)`$: for the Galois conjugate $`Q^\prime`$ of the defining representation $`Q`$ of the binary icosahedral group, a flat connection on the Poincaré homology sphere $`S^3/2I`$, the bottom is $`36/R^2`$. In each case the full adjoint $`1`$-form Laplacian has the same spectral gap.

The exception reflects two related features of $`2I`$: its perfectness prevents $`Q^\prime`$ from being a character twist of $`Q`$, while the distinct adjoint $`\mathrm{Sym}^2 Q^\prime`$ occupies the $`3`$-dimensional node at distance six in affine $`E_8`$; every other adjoint has its nearest constituent at distance two.

One rule carries the computation. The McKay correspondence [McKay] between finite subgroups of $`\mathrm{SU}(2)`$ and the affine ADE diagrams answers the first-occurrence problem: an irreducible representation first occurs in the restricted symmetric-power tower at its graph distance from the trivial node (Lemma 4.1); from distance two on, that is also its first coexact level (Theorem 4.2), which gives the rule stated at the outset. The constituents of an adjoint twist always lie at distance at least two, so the rule applies to them without qualification. Three classical spectral ingredients, recorded next, combine with the correspondence into that rule, and Theorem 1.1 follows from it; only the graph metric of the correspondence enters here.

Ikeda and Taniguchi [IkedaTaniguchi] give the round-sphere coexact spectrum, Ikeda [Ikeda1989] its descent to general spherical space forms, and Lauret, Miatello and Rossetti [LauretMiatelloRossetti] the representation-equivalence form of that descent; Bär gives the Dirac analogue [Bar1996] and, by Poincaré-series methods, the untwisted curl spectrum on spherical space forms itself [Bar2019], the $`\tau = \mathbf{1}`$ case of the descent below.

Twisted spectral problems on these spaces with arbitrary coefficients are themselves classical. Dowker [Dowker2009] treats Laplacians of twisted $`p`$-forms on the homogeneous three-sphere factors in the flat-bundle framework of Ray and Singer [RaySinger1971], expressing any spectral quantity for any twisting through induction from cyclic subgroups, with the McKay correspondence recovered along the way by Artin's theorem. That framework is directed toward spectral quantities obtained through isospectral induction. The question here is instead the bottom of the spectrum. Those formulas determine it in principle, twist by twist; what is proved below is a closed rule, identifying the first coexact level with McKay graph distance whenever that distance is at least two, and it is the closed form that makes the uniform adjoint classification and its single exception available.

Nearby work extends in two other directions: Henkel and Lauret [HenkelLauret2026] keep the coefficient system trivial and vary the homogeneous metric on $`S^3`$ and $`\mathrm{SO}(3)`$, while Lauret [LauretLens2018, LauretCyclic] fixes constant curvature but allows at most a one-dimensional twist, for the ordinary $`p`$-form spectrum of a lens space and the character-twisted spectrum of functions over a cyclic fundamental group; character-twisted spectra on lens spaces in fact go back to Ray's computation of analytic torsion [Ray1970].

Coexact $`1`$-form gaps are approached instead by isoperimetric methods on closed Riemannian manifolds [BoulangerCourtois], sharpened for hyperbolic $`3`$-manifolds [Rudd2023], where negative curvature and an infinite fundamental group replace the representation theory used here.

The objects throughout are flat bundles on spherical space forms carrying their round metrics, and the spectrum studied is that of the Hodge Laplacian on the coexact $`1`$-form summand. Section 2 fixes the metric, the bundles, and the operator. Section 3 records the $`S^3`$ coexact spectrum and the descent to $`S^3/\Gamma`$. Section 4 proves the gap for a general flat bundle and derives Theorem 1.1 across the ADE classification, indexed by the affine Dynkin diagrams $`\widetilde{A}`$, $`\widetilde{D}`$, $`\widetilde{E}`$ that the McKay correspondence attaches to each $`\Gamma \subset \mathrm{SU}(2)`$ (Section 2.1).

---

## 2. Setup

### 2.1 The space and the McKay graph

Identify $`S^3`$ with $`\mathrm{SU}(2)`$ carrying the bi-invariant metric of constant sectional curvature $`1/R^2`$. Let $`\Gamma \subset \mathrm{SU}(2)`$ be a finite subgroup acting on $`S^3`$ by left translation, and write $`X = S^3/\Gamma`$ for the resulting spherical space form, a closed oriented $`3`$-manifold of constant curvature $`1/R^2`$ with $`\pi_1(X) = \Gamma`$; since right translation still acts transitively on $`X`$, this is a homogeneous spherical space form in the sense of Ikeda [Ikeda1995]. The finite subgroups are the cyclic groups $`\mathbb{Z}_n`$, the binary dihedral groups $`D_n^*`$, $`n \ge 2`$, of order $`4n`$, and the binary tetrahedral, octahedral, and icosahedral groups $`2T, 2O, 2I`$ of orders $`24, 48, 120`$.

Let $`V_j = \mathrm{Sym}^j \mathbb{C}^2`$ be the irreducible $`\mathrm{SU}(2)`$ representation of dimension $`j+1`$, so $`V_1`$ is the defining representation. The *McKay graph* of $`\Gamma`$ has the irreducible representations of $`\Gamma`$ as vertices, the trivial representation as distinguished vertex, and $`m_{\sigma\sigma^\prime} = \dim \mathrm{Hom}_\Gamma(\sigma^\prime,\, V_1\vert_\Gamma \otimes \sigma)`$ edges between $`\sigma`$ and $`\sigma^\prime`$. The McKay correspondence [McKay] identifies it with the affine Dynkin diagram attached to $`\Gamma`$.

The graph is bipartite exactly when $`-I \in \Gamma`$. If $`-I \in \Gamma`$, then $`-I`$ acts by a scalar on each irreducible $`\Gamma`$-representation, and tensoring with $`V_1`$ changes this scalar; the two central characters give the bipartition, so the scalar on a vertex at distance $`d`$ from the trivial vertex is $`(-1)^d`$. The subgroups omitting $`-I`$ are exactly the odd cyclic groups $`\mathbb{Z}_n`$, since every binary family contains $`-I`$ and $`\mathbb{Z}_n`$ contains $`-I`$ if and only if $`n`$ is even; for these groups the McKay graph is the odd cycle $`\widetilde{A}_{n-1}`$. Graph distances $`d(\sigma)`$ from the trivial vertex are taken on the underlying unweighted graph, and for a representation $`\tau`$ we set

```math
d_\tau = \min\lbrace\, d(\sigma) : \sigma \text{ a constituent of } \tau \,\rbrace.
```

### 2.2 Flat bundles and the adjoint

A finite-dimensional unitary representation $`\tau \colon \Gamma \to \mathrm{U}(V_\tau)`$ determines a flat Hermitian bundle $`E_\tau = (S^3 \times V_\tau)/\Gamma`$ on $`X`$, with the flat connection $`\nabla`$ descended from the trivial connection upstairs; unitarity costs no generality, since averaging any Hermitian product over the finite $`\Gamma`$ makes an arbitrary finite-dimensional complex representation unitary. Gauge-equivalence classes of flat $`\mathrm{SU}(2)`$ connections on $`X`$ are identified with conjugacy classes of homomorphisms $`\rho \colon \Gamma \to \mathrm{SU}(2)`$; the real adjoint bundle $`\mathrm{ad}_\rho`$ has fibre $`\mathfrak{su}(2)`$ and holonomy $`\mathrm{Ad} \circ \rho`$. We work with the complexification, the flat bundle $`E_\tau`$ for

```math
\tau = (\mathrm{ad}_\rho)_{\mathbb{C}} \cong \mathrm{Sym}^2 \rho \quad \text{as a complex } \Gamma\text{-representation,}
```

the isomorphism being the identification of $`\mathfrak{su}(2)_{\mathbb{C}} = \mathfrak{sl}(2, \mathbb{C})`$ with the spin-1 representation $`V_2`$ of the $`\mathrm{SU}(2)`$ acting through $`\rho`$. Complexifying changes no eigenvalue: the complexified Laplacian is the complexification of the real one and its eigenspaces are the complexified real eigenspaces, so the bottom in Theorem 1.1 may be computed on $`E_\tau`$.

### 2.3 The operator and positivity

Let $`d_\nabla`$ be the flat exterior derivative of $`E_\tau`$ and $`\Delta_\tau = d_\nabla^* d_\nabla + d_\nabla d_\nabla^*`$ the twisted Hodge Laplacian. For the flat unitary connection the Hodge decomposition reads

```math
\Omega^1(X; E_\tau) = \mathrm{im} d_\nabla\ \oplus\ \mathrm{im} d_\nabla^*\ \oplus\ \mathcal{H}^1(X; E_\tau),
```

with $`\Delta_\tau`$ preserving each summand; the coexact $`1`$-forms are $`\mathrm{im} d_\nabla^*`$.

This summand carries the only part of the twisted $`1`$-form spectrum that lies beyond functions: the exact and harmonic summands are already determined. On the exact summand $`\mathrm{im} d_\nabla`$, the identity $`\Delta_\tau(d_\nabla f) = d_\nabla(\Delta_\tau f)`$ sends each positive twisted $`0`$-form eigenvalue to the same $`1`$-form eigenvalue, while $`d_\nabla`$ annihilates the zero modes. Thus the exact summand reproduces the positive part of the twisted function spectrum. The harmonic summand $`\mathcal{H}^1(X; E_\tau)`$ vanishes for every finite-dimensional $`\tau`$ (Lemma 2.1 below). The coexact summand $`\mathrm{im} d_\nabla^*`$ therefore carries the entire twisted $`1`$-form spectrum beyond functions.

On that summand the curl operator $`\ast d_\nabla`$ is formally self-adjoint, and the standard three-dimensional curl identity [Bar2019, CapoferriVassiliev] persists for flat unitary bundles. With the convention $`d_\nabla^* = (-1)^k \ast d_\nabla \ast`$ on $`k`$-forms in three dimensions, a coclosed $`1`$-form $`\alpha`$ satisfies

```math
d_\nabla^*(\ast d_\nabla \alpha) = -\ast d_\nabla \ast(\ast d_\nabla \alpha) = -\ast d_\nabla d_\nabla \alpha = -\ast(F_\nabla \wedge \alpha) = 0,
```

flatness entering through the vanishing of the curvature $`F_\nabla`$, so $`\ast d_\nabla`$ preserves the coclosed $`1`$-forms, and on them

```math
(\ast d_\nabla)^2 \alpha = \ast d_\nabla \ast(d_\nabla \alpha) = d_\nabla^* d_\nabla \alpha = \Delta_\tau \alpha.
```

Since $`\Delta_\tau`$ is elliptic and self-adjoint on the closed manifold $`X`$, its coexact spectrum is discrete with finite-dimensional eigenspaces; $`\ast d_\nabla`$ preserves each eigenspace and is symmetric there, so the eigenspace of eigenvalue $`\lambda`$ decomposes into curl eigenspaces with eigenvalues in $`\lbrace \pm\sqrt{\lambda} \rbrace`$. The coexact spectrum of $`\Delta_\tau`$ is therefore the set of squares of the curl eigenvalues, and the bottom coexact eigenvalue is the square of the smallest $`\lvert \ast d_\nabla \rvert`$; for the self-adjoint realization of the curl operator itself, see [Bar2019, CapoferriVassiliev].

> **Lemma 2.1** (Vanishing of harmonic $`1`$-forms)**.** For every finite-dimensional twist $`\tau`$, $`H^1(X; E_\tau) = 0`$. Consequently the coexact $`1`$-forms coincide with the coclosed $`1`$-forms, and $`\Delta_\tau`$ is strictly positive on them.

*Proof.* By the Hodge theorem and de Rham with local coefficients, $`\mathcal{H}^1(X; E_\tau) \cong H^1(X; E_\tau)`$. Since the universal cover $`S^3`$ has $`H^1(S^3) = 0`$, the Cartan-Leray spectral sequence for the covering $`S^3 \to X`$ collapses in degree one, so $`H^1(X; E_\tau) \cong H^1(\Gamma; \tau)`$, computed by crossed homomorphisms. Since $`\Gamma`$ is finite and the coefficients have characteristic zero, averaging over $`\Gamma`$ gives $`H^1(\Gamma; V) = 0`$ for every finite-dimensional $`\Gamma`$-module $`V`$; hence $`H^1(X; E_\tau) = \mathcal{H}^1(X; E_\tau) = 0`$. The kernel of $`\Delta_\tau`$ on $`1`$-forms is exactly $`\mathcal{H}^1`$, and the spectrum is discrete, so $`\Delta_\tau`$ is strictly positive on $`\Omega^1(X; E_\tau)`$, and in particular on the coexact summand; and with $`\mathcal{H}^1 = 0`$ that summand $`\mathrm{im} d_\nabla^*`$ is the full space $`\ker d_\nabla^*`$ of coclosed $`1`$-forms. $`\square`$

---

## 3. The coexact spectrum and its descent

This section delivers the occurrence criterion: the twisted coexact spectrum of $`X`$ is read off from which round-sphere levels contain a constituent of the twist after restriction to $`\Gamma`$ (Proposition 3.1); Section 4 converts that criterion into McKay distance.

### 3.1 The coexact spectrum on $`S^3`$

Write $`L^2(S^3) = \bigoplus_{k \ge 0} V_k \boxtimes V_k^*`$ for the Peter-Weyl decomposition of functions, fixing the convention that $`\mathrm{SU}(2)_L`$ acts by left translation on the first factor and the commuting right $`\mathrm{SU}(2)`$ on the second. Trivialize $`T^* S^3`$ by the left-invariant coframe, so $`\Omega^1(S^3; \mathbb{C}) \cong C^\infty(S^3) \otimes \mathfrak{su}(2)^*_{\mathbb{C}}`$, the coframe carrying the trivial left action and the right adjoint representation $`V_2`$. Peter-Weyl and the self-duality $`V_k^* \cong V_k`$ of every $`\mathrm{SU}(2)`$ irreducible then give

```math
\Omega^1(S^3; \mathbb{C}) \cong \bigoplus_{k \ge 0} V_k \boxtimes (V_k \otimes V_2),
```

and Clebsch-Gordan splits $`V_k \otimes V_2 \cong V_{k+2} \oplus V_k \oplus V_{k-2}`$ for $`k \ge 2`$, with $`V_1 \otimes V_2 \cong V_3 \oplus V_1`$ and $`V_0 \otimes V_2 \cong V_2`$. For $`k \ge 1`$ the middle summand $`V_k \boxtimes V_k`$ occurs exactly once in $`\Omega^1`$. The exterior derivative $`d \colon C^\infty(S^3) \to \Omega^1(S^3)`$ is $`\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R`$-equivariant and injective on nonconstants, so $`\mathrm{im} d`$ is exactly the middle summands $`V_k \boxtimes V_k`$, $`k \ge 1`$. The harmonic $`1`$-forms vanish since $`H^1(S^3) = 0`$, so the coexact $`1`$-forms are the outer summands $`V_k \boxtimes V_{k \pm 2}`$. Reindexing, the coexact level $`m \ge 2`$ is

```math
\mathcal{E}_m = \bigl(V_m \boxtimes V_{m-2}\bigr)\ \oplus\ \bigl(V_{m-2} \boxtimes V_m\bigr),
```

the first factor carrying left translation and the second the commuting right action. Each summand is a distinct $`\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R`$ irreducible, so by Schur the curl $`\ast d`$ is scalar on each. The Laplacian eigenvalue on this level is $`m^2/R^2`$ by Ikeda and Taniguchi [IkedaTaniguchi], so with $`(\ast d)^2 = \Delta`$ the two scalars are $`\pm m/R`$; the signed curl spectrum, one sign on each summand, is computed by Bär [Bar2019], and only the squares enter below. The lowest level $`m = 2`$ gives $`\mathcal{E}_2 = (V_2 \boxtimes V_0) \oplus (V_0 \boxtimes V_2)`$ and eigenvalue $`4/R^2`$.

### 3.2 Descent to $`X = S^3/\Gamma`$

Fix the associated-bundle convention $`\gamma \cdot (x, v) = (\gamma x, \tau(\gamma) v)`$ on $`E_\tau = (S^3 \times V_\tau)/\Gamma`$. Sections of $`E_\tau`$ then identify with the equivariant functions $`f \colon S^3 \to V_\tau`$, $`f(\gamma x) = \tau(\gamma) f(x)`$, and $`E_\tau`$-valued $`1`$-forms with the $`V_\tau`$-valued $`1`$-forms $`\alpha`$ on $`S^3`$ satisfying

```math
L_\gamma^* \alpha = \tau(\gamma)\, \alpha, \qquad \gamma \in \Gamma,
```

the fixed points of the diagonal action $`\gamma \cdot \alpha = \tau(\gamma)\, L_{\gamma^{-1}}^* \alpha`$, $`\Gamma`$ acting by left translation on the form and by $`\tau`$ on $`V_\tau`$. Left translation commutes with the curl and preserves each $`\mathcal{E}_m`$. Pulling $`E_\tau`$ back to $`S^3`$ trivializes it with the product flat connection, so the lifted operators are $`d \otimes 1`$, $`d^* \otimes 1`$ and $`\ast \otimes 1`$, and the lifted twisted Laplacian is $`\Delta_{S^3} \otimes 1`$ on $`V_\tau`$-valued forms. The identification of the twisted spectrum in Proposition 3.1 is the descent of the $`p`$-spectrum of a constant-curvature space form, due to Ikeda [Ikeda1989] and given its representation-equivalence form by Lauret, Miatello and Rossetti [LauretMiatelloRossetti], with the coefficient $`V_\tau`$ inserted by the diagonal action; the proof below assembles the general case in a few lines.

Under left translation only the first factor of each piece of $`\mathcal{E}_m`$ is acted on, so the right factors are multiplicity spaces carrying the trivial $`\Gamma`$-action:

```math
\mathcal{E}_m\big\vert_\Gamma = \bigl(V_m\big\vert_\Gamma\bigr)^{\oplus(m-1)}\ \oplus\ \bigl(V_{m-2}\big\vert_\Gamma\bigr)^{\oplus(m+1)},
```

the *left content* $`V_m\vert_\Gamma`$ and $`V_{m-2}\vert_\Gamma`$ carrying the right-factor multiplicities $`\dim V_{m-2} = m-1`$ and $`\dim V_m = m+1`$. The dimensions check: $`(m-1)(m+1) + (m+1)(m-1) = 2(m^2-1)`$, the Ikeda-Taniguchi multiplicity of the level-$`m`$ coexact eigenvalue. The invariants of $`\mathcal{E}_m \otimes V_\tau`$ are therefore computed from this left content alone; the next proposition records the outcome.

> **Proposition 3.1** (Twisted coexact spectrum)**.** For $`m \ge 2`$, write $`W_m = V_m\vert_\Gamma \oplus V_{m-2}\vert_\Gamma`$ for the left content of level $`m`$. The multiplicity of the eigenvalue $`m^2/R^2`$ in the $`E_\tau`$-valued coexact $`1`$-form spectrum on $`X`$ is
>
> ```math
> \mu_\tau(m) = (m-1)\dim \mathrm{Hom}_\Gamma\!\bigl(\tau^*, V_m\vert_\Gamma\bigr) + (m+1)\dim \mathrm{Hom}_\Gamma\!\bigl(\tau^*, V_{m-2}\vert_\Gamma\bigr).
> ```
>
> As a set of eigenvalues the twisted coexact spectrum is
>
> ```math
> \bigl\lbrace\, m^2/R^2 :\ m \ge 2,\ \mathrm{Hom}_\Gamma\!\bigl(\tau^*, W_m\bigr) \ne 0 \,\bigr\rbrace,
> ```
>
> equivalently those $`m`$ at which a constituent of $`\tau`$ occurs in $`W_m`$. Its bottom is $`q_\tau^2/R^2`$, where
>
> ```math
> q_\tau = \min\bigl\lbrace\, m \ge 2 :\ \text{a constituent of } \tau \text{ occurs in } W_m \,\bigr\rbrace.
> ```

*Proof.* Pullback along the covering $`S^3 \to X`$ identifies $`E_\tau`$-valued forms with the equivariant $`V_\tau`$-valued forms above and intertwines $`d_\nabla`$, $`d_\nabla^*`$ and $`\ast`$ with $`d \otimes 1`$, $`d^* \otimes 1`$ and $`\ast \otimes 1`$, since $`\Gamma`$ acts by orientation-preserving isometries and the pulled-back connection is the product one. The averaging projector $`\frac{1}{\lvert\Gamma\rvert} \sum_{\gamma \in \Gamma} \tau(\gamma) \circ L_{\gamma^{-1}}^*`$ onto the equivariant forms commutes with all three operators. On $`S^3`$ the coclosed $`V_\tau`$-valued $`1`$-forms decompose as $`\bigoplus_{m \ge 2} \mathcal{E}_m \otimes V_\tau`$, an orthogonal sum complete in $`L^2`$ by Peter-Weyl, with $`\Delta_{S^3} \otimes 1`$ acting by $`m^2/R^2`$: the level decomposition and the eigenvalue computation of Section 3.1, applied factorwise. Coclosed coincides with coexact on both levels, upstairs since $`H^1(S^3) = 0`$ and on $`X`$ by Lemma 2.1. Projecting each level onto its equivariant part and descending, the twisted coexact spectrum on $`X`$ is therefore exactly the set of $`m^2/R^2`$ with $`(\mathcal{E}_m \otimes V_\tau)^\Gamma \ne 0`$, with eigenspace $`(\mathcal{E}_m \otimes V_\tau)^\Gamma`$ at level $`m`$. Computing invariants by restriction and the tensor-hom adjunction,

```math
\bigl(\mathcal{E}_m \otimes V_\tau\bigr)^\Gamma \cong \mathrm{Hom}_\Gamma\!\bigl(\tau^*,\, \mathcal{E}_m\vert_\Gamma\bigr),
```

which, with the right-factor multiplicities $`m-1`$ and $`m+1`$ of the decomposition of $`\mathcal{E}_m\vert_\Gamma`$, yields the multiplicity formula; and $`(\mathcal{E}_m \otimes V_\tau)^\Gamma \ne 0`$ exactly when $`\tau^*`$ shares a constituent with $`W_m`$. Each $`V_j`$ is self-dual, so $`W_m`$ is self-dual as a $`\Gamma`$-module; hence $`\tau^*`$ meets $`W_m`$ if and only if $`\tau`$ meets $`W_m^* = W_m`$, and the eigenvalue criterion follows. The reduction uses the self-duality of the left content, not of $`\tau`$, so it holds for arbitrary $`\tau`$; the adjoint case is self-dual only incidentally. It remains to see that the defining set for $`q_\tau`$ is nonempty: $`V_1\vert_\Gamma`$ is faithful, so by Burnside-Brauer every irreducible representation of $`\Gamma`$ occurs in some tensor power $`V_1^{\otimes k}\vert_\Gamma`$, and Clebsch-Gordan decomposes these into symmetric powers $`V_j\vert_\Gamma`$. Hence every irreducible occurs in some $`V_m\vert_\Gamma`$, and $`q_\tau`$ is finite; the sharp first occurrence in the symmetric-power tower, at $`a = d(\sigma)`$, is proved in Lemma 4.1. $`\square`$

For the trivial bundle, where $`\tau = \mathbf{1}`$, the descent recovers the classical untwisted coexact $`1`$-form spectrum, the $`\Gamma`$-invariant part $`(\mathcal{E}_m)^\Gamma`$ of each round-sphere level $`\mathcal{E}_m`$. The round-sphere levels are computed by Ikeda and Taniguchi [IkedaTaniguchi], the $`p`$-form spectra of spherical space forms by Ikeda [Ikeda1989], and those of lens spaces by Lauret [LauretLens2018]. The trivial representation occurs in $`W_2 = V_2\vert_\Gamma \oplus V_0\vert_\Gamma`$ through its $`V_0`$ summand, which is present for every $`\Gamma`$, so $`q_{\mathbf{1}} = 2`$ and the untwisted coexact gap is $`4/R^2`$ on every $`S^3/\Gamma`$ considered here.

For the full untwisted $`1`$-form spectrum we compare the coexact gap with the exact summand. The scalar level $`k`$ on $`S^3/\Gamma`$ is present precisely when $`V_k\vert_\Gamma`$ contains the trivial representation. If $`\Gamma \ne \lbrace 1\rbrace`$, then $`V_1\vert_\Gamma`$ has no nonzero invariant vector: such a vector would be fixed by every element of $`\Gamma`$, in particular by a nonidentity $`\gamma`$; but an element of $`\mathrm{SU}(2)`$ fixing a nonzero vector has eigenvalue $`1`$, and since $`\det \gamma = 1`$ both eigenvalues are $`1`$, so $`\gamma = I`$, a contradiction. The level-one scalar eigenvalue $`3/R^2`$ is therefore absent, the exact $`1`$-forms can only begin at level $`k \ge 2`$, and their eigenvalues are at least $`8/R^2`$. The coexact gap $`4/R^2`$ is thus the gap of the full untwisted $`1`$-form Laplacian for every nontrivial $`\Gamma \subset \mathrm{SU}(2)`$. For $`\Gamma = \lbrace 1\rbrace`$, the level-one scalar harmonics on $`S^3`$ give exact $`1`$-forms with eigenvalue $`3/R^2`$.

---

## 4. The gap and the ADE classification

### 4.1 First occurrence

Let $`A`$ be the McKay adjacency matrix, with entries $`A_{\sigma\sigma^\prime} = \dim \mathrm{Hom}_\Gamma(\sigma^\prime, V_1\vert_\Gamma \otimes \sigma)`$, so that multiplication by $`V_1`$ in the representation ring acts as $`A`$. The symmetric powers satisfy $`V_{a+1} = V_1 V_a - V_{a-1}`$, hence $`V_a = U_a(A)`$ applied to the trivial node, where $`U_a`$ is the degree-$`a`$ monic Chebyshev polynomial of the second kind, $`U_a(2\cos\theta) = \sin((a+1)\theta)/\sin\theta`$. The decompositions of the restrictions $`V_a\vert_\Gamma`$ are classical: Kostant [Kostant1984, Kostant1985] organizes their full multiplicity generating functions through the Coxeter element attached to $`\Gamma`$ by the McKay correspondence. Only the leading edge of that structure is needed here, the first-occurrence statement of Lemma 4.1, and we prove it directly.

> **Lemma 4.1** (First occurrence)**.** For an irreducible $`\Gamma`$-representation $`\sigma`$ at McKay distance $`d(\sigma)`$, the least $`a`$ with $`\sigma \subset V_a\vert_\Gamma`$ is $`a = d(\sigma)`$. If moreover $`-I \in \Gamma`$, equivalently the McKay graph is bipartite, then $`\sigma \subset V_a\vert_\Gamma`$ forces $`a \equiv d(\sigma) \pmod 2`$.

*Proof.* The multiplicity of $`\sigma`$ in $`V_a\vert_\Gamma`$ is the matrix element $`(U_a(A))_{0\sigma}`$. Since $`U_a`$ has degree and parity $`a`$ and leading coefficient one, this is a combination of $`(A^a)_{0\sigma}, (A^{a-2})_{0\sigma}, \dots`$, and $`(A^k)_{0\sigma}`$ counts length-$`k`$ walks from $`0`$ to $`\sigma`$, a count that vanishes for $`k < d(\sigma)`$. Hence the multiplicity vanishes for $`a < d(\sigma)`$. At $`a = d(\sigma)`$ the lower terms $`(A^{d(\sigma)-2})_{0\sigma}, (A^{d(\sigma)-4})_{0\sigma}, \ldots`$ vanish, since their exponents are below $`d(\sigma)`$. The unit-coefficient leading term remains, so the multiplicity is $`(A^{d(\sigma)})_{0\sigma}`$, the positive count of length-$`d(\sigma)`$ walks from $`0`$ to $`\sigma`$. When $`-I \in \Gamma`$, the preceding bipartition gives that $`-I`$ acts on $`\sigma`$ by $`(-1)^{d(\sigma)}`$, while it acts on $`V_a\vert_\Gamma`$ by $`(-1)^a`$. Hence occurrence of $`\sigma`$ in $`V_a\vert_\Gamma`$ forces $`a \equiv d(\sigma) \pmod 2`$. $`\square`$

### 4.2 The gap

Three occurrence quantities are now in play: the graph distance $`d(\sigma)`$ of a single irreducible, which by Lemma 4.1 is its first symmetric-power level; the first coexact level $`e(\sigma)`$ of that irreducible; and the first coexact level $`q_\tau`$ of the whole twist, from Proposition 3.1. The next theorem relates all three.

> **Theorem 4.2** (Gap from first occurrence)**.** Let $`\tau`$ be a finite-dimensional representation of $`\Gamma`$ and let $`d_\tau = \min\lbrace d(\sigma) : \sigma \text{ an irreducible constituent of } \tau \rbrace`$. For an irreducible constituent $`\sigma`$, let $`e(\sigma)`$ be the least $`m \ge 2`$ for which $`\sigma`$ occurs in $`W_m = V_m\vert_\Gamma \oplus V_{m-2}\vert_\Gamma`$. Then
>
> ```math
> e(\sigma) = 2 \quad \text{if } d(\sigma) = 0, \qquad e(\sigma) = d(\sigma) \quad \text{if } d(\sigma) \ge 2,
> ```
>
> with no hypothesis on $`\Gamma`$. If $`-I \in \Gamma`$, then also $`e(\sigma) = 3`$ for $`d(\sigma) = 1`$. Consequently
>
> ```math
> q_\tau = \min_{\sigma \subset \tau} e(\sigma),
> ```
>
> where the minimum runs over irreducible constituents. In particular, if $`d_\tau \ge 2`$, then $`q_\tau = d_\tau`$ and the bottom of the twisted coexact spectrum is $`d_\tau^2/R^2`$.

*Proof.* The equality $`q_\tau = \min_{\sigma \subset \tau} e(\sigma)`$ is just the definition of $`q_\tau`$ (Proposition 3.1). If $`d(\sigma) = 0`$, then $`\sigma`$ is the trivial representation and occurs in $`V_0`$, hence in $`W_2`$, and no level below $`2`$ is allowed. If $`d(\sigma) \ge 2`$, Lemma 4.1 places $`\sigma`$ first in $`V_{d(\sigma)}\vert_\Gamma`$, so $`W_{d(\sigma)}`$ contains $`\sigma`$ through its $`V_{d(\sigma)}`$ summand. For $`m < d(\sigma)`$, both $`m`$ and $`m-2`$ are below the first occurrence, so $`W_m`$ contains no copy of $`\sigma`$. Thus $`e(\sigma) = d(\sigma)`$. Finally assume $`-I \in \Gamma`$ and $`d(\sigma) = 1`$. The first occurrence is in $`V_1\vert_\Gamma`$, while the parity restriction excludes $`\sigma`$ from the even levels $`V_0\vert_\Gamma`$ and $`V_2\vert_\Gamma`$ appearing in $`W_2`$. Hence the first coexact level is $`m = 3`$, through the $`V_{m-2} = V_1`$ summand. $`\square`$

The bipartite hypothesis enters only for $`d_\tau \le 1`$, where the non-bipartite odd cyclic groups need separate treatment. For $`\Gamma = \mathbb{Z}_n`$ odd, write $`V_1\vert_{\mathbb{Z}_n} = \chi \oplus \chi^{-1}`$; for the distance-one character $`\chi`$, $`V_2\vert_{\mathbb{Z}_n} = \chi^2 \oplus \mathbf{1} \oplus \chi^{-2}`$, so $`\chi`$ already occurs at $`m = 2`$ exactly when $`\chi^3 = 1`$, i.e. only for $`n = 3`$; for every other odd $`n`$, $`\chi`$ first occurs at $`m = 3`$. The adjoint uses only the $`d_\tau \ge 2`$ case.

### 4.3 The adjoint

A flat $`\mathrm{SU}(2)`$ connection is irreducible precisely when $`\rho \colon \Gamma \to \mathrm{SU}(2)`$ is an irreducible $`2`$-dimensional representation. Its complexified adjoint is $`\mathrm{Sym}^2 \rho`$ (Section 2.2), a $`3`$-dimensional representation of $`\Gamma`$, irreducible for the binary polyhedral groups $`2T, 2O, 2I`$ and reducible for the binary dihedral groups; both cases are worked out in Section 4.4.

> **Proposition 4.3** (Adjoint gap)**.** For an irreducible flat $`\mathrm{SU}(2)`$ connection $`\rho`$ on $`X = S^3/\Gamma`$, the bottom of the adjoint coexact spectrum is $`d_{\mathrm{Sym}^2 \rho}^2/R^2`$, and $`d_{\mathrm{Sym}^2 \rho} \ge 2`$.

*Proof.* An irreducible $`2`$-dimensional $`\rho`$ forces $`\Gamma`$ nonabelian, hence binary dihedral or polyhedral, so $`-I \in \Gamma`$. Being central, $`-I`$ acts on the irreducible $`\rho`$ by a scalar, necessarily $`\pm I`$ since $`\det \rho = 1`$, so $`\mathrm{Sym}^2 \rho(-I) = I`$: the adjoint factors through $`\Gamma/\lbrace\pm I\rbrace`$, and as $`-I`$ acts on a distance-$`d`$ node by $`(-1)^d`$, every constituent lies at even distance. The trivial is not among them: since $`\det \rho = 1`$ the representation $`\rho`$ is self-dual, so $`\mathrm{Hom}_\Gamma(\mathbf{1}, \rho \otimes \rho) \cong \mathrm{Hom}_\Gamma(\rho^*, \rho)`$ is one-dimensional by Schur, and as $`\rho \otimes \rho = \mathrm{Sym}^2 \rho \oplus \Lambda^2 \rho`$ with $`\Lambda^2 \rho = \det \rho = \mathbf{1}`$, that unique trivial summand is the determinant, lying in $`\Lambda^2`$. Even distance and no trivial constituent give $`d_{\mathrm{Sym}^2 \rho} \ge 2`$, and Theorem 4.2 returns the bottom $`d_{\mathrm{Sym}^2 \rho}^2/R^2`$. $`\square`$

### 4.4 The ADE table

The distance $`d_{\mathrm{Sym}^2 \rho}`$ is read from the McKay graph. Cyclic groups carry no irreducible flat $`\mathrm{SU}(2)`$ connection, the image of any such $`\rho`$ being abelian. In every other case the nearest constituent of the adjoint sits at distance two, with a single exception.

The table lists only the $`2`$-dimensional irreducibles of determinant one, the flat connections valued in $`\mathrm{SU}(2)`$. In the binary dihedral row, $`D_n^* = \langle a, b \mid a^{2n} = 1,\ b^2 = a^n,\ bab^{-1} = a^{-1} \rangle`$, the $`2`$-dimensional irreducibles are $`\tau_\ell`$, $`1 \le \ell \le n-1`$, with $`\chi_{\tau_\ell}(a^k) = 2\cos(\pi\ell k/n)`$ and $`\chi_{\tau_\ell}(ba^k) = 0`$, and $`\varepsilon_D`$ denotes the sign character ($`a \mapsto 1`$, $`b \mapsto -1`$); since $`b^2 = a^n`$ and $`\chi_{\tau_\ell}(a^n) = 2(-1)^\ell`$, the determinant character $`\Lambda^2 \tau_\ell`$ is trivial on $`a`$ and equals $`\bigl(\chi_{\tau_\ell}(b)^2 - \chi_{\tau_\ell}(b^2)\bigr)/2 = -(-1)^\ell`$ on $`b`$, so the determinant-one representations are the odd-index $`\tau_{2j-1}`$, $`j = 1, \dots, \lfloor n/2 \rfloor`$. For $`2T`$ only the defining $`Q`$ qualifies: $`\det(Q \otimes \chi) = \chi^2 \det Q = \chi^2`$ for a character $`\chi`$, and the two nontrivial cube-root characters of $`2T`$ have nontrivial square. For $`2O`$ both $`Q`$ and $`Q \otimes \varepsilon`$ qualify, since the sign character $`\varepsilon`$ has $`\varepsilon^2 = \mathbf{1}`$, while the remaining $`2`$-dimensional irreducible, the lift of the $`2`$-dimensional representation of $`S_4 \cong 2O/\lbrace \pm I \rbrace`$, has determinant $`\varepsilon`$. And $`2I`$, being perfect, has no nontrivial $`1`$-dimensional character at all, so both $`Q`$ and $`Q^\prime`$ have determinant one and appear.

The ADE classification of the finite subgroups and the McKay labelling of their irreducibles are classical [McKay]; the labelled diagrams, character tables and flat-connection lists for the binary dihedral and polyhedral groups are collected in [Helle, Appendix A]. The table records the remaining datum needed here: the nearest irreducible constituent of $`\mathrm{Sym}^2 \rho`$ to the trivial node in the corresponding affine Dynkin diagram; the connection's own distance appears for orientation on the diagram, and only the adjoint column enters the gap. The binary dihedral row is checked by characters below, the $`2T`$, $`2O`$, and first $`2I`$ rows follow from the neighbour and shared-adjoint computations below, and the $`2I`$ exception is derived and cross-checked after the table.

| $`\Gamma`$ | connection $`\rho`$ (dim, dist) | nearest adjoint constituent (dim, dist) | gap |
|---|---|---|---|
| $`\mathbb{Z}_n`$ ($`\widetilde{A}_{n-1}`$) | none | n/a | n/a |
| $`D_n^*`$ ($`\widetilde{D}_{n+2}`$) | $`\tau_{2j-1}\ (2,\, 2j-1)`$ | $`\varepsilon_D\ (1,\, 2)`$ | $`4/R^2`$ |
| $`2T`$ ($`\widetilde{E}_6`$) | $`Q\ (2, 1)`$ | $`\mathrm{Sym}^2 Q\ (3, 2)`$ | $`4/R^2`$ |
| $`2O`$ ($`\widetilde{E}_7`$) | $`Q\ (2, 1),\ Q \otimes \varepsilon\ (2, 5)`$ | $`\mathrm{Sym}^2 Q\ (3, 2)`$ | $`4/R^2`$ |
| $`2I`$ ($`\widetilde{E}_8`$) | $`Q\ (2, 1)`$ | $`\mathrm{Sym}^2 Q\ (3, 2)`$ | $`4/R^2`$ |
| $`2I`$ ($`\widetilde{E}_8`$) | $`Q^\prime\ (2, 7)`$ | $`\mathrm{Sym}^2 Q^\prime\ (3, 6)`$ | $`36/R^2`$ |

*Binary dihedral.* The row covers every odd index at once. The four $`1`$-dimensional characters of $`D_n^*`$ and the $`\tau_\ell`$ exhaust $`\lvert D_n^* \rvert = 4n`$ by the sum of squares [Helle, Prop. A.3], and $`\tau_1 = V_1\vert_\Gamma`$ in the standard realization [Helle, App. A.2]. From $`(ba^k)^2 = a^n`$ and $`\chi_{\tau_\ell}(a^n) = 2(-1)^\ell`$,

```math
\chi_{\mathrm{Sym}^2 \tau_\ell}(a^k) = 1 + 2\cos(2\pi\ell k/n), \qquad \chi_{\mathrm{Sym}^2 \tau_\ell}(ba^k) = (-1)^\ell.
```

For the connections $`\tau_{2j-1}`$ the displayed characters give $`\varepsilon_D`$ multiplicity one in $`\mathrm{Sym}^2 \tau_{2j-1}`$, the cosine sum vanishing over the powers of $`a`$; subtracting it leaves a degree-two character, possibly reducible. The distance of $`\varepsilon_D`$ is two: even and nontrivial, it lies at distance at least two, while its occurrence in $`\mathrm{Sym}^2 \tau_1 \subset V_1\vert_\Gamma \otimes \tau_1`$ makes it adjacent to $`\tau_1`$, at distance at most two. No closer constituent of $`\mathrm{Sym}^2 \tau_{2j-1}`$ occurs: the trivial character has multiplicity zero by the same sums, and odd-distance constituents are excluded by parity, since $`\mathrm{Sym}^2 \tau_\ell(-I) = I`$ as in Proposition 4.3. The nearest constituent is therefore $`\varepsilon_D`$ at distance two and the gap is $`4/R^2`$.

*Binary polyhedral.* Since $`Q = V_1\vert_\Gamma`$ is the distance-one node adjacent to $`\mathbf{1}`$ in each polyhedral diagram, the constituents of $`V_1\vert_\Gamma \otimes Q \cong \mathbf{1} \oplus \mathrm{Sym}^2 Q`$ are exactly the McKay neighbours of $`Q`$; every constituent of $`\mathrm{Sym}^2 Q`$ therefore lies within distance two, and being even and nontrivial (as in Proposition 4.3) it lies at distance exactly two. The polyhedral adjoints are moreover irreducible: a $`1`$-dimensional constituent $`\chi`$ of $`\mathrm{Sym}^2 \rho \subset \rho \otimes \rho`$ forces $`\chi \otimes \rho \cong \rho`$ by Schur and self-duality of $`\rho`$, hence $`\chi^2 = \mathbf{1}`$ on determinants. $`2T`$ and $`2I`$ have no $`1`$-dimensional character of order two. For $`2O`$ the twist $`\varepsilon \otimes \rho`$ is distinguished from $`\rho`$ by its character on the order-eight classes [Helle, App. A.4]. The trivial character lies in $`\Lambda^2 \rho`$, not in $`\mathrm{Sym}^2 \rho`$ (Proposition 4.3). So each polyhedral $`\mathrm{Sym}^2 \rho`$, of dimension three with no $`1`$-dimensional constituent, is irreducible. The two $`2O`$ connections share an adjoint, since $`\varepsilon^2 = \mathbf{1}`$ gives $`\mathrm{Sym}^2(Q \otimes \varepsilon) = \mathrm{Sym}^2 Q`$, again distance two.

*The icosahedral exception.* The binary icosahedral group is perfect, so it has no nontrivial $`1`$-dimensional character at all, in particular none to twist $`Q`$ by, and its only other irreducible $`\mathrm{SU}(2)`$ connection is the Galois conjugate $`Q^\prime`$. Its adjoint $`\mathrm{Sym}^2 Q^\prime`$ is irreducible, as above, and distinct from $`\mathrm{Sym}^2 Q`$: with $`\Lambda^2 Q = \Lambda^2 Q^\prime = \mathbf{1}`$ (as in the proof of Proposition 4.3), the adjoint characters are $`\chi_{\mathrm{Sym}^2 Q} = \chi_Q^2 - 1`$ and $`\chi_{\mathrm{Sym}^2 Q^\prime} = \chi_{Q^\prime}^2 - 1`$, and on an order-ten class of $`2I`$, where $`\chi_Q = 2\cos(\pi/5)`$ and $`\chi_{Q^\prime} = 2\cos(3\pi/5)`$ [Helle, App. A.5], they take the Galois-conjugate values $`1 + 2\cos(2\pi/5) \ne 1 + 2\cos(4\pi/5)`$, exchanged by the automorphism $`\sqrt5 \mapsto -\sqrt5`$ of $`\mathbb{Q}(\sqrt5)`$. The affine $`E_8`$ diagram has exactly two $`3`$-dimensional nodes, at distances two and six (Figure 1); $`\mathrm{Sym}^2 Q`$ occupies the first, so $`\mathrm{Sym}^2 Q^\prime`$ is the one at distance six, and the Galois connection has gap $`36/R^2`$.

*The branching through level six.* Lemma 4.1 now forces the full branching up to level six: affine $`E_8`$ is a tree, so shortest walks are unique and each node $`\sigma`$ first occurs in $`V_{d(\sigma)}\vert_{2I}`$ with multiplicity one, and at every level $`a \le 6`$ the distance-$`a`$ nodes alone already exhaust $`\dim V_a`$, leaving room for nothing else:

| $`a`$ | $`\dim V_a`$ | $`V_a\vert_{2I}`$ | McKay distance(s) |
|:---:|:---:|:---:|:---:|
| 0 | 1 | $`\mathbf{1}`$ | 0 |
| 1 | 2 | $`Q`$ | 1 |
| 2 | 3 | $`\mathrm{Sym}^2 Q`$ | 2 |
| 3 | 4 | $`\mathbf{4}`$ | 3 |
| 4 | 5 | $`\mathbf{5}`$ | 4 |
| 5 | 6 | $`\mathbf{6}`$ | 5 |
| 6 | 7 | $`\mathbf{4}^\prime \oplus \mathrm{Sym}^2 Q^\prime`$ | 6, 6 |

where $`\mathbf{4}^\prime`$ denotes the second $`4`$-dimensional irreducible. Thus $`\mathrm{Sym}^2 Q`$ first occurs at level two, and $`\mathrm{Sym}^2 Q^\prime`$ is absent from $`V_a\vert_{2I}`$ for $`a < 6`$ and first occurs in $`V_6\vert_{2I}`$.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/e8-mckay-graph.png?raw=true" width="80%" alt="The affine E8 McKay graph of 2I: the trivial node, the defining representation Q with its Galois conjugate Q', their adjoints Sym^2 Q and Sym^2 Q', and the second 4-dimensional irreducible 4', labelled by name and McKay distance">

**Figure 1.** The affine $`E_8`$ McKay graph of $`2I`$: the trivial node $`\mathbf{1}`$, the defining representation $`Q`$ with its Galois conjugate $`Q^\prime`$, their adjoints $`\mathrm{Sym}^2 Q`$ and $`\mathrm{Sym}^2 Q^\prime`$, and the second $`4`$-dimensional irreducible $`\mathbf{4}^\prime`$, labelled by name and McKay distance. The three unlabelled nodes are the remaining irreducibles of $`2I`$, of dimensions $`4, 5, 6`$ from $`\mathbf{1}`$ to the branch node.

Every irreducible flat $`\mathrm{SU}(2)`$ connection on a quotient $`S^3/\Gamma`$ with $`\Gamma \subset \mathrm{SU}(2)`$ thus has adjoint coexact gap $`4/R^2`$, with the single exception of the Galois connection on $`S^3/2I`$, whose gap is $`36/R^2 = 6^2/R^2`$. This proves the coexact statement of Theorem 1.1.

These coexact gaps are also the gaps for the full adjoint $`1`$-form spectrum. By Section 2.3 and Lemma 2.1, the only other contribution is the exact summand, which carries the positive twisted function spectrum. On $`S^3`$ the scalar Laplacian has levels $`k(k+2)/R^2`$ for $`k \ge 0`$, with level-$`k`$ left content $`V_k\vert_\Gamma`$ [IkedaTaniguchi]; the averaging argument in the proof of Proposition 3.1, applied to functions, puts the twisted scalar level $`k`$ on $`X`$ exactly when a constituent of the twist occurs in $`V_k\vert_\Gamma`$, with the same self-duality reduction. By Lemma 4.1 the adjoint therefore first occurs in the function spectrum at level $`k = d_{\mathrm{Sym}^2\rho}`$, where the exact bottom is $`d_{\mathrm{Sym}^2\rho}(d_{\mathrm{Sym}^2\rho}+2)/R^2`$. Since $`d_{\mathrm{Sym}^2\rho} \ge 2`$ (Proposition 4.3), this exceeds the coexact bottom $`d_{\mathrm{Sym}^2\rho}^2/R^2`$, so the coexact gap is the gap of the full adjoint $`1`$-form Laplacian:

| case | $`d_{\mathrm{Sym}^2\rho}`$ | coexact bottom | exact bottom | full $`1`$-form gap |
|---|---|---|---|---|
| nonexceptional | $`2`$ | $`4/R^2`$ | $`8/R^2`$ | $`4/R^2`$ |
| $`2I`$ Galois | $`6`$ | $`36/R^2`$ | $`48/R^2`$ | $`36/R^2`$ |

The full $`1`$-form gap equals the coexact gap in each case; this completes the proof of Theorem 1.1.

---

## 5. Conclusion

The classification of Theorem 1.1 is representation-theoretic from end to end: the gap is set by a first-occurrence level in the restricted symmetric powers; that level is the McKay-graph distance for every adjoint twist, whose constituents all lie at distance at least two, and the single exception arises because the Galois adjoint $`\mathrm{Sym}^2 Q^\prime`$ is forced onto the $`3`$-dimensional node at distance six in affine $`E_8`$.

The spectral gap computed here is a static quantity, the bottom of a Laplacian at a fixed connection, rather than a path invariant such as spectral flow. Whether finer spectral data at the connection distinguishes flat connections with distinct adjoints (the two $`2O`$ connections share theirs outright) beyond what the bottom eigenvalue shows is a natural question left open here. Proposition 3.1 makes the full multiplicity function computable from branching data that Kostant's generating functions [Kostant1984, Kostant1985] organize, and the binary dihedral family, where every connection has bottom $`4/R^2`$, is the natural first test; for the sign of the curl eigenvalue, the eta-invariant methods of Capoferri and Vassiliev [CapoferriVassiliev2025] are one avenue.

---

## References

- **[Bar1996]** C. Bär, The Dirac operator on space forms of positive curvature. *J. Math. Soc. Japan* **48** (1996), 69–83.
- **[Bar2019]** C. Bär, The curl operator on odd-dimensional manifolds. *J. Math. Phys.* **60** (2019), no. 3, 031501.
- **[BoulangerCourtois]** A. Boulanger and G. Courtois, A Cheeger-like inequality for coexact 1-forms. *Duke Math. J.* **171** (2022), 3593–3641.
- **[CapoferriVassiliev]** M. Capoferri and D. Vassiliev, Beyond the Hodge theorem: curl and asymmetric pseudodifferential projections. *J. Lond. Math. Soc.* **113** (2026), no. 1, e70431.
- **[CapoferriVassiliev2025]** M. Capoferri and D. Vassiliev, A microlocal pathway to spectral asymmetry: curl and the eta invariant. arXiv:2502.18307 (2025).
- **[Dowker2009]** J. S. Dowker, Group theory aspects of spectral problems on spherical factors. arXiv:0907.1309 (2009).
- **[FintushelStern]** R. Fintushel and R. Stern, Instanton homology of Seifert fibred homology three spheres. *Proc. Lond. Math. Soc. (3)* **61** (1990), 109–137.
- **[Helle]** G. O. Helle, Equivariant instanton Floer homology and calculations for the binary polyhedral spaces. arXiv:2203.09471 (2022).
- **[HenkelLauret2026]** J. Henkel and E. A. Lauret, Hodge Laplacian on $`1`$-forms of homogeneous $`3`$-spheres. arXiv:2605.05406 (2026).
- **[Ikeda1989]** A. Ikeda, Riemannian manifolds $`p`$-isospectral but not $`(p+1)`$-isospectral. In *Geometry of Manifolds* (Matsumoto, 1988), Perspect. Math. **8**, Academic Press (1989), 383–417.
- **[Ikeda1995]** A. Ikeda, On the spectrum of homogeneous spherical space forms. *Kodai Math. J.* **18** (1995), 57–67.
- **[IkedaTaniguchi]** A. Ikeda and Y. Taniguchi, Spectra and eigenforms of the Laplacian on $`S^n`$ and $`P^n(\mathbb{C})`$. *Osaka J. Math.* **15** (1978), 515–546.
- **[KirkKlassen]** P. Kirk and E. Klassen, Computing spectral flow via cup products. *J. Differential Geom.* **40** (1994), no. 3, 505–562.
- **[Kostant1984]** B. Kostant, On finite subgroups of $`\mathrm{SU}(2)`$, simple Lie algebras, and the McKay correspondence. *Proc. Nat. Acad. Sci. U.S.A.* **81** (1984), 5275–5277.
- **[Kostant1985]** B. Kostant, The McKay correspondence, the Coxeter element and representation theory. In *Élie Cartan et les mathématiques d'aujourd'hui* (Lyon, 1984), Astérisque, numéro hors série, Soc. Math. France (1985), 209–255.
- **[LauretCyclic]** E. A. Lauret, Spectra of orbifolds with cyclic fundamental groups. *Ann. Global Anal. Geom.* **50** (2016), no. 1, 1–28.
- **[LauretLens2018]** E. A. Lauret, The spectrum on $`p`$-forms of a lens space. *Geom. Dedicata* **197** (2018), 107–122.
- **[LauretMiatelloRossetti]** E. A. Lauret, R. J. Miatello and J. P. Rossetti, Representation equivalence and $`p`$-spectrum of constant curvature space forms. *J. Geom. Anal.* **25** (2015), no. 1, 564–591.
- **[McKay]** J. McKay, Graphs, singularities, and finite groups. *Proc. Sympos. Pure Math.* **37** (1980), 183–186.
- **[Nasatyr1992]** E. B. Nasatyr, Seifert-fibred homology 3-spheres, V-surfaces and the Floer index. *Math. Proc. Cambridge Philos. Soc.* **111** (1992), no. 3, 461–485.
- **[Ray1970]** D. B. Ray, Reidemeister torsion and the Laplacian on lens spaces. *Adv. Math.* **4** (1970), 109–126.
- **[RaySinger1971]** D. B. Ray and I. M. Singer, $`R`$-torsion and the Laplacian on Riemannian manifolds. *Adv. Math.* **7** (1971), 145–210.
- **[Rudd2023]** C. G. Rudd, Stable isoperimetric ratios and the Hodge Laplacian of hyperbolic manifolds. *J. Topol.* **16** (2023), 588–633.

---

## Citation

```
Shatto, B. (2026).
Coexact Spectral Gaps and McKay Distance for Flat Bundles on Homogeneous Spherical Space Forms.
SSRN.
https://ssrn.com/abstract=6968698
```

---

## Independent numerical certification

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_1_method_note.md)

Theorem 1.1 has been reproduced on the OpenWave M8 track by an independent, blind computation. The solver was built from explicit $`2 \times 2`$ matrix generators alone, each group by closure, its irreducible characters by the class-algebra method, the symmetric powers $`V_a = \mathrm{Sym}^a \mathbb{C}^2`$ as monomial-basis matrices, with no classification, no Dynkin label, and no imported character table entering, which is what makes the result independent of this paper's own route. An adversarial audit recomputed everything in a disjoint method, exact $`\mathrm{GF}(p)`$ arithmetic with characters by isotypic splitting and exact projector ranks, and refuted nothing.

Across the finite subgroups of $`\mathrm{SU}(2)`$ the run covered, it confirmed the gap and its single exception: of the fourteen irreducible flat $`\mathrm{SU}(2)`$ connections in range, thirteen return bottom $`4/R^2`$ and exactly one returns $`36/R^2`$, the Galois connection $`Q^\prime`$ on $`S^3/2I`$, with the exact-summand bottoms $`8/R^2`$ and $`48/R^2`$ confirming that the coexact gap is the full adjoint $`1`$-form gap in each case. The first-occurrence rule of Theorem 4.2, the first coexact level equal to the McKay distance, held on all 114 irreducibles without exception, and the parity restriction requiring $`-I \in \Gamma`$ did real work: it held wherever $`-I`$ is present and failed in the five groups without it. The branching through level six came out $`\mathbf{1}, Q, \mathrm{Sym}^2 Q, \mathbf{4}, \mathbf{5}, \mathbf{6}, \mathbf{4}^\prime \oplus \mathrm{Sym}^2 Q^\prime`$, placing $`\mathrm{Sym}^2 Q^\prime`$ first at level six. The audit widened the search to 34 groups and 344 irreducibles and reached the same verdicts.

The affine $`E_8`$ diagram itself was a blind output rather than an input: the order-120 group's distance vector came out $`[0, 7, 1, 2, 6, 3, 6, 4, 5]`$ over the dimensions $`[1, 2, 2, 3, 3, 4, 4, 5, 6]`$, reconstructed from the matrix generators by an agent never told which diagram to expect. The [method note](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_1_method_note.md) carries the full record.

This is a numerical certification across the finite family the run covers, not a second proof. The classical spectral inputs it rests on, the round-sphere coexact spectrum of Ikeda and Taniguchi among them, are handed to the solver as definitions rather than tested; the run verifies every step built on them.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
