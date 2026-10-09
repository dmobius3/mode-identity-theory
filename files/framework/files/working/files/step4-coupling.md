<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Step 4 of the postulate bridge, part two: the coupling identity

**Type:** Result
**State:** Closed
**Status (2026-07-01):** Part two closed, terminal: the coupling identity holds and the Möbius channel decouples route-specifically, so the staged route closes as a split.
**Summary:** Proves the coupling identity and the Möbius-channel decoupling, the terminal document of the bridge's staged route, part two of Step 4.
**Parent:** `postulate-bridge.md`

Closed; the terminal document of the staged route. The three-ingredient identity degenerates, and the degeneration is proved, not estimated: along every restriction-route formula with the canonical pullback coefficient bundle, the Möbius ingredient couples to the Galois sector with coefficient exactly zero (the triviality lemma: every coefficient built on $`W`$ restricts rank-trivially to the characteristic slot). The negative is route-specific, per the program's standing standard; the positive residue, the boundary-interior gauge dictionary, survives as theorems. Worksheet: [step4-coupling.test.py](scripts/step4-coupling.test.py) (sanity check on the evaluations, not a substitute for the route scoping).

**Related:** [Step 4, part one](step4-bookkeeping.md), [Step 3](step3-interior-classes.md), [Step 2](step2-analytic-setup.md), [η-gatekeeper (Step 1)](eta-gatekeeper.md), [Postulate bridge](postulate-bridge.md).

---

**Goal.** Decide the revised Step-4 question: is there an identity in which the boundary Galois asymmetry ($`\Delta\rho=-8/5`$, equivalently $`\Delta D=-2/5`$), the interior tautological distance-six data ($`\mathrm{ch}(\mathcal{R}_{d6})`$, $`k=71/30`$), and the characteristic-slot Möbius data ($`e(F)`$, $`\beta(F)`$, anchored by $`\bar\mu=-1`$) all appear with nontrivial coefficients; or does the characteristic slot decouple route-specifically? The answer is the second, and it is now a proof.

**Conventions.** As in parts one and three: $`W`$ the compact truncation of the ALE resolution, $`\partial W=+\Sigma`$, curve basis and tautological bundles $`\mathcal{R}_i`$ with $`c_1(\mathcal{R}_j)`$ dual to the curves ($`\langle c_1(\mathcal{R}_j),[E_i]\rangle=\delta_{ij}`$), the characteristic class of $`W`$ equal to $`0`$ (Step 3).

## 1. How a surface enters an index formula

The mechanisms on the program's table, by which an embedded surface $`F\subset\mathrm{int}\,W`$ participates in an index formula, are of one family: pass to the double branched cover $`\widetilde{W}\to W`$ along $`F`$ when the $`\mathbb{Z}_2`$-null condition permits it, or equivalently work on $`W\smallsetminus F`$ with the appropriate meridian-twisted pin structure; the spin/pin correction along $`F`$ is exactly the Brown/Guillou-Marin datum, not an additional automatic assumption; then apply an APS-type theorem, equivariantly for the deck involution. In every version the formula splits into three kinds of terms: global interior terms (Chern-Weil integrals of the coefficient bundle over $`W`$), boundary terms (eta invariants of the flat limit; here $`\partial\widetilde{W}`$ is two copies of $`+\Sigma`$, because $`2I`$ is perfect and $`\Sigma`$ admits no connected double cover), and **$`F`$-localized terms** (the Atiyah-Singer $`G`$-signature/Lefschetz contribution of the fixed set, which is where $`e(F)`$ and, through the pin refinement, $`\beta(F)`$ live; the Guillou-Marin congruence is the mod-16 shadow of exactly this localization). The Möbius ingredient enters only through the $`F`$-localized terms; the Galois ingredient enters the global and boundary terms, as established in part one. The question is whether the $`F`$-localized terms can carry Galois information when the coefficient bundle is $`\mathcal{R}_{d6}`$ versus $`\mathcal{R}_{d2}`$. Call this family of formulas the *restriction route*: every surface contribution is computed from data of the coefficient bundle restricted to $`F`$ (its characteristic forms and classes on $`F`$, coupled to the normal-bundle data), with the coefficient bundle carried through as the canonical pullback, whose deck action on fibres over the fixed set is trivial, so the $`F`$-localized coefficient factor is the ordinary Chern character of $`\mathcal{R}|_F`$.

## 2. The triviality lemma

**Lemma.** Let $`F\subset W`$ be a closed non-orientable surface with $`[F]_2=0`$ (the characteristic slot, the only slot carrying the canonical Guillou-Marin package, by Step 3). Then **every** complex or real vector bundle on $`W`$, virtual bundles included, restricts to $`F`$ trivially; in particular every tautological bundle does.

