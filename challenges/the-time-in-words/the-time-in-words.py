#!/usr/bin/env python

h = int(raw_input().strip())
m = int(raw_input().strip())

d = dict()
d[0] = None
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
d[4] = 'four'
d[5] = 'five'
d[6] = 'six'
d[7] = 'seven'
d[8] = 'eight'
d[9] = 'nine'
d[10] = 'ten'
d[11] = 'eleven'
d[12] = 'twelve'
d[13] = 'thirteen'
d[14] = 'fourteen'
# d[15]
d[16] = 'sixteen'
d[17] = 'seventeen'
d[18] = 'eighteen'
d[19] = 'nineteen'
d[20] = 'twenty'
for i in range(21, 30):
    d[i] = 'twenty ' + d[i % 20]
# d[30]


def time_in_words(h, m):
    if m == 0:
        print d[h], "o' clock"
    elif m == 1:
        print 'one minute past', d[h]
    elif 2 <= m <= 14 or 16 <= m <= 29:
        print d[m], 'minutes past', d[h]
    elif m == 15:
        print 'quarter past', d[h]
    elif m == 30:
        print 'half past', d[h]
    elif 31 <= m <= 44 or 46 <= m <= 58:
        print d[60-m], 'minutes to', d[(h+1) % 12]
    elif m == 45:
        print 'quarter to', d[(h+1) % 12]
    elif m == 59:
        print 'one minute to', d[(h+1) % 12]
    else:
        assert False, m

time_in_words(h, m)
