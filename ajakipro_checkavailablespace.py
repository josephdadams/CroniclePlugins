#!/usr/bin/python3

# File name: ajakipro_checkavailablespace.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/23/2021
# Date last modified: 5/23/2021

# Checks to see amount of available space on the Ki Pro. If the percentage is >= the threshhold, the job succeeds. If it is less, it fails.
# Job succeed/error chaining is then used to send an alert if needed

import sys
import json
import requests
from datetime import datetime
import uuid

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	percentage = data['params']['percentage']

	url = 'http://' + ip + '/config?action=get&paramid=eParamID_CurrentMediaAvailable'
	r = requests.get(url)

	availableSpace = int(json.loads(r.text)['value_name'])

	if availableSpace >= int(percentage):
		#success
		print('{ "complete": 1 }')
	else:
		#failed
		print('{ "complete": 1, "code": 999, "description": "Not enough space on the Ki Pro.", "chain_data": { "message": "Only ' + str(availableSpace) + '% remaining on KiPro: ' + ip + '"} }')
except Exception as e:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
	print(e)