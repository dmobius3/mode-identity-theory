<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🤑 Yang-Mills

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/yang%20mills%20banner.png?raw=true" width="100%" alt="Yang Mills">

The Millennium Prize asks whether pure Yang-Mills on flat $`\mathbb{R}^4`$ has a positive mass gap in the full quantum theory. That is open and hard. This page takes its easier cousin: the same gap question on the compact, curved Poincaré Homology Sphere $`M = S^3/2I`$, at the linearized level, where the answer falls out of the shape.

| | The Prize asks for | This page delivers |
|---|---|---|
| Space | flat $`\mathbb{R}^4`$ | compact $`S^3/2I`$ |
| Object | nonperturbative quantum mass gap | linearized coexact gap |
| Status | open and hard | classical, forced by the geometry |

The surprise is the bottom-right cell: a mass gap appears for free from a shape, and its coefficient in units of $`1/R^2`$ is read off the McKay structure. Positive Ricci curvature forces a gap to exist; the finite group $`2I`$ gives exactly three isolated vacua (trivial, standard, Galois conjugate); and the McKay graph, the affine $`E_8`$ diagram, fixes the value at each, $`4/R^2`$ at two and $`36/R^2`$ at the third, a ninefold enhancement at the Galois sector. The same curvature that forces this gap also enters the conversion that sets the vacuum-reference $`\Lambda_\text{ref}`$: one geometry, two consequences.

