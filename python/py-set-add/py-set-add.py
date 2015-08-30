#!/usr/bin/env python

N = int(raw_input())

countries = set()

for i in range(N):
    countries.add(raw_input())

print len(countries)
