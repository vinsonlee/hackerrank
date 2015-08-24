#!/usr/bin/env python

import re


def isValidAddress(address):
    result = re.match(r'[a-zA-z0-9\-_]+@[a-zA-Z0-9]+\..{1,3}$', address)
    return True if result else False

N = int(raw_input())
addresses = []
for i in range(N):
    addresses.append(raw_input())

addresses = filter(isValidAddress, addresses)
addresses.sort()
print addresses
