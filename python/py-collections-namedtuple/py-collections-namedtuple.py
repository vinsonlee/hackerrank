#!/usr/bin/env python

from __future__ import division
import collections

N = int(raw_input())
columns = ','.join(raw_input().split())
Student = collections.namedtuple('Student', columns)

sum = 0
for i in range(N):
    line = raw_input().split()
    student = Student(*line)
    sum += int(student.MARKS)

print sum / N
