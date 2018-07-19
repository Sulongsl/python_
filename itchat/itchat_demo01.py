# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 下午4:51
# @Author  : Sulong
# @File    : itchat_demo01.py
# @Software: PyCharm
import os
import re
import shutil
import time
import itchat
from itchat.content import *

itchat.auto_login(hotReload=True)
itchat.send("hello word",toUserName="filehelper")