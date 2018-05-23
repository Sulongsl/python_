from django.shortcuts import render
from django.http import HttpResponse


# from django.shortcuts import render
# Create your views here.
def add(request):
	a = request.GET.get('a', 0)
	b = request.GET.get('b', 0)
	c = int(a) + int(b)
	return HttpResponse(str(c))


def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))


def index(request):
	# 这里的rnder是渲染模板
	return render(request, 'home.html')

def home_spring(request):
	spring  =u"我在自强学堂学习Django，用它来建网站"
	return render(request,'home_spring.html',{'string':spring})
