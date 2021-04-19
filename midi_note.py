#!/usr/bin/python3

# File name: midi_note.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/15/2020
# Date last modified: 4/19/2021

import sys
import json
import requests

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	port = data['params']['port']
	midiport = data['params']['midiport']
	midicommand = data['params']['midicommand']
	channel = data['params']['channel']
	note = data['params']['note']
	velocity = data['params']['velocity']

	url = 'http://' + ip + ':' + port + '/sendmidi'
	
	jsonData = {
		"midiport": midiport,
		"midicommand": midicommand,
		"channel": channel,
		"note": note,
		"velocity": velocity
	}
	
	r = requests.post(url = url, json = jsonData)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')