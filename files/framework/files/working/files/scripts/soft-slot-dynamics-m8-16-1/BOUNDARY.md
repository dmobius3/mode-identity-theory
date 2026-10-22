# M8.16.1 development: the build-versus-qualification boundary

Fixed 2026-10-22T18:01:46Z, before amendment 5's ladder runs. M8.16.1's split is M8.16's. xrodz's ruling on [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19071299) carries it over: "author-side development runs only a GO list, as M8.16's split does". That split is Blake's ruling of 2026-10-15, with its four amendments, the correction to amendment 1 and the note to amendments 2 and 3, in M8.16's [`BOUNDARY.md`](https://github.com/dmobius3/mode-identity-theory/blob/deec830b29f4bd6b45e58d2c333946dbbb60e964/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16/BOUNDARY.md), SHA-256 `a54619de4a31e0abc12e5e7ef55165a5ad0b2fcd9ec9f921b9eb55c7208a4eea`. M8.16.1's terms (§ The split) state what stays SEALED until M8.16.1's freeze.

This file adds one amendment. It is not edited after its first write: a change enters as a dated amendment or note at the bottom, and DEVLOG.md records each one.

## Amendment 5, 2026-10-22T18:01:46Z: `R5`'s coherent branch, along M8.15's grid to `ε = 32`, joins the GO list for development only

Blake's decision of 2026-10-20, with both units' agreement, recorded in M8.16.1's terms (§ The split) and in DEVLOG.md's entries 1 and 22. `R5`'s coherent branch, C2a/R5, is on the GO list for its sample under amendments 3 and 4. It also runs along M8.15's grid, `ε_k = 0.25 · 2^(k/2)` for `k = 0` to 14, from 0.25 to 32, at `N = 16, 24` and 32, before the freeze. It is logged in DEVLOG.md and disclosed, and it earns no qualification credit. It is not a registered control: amendment 4's run of the branch in the registered run, at the controls' points, is unchanged.

**Why it leaks nothing.** It solves only C2a/R5's branch, whose sample is on M8.16's record. It is not a census row, the C3 ray in `R4` or T5's second member, the cases M8.16.1's terms seal, and its readings say nothing about any of them.

**Why it is needed.** No `R5` ladder has run on this instrument, and the margin was fitted in `R2`, `R3` and `R4` (M8.16's terms, STATED LIMITS). In the registered run, T2 and T3 in `R5` run along this grid. This ladder is the only evidence on `R5`'s acceptance and calibration along a ladder that unseals no row.

**Its reading** is amendment 3's note's, with one difference. It reports against the calibration as it stands, and no constant is refitted on it. The calibration's constants are in `instrument/linear.py`, which M8.16.1's terms fix byte for byte (THE INSTRUMENT: UNCHANGED). If one of the calibration's own conditions fails, the failure is disclosed, and a refit would be a revised instrument, which files only under a ruling on #512.

A failed calibration condition is preserved and returned to Blake and the units before further development. Amendment 3's conditional language does not authorize changing `instrument/` or the registered calibration under M8.16.1. Any proposed change that breaks the byte-identical-instrument condition requires a separate maintainer ruling; it is not part of this amendment.

Everything else in M8.16's BOUNDARY.md stands as written.
