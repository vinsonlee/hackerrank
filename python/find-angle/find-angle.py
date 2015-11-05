#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import math

ab = int(raw_input())
bc = int(raw_input())
c = math.degrees(math.atan(ab / bc))
c = int(round(c))
print str(c) + '°'
