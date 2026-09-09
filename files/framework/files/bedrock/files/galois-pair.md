<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# ☯️ Galois Pair

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/galois%20pair%20banner.png?raw=true" width="100%" alt="Galois Pair">

Up to conjugacy the Poincaré homology sphere $`S^3/2I`$ carries, besides the trivial connection, exactly two irreducible flat $`\mathrm{SU}(2)`$ connections, interchanged by the Galois automorphism of $`\mathbb{Q}(\sqrt5)`$; it bounds the $`E_8`$ plumbing $`W`$. We record a conversion, obtained by combining the classical Atiyah-Patodi-Singer defect formula with the Dirac/Molien character sums, expressing the odd-signature rho invariant of any flat twist without trivial constituent on any $`S^3/\Gamma`$, $`\Gamma\subset\mathrm{SU}(2)`$ finite, as an affine function of the character sums of the Kronheimer-Nakajima index formulas. On $`S^3/2I`$ it reproduces the printed adjoint rho invariants $`-73/15`$ and $`-97/15`$ from the character sums, and locates their difference $`-8/5`$ exactly on the four conjugacy classes moved by $`\sqrt5\mapsto-\sqrt5`$. The tautological bundles on $`W`$ retain that asymmetry exactly, and retain it as charge: $`k\equiv cs\bmod 1`$ in all four sectors, and $`k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})=-3/5`$ exactly, refining a congruence of Helle to an equality.

The filling's raw homology, by contrast, cannot see the asymmetry: the automorphism group of the mod-2/mod-4 quadratic package is transitive on the $`120`$ root classes, and every bundle on $`W`$ restricts topologically trivially to every closed connected non-orientable surface with $`[F]_2=0`$, so the surface terms it feeds retain only rank and cancel in the Galois difference. Equivariant-lift and restricted-connection channels use more of the bundle than topological restriction and are not addressed. The dichotomy is the result: the filling detects the Galois pair through its tautological decoration, while its undecorated mod-2/mod-4 package and its ordinary characteristic-surface restriction data are blind to it.

---

## 1. Introduction

A characteristic surface in a compact oriented $`4`$-manifold detects an eta-type invariant of the manifold's boundary: the Guillou-Marin congruence reads the signature defect mod $`16`$ from the normal Euler number and the Brown invariant of the surface. The Poincaré homology sphere carries a finer eta-type asymmetry than the signature defect. Up to conjugacy it has, besides the trivial connection, exactly two irreducible flat $`\mathrm{SU}(2)`$ connections; their characters generate $`\mathbb{Q}(\sqrt5)`$, the Galois automorphism $`\sigma:\sqrt5\mapsto-\sqrt5`$ interchanges them, and the difference of their adjoint Atiyah-Patodi-Singer rho invariants is $`-8/5`$, supported exactly on the four conjugacy classes that $`\sigma`$ moves. Its canonical filling, the $`E_8`$ plumbing $`W`$, is homologically as symmetric as a $`4`$-manifold can be. The question this paper answers, with a yes and a no, is: which structures on the filling see the boundary's asymmetry?

The setting is uniform in the group. For a finite subgroup $`\Gamma\subset\mathrm{SU}(2)`$, write $`Y_\Gamma^+`$ for $`S^3/\Gamma`$ with the quotient orientation of the link of $`\mathbb{C}^2/\Gamma`$, and for a flat unitary twist $`\alpha`$ write $`D_\alpha`$ for the character sums of the Kronheimer-Nakajima index formulas (§3.1). For $`2I`$ the two irreducible flat connections are named by their representations $`Q`$ and $`Q'`$, and $`+\Sigma:=Y_{2I}^+`$. We first record a conversion identity valid for every $`\Gamma`$ (Theorem 1.1), then apply it to $`2I`$ and its filling (Theorem 1.2), and finally delimit the correspondence (Theorem 1.3).

> **Theorem 1.1** (Conversion identity)**.** For every finite $`\Gamma\subset\mathrm{SU}(2)`$ and every flat unitary twist $`\alpha`$ on $`Y_\Gamma^+`$ with no trivial constituent,
> ```math
> \rho_\alpha(Y_\Gamma^+)\;=\;\dim\alpha\;+\;4\bigl(D_\alpha-\dim\alpha\cdot D_1\bigr).
> ```
> The hypothesis is sharp: a trivial constituent of multiplicity $`m`$ shifts the identity by exactly $`m`$ (Corollary 3.2).

> **Theorem 1.2** (Galois asymmetry, tautologically realized)**.** On $`+\Sigma`$ the adjoint rho invariants of the Galois pair are $`\rho_{\mathrm{Sym}^2Q}=-73/15`$ and $`\rho_{\mathrm{Sym}^2Q'}=-97/15`$ (both in print: [Anvari, Table 1]; the first also [BHKK, §6], transported); their difference
> ```math
> \rho_{\mathrm{Sym}^2Q'}-\rho_{\mathrm{Sym}^2Q}\;=\;4\,\bigl(D_{\mathrm{Sym}^2Q'}-D_{\mathrm{Sym}^2Q}\bigr)\;=\;-\tfrac{8}{5}
> ```
> is supported exactly on the four golden classes; and the tautological bundles on $`W`$ realize the asymmetry as charge: $`k(\mathcal{R}_\alpha)\equiv cs(\alpha)\bmod 1`$ in all four sectors $`\alpha\in\lbrace Q,Q',\mathrm{Sym}^2Q,\mathrm{Sym}^2Q'\rbrace`$, with the exact equality $`k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})=\varepsilon(H)/\lvert 2I\rvert=-3/5`$, where $`H`$ is Helle's normalized virtual character (§5.2) and $`\varepsilon`$ its augmentation.

> **Theorem 1.3** (Blindness and restriction triviality)**.** (i) The automorphism group of $`(H_2(W;\mathbb{Z}_2),\ \cdot\ ,\mathfrak{P})`$, with $`\cdot`$ the mod-2 intersection pairing and $`\mathfrak{P}`$ its mod-4 Pontryagin-square refinement (§6), is transitive on the $`120`$ classes with $`\mathfrak{P}=2`$; consequently no invariant of the isomorphism class of the pointed quadratic space distinguishes the class of the distance-six adjoint node $`\mathrm{Sym}^2Q'`$ from any other class with $`\mathfrak{P}=2`$. (ii) Let $`F\subset W`$ be a closed connected non-orientable surface with $`[F]_2=0`$. Every real or complex vector bundle on $`W`$ restricts topologically trivially to $`F`$, and every virtual class restricts to its virtual rank: restriction from $`W`$ to such an $`F`$ retains nothing but rank.

> **Corollary 1.4.** Every restriction-route term, in the precise sense of Definition 7.3, is therefore independent of the coefficient bundle beyond its rank, and cancels identically in the Galois difference of the rank-three adjoints. Terms using more of the bundle, a nontrivial equivariant fibre action or the holonomy of the restricted connection, lie outside Definition 7.3 and are not addressed.

The dichotomy is not a failure of information transfer. The filling sees the boundary's Galois asymmetry exactly: by Theorem 1.1 the rho difference and the tautological charge difference are the same character sum read twice, and Theorem 1.2 records the asymmetry in the filling's own currency. Theorem 1.3 isolates two places that information does not reach: the raw mod-2/mod-4 homology, and, beyond rank, whatever a bundle on $`W`$ restricts to a $`\mathbb{Z}_2`$-null non-orientable surface. Blindness of the package, sensitivity of the decoration.

On attribution. Four statements below are new: the affine conversion identity (Theorem 1.1), whose two inputs are long known but whose combination we could not locate in print; the golden-class localization of the rho difference (Corollary 4.2); the exact charge equality refining Helle's congruence (Proposition 5.3); and the two negatives, the homological transitivity of Theorem 1.3(i) and the restriction triviality of Theorem 1.3(ii) with the route cancellation it yields (Corollary 1.4). The rest is classical and cited as such: the printed rho pair, which Proposition 4.1 verifies three independent ways, and the mod-1 principle behind the four-sector charge table (Proposition 5.2). Theorem 1.3(ii) is a statement about topological restriction; Corollary 1.4, which converts it into a statement about identities, is scoped to Definition 7.3 and is not a universal independence theorem.

The neighboring literature. The identification $`\Sigma(2,3,5)=S^3/2I`$ is used throughout without further comment. The rho values and their integrality mechanism are [BHKK]; the printed table on the link orientation is [Anvari], after [Saveliev]; the flat connections' isolation and the $`R`$-invariant technology are [FintushelStern]. The tautological bundles and index formulas are [KronheimerNakajima] and [Nakajima]; the Dirac-side character sums are printed in [Degeratu] (Molien form) and [CisnerosMolina] (spectra); the defect-sum lineage is [APS2], [Gilkey], [BotvinnikGilkey]. The Chern-Simons machinery is [Helle], with classical antecedents [Auckly], [KirkKlassen]; the transgression principle in cylindrical-end form is [HeddenKirk]. On the surface side, the closed congruence is [GuillouMarin] in [Matsumoto]'s exposition, the topological correction is [KirbyTaylor], the relative form is [Klug], the $`S^4`$ ancestor is [Massey], and the homology-cobordism setting is [LRS]. The $`\bar\mu`$ identity checked at the end of §4 is that of [RubermanSaveliev], in the normalization of [NeumannSiebenmann].

