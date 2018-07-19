# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午4:09
# @Author  : Sulong
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from assets import views

app_name = 'assets'

urlpatterns = [
	url(r'^report/', views.report, name='report'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^index/', views.index, name='index'),
	url(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^$', views.dashboard),
]
