<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Step 2 of the postulate bridge: the analytic setup and the sign

**Type:** Result
**State:** Closed
**Status (2026-07-01):** The analytic framework is fixed (ALE instanton on the minimal resolution of C²/2I, Kronheimer-Nakajima; the orbifold cone a consistency check). The distance-six coefficient the bridge needs is set up here, not proved; that is Step 3's target.
**Summary:** Fixes the analytic setup for the postulate-bridge coupling calculation: the ALE filling, the tautological-bundle basis, and the rho-invariant conventions the later steps compute in.
**Inputs:** `eta-gatekeeper.md`, BHKK (arXiv:math/9908020), Kronheimer-Nakajima, Nakajima, Fintushel-Stern
**Parent:** `postulate-bridge.md`

Closed. The analytic framework is fixed (ALE instanton on the minimal resolution of $`\mathbb{C}^2/2I`$, Kronheimer-Nakajima; the orbifold cone is a consistency check only), and the orientation is resolved: on the resolution-boundary orientation $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$, with the magnitude $`73/15`$ anchored in print (BHKK). The Step-1 gate conclusion is unchanged; [Step 3](step3-interior-classes.md) is closed (interior classes computed, Galois-blind) and Step 4 is complete ([part one](step4-bookkeeping.md), [part two](step4-coupling.md): route-specific split).

**Related:** [η-gatekeeper (Step 1)](eta-gatekeeper.md), [Postulate bridge](postulate-bridge.md), [Coexact gap](../../bedrock/files/coexact-gap.md).

---

**Goal.** Step 1 left two items to the filling. First, the analytic framework: $`W`$ is simply connected, so the flat $`Q'`$ on $`\partial W`$ does not extend flatly, and the extension scheme decides which index formula Steps 3 and 4 write. Second, the sign: the Step-1 difference $`8/5`$ was computed in a convention whose orientation was deferred. Both are settled here. The framework is the ALE instanton setting of Kronheimer-Nakajima on the minimal resolution, with the orbifold cone as a consistency check rather than a vehicle. The sign: on the resolution-boundary orientation, $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$; Step 1's $`+8/5`$ lives on the reversed orientation. The Step-1 gate conclusion (nonzero, Galois-sourced) is orientation-independent and unchanged.

**Convention box (the orientation dictionary).** Write $`+\Sigma`$ for $`\Sigma(2,3,5)`$ with its standard orientation. Four descriptions agree: the link of the $`E_8`$ singularity $`\mathbb{C}^2/2I`$; the Brieskorn orientation of $`\{x^2+y^3+z^5=0\}\cap S^5`$; the quotient orientation of $`S^3/2I`$ from the standard $`S^3\subset\mathbb{C}^2`$; and the boundary of the minimal resolution $`\widetilde{X}\to\mathbb{C}^2/2I`$, whose intersection form is the negative definite $`E_8`$ (eight $`(-2)`$-curves, the Gompf-Stipsicz "(negative) $`E_8`$-plumbing"). The Boden-Herald-Kirk-Klassen Poincaré sphere $`X_{+1}`$ ($`+1`$ surgery on the right-hand trefoil) is $`-\Sigma`$: "as oriented manifolds, $`X_k\cong-\Sigma(2,q,2qk-1)`$" (BHKK, remark after Theorem 6.7, with the Brieskorn sphere carrying "a natural orientation as the link of an algebraic singularity"). Both $`cs`$ and $`\rho`$ flip sign under orientation reversal. Consistency across the record: Helle's $`cs(Q)=-1/120`$ lives on the quotient orientation $`+\Sigma`$; BHKK's $`cs(A_1)=+1/120`$ lives on $`X_{+1}=-\Sigma`$; these are the same statement. Boundary orientations throughout use the outward-normal-first convention; on a compact truncation of the ALE end, the induced boundary orientation of $`\widetilde{X}`$ is $`+\Sigma`$ in this convention.

## 1. The framework decision

**The fork.** $`\pi_1(W)=1`$, so the holonomy $`2I\to\mathrm{SU}(2)`$ cannot factor through the interior and no flat extension of $`Q'`$ exists. The two candidate schemes from the bridge note:

- **(A) Cylindrical-end / ALE instanton.** A finite-action anti-self-dual connection on the smooth minimal resolution, asymptotic at infinity to the flat connection on $`S^3/2I`$. The extension is non-flat and carries instanton charge; the boundary data enter the index formula as finite group sums of exactly the Step-1 defect type.
- **(B) Orbifold cone.** On the orbifold $`\mathbb{C}^2/2I`$ itself the flat connection does extend (the orbifold fundamental group is $`2I`$), and the index localizes at the cone point.

