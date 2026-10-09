<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Torsion Null Test

**Type:** Test
**State:** Closed
**Verdict:** Uninformative
**Status (2026-07-28):** v1.1 executed (p_A = 0.690): randomly reassigning the 24 torsion factors across the fixed quantum-number slots reproduces or exceeds the observed ×3 coverage in 69% of draws, so the proximity count is uninformative about the specific torsion values. The structural outputs and outliers carry the weight.
**Summary:** A pre-registered null test asking whether the mass scorecard's within-×3 hit rate carries information about the specific torsion values, or is density.
**Inputs:** the mass formula and 24-entry table (mass-spectrum §II-III), the torsion tables, the Coxeter-Galois gate and stabilizer decompositions
**Frozen:** 2026-07-11 the v1.0 design and 2026-07-28 the v1.1 registration, each frozen before its run

v1.0 EXECUTED (2026-07-11, Results below); **v1.1 EXECUTED (2026-07-28: registered §IX, run §X, $`p_A = 0.690`$, uninformative band)** against the corrected torsion table. The v1.0 record (§I-§VIII and its Results) is the frozen history of the pre-correction run and is not edited; v1.1 changes the inputs only and retains the statistic, the four nulls, the scoring rule, the seed, and the decision bands verbatim.

> **Re-baselined to the canonical torsion table (2026-07-11).** The torsion inputs are the canonical values from [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) §4, including $`T^2(R_0) = 1`$: the canonical topological value of the non-acyclic trivial local system, not a constant chosen for convenience. This re-baseline updated only the *inputs the test reads*. The statistic, the four nulls, the scoring rule, the RNG seed (120), and the §VII decision bands are unchanged from the pre-correction design. Input error is correctable; the statistic and verdict bands are retained unchanged and are proposed for freeze, the same line drawn for the mass table. The null statistic is $`S_1 = 6`$ (a compatible-coverage count) while the public headline is 5-of-8 (an assignment count); §I explains why the two differ by exactly one fermion.

**The claim under audit** ([mass-spectrum.md](../../../../spectrum/files/mass-spectrum.md), §III): the ×3 proximity comparison. Under the compatible-coverage reading (§I), $`S_1 = 6`$ of the 8 scored charged fermions have a quantum-number-compatible entry within a factor of 3 (down outside at 3.22, charm without a compatible entry). The page's assignment headline is 5 of 8; §I explains the one-fermion difference. The page states the caveat this test quantifies: "at this entry density a measured mass sits near some entry largely by counting."

**Related:** [Claim Ledger](claim-ledger.md), [McKay Propagator Correction](mckay-propagator-correction.md) (negative on the pre-correction table, and again on the corrected one, its primary form in a registered re-test; its residual scatter is context for this test), [R from the Mass Spectrum](r-from-mass-spectrum.md).

---

## I. The Question

How much of the compatible-coverage count ($`S_1 = 6`$, §IV) survives when the corrected torsion-factor values are randomly reassigned across the entry table, holding everything else fixed?

The formula is $`m(\rho, \sigma) = \mu_\Lambda \cdot C_{\text{geom}}(\rho) \cdot (\sqrt{\Omega_\Lambda})^{\text{dist}(\rho)/30} \cdot T^2(\rho \otimes \sigma)`$. The first three factors set the coarse ladder (thirteen orders of magnitude of placement); the torsion is the fine dial within each shell. This test isolates the dial. It does not test the ladder, the entry count, the quantum-number gates, or the exact ratios; those are held fixed as the skeleton, and their standing is unaffected by any outcome here.