(Throughout, $`R`$ is the curvature radius of the round metric, the framework's $`R_\Lambda`$; for $`S^3/2I`$, $`\Lambda_\text{ref} = 3/R_\Lambda^2`$.)

| Property | Value |
|---|---|
| Gap exists | positive Ricci, and $`H^1 = 0`$ |
| Vacua | 3 isolated (trivial, standard, Galois) |
| Gap (trivial, standard) | $`\Delta^2 = 4/R^2`$ (adjoint enters at level 2) |
| Gap (Galois) | $`\Delta^2 = 36/R^2`$ (adjoint at level 6; 9×) |
| Three vacua → three generations | MIT reading, an interpretation layered on the three vacua |

## I. The Geometry

In the Hamiltonian formulation of Yang-Mills on $`M \times \mathbb{R}`$, temporal gauge ($`A_0 = 0`$) with the Coulomb condition ($`d_A^\ast a = 0`$) reduces the linearized equation around a flat connection to $`\partial_t^2 a + \Delta_{\mathrm{Hodge}} a = 0`$. Modes oscillate as $`e^{i\omega t}`$ with $`\omega^2 = \lambda`$, so the gap is the lowest eigenvalue of the Hodge Laplacian on the coexact 1-forms, the physical fluctuations after gauge-fixing.

That this lowest eigenvalue is strictly positive is forced two ways before any dynamics, by curvature and by topology. Geometrically, for a flat connection ($`F_A = 0`$) the Weitzenböck identity reads

```math
\Delta_{\mathrm{Hodge}} = \nabla_A^\ast \nabla_A + \mathrm{Ric},
```

and on the round $`S^3`$ of radius $`R`$ the curvature $`\mathrm{Ric} = 2/R^2 > 0`$ bounds every coexact (divergence-free) fluctuation away from zero. Topologically, the twisted harmonic 1-forms vanish, $`H^1(M; \mathrm{ad}\,\rho) = 0`$ (§II), so $`\Delta_{\mathrm{Hodge}}`$ is strictly positive on the coexact summand at every vacuum. The gap exists.

Its value is sharper than the curvature bound: it comes from the coexact form spectrum of $`S^3`$ read through the McKay structure (§III), giving $`4/R^2`$ and $`36/R^2`$. The Bochner floor $`\lambda \geq 2/R^2`$ sits below the actual gap. (That floor $`2/R^2`$ is numerically the surface eigenvalue $`\Lambda_\text{top}`$ of the $`\Lambda`$ sector, but it is a different operator; here it is only a loose lower bound on the gauge gap.)

## II. Three Vacua

Flat $`\mathrm{SU}(2)`$ connections on $`M`$ are classified by $`\mathrm{Hom}(2I, \mathrm{SU}(2))/\mathrm{conj}`$. A homomorphism $`\rho: 2I \to \mathrm{SU}(2)`$ is equivalently a 2-dimensional unitary representation with determinant 1. The character table of $`2I`$ has exactly nine irreducible representations, of which exactly two have dimension 2: $`R_1`$ and $`R_2`$, the standard connection $`Q = R_1`$ and its Galois conjugate $`Q' = R_2`$. Both are faithful. The only remaining possibility is the trivial map ($`\rho(g) = I`$). This gives three conjugacy classes total.

| Vacuum | Connection | Adjoint | $`2I`$ irrep | adjoint distance |
|---|---|---|---|---|
| 1st | trivial | trivial | $`R_0^{\oplus 3}`$ | 0 |
| 2nd | $`\rho_{\mathrm{std}} = Q`$ ($`R_1`$) | $`\mathrm{Sym}^2 Q`$ | $`R_3`$ | 2 |
| 3rd | $`\rho_{\mathrm{gal}} = Q'`$ ($`R_2`$) | $`\mathrm{Sym}^2 Q'`$ | $`R_4`$ | 6 |

The standard and Galois embeddings are distinguished by the golden ratio: $`\rho_{\mathrm{std}}`$ has trace $`\varphi = (1+\sqrt{5})/2`$ on order-10 elements, while $`\rho_{\mathrm{gal}}`$ has trace $`\bar\varphi = (1-\sqrt{5})/2`$. Since $`\mathrm{SU}(2)`$ conjugation preserves traces and $`\varphi \neq \bar\varphi`$, the two define distinct conjugacy classes. The kernel $`\{\pm 1\}`$ case (factoring through $`A_5`$) produces no additional class because $`A_5`$ has no faithful 2-dimensional representation.

### Vacuum isolation

Each vacuum is isolated: vanishing $`H^1(M; \mathrm{ad}\ \rho) = 0`$ at each flat connection guarantees that no continuous moduli connect the families and no massless modes bridge them. For any finite group $`G`$ and any $`\mathbb{R}G`$-module $`V`$, Maschke's theorem ($`\lvert G \rvert`$ invertible in $`\mathbb{R}`$) implies $`H^n(G; V) = 0`$ for all $`n \geq 1`$. Applied with $`G = 2I`$ and $`V = \mathfrak{su}(2)`$ under $`\mathrm{Ad} \circ \rho`$, this gives $`H^1 = 0`$ for every $`\rho`$, irreducible or trivial. For the trivial connection specifically, $`H^1(M; \mathrm{ad}\ \rho_\mathrm{triv}) = H^1(M; \mathbb{R})^3`$; since $`\pi_1(M) = 2I`$ is a perfect group ($`2I`$ equals its own commutator subgroup), $`H_1(M; \mathbb{Z}) = 0`$, so $`H^1(M; \mathbb{R}) = 0`$ by universal coefficients. Both routes give the same conclusion.

Each vacuum is stable on the physical fluctuation space. This is independent of the $`H^1`$ argument: the Weitzenböck bound from Section I applies to coexact (divergence-free) 1-forms, which are precisely the physical gauge fluctuations after Coulomb gauge-fixing. Since $`\lambda \geq 2/R^2 > 0`$ for every such mode, no physical fluctuation has zero or negative eigenvalue. Isolation (no directions to move) and stability (no soft modes) are established by separate mechanisms. The number three is the count of flat $`\mathrm{SU}(2)`$ connections on $`S^3/2I`$. The identification of three vacua with three particle generations is a structural observation within Mode Identity Theory; it is not a consequence of the Yang-Mills analysis presented here. The mathematical result is that exactly three isolated, stable vacua exist.

## III. The Spectral Filter

<p align="center"><img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/ym-mckay-gaps.png?raw=true" width="90%" alt="The affine E8 McKay graph of 2I with each irreducible representation R0 to R8 labeled by its McKay distance from R0; the adjoints of the three vacua are open circles: R0 and R3 = Sym2 Q first appear at level m = 2, a gap of 4/R^2, and R4 = Sym2 Q prime at distance 6 first appears at m = 6, a gap of 36/R^2"></p>

The McKay graph of $`2I`$ is the extended (affine) $`E_8`$ Dynkin diagram. Each node corresponds to an irreducible representation of $`2I`$; the edges encode tensor product with the fundamental 2-dimensional representation. The restriction of the spin-j representation of $`\mathrm{SU}(2)`$ to $`2I`$ follows the McKay recursion along this graph. Since each recursion step extends the reachable subgraph by at most one edge, an irrep at graph distance $`d`$ from $`R_0`$ requires at least $`d`$ steps to first appear: distance controls the filtration depth.

### Coexact spectrum on $`S^3`$

On the round $`S^3`$ of radius $`R`$, coexact (divergence-free) 1-forms organize into levels $`m = 2, 3, 4, \ldots`$ with eigenvalue:

```math
\lambda_m = \frac{m^2}{R^2}
```

This is the coexact form spectrum of Ikeda–Taniguchi, descended to the quotient by the equivariant method of Lauret–Miatello–Rossetti.

On $`S^3 = \mathrm{SU}(2)`$, the Hodge Laplacian commutes with the isometry group $`\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R`$, so its eigenvalue on an irreducible component $`(j_L, j_R)`$ takes the form $`\lambda = a \cdot j_L(j_L+1) + b \cdot j_R(j_R+1) + c`$. Hodge star symmetry ($`*`$ swaps $`j_L \leftrightarrow j_R`$) forces $`a = b`$. Agreement with the scalar Laplacian on exact 1-forms at $`(j, j)`$ fixes $`a = 2/R^2`$, $`c = 0`$. Coexact 1-forms appear at $`(j_R \pm 1, j_R)`$; both series yield eigenvalue $`m^2/R^2`$ with $`m = 2, 3, 4, \ldots`$

On the quotient $`M = S^3/2I`$, physical modes at level $`m`$ must satisfy a twisted equivariance condition: the adjoint representation $`\mathrm{ad}(\sigma) = \mathrm{Sym}^2\rho`$ of the vacuum must appear in the $`2I`$-decomposition of the 1-form representation at that level. By Frobenius reciprocity, the dimension of the $`\mathrm{ad}(\sigma)`$-isotypic equivariant subspace at level $`m`$ is $`\langle \mathrm{ad}(\sigma), (V_{m-2} \oplus V_m)\vert_{2I} \rangle_{2I}`$. When this inner product vanishes, no equivariant section exists and the level is filtered out entirely.

### Representation content at each level

The left-<i>SU(2)</i> content of coexact 1-forms at eigenvalue $`m^2/R^2`$ is $`V_{m-2} \oplus V_m`$, combining the two coexact series identified above. Restricting to $`2I`$ via the McKay recursion $`V_{l+1}\vert_{2I} = R_1 \otimes V_l\vert_{2I} - V_{l-1}\vert_{2I}`$ gives:

```math
V_0 = R_0, \quad V_1 = R_1, \quad V_2 = R_3, \quad V_3 = R_6, \quad V_4 = R_7, \quad V_5 = R_8, \quad V_6 = R_5 \oplus R_4
```

Here $`R_3 = \mathrm{Sym}^2 Q`$ is the standard adjoint (first appearing at $`V_2`$, McKay distance 2) and $`R_4 = \mathrm{Sym}^2 Q'`$ is the Galois adjoint (first appearing at $`V_6`$, distance 6).

The $`2I`$ content of gauge-valued 1-forms at each coexact level is therefore $`(V_{m-2} \oplus V_m)\vert_{2I}`$:

| $`m`$ | $`\lambda_m`$ | $`V_{m-2}\vert_{2I}`$ | $`V_m\vert_{2I}`$ | Combined $`2I`$ content | $`R_0`$? | $`R_3 = \mathrm{Sym}^2 Q`$? | $`R_4 = \mathrm{Sym}^2 Q'`$? |
|---|---|---|---|---|---|---|---|
| 2 | $`4/R^2`$ | $`R_0`$ | $`R_3`$ | $`R_0,\; R_3`$ | ✓ | ✓ | — |
| 3 | $`9/R^2`$ | $`R_1`$ | $`R_6`$ | $`R_1,\; R_6`$ | — | — | — |
| 4 | $`16/R^2`$ | $`R_3`$ | $`R_7`$ | $`R_3,\; R_7`$ | — | ✓ | — |
| 5 | $`25/R^2`$ | $`R_6`$ | $`R_8`$ | $`R_6,\; R_8`$ | — | — | — |
| 6 | $`36/R^2`$ | $`R_7`$ | $`R_5 \oplus R_4`$ | $`R_7,\; R_5,\; R_4`$ | — | — | ✓ |

Each vacuum requires its adjoint representation to appear in the combined column. The trivial vacuum ($`\mathrm{ad} = 3 \times R_0`$: trivial $`2I`$-action on $`\mathfrak{su}(2)`$) requires $`R_0`$; the standard vacuum ($`\mathrm{ad} = \mathrm{Sym}^2 Q = R_3`$) requires $`R_3`$. Both pass at $`m = 2`$. The Galois vacuum ($`\mathrm{ad} = \mathrm{Sym}^2 Q' = R_4`$) requires $`R_4`$, which is absent at $`m = 2`$ through $`m = 5`$ and first appears at $`m = 6`$. Four levels are filtered. The computation is finite and verifiable from the character table of $`2I`$.

### Gap values

The lowest coexact level on $`S^3`$ is $`m = 2`$, so every vacuum's gap is at least $`4/R^2`$: that $`m = 2`$ level is the baseline. Above it, an adjoint at McKay distance $`d`$ first appears at level $`m = \max(2, d)`$, and the gap is $`m^2/R^2`$:

| Vacuum | Adjoint | distance $`d`$ | first level $`m`$ | gap |
|---|---|---|---|---|
| $`\rho_{\mathrm{triv}}`$ | $`R_0`$ | 0 | 2 (baseline) | $`4/R^2`$ |
| $`\rho_{\mathrm{std}}`$ | $`\mathrm{Sym}^2 Q = R_3`$ | 2 | 2 | $`4/R^2`$ |
| $`\rho_{\mathrm{gal}}`$ | $`\mathrm{Sym}^2 Q' = R_4`$ | 6 | 6 | $`36/R^2`$ |

Trivial and standard sit at the $`m = 2`$ baseline; the Galois adjoint clears it and is pushed to $`6^2 = 36`$. The ninefold enhancement is the Galois-over-baseline ratio, $`(6/2)^2 = 9`$, and $`R_4`$ first enters the combined content at $`m = 6`$. These gaps are eigenvalues ($`\omega^2 = \lambda`$, §I), so the physical mode masses are $`\sqrt{\lambda} = 2/R`$ and $`6/R`$: the 9× in eigenvalue is 3× in mass. The level index is topological (the Galois adjoint sits at graph distance 6); the eigenvalue scale is metric-dependent (the round-metric formula $`\lambda_m = m^2/R^2`$). Vacuum-to-generation assignment is open; the topology fixes these three gauge-sector gap values, and any fermion mass ordering read from them is a separate, open question.

## IV. Three Pillars

The spectral gap result rests on three independent arguments, each verifiable with standard mathematical tools:

| Pillar | Method | What it establishes |
|---|---|---|
| Curvature floor | Riemannian geometry (Weitzenböck) | $`\lambda \geq 2/R^2`$ for all coexact gauge fluctuations around any flat connection on any $`S^3`$ quotient. The gap exists. |
| Vacuum isolation | Algebraic topology | Finiteness of $`\pi_1 = 2I`$ gives a finite moduli space. $`H^1 = 0`$ at each flat connection: no moduli, no massless modes. |
| Spectral computation | Finite group theory (McKay) | Explicit gap values at each vacuum. Icosahedral filtering at the Galois sector produces the 9× enhancement. |

### What is topological vs metric-dependent

The existence of the gap, the discreteness of vacua, the vanishing $`H^1`$, and the number of filtered levels are all topological. The 9× enhancement ratio and the numerical value of $`\lambda_{\min}`$ are metric-dependent, following from the round-metric eigenvalue formula $`\lambda_m = m^2/R^2`$.

### Connection to MIT

Within Mode Identity Theory, $`R`$ is the curvature radius of the spatial $`S^3`$, the same length scale that sets $`\Lambda_\text{ref}`$, so $`\Delta^2 = 4/R^2`$ is tied to that one geometric input rather than a free dial. Its numerical value is currently known only to order of magnitude: the coupling and the fermion mass spectrum give two independent readings that agree on the scale but not on the value, the canonical electron-muon pair sitting about $`3.2\times`$ above the coupling route while tighter assigned-pair reads narrow the gap, an open tension carried explicitly (see [the R problem](../../framework/files/working/files/r-problem.md)). The same positive curvature $`\mathrm{Ric}(S^3) = 2/R^2`$ that guarantees the linearized coexact gap here enters the conversion that produces $`\Lambda_\text{ref}`$. One geometry, two consequences: the vacuum-reference term and the spectral gap share a common geometric origin in the curvature of $`S^3`$.

The $`2I`$ structure performs three roles: it partitions phase space into the 120-domain (the scaling law), it filters gauge fluctuations into three isolated vacua with computed spectral gaps (this result), and it provides the spectral geometry whose McKay multiplicities are the $`E_8`$ root system.

### A parallel gap in the scalar sector

The same McKay filtering, applied to the trivial representation $`R_0`$ rather than the adjoint, governs a separate operator: the scalar harmonics on $`S^3/2I`$, graded by polynomial degree $`N`$, a separate index from the gauge level $`m`$. This is a distinct computation from the gauge gap above, sharing only the mechanism. Scalar harmonics on $`S^3`$ have eigenvalue $`N(N+2)/R^2`$ for $`N = 0, 1, 2, \ldots`$. The center $`\{-1\} \in 2I`$ acts on degree $`N`$ by $`(-1)^N`$, restricting $`R_0`$-invariants to even $`N`$. Among these, the Molien series

```math
P(t) = \frac{1 - t^{60}}{(1 - t^{12})(1 - t^{20})(1 - t^{30})}
```

shows the first nontrivial invariant at $`N = 12`$. Five even-degree shells ($`N = 2, 4, 6, 8, 10`$) are empty. The mechanism parallels the gauge sector: the McKay recursion walks along the $`E_8`$ graph, and the trivial representation does not reappear until the walk returns after twelve steps. This shell gap is a spectral fact about the scalar sector. The same gap underlies the Molien account of the CMB low-ℓ deficit, which survives under the flat-FLRW cosmology; it does not by itself fix the curvature radius (see [CMB Anomalies](../../cosmos/files/cmb-anomalies.md) and [the R problem](../../framework/files/working/files/r-problem.md)).

## V. Falsification

Every prediction is checkable by finite computation.

| Prediction | Falsified if |
|---|---|
| 3 conjugacy classes in $`\mathrm{Hom}(2I, \mathrm{SU}(2))/\mathrm{conj}`$ | Additional class constructed, or standard and Galois proved conjugate |
| $`H^1(M; \mathrm{ad}\ \rho) = 0`$ at irreducible flats | Nonzero cohomology demonstrated |
| First $`\mathrm{Sym}^2 Q'`$ appearance at $`m = 6`$ ($`R_4`$ first in $`V_6\vert_{2I}`$) | Character sum yields $`R_4`$ at lower $`m`$ |
| Galois gap at $`m = 6`$ | Coexact 1-form of $`\mathrm{Sym}^2 Q'`$ type found at lower $`m`$ |

### Physical predictions (conditional on compact topology)

| Prediction | Test |
|---|---|
| Spectral gap scales as $`1/R^2`$ | Lattice Yang-Mills on $`S^3/2I`$ geometry |
| 9× enhancement at Galois vacuum | Lattice measurement of sector-resolved spectrum |

---

SU(2) Yang-Mills on the Poincaré Homology Sphere has a positive spectral gap. Positive curvature forces it. Three isolated vacua emerge, which MIT reads as three generations. The McKay correspondence filters the Galois sector through four empty levels, yielding a ninefold enhancement at the distance-6 node of the $`E_8`$ graph. The level gap is topological; the eigenvalues are geometric. The computation reduces to finite group representation theory, standard gauge theory, and Riemannian geometry.

*On curved ground, a gap is easy money.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
