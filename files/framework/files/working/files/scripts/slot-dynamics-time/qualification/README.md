# The time arm's qualification, M8.20: its code

The code that qualifies the time arm, `timearm.py` and `fftcubic.py` one folder up, byte for byte, on M8.16.1's instrument at its pin, under M8.20's terms on OpenWave. It is development code until the terms file and the freeze: nothing here is registered, and nothing in it earns credit before then. Every run is logged in `DEVLOG.md`, with its script's SHA-256 and each output's.

- `readcore.py`: the read that does not touch the instrument. It covers the one-step map fitted at the data's numerical rank, the mode fraction, the slow circle, mode admission, the floor, the Krein test and the ratio of successive differences.
- `loader.py`: M8.16.1's stored records and frozen values, each by its pin, and Theorem 4.2's leading order at a point.
- `member.py`: the member path on the pinned instrument: a slot at a cutoff, a member's linear record, the perturbation's directions with the charges the rotating frame conserves removed, the `±δ` pairs under the time arm, and their read in the member's rotating frame.
- `dev/`: the development runs so far, on synthetic systems, on the stored records, and on the rigid families at points the terms leave unregistered. They never run a member the terms read, nor a point they register (`DEVLOG.md`, entry 1).
- `dev/runs/`: each logged run's outputs, under the time it started. Two outputs whose tracebacks name local paths stay out of the repository; `DEVLOG.md` keeps their SHA-256s (entries 4 and 6).
- `dev/entry4_as_run/`: entry 4's two scripts, rebuilt as they ran (`DEVLOG.md`, entry 6).
