"""Emit the ITEMS table of test_constants.py: one item per line that holds a number, its anchor from the document."""
import re, sys
text = open(sys.argv[1], encoding='utf-8').read()
TOKEN = re.compile(r'(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?×10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|\d+(?:\.\d+)?(?:/\d+)?%?)(?![A-Za-z0-9_])')
NOT = [r'§ [0-9]+(?:\.[0-9]+)?', r'SHA-256', r'#[0-9]+', r'[0-9]{4}-[0-9]{2}-[0-9]{2}', r'\]\([^)]*\)', r'\[[0-9]+\]', r'(?m)^[0-9]+\. ', r'(?:step|clause|level|amendment|test) [0-9]+']
sp = [(m.start(), m.end()) for p in NOT for m in re.finditer(p, text)]
ref = lambda i: any(a <= i < b for a, b in sp)
pos, lines = 0, []
for ln, line in enumerate(text.split('\n'), 1):
    ms = [m for m in TOKEN.finditer(line) if not ref(pos + m.start())]
    if ms:
        a, b = ms[0].start(), ms[-1].end()
        left, right = max(0, a - 14), min(len(line), b + 8)
        while text.count(line[left:right]) != 1:
            if left > 0:
                left -= 1
            elif right < len(line):
                right += 1
            else:
                break
        lines.append((ln, line[left:right], [m.group(1) for m in ms]))
    pos += len(line) + 1
for ln, anchor, toks in lines:
    print(f'    ({ln}, {anchor!r}, {toks!r}),')
