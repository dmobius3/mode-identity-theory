# M8.17: THE SLOT DYNAMICS CENSUS RUN, a delta on M8.16.1's terms

Pre-registration, for review. It governs nothing until the maintainer's go. **Sealed until the freeze:** all 56 first-time spectral readings, the four points M8.16.1 solved without a linear record among them, and every point the locator computes (§ THE POINTS). None of them has a classification on any instrument: M8.15 left each undecided, and M8.16.1 either never reached it or solved it without computing its record.

## TASK PLANNING

### The question

**What M8.16.1 settled.** The maintainer adjudicated M8.16.1 on [#653](https://github.com/openwave-labs/openwave/pull/653#pullrequestreview-5646373760) (2026-10-26): QUALIFIED. The instrument qualifies, with K3 resolved, and so do nine census rows: T1 to T4 in `R4` and `R5`, and T5 in `R2`. T5's second member, T5J/R2, is not qualified and is not offered to this instrument again. The after-verdict records landed on [#654](https://github.com/openwave-labs/openwave/pull/654#pullrequestreview-5658749898).

**What the census still needs.** The census page's catalog (MIT `e09d453`, § III) is the home of the rows' statuses, and S4 (§ VI) is the obligation: every nondegenerate row born elliptic accounted for at every registered point of its window, each classified point by a method shown adequate by a registered test. On the nine qualified rows the statuses leave these open:
- **T1 and T4, in both slots:** every registered point but M8.16.1's four samples, `ε` = 0.25, 0.5, 1 and 2, which read Elliptic and converged;
- **T2 in `R4`:** its change of type, bracketed in (11.31, 32), with M8.15's two points inside the bracket undecided;
- **T3 in `R4`:** `ε = 32`, which M8.15 left undecided;
- **T5 in `R2`:** `ε` = 45.25, 128 and 132, which M8.15 left Unresolved.

Two rows owe nothing here:
- **T2 in `R5`** is Elliptic at every point on M8.15's record.
- **T3 in `R5`** is closed on M8.15.2's location, under its clause 3 ([#632](https://github.com/openwave-labs/openwave/pull/632#pullrequestreview-5511519208)). The change of type is located between its guard readings, Elliptic at 15.6356 and Hyperbolic at 16.5832 at level 3. Its one undecided grid point, `ε = 16`, lies between them, so the location accounts for it.

**What this task asks:** classify each of those points with the frozen instrument and its frozen convergence rule, locate each change of type the classified points bracket, and record each of the nine rows' outcomes, stating separately whether it meets an S4 completion condition.

**Old and new evidence.** The instrument is deterministic, and every point M8.15 decided or M8.16.1 read has its outcome on record (§ Known outcomes). This task claims no new evidence from them. The new evidence is the 56 points above, never classified on any instrument, and the points the locator computes.

### Standing

- **The rulings it files under,** all on #512:
  - the answer of 2026-10-15 ([18955679](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-18955679)), whose § 3 is the boundary below;
  - the ruling of 2026-10-20 ([19071299](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19071299)), which made M8.16.1 the instrument's last qualification and set the census run's conditions;
  - the answers of 2026-10-20 ([19076863](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19076863)), § 2, on the census run's adequacy tests.
- **The conditions, and where they are met:**

| Condition | Where |
| --- | --- |
| The census run takes the next free ID | M8.17; ID, below |
| Its adequacy tests are its own, registered before its go and never redesigned after | § CLASSIFYING A POINT; § LOCATING A CHANGE OF TYPE |
| Only the rows and members M8.16.1 qualifies | § THE POINTS |
| The qualified code byte for byte | § THE INSTRUMENT, THE RULE AND THE CUTOFFS |
| A cutoff other than 16, 24 and 32 only after the structural kernel is measured on the controls against M8.16.1's K1, with the calibration unchanged | not taken: this run uses 16, 24 and 32 only |
| It repairs and reruns nothing | inherited, § THE FREEZE, THE GUARD AND THE RUN |
| A point it does not classify is not offered to this instrument again without a ruling | § THE ROW OUTCOMES |
| No persistence test (the boundary) | § What this task is not |

- **Word budget.** About 4,500 words, inside § 12.2's cap of about 8,000.
- **Run-before-write** (`PR_REVIEW_STANDARDS.md` § 12.2) is met: M8.16.1 ran and was adjudicated (#653), and its records after the verdict landed (#654).
- **ID.** M8.17, which no M8 file or open pull request carries. The BACKLOG row the filing creates allocates it (`ROADMAP_STANDARDS.md` § 6).
- **Inherited.** Every rule of M8.16.1's terms that this document does not change governs here: the filed text, SHA-256 `9d167129…`, the 47,420-byte prefix of [`m8_16_1_task_details.md`](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_16_1_task_details.md), and through it M8.16's. Inherited unchanged, in particular:
  - the instrument and the separation statement, the seeds and their check, continuation, the solve and its acceptance bound, and the linear record;
  - the cases' definitions, seeds and expected columns for the nine rows;
  - K1, applied here at every point;
  - THE CONVERGENCE RULE, as built and frozen, with its band-edge guard;
  - branch identity between `N = 24` and 32, as M8.16's terms define it;
  - THE RUN's interruption and resume rules, and its power and sleep conditions;
  - validity, and no search;
  - STATED LIMITS, with the additions below;
  - the guard, the freeze block and provenance, with new pins.
- **What this task changes:**
  - the points: every registered point the census still needs on the nine rows (§ THE POINTS);
  - what a classified point is, from the frozen rule and M8.15's adjudicated readings (§ CLASSIFYING A POINT);
  - a locator for a change of type (§ LOCATING A CHANGE OF TYPE);
  - how each row ends under S4, and what this run leaves to S6 (§ THE ROW OUTCOMES);
  - no qualification verdict: this task qualifies nothing.

  Its code is new, in `run/`, in a folder of its own beside M8.16.1's, which it leaves unchanged. The instrument's files are copied byte for byte.

### The boundary (#512, § 3, verbatim)

> Admitted on #512: a harmonic Galerkin instrument on the slot action's nontrivial sectors, used only for stationary continuation of named branches and their linear-spectrum record, under a law it derives and pins itself, with nothing from `m8_5c/design_inputs/` or the C2 room. It is not a second qualification of the spectral chassis that `M8.5-C2-FAILED` closed: M8.5-C2 does not rerun, no M8.4 observable enters, `M8.4-R1` never files, and its results say nothing about that chassis in either direction. Outside this admission: time integration in a harmonic basis, which is the closed route's evolving half and needs a ruling on this thread; any use as a route for the two MODELS.md criteria gated on field dynamics; and the census's persistence tests, which need their own pre-registration.

Every point below runs inside it.

### What this task is not

- **No persistence test,** per the boundary. S5's obligation for the Elliptic stretches this run finds on T1 and T4, where M8.15 ran none, stays open, under a pre-registration of its own (the census page, § V, step 5, the note of 2026-10-15). So does the census's close, which needs S5.
- **No new instrument, no revised code, no new bar.** The instrument, the convergence rule, K1 and branch identity are M8.16.1's, byte for byte. Nothing here relaxes them, and no point is read from fewer cutoffs than the rule registers.
- **No cutoff but 16, 24 and 32.** The ruling's route to another cutoff, with the structural kernel measured on the controls first, is not taken, and no higher cutoff is added after the freeze. A point the rule leaves Unresolved at these cutoffs stays unclassified on this instrument.
- **No point on T3 in `R5`,** whose outcome rests on known ones (§ THE POINTS), and **none on T5J** or T5's other members, which no qualification carried.
- **Not a rescoring of M8.15, M8.15.2 or M8.16.1.** Their verdicts stand as adjudicated.
- **No M8.4 object, and no slot relation, mass or particle state,** as in M8.16.1. Nothing here moves M8.7's gate or a MODELS.md cell (the census page, § VII).

### Known outcomes, and what is new

These have outcomes on record. This task names them and claims no new evidence from them.
- **M8.15's adjudicated readings** ([#620](https://github.com/openwave-labs/openwave/pull/620)), on one finite-element discretization with its two-level check, at every point it decided on T2 to T5, and **M8.15.2's location on T3/R5** (#632).
- **M8.16.1's readings** ([`RECORD.md`](https://github.com/dmobius3/mode-identity-theory/blob/292b158/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16-1/RECORD.md), § 5): the four samples of T1 and T4 in both slots, and every read point of the five ladders, the eleven Unresolved ones among them. At those eleven, this task's development record holds a read-only check: their failures are count changes and non-contractions on the cutoffs' spectra, not the grouping merge that failed T5J (`DEVLOG.md`, the grouping check).
- **T2/R5's reading on this instrument** is a known outcome, read under this task's test, and adds no new evidence.
- **This run recomputes the known points on its paths,** since only the pyramid's solution vectors are stored (§ THE FREEZE, THE GUARD AND THE RUN).

**New evidence:**
- T1 and T4's points beyond the samples: 50 in all;
- four points M8.16.1 solved for continuation without computing their record: T2/R4 at 16 and 22.63, T3/R4 at 32, and T5/R2 at 45.25. Its fifth such point, T3/R5 at 16, lies inside M8.15.2's location, and this run does not compute it;
- T5/R2 at 128 and 132, never solved on this instrument;
- the locator's points.

### Ownership and run format

Author-proposed, author-run, maintainer-adjudicated, as M8.16.1. One registered run on the author's machine, on mains power with sleep off, after the maintainer's go and the freeze block's pull request.

## THE INSTRUMENT, THE RULE AND THE CUTOFFS: UNCHANGED

The instrument is M8.16.1's, byte for byte: each file under `instrument/` carries the SHA-256 it has at MIT `d1c0ec8`, under the manifest M8.16.1's pin `8cc2d7e2…` covers. The cases' definitions, the seeds and their checks are M8.16.1's `run/cases.py` and `run/seeds.py`, byte for byte; the points are this task's. The cutoffs are `N = 16, 24` and 32, each from its own seed, along its own continuation path. Each point's solve and record use M8.16.1's `run/driver.py` functions, and its reading M8.16.1's `run/checks.py`, all byte for byte: K1 (`checks.k1`), and the convergence rule with its band-edge guard (`checks.reading`). Branch identity between `N = 24` and 32 is M8.16.1's driver's: the `N = 24` solution, embedded at `N = 32`, lies within `10⁻²` of its norm once the orbit-tangent components are removed, and the two records agree in type, `n(L)`, `n(D)`, `K`, Krein counts, `V₀`'s dimension and ranks. This task's own code orders the points, runs the locator and classifies.

## THE POINTS

**The windows** are the census page's (§ II), on M8.15's grid, `ε_k = 0.25 · 2^{k/2}`: in `R4`, `k = 0` to 16 with 72 appended, 18 points; in `R5`, `k = 0` to 14, 15 points; in `R2`, `k = 0` to 18 with 132 appended, 20 points.

| Row | M8.15 decided | M8.16.1 read | This run classifies | This run's path |
| --- | --- | --- | --- | --- |
| T1/R4, T4/R4 | none | 0.25, 0.5, 1, 2 | the other 14 | the whole grid, to 72 |
| T1/R5, T4/R5 | none | 0.25, 0.5, 1, 2 | the other 11 | the whole grid, to 32 |
| T2/R4 | Elliptic to 11.31; Hyperbolic from 32 | 16 points | 16 and 22.63, and the change of type | the grid to 22.63, and on to 32 where its type bracket is (22.63, 32), then the locator |
| T2/R5 | Elliptic at all 15 | all 15 | none: Elliptic throughout on M8.15's record | none |
| T3/R4 | Elliptic at 17, all but 32 | 17 points | 32 | the grid to 32 |
| T3/R5 | Elliptic to 11.31; Hyperbolic at 22.63 and 32; the change located between 15.6356 and 16.5832 | 14 points | none: `ε = 16` lies inside the location | none |
| T5/R2 | Elliptic at 17, all but 45.25, 128 and 132 | 17 points, to 90.51 | 45.25, 128 and 132 | the grid to 132 |

**Each path** starts at the case's seed at `ε = 0.25` and continues along the grid, as M8.16.1's driver continues a ladder. A point where the solve fails or is not accepted ends its cutoff's path, as inherited, and every later point on that path is untested at that cutoff.

## CLASSIFYING A POINT

This is S4's registered test for the feature it classifies: the linear type, with `(n(L), n(D), K)` and `k_i⁻`.

**On this instrument,** a point is classified when all of these hold:
- at every cutoff, it is accepted and K1 holds;
- the convergence rule, on its three cutoffs' summaries (`checks.reading`), reads it converged. "Converged" is the rule's verdict alone, not M8.16.1's `checks.converged`, which also asks the expected type and would refuse every change of type;
- branch identity holds between `N = 24` and 32.

The rule's type, with the highest cutoff's indices, is the point's.

**On M8.15's,** a point is classified when M8.15 decided it, by its adjudicated reading.

**A point is classified** when either instrument classifies it and neither contradicts the other: where both classify it, they must agree in type, `K` and `k_i⁻`. A contradiction leaves the point unclassified and is reported as a disagreement between the instruments. M8.16.1's K6 found none at the 79 points M8.15 decided and it read (#653). The record names the instrument that supplies each point's type. An Unresolved reading on this instrument is not a second confirmation of M8.15's.

**A point is not classified** when neither instrument classifies it, or when they disagree. On this instrument a point goes unclassified when it is untested at a cutoff, K1 fails, the rule reads it Unresolved, or branch identity fails. Each such point is named in the record, with the rule's reasons or the failure.

## LOCATING A CHANGE OF TYPE

S4's second ending needs each change of type located, by its `n(L)` interval and its guard readings.

**The brackets:**
- **A change already located,** M8.15.2's on T3/R5, keeps its location: its grid point inside the location, `ε = 16`, is accounted for, and the locator does not rerun it.
- **A type bracket** is two consecutive registered grid points of a row, both classified, whose types differ. A change of type across an unclassified grid point has no type bracket: it is bracketed by the nearest classified points and not located, with that point named.
- **An index bracket** is a type bracket whose ends have `n(L)` resolved at `N = 24` and 32, and different between the ends at both. These are the cutoffs that decide a location. `N = 16` is bisected where its ends' `n(L)` is resolved and different, and reported otherwise.
- **A type bracket whose ends' `n(L)` is resolved and equal at `N = 24` and 32** is a type change with no `n(L)` change, such as a Krein collision, which T1's Krein-mixed spectrum allows. The record names it: "Type change detected without an `n(L)` change. The registered index locator is inapplicable; the location remains OPEN. No location or S6 closure is claimed."
- **A type bracket whose ends' `n(L)` is missing or unresolved at `N = 24` or 32, or changes at one of them and not the other,** has inadequate index evidence. The record names it so: "The index evidence is inadequate; it is not evidence of no index change." It is not located, and no S6 closure is claimed.

**The bisection,** on each index bracket, at each cutoff on its own path:
- where an end has a known record but no stored solution vector, the registered path recomputes that end, and it passes the reproduction gate (§ THE FREEZE, THE GUARD AND THE RUN) before either inward continuation begins;
- the midpoint is the arithmetic one, and it is solved twice, by continuation from each end of the current interval;
- the two solutions must agree: the aligned distance between them, at that cutoff, is within `10⁻²` of the solution's norm once the orbit-tangent components are removed, and their `n(L)` is the same;
- each midpoint is recorded and K1 checked, and `n(L)` is read by inertia, as at a grid point;
- the half whose ends differ in `n(L)` is kept;
- it completes when the interval is narrower than `w/2 = 5×10⁻⁴` of its lower end.

**An unsuccessful stop,** at a cutoff, is any of these, and the record names which:
- a bracket end that is missing, or does not reproduce;
- a solve that fails or is not accepted;
- K1 failing;
- the two solutions disagreeing;
- `n(L)` unresolved;
- `n(L)` matching neither end, which reads two changes in the bracket.

**Located** means all of these hold. Otherwise the change is bracketed and not located, and the record names the condition that failed.
- The bisections at `N = 24` and 32 both complete, with no unsuccessful stop. `N = 16`'s is run and reported, and does not decide.
- Their intervals overlap, and their union, the change's `n(L)` interval, is narrower than `w = 10⁻³` of its lower end.
- The two cutoffs agree on the signed change: `Δn(L)` at `N = 24` equals `Δn(L)` at `N = 32`, and is not zero. A discrepancy is reported. `N = 16`'s is a reported diagnostic.
- **The guard readings** are classified on this instrument, each with its bracket end's type:
  - the lower guard sits at the union's lower end times `1 − δ` and the upper at its upper end times `1 + δ`, with `δ = 0.01`;
  - each is solved by continuation from its own bracket end, so that neither path crosses the change;
  - each is read at all three cutoffs at one `ε`, with branch identity between `N = 24` and 32;
  - a guard that is not classified is read once more at `δ = 0.05`, and the first classified reading counts;
  - a guard that would fall outside the window is not computed, and the change is not located.

**The name,** wherever it is reported: "a change of type located between the guard readings, with `n(L)` changing by `Δ` inside the interval at `N = 24` and 32". What the location does not establish is the change's identification with the genuine index crossing. That stays as the census page's step 2 note states it: The Hamiltonian–Krein Identification's Corollary I is a conditional test, and it is not applied here.

## THE ROW OUTCOMES

After the registered readings, each of the nine rows receives one of these run outcomes, from the classified points and the locations. Whether a row has met an S4 completion condition is stated separately, in the record:
- **Elliptic throughout:** every registered point of the window classified Elliptic.
- **Each change of type located:** every registered point classified, apart from those between a located change's guard readings, which its location accounts for; and every type bracket located.
- **Not settled by this run:** some registered point neither classified nor accounted for by a location, or some type bracket not located.
  - The record names each such point or bracket, with its evidenced cause, and claims no type there.
  - The row is not declared closed under S6 here. S6's same-root-cause or no-admitted-remedy condition is for the census page to establish, after the adjudication, and until then the row's census closure stays pending.
  - Under the ruling of 2026-10-20, a point this run does not classify is not offered to this instrument again without a ruling on #512.

T2/R5 ends Elliptic throughout, and T3/R5 with its change located, both on known outcomes.

S4's third ending, an Unresolved point documented after it survives an adequacy test, is not reached here: no registered test in this run tells a genuine degeneracy from the instrument's resolution.

**T5's upper window.** At T5's read points from 5.66 to 90.51, M8.16.1's eigenvalues are still moving between `N = 24` and 32 (the grouping check). So T5's 45.25, 128 and 132 will likely end Unresolved on this instrument, as on M8.15's. The census page may then consider closing them as instrument-limited under S6, but only where its condition is established. This run makes no S6 ruling, and reopening those points on this instrument takes a ruling on #512.

**For the catalog,** the census page's dated note after the adjudication gives each row's ending and moves its status, on MIT. M8.15's readings keep their discretization's label: a row classified on both instruments at every point is "on both discretizations", and otherwise each point's instrument is named. T3/R5's `ε = 16` stays unclassified, accounted for by M8.15.2's location.

## STATED LIMITS: WHAT IS ADDED

- **The calibration's range.** M8.16.1's stated limits carry over:
  - the margin was fitted in `R2`, `R3` and `R4`, so `R5` lies outside the fitted slots;
  - three cases' smallest-amplitude points lie below the fitted `m = ‖φ‖²`;
  - the ten-fold headroom is missed at 54 of 381 points, every cluster separated.

  T1 and T4 have never been solved on this instrument beyond `ε = 2`. Where K1 fails there, the point is not classified.
- **The rule at the cutoffs it registers.** At the eleven points M8.16.1 read Unresolved, this task's development record (the grouping check) finds count changes and non-contractions on the cutoffs' spectra:
  - at nine of the ten count changes, the cutoff with fewer members holds a same-sign eigenvalue just outside the closure's window (DERIVED), most of them read by proximity as the member the set lacks (INFERRED);
  - the non-contractions are eigenvalues still moving between `N = 24` and 32 at T5's larger amplitudes.

  This run changes neither the rule nor its cutoffs, so points like these end unclassified on this instrument. Where M8.15 classified them, M8.15's reading stands.
- **Two discretizations, one label each.** Where a row's classification rests on M8.15 at a point, it is the finite-element instrument's, on one discretization, as the catalog labels it.
- **T3/R5's location** is M8.15.2's, as adjudicated: between the registered guard readings, Elliptic at 15.6356 and Hyperbolic at 16.5832 at level 3. Its evidence does not place the change at the interpolated zeros. Its identification with the genuine `n(L)` crossing is not established, and the same-`ε` cross-level diagnostics near it read Unresolved.
- **The locator's resolution.** A location is an `n(L)` interval narrower than `10⁻³` of its lower end, with two guard readings, not a crossing point. Its identification with the genuine crossing is not claimed.

## THE TESTS BEFORE THE FREEZE

Each test is logged in this task's `DEVLOG.md` with its script's SHA-256.
1. **Every constant.** Every numeric item in this document is classified as a literal the code reads and `FROZEN.json` holds, a value its calculation reproduces, or an unscored report, with M8.16.1's reverse scan.
2. **The reader, on M8.16.1's outputs, with no solve.** The classification code reproduces M8.16.1's reading at every point it read, from its stored summaries, applying `checks.k1` at every point and branch identity from the stored identity records. It refuses all 56 first-time readings, the four withheld points among them, and the locator's points.
3. **The reproduction gate, on data already on record, with no solve:**
   - its exact comparison on M8.16.1's controls and pyramid, which reproduce M8.16's records;
   - its categorical comparison on amendment 5's `R5` ladder (`dev/runs/015_ladder/`), which reached 0.5, 1 and 2 by other steps than the registered C2a/R5 sample;
   - its withheld-point comparison on the stored solves at M8.16.1's five withheld points, whose records hold only the solve and acceptance fields.

   All three must pass, and a mutation of each compared field must fail them. The passing data carries no Krein counts, since C2a/R5's records hold none, so only the mutation arm exercises that field before the freeze; T1's Krein-mixed spectrum exercises it in the run. This shows the gate can pass where it should. It does not show that T1's and T4's new paths will reproduce M8.16.1's categories.
4. **The locator and the classification, on synthetic records, with no solve.** Each condition above must be load-bearing: it has an arm, a mutation that removes it and must let a counterexample through. The conditions:
   - `w/2` and the union's `w`;
   - both guard offsets, and the window bound;
   - the two-ends agreement;
   - a bracket end missing or not reproducing;
   - the overlap, and the signed `Δn(L)` agreement;
   - the two-change stop;
   - the type and index brackets, with the unchanged index and the inadequate index evidence kept apart;
   - the precedence, and the contradiction.

## FROZEN VALUES: WHAT IS NEW

- the grid, the windows and the points of § THE POINTS;
- the cutoffs, 16, 24 and 32;
- `w = 10⁻³`, its half for each cutoff's bisection, and `δ` = 0.01 and 0.05;
- the two-ends agreement's `10⁻²`, branch identity's own;
- M8.15's adjudicated readings, as copied in M8.16.1's `reference/m815_targets/`, with their SHA-256;
- M8.16.1's outputs, by the SHA-256 its run's log records (`run/out/RUNLOG.json`, `84f2c9f6…`);
- the instrument's files at `d1c0ec8` and this task's manifest pin.

## THE FREEZE, THE GUARD AND THE RUN

As M8.16.1's: the guard writes `run/FROZEN.json` and its pin, the freeze block files on OpenWave before the run, and the run starts after the maintainer's go. Two additions:
- **The known points reproduce,** by three rules:
  - **a point M8.16.1 read, reached by its own continuation steps,** must equal its record, field for field, its timings aside: every read point on the paths of T2/R4, T3/R4 and T5/R2, and `ε = 0.25` on T1 and T4;
  - **a point M8.16.1 withheld, reached by its own steps,** must equal its stored solve and acceptance fields, its timings aside: `accepted`, the reached amplitude, `λ`, `m = ‖φ‖²`, the floor and the evaluation count. These are the four points this run computes. Their spectral records are new, compared with nothing, and sealed until the run;
  - **T1's and T4's points at `ε` = 0.5, 1 and 2,** reached from different predecessors, must each equal M8.16.1's record in type, indices, `V₀`'s dimension and ranks, chains, Krein counts and the rule's verdict.

  The first point that does not reproduce stops the run, as a reproducibility failure, and nothing is repaired or rerun.
- **The estimate.** From M8.16.1's timings, about 15 to 16 hours of compute:
  - about 7.7 hours for T1's and T4's paths;
  - 3.8 for the paths of T2/R4, T3/R4 and T5/R2;
  - about 4 for the locator on T2/R4's change, its path recomputed from the seed to 32 and its midpoints solved from both ends;
  - about 2 to 6 more for each further bracket in `R4`, about 2 in `R2`, and about 4 to 9 in `R5`, by its row and its upper end.

## DEFINITION OF DONE

- **The record:**
  - every point of the nine rows' windows with its classification, its instrument and, on this instrument, the rule's reading;
  - every point not classified, with its cause;
  - every bracket, with its location or the condition it failed;
  - each row's ending.
- **The publication:** the record, `REPRODUCE.md` and the run's outputs, on MIT, in this task's folder.
- **The method note** on OpenWave, and the maintainers' adjudication.
- **The roadmap:** both M8 status rows record the filing, and the Done row states the adjudicated outcome.
- **After the adjudication,** a dated note on the census page with each row's ending and its catalog status, any S6 question the record raises, and S5's obligation stated as open.
