"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views
from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views as views_cmdb

'''
　　路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。
'''
'''url()方法
    regex 和 view     必填参数  
    kwargs 和 name    选填参数
    1、regex  正则表达式 
        用来匹配 网址URL.用户拿着请求网址 在urlpatterns列表中按顺序进行匹配  
        一旦匹配成功 立即执行 该条目所映射的函数和视图 在其后的条目将不会进行匹配 编写顺序很重要，正则也很重要。
        regex不会去匹配GET或POST参数或域名
        
    2.view url请求的视图地址
    	
    	
    3.kwarg  参数
    	任意数量的关键字参数可以作为一个字典传递给目标视图
    
    4.name 
    	对URL进行命名 可以在django的任意处使用（模板内显式地引用它）
'''

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^pollsdetail', views.detail, name='detail'),
	# # ex: /polls/5/results/
	url(r'^pollsresults', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^pollsvote', views.vote, name='vote'),

	url(r'^polls/', include('polls.urls')),  # include语法相当于多级路由
	url(r'^admin/', admin.site.urls),
	url(r'^demo/', views_cmdb.demo_1),
	url(r'index/', views.index)
	# path('admin/', admin.site.urls),
]

