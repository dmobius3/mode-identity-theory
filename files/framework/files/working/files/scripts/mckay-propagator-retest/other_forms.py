#!/usr/bin/env python3
"""Deterministic post-run adjudication of McKay Propagator Correction's other forms on the corrected table (2026-10-03).

Not part of the registered re-test, which tested the literal Pi_T alone (retest.py, record retest.out). This applies the
same registered grade to the page's other complete parameter-free forms, so that the page's closure covers them:
  Pi    (§4.1): the product of C_geom over the intermediate nodes of the McKay path. delta (§4.3), exponentiated as a
        mass factor, is the same product; without that reading its insertion rule is undefined.
  kappa (§4.4): C_geom(rho) / (the product of C_geom over the intermediate nodes)^(1/dist).
Each is read multiplicatively at power 1, in both directions, re-benchmarked to the electron's own factor at (R7, triv),
and graded on retest.py's scored set by retest.py's grade: the uncentered RMS falls, every scored fermion ends within x3,
and |r| falls for d and for tau. Distance alone needs a coefficient, and branch splitting and the combined form need
weights the page does not define; they are outside the parameter-free class and are not computed.

Precondition: retest.py's input gates and self-tests pass. T1 checks both definitions on a toy path; --arms plants a
defect in each definition and requires T1 to catch it.
"""
import math
import sys

import retest


def pi_c(cgeom, inter, rho, plant=None):
    nodes = inter[rho] + ([rho] if plant == "pi-includes-target" else [])
    return math.prod(cgeom[i] for i in nodes)


def kappa(cgeom, inter, dist, rho, plant=None):
    n = dist[rho] + (1 if plant == "kappa-dist" else 0)
    return cgeom[rho] / pi_c(cgeom, inter, rho) ** (1.0 / n)


def toy(plant=None):
    dist, paths = retest.bfs([("R0", "A"), ("A", "B"), ("B", "C")])
    inter = retest.intermediates(paths)
    c = {"A": 2.0, "B": 3.0, "C": 5.0}
    ok_pi = pi_c(c, inter, "C", plant) == 6.0
    ok_kappa = abs(kappa(c, inter, dist, "C", plant) - 5.0 / 6.0 ** (1.0 / 3.0)) < 1e-12
    return {"T1 the C_geom path product and kappa match their definitions on a toy path": ok_pi and ok_kappa}


def main():
    res, (d, dist, inter) = retest.checks()
    res.update(toy())
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    if not all(res.values()):
        return 1
    rc = 0
    if "--arms" in sys.argv:
        for plant in ("pi-includes-target", "kappa-dist"):
            fired = not toy(plant)["T1 the C_geom path product and kappa match their definitions on a toy path"]
            print(("ARM FIRED " if fired else "ARM SILENT ") + f"T1 [{plant}]")
            rc |= 0 if fired else 1
    r0 = {f: math.log10(retest.mass(d, dist, rho, sig) / d["fermions"][f][2]) for f, rho, sig in retest.SCORED}
    forms = {"Pi (C_geom path product)": lambda rho: pi_c(d["C_geom"], inter, rho),
             "kappa": lambda rho: kappa(d["C_geom"], inter, dist, rho)}
    addr = {f: (rho, sig) for f, rho, sig in retest.SCORED}
    print(f"uncentered RMS before: {retest.rms(r0.values()):.3f}")
    verdicts = []
    for fname, fn in forms.items():
        bench = math.log10(fn(retest.BENCH[0]))
        delta = {a: math.log10(fn(a[0])) - bench for a in retest.ADDRESSES}
        print(f"{fname}: log10 correction rel. e at " + ", ".join(f"({a[0]}, {a[1]}) {delta[a]:+.3f}" for a in retest.ADDRESSES))
        passed = False
        for arm, s in (("multiply", +1), ("divide", -1)):
            r1, (c1, c2, c3), ok = retest.grade(r0, delta, s)
            cells = " ".join(f"{f} {r1[f]:+.3f}" for f, _, _ in retest.SCORED)
            print(f"  {arm}: r {cells}; RMS after {retest.rms(r1.values()):.3f}; (1) RMS falls {c1}; (2) all within x3 {c2}; "
                  f"(3) |r| falls for d and tau {c3}: {'PASS' if ok else 'FAIL'}")
            passed |= ok
        verdicts.append(passed)
        print(f"  {fname}: {'an arm passes' if passed else 'both arms fail'}")
    print("ADJUDICATION: " + ("a form passes (check)" if any(verdicts) else "NEGATIVE, every computed form fails in both directions"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
