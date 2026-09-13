"""Where erratum E1's shift sits, per multipole: split into the unlensed spectrum and the lensing step, from the two runs'
g1b_diagnosis.out files alone (no new CAMB computation). With d = lensed/Planck - 1 and x = unlensed/lensed - 1 per run,
the lensed shift is (1+d2)/(1+d1) - 1, the unlensed shift (1+d2)(1+x2)/((1+d1)(1+x1)) - 1, and the lensing-step shift
(1+x1)/(1+x2) - 1, which multiply to the lensed shift.
Usage: python3 g1b_stages.py <run 1 g1b_diagnosis.out> <run 2 g1b_diagnosis.out>
"""
import re, sys


def rows(path):
    return {int(m.group(1)): (float(m.group(2)), float(m.group(3))) for m in re.finditer(
        r"^\s*(\d+)\s+([+-]\d\.\d+)(?:  > 2e-3)?\s+\(([+-][\d.]+e[+-]\d+)\)", open(path, encoding="utf-8").read(), re.M)}


r1, r2 = rows(sys.argv[1]), rows(sys.argv[2])
assert sorted(r1) == sorted(r2) == list(range(2, 30))
print(" l   lensed shift   unlensed shift   lensing-step shift   run 2 lensing correction")
for l in range(2, 30):
    (d1, x1), (d2, x2) = r1[l], r2[l]
    lensed = (1 + d2) / (1 + d1) - 1
    unlensed = (1 + d2) * (1 + x2) / ((1 + d1) * (1 + x1)) - 1
    step = (1 + x1) / (1 + x2) - 1
    print(f"{l:2d}   {lensed:+.5f}       {unlensed:+.5f}         {step:+.5f}             {x2:+.1e}")
