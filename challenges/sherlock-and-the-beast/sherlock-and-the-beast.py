#!/usr/bin/env python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    # https://www.hackerrank.com/challenges/sherlock-and-the-beast/forum
    z = n

    while z % 3 != 0:
        z -= 5

    if z < 0:
        print '-1'
    else:
        print z * '5' + (n - z) * '3'
