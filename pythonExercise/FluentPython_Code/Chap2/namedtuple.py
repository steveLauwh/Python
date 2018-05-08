#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
具名元组：collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类。
'''
from collections import namedtuple

# 具名数组两个参数：类名，类的各个字段的名字
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(tokyo.population)

print(tokyo.coordinates)

print(tokyo[1])

# _fields 属性是一个包含这个类所有字段名称的元组
print(City._fields)
