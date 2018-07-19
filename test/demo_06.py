# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 下午3:50
# @Author  : Sulong
# @File    : demo_06.py
# @Software: PyCharm

class A(object):
	@staticmethod #返回函数的静态方法
	def f(*args):
		print(args)

A.f("A")
