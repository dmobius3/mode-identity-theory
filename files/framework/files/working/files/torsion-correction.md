<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Half-Integer Torsion Correction

**Type:** Result
**State:** Closed
**Status (2026-09-01):** Applied 2026-07-28: the four half-integer torsion singles were the coexact-only truncation; the corrected Ray-Singer values revised twelve of the twenty-four products. This correction reopened the McKay propagator question (see mckay-propagator-correction).
**Summary:** Corrects the four half-integer torsion values on the mass-spectrum table from their coexact-only truncation to the full Ray-Singer closed forms.
**Inputs:** mass-spectrum §4 torsion tables and §III ledger, `mckay-propagator-correction.md`, the registered `mass-null-v1.1` rerun

APPLIED (2026-07-28). The four half-integer torsion singles on [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) were the coexact-only quantity; the full Ray-Singer values carry exact closed forms. 12 of the 24 table entries revised; headline 5-of-8 recomputed to 5 compatible / 4 adjudicated. Verification artifact: [`torsion-correction.test.py`](scripts/torsion-correction.test.py): 12 gates with stable ids, a mutation registry whose meta-guard enforces that the set of mutation targets equals the set of gate ids AND that every declared defect turns its gate red (13 mutations, all red; a gate added without a mutation fails the suite by construction).

---

## 1. The finding

The Ray-Singer torsion of a flat bundle on this space form combines both spectral towers:

```math
\log T^2 = \zeta'_{\text{coexact}}(0) - 2\,\zeta'_{\text{scalar}}(0)
```

For a half-integer irrep the scalar tower is supported at half-integer $`j`$ (odd $`n`$): $`V_1|_{2I} = R_1`$ is the first occupant. The original M5-era computation checked scalar multiplicities at integer $`j`$, found zeros, recorded "scalar sector identically zero for all half-integer irreps," and computed those four torsions from the coexact tower alone. The recomputation reproduces the pre-correction page values as exactly that truncation:

| Irrep | Pre-correction (page) | $`e^{\zeta'_{\text{coex}}(0)}`$ recomputed | Full Ray-Singer (corrected) |
|---|---|---|---|
| $`R_1`$ | 15.887 | 15.8870 | $`\varphi^{-4}/4 = 0.0365`$ |
| $`R_2`$ | 0.473 | 0.4732 | $`\varphi^{4}/4 = 1.7135`$ |
| $`R_6`$ | 4.328 | 4.3284 | $`1`$ |
| $`R_8`$ | 0.257 | 0.2574 | $`4`$ |

The omission is isolated exactly: add the scalar term and the pre-correction values become the corrected ones. The scalar sector is also where the golden ratio enters, which resolves the old record's observed asymmetry ("the $`\varphi`$ mechanism is structurally absent for half-integer irreps") as an artifact of the truncation rather than a property of the torsion.

## 2. What the corrected values satisfy

| Identity | Value | Status |
|---|---|---|
| Sign calibration | $`T^2(R_7) = 9/4`$ | the ONE target that fixes the overall sign convention; its magnitude is still a nontrivial match |
| Independent integer-spin closed forms | $`(4/5)\varphi^{-2}`$, $`25/9`$, $`(4/5)\varphi^{2}`$ | validate the resulting pipeline, 1e-8 |
| Galois pair (integer) | $`T^2(R_3)/T^2(R_4) = \varphi^{-4}`$ | consistency identity, 1e-10 |
| Galois pair (half-integer) | $`T^2(R_1)/T^2(R_2) = \varphi^{-8}`$ | consistency identity, 1e-10; the pair swaps under $`\varphi \to -1/\varphi`$ |
| Sector products | integer $`= 4`$, half-integer $`= 1/4`$ | consistency identities, exact inverses |
| Galois-fixed irreps | $`R_6 = 1`$, $`R_8 = 4`$ (with $`R_7 = 9/4`$, $`R_5 = 25/9`$) | rational, as Galois-fixedness requires |
| Tensor multiplicities $`N_{\rho\sigma\tau}`$ | derived from the reconstructed character table | gated against known decompositions + all 81 dimension sums; the 24-product propagation uses these derived $`N`$, no handwritten constituent lists |

Every value is elementary algebraic in $`\mathbb{Q}(\varphi)`$, uniformly across both spin parities.

## 3. Consequences on the ledger

12 of 24 products revised (the triv column of half-integer rows; the std/gal columns of integer rows; every product built purely from integer constituents is unchanged, including both non-acyclic diagonals). On the [mass-spectrum](../../../../spectrum/files/mass-spectrum.md) comparison: the electron benchmark, muon/strange, and down are unchanged; the top's nearest compatible entry becomes $`(R_2,\text{triv})`$ at 0.93; the tau moves to the $`(R_4,\text{gal})`$ singlet channel at 2.75; the up quark's former 6% hit was an artifact of the truncated torsion and the up is now unassigned; the bottom's nearest compatible coverage improves to 1.17, still unassigned under the sector-first rule. Headline: 5 of 8 compatible coverage, 4 of 8 adjudicated (pre-correction: 8/6/5). The $`R_1`$ sector becomes an ascending ladder (0.87, 7.3, 66.7 meV) in ordered qualitative resemblance to the observed splitting scales (splitting-level ratios 0.72 and 1.8), carried as proxy comparison only. The 2026-06 propagator elimination analyzed the pre-correction residuals and does not transfer; that question was reopened on the mass-spectrum §VI ledger and has since closed negative on the corrected table ([McKay Propagator Correction](mckay-propagator-correction.md#retest-result)).

