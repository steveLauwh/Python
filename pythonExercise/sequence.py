#!/usr/bin/env python3

# tuple(元组)

tuple1 = (11, 2, 9, 1)

print(tuple1, type(tuple1))

tuple2 = ('H', 2, 1.1, False)

print(tuple2, type(tuple2))

print(tuple1[3], tuple2[0])

print(tuple1[:4])

print(tuple1[2:4])

# 字符串也是 tuple

str1 = 'Hello'

print(str1[2:4])

#str1[0] = 1
#print(str1)

# list(表)

list1 = ['a', 1.2, 4, True]

print(list1, type(list1))

list1[0] = 1

print(list1)

print(list1[-1])

# tuple 中包含 list

tuple3 = (tuple1,list1)

print(tuple3, type(tuple3))

tuple3[1][2] = 'H'  # tuple中存储的是固定的list地址，但list中的元素是可变的

print(tuple3, type(tuple3))

# list 中包含 tuple

list2 = [tuple1, list1]

print(list2, type(list2))

print(list2[0])

print(list2[1])










