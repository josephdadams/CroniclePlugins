#!/usr/bin/python3

# File name: shure_charger.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 9/18/2023
# Date last modified: 9/18/2023

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = 2202
	room_name = data['params']['room_name']
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	message = '< GET 1 BATT_DETECTED >'
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(0.3)

	print(data.decode())

	batt1 = data.decode().split(' ')
	batt1_status = batt1[4]

	message = '< GET 2 BATT_DETECTED >'
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(0.3)

	print(data.decode())

	batt2 = data.decode().split(' ')
	batt2_status = batt2[4]

	s.close()

	if batt1_status == 'YES' and batt2_status == 'YES':
		msg = room_name + ' - ' + 'Both mics are detected in the charger.'
		print('{ "complete": 1, description": "' + msg + '" }')
	else:
		if batt1_status == 'NO' and batt2_status == 'NO':
			msg = 'No mics detected in either slot of the charger.'
		elif batt1_status == 'NO':
			msg = 'No mic detected in Slot 1 of the charger.'
		elif batt2_status == 'NO':
			msg = 'No mic detected in Slot 2 of the charger.'
		msg = room_name + ' - ' + msg
		print('{ "complete": 1, "code": 999, "description": "' + msg + '", "chain_data": { "message": "' + msg + '" } }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute: ' + str(sys.exc_info()[0]) + '" }')
