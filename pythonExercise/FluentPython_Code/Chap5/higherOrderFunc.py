#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Chap5
高阶函数
'''
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=len))

################################################################
def factorial(n):
	return 1 if n < 2 else n * factorial(n-1)

fact = factorial

# 构建 0! 到 5! 的一个阶乘列表
print(list(map(fact, range(6))))

# 使用列表推导执行相同的操作
print([fact(n) for n in range(6)])

# 使用 map 和 filter 计算直到 5! 的奇数阶乘列表
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))

# 使用列表推导做相同的工作，换掉 map 和 filter，并避免了使用 lambda 表达式
print([factorial(n) for n in range(6) if n % 2])