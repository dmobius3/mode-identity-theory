<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Step 4 of the postulate bridge, part one: the bookkeeping

**Type:** Result
**State:** Closed
**Status (2026-07-04):** Part one closed: the four bookkeeping items are assembled, with the Degeratu sign caveat applied.
**Summary:** Assembles the index-theoretic bookkeeping for the bridge coupling calculation, part one of Step 4.
**Parent:** `postulate-bridge.md`

Closed (part one of Step 4). The four items carried from Steps 2-3 are closed by exact computation, and the three ingredients of the revised Step 4 now compute in one currency, character sums on $`2I`$: the odd-signature rho is an affine function of the KN Dirac-type sums (the conversion identity, gate value $`-8/5=4\,\Delta D`$); the KN tautological K-class is pinned, its charges reproducing the Step-2 Chern-Simons web mod 1 in all four sectors; the boundary sign convention is pinned ($`\eta_{\mathrm{Dir}}=1079/720`$ on $`+\Sigma`$), triply locked; and $`\bar\mu=-1`$, verified exactly through Ruberman-Saveliev. Part two is resolved in [Step 4, part two](step4-coupling.md): route-specific decoupling, with the gauge dictionary as the positive residue. Numerical claims are exact; the worksheet is [step4-bookkeeping.test.py](scripts/step4-bookkeeping.test.py).

**Related:** [Step 3](step3-interior-classes.md), [Step 2](step2-analytic-setup.md), [η-gatekeeper (Step 1)](eta-gatekeeper.md), [Postulate bridge](postulate-bridge.md).

---

**Goal.** Close the four carried items: (1) reconcile the Dirac-type boundary sums of the Kronheimer-Nakajima formulas with the bridge's odd-signature rho; (2) identify the K-class of the charge-carrying extension; (3) pin the boundary-correction sign convention; (4) pin the $`\bar\mu`$ normalization for the characteristic-slot machinery. All four close, and more tightly than expected: the four quantities turn out to compute in a single currency, the character sums
```math
D_W \;=\; \frac{1}{120}\sum_{1\neq g\in 2I}\frac{\chi_W(g)}{2-\chi_Q(g)},
```
so the three ingredients of the revised Step 4 now share one exact-arithmetic language. Every number below is an exact rational verified by the worksheet ([step4-bookkeeping.test.py](scripts/step4-bookkeeping.test.py)); nothing is floating-point.

