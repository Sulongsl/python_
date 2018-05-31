from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import datetime
# Create your views here.

def current_datetime(request): # 返回时间页面
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def my_view(request):
	return HttpResponse(status=201)

