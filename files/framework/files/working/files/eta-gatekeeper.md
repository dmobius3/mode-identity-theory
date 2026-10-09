<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The η-gatekeeper: $`Q`$ versus $`Q'`$ on $`S^3/2I`$

**Type:** Test
**State:** Closed
**Verdict:** Positive
**Status (2026-07-01):** Step 1 closed: the boundary spectral asymmetry $`\rho_{\mathrm{ad}Q'} - \rho_{\mathrm{ad}Q} = -8/5`$ is nonzero and Galois-sourced, so the gate opens and Steps 2-4 proceed.
**Summary:** Computes the odd-signature rho-invariant difference between the Galois-conjugate flat connections Q and Q' on S³/2I, the Step-1 gate the bridge must clear.
**Inputs:** `../../bedrock/files/galois-pair.md`, BHKK (arXiv:math/9908020)
**Parent:** `postulate-bridge.md`
**Frozen:** 2026-07-01 the convention block (the rho normalization, fixed before computing)

Step 1 of the postulate-bridge staged plan, closed; gate open. The boundary rho difference is $`8/5`$ in magnitude, nonzero and Galois-sourced. Step 2 fixes the orientation: on the resolution boundary, $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$, and the magnitude $`73/15`$ is now anchored in print (BHKK); see [Step 2](step2-analytic-setup.md). The interior classes are computed in [Step 3](step3-interior-classes.md); the coupling question is resolved in [Step 4](step4-coupling.md) (route-specific split: gauge dictionary proved, Möbius channel decoupled).

**Related:** [Galois pair](../../bedrock/files/galois-pair.md) (the published pillar), [Postulate bridge](postulate-bridge.md), [First eigenvalue](../../bedrock/files/first-eigenvalue.md), [Coexact gap](../../bedrock/files/coexact-gap.md).

---

**Goal.** Decide whether the boundary carries a nonzero, connection-sensitive spectral asymmetry separating $`Q`$ from its Galois conjugate $`Q'`$, sourced by the same $`\mathbb{Q}(\sqrt5)`$ arithmetic that makes the coexact gap $`36/R^2`$ rather than $`4/R^2`$. Boundary-only, independent of the filling. A zero or Galois-blind answer stops the program.

> **Convention (fixed before computing).** $`\rho_\alpha`$ is the APS odd-signature rho invariant in the **unreduced** normalization $`\rho_\alpha=\eta_\alpha-\dim(\alpha)\,\eta_{\mathrm{triv}}`$. Orient $`\Sigma(2,3,5)`$ **as the boundary $`\partial W`$ of the $`E_8`$ plumbing** chosen in Step 2 (not merely the Seifert orientation), with the APS II sign of the $`G`$-signature defect; the sign of the answer is fixed by that choice and is what Step 4 reads as match-or-oppose. Under the reduced convention $`\bar\eta=(\eta+h)/2`$ (here $`h=0`$, so $`\bar\eta=\eta/2`$), every rho difference below is halved. The magnitude and the golden-class support are independent of the orientation choice.

## 1. The object

$`M=S^3/2I=\Sigma(2,3,5)`$, round radius $`R`$, $`2I`$ acting by left translation. The irreducible flat $`\mathrm{SU}(2)`$ connections are the two $`2`$-dimensional irreps: the defining $`Q`$ (McKay distance $`1`$) and its Galois conjugate $`Q'`$ (distance $`7`$). Both are isolated and nondegenerate (Fintushel-Stern), so the adjoints $`\mathrm{ad}_Q,\mathrm{ad}_{Q'}`$ are acyclic ($`H^0=H^1=0`$); complexified, $`\mathrm{ad}_\rho\cong\mathrm{Sym}^2\rho`$, the $`3`$-dimensional irreps at distances $`2`$ and $`6`$ (the coexact gap is the squared McKay distance over $`R^2`$: $`4/R^2`$ for $`\mathrm{ad}_Q`$, $`36/R^2`$ for $`\mathrm{ad}_{Q'}`$).

The primary invariant is the APS odd-signature rho invariant $`\rho_{\mathrm{ad}\rho}(M)`$, the boundary quantity the index theorem on $`W`$ requires in Step 4.

