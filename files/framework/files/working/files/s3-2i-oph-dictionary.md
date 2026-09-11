<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# S³/2I and the OPH Carrier

**Type:** Note
**State:** Active
**Status (2026-09-11):** The character match is computed: as A5 representations, the two golden triplets of OPH's committed face operator are the adjoints of the holonomies of the two irreducible flat SU(2) connections on S³/2I, with W− ≅ Sym²Q (OPH's committed port frame) and W+ ≅ Sym²Q′, checked class by class in exact arithmetic against OPH commit 621edbb2. The Seifert rows are classical and checked against their sources. Next: the low-ℓ Molien structure of 2I against OPH's frozen angular multiplet signature, FZ-02, compared as branching templates.
**Summary:** Where MIT's reading of S³/2I meets the twelve-port carrier of Observer Patch Holography (OPH), each framework computing in its own terms: the Seifert base and its orbifold relation against OPH's coset carrier certificate, and OPH's two golden triplets against the adjoints of MIT's two flat connections.
**Inputs:** `../../bedrock/files/coexact-gap.md` §4.4, `scripts/golden-sector-match.test.py`

[Observer Patch Holography](https://github.com/FloatingPragma/observer-patch-holography) (OPH) declares a local carrier of twelve ports with the oriented boundary complex of the icosahedron. Following the proposal in [OPH #769](https://github.com/FloatingPragma/observer-patch-holography/discussions/769), OPH merged a certificate, [OPH #784](https://github.com/FloatingPragma/observer-patch-holography/pull/784), that reconstructs the carrier as the coset geometry of a supplied $`\mathrm{SL}(2,\mathbb{F}_5)`$, conditional on that group, and its selection ledger now cites it: given the group, the carrier is derived rather than separately supplied. This note records where the carrier meets MIT's reading of $`S^3/2I`$. Each side computes in its own framework, and neither adopts the other's physical interpretation.

## I. The dictionary

| MIT, $`S^3/2I`$ | OPH, the twelve-port carrier | Basis |
|---|---|---|
| $`S^3/2I`$ is Seifert fibred over the orbifold $`S^2/A_5 = S^2(2,3,5)`$, the structure inherited from the Hopf fibration; the three cone points lift to the 30 edge midpoints, 20 face centres and 12 vertices of the icosahedron, with stabilizers $`C_2, C_3, C_5`$ | the coset sets $`G/C_2, G/C_3, G/C_5`$ of the certificate: 30 edges, 20 faces, 12 ports | classical (Scott pp. 412-413, 456; Ebert §8.1); the certificate |
| the base's orbifold group $`\langle x, y, z \mid x^2 = y^3 = z^5 = xyz = 1 \rangle \cong A_5`$, with $`x, y, z`$ the rotations about the corners of one $`(2,3,5)`$ triangle | the certificate's compatibility criterion (Theorem 769.1(b)): generators of $`C_2, C_3, C_5`$ can be chosen with $`xyz = 1`$, met by 120 of the 900 placements | classical (Scott pp. 410-413, 423, 453, 479; Milnor pp. 179, 185); the certificate |
| $`\pi_1(S^3/2I) = 2I`$, Milnor's centrally extended triangle group $`\gamma_1^2 = \gamma_2^3 = \gamma_3^5 = \gamma_1\gamma_2\gamma_3`$, the common value being the lift of a full turn, $`-1`$, which is also the class of the regular fibre | the 120 solutions of $`a^2 = b^3 = c^5 = abc = -I`$ in $`\mathrm{SL}(2,5)`$, one per compatible placement (Theorem 769.1(c)); the certificate factors through the centre | classical (Milnor pp. 175, 186-187; Scott p. 432; Ebert §8.1); the certificate |
| $`\mathrm{Sym}^2 Q`$: McKay distance 2, twisted coexact gap $`4/R^2`$ | $`W_-`$, the golden image at $`\lambda_- = 3 - \sqrt5`$, with the character of the committed port frame | computed here (§II); the gap from [Coexact gap](../../bedrock/files/coexact-gap.md) §4.4 |
| $`\mathrm{Sym}^2 Q^\prime`$: McKay distance 6, twisted coexact gap $`36/R^2`$ | $`W_+`$, the golden image at $`\lambda_+ = 3 + \sqrt5`$ | computed here (§II); the gap as above |
| the Galois twin has the higher gap, $`36/R^2`$ against $`4/R^2`$ | the Galois twin has the higher eigenvalue, $`3 + \sqrt5`$ against $`3 - \sqrt5`$ | ordering only (§III) |
| the low-ℓ Molien structure of $`2I`$ | FZ-02, OPH's frozen angular multiplet signature: the $`A_5`$ branching of the harmonics through $`\ell = 6`$, with the first nonconstant invariant at $`\ell = 6`$ | open (§IV) |
| $`2I`$ singled out by perfectness and the coexact exception | the row-4 family menu, whose convergence question is parked in [OPH #769](https://github.com/FloatingPragma/observer-patch-holography/discussions/769) | open, parked |

Classical topology and the certificate together identify the compatibility condition the certificate found by exhaustive search with the orbifold relation of the Seifert base: on the icosahedron the corners of a $`(2,3,5)`$ triangle are a vertex, the midpoint of an edge at that vertex, and the centre of a face containing both, which is the incident triple the criterion detects. They also identify the binary presentation that selects the compatible placements with the fundamental group of $`S^3/2I`$. The certificate takes the finite group as supplied and claims neither identification; both are this note's reading.

## II. The golden triplets

The [coexact gap](../../bedrock/files/coexact-gap.md) works with the two irreducible flat $`\mathrm{SU}(2)`$ connections on $`S^3/2I`$: the defining representation $`Q`$ of $`2I \subset \mathrm{SU}(2)`$ and its Galois conjugate $`Q^\prime`$. After complexifying, their adjoint representations are $`\mathrm{Sym}^2 Q`$ and $`\mathrm{Sym}^2 Q^\prime`$, the two three-dimensional irreducibles of $`A_5`$. On OPH's side, [GoldenSectorCharacters.lean](https://github.com/FloatingPragma/observer-patch-holography/blob/621edbb2a56b388b3590a5c766a59bd9d2012a17/Lean/Screen/GoldenSectorCharacters.lean) has `goldenPlusZ` and `goldenMinusZ`, twenty times the spectral projectors of the face normal operator $`N = 3I - A`$, with $`A`$ the adjacency of the twenty faces, at $`\lambda_\pm = 3 \pm \sqrt5`$. The two matrices have trace 60 (`plus_trace`, `minus_trace`), so the projectors have trace 3; the file flags the step from trace to rank three as an inference outside its theorems. The images are written $`W_\pm`$ here, following [OPH #785](https://github.com/FloatingPragma/observer-patch-holography/pull/785).

Comparing characters needs a labelling of the two classes of order-five rotations that is intrinsic to each side. An order-five rotation is *one-step* when it moves each neighbour of its fixed vertex to an adjacent neighbour, and *two-step* otherwise; every graph isomorphism preserves the distinction. The one identification used comes from OPH's committed data: `PortFrameGram` places graph neighbours at inner product $`1/\sqrt5`$, the nearest-neighbour value on the unit icosahedron, and the certificate relabels the coset graph onto that same neighbour list.

| order-five rotations | port frame | $`W_-`$ | $`W_+`$ | $`\mathrm{Sym}^2 Q`$ | $`\mathrm{Sym}^2 Q^\prime`$ |
|---|---|---|---|---|---|
| one-step (12) | $`\varphi`$ | $`\varphi`$ | $`1-\varphi`$ | $`\varphi`$ | $`1-\varphi`$ |
| two-step (12) | $`1-\varphi`$ | $`1-\varphi`$ | $`\varphi`$ | $`1-\varphi`$ | $`\varphi`$ |

All five take $`3`$, $`-1`$, $`0`$ on the elements of order 1, 2, 3, so the characters agree class by class: $`\mathrm{Sym}^2 Q \cong W_-`$, the representation of the committed port frame, and $`\mathrm{Sym}^2 Q^\prime \cong W_+`$. Relative to the committed port frame, $`W_-`$ is the matching triplet and $`W_+`$ its Galois twin. This labels the twelve-and-twelve split of the order-five rotations that `GoldenSectorCharacters` records without a geometric label: $`\chi_+ = \varphi`$ exactly on the two-step class.

A check by hand needs neither the committed projectors nor quaternions. The face graph is the dodecahedron graph, and the dodecahedron vertex $`(1,1,1)`$ has neighbours $`(0, 1/\varphi, \varphi)`$, $`(1/\varphi, \varphi, 0)`$ and $`(\varphi, 0, 1/\varphi)`$, which sum to $`\sqrt5\,(1,1,1)`$ since $`\varphi + 1/\varphi = \sqrt5`$. So the coordinate triplet sits at adjacency eigenvalue $`\sqrt5`$, the eigenvalue $`3 - \sqrt5`$ of $`N`$, and a one-step rotation, through $`2\pi/5`$, has trace $`1 + 2\cos 72^\circ = \varphi`$ on it. The port frame is the coordinate triplet by construction: `PortFrameGram` proves $`G^2 = 4G`$ with trace 12, so $`G/4`$ is a rank-three projector and the ports are twelve vertex directions in $`\mathbb{R}^3`$. On the $`S^3/2I`$ side a one-step rotation lifts to trace $`\pm 2\cos 36^\circ = \pm\varphi`$ in $`Q`$, and the sign drops out: $`\chi_{\mathrm{Sym}^2 Q} = \chi_Q^2 - 1 = \varphi`$, the value §4.4 of the [coexact gap](../../bedrock/files/coexact-gap.md) gives on the order-ten class.

## III. Limits

- The same Galois-conjugate triplet is higher in both constructions: $`36/R^2`$ against $`4/R^2`$ here, $`3 + \sqrt5`$ against $`3 - \sqrt5`$ in OPH. MIT's numbers are squared first-occurrence levels in the branching of $`2I`$: $`\mathrm{Sym}^2 Q`$ first occurs at level two and $`\mathrm{Sym}^2 Q^\prime`$ not until level six ([coexact gap](../../bedrock/files/coexact-gap.md), Theorem 4.2 and §4.4). OPH's are eigenvalues of a face operator on a twenty-dimensional space. The quantities are of different kinds and the ratios differ, $`9`$ against $`\varphi^4`$, so no shared mechanism is claimed.
- Both adjoints are trivial on the centre, so the match lives on $`A_5`$. The faithful two-dimensional $`Q`$ has no counterpart in the carrier, and the certificate cannot see the centre either.
- Nothing here selects $`2I`$ or bears on OPH's selection ledger.

## IV. Open

- **Next:** the low-ℓ Molien structure of $`2I`$ against FZ-02, comparing the two branching patterns as templates. FZ-02 is a frozen forward target in OPH's register, with its own kill bands and custody, and the comparison leaves those untouched.
- Whether the ordering in §III reflects anything beyond itself.
- Whether OPH's $`\lambda_+`$ triplet plays any distinguished role there beyond being the Galois partner of the $`\lambda_-`$ triplet.
- Selection: why $`2I`$ among the finite subgroups of $`\mathrm{SU}(2)`$. Parked on both sides.

## Check

[golden-sector-match.test.py](scripts/golden-sector-match.test.py) reads OPH's committed Lean tables at commit [621edbb2](https://github.com/FloatingPragma/observer-patch-holography/tree/621edbb2a56b388b3590a5c766a59bd9d2012a17) as data, executing nothing from OPH, and builds $`2I`$ as 120 exact unit quaternions over $`\mathbb{Q}(\sqrt5)`$. It reproduces the character facts `GoldenSectorCharacters` proves, and asserts that the port frame has the character of $`W_-`$ rotation by rotation, that $`\chi_{\mathrm{Sym}^2 Q}`$ agrees with $`\chi_{W_-}`$ on every class, and that `goldenPlusZ` and `goldenMinusZ` are eigen-images of `faceNormalZ` at $`3 \pm \sqrt5`$, entrywise. Three mutation arms, each run after its parent passes, confirm that the port frame fails against $`W_+`$, that classifying the rotations with the distance-two graph breaks the match, and that swapping the eigenvalues breaks the entrywise check. The run is recorded in [golden-sector-match.out](scripts/golden-sector-match.out). Standard library only; run it as `OPH_CLONE=/path/to/observer-patch-holography python3 golden-sector-match.test.py`.

## References

- P. Scott, The geometries of 3-manifolds, *Bull. London Math. Soc.* 15 (1983), 401-487, doi:[10.1112/blms/15.5.401](https://doi.org/10.1112/blms/15.5.401). Triangle groups with $`xyz = 1`$ (p. 410); the spherical triangle groups as the rotation groups of the regular solids (pp. 412-413); orbifold fundamental groups (p. 423; three cone points, p. 479); Lemma 3.2, the regular fibre generates the kernel (p. 432); $`I \cong A_5`$ (p. 453); the Poincaré sphere's Seifert structure from the Hopf fibration, with base $`S^2/I`$ (p. 456).
- J. Milnor, On the 3-dimensional Brieskorn manifolds $`M(p,q,r)`$, in *Knots, Groups, and 3-Manifolds*, Ann. of Math. Stud. 84 (1975), 175-225, MR 418127. $`M \cong \Pi \backslash G`$ with $`G = \mathrm{SU}(2)`$ and $`\Pi`$ finite when $`1/p + 1/q + 1/r > 1`$ (p. 175); the $`(2,3,5)`$ rotation group is the icosahedral group, the alternating group on five letters (pp. 179, 185); Lemma 3.1, the centrally extended triangle group and its presentation, the common value the lift of a full turn (pp. 186-187).
- J. Ebert, *Characteristic classes of spin surface bundles: Applications of the Madsen-Weiss theory*, dissertation, Bonn (2006), [arXiv:math/0611612](https://arxiv.org/abs/math/0611612), §8.1: the stabilizers of orders 2, 3, 5; $`\mathrm{SL}_2(\mathbb{F}_5)`$ as the binary icosahedral group; the Poincaré sphere's three singular fibres over the vertex, edge and face orbits.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