*Proof.* For a closed non-orientable surface, $`H^2(F;\mathbb{Q})=0`$ and $`H^2(F;\mathbb{Z})=\mathbb{Z}_2`$ (universal coefficients: the $`\mathrm{Ext}`$ of $`H_1`$), and the mod-2 reduction $`H^2(F;\mathbb{Z})\to H^2(F;\mathbb{Z}_2)`$ is injective, with evaluation against the $`\mathbb{Z}_2`$-fundamental class computing, for a class restricted from $`W`$, the pairing $`\langle c \bmod 2,\ i_*[F]_2\rangle_W`$. Since $`i_*[F]_2=0`$, every class of $`W`$ restricts to zero in $`H^2(F;\mathbb{Z})`$ and in $`H^2(F;\mathbb{Z}_2)`$. Every bundle from $`W`$ has $`w_1=0`$ ($`H^1(W;\mathbb{Z}_2)=0`$), hence is orientable along $`F`$, and its classifying data over the $`2`$-complex $`F`$ (rank and $`c_1`$ for complex bundles; $`w_2`$, or the untwisted Euler class in the oriented rank-$`2`$ case, for real bundles) all live in these two vanishing groups. So every restriction is trivial; virtual bundles follow by additivity. The tautological structure of $`\mathcal{R}_i`$ enters nowhere. $`\square`$

*Corollary.* Part one's carried K-class caveat is discharged: any gauge-deformation complex's K-class is a virtual bundle on $`W`$, and its $`F`$-localized data on the characteristic slot is rank times trivial, automatically.

Consequently every $`F`$-localized term of every restriction-route formula depends on the coefficient bundle only through its rank: the rational characteristic data of $`\mathcal{R}_i|_F`$ vanishes identically (there is no rational $`H^2`$ to hold it), the torsion and Stiefel-Whitney data vanish on this slot, and Chern-Weil integrands built from the restricted connection integrate over $`F`$ to exactly these vanishing characteristic numbers. Nothing else about $`\mathcal{R}_i`$ is visible from $`F`$.

## 3. The decoupling theorem

**Theorem (route-specific decoupling).** In every restriction-route identity on $`W`$ using the canonical pullback coefficient bundle, so that the $`F`$-localized coefficient factor is the ordinary Chern character of $`\mathcal{R}|_F`$ with the standard (trivial) fibre action over the fixed set, the $`F`$-localized contribution has the form $`\mathrm{rk}(\mathcal{R})\cdot T_F`$, where $`T_F`$ depends only on the surface data ($`e(F)`$, $`\beta(F)`$, normal-bundle and pin data) and not on $`\mathcal{R}`$. Since $`\mathrm{rk}(\mathcal{R}_{d6})=\mathrm{rk}(\mathcal{R}_{d2})=3`$, the surface term cancels identically from the Galois difference: the coefficient coupling $`(e(F),\beta(F))`$ to $`\Delta\rho=-8/5`$ is exactly zero along this route. A formula that inserts an additional nontrivial equivariant fibre action along $`F`$ is outside this route and would need to be specified separately; none is on the program's table.

The complementary fork closes the other escape:

- On a **root class** (say $`[F]_2=x_{d6}`$), the restriction is nontrivial ($`\langle c_1(\mathcal{R}_{d6}) \bmod 2,\ x_{d6}\rangle=1`$: the bundle does couple to the surface), but the canonical Guillou-Marin quadratic enhancement supplied by the ambient characteristic-surface setup is not available there (Step 3): extra choices could decorate such a surface with pin data, but the canonical $`W`$-tied package, the one the bridge's Möbius ingredient names, does not attach.
- An **orientable** characteristic surface (integral class $`2\xi`$) pairs integrally with $`c_1(\mathcal{R}_{d6})`$, but carries the Arf package of the classical Rokhlin story, not the Möbius one: its normal data is orientation-preserving, $`w_1(F)=0`$, and the band's $`\mathbb{Z}_2`$ normal twist is exactly what it lacks.

So the two data types occupy channels whose intersection is empty: where the Möbius datum exists, the tautological restriction is trivial; where the tautological restriction is nontrivial, the Möbius datum does not exist. The three-ingredient identity of the revised Step 4 degenerates in every restriction-route formula, and the degeneration is structural, not numerical: it would persist for any $`\Gamma`$ and any pair of equal-rank tautological bundles.

**Scope of the negative.** This is a statement about the restriction route: formulas whose surface dependence enters through $`F`$-localized characteristic data of the coefficient bundle. It covers the $`G`$-signature theorem on branched covers, the Guillou-Marin congruence and its with-boundary refinements, and the twisted-pin-Dirac formulations, which are the mechanisms the staged plan named. It is not a claim that no conceivable invariant links the band to the Galois selection; a coupling would need a mechanism whose surface term sees more of the bundle than its restriction, and no such mechanism is on the program's table.

## 4. The positive residue

