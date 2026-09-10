<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# ⏈ First Eigenvalue

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/cone%20point%20banner.png?raw=true" width="100%" alt="First Eigenvalue">

In a singular quantum system a global topological holonomy and a local point defect can both enter the spectrum; here they separate, the defect controlling the ground state while the topology and the curvature control the first positive level. We study an exactly solvable quantum Hamiltonian on a singular non-orientable surface: the Laplace-Beltrami operator on sections of the orientation line bundle over a constant-curvature Möbius band $`M(W)`$ of curvature radius $`R`$, with one transverse fiber collapsed to a cone point. The orientation bundle imposes a $`\mathbb{Z}_2`$ sign holonomy; the collapsed fiber is a conic point defect at which the Hamiltonian is not essentially self-adjoint, whose self-adjoint extensions are the physical boundary conditions. We compare the Friedrichs realization with the sector-regular bridging family, the two-dimensional point interaction at the defect with renormalization length $`\delta_0`$. The ground state is extension-dependent: the Friedrichs realization has bottom $`0`$, with a discontinuous zero mode, and is unitarily equivalent to a Neumann lune problem, while bridging carries a cone-localized defect bound state $`\lambda_b(\delta_0) = -4e^{-2\gamma}/\delta_0^2\,(1 + O(\delta_0^2/R^2))`$ as $`\delta_0 \to 0^+`$, and no self-adjoint extension has strictly positive bottom. The first positive level, by contrast, is stable even though the gap above the ground state is not: for the Friedrichs extension and for bridging with $`\delta_0 > 2R/e`$ it equals $`2/R^2`$ for $`0 < W \le \pi R/2`$ and $`\alpha_0(\alpha_0+1)/R^2`$, $`\alpha_0 = \pi R/(2W)`$, beyond, a width-driven mode crossing. The spectrum is reduced explicitly to Legendre functions.

---

## 1. Introduction

Quantum mechanics on Möbius and other non-orientable geometries is by now an active mesoscopic subject, from energy levels and optical transitions on Möbius rings [LiRM] to electronic states in Möbius quantum wires [PSA]. Across it, and across the broader study of singular quantum systems, two ingredients recur: a global flat holonomy, the spectral analogue of an Aharonov-Bohm phase [Shigekawa], and a local point interaction at a defect [AGHH, KayStuder]. In many models the two spectral effects are coupled. The purpose of the present paper is to isolate them in an exactly solvable non-orientable conic geometry: the defect controls the bottom of the spectrum, while the holonomy and curvature control the first positive level.

On a Möbius band the orientation line bundle has nontrivial holonomy: after one circuit of the core loop a section changes sign. On a smooth non-orientable surface a continuous nowhere-vanishing section of the orientation line bundle would trivialize it, so the usual scalar Perron-Frobenius ground-state mechanism is unavailable for the twisted Laplacian (cf. [Shigekawa] for the magnetic spectral-positivity criterion). This paper asks how that topological obstruction is expressed when the configuration space also carries a conic defect.

**The model.** We study the Hamiltonian of a quantum particle constrained to a singular non-orientable surface. The operator is $`H = -\Delta_{\mathcal{L}}`$, the Laplace-Beltrami operator on sections of the orientation line bundle $`\mathcal{L}`$ over the constant-curvature Möbius band $`M(W)`$. The band is constructed from a spherical band on $`S^2(R)`$ of half-width $`W`$, with metric $`ds^2 = dy^2 + \cos^2(y/R)\,dw^2`$, cone point $`p_c`$ at $`y = \pi R/2`$, and Neumann conditions on the regular boundary arcs. Both singular structures are intrinsic. The twist is the holonomy of the orientation bundle. The cone is produced by the metric itself, as the meridians focus at the pole of the covering sphere. The physical dictionary is short. The Möbius twist is the nontrivial flat real line-bundle holonomy, the real analogue of an Aharonov-Bohm phase $`\pi`$. The cone is a point defect at which $`H`$ fails to be essentially self-adjoint, so the self-adjoint extensions are the physical boundary conditions at the defect. The bridging family among them realizes the standard two-dimensional point interaction, with the renormalization length $`\delta_0`$ entering as short-distance defect data rather than as geometry. Negative eigenvalues are defect-bound states. The paper tracks the first positive level, measured from zero rather than from the extension-dependent ground state. Constant curvature is chosen not as a geometric restriction but as an exact-solvability mechanism: every reduced one-dimensional problem below is Legendre. The competition between bundle topology and defect data therefore closes in special functions, from the operator domain to the individual eigenfunctions.

**The two realizations.** At $`p_c`$ the operator is not essentially self-adjoint in the constant transverse sector (the transverse-mode subspaces of §3.4), and it is there that the realizations we compare differ. They are the *Friedrichs extension* $`\Delta_F`$, the standard conic choice, and the *sector-regular bridging realization* $`A^{\mathrm{br}}_{\delta_0}`$, the point interaction at renormalization length $`\delta_0`$ (Definition 3.5). In the wide-band regime $`W > \pi R/2`$ the first odd transverse sector is also limit-circle at the cone. Both realizations fix it by the regular Frobenius branch, and the scope of the stability statement is fixed accordingly (Remark 1.3). Geometrically, $`M(W)`$ is a spherical lune with its two vertices identified, the antipodal quotient of a double lune (Remark 2.1). The Friedrichs conditions impose independent data at the two vertices, while the bridging conditions couple them across the identification.

**Results.** The two singular structures act on different spectral data, and separating their effects is the point of the paper. The twist is a sign condition on eigenfunctions, while the location of the bottom is settled by the extension at the defect. The discontinuous piecewise-constant section $`\phi_0`$ is a genuine zero mode of the Friedrichs realization, whose maximality bounds the bottom of every self-adjoint extension from above by $`0`$; the bridging family replaces $`\phi_0`$ by a logarithmic defect-bound state below zero. The gap above the ground state is therefore extension-dependent, moving with $`\delta_0`$, while the first positive level is stable. It is common to the Friedrichs realization and to every sector-regular bridging realization with $`\delta_0 > 2R/e`$, with a width-driven mode crossing at the critical width $`W = \pi R/2`$. In short, the conic defect controls the ground state, while the topology and the curvature control the first positive level.

> **Theorem 1.1** (Ground-state dependence on the cone interaction)**.** Let $`0 < W < \pi R`$.
>
> **(i)** *(Universal bound)* Every self-adjoint extension $`A`$ at the cone of the twisted Laplacian on $`M(W)`$ satisfies $`\inf\sigma(A) \le 0`$, with equality if and only if $`A`$ is nonnegative. In particular no self-adjoint extension has strictly positive spectral bottom.
>
> **(ii)** *(Friedrichs)* Among the nonnegative extensions the Friedrichs extension is maximal, and its bottom $`0`$ is attained by the discontinuous piecewise-constant zero mode $`\phi_0`$, the constant-sector kernel.
>
> **(iii)** *(Sector-regular bridging)* The sector-regular bridging realization $`A^{\mathrm{br}}_{\delta_0}`$ (Definition 3.5) is not nonnegative: it carries a single cone-localized negative eigenvalue $`\lambda_b(\delta_0)`$, with small-$`\delta_0`$ asymptotic $`\lambda_b(\delta_0) = -4e^{-2\gamma}/\delta_0^2\,(1 + O(\delta_0^2/R^2))`$, $`\gamma`$ the Euler-Mascheroni constant, and zero lies in its resolvent set.

> **Theorem 1.2** (Stable first positive level and width-driven mode crossing)**.** The first positive eigenvalue of the twisted Laplacian on $`M(W)`$ is shared by the Friedrichs extension $`\Delta_F`$ and by the sector-regular bridging realization $`A^{\mathrm{br}}_{\delta_0}`$ (Definition 3.5) for every $`\delta_0 > 2R/e`$, and equals
>
> ```math
> \lambda_1(W) = \begin{cases} 2/R^2, & 0 < W \le \pi R/2, \\ \alpha_0(\alpha_0+1)/R^2, & \pi R/2 < W < \pi R, \end{cases} \qquad \alpha_0 = \frac{\pi R}{2W}.
> ```
>
> At $`W = \pi R/2`$ it is doubly degenerate. Both branches are realized by explicit eigenfunctions: in the narrow regime $`\sin(y/R)`$, the $`\ell = 1`$ zonal Legendre polynomial; in the wide regime $`\lvert\cos(y/R)\rvert^{\alpha_0}\sin(\pi w/2W)`$, whose profile in $`y`$ is $`(1-x^2)^{\alpha_0/2}`$ in the variable $`x = \sin(y/R)`$, reducing to the sectoral harmonic $`P_{\alpha_0}^{\alpha_0}`$ at integer degree.

> **Remark 1.3** (Scope of the stability statement)**.** Theorem 1.2 is not a statement about every self-adjoint extension of the singular operator: it concerns the Friedrichs extension and the sector-regular bridging family of Definition 3.5. In the wide-band regime $`W > \pi R/2`$ the first odd transverse sector is also limit-circle at the cone (Lemma 3.3), and non-sector-regular extensions there lie outside the class studied here. Part (i) of Theorem 1.1 is, by contrast, universal: $`\inf\sigma(A) \le 0`$ holds for every self-adjoint extension $`A`$, with no sector-regularity hypothesis.

For the Friedrichs extension the operator is unitarily equivalent to the Neumann Laplacian on a spherical lune of opening $`2W/R`$ (Proposition 4.2); there Theorem 1.2 is the first nonzero Neumann eigenvalue of the lune, and the mode crossing is the crossing of the two lowest lune branches. What the lune does not capture is the persistence across the bridging family and the extension-dependence of the bottom.

**Related work and placement.** Two lines of work meet in this model: the quantum mechanics of point interactions and cones, and the spectral geometry of conic extensions.

*Point interactions and cone quantum mechanics.* The two-dimensional one-center point interaction is classical [AGHH]. On a cone, Kay and Studer [KayStuder] parametrized the apex extension by a length scale and obtained a logarithmic bound-state branch. Our bridging condition is the Kirchhoff-type vertex condition [BK] realizing the corresponding one-center interaction at the conic apex of a curved non-orientable surface: the same logarithmic defect-bound branch appears in the constant sector, now coupled to the Möbius $`\mathbb{Z}_2`$ holonomy and to the width-driven transition, neither of which is present in the single-cone setting. The deformed eigenvalue tower this produces is an instance of the rank-one secular mechanism of Colin de Verdière's pseudo-Laplacians [CdV], here with the interlacing towers explicit. Within the mesoscopic Möbius family, the present model supplies an exactly solvable singular endpoint.

*Conic extension theory.* The spectral geometry of cone-like singularities begins with Cheeger [Cheeger1979, Cheeger1983], who fixed the Friedrichs extension at such points, and was classified for the model conic metric by Boscain and Prandi [BP]. Our surface sits at their cone parameter $`\alpha_{\mathrm{BP}} = -1`$, the regime in which the constant angular mode is the distinguished sector carrying the extension ambiguity; in the wide-band case the first odd sector also becomes limit-circle, but the sector-regular class studied here fixes it by the regular Frobenius branch. This is the dichotomy we exploit, together with the holonomy spectra of flat line bundles [BBC]. The closest Möbius-strip predecessor is Kalvoda, Krejčiřík, and Zahradová [KKZ], whose thin-strip analysis of the Dirichlet Laplacian on a curved Möbius strip in $`\mathbb{R}^3`$ yields effective Mathieu dynamics. We differ in two decisive ways: the Neumann condition supplies the constant mode that makes the cone a limit-circle endpoint, and the geodesic core keeps the conic degeneration present at every width. The result is an exact finite-width calculation rather than a thin-strip asymptotic; the common feature with the thin-strip model is the parity bookkeeping imposed by the Möbius holonomy, discussed again in §7.

Against this background, the contribution is not a new extension theory or a new secular method, but the exact assembly of these classical ingredients in the orientation-bundle Möbius geometry, where the extension-dependent bottom and the extension-stable first positive level are computed simultaneously and explicitly.

**Method and organization.** The proof separates the operator into transverse Neumann sectors and solves each reduced Sturm-Liouville problem in closed form via Legendre functions. Only the constant (zonal) sector carries the cone-condition ambiguity that separates the realizations. Cone parity (reflection about $`p_c`$, $`y \mapsto \pi R - y`$, equivalently the exchange of the two lune vertices) splits it into a symmetric tower, common to both, and an antisymmetric tower, where they differ. The value $`2/R^2`$ comes from the symmetric tower; the zero or negative bottom comes from the antisymmetric tower, where the bridging condition deforms the Friedrichs zero mode through an explicit secular function (§4). The rest of the paper follows this separation. Section 2 sets up the geometric model and Section 3 the operator domain, the extensions, and Friedrichs maximality. We then analyze the zonal sector by parity (§4), assemble the ground-state classification (§5), resolve the nonconstant sectors and the mode crossing (§6), and close with the physical interpretation and limiting regimes (§7).

---

## 2. The Geometric Model $`M(W)`$

Consider the round 2-sphere $`S^2(R)`$ of radius $`R`$. Throughout, $`R`$ is the curvature radius of this constant-curvature model. Let $`C`$ be a great circle, and let $`y`$ denote arclength along a meridian measured from $`C`$, so that $`y = 0`$ and $`y = \pi R`$ correspond to antipodal arcs of $`C`$ reached on opposite sides of the pole at $`y = \pi R/2`$. Let $`w`$ denote arclength along $`C`$, with $`w \in [-W, W]`$ for a half-width parameter $`0 < W < \pi R`$. The induced metric on the band $`\{(y, w) : 0 \le y \le \pi R,\; \lvert w\rvert \le W\}`$ is

```math
ds^2 = dy^2 + \cos^2(y/R)\,dw^2.
```

The Gauss curvature is $`K = 1/R^2`$ on the smooth locus and the scalar curvature is $`R_{\mathrm{sm}} = 2/R^2`$.

