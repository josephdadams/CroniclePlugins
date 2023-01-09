/*
 * Vizio Smartcast Cronicle Plugin
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

var smartcast = require('vizio-smart-cast');

var data;

var ip, token, command, input;

var tv = null;

process.stdin.on('data', (res) => {
	data = JSON.parse(res);
	console.log('Starting Plugin');

	try {
		ip = data['params']['ip'];
		token = data['params']['token'];
		command = data['params']['command'];
		input = data['params']['input'];

		tv = new smartcast(ip);
		tv.pairing.useAuthToken(token);

		switch(command) {
			case 'Power On':
				controlPower(true);
				break;
			case 'Power Off':
				controlPower(false);
				break;
			case 'Change Input':
				controlInput();
				break;
		}
	}
	catch (error) {
		throwError(error);
	}
});

function controlPower(state) {
	console.log(`Turning TV Power ${(state ? 'On' : 'Off')}`);
	if (state) {
		tv.control.power.on()
		.then((data) => {
			console.log(data);

			console.log(`{"complete": 1}`);
		})
		.catch((error) => {
			throwError(error);
		});
	}
	else {
		tv.control.power.off()
		.then((data) => {
			console.log(data);

			console.log(`{"complete": 1}`);
		})
		.catch((error) => {
			throwError(error);
		});
	}
}

function controlInput() {
	console.log(`Turning TV to Input ${(input)}`);

	tv.input.set(input)
	.then((data) => {
		console.log(data);

		console.log(`{"complete": 1}`);
	})
	.catch((error) => {
		throwError(error);
	});
}

function throwError(err) {
	console.log(`{ "complete": 1, "code": 999, "description": "Failed to execute. See log.}" }`);

	console.log('Got this error:');
	console.log(err.toString());
	process.exit(999);
}