from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)  # 添加polls应用
admin.site.register(Choice)