Organization. Section 2 fixes the group data, the golden classes, and the orientation dictionary. Section 3 proves Theorem 1.1 and checks its signs against print. Sections 4 and 5 prove Theorem 1.2, the boundary half and the interior half. Section 6 proves Theorem 1.3(i). Section 7 exhibits the localization mechanisms, isolates the restriction route, and proves Theorem 1.3(ii), from which Corollary 1.4 follows. Section 8 collects the dichotomy, the open questions, and the directions this suggests.

---

## 2. The Galois pair on $`S^3/2I`$

### 2.1 The binary icosahedral group

Let $`2I\subset\mathrm{SU}(2)`$ denote the binary icosahedral group, the preimage of the icosahedral rotation group under $`\mathrm{SU}(2)\to\mathrm{SO}(3)`$: the unique nontrivial perfect finite subgroup of $`\mathrm{SU}(2)`$, of order $`120`$. It has nine conjugacy classes; an element $`g\neq\pm I`$ is determined up to conjugacy by its defining-representation angle $`\phi_g\in(0,\pi)`$, the defining representation having eigenvalues $`e^{\pm i\phi_g}`$. The nine irreducible representations, of dimensions $`1,2,2,3,3,4,4,5,6`$, are the nodes of the affine $`E_8`$ diagram under the McKay correspondence [McKay], with the trivial representation at the affine node. We write $`Q`$ for the defining two-dimensional representation (McKay distance $`d(Q)=1`$ from the affine node), $`Q'`$ for the other two-dimensional irreducible ($`d(Q')=7`$), and note $`d(\mathrm{Sym}^2Q)=2`$, $`d(\mathrm{Sym}^2Q')=6`$.

### 2.2 The Galois automorphism and the golden classes

The character field of $`2I`$ is $`\mathbb{Q}(\sqrt5)`$, and the nontrivial field automorphism $`\sigma:\sqrt5\mapsto-\sqrt5`$ acts on characters. On the two-dimensional irreducibles it acts by exchange: $`\sigma(\chi_Q)=\chi_{Q'}`$, and consequently $`\sigma(\chi_{\mathrm{Sym}^2Q})=\chi_{\mathrm{Sym}^2Q'}`$. We call $`Q`$ and $`Q'`$ the *Galois pair*.

> **Definition 2.1** (Golden classes)**.** The *golden classes* of $`2I`$ are the four conjugacy classes of elements of orders $`5`$ and $`10`$, with defining-representation angles $`\phi\in\lbrace \pi/5,\ 2\pi/5,\ 3\pi/5,\ 4\pi/5\rbrace`$. They are precisely the classes on which some character of $`2I`$ is irrational, that is, the locus moved by $`\sigma`$.

The table records the class data the proofs below consume; the full character table is in [Helle]. Sizes refer to the number of elements in the class.

| $`\phi`$ | size | $`\chi_Q`$ | $`\chi_{Q'}`$ | $`\chi_{\mathrm{Sym}^2Q}`$ | $`\chi_{\mathrm{Sym}^2Q'}`$ |
|---|---|---|---|---|---|
| $`0`$ | $`1`$ | $`2`$ | $`2`$ | $`3`$ | $`3`$ |
| $`\pi`$ | $`1`$ | $`-2`$ | $`-2`$ | $`3`$ | $`3`$ |
| $`\pi/2`$ | $`30`$ | $`0`$ | $`0`$ | $`-1`$ | $`-1`$ |
| $`2\pi/3`$ | $`20`$ | $`-1`$ | $`-1`$ | $`0`$ | $`0`$ |
| $`\pi/3`$ | $`20`$ | $`1`$ | $`1`$ | $`0`$ | $`0`$ |
| $`\pi/5`$ | $`12`$ | $`\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{1-\sqrt5}{2}`$ | $`\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{1-\sqrt5}{2}`$ |
| $`2\pi/5`$ | $`12`$ | $`\tfrac{\sqrt5-1}{2}`$ | $`-\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{1-\sqrt5}{2}`$ | $`\tfrac{1+\sqrt5}{2}`$ |
| $`3\pi/5`$ | $`12`$ | $`\tfrac{1-\sqrt5}{2}`$ | $`\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{1-\sqrt5}{2}`$ | $`\tfrac{1+\sqrt5}{2}`$ |
| $`4\pi/5`$ | $`12`$ | $`-\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{\sqrt5-1}{2}`$ | $`\tfrac{1+\sqrt5}{2}`$ | $`\tfrac{1-\sqrt5}{2}`$ |

> **Lemma 2.2** (Galois equivariance)**.** Let $`c`$ be a class function on $`2I`$ with values in $`\mathbb{Q}(\sqrt5)`$ whose value $`c(g)`$ is fixed by $`\sigma`$ whenever $`g`$ does not lie in a golden class, and for a tuple $`\boldsymbol\alpha=(\alpha_1,\dots,\alpha_r)`$ of representations let $`F_{\boldsymbol\alpha}(g)=P\bigl(\chi_{\alpha_1}(g),\dots,\chi_{\alpha_r}(g);\ c(g)\bigr)`$ with $`P`$ a polynomial with rational coefficients. If $`\boldsymbol\alpha^\sigma=(\alpha_1^\sigma,\dots,\alpha_r^\sigma)`$ is the induced action on representations, then $`F_{\boldsymbol\alpha^\sigma}-F_{\boldsymbol\alpha}`$ is supported on the golden classes. In particular $`c=1/(2-\chi_Q)`$ is allowed: it is irrational on the golden classes, but on every other class $`\chi_Q`$ is rational, so $`c`$ is $`\sigma`$-fixed there.

*Proof.* Let $`g`$ lie outside the golden classes. By Definition 2.1 every character value at $`g`$ is rational, so $`\chi_{\alpha_i^\sigma}(g)=\sigma(\chi_{\alpha_i}(g))=\chi_{\alpha_i}(g)`$ for each $`i`$, and $`c(g)`$ is $`\sigma`$-fixed by hypothesis. Every input of $`P`$ is therefore unchanged by the substitution $`\boldsymbol\alpha\mapsto\boldsymbol\alpha^\sigma`$, so $`F_{\boldsymbol\alpha^\sigma}(g)=F_{\boldsymbol\alpha}(g)`$. $`\square`$

Every "supported on the golden classes" statement below reduces to Lemma 2.2: any rationally-built class-function difference between $`\sigma`$-conjugate inputs lives on the golden locus.

### 2.3 Flat connections and their adjoints

Conjugacy classes of homomorphisms $`\pi_1(S^3/2I)=2I\to\mathrm{SU}(2)`$ correspond to flat $`\mathrm{SU}(2)`$ connections on $`S^3/2I`$ up to gauge. Up to conjugacy there are, besides the trivial one, exactly two irreducible classes, given by $`Q`$ and $`Q'`$; both are isolated and nondegenerate [FintushelStern]. We name flat connections by their representations. The complexified adjoint of the flat connection $`Q`$ is $`\mathrm{Sym}^2Q`$, and likewise for $`Q'`$: the Galois pair of two-dimensional representations induces the Galois pair of three-dimensional adjoints, at McKay distances $`2`$ and $`6`$. Among the exceptional binary polyhedral groups $`2T`$, $`2O`$, $`2I`$, only $`2I`$ has an adjoint Galois pair that is distinct; perfectness is what rules out the octahedral coincidence, as Section 8 records.

### 2.4 Orientations and conventions

**Conventions are load-bearing.** Every signed rational in this paper is pinned to an explicit orientation, and the table below is the dictionary. Write $`Y_\Gamma^+`$ for $`S^3/\Gamma`$ with the quotient orientation it inherits as the link of $`\mathbb{C}^2/\Gamma`$ (the boundary at infinity of the minimal resolution), and $`+\Sigma:=Y_{2I}^+`$ for the Poincaré homology sphere so oriented; $`W`$ denotes the $`E_8`$ plumbing, the compact truncation of the minimal resolution of $`\mathbb{C}^2/2I`$ (the noncompact resolution itself is $`X`$, §3.1), a simply connected spin $`4`$-manifold with $`\partial W=+\Sigma`$, intersection form the negative definite $`E_8`$ lattice, and $`H^1(W;\mathbb{Z}_2)=0`$.

| convention | statement | source |
|---|---|---|
| orientation | $`+\Sigma=Y_{2I}^+`$, the link orientation, equal to the resolution-boundary orientation, to Helle's $`S^3\subset\mathbb{H}`$ standard orientation, and to Degeratu's boundary-at-infinity; one oriented manifold under different names | standard, [Helle], [Degeratu] |
| the surgery model | $`X_{+1}`$ ($`+1`$ surgery on the right-hand trefoil) satisfies $`X_{+1}\cong-\Sigma`$ as oriented manifolds | [BHKK] |
| reversal | $`\rho`$ and $`cs`$ change sign under orientation reversal | [APS2], [Helle] |
| Chern-Simons | $`cs(Q)=-1/120`$ on $`+\Sigma`$, equivalently $`+1/120`$ on $`X_{+1}`$ | [Helle], [BHKK] |
| normalization | $`\rho_\alpha=\eta_\alpha-\dim\alpha\cdot\eta`$, unreduced, where $`\eta_\alpha`$ is the eta invariant of the odd-signature operator twisted by $`\alpha`$, $`\eta`$ its untwisted value, and $`h`$ the kernel dimension of the twisted odd-signature operator (equivalently, the dimension of the twisted cohomology) | [APS2] |

One further prose note the table cannot carry: the matching of our $`(Q,Q')`$ with printed connection labels is fixed by Chern-Simons values ($`cs(Q)\equiv-1/120`$, $`cs(Q')\equiv-49/120`$ on $`+\Sigma`$); [Anvari, Table 1] binds the Floer index, half the rho invariant, and the Chern-Simons value per connection in one printed place on this orientation. The dictionary above aligns it with [BHKK]'s surgery model, so every comparison in this paper can be checked line by line. Finally, the rho invariant of a flat bundle is independent of the Riemannian metric [APS2], so no metric parameter enters this paper.

