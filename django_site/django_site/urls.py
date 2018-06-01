"""django_site URL Configuration

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
from django.conf.urls import url
from login import views
from django.conf.urls import include

'''
URL设计
/index/     login/views.index()     index.html      主页

/login/     login.views.login()     login.html      登录

/register/  login.views.register()  register.html   注册
    
/logout/    login.views.logout()    无需专门页面      登出

'''

urlpatterns = [
    path('', views.leesang),  # new

    # path('admin/', admin.site.urls),
    url(r'^admin/',admin.site.urls),
    url(r'^index/',views.index),
    url(r'^login/',views.login),
    url(r'register/',views.register),
    url(r'^logout',views.logout),
    url(r'^captcha', include('captcha.urls'))  # 增加这一行

]
