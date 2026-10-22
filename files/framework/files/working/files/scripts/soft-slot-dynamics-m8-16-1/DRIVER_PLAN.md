# M8.16.1: the scoring code and the frozen-text tests (development step 2; plan v2, the units' reviews of v1 folded, 2026-10-22)

For the units first. This plan turns these sections of terms v3 into code in `run/`: THE NEXT-ORDER BAR; THE CASES: WHAT IS ADDED; T5'S SECOND MEMBER; THE VERDICT RULE: WHAT CHANGES; THE TESTS BEFORE THE FREEZE; and THE FREEZE, THE GUARD AND THE RUN. The code sits beside M8.16's `instrument/`, which is copied byte for byte. The plan follows M8.16's `DRIVER_PLAN.md` (v4) file by file, and whatever M8.16 built stands unless an item below changes it. Nothing sealed is constructed, solved or read, and no `FROZEN.json` is written. The code is built only after both units' GO.

## The tree

M8.16.1's folder is `soft-slot-dynamics-m8-16-1/` on the bench. At filing it goes to MIT as `scripts/soft-slot-dynamics-m8-16-1/`.
- **`instrument/` and `reference/m815/`** are M8.16's, copied from MIT `deec830`. Each of the fifteen files must equal its line in M8.16's manifest, and that manifest still reproduces M8.16's pin, `a5f45173…`, at `deec830` (36 entries).
- **Not copied:** M8.16's `run/`, `dev/` and `reference/m815_targets/`, and all of its outputs.
  - The target records stay named by blob id in `run/targets.json`, which is M8.16's file byte for byte.
  - `write_guard.py` copies them only after the go, and refuses unless each blob id matches.
- **`run/`** holds:
  - M8.16's files where nothing changes;
  - the changed and new files below;
  - step 1's `next_order_values.py` with its two outputs.
- **The filed terms** enter `run/` as `run/m8_16_task_details.md`, byte for byte, before the pin. `instrument/devtools.py` reads that name in `frozen()`, and `instrument/` cannot change, so M8.16.1's terms must carry M8.16's file name.

## What is built

**1. `run/cases.py`: seventeen cases** (changed).
- **The order.** `ORDER` follows THE RUN:
  - the controls C1, C2a, C2b, C3 and C2a/R5;
  - P5;
  - `C3R/R4`;
  - the samples T1/R4, T1/R5, T4/R4, T4/R5 and `T5J/R2`;
  - the ladders T2/R4, T2/R5, T3/R4, T3/R5 and T5/R2.

  The two new names are the ones the pinned values file uses.
- **The roles and columns.** `C3R/R4` takes the role `ray`, and `T5J/R2` the role `member`. Their columns come from the terms' table: `Q`, the signature, `(k, r_u)`, and the points `ε ∈ {0.25, 0.5, 1, 2}`. `_derive` gives each case its `V₀`, type and indices, as it does for every case:
  - C3R: `V₀` (6; 2, 0), Hyperbolic, (5, 1, 4);
  - T5J: `V₀` (10; 4, 0), Elliptic, (9, 3, 6).

  These are the table's values.
- **Their frozen spectra.**
  - T5J's is exact, from its slow polynomial, built the way T5's is: `τ² = 15680/1859`, and `τ² = −ν` at the roots of `418161601ν² + 6605190592ν + 25491013632`.
  - C3R's three `τ` have no closed form here. They are read from the pinned values file at its 25 digits, where its check A froze them.
- **The next-order values.**
  - Each case the bar reads carries its groups from `run/next_order_values.json`, by cutoff: P5, the ten rows, T5J and C3R.
  - Each group carries `s`, its multiplicity, class and Krein sign, `κs_g` and `c_g(N)`; at C3R, also `c_g°(N)`.
  - `serialize` writes them into `FROZEN.json`.
