#!/usr/bin/env python

A = set(map(int, raw_input().split()))
N = int(raw_input())

isstrictsuperset = True

for i in range(N):
    s = set(map(int, raw_input().split()))
    if not s.issubset(A):
        isstrictsuperset = False
    if len(s) >= len(A):
        isstrictsuperset = False

print isstrictsuperset
