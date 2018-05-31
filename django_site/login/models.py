from django.db import models

# Create your models here.
'''
设计数据库模型
用户注册系统 --->  注册与登录
User表
	用户名 
	密码
	邮箱
	性别
	创建时间
	是否注销
	
'''


class User(models.Model):
	gender = (
		('male', "男"),
		('female', "女"),
	)
	name = models.CharField(max_length=128,unique=True)
	password = models.CharField(max_length=256)
	email = models.EmailField(unique=True)
	sex = models.CharField(max_length=32,choices=gender,default="男")
	c_time = models.DateTimeField(auto_now_add=True)
	is_delted = models.BooleanField(unique=False)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ["-c_time"]
		verbose_name = '用户'
		verbose_name_plural = '用户'
