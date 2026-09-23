# The Surviving Ray, second version: scripts

This folder holds the computations behind [The Surviving Ray](/files/framework/files/bedrock/files/surviving-ray.md): the certificates of
Section 7.2, five exact checks of arguments the paper gives itself, and the [map of the daggers](dagger-map.md)
in the proof of Theorem 7.5.

## The certificates of Section 7.2

The three orbits of Section 7.2 outside the census's class are certified by this paper, in 60-digit
interval arithmetic; the certificates are its own computation, not a reproduction. They are published
here, with their scripts, in two layers.

The record is the certification as it ran, unmodified. Its three work items were fixed in advance by
frozen packets, published with the scripts and their logs, and the two runs after them, the
one-certificate rows and the export of the boxes, are marked as supplements. Each log opens with the
SHA-256 of its script and of the files it rests on, and the second work item's failed first run, stopped
by a control, is kept beside its second. The certificates start from points of an exploratory numerical
census, which the first packet pins by hash and which is not distributed, so the archived scripts are not
meant to be rerun. A certificate does not depend on where its starting point came from: given the system
and the box, the Krawczyk inclusion holds or it does not.

The reproduction is what a reader reruns. The data file gives, for each orbit, the fixed set of its
full isotropy, its slices, the box centre recorded to 64 digits and the radius, $`10^{-55}`$. The verifier
rebuilds each system from that data and repeats the Krawczyk test, both bounds on the isotropy, the
signatures and the value enclosure. Its controls start from the census's exact representatives
([M8.12](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md)), not from boxes: the model's values at the four weight states; the six census orbits with
finite stabilisers, each certified from its exact point with the exact signature and value the census
records; the pyramid and the prism in their own fixed sets, with isotropy of orders 10 and 12 and their
line extrema; and the D2 ray's isotropy, of order 8. Planted failures, each on a passing parent, are
caught. Each statement of Section 7.2 maps to the log lines that give it:

| Section 7.2 says | as run | re-checked |
| --- | --- | --- |
| each outside orbit is a critical orbit, certified in the fixed set of its full isotropy at radius $`10^{-55}`$ | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the rotation stabiliser and the full isotropy of each row | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the three signatures of each row, and no transverse kernel | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the values, and $`\mathcal{O}_2`$'s interval of width $`3.1 \times 10^{-52}`$ containing $`28800/121`$ | `one_certificate_rows_log.txt` | `verify_certificates_log.txt` |
| the census's exact full signatures at the pyramid, the prism and the D2 ray, from their own fixed sets | `one_certificate_rows_log.txt` | `verify_certificates_log.txt`, the pyramid and the prism |
| the same at all six census orbits with finite stabilisers, from the whole sphere | `certify_inertia_log.txt` | `verify_certificates_log.txt` |

Five exact checks accompany them, each with its log, of arguments the paper gives itself: Proposition 6.1,
the line extrema of Section 7.2, Lemma 7.3 with the minimum, the steps of the maximum, and the prior
diagrams of Section 9.2.

`SHA256SUMS` lists the SHA-256 of every other file in this folder, and `shasum -a 256 -c SHA256SUMS`
checks them.
