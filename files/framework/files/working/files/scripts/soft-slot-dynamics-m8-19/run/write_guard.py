"""M8.19's freeze (the terms: THE FREEZE, THE GUARD AND THE RUN): run/FROZEN.json and its pin, run/FROZEN_PIN, written
once after the maintainer's go, by exclusive create, as M8.18's run/write_guard.py wrote its own.

  write_guard.py GO_LINK [--terms-from OPENWAVE_CLONE]     after record_environment.py has written run/ENVIRONMENT.json

FROZEN.json holds: frozen, the go, the time; the terms' SHA-256 (run/m8_19_task_details.md, which must equal OpenWave's
merged task document when a clone is named); the SHA-256 of every file under run/ (but out/ and the freeze's own two
files) and reference/; the instrument's manifest SHA-256, with every instrument file at its manifest; the solver commit;
and M8.15's frozen numbers, the instrument's out/freeze_numbers.json. m819_branch.validate_frozen then reads it back
before anything sealed runs, and this script refuses unless that reading passes."""
import datetime
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import m819_branch as D  # noqa: E402

MERGED = 'openwave/xperiments/m8_mit/research/tasks/m8_19_task_details.md'


def main():
    go = sys.argv[1]
    if not go.startswith('https://github.com/openwave-labs/openwave/'):
        raise SystemExit('REFUSED: the go is a link to OpenWave')
    if not os.path.exists(os.path.join(HERE, 'ENVIRONMENT.json')):
        raise SystemExit('REFUSED: no run/ENVIRONMENT.json: run record_environment.py first')
    terms = os.path.join(HERE, 'm8_19_task_details.md')
    if '--terms-from' in sys.argv:
        clone = sys.argv[sys.argv.index('--terms-from') + 1]
        merged = subprocess.run(['git', '-C', clone, 'show', f'upstream/main:{MERGED}'], capture_output=True, check=True).stdout
        if open(terms, 'rb').read() != merged:
            raise SystemExit("REFUSED: run/m8_19_task_details.md differs from OpenWave's merged task document")
    man = json.load(open(os.path.join(D.INSTRUMENT, 'out', 'MANIFEST.json')))
    bad = [f for f in sorted(os.listdir(D.INSTRUMENT)) if f.endswith('.py') and man['sha256'].get(f) != D.sha(os.path.join(D.INSTRUMENT, f))]
    if bad:
        raise SystemExit(f'REFUSED: the instrument differs from its manifest ({bad})')
    F = dict(frozen=True, go=go, written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             terms_sha256=D.sha(terms), solver_commit='97a8c08',
             instrument_manifest_sha256=D.sha(os.path.join(D.INSTRUMENT, 'out', 'MANIFEST.json')),
             pins={rel: D.sha(os.path.join(D.ROOT, rel)) for rel in D.pinned_files()},
             freeze_numbers=D.frozen_numbers('C1'))
    path = os.path.join(HERE, 'FROZEN.json')
    with open(path, 'x') as f:
        json.dump(F, f, indent=1)
        f.write('\n')
    with open(os.path.join(HERE, 'FROZEN_PIN'), 'x') as f:
        f.write(D.sha(path) + '\n')
    D.validate_frozen()
    print(f'FROZEN.json written: {len(F["pins"])} files pinned; pin {D.sha(path)}')


if __name__ == '__main__':
    main()
