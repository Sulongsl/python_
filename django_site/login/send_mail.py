# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 上午10:35
# @Author  : Sulong
# @File    : send_mail.py
# @Software: PyCharm

import os
import datetime
from django.core.mail import send_mail

# 通过os模块 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


def ye(n):
	while True:
		n = yield n  # yield  与 赋值语句 优先运行 yield
		print(str(n) + '*****')

def say_hello(x):
	print('hello %s' %str(x))



if __name__ == '__main__':
	say_hello(222)


# g = ye(1) # g是一个生成器对象
# print(next(g)) # 第一次调用 返回n 但是 并没有对n赋值
# print(next(g)) # 第二次调用

# send_mail(
#     '来自www.liujiangblog.com的测试邮件',
#     '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
#     'sulong_@sohu.com',
#     ['767244811@qq.com'],
# )
