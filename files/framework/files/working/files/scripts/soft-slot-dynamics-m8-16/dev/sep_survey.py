#!/usr/bin/env python3
"""The separation survey: DESIGN.md section 10.2's separation rule, its record-only terms, on the controls' shipped
records. An analysis of records, not a run: it solves nothing and builds no operator. It informs SEPARATION_PLAN.md.

The points: D7's sample (C2a, C2b, C3 at eps in {0.5, 1, 2}; N = 16, 24, 32 from d7_*_N16_24_32.json, DEVLOG 69 to 71, and
N = 40 from d7_*_N40.json, 75 to 77) and D7's ladders (N = 24 and 32 at every eps, and N = 40 at each ladder's top three,
d7_ladders_*.json, 103 to 105). The sample's N = 16 to 40 records predate the GEMM fix (entry 94), at about 1e-13 in the
eigenvalues; the ladders follow it. All predate section 7's recalibration, so each point's margin is recomputed at that
calibration, 2 sqrt(u ||A|| max(m, 0.2)), from its ||A|| (the sample's normA; for the ladders, from the margin they
recorded, 30 sqrt(u ||A||)) and its m. The eigenvalues do not depend on the calibration.

The slow band: the sample's own (the record's typed eigenvalues below 1: the positive imaginary parts for C2a and C2b,
the positive reals for C3); the ladders' M8.15-tracked slow eigenvalues, matched (compare.slow, per unit eps, times eps).
For each slow eigenvalue at the highest N: its last change d2 (the two highest N), and with three cutoffs d1 before it;
the remaining error, d2^2 / (d1 - d2) where d2 < d1, else non-contracting, and d2 with two cutoffs; the floor, the larger
margin of the two highest N; its distance to the nearest type-changing event: the top of A's gray zone, 3 margins, at the
highest N; the imaginary axis for C3's real ones; and the nearest imaginary eigenvalue of opposite Krein sign for C2a's
and C2b's, which the records show do not exist (checked below). The ratio is the distance over max(remaining, floor).
Not in the records, so not read: eigenvalue residuals and sensitivities (DEVLOG 113's limitation 7), and the next
level's near-zero modes at the ladders' tops (its limitation 2).
"""
import json
import os
import re
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
U = np.finfo(float).eps
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def margin(normA, m):
    return 2 * np.sqrt(U * normA * max(m, 0.2))


def load():
    pts, krein_neg = [], 0
    for c in ('C2a', 'C2b', 'C3'):
        sample = {}
        for f in (f'd7_{c}_N16_24_32.json', f'd7_{c}_N40.json'):
            for k, v in json.load(open(os.path.join(HERE, f), encoding='utf-8')).items():
                mm = re.match(r'N(\d+)_eps([\d.]+)$', k)
                if mm and isinstance(v, dict) and 'slow' in v:
                    krein_neg += sum(g[2] for g in v.get('slow_groups', []))
                    sample.setdefault(float(mm.group(2)), {})[int(mm.group(1))] = (np.array(v['slow']), margin(v['normA'], v['m']))
        for e, dd in sorted(sample.items()):
            pts.append(('sample', c, e, dd))
        ladder = {}
        for k, v in json.load(open(os.path.join(HERE, f'd7_ladders_{c}.json'), encoding='utf-8')).items():
            mm = re.match(r'N(\d+)_eps([\d.]+)$', k)
            if mm and v.get('ok') and v['compare']['slow'] is not None:
                krein_neg += len(v['record']['krein'])
                nA = (v['record']['margin'] / 30) ** 2 / U
                ladder.setdefault(float(mm.group(2)), {})[int(mm.group(1))] = (np.array(v['compare']['slow']) * v['eps'],
                                                                               margin(nA, v['m']))
        for e, dd in sorted(ladder.items()):
            pts.append(('ladders', c, e, dd))
    return pts, krein_neg


def main():
    pts, krein_neg = load()
    say("The separation survey (an analysis of records): section 10.2's record-only terms at section 7's calibration.")
    say(f"Krein-negative imaginary groups in C2a's and C2b's records, and among the sample's slow groups: {krein_neg}.")
    rows = []
    for src, c, e, dd in pts:
        Ns = sorted(dd)
        lh, mh = dd[Ns[-1]]
        ll, ml = dd[Ns[-2]]
        assert len(lh) == len(ll)
        d2 = np.abs(lh - ll)
        if len(Ns) >= 3:
            d1 = np.abs(ll - dd[Ns[-3]][0])
            rem = np.where(d2 < d1, d2 * d2 / np.maximum(d1 - d2, 1e-300), np.inf)
        else:
            rem = d2
        floor = max(mh, ml)
        dist = np.abs(lh) - 3 * mh                    # the gray zone's top; C3's axis, |lam|, is farther
        ratio = dist / np.maximum(rem, floor)
        j = int(np.argmin(ratio))
        binds = 'non-contracting' if not np.isfinite(rem[j]) else ('the floor' if floor >= rem[j] else 'the change')
        rows.append((float(ratio[j]), src, c, e, Ns, float(lh[j]), float(rem[j]), floor, binds))
        say(f"{src:7s} {c:3s} eps {e:8.4g} N {Ns}: slowest-ratio eigenvalue {lh[j]:.4e}; remaining {rem[j]:.2e}, floor"
            f" {floor:.2e} ({binds}); ratio {ratio[j]:.3g}")
    say()
    for src in ('sample', 'ladders'):
        rr = [x for x in rows if x[1] == src]
        w = min(rr)
        ch = [x for x in rr if x[8] == 'the change']
        say(f"{src}: {len(rr)} points; the smallest ratio {w[0]:.3g} ({w[2]}, eps {w[3]:g}, N {w[4]}, {w[8]}); the change binds"
            f" at {len(ch)}, smallest {min(ch)[0]:.3g} ({min(ch)[2]}, eps {min(ch)[3]:g})" if ch else
            f"{src}: {len(rr)} points; the smallest ratio {w[0]:.3g} ({w[2]}, eps {w[3]:g}, N {w[4]}, {w[8]}); the floor binds at all")
    say(f"All {len(rows)} points: below 10, {sum(x[0] < 10 for x in rows)}; non-contracting, {sum(x[8] == 'non-contracting' for x in rows)};"
        f" the smallest ratio {min(rows)[0]:.3g}.")
    with open(os.path.join(HERE, 'sep_survey.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
