#!/usr/bin/python3

import sys
import json
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	command = data['params']['command']

	payload_on_hex = '0000002AD0F281F88BFF9AF7D5EF94B6C5A0D48BF99CF091E8B7C4B0D1A5C0E2D8A381F286E793F6D4EEDFA2DFA2'
	payload_off_hex = '0000002AD0F281F88BFF9AF7D5EF94B6C5A0D48BF99CF091E8B7C4B0D1A5C0E2D8A381F286E793F6D4EEDEA3DEA3'

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, 9999))
	if (command == 'on'):
		s.send(bytes.fromhex(payload_on_hex))
		s.send(('\r\n').encode())
	elif (command == 'off'):
		s.send(bytes.fromhex(payload_off_hex))
		s.send(('\r\n').encode())
	time.sleep(.5)
	s.close()

	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')