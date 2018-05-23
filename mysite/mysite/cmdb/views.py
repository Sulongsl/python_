from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

'''
index这个url指向了views里的index（）函数，它接收用户请求，并返回一个“hello world”字符串
'''

user_list = [{"user": "Jack", "pwd": "abc"}, {"user": "Tom", "pwd": "ABC"}, ]


def index_1(request):  # request 参数封装了 用户请求的序偶有内容 类似于self 必填
	return render(request, "index.html")  # 第一个参数固定 第二个指定文件


# return HttpResponse("你得非常使劲，才能看起来生活的毫不费劲")  # 返回的 字符创 不许被HttpResponse封装 django要求

def index(request):
	if request.method == "POST":
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		print(username, password)
		models.UserInfo.objects.create(user=username, pwd=password)
		user_list = models.UserInfo.objects.all()
	# temp = {"user":username,"pwd":password}
	# user_list.append(temp)
	return render(request, "index.html", {"data": user_list})
