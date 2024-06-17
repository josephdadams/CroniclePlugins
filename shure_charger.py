#!/usr/bin/python3

# File name: shure_charger.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 9/18/2023
# Date last modified: 6/17/2024

import sys
import json
import socket
import time
import os

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	print(str(stdinput))

	print('Getting battery status...')
	print('IP: ' + data['params']['ip'])
	print('Room Name: ' + data['params']['room_name'])
	
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

	jobStatus = {}

	if batt1_status == 'YES' and batt2_status == 'YES':
		msg = room_name + ' - ' + 'Both mics are detected in the charger.'
		jobStatus = { "complete": 1, "code": 0, "description": msg, "chain_data": { "message": msg } }
		print(json.dumps(jobStatus))
	else:
		if batt1_status == 'NO' and batt2_status == 'NO':
			msg = 'No mics detected in either slot of the charger.'
		elif batt1_status == 'NO':
			msg = 'No mic detected in Slot 1 of the charger.'
		elif batt2_status == 'NO':
			msg = 'No mic detected in Slot 2 of the charger.'
		msg = room_name + ' - ' + msg
		jobStatus = { "complete": 1, "code": 999, "description": msg, "chain_data": { "message": msg } }
except OSError as error: 
	jobStatus = { "complete": 1, "code": 999, "description": "Job Failed to execute: " + str(error), "chain_data": { "message": "Job failed to execute: " + os.environ['JOB_EVENT_TITLE'] + " - Error: " + str(error) } }
except:
	jobStatus = { "complete": 1, "code": 999, "description": "Failed to execute: " + str(sys.exc_info()[0]), "chain_data": { "message": "Failed to execute: " + str(sys.exc_info()[0]) } }
finally:
	print(json.dumps(jobStatus))
