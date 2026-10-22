#!/usr/bin/env python3
"""The record regression (DRIVER_PLAN.md v2, The development runs in this step, 2). Case: synthetic.

Usage: score_record.py MIT_REPO

M8.16.1's checks read M8.16's recorded outputs, with no solve. The outputs of C1, C2a, C2b, C3, C2a/R5 and P5 are read
from MIT_REPO's history at the record's commit, 87fc643, each against the SHA-256 its RUNLOG.json records. Each case is
scored as the driver scores it (driver.checks_of), with M8.16.1's own serialized case, whose M8.16 fields must equal
those the record carries; the pyramid's next-order values come from the pinned values file. It computes no verdict,
which only the registered run gives, and claims nothing new: these are the terms' known outcomes, read by the code
that will score the run. A mismatch is a code defect against the frozen text, logged with its fix; it moves none of
the bar's constants (UB).

Claims, derived before the run from the terms' Known outcomes and DEVLOG.md entry 8:
  1. Every output equals the SHA-256 its RUNLOG.json records; as recorded, M8.16's K3 read 'instrument failure: the
     diagnosis is untested' and its K4 failed, on its leading-order bar.
  2. M8.16.1's serialized cases equal the recorded cases on every M8.16 field.
  3. The controls' K1 and K4, K2 at C2a and C2b, and C2a/R5's K1 and K4 pass, as recorded.
  4. At the pyramid, K1 and K2 pass.
  5. The bar's c2 and c3 at the pyramid, over kappa s_g, equal the record values the landed next_order_check.py
     prints (its claim F), for the quartet and the Krein-positive pair at N = 16, 24 and 32, to the digits printed.
  6. The bar passes on both groups at every cutoff, under check 1 as the terms write it and as K3(a) reads it.
  7. Check 2 passes at every cutoff, each group's margin, log10 of a tenth of the ceiling over E_c, equal to entry 8's
     to the 0.1 decade it prints.
  8. K3 reads 'resolved', with (a) at every cutoff, and K4 passes.
"""
import hashlib
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402

REPO = sys.argv[1]
RECORD = '87fc643'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
LANDED = 'files/framework/files/working/files/scripts/soft-slot-branches/next-order/next_order_check.out'
ENTRY8 = os.path.join(ROOT, 'dev', 'pyramid_check2_from_record.out')
NAMES = ('C1', 'C2a', 'C2b', 'C3', 'C2a/R5', 'P5')
out, failed = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def claim(n, ok, line):
    say(f"{n}. {'PASS' if ok else 'FAIL'}: {line}")
    if not ok:
        failed.append(n)


