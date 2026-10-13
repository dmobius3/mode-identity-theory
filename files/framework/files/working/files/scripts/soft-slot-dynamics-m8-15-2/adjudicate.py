"""M8.15.2's adjudication reading (the terms, § NAMING): the ceiling, through the function the tests verified, `ceiling`
in tests/synthetic.py, applied to each bracket of a target's record as loaded from its JSON. The one difference between
a record and the in-memory result the tests read is the level keys, which JSON writes as strings ("3", "2"). They are
read as integers here, and nothing else is changed. The adjudication is the maintainer's; this prints its reading.

  python3 adjudicate.py RECORD.json       each bracket's adjudicated names, with the record's own names beside them
  python3 adjudicate.py --check           the round trip on every synthetic plant, written to adjudicate_check.out:
                                          each result, written to JSON as the driver writes its records and read
                                          back, must give the names the in-memory result gives; and on every result
                                          that locates a change of type, the round trip without the key conversion
                                          must fail"""
import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'tests'))
sys.path.insert(0, HERE)


def int_levels(res):
    """A bracket record as loaded from JSON, its level-keyed maps read with integer keys."""
    out = dict(res)
    for k in ('levels', 'points', 'brackets'):
        if isinstance(res.get(k), dict):
            out[k] = {int(lv): v for lv, v in res[k].items()}
    return out


def adjudicate(record):
    """Each bracket's adjudicated names, read by the tests' ceiling function."""
    import synthetic
    return [dict(label=b['label'], **x) for b in record['brackets'] for x in synthetic.ceiling(int_levels(b))]


def round_trip(res):
    """A result as the driver writes it (json.dump with default=str) and as it is read back."""
    return json.loads(json.dumps(res, default=str))


def check():
    import mock, synthetic
    lines, runs, located, bad = [], 0, 0, []
    for name, plant, expect, arms in synthetic.TESTS:
        cases = [(name, plant)] if isinstance(plant, dict) else [(f'{name} {lab}', kw) for lab, kw in plant]
        for label, kw in cases:
            res = mock.run(mock.Plant(**kw))
            want = synthetic.ceiling(res)
            got = synthetic.ceiling(int_levels(round_trip(res)))
            runs += 1
            if got != want:
                bad.append(f'{label}: the round trip gives {[x["name"] for x in got]} against {[x["name"] for x in want]}')
            if any(x['record_name'] == synthetic.LOCATED for x in want):
                located += 1
                try:
                    synthetic.ceiling(round_trip(res))
                    bad.append(f'{label}: without the key conversion the round trip did not fail')
                except KeyError:
                    pass
    lines.append(f'adjudicate.py --check: {runs} synthetic results; the round trip gives the in-memory names at each: '
                 f'{"yes" if not any("gives" in b for b in bad) else "NO"}')
    lines.append(f'the arm, the key conversion dropped: fails on each of the {located} results that locate a change of type: '
                 f'{"yes" if not any("did not fail" in b for b in bad) else "NO"}')
    lines += [f'  {b}' for b in bad]
    lines.append('PASS' if not bad and located else 'FAIL')
    text = '\n'.join(lines) + '\n'
    open(os.path.join(HERE, 'adjudicate_check.out'), 'w').write(text)
    print(text, end='')
    return not bad and located > 0


if __name__ == '__main__':
    if sys.argv[1:] == ['--check']:
        sys.exit(0 if check() else 1)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    rec = json.load(open(sys.argv[1]))
    for row in adjudicate(rec):
        print(f'{row["label"]}: {row["name"]}' + (f' ({"; ".join(row["reasons"])})' if row.get('reasons') else '')
              + f'  [the record: {row["record_name"]}]')
