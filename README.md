# CroniclePlugins

Plugins I have created to use with Cronicle (https://github.com/jhuckaby/Cronicle)

Create a new plugin in Cronicle and upload each script to the Cronicle server. You can make the scripts directly executable by using `chmod +x plugin.py` and then just specify the path to the file for the plugin to execute.

Read more about how I am using these plugins here: https://techministry.blog/2020/07/16/automating-production-equipment-using-a-chromebox-and-a-scheduling-server/

## ajakipro.py

Allows control of an AJA Ki Pro unit.
Requires the following parameters:

- `ip`: Text Field: IP Address of the AJA Ki Pro
- `transport`: Menu: Items `record`, `stop`, `play`
- `clipname`: TextField: Name of the clip. All clips will automatically be appended with the date in yyyymmdd format followed by an 8-character uuid to ensure a unique filename

## ajakipro_mediastate.py

Allows control of an AJA Ki Pro unit's media state to put it in Record-Play or Data-LAN state depending on your needs.
Requires the following parameters:

- `ip`: Text Field: IP Address of the AJA Ki Pro
- `state`: Menu: Items `record`, `data`

## ajakipro_checkavailablespace.py

Checks the available space on the AJA Ki Pro. If the percentage is less than the desired percentage free, the job will fail and pass a message in the `chain_data` to be used in the next job (if configured).
Requires the following parameters:

- `ip`: Text Field: IP Address of the AJA Ki Pro
- `percentage`: Text Field: Threshold percentage. If the available space on the drive is less than this number, the job will fail.

## ajakipro_checktransportstate.py

Checks the transport state on the AJA Ki Pro. If it does not match the desired transport state, the job will fail and pass a message in the `chain_data` to be used in the next job (if configured).
Requires the following parameters:

- `ip`: Text Field: IP Address of the AJA Ki Pro
- `transport_state`: Menu: Items `Playing Reverse`, `Reverse 2X`, `Forward 2X`, `Forward 4X`, `Forward 8X`, `Forward 16X`, `Stop`, `Paused`, `Recording`, `Idle`

## christie_lamphours.py

Checks the lamp hours of the Christie projector. If the lamp hours are past the threshold, the job will fail and pass a message in the `chain_data` to be used in the next job.
Requires the following parameters:

- `ip`: Text Field: IP Address of the Projector
- `name`: Text Field: Friendly name of the Projector used in the error message
- `threshold`: Text Field: Threshold number of hours. If the lamp hours are greater than this, the job will fail.

## christie_power.py

Allows you to send on/off commands to Christie projectors.
Requires the following parameters:

- `ip`: Text Field: IP Address of the Projector
- `port`: Text Field: Port to establish connection with. Default is 3002
- `command`: Text Field: Command to send to projector (on/off). Job will fail if invalid command is passed

## companion.py

Allows buttons in Bitfocus Companion to be pressed remotely.
Requires the following parameters:

- `ip`: Text Field: IP address of the device running Bitfocus Companion
- `port`: Text Field: TCP listening port in Companion (default of 51234)
- `page`: Text Field: Page that the button is on that you want to execute
- `button`: Text Field: Button number on that page that you want to execute

## cueserver.py

Allows you to execute CueScripts on an Interactive Technologies CueServer.

Requires the following parameters:
- `ip`: Text Field: IP address of the CueServer
- `cuescript`: Text Field: CueScript to execute (will be URL encoded)

## generic_tcp.py

Allows you to send generic TCP strings to the specified IP/port.
Requires the following parameters:

- `ip`: Text Field: IP address of the device
- `port`: Text Field: TCP listening port
- `message`: Text Field: Message string you want to send. Automatically sends `\n` at the end.

## jtech-matrix.py

Allows you to control routings on a JTech Digital HDMI Matrix.
Requires the following parameters:

- `ip`: Text Field: IP address of the device
- `output`: Text Field: Output Number; also accepts `All` to assign the Input to all Outputs
- `input`: Text Field: Input Number

## jtech-matrix-ip2sl.py

Allows you to control routings on a JTech Digital HDMI Matrix but sends the command via a GlobalCache IP2SL device to the matrix via serial.
Requires the following parameters:

- `ip`: Text Field: IP address of the GlobalCache IP2SL
- `output`: Text Field: Output Number; also accepts `All` to assign the Input to all Outputs
- `input`: Text Field: Input Number

## kxwell.py

Allows you to control a KXWell PTZ head and recall presets.
Requires the following parameters:

- `ip`: Text Field: IP address of the device
- `preset`: Text Field: Preset to recall.
  Uses port 5000.

# lyntec_zone.py

Allow you to turn a Lyntec RPC breaker zone on/off.
Requires the following parameters:

- `ip`: Text Field: IP address of the device
- `zone`: Text Field: Zone number to control. e.g. `001`
- `power`: Menu: Items `on`, `off`

## midi_note.py

Allows you to send MIDI notes via [midi-relay](http://github.com/josephdadams/midi-relay/) to the specified IP/port.
Requires the following parameters:

- `ip`: Text Field: IP address of the device running `midi-relay`
- `port`: Text Field: TCP listening port for `midi-relay` (default of 4000)
- `midiport`: Text Field: MIDI port to send messages to
- `midicommand`: Menu: Items: `noteon`, `noteoff`
- `channel`: Text Field: Channel Number (0-15)
- `note`: Text Field: Note Number (0-127)
- `velocity`: Text Field: Velocity Number (0-127)

## ntfy.py

Allows you to send notifications to the [ntfy](https://ntfy.sh) service (or a custom ntfy server).
Requires the following parameters:

- `server`: Text Field: Server address for ntfy (default of https://ntfy.sh)
- `topic`: Text Field: Topic to send the notification to
- `useauth`:  Checkbox: Whether or not to use Authentication with the request (the default ntfy server does not require it)
- `authtype`: Menu: Items: (Basic Auth, Bearer Token), Default: “Basic Auth”
- `override`: Checkbox: Whether or not to override the headers with custom headers (useful for utilizing additional parameters I did not feel like implementing)
- `headers`: Text Box: All the custom headers, JSON format
- `title`: Text Field: Title to include with the notification
- `message`: Text Box: Message Body
- `priority`: Menu: Items: (Min, Low, Default, High, Max/Urgent), Default: “Default”
- `email`: Text Field: Email Address to also send notification to

## OBS

Allows you to control OBS Studio using the Websockets protocol.

* Requires the following parameters:
	* `host`: Text Field: IP Address of OBS computer.
	* `port`: Text Field: Port that OBS websockets is using. Example: `4455`
	* `password`: Text Field: Password that OBS websockets is using.
	* `command`: Menu: Command to send to OBS. Items: Start Stream, Stop Stream, Switch Scene
	* `destinationScene`: Text Field: Scene to switch to in OBS

*Copy the `obs` folder to your Cronicle server and then run `npm install` within that folder to install the dependencies.*

## panasonic_ptz.py

Allows you to control presets of your Panasonic PTZ.
Requires the following parameters:

- `ip`: Text Field: IP address of the camera
- `preset`: Text Field: Preset Number

## pco_live_vicreo.py

Allows you to use Cronicle to load the PCO LIVE page for your next plan in a service type automatically in Safari on the computer running VICREO Listener.
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `appid`: Hidden: AppID you set up in your PCO Developer Account for this application.
- `secret`: Hidden: Secret Key you set up in your PCO Developer Account for this application.
- `servicetype`: Text Field: PCO Service Type Id for plan you want to load the LIVE page for

## pco_print.py

Allows you to generate the PDF path needed to print Planning Center Services custom reports on a schedule. More information here: https://techministry.blog/2020/09/16/using-cronicle-the-planning-center-online-api-and-automator-on-a-mac-to-automate-printing-weekly-paperwork/
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `appid`: Hidden: AppID you set up in your PCO Developer Account for this application.
- `secret`: Hidden: Secret Key you set up in your PCO Developer Account for this application.
- `servicetypes`: Text Field: semicolon `;` delimited list of PCO Service Type Ids for plans you want to include in the report
- `reportid`: Text Field: Custom Report Id of the report you want to use
- `pagesize`: Menu: Items `A4`, `US-Letter`, `US-Legal`, `US-Tabloid`
- `printorientation`: Menu: Items `Portrait`, `Landscape`
- `printmargin`: Menu: Items `0.0in`, `0.25in`, `0.5in`, `0.75in`, `1.0in`

## ping.py

Performs a ping test to the hostname.

- `hostname`: Text Field: IP or host to ping
- `scenario`: Menu: Items `Test`, `Success`, `Failure`
- `timeout`: Text Field: Timeout in seconds so that it won't try to ping forever

* For `Test`: If it pings succesfully, the job succeeds. If it can't ping, it fails.
* For `Success`: It will ping the hostname until it succeeds (or hits the timeout). This lets you use the job with chaining, to only do something once it is online.
* For `Failure`: Same as Success, but with fail. It will ping until it fails to respond (or hits the timeout). This lets you do something once the host has gone offline.

## rock_workflow.py

Allows you to send data to a Rock RMS workflow via webhook. Specifically designed to use a workflow that sends texts/emails to a Rock Group in the event that a Cronicle job fails, or to simply send a notfication at a certain time.
Requires the following parameters:

- `workflowid`: Hidden: The ID of the workflow to run
- `groupid`: Text Field: The Group ID to send the notification to
- `type`: Menu: Items `SMS`, `Email`
- `subject`: Text Field
- `body`: Text Field
- `token`: Hidden: Auth token to authenticate the webhook request
- `workflowurl` Hidden: Complete URL to Rock server and workflow entry API (`/api/Workflows/WorkflowEntry/`)

## rosstalk.py

Allows commands to be sent to any device that accepts RossTalk commands.
Requires the following parameters:

- `ip`: Text Field: IP Address of the Ross switcher
- `port`: Text Field: Port of the switcher (default of 7788)
- `command`: RossTalk command to send (send multiple commands in the same string by separating them with semicolons `;`) For a list of RossTalk commands: http://help.rossvideo.com/carbonite-device/Topics/Protocol/RossTalk/CNT/RT-CNT-Comm.html

## Smartcast

Allows you to control Vizio TVs with Smartcast.

Requires the following parameters:

- `ip`: Text Field: IP Address of the TV
- `port`: Text Field: Port (7345 or 9000 - older tv's use 9000)
- `token`: Text Field: Auth Token
- `command`: Menu: Items (`Power On`, `Power Off`, `Change Input`)
- `input`: Text Field: Input Name (`HDMI-1`) if changing the input

*Copy the `smartcast` folder to your Cronicle server and then run `npm install` within that folder to install the dependencies.*

## spotify-controller.py

Allows you to send commands via the REST API to [spotify-controller](http://github.com/josephdadams/spotify-controller).
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running spotify-controller
- `command`: Menu: Items: (`Play`, `Play Track`, `Play Track In Context`, `Pause`, `Play Toggle`, `Next`, `Previous`, `Volume Up`, `Volume Down`, `Set Volume`, `Ramp Volume`, `Mute`, `Unmute`, `Repeat On`, `Repeat Off`, `Repeat Toggle`, `Shuffle On`, `Shuffle Off`, `Shuffle Toggle`
- `trackid`: Text Field: Track ID to play
- `contextid`: Text Field: Context of Track ID
-  `volume`: Text Field: Volume Level (0-100)

## shure_charger.py

Allows you to check if your Shure batteries in your SBC220 or SBC240 are present in the dock. Useful to make sure people put the mics back on charge after an event.
Requires the following parameters:

- `ip`: Text Field: IP Address of the Shure charger
- `room_name`: Text Field: Friendly name of the room/location of this charger, for the chain message.

It currently only checks for Battery Detection in Slots 1 & 2. If both are present, the job will succeed. If one or both are missing, the job will fail and print a message for job chaining. Then you can set a chaining job to send a notification, for example.

## symetrix_dsp.py

Allows you to update dB values for controller inputs on your Symetrix DSP over TCP.
Requires the following parameters:

- `ip`: Text Field: IP address of the device running Bitfocus Companion
- `port`: Hidden Field: TCP port (default should be "48631")
- `controller`: Text Field: Controller Number / Input to adjust. Might need to be 0-based depending on your configuration.
- `db`: Text Field: dB value to adjust to. The plugin uses this formula to calculate the Controller Position: Volume dB = -72 + 84\*(CONTROLLER POSITION/65535)

## timekeeper.py

Allows commands to be sent to a [TimeKeeper](http://github.com/josephdadams/timekeeper) server to set up timers automatically.
Requires the following parameters:

- `ip`: Text Field: IP Address of the TimeKeeper server
- `port`: Text Field: Port of the server (usually 4000)
- `date`: Text Field: Date you want to use for the timer. Must be M/D/YY. Keep blank and it will use "today's date" (based on the server)
- `time`: Text Field: Time you want to use for the timer. Must be H:M:S. Keep blank and it will use 6AM.
- `label`: Text Field: The label for the timer.
- `roomid`: Text Field: The room ID to target. You can use `room-0` to target all rooms.
- `timerid`: Text Field: The Timer ID, if you want to choose it explicitly rather than having it auto generated.
- `triggers`: Text Box: JSON Object Array for triggers. See [TimeKeeper documentation](http://github.com/josephdadams/timekeeper) for more information.

## tplink-hs100.py

Allows you to turn on/off TP-Link HS100 Wifi Outlets.
Requires the following parameters:

- `ip`: Text Field: IP address of the HS100 outlet. Recommend you set a DHCP reservation for the outlet if you do not want this to change.
- `command`: Menu: Command to send. Items: `on`, `off`

## tplink-kasa-offon.py

Turns a TP Link Kasa Plug Off, waits the specified delay time in seconds, and then turns the plug back on. Helpful to avoid multiple events just to turn on a device that might need to be turned off before it will boot up on power.
Requires the following parameters:

- `ip`: Text Field: IP address of the HS100 outlet. Recommend you set a DHCP reservation for the outlet if you do not want this to change.
- `delay`: Text Field: Delay time in seconds to wait between turning the plug off and then back on. Default of 5 seconds.

## vicreo_applescript.py

Allows AppleScripts to be executed on the remote computer running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software, provided that the remote computer is MacOS.

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `applescript`: Text Box: The AppleScript to execute. Recommend you test it locally on the remote computer first to ensure proper syntax of the AppleScript. Any necessary `'` or `"` marks must be escaped (i.e. `\'` or `\"`).
- `password`: Text Box: _optional_ If your instance of VICREO Listener has a password set, then include this.

## vicreo_file.py

Allows files and programs to be opened on remote computers running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software.
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `path`: Text Field: File to open or Program to execute on the remote computer
- `password`: Text Box: _optional_ If your instance of VICREO Listener has a password set, then include this.

## vicreo_key.py

Allows hotkeys to be sent to a remote computer running VICREO Listener.
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `key`: Menu: Remote key to press
  - Items: backspace, delete, enter, tab, escape, up, down, right, left, home, end, pageup, pagedown, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, command, alt, control, shift, right_shift, space, audio_mute, audio_vol_down, audio_vol_up, audio_play, audio_stop, audio_pause, audio_prev, audio_next, numpad_0, numpad_1, numpad_2, numpad_3, numpad_4, numpad_5, numpad_6, numpad_7, numpad_8, numpad_9, lights_mon_up, lights_mon_down, lights_kbd_toggle, lights_kbd_up, lights_kbd_down
- `modifiers_shift`: Checkbox
- `modifiers_fn`: Checkbox
- `modifiers_ctrl`: Checkbox
- `modifiers_command`: Checkbox
- `modifiers_alt`: Checkbox
- `modifiers_rightshift`: Checkbox
- `modifiers_rightalt`: Checkbox
- `modifiers_rightctrl`: Checkbox
- `password`: Text Box: _optional_ If your instance of VICREO Listener has a password set, then include this.

## vicreo_shell.py

Allows shell scripts to be executed on remote computers running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software.
Requires the following parameters:

- `ip`: Text Field: IP Address of the computer running VICREO Listener
- `port`: Text Field: Port of the VICREO program (default of 10001)
- `shell`: Text Field: Shell script/command execute on the remote computer
- `password`: Text Box: _optional_ If your instance of VICREO Listener has a password set, then include this.

## videohub.py

Allows destinations routes to be changed on Blackmagic VideoHub devices.
Requires the following parameters:

- `ip`: Text Field: IP Address of the VideoHub
- `destination`: Destination to change (not zero-based, use the actual number)
- `source`: Source to use (not zero-based)

## videohub_bulk.py

Allows destinations routes to be changed **in bulk** on Blackmagic VideoHub devices.
Requires the following parameters:

- `ip`: Text Field: IP Address of the VideoHub
- `routes`: Text Box: A list of Destinations and their new Sources, not zero-based, separated by a space

	Example: This routes Destinations 53 and 54 to Source 7
	```
	53 7
	54 7
	```

## vista.py

Allows cues to be triggered on Chroma-Q/Jands Vista consoles, provided they are configured to respond to midi messages via [midi-relay](http;//github.com/josephdadams/midi-relay)
Requires the following parameters:

- `ip`: Text Field: IP Address of Vista computer/console
- `midiport`: Text Field: MIDI port to send messages to
- `cuelist`: Text Field: Cue List that contains Cue to trigger
- `cue`: Text Field: Cue to trigger

## wakeonlan.py

Allows magic packets to be sent to the specified MAC address. Requires the `wakeonlan` command line function. You can install this on Ubuntu with `sudo apt-get install wakeonlan`
Requires the following parameters:

- `mac`: Text Field: MAC Address of the device you want to send the magic packet to.
