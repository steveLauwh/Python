# Python 进阶

## 面向对象

Python 与 Java/C++ 一样，都可以进行面向对象编程(OOP)。

* class(类)、object(对象)、attribute(属性)、method(方法)、inheritance(继承)、override(重写)、多重继承

* 类的私有属性：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问，可以在类内部的方法中使用

* 类的私有方法：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用

* 定义一个类，使用 class，在类中定义方法，参数必须有 self，通过 self 调用类的属性

* 特殊方法：`__init__()`，创建对象会自动调用；类似构造函数概念

* 运算符也是特殊方法，可以进行重载

```python
class Animal(object):
     name = 'Tiger'
     def eat(self)：
         print('I can eat!', self.name)

x = Animal()

print(x.name)

print(x.eat())
```

## 文件的输入和输出

> **键盘输入：input()**

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

## 错误异常处理


