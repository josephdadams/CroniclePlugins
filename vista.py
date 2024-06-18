#!/usr/bin/python3

# File name: vista.py
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
	midiport = data['params']['midiport']
	cueList = data['params']['cuelist']
	cue = data['params']['cue']

	url = 'http://' + ip + ':4000/sendmidi'
	
	jsonData = {
		"midiport": midiport,
		"midicommand":"msc",
		"deviceid": "0",
		"commandformat": "lighting.general",
		"command": "go",
		"cue": cue,
		"cuelist": cueList,
		"cuepath": ""
	}

	try:
		requests.post(url = url, json = jsonData, timeout=10)
		jobStatus = { "complete": 1 }
	except requests.exceptions.Timeout:
		jobStatus = { "complete": 1, "code": 999, "description": "Request timed out." }
except:
	jobStatus = { "complete": 1, "code": 999, "description": "Failed to execute." }
finally:
	print(json.dumps(jobStatus))