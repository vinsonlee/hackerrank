#!/usr/bin/env python

N = int(raw_input())
A = map(int, raw_input().split())
A = list(set(A))
print A[-2]