- **Each group is tied to its frozen mode** once, when the values are loaded:
  - the same class, Krein sign and multiplicity, one to one;
  - the slot's factor times `τ` equal to `s` to the precision the frozen value is written in: half a unit in the last digit of a decimal literal, and double precision for a value computed in floating point.

  On the pinned file, every tie holds. The largest relative difference is 3.2×10⁻¹⁰, at P5's quartet, whose literal has ten decimals. A tie that fails refuses the file.
- **New constants:**
  - the ceiling's factors, 0.1 and 10⁻³;
  - the resolution test's tenth;
  - check 4's floor factor, 0.1;
  - the points 0.25, 0.5 and 1.

**2. `run/seeds.py`: the two new seeds** (new).
- **Why it exists.** `instrument/branches.py` knows only M8.16's fifteen cases. For an unknown name, `seed_state` and `representative` raise `KeyError`, and `SEALED` has no entry for either new name.
- **What it holds:**
  - their representatives: C3R as `{2: 1, −1: 2}` on level 6 in `R4`, and T5J as the terms' four components on level 7 in `R2`;
  - `representative(name)` and `seed_state(name, B)`. For M8.16's names, both hand over to `branches`. For the new names, both build the vector with `branches._unit_vector`, so it follows the instrument's own convention.
- **Its guards** reproduce the instrument's own, as explicit raises, which `python -O` keeps:
  - `seed_state` refuses a new name unless `devtools.admitted(name)`, which is `branches.seed_state`'s test for a sealed seed;
  - `seed_for_check` refuses outside a seedcheck process, which is `branches.sealed_seed_for_check`'s test. Inside one, every solver path already refuses, through the instrument.
  - Both refuse a basis of the wrong slot or lowest level.

**3. `run/checks.py`: the next-order bar** (new functions).
- **The points.** For each group the bar reads, at each cutoff, the reading uses the points at 0.25, 0.5 and 1. Each `x_i` is the point's reached amplitude, `eps_reached`.
- **`λ_i`** is the mean of the computed values that K2's assignment gives the group's predicted modes. Where those values lie in one record group, that group's centre is used. For an imaginary pair this is the member at `+iτ`; for a quartet, its member in the first quadrant, as the record's representative groups give them.
- **The extrapolation.** With `h_i = (λ_i/x_i − κs_g)/x_i` and `κs_g` the values file's 25 digits:
  - `ĉ₂` and `ĉ₃` are the Lagrange values at 0 through two and three points;
  - the spread is `|ĉ₃ − ĉ₂|`;
  - `C_g(N) = max(0.1|c_g(N)|, 10⁻³|κs_g|)`.
- **Check 1.** At each point:
  - the point is accepted;
  - its cutoff's seed passed its check;
  - K1 holds at the point;
  - `converged` holds at that `ε`;
  - K2's matching holds over the slow band, with equal counts in every class-and-sign bucket.
- **Check 1 at K3(a)** (for the units, and for terms v4).
  - **The conflict.** A merged in-span mode breaks `V₀`, the indices and K2's matching. With check 1 as terms v3 writes it, the bar at K3(a) would then read Unresolved, and K3 "instrument failure". M8.16's K3 reads "not resolved, kernel exact: the diagnosis is wrong" in that case. Its terms say that (a) "never reads `A`'s zero cluster, so an in-span mode merged there does not fail (a)". So (a) reads L's certificate and the slow band outside the in-span pair's class, and a merged in-span mode leaves (a) to the certificate (`test_k3.py`, claim 7). Terms v3 also inherits K3's three outcomes unchanged, so its two statements conflict (FIXABLE).
  - **The plan keeps the outcomes** (both units: KEEP). At K3(a), check 1 asks only that the point be accepted, with its seed checked, and matched outside the in-span pair's class, as `theorem_r_outside` matches. `V₀` and the indices stay where M8.16 reads them, and K1 and K2 are not restored to K3(a)'s check 1.
  - **K4's pyramid item** reads check 1 as the terms write it.
  - **On M8.16's record** both readings hold at the pyramid. At 0.25, 0.5 and 1, every point is accepted, with K1, `converged` and K2's matching at every cutoff.
