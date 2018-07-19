# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 上午11:35
# @Author  : Sulong
# @File    : tasks.py
# @Software: PyCharm
import time
from celery.task import task

@task
def say(x,y):
	time.sleep(3)
	return x+y