<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# McKay Propagator Correction to the Fermion Mass Formula

**Type:** Test
**State:** Reopened
**Status (2026-10-03):** Registered (below): the literal $`\Pi_T`$ path product, both directions declared, one run against the corrected table next. Resolved as a negative result on the pre-correction mass table (2026-06-06): no parameter-free propagator or branch-point correction tracked the high-distance residuals. Reopened 2026-07-28 by the half-integer torsion correction, which revised twelve of the twenty-four products; the propagator question is open again against the corrected residuals. Charm remains unplaced.
**Summary:** Tests whether a parameter-free McKay-propagator or branch-point correction accounts for the high-McKay-distance mass residuals.
**Inputs:** the fermion mass formula, C_geom and torsion tables, the Coxeter-Galois gate, the McKay graph for 2I, the maintained scorecard (`../../../../spectrum/files/mass-spectrum.md`), `scripts/mass-null-inputs.json` (the frozen v1.1 inputs), `scripts/mckay-propagator-retest/`
**Frozen:** 2026-06-06 the original negative result and its residual/correlation tables; 2026-10-03 the literal $`\Pi_T`$ registration, before its run

RESOLVED as a negative result on the pre-correction mass table (2026-06-06); **REOPENED 2026-07-28** by the half-integer torsion correction (see the update below). The 2026-06 finding was that the propagator/branch-point correction is eliminated by the signed-residual test, the high-distance residual being scatter rather than a correctable distance trend, with down and tau as two separate standing anomalies missing in opposite directions. That residual landscape no longer obtains: on the corrected table both are overshoots. Everything from the Result section down is preserved unedited as the 2026-06 record. **Registered 2026-10-03:** the literal $`\Pi_T`$ re-test, [below](#registration), runs once against the corrected table.

**Update (2026-06-19).** The honesty pass reframed the mass spectrum from prediction to comparison, and this negative result is its empirical backbone: the high-distance residual is irreducible symmetric scatter (~×1.8), not a recoverable distance or branch trend, so the ladder is read as a comparison against the measured fermions, not a fully-determined prediction. The propagator/branch route explored in §1–§11 was the attempt to make the masses fully determined; eliminating it is what the comparison framing now states plainly. Three reconciling facts for the counts below: $`m_e`$ is the benchmark that sets the absolute scale (its 1.02 is the $`m_e \leftrightarrow \Lambda`$ loop closing, not a hit), so the charged within-×3 count is 6 of 8 (down outside, charm unassigned; the maintained scorecard is in [the mass spectrum](../../../../spectrum/files/mass-spectrum.md)), and the within-6% comparisons are the up and muon. The §1–§11 body is kept as the 2026-06-06 record.

**Update (2026-07-11).** The July 2026 $`T^2(R_0)`$ correction ([mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §4) drops the maintained charged tally to **5 of 8**: the bottom-quark entry $`(R_2,\text{gal})`$ was the non-acyclic diagonal product carrying the manifold volume, so at the canonical topological value $`T^2(R_0)=1`$ it recomputes to ~197 GeV and is uncounted. The 6-of-8 figures above, and the $`b`$/1.28 entries in the §1–§11 propagator tables and the companion `.test.py`, predate that correction and are kept as the 2026-06 record.

**Update (2026-07-28).** The half-integer torsion correction ([mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §4: the pre-correction values were the coexact-only quantity; the restored scalar term gives exact closed forms; artifact at [torsion-correction](torsion-correction.md)) revises 12 of the 24 entries and re-lands this file's subject matter. The maintained tally is now **5 of 8 compatible coverage / 4 of 8 adjudicated**. The residual landscape analyzed below no longer exists: the tau's $`(R_4,\text{std})`$ address moved to 11.4 GeV (its residual now lives at $`(R_4,\text{gal})`$, an overshoot), the up quark's 6% hit at $`(R_8,\text{triv})`$ vacated (u unassigned), and $`(R_2,\text{triv})`$, the §2.2 "undershooting top candidate," moved to 161.3 GeV, ratio 0.93, where it now carries the top. Under the corrected table the two remaining large residuals (d +0.51, τ +0.44) are both overshoots at Galois vacua, so the Result section's opposite-directions argument, correct for the table it analyzed, does not transfer: the propagator question is formally REOPENED against the corrected residuals on the [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §VI ledger. Everything below predates the correction and is kept as the 2026-06 record of the pre-correction test.

---

<a id="registration"></a>
## Registration (2026-10-03): the literal $`\Pi_T`$ re-test

Registered before the run: one run of `scripts/mckay-propagator-retest/retest.py --run`, which refuses until this section and the script's SHA-256 are on main. Fetch first: the guard compares HEAD with the local `origin/main`.

- **Why it runs.** The 2026-06 test fitted a slope and an intercept to $`\log \Pi_T`$ before reporting its RMS ([its script](scripts/mckay-propagator-correction.test.py)), so the primary candidate of §4.5 has never been tested as the page defines it. On the corrected table four of §6.2's forms, $`\Pi`$, $`\delta`$, $`\kappa`$ and the distance alone, depend on $`\rho`$ alone: they move d at $`(R_8,\text{gal})`$ and the muon and strange at $`(R_8,\text{std})`$ together, though d overshoots and the other two do not. Branch splitting and the combined form need weights the page does not define (§4.6). $`\Pi_T`$ is the one parameter-free candidate left.
- **The candidate.** $`\Pi_T(\rho, \sigma) = \prod_i T^2(i \otimes \sigma)`$ over the intermediate nodes $`i`$ of the unique shortest McKay path from $`R_0`$ to $`\rho`$ (§2.5, $`R_0`$ and $`\rho`$ excluded), with $`T^2`$ from the corrected table: one factor per intermediate node, exponent 1, and no slope, intercept, offset or rescaling.
- **Two arms, both declared.** The page does not say how $`\Pi_T`$ enters the mass (§4.5), and its only directional reasoning (§4.1, §4.2) reads the sign of the residual. Both directions are registered: arm M multiplies the predicted mass by $`\Pi_T`$, arm D divides it. Each arm is re-benchmarked to the electron by applying the correction relative to the electron's own factor: arm M multiplies by $`\Pi_T(\rho, \sigma)/\Pi_T(R_7,\text{triv})`$ and arm D divides by that ratio, so the electron's prediction, which sets the scale, does not move.
- **Inputs.** `scripts/mass-null-inputs.json`, the torsion null test's frozen v1.1 inputs, for $`C_\text{geom}`$, the nine base torsions, the tensor multiplicities, the McKay distances, $`\mu_\Lambda`$, $`\sqrt{\Omega_\Lambda}`$ and the observed masses, its SHA-256 pinned in the script; the McKay graph of §2.5; and the adjudicated addresses of [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §III. Six input gates check them against the pages at 3c7423b.
- **The scored set.** d at $`(R_8,\text{gal})`$, the muon and strange at $`(R_8,\text{std})`$, τ at $`(R_4,\text{gal})`$ and t at $`(R_2,\text{triv})`$: the five assigned charged fermions with measured masses. The muon and strange are scored separately and share their address's correction. The electron is the benchmark and is not scored; b is not counted, its compatible entry recorded but not promoted; u and c are unassigned. The residual is $`r = \log_{10}(m_\text{pred}/m_\text{obs})`$, from the masses the inputs give.
- **The grade, set by rule.** An arm passes only if (1) the uncentered RMS of $`r`$ over the five falls, like for like, with the same five fermions and the same benchmark before and after and nothing centered; (2) every scored fermion ends inside the scorecard's ×3 window, $`\lvert r\rvert \le \log_{10} 3`$; and (3) $`\lvert r\rvert`$ falls for d and for τ. The test is positive if an arm passes, reported as one of two declared arms, and negative if both fail. Nothing else enters the verdict.
- **A diagnostic, not a p-value.** For each arm the script ranks the observed arrangement among the 24 ways of placing the four address corrections on the four addresses. The rank is descriptive: it treats the four addresses as exchangeable, an assumption rather than a fact.
- **Outcomes.** Negative: the page closes with Verdict Negative. With the rest of §6.2 out on the corrected table, no parameter-free propagator form on this page survives, and d and τ stand as the two overshoots; the closing propagates to [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §VI, the [framework](../../../README.md) page's One Formula paragraph and research frontier, the [claim ledger](claim-ledger.md), the [working index](../README.md), [the scaling law](scaling-law-uniqueness.md)'s historical note and [the torsion null test](mass-null-test.md). Positive: suggestive only, four address units carrying little weight; the page stays open, no scorecard change follows, and a mechanism for the arm that passed is the next step.
- **§10 on the corrected table.** Its constraints 3 to 5, the top's miss at distance 7 and the reversal, describe the pre-correction table; the grade above replaces them. Constraint 7, charm, is not tested: charm is unassigned.
- **Expectations.** The drafter expects both arms to fail: while reading the recon of 2026-10-02 it formed $`\Pi_T`$ at the four addresses and the benchmark and tried two exponents, numbers neither recorded nor used. Both reviewers read that expectation: one states it formed no $`\Pi_T`$ value, the other that the registered result is unopened on its side. No choice above uses those numbers: both directions are declared, and the grade comes from the reviewers' specification and the scorecard's existing ×3 window.
- **Frozen.** `retest.py`, SHA-256 `c5bc9dd03c7b0e80edca5a487056de77caff23e1ec824848f3f2186f38497b4e`. Without `--run` it checks its inputs and machinery, each check with a planted defect that must fire, and forms no $`\Pi_T`$ on the real table.

---

## Result: hypothesis eliminated (negative)

*Everything from here down is the 2026-06 pre-correction record, preserved unedited; its verdicts are scoped to the table analysed then. The route is formally REOPENED against the corrected residuals per the 2026-07-28 banner above.*

The protocol (§6, §11) was run against the full §II data. The formula places the 10 SM-assigned masses within ×3.3 (most within ×1.5; the down quark, the worst, at ×3.2), then the signed residual $`r = \log_{10}(m_\text{pred}/m_\text{obs})`$ was computed and correlated against every parameter-free candidate. Reproducible script: [`mckay-propagator-correction.test.py`](scripts/mckay-propagator-correction.test.py).

**1. The residual is not a systematic overshoot.** The two worst assigned fermions miss in opposite directions, so no single multiplicative factor can fix both.

| Fermion | $`(\rho, \sigma)`$ | dist | $`r`$ | Direction |
|---|---|---|---|---|
| down | R8, gal | 5 | +0.509 | overshoot ×3.23 |
| tau | R4, std | 6 | -0.384 | undershoot ×2.42 |
| top (assigned) | R2, std | 7 | +0.181 | overshoot ×1.52 |

The §6.2 critical check assumed both misses were overshoots. They are not.

**2. The reversal that motivates §2 is not in the assigned data.** The "dist-7 triv miss" of §2.2 is R2 triv (44.5 GeV), the unassigned top candidate, and it undershoots: it sits below the 172.7 GeV top, not above. The assigned dist-7 fermions (b on R2 gal, t on R2 std) are both within ×1.5. With no reversal, the branch-point hypothesis (§2.3, §2.4, §4.6) loses its motivating evidence.

**3. No parameter-free candidate tracks the residual** (signed, clean charged set, n = 7):

| Candidate | Pearson vs $`r`$ | RMS resid after |
|---|---|---|
| $`\log \Pi_T`$ (§4.5, primary) | -0.15 | 0.254 → 0.245 |
| $`\log \Pi_C`$ (§4.1) | +0.23 | 0.254 → 0.242 |
| dist (baseline) | -0.02 | 0.254 → 0.248 |

All are consistent with zero; none cut the scatter by more than a few percent. The branch and Galois forms (§4.6, §4.7) carry sign only through undefined vacuum weights, which violates constraint #1 (no fitted parameters).

**Verdict.** This is the §8 failure mode: no propagation- or branching-based correction improves the fit. The high-distance residual is roughly symmetric scatter at the ~×1.8 level, not a distance trend. Two isolated, unrelated anomalies remain: the down overshoot (a lone Galois miss at R8, borderline given the 4.67 ± 0.5 MeV lattice uncertainty) and the tau undershoot (a lone standard-vacuum miss at R4). They share no mechanism and are not captured by any path quantity. The propagator/branch-point route is closed; §1 to §11 below are retained as the record of what was tried.

---

## 1. The Problem

The fermion mass formula systematically overshoots at high McKay distance.

```math
m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot (\sqrt{\Omega_\Lambda})^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)
```

Scorecard at the outset of this investigation: 10/12 SM fermions within ×3 (superseded; see the Update and Result sections, and today's 6-of-8 charged count with $`m_e`$ as the benchmark). The two misses examined here both sit at high McKay distance:

| Fermion | Irrep | Vacuum | dist | Predicted (GeV) | Observed (GeV) | Ratio |
|---|---|---|---|---|---|---|
| Down quark | R8 | gal | 5 | 1.51 × 10⁻² | 4.67 × 10⁻³ | 3.22 |
| Top quark | R2 | triv | 7 | 44.54 | 172.7 | 3.88 |

Initial assessment: overshoot grows with McKay distance. But detailed examination reveals the correction is **not purely distance-dependent**. At the same distance, some vacua hit while others miss.

### 1.1 Full Residual Table (SM-assigned entries)

| Fermion | Irrep | Vacuum | dist | Predicted/Observed | Notes |
|---|---|---|---|---|---|
| electron | R7 | triv | 4 | 1.02 | benchmark (loop closure, not a hit) |
| up | R8 | triv | 5 | 1.06 | hit |
| muon | R8 | std | 5 | 1.02 | hit |
| **down** | **R8** | **gal** | **5** | **3.22** | **miss: same irrep, same dist as up and muon** |
| tau | R4 | std | 6 | 2.42 | moderate miss |
| bottom (best) | R2 | gal | 7 | 1.28 | hit |
| **top** | **R2** | **triv** | **7** | **3.88** | **miss: same irrep, same dist as bottom** |

**Key finding:** At dist = 5, triv and std hit within 6%. Gal misses by ×3.2. At dist = 7, gal hits within 28%. Triv misses by ×3.9. The correction is not a function of distance alone. It interacts with the vacuum label.

---

## 2. The Hypothesis (Revised)

The correction is vacuum-dependent and concentrated at the branch point of the McKay graph.

### 2.1 Original Hypothesis (Superseded)

The McKay graph is the actual structure through which modes propagate. Each intermediate node along the path from R0 to the target irrep contributes a cumulative correction. The current formula treats the elevator as a single exponential step. The correction accounts for what happens at each floor the elevator passes through.

This hypothesis predicted a correction monotonic in distance. The data rules this out: at the same distance, different vacua produce different residuals. The correction must be vacuum-dependent.

### 2.2 Revised Hypothesis

The Galois vacuum has a 9× enhanced gap (first allowed k = 5 vs k = 1 for triv and std). At low McKay distance, this enhancement is invisible because the elevator hasn't climbed far enough for the accumulated difference to manifest. At high distance, the Galois vacuum's different spectral structure produces a measurable deviation.

**The pattern:**

| dist | Vacuum that misses | Vacuum(s) that hit | Galois gap relevance |
|---|---|---|---|
| 5 (R8) | gal (×3.2) | triv (×1.06), std (×1.02) | Galois enhanced gap accumulates over 5 steps |
| 7 (R2) | triv (×3.9) | gal (×1.28), std (×1.51) | At dist 7, the path passes through R5 (Galois-fixed irrep); triv is now the outlier |

The reversal at dist 7 (gal hits, triv misses) is the strongest constraint. A pure "Galois penalty" would predict gal always misses. Instead, the miss swaps vacuum at the branch point. This points to the branch structure itself as the source.

### 2.3 The Branch Point at R8

```
R0(1) --- R1(2) --- R3(3) --- R6(4) --- R7(5) --- R8(6) --- R5(4) --- R2(2)
                                                       |
                                                      R4(3)
```

R8 is the fork. R4 and R5 branch off in different directions. The path to R2 goes through R5 (which is Galois-fixed: R5 maps to itself under Galois conjugation). The path to R4 branches directly from R8.

R5 and R4 are the only irreps reached through a fork rather than a straight chain. The single-path approximation may break down precisely here, because the mode "sees" two possible exits at R8 and the branching ratio depends on the vacuum.

### 2.4 Lattice Propagator Analogy (Updated)

On a lattice graph, propagators pick up vertex corrections at each node traversed. At a branch point, the propagator splits. The relative weight of each branch depends on the coupling structure at the node, which in MIT is vacuum-dependent through T²(ρ ⊗ σ).

The correction should be:

- Multiplicative (each node contributes a factor)
- Vacuum-dependent (torsion varies with σ at each intermediate node)
- Sensitive to branching (different behavior at the R8 fork)
- Computable from existing data (C_geom and torsion values are known for all nodes and all vacua)

### 2.5 The McKay Graph (SPECTRUM Convention)

```
R0(1) --- R1(2) --- R3(3) --- R6(4) --- R7(5) --- R8(6) --- R5(4) --- R2(2)
                                                       |
                                                      R4(3)
```

Unique shortest paths from R0:

| Target | Path | dist | Intermediate nodes |
|---|---|---|---|
| R0 | — | 0 | none |
| R1 | R0→R1 | 1 | none |
| R3 | R0→R1→R3 | 2 | R1 |
| R6 | R0→R1→R3→R6 | 3 | R1, R3 |
| R7 | R0→R1→R3→R6→R7 | 4 | R1, R3, R6 |
| R8 | R0→R1→R3→R6→R7→R8 | 5 | R1, R3, R6, R7 |
| R5 | R0→R1→R3→R6→R7→R8→R5 | 6 | R1, R3, R6, R7, R8 |
| R4 | R0→R1→R3→R6→R7→R8→R4 | 6 | R1, R3, R6, R7, R8 |
| R2 | R0→R1→R3→R6→R7→R8→R5→R2 | 7 | R1, R3, R6, R7, R8, R5 |

Note: R4 branches from R8, not from R5. Both R4 and R5 are at dist = 6 but take different paths from R8.

---

## 3. C_geom Values Along Each Path

| Irrep | dim | Spin | D | C_geom |
|---|---|---|---|---|
| R0 | 1 | Int | 60 | — (trivial, no Kostant exponents) |
| R1 | 2 | Half | 120 | 0.0988 |
| R3 | 3 | Int | 60 | 0.5553 |
| R6 | 4 | Half | 120 | 0.2098 |
| R7 | 5 | Int | 60 | 0.7564 |
| R8 | 6 | Half | 120 | 0.2382 |
| R5 | 4 | Int | 60 | 0.8017 |
| R4 | 3 | Int | 60 | 0.7970 |
| R2 | 2 | Half | 120 | 0.2436 |

---

## 4. Candidate Correction Forms

### 4.1 Product of Intermediate C_geom (ELIMINATED)

The simplest candidate: multiply C_geom of each intermediate node along the path.

```math
\Pi(\rho) = \prod_{i \in \text{path}(R0 \to \rho)} C_{\text{geom}}(i)
```

| Target | Intermediate nodes | Π |
|---|---|---|
| R1 | none | 1 |
| R3 | R1 | 0.0988 |
| R6 | R1, R3 | 0.0988 × 0.5553 = 0.0549 |
| R7 | R1, R3, R6 | 0.0549 × 0.2098 = 0.01152 |
| R8 | R1, R3, R6, R7 | 0.01152 × 0.7564 = 0.00871 |
| R5 | R1, R3, R6, R7, R8 | 0.00871 × 0.2382 = 0.00207 |
| R4 | R1, R3, R6, R7, R8 | 0.00871 × 0.2382 = 0.00207 |
| R2 | R1, R3, R6, R7, R8, R5 | 0.00207 × 0.8017 = 0.00166 |

Problem: Π drops fast with distance. If this enters as a direct multiplicative correction, it would crush high-distance masses rather than correct an overshoot. The correction needs to go in the right direction.

### 4.2 Inverse Product (Denominator Correction, ELIMINATED)

If the propagator correction appears in the denominator:

```math
m_{\text{corrected}} = \frac{m_{\text{current}}}{\Pi(\rho)^{p}}
```

For some power p. This would increase high-distance masses, which is the wrong direction (the formula already overshoots).

### 4.3 Ratio or Logarithmic Form

Perhaps the correction is logarithmic:

```math
\delta(\rho) = \sum_{i \in \text{path}} \ln C_{\text{geom}}(i)
```

| Target | δ |
|---|---|
| R1 | 0 |
| R3 | -2.315 |
| R6 | -5.222 |
| R7 | -4.945 |
| R8 | -6.373 |
| R5 | -7.800 |
| R4 | -7.800 |
| R2 | -8.021 |

Note: δ is monotonically decreasing (more negative) with distance, except R7 which is slightly less negative than R6 due to R6's low C_geom. The pattern is approximately linear in distance.

### 4.4 Normalized Path Correction

Perhaps what matters is the ratio of the target's C_geom to the geometric mean of the intermediate C_geom values:

```math
\kappa(\rho) = \frac{C_{\text{geom}}(\rho)}{\left(\prod_{i \in \text{path}} C_{\text{geom}}(i)\right)^{1/\text{dist}}}
```

This normalizes the correction per step. Compute and check if κ correlates with the mass residual.

### 4.5 Torsion Along the Path (NOW PRIMARY CANDIDATE)

The correction involves torsion at each intermediate node, making it vacuum-dependent:

```math
\Pi_T(\rho, \sigma) = \prod_{i \in \text{path}} T^2(i \otimes \sigma)
```

This is now the primary candidate because:

1. The residual pattern is vacuum-dependent (same dist, different vacua, different misses).
2. Torsion is the only factor in the mass formula that varies with vacuum.
3. The Galois vacuum has distinct spectral structure (9× enhanced gap).
4. The reversal at dist 7 (gal hits, triv misses) requires the correction to swap sign across vacua, which torsion can do.

### 4.6 Branch-Point Splitting

At R8, the propagator encounters a fork. The effective correction may involve a weighted sum over branches rather than a single path:

```math
\Pi_{\text{branch}}(\rho, \sigma) = \Pi_{\text{chain}}(R0 \to R8, \sigma) \cdot \left[ w_{R5}(\sigma) \cdot T^2(R5 \otimes \sigma) + w_{R4}(\sigma) \cdot T^2(R4 \otimes \sigma) \right]
```

where the weights w depend on the vacuum through the branching ratio at R8. This would produce different corrections for modes that pass through R5 (path to R2) vs modes that terminate at R4 or R5 directly.

### 4.7 Galois Conjugation Correction

The Galois conjugation swaps R1 ↔ R2 and R3 ↔ R4 while fixing R5 and R7. At the branch point, R4 is the Galois conjugate of R3. The path from R0 to R4 (through R8) passes through R3's conjugate territory. The Galois vacuum may experience an additional phase or sign at nodes where conjugation is active.

---

## 5. The Charm Displacement

### 5.1 The Problem

The Coxeter-Galois gate locks all R4 entries to T₃ = -1/2 (all R4 entries have integer j_first). Charm requires T₃ = +1/2. The framework's own assignment rules exclude charm from its obvious candidate slot at R4 std (~734 MeV, within ×1.73 of charm's 1.27 GeV).

### 5.2 Why This Matters

This is the most informative kind of failure. A framework that bends its rules to fit every particle is less credible. MIT's rules actively exclude the obvious candidate. Either:

1. There is a subtlety at the R4 branch point that modifies the gate (the fork may carry different j_first behavior than the main chain).
2. Charm's assignment involves a mechanism the current formula doesn't capture.
3. Charm is telling you something about the limits of the branch-point approximation.

### 5.3 Connection to Branch-Point Correction

R4 is one of only two irreps reached through the fork at R8. If the branch-point splitting (§4.6) modifies the effective j_first or the Coxeter-Galois gate behavior at branched nodes, this could open a T₃ = +1/2 slot for charm without breaking the gate elsewhere. The correction and the charm assignment may be the same problem.

### 5.4 Status

OPEN. The charm displacement is the tightest constraint on any branch-point correction. Any proposed fix to the mass residual at high distance must simultaneously address (or at minimum not worsen) the charm assignment problem.

---

## 6. Test Protocol

### 6.1 Compute the Residual

For each of the 24 mass formula entries, compute:

```math
r(\rho, \sigma) = \log_{10}\left(\frac{m_{\text{predicted}}}{m_{\text{observed}}}\right)
```

Positive r = overshoot. Negative r = undershoot.

### 6.2 Correlate with Candidate Corrections

Plot r against (in priority order):

1. Π_T (product of intermediate torsion along path). **PRIMARY: vacuum-dependent.**
2. Branch-point splitting factor. **PRIMARY: fork-sensitive.**
3. Combined Π_T × branch correction. **PRIMARY: full propagator.**
4. Π (product of intermediate C_geom). Secondary: vacuum-independent.
5. δ (sum of log C_geom along path). Secondary: distance-only.
6. κ (normalized path correction). Secondary.
7. dist alone. Baseline: check if simple linear correction suffices.

**Critical check:** For each candidate, verify that the correction reverses sign between the two misses. Down (R8 gal, dist 5) overshoots. Top (R2 triv, dist 7) also overshoots but from a different vacuum. The correction must overshoot gal at dist 5 while overshooting triv at dist 7. A correction that only works for one is wrong.

### 6.3 Evaluate

| Outcome | Interpretation |
|---|---|
| r correlates tightly with one candidate | Correction identified; apply and recompute scorecard |
| r correlates with dist but no candidate improves over linear | One-parameter linear correction in dist is sufficient |
| r shows no pattern | Residual is not from propagation; look elsewhere |
| Correction improves some fermions but worsens others | Multiple effects at play; decompose further |

---

## 7. What Success Looks Like

If a single multiplicative correction computable from the McKay graph structure closes the systematic overshoot at high distance:

- The two high-distance misses (down, tau) would close (the eliminated goal: turn the standing anomalies into hits).
- The low-distance comparisons (up quark 6%, muon 3%, with $`m_e`$ the benchmark) should remain unchanged (low dist, correction ≈ 1).
- The correction is parameter-free (computed from known C_geom and torsion values).
- The mass formula becomes fully determined by topology with no residual trend.

---

## 8. What Failure Looks Like

| Failure mode | Implication |
|---|---|
| No vacuum-dependent correction improves the fit | The overshoot is not from propagation or branching; the mass formula structure itself may need revision |
| Correction requires a fitted parameter | Not parameter-free; reduces to curve fitting |
| Correction fixes down quark but breaks top quark (or vice versa) | The vacuum reversal at the branch point is not captured; branching mechanism is wrong |
| Correction fixes masses but breaks charm assignment further | The branch-point gate modification is inconsistent; charm's exclusion is real and permanent |
| Torsion product diverges or vanishes along path | Intermediate torsion values may need regularization; check if T² = 0 at any node for any vacuum |
| Distance-only correction works as well as vacuum-dependent | Vacuum dependence was a red herring; simpler model preferred |

---

## 9. Connection to Open Items in Engine File

| Engine file item | Relevance |
|---|---|
| Fermion mass residual (OPEN) | Direct target of this work |
| dist/30 hierarchy exponent (ESTABLISHED) | Correction modifies the elevator without changing the exponent |
| Assignment problem (OPEN) | Charm displacement is the tightest constraint; branch-point correction may open a new slot |
| ν₂ gap (OPEN) | If correction affects low-distance entries, neutrino predictions change |
| Dead zone (OPEN) | Six entries between eV and keV with no SM occupants. If the branch-point correction modifies the dead zone masses, some entries might shift into or out of the experimentally probed range. The dead zone is the most interesting region strategically: any propagating state found there is a discovery |
| Charm as homeless (NEW) | R4 entries locked to T₃ = -1/2 by Coxeter-Galois gate. Charm needs T₃ = +1/2. Either the gate has a subtlety at the branch point or charm signals a limit of the current formula |
| Galois vacuum enhanced gap (ESTABLISHED) | 9× enhancement at Galois (first allowed k = 5) is the likely source of vacuum-dependent residual at high dist |
| Vertex $`Z_5`$ completion (OPEN) | The $`(1+z)^1`$ term in $`H^2(z)`$ may derive from the vertex stabilizer $`Z_5`$, completing the face/edge/vertex decomposition of the 3/2 accounting. Face ($`Z_3`$) contributes matter dilution, edge ($`Z_2`$) contributes the Friedmann square root. The vertex role in the temporal correction is unwalked. The stabilizer decomposition $`\|2I\| = 2^3 \cdot 3 \cdot 5`$ is the same group whose McKay graph governs the mass formula; the branch point at R8 may be where the vertex contribution becomes visible |

---

## 10. Key Constraints (Revised)

The correction must satisfy:

1. Computed from graph structure and torsion alone (no fitted parameters).
2. Vacuum-dependent (matching the observed pattern: different vacua miss at different distances).
3. Negligible at low distance (preserving up quark 6%, muon 3%; $`m_e`$ is the benchmark).
4. Significant at dist = 5 gal and dist = 7 triv (fixing down quark and top quark).
5. Consistent with the reversal (gal misses at dist 5 but hits at dist 7; triv hits at dist 5 but misses at dist 7).
6. Sensitive to the branch point at R8 (R4 and R5 are reached through a fork).
7. Compatible with (or resolves) the charm displacement at R4.

If constraints 1-6 are satisfied, the correction is structural. If constraint 7 is also satisfied, the charm assignment opens (charm gains a slot it currently lacks). If any of 1-6 require tuning, it's a fit.

---

## 11. Next Steps

1. Compute residuals r(ρ,σ) for all 24 entries against observed masses.
2. Tabulate T²(i ⊗ σ) for all intermediate nodes along each path, for all three vacua.
3. Compute Π_T for each (ρ,σ) entry and check correlation with residual r.
4. Check if the vacuum reversal (gal misses at dist 5, triv misses at dist 7) is explained by intermediate torsion products.
5. Examine the R8 branch point: compute effective branching ratios for R4 vs R5 exit in each vacuum.
6. Check if the branch-point correction modifies the effective j_first at R4, potentially opening a T₃ = +1/2 slot for charm.
7. If a candidate works: apply, recompute full 24-entry scorecard, check charm status, update engine file.
8. If no candidate works: flag as unsolved, document what was tried, record which constraints failed.

---

*The mass ladder is the McKay graph. The correction is in the stairs. The stairs have different treads depending on which vacuum you're climbing in, and the landing at R8 is where the staircase forks.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
