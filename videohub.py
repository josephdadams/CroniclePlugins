#!/usr/bin/python3

# File name: videohub.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/15/2020
# Date last modified: 4/19/2021

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = 9990
	source = int(data['params']['source'])
	destination = int(data['params']['destination'])

	source -= 1
	destination -= 1
	
	message = 'VIDEO OUTPUT ROUTING:\r\n' + str(destination) + ' ' + str(source) + '\r\n\r\n'
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	print(data)
	time.sleep(1)
	s.close()
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
