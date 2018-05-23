from django.db import models


# Create your models here.

class UserInfo(models.Model):# 继承
	user = models.CharField(max_length=32)  # 创建字段
	pwd = models.CharField(max_length=32)
