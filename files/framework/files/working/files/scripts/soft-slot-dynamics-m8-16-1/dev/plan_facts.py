#!/usr/bin/env python3
"""The facts DRIVER_PLAN.md v1 states about M8.16's tree, its record and the pinned values, read again from source
(development, off the instrument: nothing is solved, and no sealed seed is constructed).

  python3 -I -B plan_facts.py MIT_REPO VALUES_JSON DEVLOG_MD TERMS_MD

MIT_REPO:    a checkout of mode-identity-theory at deec830; M8.16's folder is read from its working tree, and its
             record's history through git.
VALUES_JSON: step 1's pinned run/next_order_values.json.
DEVLOG_MD:   M8.16.1's DEVLOG.md.
TERMS_MD:    M8.16.1's terms, draft v3.

Facts, each of which must hold, or the exit status is 1:
  1. M8.16's manifest at the checkout has 36 entries and reproduces its pin, run/MANIFEST_PIN; fifteen of them are
     instrument/ and reference/m815/.
  2. M8.16's recorded outputs are unchanged from the record's commit 87fc643 to the checkout, and each equals the
     SHA-256 its RUNLOG.json records.
  3. The recorded pyramid: K3's (a) fails at every cutoff while the seeds and L's certificate hold there at 0.25, and
     (b), (c) and (d) hold, so on the record (a) failed only at its slow-band clause.
  4. Check 1 at the recorded pyramid, at 0.25, 0.5 and 1 and every cutoff: the point accepted, the seed checked, K1,
     converged, K2's matching, and the matching outside the in-span pair's class.
  5. Each values group of M8.16's ten cases ties one to one to a frozen mode of its class, Krein sign and
     multiplicity, within the frozen value's written precision; T5J's exact spectrum equals the file's; every case's
     s is the same at every cutoff.
  6. instrument/branches.py: representative and seed_state raise KeyError for C3R/R4 and T5J/R2, and SEALED lists
     neither (seed_state is given no basis, and fails before reading one).
  7. devtools.log_run numbers a new entry by the count of the log's '## ' lines. M8.16's log begins at entry 0;
     M8.16.1's begins at 1, so its next entry would repeat the last number.
  8. devtools.frozen reads the terms at run/m8_16_task_details.md.
  9. Terms v3's new constants list the ceiling's factors, the tenth and the points, and not check 4's floor factor.
Arms, each of which must turn its fact red:
  A1. Fact 4 with the pyramid's in-span group removed at N = 24, eps = 0.5: K2's matching fails there, while the
      matching outside the in-span pair's class holds (the plan's check 1 at K3(a)).
  A2. Fact 5 with P5's quartet literal moved by two units in the last digit its real part prints with: its tie
      fails.
"""
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys

REPO, VALUES, DEVLOG, TERMS = sys.argv[1:5]
M816 = os.path.join(REPO, 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16')
REL = os.path.relpath(M816, REPO)
sys.path.insert(0, M816)
sys.path.insert(0, os.path.join(M816, 'run'))
from instrument import branches as br, devtools as dt, linear as ln  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402

failed = []


def fact(n, ok, line):
    print(f'{n}. {"PASS" if ok else "FAIL"}: {line}')
    if not ok:
        failed.append(str(n))


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True)


print("DRIVER_PLAN.md v1's facts, read again from source")
print(f"   the checkout: {git('rev-parse', 'HEAD').stdout.strip()}; the values file: {sha(VALUES)}")

