#!/usr/bin/python3

# File name: jtech-matrix-ip2sl.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 2/10/2023
# Date last modified: 2/10/2023

import sys
import json
import time
import socket

try:
	print('Starting JTech HDMI Matrix Plugin IP2SL Version.')
	print('Sends the command via TCP/IP to the IP2SL module, which then sends the command to the matrix.')

	def sendCommand(ip, port, output, input):
		payload = '#video_d out' + str(output) + ' matrix=' + str(input) + ' onoff=1'

		print('Sending command to IP2SL module.')
		print('IP: ' + ip)
		print('Port: ' + str(port))
		print('Routing Output ' + str(output) + ' to Input ' + str(input))
		print('Payload: ' + payload)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(payload.encode())
		data = str(s.recv(1024))
		print(data)
		s.close()

	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	port = 4999
	output = str(data['params']['output'])
	input = str(data['params']['input'])

	if output == 'All':
		print('Changing all outputs to input ' + input)
		count = 1
		numoutputs = 4
		while (count <= numoutputs):
			sendCommand(ip, port, count, input)
			count += 1
			time.sleep(3) #wait 3 seconds between each output
	else:
		sendCommand(ip, port, output, input)
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')