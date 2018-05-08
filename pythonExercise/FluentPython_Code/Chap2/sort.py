#!/usr/bin/env python3
# coding:utf-8

'''Chap 2
list.sort 方法和内置函数 sorted

list.sort 方法会就地排序列表，不会把原列表复制一份。

内置函数 sorted 会新建一个列表作为返回值。
'''
fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))

print(fruits)

print(sorted(fruits, reverse = True))

print(sorted(fruits, key = len))

print(sorted(fruits, key = len, reverse = True))

print(fruits)

print(fruits.sort())

print(fruits)
