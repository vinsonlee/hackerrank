#!/usr/bin/env python

import collections
import sys

T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    sideLengths = collections.deque(map(int, raw_input().split()))

    lastLength = sys.maxint
    answer = 'Yes'

    while len(sideLengths) > 0:
        if len(sideLengths) == 1:
            item = sideLengths.pop()
        else:
            if sideLengths[0] < sideLengths[-1]:
                item = sideLengths.pop()
            else:
                item = sideLengths.popleft()

        if item > lastLength:
            answer = 'No'
            break
        else:
            lastLength = item

    print answer
