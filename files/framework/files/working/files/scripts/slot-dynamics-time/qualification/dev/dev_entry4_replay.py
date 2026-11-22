"""Development: entry 4's run, replayed in part from its two scripts as they ran (DEVLOG entry 6). dev/entry4_as_run/
holds dev_rigid.py and member.py rebuilt to the SHA-256s entry 4 names. With them in place of today's files, this script
reads R1 at ||phi||^2 = 0.5 and 2, N = 16 and 24, then R3 at 0.5 and N = 16, each at h0 alone, in entry 4's order and
from its seed, and prints each read as entry 4's run printed it. Development seed only.

Usage: python3 -I -B -u dev_entry4_replay.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
QUAL = os.path.dirname(HERE)
AS_RUN = os.path.join(HERE, 'entry4_as_run')
sys.path[:0] = [AS_RUN, QUAL, os.path.dirname(QUAL)]
sys.argv = [sys.argv[0], os.devnull]
import importlib.util  # noqa: E402

import numpy as np  # noqa: E402


def as_run(name):
    """Entry 4's file by its path, so that no file of today's can stand in for it."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(AS_RUN, name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


member = as_run('member')
dr = as_run('dev_rigid')

assert os.path.dirname(os.path.abspath(member.__file__)) == AS_RUN and os.path.dirname(os.path.abspath(dr.__file__)) == AS_RUN
rng = np.random.default_rng(dr.SEED)
print(f'replay of entry 4: seed {dr.SEED}; T {dr.T}; h0 alone; numpy {np.__version__}', flush=True)
for slot, kappa, N in (('R1', 0.5, 16), ('R1', 0.5, 24), ('R1', 2.0, 16), ('R1', 2.0, 24), ('R3', 0.5, 16)):
    dr.point(slot, kappa, N, rng, lambda s: print(s, flush=True), (1,))
