# The slot dynamics in time: files

The working record is [the page](../../slot-dynamics-time.md). This folder holds the work behind it.

| File | What it holds |
|---|---|
| `DESIGN.md` | the method, stated before the prototype runs and unedited once it starts: the equation, the instrument, the stepper and the rule that chooses it, the step bound, the FFT cubic, and the controls with their pass lines and stopping rules |
| `INSTRUMENT.sha256` | the SHA-256 of M8.16.1's 12 instrument files at its frozen commit, `d1c0ec8`, computed from git |
| `pin.py` | the check every script here runs before it imports the instrument: the 12 pinned paths, distinct and exactly the files present in the instrument folder, `__pycache__` aside, each against its SHA-256 in `INSTRUMENT.sha256` |
| `timing/` | the timing run before the dated note, of the instrument's dense cubic: `time_cubic.py` and its output |
| `SHA256SUMS` | the hashes of this folder's files, excluding itself |

To check the instrument by hand, from this folder:

```bash
shasum -a 256 -c INSTRUMENT.sha256
```

To repeat the timing, from this folder (Python 3 and numpy; the times are this machine's):

```bash
python3 -I -B timing/time_cubic.py R4 8 16 24 32
```
