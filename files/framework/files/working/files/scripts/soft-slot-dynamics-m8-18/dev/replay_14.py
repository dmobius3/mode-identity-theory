"""Replay the grouping check's failing() on M8.17's stored summaries at the 14 unclassified points (read-only)."""
import importlib.util, json, os, sys
BENCH = sys.argv[1]
sys.argv = [sys.argv[0], BENCH]
spec = importlib.util.spec_from_file_location('gc', os.path.join(BENCH, 'dev', 'grouping_check.py'))
gc = importlib.util.module_from_spec(spec); spec.loader.exec_module(gc)
cv = gc.cv
PTS = {'T1_R4': (1.41421356237, 32, 45.254834, 64, 72), 'T1_R5': (32,), 'T4_R4': (4, 8, 11.313708499, 64, 72),
       'T5_R2': (45.254834, 128, 132)}
total, n16_short_24_32_agree, other = 0, 0, []
for name, eps in PTS.items():
    r = json.load(open(os.path.join(BENCH, 'run', 'out', f'{name}.json'), encoding='utf-8'))
    for e in eps:
        key = [k for k in r['readings'] if abs(float(k) - e) < 1e-6]
        assert len(key) == 1, (name, e, key); key = key[0]
        sums = [r['cutoffs'][N]['points'][key]['summary'] for N in gc.NS]
        res, rows = gc.failing(sums, r['readings'][key])          # refuses unless the replay matches the record
        struct = [cv._structure(s) for s in sums]
        line = []
        for x in rows:
            if x['kind'] == 'set' and len(set(x['counts'])) > 1:
                total += 1
                c16, c24, c32 = x['counts']
                ok = c16 < c24 == c32
                n16_short_24_32_agree += ok
                if not ok: other.append((name, e, x['counts']))
                line.append(f"set {x['centre'].imag:.4f}i counts {x['counts']}")
            else:
                line.append(f"{x['kind']} {x['centre'].imag:.4f}i {x['why']} counts {x['counts']}")
        sdiff = len(set(struct)) > 1
        odd = [gc.NS[i] for i in range(3) if sdiff and sum(struct[i] == struct[j] for j in range(3)) == 1]
        print(f"{name} {e:g}: " + '; '.join(line) + (f" | structure differs, odd one out at N = {odd}" if sdiff else ''))
print(f"\ncount changes: {total}; with N = 16 short and N = 24, 32 agreeing: {n16_short_24_32_agree}; other: {other}")
