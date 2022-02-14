#!/usr/bin/python3

import sys
import json
import urllib.request
import base64
import socket
import time

try:
	stdinput = sys.stdin.readline()
	data = json.loads(stdinput)

	ip = data['params']['ip'] #vicreo computer IP
	port = int(data['params']['port']) #vicreo computer port
	appid = data['params']['appid'] # pco app id
	secret = data['params']['secret'] #pco secret key
	servicetype = data['params']['servicetype'] #pco service type id to load the live screen for

	credentials = ('%s:%s' % (appid, secret))
	encoded_credentials = base64.b64encode(credentials.encode('ascii'))

	planId = ''

	url = 'https://api.planningcenteronline.com/services/v2/service_types/' + servicetype + '/plans?filter=future&per_page=1'
	req = urllib.request.Request(url)
	req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
	with urllib.request.urlopen(req) as response:
		responseData = json.loads(response.read())
		planId = responseData['data'][0]['id']

	if (planId != ''):
		#send the VICREO commands
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))

		#build the Live URL Path
		livePath = 'https://services.planningcenteronline.com/live/' + planId
		path = '/usr/bin/open -a Safari \'' + livePath + '\''
		message = '{ "type":"shell","shell":"' + path + '" }'
		s.send(message.encode())
		data = s.recv(1024)
		time.sleep(1)
		s.close()

	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')