---

## 3. The conversion identity

This section is general: $`\Gamma`$ is any finite subgroup of $`\mathrm{SU}(2)`$, and $`2I`$ plays no special role until §4.

### 3.1 The two currencies

For a flat unitary twist $`\alpha`$ on $`Y_\Gamma^+`$, the Atiyah-Patodi-Singer rho invariant is computed by the classical $`G`$-signature defect sum [APS2]:
```math
\rho_\alpha(Y_\Gamma^+)\;=\;\frac{1}{\lvert\Gamma\rvert}\sum_{1\neq g\in\Gamma}\bigl(\chi_\alpha(g)-\dim\alpha\bigr)\,\cot^2(\phi_g/2),
```
where $`e^{\pm i\phi_g}`$ are the defining eigenvalues of $`g`$. The sign is tied to the orientation: the raw fixed-point datum for the angle pair $`(\phi,-\phi)`$ is $`\cot(\phi/2)\cot(-\phi/2)=-\cot^2(\phi/2)`$, and the $`+\cot^2`$ displayed here is that datum read on the link orientation $`Y_\Gamma^+`$. Proposition 3.3 below checks the choice against printed values. The computation belongs to the classical defect-sum technology of Atiyah-Patodi-Singer and Gilkey [APS2], [Gilkey].

The second currency is the character sum
```math
D_\alpha\;:=\;\frac{1}{\lvert\Gamma\rvert}\sum_{1\neq g\in\Gamma}\frac{\chi_\alpha(g)}{2-\chi_Q(g)}\;=\;\frac{1}{\lvert\Gamma\rvert}\sum_{1\neq g\in\Gamma}\frac{\chi_\alpha(g)}{\det(I_2-g)},
```
writing $`D_1`$ for the trivial twist. All Dirac eta invariants below are taken for the natural $`\Gamma`$-invariant spin structure on $`Y_\Gamma^+`$, the one induced by the canonical lift of $`\Gamma\subset\mathrm{SU}(2)`$ to $`\mathrm{Spin}(4)`$; this is the structure for which the formulas cited below are stated, and for $`\Gamma=2I`$ it is the only one, $`\mathrm{Hom}(2I,\mathbb{Z}_2)`$ being trivial. These sums are simultaneously spectral and geometric objects in the literature. Spectrally, they are Dirac eta invariants: Degeratu's direct group-sum formula for the twisted Dirac operator on $`S^{2n-1}/\Gamma`$ ([Degeratu], Cor. 2.4, with the half-determinant trivial for $`\Gamma\subset\mathrm{SU}(n)`$ by her Cor. 3.3) reads, at $`n=2`$,
```math
\eta_{\mathrm{Dir},\alpha}(Y_\Gamma^+)\;=\;2\,D_\alpha,
```
Her sphere at infinity is the boundary of the minimal resolution of $`\mathbb{C}^2/\Gamma`$, so it carries the link orientation $`Y_\Gamma^+`$ by construction; the sign convention is calibrated in Proposition 3.3 below. Thus $`D_\alpha`$ is half the twisted Dirac eta, and her Molien-series theorem expresses the same quantity as a residue of the singularity's graded character series. Geometrically, they are index integrals: by the Kronheimer-Nakajima index theorem on the minimal resolution ([KronheimerNakajima], (A.2) with one trivial factor), $`D_\alpha=\int_X\mathrm{ch}(\mathcal{R}_\alpha)\hat{A}`$ for the tautological bundle $`\mathcal{R}_\alpha`$ over the minimal resolution $`X`$ of $`\mathbb{C}^2/\Gamma`$, the standard such bundle for nontrivial irreducible $`\alpha`$, the reducible case following additively. This double role is used in §5.

Theorem 1.1 is the statement that the first currency is an affine function of the second. It follows in three lines from the two classical formulas just cited; its content is the exact form, which we could not locate in print, and which is what §§4-5 consume.

### 3.2 The trigonometric kernel

> **Lemma 3.1.** For $`g\neq I`$ in $`\Gamma\subset\mathrm{SU}(2)`$ with defining eigenvalues $`e^{\pm i\phi}`$,
> ```math
> \csc^2(\phi/2)\;=\;\frac{4}{2-\chi_Q(g)},\qquad\text{hence}\qquad \cot^2(\phi/2)\;=\;-1+\frac{4}{2-\chi_Q(g)}.
> ```

*Proof.* $`2-\chi_Q(g)=2-2\cos\phi=4\sin^2(\phi/2)`$, which is nonzero for $`g\neq I`$ (for $`g=-I`$, $`\phi=\pi`$, both sides of the first identity equal $`1`$). The second identity is $`\cot^2=\csc^2-1`$. $`\square`$

The factor $`4`$ produced here is trigonometric. It is unrelated to the Dynkin-index factor $`4`$ by which the Chern-Simons invariants of adjoint and defining flat connections are compared in §5, and the two must not be conflated.

### 3.3 The identity

*Proof of Theorem 1.1.* Let $`\alpha`$ contain no trivial constituent, so that $`\sum_{g\in\Gamma}\chi_\alpha(g)=0`$ and hence $`\sum_{g\neq 1}\chi_\alpha(g)=-\dim\alpha`$. Substituting Lemma 3.1 into the defect sum,
```math
\rho_\alpha(Y_\Gamma^+)\;=\;-\frac{1}{\lvert\Gamma\rvert}\sum_{g\neq 1}\bigl(\chi_\alpha(g)-\dim\alpha\bigr)\;+\;\frac{4}{\lvert\Gamma\rvert}\sum_{g\neq 1}\frac{\chi_\alpha(g)-\dim\alpha}{2-\chi_Q(g)}.
```
The first sum evaluates by orthogonality: $`\sum_{g\neq 1}(\chi_\alpha-\dim\alpha)=-\dim\alpha-(\lvert\Gamma\rvert-1)\dim\alpha=-\lvert\Gamma\rvert\dim\alpha`$, contributing $`+\dim\alpha`$. The second is $`4(D_\alpha-\dim\alpha\,D_1)`$ by definition. Hence
```math
\rho_\alpha(Y_\Gamma^+)\;=\;\dim\alpha\;+\;4\bigl(D_\alpha-\dim\alpha\cdot D_1\bigr). \qquad\square
```

Equivalently, through Degeratu's formula, $`\rho_\alpha=\dim\alpha+2\bigl(\eta_{\mathrm{Dir},\alpha}-\dim\alpha\,\eta_{\mathrm{Dir},1}\bigr)`$: the odd-signature rho invariant of a flat twist is an affine function of twisted Dirac eta invariants.

> **Corollary 3.2** (Sharpness)**.** If $`\alpha`$ contains the trivial representation with multiplicity $`m`$, then the left side of Theorem 1.1 equals $`\rho_\beta`$ for $`\beta=\alpha\ominus\mathbf{1}^{\oplus m}`$, while the right side equals $`\rho_\beta+m`$: the identity acquires the exact additive offset $`m`$.

*Proof.* Trivial summands contribute zero to $`\chi_\alpha-\dim\alpha`$ pointwise, so the defect sum, and with it the left side, equals $`\rho_\beta`$. On the right, $`D_{\beta\oplus\mathbf{1}^{\oplus m}}=D_\beta+m\,D_1`$ and $`\dim(\beta\oplus\mathbf{1}^{\oplus m})=\dim\beta+m`$, so
```math
\dim\beta+m+4\bigl(D_\beta+mD_1-(\dim\beta+m)D_1\bigr)\;=\;\rho_\beta+m.
```
(Checked instance: $`\alpha=Q\oplus\mathbf{1}`$ gives right side $`-29/30`$ against $`\rho_Q=-59/30`$, offset exactly $`1`$.) $`\square`$

> **Proposition 3.3** (Verification against print)**.** With the conventions of §2.4, Theorem 1.1 reproduces the canonical-representation rho invariants of the Poincaré homology sphere printed by Boden, Herald, Kirk, and Klassen: $`\rho_Q(X_{+1})=59/30`$ and $`\rho_{Q'}(X_{+1})=131/30`$ [BHKK, §5.4-5.5].

*Proof.* The character sums for $`\Gamma=2I`$, computed exactly from the table of §2.2, are
```math
D_1=\tfrac{1079}{1440},\quad D_Q=\tfrac{73}{144},\quad D_{Q'}=-\tfrac{67}{720},\quad D_{\mathrm{Sym}^2Q}=\tfrac{9}{32},\quad D_{\mathrm{Sym}^2Q'}=-\tfrac{19}{160},
```
and Theorem 1.1 gives, on $`+\Sigma`$:

| $`\alpha`$ | $`\dim\alpha+4(D_\alpha-\dim\alpha\,D_1)`$ | comparison / later use |
|---|---|---|
| $`Q`$ | $`-59/30`$ | $`=-\rho_Q(X_{+1})`$, [BHKK] |
| $`Q'`$ | $`-131/30`$ | $`=-\rho_{Q'}(X_{+1})`$, [BHKK] |
| $`\mathrm{Sym}^2Q`$ | $`-73/15`$ | $`=`$ printed $`\rho/2=-73/30`$ doubled, [Anvari, Table 1]; see §4 |
| $`\mathrm{Sym}^2Q'`$ | $`-97/15`$ | $`=`$ printed $`\rho/2=-97/30`$ doubled, [Anvari, Table 1]; see §4 |