**Decision: (A) is the vehicle, (B) is a check.** The reason is visible in Nakajima's own pair of formulas. For the ALE space, the dimension of the moduli space of anti-self-dual connections asymptotic to a flat $`\rho`$ is (Nakajima, Invent. Math. 102 (1990), Theorem (2.7)):

```math
\dim M \;=\; \dim G_{\rho} \;-\; \int_X \mathrm{ch}(E^*\otimes E)\,\mathrm{ch}(S^+)\,\hat{A}(X) \;-\; \frac{1}{2\lvert\Gamma\rvert}\sum_{\gamma\neq e} \chi_{\rho}(\gamma^{-1})\,\chi_{\rho}(\gamma)\Bigl(1-\cot\tfrac{r(\gamma)}{2}\cot\tfrac{s(\gamma)}{2}\Bigr),
```

an interior Chern-Weil term plus the boundary group sum. For the orbifold treated equivariantly, the same paper's (2.8) has **no interior class content at all**: the topology term collapses to the charge $`2r\int c_2(E)`$ and the group sum doubles, one copy at the cone point and one at infinity (with $`r_0=r_\infty`$, $`s_0=-s_\infty`$: the two ends see opposite orientations). Route (B) is therefore structurally the Step-1 computation run twice: it sees the local representation data of $`\Gamma`$ at the cone points, but not the resolved exceptional-curve homology or any non-orientable surface representatives, because the cone has no $`H_2`$. The moment one resolves to obtain the classes, the flat extension is gone and one is in (A). So (B) survives as a two-cone-point consistency identity, and the bridge program lives in (A).

**What (A) buys Steps 3 and 4.** Kronheimer-Nakajima prove the index machinery in exactly this setting (Math. Ann. 288 (1990), Appendix). Their (A.1), for the twisted Dirac operator on the ALE space with $`A`$ asymptotic to the flat connection of the $`\Gamma`$-module $`W`$:

```math
\dim L^2\text{-}\mathrm{Ker}\, D_A^- \;=\; -\int_X \mathrm{ch}(E)\,\hat{A}(X) \;+\; \frac{1}{\lvert\Gamma\rvert}\sum_{\gamma\neq 1} \frac{\chi_W(\gamma)}{2-\chi_Q(\gamma)},
```

and, decisively for us, their (A.2): the tautological bundles $`\mathcal{R}_i`$ (one per nontrivial irrep of $`\Gamma`$, each carrying a finite-action anti-self-dual connection) satisfy

```math
\int_X \mathrm{ch}(\mathcal{R}_i\otimes\mathcal{R}_j^*)\,\hat{A}(X) \;=\; \frac{1}{\lvert\Gamma\rvert}\sum_{\gamma\neq 1} \frac{\chi_{R_i}(\gamma)\,\chi_{R_j^*}(\gamma)}{2-\chi_Q(\gamma)},
```

where the exceptional curves have intersection matrix $`-C_{E_8}`$ and the dual tautological $`c_1(\mathcal{R}_i)`$ classes pair by $`-C_{E_8}^{-1}`$ (their Theorem A.7). This is the geometric McKay correspondence in index form. It supplies the correct interior basis, the $`c_1(\mathcal{R}_i)`$ with the distance-six node a definite one of them, and a theorem-level pairing between tautological classes and boundary character sums. What remains for Steps 3 and 4 is to show that the specific surface and normal-twist term the bridge needs lands in this basis with the distance-six coefficient; that is not proved by (A.2), it is set up by it. Note $`2-\chi_Q(\gamma)=4\sin^2(\phi_\gamma/2)`$: the same golden-class arithmetic as Step 1 sits in the denominators.

**Cost check.** The ALE metric is not the round quotient metric at the boundary, but $`\rho`$ of a flat connection is metric-independent (APS II, the rho invariant), so the Step-1 boundary values transfer to the ALE end unchanged. Nothing in Step 1 is re-derived or modified by the framework choice; only the sign convention is pinned, next.

## 2. The sign

**The published anchor.** BHKK (arXiv:math/9908020, Section 6) compute the adjoint rho invariant of the first flat connection on the Poincaré sphere, in their orientation $`X_{+1}`$. Their equation (6.5), for a path $`A_t`$ from the trivial connection $`\Theta`$ to a flat $`A_1`$:

