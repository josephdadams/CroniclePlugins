#!/usr/bin/python3

# File name: scriptlauncher_saytext.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/14/2025
# Date last modified: 5/14/2025

# Sends a command to the computer running ScriptLauncher to speak text using the say command.

import json, requests, sys

if __name__ == "__main__":
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	try:
		host = data['params']['host']
		port = 8810
		if host is None:
			print(json.dumps({"error": "ScriptLauncher host not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		password = data['params']['password']
		if password is None:
			print(json.dumps({"error": "ScriptLauncher password not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		text = data['params'].get('text', 'Hello, world!')
		
		voice = data['params'].get('voice', 'Alex')
		rate = str(data['params'].get("rate", 200))
		volume = str(data['params'].get("volume", 100))

		print("Host:" + host)
		print("Text:" + text)
		print("Voice:" + voice)
		print("Rate:" + rate)
		print("Volume:" + volume)

		args = [text, "-v", voice, "-r", rate, "-a", volume]

		params = {
			"command": "runScript",
			"password": password,
			"executable": "say",
			"args": args,
			"stdin": ""
		}

		r = requests.post(f"http://{host}:{port}/command", json=params)
		print(r.text)

		print('{ "complete": 1 }')
	except Exception as e:
		print('Error:')
		print(e)
		print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')