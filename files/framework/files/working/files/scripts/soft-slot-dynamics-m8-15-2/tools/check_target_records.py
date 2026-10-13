"""M8.15.2's two target records, checked after the run (the terms, § THE FREEZE, THE GUARD AND THE RUN, item 4, and the
maintainer's approval of openwave-labs/openwave#630): their custody, the ladder's regression against M8.15, and the
point records' regression against M8.15.1's target records at MIT b13e0f4.

  python3 check_target_records.py      prints the outcome and writes check_target_records.out; exit status 1 on any failure

Custody, for each target record, out/t1_T2_R4.json and out/t1_T3_R5.json:
  - its terms' SHA-256 is the guard's, and the hash stands in MIT's soft-slot-branches.md (the § VI note of 9eab674);
  - its locator SHA-256s are this folder's manifest's, the files' and the guard's; its instrument manifest SHA-256 is the
    file's, this folder's manifest's and the guard's; its extracted decide's SHA-256 is the manifest's;
  - its frozen block is freeze_numbers.json's values, with s2 for its slot.
And once: the guard carries freeze_numbers.json's values unchanged, frozen true and the go; the instrument's FROZEN.json,
which a target run reads, is the file pinned in M8.15.1's RECORD.md; out/ holds no crash record.

The ladder against M8.15: each record's own comparison ran (compared true) and found no difference. A comparison that did
not run is a failure, not a pass.

The point records against M8.15.1 (M8.15.1's two records here equal to their files at b13e0f4): every ladder point
M8.15.1 evaluated up to this run's last target, and every point of M8.15.1's primary bracket at each level, is evaluated
here at the same eps and equals M8.15.1's record value for value. A bracket's points are recorded by eps, not in the order
evaluated, so the order itself is not checked. Any difference is reported, and changes no name.

Then the mutation arms, each on a copy of what was read, each of which must fail its own check. The parent must pass
before the arms run."""
import os, sys, json, re, copy, math, hashlib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
LOC = os.path.dirname(HERE)
S = os.path.dirname(LOC)
OLD = os.path.join(S, 'soft-slot-dynamics-m8-15x-target1')
SOL = os.path.join(S, 'soft-slot-dynamics-m8-15x', 'm8_15x_solver')
PAGE = os.path.join(os.path.dirname(S), 'soft-slot-branches.md')
OLD_COMMIT = 'b13e0f4'
GO = 'https://github.com/openwave-labs/openwave/pull/630#issuecomment-6147458225'
TARGETS = [('T2', 4), ('T3', 5)]

sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()


def blob(folder, rel, commit):
    prefix = subprocess.check_output(['git', '-C', folder, 'rev-parse', '--show-prefix'], text=True).strip()
    return subprocess.check_output(['git', '-C', folder, 'show', f'{commit}:{prefix}{rel}'])


def load():
    D = dict(new={}, old={}, old_committed={})
    for case, slot in TARGETS:
        tag = f'{case}_R{slot}'
        D['new'][tag] = json.load(open(os.path.join(LOC, 'out', f't1_{tag}.json')))
        p = os.path.join(OLD, 'out', f't1_{tag}.json')
        D['old'][tag] = json.load(open(p))
        D['old_committed'][tag] = open(p, 'rb').read() == blob(OLD, f'out/t1_{tag}.json', OLD_COMMIT)
    D['guard'] = json.load(open(os.path.join(LOC, 'out', 'FROZEN.json')))
    D['fn'] = json.load(open(os.path.join(SOL, 'out', 'freeze_numbers.json')))
    D['man'] = json.load(open(os.path.join(LOC, 'MANIFEST.json')))
    D['im_sha'] = sha(os.path.join(SOL, 'out', 'MANIFEST.json'))
    D['code'] = {f: sha(os.path.join(LOC, f)) for f in ('locate.py', 't1_branch.py')}
    D['page'] = open(PAGE).read()
    pin = re.search(r'm8_15x_solver/out/FROZEN\.json` \| `([0-9a-f]{64})`', open(os.path.join(OLD, 'RECORD.md')).read())
    D['ifz_pin'] = pin.group(1) if pin else None
    D['ifz_sha'] = sha(os.path.join(SOL, 'out', 'FROZEN.json'))
    D['crash'] = sorted(f for f in os.listdir(os.path.join(LOC, 'out')) if f.startswith('crash_'))
    return D


