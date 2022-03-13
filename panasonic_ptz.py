#!/usr/bin/python3

# File name: panasonic_ptz.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 3/13/2021
# Date last modified: 3/13/2021

import sys
import json
import requests

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	preset = data['params']['preset']

	preset_padded = str(int(preset)-1).zfill(2)

	url = 'http://' + ip + '/cgi-bin/aw_ptz?cmd=%23R' + preset_padded + '&res=1'

	print('Going to Preset: ' + preset)
	print(url)

	r = requests.get(url)
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')