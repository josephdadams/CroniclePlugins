#!/usr/bin/python3

# File name: ping.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/11/2024
# Date last modified: 7/11/2024

# Sends a ping to the host and returns the result
# Job succeed/error chaining is then used to send an alert if needed

import sys
import json
import os

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	hostname = data['params']['hostname']

	response = os.system("ping -c 1 " + hostname)
	if response == 0:
		#success
		print('{ "complete": 1 }')
	else:
		#failed
		message = "Ping to host " + hostname + " failed."
		print('{ "complete": 1, "code": 999, "description": "' + message + '", "chain_data": { "message": "' + message + '"} }')
except Exception as e:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
	print(e)