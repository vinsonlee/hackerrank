#!/usr/bin/env python

from __future__ import division
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Point(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def cross(self, other):
        u1 = self.x
        u2 = self.y
        u3 = self.z
        v1 = other.x
        v2 = other.y
        v3 = other.z
        s1 = u2 * v3 - u3 * v2
        s2 = u3 * v1 - u1 * v3
        s3 = u1 * v2 - u2 * v1
        return Point(s1, s2, s3)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


(x, y, z) = map(float, raw_input().split())
A = Point(x, y, z)

(x, y, z) = map(float, raw_input().split())
B = Point(x, y, z)

(x, y, z) = map(float, raw_input().split())
C = Point(x, y, z)

(x, y, z) = map(float, raw_input().split())
D = Point(x, y, z)

X = (B - A).cross(C - B)

Y = (C - B).cross(D - C)

phi = X.dot(Y) / (X.magnitude() * Y.magnitude())
phi = math.acos(phi)
phi = math.degrees(phi)

print '{:.2f}'.format(phi)