**The null statistic is a compatible-coverage count, not the public assignment scorecard, and the two differ by one fermion for a principled reason.** The [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) headline reports **5 of 8** under an assignment-level no-slide standard: once $`(R_2,\text{gal})`$ is named the bottom quark's entry and it sits at 197 GeV under the canonical torsion, the nearest survivor is not renamed to hold the count. This test scores **$`S_1 = 6`$** under a slot-availability standard: its pre-registered rule (§IV) asks whether *any* quantum-number-compatible slot lies within ×3, and the bottom quark is covered by $`(R_4,\text{gal})`$ at ratio 1.40. The one-entry gap between the two counts is exactly the bottom quark, which is precisely the fermion whose hit is density-supplied rather than uniquely assigned. The gap is informative, not a disagreement: it localizes, to a single fermion, where the ×3 count depends on density versus unique assignment. "No-slide" is meaningful only for a fixed assignment; under torsion randomization there is no assignment to slide, so the any-compatible rule of §IV is the pre-registered statistic appropriate to the compatible-coverage question.

**The canonical-torsion correction is itself a first data point for this test.** Correcting one load-bearing torsion value, $`T^2(R_0)`$, displaced the original bottom-quark entry $`(R_2,\text{gal})`$ by a factor of 37, yet the coverage count did not move: a compatible slot $`(R_4,\text{gal})`$ was already inside the ×3 window. That is a natural out-of-sample perturbation illustrating the process the ensemble samples: perturb a torsion, ask whether a fermion keeps a compatible slot nearby. It did. (It is not itself a draw from the registered null: the correction was a deterministic provenance fix to one base factor, not a randomization.) The correction is a hand-computed preview of the density effect the null test exists to quantify, pointing the same way the test predicts, which makes the test more necessary, not less.

---

## II. What Is Frozen (the skeleton)

| Item | Frozen value / source |
|---|---|
| Overall scale $`\mu_\Lambda`$ | $`\rho_\Lambda^{1/4} \approx 2.25`$ meV, from measured $`\Lambda`$; no refit per draw |
| Seats $`C_{\text{geom}}(\rho)`$ | the 8 published values (mass-spectrum.md §II.2) |
| Elevator | $`(\sqrt{\Omega_\Lambda})^{\text{dist}(\rho)/30}`$, $`\sqrt{\Omega_\Lambda} = 1.019 \times 10^{61}`$, McKay distances as published |
| Quantum numbers per slot | $`(T_3, \text{color channels}, Q)`$ for all 24 $`(\rho, \sigma)`$ slots, computed from the published rules (spectral parity, Coxeter-Galois gate, $`Z_3`$ channels, Gell-Mann-Nishijima); torsion-independent by construction |
| Scoring rule | Section IV below, verbatim |
| Measured masses (GeV) | $`u`$ $`2.16 \times 10^{-3}`$, $`d`$ $`4.67 \times 10^{-3}`$, $`s`$ $`9.34 \times 10^{-2}`$, $`c`$ $`1.27`$, $`b`$ $`4.18`$, $`t`$ $`172.7`$, $`\mu`$ $`1.057 \times 10^{-1}`$, $`\tau`$ $`1.777`$ (page values, except $`c`$ $`1.27`$ imported from PDG since the page leaves charm unassigned; charm is the one mass not traceable to the source page, and is a miss under both scoring rules, so nothing turns on it) |
| Excluded from scoring | electron (benchmark), the three neutrinos (absolute masses unmeasured) |

The quantum-number map is skeleton because every ingredient of the gates ($`j_\text{first}`$ parity, the $`(13,17)`$ Coxeter pair, Galois-fixed content, $`Z_3`$ channels) is representation theory with no torsion input. Reassigning torsions moves masses; it never moves a slot's kind.

---

## III. What Is Randomized (four nulls)

| Null | Operation | Question it answers |
|---|---|---|
| **A (primary)** | Permute the 24 published $`T^2(\rho \otimes \sigma)`$ values uniformly across the 24 slots | Do the specific value-to-slot pairings matter at all, or does density plus spread suffice? |
| B | Permute within each vacuum column separately ($`8!`$ each) | Same, controlling for each vacuum's torsion distribution |
| C | Redraw each $`\log T^2`$ i.i.d. log-uniform over the observed 24-value range | Does anything beyond the overall spread matter? |
| D | Permute the 9 base torsions $`T^2(\tau)`$ within spin class ($`R_3, R_4, R_5, R_7`$ among themselves; $`R_1, R_2, R_6, R_8`$ among themselves; $`R_0`$ fixed at its canonical topological value $`1`$), then re-derive all 24 via $`\log T^2(\rho \otimes \sigma) = \sum_\tau N_{\rho\sigma\tau} \log T^2(\tau)`$ | The structure-preserving counterfactual: does it matter which irrep carries which torsion, keeping the tensor algebra intact? |

