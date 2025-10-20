#!/usr/bin/python3

# File name: scriptlauncher_systemcontrol.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 5/14/2025
# Date last modified: 5/14/2025

# Sends a command to the computer running ScriptLauncher to shutdown, reboot, or lock the system.

import json, requests, sys

if __name__ == "__main__":
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	try:
		host = data['params'].get("host")
		port = 8810
		if host is None:
			print(json.dumps({"error": "ScriptLauncher host not set"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)
		password = data['params'].get("password", "admin22")
		command = data['params'].get("command")  # 'shutdown', 'reboot', or 'lock'

		if command not in ("shutdown", "reboot", "lock"):
			print(json.dumps({"error": "Invalid command"}))
			print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
			sys.exit(1)

		print("Host:" + host)
		print("Command:" + command)

		params = {
			"command": command,
			"password": password,
		}

		if command == "shutdown":
			params["time"] = data.get("delay", 1)

		r = requests.post(f"http://{host}:{port}/command", json=params)
		print(r.text)

		print('{ "complete": 1 }')
	except Exception as e:
		print('Error:')
		print(e)
		print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')