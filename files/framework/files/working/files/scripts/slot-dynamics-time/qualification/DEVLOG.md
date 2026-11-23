# M8.20, the time arm's qualification: development log

Each entry is written by hand, in order, and never edited; a correction is a new entry. Every run names its script's SHA-256 and each output's. Development earns no qualification credit.

## 1. The development boundary (2026-11-22T14:52:35Z)

Development runs before the terms file, under #512's answers of 2026-11-21 ([19803452](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19803452)) and of 2026-11-22 ([19812666](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19812666)).

**It may run:**
- synthetic linear systems with known eigenvalues, Krein signs and multiplicities, for the read's code, its mode admission and its arms;
- multi-level and single-level states from development seeds, never a registered seed, in `R1` to `R5`;
- the stored records of M8.16.1, read, loaded or refused by the loader, with no evolution;
- the rigid families in `R1` and `R3` at points the terms leave unregistered: `‖φ‖²` = 0.5 and 2, never 1, at any cutoff.

**It may not run:**
- any of the seven members the reading admits, at any amplitude, registered or not (19812666, § 1);
- any point the terms register, at any cutoff; and no point read here is registered afterwards (19812666, § 2).

**Its conditions on the rigid families** (19812666, § 2): development seeds; every run logged here and disclosed before the freeze; no credit; such a run classifies no row, changes no point's reading, no stretch and no ending, is cited to no row of the census, and is no finding on M8.16.1's readings; the census's analytic closing of those rows is not read again. The terms name these readings as known outcomes, with the choices made knowing them, and quote the answer.

Nothing has run in this folder before this entry.

## 2. The read core on synthetic systems (2026-11-22T14:56:30Z)

`readcore.py` `67d7b197417509c3e0d29093bc9b62f6f2c52f5b868dae6f677911ed71107065` holds the read that does not touch the instrument: the one-step map fitted at the data's numerical rank (singular values above 10⁻⁸ of the largest), the mode fraction (10⁻³ of a trajectory's projected data), the slow circle, mode admission, the floor by a refit on nine tenths, the Krein test on a group's read eigenspace and the ratio of successive differences.

`dev/dev_synthetic.py` `bf29b5af54ac2491e45fcbced08bec9edc176a0a349cf5a833633f397972c461`, development seed 7300101, output `dev/dev_synthetic.out` `2bcc745b973e99e8031cc6b114bee14211890254730fddb110455096d11f5158`: 29 of 29 checks pass. Four quadratic Hamiltonians, mixed by a random symplectic map, each with six fast modes outside the slow circle and two weakly excited zero-frequency directions at 2.3 × 10⁻⁵, as DEVLOG entry 11 of the prototype found them. Each is seen through a carrier turning 5.5 × 10⁻⁵ faster than the continuum, with a second-order term the pair must cancel:
- five simple imaginary pairs, Krein +;
- the hexagon's shape, a simple and a double pair, Krein −;
- C3's shape, a real triple;
- P5's shape, a quartet and two pairs, Krein − and +.

Each spectrum is recovered with its multiplicities, the worst relative error 2.1e-07, each floor below a tenth of its tolerance, and each Krein sign definite and right. Every arm is refused: the mode fraction off (the weak directions fail the admission), demodulation at the continuum's rotation, the broken pair, the flipped form, and one direction for a multiple group. No census point and no member ran.

## 3. The loader on M8.16.1's stored records (2026-11-22T14:57:57Z)

`loader.py` `50cdf037fa8405ba8e2368ad88029609dd0c7c9e0129d426404bb673fe984cb9` loads a stored point from M8.16.1's `run/out/`, each record pinned by the SHA-256 its `RECORD.md` lists, and pairs each stored slow group with Theorem 4.2's leading order, `L_g = εκsτ_g` at the point's reached amplitude, from `run/FROZEN.json`, pinned by `run/FROZEN_PIN`. A read refuses a stored point of another case, cutoff, amplitude or pin, before any value is compared.

