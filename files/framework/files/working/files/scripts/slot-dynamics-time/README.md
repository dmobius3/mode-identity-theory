# The slot dynamics in time: files

The working record is [the page](../../slot-dynamics-time.md). This folder holds the work behind it.

| File | What it holds |
|---|---|
| `DESIGN.md` | the method, stated before the prototype runs and unedited once it starts: the equation, the instrument, the stepper and the rule that chooses it, the step bound, the FFT cubic, and the controls with their pass lines and stopping rules |
| `INSTRUMENT.sha256` | the SHA-256 of M8.16.1's 12 instrument files at its frozen commit, `d1c0ec8`, computed from git |
| `pin.py` | the check every script here runs before it imports the instrument: the 12 pinned paths, distinct and exactly the files present in the instrument folder, `__pycache__` aside, each against its SHA-256 in `INSTRUMENT.sha256` |
| `timing/` | the timing run before the dated note, of the instrument's dense cubic: `time_cubic.py` and its output |
| `fftcubic.py` | new code: the instrument's cubic and quartic energy through two-dimensional FFTs on its rule's angular nodes (§ 7), with the mutation arms of control 1 |
| `timearm.py` | new code: the two steppers, Störmer–Verlet and the splitting with the exact linear flow (§ 4), the stop when ‖c‖² exceeds C̄ (§ 5), the matched rigid waves, and the diagnostics |
| `controls.py` | new code: the controls of § 8, with the dry run that measures the floors first, then controls 1 to 11 under the stopping rules, and the rule of § 4. Every seed, size, duration and normalization is fixed in it, with the readings of the design it makes. It refuses the registered run until this folder's code is committed, and writes `record/` once |
| `fecheck.py` | new code: control 11, the cross-check against M8.15.x's finite-element Verlet |
| `FE.sha256` | the SHA-256 of the six finite-element modules and two frozen records that control 11 reads, at M8.15.x's freeze, `97a8c088`, computed from git |
| `DEVLOG.md` | the development log, append-only: every development run, on development seeds and at N ≤ 12, and what it showed; after the registered run, one replay of a registered run on its seed, outside the record (entry 14) |
| `dev/` | the development scripts the log names. None is a control, and none is in the record. Their outputs stay out of the repository: the seeds regenerate them |
| `record/` | the registered run's record, written once on 2026-11-21 from `d14d06be`: the dry run's floors, controls 1 to 11 and the rule of § 4, one JSON file each carrying the environment, the parameters and the sixteen readings, with `SUMMARY.json` and the run's log, `run.log`. The page's third dated note reads it |
| `SHA256SUMS` | the hashes of this folder's files, excluding itself |

To check the instrument by hand, from this folder:

```bash
shasum -a 256 -c INSTRUMENT.sha256
```

To repeat the timing, from this folder (Python 3 and numpy; the times are this machine's):

```bash
python3 -I -B timing/time_cubic.py R4 8 16 24 32
```

To run the controls on the development seeds, from this folder (Python 3, numpy and scipy; about ten minutes), into `dev/runs/`:

```bash
python3 -I -B -u controls.py --dev
```

The registered run, once, into `record/` (2 h 57 min on this machine; refused unless the code is committed and unchanged and `record/` is absent):

```bash
python3 -I -B -u controls.py
```