What the route proves, rather than fails to prove, is worth stating as the surviving content of the bridge:

- **The gauge dictionary (A and B are coupled, as theorems).** The boundary Galois asymmetry and the interior tautological data determine each other: $`\int_X\mathrm{ch}(\mathcal{R}_W)\hat{A}=D_W`$ (KN), $`\rho^{\mathrm{sign}}_\alpha=\dim\alpha+4(D_\alpha-\dim\alpha\,D_{\mathrm{triv}})`$ (part one), $`k\equiv cs \bmod 1`$ in all four sectors, $`\Delta\rho=-8/5=4\Delta D`$, $`\Delta k=2/5`$. The embedding does real work in the gauge sector: the McKay decoration of $`W`$ carries exactly the boundary's Galois information.
- **The Möbius sector keeps its own identity, Galois-blindly.** For characteristic non-orientable $`F\subset W`$, the with-boundary Guillou-Marin congruence reads $`e(F)+2\beta(F)\equiv\mathrm{sign}(W)-8\mu(\Sigma)\pmod{16}`$, with $`\mu(\Sigma)=1`$ the Rokhlin invariant; since $`\mu\equiv\bar\mu\bmod 2`$, $`8\mu\equiv 8\bar\mu\bmod{16}`$, and part one's $`\bar\mu=-1`$ gives the same landing: $`-8-8=-16\equiv 0\pmod{16}`$ (calibrated on $`B^4`$, where the local $`\mathbb{RP}^2`$ with $`e=+2`$, $`\beta=-1`$ gives $`0`$). Every constant in it ($`\mathrm{sign}=-8`$, $`\mu=1`$, $`\bar\mu=-1`$) is Galois-blind, as Step 3's transitivity theorem requires.
- **No curvature coincidence to check.** Every quantity in both identities is a dimensionless character sum or a surface integer; $`2/R^2`$ never appears, so the curvature-scale-coincidence check of the staged plan is vacuous here.

## 5. The program verdict

The staged APS/index route terminates here, and the 2026-06-28 expectation (the split) is confirmed at the sharper three-ingredient bar, with both halves now proved rather than expected:

1. **Positive.** Boundary gauge asymmetry and interior McKay/tautological topology are linked by identities: the gate value $`-8/5`$ is interior-computable, the CS web is charge-realized, and the whole dictionary is exact. This is the theorem the bridge program produces.
2. **Negative, route-specific.** The band's $`\mathbb{Z}_2`$ normal data cannot be index-coupled to the Galois selection along any restriction-route formula, because on the only slot where that data lives, the tautological bundles are cohomologically invisible. Stated per the standing standard: this route is topological and its surface terms are rank-blind; no claim is made that the two spectra are independent in any universal sense.

For the postulate ($`S^1=\partial(\text{Möbius})\hookrightarrow S^3`$, $`\partial S^3=\emptyset`$): the two pieces remain two consequences of one shape, now with a proven boundary-interior dictionary on the gauge side and a proven obstruction telling us where the Möbius piece cannot be attached. The framework never owed this bridge; what it gets instead is sharper: the exact reason the two pillars stand independently along this path, and the exact identities by which the $`E_8`$ filling remembers the boundary's Galois arithmetic.

## Verdict

Step 4 part two is closed, negative route-specifically and positive where it matters: the coupling coefficient of the Möbius data against the Galois asymmetry is exactly zero in every restriction-route identity (triviality lemma plus equal ranks), the complementary channels are disjoint (root classes couple but carry no Brown package; orientable characteristic surfaces carry Arf, not Möbius, data), and the surviving content is the exact gauge dictionary of part one together with the Galois-blind Guillou-Marin congruence $`e+2\beta\equiv 0 \bmod 16`$ on $`W`$. The staged route is complete. The carried gauge-deformation K-class check is discharged for the $`F`$-localized coupling question: any coefficient built on $`W`$ restricts rank-trivially on the characteristic slot.

## Sources

- Atiyah, Singer ($`G`$-signature theorem, fixed-point localization); Atiyah, Patodi, Singer I-II (APS form; the with-boundary machinery).
- L. Guillou, A. Marin (the congruence and its branched-cover/pin proof mechanism); N. Saveliev, *Invariants for Homology 3-Spheres* (the with-boundary form with the Rokhlin correction).
- P. B. Kronheimer, H. Nakajima, Math. Ann. 288 (1990) (tautological bundles, $`c_1`$ dual basis, the index identities of part one).
- Steps 1-3 and part one of this program (the eta-gatekeeper; the analytic setup and sign; the interior classes; the bookkeeping identities), this working folder.
- Worksheet: [step4-coupling.test.py](scripts/step4-coupling.test.py) (the restriction evaluations and the Galois-difference cancellation, exact; a sanity check on the lemma's evaluations, not a substitute for the route scoping of §§1-3).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
