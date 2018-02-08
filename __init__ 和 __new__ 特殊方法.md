## __init__ 和 __new__ 特殊方法

__new__ 特殊方法是在类创建的时候调用，第一个参数是 cls，用来控制类的创建行为，属于类级别，最先调用。

__init__ 特殊方法是类实例化过程中，进行初始化属性，属于实例级别。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
    def __new__(cls, name, age):
        print('__new__ called')
        return super(Person, cls).__new__(cls)
    def __init__(self, name, age):
        print('__init__ called')
        self.name = name
        self.age = age 
    def __str__(self):
        return '<Person: %s(%s)>' %(self.name, self.age)

if __name__ == '__main__':
    p = Person('CC', 20) 
    print(p
```

