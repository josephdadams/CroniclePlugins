#!/usr/bin/python3

# File name: videohub_bulk.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 9/14/2022
# Date last modified: 9/14/2022

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	ip = data['params']['ip']
	port = 9990
	routes = str(data['params']['routes'])

	newroutes = ''

	for route in routes.splitlines():
		pieces = route.split(' ')
		
		dest = int(pieces[0])
		dest -= 1 #zero base
		
		source = int(pieces[1])
		source -= 1 #zero base
		
		newroutes = newroutes + str(dest) + ' ' + str(source) + '\r\n'
	
	message = 'VIDEO OUTPUT ROUTING:\r\n' + newroutes + '\r\n'

	print(message)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	print(data)
	time.sleep(1)
	s.close()
	
	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
