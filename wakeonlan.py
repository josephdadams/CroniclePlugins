#!/usr/bin/python3

import sys
import json
import os

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	mac = data['params']['mac']
	
	command = 'wakeonlan ' + str(mac)

	stream = os.popen(command)
	output = stream.read()
	print(output)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')