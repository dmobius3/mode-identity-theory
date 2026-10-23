# M8.16.1 development log

The development record of M8.16.1, the second and last qualification of the stationary harmonic Galerkin instrument. Every development run is logged here with its script's SHA-256, its case and its outcome, including how it informed a tolerance, and is disclosed in the filed terms. Development earns no qualification credit. Entries are never edited; a correction enters as a new entry.

## 1. 2026-10-20T18:13:55Z: the folder opened, on the bench; the terms at draft v3

**The folder.** This folder mirrors `scripts/soft-slot-dynamics-m8-16-1/` on MIT, where it lands with the terms. `instrument/` will be M8.16's, byte for byte. `run/` is new.

**The terms.** Draft v3, `m8_16_1_task_details.md`, after two rounds with both units:
- the draft: `fae99a5c0ffc3856b09c298561a4c64a27c8242c8801675d93f25817c370fe43`
- its template: `41f4b31da4b13a4730b767a958bbd2dcfc4d87f455b0dc0d82a4b2ded80e04f7`
- its builder: `73f68156a97242bcace9553c8acf7733a3e2137749192cee87cdc94019718ad1`

**The split.** Amendment 5, Blake's decision of 2026-10-20 (C2a/R5's full ladder for development), is to be written into this folder's `BOUNDARY.md`, citing M8.16's by SHA-256, before its ladder runs.

**First,** the pinned next-order script, `run/next_order_values.py`. It runs off the instrument: no case is solved on it, and the sealed cases' values come from the reduced quartic alone.

## 2. 2026-10-20T18:26:23Z: run `run/next_order_values.py` (cases: P5, T1 to T4 in R4 and R5, T5, T5J, C3R; off the instrument)

**Script** SHA-256 `e9f1b6afd6795f9e7f0a6fb4a710e13cfd3e93e94f23b40f9fccb5c9005adee7`. **Imports,** used unchanged, from MIT at deec830:
- `files/framework/files/working/files/scripts/soft-slot-branches/next-order/next_order_check.py` `a2e67c7e20268142e9bb18e7ce0a006dada9d4dcc203342281f9a1b2693793df`
- `files/framework/files/working/files/scripts/soft-slot-branches/next-order/next_order_check.out` `2afa6b065a174121e13d01cefa8df54df9f65449aba6a71646b7c08a97565105`
- `files/framework/files/working/files/scripts/soft-slot-branches/second_order_check.py` `abc13f3d0d9dab687668cb2976b3090620f804e21f03f6c741285c5aad99dc8e`
- `files/framework/files/working/files/scripts/soft-slot-branches/branches_check.py` `555b78339862a40e5ec978719eeae491cc7b79d41511d954efaf436fb658901d`

**Outputs,** kept as `dev/runs/001_next_order_values.out` (`cb3de2c4ea844be2290d6584e254a245edaee3ee47393f1ccaf9844cec1740bc`) and `dev/runs/001_next_order_values.json` (`636138cba7fca1af8dcdc8ba9f7ed82825585b543a7be5ee5386698156ad89bc`).

**Outcome:** all checks A to F passed at all twelve cases and three cutoffs, and the four arms were red.
- The full-channel values reproduce the bench's preview to every printed digit.
- The pyramid reproduces claim F's printed values at N = 16, 24 and 32.
- At T4, check i holds at 50 digits: the Hessian at the germ annihilates every orbit tangent to 1.6e-51.

**A gap, found on reading the output.** At the C3 ray, which has no prior frozen tau, check A tested Q, k and the zero multiplicity but not the spectrum's structure, so that part could not fail. The record's groups were right: a quartet, then a Krein-negative pair, then a Krein-positive pair. The script now checks the structure against the terms' type, with a mutation arm. No tolerance was informed.

## 3. 2026-10-20T18:26:23Z: run `run/next_order_values.py` again, with the C3 ray's structure check

**Script** SHA-256 `165544b45d2d07fa49550b3affdcfeb032712e00d8e861024d8baeb37f1cfb23`. Imports as in entry 2.

**Outputs:**
- `run/next_order_values.out` `b70f760384be75057ed4fc0c378d8075c19266f0d0e37f4f5896eea3d7429408`
- `run/next_order_values.json` `f44fd4fd22bfdaefee875a23709183a8f1d0786a0f8ab0e9c505263d5870b409`

Both are kept as `dev/runs/002_*`.

**Outcome:** all checks pass, and the five arms are red. The values for every case are identical to entry 2's. The C3 ray's off-ray part exceeds check 4's floor by at least 45.7 at N = 16, and by 44.3 at N = 24 and 32.

## 4. 2026-10-20T18:36:49Z: run `run/next_order_values.py` again, with every imported module in its record

**Why.** Entry 3's record listed three of the four modules the script loads from MIT. It missed `germ_check.py`, which `second_order_check.py` imports. That is the "every import" class of M8.16's seeds line. The record now lists every module loaded from the checkout, read from `sys.modules`, and the data file it reads. A count guard of four stops the run if that set changes.

**Script** SHA-256 `7f5ea8d8fcf508f4e28914e1baa4d943901cc669b5ab579a4a5ca682e9a977c3`.

**Outputs:**
- `run/next_order_values.out` `119fc932adaf8d4a2d0d49198abb259490486801650ff6324c1ba960041ac119`
- `run/next_order_values.json` `d32ffe3e31beade38a165b19f4c5d864e6de8aba3d5fa31bf5b08ce38b719764`

Both are kept as `dev/runs/003_*`.

**Outcome:** all checks pass, and the five arms are red. Every case's values and every arm are identical to entry 3's; only the record's import list changed.

## 5. 2026-10-20T19:26:49Z: a correction to entries 2 and 3's times

Entries 2 and 3 carry one time, 2026-10-20T18:26:23Z, when both were written. It is the time of the writing, not of the runs:
- entry 2's run ended at 18:18:49Z, its outputs' file time, read in this session before they were replaced;
- entry 3's run ended shortly before 18:26:23Z.

