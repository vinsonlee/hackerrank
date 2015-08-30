#!/usr/bin/env python

# https://docs.python.org/2/library/xml.etree.elementtree.html#xmlparser-objects
from xml.etree.ElementTree import XMLParser


class MaxDepth:
    maxDepth = -1
    depth = -1

    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        assert self.maxDepth != -1
        return self.maxDepth

lines = int(raw_input())

xml = ''
for i in range(lines):
    xml += raw_input()

target = MaxDepth()
parser = XMLParser(target=target)
parser.feed(xml)
maxDepth = parser.close()
print maxDepth
