#!/usr/bin/python3

# File name: ajakipro.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/5/2021
# Date last modified: 5/5/2021

import sys
import json
import requests
from datetime import datetime
import uuid

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	transport = data['params']['transport']
	clipname = data['params']['clipname']

	KiProURL = '/config?action=set&paramid='
	KiProParameter = ''
	KiProParameterValue = ''

	baseurl = 'http://' + ip + KiProURL

	if transport == 'record':
		#first build a unique clip name
		uniqueID = str(uuid.uuid4())
		uniqueID = uniqueID[0:8]
		clipname = clipname + '_' + datetime.today().strftime('%Y%m%d') + '_' + uniqueID
		print(clipname)

		#next turn off custom clip take
		KiProParameter = 'eParamID_UseCustomClipTake'
		KiProParameterValue = '0'
		url = baseurl + KiProParameter + '&value=' + KiProParameterValue
		r = requests.get(url)

		#next turn on custom clip name
		KiProParameter = 'eParamID_UseCustomClipName'
		KiProParameterValue = '1'
		url = baseurl + KiProParameter + '&value=' + KiProParameterValue
		r = requests.get(url)

		#next set custom clip name
		KiProParameter = 'eParamID_CustomClipName'
		KiProParameterValue = clipname
		url = baseurl + KiProParameter + '&value=' + KiProParameterValue
		r = requests.get(url)

		#now send record transport command
		KiProParameter = 'eParamID_TransportCommand'
		KiProParameterValue = '3'
	elif transport == 'stop':
		KiProParameter = 'eParamID_TransportCommand'
		KiProParameterValue = '4'
	elif transport == 'play':
		KiProParameter = 'eParamID_TransportCommand'
		KiProParameterValue = '1'
	else:
		print('Invalid transport command: ' + transport)

	if (KiProParameter != ''):
		url = baseurl + KiProParameter + '&value=' + KiProParameterValue
		r = requests.get(url)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')