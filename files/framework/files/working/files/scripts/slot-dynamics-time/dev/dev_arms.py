"""Development (DEVLOG entry 7): two mutation arms, planted so that they can bite, at N = 8 and 12, dev seed 900104.
Not a control. The grid one point short of exactness for the levels present, M = 4 max(levels), beside the 3N + 1
first planted and the exact 4 max(levels) + 1; and the missing conjugation of A in a basis whose intertwiners carry a
complex phase per copy, against the instrument's cubic transformed to that basis."""
import sys, copy, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fftcubic  # noqa: E402
import numpy as np  # noqa: E402
from instrument import basis, functional as fn  # noqa: E402
rng = np.random.default_rng(900104)
for slot in ('R1', 'R2', 'R3', 'R4'):
    for N in (8, 12):
        B = basis.Basis(slot, N); F = fn.Functional(B)
        c = rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m); c /= np.linalg.norm(c)
        Gd = F.cubic(c); nd = np.linalg.norm(Gd)
        out = []
        for M in (3 * N + 1, 4 * max(B.levels), 4 * max(B.levels) + 1):
            X = fftcubic.FFTCubic(B, M=M)
            out.append(f'M={M}: {np.linalg.norm(X.cubic(c) - Gd) / nd:.1e}')
        chi = {n: rng.uniform(0, 2 * np.pi, len(B.A[n])) for n in B.levels}
        B2 = copy.copy(B); B2.A = {n: [np.exp(1j * x) * a for x, a in zip(chi[n], B.A[n])] for n in B.levels}
        ph = np.concatenate([np.repeat(np.exp(1j * chi[n]), n + 1) for n in B.levels])
        ref = np.conj(ph) * F.cubic(ph * c)
        good = np.linalg.norm(fftcubic.FFTCubic(B2).cubic(c) - ref) / np.linalg.norm(ref)
        bad = np.linalg.norm(fftcubic.FFTCubic(B2, mutation='unconjugated_A').cubic(c) - ref) / np.linalg.norm(ref)
        print(f'{slot} N={N} levels {B.levels}: ' + ', '.join(out) + f'; phased basis: instrument {good:.1e}, unconjugated {bad:.1e}')
