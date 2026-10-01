#!/usr/bin/env python3
"""Scores the M8.14 run of projective-carrier.md §IX's frozen independent check, from the two rooms' returns. R = 1.

The returns are copied byte for byte from openwave-labs/openwave at 63c5d03 (#610),
openwave/xperiments/m8_mit/research/m8_14/run/rooms/solver_{a,b}/results.json. MANIFEST holds the SHA-256 that the
record's rooms/SHA256SUMS states for them. Each return gives, at each width, the lowest six levels at every refinement;
the bottom is the first.

Checks (exit 1 on any failure):
  K1  each copy's SHA-256 is the record's
  K2  in each room, at each of the seven widths, the order from the last three bottoms, the Richardson extrapolation
      from the last two and the error estimate |λ_extrap − λ_finest| equal what the room reports, to 1e-12 relative
  K3  the two rooms' bottoms agree at every width and refinement to 1e-12 relative
  K4  under the frozen rules, the tolerance a relative 1e-3, each of the five frozen widths W/R = 1/4, 1/2, 1, 7/5,
      3/2 scores Reproduced in both rooms
  K5  the rules' Contradicted branch fires: the bottom at W/R = 1 raised by one percent misses by more than both the
      tolerance and ten times its error estimate
--arms plants a defect for each check and requires it to fire."""
import hashlib
import json
import math
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = {'solver_a_results.json': 'ceba30fbf658857edf0d2fad11a1ce1641e5e982e8c46951408536d314dcc200', 'solver_b_results.json': 'a942b737070b9256ca46ff5cb7555013db03b2d62988f047227cdda8f4008702'}
FROZEN = ["1/4", "1/2", "1", "7/5", "3/2"]
EXTRA = ["pi/2", "17/10"]
TOL = 1e-3


def load(name, plant=False):
    raw = open(os.path.join(HERE, name), "rb").read()
    if plant:  # planted: one byte changed
        raw = raw[:100] + bytes([raw[100] ^ 1]) + raw[101:]
    return raw


def target(w):
    a0 = math.pi / (2 * (math.pi / 2 if w == "pi/2" else float(Fraction(w))))
    return a0 * (a0 + 1)


def recompute(levels):
    b = [float(lv[0]) for lv in levels]
    p = math.log2((b[-3] - b[-2]) / (b[-2] - b[-1]))
    ext = b[-1] + (b[-1] - b[-2]) / (2**p - 1)
    return p, ext, abs(ext - b[-1])


def classify(p, ext, err, w, absolute=False):
    """The frozen Outcomes, at one width."""
    tol = TOL if absolute else TOL * target(w)
    miss = abs(ext - target(w))
    if not (p > 0 and math.isfinite(ext)):
        return "Unresolved"
    if miss > tol and miss > 10 * err:
        return "Contradicted"
    if miss <= tol and err <= tol:
        return "Reproduced"
    return "Unresolved"


def rooms():
    return {n: json.loads(load(n))["t4"] for n in MANIFEST}


def k1(plant=False):
    return all(hashlib.sha256(load(n, plant and n.startswith("solver_a"))).hexdigest() == h for n, h in MANIFEST.items())


def k2(plant=False):
    for name, t4 in rooms().items():
        for w in FROZEN + EXTRA:
            r = t4[w]
            levels = [list(lv) for lv in r["levels"]]
            if plant and name.startswith("solver_a") and w == "1":  # planted: the finest bottom moved by 1e-6
                levels[-1][0] *= 1 + 1e-6
            p, ext, err = recompute(levels)
            if max(abs(p - r["p"]), abs(ext - r["extrap"]) / ext, abs(err - r["err"]) / err) > 1e-12:
                return False
    return True


def k3(plant=False):
    t = rooms()
    a, b = t["solver_a_results.json"], t["solver_b_results.json"]
    for w in FROZEN + EXTRA:
        for k, (x, y) in enumerate(zip(a[w]["levels"], b[w]["levels"])):
            yb = y[0] * (1 + 1e-9) if (plant and w == "7/5" and k == 2) else y[0]  # planted: one bottom moved
            if abs(x[0] - yb) / abs(yb) > 1e-12:
                return False
    return True


def k4(plant=False):
    for t4 in rooms().values():
        for w in FROZEN:
            if classify(*recompute(t4[w]["levels"]), w, absolute=plant) != "Reproduced":  # planted: absolute reading
                return False
    return True


def k5(plant=False):
    for t4 in rooms().values():
        p, ext, err = recompute(t4["1"]["levels"])
        shifted = ext * (1.0 if plant else 1.01)  # planted: no shift
        if classify(p, shifted, err, "1") != "Contradicted":
            return False
    return True


CHECKS = [
    ("K1 the two returns are the record's bytes", k1),
    ("K2 each room's order, extrapolation and error estimate equal their recomputation from its levels", k2),
    ("K3 the two rooms' bottoms agree at every width and refinement", k3),
    ("K4 under the frozen rules, with a relative tolerance, all five frozen widths score Reproduced in both rooms", k4),
    ("K5 a bottom raised by one percent at W/R = 1 scores Contradicted", k5),
]


def report():
    t4 = rooms()["solver_a_results.json"]
    print("W/R    p        extrapolated    error est.   alpha0(alpha0+1)   rel. miss   rel. error   relative    absolute")
    for w in FROZEN + EXTRA:
        p, ext, err = recompute(t4[w]["levels"])
        tg = target(w)
        rel = classify(p, ext, err, w) if w in FROZEN else "control"
        ab = classify(p, ext, err, w, absolute=True) if w in FROZEN else ""
        print(f"{w:<6} {p:.4f}   {ext:.9f}   {err:.2e}     {tg:.9f}       {abs(ext - tg) / tg:.1e}     {err / tg:.1e}      {rel:<11} {ab}")


def main():
    res = {name: fn() for name, fn in CHECKS}
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    report()
    if "--arms" in sys.argv:
        assert all(res.values()), "arms need a green parent"
        rc = 0
        for name, fn in CHECKS:
            fired = not fn(plant=True)
            print(("ARM FIRED " if fired else "ARM SILENT ") + name)
            rc |= 0 if fired else 1
        return rc
    return 0 if all(res.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