```math
SF_{su(2)}(A_t;X) \;=\; 8\bigl(cs(A_1)-cs(A_0)\bigr) \;+\; \tfrac{1}{2}\bigl(\varrho_X(\mathrm{ad}\,\alpha_1)-\varrho_X(\mathrm{ad}\,\alpha_0)\bigr) \;+\; \tfrac{1}{2}\bigl(\dim H^{0+1}(X;su(2)_{\alpha_1})-\dim H^{0+1}(X;su(2)_{\alpha_0})\bigr),
```

"where the rho invariants are defined relative to the odd signature operator acting on $`su(2)`$-forms via the adjoint action." They then state: "one can compute that $`\varrho_X(\mathrm{ad}\,\alpha_1)=\pm\frac{73}{15}`$ by standard methods. The sign ambiguity comes about because the answer depends on how $`X`$ is oriented. This problem can be resolved since we know that $`cs(A_1)=\frac{1}{120}`$: the only way the left hand side can be an integer is if $`\varrho_X(\mathrm{ad}\,\alpha_1)=\frac{73}{15}`$, in which case $`SF_{su(2)}(\Theta,A_1;X)=1`$."

Two things follow at once. The magnitude $`73/15`$, which Step 1 computed and could not match to a printed value, **is in print**. And the sign on $`X_{+1}`$ is $`+73/15`$, fixed by integrality.

**The same argument for $`Q'`$, with the lift stated.** With $`h(\Theta)=\dim H^{0+1}=3`$, $`h(\alpha)=0`$ (acyclicity), $`cs(\Theta)=0`$, and $`\rho_{\mathrm{ad}}(\Theta)=0`$, equation (6.5) reads $`SF = 8\,cs + \rho/2 - 3/2`$. The magnitude here is Step-1 data: the individual $`G`$-signature computation gives $`\lvert\rho_{\mathrm{ad}Q'}\rvert=97/15`$; the integrality equation only chooses the sign. One bookkeeping point: (6.5) uses a real lift of $`cs`$, and BHKK's Table 1 prints the representative $`cs(A_2)=-71/120`$, the class of $`+49/120`$ mod $`\mathbb{Z}`$. The argument does not depend on the choice: shifting the lift by an integer shifts $`8\,cs`$ by a multiple of $`8`$, so both the integrality of $`SF`$ and its value mod $`8`$ are lift-independent. Exactly:

