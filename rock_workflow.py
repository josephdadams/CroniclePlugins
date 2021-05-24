#!/usr/bin/python3

# File name: rock_workflow.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/13/2021
# Date last modified: 5/13/2021

import sys
import json
import requests
import urllib.parse

try:
	stdinput = sys.stdin.readline()
	
	data = json.loads(stdinput)

	workflow_url = data['params']['workflowurl']
	workflow_id = data['params']['workflowid']
	token = data['params']['token']
	group_id = data['params']['groupid']
	message_type = data['params']['type']
	subject = data['params']['subject']
	body = data['params']['body']
	
	print(data)
	
	if "chain_data" in data:
		if "message" in data['chain_data']:
			body = body + ' ' + data['chain_data']['message']
	
	params = { 'GroupId': group_id, 'MessageType': message_type, 'EmailSubject': subject, 'MessageBody': body }

	url = '{}{}?{}'.format(workflow_url,workflow_id,urllib.parse.urlencode(params))
	
	print(url)
	
	headers = {
		"accept": "application/x-www-form-urlencoded",
		"Authorization-Token": token,
		"Content-Length": "0"
	}
	
	r = requests.post(url = url, headers = headers)
	
	print(r)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')