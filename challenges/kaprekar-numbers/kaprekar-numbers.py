#!/usr/bin/env python

r = int(raw_input())
q = int(raw_input())

kaprekar_numbers = list()

for n in range(r, q + 1):
    s = str(n * n)
    d = len(s) / 2

    if len(s) == 1:
        l = 0
    else:
        l = int(s[0:d])
    r = int(s[d:len(s)])

    if l + r == n:
        kaprekar_numbers.append(n)

if len(kaprekar_numbers) > 0:
    print ' '.join([str(x) for x in kaprekar_numbers])
else:
    print 'INVALID RANGE'