# 1. the manifest
text, msha = dt.manifest(M816)
rows = text.splitlines()
pin = open(os.path.join(M816, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
inst = [r.split('  ')[1] for r in rows if r.split('  ')[1].startswith(('instrument/', 'reference/m815/'))]
fact(1, len(rows) == 36 and msha == pin and len(inst) == 15,
     f'M8.16\'s manifest: {len(rows)} entries, SHA-256 {msha}, its pin {pin}; instrument/ and reference/m815/: {len(inst)} files')

# 2. the record
d2 = git('diff', '--name-only', '87fc643', 'HEAD', '--', f'{REL}/run/out')
moved = d2.stdout.split() if d2.returncode == 0 else None
log = json.load(open(os.path.join(M816, 'run', 'out', 'RUNLOG.json'), encoding='utf-8'))
files = {f: h for r in log['completed'].values() for f, h in r['files'].items()}
bad = [f for f, h in files.items() if sha(os.path.join(M816, 'run', 'out', f)) != h]
fact(2, moved == [] and not bad and len(files) == 7,
     ('run/out unchanged since 87fc643: ' + ('not read, since git could not compare: MIT_REPO is not a checkout holding 87fc643'
                                             if moved is None else f'{len(moved)} files moved'))
     + f'; {len(files)} logged outputs, {len(bad)} differing from RUNLOG.json')

# 3. K3 on the recorded pyramid
P = json.load(open(os.path.join(M816, 'run', 'out', 'P5.json'), encoding='utf-8'))
case = P['case']
k3 = P['checks']['K3']
cert = {N: ck.kernel_exact(c['points'][ck.key(0.25)], case) for N, c in P['cutoffs'].items()}
seeds = ck.seeds_ok(P)
parts = {N: {x: v[x] for x in ('a', 'b', 'c', 'd')} for N, v in k3['per_N'].items()}
fact(3, all(not v['a'] and v['b'] and v['c'] and v['d'] for v in parts.values()) and seeds and all(cert.values()),
     f"K3 '{k3['outcome']}': {parts}; the seeds {seeds}; L's certificate at 0.25 {cert}")


def outside(p, eps):
    pred = [x for x in ck.predicted(case, eps) if (x[0], x[1]) != ('imag', -1)]
    comp = [x for x in ck.computed(p, ck.slow_band(case, eps)) if (x[0], x[1]) != ('imag', -1)]
    return ck.match(pred, comp)[0]


def check1(rec):
    out = {}
    for e in (0.25, 0.5, 1.0):
        for N, c in rec['cutoffs'].items():
            p = c['points'][ck.key(e)]
            k2m = ck.match(ck.predicted(case, e), ck.computed(p, ck.slow_band(case, e)))[0]
            out[(N, e)] = dict(accepted=bool(p['accepted']), seed=bool(c['seed']['ok']), k1=ck.k1(p, case),
                               converged=ck.converged(rec, e, case), k2_matching=k2m, outside=outside(p, e))
    return out


# 4. check 1 at the recorded pyramid
c1 = check1(P)
fact(4, all(all(v.values()) for v in c1.values()),
     f'check 1 at the pyramid: {sum(all(v.values()) for v in c1.values())} of {len(c1)} points hold every part, both forms')

# A1. the in-span group removed at one point
Pa = json.loads(json.dumps(P))
pt = Pa['cutoffs']['24']['points'][ck.key(0.5)]
pt['groups'] = [g for g in pt['groups'] if not (g['cls'] == 'imag' and g['status'] == 'definite' and g['neg'] == g['size']
                                                 and abs(complex(*g['c'])) <= ck.slow_band(case, 0.5))]
a1 = check1(Pa)[('24', 0.5)]
fact('A1', not a1['k2_matching'] and a1['outside'],
     f"arm: in-span group removed at N = 24, eps = 0.5: K2's matching {a1['k2_matching']}, outside the in-span class {a1['outside']}")
# 5. the ties
vals = json.load(open(VALUES, encoding='utf-8'))['cases']


def written(t):
    """Half a unit in the last digit a decimal literal is written with; double precision for an exact value."""
    if isinstance(t, (int,)) or type(t).__name__ == 'Fraction':
        return 0.0
    r = repr(float(t))
    if 'e' in r or len(r.replace('-', '').replace('.', '').lstrip('0')) >= 16:
        return 4 * sys.float_info.epsilon * abs(float(t))
    return 0.5 * 10 ** -len(r.split('.')[1])


def tie(name, spectrum, groups):
    fac = float(cs.CASES[name]['s']) if name in cs.CASES else 1.0
    worst = 0.0
    for g in groups:
        sign = {'+': 1, '-': -1, None: None}[g['krein']]
        s = complex(float(g['s'][0]), float(g['s'][1]))
        hits = [m for m in spectrum if m[0] == g['cls'] and m[1] == sign and m[3] == g['mult']]
        if not hits:
            return None
        m = min(hits, key=lambda m: abs(complex(m[2]) * (1j if m[0] == 'imag' else 1) * fac - s))
        t = complex(m[2])
        pred = t * (1j if m[0] == 'imag' else 1) * fac
        tol = (math.hypot(written(t.real), written(t.imag)) if m[0] == 'complex' else written(m[2])) * fac \
            + 4 * sys.float_info.epsilon * abs(s)
        if abs(pred - s) > tol:
            return None
        worst = max(worst, abs(pred - s) / abs(s))
        spectrum = [x for x in spectrum if x is not m]
    return worst if not spectrum else None


rels, ok5 = {}, True
for n in ('P5', 'T1/R4', 'T1/R5', 'T2/R4', 'T2/R5', 'T3/R4', 'T3/R5', 'T4/R4', 'T4/R5', 'T5/R2'):
    r = tie(n, list(cs.CASES[n]['spectrum']), vals[n]['cutoffs']['24']['groups'])
    rels[n] = r
    ok5 &= r is not None
same = all(len({json.dumps([g['s'] for g in c['cutoffs'][N]['groups']]) for N in c['cutoffs']}) == 1 for c in vals.values())
a, b, c = 418161601, 6605190592, 25491013632
d = math.sqrt(b * b - 4 * a * c)
t5j = sorted([math.sqrt(15680 / 1859)] + [math.sqrt(-x) for x in ((-b + d) / (2 * a), (-b - d) / (2 * a))])
f5j = sorted(float(g['s'][1]) for g in vals['T5J/R2']['cutoffs']['24']['groups'])
d5j = max(abs(x - y) / y for x, y in zip(t5j, f5j))
worst = max(rels.values()) if ok5 else None
fact(5, ok5 and same and d5j <= 4 * sys.float_info.epsilon,
     f'ties: every one holds; the largest relative difference {worst:.1e}, at '
     f'{max(rels, key=rels.get) if ok5 else None}; T5J against its exact spectrum {d5j:.1e}; s the same at every cutoff {same}')

# A2. P5's quartet literal moved by two units in the last digit its real part prints with (0.041735286)
sp = [(m[0], m[1], complex(m[2].real + 2e-9, m[2].imag) if m[0] == 'complex' else m[2], m[3]) for m in cs.CASES['P5']['spectrum']]
fact('A2', tie('P5', sp, vals['P5']['cutoffs']['24']['groups']) is None,
     "arm: P5's quartet literal moved by 2e-9 in its real part: its tie fails")

# 6. the instrument's seeds know only M8.16's names
raised = {}
for n in ('C3R/R4', 'T5J/R2'):
    for fn, call in (('representative', lambda n=n: br.representative(n)), ('seed_state', lambda n=n: br.seed_state(n, None))):
        try:
            call()
            raised[(n, fn)] = False
        except KeyError:
            raised[(n, fn)] = True
fact(6, all(raised.values()) and not ({'C3R/R4', 'T5J/R2'} & set(br.SEALED)),
     f'KeyError from branches: {raised}; in SEALED: {sorted({"C3R/R4", "T5J/R2"} & set(br.SEALED))}')

# 7. log_run's numbering
src = open(os.path.join(M816, 'instrument', 'devtools.py'), encoding='utf-8').read()
rule = "n = sum(1 for line in f if line.startswith('## '))" in src and "f'\\n## {n}. {ts}" in src
mine = [line for line in open(DEVLOG, encoding='utf-8') if line.startswith('## ')]
nums = [int(re.match(r'## (\d+)\.', x)[1]) for x in mine]
first816 = next(int(re.match(r'## (\d+)\.', x)[1]) for x in open(os.path.join(M816, 'DEVLOG.md'), encoding='utf-8')
                if x.startswith('## '))
fact(7, rule and first816 == 0 and nums[0] == 1 and len(mine) == nums[-1],
     f"log_run numbers by the count of '## ' lines: {rule}; M8.16's log begins at {first816}; M8.16.1's has {len(mine)}"
     f' such lines, its last entry {nums[-1]}, so log_run would write entry {len(mine)} again')

# 8. the terms' name in frozen()
fact(8, "os.path.join(root, 'run', 'm8_16_task_details.md')" in src,
     "devtools.frozen reads run/m8_16_task_details.md")

# 9. terms v3's new constants
t = open(TERMS, encoding='utf-8').read()
block = t[t.index('**New constants:**'):t.index('**Unchanged:**')]
items = [x[2:].strip() for x in block.splitlines() if x.startswith('- ')]
fact(9, len(items) == 3 and 'floor' not in block and '0.1 and 10⁻³' in items[0],
     f'terms v3\'s new constants: {items}; check 4\'s floor factor listed: {"floor" in block}')

print('ALL FACTS HOLD; every arm red' if not failed else 'FAILED: ' + ', '.join(failed))
sys.exit(1 if failed else 0)
