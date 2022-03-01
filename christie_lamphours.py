#!/usr/bin/python3

import sys
import json
import urllib.request

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip'] #projector IP
	projectorName = data['params']['name']
	threshold = int(data['params']['threshold']) # lamp hour threshold, if the hours are past this, the job will fail

	url = 'http://' + ip + '/cgi-bin/webctrl.cgi.elf?&t:26,c:10,p:196608&t:26,c:10,p:196609'

	lamp1 = 0
	lamp2 = 0

	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		responseString = response.read().decode('utf8').replace(',]',']')
		responseData = json.loads(responseString)

		lamp1 = int(responseData[0]['string'])
		lamp2 = int(responseData[1]['string'])

	print(projectorName)
	print('Lamp 1 Current Hours: ' + str(lamp1))
	print('Lamp 2 Current Hours: ' + str(lamp2))
	print('Threshold: ' + str(threshold))

	failed = False

	if lamp1 > threshold:
		failed = True
	
	if lamp2 > threshold:
		failed = True

	if failed:
		message = 'Lamp hours exceeded on Christie Projector: ' + projectorName + '.'
		print('{ "complete": 1, "code": 999, "description": "' + message + '", "chain_data": { "message": "' + message + '"} }')
	else:
		print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')