`dev/dev_loader.py` `7222d6626cb00055efbabbe126ff30381833cd1e1e1ef3e2b57afc941b3642a7`, output `dev/dev_loader.out` `03ddc2fbb20874140ffe085cafbb5d5597349f3baa83de4e10d37e85f914ea8f`: 6 of 6 checks pass, with no evolution.
- Every one of the 41 planned reads loads, and pairs with the frozen spectrum.
- C2a's recorded deviations from leading order are reproduced as `RECORD.md` states them, {1.0: [2.76, 2.86, 2.86], 2.0: [5.4, 5.59, 5.59]} in per cent at `N = 16`, 24 and 32. That holds the leading-order formula and the pairing to M8.16.1's own numbers.
- The arms are refused: `N = 16`'s point for a read at `N = 24`, another amplitude, another member, and a record that is not the pinned one.

## 4. The rigid families' first run, and a defect it found (2026-11-22T16:03:42Z)

`dev/dev_rigid.py` `511d52c4c45c2563c70a376e51c59c08b06cd41602b1b977de8eb1fbcab0824c`, development seed 7300202, with `member.py` `09e53e7101d1f7698a3eef1d7c9d91e1163fc07428922495af7325850d1c150d` and `readcore.py` `4c307afcf78f1d926b2486103d51a7061a1626156fb76ae7fee70ac54a56093c`, ran on 2026-11-22 into `dev/runs/20261122T150542Z/`, its output `rigid.out` `083aacff25849ecc83c722d9f24c60619559b69f027fc654d209c8e767f782eb`. It reads the rigid families at ‖φ‖² = 0.5 and 2, `N = 16` with the six-step ladder and `N = 24` at `h₀`, `T` = 30, the perturbation on `E₀`, held to Theorem 3.7's two frequencies on `E₀`.
- **In `R3`** every read admitted both frequencies with their sizes and Krein signs. The instrument's recomputed record was held to M8.16.1's stored record of C1 at the same amplitude and cutoff: 0.5 at N = 16: True, 0.5 at N = 24: True, 2.0 at N = 16: True, 2.0 at N = 24: True. The ratios of successive differences at `N = 16`: 0.5: [3.995949500497291, 4.00001994286472]; 2.0: [4.0002334234279235, 4.000287480665742].
- **In `R1`** every read failed its admission: two admitted eigenvalues against four, the `±2iω` pair missing.

**The cause, DERIVED.** `charge_free` removed the first-order change of every conserved charge, the two Sp(1) charges among them. Their generators are antilinear, so in the rotating frame they turn at `2ω`; their first-order directions are the `±2iω` modes themselves, and removing them left those modes unexcited. The prototype's control 6 removed only the phase charge. The charges the rotating frame conserves, the phase and right SU(2), have complex-linear generators; an eigenmode with a nonzero eigenvalue carries no first-order change of those, so removing them takes nothing the read reads.

**The fix.** `charge_free` now removes the phase and right-SU(2) charges only. A check at `N = 16`, `h₀` and `h₀/8`, development seed 7300202, admitted both frequencies in `R1` at ‖φ‖² = 0.5 and 2, Krein + and definite, the errors falling about sixty-fourfold from `h₀` to `h₀/8`. The arms did not run, since the first `N = 16` point failed its admission. The run is repeated whole, entry 5. This changes THE READ's step 3 in the terms, a choice made knowing this reading.

## 5. The rigid families, run again whole (2026-11-22T16:56:06Z)

`dev/dev_rigid.py` `33295ccdc67f9f68c46ab429398921958863faeded15b0d9e4993dd8d5cdf044`, development seed 7300202, with `member.py` `4c79049f166cdccc9dd0a886552b5bdae59f04119daa90388143ef410bc45be6` and `readcore.py` `4c307afcf78f1d926b2486103d51a7061a1626156fb76ae7fee70ac54a56093c`, ran on 2026-11-22 into `dev/runs/20261122T160353Z/`, its outputs `rigid.out` `3c5956aa5e2ef8e03534c8dc8eb065669ce2003e7fbfb8faa95673a1e47779d3` and `rigid.json` `4be2177f928b8753ba3a2d73bb03f3bc45498c41b10ff4ee4a3dc33b553ec095`. It repeats entry 4's run after entry 4's fix, at the same points, seed, ladder and `T`. The script changed in one place: the arms run at the first point at `N = 16` whose reads all admitted, so that a failed point no longer stops the run.
- **Every read admitted both frequencies,** in `R1` and `R3` at `‖φ‖²` = 0.5 and 2, at every step of the ladder at `N = 16` and at `h₀` at `N = 24`, each Krein + and definite as the record's groups are. The largest floor is 4.8 × 10⁻³ of its tolerance, where a tenth would leave a group Unresolved.
- **At `N = 16`** the errors fall fourfold per halving: at `h₀` from 2.0 × 10⁻⁵ to 3.8 × 10⁻⁴ relative, and at `h₀/32` from 2.0 × 10⁻⁸ to 3.7 × 10⁻⁷. The ratios of successive differences run from 3.9959 to 4.0003.
- **At `N = 24`,** at `h₀`, the errors run from 8.0 × 10⁻⁶ to 1.3 × 10⁻⁴.
- **In `R3`** the instrument's recomputed record was held to M8.16.1's stored record of C1 at all four points, within 10⁻¹⁰, with the same sizes and Krein counts.
- **The arms,** at `R1`, `‖φ‖²` = 0.5 and `N = 16`: the kick at half its factor, the broken pair and the flipped form each turned its check red.