The Möbius band is obtained from the rectangle $`[0, \pi R] \times [-W, W]`$ by the single edge identification $`(0, w) \sim (\pi R, -w)`$. This gluing is the restriction to the edge $`\{y = 0\}`$ of the isometry $`\tau(y, w) = (\pi R - y, -w)`$, since $`\tau(0, w) = (\pi R, -w)`$. The interior $`0 < y < \pi R`$ carries no identification, so $`M(W)`$ is not the quotient of the band by the global involution $`\tau`$. The result is the non-orientable surface

```math
M(W) = [0, \pi R] \times [-W, W] \;/\; (0, w) \sim (\pi R, -w)
```

with boundary $`\partial M \cong S^1`$, since the two arcs $`w = \pm W`$ join into a single closed curve under the identification. The non-orientability arises from the edge identification itself: the seam reverses the boundary coordinate, $`w \mapsto -w`$, while the inward normal direction continues across it, so a frame transported around the core loop returns with $`\partial_w \mapsto -\partial_w`$ and no orientation can be chosen consistently.

At $`y = \pi R/2`$, the metric coefficient $`\cos(y/R)`$ vanishes, collapsing the transverse fiber $`\{y = \pi R/2\} \times [-W, W]`$ to a single point $`p_c`$ in the metric space. Both boundary arcs pass through $`p_c`$ (the boundary meridians meet at the pole), so $`p_c \in \partial M`$ and the boundary curve has a corner there. The two descriptions of the boundary operate at different levels: $`\partial M \cong S^1`$ refers to the boundary circle of the underlying band, while in the metric space $`M(W)`$ the image of this circle passes through $`p_c`$ twice, the wedge of two loops described below.

The local model is the one-point union of two half-cones meeting at the apex $`p_c`$: a punctured neighborhood of $`p_c`$ is disconnected into the $`y < \pi R/2`$ and $`y > \pi R/2`$ halves, since the geodesic distance to $`p_c`$ equals $`\lvert y - \pi R/2\rvert`$ and crossing between halves requires the collapsed fiber, every point of which is $`p_c`$. The link is two disjoint intervals $`[-W, W]`$, each of angular length $`2W/R`$; each half-cone has opening angle $`2W/R`$; and the closed boundary curve passes through $`p_c`$ twice, a figure-eight through the apex, with a corner on each side. This two-sided structure is what the four-dimensional cone boundary space and the deficiency count of §3 already encode.

> **Remark 2.1** (Double-lune realization)**.** There is a complementary fundamental domain that makes the role of the cone conditions geometric. For $`0 < W < \pi R/2`$, let $`L`$ be the closed spherical lune bounded by the meridians at longitude $`\pm W/R`$, with vertices at the two poles $`N`$ and $`S`$, and let the *double lune* be $`L \cup (-L)`$, with $`-L`$ its antipodal image; the two embedded lunes then meet exactly at the shared vertices. For $`W \ge \pi R/2`$ the same construction is understood as an abstract double lune, the embedded lunes no longer meeting only at the vertices. The antipodal map exchanges $`L`$ with $`-L`$ and $`N`$ with $`S`$, and the quotient of the double lune by it is the single lune $`L`$ with its two vertices identified (Figure 1). This quotient is $`M(W)`$: collapsing the fiber $`\{y = \pi R/2\}`$ and cutting along the seam reassembles the band into $`L`$, with the identified vertex pair becoming the cone point $`p_c`$. The two half-cones of the local model above are the two lune vertices (each of opening $`2W/R`$), and the figure-eight boundary is the two meridians closing through the identified vertex. The picture makes the extension dichotomy of §3.5 geometric: the Friedrichs domain imposes independent regularity conditions at the two lune vertices, so after trivialization its spectrum is the Neumann lune spectrum of Proposition 4.2, without encoding the vertex identification, while the bridging domains impose continuity of the regularized values and Kirchhoff matching of the logarithmic fluxes between the two vertex traces, thereby encoding the quotient identification $`N \sim S`$.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/double-lune.png?raw=true" width="70%" alt="Schematic double-lune realization: double lune on the sphere and its antipodal quotient, a lune with identified vertices">

**Figure 1.** Schematic double-lune realization of Remark 2.1, narrow case $`W < \pi R/2`$. Left: the double lune $`L \cup (-L)`$ on $`S^2(R)`$, the antipodal lune dashed. Right: the quotient by the antipodal map, a single lune whose two vertices are identified; the identified vertex pair is the cone point $`p_c`$ of $`M(W)`$, and the two lune sides become the boundary curve through $`p_c`$.

Under Neumann boundary conditions at $`w = \pm W`$, the transverse problem unfolds onto a circle link of angular circumference $`4W/R`$ (§3.4), recovering the circle-link framework of Boscain and Prandi [BP] with parameter $`\alpha_{\mathrm{BP}} = -1`$. Although $`p_c`$ lies on $`\partial M`$ as a surface point, it lies at $`y = \pi R/2`$, interior to the longitudinal interval $`(0, \pi R)`$. The reduced one-dimensional eigenvalue problems of §§4 and 6 inherit this interior singular-point structure, and the extension theory of §3 applies in full.

The cone angle $`2W/R`$ equals $`\pi`$ at the critical width $`W = \pi R/2`$. For $`W < \pi R/2`$ (narrow band), the cone angle is less than $`\pi`$; for $`W > \pi R/2`$ (wide band), it exceeds $`\pi`$. As $`W \to \pi R`$, each half of the band approaches a hemisphere.

---

## 3. Twisted Sections and the Operator Domain

### 3.1 The orientation line bundle

Real line bundles over $`M(W)`$ are classified by $`H^1(M; \mathbb{Z}_2) = \mathbb{Z}_2`$ (the band retracts to its core circle): the trivial bundle carries the ordinary scalar Laplacian, and the orientation line bundle $`\mathcal{L}`$ carries the twisted sector studied here, the sign-holonomy sector of the introduction. A smooth function on the parameter rectangle $`[0, \pi R] \times [-W, W]`$ descends to a section of $`\mathcal{L} \to M`$ if and only if it satisfies the equivariance condition

```math
\psi(\pi R, -w) = -\psi(0, w) \qquad \text{for all } w \in [-W, W].
```

This sign reversal is the defining property of a section of $`\mathcal{L}`$.

The *twisted Laplacian* is the Laplace-Beltrami operator acting on sections of $`\mathcal{L}`$. It is the standard Laplace-Beltrami operator on the smooth locus, twisted only in its domain (sections of $`\mathcal{L}`$ rather than functions). The eigenvalue problem $`-\Delta\psi = \lambda\psi`$ is posed for sections of $`\mathcal{L}`$ throughout this paper. Throughout, the analysis lives on the smooth locus $`M^\circ = M \setminus \{p_c\}`$. Sections are $`L^2`$ sections over $`M^\circ`$ subject to the seam condition; no value or continuity at $`p_c`$ is imposed unless a self-adjoint extension selects it (§3.5). In particular the discontinuous Friedrichs zero mode of §4 is a legitimate section in this sense: the cone point enters only through the metric completion and through the extension data at the cone traces.

### 3.2 The formal operator

On the smooth locus $`M^\circ = M \setminus \{p_c\}`$ (where $`p_c`$ denotes the cone point at $`y = \pi R/2`$), the Laplace-Beltrami operator associated to the metric $`ds^2 = dy^2 + f(y)^2\,dw^2`$ with $`f(y) = \cos(y/R)`$ is

```math
\Delta\psi = \psi_{yy} + \frac{f'}{f}\psi_y + \frac{1}{f^2}\psi_{ww} = \psi_{yy} - \frac{1}{R}\tan\!\Bigl(\frac{y}{R}\Bigr)\psi_y + \frac{1}{\cos^2(y/R)}\psi_{ww}.
```

The area element is $`dA = \lvert f(y)\rvert\,dy\,dw`$, and $`L^2(M, dA)`$ denotes the Hilbert space of square-integrable sections of $`\mathcal{L}`$ with respect to this measure. Although the formal operator is written using $`f`$ on each smooth coordinate patch, the global measure and the reduced Sturm-Liouville forms use $`\lvert f\rvert`$, which is nonnegative across the two sides of the collapsed fiber.

The boundary $`\partial M`$ consists of two geodesic arcs at $`w = \pm W`$. We impose Neumann boundary conditions: $`\partial_w\psi\big\vert_{w = \pm W} = 0`$.

### 3.3 The collapsed fiber and the cone point

The cone point $`p_c`$ arises from the metric degeneration alone: at $`y = \pi R/2`$ the coefficient $`f = \cos(y/R)`$ vanishes, so the whole transverse fiber $`\{y = \pi R/2\} \times [-W, W]`$ collapses to the single point $`p_c`$ of the metric completion, independently of the edge identification. The reflection $`\delta \mapsto -\delta`$ about this fiber ($`\delta = y - \pi R/2`$), that is $`y \mapsto \pi R - y`$, is realized by the covering isometry $`\tau(y, w) = (\pi R - y, -w)`$; its fixed point $`(\pi R/2, 0)`$ is one point of the collapsed fiber, not $`p_c`$ itself. Thus $`\tau`$ enters the construction in two distinct ways: its restriction to the edge $`\{y = 0\}`$ is the gluing map of §2, and the reflection $`\delta \mapsto -\delta`$ commutes with the reduced operator and organizes the parity decomposition of §4.

At $`p_c`$, $`f(\pi R/2) = \cos(\pi/2) = 0`$. Setting $`\delta = y - \pi R/2`$:

```math
f(y) = \cos(y/R) = -\sin(\delta/R) \quad \Longrightarrow \quad \lvert f\rvert \sim \frac{\lvert\delta\rvert}{R} \quad \text{as } \delta \to 0.
```

The transverse fiber $`[-W, W]`$ has metric length $`2W\lvert f(y)\rvert`$, which collapses to zero. On the covering $`S^2`$, the coordinate $`y = \pi R/2`$ is a smooth pole; on the edge-identified Möbius band, the same collapse produces a conical singularity with cone angle $`2W/R`$.

The surface is smooth away from $`p_c`$, with constant Gaussian curvature $`K = 1/R^2`$ and smooth-locus scalar curvature $`R_{\mathrm{sm}} = 2K = 2/R^2`$. Distributional curvature at $`p_c`$ is not invoked in this paper.

### 3.4 Transverse decomposition and cone asymptotics

Separation of variables $`\psi(y,w) = u(y)\,\Phi(w)`$ with $`-\Phi'' = \mu\,\Phi`$ subject to Neumann conditions $`\Phi'(\pm W) = 0`$ yields two families of transverse eigenmodes on $`[-W, W]`$.

*Even family* (symmetric under $`w \mapsto -w`$):

```math
\Phi_k^{\mathrm{e}}(w) = \cos(k\pi w/W), \qquad \mu_k^{\mathrm{e}} = (k\pi/W)^2, \qquad k = 0, 1, 2, \ldots
```

The case $`k = 0`$ is the constant mode $`\Phi_0^{\mathrm{e}} \equiv 1`$ with $`\mu_0 = 0`$.

*Odd family* (antisymmetric under $`w \mapsto -w`$):

```math
\Phi_j^{\mathrm{o}}(w) = \sin\bigl((2j+1)\pi w/(2W)\bigr), \qquad \mu_j^{\mathrm{o}} = \bigl((2j+1)\pi/(2W)\bigr)^2, \qquad j = 0, 1, 2, \ldots
```

Together these modes generate the orthogonal decomposition

```math
L^2(M, dA) \;=\; \bigoplus_{\sigma} \mathcal{H}_\sigma, \qquad \mathcal{H}_\sigma = \bigl\lbrace\, u(y)\,\Phi_\sigma(w) \;:\; u \in L^2\bigl((0, \pi R), \lvert f\rvert\,dy\bigr) \bigr\rbrace,
```

with $`\sigma`$ running over the transverse modes $`\Phi_k^{\mathrm{e}}`$, $`\Phi_j^{\mathrm{o}}`$ above. We call the summands $`\mathcal{H}_\sigma`$ *transverse sectors*; the *constant sector* is the $`k = 0`$ summand, and the qualifiers *odd*, *even*, and *nonconstant* always refer to this decomposition. Proposition 3.7 shows that the realizations studied here reduce over it, so the spectral problem becomes the family of one-dimensional problems treated below. At the $`L^2`$ level the seam and the collapsed fiber have measure zero, so the decomposition is one of Hilbert spaces only; the periodic or anti-periodic seam condition attached to each transverse parity, and the cone conditions, enter through the reduced operator domains, not through the decomposition itself.

The Möbius identification $`\psi(\pi R, -w) = -\psi(0, w)`$ interacts with the transverse parity as follows. For even $`\Phi(w) = \Phi(-w)`$, the identification forces $`u(\pi R) = -u(0)`$: the longitudinal function is anti-periodic. For odd $`\Phi(-w) = -\Phi(w)`$, it forces $`u(\pi R) = u(0)`$: the longitudinal function is periodic. In the operator domain the derivative traces inherit the same matching, $`u'(\pi R) = -u'(0)`$ in the even case and $`u'(\pi R) = u'(0)`$ in the odd case, so the seam is a regular endpoint carrying a self-adjoint anti-periodic or periodic condition.

A Neumann eigenmode on $`[-W, W]`$ extends by even reflection to a periodic function on the circle link of angular circumference $`4W/R`$ in the variable $`\theta = w/R`$. Labeling harmonics by their index on this circle, the even family $`\Phi_k^{\mathrm{e}}`$ carries the even harmonics (index $`2k`$) and the odd family $`\Phi_j^{\mathrm{o}}`$ the odd harmonics (index $`2j+1`$); the $`k = 0`$ constant mode is the zero harmonic, the analogue of the $`k = 0`$ Fourier sector in [BP], and the non-essential-self-adjointness of the constant-sector reduced operator at the cone (Theorem 1.6(ii) of [BP]) is the same phenomenon in both settings.

> **Lemma 3.1** (Neumann unfolding)**.** After the change of angular variable $`\theta=w/R`$, even reflection at the Neumann endpoints identifies each transverse Neumann eigensector on $`[-W,W]`$ with a Fourier eigensector on the circle link of angular circumference $`4W/R`$ (unitarily, up to a normalization factor from reflection). For each transverse sector, the reduced one-dimensional operator in $`y`$ has the same singular endpoint at $`\delta = 0`$, the same weight $`\lvert\delta\rvert/R`$, and the same indicial equation. Since the maximal domain, Lagrange bracket, and deficiency indices depend only on the local behavior at the singular endpoint [Weidmann], the same local boundary data appear as in the Boscain-Prandi cone model [BP], and the Friedrichs and bridging realizations are defined directly from these cone traces in §3.5 (Definition 3.5).

