#!/usr/bin/python3
#
# christie_power.py
#
# Created by Ian Thompson on Thu Jun 23 2022
# ianthompson@nicelion.com

# Control Christie Projectors via TCP

import sys
import json
import socket

try: 
    stdinput = sys.stdin.readline()
    data = json.loads(stdinput)

    ip = data['params']['ip']           # IP address of projector
    port = int(data['params']['port'])  # Port to establish connection, default should be 3002
    command = data['params']['command'] # On/off command

    # Check which command is being requested, then format relevant message to be sent over TCP.
    if command.lower() == "on":
        message = '(PWR1)' + '\r\n'
    elif command.lower() == "off":
        message = '(PWR0)' + '\r\n'
    else:
        # User did not provide a valid command, we will raise an error to abort the task.
        raise Exception("Invalid command provided")

    print(message)

    # Establish TCP connection with projector and send relevant command.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(message.encode())
    s.close()

    # The process has completed, though we do not know if the projector has successfully turned on.
    print('{ "complete": 1 }')

except:
    # An ambiguous error message that will definitely help the user 
    print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')

