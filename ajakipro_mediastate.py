#!/usr/bin/python3

# File name: ajakipro_mediastate.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 6/29/2021
# Date last modified: 6/10/2022

import sys
import json
import requests
from datetime import datetime
import uuid

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	state = data['params']['state']

	KiProURL = '/config?action=set&paramid='
	KiProParameter = ''
	KiProParameterValue = ''

	baseurl = 'http://' + ip + KiProURL

	if state == 'record':
		#send record-play state command
		KiProParameter = 'eParamID_MediaState'
		KiProParameterValue = '0'
	elif state == 'data':
		#send data-lan state command
		KiProParameter = 'eParamID_MediaState'
		KiProParameterValue = '1'
	else:
		print('Invalid state command: ' + state)

	if (KiProParameter != ''):
		url = baseurl + KiProParameter + '&value=' + KiProParameterValue
		r = requests.get(url)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
