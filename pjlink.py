#!/usr/bin/python3

# File name: pjlink.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 12/5/2024
# Date last modified: 12/5/2024

# Simple non dependency PJLink control script. This script will send a PJLink command to a projector to turn it on or off.

from os import error
import sys
import json
import socket

def send_pjlink_command(host, port, command):
    """
    Sends a PJLink command to a projector.
    
    :param host: IP address or hostname of the projector
    :param port: Port number (default is usually 4352)
    :param command: PJLink command to send (e.g., '%1POWR 1' to turn on, '%1POWR 0' to turn off)
    """
    try:
        # Establish a connection to the projector
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            # Receive and ignore PJLink authentication message
            auth_message = sock.recv(1024).decode()
            print(f"Auth Message: {auth_message.strip()}")
            
            # Send the PJLink command
            sock.sendall(f"{command}\r".encode())
            # Receive and print the projector's response
            response = sock.recv(1024).decode()
            print(f"Response: {response.strip()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	try:
		host = data['params']['host']
		command = data['params']['command']

		print("Host:" + host)
		print("Command:" + command)

		if command == 'On':
			cmd = '%1POWR 1'
		else:
			cmd = '%1POWR 0'

		send_pjlink_command(host, 4352, cmd)

		print('{ "complete": 1 }')
	except Exception as e:
		print('Error:')
		print(e)
		print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
