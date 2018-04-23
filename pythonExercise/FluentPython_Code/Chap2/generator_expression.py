#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
生成器表达式(generator expression)：背后遵守迭代器协议，可以逐个地产出元素

作用：避免额外的内存占用
'''
symbols = '$¢£¥€¤'

# 用生成器表达式初始化元组
codes = tuple(ord(symbol) for symbol in symbols)

print(codes)

#######################################
import array

# 用生成器表达式初始化数组
arr = array.array('I', (ord(symbol) for symbol in symbols))

print(arr)

#######################################
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

for tshirts in ('%s %s' % (color, size) for color in colors for size in sizes):
	print(tshirts)

#######################################

