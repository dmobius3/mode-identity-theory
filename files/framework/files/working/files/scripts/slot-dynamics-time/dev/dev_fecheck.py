"""Development (DEVLOG entry 9): control 11's cross-check alone, at the development duration, dev seed 900301. Not a
control."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import controls  # noqa: E402  (one BLAS thread, the pins)
import fecheck  # noqa: E402
import numpy as np  # noqa: E402
r = fecheck.run(controls.DEV['fe'], np.random.default_rng(900301), print)
print('conjugator u', r['conjugator_u'], '| intertwiner', r['intertwiner'], '| convention', f"{r['convention_residual']:.1e}")
print('distances', ' '.join(f"{o['t']:.2f}:{o['distance']:.2e}" for o in r['observations']))
print('charge drift: finite elements', f"{max(o['fe_charge_drift'] for o in r['observations']):.1e}",
      'Galerkin', f"{max(o['galerkin_charge_drift'] for o in r['observations']):.1e}")
