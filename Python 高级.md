# Python 高级

## 高阶函数

一个函数可以接收另一个函数作为参数，这种函数就称之为 高阶函数。

```python
#!/usr/bin/env python3

def add(x, y, f):
    return f(x) + f(y)

print(add(-1, 3, abs))
```

> **map/reduce**

map 接收两个参数，第一个参数为函数，第二个参数是 Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回。

```python
#!/usr/bin/env python3

def f(x):
    return x**2

r = map(f, [1, 2, 3, 4, 5, 6])

print(list(r))
```

reduce 接收两个参数，第一个参数为函数，第二参数是 Iterable，但是这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算。

```python
#!/usr/bin/env python3

from functools import reduce

def f(x, y):
    return x * 10 + y
    
r = reduce(f, [1, 3, 5, 7, 9]) 

print(r)   # 13579
```

> **filter**

作用是过滤序列，也是接收两个参数，第一个参数为函数，第二个参数是序列，filter 将函数依次作用于序列，根据 True 或 False 来过滤序列。

```python
#!/usr/bin/env python3

def is_odd(n):
    return n % 2 == 1
    
r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]) 

print(list(r)) 
```

> **sorted**

排序函数。

对字符串排序，是按照 ASCII 的大小比较的。

```python
#!/usr/bin/env python3

print(sorted([-5, 19, 30, -23], key=abs))
```

## 闭包(closure)

函数对象作为某个函数的返回结果。

返回函数不要引用任何循环变量，或者后续会发生变化的变量。

```python
#!/usr/bin/env python3

def f(j):
    def g():
        return j*j 
    return g

g1 = f(2)

g2 = f(3)

print(g1())

print(g2())
```

## 装饰器(decorator)

装饰器可以对一个函数、方法或者类进行封装，更加抽象。提高了程序的可重复利用性，并增加了程序的可读性。

```python
#!/usr/bin/env python3

def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))
```
