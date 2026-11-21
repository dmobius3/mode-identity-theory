"""Development (DEVLOG entry 2): the FFT cubic and quartic against the instrument's dense ones, at N <= 12, on
development seeds 900001 up. Not a control."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fftcubic  # noqa: E402  (checks the pin and puts the instrument on the path)
import numpy as np  # noqa: E402
from instrument import basis, functional  # noqa: E402

seed = 900001
for slot in ('R1', 'R2', 'R3', 'R4'):
    for N in (8, 12):
        B = basis.Basis(slot, N)
        if B.m == 0:
            continue
        F, X = functional.Functional(B), fftcubic.FFTCubic(B)
        rng = np.random.default_rng(seed); seed += 1
        c = rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)
        c /= np.linalg.norm(c)
        gd, gf = F.cubic(c), X.cubic(c)
        e_dense = F.energy(c, 0.0) - 0.5 * np.sum(B.eig * np.abs(c) ** 2)
        print(f'{slot} N={N} m={B.m}: |cubic_fft - cubic_dense|/|cubic_dense| = {np.linalg.norm(gf - gd) / np.linalg.norm(gd):.1e}, '
              f'quartic rel diff = {abs(X.quartic(c) - e_dense) / abs(e_dense):.1e}')
