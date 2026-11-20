<a id="top"></a>
| **[`<back`](/files/framework/files/dynamics/)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** | **[🌊](/files/tools/files/openwave/)** |

---

# ⏳ The Slot Dynamics in Time

**Type:** Program
**State:** Active
**Status (2026-11-20):** Opened, with its method stated in a dated note before the prototype runs: a time arm for M8.16.1's Galerkin instrument that keeps the continuous symmetry, the controls with their pass lines and stopping rules, and the rule that chooses the stepper. Only a timing of the instrument's cubic and a check of one identity of its basis at random points have run.
**Summary:** The slot fields' standing-wave branches evolved in time under the frozen slot action, on a discretization that keeps its continuous symmetry: first the instrument and its controls, then whether the small-amplitude spectral types predict the response to perturbation.
**Inputs:** `slot-action.md`, `slot-ground-states.md` (Theorem D), `slot-dynamics-census.md` (its rows, the rigid families among them), the Standing-Wave Branches (§§ 2.2 to 2.4, 3.3, 4, 5 and 6.2), M8.16.1's instrument (`scripts/soft-slot-dynamics-m8-16-1/instrument/`, frozen at `d1c0ec8`), the finite-element integrator (`scripts/soft-slot-dynamics-m8-15x/m8_15x_solver/`), and the #512 [boundary of 2026-10-15](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-18955679) and [answer of 2026-11-01](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19339563).

---

PROGRAM, with its method stated before the prototype runs. The [Standing-Wave Branches](../../dynamics/files/standing-wave-branches.md) leave the branches' dynamics to a sequel, which "needs a new discretization first, since the Galerkin method was qualified without time integration" (§ 6.2). This page carries that work. Its first step builds the discretization: M8.16.1's Galerkin instrument, unedited, with a time arm that keeps the phase, right-SU(2) and, in the quaternionic slots, Sp(1) charges exactly in exact arithmetic, and the instrument's exact cubic computed by FFT, adopted only if it agrees with the instrument's own cubic to round-off. The method, the controls and their pass lines are in [`scripts/slot-dynamics-time/DESIGN.md`](scripts/slot-dynamics-time/DESIGN.md). It is MIT's own computation, outside OpenWave's column.

**Related:** [The Slot Action](slot-action.md), [The Slot Ground States](slot-ground-states.md), [The Slot Dynamics Census](slot-dynamics-census.md), [The Hamiltonian–Krein Identification](hamiltonian-krein-identification.md), [Standing-Wave Branches](../../dynamics/files/standing-wave-branches.md).

## Notes

**Note (2026-11-20), on the instrument.** Before the prototype runs, the method is stated here. The sequel to the Standing-Wave Branches evolves the frozen slot action in time on M8.16.1's Galerkin instrument, at its frozen commit, unedited, with Störmer–Verlet as the reference and a splitting with the exact linear flow weighed beside it by a rule fixed in advance. The time arm is new code, so neither M8.16.1's qualification nor the admission of 2026-10-15 carries to it. The scheme keeps the phase, right-SU(2) and, in the quaternionic slots, Sp(1) charges exactly in exact arithmetic, and its energy is measured and gated. The cubic is computed by the instrument's rule, through two-dimensional FFTs on its uniform angular nodes, adopted only if it agrees with the instrument's own cubic to round-off. The controls, with their pass lines and stopping rules, are in the [design note](scripts/slot-dynamics-time/DESIGN.md) committed beside this note, unedited once the prototype starts. Before this note only a timing of the existing cubic, and a check of one identity of its basis at random points, have run. From the start the record names which results rest on the new code: the stepper and the FFT cubic. This prototype tests the instrument, not the persistence or instability of a census branch. The qualification that follows reads the small-amplitude frequencies at every soft-slot branch, with its criteria frozen in its own note after OpenWave's ruling on time integration. It is MIT's own computation, outside OpenWave's column: it reads none of the census's twelve unclassified points and says nothing about the closed spectral chassis.

---

| **[`<back`](/files/framework/files/dynamics/)** | **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** | **[🌊](/files/tools/files/openwave/)** |
