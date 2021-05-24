#!/usr/bin/python3

# File name: ajakipro_checktransportstate.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/23/2021
# Date last modified: 5/23/2021

# Checks to see if the Ki Pro is in the Transport State requested. Succeeds if true. Fails if false.
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
	transport_state = data['params']['transport_state']

	url = 'http://' + ip + '/config?action=get&paramid=eParamID_TransportState'
	r = requests.get(url)

	current_transport_state = json.loads(r.text)['value_name']

	if transport_state == current_transport_state:
		#success
		print('{ "complete": 1 }')
	else:
		#failed
		print('{ "complete": 1, "code": 999, "description": "The Ki Pro is not in the desired transport state.", "chain_data": { "message": "The KiPro (' + ip + ') is not in Transport State: ' + transport_state + '. It is ' + current_transport_state + '"} }')
except Exception as e:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
	print(e)