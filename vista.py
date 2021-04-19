#!/usr/bin/python3

# File name: vista.py
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
	
	r = requests.post(url = url, json = jsonData)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')