*Proof.* The Neumann condition at each endpoint of the interval link permits even reflection across both endpoints, producing a periodic function on the doubled link of length $`4W/R`$. This reflection is unitary up to the harmless factor coming from doubling the interval. Near the cone the longitudinal operator depends only on the link eigenvalue $`\mu`$ and on the weight $`\lvert f\rvert \sim \lvert\delta\rvert/R`$, so the indicial equation, maximal-domain asymptotics, Lagrange bracket, and limit-point/limit-circle classification are identical to those of the corresponding Fourier sector on the circle-link cone. The cone trace coordinates used below are therefore the same local trace coordinates as in the Boscain-Prandi model. $`\square`$

In each sector, the reduced eigenequation for the longitudinal function $`u(y)`$ takes the Sturm-Liouville form

```math
-\bigl(\lvert f\rvert\,u'\bigr)' + \frac{\mu}{\lvert f\rvert}\,u = \lambda\,\lvert f\rvert\,u, \qquad f(y) = \cos(y/R),
```

on $`L^2\bigl((0, \pi R),\,\lvert f\rvert\,dy\bigr)`$, where $`\mu`$ is the transverse eigenvalue of the sector. Near the cone ($`\delta \to 0`$, $`\lvert f\rvert \sim \lvert\delta\rvert/R`$), this becomes

```math
-\Bigl(\frac{\lvert\delta\rvert}{R}\,u'\Bigr)' + \frac{\mu R}{\lvert\delta\rvert}\,u = \lambda\,\frac{\lvert\delta\rvert}{R}\,u.
```

Substituting $`u = \lvert\delta\rvert^s`$ into the leading-order balance gives the indicial equation $`s^2 = \mu R^2`$.

*The constant sector* ($`\mu = 0`$, even family $`k = 0`$). The indicial equation gives $`s^2 = 0`$ (double root). The two local solutions are

```math
u_{\mathrm{reg}} = a_0 + a_2\delta^2 + O(\delta^4), \qquad u_{\mathrm{log}} = \log\lvert\delta\rvert + b_2\delta^2 + O(\delta^4).
```

Both are square-integrable against the weight $`\lvert\delta\rvert/R\,d\delta`$: $`\int \lvert\delta\rvert^0 \cdot \lvert\delta\rvert\,d\delta < \infty`$ and $`\int (\log\lvert\delta\rvert)^2 \cdot \lvert\delta\rvert\,d\delta < \infty`$. The cone is a limit-circle endpoint, and a self-adjoint extension must be chosen.

*Nonconstant sectors with $`\alpha \ge 1`$.* Write $`\alpha = \sqrt{\mu}\,R`$ for the indicial exponent. When $`\alpha \ge 1`$, the singular branch $`\lvert\delta\rvert^{-\alpha}`$ fails the $`L^2`$ condition against the weight:

```math
\int u^2\,\lvert f\rvert\,d\delta \sim \int \lvert\delta\rvert^{-2\alpha} \cdot \lvert\delta\rvert\,d\delta = \int \lvert\delta\rvert^{1-2\alpha}\,d\delta = \infty \qquad \text{for } \alpha \ge 1.
```

The cone is limit-point. Self-adjointness is unique; no extension choice arises.

*Nonconstant sectors with $`0 < \alpha < 1`$.* This regime occurs only for wide bands: $`W > \pi R/2`$ for the $`j = 0`$ odd mode. Both branches $`\lvert\delta\rvert^{\pm\alpha}`$ are now $`L^2`$ against the weight (since $`1 - 2\alpha > -1`$). The cone is limit-circle. The branches are distinguished by the Dirichlet energy. For the singular branch $`u = \lvert\delta\rvert^{-\alpha}`$,

```math
\int (u')^2\,\lvert f\rvert\,d\delta \sim \alpha^2\!\int \lvert\delta\rvert^{-2\alpha-1}\,d\delta = \infty \qquad \text{for all } \alpha > 0,
```

so the singular branch has infinite Dirichlet energy. The Friedrichs extension selects the regular branch $`\lvert\delta\rvert^{+\alpha}`$, the unique branch of finite Dirichlet energy, and every realization of finite Dirichlet energy in this sector coincides with it there.

The limit-point/limit-circle classification at a singular endpoint depends only on the local behavior of the coefficients [Weidmann, KSWW], and the local expansions are regular-singular in the sense of Brüning and Seeley [BS]. Near $`p_c`$, the weight $`\lvert f\rvert`$ vanishes linearly in $`\delta`$, matching the flat-cone case $`\alpha_{\mathrm{BP}} = -1`$ in the notation of [BP]. On the model cone of [BP] (angular period $`2\pi`$) only $`k = 0`$ has $`\alpha < 1`$; the unfolded period $`4W/R`$ adds the wide-band first odd sector, with exponent $`\alpha_0 = \pi R/(2W)`$, to the limit-circle list. The extension structure this produces is recorded in Lemma 3.3 below.

> **Remark 3.2** (Continuity heuristic for the constant sector)**.** If a continuous section $`\psi = u(y)\,\Phi(w)`$ has nonconstant transverse profile $`\Phi`$, then $`u(\pi R/2) = 0`$: the collapsed fiber is a single point of $`M(W)`$, and a nonzero apex value would assign it several values. The constant mode alone tolerates a nonzero apex value, which is the geometric reason why, once the regular branch is fixed in every nonconstant sector (Definition 3.5), the residual extension freedom lives in the constant sector. The operative criterion, however, is the limit-point/limit-circle classification above, not continuity: the actual ground states, the discontinuous $`\phi_0`$ and the logarithmically divergent bridging mode, both fail continuity at $`p_c`$.

> **Lemma 3.3** (Wide-band odd-sector endpoint)**.** For $`0 < W \le \pi R/2`$ every nonconstant transverse sector is limit-point at $`p_c`$ and the minimal operator has total deficiency indices $`(2,2)`$, carried entirely by the constant sector. For $`\pi R/2 < W < \pi R`$ the first odd sector, with indicial exponent $`\alpha_0 = \pi R/(2W) < 1`$, is in addition limit-circle, and the total indices are $`(4,4)`$. Under the Liouville substitution $`v = \lvert f\rvert^{1/2}u`$ the reduced operator of that sector is $`-v'' + g\,\delta^{-2}v + O(1)`$ near the cone, with inverse-square coupling $`g = \alpha_0^2 - \tfrac14 \in (-\tfrac14, \tfrac34)`$. Every sectorwise self-adjoint realization of this inverse-square endpoint is bounded below.

*Proof.* The classification follows from $`\lvert f\rvert \sim \lvert\delta\rvert/R`$ and the indicial equation $`s^2 = \mu R^2`$, whose roots are $`s = \pm\alpha_0`$: for $`\alpha_0 \ge 1`$ the singular root leaves $`L^2`$ (limit-point), for $`0 < \alpha_0 < 1`$ both roots are square-integrable (limit-circle), and at $`W = \pi R/2`$ exactly $`\alpha_0 = 1`$, so the count stays $`(2,2)`$. The substitution $`v = \lvert f\rvert^{1/2}u`$ sends $`-(\lvert f\rvert\,u')' + (\mu/\lvert f\rvert)u`$ to $`-v'' + g\,\delta^{-2}v + O(1)`$ with $`g = s^2 - \tfrac14 = \alpha_0^2 - \tfrac14`$. For $`g > -\tfrac14`$ Hardy's inequality makes the local form nonnegative, and on the finite interval with one regular (seam) endpoint the deficiency is finite, so each self-adjoint realization differs from the Friedrichs one by at most finitely many eigenvalues and is bounded below [KSWW, RS]. $`\square`$

> **Remark 3.4** (Aharonov-Bohm flux analogy)**.** In the flat-line-bundle/Aharonov-Bohm language of the introduction, the wide-band effect is the geometric analogue of lowering the shifted angular momentum at a flux line. The $`\pi`$ holonomy shifts the transverse-longitudinal pairing by half a unit, and widening the band drags the lowest shifted momentum into the limit-circle window at the origin.

Neither finite Dirichlet energy nor semiboundedness alone singles out a realization in the wide band: the constant-sector logarithmic mode of §4.4 has infinite Dirichlet energy, and by Lemma 3.3 the singular-branch odd extensions are semibounded as well. We therefore work only with realizations that select the regular (Frobenius) branch in every nonconstant sector, the Friedrichs choice there, and we do not treat realizations that couple distinct transverse sectors. The reduction of every extension question to the cone traces of the individual sectors rests on the unfolding equivalence of Lemma 3.1. The two we single out, the Friedrichs and bridging realizations, are defined in §3.5 (Definition 3.5).

### 3.5 The cone boundary form and point-interaction extensions

Once the regular Frobenius branch is fixed in every nonconstant sector (§3.4), the only remaining extension choice that distinguishes Friedrichs from bridging lies in the constant sector ($`\mu = 0`$), where both local solutions are $`L^2`$. Near the cone, the general constant-sector solution has the asymptotic form

```math
u(\delta) = u_N\,\ln\frac{\lvert\delta\rvert}{2R} + u_D + o(1) \qquad (\delta \to 0),
```

with a log coefficient $`u_N`$ (the flux datum) and a regularized value $`u_D`$ (referenced to the length $`2R`$), independently on each side of the cone. We write $`u_D^\pm`$ and $`u_N^\pm`$ for the limits from $`\delta \to 0^\pm`$.

The $`1/R`$ normalization is fixed directly by the two local branches. Take $`u_{\mathrm{reg}} = 1 + O(\delta^2)`$ (so $`u_N = 0`$, $`u_D = 1`$) and $`u_{\mathrm{log}} = \ln(\lvert\delta\rvert/2R) + O(\delta^2)`$ (so $`u_N = 1`$, $`u_D = 0`$); with $`\lvert f\rvert \sim \lvert\delta\rvert/R`$ the weighted Wronskian is

```math
\lvert f\rvert\bigl(u_{\mathrm{reg}}\,u_{\mathrm{log}}' - u_{\mathrm{reg}}'\,u_{\mathrm{log}}\bigr) = \frac{\lvert\delta\rvert}{R}\Bigl(\frac{1}{\delta} + O(\delta\ln\lvert\delta\rvert)\Bigr) \longrightarrow \frac{\mathrm{sgn}\,\delta}{R} \qquad (\delta \to 0),
```

so the Lagrange bracket of the regular and log branches at the apex is $`[u_{\mathrm{reg}}, u_{\mathrm{log}}]_{p_c} = 1/R`$ on each side. Both branches are square-integrable against $`\lvert f\rvert\,d\delta`$ (§3.4), so each of the two half-cones contributes a two-dimensional cone trace $`(u_D^\pm, u_N^\pm)`$, and together they span the four-dimensional boundary space $`(u_D^+, u_N^+, u_D^-, u_N^-)`$. This is obtained from the model's own weight $`\lvert f\rvert = \lvert\cos(y/R)\rvert`$ and the indicial data of §3.4; the circle-link cone of [BP] carries the same local structure.

The cone boundary form produced by Green's identity is

```math
[u, v]_{p_c} = \frac{1}{R}\sum_{\pm}\bigl(u_D^\pm\,v_N^\pm - u_N^\pm\,v_D^\pm\bigr),
```

where the logarithmic divergences cancel pairwise: a direct computation from the near-cone reduced form gives $`\lvert f\rvert(u v' - u' v) \to (\mathrm{sgn}\,\delta/R)(u_D v_N - u_N v_D)`$ as $`\delta \to 0`$, and the two-sided Green identity sums these limits with the outward-normal orientation, yielding the boundary form above. The normals fix the overall sign; a global sign only rescales the symplectic form, leaving its Lagrangian planes unchanged. A self-adjoint extension corresponds to a two-dimensional Lagrangian plane (a subspace on which this boundary form vanishes identically) in the four-dimensional boundary space $`(u_D^+, u_N^+, u_D^-, u_N^-)`$. The extension data here are the cone traces alone; the regular arcs $`w = \pm W`$ carry their fixed Neumann condition and enter no extension choice.

*The Friedrichs (disjoint) extension.* The Friedrichs extension [Friedrichs] is characterized by Theorem 1.8 of [BP] (applied at $`\alpha_{\mathrm{BP}} = -1`$): its domain requires

```math
u_N^+ = 0 \qquad\text{and}\qquad u_N^- = 0,
```

with no condition relating $`u_D^+`$ to $`u_D^-`$. This is two conditions on four parameters, and the plane $`\{u_N^+ = u_N^- = 0\}`$ is Lagrangian: the boundary form vanishes when both fluxes are zero. The domain imposes no matching condition at $`p_c`$, so the two cone traces $`u_D^\pm`$ are unconstrained and the constant-sector form $`q_0`$ decomposes as $`q_0^+ \oplus q_0^-`$ on the two halves $`M^\pm = \{\pm(y - \pi R/2) > 0\}`$ (coupled only through the seam identification, not through $`p_c`$). This is the "disjoint dynamics" case $`c^+ = c^- = 0`$ of [BP].

*The bridging extension at renormalization length $`\delta_0`$.* Boscain and Prandi (Theorem 1.8 of [BP]) classify the conic extensions into a disjoint family and a mixed family, the mixed one parametrized by $`K \in \mathrm{SL}_2(\mathbb{R})`$; their Remark 1.9 names the $`K = \mathrm{Id}`$ case the bridging extension. To equip this condition with a renormalization length $`\delta_0 > 0`$, we use the standard two-dimensional point-interaction renormalization [AGHH, KayStuder]. In the conic trace coordinates this means re-expressing the data relative to $`\delta_0`$,

```math
u(\delta) = u_N\,\ln\frac{\lvert\delta\rvert}{\delta_0} + \tilde u_D + o(1), \qquad \tilde u_D = u_D + u_N\,\ln\frac{\delta_0}{2R},
```

and imposing

