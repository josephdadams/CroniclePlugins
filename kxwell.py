#!/usr/bin/python3

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = 5000
	preset = int(data['params']['preset'])

	print('Preset Number: ' + str(preset))

	preset = preset - 1 #zero based

	preset_padded = ''

	if preset < 10:
		preset_padded = '0' + str(preset)
	else:
		preset_padded = str(preset)

	message = '#01R' + preset_padded

	print(ip)
	print('Sending Message: ' + message)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(1)
	s.close()
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')