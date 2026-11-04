#!/usr/bin/env python3
"""What candidate A cannot see, on stored readings: nothing is solved or read. test_regression.py's closing pair keeps both
gaps above tau(40), so A's blur leaves it alone. Here P5 at 0.25 from M8.18's record keeps the group of two at N = 40 and
takes other gaps at N = 24 and 32, each about the pair's stored centre, and the rule reads each as built and under A.

A's blur links a pair at a lower cutoff wherever its gap is inside tau(40), so a pair inside tau(40) at N = 24 and 32 is
read by its centre alone at every cutoff, and a gap that closes there is not seen. Above tau(40) at N = 24 alone, the
members' change falls to zero at N = 32 under A, and the rule reads that as contracting. Each line prints both verdicts.

Usage: closing_within_tau.py SCRIPTS_DIR
"""
import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import test_regression as tr  # noqa: E402

GAPS = ((1.1345e-5, 1.1345e-5, 'as stored: does not move'), (1.15e-5, 1.0e-5, 'closing, inside tau(40) at both'),
        (1.2e-5, 1.0e-5, 'closing, inside tau(40) at both'), (1.25e-5, 1.0e-5, 'closing, above tau(40) at N = 24 alone'),
        (1.25e-5, 1.25e-5, 'stable, above tau(40) at both'), (3e-5, 1.0e-5, 'closing, above tau(40) at N = 24 alone'))


def main():
    records = tr.load(sys.argv[1])
    label, name, e, sums, eig, lam, marg, rd = tr.p5(records)
    hi = sums[-1]
    tau = [tr.cv.ln.KAPPA_D * (tr.cv.U * s['normA'] * 4.02029) ** 0.5 for s in sums]
    print(f'P5 at 0.25, the pair near 4.02029: tau at N = 24, 32, 40: {tau[0]:.4e}, {tau[1]:.4e}, {tau[2]:.4e}')
    for g24, g32, what in GAPS:
        s2 = copy.deepcopy(sums)
        for lev, gap in ((0, g24), (1, g32)):
            g = sorted((x for x in s2[lev]['groups'] if abs(complex(*x['c']).imag - 4.02029) < 1e-5), key=lambda x: x['c'][1])
            mid = (g[0]['c'][1] + g[1]['c'][1]) / 2
            g[0]['c'][1], g[1]['c'][1] = mid - gap / 2, mid + gap / 2
        built = tr.ck.reading(s2, eig, lam, marg, tr.N_LO)['verdict']
        under = tr.changed.reading(s2, [True] * 3, eig, lam, marg, tr.N_LO)['verdict']
        print(f'gaps {g24:.4e}, {g32:.4e}, one group at N = 40 ({what}): as built {built}; under A {under}')
    assert hi is sums[-1]


if __name__ == '__main__':
    main()
