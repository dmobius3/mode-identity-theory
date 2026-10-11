# M8.15.x: qualification (§ 6), under option (a) (registered 2026-10-09, v2)

**Status:** registered, v2. It folds both review units' redlines of draft v1. It is frozen before any qualification run starts. The registration time is stamped at the foot.

## 1. What is being qualified

**The instrument** is the bench solver in `m8_15x/solver/m8_15_solver/`, under option (a) (`RESULT_2.md`): § 2 keeps the 0.9 rule. Its differences from the frozen solver at `6058f95` were computed from the files, not recalled.

| File | Change | Grounds |
|---|---|---|
| `pinned.py` | The stopping test reads the full bordered residual, with every multiplier (§ 1a). The slice covector is projected into Newton's solve space. An optional slice reference is added, unchanged by default. The controls' cases `P5` and `P5a` are added. Without a slice, only the stopping test changes, so the closing controls' Newton iterates do not. | § 1a, ratified in #620; the amendment of 22:00:59Z; the carry |
| `continuation.py` | Each Newton record carries `μ`. | § 1a ("μ and ν are recorded") |
| `m815_branch.py` | A record on every end, and a crash record with its stage, traceback and frozen block, plus test hooks for controls only. `μ` is recorded at every point (`gauge_multipliers`). | § 4; § 1a |
| `m815_controls.py` | `μ` is recorded at every control point. | § 1a |
| `m815_common.py` | The pyramid's frozen spectrum and dimension, for controls only, and a quartet type in `predicted`. | controls 1b, the carry and 2a |
| `verdict.py` | The classification is split into reusable steps (`reclassify`), with no change in output (`regress_verdict_refactor.log`). | 2a |
| `persistence.py` | The summary records `N_obs`, `N_step` and `T_int`, taken from `run_test`'s own `every`, `nsteps` and `nsteps·dt`, in the summary only. The time series are unchanged. | § 5 |
| `angle.py` (new) | § 1b's angle solve and the carry, for slice cases. The closing controls and Target 1 do not use it. | § 1b |

**Not in the instrument:** `cluster_rule.py`, 2a's candidate rule, which did not qualify.

## 2. The bench, certified first

1. **The environment.**
   - It is recorded at the start, with the same fields as `MANIFEST.json`'s `environment`, and compared field by field.
   - Any difference stops the qualification before a rerun.
   - Today's readings, taken while this was being drafted, match: Python 3.13.13 (conda-forge), numpy 2.5.0, scipy 1.18.0, macOS 15.8 arm64, Accelerate, all four thread variables at 1.
2. **A frozen-bytes arm.** `spreads` is run from `6058f95`, from a copy checked byte for byte against the commit. Its `spreads_L2.json` must equal `controls_first_2026-10-07/spreads_L2.json` bit for bit. That certifies the bench, so any later difference belongs to the code.
3. **The static inputs.** `freeze_numbers.json`, `dt_L2.json` and `orientations.json` are copied from M8.15's frozen `out/` and checked by SHA-256 against the repo. No qualification job writes `dt_L2.json`.
4. **A clean output folder.** The bench's earlier `out/` is archived, not overwritten, and the qualification writes into a fresh one.

## 3. The regression: the closing controls rerun

**The jobs** are M8.15's closing controls, as `REPRODUCE.md` lists them:
- `linear 3`, `linear 2` and `theoremD 3`;
- `spreads`;
- `dynamics` for C1, C2a, C2b and C3;
- `rate`;
- `summarize`.

**The baseline** is `out/controls_first_2026-10-07/`, the frozen bytes' own rerun in the one-thread environment.
- `theoremD_L3.json` is filed nowhere in the repo. Its baseline is therefore the frozen gate together with the recorded value, Theorem D to `1.2×10⁻¹³`. The rerun must pass the gate, and its value is reported against that figure.

**The comparator.**
- It walks each record's structure. It fails on any key added or removed, outside the listed new fields.
- `.npy` series are compared bitwise.

