#!/usr/bin/python3

# File name: epsonprojector.py
# Version: 1.0.2
# Author: Joseph Adams
# Date created: 6/12/2025
# Description: Controls Epson projector power state via Digest Auth using Cronicle params.

import json, requests, sys, time
from requests.auth import HTTPDigestAuth

if __name__ == "__main__":
    stdinput = sys.stdin.readline()
    data = json.loads(stdinput)

    try:
        ip = data['params'].get('ip')
        username = data['params'].get('username')
        password = data['params'].get('password')
        command = data['params'].get('command', '').lower()

        # Validate parameters
        if not ip:
            print(json.dumps({"error": "Projector IP not set"}))
            print('{ "complete": 1, "code": 999, "description": "Missing IP" }')
            sys.exit(1)
        if not username or not password:
            print(json.dumps({"error": "Username or password not set"}))
            print('{ "complete": 1, "code": 999, "description": "Missing credentials" }')
            sys.exit(1)
        if command not in ['on', 'off']:
            print("Invalid command")
            print('{ "complete": 1, "code": 999, "description": "Command must be on or off" }')
            sys.exit(1)

        headers = {
            "Referer": f"http://{ip}/cgi-bin/Remote/Basic_Control",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/plain, */*; q=0.01",
        }

        if command == 'on':
            timestamp = int(time.time() * 1000)
            url = f"http://{ip}/cgi-bin/Remote/directsend?IMPWR=ON&_={timestamp}"
            print(url)

            response = requests.get(url, headers=headers, auth=HTTPDigestAuth(username, password), timeout=5)

            print(f"Sent command to {ip} - Command: ON")
            print(f"HTTP {response.status_code}")
            print(response.text)

            if response.status_code == 200:
                print('{ "complete": 1 }')
                sys.exit(0)
            else:
                print('{ "complete": 1, "code": 999, "description": "Projector responded with error." }')
                sys.exit(1)

        else:  # off: send KEY=6C twice
            for i in range(2):
                timestamp = int(time.time() * 1000)
                url = f"http://{ip}/cgi-bin/Remote/directsend?KEY=6C&_={timestamp}"
                print(f"[{i+1}/2] Sending OFF command to: {url}")

                response = requests.get(url, headers=headers, auth=HTTPDigestAuth(username, password), timeout=5)
                print(f"HTTP {response.status_code}")
                print(response.text)

                if response.status_code != 200:
                    print('{ "complete": 1, "code": 999, "description": "Failed on power off command." }')
                    sys.exit(1)

                time.sleep(1)  # delay between presses

            print('{ "complete": 1 }')
            sys.exit(0)

    except Exception as e:
        print("Error:")
        print(e)
        print('{ "complete": 1, "code": 999, "description": "Unexpected failure." }')
        sys.exit(1)