"""Continuation of a pinned branch in the norm m, with eps = sigma - lambda0bar an output (the frozen algorithm):

- the ladder: eps_k = 0.25 * 2^(k/2) from eps_min up to eps_max, with eps_max appended;
- from the accepted point at eps_(k-1), m for eps_k is predicted by a secant through the last two accepted points (by
  m proportional to eps at the first step); the secant is iterated on m until |eps - eps_k| <= 1e-6 eps_k, at most 8
  iterations;
- every converged Newton solution is accepted, secant iterates included, and its (m, eps) recorded;
- a fold is declared at the first accepted solution whose eps is smaller than the previous accepted one while m
  increased; the turning point is located by a golden-section search in m maximizing eps(m) within the bracket of the
  last three accepted points, to 1e-3 relative in m; the branch ends there;
- if 8 secant iterations do not reach eps_k, the fold search runs only if the accepted points meet the fold criterion;
  otherwise the branch ends as a secant target failure, at its last accepted point;
- a Newton failure retries the step in m from the last accepted point at one half, then one quarter; a failure after
  both ends the branch;
- seeds: at eps_min the oriented germ interpolant scaled to the leading-order norm; afterwards the previous accepted
  solution scaled to the new m. No other seed, and the method is never switched."""
import numpy as np
from nonlinear import to_real
from pinned import solve_pinned

GOLD = (np.sqrt(5) - 1) / 2


def ladder(eps_min, eps_max):
    out, k = [], 0
    while True:
        e = 0.25 * 2 ** (k / 2)
        if e > eps_max * (1 + 1e-12):
            break
        if e >= eps_min * (1 - 1e-12):
            out.append(e)
        k += 1
    if not out or abs(out[-1] - eps_max) > 1e-9 * eps_max:
        out.append(eps_max)                    # also C1's single off-grid point, eps = 6
    return out


