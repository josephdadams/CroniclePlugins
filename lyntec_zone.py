#!/usr/bin/python3

# File name: lyntec_zone.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 8/9/2022
# Date last modified: 8/9/2022

import sys
import json
import requests

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	zone = data['params']['zone']
	power = data['params']['power']

	port = '80'

	print('Lyntec Zone Power Controller')
	print('IP: ' + ip)
	print('Zone: ' + zone)
	print('Set to Power State: ' + power)

	powerValue = '0'

	if power == 'on':
		powerValue = '1'
	else:
		powerValue = '0'

	url = 'http://' + ip + ':' + port + '/p2.rpc?IPZ' + zone + '=' + powerValue
	
	print('URL: ' + url)

	r = requests.get(url = url)

	print('Response:')
	print(r)

	# probably ran ok
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')