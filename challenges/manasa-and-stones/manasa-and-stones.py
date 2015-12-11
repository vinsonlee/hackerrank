#!/usr/bin/env python

T = int(raw_input())

for _ in range(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())

    values = set()

    # t = total number of remaining stones [1, n]
    # v = value of last stone
    for t in range(0, n):
        v = t * a + (n - 1 - t) * b
        values.add(v)

    print ' '.join(map(str, sorted(list(values))))
