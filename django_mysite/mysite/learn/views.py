# coding:utf-8
from django.shortcuts import render
# 引入HttpResponse 用来向网页返回内容 把内容显示到网页上
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse(u'pythoin欢迎回归雨天的暖被窝!!!!')