**Conventions.** Orientation $`+\Sigma`$ (link = quotient = resolution boundary; Step 2's dictionary). $`2-\chi_Q(g)=4\sin^2(\phi_g/2)`$ with $`\phi_g`$ the defining-representation angle, so every $`D_W`$ is a positive-denominator character sum; the values used below are
```math
D_{\mathrm{triv}}=\tfrac{1079}{1440},\quad D_Q=\tfrac{73}{144},\quad D_{Q'}=-\tfrac{67}{720},\quad D_{\mathrm{ad}Q}=\tfrac{9}{32},\quad D_{\mathrm{ad}Q'}=-\tfrac{19}{160}.
```
By KN (A.2) with one factor trivial, $`D_W=\int_X \mathrm{ch}(\mathcal{R}_W)\hat{A}`$: the same sums are simultaneously boundary data and interior Chern-Weil integrals. That double role is what unifies the bookkeeping.

## 1. Item 1: the conversion identity (Dirac-type sums determine the odd-signature rho)

The two boundary invariants weight the same group elements differently: the $`G`$-signature defect uses $`\pm\cot^2(\phi/2)`$ (orientation-dependent), the Dirac-type sums use $`1/(2-\chi_Q)=1/(4\sin^2(\phi/2))`$. These are not independent. On $`X_{+1}=-\Sigma`$ the defect is $`-\cot^2(\phi/2)=1-\frac{4}{2-\chi_Q}`$ (Step 1's convention); reversing orientation to $`+\Sigma`$ flips the sign, so the $`+\Sigma`$ defect is
```math
+\cot^2(\phi/2)\;=\;-1+\frac{4}{2-\chi_Q},
```
and summing against $`\chi_\alpha-\dim\alpha`$ with character orthogonality ($`\sum_{g\neq 1}\chi_\alpha(g)=-\dim\alpha`$ when $`\alpha`$ contains no trivial constituent) gives, for every representation with no trivial constituent,
```math
\boxed{\ \rho^{\mathrm{sign}}_\alpha(+\Sigma)\;=\;\dim\alpha\;+\;4\bigl(D_\alpha-\dim\alpha\cdot D_{\mathrm{triv}}\bigr)\ }
```
(on $`X_{+1}`$ both sides flip sign). The no-trivial-constituent hypothesis is sharp: for $`\alpha=\beta\oplus\mathbf{1}`$ the left side equals $`\rho_\beta`$ while the right side gains the trivial multiplicity as an additive offset (checked: $`\alpha=Q\oplus\mathbf{1}`$ gives offset exactly $`1`$). Verified on all four representations:

| $`\alpha`$ | $`\dim+4(D_\alpha-\dim D_{\mathrm{triv}})`$ | known $`\rho^{\mathrm{sign}}_\alpha(+\Sigma)`$ |
|---|---|---|
| $`Q`$ | $`-59/30`$ | $`-59/30`$ (BHKK's printed $`59/30`$ on $`X_{+1}`$) |
| $`Q'`$ | $`-131/30`$ | $`-131/30`$ (BHKK's printed $`131/30`$ on $`X_{+1}`$) |
| $`\mathrm{ad}\,Q`$ | $`-73/15`$ | $`-73/15`$ (Steps 1-2) |
| $`\mathrm{ad}\,Q'`$ | $`-97/15`$ | $`-97/15`$ (Steps 1-2) |

So the reconciliation is an equation, not a dictionary: the Dirac-type sums that the KN index formula uses **determine** the odd-signature rho for flat twists on $`S^3/\Gamma`$, and conversely. Two corollaries:

- Since the dimensions agree, differences obey $`\Delta\rho^{\mathrm{sign}}=4\,\Delta D`$: the Step-1 gate value is $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=4\,(D_{\mathrm{ad}Q'}-D_{\mathrm{ad}Q})=4\cdot(-\tfrac{2}{5})=-\tfrac{8}{5}`$ on $`+\Sigma`$. The boundary Galois asymmetry is visible in the KN currency as $`-2/5`$, and it is golden-sourced here too: the golden classes contribute $`+48`$ to the $`D_{\mathrm{ad}Q}`$ sum and cancel exactly in $`D_{\mathrm{ad}Q'}`$, the rational-class totals being identical ($`-57/4`$ each, times $`1/120`$).
- The factor $`4`$ here is trigonometric ($`\csc^2=4/(2-\chi_Q)`$), not the Dynkin index $`4`$ of Step 1's CS chain; the two fours have different origins and should not be conflated.

*Remark (the defining node).* For $`\alpha=Q`$ one also has the polynomial identity $`\chi_{\mathrm{ad}Q}=\chi_Q^2-1=(2-\chi_Q)(-2-\chi_Q)+3`$, whence $`D_{\mathrm{ad}Q}-3D_{\mathrm{triv}}=-\tfrac{1}{120}\sum_{g\neq 1}(2+\chi_Q(g))=-\tfrac{59}{30}`$: the same number as $`\rho^{\mathrm{sign}}_Q(+\Sigma)`$. That coincidence is special to the node whose representation angles equal the tangential angles; it fails for $`Q'`$ ($`-131/30`$ versus $`-71/30`$), and the failure gap is exactly $`2`$.

## 2. Item 2: the KN tautological K-class

KN Proposition 2.2 supplies the canonical tautological extension for each flat $`\Gamma`$-module: each $`\mathcal{R}_i`$ carries a canonical finite-action anti-self-dual connection whose flat limit at infinity is $`R_i`$. So for the flat module $`\mathrm{ad}\,Q'=\mathrm{Sym}^2Q'`$, the tautological Dirac calculation uses $`\mathcal{R}_{d6}`$, and the candidate $`(A.1)`$-type interior term of the Step-2 handoff is the honest one. This closes the K-class for the KN currency used here; if part two instead writes a gauge-deformation complex built from a rank-2 instanton and then takes adjoints, that complex's K-class ($`\mathrm{Sym}^2`$ of the rank-2 extension, a trace-free endomorphism construction, or a compactly-supported difference) must still be checked separately. (Discharged by part two for the $`F`$-localized coupling question: any coefficient built on $`W`$ restricts rank-trivially on the characteristic slot; see [Step 4, part two](step4-coupling.md).) Its charge data, with $`k_i:=\int_X(c_2-\tfrac{1}{2}c_1^2)(\mathcal{R}_i)=\mathrm{rk}_i\,D_{\mathrm{triv}}-D_i`$:

| bundle | rank | charge $`k`$ | $`k \bmod 1`$ | $`cs`$ of flat limit mod 1 ($`+\Sigma`$, Step 2) |
|---|---|---|---|---|
| $`\mathcal{R}_Q`$ | 2 | $`119/120`$ | $`119/120`$ | $`-1/120\equiv 119/120`$ |
| $`\mathcal{R}_{Q'}`$ | 2 | $`191/120`$ | $`71/120`$ | $`-49/120\equiv 71/120`$ |
| $`\mathcal{R}_{d2}`$ ($`\mathrm{ad}Q`$) | 3 | $`59/30`$ | $`29/30`$ | $`4\cdot(-1/120)\equiv 29/30`$ |
| $`\mathcal{R}_{d6}`$ ($`\mathrm{ad}Q'`$) | 3 | $`71/30`$ | $`11/30`$ | $`4\cdot(-49/120)\equiv 11/30`$ |

**All four satisfy $`k\equiv cs \bmod 1`$** on $`+\Sigma`$: the fractional instanton charge of the extension equals the Chern-Simons invariant of its flat limit, across the whole family. This ties Step 2's CS web to the interior Chern-Weil data numerically, in both sectors. Two exact (not just mod-1) echoes, stated with their signs: $`k(\mathcal{R}_Q)-k(\mathcal{R}_{Q'})=D_{Q'}-D_Q=-\tfrac{72}{120}=\tfrac{\varepsilon(H)}{\lvert\Gamma\rvert}=-\tfrac{3}{5}`$, matching Helle's $`cs(Q)-cs(Q')=\varepsilon(H)/\lvert\Gamma\rvert`$ from Step 1's Appendix A with the same sign, as an exact identity; and $`k(\mathcal{R}_{d6})-k(\mathcal{R}_{d2})=+\tfrac{2}{5}`$, the representative of $`cs(\mathrm{ad}Q')-cs(\mathrm{ad}Q) \bmod 1`$.

## 3. Item 3: the boundary sign convention, pinned

On the compact truncation $`W`$ with outward normal and $`\partial W=+\Sigma`$, the APS form used from here on is
```math
\mathrm{ind}\,D \;=\;\int_W \hat{A}\,\mathrm{ch}(E)\;-\;\tfrac{1}{2}\bigl(h+\eta\bigr)(\partial W),
```
and the convention is not a choice left open: applying it to the trivial bundle, where KN (A.1) forces the $`L^2`$-index to vanish and $`h=0`$ for the boundary Dirac operator on the spherical space form (positive scalar curvature and Lichnerowicz; the ALE interior is scalar-flat, so the vanishing is a boundary statement), yields
```math
\eta_{\mathrm{Dir}}(+\Sigma)\;=\;2\,D_{\mathrm{triv}}\;=\;\tfrac{1079}{720},
```
an exact value with the denominator $`720`$ dividing pattern familiar from equivariant eta computations on this space. Any other sign assignment breaks the (A.1)/(A.2) internal consistency.

*Remark (an independent corroboration).* The APS signature theorem on the truncation, $`\mathrm{sign}(W)=\tfrac{1}{3}\int_W p_1-\eta_{\mathrm{Sign}}(\partial W)`$, gives $`\int_W\hat{A}=-\tfrac{1}{24}\int p_1=-\tfrac{1}{8}\bigl(\mathrm{sign}+\eta_{\mathrm{Sign}}\bigr)=1-\tfrac{361}{1440}=\tfrac{1079}{1440}=D_{\mathrm{triv}}`$, using only the signature theorem and the untwisted signature eta of §4, independent of KN. The convention web is therefore triply locked: KN internal consistency, the signature route, and the Ruberman-Saveliev identity below all force the same $`\eta_{\mathrm{Dir}}`$. (Degeratu's Molien-series formulas agree exactly: her direct group sum, Cor. 2.4 with the half-determinant trivial for $`\Gamma\subset\mathrm{SU}(2)`$ by her Cor. 3.3, gives $`\eta_{\mathrm{Dir},\chi}=+2D_\chi`$ at $`n=2`$ on the boundary-at-infinity orientation, the same convention as here with no sign flip.)

## 4. Item 4: $`\bar\mu`$, pinned and absorbed into the same currency

In the Neumann normalization $`\bar\mu(\Sigma)=\tfrac{1}{8}\bigl(\mathrm{sign}(X)-w\cdot w\bigr)`$ (integer-valued, reducing mod 2 to Rokhlin), the even $`E_8`$ plumbing has Wu class $`w=0`$, so
```math
\bar\mu(\Sigma(2,3,5))=-1,
```
and the $`E_8`$ filling saturates the Fukumoto-Furuta-Ue bound $`b_2(Y)\le -8\bar\mu`$ for negative-definite spin fillings ($`8\le 8`$). Better: Ruberman-Saveliev (arXiv:1009.3201, Thm 1.1) prove, on exactly our orientation (link of the singularity) and geometry,
```math
\tfrac{1}{2}\eta_{\mathrm{Dir}}(\Sigma)+\tfrac{1}{8}\eta_{\mathrm{Sign}}(\Sigma)=-\bar\mu(\Sigma).
```
With $`\eta_{\mathrm{Dir}}(+\Sigma)=\tfrac{1079}{720}`$ from item 3 and the untwisted signature eta computed from the same class data, $`\eta_{\mathrm{Sign}}(+\Sigma)=\tfrac{1}{120}\sum_{g\neq 1}\cot^2(\phi_g/2)=\tfrac{361}{180}`$:
```math
\tfrac{1}{2}\cdot\tfrac{1079}{720}+\tfrac{1}{8}\cdot\tfrac{361}{180}=\tfrac{1079+361}{1440}=1=-\bar\mu \quad\checkmark
```
The check is sharp: of the four sign combinations of the two etas, only the matched pairs give integers ($`+,+\Rightarrow 1`$ on $`+\Sigma`$; $`-,-\Rightarrow -1`$, the $`-\Sigma`$ statement, consistent with $`\bar\mu(-Y)=-\bar\mu(Y)`$); the mixed pairs give $`\pm 359/720`$. So the convention web of items 3 and 4 is over-determined and locks, and $`\bar\mu`$, the normalizer of the characteristic-slot congruence, is itself an exact combination of the same character sums.

## 5. The unified currency, and the computation this unblocks

Everything the revised Step 4 needs, except one item, is now a closed-form rational in the single currency of character sums on $`2I`$:

| ingredient | quantity | value on $`+\Sigma`$ |
|---|---|---|
| A (boundary, Galois) | $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=4\,\Delta D`$ | $`-8/5`$ |
| B (interior, Galois) | charges $`k(\mathcal{R}_{d2})`$, $`k(\mathcal{R}_{d6})`$; $`\Delta k`$ | $`59/30`$, $`71/30`$; $`2/5`$ |
| C (characteristic slot, normalizer) | $`\bar\mu`$ via $`\tfrac12\eta_{\mathrm{Dir}}+\tfrac18\eta_{\mathrm{Sign}}`$ | $`-1`$ |

The one ingredient that is *not* a character sum is the surface itself: the pair $`(e(F),\beta(F))`$ of an actual characteristic (i.e. $`\mathbb{Z}_2`$-null) non-orientable surface $`F\subset W`$, constrained by the congruence menu of Step 3 and normalized by $`\bar\mu`$ through the with-boundary Guillou-Marin machinery. Step 4's main computation is now precisely posed: determine whether there is an identity in which the boundary Galois asymmetry ($`\Delta\rho=-8/5`$, equivalently $`\Delta D=-2/5`$), the interior tautological data ($`k(\mathcal{R}_{d6})`$, $`\mathrm{ch}(\mathcal{R}_{d6})`$), and the surface data ($`e(F)`$, $`\beta(F)`$, anchored by $`\bar\mu=-1`$) appear together with nontrivial coefficients, or prove route-specifically that the characteristic slot decouples from the tautological one. That computation, and its verdict either way, is part two.

## Verdict

All four carried items are closed. Item 1 closes as a theorem-grade identity: the odd-signature rho is an affine function of the Dirac-type sums, so the bridge's boundary invariant and the KN index currency are inter-translatable, with the gate value $`-8/5`$ equal to $`4\Delta D`$. Item 2 closes for the KN currency used here: the tautological extension is canonical, its charges reproduce the Step-2 Chern-Simons web mod 1 in all four sectors, and the $`\varepsilon(H)=-72`$ augmentation reappears exactly; the K-class of any gauge-deformation complex part two may write remains its own check. Item 3 is pinned by internal consistency ($`\eta_{\mathrm{Dir}}=1079/720`$), item 4 by the Neumann normalization ($`\bar\mu=-1`$) and verified through the Ruberman-Saveliev identity, which lands exactly on $`1`$ and locks the whole sign web. Part two, the coupling identity itself, is unblocked and precisely posed.

## Sources

- P. B. Kronheimer, H. Nakajima, Math. Ann. 288 (1990) (Prop. 2.2: tautological ASD connections with flat limits; (A.1), (A.2)).
- H. U. Boden, C. M. Herald, P. Kirk, E. Klassen, arXiv:math/9908020 (the printed canonical-representation rho values $`59/30`$, $`131/30`$ re-derived here from the conversion identity).
- D. Ruberman, N. Saveliev, *The $`\bar\mu`$-invariant of Seifert fibered homology spheres and the Dirac operator*, arXiv:1009.3201 (Thm 1.1, the $`\tfrac12\eta_{\mathrm{Dir}}+\tfrac18\eta_{\mathrm{Sign}}=-\bar\mu`$ identity; link orientation).
- W. Neumann; L. Siebenmann ($`\bar\mu`$ and its plumbing definition); Y. Fukumoto, M. Furuta, M. Ue (the $`b_2\le-8\bar\mu`$ bound for spin fillings).
- Atiyah, Patodi, Singer I-II (the index form with $`(h+\eta)/2`$; the $`G`$-signature defect).
- A. Degeratu, *Eta-invariants from Molien series*, Q. J. Math. 60 (2009) (Cor. 2.4, Cor. 3.3: the direct group-sum eta formula; at $`n=2`$ it reads $`\eta_{\mathrm{Dir},\chi}=+2D_\chi`$ on the same orientation as §3).
- Worksheet: [step4-bookkeeping.test.py](scripts/step4-bookkeeping.test.py) (all sums exact in $`\mathbb{Q}(\sqrt5)`$, surds cancelling).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
