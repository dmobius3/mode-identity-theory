"""Run 2 against run 1, per multipole: G1b's deviation from Planck's spectrum before and after erratum E1, beside run 1's
lensing correction at the same multipole. Reads the two runs' g1b_diagnosis.out files; computes nothing new in CAMB.
Usage: python3 g1b_shift.py <run 1 g1b_diagnosis.out> <run 2 g1b_diagnosis.out>
"""
import re, sys


def rows(path):
    return {int(m.group(1)): (float(m.group(2)), float(m.group(3))) for m in re.finditer(
        r"^\s*(\d+)\s+([+-]\d\.\d+)(?:  > 2e-3)?\s+\(([+-][\d.]+e[+-]\d+)\)", open(path, encoding="utf-8").read(), re.M)}


r1, r2 = rows(sys.argv[1]), rows(sys.argv[2])
assert sorted(r1) == sorted(r2) == list(range(2, 30))
print(" l   run 1      run 2      shift      run 1 lensing   shift larger than run 1's lensing correction")
for l in range(2, 30):
    d1, x1 = r1[l]
    d2 = r2[l][0]
    s = d2 - d1
    print(f"{l:2d}   {d1:+.5f}   {d2:+.5f}   {s:+.5f}   {x1:+.1e}        {'yes' if abs(s) > abs(x1) else ''}")
over = [l for l in range(2, 30) if abs(r2[l][0]) > 2e-3]
shifts = {l: r2[l][0] - r1[l][0] for l in r1}
print(f"run 2 above 2e-3 at l = {over}; shift between {min(shifts.values()):+.5f} and {max(shifts.values()):+.5f}; "
      f"larger than run 1's lensing correction at {sum(abs(s) > abs(r1[l][1]) for l, s in shifts.items())} of 28 multipoles")
