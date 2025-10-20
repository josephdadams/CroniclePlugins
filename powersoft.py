#!/usr/bin/python3

# File name: powersoft_control.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/7/2025
# Date last modified: 5/7/2025

# Toggles standby mode on a Powersoft amplifier via HTTP.
# power=on -> standby off (amp on)
# power=off -> standby on (amp off)

import sys
import json
import requests

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	power = data['params']['power'].lower()

	if power not in ['on', 'off']:
		print('{ "complete": 1, "code": 999, "description": "Invalid power value. Use \'on\' or \'off\'." }')
		sys.exit(1)

	bool_value = False if power == 'on' else True

	url = 'http://' + ip + '/am'
	payload = {
		"clientId": "x8-panel",
		"payload": {
			"type": "ACTION",
			"action": {
				"type": "WRITE",
				"values": [
					{
						"id": "/Device/Audio/Presets/Live/Generals/Standby/Value",
						"data": {
							"type": "BOOL",
							"boolValue": bool_value
						}
					}
				]
			}
		}
	}

	headers = {
		"User-Agent": "Cronicle/1.0",
		"Accept": "*/*",
		"Content-Type": "application/json"
	}

	response = requests.post(url, headers=headers, json=payload, timeout=2)

	if response.status_code == 200:
		print('{ "complete": 1 }')
	else:
		print('{ "complete": 1, "code": 999, "description": "Amplifier rejected the request. HTTP ' + str(response.status_code) + '" }')

except Exception as e:
	print('{ "complete": 1, "code": 999, "description": "Failed to communicate with amplifier." }')
	print(e)