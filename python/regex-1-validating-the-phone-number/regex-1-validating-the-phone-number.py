#!/usr/bin/env python

import re

N = int(raw_input())

prog = re.compile(r'[789][0-9]{9}$')

for i in range(N):
    number = raw_input()
    result = prog.match(number)

    if result:
        print 'YES'
    else:
        print 'NO'
