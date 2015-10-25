#!/usr/bin/env python

K = int(raw_input())
room_numbers = map(int, raw_input().split())
rooms = set(room_numbers)

print (sum(rooms) * K - sum(room_numbers)) / (K - 1)
