#!/usr/bin/env python3
"""The comparison data for the quartet's next-order term, extracted from M8.16's record before any derivation.

Usage: python3 -I -B extract_comparison.py RECORD_FOLDER OUT_JSON
  RECORD_FOLDER: M8.16's instrument folder as published on MIT (scripts/soft-slot-dynamics-m8-16/), whose run/out/
                 holds the registered run's case files.
  OUT_JSON:      the file to write. A Markdown summary is printed.

It checks each case file against the SHA-256 the run's log recorded, then, for the four soft-slot controls and the
pyramid, at every cutoff and every registered point, reads each slow group that the pinned checks.leading matches to
Theorem R's leading order: the class and Krein sign, the computed eigenvalue (the record's group centre, complex), the
leading-order prediction eps kappa s tau at the nominal eps, and the eps the point reached. It refuses unless the slow
band holds every predicted mode, with multiplicity, whatever the deviations. It also writes each case's
lambda0, Q, kappa, slot factor s and frozen spectrum. Nothing is fitted, and nothing is derived here."""
import hashlib
import json
import math
import os
import sys

ROOT, OUT = sys.argv[1:3]
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import checks as ck  # noqa: E402

CASES = ('C2a', 'C2b', 'C3', 'C2a/R5', 'P5')
OUTDIR = os.path.join(ROOT, 'run', 'out')


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    with open(os.path.join(OUTDIR, 'RUNLOG.json'), encoding='utf-8') as f:
        log = json.load(f)
    data = dict(source=dict(runlog_sha256=sha(os.path.join(OUTDIR, 'RUNLOG.json')), files={}), cases={})
    for name in CASES:
        fname = name.replace('/', '_') + '.json'
        path = os.path.join(OUTDIR, fname)
        h = sha(path)
        if log['completed'][name]['files'][fname] != h:
            raise SystemExit(f'{fname} differs from the SHA-256 the run log recorded')
        data['source']['files'][fname] = h
        with open(path, encoding='utf-8') as f:
            out = json.load(f)
        case = out['case']
        lam0, Q, s = case['lam0'], ck.num(case['Q']), ck.num(case['s'])
        kappa = 1 / (8 * math.sqrt(lam0) * Q)
        rec = dict(slot=case['slot'], lam0=lam0, Q=Q, Q_frac=case['Q'].get('frac'), kappa=kappa, s=s,
                   spectrum=case['spectrum'], points={})
        for N, cut in sorted(out['cutoffs'].items(), key=lambda kv: int(kv[0])):
            for e in (0.25, 0.5, 1.0, 2.0):
                p = cut['points'].get(ck.key(e))
                if not p or 'record' not in p:
                    continue
                ok, worst, rows = ck.leading(p, case, e)
                pred = ck.predicted(case, e)
                counts_ok = ck.match(pred, ck.computed(p, ck.slow_band(case, e)))[0]
                if not counts_ok or len(rows) != len(pred):
                    raise SystemExit(f'{name} at N = {N}, eps = {e:g}: the slow band does not hold every predicted mode, '
                                     'with multiplicity')
                rec['points'][f'N{N}_eps{e:g}'] = dict(
                    N=int(N), eps=e, eps_reached=p['eps_reached'], within_bar=ok,
                    groups=[dict(cls=c, sign=sg, predicted=[complex(pr).real, complex(pr).imag],
                                 computed=[complex(cm).real, complex(cm).imag], deviation=d)
                            for c, sg, pr, cm, d in rows])
        data['cases'][name] = rec
    text = json.dumps(data, indent=1)
    with open(OUT, 'x', encoding='utf-8') as f:
        f.write(text + '\n')
    print(f'# The comparison data, from M8.16\'s record\n\n`{os.path.basename(OUT)}`: SHA-256 `{sha(OUT)}`. '
          f'The run log: `{data["source"]["runlog_sha256"]}`.\n')
    print('| case | slot | kappa | s | slow groups at N = 32, eps = 0.25: class, sign, deviation |')
    print('| --- | --- | --- | --- | --- |')
    for name, rec in data['cases'].items():
        g = rec['points'].get('N32_eps0.25', {}).get('groups', [])
        cells = '; '.join(f"{x['cls']} {x['sign'] if x['sign'] is not None else ''} {100 * x['deviation']:.2f}%".replace('  ', ' ')
                          for x in g)
        print(f"| {name} | {rec['slot']} | {rec['kappa']:.6f} | {rec['s']:g} | {cells} |")


if __name__ == '__main__':
    main()