- $`Q`$ ($`cs=+1/120`$, BHKK's lift): $`\rho=+73/15`$ gives $`SF = \tfrac{2}{30}+\tfrac{73}{30}-\tfrac{45}{30} = 1`$ (integer); $`\rho=-73/15`$ gives $`-58/15`$ (excluded).
- $`Q'`$ ($`cs=-71/120`$, BHKK's printed representative): $`\rho=+97/15`$ gives $`SF = -\tfrac{142}{30}+\tfrac{97}{30}-\tfrac{45}{30} = -3\equiv 5\bmod 8`$ (integer); $`\rho=-97/15`$ gives $`-142/15`$ (excluded). The $`+49/120`$ lift gives $`SF=5`$ directly, the same class mod $`8`$.

So on $`X_{+1}`$: $`\rho_{\mathrm{ad}Q}=+73/15`$ (published) and $`\rho_{\mathrm{ad}Q'}=+97/15`$ (forced by the same equation, lift-independently), with spectral flows $`1`$ and $`5`$ mod $`8`$, both odd, as BHKK's parity requirement demands. (A reader consulting their Table 1 will see an $`SF(\Theta,A)`$ column of zeros: that column records the spectral flow on the knot-complement piece $`Z`$ of their splitting, which vanishes; the closed-manifold value $`SF_{su(2)}(\Theta,A_1;X_{+1})=1`$ is stated in their Section 6 text.)

**The machinery identification.** BHKK also print the canonical-representation rho invariants on $`X_{+1}`$: $`\varrho(A_1)=59/30`$ and $`\varrho(A_2)=131/30`$. Running the Step-1 defect machinery (per-element defect $`-\cot^2(\phi/2)`$, the convention of the eta-gatekeeper note) on the fundamental characters reproduces both printed values exactly, in $`\mathbb{Q}(\sqrt5)`$ arithmetic with the surds cancelling. The Step-1 convention **is** the $`X_{+1}`$ orientation, established against print and independently of the adjoint computation.

**Transfer.** $`X_{+1}\cong-\Sigma`$ as oriented manifolds, and $`\rho`$ flips under reversal. On $`+\Sigma=\partial\widetilde{X}`$, the resolution-boundary orientation:

```math
\boxed{\ \rho_{\mathrm{ad}Q}=-\tfrac{73}{15},\qquad \rho_{\mathrm{ad}Q'}=-\tfrac{97}{15},\qquad \rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-\tfrac{8}{5}\ \text{ on }\partial W\ }
```

**Independent corroborations.**

1. *Direct APS bookkeeping.* Under the quotient orientation of $`S^3/\Gamma`$ (the APS complex-orientation convention), the orientation-compatible angle assignment gives per-element defect $`+\cot^2(\phi/2)`$, not $`-\cot^2`$; the $`G`$-signature sum then lands on $`-8/5`$ on $`+\Sigma`$ directly.
2. *Fintushel-Stern consistency check.* FS (3.8) gives $`R(e)=\frac{2e^2}{a}-3+m+\sum_i\frac{2}{a_i}\sum_{k=1}^{a_i-1}\cot\bigl(\tfrac{\pi a k}{a_i^2}\bigr)\cot\bigl(\tfrac{\pi k}{a_i}\bigr)\sin^2\bigl(\tfrac{\pi e k}{a_i}\bigr)`$ with $`SF(\alpha,\theta)=R(e)\bmod 8`$ in their conventions. For $`\Sigma(2,3,5)`$: $`R(1)=1`$, $`R(7)=5`$ exactly (implementation verified against FS's own $`\Sigma(4,3,5)`$ table: $`e=103,109,94,118\to 1,3,5,7`$). Run through the grading packages of §3, this is consistent with the negative branch on the Brieskorn orientation and not with the positive one. BHKK carries the sign; this is filed as a consistency check rather than an independent pillar, with the convention chain recorded in the computation notes.
3. *The $`cs`$ web.* Helle's link-orientation $`cs(Q)=-1/120`$ and BHKK's $`X_{+1}`$ value $`+1/120`$ agree under the flip; and the affine-$`E_8`$ solve's $`cs(Q')=-49/120`$ (computed by Helle's method; the value itself is ours) flips to $`+49/120`$ on $`X_{+1}`$, the same class mod $`\mathbb{Z}`$ as BHKK's printed representative $`-71/120`$.

**What this does to Step 1.** Nothing in the gate changes: the magnitude $`8/5`$, the golden-class support, and the mod-$`\mathbb{Z}`$ normalization test are orientation-independent. The deferred sign is now fixed, and the Step-1 caveat "the integer part rests on the $`G`$-signature computation alone" is retired: $`\pm 73/15`$ is published (BHKK Section 6), resolved by the same integrality argument used here, and the machinery that produced Step 1 reproduces BHKK's printed canonical-rep values exactly.

## 3. Grading conventions (a reader's guard)

The literature carries three internally consistent grading packages for the same two connections, and mixing them manufactures sign paradoxes. For the record:

Three different quantities travel under the symbol $`SF`$; they are subscripted here by owner.

| Package | Orientation | Grading of $`(Q, Q')`$ | Convention |
|---|---|---|---|
| Fintushel-Stern 1990 | $`+\Sigma`$ | $`\mu_{\mathrm{FS}}=-R_{\mathrm{FS}}(e)-3=(4,0)`$, even | $`R_{\mathrm{FS}}(e)=(1,5)`$ is FS's rotation-number quantity |
| Modern instanton $`I_*`$ | $`+\Sigma`$ | $`(1,5)`$ | $`\mu=-3-SF_{\mathrm{mod}}`$ with $`SF_{\mathrm{mod}}=(4,0)`$ |
| KKR / BHKK | $`X_{+1}=-\Sigma`$ | $`SF_{\mathrm{BHKK}}=(1,5)`$ as the grading | $`(-\varepsilon,-\varepsilon)`$ spectral-flow convention |

The line connecting the last two rows is the reversal identity $`SF_{\mathrm{BHKK}}(-\Sigma)=-SF_{\mathrm{mod}}(+\Sigma)-3`$ (irreducible, acyclic endpoints): $`-(4,0)-3\equiv(1,5)\bmod 8`$. The numerical agreement of $`R_{\mathrm{FS}}=(1,5)`$ on $`+\Sigma`$ with $`SF_{\mathrm{BHKK}}=(1,5)`$ on $`-\Sigma`$ is that identity at work, not the same quantity read twice; mistaking them for equal is precisely the trap this table guards. The familiar $`I_*(\Sigma(2,3,5))=\mathbb{Z}_{(1)}\oplus\mathbb{Z}_{(5)}`$ is the middle row; the assignment $`Q\to 1`$, $`Q'\to 5`$ is derived (Helle's grading data plus the reversal rule), stated directly by no single source.

## 4. Handoff to Step 3

Fixed inputs going forward: $`W=\widetilde{X}`$ (minimal resolution, intersection form negative definite $`E_8`$), $`\partial W=+\Sigma`$, boundary data $`\rho_{\mathrm{ad}Q}=-73/15`$ and $`\rho_{\mathrm{ad}Q'}=-97/15`$, vehicle formulas KN (A.1)/(A.2) and Nakajima (2.7), interior basis the tautological $`c_1(\mathcal{R}_i)`$ pairing by $`-C_{E_8}^{-1}`$ (KN Thm A.7).

The Step-3 target formula, stated so the entry point is actionable: write the APS index of the adjoint-twisted operator on $`W`$, with the charge-carrying extension asymptotic to $`Q'`$, as an interior Chern-Weil term in the tautological basis (for the distance-six bundle, the candidate (A.1)-type term $`\int_W \mathrm{ch}(\mathcal{R}_{d6})\,\hat{A}`$) plus the boundary correction of the flat limit, and determine whether the surface and normal-twist term the bridge needs enters with the distance-six coefficient. Two bookkeeping items belong to that step, not here. First, KN's boundary sums are Dirac-type eta invariants while the bridge's boundary invariant is the odd-signature $`\rho`$; the formula must either be written for the odd-signature complex or the two etas related explicitly. Second, the sign convention of the boundary correction ($`\eta`$ versus $`-\eta`$, outward normal) must be fixed in whichever form is used. The oriented $`\rho`$ values above are the invariant inputs to both. Step 3 also computes $`H_2(W;\mathbb{Z}_2)`$, which classes are representable by non-orientable embedded surfaces, and which class the McKay correspondence assigns to the distance-six node.

## Verdict

Step 2 is closed, with the evidentiary weights stated plainly. Framework: the ALE instanton setting on the minimal resolution (Kronheimer-Nakajima); the orbifold cone is a consistency check only, because it lacks the resolved $`H_2`$ surface-class content Steps 3 and 4 need. Sign: $`\rho_{\mathrm{ad}Q'}-\rho_{\mathrm{ad}Q}=-8/5`$ on the resolution-boundary orientation. The anchors, in order of directness: BHKK's published $`+73/15`$ for $`Q`$ on $`X_{+1}=-\Sigma`$; the same integrality equation forcing $`+97/15`$ for $`Q'`$, lift-independently; the machinery identification against BHKK's printed canonical-rep values $`59/30`$ and $`131/30`$; and the direct APS orientation bookkeeping, with the Fintushel-Stern package as a consistency check. The $`Q`$ sign is in print; the $`Q'`$ sign is forced by a published equation applied to the Step-1 magnitude. Step 1 stands with its digit-match caveat retired. Step 3 is unblocked.

## Sources

- H. U. Boden, C. M. Herald, P. Kirk, E. Klassen, *Gauge theoretic invariants of Dehn surgeries on knots*, Geom. Topol. 5 (2001), arXiv:math/9908020 (eq. (6.5); Section 6 Poincaré-sphere computation, $`\varrho=\pm 73/15`$ resolved to $`+73/15`$ on $`X_{+1}`$; canonical-rep values $`59/30`$, $`131/30`$; the oriented identification $`X_k\cong-\Sigma(2,q,2qk-1)`$).
- P. B. Kronheimer, H. Nakajima, *Yang-Mills instantons on ALE gravitational instantons*, Math. Ann. 288 (1990) 263-307 (Appendix: (A.1), (A.2), Theorem A.7).
- H. Nakajima, *Moduli spaces of anti-self-dual connections on ALE gravitational instantons*, Invent. Math. 102 (1990) 267-303 (Theorem (2.7); orbifold formula (2.8)).
- R. Fintushel, R. Stern, *Instanton homology of Seifert fibred homology three spheres*, Proc. LMS (3) 61 (1990) 109-137 (formula (3.8); Theorem 3.9; Proposition 3.10; the $`\Sigma(4,3,5)`$ worked table).
- Atiyah, Patodi, Singer, *Spectral asymmetry and Riemannian geometry II* (metric independence of $`\rho`$ for flat bundles; sign flip under orientation reversal).
- G. O. Helle, arXiv:2203.09471 ($`cs`$ conventions on the quotient orientation; orientation reversal flips $`cs`$).
- A. Daemi, arXiv:1810.08176 (modern-convention gradings $`(4,0)`$ on $`-\Sigma(2,3,5)`$, corroborating the convention table).

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