The first two rows match the printed values through the oriented identification $`X_{+1}\cong-\Sigma`$ and the sign reversal of §2.4; the last two match [Anvari]'s table directly on $`+\Sigma`$. $`\square`$

---

## 4. The rho invariants of the Galois pair

> **Proposition 4.1** (The pair, in print and twice re-derived)**.** On $`+\Sigma`$: $`\rho_{\mathrm{Sym}^2Q}=-73/15`$ and $`\rho_{\mathrm{Sym}^2Q'}=-97/15`$.

*Proof.* Three independent routes, recorded because each pins a different convention.

(i) *Print.* Anvari's table for $`\Sigma(2,3,5)`$ lists, per flat connection, the halved rho invariants $`-73/30`$ and $`-97/30`$ beside $`-cs=1/120`$ and $`49/120`$, on exactly this orientation, computed by a flat $`\mathrm{SO}(3)`$-cobordism to lens spaces [Anvari, Table 1], after [Saveliev, p. 144]. (He tabulates $`\rho/2`$ of the unreduced $`\rho`$ of §2.4.) The $`cs`$ pairing matches the dictionary of §2.4. Independently, Boden, Herald, Kirk, and Klassen compute $`\rho_{\mathrm{Sym}^2Q}(X_{+1})=\pm 73/15`$ and resolve the sign to $`+73/15`$ by integrality [BHKK, §6]; the §2.4 bookkeeping ($`X_{+1}\cong-\Sigma`$, $`\rho`$ reverses) transfers it to $`-73/15`$ here, agreeing.

(ii) *Character sums.* Theorem 1.1 with the values of Proposition 3.3 gives both numbers (rows three and four of that table).

(iii) *Integrality, both connections.* The sign of either value is fixed independently of the calibration of §2.4 by the mechanism of [BHKK]: their equation (6.5), for a path on $`X_{+1}`$ from the trivial connection $`\Theta`$ to a flat $`\alpha`$,
```math
SF\;=\;8\bigl(cs(\alpha)-cs(\Theta)\bigr)+\tfrac12\bigl(\rho_{\mathrm{ad}\,\alpha}-\rho_{\mathrm{ad}\,\Theta}\bigr)+\tfrac12\bigl(h_\alpha-h_\Theta\bigr),
```
must have integer left side, where $`SF`$ is the spectral flow and $`h_\gamma`$ the kernel dimension at the flat connection $`\gamma`$. For the second connection, $`h_\Theta=3`$, $`h_\alpha=0`$ (nondegeneracy [FintushelStern]), $`cs(\Theta)=0`$, and $`\rho_{\mathrm{ad}\,\Theta}=0`$; the printed representative is $`cs(Q')=-71/120`$ on $`X_{+1}`$ [BHKK, Table 1] (the same residue as §2.4: $`-71/120\equiv 49/120 \bmod 1`$, and $`-49/120`$ on $`+\Sigma`$ corresponds to $`+49/120`$ on $`X_{+1}`$). The two sign candidates for the second connection give
```math
SF=-\tfrac{71}{15}+\tfrac{97}{30}-\tfrac{3}{2}=-3,\qquad\text{respectively}\qquad SF=-\tfrac{71}{15}-\tfrac{97}{30}-\tfrac{3}{2}=-\tfrac{142}{15}\notin\mathbb{Z},
```
so only $`+97/15`$ on $`X_{+1}`$, that is $`-97/15`$ here, is admissible. The conclusion is lift-independent, since an integer shift of the Chern-Simons representative shifts $`SF`$ by a multiple of $`8`$; the same two-candidate check for the first connection reproduces [BHKK]'s own resolution. $`\square`$

> **Corollary 4.2** (Golden support)**.** On $`+\Sigma`$,
> ```math
> \rho_{\mathrm{Sym}^2Q'}-\rho_{\mathrm{Sym}^2Q}\;=\;4\,\bigl(D_{\mathrm{Sym}^2Q'}-D_{\mathrm{Sym}^2Q}\bigr)\;=\;4\cdot\bigl(-\tfrac{2}{5}\bigr)\;=\;-\tfrac{8}{5},
> ```
> and every contribution to the difference is supported on the four golden classes.

*Proof.* The first equality is Theorem 1.1 applied to the two adjoints, whose dimensions agree. Support: the defect summand is built rationally from characters and the $`\sigma`$-fixed-off-golden class function $`\cot^2(\phi/2)`$, and $`\mathrm{Sym}^2Q'=(\mathrm{Sym}^2Q)^\sigma`$, so Lemma 2.2 applies; concretely, the four non-identity non-golden classes contribute $`-\tfrac{57}{4}`$ (times $`\tfrac{1}{120}`$) to each of $`D_{\mathrm{Sym}^2Q}`$ and $`D_{\mathrm{Sym}^2Q'}`$ alike, while the four golden classes contribute $`+48`$ and $`0`$ respectively. $`\square`$