`dev/dev_synthetic.py` `bf29b5af54ac2491e45fcbced08bec9edc176a0a349cf5a833633f397972c461` and `dev/dev_loader.py` `7222d6626cb00055efbabbe126ff30381833cd1e1e1ef3e2b57afc941b3642a7` ran again on this entry's `readcore.py` and on `loader.py` `50cdf037fa8405ba8e2368ad88029609dd0c7c9e0129d426404bb673fe984cb9`, unchanged since entry 3. Their outputs are `dev/runs/20261122T165550Z/synthetic.out` `2bcc745b973e99e8031cc6b114bee14211890254730fddb110455096d11f5158` and `dev/runs/20261122T165550Z/loader.out` `03ddc2fbb20874140ffe085cafbb5d5597349f3baa83de4e10d37e85f914ea8f`: 29 of 29 and 6 of 6 checks pass, byte for byte the outputs of entries 2 and 3.

These are the readings the terms name as known outcomes. The charge removal is the choice made knowing entry 4.

## 6. Entry 4's record, completed (2026-11-22T17:30:33Z)

**Entry 4's check after the fix** ran from the console and kept no file: a script read from standard input imported entry 4's `dev/dev_rigid.py` in its smoke mode, `T` = 10, with the fixed `member.py`, and read `R1` at `‖φ‖²` = 0.5 and 2, `N = 16`, at `h₀` and `h₀/8`, from development seed 7300202. Entry 4 summarizes its figures; entry 5 read the same points whole, with its outputs kept.

**Entry 4's scripts, as they ran.** No copy of `member.py` was kept before the fix. The file as it ran is rebuilt from today's by the fix's own edit, its earlier `charge_free` restored; nothing else in the file changed between the run and the fix. `dev/dev_rigid.py` is rebuilt the same way, with the arms' guard taken out. Both are kept: `dev/entry4_as_run/member.py` `09e53e7101d1f7698a3eef1d7c9d91e1163fc07428922495af7325850d1c150d` and `dev/entry4_as_run/dev_rigid.py` `511d52c4c45c2563c70a376e51c59c08b06cd41602b1b977de8eb1fbcab0824c`. The second matches the SHA-256 that entry 4 took from the file itself; the first matches the SHA-256 that entry 4 took from the same rebuild.

**A replay from them.** A first attempt, with `dev/dev_entry4_replay.py` `3967d14224ad8b40bc85a628c027602ab8d2a60a5ab7902867ce1602be94afbc`, stopped at its own import check before any read, because today's `dev_rigid.py` came first on the path. Its output, `dev/runs/20261122T172447Z/replay.out` `0af344540c102d363dfd8fa1597c72ec9a95bf2794e77a013845092bf61e855b`, is a traceback that names local paths. The script now loads both files by their paths. `dev/dev_entry4_replay.py` `b154c76ed9998ceb9b280165cf231ef4796524ca45c9c6960899004006bdaeca` read, in entry 4's order and from its seed, `R1` at `‖φ‖²` = 0.5 and 2, `N = 16` and 24, then `R3` at 0.5 and `N = 16`, each at `h₀` alone, into `dev/runs/20261122T172517Z/`, its output `replay.out` `90f1dbbf02a41cf69049e974d306e5505aab92bf8d3981bb128cdb7d48e347c6`. Each read prints as entry 4's run printed it: every `R1` read failed its admission, with two eigenvalues against four, and `R3` read errors of 2.0 × 10⁻⁵ and 4.2 × 10⁻⁵.

