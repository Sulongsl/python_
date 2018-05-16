# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 下午4:55
# @Author  : Sulong
# @File    : baidu.py
# @Software: PyCharm

'''
百度语音识别SDK
'''
from aip import AipSpeech
import wave
import webbrowser
import pyaudio
import sys

# 定义常量
APP_ID = '11192724'
API_KEY = '81mEtVQ3bk1Py23Y1M6O86mk'
SECRET_KEY = '8LQN6SWiTnTuewvj6tKn8w8cvlgxyFCk'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

'''
录音生成
'''


def record_wave():
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	print("* recording")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()


'''
解析语音
'''


def browser_open_text(text):
	str = (text[0])[:-1]
	print(str)
	if str is None:
		return
	elif '打开百度' == str:
		webbrowser.open_new_tab("https://www.baidu.com/")
	elif '知乎' == str:
		webbrowser.open_new_tab("https://www.baidu.com/")
	elif '百度' == str:
		webbrowser.open_new_tab("https://www.baidu.com/")
	else:
		webbrowser.open_new_tab("doubiiot.cn")


def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


if __name__ == '__main__':
	# record_wave()
	res = aipSpeech.asr(get_file_content("output.wav"), 'wav', 8000, {'lan': 'zh', })
	# 翔哥方法实现循环 即 听完后 回答一句话 打开操作or 再说一次 / 关闭程序 打开程序
	while res['err_no'] != 0:
		print("Please speak again")
		record_wave()
	if 'result' in res:
		text = res['result']
		browser_open_text(text)