In this rho difference, the boundary sees the Galois action exactly on the golden classes. The fundamental sector behaves the same way. Lemma 2.2 applies verbatim to $`Q'=Q^\sigma`$, and Theorem 1.1 with the values of Proposition 3.3 gives $`\rho_{Q'}-\rho_Q=4(D_{Q'}-D_Q)=-12/5`$, again supported on the golden classes; these are the rho invariants of the twists $`Q`$ and $`Q'`$ themselves, not of their adjoints. There are no further instances. Write $`\sigma`$ also for the permutation it induces on conjugacy classes, through the power map by which it acts on roots of unity; Definition 2.1 identifies the classes it moves as the four golden ones, so it fixes five of the nine. Brauer's permutation lemma, which equates the number of irreducible characters fixed by such an action with the number of classes it fixes, then gives five fixed irreducibles, so $`\sigma`$ moves exactly four: the two pairs $`(Q,Q')`$ and $`(\mathrm{Sym}^2Q,\mathrm{Sym}^2Q')`$.

**One check before going inside.** The same conventions give the two untwisted eta invariants $`\eta_{\mathrm{Dir}}(+\Sigma)=2D_1=\tfrac{1079}{720}`$ and $`\eta_{\mathrm{Sign}}(+\Sigma)=\tfrac{1}{120}\sum_{g\neq 1}\cot^2(\phi_g/2)=\tfrac{361}{180}`$, whence
```math
\tfrac12\,\eta_{\mathrm{Dir}}+\tfrac18\,\eta_{\mathrm{Sign}}\;=\;\tfrac{1079}{1440}+\tfrac{361}{1440}\;=\;1\;=\;-\bar\mu\bigl(\Sigma(2,3,5)\bigr),
```
the identity of Ruberman and Saveliev on this orientation [RubermanSaveliev, Thm 1.1], with $`\bar\mu=-1`$ in the Neumann normalization [NeumannSiebenmann]. Mixed sign conventions would give $`\pm\tfrac{359}{720}`$ instead, so the agreement checks the dictionary of §2.4 independently of Proposition 3.3. The second of the two eta values is used in Lemma 5.1 below.

---

## 5. Tautological bundles and exact charges

### 5.1 The bundles and their charges

This is the interior half of Theorem 1.2: the same character sums, now read on the filling. In the ALE setting of [KronheimerNakajima], $`X`$ (§3.1) is the noncompact minimal resolution of $`\mathbb{C}^2/2I`$ and $`W`$ (§2.4) is its compact truncation, so finite-action Chern-Weil integrals are computed on $`X`$ while boundary-sign checks live on $`(W,+\Sigma)`$. Each nontrivial irreducible representation $`\alpha`$ of $`2I`$ determines the tautological bundle $`\mathcal{R}_\alpha`$ on $`X`$, carrying a canonical finite-action anti-self-dual connection whose flat limit at infinity is the flat connection of $`\alpha`$ [KronheimerNakajima, Prop. 2.2]. The first Chern classes of these bundles are dual to the exceptional curves $`\mathcal{E}_\alpha`$ of the resolution, $`\langle c_1(\mathcal{R}_\alpha),[\mathcal{E}_\beta]\rangle=\delta_{\alpha\beta}`$, the curves realizing the McKay nodes in $`H_2`$ [KronheimerNakajima, Thm. A.7]; this dual-basis fact is used in §7. Define the charge by the curvature integral
```math
k(\mathcal{R}_\alpha)\;:=\;\int_X\Bigl(c_2-\tfrac12 c_1^2\Bigr)(\mathcal{R}_\alpha).
```

> **Lemma 5.1** (Evaluation)**.** $`k(\mathcal{R}_\alpha)=\dim\alpha\,D_1-D_\alpha`$.

*Proof.* The degree-four part of $`\mathrm{ch}(\mathcal{R}_\alpha)\hat{A}`$ is $`\bigl(\tfrac12 c_1^2-c_2\bigr)+\dim\alpha\,\hat{A}_2`$, with $`\hat{A}_2`$ the component of complex degree $`2`$ (real degree $`4`$), so $`\int_X\mathrm{ch}(\mathcal{R}_\alpha)\hat{A}=-k(\mathcal{R}_\alpha)+\dim\alpha\int_X\hat{A}`$. The left side is $`D_\alpha`$ by [KronheimerNakajima, (A.2)] with one trivial factor, and $`\int_X\hat{A}=D_1`$ is the trivial instance of the same identity; independently, the signature theorem on the compact truncation gives $`\int_X\hat{A}=-\tfrac18\bigl(\mathrm{sign}(W)+\eta_{\mathrm{Sign}}(+\Sigma)\bigr)=1-\tfrac{361}{1440}=\tfrac{1079}{1440}=D_1`$, corroborating the constant $`D_1`$ from a second direction. $`\square`$

> **Proposition 5.2** (Charge realizes Chern-Simons)**.** In the four sectors $`\alpha=Q,\ Q',\ \mathrm{Sym}^2Q,\ \mathrm{Sym}^2Q'`$ the charges are
>
> | bundle | rank | $`k`$ | $`k\bmod 1`$ | $`cs`$ of the flat limit mod 1, on $`+\Sigma`$ |
> |---|---|---|---|---|
> | $`\mathcal{R}_Q`$ | 2 | $`119/120`$ | $`119/120`$ | $`-1/120\equiv 119/120`$ |
> | $`\mathcal{R}_{Q'}`$ | 2 | $`191/120`$ | $`71/120`$ | $`-49/120\equiv 71/120`$ |
> | $`\mathcal{R}_{\mathrm{Sym}^2Q}`$ | 3 | $`59/30`$ | $`29/30`$ | $`4\cdot(-1/120)\equiv 29/30`$ |
> | $`\mathcal{R}_{\mathrm{Sym}^2Q'}`$ | 3 | $`71/30`$ | $`11/30`$ | $`4\cdot(-49/120)\equiv 11/30`$ |
>
> and in each row $`k\equiv cs \bmod 1`$. In the adjoint sectors $`k(\mathcal{R}_{\mathrm{Sym}^2Q'})-k(\mathcal{R}_{\mathrm{Sym}^2Q})=+\tfrac25`$, the representative in $`[0,1)`$ of $`cs(\mathrm{Sym}^2Q')-cs(\mathrm{Sym}^2Q) \bmod 1`$.

*Proof.* The charges are obtained from Lemma 5.1 using the character sums of Proposition 3.3. Reducing the resulting four rational values modulo $`1`$ gives exactly the Chern-Simons residues displayed in the final column: in the fundamental sectors, $`cs(Q)=-1/120`$ and $`cs(Q')=-49/120`$ on $`+\Sigma`$, as fixed in §2.4 and derived in §5.2 below [Helle], [BHKK], with classical antecedents [FintushelStern], [Auckly], [KirkKlassen]; in the adjoint sectors, the residues follow from the Dynkin-index relation $`cs(\mathrm{Sym}^2\alpha)\equiv 4\,cs(\alpha)\bmod 1`$ for $`\mathrm{SU}(2)`$. Thus $`k(\mathcal{R}_\alpha)\equiv cs(\alpha)\bmod 1`$ in each of the four listed sectors. The verification is case by case: Hedden and Kirk [HeddenKirk, Defs. 2.2-2.4] give a related $`\mathrm{SO}(3)/p_1`$ transgression framework on cylindrical ends, but no transfer of their argument to the ALE setting is claimed here. $`\square`$

### 5.2 The affine solve

Helle associates to the pair $`(Q,Q')`$ the virtual character $`H`$ solving $`(2-Q)H=Q-Q'`$ in the representation ring $`R(2I)`$, unique up to the kernel of multiplication by $`2-Q`$, and proves $`cs(Q)-cs(Q')=\varepsilon(H)/\lvert 2I\rvert \bmod 1`$, where $`\varepsilon(H)=\chi_H(1)`$ is the augmentation [Helle, Prop. B.16]. Multiplication by $`Q`$ is the adjacency operator of the affine $`E_8`$ graph (the McKay correspondence), so that equation is the linear system $`(2I_9-A)H=e_{d(Q)}-e_{d(Q')}`$ on the nine nodes. Solvability requires the right side to pair to zero with the kernel vector, the vector $`\delta`$ of Coxeter marks, and it does: both marks are $`2`$. Normalizing the trivial component to $`h_0=0`$ fixes $`H`$, and the back-substitution is then forced:
```math
H=(0,\,0,\,-1,\,-2,\,-3,\,-4,\,-3,\,-2,\,-2),\qquad \varepsilon(H)=\langle H,\delta\rangle=-72.
```
The coordinates list the nine irreducibles by increasing McKay distance; the two at distance six carry the coordinates $`-3`$ and $`-2`$, on the second four-dimensional irreducible and on the adjoint $`\mathrm{Sym}^2Q'`$ respectively, so the tuple is unambiguous.

With $`cs(Q)=-1/120`$ on $`+\Sigma`$ [Helle, Ex. B.15], Helle's congruence now returns $`cs(Q')=-49/120`$ on $`+\Sigma`$, the residue Proposition 5.2 uses; the residues are also in print [BHKK, Table 1], with classical computations in [FintushelStern], [Auckly], [KirkKlassen]. With the order $`Q-Q'`$ fixed throughout the display, the three residue checks are
```math
cs(Q)-cs(Q')\equiv\tfrac25,\qquad cs(\mathrm{Sym}^2Q)-cs(\mathrm{Sym}^2Q')\equiv\tfrac35,\qquad \rho_{\mathrm{Sym}^2Q}-\rho_{\mathrm{Sym}^2Q'}\equiv\tfrac35\pmod 1
```
(the Dynkin rescaling moves the class: $`4\cdot\tfrac25=\tfrac85\equiv\tfrac35`$). Equivalently, in the $`Q'-Q`$ order used for the main asymmetry,
```math
cs(\mathrm{Sym}^2Q')-cs(\mathrm{Sym}^2Q)\;\equiv\;\rho_{\mathrm{Sym}^2Q'}-\rho_{\mathrm{Sym}^2Q}\;\equiv\;\tfrac25\pmod 1.
```
The checks are mutually consistent and consistent with the unreduced normalization of §2.4; the reduced convention would halve the third residue of the first display to $`\tfrac45`$ and break the $`\tfrac35`$ agreement.

### 5.3 The exact echo

Helle's relation is a congruence mod $`1`$. With $`\varepsilon(H)=-72`$ from the solve, it holds exactly.

> **Proposition 5.3** (Exact echo)**.** With the normalization $`h_0=0`$,
> ```math
> k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})\;=\;D_{Q'}-D_Q\;=\;\frac{\varepsilon(H)}{\lvert 2I\rvert}\;=\;-\frac{72}{120}\;=\;-\frac35,
> ```
> an equality of charges, not only a congruence: Helle's relation lifts to an exact identity in the Kronheimer-Nakajima currency.

*Proof.* The first equality is Lemma 5.1 (the ranks agree). For the second: $`(2-Q)H=Q-Q'`$ gives $`\chi_Q-\chi_{Q'}=(2-\chi_Q)\chi_H`$ pointwise, so
```math
D_{Q'}-D_Q\;=\;\frac{1}{120}\sum_{g\neq 1}\frac{\chi_{Q'}(g)-\chi_Q(g)}{2-\chi_Q(g)}\;=\;-\frac{1}{120}\sum_{g\neq 1}\chi_H(g)\;=\;-\frac{1}{120}\Bigl(120\,h_0-\chi_H(1)\Bigr)\;=\;\frac{\varepsilon(H)}{120},
```
where $`h_0`$ is the trivial multiplicity of $`H`$, which the normalization $`h_0=0`$ makes zero. $`\square`$

> **Corollary 5.4** (The augmentation in three currencies)**.** In the order $`Q-Q'`$ of §5.2,
> ```math
> \rho_Q-\rho_{Q'}\;=\;-4\bigl(k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})\bigr)\;=\;-\frac{4\,\varepsilon(H)}{\lvert 2I\rvert}\;=\;\frac{12}{5}.
> ```

*Proof.* Theorem 1.1 applied to $`Q`$ and $`Q'`$, whose dimensions agree, gives $`\rho_Q-\rho_{Q'}=4(D_Q-D_{Q'})`$; Lemma 5.1 gives $`k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})=D_{Q'}-D_Q`$, whence the first equality, and Proposition 5.3 identifies that charge difference with $`\varepsilon(H)/\lvert 2I\rvert=-3/5`$. $`\square`$

