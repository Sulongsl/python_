# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 上午10:59
# @Author  : Sulong
# @File    : demo_04.py
# @Software: PyCharm

import json
import sys
a = "帅哥"
print(type(a)) #<class 'str'>
print(json.dumps(a)) #"\u5e05\u54e5"

b = a.encode('utf8') # 编码(encode)
print(type(b)) #<class 'bytes'>
print(b) #b'\xe5\xb8\x85\xe5\x93\xa5'

c = b.decode('utf8') # 解码(decode)
print(type(c)) #<class 'str'>
print(c)#帅哥
print(json.dumps(c)) #"\u5e05\u54e5"

print(sys.getdefaultencoding())