```math
\tilde u_D^+ = \tilde u_D^- \qquad \text{(continuity of the regularized value),}
```

```math
u_N^+ + u_N^- = 0 \qquad \text{(Kirchhoff flux matching).}
```

This is two conditions on four parameters. The plane is Lagrangian: since $`u_D^\pm = \tilde u_D^\pm - u_N^\pm\ln(\delta_0/2R)`$, the $`\ln(\delta_0/2R)`$ terms cancel pairwise in the boundary form, and for $`u, v`$ both satisfying the bridging conditions,

```math
[u, v]_{p_c} = \frac{1}{R}\Bigl[\tilde u_D\bigl(v_N^+ + v_N^-\bigr) - \tilde v_D\bigl(u_N^+ + u_N^-\bigr)\Bigr] = 0.
```

The value condition is continuity across the cone; the flux condition is the sign-flipped (Kirchhoff) matching dictated by the opposite outward normals on the two sides. Different choices of $`\delta_0`$ yield distinct self-adjoint extensions with distinct spectra. In the fixed trace coordinates $`(u_D^\pm, u_N^\pm)`$ the family sweeps a one-parameter family of Lagrangian planes, each the $`K = \mathrm{Id}`$ condition expressed in its own $`\delta_0`$-renormalized coordinates. The renormalization length is a genuine parameter, set neither by the metric nor by the bundle alone.

> **Definition 3.5** (Sector-regular realizations)**.** A self-adjoint realization of the twisted Laplacian is *sector-regular* if at $`p_c`$ it selects the regular (Frobenius) branch in every nonconstant transverse sector. We use two. The *Friedrichs extension* $`\Delta_F`$ takes the regular branch in the constant sector as well. For each $`\delta_0 > 0`$ the *bridging realization* $`A^{\mathrm{br}}_{\delta_0}`$ takes in the constant sector the logarithmic matching $`\tilde u_D^+ = \tilde u_D^-`$, $`u_N^+ + u_N^- = 0`$ at renormalization length $`\delta_0`$ (the condition above), and the regular branch in every nonconstant sector. These realizations are self-adjoint; $`\Delta_F`$ is nonnegative (§3.6), and §4.4 shows that $`A^{\mathrm{br}}_{\delta_0}`$ is semibounded with bottom $`\lambda_b(\delta_0) < 0`$. In the wide band both additionally take the regular (Frobenius) branch in the first odd sector, so they lie within the $`(4,4)`$-family of Lemma 3.3, while the realizations that activate the singular odd branch are not sector-regular. Sector-regularity fixes every nonconstant branch but leaves the constant-sector cone condition free, so $`\Delta_F`$ and $`A^{\mathrm{br}}_{\delta_0}`$ are two distinguished sector-regular realizations, not an exhaustive pair.

> **Remark 3.6** (Scattering dictionary)**.** In the point-interaction language of [AGHH, KayStuder], sector-regularity confines the defect interaction to the s-wave, i.e. the constant angular channel. Every other channel, including the wide-band first odd one, is held at the regular branch, so the width transition remains a holonomy/geometry effect rather than a second point-interaction parameter.

For any constant $`c \ne 0`$, the discontinuous piecewise-constant section

```math
\phi_0(y, w) = \begin{cases} +c & \text{if } y < \pi R/2, \\ -c & \text{if } y > \pi R/2, \end{cases}
```

has $`u_N^\pm = 0`$ and $`\tilde u_D^+ = -c \ne +c = \tilde u_D^-`$, so it lies in the Friedrichs domain (it satisfies the Friedrichs flux conditions) but is excluded from every bridging domain (it fails value-continuity). Since $`-\Delta\phi_0 = 0`$ on the smooth locus and $`\phi_0`$ satisfies the equivariance condition, it is a genuine eigenfunction with eigenvalue $`0`$ for the Friedrichs extension: a domain wall pinned at the defect. Its transverse profile is constant, so it lies in the constant sector.

The covering geometry constrains, but does not by itself fix, the extension. A section of $`\mathcal{L}`$ that lifts to a function smooth at the pole of the covering $`S^2`$ is regular there ($`u_N = 0`$) and even in $`\delta`$; this forces the regular branch in the symmetric subsector (§4.2) but does not determine the cone condition in the antisymmetric subsector, where the natural candidates are the Friedrichs and bridging conditions above. The remaining choice is the antisymmetric cone condition, which is what separates Friedrichs from bridging in §5.

> **Proposition 3.7** (Operator realization)**.** The formal twisted Laplacian commutes with the transverse Neumann Laplacian, since $`\cos^2(y/R)`$ depends on $`y`$ alone. The Friedrichs extension and the sector-regular bridging realization $`A^{\mathrm{br}}_{\delta_0}`$ impose cone conditions sector by sector, so the transverse Neumann decomposition $`L^2(M, dA) = \bigoplus_\sigma \mathcal{H}_\sigma`$ reduces both operators. In each sector the reduced Sturm-Liouville operator in $`y`$, with the seam condition from anti-equivariance and the cone condition of Definition 3.5, is self-adjoint with compact resolvent. The sector bottoms diverge, so each direct sum is self-adjoint with compact resolvent and discrete spectrum. Thus $`\Delta_F`$ and $`A^{\mathrm{br}}_{\delta_0}`$ are these orthogonal direct sums.

*Proof.* Commutation gives the reducing decomposition, and the form closure respects it: each transverse spectral projection maps the core into itself with $`\sum_\sigma q[P_\sigma\psi] = q[\psi]`$ by Parseval in $`w`$, so the closed form is the orthogonal sum of the sector forms. Each reduced operator is regular-singular on a finite interval with integrable weight $`\lvert f\rvert`$; by §3.4 the cone is limit-point in every sector except the constant one and, for $`W > \pi R/2`$, the first odd one (Lemma 3.3), where Definition 3.5 imposes a self-adjoint cone condition. So each sector operator is self-adjoint with compact resolvent [Weidmann], and since the sector bottoms tend to infinity (established at the end of §6.2) the orthogonal direct sum has compact resolvent. $`\square`$

### 3.6 Friedrichs maximality

Friedrichs maximality is a statement about a fixed lower-semibounded symmetric operator, which we name here. Let $`T_{\min}`$, the *minimal twisted Laplacian*, be the closure in $`L^2(M(W), \mathcal{L})`$ of $`-\Delta`$ acting on smooth anti-equivariant sections that vanish in a neighborhood of the cone point $`p_c`$ and satisfy the Neumann condition $`\partial_w\psi\big\vert_{w = \pm W} = 0`$. It is densely defined, symmetric, and nonnegative (the form $`q`$ below is $`\ge 0`$ on its domain), and its only locus of non-essential-self-adjointness is $`p_c`$, every boundary arc being a regular endpoint (§3.4). The *Friedrichs extension* $`\Delta_F`$ is the Friedrichs extension of $`T_{\min}`$, and $`q_F`$ is the closure of the form $`\psi \mapsto \langle T_{\min}\psi, \psi\rangle`$ in the form norm $`\lVert\cdot\rVert_q`$ of the associated quadratic form $`q`$ below. Imposing $`\partial_w\psi = 0`$ pointwise on the operator core does not shrink the form domain: the form carries no boundary term at the arcs, and smooth sections with vanishing normal derivative there are dense in form norm among all smooth sections (flattening the transverse parametrization near a regular arc changes the energy arbitrarily little), so the closure returns the same $`\mathcal{D}(q_F)`$ obtained below from the free core $`\mathcal{C}`$.

The Dirichlet form on $`M(W)`$

```math
q[\psi] = \int_{M^\circ}\lvert\nabla\psi\rvert^2\,dA, \qquad M^\circ = M(W)\setminus\{p_c\},
```

is nonnegative on the core $`\mathcal{C}`$ of smooth anti-equivariant sections on the closed smooth locus $`\overline{M^\circ}`$, smooth up to the boundary arcs $`w = \pm W`$ with no condition imposed there, and with support compact in $`\overline{M^\circ}\setminus\{p_c\}`$ (excised only at the cone). The free arcs make the Neumann condition natural: $`\partial_w\psi\big\vert_{w = \pm W} = 0`$ is recovered from $`q`$ on closure, whereas a core of support compact in the open manifold would close to Dirichlet data at $`w = \pm W`$ and remove the constant transverse mode. The Friedrichs extension $`\Delta_F`$ is the self-adjoint operator associated with the closure of $`q`$ on $`\mathcal{C}`$: "Friedrichs" designates the extension at the cone $`p_c`$, the only locus of extension ambiguity (§3.5), the arcs keeping their Neumann condition throughout. Its form domain $`\mathcal{D}(q_F) = \overline{\mathcal{C}}^{\,\lVert\cdot\rVert_q}`$ is contained in the form domain of every self-adjoint extension at the cone whose form is bounded below by that of $`q`$; by finite deficiency every extension here is semibounded, so after a shift this covers them all (§5).

> **Lemma 3.8** (Friedrichs maximality)**.** Let $`A`$ be any self-adjoint extension of the minimal twisted Laplacian on $`M(W)`$.
>
> **(i)** The minimal operator is nonnegative, and $`\Delta_F`$ is its largest nonnegative extension in the Birman-Krein-Vishik order [AlonsoSimon]: $`\mathcal{D}(q_F) \subseteq \mathcal{D}(q_A)`$ for every nonnegative extension $`A`$, so by min-max $`\lambda_n(A) \le \lambda_n(\Delta_F)`$ for all $`n`$, and in particular $`\inf\sigma(A) \le \inf\sigma(\Delta_F)`$.
>
> **(ii)** $`\inf\sigma(\Delta_F) = 0`$: the form $`q \ge 0`$ gives $`\inf\sigma(\Delta_F) \ge 0`$, and $`\phi_0 \in \mathcal{D}(\Delta_F)`$ with $`\Delta_F\phi_0 = 0`$ (Lemma 4.1) gives $`\inf\sigma(\Delta_F) \le 0`$.
>
> **(iii)** Consequently $`\inf\sigma(A) \le 0`$ for every self-adjoint extension $`A`$: for nonnegative $`A`$ by (i)–(ii), and for non-nonnegative $`A`$ by definition. The argument uses only nonnegativity of the minimal operator, with no parity hypothesis.

*Proof.* (i) is the Birman-Krein-Vishik characterization of the Friedrichs extension as the largest nonnegative self-adjoint extension of a nonnegative symmetric operator [AlonsoSimon]: its form domain $`\mathcal{D}(q_F) = \overline{\mathcal{C}}`$ is contained in $`\mathcal{D}(q_A)`$ for every nonnegative extension $`A`$, and a smaller form domain yields larger Rayleigh quotients, so $`\lambda_n(A) \le \lambda_n(\Delta_F)`$ by min-max. (ii) The cutoff estimate of Lemma 4.1 below shows $`\phi_0 \in \mathcal{D}(\Delta_F)`$ with $`\Delta_F\phi_0 = 0`$, so $`\inf\sigma(\Delta_F) \le 0`$; and $`q \ge 0`$ gives $`\inf\sigma(\Delta_F) \ge 0`$. (iii) Immediate. $`\square`$

Lemma 3.8 proves the part of Theorem 1.1 that needs no separation of variables: every realization has bottom at most $`0`$.

---

## 4. The Zonal Sector by Parity: Zero Mode versus Defect Bound State

The constant transverse mode ($`k = 0`$ even family, $`\Phi_0^{\mathrm{e}} \equiv 1`$) reduces the eigenvalue problem to a single ODE in $`y`$ with anti-periodic boundary conditions. This is the zonal sector, where the Friedrichs and bridging realizations differ. We analyze it by parity about the cone.

### 4.1 The reduced operator and parity reduction

On the constant-curvature band, the zonal eigenequation from §3.4 with $`\mu = 0`$ is

```math
-\Delta u = -u'' + \frac{1}{R}\tan\!\Bigl(\frac{y}{R}\Bigr)u' = \lambda\,u \qquad \text{on } (0, \pi R),
```

with anti-periodic boundary conditions $`u(\pi R) = -u(0)`$ and $`u'(\pi R) = -u'(0)`$, and a cone condition at $`y = \pi R/2`$ from §3.5. Decompose the constant-sector functions into modes symmetric and antisymmetric under reflection about the cone $`\delta \mapsto -\delta`$. Anti-periodicity interacts with this parity as follows.

*Symmetric modes* satisfy $`u(\pi R) = u(0)`$ automatically, so the anti-periodic value condition forces $`u(0) = 0`$ (Dirichlet at the seam), while the derivative condition $`u'(\pi R) = -u'(0)`$ is then free. The symmetric sector is the half-interval problem on $`(0, \pi R/2)`$ with Dirichlet at the seam and a cone condition.

*Antisymmetric modes* satisfy $`u(\pi R) = -u(0)`$ automatically, so the value condition is free and the derivative condition forces $`u'(0) = 0`$ (Neumann at the seam). The antisymmetric sector is the half-interval problem on $`(0, \pi R/2)`$ with Neumann at the seam and a cone condition.

On the bridging side, a symmetric mode has equal log coefficients on the two sides, so the Kirchhoff flux condition forces the log coefficient to vanish, and the symmetric mode lies in the Friedrichs domain. An antisymmetric mode has $`\tilde u_D^+ = -\tilde u_D^-`$, so the value-continuity condition forces $`\tilde u_D = 0`$, and the log datum is active. The two subsectors decouple: the symmetric subsector gives the same spectrum for the Friedrichs and bridging extensions and is treated in §4.2; the antisymmetric subsector is where these extensions differ and is treated in §§4.3–4.4. The resulting constant-sector parity dictionary:

| parity about $`p_c`$ | half-interval seam condition | active cone datum (bridging) |
|---|---|---|
| symmetric | Dirichlet, $`u(0) = 0`$ | none ($`u_N = 0`$ forced) |
| antisymmetric | Neumann, $`u'(0) = 0`$ | $`\tilde u_D = 0`$ (log datum active) |

### 4.2 Legendre reduction and the symmetric tower

The substitution $`x = \sin(y/R)`$ maps $`(0, \pi R/2)`$ bijectively to $`(0, 1)`$ and converts the zonal operator to the Legendre equation. With $`u(y) = v(\sin(y/R))`$,

