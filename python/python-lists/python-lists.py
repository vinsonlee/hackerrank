#!/usr/bin/env python

L = []

N = int(raw_input())

for i in range(0, N):
    tokens = raw_input().split()

    if tokens[0] == 'insert':
        L.insert(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'print':
        print L
    elif tokens[0] == 'remove':
        L.remove(int(tokens[1]))
    elif tokens[0] == 'append':
        L.append(int(tokens[1]))
    elif tokens[0] == 'sort':
        L.sort()
    elif tokens[0] == 'pop':
        L.pop()
    elif tokens[0] == 'reverse':
        L.reverse()
