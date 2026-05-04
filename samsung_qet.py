#!/usr/bin/python3

# File name: samsung_qet.py
# Version: 1.0.1
# Author: Joseph Adams
# Date created: 3/30/2025
# Date last modified: 5/4/2026

import socket
import sys
import json

DISPLAY_PORT = 1515  # Default MDC port for Samsung displays

def fail(message):
    print(f'{{ "complete": 1, "code": 999, "description": "{message}" }}')
    sys.exit(1)

def success():
    print('{ "complete": 1 }')
    sys.exit(0)

def send_mdc_command(ip, port, command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # prevent hanging forever
            s.connect((ip, port))
            s.sendall(command)
    except Exception as e:
        fail(str(e))


try:
    stdinput = sys.stdin.readline()
    data = json.loads(stdinput)

    args = data['params']['ARGS'] #args is something like: 'ip=10.40.80.72,power=on'
    args = args.split(',')
    args = [x.split('=') for x in args]

    DISPLAY_IP = ''
    power_command = ''

    for arg in args:
        if arg[0] == 'ip':
            DISPLAY_IP = arg[1]
        elif arg[0] == 'power':
            power_command = arg[1]

    if not DISPLAY_IP:
        fail("Missing IP address")

    # Samsung MDC Power Commands (Hex)
    POWER_ON_COMMAND = bytes([
        0xAA, 0x11, 0x01, 0x01, 0x01, 0x14,
        0xAA, 0x11, 0xFE, 0x01, 0x01, 0x11
    ])

    POWER_OFF_COMMAND = bytes([
        0xAA, 0x11, 0x01, 0x01, 0x00, 0x13,
        0xAA, 0x11, 0xFE, 0x01, 0x00, 0x10
    ])

    if power_command == "on":
        send_mdc_command(DISPLAY_IP, DISPLAY_PORT, POWER_ON_COMMAND)
        success()

    elif power_command == "off":
        send_mdc_command(DISPLAY_IP, DISPLAY_PORT, POWER_OFF_COMMAND)
        success()

    else:
        fail("Invalid command. Use 'on' or 'off'.")

except Exception as e:
    fail(str(e))