def show(rev, path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{rev}:{path}'], check=True, capture_output=True).stdout


def printed(s):
    """A complex or real value as the landed check prints it, with each component's half unit in its last digit."""
    s = s.strip().strip('()')
    m = re.fullmatch(r'([-+]?[0-9.]+(?:e[-+]?\d+)?)(?:\s*([-+])\s*([0-9.]+(?:e[-+]?\d+)?)j)?', s)
    parts = [m[1]] + ([m[2] + m[3]] if m[2] else [])

    def half(x):
        mant, _, exp = x.lstrip('+-').partition('e')
        dec = len(mant.split('.')[1]) if '.' in mant else 0
        return 0.5 * 10 ** (-dec + (int(exp) if exp else 0))
    vals = [float(x) for x in parts]
    return complex(vals[0], vals[1] if len(vals) > 1 else 0.0), (half(parts[0]), half(parts[1]) if len(parts) > 1 else 0.0)


def main():
    devtools.require('synthetic')
    say("The record regression: M8.16.1's checks on M8.16's recorded outputs (DRIVER_PLAN.md v2); nothing solved.")
    say(f'   the record: MIT {RECORD}; the values file: {devtools.sha256(cs.VALUES_FILE)}')
    log = json.loads(show(RECORD, f'{M816}/run/out/RUNLOG.json'))
    files = {f: h for r in log['completed'].values() for f, h in r['files'].items()}
    raw = {f: show(RECORD, f'{M816}/run/out/{f}') for f in files}
    bad = [f for f, h in files.items() if hashlib.sha256(raw[f]).hexdigest() != h]
    rec = {n: json.loads(raw[n.replace('/', '_') + '.json']) for n in NAMES}
    k3_was, k4_was = rec['P5']['checks']['K3']['outcome'], rec['P5']['checks']['K4']
    claim(1, not bad and len(files) == 7 and k3_was == 'instrument failure: the diagnosis is untested' and k4_was is False,
          f'{len(files)} outputs, {len(bad)} differing from RUNLOG.json; as recorded, K3 {k3_was!r}, K4 {k4_was}')

    cases, diffs = {}, []
    for n in NAMES:
        mine = json.loads(json.dumps(dr.jsonable(cs.serialize(n, cs.CASES[n]))))
        theirs = rec[n]['case']
        diffs += [f'{n}.{k}' for k in theirs if mine.get(k) != theirs[k]]
        cases[n] = mine
    claim(2, not diffs, f'the serialized cases against the recorded ones: {diffs or "equal on every M8.16 field"}')

    chk = {n: dr.checks_of(n, cases[n], rec[n], None, False) for n in NAMES}
    ctrl = (all(chk[n]['K1'] and chk[n]['K4'] for n in ('C1', 'C2a', 'C2b', 'C3', 'C2a/R5'))
            and chk['C2a']['K2'] and chk['C2b']['K2'])
    claim(3, ctrl, 'controls: ' + '; '.join(f"{n} {', '.join(k for k in ('K1', 'K2', 'K4') if chk[n].get(k))}"
                                            for n in ('C1', 'C2a', 'C2b', 'C3', 'C2a/R5')))
    p = chk['P5']
    claim(4, p['K1'] and p['K2'], f"the pyramid: K1 {p['K1']}, K2 {p['K2']}")

    landed = show('deec830', LANDED).decode('utf-8')
    rows = {(int(N), int(g)): (c3, c2) for N, g, c3, c2 in re.findall(
        r'^\s+P5\s+N = (\d+), group (\d+) \([^)]*\): c_g/\(kappa s\) = [^;]*; record c3 (\([^)]*\)|\S+), c2 (\([^)]*\)|\S+);',
        landed, re.M)}
    full, k3a = p['next_order'], p['K3']['next_order']
    ok5, lines5 = len(rows) == 9, []
    for gi, r in full.items():
        for N, x in r['per_N'].items():
            ks = ck._c(cases['P5']['next_order'][N][gi]['kappa_s'])
            for name, mine_ in (('c3', x['c3hat']), ('c2', x['c2hat'])):
                want, (hr, hi) = printed(rows[(int(N), gi + 1)][0 if name == 'c3' else 1])
                got = mine_ / ks
                hit = abs(got.real - want.real) <= hr and abs(got.imag - want.imag) <= hi
                ok5 &= hit
                lines5.append(f'      N = {N}, group {gi + 1}, {name}: {got.real:+.10g} {got.imag:+.6e}j against'
                              f' {rows[(int(N), gi + 1)][0 if name == "c3" else 1]}: {"ok" if hit else "DIFFERS"}')
    claim(5, ok5 and len(lines5) == 12, f'c2 and c3 against the landed check\'s printed record values: {len(lines5)} compared')
    for line in lines5:
        say(line)

    both = {f: {gi: r['reading'] for gi, r in rd.items()} for f, rd in (('full', full), ('k3a', k3a))}
    claim(6, all(v == 'pass' for d in both.values() for v in d.values()) and all(len(d) == 2 for d in both.values()),
          f'the bar, by group index: as the terms write check 1 {both["full"]}; as K3(a) reads it {both["k3a"]}')

    e8 = {(N, cls): float(d) for N, cls, d in re.findall(r'^N = (\d+) (\w+)\s*:.*?, ([0-9.]+) decades', open(
        ENTRY8, encoding='utf-8').read(), re.M)}
    ok7, lines7 = True, []
    for gi, r in full.items():
        cls = cases['P5']['next_order']['24'][gi]['cls']
        for N, x in r['per_N'].items():
            dec = math.log10(ck.RESOLUTION * x['ceiling'] / x['E_c']) if x['c2'] and x['E_c'] else None
            hit = dec is not None and round(dec, 1) == e8.get((N, cls))
            ok7 &= hit
            lines7.append(f'      N = {N} {cls}: E_c {x["E_c"]:.2e}, {dec:.2f} decades, entry 8 {e8.get((N, cls))}:'
                          f' {"ok" if hit else "DIFFERS"}')
    claim(7, ok7 and len(lines7) == 6 and len(e8) == 6, 'check 2, by exact index association, against entry 8')
    for line in lines7:
        say(line)

    a = {N: v['a'] for N, v in p['K3']['per_N'].items()}
    claim(8, p['K3']['outcome'] == 'resolved' and all(a.values()) and p['K4'],
          f"K3 {p['K3']['outcome']!r}, (a) {a}; K4 {p['K4']}")
    say(f'{len(failed)} of 8 claims failed' + (f': {failed}' if failed else '') + '; no verdict is computed')
    with open(os.path.join(HERE, 'score_record.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
