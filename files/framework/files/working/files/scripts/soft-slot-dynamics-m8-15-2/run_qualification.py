"""M8.15.2's qualification chain (REGISTER_5.md § 5 item 3), run on the bench folder, detached, one step at a time:
the synthetic tests, R4b, R5, the five real-solver runs (r3, r3arm, r1arm, c3, c2a), then the evaluation. The first
failing step stops the chain. Each step's start, exit and end go to out/chain.log in the locator folder.

  python3 run_qualification.py               starts the chain in its own session and returns
  python3 run_qualification.py --from STEP   resumes at STEP after an interruption (the steps before it completed)
  python3 run_qualification.py --chain [STEP] the chain itself (what the detached process runs)

TERMS stands in for M8.15.2's terms, which come after RESULT_5; OLD_TERMS is M8.15.1's (fc566c04..., the hash the
instrument's FROZEN.json carries)."""
import os, sys, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
LOC = os.path.join(HERE, 'scripts', 'soft-slot-dynamics-m8-15-2')
TERMS = os.path.join(HERE, '..', 'REGISTER_5.md')
OLD_TERMS = os.path.join(HERE, '..', '..', 'm8_15x', 'm8_15_1_task_details.md')
QUALDIR = os.path.join('..', 'soft-slot-dynamics-m8-15x', 'qualification', 'solver', 'm8_15_solver', 'out')
STEPS = [('synthetic', ['tests/synthetic.py']),
         ('r4b', ['tests/real.py', 'r4b']),
         ('r5', ['tests/real.py', 'r5', os.path.normpath(TERMS), os.path.normpath(OLD_TERMS)]),
         ('r3', ['tests/real.py', 'run', 'r3']),
         ('r3arm', ['tests/real.py', 'run', 'r3arm']),
         ('r1arm', ['tests/real.py', 'run', 'r1arm']),
         ('c3', ['tests/real.py', 'run', 'c3']),
         ('c2a', ['tests/real.py', 'run', 'c2a']),
         ('evaluate', ['tests/real.py', 'evaluate', QUALDIR])]


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def chain(first=None):
    os.makedirs(os.path.join(LOC, 'out'), exist_ok=True)
    log = open(os.path.join(LOC, 'out', 'chain.log'), 'a', buffering=1)
    names = [n for n, _ in STEPS]
    steps = STEPS[names.index(first):] if first else STEPS
    log.write(f'chain start {now()}' + (f', resumed at {first}' if first else '') + '\n')
    for name, args in steps:
        log.write(f'{name} start {now()}\n')
        r = subprocess.run([sys.executable] + args, cwd=LOC, stdout=open(os.path.join(LOC, 'out', f'step_{name}.log'), 'w'),
                           stderr=subprocess.STDOUT)
        log.write(f'{name}: exit {r.returncode}\n{name} end {now()}\n')
        if r.returncode != 0:
            log.write(f'chain stopped at {name} {now()}\n')
            return 1
    log.write(f'chain done {now()}\n')
    return 0


if __name__ == '__main__':
    if '--chain' in sys.argv:
        i = sys.argv.index('--chain')
        sys.exit(chain(sys.argv[i + 1] if len(sys.argv) > i + 1 else None))
    first = sys.argv[sys.argv.index('--from') + 1] if '--from' in sys.argv else None
    if first is not None and first not in [n for n, _ in STEPS]:
        raise SystemExit(f'refused: no step {first}')
    if first is None and (os.listdir(os.path.join(LOC, 'out')) if os.path.isdir(os.path.join(LOC, 'out')) else []):
        raise SystemExit(f'refused: {os.path.join(LOC, "out")} is not empty; the recorded run starts clean')
    p = subprocess.Popen([sys.executable, os.path.abspath(__file__), '--chain'] + ([first] if first else []), cwd=HERE,
                         start_new_session=True, stdout=subprocess.DEVNULL,
                         stderr=open(os.path.join(HERE, 'run_qualification.err'), 'a'))
    print(f'qualification chain started{", resuming at " + first if first else ""}, pid {p.pid}; out/chain.log in {LOC}')