- **Check 2.**
  - **The association** (UA). After the one-to-one matching with multiplicity, each assigned record group is associated with its entry in the point's convergence summary by its exact eigenvalue-index set. The entry must agree with the record group in centre, class, size and Krein count, which the same record gives both. A multiple group may contribute several entries.
  - **The estimate.** Every associated entry must be usable, and `E` is the largest `‖P_g‖ max(‖R_g‖, u‖A‖)` among them.
  - **The test.** `E_c = Σ|w_i| E_i/x_i²`, with `w_i` the Lagrange weights at 0 of the reached amplitudes, must be at most `C_g(N)/10`.
  - **A missing, duplicated or inconsistent association** fails check 2, so the group reads Unresolved (UA). The summary keeps no entry for a group inside the gray zone, so such a group's association is missing.
- **Checks 3 and 4.** The spread must be at most `C_g(N)`, and `|c_g(N) − ĉ₃|` at most `max(spread, 0.1 C_g(N))`.
- **The reading:**
  - **pass:** checks 1 to 4 hold at every cutoff;
  - **fail:** check 3 or 4 fails at a cutoff where checks 1 and 2 hold;
  - **Unresolved,** otherwise, naming the failing check, cutoff and point.
- **Reported, unscored:**
  - `c_g`, `ĉ₂`, `ĉ₃`, the spread, the ceiling and `E_c`;
  - the two-term residual at 0.25, beside 1%;
  - the deviation from leading order, as M8.16 reports it.

**4. `run/checks.py`: the checks that read the bar** (changed).
- **K3(a)** requires three things: the seeds; L's certificate at 0.25 at every cutoff, as now; and the bar's pass on the quartet and the Krein-positive pair, with check 1 as above. `theorem_r_outside` stays, as the reported leading-order deviation. K3(b) to (d) and the three outcomes are unchanged.
- **K4's pyramid item:** `converged` at 0.25, the seeds, and the bar's pass on the same two groups.
- **K5:**
  - **The clauses that stay:** the seeds; at 0.25 at every cutoff, the point accepted with K1; and `converged` at 0.25.
  - **The bar:** every predicted group must pass. Its check 1 now scores 0.5 and 1.
  - **At ε = 2,** the readings stay reported and unscored, as in M8.16.
- **The C3 ray:**
  - **Its checks:** K1 and K2 at its four points; the bar on its three groups; and the discrimination. Wherever checks 1 and 2 hold, `|c_g°(N) − ĉ₃|` must exceed `max(spread, 0.1 C_g(N))`, with `C_g(N)` from `c_g(N)`, so that `c_g°` fails check 4 at `c_g`'s tolerance.
  - **Its outcome** is "passed", or the failing check named. It enters no other outcome.
- **T5J:** K5 alone, with no K6. Its outcome is its own.
- **`verdict`:**
  - **The instrument:** as M8.16's. The stop list stays C1, C2a, C2b, C3 and P5, so the C3 ray stops nothing.
  - **Rows:** as M8.16's, including the `R5` gate.
  - **New:** a `members` entry for T5J, and the C3 ray's outcome, under its own key.
  - **The verdict text:** QUALIFIED names the rows and members it qualifies; NOT QUALIFIED names the failing checks.
- **Unchanged:**
  - the matching and the band: `predicted`, `computed`, `match` and `slow_band`;
  - the band-edge guard and the withheld-point guard;
  - K3's spans, overlaps, pick and (d);
  - K1, K2, the controls' K4, C1's checks, K6 and its comparison, and the stop and `R5` functions.
- **`BAR` stays** for K3(b), the controls' K4 and C2a/R5.

