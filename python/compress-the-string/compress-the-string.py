#!/usr/bin/env python

import itertools

S = raw_input()

for k, g in itertools.groupby(S):
    print (len(list(g)), int(k)),
