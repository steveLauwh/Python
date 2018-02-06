# Python 进阶

## 面向对象

Python 与 Java/C++ 一样，都可以进行面向对象编程(OOP)。

* class(类)、object(对象)、attribute(属性)、method(方法)、inheritance(继承)、override(重写)、多重继承、多态

* 类的私有属性：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问，可以在类内部的方法中使用

* 类的私有方法：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用

* 定义一个类，使用 class，在类中定义方法，参数必须有 self，通过 self 调用类的属性

* 特殊方法：`__init__()`，创建对象会自动调用；类似构造函数概念

* 运算符也是特殊方法，可以进行重载

* 类名通常是大写开头的单词

```python
class Animal(object):
     name = 'Tiger'
     def eat(self)：
         print('I can eat!', self.name)

x = Animal()

print(x.name)

print(x.eat())

x.age = 1  # Python 允许对实例变量绑定任何数据

print(x.age)
```

## 多态

```python
#!/usr/bin/env python3

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

# Python 不一定要继承 Animal 类型
class Xx(object):
	def run(self):
		print('Xx is running...')

# 多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())

run_twice(Cat())

run_twice(Xx())
```

著名的“开闭”原则：

对扩展开放：允许新增 Animal 子类；

对修改封闭：不需要修改依赖 Animal 类型的 run_twice() 等函数。


## 文件的输入和输出

> **键盘输入：input()**

input() 默认输入的为 str 格式。

```python
#!/usr/bin/env python3

str = input('Please input: ')

print(str)
```

> **输出：print()**

* 使用 str.format() 函数来格式化输出值
* `%` 操作符也可以实现字符串格式化
* 输出的值转成字符串 str()

```python
#!/usr/bin/env python3

name = 'steve'

print('{0} 和 {1}'.format('steve', 'Lau'))

print('who are you: %s' %name)
```

> **文件操作**

打开一个文件：open(filename, mode)

文件对象的方法：
* 读 read()
* 从文件中读取单独的一行 readline()
* 读取文件中包含的所有行 readlines()
* 将 string 写入到文件中, 然后返回写入的字符数 write()
* 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数 tell()
* 要改变文件当前的位置 seek(offset, from_what)
* 关闭文件 close()

对文件的操作，还有很多方法，直接看 Python 官方文档手册

```python
#!/usr/bin/env python3

f = open('/home/steve/test.txt', r+)

str = f.read()
print(str)

str = f.readline()
print(str)

num = f.write('Hello')
print(num)

off = f.seek(2)
print(off)

f.close()
```

## 模块

python 是胶水语言，有丰富的模块和库。

一个 .py 文件就构成一个模块。

```python
# import 语句，导入模块
import module1[, module2[,... moduleN]
```
```python
# from...import ... 语句，从模块中导入一个指定的部分到当前命名空间，也可以把模块的所有内容全都导入到当前的命名空间
from modname import name1[, name2[, ... nameN]]

from modname import *  
```

每个模块都有一个 __name__ 属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。

```python
#!/usr/bin/env python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

可以将功能相似的模块放在同一个文件夹中，构成一个模块包，包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。

如：`import filedir.module`

该文件夹下必须包含一个 `__init__.py` 的文件，说明该文件夹是一个模块包。

## 异常处理

异常处理的格式：

```python
try:
    ...
except exception1:
    ...
except exception2:
    ...
except:
    ...
else:
    ...
finally:
    ...
```
抛出指定的异常：raise 语句

```python
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print ('参数没有包含数字')

# 调用函数
temp_convert('xyz');
```

## 迭代器

迭代器含义与 C++ STL 迭代器一样，python 中迭代器有两种基本方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器。

```python
#!/usr/bin/env python3

import sys
 
list=[1, 2, 3, 4, 5]
it = iter(list)    # 创建迭代器对象

while True:
    try:
        print(next(it))  # 输出迭代器的下一个元素
    except StopIteration:
        sys.exit()
```

## generator(生成器)

使用了 yield 的函数被称为生成器(generator)。

原理：在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。并在下一次执行 next() 方法时从当前位置继续运行。

```python
#!/usr/bin/env python3
 
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```
1.什么时候需要使用 yield ？

## 表推导

表推导(list comprehension)是快速生成表的方法。

```python
L = [x**2 for x in range(10)]

print(L)
```

## 总结

> **内置函数 dir()**

dir() 用来查询一个类或者对象所有属性。如 `print dir(list)`

> **内置函数 help()**

help() 用来查询的说明文档。

> **内置函数 enumerate()**

每次循环中同时得到下标和元素。

> **内置函数 zip()**


