# CroniclePlugins
Plugins I have created to use with Cronicle (https://github.com/jhuckaby/Cronicle)

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
