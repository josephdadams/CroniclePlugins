#!/usr/bin/python3

# File name: cueserver.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 8/8/2022
# Date last modified: 8/8/2022

import sys
import json
import requests

import urllib.parse

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	cuescript = data['params']['cuescript']

	port = '80'

	print('CueScript: ' + cuescript)

	if cuescript != '':
		url = 'http://' + ip + ':' + port + '/exe.cgi?cmd=' + urllib.parse.quote_plus(cuescript)
		
		print('URL: ' + url)

		r = requests.get(url = url)

		print('Response:')
		print(r)

		# probably ran ok
		print('{ "complete": 1 }')
	else: #invalid command
		print('{ "complete": 1, "code": 999, "description": "Invalid CueScript." }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')