**Allowed to change:**
1. **`residual`,** now the full bordered residual. Both the old and the new value must be at or below `10⁻¹¹`, and `|new − old| ≤ Σ_k |μ_k| + 10⁻¹³`.
   - This is the triangle-inequality bound. The new test adds exactly the `μ` terms, and each gauge vector has the norm of `M x`, since the fibre maps are isometries.
   - `μ` is read from the record's `gauge_multipliers`.
2. **New fields:** `gauge_multipliers`, and `N_obs`, `N_step` and `T_int`.
3. **Timing fields:** `seconds`.

**Must reproduce bit for bit: everything else.** That includes:
- every Newton iteration count, and `σ`, `ε` and `m`;
- every eigenvalue, and every verdict and gate field;
- every time series and summary value.

**If a Newton iteration count moves,** it is accepted only if both of these hold:
- a frozen-bytes trace of that solve, made as control 1a traced its arms, shows the old and new test values straddling `10⁻¹¹` at that iteration, by the `μ` term;
- every verdict and gate is unchanged, and the downstream numbers agree within the branch rule of § 5.

Otherwise it is a regression failure. Such a straddle is very unlikely, because without a slice `μ` is round-off and Newton's last steps jump by orders of magnitude.

**`spreads` and `summarize`.**
- The new `spreads_L2.json` must equal `controls_first`'s bit for bit.
- The new `freeze_numbers.json` must then differ from the frozen one only in `s2`, by exactly the recorded amounts: `1.054×10⁻¹⁰` relative in R4, `2.23×10⁻¹¹` in R5 and `2.00×10⁻¹¹` in R2.
- As in M8.15, the frozen values govern.

## 4. The § 5 unit check

For every dynamics record:
- `N_obs = round(1/dt)`;
- `N_step = round(T/dt)`;
- `T_int = N_step · dt`;
- the series' times are `(k · N_obs) · dt`, with the integer product taken first, for `k = 0, …, ⌊N_step/N_obs⌋`. They are compared bitwise.

## 5. The branch reruns: required

**What runs.** `m815_branch.py C3 4` and `m815_branch.py C2a 4`, at both levels, with their persistence scheduling.
- **Why they are needed.** `m815_controls.py` does not import `m815_branch.py`. So without these, the edited driver's first full ladder would be a target's.
- **What each adds.** C3 is Hyperbolic at every point, so it covers the cross-level side that Target 1's guard offsets read. C2a adds the driver's own persistence runs.
- **What neither covers:** a change-of-type bisection, or a crash. Target 1's bisection and guard offsets are new code, and they need their own tests in Target 1's registration.

**The governing freeze numbers.** The branches read the frozen `freeze_numbers.json`, the governing values that M8.15's branch records were made with. `summarize` runs last, after both branches have started.

**The baselines** are `out/branch_C3_R4.json` and `out/branch_C2a_R4.json`. They were committed with the frozen solver, but whether they predate the one-thread pin is not recorded. The comparison:
- **must match exactly:**
  - every categorical result: types, verdicts, classes, end reasons, persistence verdicts and the schedule;
  - the record's structure, apart from the listed new fields.
- **numbers:** `|new − old| ≤ max(10⁻⁹ |old|, floor)`, with these floors:
  - **eigenvalues and other complex values:** `10⁻¹³` times the largest modulus in the same list;
  - **persistence diagnostics at round-off** (`r`, `max_dref`, `charge_drift`, `energy_drift`, `energy_secular_drift`, `max_drot`, `max_d`, `max_dperp`): `10⁻¹¹`;
  - **every other number:** zero, so the relative rule alone applies.
- **`residual`:** the rule of § 3.
- **The report.** It records whether each record came out bit-identical or only within tolerance, and lists every field that used a floor.

## 6. The controls of § 6.3, on the final bytes

