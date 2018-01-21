## Python 入门

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
* sets（集合）
* dictionary（字典）

### number（数字）

用于存储数值。

内置函数type(), 用以查询变量的类型。

1.变量为什么不需要声明类型？

2.变量怎么回收？

### string（字符串）

关键字 str

```python
#!/usr/bin/env python3

str1 = 'Hello'

print(str1[0])
```
字符串也是一种特殊的元组。不能改变字符串中的某个元素的值。

### list (列表)

关键字 list

```python
#!/usr/bin/env python3

list1 = [True, 1, 'Hello']

print(list1)
```
* list 的数据项可以不同类型
* list 的各个元素可以改变
* list 是使用 [ ] 方括号包含各个数据项

### tuple (元组)

关键字 tuple

```python
#!/usr/bin/env python3

tuple1 = (True, 1, 'Hello')

print(tuple1)
```
* tuple 是使用 ( ) 小括号包含各个数据项
* tuple 与 list 的唯一区别是 tuple 的元素是不能修改，而 list 的元素可以修改。

### dictionary（字典）

关键字 dict

* 字典的每个元素是键值对，元素没有顺序
* 字典是可变容器模型，且可存储任意类型对象
* 字典可以通过键来引用，键必须是唯一的，但值则不必
* 字典是使用 { } 花括号包含键值对

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
