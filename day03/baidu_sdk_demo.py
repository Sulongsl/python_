# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 下午6:22
# @Author  : Sulong
# @File    : baidu_sdk_demo.py
# @Software: PyCharm

from aip import AipSpeech
import wave
import webbrowser
import pyaudio
import sys
import requests

# 定义常量
APP_ID = '15809515380'
API_KEY = 'e17bbf788c16481f8bcb2d0764aecaee'
SECRET_KEY = '77056463ffab4f9bbf981470fdf2a9b0'
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


if __name__ == '__main__':
	get_file_content('output.wav')
	# 识别本地文件
	# res = aipSpeech.asr(get_file_content('output.wav'), 'wav', 8000, {
	# 	'lan': 'zh',
	# })
	res = aipSpeech.asr(get_file_content('output.wav'), 'wav', 16000, {
		'dev_pid': '1536',
	})
