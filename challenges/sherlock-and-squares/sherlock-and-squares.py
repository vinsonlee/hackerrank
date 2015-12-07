#!/usr/bin/env python

import math

t = int(raw_input())

for line in range(t):
    (a, b) = map(int, raw_input().split())

    lower = int(math.floor(math.sqrt(a)))
    higher = int(math.ceil(math.sqrt(b))) + 1

    print len([x for x in range(lower, higher) if x**2 >= a and x**2 <= b])
