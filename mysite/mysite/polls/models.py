from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

''' 创建数据库模型的文件
	
	django通过建立python的自定义类 来构造 数据库中的模型表 
	
	一个类对应一张表 每个类的实例即为一条数据
'''

# Question包含一个问题和一个发布日期。Choice包含两个字段：该选项的文本描述和该选项的投票数

#  两个类都是django.db.models.Model的子类  每个字段都是 Field 的实例

'''
问题类
问题内容 question_text
创建时间 pub_date
'''


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	# 自己定义的方法可以用于shell
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	# 一个判定
	# return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


'''
一个问题的回答投票 Choice
问题回复 choice_text
票数    votes
'''


class Choice(models.Model):
	questtion = models.ForeignKey(Question, on_delete=models.CASCADE)  # Django支持通用的数据关系：一对一，多对一和多对多。 定义外键
	choice_text = models.CharField(max_length=200)  # 设定了默认列名
	votes = models.IntegerField(default=0)  # 将其默认值设为0

	def __str__(self):
		return self.choice_text
