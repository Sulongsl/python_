# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 下午2:41
# @Author  : Sulong
# @File    : demo_05.py
# @Software: PyCharm

import os,sys

'''
os 模块与 sys模块

'''
print(os.access('a', mode=os.F_LOCK))
print(os.access('a', os.R_OK))  # 是否可读
print(os.access('a', os.F_OK))  # 是否存在
print(os.access('/python/test.py', os.X_OK))  # 是否可执行
print(os.access('a',os.X_OK)) #是否可执行

print(os.getcwd())
print(os.name)
os.listdir('.')

print('脚本:{}'.format(sys.argv[0])) # 获取自身文件名称
print(sys.argv)
print(sys.modules.keys()) # 返回所有已经导入的模块列表
print(sys.exc_info())
print(sys.path) #模块的搜索路径，初始化时使用PYTHONPATH环境变量的值

print('*****'*30)
'''
 sys.stdout标准输出
 sys.stdin标准输入
'''
f = open('log.text','a') # 打开一个文件
__conseole__ = sys.stdout ## 备份
sys.stdout = f #指定标准输出到文件
# print('hello333')
# sys.stdout = __conseole__# 将标准输出改为模式的console命令行模式
# print('hello2') #输出将会在console命令行下

name = sys.stdin.readline()
print('输出：',name)
print('*****'*30)
print(open('log.text','r'))