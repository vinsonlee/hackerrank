#!/usr/bin/env python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    # plant in spring
    height = 1
    # cycle 1 - summer
    # cycle 2 - spring
    # cycle 3 - summer
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:
            height = 2 * height
        else:
            height = height + 1

    print height
