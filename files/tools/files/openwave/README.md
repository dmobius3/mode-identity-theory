<a id="top"></a>
| **[`<back`](/files/tools/)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |

---

# 🏄‍♂️ M8 on OpenWave

[![OpenWave](/files/assets/openwave-banner-graphite.svg)](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/__M8_model_briefing.md)

[OpenWave](https://github.com/openwave-labs/openwave) is an open-source physics simulator that holds candidate field theories to the same public pass/fail criteria, one column per model, and M8 is MIT's. Each run there is pre-registered and frozen before it goes, and the maintainer reproduces or adjudicates the result in public review. The verdicts are OpenWave's, and so are the blind runs before M8.15; from M8.15 on, the author runs each task, and its run record is MIT's. This page maps every M8 task to its record on OpenWave, its outcome, and what MIT holds for it.

The tasks verify the mathematics and run effective models, and none of them settles a physics criterion: in OpenWave's [comparison table](https://github.com/openwave-labs/openwave/blob/main/MODELS.md#mit-m8), M8 has one cell partially validated, Λ / cosmic acceleration, on the spectral seed M8.1 confirmed, and its other 30 criteria are not yet tested.

## The Tasks

| Task | What it asked | Outcome | MIT's side |
|---|---|---|---|
| [M8.1](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_1_task_details.md) | A blind eigensolve of the twisted Möbius Laplacian: the certification gate | ✅ Passed: all five claims confirmed by two independent blind solvers, audited | [First Eigenvalue](/files/framework/files/bedrock/files/first-eigenvalue.md) |
| [M8.1.1](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_1_1_task_details.md) | A blind run on the coexact gap and the Galois pair | ✅ Both papers verify: 18 claims confirmed blind, two audits refuting nothing; ⚠️ the conversion identity is algebraically forced, a platform-side overclaim corrected at review | [Coexact Gap](/files/framework/files/bedrock/files/coexact-gap.md), [Galois Pair](/files/framework/files/bedrock/files/galois-pair.md) |
| [M8.1.2](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_1_2_task_details.md) | A blind run on the Surviving Ray | ✅ All 21 frozen claims reproduce, blind and audited; ⚠️ the packet's `w_K` wording was loose, the paper's is not | [Surviving Ray](/files/framework/files/bedrock/files/surviving-ray.md), its [first version](https://doi.org/10.5281/zenodo.22681502) |
| [M8.2](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_2_task_details.md) | The pre-registration lock for the field-dynamics program | ✅ Locked, author-contributed ([#350](https://github.com/openwave-labs/openwave/pull/350)) | on OpenWave |
| [M8.3](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_3_task_details.md) | A reproducer script for the mass formula | ✅ Complete, author-contributed ([#362](https://github.com/openwave-labs/openwave/pull/362)); it found a defect in the published page, since corrected | [Mass Spectrum](/files/spectrum/files/mass-spectrum.md) |
| [M8.4](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_4_task_details.md) | A survey of Lagrangian families on S³/2I | ❌ Closed unresolved: no target configuration ran; not a verdict on MIT dynamics | on OpenWave |
| [M8.5](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_5_task_details.md) | Simulation engineering on the quotient | ✅ Closed: the grid backend certified for its own target | on OpenWave |
| [M8.5-C](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_5_task_details.md) | A spectral dynamics substrate for S³/2I | ❌ `M8.5-C2-FAILED`, attributed to the instrument | on OpenWave |
| [M8.6](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_6_task_details.md) | A comparison with M5's lepton hierarchy | ❌ Closed without running: permanently inadmissible as instrumented | [Mass Spectrum](/files/spectrum/files/mass-spectrum.md) |
| [M8.7](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_7_task_details.md) | The 3D rendering port | Held behind its gate: field dynamics validated in-platform, through a future program nothing currently authorizes | none yet |
| [M8.8](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_8_task_details.md) | An independent-method reproduction of M8.3's torsion closed forms | ✅ Reproduced, under the protocol's convention-difference category; a first attempt's structural failure stays on record | [Mass Spectrum](/files/spectrum/files/mass-spectrum.md) |
| [M8.9](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_9_task_details.md) | Localizing a discrete-spectrum source | ✅ Adjudicated `S1b-SPECTRAL`: instrument defect, source not separated | on OpenWave |
| [M8.10](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_10_task_details.md) | The first correction at the level-6 critical rays | ✅ All frozen claims reproduce, blind; ⚠️ four solver checks could not fail, and the block cubic's `M_K` form is not unique; no value moves | §8 of the Surviving Ray's [second version](https://doi.org/10.5281/zenodo.24145098) |
| [M8.11](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_11_task_details.md) | Local branch germs at the level-6 critical rays | ✅ Every value reproduces blind; existence passes as an audited argument, for local germs at small amplitude, with no radius or stability; ⚠️ the `λ₄` lemma's sign step rests on M8.10's level sets | §8 of the Surviving Ray's [second version](https://doi.org/10.5281/zenodo.24145098) |
| [M8.12](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md) | The reduced Morse census of the level-6 quartic | ✅ Every frozen claim reproduces; one uniqueness clause left to M8.13; no stability claim, no radius | [Surviving Ray](/files/framework/files/bedrock/files/surviving-ray.md), §7.2, and its [certification scripts](/files/framework/files/bedrock/files/scripts/surviving-ray-v2/README.md) |
| [M8.13](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_13_task_details.md) | The uniqueness of the top-multipole maximum | ✅ Audited argument: the hexagon is the only maximizer; no stability claim | [Surviving Ray](/files/framework/files/bedrock/files/surviving-ray.md), §7.3 |
| [M8.14](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_14_task_details.md) | Fixed-edge stability of the conic carrier | ✅ Reproduced blind: strictly stable with the edge held fixed, at every embedded width; surface only, twist-blind | [The Fixed-Edge Stability Check](/files/framework/files/working/files/fixed-edge-check.md) |
| [M8.15](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_15_task_details.md) | The soft-slot branches at finite amplitude | ✅ Adjudicated per branch: five scored, two turning Hyperbolic within bracketed intervals; all eight persistence tests Persist; T1 INVALID and T4 Not reached in both slots, instrument outcomes | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics/RECORD.md); [The Soft-Slot Branches](/files/framework/files/working/files/soft-slot-branches.md) |
| [M8.15.1](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_15_1_task_details.md) | Locating the two changes of type | ✅ Adjudicated: no change of type located | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x-target1/RECORD.md) |
| [M8.15.2](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_15_2_task_details.md) | Locating them through the avoided crossing | ✅ Adjudicated: T3/R5's change of type located, under clause 3's qualifier; none located on T2/R4 | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15-2/RECORD.md) |
| [M8.16](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_16_task_details.md) | Qualifying a stationary harmonic Galerkin instrument | ❌ Not qualified: the pyramid's quartet 5.78% from leading order, over the 5% bar; the five controls pass, and no census row ran | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16/RECORD.md) |
| [M8.16.1](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_16_1_task_details.md) | That instrument's second and last qualification | ✅ Qualified: the instrument and nine rows; T5's second member not qualified | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16-1/RECORD.md) |
| [M8.17](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_17_task_details.md) | The census run | ✅ Adjudicated as recorded: four rows meet an S4 completion condition, and five are not settled by the run | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-17/RECORD.md) |
| [M8.18](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_18_task_details.md) | The census's two remedies | ✅ Adjudicated as recorded: T4/R5's change of type located; the items left open close instrument-limited | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-18/RECORD.md) |
| [M8.19](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/tasks/m8_19_task_details.md) | The census's persistence tests (S5) | ✅ Adjudicated, the record as filed: the coherent row in R5 Persists at 32; T1's and T4's stretches end untested | [run record](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19/RECORD.md) |

From M8.12 on, each Done row adds that the task leaves every `MODELS.md` cell and M8.7's gate as they were, and from M8.15 on, that it stands at the Row 6 ceiling. [The Slot Dynamics Census](/files/framework/files/working/files/slot-dynamics-census.md) gathers what M8.15 to M8.19 found, row by row, and how the census closed.

## Where the Files Are

The author's runs, M8.15 to M8.19, keep their folders beside the census, in `working/files/scripts/`, where their records pin them; the M8.15.x instrument that M8.15.1, M8.15.2 and M8.19 ran on is [`soft-slot-dynamics-m8-15x`](/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x/REPRODUCE.md). Before M8.15 the runs and their records are on OpenWave, the author's two contributions, M8.2 and M8.3, among them; MIT holds the papers and the checks they reproduced.

From the next M8 task on, each task's files live here, in a folder named for its ID with hyphens for dots, such as `m8-20/` or `m8-19-1/`:

| File | What it holds |
|---|---|
| `README.md` | the question, the links to the terms, the go, the method note and the adjudication, the outcome, and the page that carries it |
| `terms/` | a copy of the filed terms, byte for byte, with their hash and a link to the original |
| `run/` | the frozen code, its pins and its outputs |
| `RECORD.md` | the run record, built from the outputs |
| `DEVLOG.md` | the log from the build to the record |
| `POST_RUN.md` | what follows the run: the link to the adjudication, the author's records on both repositories, and dated notes |
| `tools/` | the scripts that build and check the record |
| `SHA256SUMS` | hashes of the task files, excluding this manifest |

## Outside M8

MIT's own computation, [`soft-slot-dynamics-mit`](/files/framework/files/working/files/scripts/soft-slot-dynamics-mit/RECORD.md), lies outside M8: as the maintainer answered on [#512](https://github.com/openwave-labs/openwave/discussions/512#discussioncomment-19339563), it runs on a different instrument from M8.16.1's, and OpenWave reads its values as MIT's own, outside M8's outcomes and `MODELS.md`.

## On OpenWave

The column's [roadmap](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/research/m8_roadmap.md) holds every task with its gates, and its [briefing](https://github.com/openwave-labs/openwave/blob/main/openwave/xperiments/m8_mit/__M8_model_briefing.md) the column at a glance.

---

| **[`<back`](/files/tools/)** | **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |
