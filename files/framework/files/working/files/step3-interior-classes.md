<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Step 3 of the postulate bridge: the interior classes mod 2

**Type:** Result
**State:** Closed
**Status (2026-07-01):** The interior mod-2 classes are computed and are Galois-blind, so the boundary's Galois asymmetry cannot reach the interior through bare homology; it must run through the tautological decoration.
**Summary:** Computes the interior mod-2 homology classes of the E8 filling and shows they are Galois-blind, the Step-3 result of the bridge's staged route.
**Parent:** `postulate-bridge.md`

Closed. The three staged items are computed: $`H_2(W;\mathbb{Z}_2)=\mathbb{Z}_2^8`$ carries the $`E_8`$ adjacency form ($`W`$ spin, unique characteristic class $`0`$); every class carries non-orientable embedded surfaces with the mod-4 invariant menu; the Galois node is the short-arm curve, mod 2 one of the $`120`$ root classes. The structural finding: the interior mod-2/mod-4 homology is Galois-blind, the Möbius and Galois channels occupy disjoint slots, and Step 4 is revised to a three-ingredient identity. Scope: no surface insertion and no index formula; those are Step 4. Numerical claims are exact; the worksheet is [step3-interior-classes.test.py](scripts/step3-interior-classes.test.py).

**Related:** [Step 2](step2-analytic-setup.md), [η-gatekeeper (Step 1)](eta-gatekeeper.md), [Postulate bridge](postulate-bridge.md), [Coexact gap](../../bedrock/files/coexact-gap.md).

---

**Goal.** Compute $`H_2(W;\mathbb{Z}_2)`$ for the $`E_8`$ plumbing $`W=\widetilde{X}`$, determine which classes carry non-orientable embedded surfaces and with what invariants, and locate the class the McKay correspondence assigns to the Galois node $`\mathrm{Sym}^2Q'`$. The step is topological and closes by direct computation. It also produces one structural finding that sharpens Step 4: the mod-2 and mod-4 homology of $`W`$ is Galois-blind, so the interior's Galois-sensitivity lives entirely in the McKay/tautological structure, and the Möbius channel and the Galois channel occupy different slots of the topology.

