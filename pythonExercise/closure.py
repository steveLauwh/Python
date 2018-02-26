#!/usr/bin/env python3
# coding:utf-8

##########################
def foo():
	print('I am foo')

def bar():
	print('I am bar')

foo.bar = bar
foo.bar()
##########################
def f(j):
    def g():   # g 就是闭包函数
        return j*j 
    return g

g1 = f(2)

print(g1.__closure__) # __closure__ 就是 enclosing作用域

print(g1())
##########################
def dec(func):
	def wrapper():
		func()
	return wrapper

def sum():
	print('sum')

foo = dec(sum)

foo()

print(foo.__closure__)
##########################