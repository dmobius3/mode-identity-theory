#!/usr/bin/env python3
"""The section 7 recalibration's evidence: the controls' zero clusters, gaps and symmetry leaks at every recorded point
(D6's C1, D7's sample and D7's ladders), and the proposed margin, gray zone and leak bound evaluated on them.

An analysis of the shipped records (dev/*.json), not a run: it solves nothing and builds no operator. It is logged in
DEVLOG.md by its hash and its output's, with RECAL_PLAN.md.

The record today (instrument/linear.py; the drivers' point_record): margin = 30 sqrt(u ||A||), one margin for the zero
cluster, the grouping and the typing; gray zone (margin/10, 10 margin); V0's symmetry leak at most 1e-8.
The proposal (RECAL_PLAN.md): margin = KAPPA sqrt(u ||A|| max(m, M_MIN)), m = ||phi||^2, gray zone (margin/G, G margin),
and the leak at most KAPPA_L u ||A|| / gap, gap the smallest |lambda| outside the cluster.
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
U = np.finfo(float).eps
KAPPA, G, M_MIN, KAPPA_L, TARGET = 2.0, 3.0, 0.2, 200.0, 1.04e-5
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def load():
    pts = []

    def add(src, c, N, eps, m, rec, steps=None):
        mg = rec['margin']
        nA = rec.get('normA') or (mg / 30) ** 2 / U          # the margin was 30 sqrt(u ||A||) at every recorded point
        pts.append(dict(src=src, c=c, N=N, eps=eps, m=m, normA=nA, margin=mg, cl=rec['cluster_max'],
                        gap=rec['outside_min'], leak=rec['leak'], floor=steps[-1]['floor'] if steps else None))

    for k, v in json.load(open(os.path.join(HERE, 'd6_theoremD_N16_24_32_40.json'))).items():
        e = float(k.split('_eps')[1])
        add('D6', 'C1', int(k[1:3]), e, e, v)                 # C1: c = sqrt(eps) v with |v| = 1, so m = eps
    for c in ('C2a', 'C2b', 'C3'):
        for f in (f'd7_{c}_N16_24_32.json', f'd7_{c}_N40.json'):
            for k, v in json.load(open(os.path.join(HERE, f))).items():
                if k.startswith('N') and v.get('ok', True) and 'margin' in v:
                    add('D7 sample', c, int(k[1:3]), v['eps'], v['m'], v, v.get('steps'))
        for k, v in json.load(open(os.path.join(HERE, f'd7_ladders_{c}.json'))).items():
            if k.startswith('N') and v.get('ok'):
                add('D7 ladders', c, int(k[1:3]), v['eps'], v['m'], v['record'], v['steps'])
    return pts


def main():
    pts = load()
    srcs = ('D6', 'D7 sample', 'D7 ladders')
    say(f"{len(pts)} control points: " + ', '.join(f"{s} {sum(p['src'] == s for p in pts)}" for s in srcs))
    a = {k: np.array([p[k] for p in pts], dtype=float) for k in ('normA', 'margin', 'cl', 'gap', 'leak', 'm', 'eps', 'N')}
    root = np.sqrt(U * a['normA'])
    say(f"||A|| {a['normA'].min():.1f} to {a['normA'].max():.1f}; sqrt(u ||A||) {root.min():.2e} to {root.max():.2e};"
        f" m = ||phi||^2 {a['m'].min():.3g} to {a['m'].max():.3g}")
    say()
    say('1. The record today: margin = 30 sqrt(u ||A||), gray zone (margin/10, 10 margin), leak at most 1e-8.')
    say(f"   margin {a['margin'].min():.2e} to {a['margin'].max():.2e}; the cluster's largest eigenvalue {a['cl'].min():.2e} to"
        f" {a['cl'].max():.2e}, {np.min(a['margin'] / a['cl']):.0f} to {np.max(a['margin'] / a['cl']):.0f} times below the margin")
    say(f"   gap (the smallest |lambda| outside the cluster) {a['gap'].min():.2e} to {a['gap'].max():.2e}, at least"
        f" {np.min(a['gap'] / a['margin']):.1f} margins; leak {a['leak'].min():.1e} to {a['leak'].max():.1e}")
    floor_now = 10 * a['margin']
    say(f"   the smallest resolvable slow pair, 10 margins: {floor_now.min():.1e} to {floor_now.max():.1e};"
        f" at N = 40, {floor_now[a['N'] == 40].min():.1e} to {floor_now[a['N'] == 40].max():.1e}. A pair below"
        f" {TARGET:.2e} lies in the gray zone at every point, so it is Unresolved.")
    say()
    say('2. What sets the cluster: its largest eigenvalue against two scales.')
    for name, s in (('sqrt(u ||A||)', root), ('sqrt(u ||A|| m)', np.sqrt(U * a['normA'] * a['m']))):
        r = a['cl'] / s
        say(f"   cluster / {name:16s}: {r.min():.4f} to {r.max():.4f}, a spread of {r.max() / r.min():.0f}x")
    say('   The amplitude-scaled scale holds the cluster within a spread about eight times narrower. Along each ladder the')
    say('   cluster grows about as eps^0.5 to eps^0.7, while sqrt(u ||A||) stays flat:')
    for c in ('C2a', 'C2b', 'C3'):
        for N in (24, 32):
            q = sorted((p['m'], p['cl']) for p in pts if p['src'] == 'D7 ladders' and p['c'] == c and p['N'] == N)
            m_, cl_ = map(np.array, zip(*q))
            say(f"     {c} N = {N}: m {m_[0]:.3g} to {m_[-1]:.3g}, cluster {cl_[0]:.1e} to {cl_[-1]:.1e},"
                f" log-log slope in m {np.polyfit(np.log(m_), np.log(cl_), 1)[0]:.2f}")
    cmax = float(np.max(a['cl'] / np.sqrt(U * a['normA'] * np.maximum(a['m'], M_MIN))))
    say(f"   the largest coefficient, cluster / sqrt(u ||A|| max(m, {M_MIN})): {cmax:.4f}")
    say()
    say(f'3. The proposal: margin = {KAPPA:g} sqrt(u ||A|| max(m, {M_MIN})), gray zone (margin/{G:g}, {G:g} margin),'
        f' leak at most {KAPPA_L:g} u ||A|| / gap.')
    mg = KAPPA * np.sqrt(U * a['normA'] * np.maximum(a['m'], M_MIN))
    below = (mg / G) / a['cl']
    say(f"   KAPPA = {KAPPA:g} is the smallest round value with the cluster at least ten times below the gray zone's lower"
        f" edge at every point: KAPPA / G >= 10 x {cmax:.4f} needs KAPPA >= {10 * G * cmax:.2f}.")
    say(f"   (a) the cluster sits {below.min():.1f} to {below.max():.0f} times below the gray zone, at least ten at"
        f" {int(np.sum(below >= 10))} of {len(pts)} points;")
    out_g = a['gap'] / (G * mg)
    say(f"   (b) every control's spectrum outside the cluster stays outside the gray zone: the gap is {out_g.min():.0f} to"
        f" {out_g.max():.0e} times its upper edge, at least one at {int(np.sum(out_g >= 1))} of {len(pts)} points;")
    lr = a['leak'] / (U * a['normA'] / a['gap'])
    say(f"   (c) the leak is {lr.min():.2f} to {lr.max():.1f} times u ||A|| / gap, so the bound {KAPPA_L:g} holds with at least"
        f" {KAPPA_L / lr.max():.0f}x to spare; KAPPA_L is ten times the largest ratio, rounded up. The fixed 1e-8 would fail"
        f" a gap below {U * a['normA'].max() * lr.max() / 1e-8:.1e} at the controls' largest ratio.")
    say()
    say(f'4. What it buys: the smallest resolvable slow pair, {G:g} margins, against {TARGET:.2e} (M8.15\'s level-3 cluster'
        ' tolerance; DESIGN.md section 7).')
    for N in (24, 32, 40):
        nA = a['normA'][a['N'] == N]
        for tag, v in (('smallest', nA.min()), ('largest', nA.max())):
            m_max = (TARGET / (G * KAPPA)) ** 2 / (U * v)
            say(f"   N = {N}, the {tag} ||A|| ({v:.0f}): {G * KAPPA * np.sqrt(U * v * M_MIN):.1e} at m <= {M_MIN},"
                f" {TARGET:.2e} up to m = {m_max:.1f}, {G * KAPPA * np.sqrt(U * v * 72):.1e} at m = 72,"
                f" {G * KAPPA * np.sqrt(U * v * 132):.1e} at m = 132")
    k10 = 10 * 10 * cmax
    say(f"   With G = 10 the same cluster condition needs KAPPA >= {k10:.1f}, so the floor is 10 KAPPA sqrt(u ||A|| m), and at"
        f" N = 40 a pair at {TARGET:.2e} is resolvable only up to m ="
        f" {(TARGET / (10 * k10)) ** 2 / (U * a['normA'][a['N'] == 40].max()):.3f}, below the ladders' first point.")
    with open(os.path.join(HERE, 'recal_survey.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
