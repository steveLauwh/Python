#!/usr/bin/env python3
# coding:utf-8

'''Chap 3
字典 dict，提供多种构造方法
'''
a = dict(one = 1, two = 2, three = 3)

b = {'one': 1, 'two': 2, 'three': 3}

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

d = dict([('two', 2), ('one', 1), ('three', 3)])

e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)