class Branch:
    def __init__(self, st, case, lam0, Q, vol, slices=(), tol=1e-11, maxit=40, log=print):
        self.st, self.case, self.lam0, self.Q, self.vol = st, case, lam0, Q, vol
        self.slices, self.tol, self.maxit, self.log = slices, tol, maxit, log
        self.accepted = []          # dicts: m, eps, sigma, x (real), it, full, nu
        self.points = []            # ladder points reached: index into accepted
        self.end = None

    def newton(self, m, x_from, m_from, eps_guess):
        x0 = x_from * np.sqrt(m / m_from)
        try:
            Phi, sigma, info = solve_pinned(self.st, self.case, m, self.lam0 + eps_guess, slices=self.slices,
                                            tol=self.tol, maxit=self.maxit, x0=x0)
        except (RuntimeError, np.linalg.LinAlgError, ValueError):
            return None
        rec = dict(m=m, eps=sigma - self.lam0, sigma=sigma, x=to_real(Phi), it=info['it'], full=info['full'],
                   nu=info['nu'])
        return rec

    def accept(self, rec):
        """Append; return True if this acceptance declares a fold."""
        self.accepted.append(rec)
        if len(self.accepted) >= 2:
            a, b = self.accepted[-2], self.accepted[-1]
            if b['m'] > a['m'] and b['eps'] < a['eps']:
                return True
        return False

    def first(self, eps0):
        x = to_real(self.case.seed)
        x = self.case.P @ x
        m0 = eps0 / (self.Q / self.vol) / 120
        m_x = x @ (self.st.Mr @ x)
        rec = self.newton(m0, x, m_x, eps0)
        if rec is None:
            self.end = ('Newton failure at the seed', None)
            return False
        self.accept(rec)
        # the seed point is a ladder point only once it meets eps0; iterate the secant like any other target
        return True

    def solve_target(self, eps_k, first_step=False):
        """Secant on m toward eps_k. Returns 'ok', 'fold', 'secant', 'newton'."""
        for it in range(8):
            last = self.accepted[-1]
            if abs(last['eps'] - eps_k) <= 1e-6 * eps_k:
                return 'ok'
            if len(self.accepted) == 1 or (first_step and it == 0):
                m_pred = last['m'] * eps_k / last['eps']
            else:
                a, b = self.accepted[-2], self.accepted[-1]
                if b['eps'] == a['eps']:
                    m_pred = b['m'] * eps_k / b['eps']
                else:
                    m_pred = b['m'] + (eps_k - b['eps']) * (b['m'] - a['m']) / (b['eps'] - a['eps'])
            rec = None
            for frac in (1.0, 0.5, 0.25):
                m_try = last['m'] + frac * (m_pred - last['m'])
                rec = self.newton(m_try, last['x'], last['m'], eps_k if frac == 1.0 else last['eps'] + frac * (eps_k - last['eps']))
                if rec is not None:
                    break
            if rec is None:
                return 'newton'
            if self.accept(rec):
                return 'fold'
        last = self.accepted[-1]
        return 'ok' if abs(last['eps'] - eps_k) <= 1e-6 * eps_k else 'secant'

    def fold_search(self):
        """Golden section in m maximizing eps(m) over the bracket of the last three accepted points."""
        three = self.accepted[-3:] if len(self.accepted) >= 3 else self.accepted[-2:]
        lo, hi = min(r['m'] for r in three), max(r['m'] for r in three)
        best = max(three, key=lambda r: r['eps'])
        def f(m):
            src = min(self.accepted, key=lambda r: abs(r['m'] - m))
            rec = self.newton(m, src['x'], src['m'], src['eps'])
            if rec is not None:
                self.accepted.append(rec)            # every converged Newton solution is recorded
            return rec
        a, b = lo, hi
        c, d = b - GOLD * (b - a), a + GOLD * (b - a)
        fc, fd = f(c), f(d)
        while (b - a) > 1e-3 * abs(b):
            if fc is None or fd is None:
                break
            if fc['eps'] > fd['eps']:
                b, d, fd = d, c, fc
                c = b - GOLD * (b - a)
                fc = f(c)
            else:
                a, c, fc = c, d, fd
                d = a + GOLD * (b - a)
                fd = f(d)
        cands = [r for r in (fc, fd, best) if r is not None]
        top = max(cands, key=lambda r: r['eps'])
        return top

    def run(self, targets, on_point=None):
        """Follow the ladder. on_point(index, eps_k, rec) is called at every ladder point reached."""
        if not self.first(targets[0]):
            return self
        for k, eps_k in enumerate(targets):
            status = self.solve_target(eps_k, first_step=(k == 1))
            if status == 'ok':
                rec = self.accepted[-1]
                self.points.append((k, eps_k, len(self.accepted) - 1))
                self.log(f'    eps_k {eps_k:.6g}: eps {rec["eps"]:.9f}, m {rec["m"]:.6e}, Newton {rec["it"]} it, residual {rec["full"]:.1e}'
                         + (f', slice force {rec["nu"]}' if len(rec['nu']) else ''))
                if on_point is not None:
                    on_point(k, eps_k, rec)
                continue
            if status == 'fold' or (status == 'secant' and self._meets_fold_criterion()):
                tp = self.fold_search()
                self.end = ('fold', dict(m=tp['m'], eps=tp['eps']))
            elif status == 'secant':
                self.end = ('secant target failure', dict(m=self.accepted[-1]['m'], eps=self.accepted[-1]['eps']))
            else:
                self.end = ('Newton failure', dict(m=self.accepted[-1]['m'], eps=self.accepted[-1]['eps']))
            self.log(f'    branch ends before eps_k {eps_k:.6g}: {self.end[0]} at eps {self.end[1]["eps"]:.6f}')
            return self
        self.end = ('eps_max', None)
        return self

    def goto(self, eps_target, start):
        """Secant from a given accepted record to eps_target (for change-of-type bisection); returns the record or None."""
        saved = self.accepted
        self.accepted = [start]
        try:
            status = self.solve_target(eps_target)
            rec = self.accepted[-1] if status == 'ok' else None
        finally:
            self.accepted = saved
        return rec

    def _meets_fold_criterion(self):
        A = self.accepted
        return any(A[i]['m'] > A[i - 1]['m'] and A[i]['eps'] < A[i - 1]['eps'] for i in range(1, len(A)))
