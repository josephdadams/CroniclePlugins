# CroniclePlugins
Plugins I have created to use with Cronicle (https://github.com/jhuckaby/Cronicle)

Create a new plugin in Cronicle and upload each script to the Cronicle server. You can make the scripts directly executable by using `chmod +x plugin.py` and then just specify the path to the file for the plugin to execute.

Read more about how I am using these plugins here: https://techministry.blog/2020/07/16/automating-production-equipment-using-a-chromebox-and-a-scheduling-server/

## rosstalk.py
Requires the following parameters:
* `ip`: Text Field: IP Address of the Ross switcher
* `port`: Text Field Port of the switcher (default of 7788)
* `command`: RossTalk command to send (send multiple commands in the same string by separating them with semicolons `;`) For a list of RossTalk commands: http://help.rossvideo.com/carbonite-device/Topics/Protocol/RossTalk/CNT/RT-CNT-Comm.html

## vicreo_file.py
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/)
* `port`: Text Field: Port of the VICREO program (default of 10001)
* `path`: Text Field: Path to execute on the remote program

## vicreo_key.py
Requires the following parameters:
* `ip`: Text Field: IP Address of the computer running [VICREO Listener](https://jeffreydavidsz.github.io/VICREO-Listener/)
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

## videohub.py
Requires the following parameters:
* `ip`: Text Field: IP Address of the VideoHub
* `destination`: Destination to change (not zero-based, use the actual number)
* `source`: Source to use (not zero-based)
