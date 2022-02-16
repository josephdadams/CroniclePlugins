#!/usr/bin/python3

# File name: timekeeper.py
# Version: 1.0.1
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/5/2021
# Date last modified: 2/15/2022

import sys
import json
import requests
import time
from datetime import datetime

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	port = data['params']['port']
	date_str = data['params']['date']
	time_str = data['params']['time']
	label = data['params']['label']
	roomID = data['params']['roomid']

	triggers = ''

	if 'triggers' in data['params']:
		triggers = data['params']['triggers']
	
	if (triggers == ''):
		triggers = '[]'

	timerid = ''

	if 'timerid' in data['params']:
		timerid = data['params']['timerid']

	url = 'http://' + ip + ':' + port + '/api/timer/add'

	#create a new datetime object using the fields provided
	#if date field is blank, use the system date
	#if time field is blank, use 6AM

	if (date_str == ''):
		date_str = datetime.today().strftime('%m/%d/%y')

	if (time_str == ''):
		time_str = '6:00:00'

	date_time_str = date_str + ' ' + time_str
	d = datetime.strptime(date_time_str, '%m/%d/%y %H:%M:%S')

	epochSeconds = int(d.timestamp()) * 1000

	jsonData = {
		"label": label,
		"datetime": epochSeconds,
		"publishMillis": 86400000, #1 day
		"expireMillis": 60000, #1 minute
		"roomID": roomID,
		"triggers": json.loads(triggers)
	}

	if (timerid != ''): #only include the ID if it was sent in the params
		jsonData['id'] = timerid

	print(jsonData)
	
	r = requests.post(url = url, json = jsonData)
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')