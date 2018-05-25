# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 下午7:00
# @Author  : Sulong
# @File    : test.py
# @Software: PyCharm
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionMethodTests(TestCase):
	# 保证无论发布时间是在过去、现在还是未来Question.was_published_recently()都将返回正确的结果。
	"""
	在将来发布的问卷应该返回False

	"""

	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		'''
		只要是超过1天的问卷，即返回False
		'''
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		'''
		最近一天内的问卷，返回True
		'''
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)
