<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Fixed-Edge Stability Check

**Type:** Result
**State:** Closed
**Status (2026-10-01):** Run blind against terms frozen before it, and reviewed. Reproduced: two blind rooms each derived the reduction to the lune, by its own route, and the lune's Dirichlet spectrum without taking either from the carrier page, and the frozen finite-element cross-check matched $`\alpha_0(\alpha_0 + 1)/R^2`$ at all five widths, with a largest miss of $`3.0 \times 10^{-7}`$ and a largest error estimate of $`1.2 \times 10^{-4}`$, both relative, inside the tolerance of a relative $`10^{-3}`$. Two steps of the rederivation were asserted rather than argued in both rooms, and the check cannot see the seam's twist, which the carrier page already says does not enter. The result counts toward the Tier 2 bar only as the carrier page's fence on it says.
**Summary:** The independent check registered with the carrier page's §IX, run blind on OpenWave as M8.14, and scored here against the frozen terms.
**Inputs:** `projective-carrier.md` (§IX and its frozen terms), `carrier-edge-regimes.md`
**Parent:** `projective-carrier.md`

---

RESULT, Reproduced. The [projective carrier](projective-carrier.md)'s §IX derives fixed-edge stability of the unbent conic carrier $`M(W)`$ at every embedded width, for its declared class of variations, and registered an independent check of it on 2026-09-27, frozen in that page's header. The check has run blind, on OpenWave as M8.14, and every frozen condition for Reproduced holds.

