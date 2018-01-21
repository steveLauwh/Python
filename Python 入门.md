## Python 入门

## 运行

* 命令行方式：在 Linux 终端，输入 python 或 ipython 进入
* 程序方式：例如写一个 hello.py 文件，执行 `python hello.py`
* 脚本方式：修改文件为可执行文件，`python +x hello.py`；然后执行 `./hello.py`

```python
#!/usr/bin/env python3

print('Hello, World!')
```

## 数据类型

Python3 中有六个标准的数据类型：

* Number（数字）
* String（字符串）
* List（列表）
* Tuple（元组）
* Sets（集合）
* Dictionary（字典）

1.变量为什么不需要声明类型？

2.变量怎么回收？

## 运算符

1.返回 True 和 False 的问题？

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
while 条件:
    statement
else:
    statement
```

中断循环：break 或 continue，与 C/C++ 功能一样。

pass 语句：空语句，不做任何事情，保证程序结构完整性，防止语法错误。

## 函数
