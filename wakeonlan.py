#!/usr/bin/python3

# File name: wakeonlan.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 11/4/2020
# Date last modified: 4/19/2021

# Notes: Requires the 'wakeonlan' command line function to be installed.

import sys
import json
import os

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)
	
	mac = data['params']['mac']
	
	command = 'wakeonlan ' + str(mac)

	stream = os.popen(command)
	output = stream.read()
	print(output)
	
	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