<div align="center">

$`\displaystyle \frac{d}{dx}\Bigl[(1-x^2)\frac{dv}{dx}\Bigr] + \nu(\nu+1)v = 0, \qquad \lambda = \frac{\nu(\nu+1)}{R^2}`$

</div>

where $`\nu \ge 0`$ is a continuous spectral parameter. The Legendre function of the first kind $`P_\nu(x)`$ is regular at $`x = 1`$ (the cone); the Legendre function of the second kind $`Q_\nu(x)`$ diverges logarithmically and supplies the log datum $`u_N`$. The substitution $`x = \sin(y/R)`$ is two-to-one ($`y`$ and $`\pi R - y`$ map to the same $`x`$) and produces exactly the modes symmetric about the cone.

In the symmetric subsector both the Friedrichs and bridging conditions force the regular branch (the log coefficient vanishes, by §4.1), so the admissible symmetric solutions are $`P_\nu(\sin(y/R))`$. The Dirichlet seam condition $`u(0) = 0`$ is $`P_\nu(0) = 0`$. Since

<div align="center">

$`\displaystyle P_\nu(0) = \frac{\sqrt{\pi}}{\Gamma((1-\nu)/2)\Gamma(1+\nu/2)}`$

</div>

[DLMF, Eq. 14.5.1], this holds exactly when $`(1-\nu)/2`$ is a non-positive integer, i.e. $`\nu = 1, 3, 5, \ldots`$ The symmetric zonal tower is therefore

<div align="center">

$`\displaystyle \sigma_{\mathrm{sym}} = \Bigl\lbrace\frac{\ell(\ell+1)}{R^2} : \ell = 1, 3, 5, \ldots\Bigr\rbrace = \Bigl\lbrace\frac{2}{R^2}, \frac{12}{R^2}, \frac{30}{R^2}, \ldots\Bigr\rbrace`$

</div>

the same for the Friedrichs and bridging extensions. The lowest member is $`\ell = 1`$, with eigenfunction $`P_1(\sin(y/R)) = \sin(y/R)`$, the restriction of the zonal harmonic $`Y_1^0 \propto \sin(y/R)`$. It is strictly positive on $`(0, \pi R)`$, lies in the regular Frobenius branch at the cone, and gives

<div align="center">

$`\displaystyle \frac{\ell(\ell+1)}{R^2}\Big\rvert_{\ell=1} = \frac{2}{R^2} = R_{\mathrm{sm}}`$

</div>

independent of the half-width $`W`$.

On the flat strip (Euclidean metric, anti-periodic condition, same period $`\pi R`$), the lowest eigenvalue is $`1/R^2 = R_{\mathrm{sm}}/2`$, with the same eigenfunction $`\sin(y/R)`$. The curvature term $`(1/R)\tan(y/R)u'`$ doubles this to $`2/R^2 = R_{\mathrm{sm}}`$, matching the familiar $`\ell = 1`$ eigenvalue on $`S^2(R)`$.

### 4.3 The Friedrichs antisymmetric tower and the kernel

Under the Friedrichs extension, the antisymmetric subsector (Neumann seam, regular cone) admits $`\mathrm{sgn}(\delta)P_\nu(\sin(y/R))`$ with the regular branch at the cone, and the Neumann seam condition is $`P_\nu'(0) = 0`$, i.e. $`\nu = 0, 2, 4, \ldots`$ The Friedrichs antisymmetric tower is

<div align="center">

$`\displaystyle \sigma_{\mathrm{anti}}^{\mathrm{Fr}} = \Bigl\lbrace\frac{\ell(\ell+1)}{R^2} : \ell = 0, 2, 4, \ldots\Bigr\rbrace = \Bigl\lbrace0, \frac{6}{R^2}, \frac{20}{R^2}, \ldots\Bigr\rbrace`$

</div>

The $`\ell = 0`$ member is $`\mathrm{sgn}(\delta)\,P_0 = \mathrm{sgn}(\delta)`$, a scalar multiple of the zero mode $`\phi_0`$: odd about the cone, as the antisymmetric subsector requires.

> **Lemma 4.1** (Friedrichs kernel in the constant sector)**.** In the constant transverse sector, the Friedrichs form decomposes as the direct sum of the two half-band forms on $`M^+`$ and $`M^-`$. Consequently $`\phi_0`$ belongs to $`\mathcal{D}(\Delta_F)`$ and satisfies $`\Delta_F\phi_0 = 0`$, and the zero eigenspace in the constant sector is one-dimensional, spanned by $`\phi_0`$.

*Proof.* Let $`\chi_\varepsilon(\delta)`$ be smooth, equal to $`0`$ for $`\lvert\delta\rvert \le \varepsilon`$, equal to $`1`$ for $`\lvert\delta\rvert \ge \sqrt{\varepsilon}`$, and satisfying $`\lvert\chi_\varepsilon'(\delta)\rvert \le C/(\lvert\delta\rvert\lvert\log\varepsilon\rvert)`$ for $`\varepsilon < \lvert\delta\rvert < \sqrt{\varepsilon}`$. Since $`\lvert f(y)\rvert \sim \lvert\delta\rvert/R`$ at the cone, the cutoff energy (the transverse integration contributing only the constant factor $`2W`$) obeys

<div align="center">

$`\displaystyle \int_{\varepsilon < \lvert\delta\rvert < \sqrt{\varepsilon}} \lvert\chi_\varepsilon'(\delta)\rvert^2 \lvert f(y)\rvert d\delta \le \frac{C}{\lvert\log\varepsilon\rvert^2}\int_\varepsilon^{\sqrt\varepsilon}\frac{d\delta}{\delta} = O(\lvert\log\varepsilon\rvert^{-1}) \to 0.`$

</div>

Thus the jump of $`\phi_0`$ across the collapsed point is invisible to the Friedrichs form closure: $`\chi_\varepsilon\phi_0 \to \phi_0`$ in the form norm, so $`\phi_0 \in \mathcal{D}(q_F)`$ and $`q_F(\phi_0, \eta) = 0`$ for every form-domain test section $`\eta`$, whence $`\phi_0 \in \mathcal{D}(\Delta_F)`$ and $`\Delta_F\phi_0 = 0`$. By contrast the logarithmic branch has $`u'(\delta) \sim 1/\delta`$, hence $`\int \lvert u'\rvert^2\lvert f\rvert d\delta \sim \int d\delta/\lvert\delta\rvert = \infty`$, and is excluded from the Friedrichs domain. Conversely, if $`q_F[\psi] = 0`$ in the constant sector then $`\nabla\psi = 0`$ a.e. on each connected half, so $`\psi`$ is constant on each of $`M^\pm`$; the anti-periodic seam condition forces the two constants to be opposite, giving a scalar multiple of $`\phi_0`$. $`\square`$

> **Proposition 4.2** (Lune equivalence)**.** For the Friedrichs extension, multiplication by the trivializing section, $`U\psi = \phi_0\cdot\psi`$ with $`\phi_0`$ the unit-modulus zero mode ($`c = 1`$), is a unitary operator from $`L^2(M(W), \mathcal{L})`$ onto $`L^2`$ of the spherical lune of opening angle $`2W/R`$, and it restricts to a unitary from the Friedrichs form domain $`\mathcal{D}(q_F)`$ onto the Neumann form domain $`H^1`$ of the lune. Consequently the Friedrichs twisted Laplacian $`\Delta_F`$ is unitarily equivalent to the Neumann Laplacian of the lune, with $`\phi_0`$ carried to the constant function. The equivalence is specific to the Friedrichs extension: no bridging realization is unitarily equivalent to the lune Neumann Laplacian, under $`U`$ or under any other unitary map.

*Proof.* *Trivialization and $`L^2`$ unitarity.* Over the smooth locus $`M^\circ`$ the bundle $`\mathcal{L}`$ is trivial, and $`\phi_0`$ (with $`c = 1`$) is the trivializing section. Set $`\tilde\psi = \psi`$ on $`\lbrace y < \pi R/2\rbrace`$ and $`\tilde\psi = -\psi`$ on $`\lbrace y > \pi R/2\rbrace`$; in coordinates $`t = y`$ on the first half and $`t = y - \pi R`$ on the second (with $`w' = w`$ and $`w' = -w`$ respectively), the anti-equivariance condition becomes plain continuity of $`\tilde\psi`$ across $`t = 0`$, and the metric becomes $`dt^2 + \cos^2(t/R)\,dw'^2`$ on the lune of opening $`2W/R`$ ($`t \in (-\pi R/2, \pi R/2)`$, $`w' \in [-W, W]`$). The anti-periodic seam maps to interior continuity and the Neumann edges $`w = \pm W`$ to the two geodesic Neumann sides of the lune, both away from the poles. Since $`\lvert\phi_0\rvert = 1`$ a.e., $`\lVert U\psi\rVert_{L^2} = \lVert\psi\rVert_{L^2}`$, and $`U`$ is unitary onto $`L^2`$ of the lune.

*Energy isometry on the smooth locus.* On $`M^\circ`$, $`\nabla\phi_0 = 0`$ and $`\lvert\phi_0\rvert = 1`$, so $`\lvert\nabla(\phi_0\psi)\rvert = \lvert\nabla\psi\rvert`$ pointwise. Hence $`U`$ maps the core $`\mathcal{C}`$ onto the corresponding core on the lune (smooth functions, free at the Neumann sides, supported away from the poles), preserving both $`\lVert\cdot\rVert_{L^2}`$ and the energy $`q`$; it is a $`\lVert\cdot\rVert_q`$-isometry of these test spaces.

*Form-domain identification via zero capacity.* By definition $`\mathcal{D}(q_F) = \overline{\mathcal{C}}^{\,\lVert\cdot\rVert_q}`$. Each pole is a single point and has zero $`2`$-capacity: the same logarithmic cutoff $`\chi_\varepsilon`$ as Lemma 4.1, whose energy is $`O(\lvert\log\varepsilon\rvert^{-1}) \to 0`$, shows that the smooth functions on the lune supported away from the poles are $`H^1`$-dense in $`H^1`$ of the lune. Taking $`\lVert\cdot\rVert_q`$-closures, $`U`$ is unitary from $`\mathcal{D}(q_F)`$ onto $`H^1`$ of the lune. Thus $`U`$ intertwines the closed forms and the associated self-adjoint operators, and $`\phi_0`$ maps to the constant.

*Friedrichs-specificity.* The mode $`\phi_0`$ is discontinuous at the cone, so it satisfies the Friedrichs flux conditions but fails the bridging value-continuity $`\tilde u_D^+ = \tilde u_D^-`$; and every bridging form domain contains the logarithmic mode $`u' \sim 1/\delta`$, whose raw Dirichlet energy $`\int (u')^2\lvert f\rvert\,d\delta \sim \int d\delta/\lvert\delta\rvert`$ diverges, so its image is not in $`H^1`$ of the lune. Hence $`U`$ is not unitary onto the lune Neumann form domain for any bridging extension. More strongly, no unitary map at all can intertwine them: spectra are unitary invariants, the lune Neumann Laplacian is nonnegative, and every bridging realization at finite $`\delta_0`$ carries the negative eigenvalue $`\lambda_b(\delta_0)`$. $`\square`$

The trivialization and the zero-capacity estimate are sector-independent, so the equivalence is for the full Friedrichs operator, with the sector towers organized by longitude order. The Friedrichs spectrum is therefore the lune Neumann spectrum, obtained by separation of variables: longitude Neumann modes of order $`m_n = n\pi R/(2W)`$ combined with colatitude Legendre functions regular at both poles give eigenvalues $`(m_n + \ell')(m_n + \ell' + 1)/R^2`$ for $`n, \ell' \ge 0`$. In particular, for the Friedrichs realization the first positive eigenvalue of Theorem 1.2 is the first nonzero Neumann eigenvalue of this lune: the $`(n,\ell') = (0,1)`$ and $`(1,0)`$ modes give $`2/R^2`$ and $`\alpha_0(\alpha_0+1)/R^2`$, crossing doubly at $`W = \pi R/2`$. The width transition is thus the crossing of the two lowest lune branches. Explicit Legendre analyses of lune and spherical-triangle spectra are a classical and active subject: Seto, Wei, and Zhu [SWZ] compute Dirichlet eigenvalues and eigenfunctions of spherical lunes and triangles in the same Legendre framework. What Proposition 4.2 adds is the identification of the twisted-bundle problem with the Neumann lune problem, and its failure for every bridging extension.

### 4.4 The deformed antisymmetric branch

The bridging extension deforms the Friedrichs antisymmetric tower. By §4.1, the antisymmetric subsector under bridging is the half-interval problem on $`(0, \pi R/2)`$ with Neumann at the seam and the regularized condition $`\tilde u_D = 0`$ at the cone. Let $`u_\lambda`$ denote the solution of the zonal equation on $`(0,\pi R/2)`$ normalized by $`u_\lambda'(0) = 0`$, $`u_\lambda(0) = 1`$. Near the cone it has the expansion

```math
u_\lambda(\delta) = \mathcal{N}(\lambda)\,\ln\frac{\lvert\delta\rvert}{2R} + \mathcal{D}(\lambda) + o(1),
```

with $`\mathcal{N}(\lambda)`$ the log coefficient and $`\mathcal{D}(\lambda)`$ the regularized value, both real-analytic.

The reference length $`2R`$ is not a free normalization: it is fixed by the near-cone behavior of the Legendre function of the second kind. As $`x \to 1^-`$,

```math
Q_\nu(x) = -\tfrac{1}{2}\ln\frac{1-x}{2} - \gamma - \psi(\nu+1) + O\bigl((1-x)\ln(1-x)\bigr)
```

[DLMF, Eq. 14.8.3], the Ferrers function of the second kind on $`(-1, 1)`$, the same convention as the $`P_\nu'(0)`$, $`Q_\nu'(0)`$ values below. With $`x = \sin(y/R)`$ and $`\delta = y - \pi R/2`$ one has $`x = \cos(\delta/R)`$, so $`1 - x = \delta^2/(2R^2) + O(\delta^4)`$ and $`\tfrac{1}{2}\ln\frac{1-x}{2} = \ln\frac{\lvert\delta\rvert}{2R} + o(1)`$. Hence

