#!/usr/bin/python3

# File name: scriptlauncher_sendalert.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/14/2025
# Date last modified: 5/14/2025

# Sends a command to the computer running ScriptLauncher to display a notification.

import json, requests, sys

if __name__ == "__main__":
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	try:
		host =  data['params']['host']
		port = 8810
		if host is None:
			print(json.dumps({"error": "ScriptLauncher host not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		password =  data['params']['password']
		if password is None:
			print(json.dumps({"error": "ScriptLauncher password not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		message = data['params']['message']

		print("Host:" + host)
		print("Message:" + message)

		params = {
			"command": "sendAlert",
			"password": password,
			"message": message
		}

		r = requests.post(f"http://{host}:{port}/command", json=params)
		
		# convert the response to JSON
		try:
			response_json = r.json()
			if response_json.get("error"):
				print(json.dumps({"error": response_json["error"]}))
				print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
				sys.exit(1)
		except json.JSONDecodeError:
			print(json.dumps({"error": "Invalid JSON response"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		print("Response:")
		print(r.text)
		print("Response JSON:")
		print(response_json)

		print('{ "complete": 1 }')
	except Exception as e:
		print('Error:')
		print(e)
		print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')