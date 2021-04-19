# CroniclePlugins
Plugins I have created to use with Cronicle (https://github.com/jhuckaby/Cronicle)

Create a new plugin in Cronicle and upload each script to the Cronicle server. You can make the scripts directly executable by using `chmod +x plugin.py` and then just specify the path to the file for the plugin to execute.

Read more about how I am using these plugins here: https://techministry.blog/2020/07/16/automating-production-equipment-using-a-chromebox-and-a-scheduling-server/

## companion.py
Allows buttons in Bitfocus Companion to be pressed remotely.
Requires the following parameters:
* `ip`: Text Field: IP address of the device running Bitfocus Companion
* `port`: Text Field: TCP listening port in Companion (default of 51234)
* `page`: Text Field: Page that the button is on that you want to execute
* `button`: Text Field: Button number on that page that you want to execute

## generic_tcp.py
Allows you to send generic TCP strings to the specified IP/port.
Requires the following parameters:
* `ip`: Text Field: IP address of the device running Bitfocus Companion
* `port`: Text Field: TCP listening port in Companion (default of 51234)
* `message`: Text Field: Message string you want to send. Automatically sends `\n` at the end.

## midi_note.py
Allows you to send MIDI notes via [midi-relay](http://github.com/josephdadams/midi-relay/) to the specified IP/port.
Requires the following parameters:
* `ip`: Text Field: IP address of the device running `midi-relay`
* `port`: Text Field: TCP listening port for `midi-relay` (default of 4000)
* `midiport`: Text Field: MIDI port to send messages to
* `midicommand`: Menu: Items: `noteon`, `noteoff`
* `channel`: Text Field: Channel Number (0-15)
* `note`: Text Field: Note Number (0-127)
* `velocity`: Text Field: Velocity Number (0-127)

## pco_print.py
Allows you to generate the PDF path needed to print Planning Center Services custom reports on a schedule. More information here: https://techministry.blog/2020/09/16/using-cronicle-the-planning-center-online-api-and-automator-on-a-mac-to-automate-printing-weekly-paperwork/
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running VICREO Listener
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `appid`: Text Field: AppID you set up in your PCO Developer Account for this application.
* `secret`: Text Field: Secret Key you set up in your PCO Developer Account for this application.
* `servicetypes`: Text Field: semicolon `;` delimited list of PCO Service Type Ids for plans you want to include in the report
* `reportid`: Text Field: Custom Report Id of the report you want to use
* `pagesize`: Menu: Items `A4`, `US-Letter`, `US-Legal`, `US-Tabloid`
* `printorientation`: Menu: Items `Portrait`, `Landscape`
* `printmargin`: Menu: Items `0.0in`, `0.25in`, `0.5in`, `0.75in`, `1.0in` 

## rosstalk.py
Allows commands to be sent to any device that accepts RossTalk commands.
Requires the following parameters:
* `ip`: Text Field: IP Address of the Ross switcher
* `port`: Text Field: Port of the switcher (default of 7788)
* `command`: RossTalk command to send (send multiple commands in the same string by separating them with semicolons `;`) For a list of RossTalk commands: http://help.rossvideo.com/carbonite-device/Topics/Protocol/RossTalk/CNT/RT-CNT-Comm.html

## tplink-hs100.py
Allows you to turn on/off TP-Link HS100 Wifi Outlets.
Requires the following parameters:
* `ip`: Text Field: IP address of the HS100 outlet. Recommend you set a DHCP reservation for the outlet if you do not want this to change.
* `command`: Menu: Command to send. Items: `on`, `off`

## vicreo_applescript.py
Allows AppleScripts to be executed on the remote computer running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software, provided that the remote computer is MacOS.
* `ip`: Text Field: IP Address of the computer running VICREO Listener
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `applescript`: Text Box: The AppleScript to execute. Recommend you test it locally on the remote computer first to ensure proper syntax of the AppleScript. Any necessary `'` or `"` marks must be escaped (i.e. `\'` or `\"`).

## vicreo_file.py
Allows files and programs to be opened on remote computers running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software.
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running VICREO Listener
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `path`: Text Field: File to open or Program to execute on the remote computer

## vicreo_key.py
Allows hotkeys to be sent to a remote computer running VICREO Listener.
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running VICREO Listener
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `key`: Menu: Remote key to press
  * Items: backspace, delete, enter, tab, escape, up, down, right, left, home, end, pageup, pagedown, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, command, alt, control, shift, right_shift, space, audio_mute, audio_vol_down, audio_vol_up, audio_play, audio_stop, audio_pause, audio_prev, audio_next, numpad_0, numpad_1, numpad_2, numpad_3, numpad_4, numpad_5, numpad_6, numpad_7, numpad_8, numpad_9, lights_mon_up, lights_mon_down, lights_kbd_toggle, lights_kbd_up, lights_kbd_down
* `modifiers_shift`: Checkbox
* `modifiers_fn`: Checkbox
* `modifiers_ctrl`: Checkbox
* `modifiers_command`: Checkbox
* `modifiers_alt`: Checkbox
* `modifiers_rightshift`: Checkbox
* `modifiers_rightalt`: Checkbox
* `modifiers_rightctrl`: Checkbox

## vicreo_shell.py
Allows shell scripts to be executed on remote computers running the free [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/) software.
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running VICREO Listener
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `shell`: Text Field: Shell script/command execute on the remote computer

## videohub.py
Allows destinations routes to be changed on Blackmagic VideoHub devices.
Requires the following parameters:
* `ip`: Text Field: IP Address of the VideoHub
* `destination`: Destination to change (not zero-based, use the actual number)
* `source`: Source to use (not zero-based)

## vista.py
Allows cues to be triggered on Chroma-Q/Jands Vista consoles, provided they are configured to respond to midi messages via [midi-relay](http;//github.com/josephdadams/midi-relay)
Requires the following parameters:
* `ip`: Text Field: IP Address of Vista computer/console
* `midiport`: Text Field: MIDI port to send messages to
* `cuelist`: Text Field: Cue List that contains Cue to trigger
* `cue`: Text Field: Cue to trigger

## wakeonlan.py
Allows magic packets to be sent to the specified MAC address. Requires the `wakeonlan` command line function. You can install this on Ubuntu with `sudo apt-get install wakeonlan`
Requires the following parameters:
* `mac`: Text Field: MAC Address of the device you want to send the magic packet to.
