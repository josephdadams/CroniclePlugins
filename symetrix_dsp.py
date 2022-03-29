#!/usr/bin/python3

# File name: symetrix_dsp.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 3/29/2022
# Date last modified: 3/29/2022

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	port = int(data['params']['port'])
	controller = int(data['params']['controller'])
	db = float(data['params']['db'])

	#Volume dB = -72 + 84*(CONTROLLER POSITION/65535)
	
	min = -72
	max = 12

	value = ((db - min) / 84) * 65535

	value = int(value)

	message = 'CS ' + str((controller)) + ' ' + str(value) + '\r\n'

	print('Controller/Input: ' + str(controller))
	print('dB Value: ' + str(db))
	print('Controller Value: ' + str(value))
	print('TCP Message:')
	print(message)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(1)
	s.close()

	print('Response:')
	print(data.decode("utf-8"))

	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')