Null A is primary because it is the direct reading of the published caveat ("a random reassignment of the torsions, holding the quantum-number structure fixed"). Null D is the sharpest secondary: it respects the generative algebra, its ensemble is exactly enumerable ($`4! \times 4! = 576`$ permutations, no Monte Carlo error), and a divergence between A and D would itself be informative (it would mean the tensor rule, not the base values, carries the fit).

The verdict hangs on Null A alone. B, C, D are reported as texture and cannot rescue or overturn the primary verdict.

---

## IV. The Scoring Rule (frozen)

For each of the 8 scored fermions $`f`$ with measured mass $`m_f`$:

1. A slot $`(\rho, \sigma)`$ is **compatible** with $`f`$ iff its frozen quantum numbers admit $`f`$'s kind: matching $`T_3`$, and a color channel of $`f`$'s type (singlet for leptons, colored pair for quarks), with $`Q`$ closed by Gell-Mann-Nishijima.
2. $`f`$ **hits** iff some compatible slot has $`\max(m_f/m_{\text{slot}},\ m_{\text{slot}}/m_f) \leq 3`$.
3. Sharing is allowed: two fermions of different kind may hit the same slot through different channels (the published $`\mu/s`$ case at rank 15).

At freeze time the compatibility relation is committed as a machine-readable $`8 \times 24`$ matrix $`C_{f,s} \in \{0,1\}`$ (the full 24-slot quantum-number map is the Step-0 deliverable, §VI); the execution code reads $`C`$ and does not re-derive compatibility during the ensemble. Reproduction gate G3 checks the matrix itself, not only the resulting $`S_1`$.

Primary statistic $`S_1`$ = number of the 8 that hit. Observed scorecard under this rule (compatible coverage, §I):

| $`f`$ | best compatible ratio | hit at $`\times 3`$? |
|---|---|---|
| $`u`$ | 1.06 | yes |
| $`d`$ | 3.23 | no |
| $`s`$ | 1.10 | yes |
| $`c`$ | none within ×3 (nearest compatible from Step-0 map) | no |
| $`\mu`$ | 1.02 | yes |
| $`\tau`$ | 2.42 | yes |
| $`b`$ | 1.40 (via $`(R_4,\text{gal})`$) | yes |
| $`t`$ | 1.51 | yes |

Observed $`S_1 = 6`$. (The bottom quark's covering slot $`(R_4,\text{gal})`$ and charm's non-coverage are the same structural fact: $`R_4`$ has integer $`j_\text{first}`$ at every vacuum, hence $`T_3 = -1/2`$ throughout, a down-type-only irrep that houses $`b`$ and excludes the up-type charm.)

**Secondaries, computed identically on real and null spectra.** Logarithms are natural throughout. For each fermion $`f`$ with at least one compatible slot, the **witness slot** is $`s_f^\star = \arg\min_{s:\,C_{f,s}=1} |\ln(m_s/m_f)|`$, ties broken by the slot's index in the frozen 24-slot list. Then: $`S_2`$ = hits at $`\times 2`$; $`S_3`$ = hits at $`\times 1.5`$; $`S_4 = \operatorname{median}_f\, |\ln(m_{s_f^\star}/m_f)|`$ over all eight scored fermions; $`S_5`$ = number of distinct witness slots $`s_f^\star`$. Charm is up-type and colored, so it has a compatible slot: its witness is $`(R_2,\text{triv})`$ at ratio 35.09 (outside $`\times 3`$), so all eight fermions carry a witness. On the real spectrum the observed secondaries are $`S_2 = 5`$, $`S_3 = 4`$, $`S_4 = 0.375`$, $`S_5 = 7`$. These are Step-0 deterministic (not ensemble outputs), and they are the frozen thresholds each secondary $`p`$-value is computed against, pinned here before the run.