**What a reader can check.** Entry 4's `rigid.out` and that first attempt's output name local paths in their tracebacks. They stay out of the repository and of any packet; their SHA-256s are kept here and in entry 4. Everything else these entries name is kept with its SHA-256. The byte-for-byte agreements of entry 5 hold on the machine that ran them, macOS 15.8.2 on arm64, Python 3.13.13 and numpy 2.5.0; elsewhere the printed round-off digits can differ while every check passes.

## 7. What entry 5's directions excited (2026-11-22T17:36:38Z)

`member.py` `55a7d31cc4b8b71e1aa718a2aec48adbdbcf73e57d861507373b2c9cc4c5b2ad` adds one function, `excitation`; without it the file is entry 5's, byte for byte. For a set of directions, `excitation` reports two things. One is each direction's share of its rotating-frame norm in the target eigenspaces, after the charge removal and the normalization. The other is, for each target group, the singular values of the directions' spectral coefficients on its eigenvectors, taken by the left eigenvectors of the linear map at its eigenvalue. The terms' THE READ, step 3, was rewritten to report these before this entry ran.

`dev/dev_excitation.py` rebuilds each of entry 5's points, in its order and from its seed, as `dev/dev_rigid.py` builds them, and checks the rebuild against entry 5's `rigid.json`: the record, the step and the targets at every point, and at `N = 16` the read at `h₀` again, value for value. Its first version, kept as `dev/runs/20261122T173139Z/dev_excitation.py` `b337ae1195fceb13b0cc6ed86d60212015eda239f210a0f41879a855306168c8`, wrote `dev/runs/20261122T173139Z/excitation.out` `10c254edae30eb9b70bf44a310b6a0fc50f98ddb1870719dd45939bf6965a2c9` and `dev/runs/20261122T173139Z/excitation.json` `2df26a7f7cd2ff1c35f4aa6946453e8425d7ee491c897aa43178f63c1cdbbbe2`. `dev/dev_excitation.py` `be12feddb89c8132a083e44721bc4c10c9faac7267c7822ef06d115b9f768a0a` adds, on the lowest level `E₀`, its phase space's dimension and the rank there of the targets with the generalized kernel. It ran into `dev/runs/20261122T173414Z/`, its outputs `excitation.out` `3cc1af9d4f9b5edaa9bb95f3275ea05c8aa78c3e94dbf16b881111205b42d597` and `excitation.json` `9922c27b2f87a630eb6fa01459358924173a6d06db2721055c63dfaa1a39cceb`, with the shares and singular values unchanged. Every rebuild matched entry 5's.
- **The split was not even.** After the removal and the normalization, each direction kept from 0.869 to 1.000 of its norm in the target eigenspaces.
- **The count.** On `E₀` the targets and the generalized kernel span the whole phase space, 8 dimensions in `R1` and 12 in `R3`, at full rank. The part outside them is empty, so `directions` normalized the round-off left there to unit norm. The rest of each direction lay in the kernel, which the read's projection sets apart. The registered members draw that part from the whole space, where it is not empty.
- **Every group was spanned.** The directions' coefficients had full rank on every target group. The smallest singular value, 0.110, is on `R3`'s double group at `2ω`, at `‖φ‖²` = 0.5 and `N = 16`, read with two directions.

These are readings the terms name as known outcomes.

## 8. Entry 7's outside part, and what another machine rebuilds (2026-11-22T21:08:35Z)

`dev/dev_outside.py` `611c8bc18379c7ce0be5868e3975570fb87814305c0b36c60eebae72a41d9b64` rebuilt entry 5's points as `dev/dev_excitation.py` does. Beside it, it drew each direction again from the same draws, by a copy of `directions` that keeps the norm of the part outside the targets and the generalized kernel before and after its projection. Each copy's direction equals `directions`', bit for bit. It ran into `dev/runs/20261122T210740Z/`, its outputs `outside.out` `e42c5bc54101c024d88608915bb5202a6ffe466366408f5278a4c6dc3084d1de` and `outside.json` `06495c1e2d0c21626f44c54f396e165519dff771232e27f0f7a8d10d11aea0fc`.
- **The outside part was round-off.** On `E₀` it kept from 1.8 × 10⁻¹⁶ to 5.7 × 10⁻¹⁶ of its draw's norm after the projection, at every point of entries 5 and 7, and `directions` scaled it to unit norm, as in entry 4. That half of each direction is set by the machine's round-off (DERIVED, from the count of entry 7).
- **What another machine rebuilds.** It rebuilds the record, the step and the targets exactly. The directions come out as its own round-off sets them, and with them the reads and floors past their round-off digits and entry 7's shares and singular values. `dev/dev_excitation.py` checks its rebuild by equality, so that check holds on the machine that ran entry 5, as does the `R3` line of entry 6's replay; the replay's `R1` failures do not depend on it. This corrects entry 6, which said that elsewhere only the printed round-off digits differ.
- **Entry 7's share is of the squared norm,** where an even split is 0.5. `member.py` `4fba01e08d12e38f6a841d4f4235e9b5c919c3127721b1e9ac146f3ec51040e0` says so in `excitation`'s docstring; nothing else in the file changed.
- **The registered members** draw the outside part from the whole space, where it is not round-off.

