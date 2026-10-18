# M8.16 development log (append-only)

Each entry is added at the bottom and never edited. A correction is a new entry. Each run entry gives the time (UTC), the script and its SHA-256, the case (it must be on BOUNDARY.md's GO list), the outcome, and any tolerance it informed, with how.

## 0. 2026-10-15T19:41:15Z: the boundary fixed

BOUNDARY.md written, SHA-256 `909433a7cc7df144efbee6a38d96f793f91b8676e28456e259ab30c172416f2d`. No M8.16 code exists yet. No run of any kind has been made.

## 1. 2026-10-15T19:47:27Z: arithmetic, not an instrument run

`dev/dims.py`, SHA-256 `fe68bbca1fdb6f26fa1a2466ffafdbccc1533d5d33fce15d7b24f5bc0d96e2f7`, output `dev/dims.out`, SHA-256 `a6c6138aa23f99a3ef3378b098c29d9344198760700d64e2a6b6e2b044a28ed3`. 2I's characters give each slot's section dimension at complete levels n ≤ N, for N ∈ {16, 24, 32, 40, 48}. The slots are R1 to R8, and R0 is untouched. No field, no basis, no solve. The lowest levels (1, 7, 2, 6, 6, 3, 4, 5) and dimensions (2, 2, 3, 3, 4, 4, 5, 6) match `soft_quartic.py`. It informed DESIGN.md §9's table. It set no tolerance.

DESIGN.md v1 written, SHA-256 `a1bfcb38ecd5ced4baee193c0784e247c019805edd1642075efa830266dccc09`. It is a draft for review, and governs no run.

## 2. Between 19:47:27Z and 20:01:50Z: C2's § 4.1 read, after DESIGN.md v1

The M8.5-C2 protocol's public § 4.1, its production quadrature, was read to check UB's comparison for the provenance line. It came from OpenWave main at 50c359e9, `research/findings/m8_5c2_protocol.md`. It was not read before DESIGN.md v1 was written and hashed (entry 1). No C2 code, design input or room file was opened.

## 3. 20:01:50Z: BOUNDARY.md amendment 1, C3 joins the GO list

Blake's decision, on both units' recommendation. The amendment is appended at the foot, and the original text is byte-identical as the file's prefix: the first 4,330 bytes still hash to entry 0's value. The file's new SHA-256 is `5561aa9b18d0094bde6435d2e4ef5875fe4b025ade3415c64e50cfaff3bae742`.

## 4. 2026-10-15T20:02:24Z: DESIGN.md v2

SHA-256 `c5789c74fa6689c24c15fc0ba52edb5625169b9e3f0c7b0bb2b89cb763726935`. Folded from the units' review of v1:
- the provenance line, now stating both passes through C2's public text, and the rule's comparison with C2's (UB);
- §7's generalized kernel, now from an ordered real Schur form of the separated near-zero cluster, with dimension, symmetry and Jordan checks, and "unresolved" when the cluster is not separated (UA). The Ω-annihilator of eigenvectors fails at a defective nonzero eigenvalue;
- §6, explicit fold handling (UA);
- D7, C3 added, with its real-pair check and Theorem K with k_r > 0;
- §10, now the decisions, in place of the questions.

No run.

## 5. 2026-10-15T20:08:36Z: the provenance line made exact (UB), DESIGN.md v2.1

Before DESIGN.md v1 was written, two sources had already said that C2's production rule was exact to degree 4N:
- UB's step 3 review, which quoted § 4.1's "exact to degree 4N" and "ZERO aliasing";
- C2's gate table, read in step 3, which names a "production 4N rule to rounding" whose arms drop to "2N points per angle".

The Hopf product rule of §4, and its node counts, were derived here. § 4.1 itself was read only after v1 was hashed (entry 2). DESIGN.md v2.1 says this in its provenance section; SHA-256 `ba159e9744e2d36bf8ea8c505bf27f461ee3a9317f7a5f01c0be0d5be9c0e5e7`. No run.

## 6. 2026-10-15T20:11:48Z: run `dev/d1_group.py` (case: synthetic): stopped by an assertion, a wrong claim

Script SHA-256 `dca4d6c983a3c3c402135a59218f00c16db9f00a9043f15b8b94d0cbb914b5ab`. Claim 1 asserted that the Galois map sends 2I onto itself. It does not: it swaps 1/(2φ) and φ/2 between coordinates, which takes the even-permutation icosians to the odd-permutation ones. That is a different copy of the group, isomorphic to 2I. γ ↦ U(σ(γ)) is still the representation 2′, and nothing else is affected. The claim is corrected to: σ is multiplicative, and its image is 120 distinct unit quaternions closed under products. No tolerance is involved.

## 7. 2026-10-15T20:11:56Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `69093297ae94b5c811b4237d8b9aad68280e34dd450c9e57dbdc1a2118f7c9d2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `df02c172a0e6e78b534421f53941e051cad865ea7d4913d2ebd3652e1bd38d75`
- `instrument/devtools.py` `8a3d98d566a3646974be64076bdf690db604c453d87bc7189699e9f0b38a7f27`
- `instrument/group2i.py` `ea99522c4e5f4314757631274bcbd942d2e7a455d935a3ac2af15ec7d3e8fc20`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `31244738a0b629f2862aac60917dc0a2df8c77c30c38cd1cd6f24a4d9323d8be`

D1, the group and its representations: PASS, 3 claims, 3 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 8. 2026-10-15T20:13:17Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `df02c172a0e6e78b534421f53941e051cad865ea7d4913d2ebd3652e1bd38d75`
- `instrument/devtools.py` `8a3d98d566a3646974be64076bdf690db604c453d87bc7189699e9f0b38a7f27`
- `instrument/group2i.py` `ea99522c4e5f4314757631274bcbd942d2e7a455d935a3ac2af15ec7d3e8fc20`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `f8472630f60158b898d255f6feaef52dda3831b1209487b06f7f48d220657d57`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 9. 2026-10-15T20:14:02Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `cc3ff60eb25c8d2697e939e1de08d3951d65292fd6536e63c8a56ceb54bdb5a4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `df02c172a0e6e78b534421f53941e051cad865ea7d4913d2ebd3652e1bd38d75`
- `instrument/devtools.py` `8a3d98d566a3646974be64076bdf690db604c453d87bc7189699e9f0b38a7f27`
- `instrument/group2i.py` `ea99522c4e5f4314757631274bcbd942d2e7a455d935a3ac2af15ec7d3e8fc20`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `6466647a429fbbf83a6909484df806b00618bc0233610ac4928ba40bfceaff5d`

D3: 1 failures; see the output.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 and 1e-12). The run informed none.

## 10. 2026-10-15T20:14:44Z: the cause of the D3 failure above, and the fix

Claim 3's witness for the t factor's limit was t^(2N+2). That monomial is not integrated exactly by N + 1 Gauss nodes, but at large N it is integrated to within 5e-15 (N = 16) and 2.5e-14 (N = 24), because the Gauss remainder on monomials decays fast. So the witness could not fail where it was meant to. That is a defect of the test's design, not of the rule; the angular witness a^(4N+1) failed as it should at every N.

The fix replaces the witness, and moves no tolerance. The new witness is the squared nodal polynomial, prod over g of (t − t_g)², of t-degree 2N + 2: the rule gives it 0, and its integral, computed by N + 2 Gauss nodes (exact to degree 2N + 3), is positive, so its relative error is 1. Claims 1, 2 and 4 and both arms are unchanged and passed.

## 11. 2026-10-15T20:14:47Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `df02c172a0e6e78b534421f53941e051cad865ea7d4913d2ebd3652e1bd38d75`
- `instrument/devtools.py` `8a3d98d566a3646974be64076bdf690db604c453d87bc7189699e9f0b38a7f27`
- `instrument/group2i.py` `ea99522c4e5f4314757631274bcbd942d2e7a455d935a3ac2af15ec7d3e8fc20`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `81e0435bfb0c65bd62826946d92af059c360b64bb2815194b1a0f2d5edbb30a6`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 12. 2026-10-15T20:15:38Z: outputs now kept per run; one failed output lost

D3's failing run (entry 9) logged its output's hash, but the passing rerun (entry 11) wrote the same file, so the failing output itself is gone. Its hash stays in entry 9, and its numbers are in entry 10. From now on `instrument/devtools.py` keeps a copy of every output under `dev/runs/`, named by its entry number, and refuses to overwrite one; its SHA-256 is now `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`. The three passing outputs are copied there now: `007_d1_group.out`, `008_d2_basis.out` and `011_d3_rule.out`, each matching the hash its entry logged (checked: True, True, True). No run.

## 13. 2026-10-15T20:35:32Z: the units' review of D1 to D3 folded; DESIGN.md v2.2; BOUNDARY.md correction 1

Both units confirmed D1 to D3 and gave GO to D4 and D5. Folded, each checked first:
- c1 (UB). The SVD fixes each intertwiner only up to a phase, or a unitary at multiplicity above 1, and LAPACK picks it per machine. So multi-level coefficient states differ between machines; D3 claim 4's values move, one-level ones don't. §3 now fixes the A_i canonically, by the group average on elementary matrices in a fixed order with Gram–Schmidt, and keeps the generator nullspace as D1's independent count. D1 to D3 rerun under it, below.
- c2 (UB). The borders are an orthonormal basis of the tangents' span, with its rank by pivoted QR (§6). Dependent tangents, as at a weight vector, would make the bordered matrix singular.
- c3 (UB). Newton runs to round-off. The kernel is read on L's inertia and on the leading Schur block's singular values, and the margin is set on the root scale (u‖A‖)^(1/j) (§§6, 7, D7).
- c4 (UB), with UA's caveat. D5 now runs unbordered and bordered, with an arm. It tests the solver's mechanics, never the unforced kernel.
- c5 (UB). M8.15's control ladders are graded as the census grades them, unscored. DESIGN's D7 wording is changed, and BOUNDARY.md takes correction 1 at its foot; the first 4,330 bytes still hash to entry 0's value.
- UA's two notes for before the qualification: an explicit frozen allowlist in place of the freeze file's existence (§6), and test states pinned independently of basis choices (§8).

DESIGN.md v2.2 SHA-256 `f02486dfb1e0194d0d2abc804de6a068f8478a58868cb441b2a5426bf4470bcf`; BOUNDARY.md now `d55dd13fabbf913b4b4d0cba572733e74f7bf61f0306c2abce6f8b37a279d47f`. No run.

## 14. 2026-10-15T20:36:53Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `155f4daa7a19ee17275819cb8ee509a2fe3246cbb6f4006c7ff6c4191e37e6f0`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/group2i.py` `cfbb006f1a9ad647443dd1ff0792095ef9738e0b78f3bd1ad85f70937ba3b212`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `7a60a87d30659f54fde51cd2f1487b1cec04cbdf163b1584f6806103a639eb99`, kept as `dev/runs/014_d1_group.out`

D1: 1 failures; see the output.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 15. 2026-10-15T20:38:06Z: the cause of D1's claim 3 failure above, and the fix

Two of claim 3's conditions failed; the rest passed, and all four arms were red.
- **My a priori Gram–Schmidt gap was wrong, not the cut.** I had required kept residuals above 1e-3 and dropped ones below 1e-12. The run shows kept residuals down to 2.83e-4 and dropped ones up to 3.9e-11, so the design's 1e-8 cut falls in a gap 2.4 orders wide below it and 4.4 above. The condition now asks that no first-pass residual lie within two orders of the 1e-8 cut, that is between 1e-10 and 1e-6. That is informed by this run, and disclosed here.
- **A real precision defect in the construction.** Normalizing a small kept residual amplifies rounding, so the canonical basis met ρ(g)A = Aπ_n(g) only to 7.4e-11, against 1.7e-13 for the old nullspace basis. That is inside the 1e-10 tolerance, but an equivariance error that size would break the exact symmetry at 1e-11, and with Jordan chains at its square root. The fix: the group average, a projector, is applied once more to each kept vector, and Gram–Schmidt runs again in the same fixed order. That stays canonical, and it is a refinement of DESIGN.md §3's text, flagged to the units. The 1e-10 tolerance is unchanged.

## 16. 2026-10-15T20:38:18Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/016_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 17. 2026-10-15T20:38:38Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/017_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 18. 2026-10-15T20:38:40Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/018_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 19. 2026-10-15T20:41:22Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `e0c42f2fcf528ce8dccef78c7c23da1dc657bc2239976ce7711fb2aa7ebeda34`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `8b20de5afea47bc9d8354c2006d761d1dd78e5c9195c15488396e3954d18b73c`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/newton.py` `cbb9cc4f33f8b7481677052fae09f4ac130d4667a06cc61b62337230e4a30f4c`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `a37b90b30168d61630354bedcb44f327b68eeff198c56151d465640ff3165fe1`, kept as `dev/runs/019_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution). The run informed none.

## 20. 2026-10-15T20:42:07Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `cce1cd2003fe04306a368d85ce06c0ae7c026510e3cae3b4f8c96f0c68068c06`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `8b20de5afea47bc9d8354c2006d761d1dd78e5c9195c15488396e3954d18b73c`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/newton.py` `cbb9cc4f33f8b7481677052fae09f4ac130d4667a06cc61b62337230e4a30f4c`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `5195bf69fb099c6f52f215aacc8e3527e72453f2a3fc9093551b03e545952c10`, kept as `dev/runs/020_d5_newton.out`

D5: 2 failures; see the output.
Tolerances: fixed before the run (a residual below 1e-12; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11; an observed order above 1.8; multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 21. 2026-10-15T20:43:54Z: the cause of D5's two failures above, and the fix

R4 and R5 failed only the order criterion, at 1.19 to 1.28 against 1.8. Every other condition passed, R2 passed outright, and the arm was red. The unbordered residual histories show the solver converging quadratically:
- R4: 2.39, 4.53e-3, 1.88e-6, 4.69e-13, with r(k+1)/r(k)² = 7.9e-4, 9.2e-2, 1.3e-1;
- R5: 3.12, 4.99e-3, 2.14e-6, 5.19e-13, ratios 5.1e-4, 8.6e-2, 1.1e-1;
- R2: 0.264, 5.93e-3, 2.49e-6, 9.34e-13, ratios 8.5e-2, 7.1e-2, 1.5e-1.

The estimator was at fault. It excluded the final step, as near round-off, so for R4 and R5 its only triple contained the first step, taken from a residual of about 2.4 and still pre-asymptotic. This was informed by the run, and is disclosed. The criterion is now:
- the order on the final three residuals, landing step included, is above 1.8;
- the last two ratios r(k+1)/r(k)² agree within a factor of 10.

Nothing else changes.

## 22. 2026-10-15T20:43:57Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `0a58d629fbd4f43d46eaf561a2d3586e231915c0d578e33c77963a9b3314716b`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `8b20de5afea47bc9d8354c2006d761d1dd78e5c9195c15488396e3954d18b73c`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/newton.py` `cbb9cc4f33f8b7481677052fae09f4ac130d4667a06cc61b62337230e4a30f4c`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `8493588cb5a0776a8373386601d1c2add78c745aa905608a1f655c5a69775cfa`, kept as `dev/runs/022_d5_newton.out`

D5: 1 failures; see the output.
Tolerances: fixed before the run (a residual below 1e-12; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11; the order on the final triple above 1.8 with r(k+1)/r(k)^2 stable within 10 (set after the first run, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 23. 2026-10-15T20:44:52Z: D5's second criterion failed too, on R2; a third, tested by an arm

The run above passed R4, R5 and the arm, and failed R2 on the revised criterion: order 0.68, with the r(k+1)/r(k)² spread at 1.3e7. In that run R2 took a fifth step, from just above the 1e-12 stop to 1.2e-14, which is the round-off floor. A step taken at the floor carries no information about convergence, and including it broke the estimate the other way. Both of my order estimators were badly built for histories this short. The solver is not at fault: every residual sequence reached round-off in 4 or 5 evaluations.

The third criterion tests the defining inequality, and is not read off a fitted order:
- every step taken from inside the basin (r(k) ≤ 1e-2) satisfies r(k+1) ≤ max(10 r(k)², 1e-12);
- at least one such step lands above the 1e-12 floor, so the test is not vacuous.

A linearly convergent iteration fails this once r(k) < 1e-2. To show that the criterion can fail, D5 gains an arm: Newton with its step halved, which converges only linearly, must fail it. The criterion was set after two runs, and both revisions are disclosed here.

## 24. 2026-10-15T20:44:57Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `29823abb4db3ccccdf412f663b41282fba3bc534398ba1982b02b7fcf20c1134`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `8b20de5afea47bc9d8354c2006d761d1dd78e5c9195c15488396e3954d18b73c`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/newton.py` `067ace5638ba6774445073483bc9db135a8773e3a1c3be16e2522a5f09d2687c`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `415a68c862b16f9f2b745d9ed8d14af872cf88e7bf37fd940a165e293d8b48e2`, kept as `dev/runs/024_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, 2 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 25. 2026-10-15T20:45:20Z: DESIGN.md v2.3, §3 records the refinement pass

§3 now states the refinement that entry 15 added to UB's c1 construction: the group average applied once more to each kept vector, with Gram–Schmidt rerun in the same order, and D1's before-and-after equivariance (7.4e-11, then 6.7e-14). It goes beyond UB's c1 text, and is flagged to the units. SHA-256 `8c7059e9ed3346efb88a5e6cdc7e8a6771468505cb1ad17dca261d5499bd93c0`. No run.

## 26. 2026-10-15T21:22:41Z: DL's first attempt stopped at claim 2; changes before the rerun

The first attempt of `dev/dl_linear.py` (case: synthetic) printed claim 1 (PASS, identities 0, spectral pairing 1.1e-15) and stopped at claim 2 with an IndexError: at N = 12, R2 has one level (its levels are 7, 13, 17, 19, 23). It made no log entry and kept no output, and `record()` had not yet run on anything. Before the rerun:
- Claim 2 runs at N = 16, the development ladder's first rung, where R2, R4 and R5 each have at least two levels. It now checks each imaginary group's Krein sign against its predicted frequency, as well as the totals.
- `record()` links eigenvalues outside the cluster within the margin, and types each group by its centre. The first version typed single eigenvalues by relative cuts of 1e-7 and 1e-6, which are below the root scale on which a defective nonzero eigenvalue splits (about 6e-7 at ‖A‖ ≈ 1,700). So a split Krein collision could have been typed complex on one side and imaginary on the other. A centre moves only on the scale u‖A‖. Typing within the margin moves no count of K, since a group of nearly equal imaginary eigenvalues and a quartet near the axis each contribute 2.
- The Krein signature takes the eigenvector route only when the eigenvectors span the group and B is nondegenerate on them. Otherwise it reads the signature on the group's real invariant subspace from an ordered real Schur form, with any failure there reported unresolved. DESIGN.md §7's text, "from B on its eigenvectors", does not cover a defective group, and v2.4 will state the fallback.
- `eigvec_annihilator()` gains a second mode, after reading how `identification_check.py` builds it: from each eigenvalue's computed eigenvector, with the null space cut at a fine tolerance. In exact arithmetic the construction is larger than V0 at a defective eigenvalue (UA's correction). As computed, the two split eigenvectors at a defect are nearly parallel but distinct, so it can return V0's dimension with an error instead. DL's arm scores the construction as defined, from exact eigenvectors (ker(A − cI) at a round-off cut); the computed variant is reported, unscored.
- Claims 3 and 4 compare against counts derived by hand in the script's docstring, not only against the unmixed blocks read by the same code. They also check the Schur V0 against the exact V0 by principal angle.
- Claim 6 was rebuilt. Its first case set an oscillator's κ to (ω + 3e-6)², which gives κ ≈ ω², not an eigenvalue near zero; κ = (ω + 3e-6)² − ω² was meant. Its second case put a pair of A in the cluster's gray zone as well as L's, so it could not show that each flag fires alone. Each case now flags exactly its own item.

None of these changes was informed by an output of `record()`, which had not run.

## 27. 2026-10-15T21:22:43Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `d841aeeb71ccda664fe28dc714874eeaa1a91b0341623b40c276d418c354599d`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `e004c0bbec1aff4e9b87e2e24361e82a7f7b509242929e0d550e0bcfc4bffff3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `c1f43c6d887632456937b2795f8fe49d20509e7fc1ea22d72fe9a0adee95c5d1`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `869cfc5fdd2f1793172436ff2c4d8106fda637d45c03efad2d9a1ae53b72d1b4`, kept as `dev/runs/027_dl_linear.out`

DL, the linear record: FAIL, 2 failures (claims and arms); see the output.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; inertia gray zones 1e-10 to 1e-7 for L and 1e-8 to 1e-5 for D; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6 and B nondegenerate above 1e-8 for the eigenvector route; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 28. 2026-10-15T21:23:24Z: entry 27's two failures, both in the test code; fixed, no tolerance moved

Entry 27 failed claim 4 and one arm. Everything `record()` returned matched the hand-derived counts, in every claim. The two failures:
- **Claim 4's angle to the exact V0, 2.1e-8 against the cut 1e-8.** 2.1e-8 is √(2u), the resolution floor of the cosine form of the principal angle, arccos of the smallest singular value of Qxᴴ Qy. Below it, the cosine rounds to 1 − u or to 1; claim 3's 0.0e+00 is the same floor, so neither number measured V0. `linear.principal_angle` now reads the angle from its sine, ‖(I − Qx Qxᴴ) Qy‖, which resolves it down to round-off. Entry 27's unscored annihilator angles, 0.0e+00 and 1.5e-8, came from the same formula and measured nothing either.
- **The arm "W's gyroscopic block with its sign flipped" stayed green.** It flipped `W[:4, :4]`, a quarter of the 8 × 8 block G = 2ω J0, which is zero there, so W was unchanged. It now flips all of G.

The angle's cut stays at 1e-8, and no other tolerance moved. Entry 27's output stands in `dev/runs/027_dl_linear.out`.

## 29. 2026-10-15T21:23:25Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `5a235e65dd935a1155931eeac214a6191249094e54f87f549486dc27901f8b58`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `e004c0bbec1aff4e9b87e2e24361e82a7f7b509242929e0d550e0bcfc4bffff3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `c5b488163c794bf1b9abf2a6a6c86bc0ba9609b0342d176bc11c078fbc30d349`, kept as `dev/runs/029_dl_linear.out`

DL, the linear record: PASS, 6 claims, 4 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; inertia gray zones 1e-10 to 1e-7 for L and 1e-8 to 1e-5 for D; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6 and B nondegenerate above 1e-8 for the eigenvector route; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 30. 2026-10-15T21:24:09Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `6c9d2046ea5f7a2671263521858dac83e44d7ddada888d1bdb0d98d8f10663b4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `e004c0bbec1aff4e9b87e2e24361e82a7f7b509242929e0d550e0bcfc4bffff3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `a8e94e3d5f18bbda4231a40334e55e55c9161597e408f236cd0d1188aed1ea08`, kept as `dev/runs/030_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 31. 2026-10-15T21:24:17Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `5238e404ea9549ce83f50bccdd0a5e7e055c4dfce17c47f4a2ec6805e9341fc2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `3efa9a0b2b358e43ce3f38797178e4d05dc8615f5ed47b2e6a306548380b0328`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `e004c0bbec1aff4e9b87e2e24361e82a7f7b509242929e0d550e0bcfc4bffff3`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `86aee38a1d216831ce4473c2b37f89bdc6fc6dc761bd42f8fb1b4557a6119e80`, kept as `dev/runs/031_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, 3 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 32. 2026-10-15T21:27:32Z: finer chunks, so UB's (b) holds at N = 40; then the whole suite on one package

Entry 30's chunks were whole t nodes, and that misses §9's budget at the ladder's top. One t node is 1.35 GB of complex basis values for R5 at N = 40, and `hess_parts` holds about five times a chunk. Chunks are now blocks of α rows at one t node, at most 64 MiB each (`chunk_bytes` = 2²⁶): 8 of 161 rows for R5 at N = 40, and 14 for R3. A whole t node is used when it fits, which is every case at N = 12. The cache is unchanged: it holds every chunk only when all of them fit under 2 GB. Whole, the cache would be 55.3 GB for R5 and 30.8 GB for R3 at N = 40, and 2.9 GB for R5 at N = 24, as UB computed. `basis.evaluate_at_t_node` takes an optional range of α rows; called without one, as D2 and D3 call it, it computes what it did before.

D4's claim 4 now compares one-row chunks, recomputed at every call and never cached (`cache_bytes` = 0, `chunk_bytes` = 1), with the cached whole nodes. Entry 30's claim 4 compared two paths that grouped the sums the same way, so it was bitwise equal (0.0) and could not show a grouping error. The new comparison changes the summation order, and its tolerance stays at 1e-14.

Two observations from entry 31, for the units:
- **The halving rule ends a linear iteration too.** It stopped the halved-step arm at evaluation 24 (maxit is 40), at a residual of 3.2e-7, far above round-off: an iteration whose residual ratio is 1/2 stops "halving" by design. D5's fixed 1e-12 stop is what marked that run unconverged. UB's §6 text has no fixed stop, so for D6 and D7 an acceptance bound on the relative floor is a decision to make before they run. Entry 31's real floors were 1.2e-17 to 5.9e-17 relative, against 1.5e-9 or so at the arm's false floor. No code changed for this.
- **D5's label differs from UB's wording.** It reads "the Jacobian's quartic part scaled by 1 + 1e-3"; UB's text is "the Hessian's quartic part". It is the same block, F″ in Newton's Jacobian, and the label is left as run.

Next, D1 to D5 and DL rerun in order, on the package as it now stands, so that every last entry hashes the same files.

## 33. 2026-10-15T21:27:43Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/033_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 34. 2026-10-15T21:27:58Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/034_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 35. 2026-10-15T21:28:03Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/035_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 36. 2026-10-15T21:28:14Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `cedbd2f71ebf3a7d5ecef2b3c541503a8a79803ff1f16fe8de0dceaf0a3cae0c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `37569cbfeb6ebf1ad11a82b2cbd174f3b8a5b30846430a7579a5fff850415c88`, kept as `dev/runs/036_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 37. 2026-10-15T21:28:26Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `5238e404ea9549ce83f50bccdd0a5e7e055c4dfce17c47f4a2ec6805e9341fc2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `86aee38a1d216831ce4473c2b37f89bdc6fc6dc761bd42f8fb1b4557a6119e80`, kept as `dev/runs/037_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, 3 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 38. 2026-10-15T21:28:32Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `5a235e65dd935a1155931eeac214a6191249094e54f87f549486dc27901f8b58`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `c5b488163c794bf1b9abf2a6a6c86bc0ba9609b0342d176bc11c078fbc30d349`, kept as `dev/runs/038_dl_linear.out`

DL, the linear record: PASS, 6 claims, 4 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; inertia gray zones 1e-10 to 1e-7 for L and 1e-8 to 1e-5 for D; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6 and B nondegenerate above 1e-8 for the eigenvector route; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 39. 2026-10-15T21:29:58Z: DESIGN.md v2.4

- **§6.** UB's text on Newton's stop replaces the fixed residual, verbatim. `newton.solve` adds ‖h‖ to the size when the problem is forced, which only D5's are.
- **§7.**
  - Groups linked within the margin, typed by their centres.
  - The Krein signature's Schur route at a defective group.
  - The unresolved outcomes of n(L) and n(D).
  - DL's margin and its cluster.
  - The annihilator's failure, both ways.

  The first two go beyond §7's v2.3 text, "from B on its eigenvectors", which does not cover a defective group (entry 26). They are flagged to the units.
- **§8.**
  - D4's chunked claim (UB).
  - D5's quadratic criterion and both arms. The halved-step arm was in DEVLOG.md (entry 23) but not yet in the design; the quartic-part arm is UB's, in UB's words.
  - The DL entry (UA, UB), before D6.
- **§9.** The memory bullet now states the chunk and the cache.
- **Header.** "No M8.16 code exists yet." was stale since entry 3, and now says where the development code is. It rides along.

No FFT note was added. The idea was mine, not a unit's, and nothing needs it. SHA-256 `63526516cc07b26ce75073223764d39418fd5e469f3e9c7e84ddcdd13ff4567c`. No run.

## 40. 2026-10-15T21:30:11Z: a correction to entry 39

Entry 39 says the header's "No M8.16 code exists yet." was stale "since entry 3". It was stale from entry 6, the first run of development code (`dev/d1_group.py`); entry 3 is BOUNDARY.md's amendment 1. The design's text is unaffected. No run.

## 41. 2026-10-15T22:07:01Z: run `dev/units_findings_r4.py` (case: synthetic)

Script SHA-256 `1239f57bf63966a77a4ecb9171fcb06865e7afc446c0b1cc657ed0a3cc108693`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `8033256cd79727a724c65d658e120ce564f41ab90f34522f7ae2f1e832b5ef43`
- `instrument/newton.py` `fd897d07bc744850b0effd7a44628856c78d22878229db41ec6089e1188b981b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/units_findings_r4.out` `dd712edd146ff884a37c824dff2841e0e9269d1e7ca08fb79b69a3252ad447cd`, kept as `dev/runs/041_units_findings_r4.out`

The units' counterexamples to §7's typing, on the package before any fix: 4 of 4 reproduced (UA: yes, UB c1 at 3e-06: yes, UB c1 at 6e-06: yes, UB c2: yes). Nothing is scored; the run records the defect before the fix.

## 42. 2026-10-15T22:14:31Z: the units' review of §7 folded, before any rerun

UA put a HOLD on D6 and D7, for one defect; UB's review said KEEP, with changes. Entry 41 reproduced every counterexample on the package as it stood, before any fix.
- **UA.** A quartet with real parts 3.16e-7 was typed imaginary, with k_c = 0, k_i = 1, K = 2, and nothing flagged.
- **UB c1.** Quartets with real parts 3e-6 and 6e-6, each one group with signature (1, 1), K = 5, and nothing flagged.
- **UB c2.** At real part 1.2e-5, the two members fell in separate groups, each "resolved" from a Krein form of ±2.2e-10, which is round-off. UB measured ±6.8e-10, on a different mixing.

**`instrument/linear.py`:**
- **Mixed groups (UA; UB c1).** An imaginary group carrying both Krein signs is a collision within the margin, possibly a quartet. K counts it, and its type is reported unresolved with its largest |Re λ|.
- **The type verdict (UA's requirement 3).** Hyperbolic when a group off the imaginary axis by more than the margin lies outside the cluster's gray zone. Otherwise Elliptic only when nothing is unresolved, and Unresolved when anything is. The balance never stands in for the type.
- **Scales (UB c2).**
  - Krein nondegeneracy is read against 1e-8 |λ| ‖W‖ in both routes, since vᴴBv = λ̄ vᴴWv bounds a unit eigenvector's form.
  - n(D)'s inertia is read against ‖B‖; `inertia` takes a scale.
- **Beyond UB's c2, mine.** Where the eigenvectors span a group but B is degenerate on them, the group is reported unresolved directly; the Schur route is taken only where they do not span it. The reason: B is nondegenerate on the eigenspaces of imaginary eigenvalues, so a degenerate form there means a member off the axis, or a collision, within the resolution. And by my estimate, the Schur subspace of an off-axis member within the margin is isotropic only to about u‖A‖/(2|Re λ|), within a factor of two of the 1e-8 |λ| ‖W‖ bound at real part 1.2e-5, so noise there could pass as resolved (INFERRED, not measured). UB's patch, the Schur route on degenerate spanning sets too, stays as the option `arm='schur_on_degenerate'`, and DL reports its result, unscored.
- **Arm options.** `record(arm=...)` gains three arm options, `mixed_resolved`, `krein_own_scale` and `d_own_scale`, each undoing one change for DL's arms. Each imaginary group records its route, its status (definite, mixed or degenerate) and its largest |Re λ|. `K_resolved` is false when any group is degenerate.

**`instrument/newton.py` (UA; UB's (d)).**
- Acceptance is enforced in `solve`, at `accept_rel` = 1e-15 relative to the size, on three things:
  - the floor (the bordered residual);
  - the unbordered residual, the equation and the norm row without the multipliers' term;
  - the multipliers.
- It returns an info dict in place of the floor tuple.
- **The value.** UA confirmed 1e-13 as provisional; UB asks for 1e-15. I take UB's value. A floor ρ breaks each symmetry chain by about ‖T r‖/‖Tφ‖ ≈ 2ερN/n₀, which I re-derived: ‖T‖ ≈ N/2, ‖Tφ‖ ≈ (n₀/2)‖φ‖, and the size is about 2ε‖φ‖. The chain splits at about its square root: 1.2e-5 at 1e-13, inside the gray zone at the top of C2b's ladder (ε = 132, N = 40, n₀ = 7), and 1.2e-6 at 1e-15, below a tenth of the margin (INFERRED; the square root's constant is not computed). The bound stays provisional, as UA said, open to revision on disclosed GO-list controls before registration.

**`dev/d5_newton.py`.** It reads the info dict. New:
- **An arm.** The halved step with no fixed stop must be refused by the acceptance bound alone.
- **The tangent arm** must now also be refused.
- **Claim 4 (UB's (d)).** R4 at N = 24, at ‖c*‖ = 2 and 20, unbordered with no fixed stop, must be accepted. The seconds per evaluation are recorded for UB's (e).

**`dev/dl_linear.py`.** Claims 2 to 6 now assert each point's type and each group's status as derived. Claim 4's expectation changes: the exact collision is now one mixed group with its type unresolved, the one unresolved item, and the point is Hyperbolic by the resolved real pair and quartet. New:
- **Claim 7 (UA's requirement 4, and UB's DL addition).** The collision model on both sides at ‖A‖ ≈ 1,700, in a system where nothing else leaves the axis, in nine cases, each with its type and group pattern set in the script before the run. The unstable side must never be typed Elliptic.
- **Claim 8.** n(D) at round-off: a semisimple double zero with D = 0 exactly.
- **Three arms.** `mixed_resolved` and `krein_own_scale` must turn claim 7 red, and `d_own_scale` must turn claim 8 red.

**Not in this round: UB's (e).** Each control's expected V₀ stated before it runs, and D7's costs. Both come before D6 and D7, as their own step.

Next, D1 to D5 and DL rerun in order, on this package.

## 43. 2026-10-15T22:14:51Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/043_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 44. 2026-10-15T22:15:11Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/044_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 45. 2026-10-15T22:15:14Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/045_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 46. 2026-10-15T22:15:27Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `cedbd2f71ebf3a7d5ecef2b3c541503a8a79803ff1f16fe8de0dceaf0a3cae0c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `37569cbfeb6ebf1ad11a82b2cbd174f3b8a5b30846430a7579a5fff850415c88`, kept as `dev/runs/046_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 47. 2026-10-15T22:16:27Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `525d629470403a14cc35ea6b991d7a550beb1fec80b76420eb6b9c1029dc631f`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `2894f7cae4d344bcc6f0b15f6679a76d63cbbf6c8dc429dbd464a6caa93c27f2`, kept as `dev/runs/047_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2 and claim 4 at N = 24, 4 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in newton.solve, for the floor, the unbordered residual and the multipliers; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 48. 2026-10-15T22:16:39Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `61d27c492b5e4f7a0d5ae299b2c2a29b70b2f131b941ec729aa4defcdd09ce70`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `cd0067fe80be4d7a09355bf9e76f9412d903c84e3fb462eb53204ba604f56b6c`, kept as `dev/runs/048_dl_linear.out`

DL, the linear record: PASS, 8 claims, 7 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 49. 2026-10-15T22:17:57Z: DESIGN.md v2.5

- **§6.** UB's acceptance text, verbatim, with 10⁻¹⁵. After it, in my words:
  - UA's requirement that the unbordered residual and the multipliers meet the same bound;
  - that `newton.solve` enforces all three;
  - UA's provisional status.
- **§7.**
  - UB's c1 sentence, verbatim, after "still contributes 2".
  - UB's c2 sentence, verbatim, after "nondegenerate on them", followed by my refinement (entry 42), which goes beyond UB's patch and is flagged. Entry 48's unscored line shows that UB's patch, as UB ran it, also flags both members at real part 1.2e-5, so my estimated noise path did not occur there. The refinement now rests on the argument that the design states: where the eigenvectors span a group, its Schur subspace is their span, so the Schur route would only reread the same form.
  - A bullet for the point's type, UA's requirement 3, in my words.
- **§8.**
  - **D5:** the acceptance bound's claim and arms.
  - **DL:** the collision regression, claim 8, and the arms, now seven. UB's DL sentence is adapted: it said "a quartet split off claim 4's collision", and the regression splits the same collision block, but in a system where nothing else leaves the axis, since claim 4's own system is Hyperbolic by its real pair and quartet. So it reads "split off the collision".
- **§9.** D5's measured 3.5 s per evaluation for R4 at N = 24, and UB's rule that D7's costs at N = 32 and 40 go to Blake before the ladders run.

SHA-256 `e93769de7d6df2ce144bb10149ce5684bb0f54ef292aa78a121f9ea6c34d90fa`. No run.

## 50. 2026-10-15T22:36:09Z: run `dev/units_findings_r5.py` (case: synthetic)

Script SHA-256 `eef496329bbbb1dda8a45c46ee624338244a6c956143ed6a4d3d4b272416ecc8`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/units_findings_r5_ua.out` `01b46a12436c32d5cef8d85acf9af8aaee9a3ee1f11277fb2b702576c6332a3e`, kept as `dev/runs/050_units_findings_r5_ua.out`

UA's index finding, on the package before any fix: L = diag(0, -100000), omega^2 = 25001. Reproduced. Nothing is scored; the run records the finding before the fix.

## 51. 2026-10-15T22:36:11Z: run `dev/units_findings_r5.py` (case: manufactured)

Script SHA-256 `eef496329bbbb1dda8a45c46ee624338244a6c956143ed6a4d3d4b272416ecc8`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `64696ca09bb345ec1772fa558f9fb69095bc16f38fd0631525dc09efd0fc95a3`
- `instrument/newton.py` `fc0b4ad4b72241c750783d615159d36baa859ef74d1c6295f638398c0f0bd19b`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/units_findings_r5_ub.out` `1dfa155038507bb1703f9660cd2f5305618fd909c367ae23612221aea35e1736`, kept as `dev/runs/051_units_findings_r5_ub.out`

UB's float-grid finding, on the package before any fix: lowest-level forced states, R2 and R4 at N = 12. Reproduced. Nothing is scored; the run records the finding before the fix.

## 52. 2026-10-15T22:39:35Z: the units' narrow review folded, before any rerun

UA confirms the classifier and holds D6 and D7 for one index check; UB keeps (a) and (b) and changes the size and the type's coupling. Entries 50 and 51 reproduced both findings on the package before any fix:
- **UA's model,** L = diag(0, −100000) at ω² = 25001. D's eigenvalues are −4.000e-5 and 0, against ‖B‖ = 1.000e5, so n(D) = 0 with two zeros against one chain, K = 0, the balance false, and Elliptic with nothing flagged.
- **UB's float grid.** Against the cancelled size, R2 and R4 at ε = 0.5 lie over the bound (1.8e-15 and 1.0e-15). Against the size before cancelling, all eight lie at or below 8.0e-17. UB found R2 at ε = 2 over the bound as well; here it reads 9.8e-16, on a different draw.

**`instrument/linear.py`:**
- **The balance (UA's 1).** A failed balance is an unresolved item.
- **D's nullity (UA's 2).** Where D's nullity differs from `blocks`, the geometric multiplicity of zero on V0, n(D) is unresolved. I re-derived UA's identity. B(x, y) = Ω(Ax, y), so x ∈ V0 lies in ker(B|V0) exactly when Ax ∈ V0 ∩ V0^⊥Ω, and that intersection is {0}, since Ω is nondegenerate on the generalized kernel of the self-paired eigenvalue 0. So dim ker(B|V0) = dim ker(A|V0).
- **The coupling (UB's (d)).**
  - `record` takes `expected`, the point's expected V0: its dimension and the ranks of A's powers on it.
  - A mismatch, or a symmetry leak above 1e-8, is an unresolved item, and Hyperbolic requires the match.
  - **Mine, flagged:** without an expectation, the type is not read.
- **Arm options.** `index_unguarded` drops UA's two checks, and `v0_unchecked` drops UB's coupling.

**`instrument/newton.py` (UB's (c)).** The size is UB's formula, verbatim, the terms before they cancel. It sets both the floor-mode threshold and the acceptance. With it, the chain estimate becomes 2λρN/n₀, which I re-derived, since the size is now about 2λ‖φ‖. At the top of C2b's ladder (λ ≈ 195, N = 40, n₀ = 7), the split is about 1.5e-6 at 1e-15, below a tenth of the margin, 1.8e-6, and about 1.5e-5 at 1e-13, inside the gray zone. So 1e-15 stands (INFERRED, as before).

**Carried forward, no change now (UB).** A mixed group can also be an exact crossing of eigenvalues that symmetry keeps apart, which can never collide. The rule types it Unresolved, which is safe. If targets lose points to it, the census pre-registration can read mixed groups per isotypic component of the branch's isotropy.

**`dev/dl_linear.py`.** Every record now carries its expected V0, derived by hand; `block_totals` reads only counts.
- **Claim 6(a)'s expectation changes.** An unseparated cluster now flags, in order: the separation, V0's mismatch with its two chains, and the index. The resolved real pair no longer types the point, so it is Unresolved, not Hyperbolic. That is UB's coupling at work, on DL's own case.
- **Claim 7's degenerate pattern** admits the balance flag, since its K is unresolved there.
- **New:** claim 9, UA's model, which must be Unresolved, flagged for the nullity and the balance, and not Elliptic; and claim 10, a structural pair lifted to ±2.5e-4, past the gray zone, which must be Unresolved, not Hyperbolic.
- **Two arms,** one per new check.

**`dev/d5_newton.py`.** New: claim 5, UB's lowest-level states off the float grid, at four ε in each of R2 and R4, all to be accepted; and an arm, in which the cancelled size must put a low-ε floor over the bound.

Every expectation was set in the scripts before any run. Next: D1 to D5 and DL, in order, on this package; then the expected-V0 step, which both units have authorized.

## 53. 2026-10-15T22:39:56Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/053_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 54. 2026-10-15T22:40:16Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/054_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 55. 2026-10-15T22:40:19Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/055_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 56. 2026-10-15T22:40:32Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `cedbd2f71ebf3a7d5ecef2b3c541503a8a79803ff1f16fe8de0dceaf0a3cae0c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `37569cbfeb6ebf1ad11a82b2cbd174f3b8a5b30846430a7579a5fff850415c88`, kept as `dev/runs/056_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 57. 2026-10-15T22:41:37Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `3525b60ab025e3e0ef8ee841383d6969d55b8fd407a14a8725d9daaaa8df78fc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `5330aa3ea2f31214e60dc846ed5034b4d70d7aeed50689535de962a66225dd52`, kept as `dev/runs/057_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, claim 4 at N = 24 and claim 5 off the float grid, 5 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in newton.solve, for the floor, the unbordered residual and the multipliers, against the size of the terms before they cancel; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 58. 2026-10-15T22:42:16Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `a764b4ff579dcc6d3029b3a1d5534efdc58760242d9c0c965a7cc641efb3d047`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/058_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 59. 2026-10-15T22:48:35Z: EXPECTED_V0.md, and DESIGN.md v2.6

**`EXPECTED_V0.md`** states each control's expected generalized kernel before any control runs (UB's (e); UA's GO). Each row is derived from MIT's pages, with M8.15's frozen algebraic dimensions as the cross-check only (UA):

| Control | k, r_u | Dimension | Ranks |
| --- | --- | --- | --- |
| C1 | 5, 1 | 6 | [1, 0] |
| C2a | 3, 1 | 4 | [1, 0] |
| C2b | 5, 1 | 6 | [1, 0] |
| C3 | 4, 4 | 8 | [4, 0] |

- **The sources.**
  - C1 from the Slot Ground States, Theorem D, item 2, at n = 2.
  - The other three from the Soft-Slot Branches: §IV's (k, r_u) rows; Theorem R(a) and (e), with Lemma S, for the count and the partners; and the zero multiplicity of Ŝ_u, read off §IV's slow-frequency lists as 14 − 10, 16 − 10 and 14 − 6.
- **The agreement.** All four agree with `FROZEN_DIM` (6, 4, 6, 8).
- **The INFERRED part.** That no genuine crossing falls at ε ∈ {0.5, 1, 2} rests on REGISTER_4 §5's statement from M8.15's qualification, quoted there. A crossing at a sample point would read as a mismatch, and so as unresolved.

SHA-256 `7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1`.

**DESIGN.md v2.6:**
- **§6:** UB's size text, verbatim, in the stop.
- **§7:**
  - UA's two index checks;
  - UB's type bullet, verbatim, plus my sentence, flagged: "Without an expected V₀ the type is not read";
  - a V₀ sub-bullet naming `EXPECTED_V0.md`.
- **§8:**
  - **D5:** UB's off-grid claim, verbatim, and its arm.
  - **DL:** claims 9 and 10, and the two new arms.
  - **Before D6 and D7:** the expected rows, and the limited first sample at ε ∈ {0.5, 1, 2} with one timed point at N = 40, whose cost goes to Blake (UB, UA).

SHA-256 `6c44d3ba469d81448e3d7f15acb65fc442f373858c3aaa58f82a5c82ff042cdc`.

**One observation, for the units: D5's new arm has a thin margin.** Against the cancelled size, the low-ε floors lie near 1e-15 itself:
- in entry 51's draw, R2 and R4 at ε = 0.5 were over the bound (1.8e-15 and 1.0e-15), and R2 at ε = 2 was under it (9.8e-16);
- in entry 56's draw, R2 at ε = 2 was over it (1.4e-15), and both ε = 0.5 cases under (9.1e-16 and 8.3e-16).

So the arm is red on these draws, but not robustly. A smaller ε, such as 0.1, where uλ/(4ε) is about 3e-14, would make it robust. That is a change for the units to choose, so it is left as run. No run.

## 60. 2026-10-15T22:48:44Z: a correction to entry 59

Entry 59 cites D5's second draw as "entry 56's draw". D5's run is entry 57; entry 56 is D4's. The numbers it quotes are entry 57's. No run.

## 61. 2026-10-15T23:07:27Z: the units confirm v3; D5's arm amended before D6 and D7

UA and UB confirm v3, and both give GO to D6 and D7's limited sample once D5's thin arm is strengthened. They differ on the ε. UA proposed adding 0.1. UB found 2 of 8 draws at 0.1 under the bound against the cancelled size (9.2e-16 and 2.8e-16), so 0.1 would still be thin, and found every draw at 0.01 over it by fifty times or more, with the seeds 1e-5 off in relative norm and λ 1e-6 off.

**The amendment** (`dev/d5_newton.py`, claim 5):
- ε = 0.01 and 0.1 are added, and the original four kept. The added two draw from their own random stream, so the original four reproduce entry 57's draws.
- At ε = 0.01 the seed is 1e-5 off in relative norm (UB); λ's seed, 1e-4 ε off, is then 1e-6 off, as UB set it.
- **The arm** is now UB's: against the cancelled size, the ε = 0.01 floors must exceed the bound in both slots.
- ε = 0.1's values against that size are reported unscored, as UA's proposal.
- The bound, 1e-15, is unchanged (UA).

Earlier outputs stay in `dev/runs/`.

## 62. 2026-10-15T23:08:26Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `4a93719a270eb02806a4555c468222b275704ce8ae7b847b2d26e9bb20955c52`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `4c59228601e05543816cb048e1a052344830035973dc527aea080c7e04666632`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `c057c9825fc5f68ddef994d2714384178181df40a7fd5ec32814bd4eee33d787`, kept as `dev/runs/062_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, claim 4 at N = 24 and claim 5 off the float grid, 5 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in newton.solve, for the floor, the unbordered residual and the multipliers, against the size of the terms before they cancel; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 63. 2026-10-15T23:13:29Z: D6 and D7 built; one unlogged seed check; trial at N = 16 next

**`instrument/branches.py`, new:**
- the seeds of the four GO-list controls, and no other;
- the orbit checks (Q(u), criticality on the lowest level, the tangents' rank k, and their σ-radical r_u);
- the continuation: Newton in ‖c‖² with a secant to each target ε within 1e-6, bordered by the orbit tangents at the slice point, as DESIGN.md §6 sets it;
- `expected_v0()`, which reads EXPECTED_V0.md's rows and requires its SHA-256 to equal the one logged in entry 59.

`linear.record` now also returns its eigenvalues.

**`dev/d6_theoremD.py` and `dev/d7_controls.py`** carry their expectations and sources in their headers, fixed before any run: the C1 row's spectrum from Theorem D; and, for C2a, C2b and C3, Q, (k, r_u), the slow frequencies, (n(L), n(D), K) and the type.

**Disclosed: one seed check ran outside a logged script.** While writing `branches.py`, I ran `orbit_checks` once at N = 12 on each control's seed, from the command line:
- Q(u) came out 1.000777000776994, 1.006993006993006 and 1.223776223776225, against 1288/1287, 144/143 and 175/143;
- criticality was about 2e-16;
- (k, r_u) came out (3, 1), (5, 1) and (4, 4);
- for C1: Q = 1, with a symmetry rank of 4 and a σ-radical of 2 at a generic v.

It informed no expectation, since these are the pages' values. D6 and D7 repeat the checks, logged, at every N.

Next: a trial of D6 and of D7 for each control at N = 16 only, then the full sample at N = 16, 24 and 32, detached.

## 64. 2026-10-15T23:13:31Z: run `dev/d6_theoremD.py` (case: theoremD:R3)

Script SHA-256 `c88e57ef38a5dc67285e3d88ab7e5a16b13650e1bd75d4e9418f54a140a724e0`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_theoremD_N16.out` `3d7ddb3c4d5f37c12efed5505d43242b4e6defe979392a63a73860187e650126`, kept as `dev/runs/064_d6_theoremD_N16.out`
- output `dev/d6_theoremD_N16.json` `6154a997ed0310619fd6fa969f3b089f5915c35562b15660f81f45a014f63c11`, kept as `dev/runs/064_d6_theoremD_N16.json`

D6, Theorem D at R3, N = [16]: PASS, 4 claims at eps 0.5, 1 and 2.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row C1 {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (the acceptance bound 1e-15 for the residual; 1e-14 off level 2; 1e-10 for the lowest level against Theorem D; the record as in DL; 1e-12 along the ladder). The run informed none.

## 65. 2026-10-15T23:13:46Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N16.out` `194ba2b0d1b7d0b17aa7ed022bddec6de22a34088c475e41d8140522a4e5ccff`, kept as `dev/runs/065_d7_C2a_N16.out`
- output `dev/d7_C2a_N16.json` `f3cfab9acacb1c0fec7d526f98f6c56ee6ac0bd64e73263a19b6a11f384638bf`, kept as `dev/runs/065_d7_C2a_N16.json`

D7, C2a, N = [16], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 66. 2026-10-15T23:13:49Z: run `dev/d7_controls.py` (case: C2b)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2b_N16.out` `0179f77c1dd0557f8ccb2d3f1e892496ec2056f96b9a4979bd2054ec07ded669`, kept as `dev/runs/066_d7_C2b_N16.out`
- output `dev/d7_C2b_N16.json` `049069467c78957dec2cb69143950425b1e908a458d0f229e58d17adea03c98b`, kept as `dev/runs/066_d7_C2b_N16.json`

D7, C2b, N = [16], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 67. 2026-10-15T23:14:01Z: run `dev/d7_controls.py` (case: C3)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C3_N16.out` `4eb8f2ad462b1a43808c9029ac34f23d4eb8298eb0686827980da32e03b9229d`, kept as `dev/runs/067_d7_C3_N16.out`
- output `dev/d7_C3_N16.json` `1df4acc9bc1fd4fc49b33f72c81035b45c8d5946279e7abf4900ca0583ab5fbd`, kept as `dev/runs/067_d7_C3_N16.json`

D7, C3, N = [16], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 68. 2026-10-15T23:17:54Z: run `dev/d6_theoremD.py` (case: theoremD:R3)

Script SHA-256 `c88e57ef38a5dc67285e3d88ab7e5a16b13650e1bd75d4e9418f54a140a724e0`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_theoremD_N16_24_32.out` `9b7fdc5f3749e5c90166b390c9e6298cfd36012749bcc74d98e399d72c15a4c6`, kept as `dev/runs/068_d6_theoremD_N16_24_32.out`
- output `dev/d6_theoremD_N16_24_32.json` `80208fc46460b7a56a9df20826d7d33047ebaf493c45896d2644db1953da2fe8`, kept as `dev/runs/068_d6_theoremD_N16_24_32.json`

D6, N = [16, 24, 32]: 6 failures; see the output.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row C1 {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (the acceptance bound 1e-15 for the residual; 1e-14 off level 2; 1e-10 for the lowest level against Theorem D; the record as in DL; 1e-12 along the ladder). The run informed none.

## 69. 2026-10-15T23:34:04Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N16_24_32.out` `28b9b993021ab24855e1bdc6d16a9cfa5aeae1666e6f452dfd8f91672dd45319`, kept as `dev/runs/069_d7_C2a_N16_24_32.out`
- output `dev/d7_C2a_N16_24_32.json` `0657827eab7dab5e22d02ee8f8827f1ae6d3654d0ac783cd563a86f7fb92b8b8`, kept as `dev/runs/069_d7_C2a_N16_24_32.json`

D7, C2a, N = [16, 24, 32], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 70. 2026-10-15T23:40:12Z: run `dev/d7_controls.py` (case: C2b)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2b_N16_24_32.out` `07ba7ac37454bfea7ae6ba35cbb46e24e97b208006c9cd7186a4e23606fc84a3`, kept as `dev/runs/070_d7_C2b_N16_24_32.out`
- output `dev/d7_C2b_N16_24_32.json` `6b1b2196af90accc3adc4101eb5bad60132dcfd826dfc4fd07ca2915c72a25cd`, kept as `dev/runs/070_d7_C2b_N16_24_32.json`

D7, C2b, N = [16, 24, 32], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 71. 2026-10-15T23:54:55Z: run `dev/d7_controls.py` (case: C3)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C3_N16_24_32.out` `f0284afa82685cc5b564cbccb6198b56a11d618dad08e9a0fdc611ae12bd0b33`, kept as `dev/runs/071_d7_C3_N16_24_32.out`
- output `dev/d7_C3_N16_24_32.json` `a913a5d024d21a6ba6d56ea3361df7f5e22af107c60ec04a38b89ade78a103e4`, kept as `dev/runs/071_d7_C3_N16_24_32.json`

D7, C3, N = [16, 24, 32], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 72. 2026-10-16T00:11:00Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N40_eps0.5.out` `4751ecde8cec2ee3be9df1b8146aacca7ad6a5c58672447a300d535607602ad9`, kept as `dev/runs/072_d7_C2a_N40_eps0.5.out`
- output `dev/d7_C2a_N40_eps0.5.json` `7afd29a6f11dfbe58ce0c135343a20f258a121329c0b64916347303573225220`, kept as `dev/runs/072_d7_C2a_N40_eps0.5.json`

D7, C2a, N = [40], eps = [0.5]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 73. 2026-10-16T00:18:59Z: run `dev/d6_diagnose.py` (case: theoremD:R3)

Script SHA-256 `e5c80c572332eff460d9c13da456bf0ea812fd210aa94009a939a383a3ee86cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_diagnose.out` `112543054d27fa51d1316899a38044e9c64203c712dbdbf49c3cdafa371c438f`, kept as `dev/runs/073_d6_diagnose.out`

A diagnostic of D6's claim 1 at N = 16, 24, 32; it scores nothing.

## 74. 2026-10-16T00:21:12Z: the first sample at N = 16, 24, 32; D6's claim 1 diagnosed; one N = 40 point timed

**D7: every claim passes** at N = 16, 24 and 32, for C2a (entry 69), C2b (entry 70) and C3 (entry 71).
- The seeds' Q matches 1288/1287, 144/143 and 175/143 to about 1e-15 at every N.
- Every point is accepted, with floors near 1e-17 relative.
- V₀ matches its row of EXPECTED_V0.md, with leaks of 1e-12 to 1e-10.
- The types and indices are as derived: C2a and C2b Elliptic with (0, 0, 0); C3 Hyperbolic with (6, 3, 3) and k_r = 3.
- Nothing is unresolved.
- **Theorem R's largest deviation at N = 32,** against the leading order: at ε = 0.5 and 2 respectively, C2a 1.45e-2 and 5.59e-2; C2b 9.12e-3 and 3.56e-2; C3 1.02e-2 and 3.96e-2. It grows with ε, as the o(1) requires, and is unchanged from N = 24.
- **The slow eigenvalues' relative change from N = 24 to 32** is 2.4e-11 to 3.0e-7 (unscored; it is the input to DESIGN.md §10.2's fraction).

**D6 (entry 68): claim 1 fails at N = 24 and 32, at all three ε; everything else passes at every N.** Claim 1 asked that Theorem B's exact member have a residual below 1e-15 against the size. It reads 4.3e-15, 6.1e-15 and 1.5e-14 at N = 24, and 1.4e-15, 2.9e-15 and 4.7e-15 at N = 32. At N = 16 it reads 7.2e-17 to 2.5e-16. The other claims pass at every N:
- the cubic off level 2 lies at about 2e-15 of it;
- the lowest level matches Theorem D to about 1e-14;
- V₀ has dimension 6, ranks [1, 0], 5 chains, and leaks of about 1e-13;
- (0, 0, 0), Elliptic, nothing unresolved;
- along the ladder, the lowest level's eigenvalues agree to 2e-14.

**The cause (entry 73, a diagnostic that scores nothing): the test, not the instrument.**
- On D6's unit seed v, |ψ|² = 1 holds at every node to 2e-15, and the weights sum to 1 within 1e-14.
- The rule's own orthonormality on level 2, ||G − I||, is 4.2e-14 to 8.7e-14 with whole-node chunks, and 3.6e-15 to 1.1e-14 with one-row chunks. D2's claim 4 measured the same scale in R4 and R5 at N = 24: 2.6e-14 and 2.8e-14.
- The cubic on level 2 is v times the rule's Gram matrix there, so it carries that error: 4e-15 to 2.2e-14 in the groupings tested. D6's own grouping gave 9.3e-14 in Q(v) at N = 24.
- At a weight vector the cross terms vanish through the exact angular sums, which is why D7's seeds read about 1e-16. D6's generic v carries the error in full.

So:
- **Newton's floors** (D5, D7) are measured on the root of the computed equations, at about u times the size.
- **Theorem B's member** is the exact continuum point, which sits off that root by the rule's round-off. Its residual is about 1e-13 of the cubic, and reads 1e-15 to 1e-14 against the size.
- **The bound is the wrong yardstick.** The acceptance bound applies to a converged iterate, and claim 1 measured an unsolved point against it.

Newton cannot settle it either. The rigid family's fifth kernel direction is not a symmetry, and the computed equations tilt along it by about the same round-off, so a border there leaves a multiplier of that size, which the bound refuses.

**For the units, not applied.** A claim 1 measured against the rule's own round-off: the residual at the member, relative to the cubic on level 2, at most ten times the level-2 Gram error, measured in the same run at the same N; and the cubic off level 2 below 1e-14 of it, as now. The proposal is informed by this run, and is disclosed as such. D6 is not rerun until the units rule.

**Timing at N = 40 (entry 72): C2a at ε = 0.5 passes every claim.**
- Accepted at a floor of 2.8e-17 relative.
- V₀ dimension 4, ranks [1, 0], leak 1.3e-10; (0, 0, 0), Elliptic; the five slow pairs at a largest deviation of 1.45e-2, as at N = 24 and 32.
- **The cost:**
  - 37 s of setup;
  - 2 solves of 4 and 3 Newton evaluations, at 114 s each (798 s);
  - the record's Hessian, 107 s, and the record itself, 21 s;
  - 927 s for the point in all.

**The other eleven N = 40 points, estimated from that point:**
- C2a's ladder, rerun from its germ so its continuation stays whole: about 53 min.
- C3: about 65 min, at 9, 9 and 13 evaluations, as at N = 32.
- C2b: about 17 min, scaling R4's per-evaluation time by r m² (0.26) and adding R2's longer setup.
- D6: about 7 min, with no solve.

In all, about 2.4 hours on this machine, unattended. That goes to Blake for the cost decision, as UA and UB set it.

## 75. 2026-10-16T01:41:01Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N40.out` `ae7bc63c773458aa2759671b008cf3d480ae7fa8bdc05a8828c0b51accd9e273`, kept as `dev/runs/075_d7_C2a_N40.out`
- output `dev/d7_C2a_N40.json` `09d46b639d18424df7bf0f2e07b966f06e50539d33a625488c7f4719065d71b6`, kept as `dev/runs/075_d7_C2a_N40.json`

D7, C2a, N = [40], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 76. 2026-10-16T02:35:40Z: run `dev/d7_controls.py` (case: C2b)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2b_N40.out` `c027711e66cabaee2b0e6ee9c56f91bc9f2d55e1b84bc84f2a8de64f1c11907a`, kept as `dev/runs/076_d7_C2b_N40.out`
- output `dev/d7_C2b_N40.json` `93a68988af39e61fc1336e10a3aaf9577471a063a8df641bc109159f6395ba8d`, kept as `dev/runs/076_d7_C2b_N40.json`

D7, C2b, N = [40], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 77. 2026-10-16T06:43:56Z: run `dev/d7_controls.py` (case: C3)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C3_N40.out` `d3ab93bb5b23308823442ef70afcb86ec82887e6792e738b0a98b11428c30ec6`, kept as `dev/runs/077_d7_C3_N40.out`
- output `dev/d7_C3_N40.json` `2a945322352112349a7f88f266d35ee1fb5dd08ac037ddfb183e22def15a89ef`, kept as `dev/runs/077_d7_C3_N40.json`

D7, C3, N = [40], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 78. 2026-10-16T06:46:23Z: D7 at N = 40, on Blake's cost decision; convergence; the cost as measured

**Blake's decision:** run D7's three ladders at N = 40 now, and D6's N = 40 points after the units rule on its claim 1.

**D7 at N = 40: every claim passes** for C2a (entry 75), C2b (entry 76) and C3 (entry 77).
- The seeds' Q matches to about 1e-15.
- Every point is accepted, at floors of 5e-18 to 3.5e-17 relative.
- V₀ matches its row, with leaks of 1.5e-12 to 1.3e-10.
- C2a and C2b are Elliptic with (0, 0, 0); C3 is Hyperbolic with (6, 3, 3) and k_r = 3. Nothing is unresolved.
- Theorem R's largest deviations at ε = 0.5, 1 and 2 are the same as at N = 32: C2a 1.45e-2, 2.86e-2 and 5.59e-2; C2b 9.12e-3, 1.81e-2 and 3.56e-2; C3 1.02e-2, 2.02e-2 and 3.96e-2.

**Convergence in N** (an analysis of the logged outputs, not a run).
- The type, (n(L), n(D), K) and the slow Krein signs agree at N = 24, 32 and 40 at every point.
- The reached ε agree to nine digits across those N, so the slow eigenvalues, each divided by its reached ε, measure convergence in N alone. Their largest relative change over the three controls and three ε is 7.0e-3 from N = 16 to 24, 3.0e-7 from 24 to 32, and 9.9e-12 from 32 to 40.
- DESIGN.md §10.2's fraction is to be fixed from these. **The proposal for the units:** 1e-6, between the two highest N. It is informed by these runs, and disclosed as such.

**The cost, as measured.** The estimate was about 2.3 h.
- **The points' own timers** add up to about 3.6 h:
  - C2a 74 min, C3 88 min and C2b 55 min;
  - per-evaluation times of 73 to 76 s in R2 and 115 to 216 s in R4, where the timing point had read 114 s;
  - C2b's setup, which includes the fibre structure's matrix, took 989 s.
- **The wall clock** ran 6 h 17 min, from 00:26:41Z to 06:43:56Z.
- **The gap.** The timers use `time.perf_counter`, which on macOS does not advance while the machine sleeps. The sleep setting is 1 minute, and `pmset -g` shows sleep held off by Claude only while the app holds an assertion. So the 2.7 h gap is most likely sleep between turns (INFERRED; the power log was not readable here).
- **Next time:** a long run requests the app's keep-awake first.
- **Flagged for later, not changed:** the fibre structure's matrix is assembled by `einsum`, which is the likely cost of R2's setup at N = 40; a GEMM would do it.

## 79. 2026-10-16T06:47:09Z: DESIGN.md v2.7

- **§8:**
  - **D5's off-grid claim:** UB's text, verbatim, with ε = 0.1 added as UA's case, its floors against the cancelled size reported unscored.
  - **"Before D6 and D7":** the scripts read the expected rows only through the logged hash, and check each seed before any solve.
  - **D6:** how the member is built; and, flagged, that claim 1 as first run measured an unsolved point against Newton's acceptance bound, and that the units are asked for a criterion (entry 74).
  - **D7:** the derived types and indices, and the o(1) check on Theorem R.
- **§9:** the costs measured at N = 40; the keep-awake rule; and the einsum flagged for later.
- **§10.2:** the proposed fraction, 1e-6 between the two highest N, informed by D7 and flagged as a proposal.

SHA-256 `bc7d2a294dece4010913e7b174ea7d6f1519510f3301c6690031cde7acf86fda`. No run.

## 80. 2026-10-16T06:47:37Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/080_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 81. 2026-10-16T06:47:48Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/081_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 82. 2026-10-16T06:47:50Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/082_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 83. 2026-10-16T06:47:57Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `cedbd2f71ebf3a7d5ecef2b3c541503a8a79803ff1f16fe8de0dceaf0a3cae0c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `37569cbfeb6ebf1ad11a82b2cbd174f3b8a5b30846430a7579a5fff850415c88`, kept as `dev/runs/083_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 84. 2026-10-16T06:48:31Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `4a93719a270eb02806a4555c468222b275704ce8ae7b847b2d26e9bb20955c52`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `d302ffbee5510b2b4ffe111484cc9ab942aa3ec2b2e6d18495ed8cdb57edfde1`, kept as `dev/runs/084_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, claim 4 at N = 24 and claim 5 off the float grid, 5 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in newton.solve, for the floor, the unbordered residual and the multipliers, against the size of the terms before they cancel; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 85. 2026-10-16T06:48:33Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `a764b4ff579dcc6d3029b3a1d5534efdc58760242d9c0c965a7cc641efb3d047`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/085_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 86. 2026-10-16T16:11:19Z: run `dev/d6_gemm_check.py` (case: theoremD:R3)

Script SHA-256 `394a176bc6abba685c6614f0df2bfef0ae20dbc12de8decd13df428e8df250a2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `71a8635e95a8c35ceb21132b2e63a1c4d58d477ecf661c52fed24262c08c5f69`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_gemm_check.out` `19853756da6fc5090f74117a496d43e89ae74675d183ba91e5d71844b219b74a`, kept as `dev/runs/086_d6_gemm_check.out`

UB's einsum finding on D6's claim 1, checked before any change to functional.py; it scores nothing.

## 87. 2026-10-16T16:12:50Z: the units' review of the first sample folded; GEMM accumulation; before any rerun

Both units confirm D5 and D7.

**D6's claim 1: the units differ, and I adjudicate for UB's route.**
- **UA** approved replacing the claim by a bounded criterion: g_N = ||G₀₀ − I||₂ and δ_N, the largest | |ψ_v|² − 1 |, each at most 1e-12, and the on-level residual at most min(10(g_N + δ_N + u), 1e-12).
- **UB** dropped any replacement. UB keeps the claim as registered and finds most of the cubic's round-off in einsum's accumulation in `functional.py`, with GEMM making the claim pass as written. UB also showed that my proposed bound, tied to the Gram error, would not measure the claim: with whole t-nodes the Gram error is 8.7e-14 while the cubic's is 4.7e-15.
- **Entry 86 checked UB's finding on this machine, before any change.** In D6's own grouping, the level-2 identity of the cubic reads, with einsum and then with GEMM:

| N | einsum | GEMM |
| --- | --- | --- |
| 24 | 1.1e-13 | 2.7e-15 |
| 32 | 5.2e-14 | 8.4e-16 |
| 40 | 3.6e-14 | 5.2e-16 |

  Claim 1's residual against the size, at N = 16 to 40, reads 5.8e-16 to 1.5e-14 with einsum, and 3.7e-17 to 2.9e-16 with GEMM, under the bound 1e-15 at every point.
- **So** claim 1 stays as registered, a test stricter than UA's bound, and nothing is relaxed after the failure.
- **UA's quantities** are reported beside it in D6, unscored, so that UA can see both. If the claim as registered failed anywhere, UA's approved criterion would be the fallback, disclosed.
- The failed run (entry 68) and the diagnostic (entry 73) stand.

**`instrument/functional.py` (UB's text, verbatim).** The cubic, the Hessian-vector product and the fibre structure's matrix accumulate each chunk by a GEMM, P.reshape(−1, m)ᴴ (·). The two einsums left contract over r or 2r terms only. UB measured equivariance unaffected, at 3e-15 under either accumulation, so D7's results stand. The fibre matrix's einsum was also the likely cost of R2's 16.5-minute setup at N = 40.

**Other items:**
- **The §10.2 fraction.** 1e-6 is approved as provisional and development-calibrated (UA), to be fixed after the full ladders, since convergence is slowest at high ε (UB). It is not a guarantee for near-zero crossing modes or the full windows, which need their own adequacy and unresolved rules before the freeze (UA).
- **UA's wording correction.** The deviations' near-linear growth in ε is consistent with Theorem R(a)'s o(1); the theorem does not require it. The DESIGN text will say so.
- **UB's §7 recalibration text, before the freeze and not blocking.** The margin, the gray zone and the leak bound are to be recalibrated on the controls' measured clusters and gaps. The cluster's largest eigenvalue is at most 2.6e-8, 420 to 1,160 times below the margin, and the leak tracks u||A||/gap. The record must resolve a slow pair below 1.04e-5 at N = 40, M8.15's level-3 cluster tolerance. UB names the pyramid's in-span mode as the case that matters. That is context from M8.15's published record; the pyramid stays sealed, and the calibration uses the controls only.
- **The full-window ladders are held (UA)** until a bounded coverage and cost plan is presented: which points compare against M8.15, at which cutoffs, and the measured budget. UB's option: every ladder at N = 24 and 32, and N = 40 only at each ladder's top three points and where the 24 → 32 change exceeds the fraction. Blake's cost decision follows the units' review of the plan.

**D6** now reports UA's quantities, unscored; its claims are unchanged.

Next, in order, on this package: D1 to D5, DL, D6 at N = 16, 24, 32 and 40 (UA's GO for its N = 40 points), and D7 at N = 16 and 24 as a regression (UB).

## 88. 2026-10-16T16:13:02Z: run `dev/d1_group.py` (case: synthetic)

Script SHA-256 `1e8deb8a8d33cc406af7b6614bf34421d3454dc0307aeb2fc886c6a43f08b873`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d1_group.out` `60b6d790369d0024b0f4be9581150b0f8fe4cd2887ee9ff3b469ad0e13001a52`, kept as `dev/runs/088_d1_group.out`

D1, the group and its representations: PASS, 3 claims, 4 arms red.
Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value below 1e-12 against a live one above 1e-3). The run informed none of them.

## 89. 2026-10-16T16:13:15Z: run `dev/d2_basis.py` (case: synthetic)

Script SHA-256 `2f9e5f0bdcefb2f6d12ee2e2b8876282fe6239f64e4cdab89bbf6f553fd1ba80`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d2_basis.out` `6b8c59fe31418f7a45574803eec5b9bc04c6f3772247619a4ce229c8ffd965e1`, kept as `dev/runs/089_d2_basis.out`

D2, the basis: PASS, 5 claims over all eight slots, 3 arms red.
Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10 and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.

## 90. 2026-10-16T16:13:16Z: run `dev/d3_rule.py` (case: synthetic)

Script SHA-256 `c6036199d6ba3dc7f4ef09d8879bf5527964818f9016c3abcd29adcbd7dfa709`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d3_rule.out` `4af02e0b9e63762efdbe7bf5fb149d446f0ab2528a80485b510bf1a3822759eb`, kept as `dev/runs/090_d3_rule.out`

D3, the rule: PASS, 4 claims, 2 arms red. Exactness is shown against the derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the quartic of random soft-slot sections), not by comparison with any other rule.
Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.

## 91. 2026-10-16T16:13:22Z: run `dev/d4_invariance.py` (case: synthetic)

Script SHA-256 `cedbd2f71ebf3a7d5ecef2b3c541503a8a79803ff1f16fe8de0dceaf0a3cae0c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d4_invariance.out` `056085a40c7285238c6db7db0bf48bb40edbc4425304be6ad56f79953613b55b`, kept as `dev/runs/091_d4_invariance.out`

D4, invariance and the Hessian identities: PASS, 3 claims on all eight slots and the chunked path, 2 arms red.
Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12 for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.

## 92. 2026-10-16T16:13:54Z: run `dev/d5_newton.py` (case: manufactured)

Script SHA-256 `4a93719a270eb02806a4555c468222b275704ce8ae7b847b2d26e9bb20955c52`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d5_newton.out` `960295fba77fc54110b1d0a05e0743f7da8999f297f1c2b46b8c42347d9146a5`, kept as `dev/runs/092_d5_newton.out`

D5, manufactured solutions: PASS, 3 claims on R4, R5 and R2, claim 4 at N = 24 and claim 5 off the float grid, 5 arms red. The forced problem tests the solver only, never the unforced kernel (UA).
Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in newton.solve, for the floor, the unbordered residual and the multipliers, against the size of the terms before they cancel; |c - c*|/|c*| below 1e-12 and |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10 relative). The run informed none.

## 93. 2026-10-16T16:13:55Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `a764b4ff579dcc6d3029b3a1d5534efdc58760242d9c0c965a7cc641efb3d047`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/093_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 94. 2026-10-16T16:26:32Z: run `dev/d6_theoremD.py` (case: theoremD:R3)

Script SHA-256 `d991e6d0bf6225dfeef1b30fecaa2c129535435e000fa0a7041371289d19c194`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_theoremD_N16_24_32_40.out` `f871b9f7e9dc2dd102e1ce05ccf9ec53e5002b13fd6ab60710e85e3f733b6d4e`, kept as `dev/runs/094_d6_theoremD_N16_24_32_40.out`
- output `dev/d6_theoremD_N16_24_32_40.json` `c4f82a172447fcfa801b42e9edbc87cd4171a5cf09619e0c06e356bcfcaf5c1c`, kept as `dev/runs/094_d6_theoremD_N16_24_32_40.json`

D6, Theorem D at R3, N = [16, 24, 32, 40]: PASS, 4 claims at eps 0.5, 1 and 2.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row C1 {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (the acceptance bound 1e-15 for the residual; 1e-14 off level 2; 1e-10 for the lowest level against Theorem D; the record as in DL; 1e-12 along the ladder). The run informed none.

## 95. 2026-10-16T16:28:29Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N16_24.out` `d239410e42bff9b079fefa5505447b5ca4a8c080ddbfee9a21531c57244120d1`, kept as `dev/runs/095_d7_C2a_N16_24.out`
- output `dev/d7_C2a_N16_24.json` `f20e77fbbf5fda33fbf6fd43cfdf27bdf128935896e05db0896f03d80ad6c243`, kept as `dev/runs/095_d7_C2a_N16_24.json`

D7, C2a, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 96. 2026-10-16T16:29:11Z: run `dev/d7_controls.py` (case: C2b)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2b_N16_24.out` `071994c7051eae28f5a055e1ecfe44f0f1471df589c02486e4fc4a502e63bc04`, kept as `dev/runs/096_d7_C2b_N16_24.out`
- output `dev/d7_C2b_N16_24.json` `a2128d30e68511d50e736874e9e0b09a34fc86bc9f9eadd9b9167f4597fd0cde`, kept as `dev/runs/096_d7_C2b_N16_24.json`

D7, C2b, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 97. 2026-10-16T16:31:15Z: run `dev/d7_controls.py` (case: C3)

Script SHA-256 `7a3f5e4007c8e89ca040b688f3a389765426aef2c1bcd15095d12a73726f2ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C3_N16_24.out` `f5a11b2b507f45648fee9095cdeb476fb2fa81c02bc512ff07b5cb808440a520`, kept as `dev/runs/097_d7_C3_N16_24.out`
- output `dev/d7_C3_N16_24.json` `ab881fd423dd183d31f1e90f02361cf6739746f44c99de01c2739784218e7cba`, kept as `dev/runs/097_d7_C3_N16_24.json`

D7, C3, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as in DL; slow eigenvalues beyond ten margins and below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 98. 2026-10-16T16:32:02Z: D6 passes as registered; D7's regression; LADDER_PLAN.md; DESIGN.md v2.8

**D6 at N = 16, 24, 32 and 40 (entry 94, on the GEMM package): every claim passes**, claim 1 as registered.
- Claim 1's residual is 5.2e-17 to 2.9e-16 of the size, against the bound 1e-15, and the cubic off level 2 is at most 1.8e-15 of it.
- The lowest level matches Theorem D to 3.8e-14 or better.
- V₀ has dimension 6, ranks [1, 0], 5 chains, and leaks of 1.0e-12 or less. The indices are (0, 0, 0), the type Elliptic, and nothing is unresolved.
- Along N = 16 to 40, the lowest level agrees to 3.5e-14.
- **UA's bounded criterion, reported unscored,** passes at every point. g_N is 3.1e-15 to 3.7e-14 and δ_N about 1.9e-15, and the on-level residual of 2.4e-16 to 2.7e-15 sits against bounds of 5.2e-14 to 3.9e-13.
- **The seed check improves with GEMM.** Criticality at N = 24 was 5.7e-14 in entry 68, and is 2.4e-15 here.
- D6's N = 40 points, on UA's GO, took 165 to 205 s each.

**D7's regression at N = 16 and 24 (entries 95 96 97 ): every claim passes.** Against the einsum runs (entries 69 to 71), the slow eigenvalues moved by at most 3.0e-12 relative, with the types and indices identical. So D7's results stand. R2's setup at N = 24 took 1.7 s, where it took 8.1 s.

**`LADDER_PLAN.md`** answers UA's hold on D7's full-window ladders: which points, at which cutoffs, and the measured budget. It is a plan for review; nothing in it runs before the units' review and Blake's cost decision.
- **The points:** M8.15's ladder(0.25, ε_max), read from its code: 18 points in R4 and 20 in R2.
- **The cutoffs:** N = 24 and 32 everywhere, and N = 40 at each ladder's top three points and where 24 → 32 exceeds the fraction.
- **The seeding:** N = 40 from N = 32 at the same ε, embedded exactly. That is a change to §6, for the units.
- **The budget:** about 6.6 h, plus those extra points.

SHA-256 `99b40ef1859770e5fc71e852e4dff40114936e47fc293cef20d3cf992f732824`.

**DESIGN.md v2.8:**
- **§4:** the GEMM accumulation.
- **§7:** UB's recalibration paragraph, verbatim.
- **§8:**
  - D6's claim 1, as resolved;
  - UA's wording on Theorem R's o(1);
  - the full ladders, held for the plan.
- **§9:** R2's setup with GEMM.
- **§10.2:** the fraction, provisional, with UA's and UB's conditions.

SHA-256 `793ee8b023d2e677cb0776dad07d43591c4da31f6b9ebfea729f306643940593`. No run.

## 99. 2026-10-16T16:50:57Z: the units confirm D6; the ladder plan's conditions folded; DESIGN.md v2.9

UA and UB confirm D6, claim 1 as registered, and the GEMM change. UA gives the ladder plan a conditional GO, and UB a GO with two changes. Both are folded into `LADDER_PLAN.md`.

**UB's comparison text, folded verbatim.**
- Each point compares: the type; K against M8.15's `nL` − `nB_cluster`; the slow Krein signs; and each slow eigenvalue per unit ε against M8.15's level 3, beside M8.15's own level-2 to level-3 change, unscored. n(L) and n(D) are reported beside `nL` and `nB_cluster`, unscored.
- **Checked first, against the records** on MIT main (2c27cea), which equal those at `6058f95`. This was an analysis of published records, not a run.
  - `nL` and `nB_cluster` are 2 and 2 in C2a and C2b through ε = 32 and 0 beyond, and 9 and 6 in C3 throughout. So K is 0, 0 and 3 at every point, and every type agrees.
  - Per unit ε, M8.16's slow eigenvalues at N = 40 sit inside M8.15's level-2 to level-3 change at every sample point. At ε = 0.5: C2a 1.8e-3 against 1.4e-2, C2b 9.1e-5 against 7.4e-3, C3 4.2e-6 against 7.3e-6. At ε = 2, C3 reads 9.9e-6 against 1.2e-4. These are UB's numbers, reproduced.

**The pause: UA's rule, which is stricter, is taken.** The base plan runs first: N = 24 and 32 at every point, and N = 40 at each ladder's top three. Then the run stops and reports how many points exceed the fraction, with their cost. No extra N = 40 point runs before Blake authorizes a bounded extension. UB's text paused only when more than three points of a ladder exceeded it.

**UA's branch-identity guard, at each N = 40 point seeded from N = 32:**
- it records the embedding's residual, the symmetry-aligned distance, and both norms and frequencies;
- the identity is Unresolved if the aligned distance exceeds 1e-2, or if the type, the indices, the slow Krein signs or V₀ differ from N = 32's;
- **1e-2 is mine, proposed and flagged.**

**Also folded:**
- **UA's §7 note.** Resolving a slow pair below 1.04e-5 needs a synthetic demonstration with its own mutation arms, in the pre-freeze review.
- **The run's tab.** The ladders run in a visible Terminal-panel tab, so Blake can watch them live (his request, 2026-10-16).

**`DESIGN.md` v2.9:**
- **§6:** the cross-N seed, with its guard.
- **§7:** UA's demonstration note.
- **§8:** the ladders, under the plan, once Blake approves its base budget.

**The hashes.** `LADDER_PLAN.md` SHA-256 `c27186b1fa31e7c8df900aa5140c2e0061ffe19d9732379cf997633c570ddbc3`. `DESIGN.md` SHA-256 `796db602074e24d78134e8f70ed69abdbbf17200e001564cfef3745660208225`.

Next: Blake's decision on the base budget, about 6.6 hours. No run.

## 100. 2026-10-16T16:55:35Z: Blake approves the base budget; M8.15's records copied; the ladder driver

**Blake's decision.** He approves the base plan of `LADDER_PLAN.md`, about 6.6 hours. He asked to watch it as a background task in the app's sidebar, not in a separate Terminal window, so it runs as a sidebar task with unbuffered output.

**M8.15's three control records are copied to `reference/m815/`, read-only,** so the packet carries what it reads. The source is `soft-slot-dynamics/m8_15_solver/out/` at MIT `6058f95` ("soft-slot dynamics: the M8.15 solver, frozen, with its control records"), identical at main, 2c27cea:
- `branch_C2a_R4.json` `c5266378170a2f425eb9423b0886f2a7e9db1628d4c5f80e0f70ac5aba888fde`;
- `branch_C2b_R2.json` `25bcee62a88a05d03703c0a523621ac1e812ce09f8b7d0792d1ebd9fc129a716`;
- `branch_C3_R4.json` `61c9d81899a80a8179582a60f52eb17fd36f71a42476374df275e28e3348d284`.

**`dev/d7_ladders.py`, new.**
- **The plan, as written:**
  - M8.15's `ladder(0.25, ε_max)`, copied from its code;
  - N = 24 and 32 along every ladder, from the germ;
  - N = 40 at the top three points, seeded from N = 32 with UA's guard;
  - the pause, which reports the points over the fraction and their estimated cost.
- **The claims, fixed before the run:** each point accepted; V₀ as expected, or the point reported Unresolved; and, where both are resolved, the type, K and k_i⁻ agreeing with M8.15's.
- **Slow eigenvalues are matched to M8.15's tracked values,** not read through a fixed window. The slow eigenvalues grow with ε, to about 1.1 at ε = 45 in C2a and 2.8 at ε = 128 in C2b, and at the top of each window the next level's modes come near zero, since ε_max is the gap. The sample's window, |λ| < 1, would lose them there.
- **A trial first:** N = 16 to ε = 2, then N = 24 at that range's top two points, seeded from N = 16, which exercises the guard.

## 101. 2026-10-16T16:56:42Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `a837eb237bcaabd583662d67e958b82c736c08d464bdebac91057f598df087a4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial.out` `68dd5cbaca44b1272d291527408f5391adf375d0a56b3745a205cdca58c76315`, kept as `dev/runs/101_d7_ladders_C2a_trial.out`
- output `dev/d7_ladders_C2a_trial.json` `0c35a51fdef90a7d8445a29117b7eff1c780e7c98013f68ce56728212ea29ab4`, kept as `dev/runs/101_d7_ladders_C2a_trial.json`

D7's ladders, C2a (trial): PASS; 0 failures of claims 1 and 3; 0 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 102. 2026-10-16T17:43:28Z: C3's ladder moved to a parallel run, with no file changed

**Timing (Blake asked, at 17:25Z).** The base run (a sidebar task, started 16:57:03Z, chained as C2b, then C2a, then C3) was running 1.6 to 2 times the first sample's pace:
- C2b's points at N = 32 took 110 to 156 s.
- At 16 to 17 s per Newton evaluation, against 8.6 s in the first sample, it projected about 11 hours.

The Mac is on AC power, Low Power Mode is off, and the run is at normal priority (31, nice 0), at full CPU. Blake closed his other apps, and the evaluations fell to about 9.8 s. Higher-ε points also take more evaluations: 15 or 16 from ε = 22.6 on, against 7 to 9 at small ε.

**Two levers were weighed.**
- **Caching the basis at N = 32.** It is 3.5 GB in R2 and 8.3 GB in R4, over the 2 GB threshold. A timing beside the live run, for R2 at N = 32, read 12.5 s per Newton evaluation without it and 8.9 s with it. It is not applied, because `log_run` hashes the script and the instrument files when a run finishes, not when it starts. Changing any of them now would make the record of every run still in flight claim code it did not run.
- **Running a second control in parallel,** on the idle cores, with no file changed. The timing test above ran beside the live job, and the job's next point (ε = 90.5, 9.9 s per evaluation) did not slow, so sharing the matrix unit costs little.

**So C3's ladder starts now, as its own sidebar task** (`python3 -u d7_ladders.py C3`, the same unchanged script).
- A sidebar watcher waits for the chain's own C3 to start, after C2a, and stops that duplicate, a child of the chain's shell, before it can log.
- C2b's and C2a's runs, and this C3 run, each log themselves. No file changes until all three have finished.

## 103. 2026-10-16T18:07:29Z: run `dev/d7_ladders.py` (case: C2b)

Script SHA-256 `a837eb237bcaabd583662d67e958b82c736c08d464bdebac91057f598df087a4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2b.out` `a8a46781af6bde3ca81f2bfc8f4c256f9dc0ab25064c7d67127d41c961cc00ab`, kept as `dev/runs/103_d7_ladders_C2b.out`
- output `dev/d7_ladders_C2b.json` `0119130f1d214e80fdff9e98a6f677fa9199a6e1fdfc476e893408a4dd5a2559`, kept as `dev/runs/103_d7_ladders_C2b.json`

D7's ladders, C2b: PASS; 0 failures of claims 1 and 3; 7 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 104. 2026-10-16T20:55:11Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `a837eb237bcaabd583662d67e958b82c736c08d464bdebac91057f598df087a4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a.out` `8fe267b05ba47842681b8b2883f43e54c312cd4d49e61ff4ec852a8a29c56f25`, kept as `dev/runs/104_d7_ladders_C2a.out`
- output `dev/d7_ladders_C2a.json` `aa2a1d9113840abbf0258c36d676f204a7186edeaaa3aabb85efcd58aea14c98`, kept as `dev/runs/104_d7_ladders_C2a.json`

D7's ladders, C2a: PASS; 0 failures of claims 1 and 3; 1 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 105. 2026-10-16T22:03:28Z: run `dev/d7_ladders.py` (case: C3)

Script SHA-256 `a837eb237bcaabd583662d67e958b82c736c08d464bdebac91057f598df087a4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C3.out` `29e70c37c57e397f70ff85d8cb3e38c2f7112b9fef1963e841b02f0b11e573e4`, kept as `dev/runs/105_d7_ladders_C3.out`
- output `dev/d7_ladders_C3.json` `a345bc094dba35c609063e97bb8e3fb611e52b9b245305ddbfad614731417997`, kept as `dev/runs/105_d7_ladders_C3.json`

D7's ladders, C3: PASS; 0 failures of claims 1 and 3; 7 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 106. 2026-10-16T22:13:34Z: D7's base ladders complete; the pause; Blake: the units first

**The three runs are entries 103, 104 and 105.**
- All three carry the same script and instrument hashes, and those equal the files on disk after the last run ended. No file changed while any run was in flight.
- The chain's own C3 started at 20:55:11Z and was stopped by the watcher at 20:55:41Z, before it wrote or logged anything. Entry 105 and `dev/d7_ladders_C3.*` are the parallel run's (entry 102).

**Claims 1 and 3 pass at all 121 points** (C2b 43, C2a 39, C3 39).
- Every point is accepted, V₀ is as expected, and nothing is unresolved.
- The type, K and k_i⁻ agree with M8.15's at every point.
- Branch identity is kept at all 9 N = 40 points, with the record as at N = 32 at each. The largest aligned distance is 3.9e-04 (C3 at ε = 72), against 1e-2.

**Convergence, against the provisional fraction 10⁻⁶:** each slow eigenvalue's change, relative to its own size, between the two highest N (§10.2).
- **N = 24 to 32:** over the fraction at the highest 4 of 18 points in C2a, the highest 10 of 20 in C2b, and the highest 10 of 18 in C3.
- **At the top three points,** N = 24 to 32, then 32 to 40:
  - C2a: ε = 45.3: 4.0e-06 → 8.8e-10; ε = 64: 7.3e-06 → 1.4e-09; ε = 72: 8.7e-06 → 1.3e-09. Met at all three.
  - C2b: ε = 90.5: 6.0e-04 → 9.8e-07; ε = 128: 1.2e-03 → 2.5e-06; ε = 132: 1.2e-03 → 2.7e-06. Met at ε = 90.5 only. Where it is not met, the values over the fraction are the three largest of the five slow eigenvalues, not near-zero ones.
  - C3: ε = 45.3: 1.7e-03 → 2.3e-05; ε = 64: 3.7e-03 → 9.9e-05; ε = 72: 4.8e-03 → 1.6e-04. Met at none. The value is C3's triple real slow eigenvalue. Its change fell 30- to 73-fold from one step in N to the next.
- So the provisional fraction is not met at the top of C2b and C3, even at N = 40. §10.2 fixes the fraction after these ladders, "where convergence is slowest", and UA asked for the full windows' own adequacy rule before the freeze.

**Unscored.** Each slow eigenvalue per unit ε sits inside M8.15's own level-2 to level-3 change at 119 of 121 points. The two outside are C3 at N = 24, ε = 64 and 72: 3.6e-03 against 3.4e-03 and 4.7e-03 against 4.0e-03. At N = 32 and 40 both are inside.

**The pause.** Below the top three, 15 points are over the fraction from N = 24 to 32, and are unjudged without N = 40:
- C2a: 1 (ε = 32), 23 min at 23.1 min per point;
- C2b: 7 (ε = 8 to 64), 46 min at 6.6;
- C3: 7 (ε = 4 to 32), 279 min at 39.9.

About 5.8 hours in all, at the measured rates.

**Time.**
- Wall clock from 16:57:03Z to 22:03:28Z, 5.1 hours, against the plan's 6.6. C3 ran beside the chain from 17:43:36Z to 20:55:11Z.
- The scripts' own sums: C2b 70.4 min, C2a 167.7 min, C3 259.9 min.
- The Mac was on battery, where its Low Power Mode setting is on, from before 19:44Z to at least 21:36Z. C2a's and C3's N = 40 points began after 19:44Z, so the rates above were measured on battery, at least through 21:36Z.
- Two `caffeinate` holds, each tied to a run, kept it from idle sleep from 19:42:12Z, and released themselves at 20:55:41Z and 22:03:28Z.

**Blake's decision (2026-10-16): the units first.** The results and the convergence finding go to UA and UB. No extra point runs until they say what an extension should cover: more N = 40 points, higher N at the top, or the full-window rule. `DESIGN.md` stays at v2.9, and §10.2's fraction waits for their answer.

Next: the packet to the units. No run.

## 107. 2026-10-16T22:34:37Z: the units confirm the ladders; no extension; the driver's fail-safe and its arms

**The units' rulings (2026-10-16).**
- **UA.**
  - CONFIRM the folding, and the base plan as executed within scope.
  - CONFIRM all 121 results, with the convergence qualification kept visible.
  - HOLD the 15 extra N = 40 points, and higher N.
  - GO to the §10.2 rewrite, two driver safeguards and inexpensive mutation checks.
  - RETAIN the pre-freeze demonstration of a slow pair below 1.04×10⁻⁵.
  - C3's two N = 24 readings are unscored discrepancies, not failures.
- **UB.**
  - KEEP the folding, the driver and the results.
  - The extension: nothing new for D7.
  - The rule: my lean, with two specifics and §10.2 text.
  - §7 text on the cluster's growth, and a dated note on the plan.
  - C3's readings: no action.
- **No extension runs,** by Blake's "units first" and both units' rulings.

**Checked against the shipped records.** This is an analysis of records, not a run.
- **UA's C3 figures hold.** At ε = 72, N = 40, the real slow eigenvalue is 0.3412 and the margin 1.9e-5.
- **UB's figures:**
  - **The cluster's largest eigenvalue** is 2.5e-9 to 9.8e-9 at ε = 0.25 (UB: "about 4e-9"). Near the tops it is 1.8e-7 to 2.5e-7; the largest is 2.5e-7 (C2b, ε = 132, N = 24).
  - **At N = 40,** the slow eigenvalues sit 13.7 to 16.3 times inside M8.15's own level-2 to level-3 change. UB wrote "15 to 20"; C2b's three are 13.7 to 13.9. UB's two examples hold.
  - **The largest last change** is 7.1e-4 (C3, ε = 32, N = 32), and at the tops 1.6e-4 (C3, ε = 72).
  - **The geometric estimate of the error left at N = 40,** largest over the slow eigenvalues: C2a 2.0e-13 to 3.2e-13, C2b 1.6e-9 to 6.4e-9, C3 3.2e-7 to 5.5e-6.
  - **The slow band against the gray zone.** The smallest ratio of the distance (|λ| less ten margins) to the change (the estimate, or the last change, times |λ|) is 1.4e3 (C3, ε = 32, N = 32).
  - **The next level's near-zero modes at the tops** are not in the shipped comparison, so their changes cannot be read from the records. No mode outside the cluster is nearer zero than the smallest slow eigenvalue at any point.
- **UA's two findings hold in the code.**
  - **The guard.** `run_high` recorded `identity=False`, but left the comparison typed and counted it as agreement.
  - **The Krein comparison.** `compare` checks k_i⁻ against M8.15's `ki_minus`, not each mode's sign.
    - M8.15's records do carry a Krein value per mode: its `genuine` list pairs each eigenvalue with its Krein value (`verdict.py`).
    - From the records: k_i⁻ is 0 on both sides at every point. Each of M8.15's 190 tracked slow imaginary modes (C2a 90, C2b 100) has a positive Krein value, and no imaginary group in M8.16's records has a negative direction.
    - So, by this analysis, the per-mode signs agree at every point; the driver did not compare them. C3's 54 tracked slow modes are real, and carry none.

**`dev/d7_ladders.py`, corrected (UA).**
- **The fail-safe.** A failed identity marks the comparison Unresolved, with no agreement and no cross-N change.
- **An Unresolved comparison,** from either path, now reads Unresolved, never agree. Claim 3 fails only on a resolved disagreement.
- **The Krein part of claim 3** is stated as the count, in the docstring.
- **Three mutation arms, on the trial only:**
  - `guard_distance` and `guard_record` must each leave every N = 24 comparison Unresolved;
  - `guard_unsafe` turns the fail-safe off, which is the as-run path, and there the check must fail.
- **The base runs** (entries 103 to 105) stand under the hashes they ran with. Nothing reruns them (UA).

Next: the trial without an arm, as the control, then the three arms, about a minute each. Then the plan's note and `DESIGN.md` v2.10.

## 108. 2026-10-16T22:35:53Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `ad69aee347a605aafbde1399a36ca6445ab95a3a0bad9186b90d0649700c1b06`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial.out` `f627e95a48a140ffacd98e190bc144183f36153026c8815cbe544f8a28c3c42f`, kept as `dev/runs/108_d7_ladders_C2a_trial.out`
- output `dev/d7_ladders_C2a_trial.json` `4a272062d4c50c1c8c889d7f141f24cc042c4ea7f9c76fafee5222120d654cd5`, kept as `dev/runs/108_d7_ladders_C2a_trial.json`

D7's ladders, C2a (trial): PASS; 0 failures of claims 1 and 3; 0 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 109. 2026-10-16T22:37:00Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `ad69aee347a605aafbde1399a36ca6445ab95a3a0bad9186b90d0649700c1b06`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial_arm_guard_distance.out` `084e2947dbbbf9e4e105c1b2f9ecddd94262c8d38d607aa4a92eb7e0dc085ae8`, kept as `dev/runs/109_d7_ladders_C2a_trial_arm_guard_distance.out`
- output `dev/d7_ladders_C2a_trial_arm_guard_distance.json` `2807e00a8fc02b77341ebeac595a8faa320fc03c21fc8b956a131d338d36fa99`, kept as `dev/runs/109_d7_ladders_C2a_trial_arm_guard_distance.json`

D7's ladders, C2a (trial), arm guard_distance: PASS; 0 failures of claims 1 and 3; the arm: the guard fired at 2 of 2 points; the comparisons Unresolved, as required: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 110. 2026-10-16T22:38:06Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `ad69aee347a605aafbde1399a36ca6445ab95a3a0bad9186b90d0649700c1b06`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial_arm_guard_record.out` `06e0fb1f4fbdf70057d9437da7a9894c1fd22ce941267e538267ef45c56049db`, kept as `dev/runs/110_d7_ladders_C2a_trial_arm_guard_record.out`
- output `dev/d7_ladders_C2a_trial_arm_guard_record.json` `d4fccea281c7fa8cb43c3e1d697cc8320e0e2a58617aed4832edee3c2339b523`, kept as `dev/runs/110_d7_ladders_C2a_trial_arm_guard_record.json`

D7's ladders, C2a (trial), arm guard_record: PASS; 0 failures of claims 1 and 3; the arm: the guard fired at 2 of 2 points; the comparisons Unresolved, as required: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 111. 2026-10-16T22:39:12Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `ad69aee347a605aafbde1399a36ca6445ab95a3a0bad9186b90d0649700c1b06`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `cee5107c0bbde32ba4a42a5876aba683830659e80dc2ba14135550ba4462bfa0`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial_arm_guard_unsafe.out` `c99d782282fb76f38872c1cf2bf06b4ddedee2c2e7f209ae93fa5e4333b9080d`, kept as `dev/runs/111_d7_ladders_C2a_trial_arm_guard_unsafe.out`
- output `dev/d7_ladders_C2a_trial_arm_guard_unsafe.json` `2d2b21e93e01871ffc8531c4091038d6d33f1e9a60f99a080cae8b3167c05e47`, kept as `dev/runs/111_d7_ladders_C2a_trial_arm_guard_unsafe.json`

D7's ladders, C2a (trial), arm guard_unsafe: PASS; 0 failures of claims 1 and 3; the arm: the guard fired at 2 of 2 points; the comparisons left typed, so the check fails, as required: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 112. 2026-10-16T22:40:53Z: the fail-safe's arms pass; the plan's dated note; DESIGN.md v2.10

**The trial and its arms (entries 108 to 111).** Each is C2a's trial: N = 16 to ε = 2, then N = 24 at ε = 1.41 and 2, seeded from N = 16. Each took about a minute.
- **The control (108).** Identity is kept at both points, and both comparisons agree, with 0 failures. Its records equal the first trial's (entry 101) at every point, apart from the timing and the new `why` field.
- **`guard_distance` (109) and `guard_record` (110).** The guard fired at both points. Each comparison reads Unresolved (branch identity), with no agreement and no cross-N change. PASS.
- **`guard_unsafe` (111).** With the fail-safe off, which is the as-run path, both comparisons stayed typed and agreeing, with a cross-N change. So the check failed, as required. PASS.

**`LADDER_PLAN.md`: a dated note is appended, and the reviewed text is untouched.** It records:
- the sidebar runs, in UB's sentence, verbatim;
- that each comparison is read at the highest N it ran (UB);
- the Krein comparison as run (UA);
- the guard's fail-safe (UA);
- convergence under v2.10's §10.2, superseding the plan's bullet on the fraction;
- that the pause ended without an extension.

SHA-256 `099d61b1dcf91c00170bde2c5a77573fc727119b7e7a24a3c5185f1c41b124ff`.

**`DESIGN.md` v2.10:**
- **§7:** UB's text on the cluster's growth, with the measured ranges in place of "about".
- **§8:** the ladders' outcome.
- **§10.2, first bullet:** it names V₀ and the Krein structure, and points to the separation test. "Small relative to its own size", the retired criterion, is gone.
- **§10.2, second bullet:** UB's rule, merged with UA's conditions:
  - Unresolved where the separation cannot be shown;
  - the factor provisional, tested on the controls and on synthetic counterexamples before the freeze;
  - 10⁻⁶ kept as a diagnostic, failed at five upper-window points.
- **Mine, flagged for the units:** UA asked for numerical uncertainty, and UB's text does not say how. I fold it as "never less than the record's margin".

SHA-256 `4c90eb76041920aab60e526a79d50409c84262345ec05864459152e709ef967a`.

`dev/d7_ladders.py` SHA-256 `ad69aee347a605aafbde1399a36ca6445ab95a3a0bad9186b90d0649700c1b06`, as in entries 108 to 111.

Next: the packet to the units. No run.

## 113. 2026-10-16T23:01:32Z: D7 closes; DESIGN.md v2.11

**Blake's decision (2026-10-16): close D7 once the units' last changes are in** ("close if/when good"). Both units CONFIRM the v2 packet, and both give a GO to close: UA once its §10.2 clarification is entered, and UB once its §8 sentence is in.

**`DESIGN.md` v2.11.**
- **§10.2, UA's clarification.** The uncertainty is never below the larger margin of the two compared records. Residuals or spectral sensitivity raise it where they imply more, and where it cannot be adequately controlled, the comparison is Unresolved. The five failed diagnostics stay failed under the rule (UA).
- **§8, UB's sentence, with two corrections of mine:**
  - UB's ratio, 1.4×10³, is the change alone. With the margin floor, which both units confirm, the smallest ratio is 30.5 (C2a, ε = 0.25, N = 32), and the floor binds at 222 of the 244 slow eigenvalues. None falls below the factor of 10, at any of the 56 points.
  - UA's clarification makes eigenvalue residuals and sensitivities part of the uncertainty, and the shipped records do not carry them. So they join the next level's near-zero modes, as things first judged in the registered run.
- SHA-256 `d50694398df4e4e61101dfb5a01a3c4ade9f80631205543c4b7cc437066b0a5a`.

**What D7 established (UA's list).**
- All 121 control points reproduced the expected structural kernels and stability classifications, agreeing with M8.15's type, K and k_i⁻.
- All nine cross-resolution branch-identity checks passed.
- The five quantitative convergence exceptions remain reported. The 10⁻⁶ diagnostic fails at C2b's ε = 128 and 132 and at C3's top three (entry 106), and it stays failed.
- The next level's near-zero modes at the upper windows were not resolved by the shipped comparison. Their adequacy is for the registered qualification.

**Its limitations, on record (UB's list, with one added).**
1. The 10⁻⁶ diagnostic fails at five upper-window points. It is reported, and retired as a gate.
2. The next level's near-zero modes at the tops are judged first in the registered run.
3. Per-mode Krein agreement rests on an analysis of the records, not on the driver.
4. The fail-safe was added after the base run, which no guard affected.
5. C3's two N = 24 readings are unscored discrepancies.
6. The separation rule was chosen after these results, and is registered before the qualification.
7. Added: eigenvalue residuals and sensitivities are not in the shipped records, so the separation test above reads only the recorded changes and margins.

**Still open before the freeze (`DESIGN.md`):**
- the separation rule's tests, on the disclosed controls and on synthetic counterexamples, with mutations that force an incorrect classification and must leave it Unresolved (§10.2; UA);
- the synthetic demonstration of a genuine slow pair below 1.04×10⁻⁵, with its own arms (§7);
- §7's recalibration of the margin, the gray zone and the leak bound, with the margin scaling with amplitude if needed;
- the Newton acceptance bound, provisional until registration (§6);
- the frozen allowlist, in place of the freeze file's existence (§6);
- the gates, which freeze before any sealed control runs (§10.2).

Next: Blake's call on the next job. UA suggests the bounded pre-freeze synthetic checks, then the registration's review. No run.

## 114. 2026-10-16T23:10:46Z: the pre-freeze checks begin; §7's recalibration proposed

**Blake's decision (2026-10-16):** after D7's closure (entry 113), the pre-freeze checks come next. They go one at a time, starting with §7's recalibration of the margin, since the separation rule and the slow-pair demonstration both read it. Each is drafted, checked on small runs or the existing records, and sent to the units before the next.

**`RECAL_PLAN.md`, new: the proposal, for the units' review.** No code changes and nothing runs before the review.
- **The margin:** 2 √(u‖A‖ max(m, 0.2)), with m = ‖φ‖².
- **The gray zone:** (margin/3, 3 margins), with the off-axis threshold moved with it.
- **The leak bound:** 200 u‖A‖/gap, in place of the fixed 10⁻⁸.

**`dev/recal_survey.py`, new.** It is the plan's evidence: an analysis of the shipped records, not a run. It reads the 169 recorded control points (D6, D7's sample and D7's ladders), solves nothing and builds no operator.
- Script SHA-256 `aaf5c28e50d170a569523772ba9a9a45c291516db0a60de9b3b98c3da173b075`.
- Output `dev/recal_survey.out`, SHA-256 `09c2f696c89aa2318c4e791f65686e7436918b0f4731e039eb8932843672cfd0`.
- `RECAL_PLAN.md` SHA-256 `21d11e54674ee33ecdfc424c0845ed6f50f952127c58f1daa7cbdb0533de7a2a`.
- `DESIGN.md` is unchanged, at v2.11.

Next: the packet to the units. No run.

## 115. 2026-10-16T23:39:18Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/115_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 116. 2026-10-16T23:39:19Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `302a275167149bd16a20b3c3779cf181b01d1c046232b05e616551b89f1a0d7c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `9ca749aad975c61cfb677ebffa97ef72391d5288420eb13162b065a15d28e963`, kept as `dev/runs/116_dl_recal.out`

DL's recalibration claims: PASS, 7 claims and 5 arms (0 failed).
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 117. 2026-10-16T23:41:47Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `042c38670e6ce13e66f286fc3533eeecd1f374a20aa4f440f92ed30699f4bd44`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `fdac2e0749182b34e892026db1e815dadfac530bd7fbbf22a2032040261be68a`, kept as `dev/runs/117_dl_recal.out`

DL's recalibration claims: PASS, 7 claims and 5 arms (0 failed).
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 118. 2026-10-17T00:00:34Z: run `dev/d6_theoremD.py` (case: theoremD:R3)

Script SHA-256 `41d1211cd168b051f0eb002402d28fae7784fd54052fb8790a853742a8adf56b`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d6_theoremD_N16_24_32_40.out` `0f623fb8b2d1e1c75e040d1b2b7b6d6d4272c8e7d83ef2eb3e40949f5031bbff`, kept as `dev/runs/118_d6_theoremD_N16_24_32_40.out`
- output `dev/d6_theoremD_N16_24_32_40.json` `01fdd3df4a21516f466518dd10263bc34e15b93c64ba1c1bba0622dcd0ea666f`, kept as `dev/runs/118_d6_theoremD_N16_24_32_40.json`

D6, Theorem D at R3, N = [16, 24, 32, 40]: PASS, 4 claims at eps 0.5, 1 and 2.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row C1 {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (the acceptance bound 1e-15 for the residual; 1e-14 off level 2; 1e-10 for the lowest level against Theorem D; the record as in DL; 1e-12 along the ladder). The run informed none.

## 119. 2026-10-17T00:01:38Z: run `dev/d7_ladders.py` (case: C2a)

Script SHA-256 `1842274fa5e42b9a8fda0136ed6532c69144fa74d80926382b76fc2ff2655b5c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_ladders_C2a_trial.out` `10260d69dc1819bad392034b3555ae6d1dbcc4c8ade9a6458daa15237b6c213e`, kept as `dev/runs/119_d7_ladders_C2a_trial.out`
- output `dev/d7_ladders_C2a_trial.json` `a9c387c5974309165f59a8d368b79cc19004d24db5db1f4c83a3dd99d22c1a32`, kept as `dev/runs/119_d7_ladders_C2a_trial.json`

D7's ladders, C2a (trial): PASS; 0 failures of claims 1 and 3; 0 extra points held at the pause; branch identity unresolved at no point.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed). The run informed none.

## 120. 2026-10-17T00:02:54Z: run `dev/d7_controls.py` (case: C2a)

Script SHA-256 `1225ce236a48f595a01f8afa42f6cc4ec26bb2199be47348e861a2f5fdb987bf`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2a_N16_24.out` `c95805e2d21dd4311be31ecf87b08727173479facd23444eeeb1b21f1db0b63b`, kept as `dev/runs/120_d7_C2a_N16_24.out`
- output `dev/d7_C2a_N16_24.json` `ceb34534ff2091205d7cfcd9c9705bbd49ed8748fdc68a4d97944b3cf40278ab`, kept as `dev/runs/120_d7_C2a_N16_24.json`

D7, C2a, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 4, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as calibrated in RECAL_PLAN.md; slow eigenvalues as the record types them, below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 121. 2026-10-17T00:03:33Z: run `dev/d7_controls.py` (case: C2b)

Script SHA-256 `1225ce236a48f595a01f8afa42f6cc4ec26bb2199be47348e861a2f5fdb987bf`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C2b_N16_24.out` `eb3bfc7bd858c25c72ca472430f29005b74f5130ea14a5ff95ae320fb3e613a6`, kept as `dev/runs/121_d7_C2b_N16_24.out`
- output `dev/d7_C2b_N16_24.json` `753cf80b0a3200ba86fa8497283684719258343c8ced16f42deea6c9716a4d70`, kept as `dev/runs/121_d7_C2b_N16_24.json`

D7, C2b, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 6, 'ranks': [1, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as calibrated in RECAL_PLAN.md; slow eigenvalues as the record types them, below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 122. 2026-10-17T00:05:30Z: run `dev/d7_controls.py` (case: C3)

Script SHA-256 `1225ce236a48f595a01f8afa42f6cc4ec26bb2199be47348e861a2f5fdb987bf`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `d6112fa9a23bfa8df7e5a7b8e0f4466c3b582078d24c2ece66942ab48a1a4d7c`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/d7_C3_N16_24.out` `a596fb1dce035115313b14b27d3e6193e629db02d7b6ac2808b6d099e1b501e3`, kept as `dev/runs/122_d7_C3_N16_24.out`
- output `dev/d7_C3_N16_24.json` `4c203c0df953275d3cd36b3784433325cbc687eb1b731e2a9bd625e28e25c783`, kept as `dev/runs/122_d7_C3_N16_24.json`

D7, C3, N = [16, 24], eps = [0.5, 1.0, 2.0]: PASS.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before the run), row {'dim': 8, 'ranks': [4, 0]}.
Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target; acceptance 1e-15 relative, enforced; the record as calibrated in RECAL_PLAN.md; slow eigenvalues as the record types them, below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from these changes, disclosed.

## 123. 2026-10-17T00:07:14Z: §7's recalibration implemented; DL, the new claims and the regression pass

**The units' rulings on `RECAL_PLAN.md` v1 (2026-10-16).**
- **UA:**
  - CONFIRM the survey, and D7's closure with `DESIGN.md` v2.11;
  - a provisional GO to κ = 2, m₀ = 0.2, G = 3 and κ_L = 200, with final acceptance held until the revised classifier and its tests pass;
  - two corrections: the drivers read the production classifier, not their own ten-margin filters; and DL's original tests are preserved, with calibration-specific tests added, including a near-defective, opposite-Krein pair;
  - the leak arm must refuse an undefined gap, or a bound too large to discriminate;
  - GO to the implementation and the regression, subject to Blake's cost approval.
- **UB:**
  - KEEP the survey, and κ, m₀, G and κ_L for the zero cluster;
  - CHANGE: nonzero groups are linked and typed against max(margin, κ_d √(u‖A‖ |λ|)), with κ_d = 10. At UB's collision near 36i, 6 of 40 mixings read Hyperbolic under one margin;
  - the fourth arm made specific.
- **Blake approved the regression's cost,** about 30 minutes.

**Checked.**
- **UA's two code findings hold:** the three drivers' ten-margin filters, and DL's own 30-root margin.
- **UB's collision reproduces.** Under one margin for every role, 18 of 40 mixings read Hyperbolic with k_c = 1 and nothing flagged in a scratch run, and 5 of 40 in `dl_recal.py`'s arm. With the scale-aware tolerance, all 40 read Unresolved.

**The code.** `RECAL_PLAN.md` v2's implementation section has the detail:
- `instrument/linear.py`: the margin, the gray zone, the nonzero tolerance, the leak bound and its refusals, and each eigenvalue's label;
- the three drivers, which now read the record's own labels;
- `dl_linear.py`, pinned to the original calibration;
- `dl_recal.py`, new.

**The runs.**
- **DL's original claims** (entry 115): PASS. Their output is byte-identical to entry 93's.
- **`dl_recal.py`** (entries 116 and 117): the 7 claims pass, and the 5 arms turn red. Entry 117 adds the unscored report on DL's original constructions: of 31 readings, 3 change.
  - **Claim 7's quartet at real part 1.2e-5:** Unresolved becomes Hyperbolic. It is now resolved beyond τ, and the system is unstable.
  - **Claim 5's case 3, at t = ±0.5:** Elliptic becomes Unresolved. These 2 × 2 models have no eigenvalue outside the cluster, so the gap is undefined, and UA's guard refuses the leak check, though the models carry no symmetry directions.
  - **Flagged for the units:** the guard could apply only where symmetry directions are given.
- **The regression** (entries 118 to 122): D6 at N = 16 to 40, D7's trial, and D7's sample at N = 16 and 24 for C2a, C2b and C3. Every run passes.
  - **Unchanged:** the type, the indices, V₀'s dimension and ranks, and the unresolved items at all 39 points. The recorded values (Theorem D's levels, the slow eigenvalues) are identical at 39 of 39 points.
  - **The margins** are now 2.3e-7 to 1.7e-6, where they were 5.2e-6 to 1.8e-5.
  - **The cluster** sits at least 12 times below the gray zone, and the gap at least 765 times above it.
  - **The leak** is at most 9.6e-2 of its bound.

**A second limit, found while building the tests: L's inertia** (`dl_recal.py`'s claim 7; `RECAL_PLAN.md` v2).
- A genuine slow pair at s needs an L eigenvalue near 2ωs, and L's inertia gray zone reaches 10⁻⁷ ‖L‖. So it bounds the resolvable pair at about 6.0×10⁻⁶ to 1.2×10⁻⁵ at the controls' N = 40 (INFERRED), the size of the 1.04×10⁻⁵ requirement.
- §7 does not list it. My lean: take it into the slow-pair demonstration.

**`RECAL_PLAN.md` v2,** SHA-256 `f90fcc42fb4515c1add26efbf738b72509254ce33d929ecb70542d46bf281e87`. The constants stay provisional until the units review this (UA).

Next: the packet to the units. No run.

## 124. 2026-10-17T00:22:12Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `2f566ced2cf8d1bb10b4572dcf90690e52ba4f12711b7ffd2c90395a119911bd`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/124_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 125. 2026-10-17T00:22:15Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `4a60000bf5b6c2ae1009c91611cb844d4726587869a651055bd58e4e63441d76`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `2f566ced2cf8d1bb10b4572dcf90690e52ba4f12711b7ffd2c90395a119911bd`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `2b7a18e0ad2126ece3b7fe450aee4a33969a4eb22010ca9d0f9d6bf9cd6e99e4`, kept as `dev/runs/125_dl_recal.out`

DL's recalibration claims: FAIL, 9 claims and 6 arms (1 failed).
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 126. 2026-10-17T00:24:34Z: the units accept the recalibration; the explicit no-symmetry guard; claim 1′ fails on its headroom

**The units' rulings on the implementation (2026-10-17).**
- **UA:**
  - CONFIRM the implementation, the new DL claims and the regression;
  - accept κ = 2, m₀ = 0.2, G = 3, κ_d = 10, κ_L = 200 and the cap of 10⁻⁴ as the pre-freeze calibration baseline, to be recorded in `DESIGN.md` §7;
  - the synthetic m values are acceptable as disclosed test fixtures;
  - one change: the leak check is skipped only for a system explicitly declared free of symmetry directions. An empty tangent list on a branch must read Unresolved, with a mutation check;
  - the L-inertia limit is confirmed, and deferred to the slow-pair demonstration;
  - HOLD the qualification freeze until that demonstration passes review.
- **UB:**
  - KEEP the implementation;
  - a fix: `dl_recal.py` imported `dl_linear` through the working directory, which fails under python3 -I;
  - add claim 1′: claim 1 at m = 21 over 40 mixings, as derived, with the cluster at least ten times below the gray zone. UB's run gave 11.2 to 32 times;
  - the leak guard's scope, as I leaned;
  - L's cut written into the limits;
  - ACCEPT the constants as the development calibration, provisional until the slow-pair demonstration, with DESIGN §7 to carry them once (c) and claim 1′ are in.

**Checked.** Under python3 -I the script's directory is off the path, and a sibling import fails (a scratch check).

**The changes.**
- **`linear.py`:** `record()` takes `symmetry_free`. With leak_abs unset, an empty list not so declared is an unresolved item ("V0 cannot be checked: no symmetry directions were given, and none were declared absent"). The original calibration's path is unchanged.
- **`dl_recal.py`:**
  - the path fix;
  - claim 1′ (UB);
  - claim 8 (UA): missing tangents, with the empty list read as declared as its arm;
  - the change report now reads DL's constructions as DL ran them, declaring no symmetry where DL gave none.

**The runs, under python3 -I** (entries 124 and 125).
- **DL's original claims:** PASS, byte-identical to entry 93's output.
- **`dl_recal.py`:** FAIL, on one claim:
  - Claims 1 to 8 pass, except 1′, and all 6 arms turn red; under κ_d = 0, UB's collision reads Hyperbolic at 2 of 40.
  - The change report reads 1 of 31: only the quartet at real part 1.2×10⁻⁵, Unresolved to Hyperbolic. The two case-3 models read Elliptic again, under the declaration.
- **Claim 1′ fails on its headroom only.**
  - All 40 mixings classify as derived: V₀ 4 [2, 0], (4, 1, 3), k_r = 1, k_c = 1, Hyperbolic, nothing unresolved.
  - But the cluster sits 9.59 to 34 times below the gray zone, under ten at 2 mixings: 9.59, 9.94.
  - Across the 40 mixings, the synthetic cluster is 0.089 to 0.318 √(u‖A‖). At m = 21 that is up to 0.0695 √(u‖A‖ m), against the controls' largest coefficient, 0.0568.
  - So the worst mixing's chains are about 22 percent stiffer than the controls' worst, and ten-fold headroom there needs κ ≥ 2.08.
  - The result stands as run. It is not re-run with other mixings, and κ is not changed for it: the units rule.
- **`DESIGN.md` §7 is held** until the units rule on claim 1′, since UB conditioned its constants on it.

Script `dev/dl_recal.py` SHA-256 `4a60000bf5b6c2ae1009c91611cb844d4726587869a651055bd58e4e63441d76`; `instrument/linear.py` SHA-256 `2f566ced2cf8d1bb10b4572dcf90690e52ba4f12711b7ffd2c90395a119911bd`.

Next: the packet to the units. No run.

## 127. 2026-10-17T00:49:08Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `5887d60bcd4179224c021145c3f5bebe202529362c7ba718f6fd1d827262b3b1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `2f566ced2cf8d1bb10b4572dcf90690e52ba4f12711b7ffd2c90395a119911bd`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `82b08d754afb06944a5badec10da1ef0025f0a2e5149635c9a13a1cecb9800bb`, kept as `dev/runs/127_dl_recal.out`

DL's recalibration claims: PASS, 9 scored claims and 6 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 128. 2026-10-17T00:50:30Z: claim 1′ reconciled, κ = 2 kept; DESIGN.md v2.12 records the calibration

**The units' rulings on the v3 packet (2026-10-17).**
- **Both units choose (a):** κ = 2 stays, and both confirm the guard, claim 8, the path fix and the L-inertia text.
- **UA** asks that claim 1′'s FAIL (38 of 40) stay on record, with its expected answer unchanged and no rerun with selected mixings. It should say that the ten-fold clearance holds on the 169 control points, not throughout the synthetic family, and record the cross-environment variation: UA's rerun of the same 40 mixings read 10.4 at its lowest, and passed.
- **UB** finds the ten-fold bar a tail statistic. Over 20,000 mixings at m = 21, every one classifies as derived, the headroom is at least 7.3, and it falls under ten at 1.6 percent, so any 40 mixings miss with probability about 0.48. UB asks that claim 1′ drop the bar from its score, with the headroom reported.
- **UB also adds:**
  - all shipped D6 and D7 records carry a nonzero leak, so no control needs a rerun for the guard;
  - the collision arm is red at almost every mixing;
  - one sentence for §7.

**Checked, in a scratch analysis with a fresh seed (no bench run):**
- **At m = 21,** 5,000 mixings all classify as derived. The headroom has median 15.4, 1st percentile 9.10 and minimum 6.96, and falls under ten at 3.1 percent here: any 40 miss with probability about 0.72.
- **At m = 72,** 2,000 mixings never fall below 13.98.
- **The collision, over 500 mixings:** κ_d = 0 reads as derived at none, Hyperbolic at 69; κ_d = 10 reads as derived at all 500.
- **The leaks:** all 538 D6 and D7 records in `dev/` and `dev/runs/` carry a nonzero leak, the smallest 6.1e-14.
- So UB's finding holds, with a heavier tail on this machine.

**The reconciliation, mine, flagged to both units.** UA's instruction and UB's conflict on whether claim 1′'s expected answer may change.
- **Claim 1′ stays exactly as written,** ten-fold bar included. Its FAIL in entries 125 and 126 stands, and it is never converted. It now runs as a reported, unscored line, so its verdict shows at every run (FAIL at the archived seed).
- **A new claim 1″** scores the classification at every mixing, which is UB's content.
- **So UA's expected answer is unchanged, and UB's suite is not gated by a tail statistic.** UB asked for the bar to be dropped from 1′ itself; this keeps 1′ whole instead.

**The rerun** (entry 127, under python3 -I): 0 failed. 1″ passes at 40 of 40. 1′, reported and unscored, reads FAIL at 9.59 and 9.94, as in entry 125. All 6 arms turn red.

**`DESIGN.md` v2.12:**
- **§7 records the calibration:** κ = 2, m₀ = 0.2, G = 3, κ_d = 10, κ_L = 200 and the cap of 10⁻⁴, as the development baseline, accepted by both units and not yet qualified.
  - Its provenance and tested range, with the √m scaling labelled MOTIVATED.
  - The ten-fold headroom read on the controls, with claim 1′'s standing FAIL.
  - UB's sentence on what low headroom costs.
  - The nonzero tolerance, and the leak guard with the explicit declaration.
  - UB's L-inertia text, and UA's condition on the slow-pair demonstration and the freeze.
- **§8** lists DL's recalibration claims.
- SHA-256 `0cb4195dcf934eeb3cbffc5090f3fad49f42eb93b6c1212267f621743c66137d`.

**`RECAL_PLAN.md`** carries claims 1′ and 1″ as above. SHA-256 `8e423104c02ef79e96a5ebdc94906d395ccae0b873888ebd7c7decf8a5468e0d`.

**The recalibration item closes here,** with the calibration accepted for development, not qualified. Next: the slow-pair demonstration, the gate before the freeze (UA, UB).

## 129. 2026-10-17T00:57:20Z: run `dev/slowpair_scout.py` (case: synthetic)

Script SHA-256 `dd8daaad1c596f4ee2a8d35b16c65e021c3f993a720a16b58c83a2e241113090`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `2f566ced2cf8d1bb10b4572dcf90690e52ba4f12711b7ffd2c90395a119911bd`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/slowpair_scout.out` `0799c88e491bca95cb25cdb5a9dc4c34fb66fb04fff4ac383b70ced76f2cf744`, kept as `dev/runs/129_slowpair_scout.out`

The slow-pair scout: reported, unscored, under today's record; it informs SLOWPAIR_PLAN.md.
Lines with a wrong type: 0.

## 130. 2026-10-17T00:59:18Z: the slow-pair demonstration planned; the scout

**Blake's go (2026-10-17):** draft the slow-pair plan, the next pre-freeze item and the gate before the freeze.

**The scout** (entry 129, `dev/slowpair_scout.py`) is a synthetic, reported and unscored run that informs the plan.
- It places four slow-pair structures at N = 40's scale, under today's record.
- **The structures:**
  - S1, soft-soft, imaginary;
  - S2, near a crossing, imaginary, Krein-positive;
  - S3, near a crossing, imaginary, Krein-negative;
  - S4, near a crossing, real.
- No reading gives a wrong type.
- **Below 1.04×10⁻⁵, it resolves almost nothing:**
  - S1, at 5 of 20 readings, and only at ω = 14, s = 10⁻⁵. Elsewhere the pair's L eigenvalue, about 2ωs, sits in L's inertia gray zone;
  - S2, only by reading its L eigenvalue, about 4ω²s², as zero;
  - S3 and S4, at none: the index fails to balance, or V₀'s leak exceeds its bound.
- **Near a crossing the leak runs up to about six times its bound.** A nearby near-chain pair tilts V₀ by about 1/gap².

**`SLOWPAIR_PLAN.md`, new, for the units' review:**
- **Step 1** measures the controls' L kernel: D6 at N = 16 to 40, D7's ladders at N = 16 and 24, and D7's sample at N = 32. About 69 minutes, for Blake's cost decision after the review.
- **Step 2** recalibrates L's zero cut on it, by §7's ten-fold conditions applied to L.
- **Step 3** is the synthetic demonstration: S1 as the pass or fail gate, with S2 to S4 scored on their own floors, and three arms.
- **Five questions,** among them the gate's scope, and whether the leak bound near a crossing stays as calibrated.
- SHA-256 `78ab746602a91f0d689e6808eb878fcf68564e91715f4125328f6bed39ff258d`; the scout's script, `dd8daaad1c596f4ee2a8d35b16c65e021c3f993a720a16b58c83a2e241113090`.

Next: the packet to the units, with entry 128's reconciliation of claim 1′ flagged for both. No run.

## 131. 2026-10-17T01:16:33Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/131_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 132. 2026-10-17T01:16:36Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `f74250c2e885de77865c78c77dfdba25a8fff44967f907aeb62fd42cab5cc3c1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `19f3e0f8ec78bb2b81261df93fd8347d48dfac6304f9a42a6362c61b221f5c0f`, kept as `dev/runs/132_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 7 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 133. 2026-10-17T01:16:37Z: run `dev/slowpair_scout.py` (case: synthetic)

Script SHA-256 `dd8daaad1c596f4ee2a8d35b16c65e021c3f993a720a16b58c83a2e241113090`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/slowpair_scout.out` `8a8f1f88d800fe449d206a7581a8913c0022001f295c428003c3a91a07367b70`, kept as `dev/runs/133_slowpair_scout.out`

The slow-pair scout: reported, unscored, under today's record; it informs SLOWPAIR_PLAN.md.
Lines with a wrong type: 0.

## 134. 2026-10-17T01:18:11Z: the units review the slow-pair plan; the zero-count check; DESIGN.md v2.13

**The units' rulings (2026-10-17).**
- **Both units** CONFIRM the claim 1′ reconciliation, `DESIGN.md` v2.12 and the scout's diagnosis. Both give Step 1 a GO, subject to Blake's approval of its cost. They keep the leak bound as calibrated.
- **UA:**
  - keep S1 as the gate, and add an unequal-stiffness soft-soft check, characterized and not gating;
  - read a pass as minimum capability, not proof about the sealed in-span mode;
  - in Step 1, measure L t for every declared kernel tangent, comparing D4's identity only where its symmetry hypothesis holds;
  - if Step 2's two conditions cannot both hold, Step 2 fails;
  - Step 2's constants and Step 3's run wait for the units to see Step 1's measurements.
- **UB:**
  - widen the gate to the soft-soft pair's three sign patterns, S1+, S1− and S1r at the controls' measured r;
  - add ρ, the controls' slow-pair structure, to Step 1, and state Step 2's target through ρ_min;
  - put L's zero-count check in the record, with an arm;
  - name the leak's cause as σ_min(T₂₂), the smallest singular value of the Schur form's outside block.
  - UB's scratch readings, cited as UB's and to be confirmed by Step 1: C2a and C2b slow pairs isotropic (ρ = 1.000); C3's real pairs at r = 1.65, ρ = 0.78; L's kernel at 4×10⁻¹⁶ to 7×10⁻¹⁶ ‖L‖ at N = 16, ε = 0.5.

**Checked (a scratch analysis, synthetic only).** σ_min(T₂₂) equals the gap for S1 to three digits, and falls like s² near a crossing. The leak tracks u‖A‖/σ_min(T₂₂) at 0.008 to 0.10 on all four structures. UB's controls readings are not rerun here; Step 1 measures them, logged.

**The reconciliation, mine.** The gate takes UB's three sign patterns. UA's unequal-stiffness check enters the gate only at the controls' measured r, and r = 10 and 100 are characterized, not gating. UA's reading of a pass, as minimum capability, is written into the plan. Flagged to both units.

**The zero-count check.**
- `record()` reports n(L) unresolved where L's zero count differs from V₀'s chains. `zero_count` is off under `ORIGINAL`, so DL is unchanged.
- `dl_recal.py`'s claim 9 places a near-crossing pair at s = 10⁻⁵ and ω = 14, its L eigenvalue near 4.6×10⁻¹¹ ‖L‖, read as zero. The item appears at every mixing, and the reading is never a clean Elliptic. With the check dropped, 10 of 10 mixings read clean Elliptic: the arm turns red.

**The reruns, under python3 -I -B.**
- **DL** (entry 131): byte-identical to entry 93's.
- **`dl_recal.py`** (entry 132): 0 failed, every arm red, and the change report still 1 of 31.
- **The scout** (entry 133): S1 5 of 20; S2 0 of 20; S3 0 of 20; S4 0 of 20. S2's clean readings were μ read as zero, and are now caught.

**`SLOWPAIR_PLAN.md`** folds both rulings, with the units' rulings recorded at its end. SHA-256 `9bbe82aeb5188d9717cf40eb68a6b91978a7ce46fad971125a8c84eb974e77e4`.

**`DESIGN.md` v2.13:** §7 adds the zero-count rule, and §8 adds claim 9 and its arm. SHA-256 `9df39102fd0e102712ea1091988712329ac01253a3e2923c3def2d2eaf211080`.

`instrument/linear.py` SHA-256 `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`; `dev/dl_recal.py` `f74250c2e885de77865c78c77dfdba25a8fff44967f907aeb62fd42cab5cc3c1`.

Next: Blake's cost decision on Step 1, about 70 minutes. No run.

## 135. 2026-10-17T01:27:02Z: Blake approves Step 1; the L-kernel measurement, `dev/lkernel.py`

**Blake's decision (2026-10-17):** Step 1 at its full scope, about 70 minutes (`SLOWPAIR_PLAN.md`).

**`dev/lkernel.py`, new.** Usage: `lkernel.py CONTROL`. It is measured and not scored, and changes nothing in the record. Its numbers feed Step 2's proposal, which the units review first.
- **Where:**
  - C1 at N = 16 to 40, ε ∈ {0.5, 1, 2}, exact;
  - C2a, C2b and C3 at N = 16 and 24 along M8.15's full ladders from the germ, and at N = 32, ε ∈ {0.5, 1, 2}.
- **What, at each point:**
  - L's spectrum by |μ|, with the kernel taken as the chain count from `EXPECTED_V0.md`: its lift, the smallest genuine |μ|, and L's zero count under today's cut against the chains (UB's check);
  - ‖L t‖ for every declared kernel tangent (UA): the generators, the phase, R2's J c and i J c, and C1's five rigid-family directions;
  - the Newton floor;
  - at D7's points, s_min, ρ, and each slow group's L restricted to its position span, with r and √|k_min k_max|/(2ωs).
- **D4's identity is used only where D4 established it:** the generators, the phase, and R2's J.
  - At a solution both sides sit near round-off, so their relative difference is noise. A first draft compared them that way, and a dry check showed it; nothing was run or logged with it.
  - ‖T F′(c)‖ is reported instead, as the lift's predictor, beside the measured ‖L T c‖ and u.
- **A dry check** on single points at N = 16, unlogged:
  - C1's kernel at 6.3×10⁻¹⁶ ‖L‖;
  - C2a's and C2b's slow pairs isotropic, with r = 1.00 and ρ = 1.000, as UB read;
  - the generators' ‖L T c‖ near round-off, against D4's ‖T F′(c)‖ about 2×10⁻¹⁷.
- **Script SHA-256** `43540dee07538a0e4fcce265b21e0bead341d111a9c7e8bda3b5c1e1c2d6d331`.

The four runs follow as their own entries, as a sidebar task under `caffeinate`.

## 136. 2026-10-17T01:41:02Z: run `dev/lkernel.py` (case: theoremD:R3)

Script SHA-256 `43540dee07538a0e4fcce265b21e0bead341d111a9c7e8bda3b5c1e1c2d6d331`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/lkernel_C1.out` `01405dc6f592d085ab37d2ee068edcec638eaf3be554ccc9d97147180a99d536`, kept as `dev/runs/136_lkernel_C1.out`
- output `dev/lkernel_C1.json` `17c70bc469c039facb5c3fa289b1e2188b130f576ecbb78f6eca664ac2cd2058`, kept as `dev/runs/136_lkernel_C1.json`

Step 1, C1: 12 points measured; largest kernel lift 6.9e-16 ||L||, smallest genuine 6.0e-04 ||L||; zero-count mismatches 0; 0 ladders ended early. Measured, not scored.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran).

## 137. 2026-10-17T02:08:03Z: run `dev/lkernel.py` (case: C2a)

Script SHA-256 `43540dee07538a0e4fcce265b21e0bead341d111a9c7e8bda3b5c1e1c2d6d331`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/lkernel_C2a.out` `2227f65b0816f199cd9cb1e890a9e81254417ab1e3246160bcf8c928279e1fe0`, kept as `dev/runs/137_lkernel_C2a.out`
- output `dev/lkernel_C2a.json` `302a55482e49210ea6234915caa7637d0a264119fbdd17a74d2e4a8f9a051957`, kept as `dev/runs/137_lkernel_C2a.json`

Step 1, C2a: 39 points measured; largest kernel lift 1.2e-15 ||L||, smallest genuine 1.4e-05 ||L||; zero-count mismatches 0; 0 ladders ended early. Measured, not scored.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran).

## 138. 2026-10-17T02:20:39Z: run `dev/lkernel.py` (case: C2b)

Script SHA-256 `43540dee07538a0e4fcce265b21e0bead341d111a9c7e8bda3b5c1e1c2d6d331`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/lkernel_C2b.out` `f61af49c4547b39b8f51b171ef36b00ec689ea713ba4e9af4b07ba2eba134c59`, kept as `dev/runs/138_lkernel_C2b.out`
- output `dev/lkernel_C2b.json` `8b58173e5e8f88a9af70f68cb757499581f2dccdbad32afa4315abdc5f8f9ed2`, kept as `dev/runs/138_lkernel_C2b.json`

Step 1, C2b: 43 points measured; largest kernel lift 1.1e-15 ||L||, smallest genuine 9.5e-05 ||L||; zero-count mismatches 0; 0 ladders ended early. Measured, not scored.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran).

## 139. 2026-10-17T02:56:28Z: run `dev/lkernel.py` (case: C3)

Script SHA-256 `43540dee07538a0e4fcce265b21e0bead341d111a9c7e8bda3b5c1e1c2d6d331`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `27a0482e51ca09c677526de15649d4c2d3ca72b2fe08985e924441ffa3fa21b8`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/lkernel_C3.out` `c70a813f6a8c115cac66fcb6b4ee4cf250ddb45b62071127187bd870c50836c4`, kept as `dev/runs/139_lkernel_C3.out`
- output `dev/lkernel_C3.json` `e37ccd1bf6d06793c77ecc3979bfc37743683317d4d0335642a856954ba993d5`, kept as `dev/runs/139_lkernel_C3.json`

Step 1, C3: 39 points measured; largest kernel lift 1.3e-15 ||L||, smallest genuine 4.6e-05 ||L||; zero-count mismatches 0; 0 ladders ended early. Measured, not scored.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1 (as logged before any control ran).

## 140. 2026-10-17T02:58:53Z: Step 1's results; Step 2's proposal, for the units

**Step 1** (entries 136 to 139, `dev/lkernel.py`): 133 points, about 90 minutes, every control's runs complete.
- **L's kernel sits at round-off:** at most 6.2 u (1.4×10⁻¹⁵ ‖L‖), with no growth with N.
- **It is not driven by the Newton floor:** D4's ‖T F′(c)‖ is at most 1.9×10⁻¹⁶.
- **L's zero count equals the chains** at every point.
- **The smallest genuine |μ|** is 1.4×10⁻⁵ ‖L‖ (C2a, N = 24, ε = 0.25).
- **ρ runs from 0.777 to 1.009,** and r reaches 1.66 (C3). The soft-soft relation √|k_min k_max| = 2ωs holds to within 5 percent over 407 slow groups.
- **These confirm UB's scratch readings:** the isotropic C2a and C2b, C3's r of 1.65 and ρ of 0.78, and the round-off kernel.

**Step 2's proposal, in `SLOWPAIR_PLAN.md`'s new last section** (not adopted, and no code changed):
- **L's cut at 100 u ‖L‖, with the gray zone up to 10 times it.** That keeps the kernel at least 16 times below the cut, and the smallest genuine eigenvalue 6e+07 times above the gray zone.
- **It meets the S1 gate's target, 6.5×10⁻⁸ ‖L‖, about 3e+05 times over.**
- **A cut too tight fails safe,** through the zero-count check.
- `SLOWPAIR_PLAN.md` SHA-256 `098552d01cf527685ad863af23296a7090b63973ccb3b001a6bd073b37a695f1`.

Next: the packet to the units. Step 3 is held until they settle Step 2's constants (UA). No run.

## 141. 2026-10-17T12:46:51Z: a provenance note on entry 140's plan hash (UA)

Entry 140 logged `SLOWPAIR_PLAN.md` at SHA-256 `098552d01cf527685ad863af23296a7090b63973ccb3b001a6bd073b37a695f1`. That was the plan before two number formats in its new last section were fixed: "6e+07 times" became "6×10⁷ times", and "3e+05 times" became "3×10⁵ times". No figure or word changed.

The final revision of that entry's plan, as shipped in `m8_16_slowpair_review_v2.zip`, is SHA-256 `16da512f5e9a1d8e4daa69ee9c7698cca290b25a17c04b587b0df8a2d6ddaa3c`. UA found the mismatch, and this note reconciles it; entry 140 stands as written.

From here, a document's hash is logged after its last edit in the step.

## 142. 2026-10-17T12:50:31Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `937dc4d7f334f805aaf1f4b825f1297d322fac4a52dc81e8960445afc8072d55`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/142_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 143. 2026-10-17T12:50:34Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `937dc4d7f334f805aaf1f4b825f1297d322fac4a52dc81e8960445afc8072d55`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/143_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 144. 2026-10-17T13:05:53Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `24677120435ebf474c33f100637524a04b8c5e08ebf03bfa1a6fcfc9755a6c03`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/144_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 145. 2026-10-17T13:05:56Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `24677120435ebf474c33f100637524a04b8c5e08ebf03bfa1a6fcfc9755a6c03`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/145_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 146. 2026-10-17T13:06:07Z: run `dev/slowpair_demo.py` (case: synthetic)

Script SHA-256 `eac11ec5ea2c958e5262b4c6edbb70cab73d129379b3e100a1e18eff8f645a46`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `24677120435ebf474c33f100637524a04b8c5e08ebf03bfa1a6fcfc9755a6c03`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/slowpair_demo.out` `89203b0f8249f6ca182bccac27ce8d28630c7506602839ef32202e31c506ef07`, kept as `dev/runs/146_slowpair_demo.out`
- output `dev/slowpair_demo.json` `830a43e39e6890b23fc56b31c0100ef6f7ce32916e7dfef9936c619a60aeabe6`, kept as `dev/runs/146_slowpair_demo.json`

Step 3, the slow-pair demonstration under Step 2's cut: the gate PASS; every other row as derived PASS (84 of 84); 0 wrong types; the claims behind arms (b) to (d) PASS; arms red 4 of 4; 0 failed.
Each outcome derived before the run (SLOWPAIR_PLAN.md, Step 3; the derivation printed first).

## 147. 2026-10-17T13:13:27Z: the units' rulings on Step 1 and Step 2; L's cut at 1000 u; the cheap checks; Step 3 passes; `DESIGN.md` v2.14

**The units' rulings (2026-10-17), on entry 140's packet.**
- **Both units** CONFIRM Step 1, recomputed from its four JSONs, and the widened gate. No regression reruns, and no new expensive control work.
- **UA:** GO for Step 2 at 100 u ‖L‖ with G_L = 10, and a conditional GO for Step 3, once the cheap checks establish the cut's implementation; a wording qualification on Step 1; a provenance note on entry 140's plan hash (entry 141). If Step 3 passes, UA recommends closing this pre-freeze gate and moving to the M8.16 registration draft and freeze review.
- **UB:** the cut at 1000 u ‖L‖, which gives the kernel's side, the one that varies by machine, 162 times headroom instead of 16; claims 7 and 9 re-derived before `dl_recal.py` reruns, since both fail under either proposed cut; replacement text for the plan.

**The adjudication, mine.** UB's 1000 u is adopted. Both cuts meet Step 2's two conditions, and UB's argument rests on Step 1's data alone. Flagged to UA.

**Implemented.**
- `instrument/linear.py`: `L_CUT` = 1000 u and `G_L` = 10, the record's defaults for L's inertia, with L's own gray-zone factor, `l_gray`. `ORIGINAL` keeps 10⁻¹⁰ and 10³, so DL runs unchanged. A's gray zone and D's cut are untouched.
- `dev/dl_recal.py`:
  - claim 7 re-derived: its pairs at 3×10⁻⁵ and 10⁻⁴, at ω = 1.3 and m = 8, each read Elliptic (1, 1, 0) with nothing unresolved. Its new arm is the earlier cut, where the first reads n(L) Unresolved, as it did in entries 116 to 132;
  - claim 9 rebuilt as UB wrote it: K = 1000 at ω = 14, s = 3×10⁻⁶, k₁ at 42.5 u ‖L‖, with the leak bound held vacuous;
  - 10 scored claims and 8 arms.

**The cheap checks.**
- **Entries 142 and 143:** DL byte-identical to entry 93's; `dl_recal.py` 0 failed, every arm red.
  - The change report moved from 1 to 3 of 31, both new changes counts inside readings that stay Unresolved. A scratch check read the same constructions under both cuts. Claim 6(a)'s L eigenvalue, −1.24×10⁻¹² ‖L‖, read as zero before, now lies in L's gray zone: n(L) 4 → 5. Claim 10's, −8.82×10⁻¹¹ ‖L‖, is now read as negative: n(L) 1 → 2, with its zero count now equal to V₀'s chains. Claim 6(b)'s, 1.0×10⁻⁸ ‖L‖, leaves the earlier gray zone, so its n(L) item clears, with its type and counts unchanged.
  - The claim-5 arm's report moved from 3 to 4 of 40 Hyperbolic mixings. A scratch replay, with the new earlier-cut call's draws taken out of the random stream, gives 3 of 40 again: the mixings changed, not the record.
- **One fix after them.** `linear.py`'s comment on the cut credited 1000 u to both units; it now reads "(UB; UA approved 100 u)". Comment only. A stray `instrument/__pycache__` from 2026-10-16, before the runs took `-B`, was removed.
- **Entries 144 and 145** reran both on the final file, with outputs identical to entries 93 and 143.

**Step 3 (entry 146): PASS.** `dev/slowpair_demo.py`, synthetic: 96 rows of 10 mixings in about 5 seconds, every outcome derived before the run and printed first. An unlogged smoke test on off-grid rows (s = 2×10⁻⁴, seed 1) checked the reading code first; no grid row was read before the logged run.
- **The gate:** 12 of 12 rows resolved at every mixing (S1+, S1− and S1r at r = 1.66; s = 10⁻⁵ and 5×10⁻⁶; m = 0.2; ω = 7 and 14).
- **Every other row as derived,** 84 of 84, with no wrong type in 960 readings.
- **Near a crossing V₀'s leak sets the floor:** every mixing resolves from 3×10⁻⁵ (S4 at ω = 7: 9 of 10 there), and fewer below. σ_min(T₂₂) follows 2ωs² at K = 1 to 0.8 percent (a fit, INFERRED); for S1r it is the gap over √r, and for S1± the gap.
- **The claims behind arms (b) to (d) pass, and all four arms are red.**
- What a pass shows, and where the run fixes what the plan left open, are in the plan's last section.

**Documents.**
- `SLOWPAIR_PLAN.md`: a status line; "today" in the planning sections now reads "before Step 2"; UA's wording qualification and UB's replacement text, folded; the fourth arm's construction noted; two new sections, the units' rulings and Step 3's results. SHA-256 `bb5ca435a32d10a07c970abc75a6d2d0290c8ebc1247ba5b591e48383c61692c`.
- `DESIGN.md` v2.14: §7 gives L's cut and the gate's result; §8 updates claims 7 and 9 and their arms, and adds the slow-pair demonstration. SHA-256 `571563247e1c0d33bc9b77c04cc8a298f5b7fd1a45bdb888c1c6b1c1cf4be10c`.
- `RECAL_PLAN.md`: a dated note at its end, flagged. Its text, closed at entry 128, gives the earlier cut in the present tense, and stands. SHA-256 `342d4f60ef15417a2fb7ca9717d4bd2c17fe7184f893e1f52f6969008fd4a54f`.
- `instrument/linear.py` `24677120435ebf474c33f100637524a04b8c5e08ebf03bfa1a6fcfc9755a6c03`; `dev/dl_recal.py` `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; `dev/slowpair_demo.py` `eac11ec5ea2c958e5262b4c6edbb70cab73d129379b3e100a1e18eff8f645a46`.

Next: the packet to the units, with the 1000 u adjudication flagged to UA. No run.

## 148. 2026-10-17T13:30:27Z: the units confirm Step 3; the slow-pair gate is closed; `DESIGN.md` v2.15

**The units' rulings (2026-10-17), on entry 147's packet.** Both CONFIRM, and the slow-pair gate is closed.
- **UA:** accepts 1000 u over its own 100 u, as an empirical calibration, not a universal error bound. It reproduced the 12 gate rows independently, and the archive's hashes match entry 146. It accepts the fourth arm on claim 9's construction. Not established: that the sealed pyramid's in-span slow mode resolves; the qualification tests that, without adjusting the accepted instrument or criteria. No further development controls or costly runs on account of this gate. GO to draft and review the M8.16 qualification registration, within #512's admission boundary and the normal freeze review; it is filed before any scored run, and does not authorize the census preregistration.
- **UB:** KEEP on every item. Its reruns of DL, `dl_recal.py` and Step 3 match, the gate's rows mixing for mixing. With L's cut at 100 u, Step 3's verdicts are unchanged. The near-crossing counts vary by machine: at 3×10⁻⁵ and ω = 7, S2 at 9 and S4 at 10 of 10 there, against 10 and 9 here. One addition to §7 (FIXABLE): S1r at r = 10 and 100 resolves wherever A's gray zone clears, on both machines.

**Checked.**
- UB's 100 u rerun reproduces here, in scratch and unlogged: the gate 12 of 12, 84 of 84 rows as derived, no wrong type, every arm red.
- UB's §7 sentence matches entry 146: S1r at r = 10 and 100 resolves at all 10 mixings in all 16 rows outside A's gray zone, σ_min(T₂₂) is the gap over √r to 0.25 percent, and the leak is at most 7.4×10⁻³ of its bound.

**Folded.**
- `DESIGN.md` v2.15: §7 reads L's cut as an empirical calibration (UA), records the gate's closure, and takes UB's sentence verbatim; §8 records the closure. SHA-256 `d4f9c2c6e026aa206bdb9b60cf6464ff4c8eb9408f0fae829ecb9f965bd1b1e0`.
- `SLOWPAIR_PLAN.md`: the status line, closed, and a last section with the units' rulings on Step 3. SHA-256 `2470d3a348cc6240e5d83f90e12a184c0ae374bfe548fc3c1010728bf7015784`.

**The slow-pair gate is closed.** §7's requirement is met for slow pairs of the controls' structure at N = 40's scale, as minimum demonstrated capability, not as proof that the sealed in-span mode resolves (UA, UB).

**Still open before the freeze** (entry 113's list, with §7's recalibration and the slow-pair demonstration now closed):
- the separation rule's tests, on the disclosed controls and on synthetic counterexamples, with mutations that force an incorrect classification and must leave it Unresolved (§10.2; UA). Neither unit's ruling on this packet addresses it;
- the Newton acceptance bound, provisional until registration (§6);
- the frozen allowlist, in place of the freeze file's existence (§6);
- the gates, which freeze before any sealed control runs (§10.2).

Next: Blake's call on the next job: the separation rule's tests, or the registration draft (UA's GO). No run.

## 149. 2026-10-17T13:49:48Z: run `dev/sep_scout.py` (case: synthetic)

Script SHA-256 `b35d1e5cd6a2ac8dbd0382bdf2b72fb435426bef9c378825e261eded8ac88928`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `24677120435ebf474c33f100637524a04b8c5e08ebf03bfa1a6fcfc9755a6c03`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_scout.out` `c2a03fdb345a6f3c9c1346fb97a4b239a47cdd136b323ae0ee4166616fec438e`, kept as `dev/runs/149_sep_scout.out`

The separation scout: reported, unscored; it informs SEPARATION_PLAN.md. The rule is not implemented here; its expected verdicts are derived from exact roots.

## 150. 2026-10-17T13:52:54Z: the separation rule's tests planned; the survey and the scout

**Blake's decision (2026-10-17):** the separation rule's tests (§10.2) come before the registration draft. They are the last test of the instrument still open on entry 113's pre-freeze list (entry 148).

**No code applied the rule before.** D7's closure read it as an analysis (entry 113). `SEPARATION_PLAN.md` makes it an algorithm, with four choices flagged for the units, and designs its tests.

**`dev/sep_survey.py`, new: an analysis of records, not a run.** It reads D7's sample and ladders, 65 points, at §7's calibration, and solves nothing.
- Every point is separated. The smallest ratio is 1.21×10³ (C2a, ε = 0.25), where the floor binds; the change binds at 8 mid-ladder points, the smallest 1.4×10³ (C3, ε = 32).
- No three-cutoff sequence is non-contracting, and C2a's and C2b's records carry no Krein-negative imaginary group.
- Script SHA-256 `3552a452db2b7d29533b9d67c649d64801ea63695f3b66a42ca070b5af932e15`; output `dev/sep_survey.out` `9c757196d8ba665c4fb258119f93cc6035ad257c7ef4705c98cd51abcde89225`.

**`dev/sep_scout.py` (entry 149): synthetic, reported and unscored.**
- Eight ladders in N, N = 16 to 40, each with one parameter converging and its limit: three converged controls, P, P′ and PK, and five counterexamples, Z, K, X, R and F.
- Each counterexample reads at all four cutoffs, at all 3 mixings, a type its limit does not have. The rule's expected verdicts are derived from exact roots: the controls separated at 1.3×10³ to 1.8×10³; the counterexamples at ratios 0.38 to 2, so not separated.
- An unlogged dry run of the same script came first, to check its code. The logged output is byte-identical to it.

**Scratch checks, unlogged.**
- An ill-conditioned congruence of the Elliptic family (condition 10² to 10⁵) did not make the numerical-estimate term bind. The record read Unresolved first, through its own Krein, V₀ and margin checks. So that term's arm is proposed as wiring only.
- A geometric step in the collision's δ makes the eigenvalues accelerate into the collision, so the sequence does not contract. Family R steps the separation geometrically instead.

**`SEPARATION_PLAN.md`, new, for the units' review.** No instrument code changes, and nothing scored runs before the review. SHA-256 `fde50a6721278e5f0631c15a3a3ea12ec6b6d8a6bd262b22a40b6b6b9f844a54`.
- **The four choices:** the tested groups; non-contracting sequences above the floor; the numerical estimate, through A's Hamiltonian pairing; the controls' run (D7's sample at N = 16 and 24, about 4 minutes, or with N = 32, about 35).
- **Step 2, after the review:** `instrument/convergence.py`, with each arm as a parameter, and `dev/sep_claims.py`, with the eight families over 10 mixings and seven arms.

Next: the packet to the units. No run.

## 151. 2026-10-17T14:23:41Z: the units review the separation plan; Step 2 built, its outcomes derived before the run

**The units' rulings (2026-10-17), on entry 150's packet.** Both CONFIRM the survey and the scout; UA reran both byte-identical.
- **UA:** a conditional GO to Step 2: one-to-one matching; a non-contracting counterexample with its arm; the projector validated, with an analytic test. Its control run: D7's sample at N = 16, 24 and 32. The factor stays a tenth, an operational adequacy test.
- **UB:** KEEP, with three changes: the opposite-sign partner tested too, with a family K′; arm (g) red at the module; the rule's rate assumption stated, with F at 15 margins reported. Its control run: the sample and the ladders at N = 16 and 24, read at the tops.
- **Checked here.** UB's rate figure holds at the ladders' tops, at most 0.0331 over 39 three-cutoff sequences. The sample's N = 24 to 40 changes sit at round-off. UB's count of 64 is not reproduced; the folded sentence carries the count checked here, flagged to UB.

**Blake's decision (2026-10-17):** both control runs, about an hour, after the synthetic claims pass. Flagged to both units.

**Built.**
- `instrument/convergence.py`, new: the rule with its nine arms, UA's matching, UB's partner, and the projector with UA's checks. SHA-256 `8892efcc12bb1798fcb756467cf62cda4e627276e9a6e9da64bf8a484bd941a0`.
- `instrument/linear.py`: the record also returns its eigenvectors and groups; no reading depends on them. SHA-256 `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`.
- `dev/sep_claims.py`, new: the scored synthetic claims, with every outcome derived from exact roots and printed before any record is read. SHA-256 `edac45dedac34e780bc4d297c631561d5946b44931e15fcdb8efc9d9e80d2f07`.
- `dev/sep_controls.py`, new: the control run. Its sample claim, derived from D7's records at the same three cutoffs, puts the slow band's ratio at 1.7×10³ or more (C2a, ε = 0.5, where the floor binds). SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`.
- `SEPARATION_PLAN.md`: UB's three texts folded in place, and two new sections, the units' rulings and Step 2 as built. SHA-256 `b4bdea74eaf0eb3e3a513335af42459385c3942cb50037be60cbc093006c8e97`.

**Unlogged checks before any scored run, on cases the scored runs do not read.**
- The analytic projector at k = 9 and under diag(1, 3): to 12 digits.
- A near-collision at δ = 10⁻¹⁴: Yᴴ X's conditioning read 1.0000003 there and would not flag the defective group, so the span test was added, the record's own 10⁻⁶ criterion. It then read not usable.
- Off-grid P, K and K′-like ladders through the rule. K′ at steps of 4 put its partner's lowest match within a factor 2 of the oscillator at 0.0357, which the rule refused as ambiguous. The scored K′ steps by 3; its exact numbers were rechecked.
- One C2a point at N = 16, ε = 0.75: all 98 typed groups' projectors usable, ‖P_g‖ from 1.0 to 7.1, and the numerical estimate five decades under the margin.

Next: DL and `dl_recal.py` rerun on the changed record, then `dev/sep_claims.py`; if it passes, the control runs as background tasks.

## 152. 2026-10-17T14:23:49Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `8892efcc12bb1798fcb756467cf62cda4e627276e9a6e9da64bf8a484bd941a0`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/152_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 153. 2026-10-17T14:23:52Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `8892efcc12bb1798fcb756467cf62cda4e627276e9a6e9da64bf8a484bd941a0`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/153_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 154. 2026-10-17T14:23:57Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `edac45dedac34e780bc4d297c631561d5946b44931e15fcdb8efc9d9e80d2f07`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `8892efcc12bb1798fcb756467cf62cda4e627276e9a6e9da64bf8a484bd941a0`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `3c5fe29eb5b7a080f26c287df56ccd254fbee8433e88f3a2bad2ed0f9bf957ef`, kept as `dev/runs/154_sep_claims.out`

The separation rule's claims: FAIL (1 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 155. 2026-10-17T14:26:11Z: entry 154's claims FAIL on arm (c); the arm corrected, the rule unchanged

**Entry 154: FAIL, 1 item.** Every claim held as derived except arm (c):
- the analytic projector, with the defective group not usable;
- P, P′ and PK converged at 10 of 10;
- Z, K, X, R, F, N and K′ Unresolved at 10 of 10;
- arms (a), (b) and (d) to (i) red.

Under arm (c), no floor, F read Unresolved at 10 of 10, not converged. That FAIL stands.

**The cause: the arm, not the rule.** The floor does two jobs in the rule:
- it is the smallest uncertainty;
- it is the threshold below which a non-contracting sequence is round-off (choice 2).

As coded, the arm set both to zero; the derivation took away only the first. With the threshold at zero, the unchanged groups' round-off changes read non-contracting about half the time. So F read Unresolved through its base oscillators, not through its slow pair. An unlogged check with another seed showed the same for the converged control P: under the arm as run, Unresolved at 5 of 5, with 10 of its 18 groups non-contracting at round-off.

**The finding.** The non-contraction rule needs its noise threshold: without it, every point reads Unresolved. That bears out choice 2's "above the floor" (UA, UB).

**The correction, bounded and documented.**
- `no_floor` now drops the floor from U only, with the margin kept as the non-contraction threshold, as the derivation took it.
- `dev/sep_claims.py`'s exact arithmetic and docstring now say the same.
- The rule itself is unchanged: with no arm, the threshold and the floor are the same margin as before.

**Also seen in entry 154:** the numerical estimate reached 5.6×10⁻⁷, as large as the floor, on K's near-collision pairs, whose ‖P_g‖ is 1.4×10⁶ at a separation of 10⁻³. It does not bind there, since a tenth of their distance is 10⁻⁴. On the control point checked in entry 151, it sat five decades under the margin.

`instrument/convergence.py` SHA-256 `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`; `dev/sep_claims.py` `b9d38ad39cb6e49a55cbf959df4841bbf499dbb7b3cfb47ba3fb83cac99ab474`.

Next: DL and `dl_recal.py` rerun on the changed instrument, then `dev/sep_claims.py`.

## 156. 2026-10-17T14:26:14Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/156_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 157. 2026-10-17T14:26:17Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/157_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 158. 2026-10-17T14:26:22Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `b9d38ad39cb6e49a55cbf959df4841bbf499dbb7b3cfb47ba3fb83cac99ab474`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `9e2eecf1fd513ca0ebbb3a6b953ae398e30f4c7412cd439a3208f04bb0ce43e7`, kept as `dev/runs/158_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 159. 2026-10-17T14:45:06Z: run `dev/sep_controls.py` (case: C2a)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2a_sample.out` `1cc46658f96f035837acfd0d591923ba5d98bb52511d5baecbca1e9534cfe290`, kept as `dev/runs/159_sep_controls_C2a_sample.out`
- output `dev/sep_controls_C2a_sample.json` `c14d394cdd134430c6b9ff797159c2b45576727e810525006053109239773c38`, kept as `dev/runs/159_sep_controls_C2a_sample.json`

The separation rule on C2a (sample): FAIL (1 failed); 2 of 3 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 4, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 160. 2026-10-17T14:53:02Z: run `dev/sep_controls.py` (case: C2b)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2b_sample.out` `d420e31badea52bb3454dbdfd1d3546b95150a82255ef740d6ddb33699010568`, kept as `dev/runs/160_sep_controls_C2b_sample.out`
- output `dev/sep_controls_C2b_sample.json` `d3a26a78fcc5462db13865d406d82206fd31c6bb193649eadd5e1ef3680a9c97`, kept as `dev/runs/160_sep_controls_C2b_sample.json`

The separation rule on C2b (sample): PASS (0 failed); 3 of 3 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 6, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 161. 2026-10-17T15:16:49Z: run `dev/sep_controls.py` (case: C3)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C3_sample.out` `91dcf5a8ba6d27a112b8a80d5b774f6adff51fac855ac5a340a5d8e6fd675a7b`, kept as `dev/runs/161_sep_controls_C3_sample.out`
- output `dev/sep_controls_C3_sample.json` `5795afe041e07e45633220ee7a2776c2af48d20cbbab826e4450d1a5a275870f`, kept as `dev/runs/161_sep_controls_C3_sample.json`

The separation rule on C3 (sample): PASS (0 failed); 3 of 3 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 8, 'ranks': [4, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 162. 2026-10-17T15:26:26Z: run `dev/sep_controls.py` (case: C2a)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2a_ladders.out` `1470ccf5b7ca9cd95a5cd61ff5950a4dffc97b3e7a77fd5650ee09503d3527c3`, kept as `dev/runs/162_sep_controls_C2a_ladders.out`
- output `dev/sep_controls_C2a_ladders.json` `0988190dd50a2ed5e495b8049350fbd6cc0aa5fda8d50d343a886204ea09481d`, kept as `dev/runs/162_sep_controls_C2a_ladders.json`

The separation rule on C2a (ladders): PASS (0 failed); 6 of 18 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 4, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 163. 2026-10-17T15:31:22Z: run `dev/sep_controls.py` (case: C2b)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2b_ladders.out` `4fb2dbdfb023239ae68989fe7d0835efe383564f9977bdfcacc7acacaa203696`, kept as `dev/runs/163_sep_controls_C2b_ladders.out`
- output `dev/sep_controls_C2b_ladders.json` `d2f3abfb6e022291d903602b47f1165deb52e4644ffa23ea1509ce0b7d1efb76`, kept as `dev/runs/163_sep_controls_C2b_ladders.json`

The separation rule on C2b (ladders): PASS (0 failed); 10 of 20 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 6, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 164. 2026-10-17T15:44:57Z: run `dev/sep_controls.py` (case: C3)

Script SHA-256 `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C3_ladders.out` `95ae8d54c1d58b2bfd322ea1df27656880d9f64c29847a3901e06506647b016c`, kept as `dev/runs/164_sep_controls_C3_ladders.out`
- output `dev/sep_controls_C3_ladders.json` `14f61fd4df89b77c5c9574b2448e2fe796fe4cda53f8172f9a30b8d9451e2ce1`, kept as `dev/runs/164_sep_controls_C3_ladders.json`

The separation rule on C3 (ladders): PASS (0 failed); 15 of 18 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 8, 'ranks': [4, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 165. 2026-10-17T15:47:52Z: the separation rule's controls: C2a's sample FAILS on matching; the claims pass; a matching proposal for the units

**The synthetic claims (entry 158): PASS,** after entry 154's FAIL on arm (c) and its correction (entry 155). The controls converge, the seven counterexamples read Unresolved, and all nine arms are red, each at 10 of 10.

**The control runs (entries 159 to 164), Blake's scope, about 78 minutes on battery.**
- **The sample** (N = 16, 24 and 32): C2b and C3 PASS, converged at 3 of 3. **C2a FAILS, at 2 of 3:**
  - at ε = 2, two tested Krein-positive groups near 4.039, 2.4×10⁻⁴ apart, have no unique, bidirectional match at the lower cutoffs, so the point reads Unresolved;
  - the slow band clears there at 3.3×10³;
  - the claim's derivation read only the slow band, from D7's records. The FAIL stands.
- **The ladders** (N = 16 and 24, to the tops): the claim, no point converged with a wrong type, PASS for all three. Reported: converged at 6 of 18 (C2a), 10 of 20 (C2b) and 15 of 18 (C3).
  - Matching makes C2a Unresolved from ε = 2 and C2b from ε = 8, among Krein-positive groups.
  - At the tops, the change between N = 16 and 24 gives separation ratios of 5 to 10. D7's records give about 3×10⁴ from 24, 32 and 40.
  - The tested group nearest zero at each top was read and reported. Which group, if any, is the next level's mode is not identified.
- **The numerical estimate on the controls:** 1.1×10⁻¹³ to 1.2×10⁻¹² over 65 readings, five or more decades under the floor.

**The finding.** One-to-one matching (UA) reads a converged control Unresolved wherever groups of one class and one Krein sign sit closer than their change across N, though such groups cannot change the type among themselves.

**For the units, not implemented:** match an ambiguous set of one class and one sign as a whole, by its count, testing its extent against its events. Ambiguity across class or sign, a missing partner, or a changed count stays Unresolved.

**Documents.** `SEPARATION_PLAN.md` gains its results section, SHA-256 `936b8d6b95de6e64a1ed323ea1c8135fa8423734d8360ac68f8c91fffc7bd277`. The code is as hashed in the run entries: `instrument/convergence.py` `4b9241be49055a05b0cc603f3dca6c1ac9f0674c43e5dc9c5c624b628aaeed4a`; `dev/sep_controls.py` `079ac7ce7a3db86c03306a4ad0dd541afe7b6a694c32e58eed74e26c0df10bed`.

Next: the packet to the units, with the matching proposal and the C2a FAIL. The separation gate stays open; nothing more runs before their ruling.

## 166. 2026-10-17T16:15:55Z: the units adopt the set rule; built, with M, M′ and arm (j), its outcomes derived before the run

**The units' rulings (2026-10-17), on entry 165's packet.** Both CONFIRM Step 2, entry 154's FAIL and its correction, and the control runs as reported. C2a's FAIL stands as the strictness of the rule as built. Both reran `sep_claims.py`: 0 failed.
- **UA:** GO to a bounded set matcher with four properties:
  - the complete set, its multiplicity preserved;
  - a conservative bottleneck displacement;
  - the nearest member's distance to each event;
  - the numerical estimate required, Unresolved where it cannot be assessed.

  Tests: a harmless permutation and a dangerous approach. Rerun C2a's sample only. Then close the gate and draft the registration.
- **UB:** adopt the proposal, with its definition (Hausdorff change, nearest member's distance, partner rule), family M and M′, and arm (j); rerun the sample and ladders, saving summaries; and a wording fix in `projector()`. UB's 64 sequences reconcile as 39 at the tops plus 25 in the sample above the records' noise.

**The merge, mine, flagged to UB:** the change is UA's bottleneck, never smaller than UB's Hausdorff distance, so UB's 1-Lipschitz argument holds, and it keeps multiplicity.

**Blake's decision:** the targeted rerun, about 33 minutes: C2a's sample and the C2a and C2b ladders. These are every reading that failed on unique matching, and so every reading the set rule can change. Flagged to both units.

**Built.**
- `instrument/convergence.py`: `ambiguous_set()`, `bottleneck()`, the set path in `separation()`, the arm `set_centroid`, `row_centre()`, and UB's wording. With no ambiguous match, every path is the one entry 158 ran. SHA-256 `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`.
- `dev/sep_claims.py`: families M and M′, arm (j), and their exact derivation, with the bottleneck written out rather than called. SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`.
- `dev/sep_controls.py`: saves each point's summary and the basis's levels, and states the rerun's derivations, among them C2a's ε = 2: one set, converged if its uncertainty is under 0.40. SHA-256 `420f353304cb873ff5291c8f6ddd3e6fb63588d29ae500ad16295ef0259001e2`.
- `SEPARATION_PLAN.md`: UB's wording fix, and a section with the units' rulings, the merged set rule, the new tests, the rerun and what the registration keeps. SHA-256 `cd927a454c3e1f9e3f5fdf8bc282de83755ff7744966ed5c8e0c11e021a267d1`.

**An unlogged check, off the scored grid:** M at centre 0.25 and M′ with other steps both form their sets. M converged; M′ was Unresolved in full and converged under arm (j). Each S1+ block's fast pair, at exactly 2ω + f, forms a mirror set with the same steps, now stated in the docstring.

Next: DL and `dl_recal.py` on the changed instrument, then `dev/sep_claims.py`; if it passes, the targeted control rerun as a background task.

## 167. 2026-10-17T16:15:58Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/167_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 168. 2026-10-17T16:16:01Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/168_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 169. 2026-10-17T16:16:08Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/169_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 170. 2026-10-17T16:34:40Z: run `dev/sep_controls.py` (case: C2a)

Script SHA-256 `420f353304cb873ff5291c8f6ddd3e6fb63588d29ae500ad16295ef0259001e2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2a_sample.out` `ef4919a84de5ed97f62a6388516ad312b9d4f84180e3b8117cc9897f38ec766a`, kept as `dev/runs/170_sep_controls_C2a_sample.out`
- output `dev/sep_controls_C2a_sample.json` `8a1031c7d4a86369e8c53666014d29cb5e445bc30e5ba39f9e871366c20f6bdb`, kept as `dev/runs/170_sep_controls_C2a_sample.json`

The separation rule on C2a (sample): PASS (0 failed); 3 of 3 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 4, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 171. 2026-10-17T16:44:29Z: run `dev/sep_controls.py` (case: C2a)

Script SHA-256 `420f353304cb873ff5291c8f6ddd3e6fb63588d29ae500ad16295ef0259001e2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2a_ladders.out` `3216df76e06919ac03525265d48662288cf004e624c3da07602f8ac103731c42`, kept as `dev/runs/171_sep_controls_C2a_ladders.out`
- output `dev/sep_controls_C2a_ladders.json` `b555798831a10d3ea78d76018c6e2e13d40d84db4752101c5c650a70ca2d0660`, kept as `dev/runs/171_sep_controls_C2a_ladders.json`

The separation rule on C2a (ladders): PASS (0 failed); 12 of 18 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 4, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 172. 2026-10-17T16:49:32Z: run `dev/sep_controls.py` (case: C2b)

Script SHA-256 `420f353304cb873ff5291c8f6ddd3e6fb63588d29ae500ad16295ef0259001e2`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `d129cd73cdb3cddf58557f58c784041c6932cf488cafd6ad0a42ccec449cbee5`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_controls_C2b_ladders.out` `8069a3a7c2c16ef435a8948df1876b375b794a2350fe9bef48644773e282e18d`, kept as `dev/runs/172_sep_controls_C2b_ladders.out`
- output `dev/sep_controls_C2b_ladders.json` `7d018ae77cbb2868b45f0522ee8934f74f1603c05a74a9502636f8ff3f537a6a`, kept as `dev/runs/172_sep_controls_C2b_ladders.json`

The separation rule on C2b (ladders): PASS (0 failed); 14 of 20 eps converged.
EXPECTED_V0.md SHA-256 7fceba14d248dc967d8480da1b425e3f53b8f8f3d35a8a351b60fdeb33aac5c1, row {'dim': 6, 'ranks': [1, 0]}. Each outcome derived before the run (the script's docstring; SEPARATION_PLAN.md).

## 173. 2026-10-17T16:50:53Z: the set rule passes; C2a's sample converges; the gate's conditions met, for the units' review; `DESIGN.md` v2.16

**The checks on the changed instrument.** DL is byte-identical to entry 93's (entry 167), and `dl_recal.py`'s output identical to entry 145's (168).

**The synthetic claims (entry 169): PASS, 0 failed.**
- P, P′, PK and M converged at 10 of 10. M's set has U = 10⁻³ against 0.149.
- Z, K, X, R, F, N, K′ and M′ Unresolved at 10 of 10.
- All ten arms red, each at 10 of 10: the nine original and (j).

**The targeted control rerun (entries 170 to 172), about 33 minutes on battery.**
- **C2a's sample: PASS, 3 of 3.** At ε = 2 the two Krein-positive groups near 4.039 form one set, whose change falls from 1.6×10⁻⁴ to 1.7×10⁻¹⁰ across the cutoffs: the floor binds, at a ratio of 3×10⁶ against the gray zone, as derived. Entry 159's FAIL stays on record.
- **The ladders keep no wrong type** (PASS for both). C2a converges at 12 of 18 points and C2b at 14 of 20, against 6 and 10 before.
- **What still reads Unresolved:** sets whose count differs between N = 16 and 24, which both units required to read so, and separation at the tops at those coarse cutoffs.
- The summaries are saved (UB).

**The gate's conditions (UA, UB) are met:**
- the set rule passes M, M′ and arm (j);
- the nine original arms stay red;
- C2a's sample no longer reads Unresolved for same-sign exchange;
- the ladders keep no wrong type.

The gate closes on the units' review (UA).

**Documents.**
- `SEPARATION_PLAN.md`: the set rule's results. SHA-256 `db1dfddb746d5a5012bd54de983c99d3e08b0e7dc04190df4f373a58b220a04c`.
- `DESIGN.md` v2.16: §10.2 gives the rule as built, its tests, and its stated limits for the registration (UA, UB). SHA-256 `f9fa4a9afcb79e52bb1050f2addf66198832496573d99cc87959e7bae523b665`.

Next: the packet to the units. On their CONFIRM the separation gate closes, and the M8.16 registration draft follows (UA's GO). No run.

## 174. 2026-10-17T19:04:51Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/174_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 175. 2026-10-17T19:04:53Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/175_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 176. 2026-10-17T19:04:57Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/176_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 177. 2026-10-17T19:04:57Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `4799e08a29002d5fdddb6c25216c9fcb12df6612fa33d5ba4517bf9d4f44186e`, kept as `dev/runs/177_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 21 of 21 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 178. 2026-10-17T19:04:57Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `4be672105ba95f9287e23618f7dd390ec6f9c79286f58e46bfe43519edd11860`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `7ee8d1982459729b079ccf330140dd83bb5a86023fff2da1b0243db5224632f3`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `ad77c4c35ba61f76b518b1fc5ddc0b5c60ac8369f156550f8c18b2be478d25c3`, kept as `dev/runs/178_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 179. 2026-10-17T19:05:17Z: UB's wording on when a set forms, folded; the checks rerun; the saved verdicts re-read; `DESIGN.md` v2.17

**UB's change (FIXABLE), from its review of entry 173's packet.** The text said a set forms when a match fails "only on uniqueness". The code forms one whenever a group's one-to-one match fails and it has candidates of its own class and Krein sign, so also on a change of size or a failed reverse match. UB judged that safe, since counts are taken with multiplicity and the bottleneck bounds every member's motion. The text now says what the code does, because the registration will quote it.

**Folded, wording only:**
- `DESIGN.md` §10.2's "Matched" bullet, UB's text verbatim. The clause after it is reworded to agree in number ("the set matches when that count agrees at every cutoff; its change is the bottleneck distance; its distance to an event is its nearest member's"), with no change of content.
- `instrument/convergence.py`: item 3 of the module docstring, as UB asked, and `ambiguous_set()`'s docstring, which said the same. No code changed.
- `SEPARATION_PLAN.md`: the set rule's "When" bullet. The v2 proposal's text stays, as proposed.

**The checks, since an instrument file's hash changed:**
- DL byte-identical to entry 93's (entry 174).
- `dl_recal.py`'s output identical to entry 145's (175).
- `sep_claims.py`'s output byte-identical to entry 169's (176).

**The saved verdicts re-read** (`dev/sep_reread.py`, new; entries 177 and 178). The rule, at the current hashes, is applied to the summaries the set-rule runs saved, with no solve: C2a 21 of 21 and C2b 20 of 20 verdicts as shipped, 41 in all, as UB's re-read found. So entries 170 to 172 stand under the instrument as it now is.

**Hashes, after the last edits:**
- `DESIGN.md` v2.17 `52f92292ca6ff8cfdcc28083a26ffb13b95e293f10546d080dc1dc071ac06edc`;
- `SEPARATION_PLAN.md` `1f5d54885047d58a557d5bffd288c24564f1b36553dc106b24030475738512c3`;
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`;
- `dev/sep_reread.py` `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`.

Next, on Blake's go: record the units' closure of the separation gate (both CONFIRM on entry 173's packet), mark the plan closed, and turn to the registration draft.

## 180. 2026-10-17T19:09:58Z: the units close the separation gate; `DESIGN.md` v2.18; the plan closed

**The units' rulings (2026-10-17), on entry 173's packet: both CONFIRM, and the separation gate is closed.**
- **UA** reran `sep_claims.py`, byte-identical, with 0 failed, and checked the bottleneck matcher against an exhaustive search over assignments in small cases. It confirms the set rule's four properties, M, M′, all ten arms, C2a's sample and the ladders' safety, and `DESIGN.md` v2.16.
- **UB** re-read all 41 control verdicts from the saved summaries, each as shipped, and finds the targeted scope complete. Its one wording change is folded (entry 179).
- **On record:** entry 159's FAIL, entry 154's FAIL on arm (c), the five 10⁻⁶ diagnostic failures of D7's ladders (§10.2), and the remaining upper-window Unresolved readings.

**UA's disposition.**
- GO to draft the M8.16 qualification registration. Every sealed case HOLDs until it is reviewed, frozen and filed. No pyramid, census target or scored qualification run is authorized, and the #512 admission restriction is unchanged.
- The registration review settles the Newton acceptance bound and the frozen allowlist (§6), as documentation and enforcement, not a new development campaign. The gates freeze before any sealed control runs (§10.2).
- The registration keeps the separation rule's limits explicit:
  - a slow rate hidden under a faster one can defeat a few-cutoff estimate (F at 15 margins; R from two cutoffs);
  - the rule rests on the leading rate dominating at the highest cutoffs, and the controls' rates there are at most 0.033;
  - the upper-window runs did not identify every next-level mode near zero. The qualification's coverage and Unresolved rules must not omit a required mode, and every group below half the band edge is tested.

**Documents.**
- `DESIGN.md` v2.18: §10.2 records the closure. SHA-256 `45cf624d3b474b6af33f27e92bea342a5230b1ad505ba741006a05a93943d632`.
- `SEPARATION_PLAN.md`: a closed status line, its opening put in the past tense, and a last section with the units' rulings. SHA-256 `77a6229c2538885e089eac29e598663efef48cfde19df10b28d1e4b3b327d3d0`.

**Instrument development is closed with this gate.** Of entry 113's pre-freeze list, the recalibration (entry 128), the slow-pair demonstration (entry 148) and the separation rule (here) are closed. The Newton acceptance bound, the frozen allowlist and the gates' freeze belong to the registration.

Next: the M8.16 registration draft, on Blake's go. No run.

## 181. 2026-10-17T20:07:28Z: the registration draft v2, the units' first review folded

**v1** (`registration/m8_16_task_details.md`, 7,610 words, built by `registration/fill_terms.py` from `m8_16_task_details.src.md`) went to UA and UB without a hash logged here.

**The reviews.** UA: CONDITIONAL GO, two corrections before filing, no further expensive development. UB: two frozen items to change, everything else KEEP; every generated value, commit and count reproduced on fresh clones.

**Each finding, verified at source:**
- **UA 1, the band edge vanishing at the window tops.** Not so as built: `n₁` is the first level above the lowest truncation cutoff `N = 16` at which the slot occurs (17 in `R2`, 18 in `R4`, 18 in `R5`, from 2I's characters, independent of the instrument and matching the levels the saved runs carry), not the slot's next level above `λ₀`. The band edge at the highest read points is 8.02 (`R4`, ε = 72), 10.03 (`R5`, ε = 32) and 5.58 (`R2`, ε = 90.51), equal to the saved control ladders' values where they exist. Folded: the definition stated precisely, the floor stated, and UA's guard added to the driver's specification (Unresolved if half the band edge lies within the gray zone), with an arm before the freeze.
- **UA 2, C1's kernel.** Folded: the `k + r_u` formula scoped to the soft-slot cases; C1's values are Theorem D's, as D6 registered them.
- **UA's generator note.** Folded: `fill_terms.py` states that the built text, not the script, is the artifact, never rebuilt after the freeze, and prints its provenance.
- **UB 1, K3(c).** Verified: M8.15.x's `verdict.static_overlap` and its continuum survey both read the projection-norm ratio, not principal cosines. Folded, with the definition. Found while verifying it: the draft's basis lacked the `√(n+1)` factor that `instrument/basis.py` carries; restored, with the basis's `L²`-orthonormality stated.
- **UB 2, T5's variable.** Verified: `ν = s²`, both roots negative. Folded, with `τ ≈ 2.6886` and `3.0802` computed by the script.

**v2:** 7893 words; the cost estimate unchanged, about 18.2 h.
- `registration/m8_16_task_details.src.md` `918301a6df6b4f2e6fc70e85d1f01e45e5a8548377f2f524697091d07b7fbdef`
- `registration/m8_16_task_details.md` `b53db95a84c90867a2677e4b461c7afc9c5e6758f842c29951bad002cc0bbc60`
- `registration/fill_terms.py` `76096cfe2a5d9da6ab8151a8c9f34a8b3f456c661614a1cef1dfcede998fb60e`

**The build's provenance:** commits CEN `787aef1`, HKI `61e548a`, M815T `4b1177c8`, QX `ae3ad04`, REC `28c8a76`, SA `341d789`, SA9 `d0de8ca`, SGS `ae05295`, SSB `b182702`; the run files read:
- `dev/runs/103_d7_ladders_C2b.json` `0119130f1d214e80fdff9e98a6f677fa9199a6e1fdfc476e893408a4dd5a2559`
- `dev/runs/104_d7_ladders_C2a.json` `aa2a1d9113840abbf0258c36d676f204a7186edeaaa3aabb85efcd58aea14c98`
- `dev/runs/105_d7_ladders_C3.json` `a345bc094dba35c609063e97bb8e3fb611e52b9b245305ddbfad614731417997`
- `dev/runs/118_d6_theoremD_N16_24_32_40.out` `0f623fb8b2d1e1c75e040d1b2b7b6d6d4272c8e7d83ef2eb3e40949f5031bbff`
- `dev/runs/160_sep_controls_C2b_sample.json` `d3a26a78fcc5462db13865d406d82206fd31c6bb193649eadd5e1ef3680a9c97`
- `dev/runs/161_sep_controls_C3_sample.json` `5795afe041e07e45633220ee7a2776c2af48d20cbbab826e4450d1a5a275870f`
- `dev/runs/164_sep_controls_C3_ladders.json` `14f61fd4df89b77c5c9574b2448e2fe796fe4cda53f8172f9a30b8d9451e2ce1`
- `dev/runs/170_sep_controls_C2a_sample.json` `8a1031c7d4a86369e8c53666014d29cb5e445bc30e5ba39f9e871366c20f6bdb`
- `dev/runs/171_sep_controls_C2a_ladders.json` `b555798831a10d3ea78d76018c6e2e13d40d84db4752101c5c650a70ca2d0660`
- `dev/runs/172_sep_controls_C2b_ladders.json` `7d018ae77cbb2868b45f0522ee8934f74f1603c05a74a9502636f8ff3f537a6a`

**Open, Blake's:** a check of each sealed seed at the lowest level only (`Q`, criticality, `(k, r_u)`; no solve, no spectrum), and `R5`'s coherent branch as a GO-list development control. Neither unit has seen them.

Next: Blake's decisions, then the pre-freeze build (the convention test and seed comparison, the registered driver with its guards and arms, `R5`'s manufactured timing), then the units' final review of the frozen terms. No run.

## 182. 2026-10-17T20:10:47Z: BOUNDARY.md's amendment 2, the sealed seeds' lowest-level check

Blake's decision (2026-10-17), on the open item of entry 181: amend for a check of each sealed seed on the lowest level only before the freeze, `Q(u)`, criticality and `(k, r_u)`, with no solve and no spectrum. Recorded as BOUNDARY.md's amendment 2, SHA-256 `7053718f108c2d33232cc9938d63e86c89d1de380de619309b71b9386ac5c13b`.

The check runs in the pre-freeze build, as its own logged run. The terms take it in with Blake's next decision, `R5`'s coherent branch as a development control, in one rebuild. No run.

## 183. 2026-10-17T20:12:26Z: BOUNDARY.md's amendment 3, `R5`'s coherent branch as a development control

Blake's decision (2026-10-17): `R5`'s coherent branch joins the GO list for development only, its sample at `ε ∈ {0.25, 0.5, 1, 2}` and `N = 16, 24` and 32, before the freeze; not a registered control. Recorded as BOUNDARY.md's amendment 3, SHA-256 `e948a9ed03b249c1cd96783d9d1205830aefa1c9571f82ac9c5a5751f83f756a`.

Its run replaces the terms' `R5` cost scaling and the manufactured `R5` timing that v2 listed. The terms take in amendments 2 and 3 in one rebuild. No run.

## 184. 2026-10-17T20:14:50Z: the registration draft v3, BOUNDARY.md's amendments 2 and 3 taken in

**What changed from v2 (entry 181):**
- the split paragraph names both amendments (Blake's one paragraph, kept one paragraph);
- the preamble is tense-neutral: no sealed case is solved before the freeze;
- BEFORE THE FREEZE: the sealed seeds' lowest-level check, and `R5`'s coherent sample, which replaces v2's manufactured `R5` timing and the cost scaling before the go;
- the freeze block carries each seed's `Q(u)`, criticality and `(k, r_u)`; the stated limit reads one `R5` development branch;
- tightened without change of meaning, for the word budget: the development list, the solve, continuation and seeds, the linear record, the representatives' coordinates, K4's C1 item and the instrument's environment.

**v3:** 7832 words; the cost table unchanged until the `R5` sample runs.
- `registration/m8_16_task_details.src.md` `1f707b36a194851aaad5c9eafc7f448a4fd4f815ea17be85d8ceac7a51b30c18`
- `registration/m8_16_task_details.md` `44446fe2a9521d8e58e1a09b30fbbb1a656c0f62e8026d8bfaa888b8be4acb4f`
- `registration/fill_terms.py` `76096cfe2a5d9da6ab8151a8c9f34a8b3f456c661614a1cef1dfcede998fb60e`
- `BOUNDARY.md` `e948a9ed03b249c1cd96783d9d1205830aefa1c9571f82ac9c5a5751f83f756a`

The build's commits: CEN `787aef1`, HKI `61e548a`, M815T `4b1177c8`, QX `ae3ad04`, REC `28c8a76`, SA `341d789`, SA9 `d0de8ca`, SGS `ae05295`, SSB `b182702`; the run files as in entry 181, unchanged.

Next, on Blake's go: the pre-freeze build, one step at a time. No run.

## 185. 2026-10-17T20:21:58Z: the units on v3 and step 1; BOUNDARY.md's note to amendments 2 and 3

**UA:** CONFIRM v3's amendments; GO to step 1 only. Step 1 stays algebraic and pre-solve at every sealed case; a failed seed is recorded before the implementation is corrected, and no frozen expectation changes to fit the code. The seed-check results and any discrepancies return before step 2.

**UB:** GO on step 1, with two conditions, both folded into BOUNDARY.md's note (SHA-256 `1f134d620d17114ba28bb58282275d8362180d702cd4883ac1de6f9d3f741a70`): amendment 2's scope written in (no Newton step; no Hessian, slow matrix, `L` or `A` formed at any sealed seed; a failure corrected in the constructor and disclosed); and amendment 3's expected values derived and logged before its run, with no refit on it unless a calibration condition fails. UB recomputed the band-edge floor (5.58, `R2`, ε = 90.51) and `R5`'s coherent `Q = 2289/2288` from `Q₅ = (9Q₄ + 7)/16`, and confirmed both DESIGN.md fixes. The terms take the note's wording in their next version, with step 1's outcome.

**For the final review (Blake's decision then):** UB recommends adding `R5`'s coherent branch to K4 as a registered conformance control. It would change what can stop the run, so it is not folded now.

Next: step 1, under the note. No run in this entry.

## 186. 2026-10-17T20:28:45Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `7112e348c28faffd5ef7ce14b74d70bc384a7c5edcef13034d707bb4f9e31b01`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `69a5790833b722499f7c68b11eca096b4b05f51130b50b60ec8ea4c19ace6d07`, kept as `dev/runs/186_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 187. 2026-10-17T20:29:05Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/187_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 188. 2026-10-17T20:29:07Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/188_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 189. 2026-10-17T20:29:11Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/189_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 190. 2026-10-17T20:29:22Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `4799e08a29002d5fdddb6c25216c9fcb12df6612fa33d5ba4517bf9d4f44186e`, kept as `dev/runs/190_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 21 of 21 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 191. 2026-10-17T20:29:23Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `d43575d75f75aad623cf88b29010ec6f862ad606c38cfa79b530deb0f9756320`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `d2248dfd3345eee7834e4738accb86a7edd45785497133655d2760dfc51ed9b5`
- `instrument/functional.py` `757f0641b7a78809c88128b12cc9daa7a7d68b835ea470791cf9aefb10638cdd`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `298b1f8042a4f1232390f0d6a7c16df231498c0d9e038ea86cd058ff7d698806`
- `instrument/newton.py` `f41d1d7f298497b2f789e1c933f487073557b15d9aa2f21917fc42077dbb7dd3`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `ad77c4c35ba61f76b518b1fc5ddc0b5c60ac8369f156550f8c18b2be478d25c3`, kept as `dev/runs/191_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 192. 2026-10-17T20:29:53Z: step 1 passes; the regression unchanged; DESIGN.md v2.19; EXPECTED_R5.md logged

**Step 1 (entry 186): PASS, 0 failed.**
- 1. The basis convention: `e_l` is the Condon–Shortley `|n/2, (n − 2l)/2⟩` with no phase, exactly, on `n ≤ 32` and on the `N = 16` bases' blocks in `R2`, `R3`, `R4` and `R5`.
- 2. The certified point: `instrument/certified.py`'s 14 strings, its source's SHA-256 and its `924 r̂₆` equal the Result's, at the commits it records.
- 3. The constructors as data: every seed's vector as its representative's components; `seed_state` refused all 10 sealed seeds.
- 4. All 15 seeds: `Q(u)` within 3.2e-15 relative of its exact value (bound 1e-12); criticality at most 1.1e-15; every `(k, r_u)` as § IV's, C1's (4, 2) as D6 reported. The R4 rule `Q = 1 + 924 r̂₆/1287` reproduced the six published R4 values, and the R5 rule `(9Q₄ + 7)/16` the four published R5 values.
- 5. No sentinel fired: no Newton step, and no Hessian, slow matrix, `L` or `A`, at any seed.

No seed failed, so no constructor was corrected.

**The regression (entries 187 to 191).** DL, `dl_recal`, the separation claims and both re-reads are byte-identical to entries 174 to 178, under the new instrument hashes (`branches.py`, `devtools.py`, and `certified.py`, new). The re-reads were first invoked with the script and its argument passed as one filename (zsh): Python could not open the file, exited 2, and nothing ran or was logged.

**Documents.**
- `DESIGN.md` v2.19: § 3's basis with `√(n+1)` and `L²`-orthonormality; § 7's `u` as machine epsilon; § 6's guard and § 8's sealed line under amendments 2 and 3. SHA-256 `56e554bc5edf323a222ad2ef5cfa73b49fcf140fb1528e7493be3780d997d35e`.
- `EXPECTED_R5.md`, `R5`'s coherent control's expected values, logged here before it runs (BOUNDARY.md's note, UB). SHA-256 `f0915cd18a36436be4b6b7b18780cc70fd0798fe029e6bbca3fdfd970f6835cb`.

Next: the seed-check results to the units before step 2, as UA asked. No further run.

## 193. 2026-10-17T20:42:13Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `10fbd6b9c0cc46705a955b93c560602205d140d7cd3f9895bf1088af2fb89925`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `e452a4571d816f7ef0c762691f058bd1262cc26239fdafb56e27f263162ba715`, kept as `dev/runs/193_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 194. 2026-10-17T20:42:24Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/194_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 195. 2026-10-17T20:42:26Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/195_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 196. 2026-10-17T20:42:30Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/196_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 197. 2026-10-17T20:42:30Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `4799e08a29002d5fdddb6c25216c9fcb12df6612fa33d5ba4517bf9d4f44186e`, kept as `dev/runs/197_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 21 of 21 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 198. 2026-10-17T20:42:31Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `ad77c4c35ba61f76b518b1fc5ddc0b5c60ac8369f156550f8c18b2be478d25c3`, kept as `dev/runs/198_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 199. 2026-10-17T20:43:12Z: the units confirm step 1; UB's guard built into the instrument; DESIGN.md v2.20

**The units on step 1 (entries 179 to 192).** Both CONFIRM, and both GO on step 2, `R5`'s coherent sample.
- UA reran the algebraic checks on its own machine: all 15 seeds pass, `Q` within 8.9×10⁻¹⁵.
- UB reran `seed_check.py` against its own MIT clone (0 failed, no sentinel fired) and rebuilt the terms v3 byte-identically from its own clones.
- UA: a calibration condition that fails in `R5` is preserved and returned before any adjustment; no refit to make `R5` agree.
- Held for the final review: whether `R5`'s coherent branch becomes a scored K4 control (Blake).

**UB's change, built before step 2.** `sealed_seed_for_check` built a sealed seed in any run, and amendment 2's scope was enforced only by the check's own sentinels. Now the instrument enforces it:
- `devtools.require('seedcheck')` marks the process (`devtools.SEEDCHECK`);
- `branches.sealed_seed_for_check` refuses outside a marked process;
- inside one, every solver path refuses: `newton.solve`, `Functional.grad`, `hess_apply`, `hess_parts` and `hess_dense`, `linear.first_order` and `linear.record`, and `branches.continue_to`.

UB allowed it after step 2; it lands first, so step 2 runs on the guarded instrument and exercises the guarded solver paths on a real branch.

**The checks.**
- `seed_check.py` gains claim 6 (UB), with its arm. Entry 193: PASS, 0 failed. Outside seedcheck (a subprocess under case C2a), the sealed seeds are refused, 10 of 10, while `first_order` runs and no guard refusal fires (the arm). In the seedcheck process all 8 paths refuse. Claims 1 to 5 are as in entry 186.
- The regression (entries 194 to 198): DL, `dl_recal`, the separation claims and both re-reads are byte-identical to entries 187 to 191.

**`DESIGN.md` v2.20:** § 6's guard states the enforcement. SHA-256 `3c3df9af43a5ab8d1a6ac58cbe7c2ccb5df2c3a4f182ae9338c82f4f28b62d0d`.

Next: step 2, `R5`'s coherent sample (`dev/r5_control.py`), on the guarded instrument.

## 200. 2026-10-17T20:43:25Z: a correction to entry 199

Entry 199's "entries 179 to 192" reads "entries 185 to 192": step 1 runs from BOUNDARY.md's note (entry 185) to its summary (entry 192). An index expression in the script that wrote entry 199 was wrong; nothing else in that entry depends on it.

## 201. 2026-10-17T21:21:10Z: run `dev/r5_control.py` (case: C2a/R5)

Script SHA-256 `78ddf6d2415be31637c1f63133b47d8376d8328c075a71ac92c84f6be4e5bcc8`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `152674079d7f57a02e14534ed473dc9c43ac5624747878af8aafb7252eb8f463`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `8fdfb0204f5db3360fc2660313f54f8414b13c643f21907e9a00c16f38e05dbf`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/r5_control.out` `fbd2693ffc0fce049b3cd1909cf88a8c9c39ae9115def13c342dd6ed6ccc5a1c`, kept as `dev/runs/201_r5_control.out`
- output `dev/r5_control.json` `1f350110995238799cd598f9c6da52e5fad17190a8dcad70596bdb11be03831c`, kept as `dev/runs/201_r5_control.json`

Step 2, R5's coherent branch: PASS (0 failed); N = [16, 24, 32], eps = [0.25, 0.5, 1.0, 2.0].
EXPECTED_R5.md SHA-256 f0915cd18a36436be4b6b7b18780cc70fd0798fe029e6bbca3fdfd970f6835cb, as logged before the run. Each outcome derived before the run (the script's docstring); no constant refitted.

## 202. 2026-10-17T21:22:26Z: step 2 passes: `R5`'s coherent sample, on the guarded instrument

**The run (entry 201): PASS, 0 claims failed,** 2171 s, `EXPECTED_R5.md` read after its SHA-256 matched the logged one.
- **1 and 2.** The seed passes at `N = 16, 24` and 32 (`Q` = 2289/2288 to round-off). All 12 points are accepted, with `V₀` of dimension 4, ranks [1, 0] and 3 chains; the leak at most 3.0e-10, within its bound; Elliptic, (0, 0, 0); nothing unresolved.
- **3. Theorem R.** Five slow pairs at every point, each definite and Krein-positive. The largest deviation from `εκsτ` is 0.88% (N = 16), 0.93% (N = 24) and 0.93% (N = 32) at ε = 0.25, inside the 5% bar, and 7.1% at ε = 2, so the trend holds at each N.
- **4. The convergence rule:** every ε converged, Elliptic, from the three cutoffs. The smallest ratio is 681, where the margin floor binds.
- **5. The calibration's conditions hold in `R5`,** as they stand:
  - (a) the cluster coefficient is at most 0.0289 (N = 24, ε = 0.5), against 1/15. The controls' largest was 0.0568.
  - (b) L's kernel lift is at most 7.3 u (N = 24, ε = 0.25), against 100 u. That is above the controls' largest, 6.2 u, and 13.7 times below the cut.
  - (c) L's smallest genuine eigenvalue is 4.4e-06 ‖L‖ (N = 32, ε = 0.25), against 10⁵ u, about 2.2×10⁻¹¹ ‖L‖. That is below the controls' smallest, 1.4×10⁻⁵ ‖L‖, as `R5`'s 9/16 scaling and ε = 0.25 make it, and about five decades above its floor.

  No constant was refitted.
- **The cost, measured.** Per point: 2 s at `N = 16`, 48 s at 24 and 489 s at 32, so 539 s at the three together. A Newton evaluation at `N = 32` takes 42 to 68 s. At the run's end the Mac was on battery with Low Power Mode on; the power source during the run is not recorded. The development rates for `R4` were also measured on battery (entries 106 and 173), so the two compare like for like only if this run was too. The rate replaces the terms' `R5` scaling in their next version.

Next: the results to the units, as UA asked; then step 3, the registered driver's dry run, on Blake's go. The terms' next version folds steps 1 to 3 together. No run.

## 203. 2026-10-17T21:22:57Z: a correction to entry 202

Entry 202's "(entries 106 and 173)" reads "(entries 106, 165 and 173)": entry 165 also records the battery runs whose `R4` sample rates the cost model reads. The two cited numbers were typed, not read from the log; both are right, and the list was incomplete. Nothing else in that entry depends on them.

## 204. 2026-10-17T21:27:26Z: step 3 planned: the registered driver and its dry run, for the units

Blake's go (2026-10-17): a packet to the units with step 2's results (entry 202) and step 3's plan, for their GO before anything is built. `DRIVER_PLAN.md` SHA-256 `5300aa24ea201235a10993edfd08a539b1a590e44a8015bc2d27b7192febf4a9`:
- the frozen allowlist in place of the freeze file (UA's condition);
- `run/write_guard.py`, `run/driver.py` and `run/checks.py`, K1 to K6 as the terms state them, with the band-edge guard and the withheld points;
- M8.15's target records copied for K6;
- a dry run on C1 to C3 (GO cases, against a development allowlist), with C2a's ladder segment to ε = 2 for K6's path, about two hours;
- the guard's tests, with no sealed seed constructed.

No run.

## 205. 2026-10-17T21:53:20Z: the units on step 2 and the plan; `DRIVER_PLAN.md` v2

**UA:**
- CONFIRM step 2 and the guard. UA recomputed the 12 records' extrema and reproduced claim 6 in an isolated process.
- GO on step 3, with one requirement: `FROZEN.json` verified against an independently published pin, with K6's records covered by hashes, and a test that edits a case entry while leaving its embedded hashes intact.
- The dry run's expectations are fixed before it runs, and its failures stay in this log.
- `R5` in K4 is Blake's decision, and is not to change the stopping conditions silently.

**UB:**
- KEEP step 2. UB re-read the four ε's verdicts offline from the saved summaries, and matched all 60 predicted modes to 10⁻¹².
- KEEP the guard.
- Changes to the plan: item 4, the target rows' records stay sealed until the go (UB: FATAL as written); and items 5 to 9, 11 and 12.
- v4's `R5` cost as a range, held for v4.

**Verified at source:**
- M8.15.x's spans, `control_2a.py`'s `point_record` and `verdict.py` at MIT `2c27cea`: the rotation span with the fibre and the phase partner projected out; `Z`, the slice direction projected into it; `XY`, its complement.
- UB's slowest-point figure, from `r5_control.json`: 2 + 57 + 642 = 701 s.

**Adjudication of item 4.** The plan of entry 204 read the seal as covering runs on the target rows, not M8.15's records. BOUNDARY.md's list says "M8.15's adjudicated ladders on the target rows are sealed with them", and its plain words bear UB's reading. The build loses nothing by it: K6's reader works on the controls' records, which have the same format. Adopted.

**`DRIVER_PLAN.md` v2** folds UB's items 4 to 9, 11 and 12 as written, UA's freeze pin (`run/FROZEN_PIN`, checked by `frozen()` before it reads anything else) and its edited-entry test, and UA's condition that the dry run's withheld point exists only in `DRY.json`. SHA-256 `6b0a22130af377e42fdae07a6f81910ac2693c2e08f952a8782d22e08c5b7923`.

**Open, Blake's:** whether `R5`'s coherent branch joins K4, decided before the dry run (UB). UA had placed it at the final review. Deciding now is explicit rather than silent, so it meets both.

Next: Blake's decision, then step 3's build. No run.

## 206. 2026-10-17T21:55:49Z: BOUNDARY.md's amendment 4, `R5`'s coherent branch a registered control gating the `R5` rows; the plan follows

Blake's decision (2026-10-17), on the open item of entry 205: `R5`'s coherent branch joins the registered run's controls' phase. Its outcome gates the four `R5` rows only: a failure leaves T1 to T4 in `R5` not qualified, and the run continues. Amendment 4, SHA-256 `a54619de4a31e0abc12e5e7ef55165a5ad0b2fcd9ec9f921b9eb55c7208a4eea`.

`DRIVER_PLAN.md` v2 now states it, and adds it to the dry run's controls, about 36 min more; SHA-256 `ec65b43fb1155b97a1654327b9ca7541bb1c60b192d3e7182d89de940f5b5013`. The terms' K4, verdict rule, run order and cost take it in v4.

Next: step 3's build. No run.

## 207. 2026-10-17T22:09:04Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `eb7e8ea63fb6232f17b1bed14f93f2a77c5356279c84e162bee68136c6f597e4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `2f2c55f4323716520886343933eb2249413adceb5fc1f7ac55d45a98fceb77a2`, kept as `dev/runs/207_test_guard.out`

The guard's tests: PASS, 38 of 38.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 208. 2026-10-17T22:09:17Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/208_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 209. 2026-10-17T22:09:18Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/209_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 210. 2026-10-17T22:09:22Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/210_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 211. 2026-10-17T22:09:23Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `4799e08a29002d5fdddb6c25216c9fcb12df6612fa33d5ba4517bf9d4f44186e`, kept as `dev/runs/211_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 21 of 21 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 212. 2026-10-17T22:09:23Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `5dac49cbe3d9237938a04c0c34ff6cc9ad804454a146c4370dccdbd631e1f34c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `ad77c4c35ba61f76b518b1fc5ddc0b5c60ac8369f156550f8c18b2be478d25c3`, kept as `dev/runs/212_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped, under the instrument as hashed above. No solve.
Derived before the run: the rule's code is unchanged since the runs; only docstrings changed.

## 213. 2026-10-17T22:09:25Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `b6acf0149ab3b4cd932586e4289d6e8180459d2c8148c03706fd3930ef815501`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `e452a4571d816f7ef0c762691f058bd1262cc26239fdafb56e27f263162ba715`, kept as `dev/runs/213_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 214. 2026-10-17T22:10:09Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ff7bb1501ea2de1e973975043270badf7a40d45cf59136ab9de8d028fab861c6`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `2d45398e3f56dc07951865d546132fcff6da18521ad2988d1a157032455e1105`, kept as `dev/runs/214_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 215. 2026-10-17T22:10:49Z: run `run/driver.py` (case: dryrun)

Script SHA-256 `f3b81cef2556853053dbf25d65f90ab2404104f43b3cfedca2c5c79d854592ec`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/dry/plumbing/driver_dry.out` `fd798c79d5311674efb7cecaea1fddca945b39f1038588de7160b2347051b009`, kept as `dev/runs/215_driver_dry.out`
- output `run/dry/plumbing/GATE.json` `6ef2a7f8b71711684e7dc7e8a6d353aafd64bcde1e54b30403e7205f1c9f0aa0`, kept as `dev/runs/215_GATE.json`
- output `run/dry/plumbing/VERDICT.json` `e4117855b6e3ad5b928e5a04ed869583c6eaeef8263f7f4348ad7e3f482b61a6`, kept as `dev/runs/215_VERDICT.json`
- output `run/dry/plumbing/RUNLOG.json` `5443e3579ea6d175635157d1a183aef34d52e489fb1849329d840e297cd37185`, kept as `dev/runs/215_RUNLOG.json`

Step 3's dry run (a plumbing pass at cutoffs [12, 16, 20], unscored): FAIL (5 of 6 claims failed): {'E1': False, 'E2': False, 'E3': False, 'E4': False, 'E5': False, 'E6': True}.
The claims were derived before the run (the driver's docstring; DRIVER_PLAN.md v2). The run's per-case outputs and their SHA-256 are in its RUNLOG.json.

## 216. 2026-10-17T22:14:15Z: run `run/driver.py` (case: dryrun)

Script SHA-256 `682a5a4a10400ad51ff3e5da7b6e5772b323471398a1e49fdce7f243d4f1ea88`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/dry/plumbing/driver_dry.out` `88dca98e4a290008803569a09ea2a21e306c0cdc79ac7deacb88a34e293b4e6b`, kept as `dev/runs/216_driver_dry.out`
- output `run/dry/plumbing/GATE.json` `c61c1f255f75bedd8e976d9ecd2b29d5f15c40052c4f75a31775307599cfc6ec`, kept as `dev/runs/216_GATE.json`
- output `run/dry/plumbing/VERDICT.json` `e4117855b6e3ad5b928e5a04ed869583c6eaeef8263f7f4348ad7e3f482b61a6`, kept as `dev/runs/216_VERDICT.json`
- output `run/dry/plumbing/RUNLOG.json` `50da77f21d2a8044e8f5bf980369394b42ea455ef6a836339d3a4e8d6413a03b`, kept as `dev/runs/216_RUNLOG.json`

Step 3's dry run (a plumbing pass at cutoffs [12, 16, 20], unscored): FAIL (3 of 6 claims failed): {'E1': False, 'E2': False, 'E3': False, 'E4': True, 'E5': True, 'E6': True}.
The claims were derived before the run (the driver's docstring; DRIVER_PLAN.md v2). The run's per-case outputs and their SHA-256 are in its RUNLOG.json.

## 217. 2026-10-17T22:15:03Z: step 3 built: the allowlist, the driver and its checks; the guard's tests pass; two plumbing passes

**Built, as `DRIVER_PLAN.md` v2 states it.**
- `instrument/devtools.py`: `manifest()`, `frozen()` (the pin first, then the manifest, the terms and the target records), `admitted()`. `require()` admits a sealed case only through `frozen()`, R0 never, and a FREEZE file nothing. A `dryrun` run label joins GO; the driver admits only GO cases under it.
- `instrument/branches.py`: `seed_state` admits a sealed seed only through `devtools.admitted()`.
- `run/cases.py`: the 15 cases and their points. Every expectation except C1's is derived from the signature, `(k, r_u)` and the frozen spectrum, and the derived rows equal the terms' table.
- `run/checks.py`: K1 to K6, K3's spans as M8.15.x forms them, the band-edge guard, the withheld-point guard and the verdict.
- `run/driver.py`: the order, the gate, the row gate, R5's gate (amendment 4), resume, and the dry run's claims E1 to E6.
- `run/write_guard.py`, `run/pin_manifest.py`, `run/build_dry.py`.
- `run/name_targets.py` and `run/targets.json`: M8.15's target records named by commit, path and blob id, unopened.
- `run/DRY.json`: the dry run's case list.

**Choices to report to the units:**
- Branch identity is read between the two highest cutoffs, which are N = 24 and 32 in the registered run.
- When the R5 control fails, the R5 rows are recorded as not qualified and are not run.
- A plumbing pass (`--cutoffs`, dry only, unscored) records a would-be stop and continues.

**The checks.**
- The guard's tests (entry 207): PASS, 38 of 38, every refusal and green parent, on temporary trees, with no sealed seed built and no sealed record opened.
- The regression (entries 208 to 213): DL, `dl_recal`, the separation claims, both re-reads and the seed check are byte-identical to their previous runs.
- K3's synthetic claim (entry 214): PASS. The unprojected-`Z` arm misreads, 0.494 against 0.5.

**Two plumbing passes at cutoffs 12, 16 and 20,** unscored. Neither met a code error.
- Entry 215 stopped at C2a: at these cutoffs the rule reads the changes as non-contracting, Unresolved.
- Entry 216 ran past such stops, so every case and every code path ran. E4 and E5 held. E1 to E3 failed only on coarse-cutoff convergence, which development shows at 16, 24 and 32 (the separation rule's samples; step 2).

**Hashes:**
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `run/cases.py` `e5e4396c748e8055b9679c84b52236ff16d9016c30d306c85f369e54a936504a`
- `run/checks.py` `7a9938045b31bc046060be21223299ebdc406bb8ef654fc7dbc0be95ac9581ff`
- `run/driver.py` `682a5a4a10400ad51ff3e5da7b6e5772b323471398a1e49fdce7f243d4f1ea88`
- `run/write_guard.py` `f3534ab61f54fd7642c540475801e63e8915139477510b1519c4057317cf364f`
- `run/pin_manifest.py` `4e7c7ab3eb36bafcb956c67751bdbc121767ba9b57bec89a8a108f5b67798580`
- `run/build_dry.py` `342553c3f06cf3f17934536b479cba789d554d68dca92bdeee74cb28f204a054`
- `run/name_targets.py` `8b4572054cd2d6cb80352d72d2ba2805b97411d21739116ee0cb6ed9d7d4cb1d`
- `run/targets.json` `6ca3854d15b5447ee2eab71670ee37b84d9bad60a4f06923d500aa72a52997af`
- `run/DRY.json` `e7db81fe8484b9080612021e1a656cdd80a07cd5266e03aa054788971fccd4bc`
- `run/test_guard.py` `eb7e8ea63fb6232f17b1bed14f93f2a77c5356279c84e162bee68136c6f597e4`
- `run/test_k3.py` `ff7bb1501ea2de1e973975043270badf7a40d45cf59136ab9de8d028fab861c6`

Next: the dry run at 16, 24 and 32, about 2.6 hours, on Blake's word about the power source.

## 218. 2026-10-17T22:48:39Z: run `run/driver.py --dry` (case: dryrun), logged by hand: the run stopped at C2a, and its claims code crashed

Script SHA-256 `682a5a4a10400ad51ff3e5da7b6e5772b323471398a1e49fdce7f243d4f1ea88`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `c29730c9c8072b4b24c213b518e34e946617d281eddf1e2c5df4e26c050c0056`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/dry/driver.log` `cbd1c5631206852295fc8aa9c10eb7977936e0fb663f79acb80c9913e856ef37`, kept as `dev/runs/218_dry_driver.log`
- output `run/dry/RUNLOG.json` `8afad61d58dc8660bf13b3313735c6c27f95c9592d8561d82cee60d571474153`, kept as `dev/runs/218_dry_RUNLOG.json`
- output `run/dry/GATE.json` `52b474819ac581cb01cd3d49b8a9f7b9904ba1ed69eac1009b93640c067473e0`, kept as `dev/runs/218_dry_GATE.json`
- output `run/dry/VERDICT.json` `e4117855b6e3ad5b928e5a04ed869583c6eaeef8263f7f4348ad7e3f482b61a6`, kept as `dev/runs/218_dry_VERDICT.json`
- output `run/dry/C1.json` `c1ebb02e1457aa65bf08cb3236564253ee6f7f379dbbf1d9574fb3065243c0b6`, kept as `dev/runs/218_dry_C1.json`
- output `run/dry/C2a.json` `8d26691571f2459b1fbab6c05f0add84ef3eb2ded8dab2a5ee49760292023a90`, kept as `dev/runs/218_dry_C2a.json`
- output `run/dry/C2a.npz` `ec646f784f5ed227b058aa43a479df043b3ffe1794bcf146c30c595dedffa954`, kept as `dev/runs/218_dry_C2a.npz`

**The run** (about 26 min, on battery).
- C1: K1 and K4 pass.
- C2a: K1, K2, the leading-order bar and the trend pass, and so does the K5 code path. K4 fails: ε = 0.25, 0.5 and 1 read converged, while ε = 2 reads Unresolved, "tested set at 4.26701e-16+4.03918j (+0): the set's count differs between cutoffs".
- The run stopped there, as registered, and wrote its gate record. C2b, C3, the R5 control and C2a's ladder segment did not run.
- The claims code then crashed (KeyError on C2b): it assumed every case had run. So the run wrote no entry of its own, and this one records it.
- **The dry run fails.** E1 is false, and E2 to E6 were not evaluated. Nothing is corrected before this record.

**The diagnosis, from the saved summaries, with no solve: the set rule's closure depends on the order of the groups.**
- At ε = 2, two Krein-positive groups near 4.039i are those of entry 159. At every cutoff their centres equal development's (entry 170) to 10⁻⁹, and so do the uniqueness ratios: 2.015, 2.114 and 1.245, none near 2.
- `ambiguous_set` closes a set from one seed group through the test "within twice the nearest candidate". That test is not symmetric.
  - From the group at 4.039179i, the closure has 1, 1 and 2 members at N = 32, 24 and 16. That count differs, so the reading is Unresolved.
  - From the group at 4.038938i, it has 2, 2 and 2. That reading converges, and it also covers the other group.
- `separation` seeds from the highest cutoff's groups in their stored order. The dry run listed 4.039179i first (position 43 against 45); development listed 4.038938i first (69 against 73).
- So the verdict turns on the eigensolver's output order, which round-off can change. The rule as built can therefore stop a GO control by chance.

Next: to Blake, with a proposed correction for the units (a symmetric competitor relation, so a set is the connected component of its seed, whichever member seeds it), tests that permute the group order, and a fix to the claims code. No run.

## 219. 2026-10-17T23:12:10Z: the symmetric closure previewed on every saved reading, logged by hand: order-free, but it joins sets through the higher cutoff's unmatched groups; not adopted

**What was built after entry 218, before any run.** `ambiguous_set` read the competitor test both ways: two groups at adjacent cutoffs were linked when either lies within twice the other's nearest candidate, so a set was the connected component of its seed. The closure as built became the arm `one_way_set`. `instrument/convergence.py` SHA-256 `2ff2ab1f2b1f81e804985f8d72b371ccca1e636d351795752258d3852cacf9da`. No logged run used it.

**The preview, unlogged, with no solve.** It read the saved summaries of every reading that carries them, with each point's band edge as the driver read it: 49 readings.
- The sources: development's C2a sample and ladders (entries 170 and 171), C2b's ladders (entry 172), the R5 control (entry 201) and the dry run's C2a (entry 218).
- Under the arm, all 49 verdicts are as shipped.
- Each reading was read 24 more times, with its groups shuffled at every cutoff. Under the either-way link, no verdict changed. Under the arm, C2a's ε = 2 changed in all three places it was read (entries 170, 171 and 218).
- Against the shipped verdicts, the either-way link changed seven:
  - the dry run's C2a at ε = 2, Unresolved to converged, as intended;
  - C2a's ladders at ε = 4, 5.66 and 32 (entry 171), Unresolved to converged;
  - C2b's ladders at ε = 11.3, 22.6 and 32 (entry 172), converged to Unresolved.

**C2b's three changes are a defect.** Take ε = 11.3, at cutoffs 16 and 24.
- The set seeded at the slow pair near 0.55i grew to 162 of the 165 Krein-positive groups at N = 24 and 38 of the 41 at N = 16, from 0.54i to 33.0i, and its count differs.
- At N = 24, the groups above the dense part of N = 16's spectrum have no counterpart. At 9.76i the nearest lies 3.68 away, so twice that distance covers 14 groups at N = 16. Links read from those groups' side join the pair to the whole spectrum.
- From the seed alone, the set is the pair: 2 and 2.
- A closure that joins sets through groups without counterparts reads a converged control as Unresolved, for a reason no type-changing event supplies. Not adopted.

**C2a's ladders.**
- At ε = 32, two closures share a group at N = 24, 4.15583i. As built, the closure [4.21093i, 4.15583i] reads Unresolved because its count differs, while [4.15583i, 4.10279i] converges. As one set they have 3 and 3, and converge. This is entry 218's defect again.
- At ε = 4, the pair at N = 24 (4.05167i and 4.05141i) has one candidate at N = 16 by its own test, 4.05179i. The other N = 16 group, 4.05230i, has both members within twice its own nearest distance, but lies beyond twice theirs. ε = 5.66 is alike.
  - Only a link read from that group's side admits it, which is the link that joined C2b's sets to the spectrum.
  - Without that link the count differs, and the reading stays Unresolved, as shipped.

**The correction, previewed the same way** (a prototype in the scratchpad, unlogged).
- The sets are the ruled ones, each the closure of one seed under the test. Closures that share a group are one set, their union, which is closed under the same test.
- Every group to be read is read; none is passed over for lying in a set already read.
- A tested set's partner joins the groups to be read before any group is read.
- Over the 49 readings and 24 shuffles each, no verdict changed. The largest set counts 5 at the highest cutoff.
- Against the shipped verdicts, two changed: the dry run's ε = 2 (2, 2 and 2: converged) and C2a's ladders at ε = 32 (3 and 3: converged). Every other verdict is as shipped, C2b's included.

Next: the correction in `instrument/convergence.py`, with the arm kept as built; a logged test of order, with the arm as its failing side on C2a's data; the claims code; the regression.

## 220. 2026-10-17T23:16:39Z: run `dev/set_order.py` (case: C2a)

Script SHA-256 `9846d9480a102792936d2b379a76a5cbde10323d51c4598fa88b06a017e8e445`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a.out` `825eb531bfd181be20eb740eb298551cb4c608b602d7b0ed028adf3e9ad263c4`, kept as `dev/runs/220_set_order_C2a.out`

The separation rule read in any order of the groups, on C2a's saved summaries: PASS (0 failed), 25 readings, 24 shuffles each. Under the arm, the shuffles turn 3. No solve.
Each claim derived before the run (the script's docstring).

## 221. 2026-10-17T23:16:45Z: run `dev/set_order.py` (case: C2b)

Script SHA-256 `9846d9480a102792936d2b379a76a5cbde10323d51c4598fa88b06a017e8e445`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2b.out` `fd5024c50ba4e98bb406419b8a3dee3f24171a422f3bf733348c114e5307c133`, kept as `dev/runs/221_set_order_C2b.out`

The separation rule read in any order of the groups, on C2b's saved summaries: PASS (0 failed), 20 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 222. 2026-10-17T23:16:47Z: run `dev/set_order.py` (case: C2a/R5)

Script SHA-256 `9846d9480a102792936d2b379a76a5cbde10323d51c4598fa88b06a017e8e445`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a_R5.out` `69c6c5b950bacacc3d9f4809907ee0d0fd782f6d2d74392c27d740566d45002b`, kept as `dev/runs/222_set_order_C2a_R5.out`

The separation rule read in any order of the groups, on C2a/R5's saved summaries: PASS (0 failed), 4 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 223. 2026-10-17T23:18:54Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `1cdb94d753999fe94f56fa8b2aee8f61ee22b44bd2918024ce7aee48597e9ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/223_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 224. 2026-10-17T23:20:08Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `eb7e8ea63fb6232f17b1bed14f93f2a77c5356279c84e162bee68136c6f597e4`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `2f2c55f4323716520886343933eb2249413adceb5fc1f7ac55d45a98fceb77a2`, kept as `dev/runs/224_test_guard.out`

The guard's tests: PASS, 38 of 38.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 225. 2026-10-17T23:20:09Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/225_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 226. 2026-10-17T23:20:11Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/226_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 227. 2026-10-17T23:20:15Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/227_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 228. 2026-10-17T23:20:15Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `bcd171e4c06b5e3ae8c5dfa846c52e179962bdd832c0c55207d42cf21d7603dc`, kept as `dev/runs/228_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 20 of 20 verdicts as shipped and 1 of 1 changed as named; under the arm, 21 of 21 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 229. 2026-10-17T23:20:16Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `43aa6f49cb647fa88732d6b7756baa1fe1dd91099165b127d5e9ad33c2986a40`, kept as `dev/runs/229_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped and 0 of 0 changed as named; under the arm, 20 of 20 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 230. 2026-10-17T23:20:30Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `b6acf0149ab3b4cd932586e4289d6e8180459d2c8148c03706fd3930ef815501`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `e452a4571d816f7ef0c762691f058bd1262cc26239fdafb56e27f263162ba715`, kept as `dev/runs/230_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 231. 2026-10-17T23:20:31Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ff7bb1501ea2de1e973975043270badf7a40d45cf59136ab9de8d028fab861c6`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `2d45398e3f56dc07951865d546132fcff6da18521ad2988d1a157032455e1105`, kept as `dev/runs/231_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 232. 2026-10-17T23:22:14Z: the set rule corrected, closures that share a group read as one set, and the claims code; the order test, the claims test and the regression pass

**Changed, after entry 219's record.**
- `instrument/convergence.py`:
  - `closure()` is the ruled closure from one seed, its body unchanged from the sets as built.
  - `merged_sets()` joins the closures of every failing group to be read that share a group, transitively, into their union.
  - `separation()` first takes the groups to be read to a fixpoint, so a tested set's partner joins before any group is read. It then reads every one of them, and a reading identical to one already made is not repeated.
  - The arm `one_way_set` keeps the sets as built: each closure alone, the groups read in stored order, those already read passed over, and set partners added as before.
  - The either-way link of entry 219 is gone.
- `run/driver.py`: in `dry_claims`, a claim that reads a case which did not run is not evaluated, and counts as failed. The docstring says so.
- New: `dev/set_order.py` and `run/test_claims.py`.
- `dev/sep_reread.py`: its claims are derived again for the rule's change. `CHANGED` names C2a's ladder at ε = 32, and a second claim reads every shipped verdict under the arm.
- `DESIGN.md` v2.21: § 10.2 states the merged closure, the order's record, and that the change awaits both units.

**The runs.**
- The order, entries 220 to 222: PASS.
  - C2a: 25 readings, none turned under the rule by 24 shuffles of every cutoff's groups. The arm turned ε = 2 in each of the three readings that carry it, by 11 (entry 170), 14 (entry 171), 11 (entry 218) of 24.
  - Exchanging the stored positions of the pair at 4.038938i and 4.039179i turned the arm each way and the rule neither way. Their closures are 2, 2 and 2 against 1, 1 and 2.
  - The dry run's ε = 2 reads converged, Elliptic, its set counting 2 at every cutoff. Under the arm it reads Unresolved, as entry 218 shipped it.
  - C2b: 20 readings, none turned under the rule or the arm; the largest set counts 5. The R5 control: 4 readings, none turned; it forms no set.
- The claims, entry 223: PASS. On entry 218's kept outputs there is no exception. All six claims read as not evaluated, each naming what did not run, and the captured entry reads FAIL, 6 of 6.
- The regression, entries 224 to 231: PASS.
  - Byte-identical to entries 207 to 214: the guard's tests (38 of 38), DL, `dl_recal`, the separation claims, the seed check, and K3's synthetic claim. The separation claims being among them means the merged closure reads every synthetic family, sets included, as the sets as built did.
  - The two re-reads differ from entries 211 and 212 as derived. C2a: 20 of 20 as shipped, and ε = 32 changed as named. C2b: 20 of 20. Under the arm: 21 of 21 and 20 of 20 as shipped.

**Not done:**
- The dry run is not rerun. It waits for the units' confirmation, about 2.6 hours.
- `run/test_k3.py`'s claim 2 waits for the dry run's arrays.

**Queued for the terms v4:**
- In § THE CONVERGENCE RULE, the set rule gains the merged closure.
- The failures on record gain the dry run's order dependence and the either-way closure.

**Hashes:**
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `run/driver.py` `0a7572592f81a411f3602551de5d50a2e432f51b69c1729725e9463e2f6832ab`
- `run/test_claims.py` `1cdb94d753999fe94f56fa8b2aee8f61ee22b44bd2918024ce7aee48597e9ae7`
- `dev/set_order.py` `9846d9480a102792936d2b379a76a5cbde10323d51c4598fa88b06a017e8e445`
- `dev/sep_reread.py` `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`
- `DESIGN.md` `39561f960fb2d2f623ae65a30cd2330390c0c0b3e27647d0164b42165b55c115`

Next: the packet to the units: entry 218's failure and diagnosis, the either-way closure's failure, the correction, its tests and the regression.

## 233. 2026-10-17T23:28:24Z: the file entry 219 previewed, rebuilt and kept; two gaps in the driver's resume, found, not built

**The file.** After entry 232's correction, `instrument/convergence.py` as entry 219 previewed it no longer existed.
- It was rebuilt from the corrected file by reversing the correction's edits. Its SHA-256, `2ff2ab1f2b1f81e804985f8d72b371ccca1e636d351795752258d3852cacf9da`, equals the one entry 219 records.
- Kept as `dev/convergence_either_way.py`, outside the instrument and the manifest.
- Read on the same 49 saved readings, unlogged, it changes the same seven verdicts entry 219 lists.

**The resume, found while preparing the units' packet.** Neither gap is built.
- (a) When the driver resumes a dry run, it does not compare the instrument's hashes with those the run started under. In the real run, the allowlist pins them.
- (b) The driver loads a completed case without the stop check, so a restarted run would pass a control that had stopped it. The rows stay protected, because the row gate refuses a gate record that does not show K1 to K4 passed.
- Either way, the dry run's rerun starts from an empty `run/dry`. Entry 218's outputs are kept in `dev/runs`.

Next: the packet to the units.

## 234. 2026-10-17T23:55:29Z: the units on step 3: the correction confirmed and the separation gate closed again; the resume safeguards and three driver fixes required before the dry run's rerun

**UA (F1):**
- CONFIRM the dry run's failure, its diagnosis, and the rejection of the either-way link.
- CONFIRM the merged closure. UA reran the order tests, the affected comparisons and the claims test, and checked that the result comes neither from a lower separation factor nor from a wider proximity rule.
  - F1 accepts reopening the separation gate (entry 180) for this defect and closing it again.
  - The closure stays an operational rule, not a proof, and its disclosed limits stand.
- CONFIRM the claims code.
- **Required before the rerun:**
  - (A) the run's log records the manifest's SHA-256 when the run starts, and a resume checks it before loading any completed case;
  - (B) a resume refuses to continue past a recorded stop;
  - a positive and a negative test for each, on synthetic logs, with no solve.
- **Conditional GO:** once the safeguards pass, the dry run reruns from an empty `run/dry`, with entry 218's outputs kept in the archive and E1 to E6 unchanged. A second failure is kept and returned for review; no automatic repair-and-rerun follows.
- **HOLD:** the terms v4 and the filing, until the dry run is reviewed; every sealed case.

**UB:**
- **Reproduced:**
  - the 11 diffs, and all eight packet checks byte for byte (the guard's tests 38 of 38);
  - the seed check, against UB's own clone;
  - the separation claims, to round-off on NumPy 2.5.3;
  - the five target records' blob ids at `33aeb754`, without opening the files.
- **KEEP:**
  - the allowlist, `cases.py`, and `checks.py` and `driver.py` apart from items 4 to 6;
  - the three reported choices;
  - the dry run's diagnosis: ratios 2.0148, 2.1140 and 1.2446, positions 43 and 45;
  - the correction: 49 readings through 200 shuffles plus the reversal, 9,849 orders, with no verdict or row turned and only a failing set's label changing;
  - the claims code.
- **CHANGE, FIXABLE:**
  - 4: at a stop, the gate record names the failed checks, and the verdict reads NOT QUALIFIED naming them. `incomplete` is kept for a dry run and for an interruption. An `R5` row that is not run names the `R5` control's failed check. The plan gains UB's bullet on `VERDICT.json` and the transcript.
  - 5: the `--cutoffs` guard raises `SystemExit` in place of an `assert`, which `python -O` removes.
  - 6: test 2's green parent runs through test 8's setup: C2a in `branches.SEALED`, `devtools.GO` emptied, C2a listed in the test `FROZEN.json`. P5 keeps only its refusal on the name.
  - 7: the plan's `R5` line names the failing check and says the rows are not run.
  - 11: the resume fix, now. Gap (b) reaches the pyramid in a real run. A crash between a case's completion entry and the gate record leaves no stop in the log, so a resume reads each completed case's stop test again. The plan's interruption bullet is replaced, and `test_guard.py` gains three refusals, with a clean interruption as the green parent.
- **GO for the rerun** once UA confirms item 9 (done, above), items 4, 5, 6 and 11 are built, `test_guard.py` and `test_claims.py` are rerun, and the regression is byte-identical.
- **For v4 (13):** the freeze's order, in FIXED AT THE FREEZE.

**Verified at source:**
- Entry 218's kept `VERDICT.json` reads `incomplete`, and its gate record's stop reads "C2a failed a check". The terms' verdict rule reads "NOT QUALIFIED, with the failing check named".
- `driver.py`'s `--cutoffs` guard is an `assert`. Test 2's green parent admits P5 through a test `FROZEN.json` that lists it, where plan v2 says the green parents list GO cases only.
- `resume()` checks only the completed outputs' hashes. The loop loads a completed case and continues without its stop test. A case's completion is saved before its stop test and gate record, so the crash window exists.

**Item 5 swept, flagged and not built:** two more guards are `assert`s that `python -O` would remove: the check in `branches.expected_v0` that `EXPECTED_V0.md` equals its logged version, and `devtools.log_run`'s refusal to overwrite a kept output. The registered command line is `python3 -I -B`, which keeps them. The other `assert`s are internal consistency checks.

Next: build items 4, 5, 6 and 11, with `DRIVER_PLAN.md` v3; the tests and the regression; then the rerun.

## 235. 2026-10-18T00:01:44Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `6e40f50b7487368ceb9fd580ac0360a6ea15ab4cbdee461e608a3af7ac3db544`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `9f9968f3808de36e3b16c742464d5c128fd94e5bfbfb97bb010ac30b802a0e0d`, kept as `dev/runs/235_test_guard.out`

The guard's tests: PASS, 52 of 52.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 236. 2026-10-18T00:01:45Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `1cdb94d753999fe94f56fa8b2aee8f61ee22b44bd2918024ce7aee48597e9ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/236_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 237. 2026-10-18T00:01:46Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/237_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 238. 2026-10-18T00:01:48Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/238_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 239. 2026-10-18T00:01:52Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/239_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 240. 2026-10-18T00:01:52Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `bcd171e4c06b5e3ae8c5dfa846c52e179962bdd832c0c55207d42cf21d7603dc`, kept as `dev/runs/240_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 20 of 20 verdicts as shipped and 1 of 1 changed as named; under the arm, 21 of 21 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 241. 2026-10-18T00:01:52Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `43aa6f49cb647fa88732d6b7756baa1fe1dd91099165b127d5e9ad33c2986a40`, kept as `dev/runs/241_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped and 0 of 0 changed as named; under the arm, 20 of 20 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 242. 2026-10-18T00:01:54Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `b6acf0149ab3b4cd932586e4289d6e8180459d2c8148c03706fd3930ef815501`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `e452a4571d816f7ef0c762691f058bd1262cc26239fdafb56e27f263162ba715`, kept as `dev/runs/242_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 243. 2026-10-18T00:01:55Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ff7bb1501ea2de1e973975043270badf7a40d45cf59136ab9de8d028fab861c6`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `2d45398e3f56dc07951865d546132fcff6da18521ad2988d1a157032455e1105`, kept as `dev/runs/243_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 244. 2026-10-18T00:03:11Z: entry 234's items built: the resume safeguards, the stop's record and the cutoffs guard; the guard's tests 52 of 52, the regression identical; `run/dry` moved aside for the rerun

**Built.**
- **`run/checks.py`:**
  - `stop_checks()` is the one stop test that the driver and the verdict share: K1, K2 and K4, and K3 at the pyramid.
  - `r5_failed()` gives the `R5` control's failed checks.
  - `verdict(results, dry)` reads NOT QUALIFIED, naming the failed checks, whenever a completed control or the pyramid failed one. It keeps `incomplete` for a dry run and for an interruption. Every verdict names its failed cases' checks, as "C2a: K4" (UB's item 4).
- **`run/driver.py`:**
  - The gate record's stop names the failed checks, as "C2a failed K4". An `R5` row that is not run names the `R5` control's failed checks (UB's item 4).
  - `VERDICT.json` and the transcript, `driver.out`, are written at the end and at a stop, each with its SHA-256 in the run's log (UB's item 4). The dry claims keep `driver.out` among their outputs.
  - `--cutoffs` without `--dry` raises `SystemExit` (UB's item 5).
  - The run's log records the manifest's SHA-256 when the run starts. Before any completed case loads, `resume()` refuses a log that records no manifest or another tree's, and a log whose gate record names a stop (UA's A and B).
  - Each completed case's stop test is read again on resume, so a crash between a case's completion and its gate record stops the resumed run there (UB's item 11).
  - My choice: a gate record is written once, so a resume after a completed pyramid writes it only if the crash came before it.
- **`run/test_guard.py`:**
  - Test 2 runs on the frozen path (UB's item 6).
  - Test 9 tests the resume through `driver.main`, with stand-in solvers that raise instead of solving. It has UB's three refusals and a clean interruption as their green parent. Mine are added: a fresh run records its manifest; a log that records none is refused; and a resume after the stop the run itself wrote is refused.
  - Test 10 tests the stop's record, with `--cutoffs` under `python -O`, and an `assert` of the same form as the arm.
- **`DRIVER_PLAN.md` v3:** UB's three texts verbatim (items 4, 7 and 11) and the new tests in its list. One line is mine: the convergence rule changed once (entries 218, 232 and 234), where v2 said it would not change.
- **`DESIGN.md` v2.22:** § 10.2 records both units' confirmation, and the gate closed again.

**The runs:**
- Unlogged first, on temporary trees: tests 2, 9 and 10, 20 of 20, to check the harness.
- The guard's tests (entry 235): PASS, 52 of 52. Against entry 224, the output differs only as derived: the plan's version, test 2's green parent and refusals, and tests 9 and 10.
- The claims test (entry 236): PASS, byte-identical to entry 223.
- The regression (entries 237 to 243): byte-identical to entries 225 to 231.
- So UB's conditions for the rerun hold, and so do UA's.

**`run/dry` moved aside** to `dev/runs/218_run_dry/`, so the rerun starts from an empty `run/dry` (UA, UB).
- Its seven files equal entry 218's kept copies.
- In `plumbing/`, the gate record, verdict, log and transcript equal entry 216's kept copies. Its eight case files equal the hashes its log records.

**Hashes:**
- `run/driver.py` `20d497db5ecef6dcef6db9fa0ea2b69cd840936bb42f0e26d1c0915d32b15f83`
- `run/checks.py` `29c8f49b4471781b47777f23c772ab1341805a7419a178f851db81c007081b26`
- `run/test_guard.py` `6e40f50b7487368ceb9fd580ac0360a6ea15ab4cbdee461e608a3af7ac3db544`
- `DRIVER_PLAN.md` `d0105bf57e566e50e82a1a2fc7ca8d6bf4b4d113bb820ff8104bfb4d0915756b`
- `DESIGN.md` `273484412f6cc29fec843b123c32182d01948948ceed04d72cf8b1765e5fc3a7`

Next: the dry run's rerun, from an empty `run/dry`, about 2.6 hours.

## 245. 2026-10-18T01:43:31Z: run `run/driver.py --dry` (case: dryrun), the rerun, logged by hand: every case ran and passed, and E1 to E5 hold; the claims code crashed at E6, so the run wrote no entry

Script SHA-256 `20d497db5ecef6dcef6db9fa0ea2b69cd840936bb42f0e26d1c0915d32b15f83`, as entry 244 logged it; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/dry/driver.log` `d7ce6fb1745aaed6a7dc73871b4638338fc838b0fba2f17d5a00aae7a3398ced`, kept as `dev/runs/245_dry_driver.log`
- output `run/dry/driver.out` `28fb8f565e74b5783534636ca886b967fb7879c08e8a09d0eb6c6495f63d45a6`, kept as `dev/runs/245_dry_driver.out`
- output `run/dry/RUNLOG.json` `26cb12199ee4685608564871205d0d180e29a3482d40ce78b7335d2712f431b1`, kept as `dev/runs/245_dry_RUNLOG.json`
- output `run/dry/GATE.json` `ce898d6e28797afed0d4970f1799ffed858485580401b3ae1b5f43ff03f6a458`, kept as `dev/runs/245_dry_GATE.json`
- output `run/dry/VERDICT.json` `0282e786f26e1004dcef66c46a7afa386db978436cf763400149f25c5e976d69`, kept as `dev/runs/245_dry_VERDICT.json`
- output `run/dry/C1.json` `25d849d6cd9be6afb902b4db36788695f8d23342b7f9655ec5a850dd7055e481`, kept as `dev/runs/245_dry_C1.json`
- output `run/dry/C2a.json` `4a045372a34a4b969f95c42754fa0610cc5faf37f00f55d9f92d27b076c0abe3`, kept as `dev/runs/245_dry_C2a.json`
- output `run/dry/C2a.npz` `ec646f784f5ed227b058aa43a479df043b3ffe1794bcf146c30c595dedffa954`, kept as `dev/runs/245_dry_C2a.npz`
- output `run/dry/C2b.json` `01887c84a2ee63556b9e63950d39b05ed96d00ecb05891da18c36dbf98878809`, kept as `dev/runs/245_dry_C2b.json`
- output `run/dry/C3.json` `f3c2e2e41ad64e167261dfe965c01e62457832dd75edffff941fc43df5520144`, kept as `dev/runs/245_dry_C3.json`
- output `run/dry/C3.npz` `366681b4958ed2c6e3c88881f442b1a085ba8a783d63c867eccc1a37a836e488`, kept as `dev/runs/245_dry_C3.npz`
- output `run/dry/C2a_R5.json` `85e367c717b9c5b4413db618dfa2161270abb6eaffa3fc26f2e2b1b9ddd3df3c`, kept as `dev/runs/245_dry_C2a_R5.json`
- output `run/dry/C2a_ladder.json` `f9824f1703cefee304f61e1bd6d73e268ba06a7245883a562138684df66cc1b2`, kept as `dev/runs/245_dry_C2a_ladder.json`

**The run,** from an empty `run/dry`, 12 minutes, from 00:03Z. The Mac was on battery at the start and on mains power by 01:15Z. Its log recorded the manifest's SHA-256 at the start, and there was no resume.
- C1: K1 and K4 pass (12 min).
- C2a: K1, K2, K4, the convergence, the bar, the trend and K5's code path pass (13 min). ε = 2 converges.
- C2b: the same checks, all pass (6 min).
- C3: K1, K4, the convergence, the bar, the trend and K5's code path pass (18 min).
- The `R5` control: K1, K4, the convergence, the bar and the trend pass (26 min), so the `R5` gate passes.
- The dry gate record, written after the `R5` control, has no stop. It reads incomplete, with P5 absent and the `R5` gate passed.
- C2a's ladder segment: K6 passes, 6 of 6 read points agree with M8.15 and none disagree, and the withheld point is accepted (23 min).
- The verdict reads `incomplete`, as a dry run's does, with nothing failed. `VERDICT.json` and the transcript `driver.out` were written, and their SHA-256s, the gate record's and every case's outputs' equal what the run's log records.
- E1, E2, E3, E4 and E5: True. On E2, K3's code path on C2a reads "not resolved, kernel exact" at (b), and (c)'s overlaps on C2a's smallest pair are near 10⁻¹².
- **E6 was not evaluated.** Its reader, `dev_points`, raised KeyError `summary` on C2b's development sample (entry 160), after reading C2a's (entry 170). So the claims' transcript, `driver_dry.out`, was not written, and the run wrote no entry. This one records it by hand, before any correction.
- Under the driver's rule, a claim not evaluated counts as failed. **So the dry run does not pass as registered.**

**The diagnosis, read only, with no solve.**
- E6's reader takes each development point's slow eigenvalues from its saved summary.
  - C2a's sample (entry 170) and the `R5` control's (entry 201) saved them.
  - C2b's sample (entry 160) and C3's (entry 161) predate the saving of summaries. Their records hold the type, the indices and the margin, but no eigenvalues.
  - D7's runs of the same controls (entries 70 and 71) hold no list of groups either.
- E6's code path had never run. The plumbing passes skip it, and entry 218's run stopped before it. This is the same kind of gap as entry 218's KeyError at E1.
- The run's outputs hold every point's record and groups. So once its reader is settled, E6 can be read from them with no solve.

Next: to Blake, and the units' review (UA: a second failure is kept and returned, with no automatic repair-and-rerun). No correction is made.

## 246. 2026-10-18T01:43:44Z: correction to entry 245: the run took 98 minutes, not 12

Entry 245 says the rerun took 12 minutes. Its verdict line in `driver.log` reads 5871 s, which is 98 minutes, from 00:03Z to 01:41Z. The 12 came from C1's 709 s, the first line that the pattern used to find the total matched. Every other number in entry 245 was read from its own field.

## 247. 2026-10-18T01:54:57Z: correction to entry 245: D7's runs hold the slow eigenvalues

Entry 245 says: "D7's runs of the same controls (entries 70 and 71) hold no list of groups either." That is wrong.
- D7's records of C2a, C2b and C3 (entries 69, 70 and 71) hold, at each of their nine points, the slow eigenvalues (`slow`) and the imaginary groups with their Krein data (`slow_groups`).
- My listing of their fields printed the first 20 of 32, and `slow` and `slow_groups` came after the cut. I read a negative from truncated output.
- UB found the fields. UA's ruling, which chose (b) over (a), rested on my statement.

## 248. 2026-10-18T01:55:14Z: the units on the rerun and E6: UA rules (b), UB proposes (c); the units split, so the decision is Blake's

**UA (F1):**
- CONFIRM the numerical success, and keep the dry run's FAIL until E6 is scored. It is a reporting and test-fixture failure, not a wrong classification.
- GO on (b): the C2b and C3 development samples rerun, about 25 minutes, saving their slow eigenvalues, with no change to the solver, tolerances, classification or calibration.
  - The new records are hashed and logged as newly made pre-freeze comparison records before E6 is scored.
  - E6 is scored from the kept outputs of the 98-minute run, with no full rerun.
  - The original records and the failed run's archive stay unchanged.
- In either case, E6's reader turns a missing required field into an explicit FAIL, not an exception, with a cheap missing-field regression.
- Why (b) over (a): it gives the comparison E6 intended without narrowing it after the failure.
- This ruling chose between (a) and (b) on my statement, corrected in entry 247, that no saved eigenvalues of C2b and C3 exist.

**UB:**
- KEEP the rerun as reported, and entries 245 and 246.
- CHANGE, FIXABLE, the claims code: a development record without the field it compares counts as a claim not evaluated, failed, with the entry still written. UB gives a docstring text.
- CHANGE, FIXABLE, E6's references, option (c).
  - E6 is scored as written: type and indices against samples 170, 160, 161 and 201, and every slow eigenvalue against the samples that saved them.
  - C2a's and the `R5` control's eigenvalues come from their samples (entries 170 and 201). C2b's and C3's come from D7's records (entries 70 and 71), which were logged before the dry run and have not yet been compared with it.
  - Against D7, the tolerance is the dry run record's own margin, the stricter one, since D7's margins predate § 7's calibration. C3's values are read as real numbers.
  - No solve and no new record.
  - Not (a), because it drops eigenvalue checks that saved records can make. Not (b), because it makes references after the dry run, from the same code on the same machine.
- The scoring: a logged run applies the edited `dry_claims` to entry 245's kept outputs, each checked against `RUNLOG.json`. E1 to E5 must come out as the run scored them, and an arm with a record's eigenvalue field removed must read E6 as not evaluated and failed, with the entry written.
- GO on that scoring. If E6 passes, step 3's dry run closes; if it fails on a real difference, that stands.

**Verified at source:**
- D7's records of C2a, C2b and C3 (entries 69, 70 and 71) hold `slow` and `slow_groups` at N = 16, 24 and 32, ε = 0.5, 1 and 2. Their SHA-256s equal the outputs at DEVLOG lines 1067 and 1087.
- D7's type and indices equal those of samples 160 and 161 at 18 of 18 points.
- D7's C2a slow eigenvalues equal sample 170's to 2.1×10⁻¹⁴ at 9 of 9 points, with the same type and indices. So the instrument's changes since D7 leave its eigenvalues usable as references.
- D7's margins run from 5.2×10⁻⁶ to 1.4×10⁻⁵, and the dry run records' from 1.7×10⁻⁷ to 1.4×10⁻⁶.
- C3's `slow` holds three equal real values, and its `slow_groups` is empty.

**My recommendation:** (c).
- It scores every slow eigenvalue of all four controls, which is what UA's principle asks, against records logged before the dry run, at a stricter tolerance, with no solve.
- UA's missing-field FAIL and its regression go in under either option.

Next: Blake's decision. Nothing is built or scored until then.

## 249. 2026-10-18T02:01:41Z: UA withdraws (b) and gives GO on (c), under four conditions; the units agree, and the first condition is verified

**UA (F1), after entry 247's correction:** GO on (c), which supersedes its (b). Its reasons: D7's records predate the dry run, so they make the stronger reference; every slow eigenvalue of all four controls is compared; and nothing is solved. The conditions:
1. D7's eigenvalues correspond to the dry run's in case, amplitude, cutoff and normalization.
2. A record with a field missing returns FAIL rather than crashing.
3. E6's registered criterion stays: within the larger margin of the two records. A stricter comparison may be reported beside it, but does not replace it.
4. E6 is scored from the archived outputs of the 98-minute run, and the original failure and the corrections stay on record.

UA accepted entry 247's provenance as reported, without inspecting the files. With UB's (c) in entry 248, the units agree, and Blake chose (c).

**Condition 3 against UB's proposal.** UB had proposed the dry run record's own margin as the tolerance against D7. Under condition 3, that test is reported beside the registered one, not in its place.

**Condition 1, verified without reading any eigenvalue, so E6's outcome is not seen before its logged scoring:**
- **The cases.** D7's definitions in `dev/d7_controls.py` equal `run/cases.py`'s: C2a in `R4`, the coherent v₃, λ₀ = 48, Q = 1288/1287, (k, r_u) = (3, 1); C2b in `R2`, v_7/2, λ₀ = 63, Q = 144/143, (5, 1); C3 in `R4`, the octahedron, λ₀ = 48, Q = 175/143, (4, 4).
- **The amplitudes and cutoffs.** Every reference point has a dry-run point at the same N and ε: 9 for each of C2a, C2b and C3, and 12 for the `R5` control. ε agrees within 5.5×10⁻¹¹ (C2a), 4.2×10⁻⁹ (C2b) and 4.9×10⁻⁷ (C3), and so does ‖φ‖², relatively within 1.1×10⁻¹⁰, 8.5×10⁻⁹ and 9.8×10⁻⁷. The `R5` control's sample is the same run's data, exactly. The basis is fixed by slot and N.
- **The normalization.** The first-order operator's ‖A‖ agrees relatively within 1.2×10⁻¹³ (C2a, D7 and sample 170), 3.9×10⁻¹¹ (C2b, D7) and 1.2×10⁻⁹ (C3, D7), and exactly for the `R5` control. Samples 160 and 161 saved no ‖A‖, but they are read for type and indices only.
- **The convention.** D7's `slow` lists each typed eigenvalue with |λ| < 1, imaginary parts for C2a and C2b, real parts for C3, one value per eigenvalue. The `R5` control's `slow` does the same.
  - The dry run's points, and sample 170, hold groups, one per orbit, outside the gray zone, each with its size. So E6 counts each group with its multiplicity. For example, C3's slow real triple is one group of size 3 in the dry run and three values in D7.
  - The reader as built did not count multiplicity. That changes the reader, not E6's criterion.

Next: the reader as UB's item 4 and UA's conditions state it; UB's docstring texts; the scoring run with its arm.

## 250. 2026-10-18T02:05:02Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `6e40f50b7487368ceb9fd580ac0360a6ea15ab4cbdee461e608a3af7ac3db544`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `9f9968f3808de36e3b16c742464d5c128fd94e5bfbfb97bb010ac30b802a0e0d`, kept as `dev/runs/250_test_guard.out`

The guard's tests: PASS, 52 of 52.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 251. 2026-10-18T02:05:02Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `1cdb94d753999fe94f56fa8b2aee8f61ee22b44bd2918024ce7aee48597e9ae7`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `6be785575017dbbd0a7e5f7b61fa661714422145cc52ac866a4394a75397ede7`, kept as `dev/runs/251_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 252. 2026-10-18T02:05:03Z: run `run/score_dry.py` (case: dryrun)

Script SHA-256 `aac99e2702f2fdfde020732f0b8959b69fc0a860a15cba09e43d3bcd179b815d`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/score_dry.out` `dd66aaa4edc5725844cc9d93c1e239549605ad68e0af6b582d2d5eef25587462`, kept as `dev/runs/252_score_dry.out`

The dry run's claims scored from entry 245's kept outputs, no solve: the scoring's checks PASS (0 failed); the dry run's claims {'E1': True, 'E2': True, 'E3': True, 'E4': True, 'E5': True, 'E6': True}: PASS.
Each claim derived before the run (the script's docstring).

## 253. 2026-10-18T02:05:58Z: two scripts read the newest kept dry-run outputs, not entry 218's; found by the claims test's output, recorded before any correction

- **What reads them.** `run/test_claims.py`'s `kept()` and `dev/set_order.py`'s C2a readings take the newest `*_dry_*` files in `dev/runs`. Both were written for entry 218's outputs: the stopped run, and the ε = 2 reading that the set rule's order turned.
- **What changed.** Entry 245 kept the rerun's outputs under the same pattern, so both scripts now read those instead.
- **The claims test.** Its run in entry 251 read `245_dry_C2a.json` and the rerun's log and gate record. It still passed, because it keeps only C1 and C2a itself. Its output differs from entry 236's only in the file it names.
- **`set_order.py`** has not run since then. Its claims 2 and 3 describe entry 218's ε = 2 reading.

Next: pin both to entry 218's kept files, then rerun the claims test and `set_order.py` on C2a, against entries 236 and 220.

## 254. 2026-10-18T02:06:23Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `77106a40d50b5f80136b996c4f09bdcf82e9764e2881de4cba7f23d88ccec49e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/254_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 255. 2026-10-18T02:06:32Z: run `dev/set_order.py` (case: C2a)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a.out` `825eb531bfd181be20eb740eb298551cb4c608b602d7b0ed028adf3e9ad263c4`, kept as `dev/runs/255_set_order_C2a.out`

The separation rule read in any order of the groups, on C2a's saved summaries: PASS (0 failed), 25 readings, 24 shuffles each. Under the arm, the shuffles turn 3. No solve.
Each claim derived before the run (the script's docstring).

## 256. 2026-10-18T02:06:45Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ff7bb1501ea2de1e973975043270badf7a40d45cf59136ab9de8d028fab861c6`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `d476a2409cc7b6c7e188b234aa1160d1fa66f758672f28f713ba11372d398d60`
- `instrument/branches.py` `397a097c3c97a6d6bebc92a78e6be9879b9e1b27997a4ca6dff6808aa0609c87`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `a372aaf9bb552f67ede0776e6be6d8efbf3ebfd9fb8b4fb7dbd2911956d32564`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3.out` `e38f4ac47837a7055577387be36e5192791a65e613561e05555d02bf13e72457`, kept as `dev/runs/256_test_k3.out`

K3's overlap: PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 257. 2026-10-18T02:07:23Z: E6 scored from the rerun's kept outputs: the dry run's six claims hold; the claims test and the order test pinned to entry 218; K3's claim 2 passes

**Built (entries 248 and 249).**
- `run/driver.py`:
  - E6's references are pinned in `E6_REFS`: samples 170, 160, 161 and 201 for the type and the indices; samples 170 and 201, and D7's records 70 and 71, for the slow eigenvalues, read in each case's class.
  - Each group counts with its multiplicity on both sides.
  - The registered tolerance governs, and the dry run record's own margin is reported beside it.
  - A reference without the field it is read for gives "not evaluated", never an exception.
  - UB's two docstring texts, with E6's adapted to UA's condition 3. The old reader, `dev_points`, is gone. E5's comparison is unchanged.
- `run/score_dry.py` is new: the scoring, with UB's arm.

**The runs.**
- Unlogged first: the hash checks, the field checks and the arm, with no E6 comparison made, so E6's outcome was first read in its logged run.
- The guard's tests (entry 250): PASS, 52 of 52, byte-identical to entry 235.
- **The scoring (entry 252): PASS, 0 failed.**
  - Entry 245's 13 kept outputs equal that entry's hashes and the run's log's. The 6 references equal the outputs their entries logged.
  - The claims code raises nothing, and E1 to E5 equal the run's own lines character for character.
  - E6 is evaluated, and is True at 39 overlapping points: the type and the indices at 39, and every slow eigenvalue within the larger margin of the two records at 39. The largest difference is 4.8×10⁻⁹. Beside it, against D7, every value lies within the dry run record's own margin, at 18 of 18 points.
  - The arm, C2b's D7 values removed at N = 32, ε = 2: E6 reads not evaluated, the entry reads FAIL, and nothing raises.
  - **So E1 to E6 all hold, and the dry run passes its six claims.** Entry 245's failed attempt stays on record.
- The claims test's run in entry 251 read the rerun's outputs (entry 253). Pinned to entry 218's, it reruns byte-identical to entries 223 and 236 (entry 254).
- `set_order.py` on C2a, pinned the same way (entry 255), is byte-identical to entry 220.
- **K3's claim 2 (entry 256): PASS.** At C2a's and C3's six points, at ε = 0.25 and every cutoff, `checks.k3_spans` and `checks.static_overlap` equal M8.15.x's functions at MIT `2c27cea` to 4.7×10⁻¹⁷. The overlaps there are near 10⁻¹², so this compares near-zero values. Claim 1's synthetic vector carries the test at order one.

**Hashes:**
- `run/driver.py` `db7bf84c754f1dbf1aae186d3be6bd0a085fc3e00185af934612776832c0bd31`
- `run/score_dry.py` `aac99e2702f2fdfde020732f0b8959b69fc0a860a15cba09e43d3bcd179b815d`
- `run/test_claims.py` `77106a40d50b5f80136b996c4f09bdcf82e9764e2881de4cba7f23d88ccec49e`
- `dev/set_order.py` `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`

Next: the packet to the units, step 3's dry run for their review; then the terms v4.

## 258. 2026-10-18T02:23:16Z: the units on step 3's v2 packet: both CONFIRM, and step 3's dry run is closed; GO on the terms v4 once UB's items 5 and 6 are built

**UA (F1):**
- **CONFIRM** the v2 packet. Step 3's dry run is CLOSED, as the closure of a development dry run, not a retroactive qualification.
- UA independently reran the scoring (E1 to E5, 5 of 5; E6 at 39 of 39 points, the largest difference 4.8×10⁻⁹; against D7, 18 of 18), the arm, the guard's tests (52 of 52), the claims test and the C2a order test.
- **The two `-O` guards** flagged in entry 234 are fixed before the freeze, each with a negative test under `-O`. This does not hold up drafting.
- **GO to draft the terms v4.** They keep the failed dry run's history, the corrected set closure, the `R5` development evidence and its registration role, the measured costs, and the order of the freeze.
- The freeze and the filing are not authorized, and the sealed cases stay sealed.

**UB:**
- **Reproduced:**
  - 14 of the 15 diffs. `driver.log`'s differs only in a local path inside entry 218's traceback.
  - Entry 218's archive, byte-identical to UB's step 3 v1 copies.
  - `score_dry.py`, `test_guard.py`, `test_claims.py` and `set_order.py C2a`, byte-identical. `test_k3.py` gives the same verdicts, to round-off.
  - E6 against D7 with UB's own reader: the largest difference is 4.75×10⁻⁹ (C3), about 1% of the dry run record's margin; C2b's is 2.5×10⁻¹⁰.
  - The merged closure on the rerun's own readings: 22 readings as shipped, and under 2,200 shuffles no verdict or row changed.
- **KEEP:** the resume and the stop's record; entries 245 to 247; E6, so step 3's dry run closes; the pinning fix.
- **CHANGE, FIXABLE, item 5:** K3 at order one, with a guard for a degenerate axis.
  - C2a's axis rotation lies in the fibre span. `k3_spans` still turns the round-off into a Z, and M8.15.x's `real_orthonormal` would do the same.
  - At the pyramid's seed, about 0.987 of the axis rotation lies outside the fibre span (UB), so the pyramid is safe, but nothing checks it.
  - So `k3_spans` reports ‖P_R z‖/‖z‖, and below 10⁻⁶, Q_Z is undefined and (c) reads failed, with that reason.
  - `test_k3.py` reads C3's points at order one in both implementations, with C2a's as the arm. E2 is checked again from the kept outputs.
  - The plan's K3 bullet gains UB's text, and the terms v4 carry it in K3(c).
- **CHANGE, FIXABLE, item 6:** the `-O` gaps, now.
  - `require` refuses under `-O`.
  - These guards raise on their own: `basis.py`'s `R0` guard, `branches.expected_v0`'s two pin checks, `log_run`'s kept-output check and the driver's embedding check.
  - The tests: `require` under `-O`, beside the `assert` arm, and each converted guard against its own mutation.
- **GO on the terms v4** once items 5 and 6 are built. Their tests take seconds, the regression should come out byte-identical, and the dry run needs no rerun: item 6 changes no computation, and item 5 adds one reported number and one failure reason, checked on the kept arrays.

**Verified at source, on entry 245's kept arrays:**
- **C2a:** ‖P_R z‖/‖z‖ is 7.0×10⁻²⁵, 6.5×10⁻²⁵ and 2.3×10⁻²⁵ at N = 16, 24 and 32. `z` equals T_zφ. With Z formed from that round-off, T_xφ reads XY 0.27, 0.42 and 0.78, and T_zφ reads (0, 0).
- **C3:** the part outside is 1.00 at every cutoff. T_xφ and T_yφ read (XY 1, Z 0), and T_zφ reads (XY 0, Z 1).
- **The pyramid's 0.987** is UB's figure, not recomputed here. A computation at the pyramid's seed beyond amendment 2's three quantities would widen the seal's exception.
- **The `assert`s UB names** are where it says. The other `assert`s in `branches.py` check a seed's own consistency, and the refusal under `-O` in `require` covers them.

**The units agree.** Next: build items 5 and 6, run their tests and the regression, check E2 again, then draft the terms v4.

## 259. 2026-10-18T02:28:34Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `3c2e2b2d0e6155fd43a73539d1d4557242fce7edba740df864c5e9884db4566d`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `e7769170904277e74f59a47bcdc7e4414b9a1a2860d5bc390cf6456d44732e45`, kept as `dev/runs/259_test_guard.out`

The guard's tests: PASS, 66 of 66.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 260. 2026-10-18T02:28:35Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `f04a7f0cf3424b53fd3c9e97ef103473fc36947fe81d23e36875705f3af316e1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3.out` `ddb98836526abf9ad2c7791b0ca6e0a07448469c1b7d652482ca25cd89972f57`, kept as `dev/runs/260_test_k3.out`

K3's overlap: PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 261. 2026-10-18T02:28:35Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `f04a7f0cf3424b53fd3c9e97ef103473fc36947fe81d23e36875705f3af316e1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `2d45398e3f56dc07951865d546132fcff6da18521ad2988d1a157032455e1105`, kept as `dev/runs/261_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 262. 2026-10-18T02:28:36Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `77106a40d50b5f80136b996c4f09bdcf82e9764e2881de4cba7f23d88ccec49e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/262_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 263. 2026-10-18T02:28:36Z: run `run/score_dry.py` (case: dryrun)

Script SHA-256 `aac99e2702f2fdfde020732f0b8959b69fc0a860a15cba09e43d3bcd179b815d`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/score_dry.out` `dd66aaa4edc5725844cc9d93c1e239549605ad68e0af6b582d2d5eef25587462`, kept as `dev/runs/263_score_dry.out`

The dry run's claims scored from entry 245's kept outputs, no solve: the scoring's checks PASS (0 failed); the dry run's claims {'E1': True, 'E2': True, 'E3': True, 'E4': True, 'E5': True, 'E6': True}: PASS.
Each claim derived before the run (the script's docstring).

## 264. 2026-10-18T02:28:37Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/264_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 265. 2026-10-18T02:28:40Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/265_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 266. 2026-10-18T02:28:44Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/266_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 267. 2026-10-18T02:28:44Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `bcd171e4c06b5e3ae8c5dfa846c52e179962bdd832c0c55207d42cf21d7603dc`, kept as `dev/runs/267_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 20 of 20 verdicts as shipped and 1 of 1 changed as named; under the arm, 21 of 21 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 268. 2026-10-18T02:28:44Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `43aa6f49cb647fa88732d6b7756baa1fe1dd91099165b127d5e9ad33c2986a40`, kept as `dev/runs/268_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped and 0 of 0 changed as named; under the arm, 20 of 20 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 269. 2026-10-18T02:28:46Z: run `dev/seed_check.py` (case: seedcheck)

Script SHA-256 `b6acf0149ab3b4cd932586e4289d6e8180459d2c8148c03706fd3930ef815501`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/seed_check.out` `e452a4571d816f7ef0c762691f058bd1262cc26239fdafb56e27f263162ba715`, kept as `dev/runs/269_seed_check.out`

Step 1, the seeds: PASS (0 failed); 15 seeds at N = 16, 10 sealed, each evaluated only for Q(u), criticality and (k, r_u).
Each outcome derived before the run (the script's docstring); expected values read from the Soft-Slot Branches' section IV at the page commit instrument/certified.py records.

## 270. 2026-10-18T02:28:55Z: run `dev/set_order.py` (case: C2a)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a.out` `825eb531bfd181be20eb740eb298551cb4c608b602d7b0ed028adf3e9ad263c4`, kept as `dev/runs/270_set_order_C2a.out`

The separation rule read in any order of the groups, on C2a's saved summaries: PASS (0 failed), 25 readings, 24 shuffles each. Under the arm, the shuffles turn 3. No solve.
Each claim derived before the run (the script's docstring).

## 271. 2026-10-18T02:28:57Z: run `dev/set_order.py` (case: C2b)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2b.out` `fd5024c50ba4e98bb406419b8a3dee3f24171a422f3bf733348c114e5307c133`, kept as `dev/runs/271_set_order_C2b.out`

The separation rule read in any order of the groups, on C2b's saved summaries: PASS (0 failed), 20 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 272. 2026-10-18T02:28:59Z: run `dev/set_order.py` (case: C2a/R5)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `dcbae5a9a253e0cef16e7811bef45fe5e599bfe99174c6c186dc840909902d6c`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `684cc9f3f0cc1947bdd40410aed28c8c5ed7905f4231f75c4e2e256cd58d6689`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a_R5.out` `69c6c5b950bacacc3d9f4809907ee0d0fd782f6d2d74392c27d740566d45002b`, kept as `dev/runs/272_set_order_C2a_R5.out`

The separation rule read in any order of the groups, on C2a/R5's saved summaries: PASS (0 failed), 4 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 273. 2026-10-18T02:30:08Z: UB's items 5 and 6 built: K3's degenerate-axis guard, and every `-O` gap closed; the guard's tests 66 of 66, K3's five claims pass, E2 holds, the regression identical

**Built (entry 258).**
- **Item 5 (UB):**
  - `checks.k3_spans` also returns ‖P_R z‖/‖z‖, and below `AXIS_MIN` = 10⁻⁶ it returns no spans.
  - `checks.k3_overlaps` forms K3's (c) record, with the reason where Q_Z is undefined, and the driver now uses it. `checks.k3` fails (c) with that reason (`c_why`).
  - `test_k3.py`:
    - claim 2 now reads C3's points only, since C2a's Q_Z is undefined;
    - claim 3 reads C3's points at order one in both implementations;
    - claim 4 is the arm, on C2a's points;
    - claim 5 checks E2 again from the kept outputs.
    - Claims 2 to 5 read entry 245's kept files, each checked against that entry's hash.
- **Item 6 (UB, with UA's two):**
  - `devtools.require` refuses under `python -O`.
  - `basis.py`'s `R0` guard, `branches.expected_v0`'s two pin checks, `log_run`'s kept-output check and the driver's embedding check raise on their own, in UB's texts.
  - Mine, for the embedding check: it moved into `driver.embeds`, so its own mutation can be tested without a solve, and its message names the cutoffs it compares rather than 24 and 32.
  - `test_guard.py` gains test 11.
- **`DRIVER_PLAN.md` v4:** UB's K3 text, with two changes of mine. Claim 2 reads C3's points, and the pyramid's 0.987 is marked as UB's figure, not recomputed, since the seed is sealed. The guard list gains the `-O` tests.

**The runs.**
- Unlogged first, on temporary trees and the kept arrays: test 11, 14 of 14, and K3's claims 1 to 5.
- **The guard's tests (entry 259): PASS, 66 of 66.** Against entry 250, the output differs as derived: the plan's version, and test 11.
- **K3 (entry 260): PASS, 5 of 5.**
  - Claim 2: at C3's 3 points, the two implementations agree to 4.7×10⁻¹⁷.
  - Claim 3: at C3's points, T_xφ and T_yφ read (1, 0) and T_zφ (0, 1), in both implementations, to 6.7×10⁻¹⁶.
  - Claim 4: at C2a's points, ‖P_R z‖/‖z‖ is 6.9×10⁻²⁵, 6.5×10⁻²⁵ and 2.3×10⁻²⁵, so Q_Z is undefined, with the reason. M8.15.x's functions, without a guard, read T_xφ's XY as 0.27, 0.42 and 0.78.
  - Claim 5: K3 on C2a, its overlaps recomputed under the guard, reads "not resolved, kernel exact". (b) holds at no cutoff, and (c) fails with its reason at 3 of 3. With the kept K5 code paths, E2 holds.
- **Byte-identical to their previous runs:**
  - K3's synthetic claim (entry 261 against 243);
  - the claims test (262 against 254);
  - the scoring (263 against 252);
  - DL, `dl_recal`, the separation claims, both re-reads and the seed check (264 to 269 against 237 to 242);
  - the order tests (270 to 272 against 255, 221 and 222).

**Hashes:**
- `run/checks.py` `583a2c41ebaf358b8d6d78c0109c7b9be98e9db04c25b54f4691d749a7214b68`
- `run/driver.py` `09abcaa558a4076f7680a8c1783029da4c59f92240d3be0a5507cbe45eb6bdc8`
- `run/test_guard.py` `3c2e2b2d0e6155fd43a73539d1d4557242fce7edba740df864c5e9884db4566d`
- `run/test_k3.py` `f04a7f0cf3424b53fd3c9e97ef103473fc36947fe81d23e36875705f3af316e1`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `DRIVER_PLAN.md` `c7cbb9e33a13d91ef6ef42ac2959107dd7536adf8c60436c0cdf05a950510bbb`

Next: the terms v4, on both units' GO.

## 274. 2026-10-18T02:41:53Z: the terms v4 drafted: steps 1 to 3 folded in, with the units' items; 7,999 words

**Built** by `registration/fill_terms.py` from the source, at 7,999 words, against the cap of about 8,000. v3 had 7,832.

**What v4 carries**, each item from the units' rulings (entries 234, 258 and those they cite):
- **Amendment 4.** C2a/R5 appears in the cases (`Q` = 2289/2288, `(0, 0, 10)`, `(3, 1)`, `V₀` 4 with ranks 1 and 0, Elliptic), in K4, in the run's order, in the verdict, in the limits, in the frozen values and in the cost. Its K1 and K4 gate the `R5` rows only, and never stop the run. The allowlist holds 15 cases.
- **The merged closure,** in the set rule.
- **The dry run's history.** The failures on record gain it, and BEFORE THE FREEZE, now written as done, gives steps 1 to 3's outcomes:
  - the seeds: 15, 10 of them sealed; `Q(u)` within 3.2×10⁻¹⁵; criticality within 1.1×10⁻¹⁵; the Condon–Shortley convention exact, so the representatives' paragraph states it;
  - `R5`'s coherent sample;
  - the driver, with its dry run's two failures and its close.
- **The run:** the stop's record (NOT QUALIFIED, naming the failing check) and the resume.
- **K3(c)'s axis guard** (UB's item 5). The pyramid's 0.987 is given as a review unit's figure, not recomputed, since the seed is sealed.
- **FIXED AT THE FREEZE:**
  - UB's freeze order, verbatim (item 13);
  - `FROZEN.json`'s pin, and both pins in the freeze block;
  - the target records, copied after the go only if each blob id matches;
  - the refusals: `python -O`, a pin mismatch, and a resume on a changed tree or past a stop.
- **The cost, with `R5` measured** (UA: the measured costs):
  - `R5` costs 1.3 to 1.6 times `R4` per point. That is its coherent branch's development sample against `R4`'s samples, and the dry run's C2a/R5 against its `R4` controls; v3 scaled it at 2.5.
  - C2a/R5 has its own row. The `R5` rows and the total are ranges: 13.6 to 15.2 h, where v3 had 18.2.
  - The dry run's controls' phase took 1.2 h.

**The trims, to the cap.** They change wording only; no criterion, value or check changed:
- The preamble no longer repeats § The split's list, and the question no longer repeats Standing's order.
- "Not the census run" is compressed, and "Records" is dropped, since DEFINITION OF DONE carries it.
- The seal's rationale and the rigid slot's alternatives are dropped; BOUNDARY.md carries both.
- D1 to D5 and DL are merged; the basis's canonical fixing, "Why 10⁻¹⁵", the separation list, the C2 reading, C1's exception, "Why 2", the interruption and the cost are all tightened.
- The sources table's last row is dropped.
- The two-weight convention sentence goes, since the convention is now fixed.

**`fill_terms.py`:** `R5` is measured from the two ratios, as above. The new placeholders are `H_R5C`, `R5_LO`, `R5_HI` and `DRY_CTRL`, and `H_S5`, `H_L5` and `H_TOT` are now ranges. As before, each build prints the run files it read. This build read:
- `dev/runs/103_d7_ladders_C2b.json` `0119130f1d214e80fdff9e98a6f677fa9199a6e1fdfc476e893408a4dd5a2559`
- `dev/runs/104_d7_ladders_C2a.json` `aa2a1d9113840abbf0258c36d676f204a7186edeaaa3aabb85efcd58aea14c98`
- `dev/runs/105_d7_ladders_C3.json` `a345bc094dba35c609063e97bb8e3fb611e52b9b245305ddbfad614731417997`
- `dev/runs/118_d6_theoremD_N16_24_32_40.out` `0f623fb8b2d1e1c75e040d1b2b7b6d6d4272c8e7d83ef2eb3e40949f5031bbff`
- `dev/runs/160_sep_controls_C2b_sample.json` `d3a26a78fcc5462db13865d406d82206fd31c6bb193649eadd5e1ef3680a9c97`
- `dev/runs/161_sep_controls_C3_sample.json` `5795afe041e07e45633220ee7a2776c2af48d20cbbab826e4450d1a5a275870f`
- `dev/runs/164_sep_controls_C3_ladders.json` `14f61fd4df89b77c5c9574b2448e2fe796fe4cda53f8172f9a30b8d9451e2ce1`
- `dev/runs/170_sep_controls_C2a_sample.json` `8a1031c7d4a86369e8c53666014d29cb5e445bc30e5ba39f9e871366c20f6bdb`
- `dev/runs/171_sep_controls_C2a_ladders.json` `b555798831a10d3ea78d76018c6e2e13d40d84db4752101c5c650a70ca2d0660`
- `dev/runs/172_sep_controls_C2b_ladders.json` `7d018ae77cbb2868b45f0522ee8934f74f1603c05a74a9502636f8ff3f537a6a`
- `dev/runs/201_r5_control.json` `1f350110995238799cd598f9c6da52e5fad17190a8dcad70596bdb11be03831c`
- `dev/runs/245_dry_C1.json` `25d849d6cd9be6afb902b4db36788695f8d23342b7f9655ec5a850dd7055e481`
- `dev/runs/245_dry_C2a.json` `4a045372a34a4b969f95c42754fa0610cc5faf37f00f55d9f92d27b076c0abe3`
- `dev/runs/245_dry_C2a_R5.json` `85e367c717b9c5b4413db618dfa2161270abb6eaffa3fc26f2e2b1b9ddd3df3c`
- `dev/runs/245_dry_C2b.json` `01887c84a2ee63556b9e63950d39b05ed96d00ecb05891da18c36dbf98878809`
- `dev/runs/245_dry_C3.json` `f3c2e2e41ad64e167261dfe965c01e62457832dd75edffff941fc43df5520144`

**The rates, as printed:** `rates (s per point, N 16/24/32): {'samp': {'C2a': 361, 'C2b': 152, 'C3': 470}, 'lad': {'C2a': 330, 'C2b': 149, 'C3': 470}, 'c1': 941.6, 'r5_dev': 1.3, 'r5_dry': 1.63, 'dry': {'C1': 709, 'C2a': 800, 'C2b': 339, 'C3': 1086, 'C2a_R5': 1540}}`

**Hashes:**
- `registration/m8_16_task_details.src.md` `45833ad7c65e63a2b9bccecdf03f10cff6a5d005052a451e8f60fe101cc75735`
- `registration/m8_16_task_details.md` `4f88bb5559e41b4cf3ddb9e9358428f962710e6e2df15a86b70622789fc40a6f`
- `registration/fill_terms.py` `2117d76be37b7dd0ec7eb6692b6995ead653944bb135722e2070792de9b5572b`

Next: the units' final pre-freeze review of v4, with the instrument as entry 273 left it. The freeze and the filing wait for Blake's go and the maintainer's.

## 275. 2026-10-18T02:58:12Z: the units on the terms v4: both confirm v4 as the text to freeze, once two text changes are in

**UA (F1): CONDITIONAL CONFIRM.**
- **Confirmed:** K3's axis guard; the `-O` safeguards; the `R5` control and its row gate; the merged closure; the freeze order and the manifest's integrity.
- **Reran independently:** the guard's tests (66 of 66), K3's synthetic check, and the scoring (E1 to E6). UA also reran the cost calculation on its archived inputs, getting 1.30 to 1.63 and 13.6 to 15.2 h; that is an estimate, not a guarantee.
- **Checked from the archive, not rerun:** K3's comparison with M8.15.x's functions, from its output and source.
- **The word count:** 7,999, with no placeholder left.
- **One required change:** the heading "Before any target: a failure stops the run, and no target runs" contradicts amendment 4. UA's wording: "Before any target: global controls stop; R5 gates its rows only".
- **The protections, confirmed intact:**
  - the seal;
  - K3 unchanged;
  - no credit for development;
  - both of the dry run's failures documented;
  - the `R5` gate on its rows only;
  - no repair-and-rerun;
  - the census pre-registration's wait;
  - #512's boundary.
- **Found:** no sealed solve or scored run in the package.
- **The ruling:** with the heading corrected, rebuild, log the new SHA-256, and keep those bytes as the definitive text. No further review or rerun is needed. After UB's approval and Blake's authorization, UA supports the registered order.

**UB: CONFIRM, once items 5 and 6 are in.**
- **Reproduced:** the 14 diffs; `test_guard.py` (66 of 66) and `score_dry.py`, byte-identical; `test_k3.py`, 5 of 5, to round-off. UB rebuilt v4 from the source with its own clones, byte-identical to entry 274's hash, and read the full diff, 317 lines.
- **KEEP:**
  - items 5 and 6, and the `driver.embeds` move;
  - the items carried, and BEFORE THE FREEZE's figures, which match the outputs;
  - every trim, as wording only;
  - the cost's method.
- **The pyramid's 0.987.** It comes from the Result's coefficients alone: at the seed `√12 v₃ + √13 v₋₂`, T_zφ's component along iφ is 10/(5√160) = 0.158, which leaves 0.987 outside it. The instrument computed nothing at the seed.
- **CHANGE 5:** K3(c) should state the projection the code applies, since read literally "`T_zφ`" is the raw tangent. UB gives a replacement for the whole bullet.
- **CHANGE 6:** the same heading, with UB's wording: "Before any target: a failure stops the run, and no target runs (C2a/R5's gates the `R5` rows only)".
- **On the cost:** the table is on the high side. The dry run's rates were 0.55 to 0.75 of development's, so at those rates the whole run takes about 8 to 9 h. The text needs no change, since it already reports the dry run's 1.2 h.
- **Item 9, for step 2:** the manifest pin covers the filed terms' bytes in `run/`. If the pull request's review changes any word, the terms' hash and the manifest pin are both redone and republished on MIT `main` before the go.

**Verified at source:**
- UB's 0.987 is arithmetic on the published representative: cos = 0.1581 against iφ, and √(1 − cos²) = 0.9874. That is the part outside iφ alone; the instrument's ‖P_R z‖ also removes the phase partner, which needs `L` at the seed. So the text says "near 0.987", as a review unit's figure from the coefficients.
- UB's (c) text matches `checks.k3_spans`:
  - the fibre and the partner are projected out of the rotation span;
  - Z is T_zφ's projection into it, and XY its complement;
  - the guard is ‖P_R z‖/‖z‖ below 10⁻⁶.

**Adjudication of the heading.** Both units ask for the same correction. UB's wording is adopted, because it names the case as the text does everywhere else; "global controls" and "R5 gates" are not terms the text defines. UA's correction is met in substance.

Next: both changes in the source, a rebuild, and the new SHA-256 and word count to the units; then the freeze's steps, each on Blake's go.

## 276. 2026-10-18T02:58:57Z: the text to freeze: the terms v4 with the units' two changes; 8,009 words

**The changes (entry 275),** each in UB's text, in the source, then rebuilt:
- The heading under THE CHECKS now reads: "Before any target: a failure stops the run, and no target runs (C2a/R5's gates the `R5` rows only)". This is UA's correction, in UB's wording (the adjudication is in entry 275).
- K3(c) now states the projection the code applies:
  - both spans are taken inside the rotation span, with `iφ` and the phase partner's static part projected out;
  - the overlap is M8.15.x's registered `verdict.static_overlap`;
  - below 10⁻⁶ of ‖T_zφ‖, the projection is undefined and (c) fails;
  - a review unit, from the Result's coefficients alone, puts the fraction near 0.987 at the sealed seed.

**The rebuild.** The built text differs from entry 274's build in those two lines alone; the build read the same commits. It has 8,009 words, stated as about 8,000, with no placeholder and no em-dash. Entry 274's build hashed to the SHA-256 that entry records, and those bytes stay in the scratchpad's record of this session.

**The definitive registration text, as the units asked:**
- `registration/m8_16_task_details.md` `34ca2ff29400770b6c207f738d9d5ea38da1d74a6b8aa0b83e7ec601e1dd59fc`
- `registration/m8_16_task_details.src.md` `dd8ab257a3d4bc9e728b634714d971b4fdea2e21862434164ac559972f25cc56`
- `registration/fill_terms.py` `2117d76be37b7dd0ec7eb6692b6995ead653944bb135722e2070792de9b5572b`, unchanged since entry 274

**For step 2 (UB's item 9).** `run/` will hold these bytes, so the manifest pin covers them. If the pull request's review changes any word, the terms' hash and the manifest pin are both redone and republished on MIT `main` before the go.

Next: the units' one-minute check of the two hunks; then the freeze's steps, each on Blake's go.

## 277. 2026-10-18T03:10:34Z: the units on entry 276's text: UB confirms it; UA confirms K3(c) and asks for its own heading; adopted, reversing entry 275's choice

**UB: CONFIRM.** UB rebuilt the text itself rather than reading the two lines. Starting from its copy of v4's first source, UB applied the two texts and rebuilt with its own MIT and OpenWave clones:
- the source matched, `dd8ab257…`;
- the built terms matched, `34ca2ff2…`, with 8,009 words;
- exactly two lines differ from v4's first build.

UB's record names entry 276's built hash as the text to freeze, and item 9 as logged correctly.

**UA: K3(c) CONFIRM; the heading, CONDITIONAL.** UA has two objections to the heading:
- it still says any failure stops the run, which contradicts its own exception;
- `C2a/R5's` is a stray possessive.

UA's wording: "Before any target: global-control failures stop the run; C2a/R5 gates `R5` rows only". With that change, rebuild and log the final hashes. No further technical review or test is needed, and UA supports the filing sequence once UB concurs.

**Adjudication.** UA's wording is adopted, reversing entry 275's choice of UB's.
- UA's new point holds. The main clause reads as universal before its parenthesis qualifies it, and the elliptical possessive is unclear in a heading.
- UA's two clauses state the rule and its exception plainly.
- Entry 275 preferred UB's wording because it uses the text's own terms. "Global-control" is a coinage, but the second clause defines it by contrast.
- The change touches one heading and no criterion. By UB's item 9 it changes the hash, so UB's concurrence on the new hash is needed.

Next: the heading in the source, a rebuild, the final hashes logged, and both units' concurrence.

## 278. 2026-10-18T03:10:54Z: the text to freeze, final: UA's heading in; 8,004 words

**The change (entry 277).** The heading under THE CHECKS now reads: "Before any target: global-control failures stop the run; C2a/R5 gates `R5` rows only", in UA's text. It changes no criterion.

**The rebuild.** The built text differs from entry 276's, which hashed to the SHA-256 that entry records, in that one line alone. It has 8,004 words, stated as about 8,000, with no placeholder and no em-dash.

**The definitive registration text:**
- `registration/m8_16_task_details.md` `d497359eb988ffedf80e866a121cb06734684ed8b5ee670a127d5267af5e8096`
- `registration/m8_16_task_details.src.md` `ebc42d6507e325554cf2917cfbbd6164983d70ccc152ebc51f78e3f147d8aa2f`
- `registration/fill_terms.py` `2117d76be37b7dd0ec7eb6692b6995ead653944bb135722e2070792de9b5572b`, unchanged

UB's item 9 stands for step 2.

Next: UB's concurrence on this hash, with UA's condition met; then the freeze's steps, each on Blake's go.

## 279. 2026-10-18T03:36:59Z: both units confirm the terms v4 for the freeze, at entry 278's hash

**UB: CONFIRM**, on the built terms at `d497359e…` as the text to freeze.
- UB applied the new heading to the source it had confirmed and rebuilt from its own clones. Both hashes match: the source at `ebc42d65…` and the built terms at `d497359e…`, at 8,004 words.
- The only difference from the text UB confirmed is the heading line.
- UA's wording reads better: it no longer opens with a claim that sounds universal. "Global-control" appears only in that heading, and THE RUN names exactly which failures stop the run, so it reads correctly in context.

**UA (F1): FINAL RULING, CONFIRM v4 for the freeze.**
- The wording passes, and the scope and the budget are unchanged, at 8,004 words. No F1 objection is outstanding.
- UA accepts the reported one-line change and hashes without recomputing them.
- Pending UB's concurrence, now given, and Blake's authorization, UA gives GO to the filing sequence. No further edit or development is requested.

**The text to freeze** is `registration/m8_16_task_details.md` at the SHA-256 entry 278 records.

Next, on Blake's go, step 1. The filed terms go into `run/` first, because the manifest pin covers them (UB's item 9). Then `pin_manifest.py`, then the solver commit, the manifest pin and the terms' hash on MIT `main`.

## 280. 2026-10-18T04:11:52Z: the units on the step-1 plan: GO on steps 1 to 7, stopping at a local commit; the push a separate go

**The plan,** put to Blake after entry 279:
1. the environment record, `run/ENVIRONMENT.json`, so that the manifest records the environment, as the terms say it does, with no word of the terms changed;
2. the terms into `run/`;
3. the pin;
4. the MIT folder, `scripts/soft-slot-dynamics-m8-16/`: the bench as it stands, about 49 MB, without `run/dry` and caches;
5. the checks;
6. the census note;
7. one commit, stopping before the push.

The terms' sentence, "The manifest records the environment", named the right values, read on this machine; but the built manifest hashes files only, and nothing recorded the environment.

**UA (F1): GO** on the full folder, the environment record, and steps 1 to 7 through the local commit. The push to `main` is a separate go; the sealed qualification stays on HOLD. Two safeguards:
- **What the pin fixes.** No manifest-covered file changes after the pin. The freeze files and outputs the manifest excludes are created later under their own checks, and the sealed target records keep their blob and hash checks. A clarification of the built design, not a change to the registration.
- **Sync before the pin.** Fast-forward first; check that the commits touch neither the destination nor the census page; then pin, copy, verify and commit against that base. If `main` advances again, review the difference rather than rebuild silently.

UA also asks that:
- the environment record hold the versions, the BLAS and LAPACK backend and the CPU, not the whole environment;
- the files be scanned before the commit for credentials, private paths beyond the disclosed ones, and caches;
- `SHA256SUMS` be generated fresh from the final inventory;
- the tests run on a scratch copy.

After the commit UA wants only the commit hash, the terms' SHA-256, the manifest pin, and the results of the file checks and the scratch tests.

**UB: GO,** with both recommendations and four checks.
- **The folder:** in full. DEVLOG cites the kept outputs by name and hash, and the definition of done files scripts, data and `REPRODUCE.md`. `REPRODUCE.md` says in one line that `run/dry` is left out, being byte-identical to `dev/runs/245_dry_*`. The machine paths in the three kept driver logs stay, since DEVLOG cites their hashes and M8.15.1 and M8.15.2 filed theirs the same way.
- **The environment record:**
  - read with the run's own `python3 -I -B`;
  - holding the Python, NumPy and SciPy versions, NumPy's BLAS and LAPACK configuration, the macOS version, since Accelerate ships with the OS, and the machine model;
  - written by exclusive create, its SHA-256 logged.

  At the run it is read again and both readings go in the freeze block. Any difference goes to the units before the run starts. UA is told of it in the step-1 note, since it touches a sentence both units confirmed.
- **Step 2:** before the copy, the registration file's SHA-256 is checked against the hash both units confirmed.
- **Step 3:** from the pin on, every test runs in a scratch copy only.
- **Step 7:** before the commit, the commits since UB's base, `origin/main` at `2c27cea`, are checked against every page and record the terms cite: the slot action, the Soft-Slot Branches, the census page, the Hamiltonian–Krein page, the slot ground states, M8.15's record, M8.15.x's qualification and the five target records. If any changed, stop and bring it to the units. The target records' blob ids at `origin/main` should still match `run/targets.json`.
- The run runs from a tree whose manifest equals the pin.

**Adopted,** both units' conditions. The recorder is `run/record_environment.py`. It writes the record once, and `--check` reads the live environment again for the freeze block.

## 281. 2026-10-18T04:12:57Z: step 1 through the pin: the sync, the scan, the environment record, the terms in `run/`, the manifest pin

Under entry 280's GO, in the order the units set.

**The sync** (UA's second safeguard; UB's step-7 check).
- The worktree stood at `787aef1662c8`, behind `origin/main` only. It was fast-forwarded to `2c27cea2d543`, which is `origin/main` and UB's base, so nothing lies after that base.
- The 10 commits change 3 files: `CONTRIBUTING.md`, `files/framework/files/dynamics/README.md`, `files/tools/README.md`.
- None is among:
  - the MIT pages the terms cite;
  - the census page;
  - M8.15's folder or M8.15.x's;
  - the destination, `scripts/soft-slot-dynamics-m8-16/`, which is absent on `main`.
- The five target records' blob ids at `origin/main` and at their named commit equal those in `run/targets.json`. No record was opened.

**The scan,** before the pin. 449 files, text and binary, the bench without `run/dry` and `.DS_Store`, were read for:
- OpenWave's local-path patterns;
- the bench's path;
- emails and personal identifiers;
- credentials;
- Claude session internals.

Hits came only in the 3 kept driver logs (`dev/runs/218_dry_driver.log`, `dev/runs/218_run_dry/driver.log`, `dev/runs/245_dry_driver.log`). They hold the bench's own paths, are disclosed and are kept as they are (UB). OpenWave's `check_no_local.py` passes the terms, reading 1 file of 1.

**The environment record.** `run/record_environment.py` `1494fb8afd942e74a646671fe16f03ad4d9b095ae62cd1be35a51b2eb3a10059` wrote `run/ENVIRONMENT.json` `69135130896341b8ba8c56cd867c2f3254fddc7e19d01734f10c31a1e49b62ca` by exclusive create, run as `python3 -I -B`. Its `--check` read the environment again and found no difference.
- **Before use,** on a scratch copy:
  - a second write was refused;
  - a record with NumPy's version and one threading variable changed failed the check, naming both;
  - unknown arguments were refused.
- **What it records:**
  - Python 3.13.13 (CPython, `3.13.13 | packaged by conda-forge | (main, Apr  8 2026, 02:29:07) [Clang 19.1.7 ]`), at `/opt/homebrew/Caskroom/miniforge/base/bin/python3`, with `-I -B` and no `-O`;
  - NumPy 2.5.0, its BLAS and LAPACK `accelerate` and `accelerate`;
  - SciPy 1.18.0, its BLAS and LAPACK `Accelerate` and `Accelerate`;
  - macOS 15.8 (24H23), kernel 24.6.0;
  - a Mac15,13, Apple M3, with 4 performance and 4 efficiency cores, arm64;
  - no threading variable set (`MKL_NUM_THREADS`, `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`).

  Each library's configuration is recorded as it reports it.

**The terms in `run/`** (UB's step 2). `registration/m8_16_task_details.md` hashes to the SHA-256 entry 278 records, the one both units confirmed. It was copied by exclusive create to `run/m8_16_task_details.md` `d497359eb988ffedf80e866a121cb06734684ed8b5ee670a127d5267af5e8096`, which equals it.

**The pin.** `run/pin_manifest.py` wrote `run/MANIFEST_PIN` by exclusive create: `00b41c591b6d2bf398783438bc565cf3ac7ad36253f1f868c7545c20c057aba2`, the manifest's SHA-256 over 36 files:
- `instrument/`;
- `reference/m815/`;
- `run/` without `run/dry`, `run/out` and the pins, its test outputs and the terms included.

The recomputed manifest equals the pin, and a second pin was refused.

From here no manifest-covered file changes (UA). Every test runs in a scratch copy only (UB). `FROZEN.json`, `FROZEN_PIN` and the run's outputs come later, under their own checks.

## 282. 2026-10-18T04:20:28Z: step 1: the MIT folder built and checked; `REPRODUCE.md`; the census note; a correction to entry 281

**The folder,** `scripts/soft-slot-dynamics-m8-16/`, in the worktree at `2c27cea2d543`, built from the bench without `run/dry/` and caches.
- **Size.** It holds 450 files, this log and `REPRODUCE.md` among them, 48.7 MB in all. The largest is `dev/runs/245_dry_C2a_ladder.json`, at 3.45 MB.
- **Against the bench.** Each file equals the bench's, byte for byte. This log is copied in again after this entry.
- **The manifest,** recomputed from the folder, equals the pin over 36 files.

**The scratch tests** (UB's step 3). A copy of the folder in a scratch directory ran the five filed tests under `python3 -I -B`, with `MIT_REPO` the worktree at `2c27cea2d543`. Each exited 0:
- `run/test_guard.py`: "0 failed of 66";
- `run/test_k3.py`: "0 failed";
- `run/test_k3.py --synthetic-only`: "0 failed";
- `run/test_claims.py`: "0 failed";
- `run/score_dry.py`: "0 of the dry run's claims failed or were not evaluated".

Each output equals the folder's, byte for byte. After the tests the copy's manifest still equals the pin, so no test wrote anything else under `run/`. Arm: on a second copy, one byte appended to `run/test_k3.out` was caught by the comparison and by the manifest alike.

A first scratch run passed the same way, but the arm was then made on its own copy. So the record is this second run, on a fresh copy, with the arm on another.

**`REPRODUCE.md`** `236c7fc489948e247bed597fb0386adc7b77ad1d40086856521c8029e2e4cd41`.
- **How it was written.** Its environment, the commit test_k3 reads, its entry numbers, the dry run's time and the terms' cost were read from the files it describes. It follows M8.15.2's.
- **Six claims made exact on review:**
  - the spectrum is read where the terms read it, not at each point;
  - the dry run's two failures are stated;
  - #512 is linked as OpenWave's;
  - caches are named among what the manifest leaves out;
  - `-O` is refused by the driver and the log, not by every script;
  - `run/dry/` and `run/out/` are excepted from the writes that change the manifest.
- **Its two checks,** run from the folder: the manifest command printed the pin, and `record_environment.py --check` found no difference.

**The census note,** § V, step 4, dated 2026-10-18. It gives the terms' SHA-256 and the pin, both read from the folder's files, and links the folder's `REPRODUCE.md`. The page's math count is unchanged. `metadata-lint.py` reports 0 FAIL and 0 WARN. The Status line stands: M8.16 is still the next step.

**Correction to entry 281.** Its scan count, 449, comes from the rescan made while writing that entry, after the pin. That rescan also read the four files step 1 added: `run/ENVIRONMENT.json`, `run/record_environment.py`, `run/m8_16_task_details.md` and `run/MANIFEST_PIN`. The scan made before the pin read 445 files, the bench as it then stood, and found the same three hits.

**Next,** in order:
1. this log copied into the folder;
2. `SHA256SUMS` generated fresh from the final inventory;
3. `shasum -c`;
4. the final folder scanned;
5. the commit.

The commit's hash and the sums' check are logged after it. The push waits for Blake's go.

## 283. 2026-10-18T04:33:24Z: step 1: the local commit `30d8991a7aea`, kept on Blake's go and verified from its own tree; the units' short look before the push

**The commit.**
- `30d8991a7aea943b63ddb03c1939fa61968ed844`, on `origin/main` at `2c27cea2d543`, which a fetch just before this entry found unmoved.
- It is 1 ahead and 0 behind, so the push would be a fast-forward. It is not pushed.
- It changes 452 files: the 451 of the new folder, and the census page's note.

**Verified from the committed tree,** extracted by `git archive`, not from the working copy:
- `shasum -a 256 -c SHA256SUMS` passes, with 450 OK and 0 other lines;
- the manifest, recomputed, equals the pin;
- the census note names the terms' SHA-256 and the pin, once each.

**Kept on Blake's go.** The commit was made on the units' GO as Blake relayed it (entry 280). Blake then confirmed it himself: "go on 1 and 2 in preparation for 3".
- **What the go covers.** Item 1 keeps the commit and logs this entry. Item 2 sends the units a short look before the push, which is item 3.
- **A review Blake relayed,** without the unit's name, agreed:
  - keep the commit;
  - log this entry on the bench only, and never amend it into the commit, which cannot contain its own hash;
  - have both units look at the four new pieces before the push makes the commit public.
- **The 36 manifest files.** The review counted 33 in its own copy, plus the three that step 1 added. They were checked against the units' last copy, the terms v4 packet's:
  - its 33 manifest files are byte-identical in the pin, with none changed or missing;
  - the 3 new ones are `run/ENVIRONMENT.json`, `run/m8_16_task_details.md`, `run/record_environment.py`;
  - with those added to that copy, its manifest equals the pin.

**What the commit carries.** The committed log ends at entry 282. This entry and any later ones stay on the bench until the next filing, the run's record.

**Next.**
1. **The units' short look** at the recorder, `ENVIRONMENT.json`, `REPRODUCE.md`, the census note and the commit's file list. A change to the recorder or the record means a new pin and a rebuilt commit, both still local.
2. **The push,** on Blake's go.
3. **Step 2,** the OpenWave branch, under UB's item 9.

## 284. 2026-10-18T04:43:51Z: the units on the step-1 packet: UA CONFIRM and GO to push on Blake's go; UB CONFIRM on three pieces, with two lines for `REPRODUCE.md` and one for the commit message, applied; the rebuilt commit waits for Blake's go

**UA (F1): CONFIRM, and GO to push, subject to Blake's explicit go.**
- **Checked from the zip:**
  - the terms' and the manifest's SHA-256;
  - the three new manifest files against their listed hashes;
  - 36 entries, 33 unchanged and 3 new;
  - the commit's 451 additions and 1 modification;
  - `SHA256SUMS`'s 450 entries;
  - both hashes in the census note.
- **CONFIRM** on the recorder, the record, `REPRODUCE.md` and the census note. The note records a freeze of the terms, not a qualification.
- **What UA could not check.** The zip does not hold all 450 summed files, so for the committed tree UA relies on the reported `git archive` check and the scratch tests.
- **Optional:** the commit's author email names this Mac's local hostname. If that is not the intended public identity, it is amended before the push, which changes the commit and not the files. Brought to Blake.

**UB: CONFIRM on the recorder, the record and the census note; two lines for `REPRODUCE.md` and one for the commit message.**
- **The pin, independently.** UB took its own v4 copy, added the terms it rebuilt and the two other new files, and recomputed the manifest. Its text equals `manifest.txt` line for line, over 36 files, and its SHA-256 is the pin.
- **`SHA256SUMS` against UB's copies.**
  - UB holds 448 of the 450 files. Each equals its reviewed copy except `DEVLOG.md`, which differs by its new entries.
  - The other two, `REPRODUCE.md` and `MANIFEST_PIN`, match the zip.
  - So nothing outside the new files has changed since the units' last review.
  - The new files' hashes equal those entry 281 logs.
- **The recorder:**
  - it reads only what its docstring lists;
  - it calls `sysctl` and `sw_vers` by fixed absolute paths, and writes once;
  - its `--check` also compares the interpreter's `-I`, `-B` and `-O` flags.
- **On UB's machine** (Linux, NumPy 2.5.3):
  - `test_guard`, `test_claims` and `score_dry` matched byte for byte;
  - `test_k3.out` differed only in the last digits of its near-zero overlaps, with the same verdicts;
  - `--check` stopped at `sw_vers`, which exists only on macOS.
- **After the rebuild** UB needs no further look. The new hash goes in a new entry; entry 283 stands as written.

**Verified at source.** `test_k3.out` prints its overlaps and differences at round-off. The recorder calls `/usr/bin/sw_vers` and `/usr/sbin/sysctl` on every reading.

**Applied, in UB's words:**
- **`REPRODUCE.md`:**
  - the byte-for-byte sentence now holds "on the recorded machine", and says that elsewhere `test_k3.out`'s near-zero overlaps can differ in their last digits, with the same verdicts;
  - the environment bullet adds "It runs on macOS only, since it reads `sw_vers` and `sysctl`." The sentence is joined to its bullet's line, as the file writes each bullet on one line, and renders as UB's text.
- **The commit message** now reads "On this machine, from a copy of this folder, the five filed tests reproduce their outputs byte for byte".

**The result.**
- `REPRODUCE.md` is now `01bd44690aa88a18656fb7feb3d9382245a0140904916d96cf9bc3276e2a96ee`.
- `SHA256SUMS`, regenerated fresh, changes in `REPRODUCE.md`'s line alone, and `shasum -c` passes. The bench's copy is updated with it.
- The pin is unchanged, since `REPRODUCE.md` lies outside the manifest.
- Against `30d8991a7aea`, the working tree differs in those two files only. The folder's `DEVLOG.md` stays as committed.

**Next, on Blake's go:**
1. the commit rebuilt from `30d8991a7aea`, with Blake's choice of its author identity (UA's point);
2. its hash logged in a new entry;
3. the push, a fast-forward.

## 285. 2026-10-18T04:47:32Z: step 1 landed: the rebuilt commit `805ddbcd240e`, verified from its own tree and pushed to MIT `main`

**The rebuild, on Blake's go.** Blake chose to keep the session identity, then to rebuild and push.
- **The commit:** `805ddbcd240ec80f988561a4d8c6718013e4048d`, rebuilt from `30d8991a7aea` with UB's lines (entry 284). Entry 283 stands as written.
- **Its base:** `origin/main` at `2c27cea2d543`, which a fetch just before the rebuild found unmoved.
- **What changed:** against `30d8991a7aea`, only `REPRODUCE.md` and `SHA256SUMS`, plus the message's one line.
- **Author and committer:** `Blake Shatto <blake@Blakes-MacBook-Air.local>`, as on the earlier session commits (UA's point; Blake's choice).
- **Size:** it changes 452 files, as before.

**Verified from the committed tree,** extracted by `git archive`:
- `shasum -c` passes, 450 OK of 450;
- the manifest equals the pin;
- the census note names the terms' SHA-256 and the pin, once each;
- `REPRODUCE.md` equals the bench's.

**The push.** `git push origin HEAD:main` was a fast-forward from `2c27cea2d543`. `ls-remote` shows `main` at the rebuilt commit.

**Live, read back through the GitHub API:**
- the census page renders 109 math elements for its 109 math spans, with the note and its link to `REPRODUCE.md`;
- `REPRODUCE.md`'s blob on `main` equals the bench's file.

**What is current.**
- MIT `main` and the worktree are at the rebuilt commit.
- Blake's main checkout is one commit behind until it pulls.
- The bench's log holds entries 283 to 285. They reach the MIT folder with the run's record.

**Next, on Blake's go: step 2, the OpenWave branch.**
- **What it holds:** the task file, byte for byte `run/m8_16_task_details.md`; its BACKLOG row; and the roadmap's two M8 status rows.
- **Who does what:** I push the branch; Blake opens the PR.
- **If review changes a word** (UB's item 9), the terms and the pin are redone and republished on MIT `main` before the maintainer's go.

## 286. 2026-10-18T04:56:01Z: step 2: the OpenWave branch pushed to the fork; Blake opens the pull request

On Blake's go ("go on step 2").

**The branch.** `m8-16-qualifying-the-harmonic-galerkin-instrument-2026-10-18`, on the fork, at `2610d727f7bf83c85e88051de23341f34d21e02e`. It sits on `upstream/main` at `50c359e9c44f` and is signed off for the DCO. It changes 2 files:
- **`tasks/m8_16_task_details.md`, new.** It is byte for byte `run/m8_16_task_details.md`. Read back raw from the fork through the API, its SHA-256 equals the pinned terms'.
- **`m8_roadmap.md`:**
  - **the BACKLOG row allocating M8.16** (`ROADMAP_STANDARDS.md` § 6). Its Description has 63 words against the cap of 65, and its Title 6 against 15, by the checker's own count;
  - **the two status rows #512's roadmap condition names.** "Where is M8?" gains M8.16 and keeps "Field dynamics has no live route", as the ruling says it stays true. "What decides the program?" no longer says nothing is pending;
  - **the snapshot's date.**

**Checks:**
- **Before branching:**
  - every link in the terms resolves, 14 distinct;
  - no upstream M8 file and no open pull request carries M8.16;
  - no M8 commit has landed since #635, so the terms' run-before-write sentence holds;
  - the recent task docs open as this one does, so no convention asks for a change to the terms' bytes.
- **On the branch:**
  - `check_roadmaps.py` is clean, and fails on an arm that adds three words to the row's Description;
  - `check_models_md.py` is clean;
  - `check_no_local.py --require-files` is clean on both files.

**The pull request's text** is `m8_16_pr_body_v1.md` in the dynamics folder, and it is on Blake's clipboard.
- **Its form:** 513 words, one line per paragraph, in the form of M8.15.2's.
- **Its links:** all resolve, MIT's at `805ddbc`.
- **Its title:** "M8.16: pre-registration for qualifying the stationary harmonic Galerkin instrument".

**Next.**
1. Blake opens the pull request against `openwave-labs/openwave` `main`.
2. The review. UB's item 9 applies to any word of the terms. Words of the roadmap rows or the pull request's text do not touch the pin.
3. The maintainer's go.
4. `write_guard.py`.
5. The freeze block, with `record_environment.py --check`'s two readings; any difference goes to the units first.
6. The run.

## 287. 2026-10-18T05:09:17Z: step 2: Blake opened the pull request, OpenWave #637

Blake opened [#637](https://github.com/openwave-labs/openwave/pull/637) at 2026-10-18T05:04:02Z. Its head is the branch entry 286 records, at `2610d727f7bf`, and its state is open.

**Next.**
1. The maintainer's review. UB's item 9 applies to any word of the terms.
2. The merge.
3. The maintainer's go.
4. `write_guard.py`.
5. The freeze block.
6. The run, on mains with sleep off.

## 288. 2026-10-18T13:56:45Z: xrodz's review of #637: changes requested, three blocking items in the frozen instrument; each verified at source

**The review** (review 5563134169, submitted 2026-10-18T13:14:04Z on `2610d727`). It is kept verbatim as `../m8_16_pr637/xrodz_review_5563134169.md`, body SHA-256 `2899414da2ccfaa8160facf81905d6a142ee2e202578c220c622592c6592ca17`.
- **What passed:** the provenance, the boundary quote, every frozen number, K6's 79 decided points, the driver's guards and the roadmap.
- **What it asks:** three blocking items, a design question that is ours to decide, and four comment-tier items.

**Verified at source:**
- **B1. K3(d) applies a location tolerance the terms do not register.** `run/checks.py`, in `k3`, requires `|row_centre(own) - c0| <= 1e-3 |c0|`. The terms' K3(d) asks only that the separation, read under THE CONVERGENCE RULE, pass, and no `10⁻³` stands there or in FROZEN VALUES.
  - The dry rerun's kept outputs give the largest relative shift of a group between `N = 16` and 32: at `ε = 0.25`, C2a 8.1e-4, C2b 8.9e-4, C3 6.4e-4 and C2a/R5 7.9e-4; at 0.5, 1.6e-3, 1.8e-3, 1.3e-3 and 1.6e-3. These equal the review's figures.
  - (d) is computed only when (b) holds, which no GO case gives, so it never ran on instrument data. `DRIVER_PLAN.md` expected it computed on C2a's smallest pair in the dry run.
- **B2. A failed seed check is not enforced on the pyramid or in K6.** The pyramid's K1 calls `k1` per point, which reads no seed, and so do its K2, `k3` and `check_pyramid_k4`. `check_row_k6` reads only acceptance. Yet the terms say a failed check ends the case as an instrument failure (Seeds), and a seed that fails its check is never scored as agreeing (the verdict rule).
- **B3. A registered failure can become a crash.** In `read_point`, K3's group is picked by `min` over the groups inside the slow band. When groups exist but none lies in the band, `min` raises `ValueError`, and no gate record or verdict is written.
- **The question on K3's outcome partition.**
  - `k1` requires `v0_matches` and `separated`. An in-span mode that stays merged at `ε = 0.25` enlarges `V₀` or lies in the gray zone, so it fails K1 and (a).
  - The record then reads "instrument failure", never "not resolved, kernel exact". So the case #512 § 1 names, and the census page's step 4, can never reach "the diagnosis is wrong".
  - The record carries the Hessian's kernel at every point (`lkernel`: the lift and the smallest genuine `|μ|` against `‖L‖`).
- **The comment tier:**
  - **The frozen driver has not run end to end.** The dry rerun (entry 245) ran driver `20d497db5ecef6dc…`, as entry 244 logged it. Entries 257 and 273 then changed it, and today's is `09abcaa558a4076f…`. The dry run reads the driver, and I did not rerun it after those edits.
  - **Three quantities the terms call "reported" are not computed:**
    - the convergence rule's change between the two highest cutoffs, against `10⁻⁶`;
    - K6's tracked slow eigenvalues beside M8.15's level-2 to level-3 change;
    - K5's per-mode deviations at 0.5, 1 and 2.
  - **The verdict's outcome string** does not carry the terms' "the diagnosis is wrong".
  - **"Every development point met it"** overstates. Entry 068's D6 run failed the residual bound, so "every accepted development point" is exact.

**What a fix moves.** Fixing B1 to B3 changes the instrument, and with it the manifest pin. A change to the terms' text also moves their hash. Both are redone and republished on MIT `main`, with a new dated note on the census page, and then pushed to #637. The go waits for that commit.

**Next.** Blake's calls: B1's form, the question on K3, and which comment-tier items to fold in. Then the fixes and their tests, the units' review, a dry rerun on the final tree, and the republication, each publishing step on Blake's go.

## 289. 2026-10-18T14:16:03Z: the revision for #637 built: B1 to B3, K3's certificate from L, the three reported readings and the outcome's sentence; tested unrecorded

On Blake's calls for entry 288's review:
- B1 by the convergence rule's own row;
- K3's kernel certificate adopted;
- all four comment-tier items taken.

B2 and B3 needed no choice.

**The changes,** against the published folder at `805ddbc`.
- **`instrument/linear.py`.** The record keeps the flag it already computed, `l_resolved`: nothing lies in `L`'s gray zone.
- **`instrument/convergence.py`:**
  - each summary group carries its eigenvalue indices;
  - each row records the eigenvalues it reads at the highest cutoff, `top`, and its relative change between the two highest cutoffs, `rel_change`;
  - no verdict reads them.
- **`run/checks.py`:**
  - **B1.** `k3_d` and `reading_row` find (d)'s row by the rule's own matching: the one tested row whose `top` holds the eigenvalues of the group (b) finds at the highest cutoff. (d) is that row's verdict. The `10⁻³` test is gone, and the unused `RATIO` with it.
  - **B2.** `seeds_ok` gates:
    - the pyramid's K1, through `check_pyramid_k1`;
    - K3(a);
    - the pyramid's K4;
    - K6, where a failed seed makes every read point invalid.
  - **B3.** `k3_pick` returns none where no group lies in the slow band, rather than raising.
  - **K3's certificate.** `kernel_exact` reads `L` alone: the point accepted, every orbit tangent with `‖L t‖ ≤ L_CUT ‖L‖ ‖t‖`, and `L`'s zero count at its cut equal to the chains, with nothing in its gray zone.
    - (a) is now the point accepted, its seed checked and the certificate.
    - (b) now carries K1 and K2.
    - The outcomes read "not resolved, kernel exact: the diagnosis is wrong" and "instrument failure: the diagnosis is untested".
  - **The reported readings, unscored:**
    - each reading's largest relative change of a tested row against `FRACTION = 10⁻⁶`;
    - K5's readings at 0.5, 1 and 2, with each mode's deviation;
    - K6's `slow_compare` at each read point, D7's reading of M8.15's tracked slow eigenvalues beside its level-2 to level-3 change.
  - **`k3_probe`** gives the dry run's (d) on C2a's smallest slow imaginary group.
- **`run/driver.py`:**
  - each read point records the certificate;
  - K3's pick goes through `k3_pick`, and a point with no group in the band records that reason;
  - the pyramid's K1 comes from `check_pyramid_k1`;
  - the dry run's C2a also records `K3_d_probe`;
  - **E2.** It compares the outcome's category, the text before its sentence, so the archived run scores as it did. Its printed line is unchanged, and the probe prints on a line of its own.
- **`run/test_k3.py`.** Claim 5 is re-pointed: the archived points predate the certificate. Claims 6 to 8 are new, each with its arm.
- **`run/test_guard.py`.** Test 12 is new: B2 on the pyramid's checks and in K6, the reported readings, and their serialization.

**The files:**
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `run/checks.py` `1bb79ccc39111924dc90c42f224b01e59df4dcfa6211ed5cb247ad82ce600b82`
- `run/driver.py` `305c22bb4ef424529e945c898463a93f3db1e68f972c92bf51df69837007162a`
- `run/test_k3.py` `ccac8085af493732bf0117fde8fcf5f94ac95bc83d0b613c811f7bd21a61ed37`
- `run/test_guard.py` `8b28fe3b6b15f26688b680df64f92998e04b65986c89c8ceedd7a140ac462def`

**Unrecorded passes,** in a scratch copy of the bench.
- **The five filed tests.**
  - The first pass found `score_dry.py`'s claim 3 failing. E2's printed line had gained the probe, so it no longer equalled the archived run's line character for character.
  - The probe moved to its own line, and the second pass gave all five green: `test_guard` 75 of 75, `test_k3` 0 failed in both modes, `test_claims` and `score_dry` clean.
- **The regression's development runs that read the edited files:** `dl_linear`, `dl_recal`, `sep_claims`, `sep_reread` for C2a and C2b, and `set_order` for C2a, C2b and C2a/R5.
  - Each exits 0, and its output is byte-identical to its kept copy.
  - A first comparison loop did not run five of them: zsh kept each command one word. Run one by one, all eight ran.
  - `seed_check` reads none of the edited paths, since its sentinels keep `record` from running. It was not rerun, so no sealed seed was built.

**The pin.** Entry 281's pin no longer matches the tree: this revision retires it. A new pin follows the units' review and the dry rerun.

**Next:**
1. the five tests and the eight regression runs, logged on the bench;
2. the terms' delta;
3. the units' packet.

## 290. 2026-10-18T14:16:24Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `8b28fe3b6b15f26688b680df64f92998e04b65986c89c8ceedd7a140ac462def`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `325f9bed9eb794a6f4ee89056b35f813c80196c3814bf498a7b802c1ca927ecc`, kept as `dev/runs/290_test_guard.out`

The guard's tests: PASS, 75 of 75.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 291. 2026-10-18T14:16:25Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ccac8085af493732bf0117fde8fcf5f94ac95bc83d0b613c811f7bd21a61ed37`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3.out` `8e3388395270dfc98a9e64aa2e6543b84d3dead18c55c99451bf9ca22dad8594`, kept as `dev/runs/291_test_k3.out`

K3's overlap: PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 292. 2026-10-18T14:16:25Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `ccac8085af493732bf0117fde8fcf5f94ac95bc83d0b613c811f7bd21a61ed37`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `b26e7e2a2a1f819083bfd5bf6bc004a74a5751395e697c06355c85fa07f773f9`, kept as `dev/runs/292_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 293. 2026-10-18T14:16:26Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `77106a40d50b5f80136b996c4f09bdcf82e9764e2881de4cba7f23d88ccec49e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/293_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 294. 2026-10-18T14:16:26Z: run `run/score_dry.py` (case: dryrun)

Script SHA-256 `aac99e2702f2fdfde020732f0b8959b69fc0a860a15cba09e43d3bcd179b815d`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/score_dry.out` `dd66aaa4edc5725844cc9d93c1e239549605ad68e0af6b582d2d5eef25587462`, kept as `dev/runs/294_score_dry.out`

The dry run's claims scored from entry 245's kept outputs, no solve: the scoring's checks PASS (0 failed); the dry run's claims {'E1': True, 'E2': True, 'E3': True, 'E4': True, 'E5': True, 'E6': True}: PASS.
Each claim derived before the run (the script's docstring).

## 295. 2026-10-18T14:16:27Z: run `dev/dl_linear.py` (case: synthetic)

Script SHA-256 `c68c848ace1529db0e8776361e186fd96c66849ae0607099cf79ecf1e89c2160`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_linear.out` `de252b4afa6fddd4f283225b85b191f8df9eb31a74b1618eee2a71fad1d7d931`, kept as `dev/runs/295_dl_linear.out`

DL, the linear record: PASS, 10 claims, 9 arms red.
Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed none.

## 296. 2026-10-18T14:16:29Z: run `dev/dl_recal.py` (case: synthetic)

Script SHA-256 `20d9295785d8025ac66a91b6680289926573ce2d1e77afa3e6048aea45f2a99e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/dl_recal.out` `0d0f9ebc3b278f63ed4dc715c845c1846d51421c5b16a46ed417ccc9651cf1bc`, kept as `dev/runs/296_dl_recal.out`

DL's recalibration claims: PASS, 10 scored claims and 8 arms (0 failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.
The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic m chosen so the synthetic cluster sits ten times below the gray zone.

## 297. 2026-10-18T14:16:33Z: run `dev/sep_claims.py` (case: synthetic)

Script SHA-256 `1570f759a62b84724892262b9f1bf289bdadd8da3a8bbae70a31502971868eb1`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_claims.out` `e9900f2cecf9f519d4b85a2d530a0c80bc1727ad0768734b665d7192598bf85d`, kept as `dev/runs/297_sep_claims.out`

The separation rule's claims: PASS (0 failed): the analytic projector, the converged controls, seven counterexamples Unresolved, and nine arms.
Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).

## 298. 2026-10-18T14:16:34Z: run `dev/sep_reread.py` (case: C2a)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2a.out` `bcd171e4c06b5e3ae8c5dfa846c52e179962bdd832c0c55207d42cf21d7603dc`, kept as `dev/runs/298_sep_reread_C2a.out`

The separation rule re-read on C2a's saved summaries: PASS, 20 of 20 verdicts as shipped and 1 of 1 changed as named; under the arm, 21 of 21 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 299. 2026-10-18T14:16:34Z: run `dev/sep_reread.py` (case: C2b)

Script SHA-256 `99b00923dfb9fe058fcf4fb56a8bb643a4a4269bc95ac0e0aaea3b9ea173d8cc`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/sep_reread_C2b.out` `43aa6f49cb647fa88732d6b7756baa1fe1dd91099165b127d5e9ad33c2986a40`, kept as `dev/runs/299_sep_reread_C2b.out`

The separation rule re-read on C2b's saved summaries: PASS, 20 of 20 verdicts as shipped and 0 of 0 changed as named; under the arm, 20 of 20 as shipped; under the instrument as hashed above. No solve.
Derived before the run (the script's docstring): the rule changed only in how it forms and reads sets.

## 300. 2026-10-18T14:16:42Z: run `dev/set_order.py` (case: C2a)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a.out` `825eb531bfd181be20eb740eb298551cb4c608b602d7b0ed028adf3e9ad263c4`, kept as `dev/runs/300_set_order_C2a.out`

The separation rule read in any order of the groups, on C2a's saved summaries: PASS (0 failed), 25 readings, 24 shuffles each. Under the arm, the shuffles turn 3. No solve.
Each claim derived before the run (the script's docstring).

## 301. 2026-10-18T14:16:44Z: run `dev/set_order.py` (case: C2b)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2b.out` `fd5024c50ba4e98bb406419b8a3dee3f24171a422f3bf733348c114e5307c133`, kept as `dev/runs/301_set_order_C2b.out`

The separation rule read in any order of the groups, on C2b's saved summaries: PASS (0 failed), 20 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 302. 2026-10-18T14:16:46Z: run `dev/set_order.py` (case: C2a/R5)

Script SHA-256 `da24033c0599ad5001a44abc956075bc1b0e2c208223a185a2f371a0d7f7b7a3`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `dev/set_order_C2a_R5.out` `69c6c5b950bacacc3d9f4809907ee0d0fd782f6d2d74392c27d740566d45002b`, kept as `dev/runs/302_set_order_C2a_R5.out`

The separation rule read in any order of the groups, on C2a/R5's saved summaries: PASS (0 failed), 4 readings, 24 shuffles each. Under the arm, the shuffles turn 0. No solve.
Each claim derived before the run (the script's docstring).

## 303. 2026-10-18T14:19:34Z: the revision's logged runs, entries 290 to 302, all passing; and the terms' delta

**The logged runs.** All thirteen exit 0.
- **The five filed tests,** entries 290 to 294:
  - `test_guard` reads 75 of 75. Against entry 259's output only test 12's lines are new, and the count moves from 66.
  - `test_k3` reads 0 failed in both modes. Against entries 260 and 261 only claim 5, re-pointed, and claims 6 to 8 change.
  - `test_claims` and `score_dry` are byte-identical to entries 262 and 263, so the archived dry runs score as they did.
- **The eight regression runs,** entries 295 to 302. `dl_linear`, `dl_recal`, `sep_claims`, `sep_reread` for C2a and C2b, and `set_order` for C2a, C2b and C2a/R5 are each byte-identical to the output entries 264 to 272 kept.

**The terms' delta,** applied alike to the built text and its source. The built text is the artifact: a rebuild would read moving heads, the census now at `805ddbc` where the terms cite `787aef1`, so the build is not rerun.
- **K3:**
  - **(a)** is the point accepted, its seed checked, and the kernel certified exact by `L` alone: `‖L t‖ ≤ 1000 u ‖L‖ ‖t‖` for each exact symmetry direction, and `L`'s zero count at that cut equal to the expected `V₀`'s number of Jordan chains, with its gray zone empty. It never reads `A`'s zero cluster.
  - **(b)** carries K1 and K2.
  - **(d)** is the group (b) finds at the highest cutoff passing THE CONVERGENCE RULE, read by the rule's own matching.
  - **Not resolved, with the kernel exact,** now names a merged in-span mode.
  - **Instrument failure** names an unaccepted point, a failed seed or an inexact kernel.
- **The floor's line** now reads "Every accepted development point met it", since entry 068's D6 run failed the bound.
- **The built text** is `registration/m8_16_task_details.md` `20a2db246893122f0e16aebc2c1943446ac5c8cb7ec9df83ce58e1721fc15eff`, at 8085 words.
- **The source** is `registration/m8_16_task_details.src.md` `017d7f7b60da184b86142200cd9558836e74a710f727363d16b13ace9b7a1e32`.
- **The count** is 81 words above entry 278's 8,004. It is still about 8,000, as `PR_REVIEW_STANDARDS.md` § 12.2 caps it, and it is reported to the units.
- **Still to come:** the lines on the dry run's history follow the dry rerun.

**Next:**
1. the units' packet: the code and its tests, the regression and the terms' delta;
2. after their review, the dry rerun on the final tree;
3. the history lines;
4. the final text and its confirmation;
5. a new pin, the MIT commit with a new dated census note, and the pull request updated, each on Blake's go.

## 304. 2026-10-18T14:42:58Z: the units on the revision packet: UA's one blocker, the seed's preflight; UB's three changes; adjudicated

**UA (F1): CONDITIONAL GO.**
- **Confirmed:**
  - B1, B2's propagation and B3;
  - K3's certificate, and K2 in (b);
  - the reported readings;
  - the terms' delta, and 8,085 words as acceptable, not to be trimmed merely for a round number.
- **Reproduced** from the archive: `test_guard` 75 of 75; `test_k3`; the certificate's arms; the failed-run claims; the saved-output scoring.
- **HOLD, B2's execution path.** In `run_case` a failed seed was scored as failing but did not stop the solver: `continue_to` ran after `seed_ok` was false. The terms check the seed before any solve and end the case on a failure.
  - UA reproduced it with a failing seed and a sentinel in place of `continue_to`, on stand-ins, with no sealed case built.
  - Required: the preflight before continuation, a recorded instrument failure in the output's shape, no call to the solver, and K1 to K6 and the stop reporting it without an exception. Also one negative test with a solver sentinel that must never fire.
- **Then:** GO to the dry rerun, once that test passes.

**UB:**
- **KEEP** B1 to B3, the reported readings, the certificate and (d).
  - UB's short solves on three GO controls at `ε = 0.25`, `N = 16` and 24, read every tangent residual between 0.02 u and 3.3 u, against the cut's 1000 u. `L`'s zero count equals the chains, and its gray zone is empty.
  - UB rebuilt the terms from the source at MIT `2c27cea`, through a local mirror. The result equals the hand-applied delta except the word-budget line.
  - UB names two misses of its own: it judged the `10⁻³` line fail-safe at step 3, and it said at item 7 of its v2 review that the dry run need not rerun.
- **CHANGE, K2 in (b).** Moving all of K2 into (b) would read a Theorem R failure outside the in-span mode, a missing quartet or Krein-positive pair or an unpredicted group, as "the diagnosis is wrong". The terms assign that case to the instrument: "A disagreement with them at the smallest amplitudes indicts the instrument."
  - The fix: (a) also requires the slow band outside the in-span pair's class to be Theorem R's, within 5%.
  - Two texts, a code test and two arms.
- **CHANGE, the word count.**
  - The builder states "about 8,100" at 8,085 words, where the hand-applied text keeps "about 8,000".
  - The final count is to be at most 8,049, with the trim in the history lines the rerun rewrites anyway.
  - The final text is to be built by the builder at the base the terms were built from, through a `--base` option, so each unit can rebuild it byte for byte.
- **ADD, E7.** Every read point of every control carries K3(a)'s certificate, with its largest tangent residual reported against the cut. Expected at most about 10 u.
- **GO** to the dry rerun once these are built, with their tests rerun in a scratch copy.

**Adjudicated.**
- **K2:** UB's form. It keeps what UA confirmed, since a merged in-span mode still passes (a), its class being excluded. It also routes a Theorem R miss elsewhere to the instrument, as the terms already say. UA sees the change in the next note.
- **The word count:** UB's form. UA objected to trimming merely for a round number. Here the reason is that the builder, the units' rebuild, must state the count the text states, and the trim lands in lines that change anyway.
- **UA's blocker** is adopted; UB had not raised it. **UB's E7** is adopted; UA had not objected.
- **Found while building UA's fix:** `check_c1` read no seed, and over an empty cutoff it passed C1's K1 vacuously. It now requires every cutoff's seed and every registered point; on a full run it reads as before.

## 305. 2026-10-18T14:42:58Z: round 2 built: the seed's preflight, C1's K1, K3(a)'s slow band, E7, the builder's base; tested unrecorded

**The code:**
- **`run/driver.py`:**
  - **The preflight.** In `run_case` and `run_c1` a failed seed now ends the case before any solve, or in C1 before any record. Its cutoff records the seed and no point; each later cutoff is recorded as not checked, with no point, by `not_checked`. So every check reads the output's full shape. C1's closing comparison along the cutoffs is false when the case ended.
  - **E7** is in `dry_claims` and its docstring. The reader is `e7`, which reads none where a read point lacks the certificate.
  - `dry_claims` takes `e7_claim`, which the archived runs' scorers set false.
- **`run/checks.py`:**
  - `check_c1` requires every cutoff's seed and every registered point.
  - `theorem_r_outside` matches the slow band outside the class `('imag', -1)` against Theorem R: equal counts, each within `BAR`. K3's (a) includes it.
- **`run/score_dry.py`** and **`run/test_claims.py`** call `dry_claims` with `e7_claim=False`, reading E1 to E6, the claims registered for their runs.
- **`registration/fill_terms.py`** takes `--base COMMIT` and reads MIT's pages there, without a fetch. `registration/` lies outside the manifest.

**The terms:** UB's two sentences, in the built text and its source.
- (a) adds: "And outside the in-span pair's class, imaginary of negative Krein signature, the slow band is Theorem R's: the quartet and the Krein-positive pair matched as in K2, each within 5% of leading order, and no other group".
- The instrument failure adds "or the slow band departs from Theorem R outside the in-span pair".
- The built text is at 8133 words.
- Built by the builder at the base, the parent of the commit that first added the folder, read from git, the result cites the census at `787aef1`. It equals the built text except the word-budget line: "about 8,100" against "about 8,000". The trim to at most 8,049 follows the rerun.

**The tests:**
- **`test_k3` claim 7** gains UB's two arms:
  - a Krein-positive pair removed reads "instrument failure";
  - an extra Krein-negative group reads "the diagnosis is wrong".
- **`test_guard` test 13,** for C2a and C1:
  - **The green parent:** with the seed passing, a sentinel in place of the solver, or for C1 the record, fires, so the sentinel is live.
  - **The negative test:** with the seed check made to fail, the sentinel never fires, and every cutoff is recorded with no point.
  - **The report:** the checks report the failure without an exception, and the stop names it.
  - **E7's reader** reads none on the kept outputs, which predate the certificate. It holds with every certificate set, and fails with one tangent ten times the cut.

**Unrecorded, in a scratch copy:**
- `test_guard` reads 84 of 84, and `test_k3` reads 0 failed in both modes.
- `test_claims` and `score_dry` are byte-identical to their last outputs.
- No development run reads a file this round edits, so the regression stands.

**The files:**
- `run/driver.py` `315df5646de2cc4332e9d2d3fbeef810f528d953e807bf368477475e1ba0727a`
- `run/checks.py` `31dc884bea7d9274949c00cc795073bb10519e8188e8a718c8c3f31ce31b8c83`
- `run/score_dry.py` `54831523820626dc847e2ba9246a031b4efeb9270227579a2cd140e649130420`
- `run/test_claims.py` `0a43d5bbc75a17d479add2bb34764b935117b0951abc2fafbe2423e5526f508e`
- `run/test_k3.py` `b769c6bb0c6a396b30e77382e90186b42632c3e6f1d1f0109415f6502ca5be7c`
- `run/test_guard.py` `b700f100d48006680930d5882e0a99c4cab179d1ff99d2982f55637da62f7720`
- `registration/fill_terms.py` `0f40225c35992b29dd06b4b81be5e03a9a8839685f4c2531b1d6a4c60fbfde7b`
- `registration/m8_16_task_details.md` `d49ebd92eb978a68b0a5c18cda9253012effbf5dc25c12ab830e123999ddc842`
- `registration/m8_16_task_details.src.md` `72fc607e14cb2e04dde82ea274e3a8d6afee865127d92d2a3cafa0202ddbfa5a`

**Next:**
1. the five tests, logged;
2. `run/dry` moved aside, its contents kept as entry 245's outputs;
3. the dry rerun on the final tree, with E7;
4. the history lines, at most 8,049 words in all, and the final text built at the base;
5. the units' confirmation;
6. the new pin, the MIT commit and its census note, and #637 updated, each on Blake's go.

## 306. 2026-10-18T14:43:19Z: run `run/test_guard.py` (case: synthetic)

Script SHA-256 `b700f100d48006680930d5882e0a99c4cab179d1ff99d2982f55637da62f7720`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_guard.out` `e1d49f0aa6a739d1c7724cab57531c7ba9735a28553a77b744b2dedc32c61bd7`, kept as `dev/runs/306_test_guard.out`

The guard's tests: PASS, 84 of 84.
Each outcome derived before the run (the script's docstring); temporary trees only, nothing solved, no sealed seed built, no sealed record opened.

## 307. 2026-10-18T14:43:19Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `b769c6bb0c6a396b30e77382e90186b42632c3e6f1d1f0109415f6502ca5be7c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3.out` `6ef7b89eee740037fc9ed1e6c638477ddc67f135a4f95968df4ff927b90b7fde`, kept as `dev/runs/307_test_k3.out`

K3's overlap: PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 308. 2026-10-18T14:43:20Z: run `run/test_k3.py` (case: synthetic)

Script SHA-256 `b769c6bb0c6a396b30e77382e90186b42632c3e6f1d1f0109415f6502ca5be7c`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_k3_synthetic.out` `b26e7e2a2a1f819083bfd5bf6bc004a74a5751395e697c06355c85fa07f773f9`, kept as `dev/runs/308_test_k3_synthetic.out`

K3's overlap (synthetic only): PASS (0 failed).
Each outcome derived before the run (the script's docstring).

## 309. 2026-10-18T14:43:20Z: run `run/test_claims.py` (case: dryrun)

Script SHA-256 `0a43d5bbc75a17d479add2bb34764b935117b0951abc2fafbe2423e5526f508e`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/test_claims.out` `13785a763e5f17102129ed7fd08a2c11e1d991a84ff404848d1b4f9eca0c132d`, kept as `dev/runs/309_test_claims.out`

The dry run's claims on a stopped run: PASS (0 failed). No solve; the claims' own entry captured, not written.
Each claim derived before the run (the script's docstring).

## 310. 2026-10-18T14:43:21Z: run `run/score_dry.py` (case: dryrun)

Script SHA-256 `54831523820626dc847e2ba9246a031b4efeb9270227579a2cd140e649130420`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/score_dry.out` `dd66aaa4edc5725844cc9d93c1e239549605ad68e0af6b582d2d5eef25587462`, kept as `dev/runs/310_score_dry.out`

The dry run's claims scored from entry 245's kept outputs, no solve: the scoring's checks PASS (0 failed); the dry run's claims {'E1': True, 'E2': True, 'E3': True, 'E4': True, 'E5': True, 'E6': True}: PASS.
Each claim derived before the run (the script's docstring).

## 311. 2026-10-18T14:44:17Z: the dry rerun on the final tree, launched; `run/dry` moved aside first

**`run/dry` moved aside.** Its 13 files are each byte-identical to entry 245's kept copies, `dev/runs/245_dry_*`. The folder is moved out of the bench, to `../m8_16_run_dry_245_moved`; it is moved, not deleted, and `run/dry` is empty. A run log from another tree would refuse the resume anyway.

**The launch:**
- **The command:** `python3 -I -B -u run/driver.py --dry`, from the bench, its output to `run/dry/driver.log`, under `caffeinate -i`, as a background task.
- **The tree:** the one entry 305 built, after the logged tests of entries 306 to 310.
- **The power:** "Now drawing from 'Battery Power'"; "-InternalBattery-0 (id=6881379)	98%; discharging; 16:27 remaining present: true". The dry run's timing feeds the terms' cost line, so the power source is recorded.
- **The claims:** E1 to E7 are scored at its end, and the run writes its own entry.

## 312. 2026-10-18T16:48:05Z: run `run/driver.py` (case: dryrun)

Script SHA-256 `315df5646de2cc4332e9d2d3fbeef810f528d953e807bf368477475e1ba0727a`; the instrument package as hashed below.
- `instrument/__init__.py` `ebb8d0440edae25ee0755fa962d24061fbebb502bf5176d3084a422188d2dcdc`
- `instrument/basis.py` `5728c5e8c9532bc4764dd5b9d111f693e5ba86c415d4a2b4f880e8196c66616b`
- `instrument/branches.py` `4e32a8cfd1cd7db4ced242ecddf5e22c9319134029877b78eae74b13b3d1a55f`
- `instrument/certified.py` `1f5dde36bde7edfc3257e7581b2538ab7853693ab8ed1b48dae6dc0e2de343d1`
- `instrument/convergence.py` `02404ab43313eb4d67cb336edbed364d9071187da66dec44bbd4f997cf66bd51`
- `instrument/devtools.py` `3a2d0f7d2c5bd74bdedf2a673989a67cadef25c508424ad25501745c7adb7d0f`
- `instrument/functional.py` `f8f9329f1fa5d2bb1f7e3718d5e5bdfa94e86f9e0dcc4dda308a7f86c0f00d79`
- `instrument/group2i.py` `0a9732afe32b3509976de2e519c0f8da3d4f773d2495c5c2d58d27fe5aaa85f0`
- `instrument/linear.py` `e0fce88f3ed8374f94f6ba329813cfb639f05a2407f9a313f66cbe79744f11c2`
- `instrument/newton.py` `36bd989fe10891ba49757025a908b95569cb7b7ee1901f87299dede2a10fe00f`
- `instrument/quadrature.py` `6c9baf9d1bd3bc8741006490f88fd4a1e134f0cd3a6ffd8f9b7f1a6074e30a71`
- `instrument/su2.py` `60c4f8088a089341e76fb159847784336f4ad6a886a72a1c7683ef86a63b75f6`
- output `run/dry/driver_dry.out` `a193d59e1d7f78d1aefb07b688c91a589af401f94ced3452f147a61ca2a004ae`, kept as `dev/runs/312_driver_dry.out`
- output `run/dry/driver.out` `9d09262376a2e997fedb416dca057524c0765eef75d2451823f6a5f65d9dec96`, kept as `dev/runs/312_driver.out`
- output `run/dry/GATE.json` `f7f86453f7246cc6fd7c4f870ec30153cd1950dea5b93d013055732127949792`, kept as `dev/runs/312_GATE.json`
- output `run/dry/VERDICT.json` `0282e786f26e1004dcef66c46a7afa386db978436cf763400149f25c5e976d69`, kept as `dev/runs/312_VERDICT.json`
- output `run/dry/RUNLOG.json` `0de77e37efa9d1f6ca36d7643985427f52fb21359c2053cff0d84d5569a87301`, kept as `dev/runs/312_RUNLOG.json`

Step 3's dry run: PASS (0 of 7 claims failed or not evaluated): {'E1': True, 'E2': True, 'E3': True, 'E4': True, 'E5': True, 'E6': True, 'E7': True}.
The claims were derived before the run (the driver's docstring; DRIVER_PLAN.md v2). The run's per-case outputs and their SHA-256 are in its RUNLOG.json.

## 313. 2026-10-18T16:49:25Z: the dry rerun on the final tree: every case and check passes, and all seven claims hold; its outputs kept

**The run** (launched in entry 311; it logged itself as entry 312).
- **Every case ran,** and every check passed: C1, C2a, C2b, C3, the `R5` control and C2a's ladder segment. The gate record has no stop. The verdict reads `incomplete`, as a dry run's does, with the `R5` gate passing and nothing failed.
- **The claims, E1 to E7,** all hold. The run's own entry reads "Step 3's dry run: PASS (0 of 7 claims failed or not evaluated)".
  - **E2.** K3 on C2a reads "not resolved, kernel exact: the diagnosis is wrong" at (b), and the probe's (d) on C2a's smallest pair passes the rule.
  - **E7** reads: "E7. K3(a)'s certificate at every read point of every control: True; the largest tangent residual 4.2 u, against the cut's 1000 u".
- **The times:**
  - by case: C1 710 s, C2a 813 s, C2b 391 s, C3 1201 s, C2a/R5 2099 s, C2a:ladder 2205 s;
  - in all, 7421 s, or 2.06 h;
  - the controls' phase, C1 to C3 and the `R5` control, 5214 s, or 1.45 h.
- **The power,** as observed: on battery at the launch; on AC at 11:18 local; on battery again at 12:42 local. The phase's time is therefore not a mains figure.
- **The tree** is the final one: entry 311's, with no edit since. This dry run closes the comment-tier finding that the frozen driver had not run end to end.

**The outputs kept.** The run's own entry kept five. The case outputs and the transcript are kept here by exclusive create, each case output equal to the SHA-256 in the run log:
- `run/dry/C1.json` `7b0ef443aca74fda0b69b2fce0d94e743ad84a7ac90a45091ada4a24047d77b6`, kept as `dev/runs/312_dry_C1.json`, as the run log records it
- `run/dry/C2a.json` `4095c043882bdbb58fe8e237d98d01681ad3fb477523cdc556a877004af7c09f`, kept as `dev/runs/312_dry_C2a.json`, as the run log records it
- `run/dry/C2a.npz` `ec646f784f5ed227b058aa43a479df043b3ffe1794bcf146c30c595dedffa954`, kept as `dev/runs/312_dry_C2a.npz`, as the run log records it
- `run/dry/C2a_R5.json` `62f5f886e60fea0c58663b4d271297fad84c7a82aeca4985f0763360c738a9f2`, kept as `dev/runs/312_dry_C2a_R5.json`, as the run log records it
- `run/dry/C2a_ladder.json` `71d7a91490de5f252507ea4644342f292ca3548a92d65439ccb360aa13293510`, kept as `dev/runs/312_dry_C2a_ladder.json`, as the run log records it
- `run/dry/C2b.json` `fb015cdf9f01688ef578f1e38c0b451a05a7b8c33cbe417a56a3106cf43c9c4e`, kept as `dev/runs/312_dry_C2b.json`, as the run log records it
- `run/dry/C3.json` `487ebfe65b33389bf5dd95a4b8306714956e7eb402fa38ece7cd4b47fb7aad54`, kept as `dev/runs/312_dry_C3.json`, as the run log records it
- `run/dry/C3.npz` `366681b4958ed2c6e3c88881f442b1a085ba8a783d63c867eccc1a37a836e488`, kept as `dev/runs/312_dry_C3.npz`, as the run log records it
- `run/dry/driver.log` `a193d59e1d7f78d1aefb07b688c91a589af401f94ced3452f147a61ca2a004ae`, kept as `dev/runs/312_dry_driver.log`

So `run/dry` is again byte-identical to its kept copies, now this entry's and entry 312's rather than entry 245's.

**Next:**
1. the history lines and the cost line in the terms, at most 8,049 words in all;
2. the final text, built by the builder at the base;
3. the units' confirmation of its hash.

## 314. 2026-10-18T16:54:21Z: round 3: the terms' history and cost from the final dry run; the final text built by the builder at the base

**The cost, from the final dry run.** The builder reads the latest dry run's files, now entry 312's.
- **The figures:** `R5` costs 1.3 to 2.1 times `R4`, against 1.3 to 1.6; the total is 13.6 to 17.3 h, against 13.6 to 15.2; and the controls' phase took 1.4 h, against 1.2.
- **The cause, from the times at the highest cutoff,** entry 245's run against entry 312's, on the same code but for the cheap certificate: C1 538 s against 538 s; C2a 731 s against 744 s; C2b 302 s against 352 s; C3 992 s against 1068 s; C2a/R5 1323 s against 1880 s; C2a ladder 1274 s against 2011 s.
  - The early cases ran at the same speed.
  - The `R5` control's first point took the same time, 223 s against 222 s, and its later points were slower.
  - The ladder segment ran about 1.5 times slower throughout.
- **Read as:** the machine's state slowed the run's second half, not the instrument. The machine is fanless and the load sustained, and the power changed during the run (entry 313).
- **The figures are kept as the builder gives them,** since the registered run meets the same machine for longer. They stay INFERRED.

**The source's edits:**
- **BEFORE THE FREEZE's driver lines** keep the two failures and the six claims. They add that the maintainer's review of these terms (#637) found three departures from them in the driver, since repaired, and that it had changed after that run. They add that on the final tree its dry run passed every check and all seven claims. Two details of the first failure move to the log, entry 219: its location and the rejected repair's mechanism.
- **The failures on record** now point to "the dry run's two failures and the review's three findings".
- **The word budget** reads "near" § 12.2's cap of about 8,000, not "inside" it.

**The word count: a change from entry 304's ruling, proposed to the units.**
- The history adds the review and the final dry run, so it frees no words.
- Reaching UB's 8,049 would need about 100 words cut from paragraphs both units have reviewed, which UA advised against.
- UB's substantive point, that the built text is the builder's output and each unit can rebuild it byte for byte, is met. So the text states the builder's own count, about 8,100, near the cap.
- The trim stays available if UB holds to 8,049.

**The final text,** built by `fill_terms.py --base` at `2c27cea2d543`, the parent of the commit that first added the folder, read from git.
- The census is cited at `787aef1`.
- 8,149 words, stated as about 8,100.
- A build in a scratch mirror and the build on the bench are byte-identical, and their reports differ only in the path written.
- `registration/m8_16_task_details.md` `86992a5f7a278d639042adad2576c666979fa20f3cb53071daa62c614e83d5cf`
- `registration/m8_16_task_details.src.md` `ffa461d1c48e8de565f0e946f54f35ec3a38a179e4091d7de639fb90a05fead1`
- `registration/fill_terms.py` `0f40225c35992b29dd06b4b81be5e03a9a8839685f4c2531b1d6a4c60fbfde7b`

**Next:**
1. the units' packet: round 2's code and tests, the dry run, and the final text;
2. their confirmation of its hash;
3. then, each on Blake's go:
   - the new pin, with `805ddbc`'s retired;
   - the MIT commit with a new dated census note;
   - the revised task file pushed to #637;
   - a reply to xrodz, which Blake posts.

## 315. 2026-10-18T17:10:32Z: both units confirm round 2, the final dry run and the final text at entry 314's hash; UB releases its word ceiling

**UA (F1): CONFIRM.** The repinning sequence has UA's GO, once UB concurs and Blake authorizes it.
- **Closed:**
  - the seed's preflight, for C1 and C2a, tested both ways;
  - `check_c1`'s vacuous pass.
- **Confirmed:**
  - UB's K3(a) split: a missing predicted mode reads "instrument failure", and an extra Krein-negative group, with the certificate holding, reads "the diagnosis is wrong";
  - (d)'s matched group.
- **Replayed:** `test_guard` 84 of 84, and `test_k3`.
- **The final dry run,** checked from its kept outputs: 7 of 7 claims, no stop, 124 minutes. E7 was recalculated directly: 60 of 60 read points carry a passing certificate, the largest tangent residual 4.2406 u.
- **The final text's SHA-256** is verified.
- **The word count.** 8,149 words is accepted under "about 8,000", while UB's ceiling remained UB's to hold.
- **What stands:** the old pin is superseded and never reused, and no scored qualification or sealed run is authorized.

**UB: CONFIRM,** on the code and tests, the final dry run, and the final text.
- **The diffs:** all 12 incremental diffs apply exactly to the v1 bundle, and the final-against-filed diff applies to the terms filed at `805ddbc`.
- **The final text,** rebuilt by `fill_terms.py --base` from UB's own clones, is byte-identical: 8,149 words, the census at `787aef1`.
- **The tests:** `test_guard` 84 of 84, `test_k3` passing with round-off digits only, and `test_claims` and `score_dry` byte-identical.
- **The final dry run,** re-scored from its kept outputs:
  - every case output and the gate record match the run log;
  - 0 of 7 claims failed, and E2's probe passes;
  - E7 holds at all 60 read points, the largest tangent residuals by case C2b 4.24 u, C1 1.97 u, C2a/R5 0.18 u, C2a 0.17 u and C3 0.10 u. That leaves at least 236 times headroom, and 0.18 u or less in the pyramid's slots.
- **KEEP:** the preflight and `check_c1`; the K2 split, with `theorem_r_outside` counting any other group, one of unresolved sign included; and the dry run and the cost, the wider range being the honest one.
- **The word count.** UB releases its 8,049 condition: reproducibility is met, "about 8,100 words, near the cap" is true, and cutting reviewed paragraphs would risk their meaning to save 1.9%.
- **FIXABLE, `REPRODUCE.md`,** outside the pin, for the next MIT commit. Five lines:
  - the dry run's history, now with #637 and the final dry run;
  - `run/dry`'s kept copies, now `dev/runs/312_*`;
  - 84 tests;
  - "The final dry run, entry 312, took 124 minutes";
  - 13.6 to 17.3 hours.

  All five match the file as UB quotes them.
- **The steps:**
  1. retire the old `run/m8_16_task_details.md` and `run/MANIFEST_PIN`, both written by exclusive create, in an entry of their own; they stay in history at `805ddbc`;
  2. copy in the final text;
  3. write the new pin;
  4. update `REPRODUCE.md` and regenerate `SHA256SUMS`;
  5. add a new dated census note naming both new hashes, beside the first;
  6. commit;
  7. on #637, replace the task doc, check its hash at the head, and update the body's provenance.

**Next,** on Blake's go: the repin and the local commits, stopping before any push.

## 316. 2026-10-18T17:12:03Z: the repin, step 1: the old terms copy and the old pin retired from `run/`

On Blake's go ("go on 1 through 5"), in the order of entry 315.

**Retired.** Both files were written by exclusive create, so they had to leave before the new ones could be written. Each was byte-identical to the copy published at MIT `805ddbc`:
- `run/m8_16_task_details.md` `d497359eb988ffedf80e866a121cb06734684ed8b5ee670a127d5267af5e8096`, the terms entry 281 copied in;
- `run/MANIFEST_PIN` `00b41c591b6d2bf398783438bc565cf3ac7ad36253f1f868c7545c20c057aba2`, entry 281's pin.

Both are moved out of the bench, to `../m8_16_retired_805ddbc/`; they are moved, not deleted. Their published copies stay in MIT's history at `805ddbc`. The old pin is superseded and is never reused (UA).

**Next:**
1. the final text into `run/`;
2. the new pin, after a scan.

## 317. 2026-10-18T17:13:03Z: the repin, step 2: the final text in `run/`, the scan, and the new pin

**The final text.** `registration/m8_16_task_details.md` hashes to the SHA-256 entry 314 records, the one both units confirmed. It is copied by exclusive create to `run/m8_16_task_details.md` `86992a5f7a278d639042adad2576c666979fa20f3cb53071daa62c614e83d5cf`, which equals it.

**The scan, before the pin.** The bench was scanned without `run/dry` and caches: every file, text and binary, for:
- OpenWave's local-path patterns;
- the bench's path;
- emails and personal identifiers;
- credentials;
- session internals.

The hits:
- the three kept driver logs already disclosed;
- one line of `DEVLOG.md`, entry 285's "Author and committer", which names the session commits' identity. That identity is already public as the author of the session commits on MIT `main`, and the log is append-only, so the line stays.

OpenWave's `check_no_local.py` passes the final text.

**The new pin.** `run/pin_manifest.py` wrote `run/MANIFEST_PIN` by exclusive create: `a5f4517360672bd6812b3f9bf79639df07304bbde19479391006ea03cd15c53a`, the manifest's SHA-256 over 36 files. The recomputed manifest equals it. Against entry 281's pin, the files are the same 36 paths. The contents differ in:
- the final text;
- `instrument/linear.py` and `instrument/convergence.py`;
- `run/checks.py`, `run/driver.py`, `run/score_dry.py` and `run/test_claims.py`;
- the two tests and their outputs.

From here no manifest-covered file changes (UA). Entry 316's retired pin is superseded.

**Next:**
1. the MIT folder rebuilt from the bench, with `REPRODUCE.md`'s five lines (UB);
2. `SHA256SUMS` fresh;
3. the checks and the scratch tests;
4. the census note;
5. the local commits.

## 318. 2026-10-18T17:15:01Z: the repin, steps 3 and 4: the MIT folder rebuilt and checked; `REPRODUCE.md`; the census note

**`REPRODUCE.md`,** outside the pin, carries UB's five lines (entry 315):
- the dry run's history, now with the review on #637, linked as OpenWave's, and the final dry run;
- `run/dry`'s kept copies, now `dev/runs/312_*`;
- 84 tests;
- "The final dry run, entry 312, took 124 minutes";
- 13.6 to 17.3 hours.

It is now `362a34432047c80655eee7e31bb1d4e671f673761abb2f252bcb600a3980b667`, on the bench and in the folder alike.

**The folder,** rebuilt from the bench without `run/dry` and caches:
- each file equals the bench's, `SHA256SUMS` apart, which is written fresh after this entry;
- its manifest, recomputed, equals entry 317's pin, `a5f4517360672bd6812b3f9bf79639df07304bbde19479391006ea03cd15c53a`.

**The scratch tests,** from a copy of the folder: all five filed tests exit 0, and each output equals the folder's, byte for byte. Afterwards the copy's manifest still equals the pin.

**The scan of the folder** finds the hits entry 317 disclosed and no other.

**The census note,** § V, step 4, below the first note, which stands as written. It names the revised terms' SHA-256 and the new pin, both read from the folder's files, and says the first note's hashes are superseded.
- The page's math count is unchanged.
- `metadata-lint.py` reports 0 FAIL and 0 WARN.
- The Status stands: M8.16 is still the next step.

**Next:**
1. this log copied into the folder;
2. `SHA256SUMS` fresh, and `shasum -c`;
3. the MIT commit, verified from its own tree;
4. #637's task file replaced on its branch, in a local commit;
5. a stop before any push.
