#!/usr/bin/env python

from __future__ import division

number = int(raw_input())
heights = map(int, raw_input().split())
assert len(heights) == number
heights = set(heights)

print '{:.3f}'.format(sum(heights) / len(heights))
