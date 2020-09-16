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

	planIdParams = '&plan_id=' + planIds[0]
	for x in planIds:
		planIdParams = planIdParams + '&' + x + '_plan=true'

	#send the VICREO commands
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	#build the PDF URL Path
	pdfPath = 'https://services.planningcenteronline.com/reports/' + reportId + '.pdf?utf8=%E2%9C%93&custom_report_id=' + reportId + '&print_to=pdf&print_page_size=' + pageSize + '&print_orientation=' + printOrientation + '&print_margin=' + printMargin + planIdParams
	path = '/usr/bin/open -a Safari \'' + pdfPath + '\''
	message = '{ "type":"shell","shell":"' + path + '" }'
	s.send(message.encode())
	data = s.recv(1024)
	time.sleep(1)
	s.close()

	print('{ "complete": 1 }')
except:
	print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')