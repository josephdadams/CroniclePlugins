#!/usr/bin/python3

# File name: pco_print.py
# Version: 1.0.1
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 9/16/2020
# Date last modified: 2/7/2023

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
	servicetypes = data['params']['servicetypes'] #pco service type ids, delimited by semicolon
	reportId = data['params']['reportid'] #pco custom report id
	pageSize = data['params']['pagesize'] #page size 'US-Letter'
	printOrientation = data['params']['printorientation'] #print orientation 'Portrait'
	printMargin = data['params']['printmargin'] #print margin '0.25in'

	credentials = ('%s:%s' % (appid, secret))
	encoded_credentials = base64.b64encode(credentials.encode('ascii'))

	serviceTypesList = servicetypes.split(';')

	planIds = []
	for x in serviceTypesList:
		url = 'https://api.planningcenteronline.com/services/v2/service_types/' + x + '/plans?filter=future&per_page=1'
		req = urllib.request.Request(url)
		req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
		with urllib.request.urlopen(req) as response:
			responseData = json.loads(response.read())
			planIds.append(responseData['data'][0]['id'])

	planIdParams = ''
	for x in planIds:
		planIdParams = planIdParams + '&plan_ids[]=' + x

	#send the VICREO commands
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	#build the PDF URL Path
	pdfPath = 'https://services.planningcenteronline.com/report_templates/' + reportId + '/report.pdf?page_size=' + pageSize + '&orientation=' + printOrientation + '&margin=' + printMargin + planIdParams
	print(pdfPath)
	path = '/usr/bin/open -a Safari \'' + pdfPath + '\''
	message = '{ "type":"shell","shell":"' + path + '" }'
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(1)
	s.close()

	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
