#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
列表(list)是一个可变的序列，并且能同时存放不同类型的元素

列表推导(list comprehension)：生成列表

生成器表达式(generator expression)：背后遵守迭代器协议，可以逐个地产出元素
'''
symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]

print(codes)

#######################################
x = 'ABC'

dummy = [ord(x) for x in x]

print(x, dummy)

#######################################
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

#######################################