**5. `run/driver.py`** (changed).
- **The order and the gate.** The order and roles are `FROZEN.json`'s, or `DRY.json`'s. The row gate also guards the roles `member` and `ray`, so nothing after the pyramid runs until the gate record shows K1 to K4 passed.
- **The seeds.** They come through `seeds.seed_state`. `load` checks each frozen representative against `seeds.representative`.
- **The dispatch.**
  - `ray`: K1, K2, the bar and the discrimination;
  - `member`: K5;
  - the pyramid and the rows: as M8.16's, reading the bar.
- **M8.16's dry-run claims are removed:** E1 to E7, `dry_claims` and its readers. They score M8.16's dry run against M8.16's development records. They also call `devtools.log_run`, whose numbering does not fit M8.16.1's log (§ The development runs).
- **The `--dry` mode stays,** admitting GO cases only. Each dry run's claims are scored by a script of its own, derived before the run.
- **Unchanged:** the outputs, the gate record, `VERDICT.json`, the transcript, the resume, the withheld points and branch identity.

**6. `run/write_guard.py`** (changed).
- **What `FROZEN.json` holds:**
  - the seventeen cases, with the next-order values;
  - `frozen_values()`, now covering every item of both texts' FROZEN VALUES, including `D`'s cut and K3's axis guard, the two values M8.16's file omitted (`RECORD.md` § 5), and the new constants;
  - the values file's SHA-256 and its cases-section SHA-256, with its environment;
  - the terms', manifest's and targets' hashes, and the go, as in M8.16.
- **It also refuses** unless:
  - the values file's cases section hashes to the SHA-256 it records;
  - its inventory (cases, cutoffs, and groups with class, Krein sign, multiplicity and bar membership) equals `cases.py`'s;
  - every check it records holds: A to F and X, with each multiple group scalar, and `N = 24` and 32 coinciding.

**7. `run/freeze_block.py`** (new). M8.16's freeze block named seven of the eleven files its seed check read (`RECORD.md` § 6). This script builds the block from the tree after the go, with every value read from a file, that list included:
- the terms' SHA-256 and the go;
- the manifest's table and both pins;
- the environment, with both readings;
- the target records;
- the seeds table, from the seed check's own record, with the files it imported;
- the values file's hashes;
- `FROZEN.json` in full, and the order.

The seed check, step 3, records the modules it loaded, and those its child processes loaded, as `next_order_values.py` records its own.

**8. Carried byte for byte, and not carried.**
- **Carried:** `pin_manifest.py`, `record_environment.py`, `name_targets.py` and `targets.json`. `ENVIRONMENT.json` is recorded again on the run's machine before the pin.
- **Not carried:** `score_dry.py`, `test_claims.py` and M8.16's test outputs, which test M8.16's dry run.
- **Rewritten for the plumbing pass:** `build_dry.py` and `DRY.json`, listing GO controls only.

## The tests (no solve; temporary trees; no sealed seed constructed)

**`test_guard.py`** (carried, extended). M8.16's thirteen tests, on M8.16.1's tree and order, plus:
- `C3R/R4` and `T5J/R2` refused on the name:
  - by `require` and by `seeds.seed_state` with no `FROZEN.json`;
  - by `seeds.seed_for_check` outside a seedcheck process;
  - by the driver, before the gate record.
- **The frozen path's green parent for `seeds.py`,** as test 8 builds one for `branches`. `devtools.GO` is emptied and C2a is entered in `seeds.py`'s own table at its slot and level. Its seed is then built through a valid test `FROZEN.json`, equal to its GO-path seed, and refused once the file is removed.
- **`seeds.py`'s guards under `python -O`,** each beside its green parent.
- **`write_guard.py`'s new refusals:**
  - a values file whose cases section differs from its recorded hash;
  - an inventory that differs from `cases.py`'s;
  - a recorded check that is false.