Nothing else in either entry changes (UB, on development step 1's review).

## 6. 2026-10-20T19:26:49Z: run `run/next_order_values.py`, v2, after the units' review of step 1

**The changes.** Both units returned GO after fixes, and every point is adopted:
- **T4 by the formula the terms name,** at 50 digits: Hess h and Hess R~0 from the landed model's `hessians`, grad R~0 by Euler, z on the normal space, D^3h[z] by an exact central difference, then the landed `leading` and `first_order`. The model's extrapolation stays as the cross-check, check X, within the landed claim E's 1e-8 (UA, UB).
- **Check i on D_u itself at T4**, with the model's tangent check kept as the model's own.
- **Arms for C, D and E,** and one for T4's check i: a non-scalar correction on T2/R4's double, N = 32 with level 18 removed, the cutoff rule with L >= N, and z dropped from D_u (UA, UB).
- **One-to-one matching** in check A (UA).
- **The record:** the method per case, T4's cross-check values and differences, a SHA-256 of the cases section alone, NumPy's version, and a note on kappa_s (UA, UB).

**Script** SHA-256 `7b8ff9a0a93548a778547b11fb42b3523fac9d9dd8268719b683aa260c9290b4`. Imports as in entry 4.

**Outputs:**
- `run/next_order_values.out` `323394dfd8fb4ce910bb39ad31532c0dbab014f53bc108bb942cdf2f52048bb7`
- `run/next_order_values.json` `52077d69a05cf3c6cc0926f55d0e5c64a1c991040082899568db654a7c6c0843`, its cases section `45ad237179b6c7176b4372f8b36fe6cf20ba95ebdff510f727eec1ea4a2ebeea`

Both are kept, with the script, as `dev/runs/004_*`.

**Outcome:** all checks pass, A to F and X, and the nine arms are red, in 616 s.
- The algebraic cases' values are identical to entry 4's.
- T4's values are now the formula's. The model agrees with them to at most 7.1e-15 relative.
- Check i on D_u holds to 4.2e-50 in R4 and 5.7e-50 in R5. UA's independent direct value of T4/R5's smallest coefficient, 0.2399899983182723736, agrees to its printed digits.

## 7. 2026-10-22T13:44:19Z: run `run/next_order_values.py` again, with UB's NIT on T4's check-i arm

**Why.** UB's confirmation of step 1 v2 carried one NIT. The arm "T4/R4's z dropped from D_u" zeroed z before the solve test. So `solved` turned red (1.0) alongside check i (0.198), and the record showed only RED. The arm now zeroes D^3h[z] in D_u after the solve, so z stays solved and only check i can turn it red. It also prints its check i value. UB: "The values stay as they are."

**The change,** against `dev/runs/004_next_order_values.py`, and nothing else:
- the two lines `if drop_z: z = z * 0` move after the `D3 =` line, as `if drop_z: D3 = D3 * 0`;
- the arm keeps its case and prints check i beside its verdict.

**Script** SHA-256 `4bf81a60beef1338c6da36b2d4c04f9d51b826322a0b1e9540769fa318f4028e`. Imports as in entry 4.

**Outputs:**
- `run/next_order_values.out` `fc0821ecdf011190c19604ae146150a604e3ec25ac5a8ecc38a740afa84c2f55`
- `run/next_order_values.json` `b05fff5ddd71c29c79318b6257f940c6035d7c954f3bafa34a22080eecc00333`, its cases section `45ad237179b6c7176b4372f8b36fe6cf20ba95ebdff510f727eec1ea4a2ebeea`

Both are kept, with the script, as `dev/runs/005_*`.

**Outcome:** all checks pass, A to F and X, and the nine arms are red, in 342 s. Against entry 6's outputs:
- the `.out` differs in two lines: the arm's, now "RED, check i 0.11", and the JSON's hash line;
- the `.json` differs only in the script's SHA-256, and its cases section is unchanged;
- under the arm, check i reads 0.11, UB's probe value. `solved` and `perp` are computed before D^3h[z] enters, so the arm leaves them as run.

## 8. 2026-10-22T14:07:43Z: the record of `dev/pyramid_check2_from_record.py`, run on 2026-10-20 (off the instrument)

**When.** Its output's file time is 2026-10-20T20:34:20Z. It was logged then in the bench's `LOG.md`, entry 33, and is logged here now, as this log's rule asks of every development run.

**What it read.** Check 2 at the pyramid, from M8.16's record: each slow group's projector output in each point's summary, against a tenth of the group's ceiling. It solves nothing.

**Script** SHA-256 `4eb117920717b0f76f34413624a0e03273eb5a68fb0bbc33b76fbbfb622b6bfb`. Inputs: M8.16's `run/out/P5.json` at MIT `deec830`, and `run/next_order_values.json` as of entry 6.

**Output:** `dev/pyramid_check2_from_record.out` `9a34ee168bc24df37a8b8a3feda9ac2f7273fbb2aba29292afcd5625a79e42f2`.

**Outcome:** check 2 passes at every cutoff, by 4.8 to 5.7 decades, with every projector usable. The largest `E_c` is 1.5×10⁻⁵ of its trigger. It informed no tolerance. It corrects terms v3's statement that check 2's estimate is not on M8.16's record, a correction for terms v4.

## 9. 2026-10-22T14:07:43Z: run `dev/plan_facts.py`, the facts `DRIVER_PLAN.md` v1 states (off the instrument)

**Why.** `DRIVER_PLAN.md` v1, development step 2's plan, states facts about M8.16's tree, its record and the pinned values. This script reads each one again from source, so the units can rerun the check.

**Script** SHA-256 `50625ae9e999132a5c5adc420d4fe5f5a9fc2f664131049856b6af406c0f780f`. Inputs: MIT `deec830`, with M8.16's folder read from its working tree and its record's history through git; `run/next_order_values.json` as of entry 7; this log; terms v3.

**Output:** `dev/plan_facts.out` `cbf1fa7fe4e73b823b912a78bc06ca4dc93ac39399e821780b7640e242cd5f82`.

**Outcome:** all nine facts hold, and both arms are red. Nothing is solved, and no sealed seed is constructed.
- **Fact 3:** on the record, K3's (a) failed only at its slow-band clause.
- **Fact 4:** check 1 holds at the recorded pyramid in both forms.
- **Arm A1:** removing the in-span group at one point breaks K2's matching, while the matching outside the in-span pair's class holds.
- **Fact 7:** `log_run` would repeat this log's last entry number.

`DRIVER_PLAN.md` v1: `bb46910434f600db57d873c84b7f73a51a0be753eff845fd3e62a728666d0a82`.

## 10. 2026-10-22T14:08:57Z: run `dev/plan_facts.py` again, with fact 2's message naming a git failure

**Why.** Against a copy of MIT that is not a git checkout, fact 2 failed as it should, but its line counted the failure as one moved file. It now says that git could not compare. Nothing else changed.

**Script** SHA-256 `c46f53286200c2665b3daf75b4dd2879a50248a6d3fb0a3c445928905969b40f`. Inputs as in entry 9.

**Output:** `dev/plan_facts.out` `eb3627eac874eff23e84bc72bb8e1b53cd3bb2d336f95063d67c8b500ed79347`.

**Outcome:** against MIT `deec830`, all nine facts hold and both arms are red, as in entry 9. Against the packet's copy, which has no git history, fact 2 fails with that reason, and every other fact and arm holds.

## 11. 2026-10-22T15:06:00Z: development step 2 begins: the tree, from MIT `deec830`

Blake, in his own words: "start the build, units first". The build follows `DRIVER_PLAN.md` v2, whose SHA-256 is `0169508518db486411bc4c50c4cb246916f3aa1107338ba03c8532b9e7e974b5`.

**Carried byte for byte.** Each file below is read from git at `deec830` and equals its line in M8.16's manifest, which reproduces M8.16's pin `a5f45173…`:
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
- `reference/m815/branch_C2a_R4.json` `c5266378170a2f425eb9423b0886f2a7e9db1628d4c5f80e0f70ac5aba888fde`
- `reference/m815/branch_C2b_R2.json` `25bcee62a88a05d03703c0a523621ac1e812ce09f8b7d0792d1ebd9fc129a716`
- `reference/m815/branch_C3_R4.json` `61c9d81899a80a8179582a60f52eb17fd36f71a42476374df275e28e3348d284`
- `run/name_targets.py` `8b4572054cd2d6cb80352d72d2ba2805b97411d21739116ee0cb6ed9d7d4cb1d`
- `run/pin_manifest.py` `4e7c7ab3eb36bafcb956c67751bdbc121767ba9b57bec89a8a108f5b67798580`
- `run/record_environment.py` `1494fb8afd942e74a646671fe16f03ad4d9b095ae62cd1be35a51b2eb3a10059`
- `run/targets.json` `6ca3854d15b5447ee2eab71670ee37b84d9bad60a4f06923d500aa72a52997af`

**The starting points of the changed files.** These are M8.16's versions, each equal to its manifest line, before any edit:
- `run/build_dry.py` `342553c3f06cf3f17934536b479cba789d554d68dca92bdeee74cb28f204a054`
- `run/cases.py` `e5e4396c748e8055b9679c84b52236ff16d9016c30d306c85f369e54a936504a`
- `run/checks.py` `31dc884bea7d9274949c00cc795073bb10519e8188e8a718c8c3f31ce31b8c83`
- `run/driver.py` `315df5646de2cc4332e9d2d3fbeef810f528d953e807bf368477475e1ba0727a`
- `run/test_guard.py` `b700f100d48006680930d5882e0a99c4cab179d1ff99d2982f55637da62f7720`
- `run/test_k3.py` `b769c6bb0c6a396b30e77382e90186b42632c3e6f1d1f0109415f6502ca5be7c`
- `run/write_guard.py` `f3534ab61f54fd7642c540475801e63e8915139477510b1519c4057317cf364f`

**Not copied:**
- M8.16's `dev/`, `reference/m815_targets/` and outputs;
- its `DRY.json`, `ENVIRONMENT.json`, `score_dry.py`, `test_claims.py` and its terms copy;
- its pins and freeze.

## 12. 2026-10-22T15:16:52Z: run `run/score_record.py`, the record regression (case: synthetic; no solve)

**Script** SHA-256 `01469629314e8b9ff4e8b7039ec99073926b1aa2747ce6ee5bccf952d1a5a566`. It reads M8.16's recorded outputs at MIT `87fc643`, through git, each against its `RUNLOG.json`, and scores them through `driver.checks_of`. The run/ code it imports, as of this run:
- `run/cases.py` `9fe0f7b928c65eeca81e6adbcc0c4ae22f3ac1b02deba92ee742e3731e4199e4`
- `run/checks.py` `3496347436fce7c768969a97387992eff401ba1781b6e95c60e3b9eeafada47e`
- `run/driver.py` `8a35c1cc357f40551957c4e2605bbec0fdf9be9c09040918bc2482f1ada92ba6`
- `run/seeds.py` `6223c6d7d8891b7941bc4d7128168e7d0b9f659419d21f3b22b4a3e80fccd55d`

`instrument/` is as entry 11 lists it; the values file is `run/next_order_values.json` as of entry 7.

**Output:** `run/score_record.out` `46ace07d27e2caeb592ef10fe33e3c83d70097b73a9ccdbc1810a011dc5c260c`, kept as `dev/runs/006_score_record.out`.

**Outcome:** all eight claims, derived before the run, hold. It computes no verdict.
- The serialized cases equal the recorded ones on every M8.16 field.
- The controls' K1, K2 and K4 pass, as recorded.
- At the pyramid, the bar's c2 and c3 over kappa s_g equal the landed `next_order_check.py`'s printed record values, digit for digit, at every cutoff, for the quartet and the Krein-positive pair: 12 comparisons, the round-off imaginary parts included.
- The bar passes under both forms of check 1.
- Check 2, by exact index association, equals entry 8's margins to the 0.1 decade printed, 4.8 to 5.7 decades.
- K3 reads "resolved", with (a) at every cutoff, and K4 passes.

The first launch stopped on a NameError in the script's own hash comparison, before reading any case; the line was fixed, and this run followed.

## 13. 2026-10-22T15:16:52Z: the plumbing pass: `run/driver.py --dry --cutoffs 12 16 20`, then `run/score_plumbing.py` (case: dryrun)

**What ran.** The driver as of entry 12, on `run/DRY.json`: C1, C2a, C2b, C3 and C2a/R5. `DRY.json` was written by `run/build_dry.py`, whose SHA-256 is `1234a87b63a053047485e76ffe757e514c048487e46a5d253bab4fa4042a722b`; `DRY.json`'s is `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`. It exited 0 in 124 s, ending 2026-10-22T15:16:15Z.

**The scorer** SHA-256 `93d9050b0b081fb528287274bf855034406f9b9deff961a6da8741f24b4f05a3`. Its claims were derived before the run.

**Outputs,** in `run/dry/plumbing/`, the small ones kept as `dev/runs/007_plumbing_*`:
- `driver.out` `60c79083237a04cbd041e9bca032a161fc665b114cbeef9e42c51f5ea564dbb9`
- `GATE.json` `e6f5243cc11fad6dd9ed78ab56bc22eca14468c5ad59cc755cddfae9a88e0fad`
- `VERDICT.json` `51e77e50c5ff52bedb21ee6eadc380f4740567a62f4adaa6208cf53942954086`
- `RUNLOG.json` `0e4284d8c54039b4d08ddf9938d3359485164a330c85b9faff4876db8c948609`
- `C1.json` `8dfb1caa9d3f72c6b4dccf7946a4588538f19c7c5ca0024de9d4b9cb96c916e2`, as `RUNLOG.json` records it
- `C2a.json` `615811dbb6e52035dcfc028e563fcadc8e9a31c544ba08322087a79f39a17cd2`, as `RUNLOG.json` records it
- `C2b.json` `64eaad55e858d70e7f6bd5fd60986da7c1f678fc7a0e6dc06f69cd89b5aeb918`, as `RUNLOG.json` records it
- `C3.json` `70e576216288e3cf285cd949756f5198434109a02b82e29ec5ef195732a5941c`, as `RUNLOG.json` records it
- `C2a_R5.json` `e1d2879e21fc2e149fe5f26a6c910d4ef653ede8cbc8c60d29fb03211d465802`, as `RUNLOG.json` records it
- `run/score_plumbing.out` `538f9603209e5f7545d01ceb76eb435f9e8b0e6966e39544220f1b928287db8e`, kept as `dev/runs/007_score_plumbing.out`

**Outcome:** all four claims hold, and the arm is red. Every case completed, with its seed checked at every cutoff and every point accepted; the gate record shows the pyramid absent, and the verdict reads incomplete. At these cutoffs, which the run never uses, K4 fails on C2a, C2b, C3 and C2a/R5 for want of convergence, unscored; the pass records each stop and continues, by design.

## 14. 2026-10-22T15:41:35Z: development step 2 built: the run/ scoring code and the three frozen-text tests, on the final tree

The build follows `DRIVER_PLAN.md` v2 (entry 11). `instrument/` and `reference/m815/` are as entry 11 lists them, byte for byte M8.16's.

**run/, every file:**
- `run/DRY.json` `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`
- `run/build_dry.py` `1234a87b63a053047485e76ffe757e514c048487e46a5d253bab4fa4042a722b` (changed from M8.16's: +6 -6 lines)
- `run/cases.py` `ec0a99123c34bc837c1dc07a2c0ad958d3a5f49e9dd4597f2b4f4dd2c32fe85b` (changed from M8.16's: +106 -11 lines)
- `run/checks.py` `3496347436fce7c768969a97387992eff401ba1781b6e95c60e3b9eeafada47e` (changed from M8.16's: +227 -35 lines)
- `run/driver.py` `8a35c1cc357f40551957c4e2605bbec0fdf9be9c09040918bc2482f1ada92ba6` (changed from M8.16's: +20 -238 lines)
- `run/freeze_block.py` `0de0304f237b53d61f38006e5f6f002a85213f672d3ebcff5dd3cfd99b931b1a` (new)
- `run/name_targets.py` `8b4572054cd2d6cb80352d72d2ba2805b97411d21739116ee0cb6ed9d7d4cb1d`
- `run/next_order_values.json` `b05fff5ddd71c29c79318b6257f940c6035d7c954f3bafa34a22080eecc00333`
- `run/next_order_values.out` `fc0821ecdf011190c19604ae146150a604e3ec25ac5a8ecc38a740afa84c2f55`
- `run/next_order_values.py` `4bf81a60beef1338c6da36b2d4c04f9d51b826322a0b1e9540769fa318f4028e`
- `run/pin_manifest.py` `4e7c7ab3eb36bafcb956c67751bdbc121767ba9b57bec89a8a108f5b67798580`
- `run/record_environment.py` `1494fb8afd942e74a646671fe16f03ad4d9b095ae62cd1be35a51b2eb3a10059`
- `run/score_plumbing.out` `538f9603209e5f7545d01ceb76eb435f9e8b0e6966e39544220f1b928287db8e`
- `run/score_plumbing.py` `93d9050b0b081fb528287274bf855034406f9b9deff961a6da8741f24b4f05a3` (new)
- `run/score_record.out` `46ace07d27e2caeb592ef10fe33e3c83d70097b73a9ccdbc1810a011dc5c260c`
- `run/score_record.py` `01469629314e8b9ff4e8b7039ec99073926b1aa2747ce6ee5bccf952d1a5a566` (new)
- `run/seeds.py` `6223c6d7d8891b7941bc4d7128168e7d0b9f659419d21f3b22b4a3e80fccd55d` (new)
- `run/targets.json` `6ca3854d15b5447ee2eab71670ee37b84d9bad60a4f06923d500aa72a52997af`
- `run/test_constants.out` `943e2157a4e457401371d221f5013e010d5d62a89439b6f461615858738e6f86`
- `run/test_constants.py` `bfbfc01cf9082e451460f125a94f1b12e6b046a6206b104014b19d4e83e5194a` (new)
- `run/test_guard.out` `d0305afa606f45d7a87de90e6bd37a80366d9fdf6e41e9df5d8932e63e7053e5`
- `run/test_guard.py` `f962431055cb532d64046a32453561ddfe66db96526e2dd42bcc540e465806e3` (changed from M8.16's: +156 -42 lines)
- `run/test_imports.out` `41334b995e9b958451deffd4867c154b7e25bee1a527fa14f7a646df042023d0`
- `run/test_imports.py` `5ad8a0988aed08bd738a517d809a970dc4271358ad97e7fb9d4e8f14c4ea4eed` (new)
- `run/test_k3.out` `7d6faa272e7d180ac3baaa3f9c76f6fa2ca1c5285143ad2ecbdff4d5fe2fba4b`
- `run/test_k3.py` `8adccbcb7236e9a087c0e32dcf6e8d9144044d8bcedc6d8a06093a11c13246cb` (changed from M8.16's: +20 -120 lines)
- `run/test_verdicts.out` `89416d470f3c73e77452d0badd3e701070fd2667448544a8cf9f5844b23bb1f1`
- `run/test_verdicts.py` `78097e817d32b9e56b6d03b12a687ce629742ca7e17577010f2f6b6676dc4419` (new)
- `run/write_guard.py` `9b86f4a9259e3ccf559947ce52e23c3cfbf1c00d810a9e33d632e5442f346e45` (changed from M8.16's: +49 -7 lines)

**Where the build departs from the plan v2,** each for the units:
1. The new constants (the ceiling's factors, the tenth, check 4's floor, the points) sit in `checks.py`, which reads them, as `AXIS_MIN` does. `write_guard.py` reads them from there. The plan's item 1 placed them in `cases.py`.
2. `test_guard.py` reads M8.16's development outputs, its log and `EXPECTED_V0.md` from M8.16's folder in MIT's history at `87fc643`, in tests 6, 11, 12 and 13, as `test_k3.py` does. The plan named this for `test_k3.py` only.
3. `test_guard.py`'s test 13 loses its reading of E7, which left with E7: 81 of M8.16's 84 results are carried.
4. `test_verdicts.py` leaves the driver paths of the stops and the resume to `test_guard.py`'s tests 9 and 10, which run them through M8.16.1's driver, and asserts the verdict's text at each stop. The plan listed them under `test_verdicts.py`.
5. `cases.py`'s `DRY_LADDER`, M8.16's dry ladder for its E3 to E5, is removed with those claims. `checks.k3_probe`, M8.16's E2 probe, stays as an unchanged function, now unused.
6. `test_imports.py` takes the seed check's record as an optional argument. Until step 3, it tests the seeds line on a synthetic record of the same form, as the plan's "before the seed check exists" foresees.
7. Two rules of the tests' own, each printed with its results:
   - the reverse scan's structural contexts: subscripts and slices, the exponents 2 and 0.5, 0 and +-1, and range bounds;
   - the forward test's section references after a section sign, which are not values.

**What the tests found, for terms v4:** `test_constants.py`'s reverse scan lists exactly the known hits as v4's FROZEN VALUES items:
- K2's slow-band factor 2;
- the band-edge guard's half;
- `real_orthonormal`'s cut, 1e-6;
- K6's boundary at eps 2;
- C1's four thresholds, 1e-15, 1e-14, 1e-10 and 1e-12;
- check 4's floor, which `FROZEN.json` holds and v3 does not list.

## 15. 2026-10-22T15:41:35Z: the final runs of step 2, on the tree of entry 14

**In order,** from 2026-10-22T15:37:39Z to 15:40:00Z, each with an exit status of 0 and an empty stderr, each script as entry 14 hashes it:
1. `run/build_dry.py`, writing `run/DRY.json`, unchanged: `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`.
2. `run/test_guard.py MIT_REPO` (case: synthetic): 0 failed of 105, in 9 s.
3. `run/test_k3.py MIT_REPO`: 0 failed, every carried claim.
4. `run/test_verdicts.py MIT_REPO`: 0 failed of 53, the four mutations red.
5. `run/test_constants.py MIT_REPO ../m8_16_1_task_details.md`, against terms v3: 0 failed, the five arms red.
6. `run/test_imports.py`: 0 failed, both arms red.
7. `run/score_record.py MIT_REPO`: 0 of 8 claims failed; no verdict is computed.
8. `run/driver.py --dry --cutoffs 12 16 20` (case: dryrun), in 126 s, after the first pass's outputs were moved to `dev/runs/007_plumbing/`, since the driver would resume from them.
9. `run/score_plumbing.py`: 0 failed, its arm red.

MIT_REPO is the worktree at `deec830`.

**Outputs,** kept as `dev/runs/008_*`:
- `run/test_guard.out` `d0305afa606f45d7a87de90e6bd37a80366d9fdf6e41e9df5d8932e63e7053e5`
- `run/test_k3.out` `7d6faa272e7d180ac3baaa3f9c76f6fa2ca1c5285143ad2ecbdff4d5fe2fba4b`
- `run/test_verdicts.out` `89416d470f3c73e77452d0badd3e701070fd2667448544a8cf9f5844b23bb1f1`
- `run/test_constants.out` `943e2157a4e457401371d221f5013e010d5d62a89439b6f461615858738e6f86`
- `run/test_imports.out` `41334b995e9b958451deffd4867c154b7e25bee1a527fa14f7a646df042023d0`
- `run/score_record.out` `46ace07d27e2caeb592ef10fe33e3c83d70097b73a9ccdbc1810a011dc5c260c`
- `run/score_plumbing.out` `538f9603209e5f7545d01ceb76eb435f9e8b0e6966e39544220f1b928287db8e`
- `run/dry/plumbing/C1.json` `f146a03a2a6c5f5dfcc33e159a47c4078d02b91aacea5ea359d94744022a374d`
- `run/dry/plumbing/C2a.json` `3132484968eb915d7435cb4816e7d641cff4542334bf9729286926a0e6eb31e1`
- `run/dry/plumbing/C2a_R5.json` `274d0c525135457714bc4b9cbb4f5e6f95136649f5c37ee308bbba6bfbb7d26d`
- `run/dry/plumbing/C2b.json` `7ae4cc8b2ad689756c44c38be7bbe123c81e98a3b4b12ca3bccf72d9dbe07a97`
- `run/dry/plumbing/C3.json` `89e219648de0d164f2c43b6118afeede5d4f9110e354cfb03f87531064a31dc8`
- `run/dry/plumbing/GATE.json` `b8dc29b21354d4610e878f19e94ca81ae7ec62a7a8fa5a32852f3a07d198467b`
- `run/dry/plumbing/RUNLOG.json` `8e259bd228bd7db2d7d129c536717dd5d433c1e6071710156d52bde2f116ebfc`
- `run/dry/plumbing/VERDICT.json` `51e77e50c5ff52bedb21ee6eadc380f4740567a62f4adaa6208cf53942954086`
- `run/dry/plumbing/driver.out` `82abbca38e600ff810a137e837ace89c037d8ebd8400d23bcd380be5276aef8f`

**Determinism.** The two plumbing passes' case records, this one and entry 13's, are identical in every field apart from their timing fields (`seconds`, `setup_seconds`, `seconds_record`): C1, C2a, C2b, C3 and C2a/R5.

## 16. 2026-10-22T16:23:01Z: the units' fixes to step 2's build, and their reruns

Blake, in his own words: "keep going if/when gucci". UA: HOLD on two fail-closed corrections. UB: GO after one fix, with two NITs. Every point was verified at source.

**The fixes:**
1. **Frozen-mode identity across the cutoffs (UA).** The bar reads a group by its place at each cutoff, and `cases._next_order` tied each cutoff on its own, so a values file with its groups in another order at one cutoff passed the tie. The loader now refuses unless every cutoff holds the same groups, in the same order, by spectrum index and bar membership.
2. **Bar membership, independently of the values file (UA).** `cases.registered_under_bar` reads the terms' rule from the frozen mode alone: at the pyramid, the quartet and the Krein-positive pair; at every row, T5J and the C3 ray, every predicted slow group. The loader refuses any other membership. `write_guard.next_order_values` now runs the loader on the file it is given, so the freeze checks the file itself, and not only its agreement with `cases.py`, which is built from the same file.
3. **`test_constants.py`'s A1 and A2 (UB).** Claim 1 names an absent `FROZEN.json` entry as a failure line, and each arm requires that line, with no `except`.
4. **`test_imports.py`'s environment (UB's NIT).** It uses a fixed environment for its test `ENVIRONMENT.json` and the block's reading again alike, since `record_environment.read()` reads macOS's `sw_vers` and `sysctl`.

**New arms,** in `test_guard.py`'s test 17 (UA), each with the hash recomputed:
- T2/R4's two groups exchanged at N = 24, their values and individual ties intact;
- P5's quartet outside the bar at every cutoff.

Each is refused by the freeze guard, and by `cases.py`'s loader before any scoring, each with its reason.

**Disclosed (UB):** `checks.k3_probe` and the driver's `dryladder` branch are now both unreachable. That is harmless; each is M8.16's, unchanged.

**The changed files:**
- `run/cases.py` `1e331a6d90421a0261225db3c5e14866994931722abb45e597d58f578ca93081`
- `run/write_guard.py` `dcd3d89322e60b94138096287e47f40e62a8c2cbe941efbf15dd806c877c3c96`
- `run/test_guard.py` `5299bd488e49b042e71bf77ba59de7cf5112be13acadc2885a061cc796c2c723`
- `run/test_constants.py` `c350365ae473cda538512d7ff1eedfae78ab46685dcdcca496d5e7f0a5552391`
- `run/test_imports.py` `e448e3101d6f12edb41f54f86ed48149c68357f267e2322e096d68c70fd910b8`

**The reruns,** of everything that reads a changed file, each with an exit status of 0 and an empty stderr; outputs kept as `dev/runs/009_*`:
- `run/build_dry.py`: `DRY.json` unchanged;
- `run/test_guard.py`: 0 failed of 109;
- `run/test_verdicts.py`: 0 failed of 53;
- `run/test_constants.py`: 0 failed, A1 and A2 red because claim 1 names the missing entry;
- `run/test_imports.py`: 0 failed;
- `run/score_record.py`: 0 of 8 claims failed; no verdict is computed.
- `run/test_guard.out` `108903eae82f80b9333e13bea284320eb5e739a904a9c0e50cc0cb3d0a7cc76b`
- `run/test_verdicts.out` `89416d470f3c73e77452d0badd3e701070fd2667448544a8cf9f5844b23bb1f1`
- `run/test_constants.out` `3a763c70f6d49748ecce4f6b543d4f3593bf16375276483f09c35cb78ddbfd27`
- `run/test_imports.out` `41334b995e9b958451deffd4867c154b7e25bee1a527fa14f7a646df042023d0`
- `run/score_record.out` `46ace07d27e2caeb592ef10fe33e3c83d70097b73a9ccdbc1810a011dc5c260c`

`test_k3.py` and the plumbing pass read none of the changed files, so their entry-15 records stand.

## 17. 2026-10-22T16:26:29Z: step 3, the seeds: run `dev/seed_check.py` (case: seedcheck), then `run/test_imports.py dev/seed_check.json`

**The script.** It is M8.16's `dev/seed_check.py` at MIT `deec830`, SHA-256 `b6acf0149ab3b4cd932586e4289d6e8180459d2c8148c03706fd3930ef815501`, with its claims 1 to 6, carried to M8.16.1's seventeen seeds:
- 12 sealed: M8.16's ten, C3R/R4 and T5J/R2;
- the new ones built through `run/seeds.py`;
- their exact values from section IV's rows for the C3 ray and for T5's line {7/2, -3/2}, which T5J shares.

It writes its record, `dev/seed_check.json`: each seed's values, and every module file under the tree that this process and its child process loaded. It writes no development log entry. Its claims were derived before the run (its docstring).

**Script** SHA-256 `779151b97357428c9002cd7a8860e44553d5688f2e24bdef1429cf82692285da`.

**Outputs,** kept as `dev/runs/010_*`:
- `dev/seed_check.out` `853cebe58f3270b024cac677a0f181c23b023d1e9e0941265c04d525993c1ee7`
- `dev/seed_check.json` `a36c9f9e822cb83a554feab9d6b6fd2b46d885d42183a07afebe989eb110ce9f`

**Outcome:** all six claims hold for the 17 seeds.
- **The new seeds:**
  - C3R/R4: Q 1.184615384615388 against 77/65, criticality 4.2e-16, (k, r_u) = (4, 2);
  - T5J/R2: Q 1.6923076923076936 against 22/13, criticality 1.5e-16, (k, r_u) = (6, 4).
- **The guards:** every sealed seed is refused outside a seedcheck process, 12 of 12. In this one, all eight solver paths refuse, and no sentinel fired.
- **The record:** 12 files loaded here and 12 in the child process: M8.16's eleven instrument files and `run/seeds.py`.

**The first run,** minutes before, gave the same values for every seed. Its record listed the script itself among the loaded files, though the script sits outside the manifest, as M8.16's did, and the record names it under `script`. The record now keeps the script out of `loaded`. This run's outputs replaced the first's.

**Then `run/test_imports.py dev/seed_check.json`,** on the real record: 0 failed.
- Claim 1 holds for the driver, `write_guard.py`, `freeze_block.py` and the seed check, whose own file equals the SHA-256 its record and the block give it.
- Claim 2 holds: the seeds line names exactly the record's 12 files.
- Both arms are red.
- `run/test_imports.py` gained the seed-check entry: SHA-256 `f8e0c9886f2e8e422dea17546da64a2525d67095d8539f43405ec20ac417434a`.
- Its output: `run/test_imports.out` `b3b408f4e16e51fb3340adbc0fa5e3e8f482815bd6713a8deb42980c04815879`.

## 18. 2026-10-22T16:52:01Z: the first run of entry 17's seed check, on its own record (UB's NIT)

**When.** Its result reached the session at 2026-10-22T16:25:14Z, minutes before entry 17's run.

**Its script** is not kept. Its SHA-256 is `c0aa8664efd70917bf5d9ef4f133a344db61ed350a62fb19f94b6e3b0ad6cf95`, reconstructed rather than read from a copy:
- the step-3 packet holds entry 17's script exactly, `779151b9…`;
- undoing that script's one later edit, which keeps the script out of its own record, gives this one.

**Its outputs,** `dev/seed_check.out` and `dev/seed_check.json`, were overwritten by entry 17's run. They are lost as files. The session's transcript holds its printed output:
- all six claims passing;
- the same values for every seed;
- its record's file lists: 13 here, the script itself among them, and 12 in the child.

## 19. 2026-10-22T16:52:01Z: claim 7, the new seeds' identity (UB), and the seed check run again (case: seedcheck)

Blake, in his own words: "keep going if/when gucci:", with both units' replies on steps 2 and 3.
- **UA:** GO on both steps, with no changes.
- **UB:** GO on step 2, and GO on step 3 after one claim. C3R's checked values are the pyramid's, and T5J's are T5's, so nothing in the record told either new seed from the orbit it shares them with. UB checked both points.

**Claim 7,** as UB worded it, verified at source and adopted:
- `seeds.REPS` equals, component for component, the representatives `run/next_order_values.py` computed C3R/R4's and T5J/R2's frozen values from. They are read from that script's own source.
- Each new seed differs from the orbit whose Q and (k, r_u) it shares by its Majorana root multiplicities, computed exactly from those components:
  - C3R/R4 [2, 1, 1, 1, 1] against P5's [1, 1, 1, 1, 1, 1];
  - T5J/R2 [1, 1, 1, 1, 1, 1, 1] against T5/R2's [2, 1, 1, 1, 1, 1].
- The polynomial is the terms' certificate's, in which T5 reads z^7 - 7 z^2 and T5J z^7 + 7i z^5 - 7 z^2 + i.
- Two arms, each red:
  - T5J's v_3/2 component taken real in a copy of `seeds.REPS`;
  - T5's components read in T5J's place.

**Script** SHA-256 `c7d5d597af6d8165c48f33b8985ae6ed1863453fac0b15947ce30c4473168ea4`.

**Outputs,** kept with the script as `dev/runs/011_*`:
- `dev/seed_check.out` `0133d0e354da378de1b589f460b9c3cc5e8ecb6804667a3b7fe0c09b2a95daff`
- `dev/seed_check.json` `2ed59da10f1ba1ccaff30a7a188d754e14e811747225ab12dbf9290c0385ad03`

**Outcome:** all seven claims hold, with every seed's values as entry 17 gives them.
- An earlier run, minutes before, had claim 7 and not its arms. It gave the same results, and its outputs were replaced by this run's. Its script differed from this one only by the arms, and is not kept.
- `run/test_imports.py dev/seed_check.json` on the new record: 0 failed. Its output is unchanged from entry 17's, `b3b408f4e16e51fb3340adbc0fa5e3e8f482815bd6713a8deb42980c04815879`.

**The units' reruns** (their replies), recorded as UB asks:
- UA reran the seed check's claims 1, 3, 4 and 6, and `test_imports.py`.
- UB reran all six commands and the seed check, on Linux, against a full clone.
- Both built the sealed seeds in a seedcheck process, within amendment 2's scope, with nothing solved.

## 20. 2026-10-22T17:14:31Z: step 4's plan; run `dev/ladder_plan_facts.py`, the facts `LADDER_PLAN.md` v1 states (off the instrument)

Blake, in his own words: "keep going if/when gucci:", with both units' replies on steps 2 and 3 (entry 19). Step 4 begins with its plan for the units: amendment 5's ladder, `R5`'s coherent branch along M8.15's grid to `ε = 32` (entry 1). Nothing in the plan is built or run before their GO and Blake's word.

**The plan.** `LADDER_PLAN.md` v1, SHA-256 `0b53eaafe5b349c9b274f4b0d94e9354f8732c3835f3c51e3a7a3cba26c3b1d8`.

**The draft of `BOUNDARY.md`,** with amendment 5, goes to the units with the plan. It is written into this folder only after their review, and its time stamps are its drafting time. SHA-256 `a8b0a4380f6dfb276cec38d0b1cf3f1c3821d02eebf4fb6e18c59ecdbe4a6db3`.

**Why the script.** The plan states facts about:
- M8.16's record and its split;
- this tree;
- the budget's inputs.

This script reads each one again from source, so the units can rerun the check. It solves nothing, and constructs no sealed seed.

**Script** SHA-256 `b788ab0cd0daca279818ef3c6cb1694b9742ad51783707cacbf4ffedfdb8ae07`. Inputs:
- MIT, through git at `deec830` and `87fc643`;
- `run/DRY.json`;
- `dev/runs/008_plumbing/`, the plumbing pass of entry 15;
- this machine's environment, read now.

**Output:** `dev/ladder_plan_facts.out` `c5b89b165a208e2e397bce6d3e503ee4a5592fad6471e837e9fd1bb92c16ffa3`, kept with the script as `dev/runs/012_*`.

**Outcome:** all nine facts hold, and the arm is red.
- **Fact 5:** this machine's environment equals the registered run's, but for the time it was recorded.
- **Fact 6:** the plumbing pass's C2a/R5 point at `N = 16`, `ε = 0.25` equals the registered run's in all 13 of its fields but its two timings.
- **Fact 8:** C2a's `R4` ladder kept its row at all 39 points to `ε = 72`.
- **Fact 9:** `checks.k2` holds at all 12 of the registered sample's points. M8.16 never scored K2 at C2a/R5.
- **The estimate:** about 2 h at the registered run's rates, on C2a's `R4` evaluation counts along the same grid (INFERRED).

It informed no tolerance.

**Two earlier runs** of drafts of this script, minutes before, each passing:
- the first had facts 1 to 8 and the arm;
- the second added fact 9.

In both, fact 4 did not yet read M8.15's outputs. This run's outputs replaced theirs, and their scripts are not kept.

## 21. 2026-10-22T17:16:07Z: run `dev/ladder_plan_facts.py` again, with fact 5 failing closed off macOS

**Why.** `record_environment.read()` calls macOS's `sw_vers` and `sysctl`. Off the recorded machine, fact 5 raised, and the script stopped before facts 6 to 9, so a unit rerunning it on Linux could not read them. Fact 5 now fails with that reason, and the other facts still run. Nothing else changed.

**The fail-closed path,** checked first. A harness replaced `record_environment.read` with one raising `FileNotFoundError` for `/usr/bin/sw_vers`, as off macOS, and ran the script through `runpy`. Fact 5 failed with that reason. Facts 1 to 4 and 6 to 9 held, the arm was red, and the exit status was 1, with "1 failed". The harness is not kept, and its output was replaced by the run below.

**Script** SHA-256 `4de2eb1435247ea788bd9d472dff54789e4d344813824c95345c16d4e17669dc`. Inputs as in entry 20.

**Output:** `dev/ladder_plan_facts.out` `c5b89b165a208e2e397bce6d3e503ee4a5592fad6471e837e9fd1bb92c16ffa3`, byte for byte entry 20's. It is kept with the script as `dev/runs/013_*`.

**Outcome:** on this machine, all nine facts hold and the arm is red, as in entry 20.

## 22. 2026-10-22T17:57:14Z: the units on step 3's last item and step 4's plan; their fixes, verified at source; plan v2

Blake, in his own words: "keep going if/when gucci:", with both units' replies.
- **UA:** CONFIRM on step 3. HOLD on step 4 until two wording corrections are in: what a failure of claim 4 or 5 establishes, and the calibration's boundary in amendment 5. One NIT: restore the plumbing `DRY.json` after the ladder.
- **UB:** CONFIRM on step 3, with one NIT on the log. GO on step 4 after three fixes: amendment 5's reading, a guard and tests for the base-case rule, and claim 2's reach past the sample. Two NITs on the draft `BOUNDARY.md`: its time stamps, and the citation for both units' agreement.
- **Their reruns.**
  - UA ran claim 7 and both its arms.
  - UB, on Linux against a full clone, reproduced:
    - the seed check's seven claims, with both of claim 7's arms red;
    - `test_imports.py`'s output, byte for byte entry 17's;
    - `ladder_plan_facts.py`'s exit 1, with fact 5 failing closed and the other eight facts holding, as entry 21 says.

**Verified at source and adopted:**
1. **Amendment 5's reading (UB, UA).** M8.16.1's terms fix `instrument/` byte for byte (§ THE INSTRUMENT: UNCHANGED), and the calibration's constants are in `instrument/linear.py`. Amendment 3's note let M8.16 refit when a calibration condition failed; inside M8.16.1 that reading is not available. `BOUNDARY.md` takes UB's text for the reading and, after it, UA's paragraph, each verbatim. `LADDER_PLAN.md`'s outcome for claim 3 follows, with both units' wording.
2. **What a failure of claim 4 or 5 establishes (UA).** v1 read any failure as a defect of the code. At ε = 0.5, 1 and 2 the path differs from the registered run's, and a failed K4 trend could be a genuine reading. UA's text replaces v1's, verbatim.
3. **The base-case rule's guard (UB).** `driver.load`'s second test reads the full name against `branches.SEALED`. That test matches neither a `:ladder` name nor either new seed. So under the base-case rule, a dry case `P5:ladder` with its admission field edited to a GO name would pass `load`, and only the seed constructor would refuse its sealed base. `load` now reads the base name against `branches.SEALED` and `seeds.NEW`, and `test_guard.py` gains UB's two tests.
4. **Claim 2's reach (UB).** K2's slow band is twice the largest εκsτ. This was read again from M8.16's `dev/d7_ladders_C2a.json` at `deec830`. Its `slow` field is each slow eigenvalue over its reached ε; here it is divided by κτ, with κ = 1/(8√48 · 1288/1287). At N = 32, the five slow modes sit at:
   - 0.993 to 0.995 of εκτ at ε = 0.25;
   - 0.804 to 0.850 at 8;
   - 0.482 to 0.573 at 32, as UB says.

   K2 is now scored to ε = 2 and reported beyond it.
   - **Adjudicated:** UB's text scores K2 "at the sample's points" and reports it "beyond ε = 2". The three grid points inside the sample's range, 0.354, 0.707 and 1.41, are scored too, since that range is the small-amplitude one.
5. **Both units' agreement (UB's NIT).** The scope check v3 (2026-10-20), § 7, "The units' leans on v1", item 5, records it:
   - UA: "add C2a/R5's full ladder to the new GO list, with no target exposure and no credit";
   - UB: "run it: the only R5 acceptance evidence available without unsealing a row".

   The scope check is a bench file and does not land with this folder, so `BOUNDARY.md` cites this entry, which quotes it.
6. **The time stamps (UB's NIT).** `BOUNDARY.md`'s time stamps are the time it is written, at the build.
7. **`DRY.json` (UA's NIT).** After the ladder's outputs are archived, `build_dry.py plumbing` restores it, byte for byte, checked against entry 15's SHA-256.
8. **The log (UB's NIT).** Entries 19 and 20 disclose earlier runs whose scripts and outputs were not kept, one of them a seed-check run that built sealed seeds within amendment 2's scope. From this entry on, each run's script and outputs are copied to `dev/runs/` before the next run starts.

**The plan.** `LADDER_PLAN.md` v2, with items 1 to 8 folded in, SHA-256 `9b761ed80f778430b62f7f592e73bf91722c65bf00a35568796ef19f5de1e226`. The base-case rule lands as `seeds.base`, which the seed check reads, so the seed check runs again with the build.

Next, under Blake's "keep going": the build, then the ladder.

## 23. 2026-10-22T18:03:37Z: step 4's build: `BOUNDARY.md` written; the changes; the scorer, logged before the run; the reruns

Under Blake's "keep going", with the units' conditions of entry 22 met.

**`BOUNDARY.md`, its first write,** by exclusive create, at 2026-10-22T18:01:46Z, the time both of its stamps carry (UB). SHA-256 `934cca3d44de6200380dde4ccd87c885f47693223a7c399676626413d995432d`. It is the draft the units reviewed (entry 20), with entry 22's items 1, 5 and 6:
- the reading paragraph is UB's text, followed by UA's, each verbatim;
- both units' agreement is cited to entries 1 and 22;
- the time stamps are the writing time.

It is not edited after this write.

**The changes** (`LADDER_PLAN.md` v2, How it runs). The starting points are the files the units reviewed, in `devstep4_review_v1`:
- `run/seeds.py` `6223c6d7d8891b7941bc4d7128168e7d0b9f659419d21f3b22b4a3e80fccd55d`
- `run/cases.py` `1e331a6d90421a0261225db3c5e14866994931722abb45e597d58f578ca93081`
- `run/driver.py` `8a35c1cc357f40551957c4e2605bbec0fdf9be9c09040918bc2482f1ada92ba6`
- `run/build_dry.py` `1234a87b63a053047485e76ffe757e514c048487e46a5d253bab4fa4042a722b`
- `run/test_guard.py` `5299bd488e49b042e71bf77ba59de7cf5112be13acadc2885a061cc796c2c723`

After the changes:
- `run/seeds.py` `11916c7ccd9c27583933c78b8d79f5c9ed0472c4ade946312acf4cf0bd80d87c`
- `run/cases.py` `cfc3663dc5c9ac469335ca71d8884312504362c455b6291b758d45b92ab25e9c`
- `run/driver.py` `6fad387effeb2ac805a09f485a11037b7575f511558776d0461dd8c6f5b622f9`
- `run/build_dry.py` `34de8225eab09c8708b67e09c8bb0308e731dabee4a78b4fd57a6fca9e0cf55c`
- `run/test_guard.py` `0ad237f2c9220ef14344f057ea1cc8737bd2b109ff59d27e64380e9d3f0c36a2`
- `run/score_ladder.py` `d5fe1b18946bc355a6152437815e0ba82bc897ef6bdd85a8a248ec7127d49153`, new.

What they do:
- **The base-case rule.** `seeds.base` is the rule's one home: a development ladder `X:ladder` is `X`'s branch, and any other name is its own. `cases.admission` and `cases.serialize` read it, and so does the driver's `run_case`. The rule replaces M8.16's special case for `C2a:ladder`, and no `C2a:ladder` remains in `run/`.
- **`driver.load`** refuses a dry case whose base is in `branches.SEALED` or `seeds.NEW`, whatever its admission field says (UB).
- **`driver.checks_of`** reads a `dryladder` case with `checks.check_control`, the `R5` control's K1 and K4.
- **`build_dry.py`** writes either list by name. `plumbing`, the default, reproduces `DRY.json` byte for byte; `ladder` writes amendment 5's one case.
- **`test_guard.py`** gains test 18, UB's two tests of the base-case rule.
- **`score_ladder.py`** scores the plan's five claims with `checks.py`'s own functions, and has four arms.

**The scorer, checked before the run.** Its functions ran in memory on the registered C2a/R5, with no output written:
- claim 5 of the record against itself is empty;
- claim 1 names the 33 ladder points the record lacks;
- claim 3's readings at the record's 12 points are M8.16's entry 202's: the largest coefficient 0.0289, the largest lift 7.3 u, the smallest genuine eigenvalue 4.4×10⁻⁶ ‖L‖;
- arm A4 is red.

**The reruns,** of everything that imports a changed file, one at a time. Each exits 0 with an empty stderr, and each script and its outputs are kept as `dev/runs/014_*` before the next starts (UB):
- `build_dry.py plumbing`: `DRY.json` unchanged, `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`;
- `test_guard.py`: 0 failed of 126, test 18's 17 checks among them. Its arm shows M8.16's second test letting all four edited ladder lists through. Output `6d9f69f0b665787df7a814e7361c2597fdb40005036cdd588ef7c4d18f0fb4b3`;
- `test_verdicts.py`: 0 failed of 53;
- `test_constants.py`: every claim holds, its reverse scan finding no new literal, and its five arms are red;
- `score_record.py`: 0 of 8 claims failed;
- these three outputs are byte for byte entry 16's;
- `dev/seed_check.py`, which reads `run/seeds.py`: all seven claims hold, with both of claim 7's arms red, in 3 s. Its output and record are byte for byte entry 19's;
- `run/test_imports.py dev/seed_check.json`: 0 failed, byte for byte entry 19's.

**The plan's facts** (entries 20 and 21) describe the tree before this build. Facts 3 and 4 read the special case and the `dryladder` branch it replaces, so a rerun now reads them otherwise, by design.

Next: `build_dry.py ladder`, then the ladder, `driver.py --dry`, under `caffeinate`.

## 24. 2026-10-22T20:41:43Z: amendment 5's ladder: run `run/driver.py --dry` on the ladder's list (case: dryrun), then `run/score_ladder.py`; claims 2 and 3 fail at ε = 32

Blake, in his own words: "plugged in, do what you gotta do". The Mac was on mains power, where Low Power Mode is off.

**What ran:**
- `run/build_dry.py ladder` wrote `run/DRY.json`, the ladder's list, SHA-256 `37461fa5d9093aee77ac16d39a3a73200bd5ba2012022c41b11c6688ed224766`, kept as `dev/runs/015_DRY_ladder.json`.
- `caffeinate -i python3 -u -I -B run/driver.py --dry`, a sidebar task, ran from 2026-10-22T18:45:59Z to 2026-10-22T20:36:54Z, 6655 s of wall time.
  - It exited 0, on files that entry 23 logs, and its log records the tree's manifest, `55ccf8d4e9a45aacfbc73827619ffc9b84c8159512f27a8c93220f51f901fec5`.
  - The case took 6654 s: 36 s at N = 16, 833 s at 24 and 5784 s at 32. The plan's estimate was about 2 h.
- `run/score_ladder.py`, entry 23's, read the outputs: exit 1, with 2 of its 5 claims failing and its four arms red.

**Kept.** The outputs and the driver were copied to `dev/runs/015_*` before the scorer ran, and the outputs then moved out of `run/dry/`:
- `dev/runs/015_ladder/C2a_R5_ladder.json` `a3937aaf2d48796344810f68a594b7f66ae555ddfb59ed037cc3756a1dee2b43`
- `dev/runs/015_ladder/GATE.json` `3a200bf2d5d2fa92c2967ebd91bd315e46bcf1d5e3435a74dd246e148c45f20c`
- `dev/runs/015_ladder/RUNLOG.json` `c310e86a150ffa1bda82412698bc7a1b7162a107686252e7f55c6b71253faee3`
- `dev/runs/015_ladder/VERDICT.json` `43a0483d1d5c8226217da7264ee78f26985f855a67cab5ecafb243021ccd02a3`
- `dev/runs/015_ladder/driver.out` `561c5380f759aa9c6efebace739d1925b43e40336f20de655eb4e0b9b6bd72e7`
- `dev/runs/015_ladder_stdout.out`, the sidebar task's output, equal to `driver.out` line for line
- `run/score_ladder.out` `b1d92bbac7765e0df8a4272ad0e0b80da1d272af8f0b575267a444464a17ce46`, kept as `dev/runs/015_score_ladder.out`, with an empty stderr

**The claims:**
1. **Acceptance: holds.** All 15 points are accepted at each of N = 16, 24 and 32, 45 in all, with every seed passing.
2. **The row: fails, at ε = 32 alone.**
   - K1 holds at all 45 points, and K2 at every point to ε = 2.
   - Every record reads Elliptic, (0, 0, 0), with nothing unresolved.
   - The convergence rule reads 14 of the 15 points converged, Elliptic. At ε = 32 it reads Unresolved: "tested set at 2.28964e-15+2.49913j (+1): the set's count differs between cutoffs".
3. **The calibration's conditions: (a) fails, at one point.**
   - (a) At N = 16, ε = 32, the cluster coefficient is 0.0806, against (κ/G)/10 = 0.0667. Everywhere else it is at most 0.0603 (N = 16, ε = 22.6).
   - (b) holds: the largest lift is 7.8 u (N = 32, ε = 11.3), against 100 u.
   - (c) holds: the smallest genuine eigenvalue is 1.98×10¹⁰ u (N = 32, ε = 0.25), against 10⁵ u.
4. **K4's reading: holds.** The bar at 0.25 and the trend hold at each N, with the registered run's deviations at 0.25.
5. **The sample: holds.**
   - At ε = 0.25, each N's point equals the registered run's, field for field apart from its timings, and so do its reading and its identity record.
   - At 0.5, 1 and 2, the records' structure is the registered run's, and the slow eigenvalues differ from it by at most 4.4×10⁻¹¹, relative.

**The evidence at ε = 32,** read from the outputs, with nothing new solved:
- **Claim 2.** Two Krein-positive imaginary groups of size 1 sit at 2.47i and 2.4991i at N = 24, and at 2.47i and 2.4991i at N = 32.
  - At N = 16 they sit at 2.5139i and 2.5845i, each shifted from N = 24's by more than the pair's spacing.
  - So both N = 24 groups have the same nearest group at N = 16, their matches are not one to one, and the set they form counts differently there. The rule reads that Unresolved, by design.
  - The pair lies below half the band edge, 5.01, so it is tested; it is not among the slow modes.
  - Each cutoff's record is Elliptic, (0, 0, 0). The pair's members share a class and a Krein sign, so they cannot change the type among themselves (the rule's step 3).
- **Claim 3.** At N = 16, the zero cluster's largest |λ| is 1.11e-07, the margin 2.75e-06, with ‖A‖ = 265.7 and m = 31.99.
  - That puts the cluster 8.3 times below the gray zone's lower edge, against the condition's 10. The cluster stays separated, and K1 holds there.
  - At N = 24 and 32 the coefficient at ε = 32 is 0.0174 and 0.0174.
  - At N = 16 it exceeds the controls' largest, 0.0568 (M8.16's terms, STATED LIMITS), at ε = 5.66, 22.6, 32.
- **Both failures sit at the grid's top point, and both involve N = 16** (INFERRED). There, N = 16 differs from N = 24 by up to 0.085 on the pair, where N = 24 and 32 agree to 10⁻⁶. Why the cluster grows at N = 16 is not diagnosed (OPEN).

**Reported, unscored:**
- K2 fails at ε = 32 at all three cutoffs. The slow band, twice the largest εκsτ, is 1.864 there. Beside the five slow modes it takes in 5 more imaginary groups, at 1.640i to 1.840i, as UB anticipated (entry 22, item 4).
- The slow modes at ε = 32 sit at 0.40 to 0.49 of εκsτ.
- The aligned distance from N = 24 to 32 is at most 1.3e-06, and each point keeps its record across the two.

**What follows** (`BOUNDARY.md`, amendment 5; `LADDER_PLAN.md` v2, What each outcome means):
- Both failures are preserved and returned to Blake and the units before further development. Nothing is repaired or rerun.
- No constant moves, and no recalibration is available inside M8.16.1.
- T2 and T3 in `R5` run along this grid to ε = 32 in the registered run, so what follows for them is Blake's decision before the freeze, with the units.

**Then:** `build_dry.py plumbing` restored `run/DRY.json`, byte for byte entry 15's, `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`, kept as `dev/runs/015_DRY_plumbing.json` (UA).

## 25. 2026-10-22T21:16:23Z: a correction to entry 24: claim 4 is K4's bar and trend (UA)

Entry 24's "**K4's reading: holds.**" reads "**K4's bar and trend: hold.**" Claim 4 of the plan is those two components only, and they hold.

The full K4 along the ladder also needs every point converged. It reads False, through the convergence rule's Unresolved at ε = 32. The driver's checks, as recorded: K1 True, K4 False, converged False, bar True, trend True.

This does not contradict the registered C2a/R5 sample's K4, which ends at ε = 2. The packet's cover, a copy, carried entry 24's wording.

## 26. 2026-10-22T21:16:23Z: the units on the build and the run; the scorer's arms (UA), run again on the kept outputs

Blake, in his own words: "Sure, let's go that way", on my recommendation to go with both units: make UA's two fixes, then draft terms v4 with the ladder's disclosure, for the units first.
- **UA:** CONFIRM on the build and on the run's record. It evaluated claims 1 to 3 and the full control check from the kept outputs, with nothing solved.
  - Two corrections: entry 25's, and the scorer's arms.
  - Its recommendation: keep the registered `R5` grids through ε = 32 and K6 unchanged, refit nothing, and disclose the failures exactly in terms v4.
- **UB:** CONFIRM on both.
  - It reproduced on Linux, against a full clone: the scorer on the kept outputs, byte for byte; `test_guard.py`, 126 of 126, byte for byte; and every hash in entries 22 to 24.
  - Its reading: both failures are N = 16's resolution limit at the grid's top point.
  - Its recommendation is UA's: keep T2 and T3 in `R5` as registered, and disclose in terms v4.

**UB's reading, checked against the kept outputs** (`dev/runs/015_ladder/`, nothing solved):
- **The family.** At ε = 0.25, nine imaginary groups sit at 2.012i to 2.021i, beside √80 − √48 = 2.016. They spread as ε grows, and at ε = 32 they span 1.640i to 2.499i:
  - its lowest five enter the slow band, the K2 report of entry 24;
  - its top two are the pair the rule could not match.
- **The pairs.** At ε = 16, two of them sit 0.027 apart, at 2.251i and 2.278i. N = 16's largest departure from N = 32 on the tested groups was 0.023 there, and the rule read the point converged. At ε = 32 the pair is 0.029 apart and that departure is 0.044, so the rule cannot match it.
- **N = 16's departure,** absolute, on the tested groups against N = 32: 5.7×10⁻⁶ at ε = 0.25, 3.5×10⁻⁴ at 2, 5.8×10⁻³ at 8, 4.4×10⁻² at 32. N = 24's is at most 1.3×10⁻⁶, at 32.
  - UB's figures are relative departures over every group below the band edge, a different measure. They are not reproduced digit for digit here, and the trend is the same.
- **The coefficient's medians** along the ladder: 0.0279 at N = 16, 0.0176 at 24 and 0.0132 at 32, as UB gives them.

**The scorer's arms (UA).** Claims 2 and 3 already fail on the outputs as they are. So A2 and A3, which asked only that their claim fail, were red without their mutations. On an unmutated copy, in memory:
- the old test reads A2 and A3 red;
- the new test reads every arm green.

Each arm now must add a failure of its own, naming the point it mutates, beyond the claim's failures as they are. Claim 4 is relabelled K4's bar and trend, with the full K4 reported beside it, unscored.

**Script** `run/score_ladder.py` `d4a0a083714cd201bc30ae86bbd954dc33ca87a6238fa1c7c6627bb4025e7b18`, kept as `dev/runs/016_score_ladder.py`.

**The rerun.** The kept outputs were copied into `run/dry/` for the run, then removed again, each verified equal to its kept copy. The scorer ran with exit 1, its stderr empty.
- Output `run/score_ladder.out` `1f34ca8ab32bc303d8747a6a1fb3d35220f529243d75933c662579a61a0012c9`, kept as `dev/runs/016_score_ladder.out`.
- Against entry 24's output, only claim 4's label differs, beside the new line for the full K4: False, with converged False.
- Claims 1, 4 and 5 hold, and claims 2 and 3 fail at ε = 32, as recorded. Every arm is red by its own failure.

Next: terms v4, with the ladder's disclosure, for the units first.

## 27. 2026-10-22T21:24:11Z: the record of T5's second member's checks, run on 2026-10-20 (off the instrument)

**When.** On the bench, before this folder opened (entry 1): the bench's `LOG.md`, entry 25, 2026-10-20T17:24:17Z. The terms list these checks among the development runs, so they are logged here now, as entry 8 logged another earlier run.

**What ran:**
- **`t5_member_check.py`,** UB's, exact. It was rerun from a fresh copy on MIT's `scripts/soft-slot-branches/`, which is unchanged since `54f3d7c`.
  - It exited 0, in 11 s, with its output byte for byte UB's record.
  - Its three claims hold, and its arm, `u` in place of `u₂`, is red.
- **`cross_check.py`,** the bench's, exact, on both candidate members:
  - the Majorana root multiplicities: the registered member's polynomial has a double root, and both candidates' are squarefree;
  - UB's machinery, read on UA's candidate, gives a nonzero resultant against the registered member's slow polynomial.

  So each unit's argument certifies the other's member too.

**Files,** each as the bench's log records it:
- `t5_second_member.md` `c524b4b3221103c965e98466f3b1eee6acdcdf2a0c99204917b4bb875e85afdb`
- `t5_member_check.py` `1bc848eb4642ef76417caa2bb5cef1d98062eed226e7e8c92c3818ca4b265a05`
- `t5_member_check.out` `9fbe3a004674857deffe12107270c813cd485ac7cdb68c3f276bd3d5fc2be214`
- `cross_check.py` `27614cd4d28af89a75ecfb75d17694d7eb55292881d7c91ed3af4dc0ceb1642e`
- `cross_check.out` `dba11f1693089ba793bc5ebe3a7e835c50cfa72090da32bbe35ea7ac10afdd75`

**Outcome:** both checks hold. Neither touches the instrument, solves anything, or builds a seed. They are the exact checks of the terms' § T5'S SECOND MEMBER, whose proposition is DERIVED. The seed check's claim 7 (entry 19) reads the same root multiplicities on the instrument's own seed components. The member's note and its check land with the terms, in `registration/`.

## 28. 2026-10-22T21:55:43Z: the units on terms v4; the eight constants into `FROZEN.json`, and the constant test on the terms' next text

Blake, in his own words: "keep going if/when gucci:", with both units' replies on terms v4.
- **UA:** CONFIRM on entries 25 to 27, and HOLD on v4 for two wordings: test 2's description, and the scope of T5's second member in § Standing. It orders the code v4 asks for:
  1. `write_guard.frozen_values()` takes the eight constants;
  2. the constant test registers them, and its pending v4 category goes;
  3. the three tests of the frozen text and the guard's tests run again on the final text.

  "Once incorporated, UA supports proceeding directly to the v4 constants build and final tests."
- **UB:** CONFIRM on entries 25 to 27, and GO on v4 after two fixes:
  - the C3 ray's figure that v4 called the spherical part is `c_g°`, the prediction without the off-ray part;
  - the floor's count depends on the cutoff.

  Its NITs: P5's row, the run of entries 8 to 10, and arm A3, which should require claim 1's named failure once the floor is registered.
  - It reproduced the builder byte for byte, through a local stand-in for `gh`, and the scorer.

**Verified at source:**
- Proposition N's five parts at the C3 ray's quartet, from the bench's `c3ray_next_order.out` (bench `rows/`), as UB computed them:
  - spherical −0.23189 − 0.024179i;
  - amplitude 0.0034315;
  - off-ray 0.29231 + 0.11457i;
  - frequency −0.010417;
  - λ² 0.00065829 − 0.0003432i.

  They sum to the total. So v3's spherical part was right, and v4's "correction" of it was mine, and wrong: it read `c_g°` as the spherical part.
- The floor's groups, from the values file: five row groups at N = 24 and 32 and seven at N = 16. Beyond the rows, the floor binds at the pyramid's Krein-positive pair and the C3 ray's third group, at every cutoff.
- The maintainer's condition on T5's second member (comment 19076863, § 3): "no symmetry of the frozen action or of the truncation carries it to the member with complex structure `i`". UA's narrower wording matches both it and the proof.

**The terms' next text** carries every fix, and is the text the tests below ran on. SHA-256 `ef868ad7120ae693bcbfb17232fb289213953eec7ecff4f7d93d2c4341de85a3`. Its drafting is logged in the bench's `LOG.md`.

**The code.** The starting points are the files of the units' packet, `terms_review_v4`:
- `run/write_guard.py` `dcd3d89322e60b94138096287e47f40e62a8c2cbe941efbf15dd806c877c3c96`
- `run/test_constants.py` `c350365ae473cda538512d7ff1eedfae78ab46685dcdcca496d5e7f0a5552391`

After the change:
- `run/write_guard.py` `38af403dbc86ca16a3f581d5728e70fc08535a30901dae812cd848c9f26d8621`
- `run/test_constants.py` `fb8a08d93cc58be073fb09260feeab51eae404bf407a0ba93982d6abf91954c4`

What changed:
- **`frozen_values()`** holds the eight constants: K2's slow band 2, the band-edge guard's half, K3's orthonormal cut 10⁻⁶, K6's ε ≤ 2, and C1's 10⁻¹⁵, 10⁻¹⁴, 10⁻¹⁰ and 10⁻¹². It already held check 4's floor.
- **The constant test:**
  - its v4 list is gone, and its nine literals are registered;
  - its forward items cover the eight constants, check 4's floor and the new cutoff sentence, 43 in all;
  - the reprinted table is an exclusion, with its reason;
  - its coverage counts a DEVLOG entry's number, a check's number and the 256 of SHA-256 as references, not values;
  - arm A3 now requires claim 1's named failure (UB);
  - a new arm, A6, puts 0.37 right after a DEVLOG reference in a copy of the text, and coverage must still catch it.

**The runs,** each kept with its script before the next started (entry 22, item 8), each with exit 0 unless noted and an empty stderr:
- `run/test_constants.py` on the new text, three times:
  - attempt 1 (`dev/runs/017_1_*`): exit 1. Claim 1 failed at K2's factor, since the anchored-line count also counted the subscript in `p[2]`. Coverage failed at "check 4" and at "SHA-256";
  - attempt 2 (`017_2_*`): every claim and arm held, after K2's check took the reverse scan's own literal reader and the reference rule its two names;
  - attempt 3 (`017_3_*`), with A6: every claim holds and all six arms are red. Output `7c7b71ea8df46666ea419c4643285e6eccf9bd9db420ee895932300685035fea`;
- `run/test_guard.py`: 0 failed of 126;
- `run/test_imports.py dev/seed_check.json`: 0 failed;
- `run/test_verdicts.py`: 0 failed of 53.

These three outputs are byte for byte entry 23's.

Next: the packet for the units.

## 29. 2026-10-22T21:56:32Z: the terms' text no longer cites the log's length; rebuilt, and the constant test run again

**Why.** The text entry 28 tested said the log runs "in entries 1 to 27", a number the builder read from the log's last heading. Entry 28 itself moved it, so a rebuild from the units' packet, whose log holds entry 28, would not reproduce that text. Every entry that records a build would move it again. The text now drops the range. Each run's bullet names its own entries.

**The text,** rebuilt: SHA-256 `cf6a5da97af3c87c1b25188976c030deee49cdd90251bcb12ced4139fbbd621a`. Its builder and template differ from entry 28's by that one sentence alone.

**The run:** `run/test_constants.py` on it, attempt 4, kept as `dev/runs/017_4_*`. It exited 0, with an empty stderr. Its output differs from attempt 3's only in the line naming the terms' SHA-256. Every claim holds, and all six arms are red. Output `16b478d9d1c4f56b057e38db7940ada85ac00653bcf9d96c5de8f348b166c7b6`.

The guard's, the import and the verdict tests read no terms text, so entry 28's runs stand.

## 30. 2026-10-22T22:13:21Z: the units on terms v5; the reference rule's bypass (UA), fixed; `registration/` landed

Blake, in his own words: "keep going if/when gucci:", with both units' replies on v5 and its code.
- **UA:** CONFIRM on v5, on `write_guard.py` and on entries 28 and 29. HOLD on `test_constants.py` for one bypass: the reference rule took a decimal after an entry list's conjunction for an entry number, so in "entry 7 and 0.37" the 0.37 escaped coverage. Once the fix passes, UA has no objection to `registration/`, the filing build and the tests on the filed text.
- **UB:** CONFIRM on v5 and its code. It reproduced on Linux, byte for byte: the builder, the constant test, test_guard, test_verdicts and test_imports. Its NITs:
  - a stale citation in v5's tests section;
  - the reference rule could accept only whole numbers.

**Verified at source.** In copies of v5's text, under the rule as it stood:
- 0.37 put after "entry 7)" was named by claim 2;
- 0.37 put inside the list, "(`DEVLOG.md` entry 7 and 0.37)", left both claims passing.

So A6 tested only the case the closing parenthesis already broke.

**The fix,** UA's logic:
- a section number after a section sign, and the 256 of SHA-256, stay references;
- an entry's or a check's number is a reference only when it is a whole number, so a decimal, a fraction, a power of ten or a percentage there stays a value.

UB's NIT asked for whole numbers after a section sign too. The section rule stays, since a section number can be dotted, as in § 12.2.

A6 now puts 0.37 in both places, and is red only if claim 2 names it in each.

**`run/test_constants.py`:** from the units' packet's `fb8a08d93cc58be073fb09260feeab51eae404bf407a0ba93982d6abf91954c4` to `214699780f5c6fd639380c07860fb42e3b3cb474a19c9c8665bab4bd802d4385`.

**The run,** on v5, kept as `dev/runs/018_1_*`. It exited 0, with an empty stderr.
- Every claim holds, with the claims' lines as in entry 29's attempt 4.
- All six arms are red, and A6 names 0.37 in both places.
- Output `7cfe34b3731e4bd8a055593e8fef3745920bc6dee3be09b79cec89cbde59c5fa`.

**`registration/` landed,** copied from the bench's `t5_member/`. Each file equals the SHA-256 entry 27 records:
- `registration/t5_second_member.md`
- `registration/t5_member_check.py`
- `registration/t5_member_check.out`
- `registration/cross_check.py`
- `registration/cross_check.out`

The folder lies outside the manifest, so the instrument's pin is unchanged.

Next: the filing candidate, with UB's citation NIT, and the tests on its text.

## 31. 2026-10-22T22:14:30Z: the filing build: terms v6, and the constant test on its text

**The text.** Terms v6 is v5 with UB's citation NIT. Its tests section cites every entry where the three tests ran, 14 to 16, 23 and 28 to 30, and the builder checks that each cited entry records a test's run. Nothing else differs from v5.
- `m8_16_1_task_details.md`, terms v6: `eb30e781577abf27690471110b9f161afac34d3bd9a27d7dfa6965962a9af7bd`
- its template, `terms_template_v6.md`: `40945d6380f24087355c6a4b4373a2a498adc486d37c577b6bd02a3dd0e4318b`
- its builder, `build_terms_v6.py`: `0f3c18444583058f117e45d41b1bfe6a1ec9a9d8a3d450f407fbf173a89ded76`

The bench's canonical terms file held v3, `fae99a5c…`, as entry 1 records it. It now holds v6. Every earlier version's bytes are kept in its review packet.

**The run,** the tests on the filed text: `run/test_constants.py` on v6, kept as `dev/runs/018_2_*`. It exited 0, with an empty stderr. Its output differs from entry 30's run only in the line naming the terms' SHA-256: every claim holds, and all six arms are red. Output `bf2965fe016ac098567d1318faa64ac9c6c4f227350e0a1f44afb462a3cff459`.

The guard's, import and verdict tests read no terms text, and their code is as entry 28 ran it, so those runs stand. The other files of `run/` are as the log records them.

Next: filing, on Blake's word.

## 32. 2026-10-22T23:18:31Z: the units on the filing plan: GO from both, with two fixes; Blake's word for step 1

Blake, in his own words: "go on step 1". It is the filing plan's step 1, through a local commit on MIT, which then stops. The plan is v2, the bench's `FILING_PLAN.md`, SHA-256 `d982d557ce15b4a7151a07a1e99435433ea763e70503341008550bc094ad2922`. Both units reviewed v1, in the bench's `filing_review_v1.zip`, SHA-256 `f762ae286fe99f9d6040862d6c669402de0fd03ad074f2d23fe3b7c653258892`.
- **UA:** GO on all eight items: terms v6, the constant test, the folder, the order of step 1, `REPRODUCE.md`, the census note, the roadmap's rows, and the commit messages with the pull request's text.
  - UA verified v6's SHA-256 and the diffs against v5, and tested the reference rule on its cases. It did not rebuild v6.
  - It keeps the builder unchanged and the answer of 2026-10-15 in `registration/`.
- **UB:** GO on six items, and GO on two after one fix each.
  - It rebuilt v6 byte for byte on Linux against a full clone at `deec830`, with a stand-in for the one `gh` fetch, and ran the constant test on it.
  - (d) The scratch tests also run `run/build_dry.py`, since `run/DRY.json` is in the manifest.
  - (e) `REPRODUCE.md` gives the two commands that put a scratch clone's `HEAD` and `origin/main` at `deec830`, where the builder reproduces the terms.

**Verified at source before adopting:**
- (d) In a scratch copy of this folder, `run/build_dry.py` rewrites `run/DRY.json` byte for byte, `b973c86fba7966ef677cdcce9d8479687c1751817c9732db0e131b1b7ad69543`.
- (e) In a scratch clone at a simulated later `main`, the builder exits 0, and its text differs from v6 in four lines: the census commit and three links. After `git checkout --detach deec830` and `git update-ref refs/remotes/origin/main deec830`, it equals v6 byte for byte.

**Adopted:** both fixes, and UA's wording for the pull request, which says only that both units confirmed the final text.

**Step 1,** in the plan's order:
1. the sync;
2. the scan;
3. the terms' source into `registration/`, and the terms rebuilt there;
4. the terms in `run/`;
5. the environment record;
6. the pin;
7. the scratch tests;
8. `REPRODUCE.md`;
9. the folder in MIT's worktree;
10. the census note;
11. `SHA256SUMS`;
12. the local commit, verified from its own tree.

The push and OpenWave's branch each wait for Blake's word.

## 33. 2026-10-22T23:20:31Z: step 1 through the pin: the sync, the scan, the terms' source and their rebuild, the terms in `run/`, the environment record, the manifest pin

Under entry 32's word, in the plan's order.

**The sync.** MIT was fetched. `origin/main` and this worktree's `HEAD` are both `deec830b29f4bd6b45e58d2c333946dbbb60e964`, and the worktree has no change. The five target records' blob ids, at `origin/main` and at their named commit, equal those in `run/targets.json`: all ten readings, by `git ls-tree`. No record was opened.

**The scan,** before the pin, of the folder's 188 files without `run/dry/`, caches and `.DS_Store`, and of the three source files `registration/` gains:
- OpenWave's local-path patterns, the bench's path and the home folder, emails and personal identifiers, credentials, and Claude session internals: no hit;
- the one email-shaped string is `test@example.invalid`, the synthetic git identity of `run/test_guard.py`'s temporary repository, in that file and its two kept copies;
- OpenWave's `check_no_local.py --require-files`: clean, reading 109 of the 188, and 3 of 3.

**The terms' source, into `registration/`,** each by exclusive create, at the SHA-256 recorded:
- `registration/build_terms_v6.py` `0f3c18444583058f117e45d41b1bfe6a1ec9a9d8a3d450f407fbf173a89ded76` (entry 31);
- `registration/terms_template_v6.md` `40945d6380f24087355c6a4b4373a2a498adc486d37c577b6bd02a3dd0e4318b` (entry 31);
- `registration/ruling_1015.json` `aa233b3661b719adecaf560ef2fb075c82fdefa1bdcc2d446e9864ac02eba9b6`, the answer of 2026-10-15 (comment 18955679), as fetched for terms v2.

**The terms, rebuilt there:** `python3 -I -B registration/build_terms_v6.py MIT_REPO registration/ruling_1015.json 5b7a56b85d733d53e257cf7559b1b69ac05276a2 . registration`, from this folder, with `MIT_REPO` this worktree at `deec830` and `gh` signed in. It exited 0, with an empty stderr. It wrote `registration/m8_16_1_task_details.md` `eb30e781577abf27690471110b9f161afac34d3bd9a27d7dfa6965962a9af7bd`, which equals terms v6 (entry 31) byte for byte.

**The terms in `run/`:** copied by exclusive create to `run/m8_16_task_details.md` `eb30e781577abf27690471110b9f161afac34d3bd9a27d7dfa6965962a9af7bd`, equal to `registration/`'s.

**The environment record.** `run/record_environment.py` `1494fb8afd942e74a646671fe16f03ad4d9b095ae62cd1be35a51b2eb3a10059`, M8.16's byte for byte, wrote `run/ENVIRONMENT.json` `4d666fce6cddfca04d0950f6cbe3ad2524056e60f52196921a18549680ee9354` by exclusive create, run as `python3 -I -B`. Its `--check` found no difference. It equals M8.16's record field for field, apart from the time of the reading:
- Python 3.13.13 (CPython, `3.13.13 | packaged by conda-forge | (main, Apr  8 2026, 02:29:07) [Clang 19.1.7 ]`), at `/opt/homebrew/Caskroom/miniforge/base/bin/python3`, with `-I -B` and no `-O`;
- NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK;
- macOS 15.8 (24H23), kernel 24.6.0;
- a Mac15,13, Apple M3, with 4 performance and 4 efficiency cores, arm64;
- no threading variable set.

**The pin.** `run/pin_manifest.py` wrote `run/MANIFEST_PIN` by exclusive create: `146bb7b13135dc73552185510b7b46a00e11d92e8a9aa3eafa24faae151f1847`. It is the manifest's SHA-256 over 48 files: `instrument/` (12), `reference/m815/` (3) and `run/` (33), with the terms, the environment record, the pinned values and the tests' outputs included. The manifest, recomputed, equals it, and a second pin was refused with `FileExistsError`.

From here no manifest-covered file changes (UA), and every test runs in a scratch copy only (UB).

## 34. 2026-10-22T23:34:20Z: step 1, the folder: the scratch tests, `REPRODUCE.md`, the folder in MIT's worktree, the census note

**The scratch tests** (UB's step 3 for M8.16). A copy of this folder, in a scratch directory, without `run/dry/`, caches and `.DS_Store`, started at the pin. There `run/dry/` was restored from its kept copies: `dev/runs/008_plumbing/` as `run/dry/plumbing/`, and `dev/runs/015_ladder/`'s five files, as entry 26 ran the ladder's scorer. Each script then ran under `python3 -I -B`, one at a time, with `MIT_REPO` this worktree at `deec830`, each with an empty stderr:
- `run/test_guard.py`: exit 0, "0 failed of 126", 16.3 s;
- `run/test_verdicts.py`: exit 0, "0 failed of 53", 2.9 s;
- `run/test_constants.py`: exit 0, "0 failed", 1.8 s;
- `run/test_imports.py`: exit 0, "0 failed", 4.4 s;
- `run/test_k3.py`: exit 0, "0 failed", 0.7 s;
- `run/score_record.py`: exit 0, "0 of 8 claims failed; no verdict is computed", 1.0 s;
- `run/score_plumbing.py`: exit 0, "0 failed", 0.1 s;
- `run/score_ladder.py`: exit 1, "2 failed", 2.4 s;
- `run/build_dry.py`: exit 0, "DRY.json written: ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5']", 0.3 s;
- `run/next_order_values.py`: exit 0, "ALL CHECKS PASS; every arm red", 602.5 s.

- **The outputs.** Each equals this folder's, byte for byte: the eight tests' outputs, `run/DRY.json`, and the values' output and record. So does every one of the manifest's 48 files.
- **The manifest.** The copy's manifest still equals the pin, so no script wrote anything else under `run/` outside `run/dry/`.
- **The records written once,** `run/ENVIRONMENT.json` and `run/targets.json`, were checked in entry 33 instead.
- **The arm.** On a second copy, one byte appended to `run/test_k3.out` was caught by the comparison and by the manifest alike.

**`REPRODUCE.md`** `0bef5f374c5c2aa45fed2ec9991de72e27ba70a6082379dc9e90f625c4d0f445`, from the draft the units reviewed, with two values read from this folder's files:
- the manifest's 48 files;
- the values script's time. The draft said its last logged run took 342 s, which the run above, logged here, makes stale. It now says "about 6 to 10 minutes", the span of entries 7 and 6.

Its two checks ran from the folder: the manifest command printed the pin, and `record_environment.py --check` found no difference.

**The folder in MIT's worktree,** `files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16-1/`, at `deec830`:
- 196 files, each equal to this folder's byte for byte, with `run/dry/`, caches and `.DS_Store` left out;
- the manifest, recomputed there, equals the pin;
- git sees all 196, and none is ignored.

This log is copied in again after this entry.

**The census note,** under § V, step 4, dated 2026-10-22, as the last of its notes. It gives the terms' SHA-256 and the pin, each read from the folder's files, and links `REPRODUCE.md`.
- The page changes by that one line. Its math spans are unchanged, 114, and `metadata-lint.py` reports 0 FAIL, 0 WARN.
- The Status line stands: its Next is still M8.16.1.

**Next,** in order:
1. this log copied into the worktree's folder;
2. `SHA256SUMS`, fresh from the final inventory, and `shasum -c`;
3. the final folder scanned;
4. the local commit, verified from its own tree.

The commit's hash is logged after it, on the bench, since a commit cannot hold its own hash.

## 35. 2026-10-22T23:36:08Z: step 1: the local commit `0d6beae76a32`, verified from its own tree; not pushed

**The commit.**
- `0d6beae76a324d5e5d5e3246f599ae8fbf4e381f`, on `origin/main` at `deec830b29f4`, which a fetch just before the commit found unmoved.
- It is 1 ahead and 0 behind, so the push would be a fast-forward. It is not pushed.
- Author and committer: `Blake Shatto <blake@Blakes-MacBook-Air.local>`, as M8.16's filing was made.
- It changes 198 files: the 197 of the new folder, and the census page's note.

**Verified from the committed tree,** extracted by `git archive`, not from the working copy:
- `shasum -a 256 -c SHA256SUMS` passes, with 196 OK and no other line;
- the manifest, recomputed, equals the pin over 48 files;
- the census note names the terms' SHA-256 and the pin once each;
- `REPRODUCE.md` equals the bench's.

**What the commit carries.** The committed log ends at entry 34. This entry and any later ones stay on the bench until the next filing, the run's record, since a commit cannot hold its own hash.

**Next,** each on Blake's word:
1. the push, `git push origin HEAD:main`, after a fetch, as a fast-forward from `deec830`;
2. step 2, the OpenWave branch, pushed to the fork, after which Blake opens the pull request.

## 36. 2026-10-22T23:41:12Z: step 1 landed: `0d6beae76a32` pushed to MIT `main`, and read back live

Blake, in his own words: "go on the push".

**The push.** MIT was fetched again, and `origin/main` was still `deec830b29f4`, the commit's parent. `git push origin HEAD:main` was a fast-forward, `deec830b..0d6beae7`, and `ls-remote` shows `main` at `0d6beae76a324d5e5d5e3246f599ae8fbf4e381f`.

**Read back live,** through GitHub's API, at `main`:
- `REPRODUCE.md`, `run/m8_16_task_details.md` and `run/MANIFEST_PIN` equal the bench's;
- the census page renders 114 math elements for its 114 math spans;
- its new note names the terms' SHA-256 and the pin once each, and links the folder's `REPRODUCE.md`.

**What is current.** MIT `main` and this worktree are at `0d6beae`. Blake's main checkout shows the folder once it pulls. The bench's log holds entries 35 and 36, and they reach the folder with the run's record.

**Next, on Blake's word:** step 2, the OpenWave branch, pushed to the fork. It carries the task doc, byte for byte `run/m8_16_task_details.md`, and the roadmap's four edits. Blake opens the pull request.

## 37. 2026-10-22T23:51:30Z: step 2: the OpenWave branch pushed to the fork; Blake opens the pull request

Blake, in his own words: "go on step 2".

**Before branching,** with `upstream` fetched again, at `42b13ab9b65d67f13a01b99af2811e4d4416b051`:
- **The links.** Every link in the terms resolves: 11 distinct, each read through GitHub's API. That covers the blobs at their commits, with their anchors in the rendered pages, the three #512 comments, #640's review and #642. A made-up anchor, comment and review each fail the same check.
- **No collision.** No file on `upstream/main` names M8.16.1, no M8 commit has landed since #642, and no pull request is open.
- **Run-before-write holds:** M8.16 ran and was adjudicated (#640), and the column has since landed only its after-verdict records (#642).
- **The openings.** M8.13 to M8.16's task docs open with their title and "Pre-registration, for review.", as this one does.

**The branch.** `m8-16-1-second-and-last-qualification-2026-10-22`, on the fork, at `0d290498e6bb1e2783e45d09c1892668caa94c7c`.
- It is one commit on `upstream/main` `42b13ab9b65d`, signed off for the DCO in the clone's local identity, with the Co-Authored-By line.
- It changes 2 files, 404 insertions(+), 3 deletions(-):
  - **`tasks/m8_16_1_task_details.md`, new:** MIT `0d6beae`'s `run/m8_16_task_details.md`, byte for byte. Read back raw from the fork through the API, its SHA-256 is the terms', `eb30e781577abf27690471110b9f161afac34d3bd9a27d7dfa6965962a9af7bd`.
  - **`m8_roadmap.md`:** the BACKLOG row allocating M8.16.1 (`ROADMAP_STANDARDS.md` § 6), the two M8 status rows the ruling's roadmap condition names, and the snapshot's date, 2026-10-22. Read back from the fork, it equals the commit's.

**Checks,** on the branch:
- `check_roadmaps.py` is clean on all 7 roadmaps. The row's Description is 59 words of 65, and its Title 11 of 15. An arm adding seven words to the Description fails it, at 66;
- `check_models_md.py` is clean;
- `check_no_local.py --require-files` is clean on both files, and `--staged` on the commit.

**The pull request's text** is the bench's `m8_16_1_pr_body_v1.md`, SHA-256 `ee97a6a100eb9939c451fa42fa4d703df523289b67f935350648e7a93619dc82`, on Blake's clipboard.
- **Its form:** 581 words, one line per paragraph. Its 5 distinct links resolve, MIT's at `0d6beae`.
- **Its title,** in `m8_16_1_pr_title_v1.txt`: "M8.16.1: pre-registration for the harmonic Galerkin instrument's second and last qualification".
- **On the units:** it says both units confirmed the final text, and no more, since one of them did not rebuild it.

**Next:**
1. Blake opens the pull request against `openwave-labs/openwave` `main`.
2. The review. A change to any word of the terms redoes, on MIT `main` before the go, the terms' two copies, the pin, `SHA256SUMS` and a census note (UB's item 9 for M8.16). A change to the roadmap's rows or the pull request's text does not touch the pin.
3. The merge, then the maintainer's go.
4. `write_guard.py`, then the freeze block with `record_environment.py --check`'s two readings, then the run, on mains power with sleep off.

## 38. 2026-10-23T00:13:42Z: step 2: Blake opened the pull request, OpenWave #650

Blake opened [#650](https://github.com/openwave-labs/openwave/pull/650) at 2026-10-22T23:55:08Z. Its head is the branch entry 37 records, at `0d290498e6bb`, its base is `main`, and its state is open.
- Its title and body are as drafted, the body `m8_16_1_pr_body_v1.md` byte for byte.
- DCO, the repository's one check, passes, and GitHub reports it mergeable. It changes the two files entry 37 records: `m8_roadmap.md` +4 −3, `tasks/m8_16_1_task_details.md` +400 −0.

Blake, in his own words: "now we wait".

**Next:**
1. The maintainer's review. Each finding is verified at source before anything changes. A change to any word of the terms redoes, on MIT `main` before the go, the terms' two copies, the pin, `SHA256SUMS` and a census note, and the task doc follows in #650. A change to the roadmap's rows or the pull request's text does not touch the pin.
2. The merge.
3. The maintainer's go.
4. `write_guard.py`, then the freeze block with `record_environment.py --check`'s two readings, then the run, on mains power with sleep off.

## 39. 2026-10-23T21:00:34Z: xrodz's review of #650: changes requested on one blocking item, B1; verified at source (case: synthetic)

**The review,** [#650's](https://github.com/openwave-labs/openwave/pull/650#pullrequestreview-5631395680), 2026-10-23T16:31:16Z, CHANGES_REQUESTED. Its text is kept on the bench as `xrodz_review_650_5631395680.md`, SHA-256 `85a0f06ca8324faf79ce98540c56f7e0bc420cacf09ee0cec962505853bb1603`.
- **B1, blocking.** Check 1 takes K2's assignment, `checks.match`, which pairs the computed values with the leading-order predictions `εκs_gτ` by least total relative distance. At T5/R2 the two lowest groups sit 2.0% apart at leading order, and at `ε = 1` their next-order shifts are about as large. So on a spectrum where Proposition N holds exactly, the assignment exchanges them, `h_g(1)` is read off the other group, the spread exceeds the ceiling and the bar reads fail. T5/R2 would fail K5 and never be offered to this instrument again.
  - The fix is the author's. The review offers three: pair against `εκs_g + ε²c_g`; carry each group's identity from `ε = 0.25`; or keep the order of `|λ|` within a bucket.
  - Test 1 then wants a T5 arm that goes red on the current pairing.
- **Comment tier, optional while the pin is redone:**
  - `check_ray`'s discrimination reads True when no group reached checks 1 and 2;
  - `verdict`'s `.get('K6', True)` would qualify a ladder row whose record has no K6 key;
  - `write_guard.py`'s inventory comparison reads the values file on both sides.
- **Found right by the maintainer:** the terms, the pin, the instrument, the boundary, the frozen values, the pyramid's known outcome, T5's second member, the code against the terms apart from B1, the sealing, the conditions and the linters.

**Verified at source.** `dev/verify_b1.py` was run from this folder as it stands at the pin, `146bb7b1…`, with nothing in it changed. For every case the bar reads, it builds a synthetic record whose slow spectrum is exactly `εκs_g + ε²c_g(N)` at each cutoff and at the three points, from `run/next_order_values.json` as `cases.py` serializes it, with a consistent summary. It stubs `checks.k1` and `checks.converged` true, so check 1 reduces to the matching. It then scores the record with `checks.bar`, and tests `checks.match` alone.
- **Two attempts,** each kept with its script, output and stderr:
  - `dev/runs/019_1_*` stopped on its own report line, which read a `τ` given only as a fraction, before scoring anything;
  - `dev/runs/019_2_*`, with `τ` read by `checks.num`, exited 0 with an empty stderr. Script `33382c8ebff32d326dfee4d94fb46d78503b05f2e1c16be5f86a312df2edabb1`, output `0fe653d47d3873b8de1d4156c7a23376546a907ba098977ec1d2f86d60c8d668`.
- **T5/R2's two lowest groups,** `τ` = 2.6886 and 2.7413, read fail at every cutoff by check 3. The numbers are the review's: at `N = 16`, the spread 1.69e-04 over the ceiling 5.05e-05. The second group also fails check 4 at 24 and 32.
- **Every other group passes:** 35 of the 37 groups under the bar in the 12 cases.
- **The exchange.** `match` moves a value to another entry only at T5/R2, at `ε = 1`, at every cutoff. There the straight pairing costs 0.0404 and the exchanged one 0.0400 at `N = 24` and 32, and 0.0394 against 0.0390 at 16.

So B1 holds as stated.

**Also read at source:**
- K2 uses the assignment for its counts alone, so an exchange within a bucket cannot change it.
- The leading-order readings at 0.5, 1 and 2 are reported, unscored.
- So the bar is the only scored reading the exchange reaches: K5, K3(a) and K4's pyramid item, and the C3 ray.

**Next:** the repair, for Blake's decision, and then the units.

## 40. 2026-10-23T21:11:40Z: the repair for #650's B1, built: check 1 matched against the next-order values; a ladder row without K6 fails closed; test 1's T5 claim and two arms; every rerun

Blake, in his own words: "go on building the repair for the units". It follows my recommendation after entry 39: B1 by the review's first fix, and of the comment tier the K6 default alone.

**The changes,** from the filed files at MIT `0d6beae`, whose pin is `146bb7b1…`:
- **`run/checks.py`,** `3496347436fce7c768969a97387992eff401ba1781b6e95c60e3b9eeafada47e` to `c3122cd0ac692e16a5a6fb7fde178e13b27d9bb1632ad8eed32432b2c6919b84`:
  - `predicted_next`, new: each frozen spectrum entry's next-order prediction, `εκs_g + ε²c_g(N)` at the cutoff, from the case's values. It returns None when the values lack an entry.
  - `mode_values`: the assignment is K2's, one to one by class and Krein sign with multiplicity and the least total relative distance, but against `predicted_next` in place of the leading order. It now takes the cutoff. Its reported deviation is still each value's from the leading order, as the terms report it (§ THE NEXT-ORDER BAR, "Reported, unscored").
  - `bar_cutoff` passes the cutoff.
  - `k6_holds`, new, read by `verdict`: a row whose case names M8.15's record qualifies only on its own K6 key, and a record without one fails closed. A row with no ladder has no K6.
- **`run/test_verdicts.py`,** `78097e817d32b9e56b6d03b12a687ce629742ca7e17577010f2f6b6676dc4419` to `498a700d46d195f9b4d9edb93d86fe97dc58ed976f3ca8286cb6910a3c988dae`:
  - claim 1i: on a synthetic T5/R2 record whose slow spectrum is exactly `εκs_g + ε²c_g(N)` at every cutoff and point, with K1, the convergence reading and a consistent summary in place, all three groups pass;
  - claim 8 gains a ladder row whose record has no K6, which is not qualified;
  - arm M5 restores the filed pairing, against the leading order, and arm M6 the filed K6 default.
- **`dev/verify_b1_fixed.py`,** new: entry 39's harness on the repaired code, with an arm.

**Left as they are,** of the comment tier, with the reason each has in the review:
- `check_ray`'s discrimination: when no group reaches checks 1 and 2, the ray's outcome already reads failed through the bar, and the ray gates nothing;
- `write_guard.py`'s inventory comparison: the protection is `_tie` and the bar-membership rule.

**The runs,** one at a time, each with its outputs kept before the next started, each with an empty stderr:
1. **`run/test_verdicts.py MIT_REPO`** (`dev/runs/020_1_*`): 0 failed of 57.
   - Against the filed output, only the four new checks and the count differ. So every earlier outcome, the pyramid's included, reads as before.
   - M5 reads T5's two lowest groups fail and its third pass, B1's outcome. M6 qualifies the ladder row without K6.
   - Output `aba8d4b2c900446efa8c77aac079507d1e91b8425145881af8af5baf9195bd21`.
2. **`dev/verify_b1_fixed.py`** (`dev/runs/020_2_*`): every one of the 37 groups under the bar in the 12 cases passes, on a spectrum exactly at the next order. `mode_values` gives every entry its own value, at every case, cutoff and point. With the filed pairing restored, the first claim is red at T5/R2's two lowest groups alone. Output `3ac4290d1441f48f34f74db5cde247247db083913f10168a46925afc3b9557ab`.
3. **Every other script that reads `run/checks.py`,** each output byte for byte the filed one:

| Script | Kept as | Exit | Its last line | Against the filed output |
| --- | --- | --- | --- | --- |
| `run/test_guard.py` | `dev/runs/020_3_*` | 0 | "0 failed of 126" | equal |
| `run/test_constants.py` | `dev/runs/020_4_*` | 0 | "0 failed" | equal |
| `run/test_imports.py` | `dev/runs/020_5_*` | 0 | "0 failed" | equal |
| `run/test_k3.py` | `dev/runs/020_6_*` | 0 | "0 failed" | equal |
| `run/score_record.py` | `dev/runs/020_7_*` | 0 | "0 of 8 claims failed; no verdict is computed" | equal |
| `run/score_plumbing.py` | `dev/runs/020_8_*` | 0 | "0 failed" | equal |
| `run/score_ladder.py` | `dev/runs/020_9_*` | 1 | "2 failed" | equal |

`run/test_constants.py` read terms v6 there. `run/score_ladder.py` read `run/dry/` holding `dev/runs/015_ladder/`'s five files, copied in for its run and removed after, each verified equal to its kept copy, as entry 26 ran it.

**The pin.** The bench's manifest is now `285917ee…`, no longer the pin `146bb7b1…`. That pin is retired at the re-filing, as M8.16's `c1ea8f2` retired its first.

**Next:**
- terms v7, built at `deec830`. It carries check 1's matching, the K3(a) paragraph's, test 1's list with its count and arms, and the tests' citation, which gains this entry;
- the constant test on v7's text;
- the units.

## 41. 2026-10-23T21:13:41Z: terms v7, built at `deec830`, and the constant test on its text

**The build.** The bench's `build_terms_v7.py` `da1c5e9cb5ec28c6287d41defe4d3cc9e05b1fe74a0ccd7419dbac7890b819e7` filled `terms_template_v7.md` `71aeacea0715b01168ac4aaad6bd17fc7cf62032db2d41ba11a23e4402e3f59b`, with `MIT_REPO` a scratch full clone whose `HEAD` and `origin/main` were both `deec830b29f4`, set by the two commands `REPRODUCE.md` gives. It read this folder, with the log through entry 40, and the answer of 2026-10-15 in `registration/`. It exited 0, with an empty stderr.
- **The text:** terms v7, `m8_16_1_task_details.md`, SHA-256 `9d16712982e5388970fca33de59958721109e09f9d88dec7a2a088489ad3efd6`, 7,669 words by `wc -w`. It replaces v6 at the bench's canonical path, whose bytes are kept in `filing_review_v1/` and at MIT `0d6beae`.
- **Against v6,** the text differs in five places (49c49, 183c183, 187c187, 307a308, 315,316c316,317 in `diff`'s numbering), and nowhere else:
  - check 1 matches each group as in K2, but against its next-order value, `εκs_g + ε²c_g(N)`, in place of its leading order, with the reason: T5's two lowest groups;
  - the K3(a) paragraph matches against the next-order values too;
  - test 1's list gains the T5 claim;
  - the tests' citation gains entry 40, with test 1's count, 57, and its arms, six;
  - the word count, computed, reads about 7,700.

  Its citations of MIT pages stay at `deec830`, as built.
- **The builder,** against v6's: the template's name; the tests' citation checked at entry 40 too; and test 1's arms counted from its output, which must hold no failure.

**The run:** `run/test_constants.py MIT_REPO ../m8_16_1_task_details.md` on v7, kept as `dev/runs/021_*`. It exited 0, with an empty stderr. Every claim holds, and all six arms are red. Its output differs from entry 40's run on v6 only in the line naming the terms' SHA-256. Output `b224670fa5ed006469ec3a90d365f60823505999ea709b670df1b59857bde02b`.

**Next:** the re-filing's plan and drafts, and the units' packet.

## 42. 2026-10-23T21:15:12Z: run `dev/b1_margins.py`, the margins behind B1's fix (case: synthetic; arithmetic on the pinned values, nothing scored)

**Why.** Before the fix of entry 40 was chosen, the review's three options were weighed on the pinned values in a scratch computation, which this run makes a logged script. It runs on the folder as it stands, with entry 40's code; it reads only the values and `checks.py`'s constants.

**Script** `dac25068704aa19d97f882039ab64bd416e4e2e78ede74b2647182e904c35b71`, kept as `dev/runs/022_*` with its output and an empty stderr. Output `b7ae992c6b4db019812ebd466698c570acdd1ae6d9f1881acbe3349b20066366`.

**Outcome,** over every case the bar reads, every cutoff and the three points, within each class-and-sign bucket:
- **No two groups change order by `|λ|`** between `εκs_g` and `εκs_g + ε²c_g(N)`. So keeping the order of `|λ|`, the review's third option, would have paired every exact spectrum correctly too.
- **The smallest separation** of two groups' next-order predictions is 9.8 ceilings, as a shift of `λ`, at T5/R2, `ε = 1`, `N = 24`, over 90 buckets of two groups or more.
  - So matching against the next-order values, the option entry 40 takes, can move a value only where some group lies about half that far from its prediction.
  - A group that far off already fails check 3, whose spread moves by a third of the shift at `ε = 1`.

## 43. 2026-10-23T21:20:07Z: the re-filing's plan and drafts, and the units' packet, self-checked

**Drafted** on the bench, with nothing committed, pushed or posted:
- `REFILING_PLAN.md` v1, `9226af187e487d4ca2e028dabc9d25712f647c4a0a5854c4ba97893ec9412b96`: M8.16's revision after #637, step for step;
- `refiling_drafts/`: the census note, `REPRODUCE.md` with three lines changed, the two commit messages, the reply to the review, and the pull request's revised paragraph. Values known only at re-filing are marked, to be computed then.

**The packet,** `repair_review_v1.zip`, 279 files, SHA-256 `ef8d11f4c235054136e5eeb404c1a025842a3e19d7a03ccb699adf53ea277136`. It holds the plan and drafts; the review; terms v7 with its source; diffs against MIT `0d6beae` and against v6; this folder through entry 42; and M8.16's revision records.

**Self-checks,** each in a scratch copy:
- terms v7 rebuilds from the packet's own copies byte for byte, with a clone set at `deec830`;
- `run/test_verdicts.py` (0 failed of 57) and `dev/verify_b1_fixed.py` reproduce their outputs on a copy of the packet's folder;
- `dev/verify_b1.py`, copied into MIT `0d6beae`'s folder as `git archive` extracts it, reproduces entry 39's output byte for byte;
- **the scan:** no hit outside the folder. In it there are two, for the units (the plan's item g):
  - `dev/runs/019_1_verify_b1.err`, the traceback of entry 39's first attempt, names the bench's path;
  - entry 35 names the MIT commit identity.

  The plan proposes filing both as they are, as M8.16 filed its kept driver logs.

**Next:** the units' replies. Then the re-filing, each outward step on Blake's word.

## 44. 2026-10-23T21:38:39Z: the units on the repair: GO from both, with fixes; the margin verified at source; corrections to entries 42 and 43

Blake relayed both replies on `repair_review_v1`, with no words of his own. So the re-filing waits for his own word.
- **UA:** GO on items (a) to (e) and (g), and CHANGE on (f).
  - The reply's sentence on the margin overstates it. Checks 3 and 4 pass `λ = μ₀ε + c_gε² + dε³` at any `d`, since `h = c_g + dε` is linear and both extrapolations are exact on it. Entry 42 makes the same inference, and a dated correction should record it, with entry 42 left as logged.
  - UA confirms the code, the tests and v7 by review. It ran the fixed harness itself, but did not rebuild v7 or rerun test 1 against MIT's history.
  - Keep both scan findings as they are.
- **UB:** GO on (a) to (g), with two CHANGEs to the reply, a NIT and a third scan finding.
  - UB rebuilt v7 at `deec830`, byte for byte, and reran test 1 (57 of 57), the harnesses and the other scripts.
  - Its own pairing, from the values file alone, fails T5/R2's groups 0 and 1 at every cutoff when matched against the leading order, and fails nothing when matched against the next order.
  - **The first CHANGE** is the margin sentence, in UB's words: the 9.8 ceilings are the whole margin, since two groups pushed toward each other by `ε³` terms exchange there with no check failing.
  - **The second CHANGE:** "Everything else is byte for byte the filed tree" becomes "Unchanged, byte for byte", since the log, `REPRODUCE.md`, `SHA256SUMS`, `registration/` and `dev/` change too. UB's last line holds once both go in exactly as given.
  - **The NIT:** the plan's step 8 changes four lines of `REPRODUCE.md`, not three, and entry 43 says three too.
  - **The third finding:** `dev/runs/020_3_test_guard.stdout` names macOS temp folders, to be filed as it is, with `var/folders` added to the scan.
  - **Open, Blake's call:** closing the margin fully, by matching `ε = 1` against each group's own extrapolation from 0.25 and 0.5.

**Verified at source.** `dev/verify_e3_margin.py` `c11d543b7c6063fdef36c5f86cad0e6bb20275d0a879310ee017cf0f4946384e` uses entry 39's harness on the repaired code. It is kept as `dev/runs/023_*`, exited 0 with an empty stderr, and its output is `058c8c62aeed56975a4ef64f6dbabc4ec40d1c7075f53236cce51648c0d9fc21`.
- A pure `ε³` term of 50 ceilings at `ε = 1`, on T5/R2's lowest group, away from the next, passes every group.
- `ε³` terms on T5/R2's two lowest groups toward each other, in each group's own ceiling: at 4.5 each every group passes, each with its own value; at 5.5 the two read fail, their values exchanged. These are UB's numbers.
- **Reported, unscored, for scale:** the pyramid's recorded departure from `εκs_g + ε²c_g(N)` at the point nearest 1 is 1.16 ceilings for the quartet and 0.11 for the Krein-positive pair, at `N = 24` and 32, and 1.13 and 0.16 at 16. These are UB's figures, at 24 and 32.
- **UB's third finding** holds: 6 lines of `dev/runs/020_3_test_guard.stdout`, each naming a different temp folder, against UB's five. The filed tree has none, and `run/test_guard.out` has none. The earlier scans missed them, because their pattern for `/private/var/` does not match the relative `var/folders` the driver prints.

**Corrections, by this entry, to entries left as logged:**
- **Entry 42's last two sentences.** The 9.8-ceiling separation is a measured margin, not a guarantee from check 3. The last sentence holds for a shift at `ε = 1` alone. Checks 3 and 4 pass a pure `ε³` term at any size, so two groups whose values depart toward each other by 9.8 ceilings in all, at `ε = 1`, exchange with no check failing.
- **Entry 43's "`REPRODUCE.md` with three lines changed"** reads "four lines": lines 33, 57, 77 and 78 of the draft.

**Adopted:**
- the reply takes UB's two replacements exactly as given;
- the plan, now v2, takes the NIT, names the three scan findings, each to be filed as it is, and adds `var/folders` to the scan;
- the adjudication on the margin sentence: UB's text, which UB asked to go in exactly, also makes UA's correction. It says the margin is measured, and why no check covers it.

**Next:** Blake's call on UB's open item, and then his word for the re-filing.

## 45. 2026-10-23T21:45:40Z: the units on the open call: file the fix as reviewed; Blake's word for the re-filing's step 1

Blake, in his own words: "go if/when gucci w/", with both units' replies on entry 44's open call. The plan is v2, the bench's `REFILING_PLAN.md`, `48e5a4471f86bf69e8b7ac532f303487330a2aa57a906e622c621e70f6128429`.
- **UA:** GO on step 1, filing the repair as reviewed. Do not build the stronger matching rule first.
  - The cubic-term counterexample changes the strength of the claim, not the ruling on the repair.
  - The distinction to keep:
    - DERIVED: the next-order matching repairs B1's demonstrated misassignment on the registered predictions;
    - OPEN: whether higher-order terms can cause a different assignment on T5's actual readings at finite amplitude.

    Neither the margin nor this uncertainty is to be read as a theorem, a certified bound or a guaranteed margin.
  - If xrodz asks for his second option, or finds the residual ambiguity unacceptable, the stronger rule is built and registered then, before his go.
  - Stop after the verified local commit.
- **UB:** CONFIRM, filing as reviewed, now.
  - **A correction to its own reply:** the test log holds six temp-folder paths, as entry 44 counted. UB's search had stopped after five lines, and those six are the only matches in the folder.
  - **The margin, on the closest comparison:** the pyramid's Krein-positive pair departs about 45 times less than a swap at T5 needs, 0.11 ceilings against 4.9. The quartet's ratio is only about 4, but its `c_g` is twelve times T5's relative to `κs`, so it is a weaker guide.
  - T5's two groups have next-order coefficients alike, −0.0207 and −0.0197 of `κs`.
  - The stronger rule has costs of its own: an error at 0.25 or 0.5 carries forward.
  - **A limit on "nothing is lost":** the matching can change before `FROZEN.json` is written, not after.
  - UB checks the applied text, entry 44 and the corrected reply in the next packet. Its GO covers its two replacements exactly as given.

**Decided:** the repair is filed as reviewed. The stronger rule is not built unless the maintainer asks, and then before the freeze.

**Next:** the re-filing's step 1, in the plan's order, through a local commit verified from its own tree; then the units' short look at the applied texts. The push, OpenWave's commit and the reply each wait for Blake's word.

## 46. 2026-10-23T21:47:26Z: the re-filing's step 1 stops at the sync: MIT's `main` has moved; and one new scan hit

Under entry 45's word, steps 1 and 2 ran, read-only, and step 1 stops there, as the plan says, for the units and Blake.

**The sync.** MIT was fetched. `origin/main` is `1ac1c7bcce03`, one commit past the filing commit `0d6beae`, at which this worktree's `HEAD` still stands, unchanged.
- **The commit:** `1ac1c7bc framework page: the gravity interface and five stale lines`, Blake's, changing `files/framework/README.md` alone.
- It touches none of these: this folder, the census page, the pages the terms cite, M8.16's folder or M8.15's.
- The five target records' blob ids at `origin/main` and at their named commit equal `run/targets.json`'s, all ten readings.
- **For Blake's call:** M8.16's sync rule fast-forwarded past such commits once they were checked (M8.16's entries 280 and 281). This plan's step 1 is stricter, and stops.

**The scan** of the folder's 249 files and v7's two source files has no hit beyond step 2's three findings, apart from one:
- **OpenWave's `check_no_local.py`** reads entry 44's mention of the pattern `/private/var/` as a machine-local path, and fails on that line. The line names a pattern, not a path. The log is never edited, and it is filed in MIT alone.
- **The three findings** are as step 2 names them: `dev/runs/019_1_verify_b1.err`, entry 35's commit identity and `dev/runs/020_3_test_guard.stdout`.

Nothing was written or pinned, and nothing in this folder changed apart from this entry.

**Next,** on Blake's word: the worktree brought up to `origin/main` as a fast-forward, the sync's check recorded, and step 1 from step 3, with this hit filed as it is.

## 47. 2026-10-23T21:49:30Z: the re-filing's step 1 through the pin: the worktree fast-forwarded, the terms' source and their rebuild, the terms in `run/`, the environment, the new pin

Blake, in his own words: "go ahead, fast-forward and continue step 1".

**The sync.** The app's `sync_with_base_branch` refused, since this repository has no git identity configured, as the bench's notes record. This worktree was behind `origin/main` only, so `git merge --ff-only origin/main` brought it to `1ac1c7bcce03101e8be9ec9a2138791cbb49e759`, with no merge commit and nothing uncommitted. Entry 46 records the one commit it took in, which touches nothing the filing reads.

**The scan** stands as entry 46 records it. The three findings and entry 44's mention of a pattern are filed as they are.

**The terms' source.** `registration/` lost v6's builder, template and built text, each first checked equal to its blob at MIT `0d6beae`, where their bytes stay. It gained:
- `registration/build_terms_v7.py` `da1c5e9cb5ec28c6287d41defe4d3cc9e05b1fe74a0ccd7419dbac7890b819e7` (entry 41);
- `registration/terms_template_v7.md` `71aeacea0715b01168ac4aaad6bd17fc7cf62032db2d41ba11a23e4402e3f59b` (entry 41).

**The terms, rebuilt there.** From this folder, `python3 -I -B registration/build_terms_v7.py MIT_REPO registration/ruling_1015.json 5b7a56b85d733d53e257cf7559b1b69ac05276a2 . registration` ran with `MIT_REPO` the scratch full clone set at `deec830`. It exited 0 with an empty stderr, and wrote `registration/m8_16_1_task_details.md` `9d16712982e5388970fca33de59958721109e09f9d88dec7a2a088489ad3efd6`, terms v7 byte for byte.

**The terms in `run/`.** v6's copy was removed, first checked equal to its blob at `0d6beae`. v7 was copied in by exclusive create: `run/m8_16_task_details.md` `9d16712982e5388970fca33de59958721109e09f9d88dec7a2a088489ad3efd6`.

**The environment record** is unchanged, `4d666fce6cddfca04d0950f6cbe3ad2524056e60f52196921a18549680ee9354`, and `--check` found no difference.

**The pin.**
- The filed `run/MANIFEST_PIN`, `146bb7b1…`, was removed: it is retired, not reused, and its bytes stay at `0d6beae`.
- `run/pin_manifest.py` wrote the new pin by exclusive create: `8cc2d7e2d01a72fc3572adabf917656abf36cbddd70ed35532b73ae5451790dd`, over the same 48 paths. `instrument/` holds 12, `reference/m815/` 3 and `run/` 33.
- The manifest, recomputed, equals it, and a second pin was refused with `FileExistsError`.

From here no manifest-covered file changes (UA), and every test runs in a scratch copy only (UB).

## 48. 2026-10-23T22:03:59Z: the re-filing's step 1, the folder: the scratch tests, `REPRODUCE.md`, the folder in MIT's worktree, the census note

**The scratch tests,** as the filing's (entry 34): a copy of this folder, without `run/dry/`, caches and `.DS_Store`, started at the new pin `8cc2d7e2…`, with `run/dry/` restored from its kept copies. The scripts ran one at a time, under `python3 -I -B`, with `MIT_REPO` this worktree at `1ac1c7b`, each with an empty stderr:
  - `run/test_guard.py`: exit 0, "0 failed of 126";
  - `run/test_verdicts.py`: exit 0, "0 failed of 57";
  - `run/test_constants.py`: exit 0, "0 failed";
  - `run/test_imports.py`: exit 0, "0 failed";
  - `run/test_k3.py`: exit 0, "0 failed";
  - `run/score_record.py`: exit 0, "0 of 8 claims failed; no verdict is computed";
  - `run/score_plumbing.py`: exit 0, "0 failed";
  - `run/score_ladder.py`: exit 1, "2 failed";
  - `run/build_dry.py`: exit 0, "DRY.json written: ['C1', 'C2a', 'C2b', 'C3', 'C2a/R5']";
  - `run/next_order_values.py`: exit 0, "ALL CHECKS PASS; every arm red";
  - `dev/verify_b1_fixed.py`: exit 0, "the arm is red at T5/R2's two lowest groups alone: holds".

- Each output equals this folder's, byte for byte, and so does every one of the manifest's 48 files.
- The copy's manifest still equals the pin.
- On a second copy, one byte appended to `run/test_k3.out` was caught by the comparison and by the manifest alike.

**`REPRODUCE.md`** `f24179e0de70f71a38aa6cbfa7acf35ce91d79929f3bf49d298f7dc57a2b7b20`: the filed text, first checked equal to its blob at `0d6beae`, with the reviewed draft's four lines: test 1's count, 57, and the builder's and template's names, v7. Its two checks ran from the folder: the manifest command printed the pin, and `record_environment.py --check` found no difference.

**The folder in MIT's worktree,** at `1ac1c7b`, brought up to this folder:
- v6's two source files were removed;
- 54 files were added, `dev/`'s scripts, outputs and kept runs since the filing among them;
- 9 were changed: the log, `REPRODUCE.md`, the two terms copies, the pin, `checks.py`, `test_verdicts.py` with its output, and `test_constants.out`;
- the old `SHA256SUMS` was removed, to be written fresh.

Each file equals this folder's, byte for byte, and the manifest, recomputed there, equals the pin. Git ignores none of them. This log is copied in again after this entry.

**The census note,** under § V, step 4, dated 2026-10-23, directly below the note of 2026-10-22, which stands. It gives the revised terms' SHA-256 and the new pin, each read from the folder's files, and says the hashes above are superseded.
- The page changes by that one line, and its math spans are unchanged, 114.
- `metadata-lint.py` reports 0 FAIL and 0 WARN. Its new INFO, "body edited 2026-10-22 after Status 2026-10-20", comes from the filing commit's own note. The Status's Next is still M8.16.1, so the Status stands, as M8.16's revision left its own.

**Next:**
1. this log copied into the worktree's folder;
2. `SHA256SUMS`, fresh, and `shasum -c`;
3. the final scan;
4. the local commit, verified from its own tree.
