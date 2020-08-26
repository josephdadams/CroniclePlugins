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
* `command`: Menu: Command to send
 * Items: on, off

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
