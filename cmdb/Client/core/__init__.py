# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 上午11:08
# @Author  : Sulong
# @File    : __init__.py.py
# @Software: PyCharm

import json
import time
import urllib.parse
import urllib.request

from conf import settings
from core import info_collection


class ArgvHandler(object):
	def __init__(self, args):
		self.args = args
		self.parse_args()

	def parse_args(self):
		"""
		分析参数，如果有参数指定的功能，则执行该功能，如果没有，打印帮助说明

		:return:
		"""
		if len(self.args) > 1 and hasattr(self, self.args[1]):
			func = getattr(self, self.args[1])
			func()
		else:
			self.help_msg()

	@staticmethod
	def help_msg():
		"""
		帮助说明
		:return:
		"""
		msg = '''
		collect_data		收集硬件信息
		report_data			收集硬件信息并汇报
		'''
		print(msg)

	@staticmethod
	def collect_data():
		'''
		收集硬件信息 用于测试

		:return:
		'''
		info = info_collection.InfoCollection()
		asset_data = info.collect()
		print(asset_data)

	@staticmethod
	def report_data():
		'''
		收集硬件信息 发送至服务器
		:return:
		'''

		# 收集信息
		info = info_collection.InfoCollection()
		asset_data = info.collect()
		# 将数据打包到字典 转为json
		data = {"asset_data": json.dumps(asset_data)}
		# 根据settings 配置 构造URL
		url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
		print('正在将数据发送至：%s .....' % url)

		try:
			data_encode = urllib.parse.urlencode(data).encode()
			response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
			print("\033[31;1m发送完毕! \033[0m ")
			message = response.read().decode()
			print("返回结果： %s" % message)
		except Exception  as e :
			message = "发送失败"
			print("\033[31;1m发送失败，%s\033[0m" % e)
		with open(settings.PATH, 'ab') as f :
			string = '发送时间：%s \t 服务器地址：%s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), url, message)