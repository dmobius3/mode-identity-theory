"""Read-only. The maintainer's table of 2026-10-30, section 3, from the stored summaries: around each set the wider band
fails on, the smallest window holding equal counts of Krein-positive imaginary eigenvalues at N = 24 and 32, the
bottleneck change between them (sorted pairing, in one dimension), and the nearest Krein-negative group."""
import json, os, sys
BENCH, OUT = sys.argv[1:3]; sys.path.insert(0, BENCH)
from instrument import convergence as cv
CASES = [('C2a/R5 at 2', OUT, 'C2a_R5', 2, 7.9787), ('T4/R4 at 4', None, 'T4_R4', 4, 7.8894), ('T1/R5 at 32', None, 'T1_R5', 32, 7.3529),
         ('T1/R4 at 64', None, 'T1_R4', 64, 6.8869), ('T4/R4 at 64', None, 'T4_R4', 64, 6.4607), ('T4/R4 at 64', None, 'T4_R4', 64, 8.0960)]
def imag(s, sign):
    out = []
    for g in s['groups']:
        if g['cls'] != 'imag': continue
        z = cv._c(g).imag
        neg = g['neg']
        if sign == '+' and neg == 0: out += [z] * g['size']
        if sign == '-' and neg > 0: out += [z] * g['size']
    return sorted(out)
for label, out, name, e, z0 in CASES:
    path = os.path.join(out or os.path.join(BENCH, 'run', 'out'), f'{name}.json')
    r = json.load(open(path, encoding='utf-8'))
    k = [x for x in r['cutoffs']['32']['points'] if abs(float(x) - e) < 1e-6][0]
    a, b = imag(r['cutoffs']['24']['points'][k]['summary'], '+'), imag(r['cutoffs']['32']['points'][k]['summary'], '+')
    best = None
    for w in sorted({abs(x - z0) for x in a + b}):
        wa = [x for x in a if abs(x - z0) <= w * (1 + 1e-12)]; wb = [x for x in b if abs(x - z0) <= w * (1 + 1e-12)]
        if wa and len(wa) == len(wb) and len(wa) >= 2:
            best = (len(wa), max(abs(x - y) for x, y in zip(wa, wb)), wb[0], wb[-1]); break
    neg = imag(r['cutoffs']['32']['points'][k]['summary'], '-')
    near = min((abs(z0 - x) for x in neg), default=None)
    print(f"{label} near {z0:.3f}i: members {best[0]}, window {best[2]:.3f}i to {best[3]:.3f}i, bottleneck 24 to 32 {best[1]:.2e}; nearest Krein-negative {'none' if near is None else f'{near:.2f} away'}")
