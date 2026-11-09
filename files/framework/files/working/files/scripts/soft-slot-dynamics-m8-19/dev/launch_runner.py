"""One orchestrator launch on a job list of the caller's, for the launch tests: m819_run.launch(OUT, JOBS, bench, PIN).

  launch_runner.py OUT JOBS_JSON PIN [DRIVER] [--registered-order]   (a stub DRIVER only with the registered order)"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'run'))
import m819_run as R  # noqa: E402

args = sys.argv[1:]
bench = '--registered-order' not in args
args = [x for x in args if x != '--registered-order']
R.launch(os.path.abspath(args[0]), json.load(open(args[1])), bench, args[2], *([os.path.abspath(args[3])] if len(args) > 3 else []))
