# Python 高级

## `__slots__`

创建了一个 class 的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

Python 允许在定义 class 的时候，定义一个特殊的 `__slots__` 变量，来限制该 class 实例能添加的属性。

```python
class Student(object):
    __slots__ = ('name', 'age') # 用 tuple 定义允许绑定的属性名称
```

注意：`__slots__` 只对当前类有效，对子类没有限制。

## @property

Python 内置的 @property 装饰器是负责把一个方法变成属性调用的。

```python
#!/usr/bin/env python3

class Screen(object):
    @property
    def width(self):
    	return self._width

    @width.setter
    def width(self, value):
    	if not isinstance(value, int):
            raise ValueError('width must be an integer!')
    	self._width = value

    @property
    def height(self):
    	return self._height

    @height.setter
    def height(self, value):
    	if not isinstance(value, int):
            raise ValueError('height must be an integer!')
    	self._height = value

    @property
    def resolution(self):
    	return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
```

## Mix-In

Python 支持多重继承，Mix-In 它本质上一种简化了的、受限的、简单的多重继承。

Mix-In 思想在 Python 中实现方式就是多重继承，但需要注意一些使用限制避免使类的关系复杂。

Mix-In 类使用需要注意的限制：

1）Mix-In 类功能需要单一，若要实现多个功能就需要创建多个 Mix-In 类

2）其次 Mix-In 类不依赖子类的实现，不能继承除了 Mix-In 以外的类

3）不单独生成使用实例（理解为一个抽象类）

Mix-In 的类状图为一棵倒立的树型图。

```python
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
```

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
