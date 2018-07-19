# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 下午7:11
# @Author  : Sulong
# @File    : demo_03.py
# @Software: PyCharm

m = 'girl'
def aa():
	m = 'boy'
	return m


b =100
def bb():
	b =200
	x = b +100
	return x


def cc():
	bar = 100
	def dd():
		print(bar)
	dd()
	print(bar)


def ee():
	bar = [100]
	def ff():
		print(bar) # 编译器报错 不可变
		bar[0] = 200
		print(bar)
	ff()
ee()