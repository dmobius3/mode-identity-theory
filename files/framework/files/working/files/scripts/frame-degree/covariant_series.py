#!/usr/bin/env python3
"""Companion to s3-2i-oph-dictionary.md, section III. Multiplicities of Q and Q' in Sym^a Q over 2I, from class sizes and traces, compared
with the series sum_g t^g / ((1 - t^12)(1 - t^20)) for the stated generator degrees g, and with
the residues mod 30 that the proposition's congruences allow. Standard library only.
"""
import math

PHI = (1 + 5 ** 0.5) / 2
# (class size, trace under Q) for the nine classes of 2I
CLASSES = [(1, 2.0), (1, -2.0), (30, 0.0), (20, 1.0), (20, -1.0),
           (12, 1 / PHI), (12, -PHI), (12, PHI), (12, 1 - PHI)]
TWIN = [(1 / PHI, -PHI), (-PHI, 1 / PHI), (PHI, 1 - PHI), (1 - PHI, PHI)]


def twin(t):
    """Trace under Q' = Q composed with sqrt5 -> -sqrt5."""
    for x, y in TWIN:
        if abs(t - x) < 1e-12:
            return y
    return t  # rational traces are fixed


def chi_sym(a, t):
    th = math.acos(max(-1.0, min(1.0, t / 2)))
    if abs(math.sin(th)) < 1e-12:
        return (a + 1) * (1 if t > 0 else (-1) ** a)
    return math.sin((a + 1) * th) / math.sin(th)


N = 95
mQ = [round(sum(s * chi_sym(a, t) * t for s, t in CLASSES) / 120) for a in range(N)]
mQt = [round(sum(s * chi_sym(a, t) * twin(t) for s, t in CLASSES) / 120) for a in range(N)]


def series(gens):
    c = [0] * N
    for g in gens:
        for i in range(0, N, 12):
            for j in range(0, N, 20):
                if g + i + j < N:
                    c[g + i + j] += 1
    return c


print("Q  in Sym^a Q, first degrees:", [a for a in range(N) if mQ[a]][:8])
print("Q' in Sym^a Q, first degrees:", [a for a in range(N) if mQt[a]][:8])
print(f"a < {N}: multiplicity of Q  equals series for generators 1, 11, 19, 29: {mQ == series([1, 11, 19, 29])}")
print(f"a < {N}: multiplicity of Q' equals series for generators 7, 13, 17, 23: {mQt == series([7, 13, 17, 23])}")


def allowed(r5):
    return [m for m in range(30) if m % 2 == 1 and m % 5 in r5 and m % 3 != 0]


print("residues mod 30 that are odd, +-1 mod 5 and prime to 3:", allowed({1, 4}))
print("residues mod 30 that are odd, +-2 mod 5 and prime to 3:", allowed({2, 3}))
