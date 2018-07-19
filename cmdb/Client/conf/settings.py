# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 上午10:39
# @Author  : Sulong
# @File    : settings.py
# 配置了服务器地址、端口、发送的url、请求的超时时间，以及日志文件路径
# @Software: PyCharm
import os

# 远端服务器配置

Params = {
	"server": "192.168.1.100",
	"port":8000,
	'url':'/assers/report/',
	'request_timeout':30,
}

#日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'codb.log')

