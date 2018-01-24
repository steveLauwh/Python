# Python 高级

## 高阶函数

一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。

```python
#!/usr/bin/env python3

def add(x, y, f):
    return f(x) + f(y)

print(add(-1, 3, abs))
```



## 闭包

## 装饰器
