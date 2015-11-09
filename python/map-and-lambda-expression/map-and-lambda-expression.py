#!/usr/bin/env python

N = int(raw_input())

if N == 0:
    fibs = []
elif N == 1:
    fibs = [0]
else:
    fibs = [0, 1]

while N > len(fibs):
    fibs.append(fibs[-1] + fibs[-2])

assert len(fibs) == N

print map(lambda x: x**3, fibs)
