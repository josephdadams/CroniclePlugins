#!/usr/bin/python3

# File name: jtech-matrix.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 6/15/2022
# Date last modified: 6/15/2022

import sys
import json
import requests
import time

try:
	print('Starting JTech HDMI Matrix Plugin.')

	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	output = data['params']['output']
	input = data['params']['input']

	numoutputs = 4

	if output == 'All':
		count = 1
		while (count <= numoutputs):   
			cgiURL = '/videoset' + str(time.time())
			payload = '#video_d out' + str(count) + ' matrix=' + input
			url = 'http://' + ip + cgiURL
			print('Routing Output ' + str(count) + ' to Input ' + input)
			print('URL: ' + url)
			print('Payload: ' + payload)
			requests.post(url, data=payload, timeout=15)			
			count = count + 1
	else:
		cgiURL = '/videoset' + str(time.time())
		payload = '#video_d out' + output + ' matrix=' + input
		url = 'http://' + ip + cgiURL
		print('Routing Output ' + output + ' to Input ' + input)
		print('URL: ' + url)
		print('Payload: ' + payload)
		requests.post(url, data=payload, timeout=15)
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')