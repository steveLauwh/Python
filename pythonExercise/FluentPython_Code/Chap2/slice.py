#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
切片：list, tuple, str 都支持切片操作.
'''
l = list(range(10))

print(l)

l[2:5] = [20, 30]

print(l)

del l[5:7]

print(l)

l[3::2] = [11, 22] 

print(l)

l[2:5] = [100]

print(l)
