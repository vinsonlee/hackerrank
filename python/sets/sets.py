#!/usr/bin/env python

M = int(raw_input())
s = set(map(int, raw_input().split()))

N = int(raw_input())
t = set(map(int, raw_input().split()))

for x in sorted(s.symmetric_difference(t)):
    print x