- **Its closing call to `devtools.log_run`,** at line 706, is removed, since it writes to the real log on exit. Its tests of `log_run` itself stay in their temporary root (UB).

**`test_k3.py`** (carried, two changes). Its claims on K3's spans, overlaps, (d) and pick run as filed, since those functions do not change.
- It reads M8.16's kept outputs, entry 245's, from M8.16's folder in the MIT checkout, each against the SHA-256 M8.16's `DEVLOG.md` records.
- Its closing call to `devtools.log_run`, at line 342, is removed (UB).

Claims 5 and 7 read K3(a)'s slow-band clause on C2a, a control with no next-order values. They move to `test_verdicts.py`, on pyramid records.

**`test_verdicts.py`, every verdict path** (new; the terms' test 1).
- **The method.** Each registered outcome comes from a record built from M8.16's recorded outputs, with the fields that outcome turns on edited. That record is scored by `checks.py`, and the test asserts the text the terms give the outcome. M8.16's outputs are read from MIT `87fc643` by git, each against the SHA-256 its `RUNLOG.json` records.
- **K1, K2 and the controls' K4:** a pass, and each way it can fail.
- **K3:**
  - "resolved";
  - "not resolved, kernel exact: the diagnosis is wrong", from claim 7's merged in-span mode: `V₀` broken, the cluster not separated, the in-span group removed at one cutoff;
  - "instrument failure: the diagnosis is untested", from each break of the certificate, a failed seed, a point not accepted, and the bar failing on the quartet.
- **The bar:**
  - a pass;
  - Unresolved by check 1 (a point not accepted, a group unmatched) and by check 2 (a projector unusable, `E_c` over its trigger);
  - a fail by check 3 and by check 4;
  - precedence: a fail at one cutoff beside Unresolved at another reads fail;
  - a group whose spread is tiny, with `|c_g − ĉ₃|` between the spread and 0.1 `C_g`, which must pass;
  - check 2's association (UA): in a record with two distinct imaginary groups of one Krein sign, their summary entries' index sets are exchanged, with their centres and classes unchanged. The test must read the inconsistency, and check 2 failed, rather than the other group's `E`.
- **The rows and members:**
  - K5 and K6 at a row;
  - the `R5` gate: an `R5` row is recorded not qualified, with C2a/R5's failing check named, and is not run;
  - T5J's independence: its failure leaves T5/R2's verdict, and the reverse.
- **The C3 ray:**
  - its failure, by the bar or by the discrimination, leaves the verdict and every row unchanged;
  - a `c_g°` that passes check 4 fails the discrimination.
- **The stops and the resume,** through `driver.main` with stand-in solvers, as `test_guard.py`'s tests 9 and 10.
- **Cutoff matching:** each cutoff's reading uses that cutoff's `c_g(N)`. A record missing a cutoff, or holding one the values lack, cannot pass.
- **Its arms.** Each outcome has one: the same record with the edit undone reads its parent, and a mutation of the scoring code turns the targeted assertion red. Two examples: check 4 without its floor, and check 1 at K3(a) with `V₀`.

**`test_constants.py`, every constant** (new; the terms' test 2). It runs on a test `FROZEN.json` written by `write_guard.py`'s own functions on a temporary tree.
- **Forward: each numeric item is classified** (UA). Every numeric item in both texts' FROZEN VALUES is one of three kinds, and the test fails if any item is left unclassified:
  - **(a) a literal scoring or guard constant.** It must be in `FROZEN.json`, equal to the value the pinned code reads.
  - **(b) an exact or algorithmically derived value.** It must be reproduced by its registered calculation, not matched to a source literal. The nominal weights 128/3, 8 and 1/3 are of this kind. The code computes its weights from the reached amplitudes, and at the nominal amplitudes its weight function must give them.
  - **(c) an explicitly unscored reported value.** It must be on an exclusion inventory, with its reason. The INFERRED tables and lists are of this kind (UB).
- **Locating a literal.** Each (a) item is found in one of three ways:
  - by name;
  - by a function's default: `continue_to`'s `tol` and `max_secant`, `newton.solve`'s `accept_rel`;
  - by its one occurrence in a named function's source: `D`'s cut in `linear.record`, the halving threshold in `newton.solve`, the seed check's `10⁻¹²` in the driver, and the overlaps in `checks.k3`.

  `BAR`, which `cases.py` and `checks.py` each define, is checked in both places.
- **Reverse** (UB, UA). The test scans `run/`'s scoring code: `cases.py`, `checks.py`, `seeds.py` and the driver, with the inherited checks as well as the new ones.
  - It finds every numeric literal, module-level constant and default from the implementation itself, independently of the list built from the terms.
  - Each must be an (a) item, or be on the test's list of non-scoring literals with its function and reason. That list is printed with the result.
  - The test runs before terms v4 is drafted, and each hit goes into v4's FROZEN VALUES or onto that list.
- **Known hits on M8.16's code,** none of them in FROZEN VALUES:
  - K2's slow-band factor 2, stated in THE CHECKS, and the band-edge guard's half, stated in THE CONVERGENCE RULE (UB);
  - K6's `ε` lookups at 10⁻⁹ and 10⁻¹² (UB);
  - `real_orthonormal`'s cut, `rel=1e-6`, in K3's spans;
  - among the driver's literals, C1's thresholds, 10⁻¹⁵, 10⁻¹⁴, 10⁻¹⁰ and 10⁻¹², stated in THE CHECKS.

  The new code adds check 4's floor factor.
- **Its arms:**
  - `FROZEN.json` without `D`'s cut, M8.16's defect;
  - `FROZEN.json` without `AXIS_MIN`;
  - `FROZEN.json` without check 4's floor;
  - a registered literal changed in a temporary copy, which tests equality;
  - a new scoring tolerance put into a temporary copy of `checks.py` with no FROZEN VALUES entry, which the reverse scan must turn red (UA). Changing a registered literal cannot test the reverse direction.

**`test_imports.py`, every import** (new; the terms' test 3).
- **The method.** The driver, `write_guard.py`, `freeze_block.py` and the seed check are each imported in a fresh `python3 -I -B` process on a temporary copy of the tree.
- **The test.** Every module file loaded from the tree must be in the manifest and named, with its SHA-256, in the freeze block that `freeze_block.py` builds there.
- **The seeds line** must name exactly the files the seed check loaded, as its own record lists them, including those its child processes loaded (UB). M8.16's seed check imports the instrument again in a `python3 -I -B -c` child (its claim 6), which an import in a fresh process does not see.
- **Its arms:** a seeds line with one loaded file dropped, M8.16's defect, and a module loaded from outside the manifest.
- **Before the seed check exists:** the test runs on the other three now, and on the seed check once step 3 lands.

## The development runs in this step

1. **The tests above,** each with its arms red.
2. **The record regression,** `run/score_record.py` (no solve).
   - **What it scores.** `checks.py` reads M8.16's recorded outputs: C1, C2a, C2b, C3, C2a/R5 and P5, from MIT `87fc643`, each against the SHA-256 its `RUNLOG.json` records. The pyramid's next-order values come from the pinned file.
   - **Expected,** derived from the terms' Known outcomes and `DEVLOG.md` entry 8:
     - the controls' K1, K2 and K4, and C2a/R5's K1 and K4, pass as recorded;
     - at the pyramid, K1 and K2 pass;
     - the bar's `ĉ₂` and `ĉ₃` equal those of the landed `next_order_check.py`, claim F, to the digits it prints;
     - the bar passes on the quartet and the Krein-positive pair at every cutoff, under both forms of check 1;
     - check 2 passes by entry 8's margins;
     - K3 reads "resolved", since on the record its (a) failed only at the slow-band clause, with the seeds and L's certificate holding at every cutoff, and (b) to (d) pass there;
     - K4 passes.
   - **What it does not do.** It computes no verdict, which only the registered run gives, and it claims nothing new: these are the terms' known outcomes, read by the code that will score the run.
   - **A mismatch** is a code defect against the frozen text, logged with its fix. It moves none of the bar's constants (UB).
3. **The plumbing pass.** `driver.py --dry --cutoffs 12 16 20` on the GO controls, as M8.16's two passes ran. Its claims, read by `run/score_plumbing.py`:
   - no exception;
   - every case's outputs are written and logged with their SHA-256;
   - the gate record is written, with the pyramid absent;
   - the verdict reads incomplete.

   It runs M8.16.1's loop on this instrument before step 4's ladder does.

**The development record.** `devtools.log_run` numbers a new entry by counting the log's `## ` headings. M8.16's log began at entry 0, and M8.16.1's began at 1, so in M8.16.1's log it would repeat the last number. No M8.16.1 script calls it, and the carried tests lose their closing calls to it (§ The tests). Each entry is written as entries 1 to 10 were: the script's SHA-256, the hashes of what it imports, and each output's. A `run/` script's outputs are kept under `dev/runs/` by run number.

## What terms v4 takes from this plan

These add to LOG entries 31 and 33's lists:
- check 1 at K3(a), and the conflict it resolves;
- `λ_g` at a multiple group: the mean of its matched values;
- check 2's estimate, from the summary's entries associated by exact eigenvalue-index set, each consistent with its record group, with `E` their largest, and a missing, duplicated or inconsistent association reading Unresolved;
- check 4's floor factor, among the new constants;
- FROZEN VALUES classified as literal, derived or unscored, with the reverse scan's hits each in FROZEN VALUES or on the non-scoring list;
- C3R's discrimination, at `c_g`'s tolerance;
- the filed terms at `run/m8_16_task_details.md`, the instrument's name for them;
- `freeze_block.py`;
- the development record kept without `log_run`;
- the record regression and the plumbing pass, among the development runs disclosed.

## The cost

- **The tests:** minutes in all.
- **The record regression:** under a minute. It reads 14.6 MB of JSON.
- **The plumbing pass:** a few minutes, as M8.16's two did (`DEVLOG.md` entries 215 and 216).

## What the plan does not do

- No `FROZEN.json`, no go, no sealed seed constructed or solved, and no filing.
- No change to `instrument/`, to `reference/m815/`, or to step 1's values.
- These follow, each on Blake's word with the units first:
  - **step 3, the seed checks:** all seventeen seeds in a seedcheck process, on the lowest level only. The terms name the two new ones; the freeze block lists every seed, so the fifteen are read again in this tree.
  - **step 4, amendment 5:** the amendment in M8.16.1's `BOUNDARY.md`, then C2a/R5's ladder through this driver's dry mode, 2 to 4 h;
  - **step 5:** terms v4.

## For the units

- (a) The tree. `instrument/` and `reference/m815/` are checked against M8.16's manifest lines. The terms sit at the instrument's fixed name.
- (b) The new seeds in `run/seeds.py`, with `branches`' guards reproduced.
- (c) The bar's code. In particular:
  - check 1 at K3(a);
  - `λ_g` at a multiple group;
  - check 2's association by exact index set, and its arm;
  - the reading's precedence.
- (d) The C3 ray's checks and discrimination, T5J's member outcome, and the verdict's additions.
- (e) `write_guard.py`'s additions, and `freeze_block.py`.
- (f) The three tests: especially the constant test's classification, its reverse scan and that scan's arm, and the import test's seeds line.
- (g) The record regression and the plumbing pass, with their expected outcomes.
  - A full dry run of the controls at the registered cutoffs is not planned. It would take about 2 h. The record regression already scores this instrument's real outputs, and step 4 runs the loop at the registered cutoffs.
- (h) GO or HOLD on step 2.
