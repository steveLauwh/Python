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

map 接受两个参数，第一个参数为函数，第二个参数是 Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回。

```python
#!/usr/bin/enb python3

def f(x):
    return x**2

r = map(f, [1, 2, 3, 4, 5, 6])

print(list(r))
```

reduce 接受两个参数，第一个参数为函数，第二参数是 Iterable，但是这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算。

```python
#!/usr/bin/env python3

from functools import reduce

def f(x, y):
    return x * 10 + y
    
r = reduce(f, [1, 3, 5, 7, 9]) 

print(r)   # 13579
```

> **filter**

过滤序列

> **sorted**



## 闭包

## 装饰器
