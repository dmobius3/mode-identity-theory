# The daggers of Section 7.3

In [The Surviving Ray](/files/framework/files/bedrock/files/surviving-ray.md), the proof of Theorem 7.5 in Section 7.3 marks with a dagger † each step
that the M8.13 audit on the OpenWave M8 track supplied to the author's argument. The audit's records are
the [task, with the adjudication](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_13_task_details.md), the
[auditor's return](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/m8_13/run/stage2b_return.md) and the
[author's dated correction](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/scripts/m8_12_author/S0_S3_MAXIMUM_CORRECTION.md).

Section 7.3 carries that argument as a complete proof, restructured in five named places, with a
dagger on each step the audit supplied, one-line facts included. The three records list different
items: (A) the auditor's return, (B) the adjudication's list, on which the maintainer's independent
grading and the auditor's agree, and (C) the author's correction, which summarises (B). The dagger means
one thing, that the audit supplied the step, and Section 7.3 marks the union of (A) and (B) where it
uses the step. The table maps each of the 24 daggers to all three, so a reader holding any one record
can match every mark. The records write $`Q`$ for the trace-free nematic tensor, which is
$`\mathring{\mathcal{N}}`$ here.

| # | where | supplied step | (A) | (B) | (C) |
| --- | --- | --- | --- | --- | --- |
| 1 | Step 1 | the five functions are invariant quartics of bidegree (2,2) | S1.2 (for $`\lVert\rho_6\rVert^2`$) | row 1, "invariance of each of the four functions" | not listed |
| 2 | Step 1 | the identification with invariant hermitian forms on $`\mathrm{Sym}^2 V_3`$, with injectivity | S1.1 | not listed (its note records the same one-line proof for the auditor's own stage-1 argument) | not listed |
| 3 | 3a | $`\mathrm{Tr}\,\mathcal{N} = 12`$ | S3a.1 | not listed | listed only among what the checker does not gate |
| 4 | 3a | $`\mathrm{Tr}(QE) = \langle u, A_E u\rangle`$ | verified in 3a, not listed as supplied | row 3a | not listed |
| 5 | 3a | $`\lVert Q\rVert = \max_E \mathrm{Tr}(QE)`$, both halves | S3a.2 | row 3a | "the variational identity" |
| 6 | 3a | rotating $`E`$ conjugates $`A_E`$ | S3a.3 | row 3a | "the equivariance" |
| 7 | 3a | the block basis and entries | S3a.5 | row 3a | "the block basis" |
| 8 | 3b | $`a + 6b \le \sqrt6`$ on the ellipse | computed in the return's § 5, not listed as supplied | row 3b $`M_1`$ | "the on-ellipse maxima" |
| 9 | 3b | $`\lvert a\rvert \le \sqrt{3/2}`$ on the ellipse | S3b3.2 | row 3b $`M_3`$ | "the on-ellipse maxima" |
| 10 | 3b $`M_1`$ | the squaring and homogenising algebra, written out | 3b $`M_1`$, Supplied | not listed | not listed |
| 11 | 3b $`M_1`$ | the second squaring is reversible when $`a + 6b > 0`$ | 3b $`M_1`$, Supplied | not listed | not listed |
| 12 | 3b $`M_3`$ | $`\lambda_{\max} = -2a + \sqrt{30 - 16a^2}`$ is the on-ellipse form | S3b3.1 | row 3b $`M_3`$ | not listed |
| 13 | 3b $`M_3`$ | $`30 - 16a^2 \ge 6`$, so the radicand stays positive | S3b3.3 | row 3b $`M_3`$ | not listed |
| 14 | 3c | the branch $`a + 6b \le 0`$ has no equality point | S3c.3 | row 3c | listed |
| 15 | 3c | the sign conditions are forced | S3c.2 | row 3c | listed |
| 16 | 3c | the equality locus of $`M_2`$, by reflection | S3c.1 | row 3c | listed |
| 17 | 3c | the locus of $`M_3`$ meets the ellipse, so $`M_3`$ attains the bound | S3c.4 | row 3c | listed |
| 18 | 3d | the whole $`E^{*} = Q/\lVert Q\rVert`$ chain | 3d, Supplied in full | row 3d | listed |
| 19 | 3e | the spectrum, top eigenspace exactly $`\mathrm{span}\{v_3, v_{-3}\}`$ | 3e, Supplied | row 3e, "and its multiplicity two" | listed |
| 20 | 4 | $`f = (0, 0, 3(\lvert\alpha\rvert^2 - \lvert\beta\rvert^2))`$ on the span | step 4, Supplied | not listed | not listed |
| 21 | 4 | $`\lVert B_0\rVert^2 = 1/7`$ follows at $`\lvert\alpha\rvert = \lvert\beta\rvert`$ | step 4, Supplied | not listed | not listed |
| 22 | 4 | $`\lVert B_0\rVert^2 = 4\lvert\alpha\beta\rvert^2/7`$ on the span | not listed (only the balanced value is computed) | row 4 | listed |
| 23 | 4 | the profile $`\widehat{r}_6 = 463/924 - (\lvert\alpha\rvert^2 - \lvert\beta\rvert^2)^2/2`$ on the span | step 4, Supplied ("the strictness") | not listed | not listed (its second refinement states the same profile as $`2\lvert\alpha\rvert^2\lvert\beta\rvert^2 + 1/924`$) |
| 24 | 4 | the relative phase is a rotation about the axis | step 4, Supplied | not listed | not listed |

Three supplied steps are not used, because Section 7.3's proof goes another way at each:

| supplied step | (A) | (B) | (C) | why Section 7.3 does not need it |
| --- | --- | --- | --- | --- |
| $`\mathrm{U}(1)`$-invariance forces bidegree (2,2) | S1.3 | row 1, "the $`\mathrm{U}(1)`$ type restriction" | listed | Step 1 works in bidegree (2,2) from the start, as Proposition 6.1 does |
| the swap of the two maxima | S3a.4 | row 3a | listed | 3a argues sufficiency, $`\lVert Q\rVert \le \max_E \lambda_{\max}(A_E)`$, not equivalence |
| the homogeneous $`M_1`$ inequality holds for all $`(a, b)`$ | 3b $`M_1`$, Supplied (a remark) | not listed | not listed | Section 7.3 uses it on the ellipse only |

The proof departs from the audited note in five places. Step 1 goes through Proposition 6.1, in bidegree
(2,2) throughout, with the basis
$`\lVert u\rVert^4, \lvert f\rvert^2, \lVert B_0\rVert^2, \mathrm{Tr}\,\mathcal{N}^2`$ and
$`B_0 = -\langle\Theta u, u\rangle/\sqrt7`$ in place of Kawaguchi and Ueda's $`a_{00}`$. Step 3a proves
sufficiency, so the swap of the maxima drops out. The basis of 3a carries a sign on its fourth vector
that makes $`M_2`$ literally $`M_1`$ at $`-b`$. Step 3b proves the two ellipse bounds by identities,
$`6N^2 - (a + 6b)^2 = 3(a - 2b)^2`$ and $`(3/2)N^2 - a^2 = 12b^2`$, where the audit supplied them as
computed maxima; the daggers mark the bounds, not these proofs. Step 4 keeps the note's own argument and
adds the supplied profile as its explicit form. Unchanged from the note, and without daggers: step 2 and
the bound of $`M_2`$, both graded ESTABLISHED as written, the eigenvalue formula of $`M_1`$, the two
identities of 3b that the note uses (a sum of squares and a completed square), the three equality loci
and the statement of 3c's conclusion.

Two steps the audit supplied to the maximum argument also appear in Section 6. Proposition 6.1's proof
uses the identification of invariant quartics with invariant hermitian forms on $`\mathrm{Sym}^2 V_3`$,
which the audit supplied to the author's argument, and Section 6.2 states the spin-3 identity
$`\mathrm{Tr}\,\mathcal{N} = 12`$, another step the audit supplied to that argument. Section 6 is
self-contained and carries no daggers; the daggers in Section 7.3 mark both steps within the audited
argument. Step 1 of that proof works in bidegree (2,2) from the start, as Proposition 6.1 does, so the
audit's restriction from $`\mathrm{U}(1)`$-invariance to that bidegree is not used.
