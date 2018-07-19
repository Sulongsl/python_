# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 下午6:24
# @Author  : Sulong
# @File    : tasks.py
# @Software: PyCharm

from celery import Celery
import pymongo
import time

import time
from celery import Celery

# broker = 'redis://127.0.0.1:6379'  # 指定生产者
# backend = 'redis://127.0.0.1:6379/0' # 指定消费者
#
# app = Celery('my_task', broker=broker, backend=backend)
#
# @app.task # 当函数被 @app.task 装饰后，就成为可被 Celery 调度的任务；
# def add(x, y): # 这是主函数 被任务调度的一个任务
#     time.sleep(5)     # 模拟耗时操作
#     return x + y

app = Celery('tasks',broker='mongo://guest@localhost//')

def say(x,y):
	time.sleep(3)
	return x+y

if __name__ == '__main__':
	say("hello","world")