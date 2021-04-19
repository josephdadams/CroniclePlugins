#!/usr/bin/python3

# File name: vicreo_key.py
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
	key = data['params']['key']
	modifiers_shift = data['params'].get('modifiers_shift')
	modifiers_fn = data['params'].get('modifiers_fn')
	modifiers_ctrl = data['params'].get('modifiers_ctrl')
	modifiers_command = data['params'].get('modifiers_command')
	modifiers_alt = data['params'].get('modifiers_alt')
	modifiers_rightshift = data['params'].get('modifiers_rightshift')
	modifiers_rightalt = data['params'].get('modifiers_rightalt')
	modifiers_rightctrl = data['params'].get('modifiers_rightctrl')

	modifiers = []

	if (modifiers_shift):
		modifiers.append('"shift"')

	if (modifiers_fn):
		modifiers.append('"fn"')

	if (modifiers_ctrl):
		modifiers.append('"control"')

	if (modifiers_command):
		modifiers.append('"command"')

	if (modifiers_alt):
		modifiers.append('"alt"')

	if (modifiers_rightshift):
		modifiers.append('"right_shift"')

	if (modifiers_rightalt):
		modifiers.append('"right_alt"')

	if (modifiers_rightctrl):
		modifiers.append('"right_ctrl"')

	message = '{ "type":"press","key":"' + key + '","modifiers":[' + ','.join(modifiers) + '] }'

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send(message.encode())
	data = s.recv(1024)
	s.close()

	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
