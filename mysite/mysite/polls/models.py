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


'''
 一.模型与字段
'''
# 每次对模型进行 增删改 修改操作时  必须执行 python3 manage.py migrate 应用至数据库
# 也可以先执行python3 manage.py makemigrations 让修改操作记录至文件中 随后执行 应用到数据库
class Person(models.Model):  # 生成表 polls_person   自动生成自增主键 id

	person_name = models.CharField(max_length=40)  # 字段  避免冲突
	person_age = models.IntegerField()
	create_date = models.DateField()

	def __str__(self):
		return self.person_name

class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Person)

	def __str__(self):
		return self.name



'''
1.在settings文件中，配置MEDIA_ROOT，作为你上传文件在服务器中的基本路径（为了性能考虑，这些文件不会被储存在数据库中）。
  再配置个MEDIA_URL，作为公用URL，指向上传文件的基本路径。
  
2.添加FileField或者ImageField字段到你的模型中，定义好upload_to参数，文件最终会放在MEDIA_ROOT目录的“upload_to”子目录中。

3.所有真正被保存在数据库中的，只是指向你上传文件路径的字符串而已。可以通过url属性，在Django的模板中方便的访问这些文件。
  例如，假设你有一个ImageField字段，名叫mug_shot，那么在Django模板的HTML文件中，可以使用 {{ object.mug_shot.url }} 来获取该文件。其中的object用你具体的对象名称代替。
4.可以通过name和size属性，获取文件的名称和大小信息。

'''
class FileClass(models.Model):  # 上传文件字段
	file = models.FileField(upload_to='uploads/')  # 文件被传至`MEDIA_ROOT/uploads`目录，MEDIA_ROOT由你在settings文件中设置
	# 或者    被传到`MEDIA_ROOT/uploads/2015/01/30`目录，增加了一个时间划分
	file_date = models.FileField(upload_to='uploads/%Y/%m/%d') # django 自动实现

class ImageClass(models.Model): # 上传图片字段
	'''
	ImageField 用法与FileField 用法相似 多了两个参数 ：height_field(保存有图片高度信息的模型字段名) width_field(保存有图片宽度信息的模型字段名)
	'''
	image = models.ImageField(upload_to='images/',width_field='None',height_field='None')

'''
path：必须指定的参数。表示一个系统绝对路径。

match:可选参数，一个正则表达式，用于过滤文件名。只匹配基本文件名，不匹配路径。例如foo.*\.txt$，只匹配文件名foo23.txt，不匹配bar.txt与foo23.png。

recursive:可选参数，只能是True或者False。默认为False。决定是否包含子目录，也就是是否递归的意思。

allow_files:可选参数，只能是True或者False。默认为True。决定是否应该将文件名包括在内。它和allow_folders其中，必须有一个为True。

allow_folders： 可选参数，只能是True或者False。默认为False。决定是否应该将目录名包括在内。
'''
class FilePathClass(models.Model):  #  默认情况只匹配文件名
	file_path = models.FilePathField(path='/home/images',match="foo.*",recursive=True)

'''
二.关系型字段
'''
# 多对一类型外键（ForeignKey）
class Car(models.Model):
	maunfacturer = models.ForeignKey('Manufacturer',on_delete=models.CASCADE,) # 这个字段 指向了一个生产厂家 也可以指向另一个APP的对象 APP_name.对象
	car_name = models.CharField(max_length=44)

class Manufacturer(models.Model):
	pass

class Comment(models.Model): # 一个评论模型
	title = models.CharField(max_length=66)
	text = models.TextField()
	parent_comment = models.ForeignKey('self',on_delete=models.CASCADE) # 定义了一个外键 一个评论下可以有多条评论

# 多对多类型外键（ManyToManyField）
'''
在数据库后台，Django实际上会额外创建一张用于体现多对多关系的中间表。
默认情况下，该表的名称是“多对多字段名+关联对象模型名+一个独一无二的哈希码”，例如‘author_books_9cdf4’
'''
class Channel(models.Model):
	channel_1 = models.ManyToManyField('Car')
	channel_2 = models.ManyToManyField('Manufacturer')

from django.conf import settings
# 一对一类型外键（OneToOneField）
# 这个一对一类型外键 可以理解为对其他模型以构建功能的继承
class MySpecialSser(models.Model):  # 两个字段都使用一对一关联到了Django内置的auth模块中的User模型
	user_name = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	supervisor = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='supervisor_of')


'''
三.字段的参数 
'''
'''
1.null
	该参数为True时 django在数据库用NULL保存空值 默认为False 
	
2.blank
	True 时 该字段可以为空 默认False 与 null参数的区别在于 null是纯数据库层面的 而  blank是用于表单验证是否可以为空的 与数据库无关 
	
3.choices
	用于页面上的选择框标签 一个二维的二元元组 第一个元素表示数据库内的真实字段，第二个元素表示页面上显示的具体内容 
	EG = （
	（'表1字段FR','选择FR'）,
	（'表1字段GT','选择GT'）,
	（'表1字段SO','选择SO'）,
	）
	一般来说 最好将选项定义在类中  也就是说将数据库中表的字段 给一个全局变量
	
4.db_column 
	定义当前字段在数据表内的列名 
	
5.db_index 
	接收布尔值 True则在数据库中创建索引
	
6.db_tablespace 
	用于 字段索引的数据库表空间的名字，前提是这个当前字段设置了索引 
	
7.default
	字段的默认值 （ 可以是值 也可以指定一个对象）
	
8。error_messages
	自定义错误信息 参数接受字典类型的值 
					字典的键可以是null、 blank、 invalid、 invalid_choice、 unique和unique_for_date其中的一个
					
9.primarg_key
	用于设置主键字段
	如果你没有给模型的任何字段设置这个参数为True，Django将自动创建一个AutoField自增字段，名为‘id’，并设置为主键
	给字段设置了此值 django则将该字段变为主键
	
10.unique
	设为True时，在整个数据表内该字段的数据不可重复。
	注： 对manyToManyField 和OneToOneField类型的值无效

11. unique_for_date
	日期唯一
	
12.umique_for_month
	月份唯一

13.unique_for_year
	年份唯一

14.verbose_name
	 为字段设置一个人类 可读 

15.validators
	运行在该字段上的验证器的列表
	
'''
