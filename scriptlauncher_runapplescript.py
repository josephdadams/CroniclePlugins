#!/usr/bin/python3

# File name: scriptlauncher_runapplescript.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/14/2025
# Date last modified: 5/14/2025

# Sends a command to the computer running ScriptLauncher to run an AppleScript.

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
		script = data['params']['script']
		if script is None:
			print(json.dumps({"error": "ScriptLauncher script not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)

		print("Host:" + host)
		print("Script:" + script)
		
		args = []
		for line in script.splitlines():
			args.extend(['-e', line])

		params = {
			"command": "runScript",
			"password": password,
			"executable": "osascript",
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