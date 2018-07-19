# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 上午11:36
# @Author  : Sulong
# @File    : client.py
# @Software: PyCharm
import sys
from celery import Celery

app = Celery()

app.config_from_object('celeryconfig')
app.send_task("tasks.say",[sys.argv[1],sys.argv[2]])
