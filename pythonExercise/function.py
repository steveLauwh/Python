#!/usr/bin/env python3

# 不可变对象
a = 1 

def change_integer(a):
    a = 2 
    return a

print(change_integer(a))

print(a)

# 可变对象
list1 = [1, 'Hello', 3]

def change_list(list1):
    list1[2] = 5 
    return list1

print(change_list(list1))

print(list1)

# 判断闰年

def isLeap(year):
    return (year%400 == 0 or (year%4 == 0 and year%100 != 0)) 

print(isLeap(2018))