```math
Q_\nu(\sin(y/R)) = -\ln\frac{\lvert\delta\rvert}{2R} - \gamma - \psi(\nu+1) + o(1),
```

the residual being $`O\bigl((\delta^2/R^2)\ln\lvert\delta\rvert\bigr)`$. This is where the length $`2R`$ enters the constant-sector expansion of §3.5. It is the square root of the $`1/(4R^2)`$ prefactor in $`(1-x)/2`$. The expansion is even in $`\delta`$, since $`x = \cos(\delta/R)`$ is. The same $`2R`$ therefore governs both sides $`\delta \to 0^\pm`$, matching the two-sided bookkeeping of §3.5. The regular branch $`P_\nu(x) \to 1`$ contributes only to $`\mathcal{D}(\lambda)`$, while $`Q_\nu`$ supplies the log datum $`\mathcal{N}(\lambda)`$ and the constant $`-\gamma - \psi(\nu+1)`$ in $`\mathcal{D}(\lambda)`$. The same $`2R`$ accordingly fixes the threshold $`\delta_0 = 2R/e`$ of Proposition 4.4 and the constant in $`\lambda_b = -4e^{-2\gamma}/\delta_0^2`$. A different reference length would shift these constants in lockstep, leaving the eigenvalues themselves invariant.

Define the secular function

```math
G(\lambda) = -\frac{\mathcal{D}(\lambda)}{\mathcal{N}(\lambda)}.
```

Since the data referenced to $`\delta_0`$ satisfy $`\tilde u_D = \mathcal{D}(\lambda) + \mathcal{N}(\lambda)\ln(\delta_0/2R)`$ (the $`\delta_0`$-rescaling above), the bridging eigenvalue condition $`\tilde u_D = 0`$ is

```math
G(\lambda) = \ln\frac{\delta_0}{2R}.
```

This is the classical secular mechanism for rank-one domain perturbations: $`G`$ is a Herglotz-type function whose poles lie at the unperturbed tower and whose level sets give the deformed eigenvalues, exactly as for the pseudo-Laplacians of Colin de Verdière [CdV] and the point interactions of [AGHH]. The closed forms below make every element of the mechanism explicit.

For $`\nu > -1/2`$ (equivalently $`\lambda > -1/(4R^2)`$), the substitution $`x = \sin(y/R)`$ and the Legendre closed forms give

```math
G\bigl(\nu(\nu+1)/R^2\bigr) = -\gamma - \psi(\nu+1) - \frac{Q_\nu'(0)}{P_\nu'(0)},
```

where $`\gamma`$ is the Euler-Mascheroni constant and $`\psi = \Gamma'/\Gamma`$ the digamma function (distinct from the section $`\psi`$). The derivative values at the origin,

```math
P_\nu'(0) = \frac{2\pi^{-1/2}\sin(\pi\nu/2)\,\Gamma(\tfrac{\nu}{2}+1)}{\Gamma(\tfrac{\nu}{2}+\tfrac{1}{2})}, \qquad Q_\nu'(0) = \frac{\pi^{1/2}\cos(\pi\nu/2)\,\Gamma(\tfrac{\nu}{2}+1)}{\Gamma(\tfrac{\nu}{2}+\tfrac{1}{2})}
```

[DLMF, Eqs. 14.5.2 and 14.5.4], share the same Gamma quotient, which cancels in the ratio, leaving

```math
G\bigl(\nu(\nu+1)/R^2\bigr) = -\gamma - \psi(\nu+1) - \frac{\pi}{2}\cot\frac{\pi\nu}{2}.
```

The cotangent has poles at the even integers $`\nu = 0, 2, 4, \ldots`$, which are exactly the Friedrichs antisymmetric tower; there $`G`$ has simple poles.

For $`\lambda < -1/(4R^2)`$, write $`\nu = -\tfrac{1}{2} + i\kappa`$ with $`\kappa = (-\lambda R^2 - \tfrac{1}{4})^{1/2}`$. The closed form continues real-analytically. With $`\cot(-\tfrac{\pi}{4} + \tfrac{i\pi\kappa}{2}) = -\mathrm{sech}(\pi\kappa) - i\tanh(\pi\kappa)`$ and $`\mathrm{Im}\,\psi(\tfrac{1}{2} + i\kappa) = \tfrac{\pi}{2}\tanh(\pi\kappa)`$, the imaginary parts cancel exactly, giving

```math
G(\lambda) = -\gamma - \mathrm{Re}\,\psi\bigl(\tfrac{1}{2} + i\kappa\bigr) + \frac{\pi}{2}\,\mathrm{sech}(\pi\kappa), \qquad \lambda \le -\frac{1}{4R^2}.
```

> **Lemma 4.3** (Monotonicity)**.** $`G`$ is strictly increasing between consecutive poles; on each interval between consecutive poles it is a bijection onto $`\mathbb{R}`$, and on $`(-\infty, 0)`$ it has no poles and increases from $`-\infty`$ to $`+\infty`$.

*Proof.* A Green identity on $`(0, \pi R/2)`$ for the Neumann-normalized solutions at distinct parameters gives, after the log terms cancel in the cone bracket and the seam bracket vanishes by the shared Neumann data,

```math
(\lambda' - \lambda)\int_0^{\pi R/2}\lvert f\rvert\,u_\lambda u_{\lambda'}\,dy = \frac{\mathcal{N}(\lambda')\mathcal{D}(\lambda) - \mathcal{N}(\lambda)\mathcal{D}(\lambda')}{R},
```

whence $`G'(\lambda) = R\,\lVert u_\lambda\rVert^2_{\lvert f\rvert}/\mathcal{N}(\lambda)^2 > 0`$ at points where $`\mathcal{N}(\lambda) \ne 0`$; at the even integers, where $`\mathcal{N} = 0`$, $`G`$ has simple poles, and monotonicity is asserted on each open interval between consecutive poles. At each even-integer pole $`\nu = 2n`$ the finite part $`-\gamma - \psi(\nu+1)`$ stays bounded while $`-\tfrac{\pi}{2}\cot(\pi\nu/2) \sim -1/(\nu - 2n)`$, so $`G \to +\infty`$ as the pole is approached from below ($`\nu \to 2n^-`$, with $`\lambda`$ increasing toward it) and $`G \to -\infty`$ from above ($`\nu \to 2n^+`$); with $`G' > 0`$ in between, $`G`$ increases from $`-\infty`$ to $`+\infty`$ across each interval between consecutive poles and is a bijection onto $`\mathbb{R}`$ there. The poles of $`G`$ are the even integers, which are nonnegative; so $`G`$ has no pole on $`(-\infty, 0)`$. The deep-negative asymptotic from $`\psi(z) = \ln z - 1/(2z) + O(z^{-2})`$ gives $`G(\lambda) = -\gamma - \tfrac{1}{2}\ln(-\lambda R^2) + O((-\lambda R^2)^{-1}) \to -\infty`$ as $`\lambda \to -\infty`$, while $`G \to +\infty`$ as $`\lambda \to 0^-`$ (the pole at $`\nu = 0`$). Strict monotonicity makes $`G`$ a bijection on $`(-\infty, 0)`$. $`\square`$

> **Proposition 4.4** (Bridging constant-sector spectrum)**.** For every $`\delta_0 > 0`$, the constant sector of $`A^{\mathrm{br}}_{\delta_0}`$ has exactly one negative eigenvalue
>
> ```math
> \lambda_b(\delta_0) = -\frac{4e^{-2\gamma}}{\delta_0^2}\bigl(1 + O(\delta_0^2/R^2)\bigr) \qquad (\delta_0 \to 0^+),
> ```
>
> a cone-localized bound state independent of the half-width $`W`$ and strictly increasing in $`\delta_0`$ with $`\lambda_b \to 0^-`$ as $`\delta_0 \to \infty`$. Zero is not an eigenvalue: it lies in the resolvent set. The symmetric tower is unchanged, and the deformed antisymmetric eigenvalues interlace the Friedrichs tower, one in each gap. Moreover, for
>
> ```math
> \delta_0 > \frac{2R}{e}
> ```
>
> the lowest positive eigenvalue of the constant sector is $`2/R^2`$ and simple; at $`\delta_0 = 2R/e`$ it is still $`2/R^2`$ but doubly degenerate within the constant sector, the deformed antisymmetric root coinciding with the symmetric $`\ell = 1`$ value (combined with the odd $`j = 0`$ sector this produces the threshold triple degeneracy of Corollary 6.3 when also $`W = \pi R/2`$), and for $`\delta_0 < 2R/e`$ it lies strictly below $`2/R^2`$.

*Proof.* By Lemma 4.3, $`G`$ is a bijection of $`(-\infty, 0)`$ onto $`\mathbb{R}`$, so the secular condition has exactly one negative root for every $`\delta_0`$. Solving the deep asymptotic against $`\ln(\delta_0/2R)`$ gives the bound state $`\lambda_b(\delta_0)`$, and $`G' > 0`$ gives monotonicity in $`\delta_0`$ with $`\lambda_b \to 0^-`$ as $`\delta_0 \to \infty`$. At $`\lambda = 0`$ the Neumann-seam solution is $`u_0 \equiv 1`$, with $`\mathcal{N}(0) = 0`$ and $`\mathcal{D}(0) = 1 \ne 0`$, so $`\tilde u_D = 1 \ne 0`$ and the bridging condition excludes $`\lambda = 0`$. On each interval between consecutive poles (the Friedrichs tower) $`G`$ is a bijection onto $`\mathbb{R}`$, giving one deformed root per gap. Finally, at $`\nu = 1`$ ($`\lambda = 2/R^2`$), $`\cot(\pi/2) = 0`$, so $`G(2/R^2) = -\gamma - \psi(2) = -\gamma - (1 - \gamma) = -1`$; since $`G`$ is increasing on $`(0, 6/R^2)`$, the lowest positive deformed root exceeds $`2/R^2`$ for $`\ln(\delta_0/2R) > -1`$ and equals $`2/R^2`$ at $`\ln(\delta_0/2R) = -1`$, so for $`\delta_0 > 2R/e`$ the lowest positive eigenvalue of the sector is $`2/R^2`$ and simple, while at $`\delta_0 = 2R/e`$ it remains $`2/R^2`$ with the deformed root coincident. $`\square`$

Every deformed antisymmetric eigenfunction has $`\mathcal{N} \ne 0`$, hence diverges like $`\mathcal{N}\ln(\lvert\delta\rvert/\delta_0)`$ at the cone; in particular the bound state at $`\lambda_b`$ is nodeless on each open half (it is the lowest eigenfunction of the half-interval problem, hence positive there by oscillation theory [Weidmann]), with opposite signs on the two halves and a logarithmic divergence at $`p_c`$. It vanishes nowhere on the smooth locus. The constant $`-4e^{-2\gamma}`$ in $`\lambda_b`$ is the standard two-dimensional one-center point-interaction binding energy [AGHH], with $`\delta_0`$ in the role of the point-interaction renormalization length. Matching the logarithmic scale identifies $`\delta_0`$ with the coupling parameter of the one-center family of [AGHH, KayStuder]; in the present finite curved cone it realizes the same renormalized constant-channel interaction, with the global Legendre geometry supplying the exact secular correction. Figure 2 displays the two constant-sector branches as functions of the renormalization length, computed from the exact secular condition.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/delta0-branches.png?raw=true" width="80%" alt="The defect-bound state and the lowest deformed root of the bridging realization as functions of the renormalization length, with the 2R/e threshold marked">

**Figure 2.** The two constant-sector branches of the sector-regular bridging realization as functions of the renormalization length, computed from the exact secular condition $`G(\lambda) = \ln(\delta_0/2R)`$ of §4.4: the defect-bound state $`\lambda_b(\delta_0)`$, with its point-interaction asymptotic $`-4e^{-2\gamma}/\delta_0^2`$ (dashed; the asymptotic is a small-$`\delta_0`$ statement, and the visible deviation at moderate $`\delta_0`$ is the $`O(\delta_0^2/R^2)`$ correction of Theorem 1.1), and the lowest deformed antisymmetric root. For $`\delta_0 > 2R/e`$ the deformed root lies above the width-independent zonal level $`2/R^2`$ (dotted), so the lowest positive constant-sector level is $`2/R^2`$, the input to Theorem 1.2; at $`\delta_0 = 2R/e`$ the two coincide (marked).

---

## 5. Ground-State Dependence on the Cone Interaction

We now assemble the zonal analysis into the ground-state classification.

> **Theorem 5.1** (Bottom of the spectrum across realizations)**.** Let $`A`$ be any self-adjoint extension of the minimal twisted Laplacian on $`M(W)`$, $`0 < W < \pi R`$. Then:
>
> **(i)** $`\inf\sigma(A) \le 0`$, with no self-adjoint extension having strictly positive spectral bottom.
>
> **(ii)** $`\inf\sigma(A) = 0`$ if and only if $`A`$ is nonnegative; the Friedrichs extension is the maximal such realization, with $`\inf\sigma(\Delta_F) = 0`$ attained by the discontinuous zero mode $`\phi_0`$.
>
> **(iii)** For the sector-regular bridging realization $`A^{\mathrm{br}}_{\delta_0}`$, $`\inf\sigma = \lambda_b(\delta_0) < 0`$, a single cone-localized defect bound state; zero lies in the resolvent set.
>
> For the Friedrichs and bridging extensions the symmetric zonal tower is unchanged, and their difference lives entirely in the antisymmetric subsector; a general parity-mixing Lagrangian cone condition can instead deform the symmetric subsector. Parts (ii)–(iii) give the explicit bottom for the nonnegative and bridging realizations, while part (i) holds for every self-adjoint extension, the parity-mixing and singular-odd-branch realizations included.