def differences(a, b, path='', out=None):
    """Every path at which two JSON values differ, a M8.15.1's and b this run's. Two NaNs agree."""
    out = [] if out is None else out
    if type(a) != type(b):
        out.append(f'{path}: {type(a).__name__} against {type(b).__name__}')
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f'{path}/{k}: only in {"M8.15.1" if k in a else "this run"}')
            else:
                differences(a[k], b[k], f'{path}/{k}', out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(f'{path}: {len(a)} entries against {len(b)}')
        for i, (p, q) in enumerate(zip(a, b)):
            differences(p, q, f'{path}[{i}]', out)
    elif a != b and not (isinstance(a, float) and math.isnan(a) and math.isnan(b)):
        out.append(f'{path}: {a!r} against {b!r}')
    return out


def by_eps(old_pts, new_pts, where):
    """Each of M8.15.1's points matched to this run's at the same eps: (number equal, number read, differences)."""
    new = {p['eps']: p for p in new_pts}
    eq, diffs = 0, []
    for p in old_pts:
        q = new.get(p['eps'])
        if q is None:
            diffs.append(f'{where} eps {p["eps"]!r}: not evaluated in this run')
            continue
        d = differences(p, q, f'{where} eps {p["eps"]:.6g}')
        eq += not d
        diffs += d
    return eq, len(old_pts), diffs


def primary(rec):
    return [b for b in rec['brackets'] if b['label'] == 'primary'][0]


def checks(D):
    """Every check, as (label, ok, details)."""
    res = []
    add = lambda label, ok, details=(): res.append((label, bool(ok), list(details)))
    g, fn, man = D['guard'], D['fn'], D['man']
    add('the guard: every value of freeze_numbers.json unchanged, frozen true, the go on #630',
        all(g.get(k) == v for k, v in fn.items()) and g.get('frozen') is True and g.get('go') == GO)
    add("the instrument's FROZEN.json, which a target run reads: the file pinned in M8.15.1's RECORD.md",
        D['ifz_pin'] is not None and D['ifz_sha'] == D['ifz_pin'])
    add('out/ holds no crash record', not D['crash'], D['crash'])
    for case, slot in TARGETS:
        tag, name = f'{case}_R{slot}', f'{case}/R{slot}'
        r, o = D['new'][tag], D['old'][tag]
        ts = r.get('terms_sha256')
        add(f"{name}: the terms' SHA-256 is the guard's and stands in MIT soft-slot-branches.md",
            ts == g.get('terms_sha256') and isinstance(ts, str) and len(ts) == 64 and D['page'].count(ts) >= 1)
        add(f"{name}: the locator's SHA-256s are the manifest's, the files' and the guard's",
            all(r['locator_sha256'].get(f) == man['sha256'][f] == D['code'][f] == g['locator_sha256'].get(f)
                for f in ('locate.py', 't1_branch.py')))
        add(f"{name}: the instrument manifest's SHA-256 is the file's, the manifest's and the guard's",
            r.get('instrument_manifest_sha256') == D['im_sha'] == man['instrument']['manifest_sha256']
            == g.get('instrument_manifest_sha256'))
        add(f"{name}: the extracted decide's SHA-256 is the manifest's", r.get('decide_sha256') == man['decide_sha256'])
        want = dict(r_f3=fn['r_f']['3'], r_f2=fn['r_f']['2'], delta_lev=fn['delta_lev'], s2=fn['s2'][f'R{slot}'])
        add(f"{name}: the frozen block is freeze_numbers.json's values, with s2 for R{slot}", r.get('frozen') == want,
            [] if r.get('frozen') == want else [f'{r.get("frozen")} against {want}'])
        mc = r.get('m815_comparison') or {}
        add(f'{name}: the ladder against M8.15: the comparison ran and found no difference',
            mc.get('compared') is True and mc.get('differences') == [], [] if mc.get('compared') is True else [str(mc)])
        add(f"{name}: M8.15.1's record here is its file at {OLD_COMMIT}", D['old_committed'][tag])
        last = max(r['targets'])
        n_t = len(r['targets'])
        add(f"{name}: this run's ladder targets are M8.15.1's first {n_t}", o['targets'][:n_t] == r['targets'])
        for key, what in (('points', 'level 3'), ('level2', 'level 2'), ('types', 'types'), ('cross', 'cross-level checks')):
            olds = [p for p in o[key] if p['eps'] <= last]
            eq, n, d = by_eps(olds, r[key], f'ladder {what}')
            add(f"{name}: the ladder's {what}: {eq} of M8.15.1's {n} entries to {last:.4g}, equal value for value",
                eq == n and not d, d[:20] + ([f'... {len(d) - 20} more'] if len(d) > 20 else []))
        bo, bn = primary(o), primary(r)
        for lv in ('3', '2'):
            eq, n, d = by_eps(bo['points'][lv], bn['points'][lv], f'primary L{lv}')
            add(f"{name}: the primary bracket, level {lv}: {eq} of M8.15.1's {n} points evaluated here, equal value for value"
                f" (this run evaluated {len(bn['points'][lv])})",
                eq == n and not d, d[:20] + ([f'... {len(d) - 20} more'] if len(d) > 20 else []))
    return res


def report(res):
    lines = []
    for label, ok, details in res:
        lines.append(f'  {"PASS" if ok else "FAIL"}  {label}')
        lines += [f'          {x}' for x in details]
    return lines


def arms(D):
    """(name, the check it must fail, the edit), each applied to a copy of what was read."""
    def bracket_value(E):
        p = primary(E['new']['T3_R5'])['points']['3']
        old = {q['eps'] for q in primary(E['old']['T3_R5'])['points']['3']}
        q = [x for x in p if x['eps'] in old][5]
        q['near_zero'][0] += 1e-12

    def bracket_missing(E):
        b = primary(E['new']['T2_R4'])
        old = {q['eps'] for q in primary(E['old']['T2_R4'])['points']['2']}
        b['points']['2'] = [x for x in b['points']['2'] if x['eps'] != sorted(old)[1]]

    def ladder_value(E):
        E['new']['T2_R4']['points'][3]['m'] += 1e-12

    def not_compared(E):
        E['new']['T2_R4']['m815_comparison'] = dict(compared=False, differences=[])

    def other_s2(E):
        E['new']['T3_R5']['frozen']['s2'] = E['fn']['s2']['R4']

    def terms(E):
        E['new']['T2_R4']['terms_sha256'] = E['new']['T2_R4']['terms_sha256'][::-1]

    def go(E):
        E['guard']['go'] = GO.replace('630', '624')

    return [
        ("a value in one of M8.15.1's primary points, as this run gives it, off by 1e-12", 'T3/R5: the primary bracket, level 3', bracket_value),
        ("one of M8.15.1's primary points not evaluated in this run", 'T2/R4: the primary bracket, level 2', bracket_missing),
        ("a ladder point's m off by 1e-12", "T2/R4: the ladder's level 3", ladder_value),
        ('the ladder comparison against M8.15 recorded as not run', 'T2/R4: the ladder against M8.15', not_compared),
        ("T3/R5's frozen block with R4's s2", 'T3/R5: the frozen block', other_s2),
        ("T2/R4's terms hash reversed", "T2/R4: the terms' SHA-256", terms),
        ("the guard's go on another pull request", 'the guard:', go),
    ]


def main():
    D = load()
    res = checks(D)
    lines = ['check_target_records.py: M8.15.2\'s target records, after the run'] + report(res)
    parent = all(ok for _, ok, _ in res)
    lines.append(f'the parent: {"ALL PASS" if parent else "FAILED"}')
    caught = []
    if parent:
        for name, target, edit in arms(D):
            E = copy.deepcopy(D)
            edit(E)
            hit = [ok for label, ok, _ in checks(E) if label.startswith(target)]
            others = [label for label, ok, _ in checks(E) if not ok and not label.startswith(target)]
            c = len(hit) >= 1 and not any(hit)
            caught.append(c)
            lines.append(f'  arm: {name}: {"caught" if c else "NOT CAUGHT"} by "{target}"'
                         + (f'; also failing: {others}' if others else ''))
    ok = parent and caught and all(caught)
    lines.append('ALL PASS' if ok else 'FAIL')
    text = '\n'.join(lines) + '\n'
    open(os.path.join(HERE, 'check_target_records.out'), 'w').write(text)
    print(text, end='')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
