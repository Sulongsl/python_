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
'''
四.模型中的元数据 Meta
	在模型中除了字段外的内容 如 排序方式，数据库表名等

	参数
	1.ordering
		排序依据
	2.abstract
		如果abstract=True，那么模型会被认为是一个抽象模型;  抽象模型本身不实际生成数据表 而是作为其他模型的父类 被继承使用
	3.app_label
		如果定义了模型的app 而没有在APP列表中注册 则必须通过这个元选项 声明 这个模型是哪个APP
		
	4.base_manager_name
		自定义模型的——base_manager管理器的名字 
		
	5.db_table
		指定在数据库中 指定当前模型 生成的数据表的表明
		
	6.db_tablespace
		自动义数据库表空间的名字（数据库名？不确定）
		
	7.default_manager_name
		自定义模型_default_manager 管理器的名字
		
	8.default_related_name
		自定义反向关系名 影响方向查询关系名
		
	9.get_latest_by
		指定一个模型的字段 作为lastest() 和earliest()方法的排序依据 从而得出 最近一个或 最前的一个对象
		get_latest_by = '字段A'
	10.managed
		默认值为True 表示Django将按照既定的规则 管理数据库表的生命周期
		如果设置为False，将不会针对当前模型创建和删除数据库表。在某些场景下，这可能有用，但更多时候，你可以忘记该选项。
		
	11.ordering
		接受一个字段名组成的元组或列表 设置排序 字段名前加 '-' 则降序 
	
	12.permissions
		创建对象时增加额外的权限 接收一个所以元素都是二元元祖的列表 或 元组 每个元素都是（权限代码，直观点的权限名称）
	
	13.default_permissions
		Django默认给所有的模型设置('add', 'change', 'delete')的权限，也就是增删改。
		可以自定义这个选项，比如设置为一个空列表，表示你不需要默认的权限，但是这一操作必须在执行migrate命令之前。
	
	14.proxy
		proxy = True，表示使用代理模式的模型继承方式
		
	15.indexes
		接受一个应用在当前模型上的索引列表
		indexes = [
		models.Index(fields=['last_name','first_name']),
		models.Index(fields=['first_name',name = 'first_name_idx']),
		]
	
	16.unique_together
		联合约束
		unique_together =(('name','birth_day','address'),)  一旦三个字段都相同 则Django会拒绝创建 
		联合唯一无法作用于普通的多对多字段。
	
	17.verbose_name
		设置模型对象的直观名称 
		 verbose_name = "披萨"
	
		
'''
class Ox(models.Model):
	horn_length = models.IntegerField()

	class Meta:  # 每个模型都可以有自己的元数据类，每个元数据类也只对自己所在模型起作用。
		ordering = ["horn_length"]
		verbose_name_plural = "oxen"  # 复数名
		verbose_name = '披萨'

'''
五.模型的继承
	1.抽象继承
		被用来继承的模型称为 Abstarct base classes 将子类的共同数据抽离出来，供子类继承使用 他不会创建实际的数据表
		关键字： 在模型的Meta类中 abstract =True 即讲一个模型转换为抽象基类
		注：
			抽象基类中有的元数据，子类型没有的话，直接继承；
			
			抽象基类中有的元数据，子类型也有的化，直接覆盖；
			
			子模型可以额外添加元数据；
			
			抽象基类中 abstract = True 这个元数据不会被继承 想定义必须在子模型中重新写入
			
			有一些元数据对抽象基类无效，比如db_table，首先是抽象基类本身不会创建数据表，其次它的所有子类也不会按照这个元数据来设置表名。
		
		警惕related_name和related_query_name参数 
'''
class CommonInfo(models.Model): # 该模型是一个抽象基类 不能被创建及正常使用
	name = models.CharField(max_length=128)
	age = models.IntegerField()

	class Meta:
		abstract = True
		ordering = ['name']

class Student(CommonInfo):  #
	home_group = models.CharField(max_length=22)  # 在这里 Student实际上有三个字段 name ,age ,home_group

	class Meta:
		db_table = 'student_info'  # z子类模型扩展了父类的Meta元数据 ordering ，db_table

'''
	2.多表继承
		父类与子类都是独立自主，功能完整，可正常使用的模型，都拥有自己的数据表，内部隐含了一个一对一的关系
		在下例中 
			Restaurant将包含Place的所有字段，并且各有各的数据库表和字段，
			
			
'''
class Place(models.Model):
	name = models.CharField(max_length=22)
	address = models.CharField(max_length=88)

class Restaurant(Place):
	serves_hot_dogs = models.BooleanField(default=False)  # default 字段的默认值
	serves_pizza = models.BooleanField(default=False)
'''
	3.Meta和多表继承 
		在多表继承的情况下 弗雷模型与子类模型在数据库中都有物理存在的表 父类的Meta类会对子类造成不确定的影响
		Django关闭了 子类继承父类的Meta功能 在这一点上 与抽象继承完全不同
		
		有两个Meta元数据特殊一点，那就是ordering和get_latest_by，这两个参数是会被继承的 子类想改变就需要重写
	
	4.多表继承和反向关联
		error:Reverse query name for 'Supplier.customers' clashes with reverse query
	
	5.代理模型
		在使用多表继承 只改变模型在Python层面的行为 可以创建、删除、更新代理模型的实例，并且所有的数据都可以像使用原始模型（非代理类模型）一样被保存
		
		关键字:将Meta中proxy的值设为True
		
		注:
			代理模型必须继承自一个非抽象的基类，并且不能同时继承多个非抽象基类;
			代理模型可以同时继承任意多个抽象基类，前提是这些抽象基类没有定义任何模型字段
			代理模型可以同时继承多个别的代理模型，前提是这些代理模型继承同一个非抽象基类
			
		代理模型管理器
		
		
'''
# class OrderedPerson(Person):
# 	class Meta:
# 		# 现在，普通的Person查询是无序的，而OrderedPerson查询会按照`last_name`排序。
# 		ordering = ["last_name"]
# 		proxy = True

'''
	6.多重继承
		一般情况，能不要多重继承就不要，尽量让继承关系简单和直接，避免不必要的混乱和复杂。
		如果多个父类都含有Meta类，则只有第一个父类的会被使用，剩下的会忽略掉
'''