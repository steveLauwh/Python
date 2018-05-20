#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Chap4
使用数组中的原始数据初始化 bytes 对象
'''
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

octets = bytes(numbers)

print(octets)