"""Post-run: made after M8.19's registered run. It reads the environment again by the launch's route, as main() in
run/m819_run.py reads it before launch(): the driver imported first, which sets the four threading variables, then
validate_frozen(), then run/record_environment.py --check as its subprocess, with -I -B. These are the replayed calls
of freeze2/freeze_2.py's step (e), the same text. It writes nothing in the folder.

Usage, from the folder: python3 -I -B tools/postrun_env.py OUT
  OUT: a new file, created exclusively, that gets the output; the console gets the same text. Exit status: the check's."""
import datetime
import subprocess
import sys

REPLAY = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch as D; "
          "F = D.validate_frozen(); print('validate_frozen: passed;', len(F['pins']), 'pins; go', F['go'], flush=True); "
          "e = subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py'), '--check'], "
          "capture_output=True, text=True); print(e.stdout, end='', flush=True); sys.exit(e.returncode)")

if len(sys.argv) != 2:
    sys.exit(__doc__)
with open(sys.argv[1], 'x', encoding='utf-8') as out:
    t = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    p = subprocess.run([sys.executable, '-I', '-B', '-c', REPLAY], capture_output=True, text=True)
    text = (f'# read after the run, at {t}\n$ (from the folder) {sys.executable} -I -B -c "{REPLAY}"\n'
            f'{p.stdout}{p.stderr}exit {p.returncode}\n')
    out.write(text)
print(text, end='')
sys.exit(p.returncode)
