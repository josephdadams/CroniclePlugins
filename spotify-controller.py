#!/usr/bin/python3

# File name: spotify-controller.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 8/2/2022
# Date last modified: 8/2/2022

import sys
import json
import requests

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	command = data['params']['command']

	port = '8801'
	cmd = ''

	if command == 'Play':
		cmd = 'play'
	elif command == 'Play Track':
		trackID = data['params']['trackid']
		cmd = 'playTrack/' + trackID
	elif command == 'Play Track In Context':
		trackID = data['params']['trackid']
		contextID = data['params']['contextid']
		cmd = 'playTrackInContext/' + trackID + '/' + contextID
	elif command == 'Pause':
		cmd = 'pause'
	elif command == 'Play Toggle':
		cmd = 'playToggle'
	elif command == 'Next':
		cmd = 'next'
	elif command == 'Previous':
		cmd = 'previous'
	elif command == 'Volume Up':
		cmd = 'volumeUp'
	elif command == 'Volume Down':
		cmd = 'volumeDown'
	elif command == 'Set Volume':
		volume = data['params']['volume']
		cmd = 'setVolume/' + volume
	elif command == 'Ramp Volume':
		volume = data['params']['volume']
		cmd = 'rampVolume/' + volume
	elif command == 'Mute':
		cmd = 'mute'
	elif command == 'Unmute':
		cmd = 'unmute'
	elif command == 'Repeat On':
		cmd = 'repeatOn'
	elif command == 'Repeat Off':
		cmd = 'repeatOff'
	elif command == 'Repeat Toggle':
		cmd = 'repeatToggle'
	elif command == 'Shuffle On':
		cmd = 'shuffleOn'
	elif command == 'Shuffle Off':
		cmd = 'shuffleOff'
	elif command == 'Shuffle Toggle':
		cmd = 'shuffleToggle'

	print('Command: ' + command)

	if cmd != '':
		url = 'http://' + ip + ':' + port + '/' + cmd
		
		print('URL: ' + url)
		r = requests.get(url = url)
		json_data = r.json()
		print('Response:')
		print(json_data)
		if 'status' in json_data.keys():
			if json_data['status'] == 'not-allowed': #control is disabled
				print('Control is currently disabled.')
				print('{ "complete": 1, "code": 999, "description": "Control is disabled at the server." }')
			else:
				print('Result:')
				print(json_data['status'])
				print('{ "complete": 1 }')
		elif 'error' in json_data.keys(): #received an error response
			print('Error:')
			print(json_data['error'])
			print('{ "complete": 1, "code": 999, "description": "Received an error. See the log." }')
		else: # probably ran ok
			print('{ "complete": 1 }')
	else: #invalid command
		print('{ "complete": 1, "code": 999, "description": "Invalid Command." }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')