The middle equality is the exchange factor $`\Delta\rho=-4\,\Delta k`$ of Theorem 1.2's proof, now exhibited in the fundamental sector as well as the adjoint one; in the $`Q'-Q`$ order of §4 the same identity reads $`\rho_{Q'}-\rho_Q=-12/5`$. So $`\varepsilon(H)`$ controls three quantities: Helle's Chern-Simons difference modulo $`1`$, the tautological charge difference exactly, and the fundamental rho difference exactly.

*Proof of Theorem 1.2.* Proposition 4.1 gives the pair $`-73/15`$, $`-97/15`$ on $`+\Sigma`$; Corollary 4.2 gives the difference $`-8/5=4\,\Delta D`$ and its golden support; Proposition 5.2 gives $`k\equiv cs\bmod 1`$ in all four sectors; Proposition 5.3 gives the exact echo. Via Theorem 1.1 the charge asymmetry and the rho asymmetry coincide as character sums: the filling does not merely remember that the boundary connections differ, it realizes the difference as a tautological charge difference. Writing every difference in the primed-minus-unprimed order, the exchange factor is $`-4`$, the sign recording that charge counts what rho discounts ($`k=\mathrm{rk}\cdot D_1-D`$ against $`\rho=\dim+4(D-\dim\cdot D_1)`$, so $`\Delta\rho=-4\,\Delta k`$ for the equal-rank pair). $`\square`$

---

## 6. Homological Galois-blindness

The positive half is complete: the filling realizes the boundary's asymmetry as tautological charge. The blind half begins here, in two negatives. This section keeps only the McKay class in the filling's mod-2/mod-4 package, stripped of its decoration; Section 7 tests the one surface refinement that package admits.

> **Lemma 6.1** (The mod-2 package)**.** $`H_2(W;\mathbb{Z}_2)=\mathbb{Z}_2^8`$, and mod 2 the intersection form of $`W`$ is the adjacency form of the $`E_8`$ graph: alternating and nondegenerate, hence a sum of four hyperbolic planes. Consequently $`W`$ has a unique characteristic class, namely $`0`$, and $`W`$ is spin. The intersection form being even, the mod-4 quadratic refinement $`\mathfrak{P}(x):=\xi\cdot\xi \bmod 4`$ (any integral lift $`\xi`$) is well defined; it takes only the values $`\lbrace 0,2\rbrace`$, with $`136=1+135`$ classes of value $`0`$ and $`120`$ of value $`2`$, the Gauss sum $`136-120=16=2^{8/2}e^{2\pi i\,\mathrm{sign}(W)/8}`$ agreeing with van der Blij at $`\mathrm{sign}(W)=-8`$. The $`120`$ classes with $`\mathfrak{P}=2`$ are exactly the mod-2 reductions of the $`240`$ classes $`\xi`$ with $`\xi\cdot\xi=-2`$.

*Proof.* The homology and the form reduction are immediate from the plumbing description ($`-2`$ diagonal vanishes mod 2, the $`-1`$ adjacencies survive); nondegeneracy holds because $`\det`$ of the $`E_8`$ Cartan matrix is $`1`$, odd; the characteristic class is $`0`$ by nondegeneracy of an alternating form, and $`w_2=0`$ then follows from the Wu relation, $`H_1(W)=0`$ leaving no torsion to hide in. The value set and counts of $`\mathfrak{P}`$ are a finite check ($`135=(2^3+1)(2^4-1)`$ is the isotropic-point count of the plus-type quadric); the Gauss-sum agreement is van der Blij's theorem [vanderBlij]. For the last statement: each $`\xi`$ with $`\xi\cdot\xi=-2`$ has $`\mathfrak{P}=2`$; two such classes $`u,v`$ are congruent mod $`2`$ only if $`v=\pm u`$: $`\gamma=(u-v)/2`$ is then integral, and computing with the positive-definite negative of the intersection form, $`\langle u,v\rangle`$ is even, so $`\langle u,v\rangle\in\lbrace -2,0,2\rbrace`$; the values $`\pm2`$ force $`v=\pm u`$ by equality in Cauchy-Schwarz, and $`0`$ is impossible, since it would make $`\gamma`$ a vector of norm $`1`$ in an even lattice. So the $`240`$ such classes reduce to exactly $`240/2=120`$ distinct mod-2 classes [ConwaySloane], all of value $`2`$, and the count matches: they exhaust. (The count $`120`$ arises through the root system of the lattice, not through any bijection with the order of $`2I`$, and no such bijection is used or asserted in this paper.) $`\square`$

*Proof of Theorem 1.3(i).* The Weyl group of the lattice acts transitively on the $`240`$ classes with $`\xi\cdot\xi=-2`$ [ConwaySloane]; it preserves the intersection form, hence descends to $`H_2(W;\mathbb{Z}_2)`$ preserving the mod-2 form and $`\mathfrak{P}`$. By Lemma 6.1 the orbit of any one such reduction is all $`120`$ classes with $`\mathfrak{P}=2`$, so the automorphism group of the triple $`(H_2(W;\mathbb{Z}_2),\ \cdot\ ,\mathfrak{P})`$ is transitive on them. Any invariant depending only on the isomorphism class of the pointed quadratic space $`(H_2(W;\mathbb{Z}_2),\cdot,\mathfrak{P};x)`$ therefore takes the same value at every such $`x`$; in particular none distinguishes $`[\,\mathcal{E}_{\mathrm{Sym}^2Q'}\,]_2`$, the class of the exceptional curve of the distance-six adjoint node, from any other class with $`\mathfrak{P}=2`$. Whether a self-diffeomorphism of $`W`$ realizes a given automorphism is a separate question, neither claimed nor needed. $`\square`$

Within the mod-2/mod-4 package, then, Galois-sensitivity cannot live in a class: it can live only in a decoration of a class. Section 5 exhibited the decoration that carries it, the tautological bundle over the node. Section 7 examines the one further slot in this package that refines a class beyond its isomorphism type, the characteristic-surface data.

---

## 7. Non-orientable characteristic surfaces and the decoupling

The Brown/Guillou-Marin theory of characteristic surfaces is the slot of the package $`(H_2(W;\mathbb{Z}_2),\ \cdot\ ,\mathfrak{P})`$ that carries data beyond the class itself: a quadratic enhancement on the curves of the surface, with its Brown invariant. This section determines whether that slot can register the Galois asymmetry. At the level of ordinary bundle restriction and the canonical Guillou-Marin enhancement it cannot, and the obstruction is a disjointness the section will substantiate: where the enhancement exists the bundles are invisible, and where the bundles are visible the enhancement does not exist. The argument is in four steps: §7.1 shows the slot is populated, §7.2 records that the slot's own constants are Galois-blind, §7.3 defines the restriction route, and §7.4 proves the restriction triviality of Theorem 1.3(ii), from which the route terms cancel in the Galois difference.

### 7.1 Non-orientable representability

> **Proposition 7.1.** Every class $`x\in H_2(W;\mathbb{Z}_2)`$ is represented by embedded closed non-orientable surfaces of every sufficiently large non-orientable genus, and the representatives constructed below satisfy
> ```math
> e(F)+2\chi(F)\;\equiv\;\mathfrak{P}(x)\pmod 4.
> ```
> The congruence ties $`e`$ to $`\chi`$, hence to the genus, so which normal Euler numbers are congruence-admissible depends on the genus. At non-orientable genus $`h`$ the construction realizes a bounded window of congruence-admissible $`e`$ about $`\xi\cdot\xi`$, widening with $`h`$, so each congruence-admissible $`e`$ appears once the genus is large enough. Which normal Euler numbers are realizable at a fixed genus by any means is not determined here.

*Proof.* Choose an integral lift $`\xi`$ of $`x`$ and a smoothly embedded closed connected oriented representative $`F_0`$ (standard for integral classes of a compact oriented $`4`$-manifold), with normal Euler number $`e(F_0)=\xi\cdot\xi`$ and $`\chi(F_0)`$ even. A local cross-cap (connected sum, inside a ball, with the standard $`\mathbb{RP}^2\subset S^4`$ of normal Euler number $`\pm2`$) changes $`(\chi,e)`$ by $`(-1,\pm2)`$ and preserves the $`\mathbb{Z}_2`$ class; the combination $`e+2\chi \bmod 4`$ is invariant under the move, and starts at $`\xi\cdot\xi\equiv\mathfrak{P}(x) \bmod 4`$. After $`k\ge 1`$ cross-caps the surface is non-orientable of genus $`h=2g_0+k`$, with $`g_0`$ the genus of $`F_0`$, and the values this construction produces are $`\xi\cdot\xi+2j`$ for the $`j`$ with $`\lvert j\rvert\le k`$ and $`j\equiv k \bmod 2`$, the parity being the mod-4 congruence itself. These are the congruence-admissible values in the window $`\lvert e-\xi\cdot\xi\rvert\le 2k`$, so each of them appears once $`k`$ is large enough. Whether some other construction produces more at a fixed genus is not addressed here, and some bound is expected: in $`S^4`$ the normal Euler number of a non-orientable surface of fixed genus lies in a finite range [Massey]. The congruence itself is the ambient form of a classical constraint (Whitney's $`e\equiv 2\chi \bmod 4`$ in $`S^4`$, proved by Massey [Massey]; a homology-cobordism version is [LRS, Prop. 2.5], whose ambient hypotheses differ from $`(W,x)`$ here, which is why the construction above is kept self-contained). $`\square`$

### 7.2 The characteristic slot and its congruence

> **Proposition 7.2.** For a closed non-orientable characteristic surface $`F\subset\mathrm{int}\,W`$ (here: $`[F]_2=0`$, the unique characteristic class), the normal Euler number and the Brown invariant of the Guillou-Marin enhancement satisfy
> ```math
> e(F)+2\beta(F)\;\equiv\;\mathrm{sign}(W)+8\,\mu(\Sigma)\;\equiv\;0\pmod{16},
> ```
> with $`\mu(\Sigma)=1`$ the Rokhlin invariant (the sign of the $`8\mu`$ term is immaterial: $`8\mu\equiv-8\mu \bmod 16`$); since $`\mu\equiv\bar\mu \bmod 2`$, the Neumann normalization $`\bar\mu=-1`$ gives the same landing. On the negative-definite $`E_8`$ convention $`\mathrm{sign}(W)=-8`$, so $`\mathrm{sign}(W)+8\mu=0`$; the positive-definite convention gives $`+8+8\equiv0\pmod{16}`$, the same. Every constant in the congruence ($`\mathrm{sign}(W)=\pm8`$, $`\mu=1`$, $`\bar\mu=-1`$) is blind to the Galois action, as Theorem 1.3(i) requires.

*Proof.* This is a specialization of the relative Guillou-Marin theorem in the form printed by Klug [Klug, Thm. 6] (notation adapted: we write $`\mathrm{sign}`$ for the signature, $`\sigma`$ being reserved): for a compact oriented topological $`4`$-manifold $`M`$ with $`\partial M`$ an integral homology sphere and $`F`$ a characteristic, not necessarily orientable, properly embedded surface, $`2\beta(F)+2\beta(\partial F)=\mathrm{sign}(M)-F\cdot F+8\mu(\partial M)+8\,\mathrm{KS}(M) \bmod 16`$, with $`\mathrm{KS}`$ the Kirby-Siebenmann invariant. Here $`F`$ is closed, so $`\beta(\partial F)=0`$; $`W`$ is smooth, so $`\mathrm{KS}=0`$; and $`F\cdot F`$ is the normal Euler number $`e(F)`$. Calibration on the closed $`\mathbb{RP}^2\subset S^4`$ (Klug's own example, $`\mathrm{sign}(S^4)=0`$, $`\mu(S^3)=0`$): $`e=+2`$ forces $`\beta=-1`$, landing on $`0`$. The closed case is Guillou-Marin [GuillouMarin], in Matsumoto's exposition [Matsumoto]; the topological correction $`8\,\mathrm{KS}`$ is Kirby-Taylor [KirbyTaylor]. $`\square`$

The Brown invariant is not an invariant of the homology class [Klug]: it is decoration data on the characteristic slot, which is exactly the role this section assigns it.

### 7.3 Mechanisms and the restriction route

How can an embedded surface enter an index identity over $`W`$? We isolate one classical localization that belongs to the restriction route for a specified equivariant lift, and then record two further candidate formulations that motivate the definition but are not used here as established examples.

**(a) The $`G`$-signature theorem on the double branched cover.** For $`[F]_2=0`$, the double cover of $`W`$ branched along $`F`$ exists, and its deck involution has fixed set $`F`$. If a coefficient bundle $`\mathcal{R}`$ on $`W`$ is pulled back with the canonical lift of the deck action, the action on its fibres over $`F`$ is trivial. The $`F`$-supported contribution to the resulting equivariant twisted index is therefore built from the ordinary characteristic classes of $`\mathcal{R}\vert_F`$, paired against the normal-bundle data of $`F`$. This specified canonical lift belongs to the restriction route. A different equivariant lift may act nontrivially on the coefficient fibres over $`F`$; such a term lies outside the route defined below.

**(b) The with-boundary Guillou-Marin mechanism.** Proposition 7.2 supplies the intrinsic surface package consisting of the normal Euler number, the pin enhancement, and its Brown invariant. We do not invoke a coefficient-twisted relative Guillou-Marin theorem. If such a theorem were to couple an external bundle $`\mathcal{R}`$ to $`F`$ only through characteristic-class data of $`\mathcal{R}\vert_F`$, its surface term would belong to the restriction route; neither the existence nor the form of that coupling is established here.

**(c) A twisted-pin-Dirac formulation.** A meridian-twisted pin-Dirac construction on $`W\smallsetminus F`$ could provide another coefficient-carrying surface formula. We do not identify a specific operator or index theorem of this kind. Any formulation whose $`F`$-supported coefficient dependence were linear in $`\mathrm{ch}(\mathcal{R}\vert_F)`$ would belong to the restriction route; formulations retaining restricted-connection, holonomy, or nontrivial equivariant-fibre data would not.

The restriction route isolates surface terms of the form
```math
\bigl(\text{characteristic-class data of }\mathcal{R}\vert_F\bigr)\times\bigl(\text{bundle-independent surface, normal, and pin data}\bigr).
```

> **Definition 7.3** (Restriction route)**.** A localization identity over $`W`$ belongs to the *restriction route* if its $`F`$-supported terms pair the characteristic-class (Chern-character) data of the restriction $`\mathcal{R}\vert_F`$ linearly against bundle-independent surface, normal-bundle, and pin data. Here $`\mathcal{R}`$ is the canonical pullback coefficient bundle, and, where a covering is present, the deck action on its fibres over the fixed set is trivial. An identity whose $`F`$-term uses more of the bundle, such as a nontrivial equivariant fibre action or the holonomy of the restricted connection, is outside the definition. Mechanism (a), for the canonical pullback lift, is an example. The possible formulations in (b) and (c) are not established here to belong to the route.

### 7.4 The triviality lemma

> **Lemma 7.4.** Every complex or real vector bundle on $`W`$ restricts topologically trivially to every closed connected non-orientable surface $`F\subset W`$ with $`[F]_2=0`$, and every virtual class on $`W`$ restricts to its virtual rank.

*Proof.* For a closed non-orientable surface, $`H^2(F;\mathbb{Q})=0`$ and $`H^2(F;\mathbb{Z})=\mathbb{Z}_2`$ (universal coefficients), and the mod-2 reduction $`H^2(F;\mathbb{Z})\to H^2(F;\mathbb{Z}_2)`$ is injective, with the evaluation of a class restricted from $`W`$ against the $`\mathbb{Z}_2`$-fundamental class equal to the pairing with $`i_*[F]_2=0`$ in $`W`$. So every degree-two class of $`W`$, integral or mod 2, restricts to zero on $`F`$. Every bundle from $`W`$ has $`w_1=0`$ ($`H^1(W;\mathbb{Z}_2)=0`$, §2.4), hence is orientable along $`F`$, and its classifying data over the $`2`$-complex $`F`$ (rank and $`c_1`$ for complex bundles; $`w_2`$, or the untwisted Euler class in the oriented rank-two case, for real bundles) are restricted from $`W`$, hence vanish on $`F`$ by the preceding argument. Standard obstruction theory over a $`2`$-complex then gives triviality; virtual classes follow by additivity, restricting to their virtual rank. Nothing about the tautological structure is used. $`\square`$

Lemma 7.4 is Theorem 1.3(ii).

*Proof of Corollary 1.4.* Let the identity belong to the restriction route. By Lemma 7.4, the coefficient restriction $`\mathcal{R}\vert_F`$ is trivial, so its characteristic-class data reduces to the rank and the $`F`$-supported term is $`\mathrm{rk}(\mathcal{R})\,T_F`$, with $`T_F`$ independent of $`\mathcal{R}`$. Since the two adjoint tautological bundles both have rank $`3`$, every such term cancels in their Galois difference, and the coefficient coupling $`(e(F),\beta(F))`$ to $`\rho_{\mathrm{Sym}^2Q'}-\rho_{\mathrm{Sym}^2Q}=-8/5`$ is exactly zero along this route. Mechanism §7.3(a), with the canonical pullback lift, supplies one instance of the route. $`\square`$

Two complementary cases delimit the remaining escapes, and their disjointness is the structural point. On a class with $`\mathfrak{P}=2`$, say $`x=[\mathcal{E}_{\mathrm{Sym}^2Q'}]_2`$, the restriction of the matching tautological bundle is nontrivial ($`\langle c_1(\mathcal{R}_{\mathrm{Sym}^2Q'}) \bmod 2,\ x\rangle=1`$ by the dual-basis property), so a surface there does couple to the decoration; but the canonical Guillou-Marin enhancement supplied by the ambient characteristic-surface setup is not available off the characteristic class, so there is no Brown datum to couple. An orientable characteristic surface (integral class $`2\xi`$) pairs integrally with $`c_1`$, but carries the Arf package of the classical Rokhlin story, $`w_1(F)=0`$: orientation-preserving data, not the non-orientable normal twist. Where the enhancement exists, the bundles are invisible; where the bundles are visible, the enhancement does not exist. What Corollary 1.4 does not assert is any universal independence: identities outside Definition 7.3 are not addressed.

*Proof of Theorem 1.3.* Part (i) is proved in §6, part (ii) is Lemma 7.4. $`\square`$

---

## 8. Discussion

The two halves of the paper are one computation seen from two sides. The same four golden classes carry the boundary rho difference (Corollary 4.2), reappear in the exact charges of the tautological bundles (Propositions 5.2 and 5.3), and are invisible to the mod-2/mod-4 quadratic package (Theorem 1.3(i)) and to every restriction-route surface term (Corollary 1.4). In one sentence: within the homological package the Galois action cannot be seen at all, and within the tautological decoration it is seen exactly; $`\mathrm{Sym}^2Q'`$ is not special as a mod-2/mod-4 class, it is special only as a decorated McKay node.

The Guillou-Marin detection that opened the paper does its classical work, reading the signature defect mod 16; the finer Galois asymmetry lies beyond it, and surfaces instead in the tautological decoration.

The working dictionary is Theorem 1.1. It is a general, quotable identity between the odd-signature and index-formula currencies for every finite $`\Gamma\subset\mathrm{SU}(2)`$, with a sharp hypothesis, and on $`S^3/2I`$ it is verified against four printed rho values ($`59/30`$ and $`131/30`$ from [BHKK]; $`-73/15`$ and $`-97/15`$ from [Anvari]) and the Chern-Simons residues of [BHKK, Table 1]. Through it, the charge asymmetry and the rho asymmetry are literally the same character sum, which is what makes the exact echo $`k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})=\varepsilon(H)/\lvert 2I\rvert`$ close arithmetically rather than merely mod 1.

Status and open questions. Whether the affine conversion appears implicitly in the space-form eta literature is a question of record, not of proof; the closest treatments ([Degeratu], [CisnerosMolina], [Gilkey]) evaluate the two sides separately, and we could not locate the odd-signature form. The minimal non-orientable genus in each class of $`H_2(W;\mathbb{Z}_2)`$ is not determined here. Whether any identity outside the restriction route of Definition 7.3 couples embedded-surface data to the Galois difference is open, as is whether the classes with $`\mathfrak{P}=2`$ admit any canonical pin-type package that could replace the characteristic-slot enhancement.

Directions. Among the exceptional binary polyhedral groups $`2T`$, $`2O`$, $`2I`$, the binary icosahedral group carries the unique Galois pair with distinct adjoints, and its two neighbours fail for different reasons. The binary octahedral group does have two determinant-one two-dimensional irreducibles, but they differ by the order-two sign character $`\varepsilon`$, so that $`\mathrm{Sym}^2(Q\otimes\varepsilon)=\mathrm{Sym}^2Q\otimes\varepsilon^2=\mathrm{Sym}^2Q`$: the pair shares its adjoint. The binary tetrahedral group fails a step earlier. Its other two-dimensional irreducibles are the twists $`Q\otimes\chi`$ by the nontrivial cube roots of unity in $`\mathrm{Hom}(2T,\mathbb{C}^\times)`$, and $`\det(Q\otimes\chi)=\chi^2\neq 1`$, so there is no second determinant-one candidate and no pair to begin with. For $`2I`$, perfectness removes the octahedral coincidence, leaving $`Q`$ and $`Q'`$ with distinct adjoints at McKay distances $`2`$ and $`6`$. The restriction to these three is needed, and is why they are named rather than called the binary polyhedral groups, a term some authors extend to the binary dihedral case: in the binary dihedral group $`D_5^*`$ the determinant-one two-dimensional irreducibles $`\tau_1`$ and $`\tau_3`$ are already exchanged by $`\sqrt5\mapsto-\sqrt5`$ and have distinct adjoints.

Beyond $`2I`$, the same defect machinery computes the conversion identity's two sides for every spherical space form, and Corollary 3.2 extends the identity to twists with trivial constituents by the exact offset. On the four-dimensional side, the other ALE fillings carry the same tautological structure, and the equivariant refinements of instanton theory ([DaemiScaduto], [MillerEismeier] as context) are the natural place to ask the coupling question beyond the restriction route.

---

## References

- **[Anvari]** N. Anvari, Extending smooth cyclic group actions on the Poincaré homology sphere. *Pacific J. Math.* **282** (2016), no. 1, 9–25.
- **[APS2]** M. F. Atiyah, V. K. Patodi, I. M. Singer, Spectral asymmetry and Riemannian geometry II. *Math. Proc. Cambridge Philos. Soc.* **78** (1975), 405–432.
- **[Auckly]** D. R. Auckly, Topological methods to compute Chern-Simons invariants. *Math. Proc. Cambridge Philos. Soc.* **115** (1994), 229–251.
- **[BHKK]** H. U. Boden, C. M. Herald, P. Kirk, E. P. Klassen, Gauge theoretic invariants of Dehn surgeries on knots. *Geom. Topol.* **5** (2001), 143–226.
- **[BotvinnikGilkey]** B. Botvinnik, P. B. Gilkey, The eta invariant and metrics of positive scalar curvature. *Math. Ann.* **302** (1995), 507–517.
- **[CisnerosMolina]** J. L. Cisneros-Molina, The $`\eta`$-invariant of twisted Dirac operators of $`S^3/\Gamma`$. *Geom. Dedicata* **84** (2001), 207–228.
- **[ConwaySloane]** J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups. 3rd ed., Grundlehren **290**, Springer (1999).
- **[DaemiScaduto]** A. Daemi, C. Scaduto, Equivariant aspects of singular instanton Floer homology. arXiv:1912.08982 (2019).
- **[Degeratu]** A. Degeratu, Eta-invariants from Molien series. *Q. J. Math.* **60** (2009), doi:10.1093/qmath/han016.
- **[FintushelStern]** R. Fintushel, R. J. Stern, Instanton homology of Seifert fibred homology three spheres. *Proc. London Math. Soc.* (3) **61** (1990), 109–137.
- **[Gilkey]** P. B. Gilkey, The eta invariant and the K-theory of odd dimensional spherical space forms. *Invent. Math.* **76** (1984), 421–454.
- **[GuillouMarin]** L. Guillou, A. Marin, Une extension d'un théorème de Rohlin sur la signature. *C. R. Acad. Sci. Paris Sér. A-B* **285** (1977), A95–A98.
- **[HeddenKirk]** M. Hedden, P. Kirk, Chern-Simons invariants, SO(3) instantons, and $`\mathbb{Z}/2`$-homology cobordism. arXiv:1009.5365 (2010).
- **[Helle]** G. O. Helle, Equivariant instanton Floer homology and calculations for the binary polyhedral spaces. arXiv:2203.09471 (2022).
- **[KirbyTaylor]** R. C. Kirby, L. R. Taylor, Pin structures on low-dimensional manifolds. In: Geometry of Low-Dimensional Manifolds 2, LMS Lecture Note Ser. **151**, Cambridge (1990), 177–242.
- **[KirkKlassen]** P. Kirk, E. Klassen, Chern-Simons invariants of 3-manifolds and representation spaces of knot groups. *Math. Ann.* **287** (1990), 343–367.
- **[Klug]** M. R. Klug, A relative version of Rochlin's theorem. arXiv:2011.12418 (2021).
- **[KronheimerNakajima]** P. B. Kronheimer, H. Nakajima, Yang-Mills instantons on ALE gravitational instantons. *Math. Ann.* **288** (1990), 263–307.
- **[LRS]** A. S. Levine, D. Ruberman, S. Strle, Nonorientable surfaces in homology cobordisms. *Geom. Topol.* **19** (2015), 439–494.
- **[Massey]** W. S. Massey, Proof of a conjecture of Whitney. *Pacific J. Math.* **31** (1969), 143–156.
- **[Matsumoto]** Y. Matsumoto, An elementary proof of Rochlin's signature theorem and its extension by Guillou and Marin. In: À la recherche de la topologie perdue, Progr. Math. **62**, Birkhäuser (1986), 119–139.
- **[McKay]** J. McKay, Graphs, singularities, and finite groups. *Proc. Sympos. Pure Math.* **37** (1980), 183–186.
- **[MillerEismeier]** M. Miller Eismeier, Equivariant instanton homology. arXiv:1907.01091 (2019).
- **[Nakajima]** H. Nakajima, Moduli spaces of anti-self-dual connections on ALE gravitational instantons. *Invent. Math.* **102** (1990), 267–303.
- **[NeumannSiebenmann]** W. D. Neumann, An invariant of plumbed homology spheres, and L. Siebenmann, On vanishing of the Rohlin invariant and nonfinitely amphicheiral homology 3-spheres. Both in: Topology Symposium Siegen 1979, Lecture Notes in Math. **788**, Springer (1980), 125–144 and 172–222.
- **[RubermanSaveliev]** D. Ruberman, N. Saveliev, The $`\bar\mu`$-invariant of Seifert fibered homology spheres and the Dirac operator. *Geom. Dedicata* **154** (2011), 93–101.
- **[Saveliev]** N. Saveliev, Invariants for Homology 3-Spheres. Encyclopaedia Math. Sci. **140**, Springer (2002).
- **[vanderBlij]** F. van der Blij, An invariant of quadratic forms mod 8. *Indag. Math.* **21** (1959), 291–293.

---

## Citation

```
Shatto, B. (2026)
An Affine Rho–Index Conversion and the Galois Pair on the Poincaré Homology Sphere
https://ssrn.com/abstract=7129118
```

---

## Independent numerical certification

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_1_method_note.md)

The arithmetic of this paper has been reproduced on the OpenWave M8 track by an independent, blind computation in exact cyclotomic arithmetic, with an adversarial audit that recomputed everything by a disjoint route: groups from presentations, characters induced from cyclic subgroups, and a purely rational path that never enters the number field. Across 37 groups and thousands of twists the audit confirmed the values and refuted none.

The substantive verifications are the exact numbers of Theorem 1.2 and its consequences, reproduced twice. The four rho invariants came out $`-59/30`$, $`-131/30`$, $`-73/15`$, $`-97/15`$, their Galois difference $`-8/5`$ supported exactly on the four conjugacy classes of element order five and ten, matching the golden-class localization of Corollary 4.2. The tautological charges $`119/120`$, $`191/120`$, $`59/30`$, $`71/30`$ reproduced; the affine solve returned $`H = (0,0,-1,-2,-3,-4,-3,-2,-2)`$ with augmentation $`-72`$ and charge difference $`-3/5`$, exactly the assignment §5 specifies; and the mod-2 package of §6 came out as $`240`$ root vectors reducing two-to-one onto $`120`$ classes, alternating and nondegenerate, with the $`\mathfrak{P}=2`$ set identical to the root classes and swept by a single reflection orbit. The kernel identity held in the field on every class of every group, at a numeric residual of $`3.7 \times 10^{-60}`$ over sixty digits. These are contingent facts about a specific group, independently reproduced.

The conversion identity of Theorem 1.1 carries a qualification the audit supplied. The solver was not told that an affine relation between the two currencies was expected, and it recovered the exact coefficients $`(1, 4, -4)`$ at zero residual, with Corollary 3.2's additive offset appearing as the trivial multiplicity in every case. The audit then derived that the relation is algebraically forced for every finite $`\Gamma \subset \mathrm{SU}(2)`$, in agreement with this paper's own reading that the identity follows in three lines from two classical formulas. The blind run therefore confirms the group construction, the character values, and the arithmetic that carry the identity, not the truth of a relation that could have come out otherwise.

The run is scoped to the paper's computable content. Theorem 1.3(ii) and the whole of §7, structural topology with no finite object to evaluate, are read only; and the classical geometric inputs the currencies rest on, the Atiyah-Patodi-Singer defect formula, Degeratu's twisted-Dirac eta identity, and the Kronheimer-Nakajima index integral, are handed to the solver as definitions rather than tested. The [method note](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_1_method_note.md) carries the full record, including the audit's split of which claims are forced and which are contingent.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