Memo § 6.3 requires 1a, 1b, 2a and control 4. Several ran on bytes that changed afterwards: control 4 before § 1a edited `m815_branch.py` and `pinned.py`, and 1a before `pinned.py` gained its slice reference. So they rerun on the final bytes, each against its registered checks. Each record carries the SHA-256 of every instrument file.

| Control | Rerun | Its checks |
|---|---|---|
| 4, arm a | `m815_branch.py C2a 4 --test-levels 2,1 --eps-max 0.5 --test-newton-maxit 1` | a full branch record, ending "Newton failure at the seed", exit 0 |
| 4, arm b | `... --test-raise-at 'level 2'` | a crash record with stage `level 2`, its traceback and the frozen block; exit 1 |
| 1a | `control_1a.py`, then `control_1a_amended.py` | `REGISTER_1.md`: 1a's seven, then the amendment's seven |
| 1b | the angle solve and the frozen arm, without the two reference runs | `REGISTER_1.md` checks 1 to 5; check 6 is carried forward only if the selected solution equals the earlier run's bit for bit |
| The carry, and the ν-sign kind | `control_carry.py`, `control_kind.py` | their registered ten and seven |
| 2a | not rerun | It stands as run: its rule is not in the instrument. |

These reruns take about half an hour. **Any unreviewed regression deviation, here or in §§ 3 to 5, blocks the freeze.**

## 7. The plan

**Memory.** A level-3 phase peaks near 6.4 GB, so only one runs at a time.
- **Stream A** holds everything at level 3, one job after another: `linear 3`, `theoremD 3`, the C3 branch, then the C2a branch.
- **Stream B:** dynamics for C1 and C2a, then `rate`.
- **Stream C:** dynamics for C2b and C3, `linear 2`, then `spreads`.
- **`summarize`** runs once B and C are done, by which time both branches have started.
- **The order:** first § 2's certification, then § 6's controls, then the three streams.

The whole qualification takes about 10 to 11 h of wall time, most of it the C2a branch.

## 8. After qualification: the freeze

1. **M8.15's folder stays byte for byte as it is.** Its `SHA256SUMS` still passes 52 of 52.
2. **The revised solver lands in a folder of its own,** with its own manifest, built as `m815_freeze.py` builds one: SHA-256 of every instrument file, `angle.py` included and `cluster_rule.py` left out, plus its own `SHA256SUMS`.
   - If `orientations` is rerun for that manifest, the new `P5` and `P5a` entries are the allowed change there.
3. **The target gate.** M8.15's `out/FROZEN.json` gates M8.15's targets only. The revised solver gets its own guard file, written at the freeze after the maintainer's go and with Target 1's frozen terms' SHA-256 on `main`. `m815_branch.py` reads it from its own folder.
4. **Then Target 1's pre-registration.**

*Registered at 2026-10-09T14:33:42Z, before any qualification run.*

## Amendment (2026-10-09T14:35:39Z): the branch floors, before any run

Written before any qualification run, after reading the branch baselines' structure. This was done while the comparator was being built, and before any qualification output existed. It concerns only § 5's numerical floors.

1. **Complex values.** Their floor is `max(10⁻¹³ S, 10⁻¹²)`.
   - `S` is the largest slow modulus at the same point, taken over `genuine_all` and `lifted`. Outside a point record, `S` is the list's own largest modulus.
   - The reason: the lifted eigenvalues are small, so a floor scaled to their own list falls far below eigensolver round-off. A floor of `10⁻¹²` is about `10⁻⁷ τ₀⁽³⁾`, far below anything a classification reads.
