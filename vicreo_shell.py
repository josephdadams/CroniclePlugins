#!/usr/bin/python3

# File name: vicreo_shell.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/15/2020
# Date last modified: 4/19/2021

import sys
import json
import socket

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = int(data['params']['port'])
	shell = data['params']['shell']
	
	message = '{ "type":"shell","shell":"' + shell + '" }'
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	s.close()
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
