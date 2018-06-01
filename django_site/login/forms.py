# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 上午10:17
# @Author  : Sulong
# @File    : from.py
# @Software: PyCharm

from django import forms
from captcha.fields import CaptchaField

'''
重构数据 用于 页面渲染
为数据创建HTML表单元素
接受处理用户从表单发送过来的数据

'''


class UserForm(forms.Form):  # 所有的表单类都要继承forms.Form类  用于登录页面
	username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
		attrs={'class': "form-control"}))  # 表单的CharField对应的是HTML中<form> 的一个 inout元素
	password = forms.CharField(label="密码", max_length=256, widget=forms.TextInput(attrs={'class': "form-control"}))

	# widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
	captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):  # 用于注册页面
	gender = (
		('male', "男"),
		('female', "女"),
	)
	username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label="确认密码", max_length=256,
								widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
	sex = forms.ChoiceField(label='性别', choices=gender) # 下拉框
	captcha = CaptchaField(label='验证码')
