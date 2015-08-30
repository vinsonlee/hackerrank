#!/usr/bin/env python


def standardize_number(number):
    return '+91 {} {}'.format(number[-10:-5], number[-5:])

N = int(raw_input())

numbers = list()

for i in range(N):
    numbers.append(raw_input())

numbers = map(standardize_number, numbers)
numbers.sort()

for number in numbers:
    print number
