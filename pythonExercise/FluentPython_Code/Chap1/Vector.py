#!/usr/bin/env python3
# coding:utf-8

''' Chap 1
一个简单的二维向量类

模拟数值类型
'''

from math import hypot

class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vector<%r, %r>' % (self.x, self.y)

	def __abs__(self):
		return hypot(self.x, self.y)

	def __bool__(self):
		return bool(self.x or self.y) 

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

# test
v = Vector(3, 4)
v2 = Vector(4, 5)

print(v)

print(abs(v))

print(bool(v))

print(v + v2)

print(v * 3)

print(v - v2)