*Proof.* Part (i) is Lemma 3.8(iii), which bounds $`\inf\sigma(A) \le \inf\sigma(\Delta_F) = 0`$ for nonnegative $`A`$ and is immediate for non-nonnegative $`A`$. The mechanism is also visible directly: since the minimal operator is nonnegative and has finite deficiency indices, every self-adjoint extension here is semibounded [AlonsoSimon]; after shifting such an extension to be nonnegative, the Birman-Krein-Vishik order gives $`\mathcal{D}(q_F) \subseteq \mathcal{D}(q_A)`$ with the form agreeing with $`q_F`$ there, and since $`\phi_0 \in \mathcal{D}(q_F)`$ has zero energy, $`\inf\sigma(A) \le 0`$ with no maximality argument needed. Part (ii): if $`A`$ is nonnegative then $`\inf\sigma(A) \ge 0`$; combined with (i) this forces $`\inf\sigma(A) = 0`$, and Lemma 3.8(i) identifies Friedrichs as the maximal nonnegative realization, with the bottom attained by $`\phi_0`$ (Lemma 4.1). Part (iii) is Proposition 4.4 for the constant sector; under the sector-regular convention every nonconstant sector is nonnegative (its bottom is $`\alpha(\alpha+1)/R^2 > 0`$ for $`\alpha > 0`$, §6), so the full-operator bottom is the constant-sector bottom $`\lambda_b(\delta_0) < 0`$, with zero in the resolvent set. The robustness of the symmetric tower for the Friedrichs and bridging extensions is §4.2; a general cone condition is not claimed robust. $`\square`$

So the cone allows the spectrum to evade the positive-bottom mechanism expected from smooth sign holonomy alone, and the form of the evasion is set by the extension: the Friedrichs ground state $`\phi_0`$ is bounded but discontinuous at $`p_c`$, while the bridging ground state at $`\lambda_b`$ is continuous in regularized value but logarithmically divergent there. Each evades the obstruction only through its singular behavior at the cone, where elliptic regularity fails. No realization raises the bottom above zero.

---

## 6. Nonconstant Sectors and the First Positive Level

The first positive eigenvalue is governed by the competition between the symmetric zonal mode at $`2/R^2`$, common to the Friedrichs and bridging realizations, and the nonconstant sectors, where these realizations agree. We record the bottom of each nonconstant sector and then prove Theorem 1.2.

### 6.1 The odd (periodic) sectors

The odd transverse modes ($`\Phi_j^{\mathrm{o}}`$, $`j = 0, 1, 2, \ldots`$) produce periodic longitudinal functions. The reduced Sturm-Liouville equation with $`\mu_j = \bigl((2j+1)\pi/(2W)\bigr)^2`$ has, in Schrödinger form, an effective potential proportional to $`\sec^2(y/R)`$, a symmetric Pöschl-Teller potential.

> **Proposition 6.1.** The function $`u = \lvert\cos(y/R)\rvert^{\alpha}`$ with $`\alpha = (2j+1)\pi R/(2W)`$ satisfies the reduced Sturm-Liouville equation with eigenvalue $`\lambda = \alpha(\alpha+1)/R^2`$.

*Proof.* Set $`r = \lvert\cos(y/R)\rvert`$, so $`\lvert f\rvert = r`$ and $`u = r^\alpha`$. On the smooth locus, $`R^2(r')^2 = 1 - r^2`$ and $`r'' = -r/R^2`$. Then $`\lvert f\rvert\,u' = \alpha\,r^\alpha r'`$ and

```math
(\lvert f\rvert\,u')' = \frac{\alpha}{R^2}\,r^{\alpha-1}\bigl[\alpha(1 - r^2) - r^2\bigr] = \frac{\alpha}{R^2}\,r^{\alpha-1}\bigl[\alpha - (\alpha+1)r^2\bigr],
```

so $`-(\lvert f\rvert\,u')' + (\mu_j/\lvert f\rvert)\,u = r^{\alpha-1}[\alpha(\alpha+1)R^{-2}r^2 - \alpha^2 R^{-2} + \mu_j]`$. With $`\mu_j = \alpha^2/R^2`$ the constant terms cancel, leaving $`\alpha(\alpha+1)R^{-2}\,\lvert f\rvert\,u`$. $`\square`$

Under the substitution $`x = \sin(y/R)`$, $`\lvert\cos(y/R)\rvert^\alpha = (1-x^2)^{\alpha/2}`$ is the branch regular at $`x = 1`$ of the associated Legendre equation of degree and order $`\alpha`$; for integer $`\alpha`$ it is proportional to the sectoral harmonic $`P_\alpha^\alpha`$, and at $`\alpha = 1`$ it reduces to $`Y_1^1`$ on the covering $`S^2`$. At both seams $`\lvert\cos\rvert^\alpha = 1`$ with vanishing derivative, so periodicity holds for all $`\alpha`$, and the spectral parameter runs continuously with $`W`$. Near the cone $`\lvert\cos(y/R)\rvert^\alpha \sim \lvert\delta/R\rvert^\alpha \to 0`$; this is the regular Frobenius branch, with finite Dirichlet energy for all $`\alpha > 0`$; for $`\alpha \ge 1`$ the cone is limit-point and it is the unique self-adjoint mode, while in the wide-band first odd sector ($`\alpha_0 < 1`$) it is the branch selected by the Friedrichs extension and by the bridging realization. A ground-state transform makes minimality explicit: writing $`u = hv`$ with $`h = \lvert\cos(y/R)\rvert^\alpha`$, integration by parts gives

```math
\int \Bigl(\lvert f\rvert\,\lvert u'\rvert^2 + \frac{\mu_j}{\lvert f\rvert}\,\lvert u\rvert^2\Bigr)dy - \frac{\alpha(\alpha+1)}{R^2}\int \lvert f\rvert\,\lvert u\rvert^2\,dy \;=\; \int \lvert f\rvert\,h^2\,\lvert v'\rvert^2\,dy \;\ge\; 0,
```

so $`\lambda = \alpha(\alpha+1)/R^2`$ is the sector ground eigenvalue, unique up to scaling. The apex boundary terms of this transform vanish for every $`\alpha > 0`$: the weighted flux factors are $`\lvert f\rvert\,h^2 = O(\lvert\delta\rvert^{2\alpha+1})`$ and $`\lvert f\rvert\,h\,h' = O(\lvert\delta\rvert^{2\alpha})`$, both $`\to 0`$ as $`\delta \to 0`$, so even the singular-derivative regular branch of the wide-band first odd sector ($`0 < \alpha_0 < 1`$) contributes no cone term. Since $`\alpha_j = (2j+1)\pi R/(2W)`$ is increasing in $`j`$, the odd-sector minimum is at $`j = 0`$:

```math
\lambda_0^{\mathrm{odd}}(W) = \frac{\alpha_0(\alpha_0+1)}{R^2}, \qquad \alpha_0 = \frac{\pi R}{2W}, \qquad \psi_0^{\mathrm{odd}} = \lvert\cos(y/R)\rvert^{\alpha_0}\sin(\pi w/2W).
```

This is decreasing in $`W`$: above $`2/R^2`$ for $`W < \pi R/2`$, equal at $`W = \pi R/2`$, and below for $`W > \pi R/2`$.

### 6.2 The even nonconstant sectors

> **Proposition 6.2.** For each even nonconstant sector, $`k \ge 1`$, the sector ground eigenvalue is $`\alpha_k(\alpha_k+1)/R^2`$ with $`\alpha_k = k\pi R/W`$, attained by the sign-flipped solution $`\mathrm{sgn}(\delta)\,\lvert\cos(y/R)\rvert^{\alpha_k}`$. Since $`\alpha_k > 1`$ for all $`k \ge 1`$ and $`W < \pi R`$, every even nonconstant sector lies strictly above $`2/R^2`$.

*Proof.* The even nonconstant modes ($`\Phi_k^{\mathrm{e}}`$, $`k \ge 1`$) produce anti-periodic longitudinal functions. The sector ground state is obtained by a sign flip across the cone,

```math
u_k(y) = \mathrm{sgn}(\delta)\,\lvert\cos(y/R)\rvert^{\alpha_k}, \qquad \alpha_k = \frac{k\pi R}{W},
```

which is anti-periodic at the seams and continuous at the cone (the sign flip multiplies a vanishing factor), with vanishing weighted flux and no distributional contribution; it lies in every self-adjoint extension's domain, the cone being limit-point in these sectors. On each half, $`\lvert\cos(y/R)\rvert^{\alpha_k}`$ is positive and nodeless, so by the Sturm oscillation theorem for the separated half-interval problem (Neumann at the seam, regular Frobenius at the cone) it is the half-interval ground state, with eigenvalue $`\alpha_k(\alpha_k+1)/R^2`$. Since $`\alpha_k = k\pi R/W \ge \pi R/W > 1`$ for all $`k \ge 1`$ and $`W < \pi R`$, every even nonconstant sector lies strictly above $`2/R^2`$. The sharp $`+1`$ in $`\alpha_k(\alpha_k+1)`$ matters: a potential-only bound gives $`\alpha_k^2/R^2`$, which fails to clear $`2/R^2`$ for $`\alpha_k \in (1, \sqrt{2})`$, whereas $`\alpha_k(\alpha_k+1)/R^2 > 2/R^2`$ for all $`\alpha_k > 1`$. $`\square`$

**Sector-bottom divergence.** The sector bottoms tend to $`+\infty`$, which is what gives each realization of Definition 3.5 compact resolvent and discrete spectrum (Proposition 3.7). In the sector with transverse Neumann eigenvalue $`\mu`$ the indicial exponent is $`\alpha = \sqrt{\mu}\,R`$, and the ground-state transforms of §6.1 and §6.2 identify the nonconstant sector bottom as $`\alpha(\alpha+1)/R^2`$. In the bridging realization the constant sector is bounded below by $`\lambda_b(\delta_0)`$ (Proposition 4.4), while in the Friedrichs realization it is bounded below by $`0`$; in either case the constant sector is a single summand and does not affect the divergence of the nonconstant sector bottoms. The transverse Neumann eigenvalues $`\mu_k^{\mathrm{e}} = (k\pi/W)^2`$ and $`\mu_j^{\mathrm{o}} = ((2j+1)\pi/(2W))^2`$ increase without bound in the sector index, so $`\alpha \to \infty`$ and the bottoms $`\alpha(\alpha+1)/R^2 \to +\infty`$.

### 6.3 The mode crossing

*Proof of Theorem 1.2.* By Proposition 3.7 the spectrum of each realization is discrete and reduces over the transverse sectors, so the first positive eigenvalue is the minimum of the first positive sector entries. By §4.2 the constant sector contributes $`2/R^2`$ as its first positive value, shared by the Friedrichs extension and, by Proposition 4.4, by every bridging extension with $`\delta_0 > 2R/e`$. The odd sectors contribute $`\alpha_0(\alpha_0+1)/R^2`$ with $`\alpha_0 = \pi R/(2W)`$ (§6.1), and by §6.2 the even nonconstant sectors lie strictly above $`2/R^2`$. The function $`\alpha \mapsto \alpha(\alpha+1)`$ is increasing, and $`\alpha_0`$ is decreasing in $`W`$, so the first positive eigenvalue is $`\min(2/R^2,\,\alpha_0(\alpha_0+1)/R^2)`$: it equals $`2/R^2`$ when $`\alpha_0 \ge 1`$, i.e. $`W \le \pi R/2`$, and $`\alpha_0(\alpha_0+1)/R^2`$ when $`W > \pi R/2`$. At $`W = \pi R/2`$ both branches give $`2/R^2`$. $`\square`$

For $`W > \pi R/2`$ the hypothesis $`\delta_0 > 2R/e`$ is sufficient but not sharp: the first positive level is then $`\alpha_0(\alpha_0+1)/R^2 < 2/R^2`$, and since $`G`$ is strictly increasing the deformed constant-sector root clears it exactly when $`\ln(\delta_0/2R) > G\bigl(\alpha_0(\alpha_0+1)/R^2\bigr)`$, a threshold strictly below $`-1`$. The uniform condition is thus sharp precisely at and below the critical width.

The transition is a crossing between two competing low modes (Figure 3). The zonal branch at $`2/R^2`$ is the curvature-set mode of the constant sector, independent of the width; the twisted branch at $`\alpha_0(\alpha_0+1)/R^2`$ is the lowest transverse mode, whose cost is set by the width through $`\alpha_0 = \pi R/(2W)`$. For narrow bands the transverse mode is expensive and the first positive level is zonal; as the band widens the twisted mode cheapens and drops below the zonal branch exactly at cone angle $`\pi`$, that is at $`W = \pi R/2`$, where the two branches cross and the first positive level is doubly degenerate.

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/mode-crossing.png?raw=true" width="70%" alt="The width-driven mode crossing: the width-independent zonal branch crossed by the falling twisted branch at cone angle pi">

**Figure 3.** The width-driven mode crossing of Theorem 1.2. The zonal mode $`2/R^2`$ (solid) is width-independent; the lowest twisted mode $`\alpha_0(\alpha_0+1)/R^2`$, $`\alpha_0 = \pi R/(2W)`$ (dashed), falls as the band widens and crosses the zonal branch at cone angle $`\pi`$, i.e. $`W = \pi R/2`$, where the two modes are degenerate. The first positive level is the lower envelope of the two branches.

> **Corollary 6.3** (Degeneracy at the transition)**.** Let $`W = \pi R/2`$; away from this critical width the first positive eigenvalue is simple.
>
> **(i)** *(Critical width)* For the Friedrichs extension and for sector-regular bridging with $`\delta_0 > 2R/e`$, the first-positive eigenspace is two-dimensional, spanned by $`\psi_1 = \sin(y/R)`$ and $`\psi_2 = \lvert\cos(y/R)\rvert\,\sin(w/R)`$. On the covering $`S^2`$, $`\psi_1`$ restricts from $`Y_1^0`$ while $`\psi_2`$ does not lift to a smooth function (the absolute value is required by equivariance, not a coordinate artifact).
>
> **(ii)** *(The next levels)* Nothing further reaches $`2/R^2`$: the next entries sit at $`6/R^2`$, from the $`k = 1`$ even bottom, the $`\ell = 2`$ entry of the Friedrichs antisymmetric tower, and the second entry of the $`j = 0`$ odd sector, and at $`12/R^2`$, from the $`\ell = 3`$ symmetric tower and the $`j = 1`$ odd bottom. For bridging with $`\delta_0 > 2R/e`$ the next eigenvalue above the two-dimensional eigenspace is instead the deformed antisymmetric root. It lies in $`(2/R^2, 6/R^2)`$ for every finite such $`\delta_0`$ and increases to $`6/R^2`$ as $`\delta_0 \to \infty`$. In that limit the deformed tower climbs back onto the Friedrichs tower, as the renormalized condition degenerates to the Friedrichs condition.
>
> **(iii)** *(Double threshold)* At $`\delta_0 = 2R/e`$ the deformed root coincides with the symmetric $`\ell = 1`$ value (Proposition 4.4), and the bridging first-positive eigenspace becomes three-dimensional, the additional mode represented by $`\mathrm{sgn}(\delta)\,Q_1(\sin(y/R))`$: the Neumann-seam solution at $`\nu = 1`$, pure $`Q_1`$ since $`Q_1'(0) = 0`$, logarithmically divergent at the cone, antisymmetric in cone parity and distinct from the transverse-odd $`\psi_2`$. The three modes are mutually orthogonal, and the next entries remain strictly above.

