/*
 * OBS Cronicle Plugin
 *
 * Copyright (c) 2022 Joseph Adams
 * Author: Joseph Adams <josephdadams@gmail.com>
 *
 * This program is free software.
 * You should have received a copy of the MIT license along with
 * this program.
 *
 * You can be released from the requirements of the license by purchasing
 * a commercial license. Buying such a license is mandatory as soon as you
 * develop commercial activities involving this software software without
 * disclosing the source code of your own applications.
 *
 */

const OBSWebSocket = require('obs-websocket-js').default;

var obs = null;

var data;

var host, port, password, command, destinationScene;

process.stdin.on('data', (res) => {
	data = JSON.parse(res);
	console.log('Starting OBS Plugin');

	try {
		host = data['params']['host'];
		port = data['params']['port'];
		password = data['params']['password'];
		command = data['params']['command'];
		destinationScene = data['params']['destinationScene'];

		console.log("Host:" + host);
		console.log("Port:" + port);
		console.log("Password:" + password);
		console.log('Command: ' + command);

		connectOBS();

		setTimeout(runCommand, 2000); //give it 2 seconds to connect to the websocket first

	} catch (err) {
		console.log(err);

		console.log(`{ "complete": 1, "code": 999, "description": "Failed to execute: ${err}" }`);
		process.exit(999);
	}
	finally {
		//disconnectOBS();
	}
});

function runCommand() {
	switch(command) {
		case 'Start Stream':
			controlStream('StartStream');
			console.log(`{"complete": 1}`);
			break;
		case 'Stop Stream':
			controlStream('StopStream');
			console.log(`{"complete": 1}`);
			break;
		case 'Switch Scene':
			console.log("Destination Scene:" + destinationScene);
			controlScene(destinationScene);
			console.log(`{"complete": 1}`);
			break;
		default:
			console.log(`{ "complete": 1, "code": 999, "description": "Failed to execute: Invalid Command." }`);
			break;
	}
}

async function controlStream(value) {
	//starts or stops the stream
	let data = await obs.call(value);
	disconnectOBS();
}

async function controlScene(sceneName) {
	//changes the program scene to the sceneName
	let data = await obs.call('SetCurrentProgramScene', { sceneName: sceneName })
	disconnectOBS();
}

async function connectOBS() {
	if (obs) {
		await obs.disconnect();
	} else {
		obs = new OBSWebSocket();
	}
	try {
		await obs.connect(
			`ws:///${host}:${port}`,
			password
		);
	} catch (error) {
		console.log(error);
	}
}

async function disconnectOBS() {
	if (obs) {
		await obs.disconnect();
	}
}