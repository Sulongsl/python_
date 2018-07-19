# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午7:58
# @Author  : Sulong
# @File    : channel_drugstore.py
# @Software: PyCharm
import xlrd
import pymongo
import time


def link_db(x):
	if x == "test":
		conn = pymongo.MongoClient('10.162.201.58', 3717)
		db = conn.zlydata
		db.authenticate("opadmin", "opadmin_2016")
		return db
	if x == "official":
		conn = pymongo.MongoClient('10.162.201.58', 3728)
		db = conn.zlydata
		db.authenticate("opadmin", "MLN8v22BXG9YOCq7")
		return db


def excel_table_byname(file='file.xlsx', colnameindex=0, by_name='sheet1'):
	data = xlrd.open_workbook(file)
	table = data.sheet_by_name(by_name)
	colnames = table.row_values(colnameindex)
	list = []
	for i in range(1, table.nrows):
		row = table.row_values(i)
		if row:
			d = {}
			for i in range(len(colnames)):
				d[colnames[i]] = row[i]
			list.append(d)
	return list


def insert(data):
	test_mongo = link_db('test')
	official_mongo = link_db('official')
	insert_mongo = test_mongo.channelDrugstore
	id = insert_mongo.insert(data)
	print(id)


def init():
	values = {}
	test_mongo = link_db('test')
	official_mongo = link_db('official')
	mongouser = test_mongo.users
	# r = initredis()
	table = excel_table_byname(file='channel_d.xlsx', by_name='sheet1')
	for row in table:
		values['drugstore_name'] = str(row['门店名称'])
		values['channel_code'] = int(row['渠道码'])
		values['channel'] = str(row['渠道名称'])
		# print(values['channel_code'])
		channel_id = find_channel_id(values['channel_code'])
		data = {}
		data['channelId'] = channel_id
		# print(type(data['channelId']))
		data['channelName'] = str(values['channel'])
		data['drugStoreName'] = str(values['drugstore_name'])
		data['channelCode'] = int(values['channel_code'])
		data['isDelted'] = False
		data['createdAt'] = time.time() * 1000
		data['updatedAt'] = time.time() * 1000
		insert(data)
	# # print(channel_id)
	# for (key, value) in data.items():
	# 	insert(data)
	# print(key, value)
	# print(type(data['channelId']))


def find_channel_id(channel_code):
	official_mongo = link_db('official')
	mongo_channel = official_mongo.tagCode
	channel = mongo_channel.find_one({'code': channel_code}, {'_id': True})
	return channel['_id']


if __name__ == "__main__":
	init()
