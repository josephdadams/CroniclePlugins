#!/usr/bin/python3

import sys
import json
import socket
import time

#try:
stdinput = sys.stdin.readline()
data = json.loads(stdinput)

ip = data['params']['ip']
port = int(data['params']['port'])
command = data['params']['command']

commandList = command.split(';')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
for i in commandList:
	s.send((str(i) + '\r\n').encode())
	time.sleep(.5)
s.close()

print('{ "complete": 1 }')
#except:
#	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')