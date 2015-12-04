#!/usr/bin/env python

time = raw_input().strip()
hh = time[0:2]
period = time[-2:]

if period == 'AM':
    if hh == '12':
        output = '00' + time[2:-2]
    else:
        output = time[0:-2]
elif period == 'PM':
    hh = time[0:2]
    if hh == '12':
        output = time[0:-2]
    else:
        output = str(int(hh) + 12) + time[2:-2]
else:
    assert False

print output
