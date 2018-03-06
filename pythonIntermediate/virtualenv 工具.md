## virtualenv 工具

virtualenv: A tool for creating isolated 'virtual' python environments. [Github](https://github.com/pypa/virtualenv)

使用 virtualenv 工具可以为每个应用创建一个独立的 Python 运行环境(虚拟)。

Python3 环境下安装 virtualenv 工具：

```
# 安装 virtualenv
pip3 install virtualenv  

# 创建一个独立的 Python 虚拟运行环境 venv
virtualenv --no-site-packages venv

# 进入一个虚拟运行环境，然后就可以在这个虚拟环境安装各种第三方包
source venv/bin/activate

# 退出当前虚拟环境
deactivate
```
