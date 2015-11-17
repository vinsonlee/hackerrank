#!/usr/bin/env python

import collections

X = int(raw_input())
sizes = collections.Counter(map(int, raw_input().split()))
N = int(raw_input())

money = 0

for i in range(N):
    (size, price) = map(int, raw_input().split())

    if sizes[size] > 0:
        sizes[size] -= 1
        money += price

print money
