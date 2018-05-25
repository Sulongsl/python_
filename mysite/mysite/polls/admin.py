from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
# admin.site.register(Question)  # 添加polls应用
admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):  # 一个继承了admin.ModelAdmin 的模型管理类
	fieldsets = [  # 修改页面样式
		(None, {'fields': ['question_text']}),
		('date information', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question_text', 'pub_date', 'was_published_recently') # http://127.0.0.1:8000/admin/polls/question/ 页面中时间及是否在规定时间内的显示

	list_filter = ['pub_date']  # http://127.0.0.1:8000/admin/polls/question/ 页面中的过滤器

	search_fields = ['question_text']  # 搜索功能

'''
上述代码：Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域
'''

# fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)  # 修改让Publication date字段显示在Question字段前面了
