# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 下午4:50
# @Author  : Sulong
# @File    : demo_01.py
# @Software: PyCharm

def demo_01():
	'''根据奇数和偶数生成字典元素'''
	dct1 = {}
	for i in range(20):
		if i % 2 == 1:
			if 'odd' in dct1.keys():
				dct1['odd'].append(i)
			else:
				dct1['odd'] = [i, ]
		else:
			if 'even' in dct1.keys():
				dct1['even'].append(i)
			else:
				dct1['even'] = [i, ]
	print(dct1)
if __name__ == '__main__':
	demo_01()