2. **Entries of the form `[eigenvalue, Krein value]`** (`genuine`, `genuine_all` and the fast search's `found`) take the complex rule for the eigenvalue, and the plain rule for the Krein value.
3. **`backward_error`** joins the round-off diagnostics, with floor `10⁻¹¹`.
4. **Krein values** join the round-off diagnostics, with floor `10⁻¹¹`. A scan of both branch baselines for round-off-sized numbers left without a floor found only these: C3's real pairs and quartets carry Krein values near `10⁻¹⁸`, since their Krein form vanishes. That scan is exhaustive: every other round-off-sized number in the two baselines is already covered.

## Note (2026-10-09T19:51Z, after the run): § 3's rationale

§ 3 says the new test adds exactly the μ terms. The run showed otherwise. The new test also evaluates the physical residual through the real forms `Kr` and `Mr`, where the frozen test applies `K` and `M` as complex matrices. At a converged iterate that difference in rounding, not the μ terms, sets the move. The rule itself is unchanged, and it passed: every move used at most 0.60 of its bound. See `RESULT_3.md`, "The residual".

## Amendment (2026-10-09T20:24Z): after both units' review of the results, before the freeze

Both review units gave GO after fixes on `RESULT_3.md` v1. This amendment carries those fixes. It changes no threshold and no result.

1. **§ 1, `pinned.py`'s row, corrected.**
   - The stopping test also evaluates the physical residual from Newton's own real-form `F` (`Kr`, `Mr`), where the frozen test called `standing.residual` (`K`, `M` complex).
   - Newton's update is unchanged, so the iterates are too. The test's value moves at round-off.
2. **§ 3, read at level 3.**
   - **The bound, at the same iterate:** `|new − old| ≤ Σ_k |μ_k| ‖T_k‖/‖M x‖ + (the recoding's move)`.
   - **A correction to the rationale.** § 3 says each gauge vector has the norm of `M x`. Each `T_k` is built at the solve's starting point, so that holds there, not at the converged iterate. At the two traced level-2 seeds, `‖T‖/‖M x‖` is 0.999988 and 0.999724 (`diag_residual.out`).
   - **The level-3 reading.** Every level-3 move is at least 2.66 times `Σ|μ|`, with one gauge per solve. The iterates are unchanged, so the recoding moved every one of the 46.
   - **Its one premise:** `‖T‖/‖M x‖` stays below 2.66 at those points. It is not recorded there.
3. **§ 3's `10⁻¹³` term** was a registered numerical allowance, not a proved bound on the changed evaluation. It absorbed the recoding's round-off, using at most 0.60 of the bound, and it is not read as a bound on that round-off.
4. **§ 8's sequence, corrected.** § 8.3 had the guard file carry Target 1's frozen terms' SHA-256 at the freeze, while § 8.4 put Target 1's pre-registration after the freeze. They now read:
   - **3. The target gate.** M8.15's `out/FROZEN.json` continues to gate M8.15 only. The revised solver receives its own guard file after Target 1's terms are frozen on `main` and their SHA-256 is recorded, before any target run.
   - **4. Target 1's pre-registration** follows the instrument freeze, before that guard file is written.
5. **At the freeze: two checks and one record.**
   - **Hashes.** Each included file's SHA-256 in the new manifest must equal the hash `QUALIFICATION.json` recorded for it, so that the frozen folder holds exactly the qualified bytes.
   - **Imports.** In the frozen folder, without `cluster_rule.py`:
     - `m815_branch.py`, `m815_controls.py`, `verdict.py` and `angle.py` must import cleanly;
     - no module may load from outside the folder;
     - no file in it may name `cluster_rule`.
   - **Theorem D's record.** The qualification's `theoremD_L3.json` is filed with the freeze, so that the next qualification has a baseline on record.

## Note (2026-10-09T20:53Z, at the freeze): Theorem D's baseline

§ 3 says `theoremD_L3.json` is filed nowhere in the repo. That is wrong: it was filed with M8.15's frozen solver in `6058f95`, as `m8_15_solver/out/theoremD_L3.json`, and M8.15's `SHA256SUMS` pins it. The qualification's rerun is byte-identical to it. The comparison ran as registered (the frozen gate, with the value reported against the recorded figure) and passed. Against the filed record it also matches bit for bit. Item 5 of the amendment of 20:24Z stands: the new folder files its own copy beside its manifest.
