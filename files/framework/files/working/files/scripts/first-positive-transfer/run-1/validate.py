import numpy as np
import time
from compute_all import *

t0 = time.time()
dots, g_c, g_d, g_p = precompute_placement('generic')
r = compute_block('2', 1, 'generic', 1.0, dots, g_c, g_d, g_p)
dt = time.time() - t0
print(f'Time: {dt:.1f}s')
print(f'hs_val    = {r["hs_val"]:.10f}  expected = {8/np.pi**2:.10f}  err = {abs(r["hs_val"]-8/np.pi**2)/(8/np.pi**2)*100:.2f}%')
print(f'proj_val  = {r["proj_val"]:.10f}  expected = {8/(3*np.pi**2):.10f}  err = {abs(r["proj_val"]-8/(3*np.pi**2))/(8/(3*np.pi**2))*100:.2f}%')
print(f'lam_val   = {r["lambda_val"]:.10f}  expected = {16/(3*np.pi**2):.10f}  err = {abs(r["lambda_val"]-16/(3*np.pi**2))/(16/(3*np.pi**2))*100:.2f}%')
print(f'lam_trans = {r["lambda_trans"]:.10f}  expected = {8/np.pi**2:.10f}  err = {abs(r["lambda_trans"]-8/np.pi**2)/(8/np.pi**2)*100:.2f}%')
ok = abs(r['lambda_val'] - 16/(3*np.pi**2)) / (16/(3*np.pi**2)) < 0.05
print(f'Accuracy OK: {ok}')
