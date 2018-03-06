## `if __name__ == '__main__': `原理

Python 中一个 .py 文件就是一个模块。经常在 .py 文件中看到 `if __name__ == '__main__': ` 这行，那它到底起什么作用？

这行其实就是一个 if 判断语句，只有特殊变量 `__name__` 等于 `__main__`，才会执行下面 test()。

```python
if __name__=='__main__':
    test()
```

那什么时候其特殊变量 `__name__` 等于 `__main__`，当直接以脚本方式执行 .py 文件，如下面 test.py 文件，
命令行运行 `python test.py`。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    print('The test()')

print(__name__) # 打印 __main__

if __name__ == '__main__':
    test() # 会执行
```

如果不是直接执行 test.py，而是把 test.py 作为模块，被其他文件(模块)调用，这样会发生什么？

新建一个 A.py，导入 test 模块，如下：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import test
```
命令行运行 `python A.py`，会发现 `__name__` 为 test，不等于 `__main__`，所以 test() 不执行。

### 总结

* 直接执行脚本，此时 `__name__` 等于 `__main__`
* 被其他文件(模块)调用，则 `__name__` 等于该文件的模块名