## 9. A correction to entry 8 (2026-11-22T21:09:03Z)

Entry 8 says another machine rebuilds the record, the step and the targets exactly. They are computed from the member and the instrument, not from the directions, so another machine reproduces them to its own round-off, not bit for bit. That is enough to stop `dev/dev_excitation.py`'s check of its rebuild, which compares by equality. No file changed and nothing ran for this entry.

## 10. Runs that entries 1 to 9 do not name, and `readcore.py` between entries 2 and 4 (2026-11-23T16:35:05Z)

The session's record of the commands run lists these besides the runs entries 2 to 9 name. Each ran from the console and kept no file in this folder. None read a member, or a point the terms register.
- **Before entry 2,** `dev/dev_synthetic.py` once, as entry 2 names it: 29 of 29, as entry 2's run then printed. **Before entry 3,** `dev/dev_loader.py` once, as entry 3 names it: 6 of 6, as entry 3's printed.
- **Before entry 4,** `dev/dev_rigid.py` three times in its smoke mode, `T` = 10, reading `R3` at `‖φ‖²` = 0.5, `N = 16`, at `h₀` alone, with entry 4's `member.py` and `readcore.py`:
  - as first written, SHA-256 `1df78e6054860bbaa8aeeb1a8dfd7130811c315074825ffd303052df8a15b7bf`, it stopped on a syntax error before any read;
  - with the ladder passed as a parameter, SHA-256 `7c62cad6abbe97d81abb553df72d3606c2b790d300495f06ba941672999d8777`, it read both frequencies, with errors of 2.2 × 10⁻⁵ and 4.2 × 10⁻⁵, Krein + and definite, and its comparison with C1's stored record failed, because it compared every group where the store keeps representatives only; the three arms ran, each red;
  - with that comparison fixed, entry 4's script itself, kept in `dev/entry4_as_run/`, it read the same, held the record to C1's, and ran the arms, each red.
- **Checking two review packets,** from their unpacked copies: `dev/dev_synthetic.py` and `dev/dev_loader.py` with each; `dev/dev_rigid.py`'s smoke mode once, reading as the third run above; and `dev/dev_entry4_replay.py` and `dev/dev_excitation.py` once. Each run that a logged run names reproduced its logged output.

**`readcore.py` between entries 2 and 4.** Entry 2 names it `67d7b197…` and entry 4 `4c307afc…`. One edit lies between them. `floor` gained a `radius` argument, passed to its refit's admission, so that the rigid reads' widened circle governs their floor as well. Its default is the slow circle, so the synthetic reads are unchanged, and entry 5's synthetic output is entry 2's byte for byte. Taking the argument out of today's file, in its signature and its call to `admit`, gives entry 2's file back, to its SHA-256.

## 11. Control 6 at the development points, with its floor (2026-11-23T17:07:46Z)

