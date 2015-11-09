#!/usr/bin/env python

import itertools

(S, k) = raw_input().split()
S = sorted(S)
k = int(k)

l = map("".join, list(itertools.combinations_with_replacement(S, k)))

for i in l:
    print i
