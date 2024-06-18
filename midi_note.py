#!/usr/bin/python3

# File name: midi_note.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/15/2020
# Date last modified: 6/17/2024

import sys
import json
import requests

jobStatus = {}

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

	print('Sending midi-relay request to: ' + url)
	print('Data: ' + str(jsonData))
	
	try:
		requests.post(url = url, json = jsonData, timeout=10)
		jobStatus = { "complete": 1 }
	except requests.exceptions.Timeout:
		jobStatus = { "complete": 1, "code": 999, "description": "Request timed out." }
except Exception as e:
	print(e)
	jobStatus = { "complete": 1, "code": 999, "description": "Failed to execute: " + str(e) }
finally:
	print(json.dumps(jobStatus))