> **Corollary 6.4** (Sign-changing first positive eigenfunction)**.** For $`W > \pi R/2`$ the representative $`\lvert\cos(y/R)\rvert^{\alpha_0}\sin(\pi w/2W)`$ of the first positive eigenfunction changes sign across $`w = 0`$ (the core loop). The sign change is a fixed parity feature of the odd transverse factor $`\sin(\pi w/2W)`$, not a movable node. The holonomy enters through the Möbius pairing of §3.4, which couples this parity class to periodic longitudinal behavior, and decisively through the absence of a globally positive representative recorded below. For $`W < \pi R/2`$ the representative $`\sin(y/R)`$ is positive on the interior but vanishes at the seam, where the Möbius identification imposes the sign reversal. Because $`\mathcal{L}`$ is nontrivial, no section admits a globally positive representative, so the Perron-Frobenius nodeless-ground argument does not apply.

---

## 7. Physical Interpretation and Limiting Regimes

**Ground state versus first positive level.** This model separates two spectral effects. The first positive level is the rigid one: in the narrow regime it equals $`2/R^2`$ for the Friedrichs extension and for bridging with $`\delta_0 > 2R/e`$, with the width-driven mode crossing at $`W = \pi R/2`$. The bottom of the spectrum, by contrast, is extension-dependent: every nonnegative extension has bottom $`0`$, while the bridging family has bottom $`\lambda_b(\delta_0) < 0`$, so the gap above the ground state moves with $`\delta_0`$ even where the first positive level does not. Anti-periodicity does not force a positive spectral bottom (Lemma 3.8). The model thus separates three mechanisms often entangled in singular quantum systems: the topology imposes the $`\mathbb{Z}_2`$ sign holonomy, the conic defect carries the self-adjoint-extension parameter, and constant curvature makes the mode competition exactly solvable.

**Sign holonomy and nodal structure.** The anti-periodicity $`\psi(\pi R, -w) = -\psi(0, w)`$ is a real Aharonov-Bohm-type sign holonomy: a wavefunction returns to minus itself around the core loop, and the anti-periodic half-integer longitudinal quantization of the even transverse sectors, the constant sector included, is its spectral signature. The nodal pattern changes at the crossing. For $`W > \pi R/2`$ the first positive eigenfunction changes sign across the core loop; for $`W < \pi R/2`$ it is positive in the interior and vanishes at the seam, where the twist imposes the sign reversal. On an orientable surface Perron-Frobenius and Courant's nodal domain theorem [CourantHilbert] would give a positive ground eigenfunction, but on $`M(W)`$ a nowhere-vanishing section would trivialize $`\mathcal{L}`$. This is the line-bundle analogue of Shigekawa's magnetic spectral-positivity criterion [Shigekawa]; the cone goes further, letting the bottom itself fall to zero or below.

**The defect scale.** The renormalization length $`\delta_0`$ is the one quantity in the model that the intrinsic geometry leaves free: it is short-distance defect data, not geometry. The Friedrichs extension needs no such scale and is the standard conic choice [Cheeger1979, Cheeger1983]; its spectrum is the Neumann lune spectrum of Proposition 4.2, so it does not encode any additional vertex-matching data from the Möbius identification, and the bottom is the zero mode. At $`\alpha_{\mathrm{BP}} = -1`$ it is moreover the unique Markovian realization (Theorem 1.13(ii) of [BP]), the bridging extensions being non-Markovian. Together with the generic decoupling of two-dimensional point interactions, this makes Friedrichs the canonical nonnegative choice. A transmitting limit of smoothed cones would be expected only under tuning to a zero-energy resonance. Whether a geometric regularization selects a canonical $`\delta_0`$, for instance as a norm-resolvent limit of smoothed-cone Laplacians [AGHH], remains open. Until then $`\lambda_b`$ is an extension-dependent quantity rather than an intrinsic invariant, and its leading form carries $`O(\delta_0^2/R^2)`$ corrections that are not small at moderate $`\delta_0`$.

**The smooth comparison.** The singular construction is a modeling choice, and it is worth stating what the conic endpoint buys. The round projective plane $`\mathbb{RP}^2(R)`$ contains a smooth constant-curvature Möbius band: the tubular neighborhood of half-width $`W`$ of a closed geodesic. It has the same core length $`\pi R`$ and the same Fermi normal form $`dt^2 + \cos^2(t/R)\,d\sigma^2`$, $`t`$ the transverse distance, and it is smooth for every $`W < \pi R/2`$. That band has a boundary of constant geodesic-curvature magnitude $`\tan(W/R)/R`$ and regular Sturm-Liouville endpoints, so its eigenvalues solve transcendental Legendre matching conditions with no closed form. The conic band trades the smooth boundary for geodesic arcs and a single point defect, and the whole spectrum closes in one secular function. The smooth family moreover exists only for $`W < \pi R/2`$, exhausting $`\mathbb{RP}^2`$ minus a point as $`W \to \pi R/2`$. The mode crossing of Theorem 1.2 therefore sits exactly at the closing width of the smooth family, and the conic model is what continues the geometry past it. Proposition 4.2 sharpens the comparison: the Friedrichs realization is spectrally an orientable object, a Neumann lune, so the bridging family is where the non-orientable defect physics genuinely lives.

**Limiting regimes.** The thin-strip limit is already visible in the closed forms, and it clarifies why this model does not converge to the effective dynamics of [KKZ]. As $`W \to 0`$ every nonconstant sector bottom $`\alpha(\alpha+1)/R^2`$ diverges, the smallest indicial exponent being $`\alpha_0 = \pi R/(2W)`$. On any fixed spectral window the spectrum therefore reduces to the $`W`$-independent constant sector, the zonal problem of §4: for the Friedrichs extension the combined towers $`\ell(\ell+1)/R^2`$, $`\ell \ge 0`$, and for bridging the symmetric tower together with the deformed antisymmetric roots and the bound state $`\lambda_b(\delta_0)`$. The limit is thus the zonal Legendre problem rather than a Mathieu-type effective operator as in [KKZ]: their effective potential is generated by the geodesic curvature of a non-geodesic core curve, while our core loop is a geodesic and the degeneration is concentrated in the cone at every width. What the two models share is the parity bookkeeping of the Möbius holonomy, visible in [KKZ] as their $`m + n`$ odd selection rule. The two thin limits lie on opposite branches of it, carried by different structures: [KKZ] carry the twist geometrically, through the $`t \mapsto -t`$ boundary identification acting on scalar functions, so their surviving Dirichlet mode is longitudinally periodic, while we carry it as the sign holonomy of the orientation bundle, so our Neumann constant mode is anti-periodic (§3.4). Natural continuations within the same self-adjoint framework include Robin conditions at the regular boundary arcs and the wider family of Lagrangian cone-trace conditions of §3.5.

---

## References

- **[AGHH]** S. Albeverio, F. Gesztesy, R. Høegh-Krohn, and H. Holden, *Solvable Models in Quantum Mechanics*. 2nd ed., AMS Chelsea Publishing, Providence, RI, 2005.
- **[AlonsoSimon]** A. Alonso and B. Simon, The Birman-Krein-Vishik theory of self-adjoint extensions of semibounded operators. *J. Operator Theory* **4** (1980), no. 2, 251–270.
- **[BBC]** W. Ballmann, J. Brüning, and G. Carron, Eigenvalues and holonomy. *Int. Math. Res. Not.* **2003** (2003), no. 12, 657–665.
- **[BK]** G. Berkolaiko and P. Kuchment, *Introduction to Quantum Graphs*. Math. Surveys Monogr. 186, Amer. Math. Soc., Providence, RI, 2013.
- **[BP]** U. Boscain and D. Prandi, Self-adjoint extensions and stochastic completeness of the Laplace-Beltrami operator on conic and anticonic surfaces. *J. Differential Equations* **260** (2016), no. 4, 3234–3269.
- **[BS]** J. Brüning and R. Seeley, Regular singular asymptotics. *Adv. Math.* **58** (1985), no. 2, 133–148.
- **[Cheeger1979]** J. Cheeger, On the spectral geometry of spaces with cone-like singularities. *Proc. Nat. Acad. Sci. U.S.A.* **76** (1979), no. 5, 2103–2106.
- **[Cheeger1983]** J. Cheeger, Spectral geometry of singular Riemannian spaces. *J. Differential Geom.* **18** (1983), no. 4, 575–657.
- **[CdV]** Y. Colin de Verdière, Pseudo-laplaciens. I. *Ann. Inst. Fourier (Grenoble)* **32** (1982), no. 3, 275–286.
- **[CourantHilbert]** R. Courant and D. Hilbert, *Methods of Mathematical Physics. Vol. I*. Interscience, New York, 1953.
- **[Friedrichs]** K. Friedrichs, Spektraltheorie halbbeschränkter Operatoren und Anwendung auf die Spektralzerlegung von Differentialoperatoren. *Math. Ann.* **109** (1934), no. 1, 465–487.
- **[KSWW]** H. Kalf, U.-W. Schmincke, J. Walter, and R. Wüst, On the spectral theory of Schrödinger and Dirac operators with strongly singular potentials. In *Spectral theory and differential equations*, pp. 182–226, Lecture Notes in Math. 448, Springer, Berlin, 1975.
- **[KKZ]** T. Kalvoda, D. Krejčiřík, and K. Zahradová, Effective quantum dynamics on the Möbius strip. *J. Phys. A* **53** (2020), no. 37, 375201.
- **[KayStuder]** B. S. Kay and U. M. Studer, Boundary conditions for quantum mechanics on cones and fields around cosmic strings. *Comm. Math. Phys.* **139** (1991), no. 1, 103–139.
- **[LiRM]** Z. Li and L. R. Ram-Mohan, Quantum mechanics on a Möbius ring: energy levels, symmetry, optical transitions, and level splitting in a magnetic field. *Phys. Rev. B* **85** (2012), 195438.
- **[DLMF]** F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain (eds.), *NIST Digital Library of Mathematical Functions*. Release 1.2.7 of 2026-06-15, https://dlmf.nist.gov.
- **[PSA]** J. J. L. R. Pinto, J. E. G. Silva, and C. A. S. Almeida, Electronic states in quantum wires on a Möbius strip. *Phys. Scr.* **99** (2024), 0659c2.
- **[RS]** M. Reed and B. Simon, *Methods of Modern Mathematical Physics. II: Fourier Analysis, Self-Adjointness*. Academic Press, New York, 1975.
- **[SWZ]** S. Seto, G. Wei, and X. Zhu, Fundamental gaps of spherical triangles. *Ann. Global Anal. Geom.* **61** (2022), no. 1, 1–19.
- **[Shigekawa]** I. Shigekawa, Eigenvalue problems for the Schrödinger operator with the magnetic field on a compact Riemannian manifold. *J. Funct. Anal.* **75** (1987), no. 1, 92–127.
- **[Weidmann]** J. Weidmann, *Spectral Theory of Ordinary Differential Operators*. Lecture Notes in Math. 1258, Springer, Berlin, 1987.

---

## Citation

```
Shatto, B. (2026).
Twisted Quantum Modes on a Conic Möbius Band: Bound States, Holonomy, and a Stable First Positive Level.
SSRN.
https://ssrn.com/abstract=6968741
```

---

## Independent numerical certification

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_method_note.md)

Theorems 1.1 and 1.2 have been reproduced numerically on the OpenWave M8 track by two mutually independent implementations, both blind: each solver was written from a transcription of the operator alone, with no access to the eigenvalues claimed here or to the text of this paper. One resolves the reduced Sturm-Liouville problem sector by sector with a weighted finite-element scheme on a mesh graded at the cone; a second discretizes the full band in two dimensions; and an adversarial audit re-runs the problem in a disjoint method family, two-half Chebyshev spectral collocation in $`\sin(y/R)`$ together with Frobenius-connection and Riccati shooting.

The two structural constants of the spectrum were recovered to roughly ten digits by solvers that had never seen them. The first positive level returns $`\lambda_1 = 2/R^2`$ across the narrow band $`0 < W \le \pi R/2`$ and the branch $`\alpha_0(\alpha_0+1)/R^2`$ beyond it, doubly degenerate at $`W = \pi R/2`$; a blind evaluation at $`W = 2R`$ gives $`\lambda_1 R^2 = 1.4022484374`$ against the closed form's $`1.4022484385`$. The extension-stability threshold was fixed by blind bisection at $`\delta_0^\ast/R = 0.7357588823`$, matching $`2/e`$ to twelve digits. The Friedrichs realization returns bottom $`0`$ with the discontinuous zero mode and no negative eigenvalue, while each bridging realization carries exactly one, whose small-$`\delta_0`$ coefficient $`\delta_0^2\lambda_b`$ extrapolates to $`-1.2609470067`$ against $`-4e^{-2\gamma} = -1.2609470067`$. All five pre-registered claims were confirmed and adversarially audited; the [method note](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_1_method_note.md) carries the full record.

This is a numerical certification of the theorems as stated, not a second proof. It covers the sector-regular class treated here; the non-sector-regular extensions and the full eigenfunction data lie outside its scope.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