**Related:** [The Projective Carrier](projective-carrier.md), [The Carrier's Edge Regimes](carrier-edge-regimes.md), [The Variational Clock Arm](variational-clock-arm.md), [The Tier 2 Fixed-Boundary Run](tier2-fixed-boundary.md).

---

## I. The terms, as frozen

The terms are §IX's span from the line beginning `*Registered` to the end of the Outcomes list's Unresolved item, frozen on 2026-09-27 with SHA-256 `43e7165a0ba67eafd722896ce493e21b896bb1f1643aa45d6ed58c39c3612cb9`, which the carrier page's gate checks. They ask for a rederivation of §IX's reduction and of the lune's Dirichlet spectrum, without taking them from the page, and for a $`P_1`$ finite-element cross-check in the band's own coordinates at $`W/R \in \{1/4, 1/2, 1, 7/5, 3/2\}`$, extrapolated from four uniform refinements, whose bottom of $`-\Delta`$ must match $`\alpha_0(\alpha_0 + 1)/R^2`$, $`\alpha_0 = \pi R/(2W)`$, to a relative $`10^{-3}`$.

## II. The run

OpenWave ran the check as M8.14, merged on 2026-10-01 ([openwave-labs/openwave#610](https://github.com/openwave-labs/openwave/pull/610)); its method note is the record ([M8.14 method note](https://github.com/openwave-labs/openwave/blob/63c5d03db2e22d7c94200886ead7f63037f41b7b/openwave/xperiments/m8_mit/research/findings/m8_14_method_note.md)). Two rooms, each a headless session with no network and no instruction file, worked from a sheet that gave the object, the variation, the admissible class and the protocol, and named neither the lune, nor the reduction, nor any formula. An auditor, also blind, recomputed every width by two methods of its own before it saw either return, then judged both rooms valid. An adversarial audit, given every return and importing none of their code, tried to refute the outcome and the seam claim, and refuted neither.

## III. Scoring against the terms

**The rederivation agrees.** The terms ask the runner to derive step 2's reduction, which multiplies by $`\phi_0`$. M8.14 declared before the run how "agrees" is read ([its pre-registration](https://github.com/openwave-labs/openwave/blob/bfd038ec6b030647dbcbbfa885a81e3fdb5dfaff/openwave/xperiments/m8_mit/research/tasks/m8_14_task_details.md?plain=1#L86-L88)): "both are ESTABLISHED, as written or with a supplied part named. The route may differ from the author's: a room is told neither the reduction nor the lune, and one that separates variables and unrolls the seam establishes the reduction sector by sector." Under that reading both rooms agree. Both reduce the band's Dirichlet problem to the lune of opening $`2W/R`$, one by unfolding the band's coordinates and one by an explicit unitary, and both derive its spectrum $`(\nu_m + \ell)(\nu_m + \ell + 1)/R^2`$, $`\nu_m = m\alpha_0`$, which is §IX's step 3.

**The cross-check.** Both rooms return the same levels to $`8.2 \times 10^{-14}`$ relative. Recomputed from their levels with the frozen rules, the order from the last three levels, the extrapolation from the last two and the error estimate $`\lvert\lambda_\text{extrap} - \lambda_\text{finest}\rvert`$:

| $`W/R`$ | extrapolated bottom | $`p`$ | error estimate | $`\alpha_0(\alpha_0 + 1)`$ | relative miss |
| --- | --- | --- | --- | --- | --- |
| 1/4 | 45.761589282 | 1.9967 | $`5.60 \times 10^{-3}`$ | 45.761602912 | $`3.0 \times 10^{-7}`$ |
| 1/2 | 13.011196550 | 1.9994 | $`1.18 \times 10^{-3}`$ | 13.011197055 | $`3.9 \times 10^{-8}`$ |
| 1 | 4.038197481 | 2.0002 | $`3.19 \times 10^{-4}`$ | 4.038197427 | $`1.3 \times 10^{-8}`$ |
| 7/5 | 2.380875543 | 2.0004 | $`1.84 \times 10^{-4}`$ | 2.380875489 | $`2.3 \times 10^{-8}`$ |
| 3/2 | 2.143820313 | 2.0003 | $`1.66 \times 10^{-4}`$ | 2.143820262 | $`2.4 \times 10^{-8}`$ |

Values are at $`R = 1`$. Each recomputed value equals the one the room reports.

**The outcome.** Reproduced: the rederivation agrees, and at all five widths the order is near 2, the miss is at most $`3.0 \times 10^{-7}`$ relative, and the error estimate is at most $`1.2 \times 10^{-4}`$ relative, at $`W/R = 1/4`$. The terms state the tolerance as relative, and their own example, an absolute $`2 \times 10^{-3}/R^2`$ at $`W/R = 3/2`$, reads it that way; under an absolute $`10^{-3}`$, which the terms do not state, $`W/R = 1/4`$ and $`1/2`$ would be Unresolved for their error estimates.

**Controls beyond the terms.** The run added two widths: at $`W = \pi R/2`$ the bottom is $`2.000000050/R^2`$, the critical width where $`J`$'s bottom reaches $`0`$; at $`W/R = 17/10`$, past it, $`J`$'s bottom is $`-0.2222301/R^2`$. Both agree with §IX's first fence.

## IV. What the run adds, and what it leaves

- **Two supplied steps.** Both rooms asserted, without the argument, that the class of sections matched only in value across the seam has the same form closure as the smooth core, and that removing the vertices leaves the lune's Dirichlet problem, since points have zero capacity in two dimensions. The record grades the reduction established with these steps supplied. The adversarial audit named both; the auditor's second stage had graded one room's sentence on the first as plain established, and its own supplied grade, on the other room's direct sum of sector operators, matters only at $`W/R = 17/10`$, outside the terms.
- **The seam.** No gate in the protocol sees how the seam is glued. With zero data on the collapsed fibre the band's two halves meet only across the seam, so the glued band is the lune with the seam as its equator, and its spectrum is the union of the half-lune's with the seam free and with the seam held at zero: the modes even and odd under the reflection in the equator. A flipped seam sign and a glue without the reversal $`w \mapsto -w`$ are unitarily equivalent to the true glue, and a strip cut at the seam with zero data on one end only has exactly that union for its spectrum. On the protocol's mesh the flipped sign and the one-sided cut are identical to roundoff, and the glue without the reversal differs only through the mirrored triangle diagonals of one sheet, an artifact that vanishes under refinement and disappears when those diagonals are mirrored back. Of the four wrong seams the record tests, only one deleted with both ends free shows, by repeating the bottom. So the check certifies the lune's Dirichlet stability, which an orientable band of the same shape shares: §IX's "The twist does not enter", sharpened.
- **Audited, not proved.** The rooms' arguments were graded by AI auditors; they are not verified theorems, and the results the rooms took from memory are named in their manifests and were not rederived.
- **What it does not change.** The result is a fixed-edge theorem, not vacuum stability. It counts toward the Tier 2 bar only under §IX's fence: the premise, the conic realization and the fixed temporal edge adopted on grounds that stand without it, and the conic type at $`p_c`$ forced or grounded. [The Carrier's Edge Regimes](carrier-edge-regimes.md) finds that no free-edged energy the ground floor names supplies the fixed edge. It selects no width, says nothing about least area, and says nothing about the widths at which the carrier's image embeds in $`S^3/2I`$.

## V. What was known when

The terms were frozen on 2026-09-27 and published with the carrier page; the packet sent to OpenWave carried them byte for byte, and merged there before the run ([openwave-labs/openwave#608](https://github.com/openwave-labs/openwave/pull/608)). The derivation was public from the same day, so the rooms were kept from it by containment rather than timing: their transcripts show no read outside their own rooms, and the auditor's second stage saw neither the frozen terms nor the frozen values.

## Files

In [`scripts/fixed-edge-check/`](scripts/fixed-edge-check/), with the SHA-256 of every other file in `SHA256SUMS`:
- `solver_a_results.json`, `solver_b_results.json`: the two rooms' returns, byte for byte as the record lands them.
- `score.py`: checks the copies against the record's manifest (K1), recomputes each room's order, extrapolation and error estimate from its levels and compares them with what it reports (K2), compares the rooms (K3), scores the five widths under the frozen rules (K4), and tests the rules' Contradicted branch on a shifted level (K5). Its `--arms` mode plants a defect for each check and requires it to fire, among them the absolute reading of the tolerance, which leaves $`W/R = 1/4`$ and $`1/2`$ Unresolved. Its record is `score.out`.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
