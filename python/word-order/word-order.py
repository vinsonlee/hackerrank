#!/usr/bin/env python

import collections

n = int(raw_input())

d = collections.OrderedDict()

for i in range(n):
    word = raw_input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print len(d)

for key, value in d.iteritems():
    print value,