*Note on the color gate.* On the scored fermion set the color-channel test carries no independent discriminating power: the only slots lacking a color-singlet channel are $`(R_1,\text{triv})`$ and $`(R_2,\text{triv})`$, both $`T_3 = +1/2`$, while both scored leptons are $`T_3 = -1/2`$, so compatibility here reduces to a $`T_3`$ match. The color logic is derived and validated (gate G3a); a reviewer should not read independent coverage into it.

One scoring variant is also pre-registered: $`S_1'`$ = hits at $`\times 3`$ **ignoring compatibility** (proximity to any slot), measuring raw density with no quantum-number skeleton. On the real spectrum $`S_1' = 8`$: every fermion has some slot within $`\times 3`$. The three structurally forbidden coverings it counts, and which the compatibility gate removes, are frozen here as witnesses: $`(t,\ \text{down-type 197 GeV orphan})`$ at 1.14, $`(d,\ \text{up-quark slot at } 2.03 \times 10^{-3})`$ at 2.30, and $`(c,\ \text{tau slot at } 0.734)`$ at 1.73. Of these, $`d`$ and $`c`$ have no compatible slot within $`\times 3`$, so the gate drops them ($`8 \to 6`$); $`t`$ also hits compatibly via $`(R_2,\text{std})`$ at 1.51, so its forbidden covering is redundant to the count. A high $`S_1'`$ null therefore speaks only to raw density and carries no bearing on the gated count; the gates take the real spectrum from $`S_1' = 8`$ (raw density) to $`S_1 = 6`$ (compatible coverage) to 5 (assignment).

---

## V. Ensembles, Seed, Single Run

Nulls A, B, C: $`M = 100{,}000`$ draws each. Null D: exact enumeration (576). RNG seed fixed at **120**. One execution, no re-draws, no post-hoc statistics beyond those named above. Reported per null: the full distribution of each statistic (as a count table), its mean and standard deviation, and its one-sided $`p`$-value with the tail direction fixed below.

Each statistic's tail is fixed now, before any draw:

| statistic | observed | tail | reported $`p`$ |
|---|---|---|---|
| $`S_1`$ | 6 | upper | $`\Pr(S_1 \geq 6)`$ |
| $`S_2`$ | from run | upper | $`\Pr(S_2 \geq S_2^{\text{obs}})`$ |
| $`S_3`$ | from run | upper | $`\Pr(S_3 \geq S_3^{\text{obs}})`$ |
| $`S_1'`$ | 8 | upper | $`\Pr(S_1' \geq 8)`$ |
| $`S_4`$ | from run | lower | $`\Pr(S_4 \leq S_4^{\text{obs}})`$ |
| $`S_5`$ | from run | none | distribution, mean, SD; no one-sided $`p`$ |

Upper tail for the count statistics ($`S_1, S_2, S_3, S_1'`$) because more or closer hits is the fit-favoring direction; lower tail for $`S_4`$ because a smaller median log-distance is; $`S_5`$ is reported descriptively, since neither direction is privileged for a distinct-slot count. For the exact Null D, $`p_D = \#\{\text{permutations at least as extreme as observed}\}/576`$ with the identity permutation included; the $`(k+1)/(M+1)`$ estimator applies only to the Monte Carlo Nulls A-C.

