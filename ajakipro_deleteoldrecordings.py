#!/usr/bin/python3

# File name: ajakipro_deleteoldrecordings.py
# Version: 1.0.1
# Author: Joseph Adams
# Date created: 4/30/2026

import sys
import json
import requests
import re
from datetime import datetime, timedelta
from urllib.parse import quote

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip']
	days = int(data['params'].get('days', 14))

	cutoff = datetime.now() - timedelta(days=days)

	clips_url = 'http://' + ip + '/clips'
	r = requests.get(clips_url, timeout=10)
	r.raise_for_status()

	raw = r.text

	clip_pattern = re.compile(
		r'clipname:\s*"([^"]+)".*?timestamp:\s*"([^"]+)"',
		re.DOTALL
	)

	matches = clip_pattern.findall(raw)

	deleted = []
	kept = []
	errors = []

	print("Ki Pro Cleanup - Target: " + ip)
	print("Cutoff Date: " + str(cutoff))
	print("----")

	for name, timestamp in matches:
		try:
			clip_date = datetime.strptime(timestamp, '%m/%d/%y %H:%M:%S')
		except Exception as date_error:
			print("SKIP: " + name + " | Unparsed timestamp: " + timestamp)
			errors.append(name + ': bad timestamp')
			continue

		if clip_date < cutoff:
			print("DELETE: " + name + " | timestamp: " + timestamp)

			try:
				encoded_name = quote(name)

				set_clip_url = 'http://' + ip + '/config?action=set&paramid=eParamID_ClipToDelete&value=' + encoded_name
				delete_url = 'http://' + ip + '/config?action=set&paramid=eParamID_TransportDeleteClip&value='

				set_clip_request = requests.get(set_clip_url, timeout=10)
				set_clip_request.raise_for_status()

				delete_request = requests.get(delete_url, timeout=10)
				delete_request.raise_for_status()

				deleted.append(name)

			except Exception as delete_error:
				print("ERROR deleting " + name + ": " + str(delete_error))
				errors.append(name + ': ' + str(delete_error))
		else:
			print("KEEP:   " + name + " | timestamp: " + timestamp)
			kept.append(name)

	print("----")
	print("Summary: " + str(len(deleted)) + " deleted, " + str(len(kept)) + " kept, " + str(len(errors)) + " errors")

	if len(matches) == 0:
		print('{ "complete": 1, "description": "No recordings found on Ki Pro: ' + ip + '" }')
	elif len(errors) > 0:
		print('{ "complete": 1, "code": 999, "description": "Some recordings failed to process.", "chain_data": { "message": "' + str(len(deleted)) + ' deleted, ' + str(len(errors)) + ' errors on Ki Pro: ' + ip + '" } }')
	else:
		print('{ "complete": 1, "chain_data": { "message": "' + str(len(deleted)) + ' old recordings processed on Ki Pro: ' + ip + '" } }')

except Exception as e:
	print('{ "complete": 1, "code": 999, "description": "Failed to delete old Ki Pro recordings." }')
	print(e)