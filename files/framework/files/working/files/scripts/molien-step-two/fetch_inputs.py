"""Fetch the Planck inputs for step two, serially, from the NASA IRSA mirror of the Planck Legacy Archive,
and record their provenance. Whole files are streamed with a SHA-256 computed on the fly and their size
checked against Content-Length. Best-fit files inside the parameter zips are extracted by HTTP range reads
(end-of-central-directory, central directory, local header, member data), each checked against the zip's
own CRC32 and uncompressed size. Nothing here evaluates a likelihood or computes a spectrum.
"""
import hashlib, io, json, os, struct, sys, time, urllib.request, zipfile, zlib

UA = "molien-shells-step-two/1.0 (independent research; contact via GitHub dmobius3)"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "planck")
IRSA = "https://irsa.ipac.caltech.edu/data/Planck/release_3/"
WHOLE = [("software/COM_Likelihood_Data-baseline_R3.00.tar.gz", "COM_Likelihood_Data-baseline_R3.00.tar.gz"),
         ("ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-full_R3.01.txt", "COM_PowerSpect_CMB-TT-full_R3.01.txt")]
ZIPS = [("ancillary-data/cosmoparams/COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip",
         ["base_plikHM_TTTEEE_lowl_lowE.minimum", "base_plikHM_TTTEEE_lowl_lowE.minimum.theory_cl", "base_plikHM_TTTEEE_lowl_lowE.minimum.inputparams"]),
        ("ancillary-data/cosmoparams/COM_CosmoParams_base-plikHM_R3.01.zip",
         ["base_plikHM_TTTEEE_lowE.minimum", "base_plikHM_TTTEEE_lowE.minimum.inputparams"])]
prov = {"user_agent": UA, "fetched_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "files": []}

def req(url, rng=None, method="GET"):
    h = {"User-Agent": UA}
    if rng:
        h["Range"] = f"bytes={rng[0]}-{rng[1]}"
    return urllib.request.urlopen(urllib.request.Request(url, headers=h, method=method), timeout=120)

def head_size(url):
    with req(url, method="HEAD") as r:
        return int(r.headers["Content-Length"]), r.headers.get("Accept-Ranges"), r.headers.get("Last-Modified")

def ranged(url, a, b):
    with req(url, (a, b)) as r:
        assert r.status == 206, f"server ignored the range request ({r.status})"
        data = r.read()
    assert len(data) == b - a + 1, (len(data), b - a + 1)
    return data

for rel, name in WHOLE:
    url = IRSA + rel
    size, ar, lm = head_size(url)
    sha, n, dest = hashlib.sha256(), 0, os.path.join(OUT, name)
    if os.path.exists(dest) and os.path.getsize(dest) == size:
        with open(dest, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                sha.update(chunk); n += len(chunk)
        prov["files"].append({"file": name, "url": url, "bytes": n, "sha256": sha.hexdigest(), "last_modified": lm,
                              "method": "whole file (fetched earlier this session; size re-checked against the server, hash recomputed)"})
        print(f"{name}: already here, {n:,} bytes, sha256 {sha.hexdigest()}")
        continue
    with req(url) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            sha.update(chunk); f.write(chunk); n += len(chunk)
    assert n == size, (name, n, size)
    prov["files"].append({"file": name, "url": url, "bytes": n, "sha256": sha.hexdigest(), "last_modified": lm, "method": "whole file"})
    print(f"{name}: {n:,} bytes, sha256 {sha.hexdigest()}")
    time.sleep(2)

class RangeFile(io.RawIOBase):
    """A read-only, seekable view of a remote file, served by HTTP range requests in cached blocks."""
    def __init__(self, url, size, block=1 << 18):
        self.url, self.size, self.pos, self.block, self.cache, self.requests, self.fetched = url, size, 0, block, {}, 0, 0
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else self.pos + off if whence == 1 else self.size + off
        return self.pos
    def _blk(self, i):
        if i not in self.cache:
            a = i * self.block
            self.cache[i] = ranged(self.url, a, min(self.size, a + self.block) - 1)
            self.requests += 1; self.fetched += len(self.cache[i])
        return self.cache[i]
    def read(self, n=-1):
        n = self.size - self.pos if n is None or n < 0 else min(n, self.size - self.pos)
        out = bytearray()
        while n > 0:
            i, off = divmod(self.pos, self.block)
            take = self._blk(i)[off:off + n]
            if not take: break
            out += take; self.pos += len(take); n -= len(take)
        return bytes(out)
    def readinto(self, b):
        data = self.read(len(b)); b[:len(data)] = data; return len(data)

for rel, members in ZIPS:
    url = IRSA + rel
    size, ar, lm = head_size(url)
    assert ar == "bytes", (rel, ar)
    rf = RangeFile(url, size)
    zf = zipfile.ZipFile(rf)
    names = zf.namelist()
    zipname = rel.split("/")[-1]
    print(f"{zipname}: {size:,} bytes on the server, {len(names)} entries in its central directory")
    for want in members:
        hits = [k for k in names if k.split("/")[-1] == want]
        assert len(hits) == 1, (want, hits)
        info = zf.getinfo(hits[0])
        data = zf.read(hits[0])
        assert len(data) == info.file_size and (zlib.crc32(data) & 0xFFFFFFFF) == info.CRC, want
        with open(os.path.join(OUT, want), "wb") as f:
            f.write(data)
        digest = hashlib.sha256(data).hexdigest()
        prov["files"].append({"file": want, "from_zip": zipname, "zip_url": url, "zip_bytes": size, "zip_last_modified": lm,
                              "member_path": hits[0], "bytes": info.file_size, "crc32": f"{info.CRC:08x}", "sha256": digest,
                              "method": "HTTP range reads through zipfile; CRC32 and size checked"})
        print(f"   {hits[0]}: {info.file_size:,} bytes, CRC32 ok, sha256 {digest}")
    others = sorted(set(k.split("/")[1] for k in names if k.count("/") >= 2 and k.startswith("base/") and "TTTEEE" in k and "lowl" not in k))
    print(f"   TTTEEE fits without lowl in this zip: {others}")
    print(f"   fetched {rf.fetched:,} bytes in {rf.requests} range requests")
    time.sleep(2)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "provenance.json"), "w") as f:
    json.dump(prov, f, indent=2)
print("provenance written:", len(prov["files"]), "files")
