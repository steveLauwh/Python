#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。
'''
from collections import deque

dq = deque(range(10), maxlen = 10)

print(dq)

dq.rotate(3)

print(dq)

dq.rotate(-4)

print(dq)

dq.appendleft(-1)

print(dq)

dq.extend([11, 22, 33])

print(dq)

dq.extendleft([10, 20, 30, 40])

print(dq)
