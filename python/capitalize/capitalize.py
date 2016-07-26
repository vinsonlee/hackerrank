#!/usr/bin/env python

import string

s = raw_input()
print ' '.join(map(string.capitalize, s.split(' ')))
