#!/usr/bin/env python

import xml.etree.ElementTree as etree

lines = int(raw_input())

xml = ''
for i in range(lines):
    xml += raw_input()
tree = etree.ElementTree(etree.fromstring(xml))

score = 0

for element in tree.getroot().iter():
    score += len(element.attrib)

print score
