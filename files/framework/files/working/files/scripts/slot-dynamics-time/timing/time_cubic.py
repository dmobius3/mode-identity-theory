"""Times the instrument's dense projected cubic, as it stands, for one slot at the cutoffs given: the basis build, the
functional's build (with its table cache when the tables fit), and one cubic evaluation on a random coefficient
vector, twice. Engineering only: no branch and no physical value. It checks the instrument against its pin first.

Usage, from the folder above: python3 -I -B timing/time_cubic.py SLOT N [N ...]"""
import os
import platform
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pin  # noqa: E402

sys.path.insert(0, pin.instrument_path())
import numpy as np  # noqa: E402
from instrument import basis, functional  # noqa: E402

print(f'instrument pin checked; python {platform.python_version()}, numpy {np.__version__}, {platform.platform()}', flush=True)
slot = sys.argv[1]
for N in map(int, sys.argv[2:]):
    t0 = time.perf_counter()
    B = basis.Basis(slot, N)
    t1 = time.perf_counter()
    F = functional.Functional(B)
    t2 = time.perf_counter()
    rng = np.random.default_rng(1)
    c = rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)
    c /= np.linalg.norm(c)
    F.cubic(c)
    t3 = time.perf_counter()
    F.cubic(c)
    t4 = time.perf_counter()
    nodes = F.rule.size
    tables = nodes * B.r * B.m * 16 / 1e9
    print(f'{slot} N={N}: m={B.m}, nodes={nodes}, tables {tables:.2f} GB, cached={F.cached}; basis {t1 - t0:.1f} s, '
          f'functional {t2 - t1:.1f} s, cubic {t3 - t2:.2f} s then {t4 - t3:.2f} s', flush=True)
