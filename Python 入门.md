## Python 入门

python 一切皆对象。

## 运行

shell 终端，设置环境变量

$ PATH=$PATH:/usr/local/python3/bin/python3
$ python3 --version

* 命令行方式：在 Linux 终端，输入 python 或 ipython 进入
* 程序方式：例如写一个 hello.py 文件，执行 `python hello.py`
* 脚本方式：修改文件为可执行文件，`python +x hello.py`；然后执行 `./hello.py`

```python
#!/usr/bin/env python3

print('Hello, World!')
```

## 数据类型

Python3 中有六个标准的数据类型：

* number（数字）
* string（字符串）
* list（列表）
* tuple（元组）
* set（集合）
* dictionary（字典）

### number（数字）

* int, float, bool, complex 四种基本类型，用于存储数值
* 内置函数 type(), 用以查询变量的类型

1.变量为什么不需要声明类型？

2.变量怎么回收？

3.内置函数 type() 与 isinstance() 区别

type() 不会认为子类是一种父类类型，isinstance() 认为子类是一种父类类型。

```python
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
type(A()) == A      # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
```

### string（字符串）

```python
#!/usr/bin/env python3

str1 = 'Hello'

print(str1[0])
```
* 字符串需要用单引号 ' ' 或双引号 " " 括起来
* 字符串也是一种特殊的元组。不能改变字符串中的某个元素的值

### list (列表)

```python
#!/usr/bin/env python3

list1 = [True, 1, 'Hello']

print(list1)
```
* list 的数据项可以不同类型
* list 的各个元素可以改变
* list 是使用 [ ] 方括号包含各个数据项

### tuple (元组)

```python
#!/usr/bin/env python3

tuple1 = (True, 1, 'Hello')

print(tuple1)
```
* tuple 是使用 ( ) 小括号包含各个数据项
* tuple 与 list 的唯一区别是 tuple 的元素是不能修改，而 list 的元素可以修改

### set（集合）

类似 C++ STL unordered_set

* set 是一个无序不重复元素的序列
* 使用大括号 { } 或者 set() 函数创建集合
* 用 set() 创建一个空集合
* 使用 set 可以去重

```python
#!/usr/bin/env python3

set1 = {'me', 'you', 'she', 'me'}

print(set1)
```
1.怎么理解 tuple, list 是有序的序列，而 set 是无序的序列

tuple 或 list 的定义元素顺序和输出一样，而 set 不是。

### dictionary（字典）

类似 C++ STL hash_map

* 字典的每个元素是键值对，无序的对象集合
* 字典是可变容器模型，且可存储任意类型对象
* 字典可以通过键来引用，键必须是唯一的，但值则不必
* 字典是使用 { } 大括号包含键值对
* 创建空字典使用 { }

```python
#!/usr/bin/env python3

dict1 = {'name': 'steve', 'age': 18}

print(dict1)
```

## 运算符

1.返回 True 和 False 的问题？

数字 0 是 False，其他都是 True。

字符 "" 是 False，其他都是 True。

2.is 和 == 区别？

`is` 用于判断两个变量引用对象是否为同一个， `==` 用于判断引用变量的值是否相等。

判断两个标识符是否引用同一个对象：is, is not

3.逻辑运算符

and, or, not

4.成员运算符

判断是否在指定的序列：in, not in

## 条件控制

```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
python 中没有 `switch ... case` 语句。

## 循环

for 循环

```python
for 元素 in 序列: 
    statement
```

for 循环使用 else 语句

```python
# 如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行。
for 元素 in 序列: 
    statement
else:
    statement
```

while 循环

```python
while 条件:
    statement
```

while 循环使用 else 语句

```python
# 如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
while 条件:
    statement
else:
    statement
```

中断循环：break 或 continue，与 C/C++ 功能一样。

pass 语句：空语句，不做任何事情，保证程序结构完整性，防止语法错误。

python 没有 do...while 循环。

## 函数

```python
def 函数名(参数列表):
    函数体
```

* 不可变对象：string，number，tuple
* 可变对象：list，dict
* 不定长参数：加了星号（*）的变量名会存放所有未命名的变量参数
* 使用 lambda 来创建匿名函数
* 默认参数必须放到最后

```python
sum = lambda arg1, arg2: arg1 + arg2

print(sum(10, 20))
```

变量的作用域：

* L （Local） 局部作用域
* E （Enclosing） 闭包函数外的函数中
* G （Global） 全局作用域
* B （Built-in） 内建作用域

以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

当内部作用域想修改外部作用域的变量时，就要用到 global 关键字。

要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字。

```python
#!/usr/bin/env python3

def who(name):
    print(name)

who(name = 'steve')
```