`dev/dev_control6.py` `a60cdfa27c3a1873f63a9d7b44842bba68bf58ec6e471331f99574eb55198793`, development seed 7300303, ran on 2026-11-23 into `dev/runs/20261123T163147Z/`, its outputs `control6.out` `94165aa5b2a47e97863b3c8861e73ea3731db49ad8975a0f499bdeb1f3bba476` and `control6.json` `c4d5563fafab2cd5c8ddfc36064addb0a442820ab37f14316212cecfe9e87043`. It reads Theorem 3.7's two frequencies on `E₀` as the prototype's control 6 reads them, through the prototype's `controls.py`, read only, SHA-256 `86e167e4a9a33db6eea834a3eee071f613d2a28109250d77557269f9fb54805c`, with the prototype's registered parameters for control 6. It reads `R1` and `R3` at `‖φ‖²` = 0.5 and 2, `N = 16`, on the ladder `h₀` to `h₀/32`, and computes each read frequency's floor as the terms' step 8 does. Its copy of the read equals `controls.perturbed_run`'s at `h₀`, value for value. It ran because a review of the filed terms asked how control 6's floor enters (R1)'s rule.
- **Every read admitted both frequencies,** at every step.
- **The errors fell fourfold per halving,** to between 7.4 × 10⁻⁹ and 2.1 × 10⁻⁷ relative at `h₀/32`. The ratios of successive differences ran from 3.9999 to 4.0043.
- **The floors stayed level down the ladder,** within a factor of 5.8 at every frequency, where entry 5's fall about fourfold per halving at those steps, from 3.89 to 4.01.
- **Every ratio is eligible** under each reading of (R1)'s ten floors: the finer read's, the larger of a difference's two reads, and the largest of the three. The least margin is 3.18.
- **Not run:** `N = 24`, whose ladder would take hours, and the registered point, `‖φ‖² = 1`, which lies between the two read here. The run took about 35 minutes on one core.

## 12. Entry 10's two earlier scripts kept, and a docstring (2026-11-23T17:46:33Z)

Entry 10's first two smoke runs used `dev/dev_rigid.py` as first written and with the ladder passed as a parameter. Both are rebuilt from the session's edit record, as entry 10 hashed them, and are now kept: `dev/entry10_as_run/dev_rigid_first.py` `1df78e6054860bbaa8aeeb1a8dfd7130811c315074825ffd303052df8a15b7bf` and `dev/entry10_as_run/dev_rigid_second.py` `7c62cad6abbe97d81abb553df72d3606c2b790d300495f06ba941672999d8777`. The session's edit for the ladder takes the first to the second, and its edit for the comparison with C1 takes the second to entry 4's file, kept in `dev/entry4_as_run/`. `dev/dev_control6.py` calls its log entry 10 in its docstring; it is entry 11, and the file stays as it ran. Nothing ran for this entry.

## 13. A packet check's runs after entry 10 (2026-11-23T18:08:31Z)

The session's record of the commands run lists one run that entries 1 to 12 do not name. Checking the review packet of 2026-11-23, from its unpacked copy, `dev/dev_synthetic.py` and `dev/dev_loader.py` ran once each at 17:11Z, after entry 10 was written, as entry 10's packet checks did. Both scripts were this folder's, at the SHA-256s entries 2 and 3 name, `bf29b5af…` and `7222d662…`. Their outputs, kept outside this folder, are `dev/dev_synthetic.out` and `dev/dev_loader.out` byte for byte, `2bcc745b…` and `03ddc2fb…`: 29 of 29 and 6 of 6. Neither reads a member or a point the terms register. Every other run in the record is named by an entry: each run with a folder in `dev/runs/` by the entry that gives the folder, and the rest by entries 2, 3 and 10. Nothing ran for this entry.

## 14. Runs from the review packets on other machines, and a count in entry 13 (2026-11-23T18:29:51Z)

The review packets carried this folder, and its development scripts were also run from them on other machines, outside this session. Those runs are logged here as they were reported to this session; their outputs are not in this folder. The packets' scripts were at the SHA-256s their entries name; the wrapper and the copy below were written there. None read a member or a point the terms register, and every read of a rigid family was at entry 5's or entry 11's points, from their seeds.
- **From the packets of 2026-11-22, before filing:** `dev/dev_synthetic.py` and `dev/dev_loader.py`, four times each; `dev/dev_entry4_replay.py`, once whole and once in part; the first point of entry 7's report, twice; entry 5's eight points from its seed, by another wrapper and without the arms; and entry 5's directions, rebuilt by a copy of `directions()` that kept the outside part's norm, with the four `N = 16` points read again at `h₀`.
- **From the first packet of 2026-11-23, after filing:** `dev/dev_control6.py` at `R1`, `‖φ‖²` = 0.5, over the whole ladder, and at 2 to `h₀/8`, where it was stopped; and its first read at `R1`, 0.5, once more, against `controls.perturbed_run`.

Entry 13 counts one run where there were two, one per script, from one check. Nothing ran for this entry.