**Conventions.** $`W`$ denotes a compact truncation of the ALE minimal resolution of $`\mathbb{C}^2/2I`$, equivalently the negative $`E_8`$ plumbing, with $`\partial W=+\Sigma`$ (Step 2's orientation dictionary). Curve basis $`E_1,\dots,E_8`$ indexed by McKay distance as in Steps 1-2: the chain $`E_1(Q)\,\text{-}\,E_2(\mathrm{Sym}^2Q)\,\text{-}\,E_3\,\text{-}\,E_4\,\text{-}\,E_5\,\text{-}\,E_6\,\text{-}\,E_7(Q')`$ with the branch $`E_8(\mathrm{Sym}^2Q')`$ attached to $`E_5`$. Intersection form $`-C_{E_8}`$ (even, unimodular, signature $`-8`$). As a star-shaped plumbing: central vertex $`E_5`$, three arms of lengths $`4`$, $`2`$, $`1`$ (all weights $`-2`$), whose continued fractions $`[2,\dots,2]`$ of length $`\ell`$ give $`(\ell+1)/\ell`$, so the arms carry the Seifert multiplicities $`5`$, $`3`$, $`2`$ respectively. The three arm tips are $`E_1=Q`$ (multiplicity-$`5`$ arm), $`E_7=Q'`$ (multiplicity-$`3`$ arm), and $`E_8=\mathrm{Sym}^2Q'`$ (multiplicity-$`2`$ arm). All numerical claims below were verified by exact computation (reflection closure for the roots; exhaustive enumeration of the $`256`$ classes for the quadratic counts).

## 1. The mod-2 homology

$`W`$ is simply connected with $`H_2(W;\mathbb{Z})=\mathbb{Z}^8`$, so
```math
H_2(W;\mathbb{Z}_2)=\mathbb{Z}_2^8,
```
and since $`\partial W`$ is an integral homology sphere, the natural map $`H_2(W;\mathbb{Z}_2)\to H_2(W,\partial W;\mathbb{Z}_2)`$ is an isomorphism: every relative class closes up, and for the classes considered here closed interior representatives suffice.

Mod 2 the diagonal entries $`-2`$ vanish and the off-diagonal entries $`-1`$ survive: **the mod-2 intersection form is the adjacency form of the $`E_8`$ graph.** Three immediate consequences:

- **Alternating.** $`x\cdot x=0`$ for every $`x\in H_2(W;\mathbb{Z}_2)`$ (symmetric matrix with zero diagonal). Nondegenerate ($`\det C_{E_8}=1`$ is odd), hence symplectic: $`(H_2(W;\mathbb{Z}_2),\cdot)\cong 4`$ hyperbolic planes.
- **Unique characteristic class, and it is zero.** A characteristic class satisfies $`c\cdot x=x\cdot x=0`$ for all $`x`$; nondegeneracy forces $`c=0`$.
- **$`W`$ is spin.** By the Wu relation $`\langle w_2,x\rangle=x\cdot x \bmod 2`$ and $`H^2(W;\mathbb{Z}_2)\cong\mathrm{Hom}(H_2(W;\mathbb{Z}_2),\mathbb{Z}_2)`$ (no torsion, $`H_1=0`$), $`w_2=0`$; with $`H^1(W;\mathbb{Z}_2)=0`$ the spin structure is unique. Consistent with Step 2: the form is even.

## 2. The mod-4 refinement

Because the integral form is even, the self-intersection of an integer lift is well-defined mod 4 on the mod-2 class: for $`x\in H_2(W;\mathbb{Z}_2)`$ with integral lift $`\xi`$, changing the lift changes $`\xi\cdot\xi`$ by $`4\mathbb{Z}`$. This defines the mod-4 quadratic refinement induced by the Pontryagin square,
```math
\mathfrak{P}:H_2(W;\mathbb{Z}_2)\to\mathbb{Z}_4,\qquad \mathfrak{P}(x+y)=\mathfrak{P}(x)+\mathfrak{P}(y)+2\,(x\cdot y),
```
with $`\mathfrak{P}(E_i \bmod 2)=-2\equiv 2`$ for every curve class. Exhaustive enumeration over all $`256`$ classes gives:

- $`\mathfrak{P}`$ takes only the values $`0`$ and $`2`$; the counts are $`N_0=136`$ (the zero class plus $`135`$ nonzero isotropic classes) and $`N_2=120`$.
- The Gauss sum is $`N_0-N_2=16=2^{8/2}\,e^{2\pi i\,\sigma/8}`$ with $`\sigma=-8`$: the van der Blij consistency check passes exactly.
- $`135=(2^3+1)(2^4-1)`$ is the isotropic-point count of the plus-type quadric on $`\mathbb{Z}_2^8`$, as it must be.
- **The $`120`$ classes with $`\mathfrak{P}=2`$ are exactly the mod-2 reductions of the $`240`$ roots of $`E_8`$** (roots reduce in $`\pm`$ pairs, $`240/2=120`$; verified by reflection closure: the root classes exhaust the $`\mathfrak{P}=2`$ set). That $`N_2=120=\lvert 2I\rvert`$ is standard lattice combinatorics, not new arithmetic, and the coincidence runs through the lattice (roots reduce in $`\pm`$ pairs), not through the McKay bijection, which matches irreps to nodes, not group elements to roots.

## 3. Non-orientable representability

**Existence, all classes.** Every $`x\in H_2(W;\mathbb{Z}_2)`$ has an integral lift (no torsion), every integral class in a compact oriented 4-manifold is represented by a smoothly embedded closed oriented surface, and a local cross-cap (connected sum with the standard $`\mathbb{RP}^2\subset B^4`$ of normal Euler number $`\pm 2`$, supported in a ball) makes any representative non-orientable without changing its $`\mathbb{Z}_2`$ class. So **every class in $`H_2(W;\mathbb{Z}_2)`$, including zero, is represented by embedded non-orientable surfaces of every sufficiently large non-orientable genus.**

**The invariant menu.** A closed non-orientable $`F\subset W`$ carries two basic invariants: its Euler characteristic $`\chi(F)`$ and its normal Euler number $`e(F)\in\mathbb{Z}`$ (twisted Euler class; the normal bundle is non-orientable along orientation-reversing loops, but the pairing with the twisted fundamental class is an integer). Each cross-cap changes $`(\chi,e)`$ by $`(-1,\pm 2)`$, so the combination $`e+2\chi \bmod 4`$ is invariant under cross-capping; starting from an orientable representative ($`e=\xi\cdot\xi`$, $`\chi`$ even) and adding local cross-caps realizes a cofinal family of pairs $`(\chi,e)`$ satisfying
```math
e(F)+2\chi(F)\equiv\mathfrak{P}([F]_2)\pmod 4,
```
cofinal in the sense that every congruence-allowed value of $`e`$ is reached at all sufficiently large non-orientable genus. This is enough for Step 4, which needs existence with controlled congruence data, not a minimal-genus classification. It is the $`W`$-form of the classical congruence (Whitney's $`e\equiv 2h \bmod 4`$ in $`\mathbb{R}^4`$, proved by Massey; the homology-cobordism version is Levine-Ruberman-Strle, Prop. 2.5). For the two values of $`\mathfrak{P}`$ on $`W`$: classes with $`\mathfrak{P}=0`$ (including zero) carry non-orientable surfaces with $`e\equiv 2\chi\equiv 2h \bmod 4`$; the $`120`$ root classes ($`\mathfrak{P}=2`$) carry them with $`e\equiv 2\chi+2 \bmod 4`$. The sharper questions (the minimal genus for given $`(x,e)`$, the full realizable range at fixed genus) are left open here.

**The characteristic slot.** Every non-orientable surface carries normal data; the specific Brown-invariant package of the Guillou-Marin/Rokhlin route (the quadratic enhancement $`q_F:H_1(F;\mathbb{Z}_2)\to\mathbb{Z}_4`$ and its invariant $`\beta(F)`$, the framing defect of orientation-reversing curves, which is where a Möbius band's $`\mathbb{Z}_2`$ normal data lives) attaches to characteristic surfaces. Since $`W`$ is spin, the unique characteristic class is $`0`$ (§1), so the Möbius/normal-twist channel available to that route lives on the $`\mathbb{Z}_2`$-null surfaces, not on the root classes. The closed-manifold congruence is $`\mathrm{sign}(X)=F\cdot F+2\beta(F) \bmod 16`$; the with-boundary version, with the boundary correction for $`\Sigma(2,3,5)`$ (Rokhlin/Neumann-Siebenmann $`\bar\mu`$; Levine-Ruberman-Strle §8 for the $`\rho`$-invariant form), is the designated Step-4 tool and is deliberately not developed here.

## 4. The Galois node, and what cannot see it

The McKay correspondence assigns $`\mathrm{Sym}^2Q'`$ the exceptional curve $`E_8`$: the tip of the multiplicity-$`2`$ arm, the shortest leg, adjacent to the central trivalent curve $`E_5`$. Its integral class has $`\xi\cdot\xi=-2`$; its mod-2 class $`x_{d6}=[E_8]_2`$ pairs nontrivially with exactly one basis class, the central one ($`x_{d6}\cdot[E_5]_2=1`$), so the pair spans a hyperbolic plane. Its refinement is $`\mathfrak{P}(x_{d6})=2`$: **the Galois class is one of the $`120`$ root classes.** So is the class of $`\mathrm{Sym}^2Q`$ ($`E_2`$, on the long arm), and so are all eight curve classes.

Now the structural finding. The Weyl group $`W(E_8)`$ acts transitively on the $`240`$ roots, and the root classes exhaust the $`\mathfrak{P}=2`$ set, so the automorphism group of the pair $`(\text{mod-2 form},\ \mathfrak{P})`$ acts transitively on the $`120`$ root classes:

```math
\boxed{\ \text{the automorphism group of }(H_2(W;\mathbb{Z}_2),\ \cdot\ ,\mathfrak{P})\ \text{is transitive on the }120\ \text{root classes: the interior homology mod }2\ \text{and mod }4\ \text{is Galois-blind.}\ }
```

Equivalently, any invariant depending only on the isomorphism class of the pointed quadratic space $`(H_2(W;\mathbb{Z}_2),\cdot,\mathfrak{P};x)`$ takes the same value for every root-class choice of $`x`$. In particular no mod-2 or mod-4 homological invariant of $`W`$ distinguishes $`[\mathrm{Sym}^2Q']_2`$ from $`[\mathrm{Sym}^2Q]_2`$, or from any other root class. (This is an algebraic statement about invariants of the class within the form; whether a self-diffeomorphism of $`W`$ realizes a given automorphism is a separate question that the blindness claim does not need.) The Galois selection of the distance-six node is carried entirely by the McKay/tautological assignment, the $`c_1(\mathcal{R}_i)`$ of Step 2's framework (KN A.2), not by the raw topology of the class.

**Consequence for Step 4, the sharpened make-or-break.** The two channels the bridge wants to couple sit in different slots of the interior topology:

- the **Möbius channel** (non-orientability, the $`\mathbb{Z}_2`$ normal data $`q_F`$, $`\beta`$) lives on the characteristic class, which is $`0`$;
- the **Galois channel** (the distance-six selection) lives on a root class, and only through the tautological bundle that decorates it, since the class itself is homologically anonymous.

The two slots are disjoint ($`0`$ is isotropic and fixed by everything; the root classes are non-isotropic and mutually equivalent), so the bridge cannot close by identifying the band's class with the Galois class. If it closes, it closes in the index formula: the boundary term (Galois-sensitive through $`\rho_{\mathrm{ad}}`$, Step 1) meeting an interior term that is Galois-sensitive only through $`\mathrm{ch}(\mathcal{R}_{d6})`$ (Step 2), with the Möbius data entering through the characteristic slot's Brown/Guillou-Marin contribution. Step 4's question is whether these three ingredients appear in one identity with nontrivial coefficients, and it inherits from this step exactly the objects to test: the $`0`$-class enhancement $`(q_F,\beta)`$, the root-class geometry of $`x_{d6}`$, and the congruence menu of §3.

**This revises Step 4 as staged.** The bridge note's Step 4 reads as a two-ingredient test: insert the band's homology class into the index formula and read whether its topological contribution couples to the boundary eta. Step 3 shows that formulation cannot run as written, because the band's data and the Galois selection do not share a class: the coupling, if any, is a three-ingredient identity (boundary $`\rho`$, tautological interior term, characteristic-slot Brown term) across two disjoint homological slots plus the bundle decoration. The bar is higher than the staged plan envisioned, and Step 4's feasibility should be assessed against this revised formulation; on filing, the bridge note's Step-4 line should be updated accordingly. By the bridge note's own standard, a negative at this bar is also a result.

## Verdict

The three staged-plan items are computed and closed: $`H_2(W;\mathbb{Z}_2)=\mathbb{Z}_2^8`$ with the $`E_8`$ adjacency form (alternating, nondegenerate, unique characteristic class $`0`$, $`W`$ spin); every class carries non-orientable embedded surfaces, with the invariant menu $`e+2\chi\equiv\mathfrak{P} \bmod 4`$ realized constructively and the Brown/Guillou-Marin data for the characteristic-surface route confined to the zero class; the Galois node is the short-arm curve $`E_8`$, a root class on which the interior homology carries no distinguishing invariant. The structural upshot for Step 4: interior Galois-sensitivity is tautological (McKay bundles), not homological, and the Möbius and Galois channels must be coupled through the index formula or not at all, which revises the staged Step-4 formulation from a two-ingredient to a three-ingredient test (§4). Carried unchanged to Step 4: the Dirac-eta versus odd-signature-$`\rho`$ reconciliation (Step-2 note, §4 handoff) and the K-class verification of the charge-carrying extension (raised in the Step-2 redline record and logged in the computation notes, not in the Step-2 file).

## Sources

- L. Guillou, A. Marin, *Une extension d'un théorème de Rohlin sur la signature* (the characteristic-surface congruence $`\mathrm{sign}=F\cdot F+2\beta \bmod 16`$; Brown invariant).
- W. S. Massey, *Proof of a conjecture of Whitney* (normal Euler numbers of non-orientable surfaces in $`S^4`$; Whitney's congruence $`e\equiv 2h\bmod 4`$).
- A. Levine, D. Ruberman, S. Strle, *Nonorientable surfaces in homology cobordisms*, Geom. Topol. 19 (2015), arXiv:1310.8516 (Prop. 2.5 congruence; §8 $`\rho`$-invariant obstructions; the with-boundary toolkit for Step 4).
- P. B. Kronheimer, H. Nakajima, Math. Ann. 288 (1990), Appendix (tautological bundles and the McKay pairing; Step 2's framework).
- F. van der Blij, *An invariant of quadratic forms mod 8* (the Gauss-sum/signature consistency used in §2).
- Root-system and quadric counts: standard; verified here by reflection closure and exhaustive enumeration ([step3-interior-classes.test.py](scripts/step3-interior-classes.test.py)).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
