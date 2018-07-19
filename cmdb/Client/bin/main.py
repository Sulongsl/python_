# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 上午11:09
# @Author  : Sulong
# @File    : main.py
# @Software: PyCharm

import os
import sys

'''客户端启动脚本目录'''

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录 使得包和模块能够正常引入
sys.path.append(BASE_DIR) # 将当前客户端所在目录设置为工作目录，如果不这么做，会无法导入其它模块；

from core import handler

if __name__ == "__main__":
	handler.ArgvHandler(sys.argv)
