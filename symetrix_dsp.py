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

	# check if mute parameter is provided, if not default to "ignore"
	if 'mute' in data['params']:
		mute = data['params']['mute']
	else:
		mute = "ignore"
	mute = mute.lower() # ensure mute value is lowercase for comparison

	# if mute is not a valid value, assume "ignore"
	if mute not in ["ignore", "mute", "unmute"]:
		mute = "ignore"

	print('Controller/Input: ' + str(controller))	
	
	if mute == "ignore":
		min = -72
		max = 12
		value = ((db - min) / 84) * 65535
		value = int(value)
		message = 'CS ' + str((controller)) + ' ' + str(value) + '\r\n'
		print('dB Value: ' + str(db))
	elif mute == "mute":
		message = 'CS ' + str((controller)) + ' 65535\r\n'
		value = 0
		print('Mute: ON')
	elif mute == "unmute":
		message = 'CS ' + str((controller)) + ' 0\r\n'
		value = 65535
		print('Mute: OFF')
	else:
		print('Invalid mute parameter: ' + mute)
		print('{ "complete": 1, "code": 998, "description": "Invalid mute parameter." }')
		sys.exit(0)
	
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