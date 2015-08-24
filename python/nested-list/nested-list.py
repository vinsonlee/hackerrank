#!/usr/bin/env python

N = int(raw_input())

students = list()
for i in range(N):
    students.append([raw_input(), float(raw_input())])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print s
