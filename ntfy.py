#!/usr/bin/python3

# File name: ntfy.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/22/2024
# Date last modified: 5/22/2024

import sys
import json
import requests
import base64

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	server = data['params']['server']
	topic = data['params']['topic']

	useAuth = data['params']['useauth']

	headers = {}

	if (useAuth == True):
		authType = data['params']['authtype'] #basic or bearer
		if authType == 'Basic Auth':
			username = data['params']['username']
			password = data['params']['password']
			headers['Authorization'] = 'Basic ' + str(base64.b64encode((username + ':' + password).encode('utf-8')).decode('utf-8'))
		else:
			token = data['params']['token']
			headers['Authorization'] = 'Bearer ' + token

	override = data['params']['override']

	if override == True:
		headers_extra = data['params']['headers_extra']
		headers.update(headers_extra)
	else:
		title = data['params']['title']
		if title != '':
			headers['Title'] = title

		priority = data['params']['priority'] #Min, Low, Default, High, Max/Urgent
		if priority == 'Min':
			headers['Priority'] = '1'
		elif priority == 'Low':
			headers['Priority'] = '2'
		elif priority == 'Default':
			headers['Priority'] = '3'
		elif priority == 'High':
			headers['Priority'] = '4'
		elif priority == 'Max/Urgent':
			headers['Priority'] = '5'

		email = data['params']['email']
		if email != '':
			headers['Email'] = email

	message = data['params']['message']

	if "chain_data" in data: # support for cronicle job chaining
		if "message" in data['chain_data']:
			message = message + ' ' + data['chain_data']['message']

	url = server + '/' + topic #host should include http:// or https://

	r = requests.post(url, headers=headers, data=message)

	print('{ "complete": 1 }')
except Exception as e:
	print(e)
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
