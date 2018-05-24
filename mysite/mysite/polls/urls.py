# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午3:07
# @Author  : Sulong
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from polls import views

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/1/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]