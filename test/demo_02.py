# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 下午5:07
# @Author  : Sulong
# @File    : demo_02.py
# @Software: PyCharm


def demo_01():
	count = 0
	name_pass = {'user1': '123', 'user2': '456', 'user3': '789'}
	for i in range(10):
		name_input = input('请输入用户名：')
		if name_input in name_pass.keys():
			passwd_input = input('请输入密码：')
			if passwd_input == name_pass[name_input]:
				print('登陆成功')
				break
			else:
				if count > 1:
					print('3次输入错误，您的账号已被注销')
					exit()
				print('{}用户名不存在或密码错误，请重新输入'.format(name_input))
				count += 1
		else:
			print('{}用户不存在'.format(name_input))
			continue


def demo_02():
	shop_list = [
		['iphone7', 6500],
		['iphone6', 4500],
		['金立s10', 3400],
		['华为r79', 2888],
		['魅族NOTE5', 1888],
		['opppR9', 3600],
	]

	money = eval(input('请输入你的欲购金额：'))
	shop_out = []  # 购物车列表
	all_kaixiao = 0 # 总金额
	while True:
		print('++++++++商品清单+++++++++')
		for num, i in enumerate(shop_list, 1): # enumerate(sequence,[start=0])讲一个可遍历的数据对象，如列表，元组或字符串 组合为一个索引序列 sequence -- 一个序列、迭代器或其他支持迭代对象。start下标起始位置
			if isinstance(i, list):# isinstance 判定对象是否属于一个已知的数据类型类似 type()。
				shop_li = i[0] + "\t" + str(i[1])
				print(num, shop_li)
			else:
				print(i)
		print('q:退出\np:打印清单')
		shop_name = input('请输入要购买的商品编号')
		shop_name = str(shop_name)

		if shop_name == 'q':
			exit()
		elif shop_name == 'p':  # 打印购物明细
			print('------购物明细-----')
			for number, i in enumerate(shop_out, 1):
				if isinstance(i, list):
					hehe = i[0] + ":" + str(i[1])
					print(number, hehe)
				else:
					print(number)
			print('---总金额---:%s---' % (all_kaixiao))
			continue  # 跳出循环 否则会输出非法信息
		if shop_name.isdigit() == 1:
			shop_name = int(shop_name)
		else:
			print("您的输入非法，请重新新输入")
			continue
		num1 = int(len(shop_list))
		if shop_name not in range(1, num1 + 1):
			print('输入有误，请重新输入')
			continue
		else:
			price = int(shop_list[shop_name - 1][1])  # 商品单价
			if money < price:
				print('您的余额不足，无法购买')
				continue
			money = money - price  # 剩余金额
			out = shop_list[shop_name - 1][:]  # 购买商品信息
			shop_out.append(out[:])  # 加入购物车
			all_kaixiao += price
			print("您购买的商品时：{} 单价：{}圆".format(*out))
			print("您还可以消费：{}".format(money))


if __name__ == "__main__":
	demo_02()
	# str_list = ['1', '2', '3']
	# for num, str_value in enumerate(str_list, 1):
	# 	print(num, str_value)