**Numerical and Monte Carlo conventions (committed at freeze).** This is a **published-precision test**: it audits the source table at its displayed precision ($`C_\text{geom}`$ to 4 dp; the four half-integer base torsions $`R_1, R_2, R_6, R_8`$ to 3-5 significant figures; the closed forms $`R_0, R_3, R_4, R_5, R_7`$ exact). The RNG is NumPy `Generator(PCG64)` seeded at 120; permutations act on the 24 factors as indexed positions (`slot_index`), so equal values remain distinct entries. Null C draws $`\log T_i^2 \overset{\text{iid}}{\sim} \operatorname{Uniform}\!\left[\min_j \log T_j^2,\ \max_j \log T_j^2\right]`$ over the committed factors. The Monte Carlo point estimator (Nulls A-C) is $`\hat p = (k+1)/(M+1)`$, which never reports zero, quoted with its binomial standard error; Null D uses the exact fraction. The §VII verdict bands use the point estimator only; the interval is numerical uncertainty and does not trigger a re-run, including when $`\hat p_A`$ falls near 0.01 or 0.1.

**Frozen artifacts.** The execution script `mass-null-test.py` builds the $`2I`$ character table from the icosians and derives the map, masses, tensor multiplicities $`N_{\rho\sigma\tau}`$, and compatibility matrix from scratch; it also emits and verifies the three committed input artifacts. Recorded SHA-256 (a run checks it is reading the tagged inputs):

```
mass-null-inputs.json   731e4a67b5916e72a290e6e70b50e42620cddc88b0ae859dc2fef47eeac59a2f
mass-null-slotmap.csv   23307267c0669150ed025164bb46960385ec2dcbfe1836e7061fc390892bcfbd
mass-null-compat.csv    d7b4def487bb25c0b944dc8dc336913010448a67a02a9452c5c3fa12729ac9cd
```

`mass-null-inputs.json` holds the base torsions, $`C_\text{geom}`$, cosmological inputs, $`N_{\rho\sigma\tau}`$, $`j_\text{first}`$, and fermion data; `mass-null-slotmap.csv` the 24-slot map ($`\text{mass}, T^2, T_3`$, color, `slot_index`); `mass-null-compat.csv` the $`8\times24`$ matrix. The four nulls, the fixed-tail $`p`$-values, and the tag-gated single-run policy are implemented in the same script, so the randomization is frozen in the committed bytes.

---

## VI. Step 0: Reproduction Gates

The pipeline must pass these deterministic gates before any randomization runs; `mass-null-test.py` runs them by default. Each compares the **committed artifacts** against an **independent from-scratch derivation** (the $`2I`$ character table rebuilt from the icosians, its tensor products, the gates, and the map), so a transcription error in the committed inputs is caught, not reproduced. Failing a gate stops the test and opens a reconciliation item against the source page.

