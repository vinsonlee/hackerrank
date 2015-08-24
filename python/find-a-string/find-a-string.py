#!/usr/bin/env python

S = raw_input()
s = raw_input()
total = 0

for i in range(0, len(S) - len(s) + 1):
    if S[i:i+len(s)] == s:
        total += 1

print total