## 4. Scope: what is and is not established

| Claim | Status |
|---|---|
| One exact target, $`T^2(R_7) = 9/4`$, fixes the overall sign convention; the remaining integer-spin closed forms validate the resulting pipeline; the Galois ratios and sector products are consistency identities | CERTIFIED at those grades |
| The pre-correction half-integer values equal the coexact-only truncation | CERTIFIED (4/4 at page precision; the diagnosis gate) |
| The tensor multiplicities and the 24-product propagation | derived in-script from the reconstructed character table and gated (known decompositions, dimension sums, revised-mass transcription, 12 unchanged products at ratio 1) |
| The corrected half-integer closed forms | REPRODUCED by a context-isolated independent-method run (OpenWave M8.8, adjudicated 2026-08-22): § 8 category `convention difference`, global inverse at $`R_7`$, 8/8 rows exact in $`\mathbb{Q}(\varphi)`$, 4/4 identities equal; see §6 |
| The corrected scorecard's statistical weight | `mass-null-v1.1` was executed 2026-07-28 against the corrected table and returned $`p_A = 0.690`$, in the uninformative band. The corrected $`\times 3`$ proximity count is therefore tested and null **as evidence for the specific torsion assignment**; the torsion algebra and the structural construction are not what this null tests |

## 5. Reproduce

```
python3 torsion-correction.test.py                   # 12 gates
python3 torsion-correction.test.py --mutation-tests  # coverage-enforced registry, 13 defects red
python3 torsion-correction.test.py --precise         # dps 50, jmax 80, derivative step 1e-5
```

Environment: python3 + numpy + mpmath. Every gate id must be attacked by at least one mutation (set equality enforced) and every mutation must turn its gate red, else the suite exits nonzero; the registry includes the original defect itself (running coexact-only breaks the corrected closed forms) and harness tests (perturbed transcription targets must fail their gates).

## 6. Independent-method reproduction (OpenWave M8.8, 2026-08-22)

[![OpenWave M8.8](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_adjudication_record.md)

**Result.** The nine closed forms above were reproduced by a context-isolated independent-method run, from a based chain complex of $`S^3/2I`$ over $`\mathbb{Z}[2I]`$ in exact $`\mathbb{Q}(\varphi)`$ arithmetic, rather than from the spectral-zeta definition this artifact uses. The protocol's § 8 category is `convention difference`: the run's native orientation is $`T^2 \leftrightarrow (T^2)^{-1}`$ relative to this page, the one convention bridge the protocol admitted, resolved at $`R_7`$ before any other row was compared; under that global inversion, 8 of 8 nontrivial rows agree exactly, 4 of 4 identities (two Galois ratios, two sector products) agree, sector coverage 8 of 8. The category is a success under the protocol, carrying the same claim as `reproduced` with the orientation recorded. The supplied topological model was verified by the run, not independently derived.

**Frozen label**, verbatim from the protocol: the M8.3 torsion closed forms were reproduced by a context-isolated independent-method run, from a based chain complex rather than the spectral-zeta definition. The word "blind" is not used: for an AI implementer the training corpus is opaque, so blindness cannot be certified even under perfect task-time isolation.

**Adjudication provenance**, fixed before the official run: the successful adjudication was obtained on a separately recorded rerun after the initially committed comparator refused pre-comparison on an exact packet-domain spelling mismatch; the post-reveal repair changed that frozen-builder literal only and altered neither the committed reproduction output nor the comparison semantics. Attempt 1 stands on record as `structural failure` at the step-7 packet-domain gate, beside attempt 2; both records are published.

| Object | Where |
|---|---|
| Protocol, with Addendum 1 (the Phase A / Phase B split) | [m8_8_reproduction_protocol.md](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_reproduction_protocol.md) |
| Adjudication record, both attempts, the byte-identity control, the governance note | [m8_8_adjudication_record.md](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/findings/m8_8_adjudication_record.md) |
| The answer packet this artifact issued, published at step 9 against its frozen hash | `data/m8_8_answer_packet.json` on the same tree, SHA-256 `744c7f25…` |
| The packet builder, with pinned inputs and a recipe that regenerates that hash | `m8_8_answer_builder/` on the same tree |

**What this does and does not change here.** Row 4 of §4 moves from one implementation to two independent methods in exact agreement. Nothing else in this note moves: the single-target orientation fix, the coexact-only diagnosis, the 24-product propagation and the null-test status are as stated, and the reproduction does not bear on whether the torsion values fit the measured masses, which `mass-null-v1.1` already answered.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
