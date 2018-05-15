#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
numpy 库
'''
import numpy as ny

# 新建 0-11 的整数 numpy.ndarray
a = ny.arange(12)

print(a)

print(type(a))

# 数组的维度
print(a.shape)

# 数组变成二维，打印
a.shape = 3, 4

print(a)

# 打印第 2 行
print(a[2])

# 打印第 2 行第 1 列元素
print(a[2, 1])

# 打印第 1 列
print(a[:, 1])

# 行和列交换
print(a.transpose())
