#!/usr/bin/env python

import operator

N = int(raw_input())

names = list()

for i in range(N):
    names.append(raw_input().split())

names.sort(key=operator.itemgetter(2))

for name in names:
    if name[3] == 'M':
        title = 'Mr.'
    else:
        title = 'Ms.'

    print '{} {} {}'.format(title, name[0], name[1])
