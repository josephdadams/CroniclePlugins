#!/usr/bin/python3

# File name: vicreo_file.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/15/2020
# Date last modified: 11/18/2021

import sys
import json
import socket
import hashlib

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = int(data['params']['port'])
	path = data['params']['path']

	if 'password' in data['params']:
		password = data['params']['password']
		passwordHash = ''

		if password != '':
			passwordHash = hashlib.md5(password.encode()).hexdigest()

		message = '{ "type":"file","path":"' + path + '","password":"' + passwordHash + '" }'
	else:
		message = '{ "type":"file","path":"' + path + '" }'

	print(message)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	s.close()
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
