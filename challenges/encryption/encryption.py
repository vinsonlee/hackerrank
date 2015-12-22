#!/usr/bin/env python

import math

s = raw_input().strip()
s = s.replace(' ', '')

L = len(s)
rows = int(math.floor(math.sqrt(L)))
cols = int(math.ceil(math.sqrt(L)))
if rows * cols < L:
    rows += 1

assert rows <= cols
assert rows * cols >= L

output = list()

for c in range(cols):
    t = ''
    for r in range(rows):
        index = r * cols + c
        if index < L:
            t += s[index]
    output.append(t)

print ' '.join(output)
