# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 上午10:35
# @Author  : Sulong
# @File    : send_mail.py
# @Software: PyCharm

import os
from django.core.mail import send_mail

# 通过os模块 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
        'sulong_@sohu.com',
        ['767244811@qq.com'],
    )