- **G1 (masses):** the committed slot-map masses match the independently derived masses to $`\texttt{rtol} = 10^{-12}`$, $`\texttt{atol} = 10^{-15}`$.
- **G2 (torsions):** the committed slot-map $`T^2`$ match the independently derived $`T^2`$ (rebuilt from the 9 base values via $`\log T^2(\rho\otimes\sigma) = \sum_\tau N_{\rho\sigma\tau}\log T^2(\tau)`$) to the same tolerance. A separate coarse check compares against the published display, e.g. $`T^2(R_6)\cdot T^2(R_8) = 4.328 \times 0.257 = 1.112`$ from the rounded inputs against the page's 1.114; the diagonals carry the canonical $`T^2(R_0) = 1`$.
- **G3a (compatibility matrix):** the independently derived $`8 \times 24`$ matrix $`C_{f,s}`$ matches the committed CSV exactly, and `slot_index` is stable across both.
- **G3b (scorecard):** the committed matrix on the real spectrum returns $`S_1 = 6`$ and $`S_1' = 8`$ with the named witnesses ($`b`$ via $`(R_4,\text{gal})`$ at 1.40, $`\mu/s`$ sharing rank 15, $`d`$ out at 3.23, charm's nearest compatible $`(R_2,\text{triv})`$ at 35.09), and the $`T_3`$ gate reproduces all ten published §IV.4 entries. The 5-vs-6 gap against the public assignment headline is expected (§I), not a gate failure.

The full 24-slot quantum-number map (the published page prints only the 10 SM-assigned rows) is completed from the stated rules by the derivation and frozen as `mass-null-slotmap.csv`; it also completes §IV.4 from 10 rows to 24, independently of this test.

---

## VII. Decision Ledger (pre-named verdicts)

The number itself is the deliverable; the bands only fix the headline language in advance.

- **$`p_A \geq 0.1`$:** the $`\times 3`$ comparison is declared uninformative about the torsion dial. Verdict text: "Random torsion reassignment reproduces the published hit rate; the mass table's evidential weight rests on the exact structural outputs (the 24-entry count, the ten-entry $`T_3`$ gate audit, the $`\varphi^{-4}`$ ratio) and the falsifiable outliers ($`\nu_2`$, rank 16, the dead zone), not on the $`\times 3`$ proximity count."
- **$`p_A \leq 0.01`$:** the torsion values carry fit information beyond density. Verdict text: "Random reassignment does not reproduce the published hit rate; the fine dial is doing measurable work. The comparison remains a comparison, and this does not validate the mechanism."
- **$`0.01 < p_A < 0.1`$:** inconclusive at the $`\times 3`$ window; the tighter-window secondaries and Null D govern the discussion, and no headline change is licensed in either direction.

**What this test cannot say.** Nothing about the skeleton it holds fixed: the entry count, the gates, the exact ratios, the elevator exponents, or the neutrino sector. A low $`p_A`$ does not validate the formula's mechanism; a high $`p_A`$ does not falsify it. The test measures one thing: whether the $`\times 3`$ scorecard is evidence about the torsions.

**Propagation.** The verdict sentence is copied, on execution, into: the mass-spectrum §III preamble and headline table, the framework README "What the formula delivers" paragraph, the claim-ledger mass-comparison row, and the working README (Data Tests section, with verdict).

---

## VIII. Protocol

1. **Draft** (this commit): design public, no ensemble run.
2. **Redline:** review pass; adjustments land as visible commits against the draft.
3. **Freeze:** status flips to REGISTERED; the execution script `mass-null-test.py` and the three input artifacts (`mass-null-inputs.json`, `mass-null-slotmap.csv`, `mass-null-compat.csv`; hashes in §V) are committed alongside; tag `mass-null-v1.0`. The script's `--run` refuses unless HEAD carries that tag, so the registered ensemble cannot predate the freeze. An archival DOI at the freeze tag is optional, following the SPARC pattern.
4. **Run:** single execution; outputs (distribution tables, p-values) and the filled Results section land in one commit.
5. **Propagate:** the verdict sentence to the four locations above, one commit.

Design and execution are separated by the freeze tag, so the git history is the audit trail: anyone can verify the ensembles were specified before they were drawn.

---

## Results

*Executed 2026-07-11 at the frozen tag `mass-null-v1.0`, `Generator(PCG64)` seed 120, 76 s. Single run, no re-draws. Full output: `mass-null-results.json`.*

**Primary verdict (Null A): $`p_A = \Pr(S_1 \geq 6) = 0.174`$, in the $`p_A \geq 0.1`$ band.** Random reassignment of the torsion values across the 24 slots reproduces the observed hit rate: the null $`S_1`$ averages 4.50, and 17% of random reassignments match or beat the observed 6.

| Null | $`p(S_1 \geq 6)`$ | $`p(S_1' \geq 8)`$ | $`p(S_2)`$ | $`p(S_3)`$ | $`p(S_4 \leq)`$ | null $`S_1`$ mean |
|---|---|---|---|---|---|---|
| A (primary) | 0.174 | 0.209 | 0.179 | 0.189 | 0.080 | 4.50 |
| B | 0.144 | 0.198 | 0.157 | 0.149 | 0.058 | 4.31 |
| C | 0.316 | 0.440 | 0.265 | 0.200 | 0.077 | 4.78 |
| D (exact, 576) | 0.326 | 0.323 | 0.375 | 0.396 | 0.215 | 4.77 |

Null A $`S_1`$ count table: $`\{1{:}45,\ 2{:}1935,\ 3{:}13816,\ 4{:}37758,\ 5{:}29079,\ 6{:}13490,\ 7{:}3877\}`$. Every null and every secondary lands well above 0.01; the tightest ($`S_4`$, lower tail) is 0.06-0.08. Nothing approaches significance in either direction.

**Verdict (§VII, $`p_A \geq 0.1`$).** Random torsion reassignment reproduces the published hit rate; the mass table's evidential weight rests on the exact structural outputs (the 24-entry count, the ten-entry $`T_3`$ gate audit, the $`\varphi^{-4}`$ ratio) and the falsifiable outliers ($`\nu_2`$, rank 16, the dead zone), not on the $`\times 3`$ proximity count.

---

## IX. v1.1 Re-registration (2026-07-28): the corrected torsion table

**Status: REGISTERED at the tag `mass-null-v1.1`, before any v1.1 ensemble is drawn.** The [half-integer torsion correction](torsion-correction.md) revised 12 of the 24 entries (mass-spectrum §4 correction note), so the v1.0 result ($`p_A = 0.174`$) is the frozen record of the pre-correction table and does not transfer. This section re-registers the identical test against the corrected table.

**What changed: the inputs, nothing else.** The four half-integer base torsions become their exact closed forms, $`T^2(R_1) = \varphi^{-4}/4`$, $`T^2(R_2) = \varphi^{4}/4`$, $`T^2(R_6) = 1`$, $`T^2(R_8) = 4`$, so all nine base factors are now exact ($`C_\text{geom}`$ stays at its 4 dp published precision). The statistic ($`S_1`$ compatible coverage), the four nulls (A primary; B, C, D texture), the §IV scoring rule, the RNG seed (120), the ensemble sizes ($`M = 100{,}000`$; Null D exact 576), the fixed tails, the §VII decision bands and verdict language, and the single-run policy are retained from v1.0 byte-for-byte in the rule machinery. The script's `--run` now refuses unless HEAD carries `mass-null-v1.1`; v1.1 results write to `mass-null-results-v1.1.json`, preserving the v1.0 results file.

**The skeleton claim, verified at the byte level.** The compatibility matrix `mass-null-compat.csv` is byte-identical to v1.0 (same SHA-256): the correction moved 12 masses and no slot's quantum numbers, exactly as §II's torsion-independence argument requires. The frozen v1.1 artifact hashes:

```
mass-null-inputs.json   9efcd3f0766239d814745e184cab56dae2be2ba098cf773ea66a707e2d622237
mass-null-slotmap.csv   86ddf8184f0df42df56704359c3d46a1c6bfbd24c9606d1905a7f671b85d34ce
mass-null-compat.csv    d7b4def487bb25c0b944dc8dc336913010448a67a02a9452c5c3fa12729ac9cd   (unchanged from v1.0)
```

**Observed scorecard on the corrected table (Step-0 deterministic, frozen here; all 12 reproduction gates pass).**

| $`f`$ | best compatible slot | ratio | hit at $`\times 3`$? |
|---|---|---|---|
| $`u`$ | $`(R_8,\text{triv})`$ at 31.6 MeV | 14.61 | no |
| $`d`$ | $`(R_8,\text{gal})`$ | 3.23 | no |
| $`s`$ | $`(R_8,\text{std})`$ | 1.11 | yes |
| $`c`$ | $`(R_8,\text{triv})`$ | 40.23 | no |
| $`\mu`$ | $`(R_8,\text{std})`$ | 1.02 | yes |
| $`\tau`$ | $`(R_4,\text{gal})`$ | 2.75 | yes |
| $`b`$ | $`(R_4,\text{gal})`$ | 1.17 | yes |
| $`t`$ | $`(R_2,\text{triv})`$ | 1.07 | yes |

Frozen observed statistics: $`S_1 = 5`$, $`S_1' = 6`$, $`S_2 = 4`$, $`S_3 = 4`$, $`S_4 = 0.58425`$, $`S_5 = 5`$. Tails as in §V with the observed values substituted (primary: $`\Pr(S_1 \geq 5)`$ under Null A).

Two structural notes, both the v1.0 §I geometry recurring one notch down. The compatible-coverage count (5) again exceeds the page's adjudicated-within-×3 count (4) by exactly the bottom quark, whose covering slot $`(R_4,\text{gal})`$ at 1.17 is outside its $`R_2`$ structural sector: the same single-fermion localization of density-versus-assignment as v1.0. And the raw-vs-gated gap ($`S_1' = 6`$ vs $`S_1 = 5`$) is now the up quark alone, whose only ×3 covers are the two electron-candidate slots $`(R_7,\text{std})`$ and $`(R_7,\text{gal})`$ at 2.33, both $`T_3 = -1/2`$ charged-lepton slots the gate correctly forbids to an up-type quark.

**Decision bands.** §VII verbatim, read against the corrected table: $`p_A \geq 0.1`$ declares the ×3 comparison uninformative about the torsion dial; $`p_A \leq 0.01`$ declares the values carry fit information beyond density; between, inconclusive, no headline change licensed. The §VII propagation list applies on execution.

---

## X. v1.1 Results

*Executed 2026-07-28 at the frozen tag `mass-null-v1.1`, `Generator(PCG64)` seed 120, 40 s. Single run, no re-draws. Full output: `mass-null-results-v1.1.json`.*

**Primary verdict (Null A): $`p_A = \Pr(S_1 \geq 5) = 0.690`$, in the $`p_A \geq 0.1`$ band.** Random reassignment of the corrected torsion values across the 24 slots reproduces the observed coverage: the null $`S_1`$ averages 5.02 against the observed 5, so on the corrected table the ×3 compatible-coverage count is not merely reachable by chance, it is the typical outcome of a random torsion assignment. The verdict is the same as v1.0's and cleaner: v1.0's observed 6 sat in the null's upper 17%; v1.1's observed 5 sits at the null's center.

| Null | $`p(S_1 \geq 5)`$ | $`p(S_1' \geq 6)`$ | $`p(S_2)`$ | $`p(S_3)`$ | $`p(S_4 \leq)`$ | null $`S_1`$ mean |
|---|---|---|---|---|---|---|
| A (primary) | 0.690 | 0.854 | 0.567 | 0.289 | 0.338 | 5.02 |
| B | 0.709 | 0.853 | 0.573 | 0.298 | 0.335 | 5.03 |
| C | 0.755 | 0.912 | 0.654 | 0.266 | 0.350 | 5.24 |
| D (exact, 576) | 0.854 | 0.809 | 0.844 | 0.443 | 0.448 | 5.44 |

Null A $`S_1`$ count table: $`\{1{:}19,\ 2{:}747,\ 3{:}7724,\ 4{:}22520,\ 5{:}33667,\ 6{:}28434,\ 7{:}6416,\ 8{:}473\}`$. Every null and every secondary sits far from significance in either direction.

**Verdict (§VII, $`p_A \geq 0.1`$ band, read against the corrected table).** Random torsion reassignment reproduces the corrected table's hit rate; the ×3 proximity count is uninformative about the torsion dial, and the mass table's evidential weight rests on the exact structural outputs (the 24-entry construction, the $`T_3`$ gate evaluations, and the closed-form torsion algebra: the Galois pairs $`\varphi^{-4}`$ and $`\varphi^{-8}`$, the exact-inverse sector products, $`R_7`$'s Galois-blind 4) together with the falsifiable outliers (the neutrino ladder's ordering, rank 16, the dead zone), not on the ×3 proximity count. The §VII sentence named the pre-correction outliers ($`\nu_2`$, rank 16, the dead zone); the corrected page's outlier set reads as above, with the $`\nu_2`$ gap replaced by the ladder's falsifiable ordering.

**What this run cannot say** is unchanged from §VII: nothing about the skeleton it holds fixed, and a high $`p_A`$ does not falsify the formula's mechanism. It measures one thing: on the corrected table, the ×3 scorecard is not evidence about the torsions. The structural outputs carry the evidential weight, exactly where the corrected page already places it.

---

*The ladder is held. The dial is shuffled. The count speaks for itself.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
