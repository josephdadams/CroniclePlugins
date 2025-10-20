#!/usr/bin/python3

import sys
import json
import requests
from requests.auth import HTTPDigestAuth

def main():
	try:
		stdinput = sys.stdin.readline()
		data = json.loads(stdinput)
		
		# Parse command arguments
		args = data['params']['ARGS']  # Example: 'ip=192.168.1.100,power=on'
		args = args.split(',')
		args = {x.split('=')[0]: x.split('=')[1] for x in args}

		CAMERA_IP = args.get('ip', '10.40.80.81')
		power = args.get('power', 'on')

		username = 'admin'
		password = 'Amplio123'

		if power == 'off':
			url = f'http://{camera_ip}/command/main.cgi?System=standby'
		elif power == 'on':
			url = f'http://{camera_ip}/command/main.cgi?System=on'
		else:
			print(json.dumps({"error": f"Invalid power setting: '{power}'. Use 'on' or 'off'."}))
			print('{ "complete": 1, "code": 999 }')
			return

		response = requests.get(url, auth=HTTPDigestAuth(username, password), timeout=5)

		if response.status_code == 200:
			print(json.dumps({"success": True, "message": f"Camera power set to '{power}' successfully"}))
			print('{ "complete": 1 }')
		else:
			print(json.dumps({"error": f"HTTP {response.status_code}", "body": response.text}))
			print('{ "complete": 1, "code": 999 }')

	except Exception as e:
		print(json.dumps({"error": str(e)}))
		print('{ "complete": 1, "code": 999 }')

if __name__ == "__main__":
	main()