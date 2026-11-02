"""The two cases M8.16.1 adds, as seeds (M8.16.1's terms: THE CASES: WHAT IS ADDED and T5'S SECOND MEMBER;
DRIVER_PLAN.md v2, item 2).

instrument/branches.py knows only M8.16's fifteen cases, and instrument/ is M8.16's byte for byte, so the C3 ray in R4
and T5's second member in R2 are built here. Each vector is made by branches' own _unit_vector, in its Condon-Shortley
components, so it follows the instrument's convention. The instrument's two guards are reproduced as explicit raises,
which python -O keeps:
  - seed_state builds a new seed only when a valid frozen allowlist lists it (devtools.admitted), as branches.seed_state
    does for a sealed seed;
  - seed_for_check builds one only in a seedcheck process (devtools.SEEDCHECK), as branches.sealed_seed_for_check
    does, and in such a process every solver path refuses, through the instrument.
Both refuse a basis of the wrong slot or lowest level. For M8.16's names, both hand over to branches.

base names the case whose branch a development ladder continues (BOUNDARY.md, amendment 5; LADDER_PLAN.md v2): X for
X:ladder. cases.py and the driver read it, so the rule has one home.
"""
import os
import sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from instrument import branches as br, devtools  # noqa: E402

# the new seeds (the terms' table): name -> (slot, lowest level)
NEW = {'C3R/R4': ('R4', 6), 'T5J/R2': ('R2', 7)}
# their representatives in Condon-Shortley components {m: coefficient}, unnormalized: the C3 ray v_2 + 2 v_{-1}; T5's
# member with complex structure j, u p0 with p0 = (1 + k)/sqrt(2) (t5_second_member.md)
REPS = {'C3R/R4': {2: 1.0, -1: 2.0},
        'T5J/R2': {3.5: np.sqrt(3 / 20), 1.5: 1j * np.sqrt(7 / 20), -1.5: np.sqrt(7 / 20), -3.5: -1j * np.sqrt(3 / 20)}}


def base(name):
    """The case whose branch a development ladder continues: X for X:ladder. Any other name is its own."""
    return name[:-len(':ladder')] if name.endswith(':ladder') else name


def representative(name):
    """The case's representative {m: coefficient}, as branches.representative gives M8.16's."""
    if name in NEW:
        return dict(REPS[name])
    return br.representative(name)


def _basis_ok(name, B):
    slot, n0 = NEW[name]
    if B.slot != slot or B.levels[0] != n0:
        raise PermissionError(f'seed {name!r}: the basis is {B.slot} from level {B.levels[0]}, not {slot} from level {n0}')


def seed_state(name, B):
    """The unit lowest-level representative, as basis coefficients. A new seed is sealed: it is refused unless a valid
    frozen allowlist lists it (devtools.admitted), as branches.seed_state refuses a sealed seed."""
    if name not in NEW:
        return br.seed_state(name, B)
    if not devtools.admitted(name):
        raise PermissionError(f'seed {name!r} is sealed and no valid frozen allowlist lists it (BOUNDARY.md)')
    _basis_ok(name, B)
    return br._unit_vector(B, NEW[name][1], REPS[name])


def seed_for_check(name, B):
    """A sealed seed's unit lowest-level vector for the seed check alone (amendment 2's scope): refused outside a
    seedcheck process, as branches.sealed_seed_for_check refuses; for M8.16's sealed names it hands over to it."""
    if not devtools.SEEDCHECK:
        raise PermissionError(f'seed {name!r}: sealed seeds are built only in a seedcheck process (BOUNDARY.md, amendment 2)')
    if name not in NEW:
        return br.sealed_seed_for_check(name, B)
    _basis_ok(name, B)
    return br._unit_vector(B, NEW[name][1], REPS[name])
