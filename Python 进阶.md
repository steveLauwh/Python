# Python 进阶

## 面向对象

Python 与 Java/C++ 一样，都可以进行面向对象编程(OOP)。

class(类)、object(对象)、attribute(属性)、method(方法)、inheritance(继承)、override(重写)

类的私有属性：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问，可以在类内部的方法中使用。

类的私有方法：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。

定义一个类，使用 class，在类中定义方法，参数必须有 self，通过 self 调用类的属性。

特殊方法：__init__()，创建对象会自动调用；类似构造函数概念。

运算符也是特殊方法，可以进行重载。

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

## 模块

## 错误异常处理


