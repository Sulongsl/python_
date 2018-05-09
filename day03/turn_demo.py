# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 上午9:58
# @Author  : Sulong
# @File    : turn_demo.py
# @Software: PyCharm

import wave
import requests
import json
import pyaudio
import sys
import webbrowser
# reload(sys)
# sys.setdefaultencoding("utf-8")

# aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


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


def get_token():
	apiKey = "Ll0c53MSac6GBOtpg22ZSGAU"
	secretKey = "44c8af396038a24e34936227d4a19dc2"

	auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
	response = requests.get(url=auth_url)
	jsondata = response.text
	return json.loads(jsondata)['access_token']


def use_cloud(token, wavefile):
	fp = wave.open(wavefile, 'rb')
	# 已经录好音的音频片段内容
	nframes = fp.getnframes()
	filelength = nframes * 2
	audiodata = fp.readframes(nframes)

	# 百度语音接口的产品ID
	cuid = '71XXXX663'
	server_url = 'http://vop.baidu.com/server_api' + '?cuid={}&token={}'.format(cuid, token)
	headers = {
		'Content-Type': 'audio/pcm; rete=8000',
		'Content-Length': '{}'.format(filelength),
	}

	response = requests.post(url=server_url, headers=headers, data=audiodata)
	return response.text if response.status_code == 200 else 'Something Wrong!'


if __name__ == '__main__':
	# record_wave()
	access_token = get_token()
	print(access_token)
	result = use_cloud(token=access_token, wavefile='./output.wav')
	print(str(str(result)))
