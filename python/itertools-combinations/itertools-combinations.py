#!/usr/bin/env python

import itertools

(S, k) = raw_input().split()
S = sorted(S)
k = int(k)

for i in range(1, k+1):
    l = map("".join, list(itertools.combinations(S, i)))

    for j in sorted(l):
        print j