> **Remark (relation to the adjoint curl $`\ast d_\nabla`$).** The odd signature operator acts on $`\Omega^0\oplus\Omega^1(M;\mathrm{ad})`$. Acyclicity removes the harmonic representatives ($`h=0`$), not the exact spectral ladder: the exact $`1`$-forms $`d_\nabla f`$ still carry the positive twisted-function spectrum. That sector is invisible to the spectral asymmetry. (For $`\Delta_\nabla f=\lambda f`$, $`\lambda>0`$, the operator exchanges $`(f,0)`$ and $`(0,\,d_\nabla f/\sqrt\lambda)`$ with opposite signs, so its eigenvalues on that pair are $`\pm\sqrt\lambda`$, which cancel in the signed count.) The asymmetry lives entirely on the coexact sector, where the operator restricts to $`\ast d_\nabla`$ with signed spectrum $`\pm m/R`$; so $`\eta(\text{odd signature})=\eta(\ast d_\nabla\ \text{coexact})`$, and with $`h=0`$ this is $`\rho`$.

## 2. The tool

For flat unitary $`\alpha`$ on $`S^3/\Gamma`$, $`\Gamma\subset\mathrm{SU}(2)`$ acting through the defining representation, the APS II $`G`$-signature defect gives
```math
\rho_\alpha(S^3/\Gamma)=\frac{1}{\lvert\Gamma\rvert}\sum_{1\neq g\in\Gamma}\bigl(\chi_\alpha(g)-\dim\alpha\bigr)\,\cot\tfrac{\theta_1(g)}{2}\cot\tfrac{\theta_2(g)}{2},
```
with $`g`$ having defining eigenvalues $`e^{\pm i\phi}`$, so $`\theta_1=\phi,\theta_2=-\phi`$ and per-element defect $`-\cot^2\tfrac{\phi}{2}`$ (the opposite boundary orientation, or the opposite APS defect convention, flips this factor's sign; that flip is exactly the overall sign, fixed in [Step 2](step2-analytic-setup.md) to $`-8/5`$ on the resolution boundary). Only the difference is needed; $`\dim=3`$ for both, so the $`\dim\alpha`$ term cancels:
```math
\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=\frac{1}{120}\sum_{1\neq g}\bigl(\chi_{\mathrm{Sym}^2Q'}(g)-\chi_{\mathrm{Sym}^2Q}(g)\bigr)\Bigl(-\cot^2\tfrac{\phi_g}{2}\Bigr).
```

## 3. Character input

$`\chi_{\mathrm{Sym}^2Q}=\chi_Q^2-1=1+2\cos 2\phi`$; $`\chi_{\mathrm{Sym}^2Q'}=\sigma(\chi_{\mathrm{Sym}^2Q})`$, $`\sigma:\sqrt5\mapsto-\sqrt5`$; $`\varphi=\tfrac{1+\sqrt5}{2}`$.

| $`\phi`$ | order | $`\lvert C\rvert`$ | $`\chi_Q`$ | $`\chi_{\mathrm{Sym}^2Q}`$ | $`\chi_{\mathrm{Sym}^2Q'}`$ | $`\Delta`$ |
|---|---|---|---|---|---|---|
| $`0`$ | 1 | 1 | $`2`$ | $`3`$ | $`3`$ | $`0`$ |
| $`\pi`$ | 2 | 1 | $`-2`$ | $`3`$ | $`3`$ | $`0`$ |
| $`\pi/2`$ | 4 | 30 | $`0`$ | $`-1`$ | $`-1`$ | $`0`$ |
| $`2\pi/3`$ | 3 | 20 | $`-1`$ | $`0`$ | $`0`$ | $`0`$ |
| $`\pi/3`$ | 6 | 20 | $`1`$ | $`0`$ | $`0`$ | $`0`$ |
| $`\pi/5`$ | 10 | 12 | $`\varphi`$ | $`\varphi`$ | $`-1/\varphi`$ | $`-\sqrt5`$ |
| $`2\pi/5`$ | 5 | 12 | $`1/\varphi`$ | $`-1/\varphi`$ | $`\varphi`$ | $`+\sqrt5`$ |
| $`3\pi/5`$ | 10 | 12 | $`-1/\varphi`$ | $`-1/\varphi`$ | $`\varphi`$ | $`+\sqrt5`$ |
| $`4\pi/5`$ | 5 | 12 | $`-\varphi`$ | $`\varphi`$ | $`-1/\varphi`$ | $`-\sqrt5`$ |

($`\Delta=\chi_{\mathrm{Sym}^2Q'}-\chi_{\mathrm{Sym}^2Q}`$.) Supported entirely on the four golden ($`\sqrt5`$) classes; the five rational classes cancel.

## 4. The computation

Each golden class has $`12`$ elements, $`\phi/2\in\{\pi/10,\pi/5,3\pi/10,2\pi/5\}`$:
```math
\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=\frac{12}{120}\sqrt5\Bigl[\cot^2\tfrac{\pi}{10}-\cot^2\tfrac{\pi}{5}-\cot^2\tfrac{3\pi}{10}+\cot^2\tfrac{2\pi}{5}\Bigr].
```
With $`\cot^2\tfrac{\pi}{10}=5+2\sqrt5`$, $`\cot^2\tfrac{\pi}{5}=1+\tfrac{2}{\sqrt5}`$, $`\cot^2\tfrac{3\pi}{10}=5-2\sqrt5`$, $`\cot^2\tfrac{2\pi}{5}=1-\tfrac{2}{\sqrt5}`$, the bracket is $`\tfrac{16\sqrt5}{5}`$, so
```math
\boxed{\ \rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=\frac{\sqrt5}{10}\cdot\frac{16\sqrt5}{5}=\frac{8}{5}\quad(\text{unreduced};\ 4/5\ \text{reduced})\ }
```
The $`\sqrt5`$ cancels in the class sum, leaving the rational $`8/5`$, as expected for this finite-image spherical calculation.

## 5. Reading

- **Nonzero.** The boundary asymmetry distinguishes $`Q`$ from $`Q'`$.
- **Galois-sourced.** The whole difference comes from the four $`\sqrt5`$-classes, the locus of the automorphism sending $`\mathrm{Sym}^2Q`$ (distance $`2`$, gap $`4/R^2`$) to $`\mathrm{Sym}^2Q'`$ (distance $`6`$, gap $`36/R^2`$).
- **Not the same invariant as the gap.** Rho is signed asymmetry; the gap is first absolute occurrence. Both are sensitive to the same Galois separation between $`\mathrm{Sym}^2Q`$ and $`\mathrm{Sym}^2Q'`$; neither computes the other.
- **Denominator $`5`$.** Consistent with the contribution being supported on the order-$`5`$ / order-$`10`$ classes.

## 6. Normalization check (closed; orientation sign fixed in Step 2)

The magnitude and the reduced/unreduced normalization are validated against $`\Sigma(2,3,5)`$ data by an independent route (Appendix A). This is a mod-$`\mathbb Z`$ test, insensitive to the overall sign.

Helle (Ex. B.15) gives $`cs(Q)=-1/120`$; solving $`(2-Q)H=Q-Q'`$ on the affine $`E_8`$ graph gives the augmentation $`\varepsilon(H)=\langle H,\delta\rangle=-72`$ ($`H`$ is virtual, so this is a signed count, not a dimension), whence $`cs(Q)-cs(Q')=-72/120=-3/5\equiv 2/5\pmod{\mathbb Z}`$ (so $`cs(Q')=-49/120`$). By the adjoint/fundamental Dynkin index $`T(\mathrm{adj})/T(\mathrm{fund})=4`$, the adjoint CS difference is $`4\cdot(-3/5)=-12/5\equiv 3/5\pmod{\mathbb Z}`$. The relation $`\rho\equiv cs(\mathrm{ad})\pmod{\mathbb Z}`$ compares this residue class with the $`G`$-signature value from §4, whose residue is $`8/5\equiv 3/5`$: they agree.

Precisely what this fixes:
- **Supports the unreduced normalization** (under the stated APS/CS convention). The reduced value $`4/5\equiv 4/5`$ does not match $`3/5`$; only the unreduced $`8/5\equiv 3/5`$ does. Treat this as a mod-$`\mathbb Z`$ consistency check, not the source of the real value $`8/5`$.
- **Does not determine the real number.** $`8/5`$ is the $`G`$-signature result (§4) alone; the CS route fixes only the residue class $`3/5\pmod{\mathbb Z}`$, not the real constant relating $`\rho`$ to CS. (The apparent real coincidence "$`8/5=8/5`$" comes from choosing the $`2/5`$ representative before multiplying by $`4`$; the $`-3/5`$ representative gives $`-12/5`$, the same class.)
- **Sign-insensitive.** The chain compares $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}`$ with $`cs(\mathrm{ad}Q)-cs(\mathrm{ad}Q')`$ in opposite order; mod $`\mathbb Z`$ these are the same class, so the flip is invisible and silently carries the $`\rho`$-to-$`cs`$ sign, which is exactly the residual below.

The Floer gradings $`1,5\bmod 8`$ are consistent (two distinct connections). **Sign (fixed in Step 2):** orienting $`\Sigma(2,3,5)`$ as $`\partial W`$ of the minimal resolution gives $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$; the $`+8/5`$ above is the reversed ($`X_{+1}=-\Sigma`$) orientation, and the $`73/15`$ magnitude is anchored in print (BHKK, spectral-flow integrality). See [Step 2](step2-analytic-setup.md).

## Verdict: the gate is open

The $`G`$-signature computation gives $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=8/5`$ in magnitude (unreduced APS odd-signature normalization); Step 2 fixes the sign to $`-8/5`$ on the resolution-boundary orientation. The difference is nonzero and supported entirely on the golden conjugacy classes. The CS/McKay computation independently matches the residue class $`3/5\pmod{\mathbb Z}`$ under the stated APS/CS convention, supporting the normalization (Appendix A). The Step-1 gate is open, and Steps 2-3 (framework, sign, interior classes) are done; the coupling identity, revised by [Step 3](step3-interior-classes.md) to a three-ingredient test, remains Step 4.

## Appendix A. Fundamental Chern-Simons via the affine $`E_8`$ solve

Helle, Example B.15: for any finite $`\Gamma\subset\mathrm{SU}(2)`$ the canonical (defining) connection has $`cs(Q)=-1/\lvert\Gamma\rvert`$ (orientation reversal flips the sign), so $`cs(Q)=-1/120`$ on $`2I`$. Proposition B.16: for two connections, $`cs(\alpha)-cs(\beta)=\varepsilon(H)/\lvert\Gamma\rvert`$, where $`\varepsilon(H)=\langle H,\delta\rangle`$ is the augmentation (the honest dimension when $`H`$ is an actual representation) and $`(2-Q)H=\alpha-\beta`$ in $`R(\Gamma)`$.

Multiplication by $`Q=V_1`$ is the McKay adjacency $`A`$, so $`(2-Q)\cdot=(2I-A)`$ on the affine $`E_8`$ graph. Index the $`9`$ nodes by McKay distance with Coxeter marks $`\delta=(1,2,3,4,5,6,4,2,3)`$; edges $`0\!-\!1\!-\!2\!-\!3\!-\!4\!-\!5\!-\!6\!-\!7`$ and the branch $`5\!-\!8`$. $`Q`$ is the mark-$`2`$ node at distance $`1`$ (node $`1`$), $`Q'`$ the mark-$`2`$ node at distance $`7`$ (node $`7`$). Solvability: $`\langle e_1-e_7,\delta\rangle=2-2=0`$.

Solving $`(2I-A)H=e_1-e_7`$ with gauge $`h_0=0`$:
```math
H=(h_0,\dots,h_8)=(0,\,0,\,-1,\,-2,\,-3,\,-4,\,-3,\,-2,\,-2).
```
(Back-substitution is forced; the node-$`7`$ equation checks: $`2(-2)-(-3)=-1`$.) Then
```math
\varepsilon(H)=\langle H,\delta\rangle=-3-8-15-24-12-4-6=-72\quad(\text{signed; }H\text{ is virtual}),
```
```math
cs(Q)-cs(Q')=\frac{-72}{120}=-\frac35\equiv\frac25\pmod{\mathbb Z},\qquad cs(Q')=-\frac{1}{120}+\frac{72}{120}=\frac{71}{120}\equiv-\frac{49}{120}.
```

The consistency check is three residues mod $`\mathbb Z`$, kept separate so the agreement is not read as a real-number coincidence:
1. **Fundamental CS difference:** $`cs(Q)-cs(Q')=-3/5\equiv 2/5`$.
2. **Adjoint index ($`\times 4`$):** $`cs(\mathrm{ad}Q)-cs(\mathrm{ad}Q')\equiv 4\cdot(-3/5)\equiv 3/5`$.
3. **Rho residue:** the $`G`$-signature value $`8/5\equiv 3/5`$.

The three agree mod $`\mathbb Z`$; the real number $`8/5`$ is claim 3's alone.

## Sources

- G. O. Helle, *Equivariant instanton Floer homology and calculations for the binary polyhedral spaces*, arXiv:2203.09471 (Ex. B.15, Prop. B.16; Chern-Simons $`=`$ second Chern class of the holonomy representation).
- R. Fintushel and R. Stern, *Instanton homology of Seifert fibred homology three spheres*, Proc. LMS (3) 61 (1990) (isolated nondegenerate flat connections; the $`R`$-invariant).
- M. Hedden and P. Kirk, *Chern-Simons invariants, SO(3) instantons, and Z/2-homology cobordism*, arXiv:1009.5365 (APS rho / Chern-Simons in the SO(3) instanton setting; used here only for the mod-$`\mathbb Z`$ relation, the precise real-valued constant is not quoted and is not needed for this test).
- Atiyah, Patodi, Singer, *Spectral asymmetry and Riemannian geometry II* (the $`G`$-signature defect / rho invariant of spherical space forms).
- Floer gradings $`1,5\bmod 8`$ for $`\Sigma(2,3,5)`$: standard (instanton Floer homology of the Poincaré sphere is $`\mathbb{Z}_{(1)}\oplus\mathbb{Z}_{(5)}`$).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
