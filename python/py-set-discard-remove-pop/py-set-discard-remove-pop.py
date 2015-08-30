#!/usr/bin/env python

n = input()
s = set(map(int, raw_input().split()))
N = int(raw_input())

for i in range(N):
    command = raw_input().split()

    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    else:
        assert False

print sum(s)
