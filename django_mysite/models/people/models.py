from django.db import models

# Create your models here.
# 数据库设置操作python manage.py makemigrationspyPerson.objects.create(name="WeizhongTu", age=24)
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name