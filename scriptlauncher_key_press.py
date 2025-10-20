#!/usr/bin/env python3
import json, requests, sys

data = json.load(sys.stdin)
host = data.get("scriptlauncher_host", "http://localhost:8810")
password = data.get("password", "admin22")
key = data.get("key", "a")
modifiers = data.get("modifiers", [])

params = {
    "command": "sendInput",
    "password": password,
    "type": "keyPress",
    "key": key,
    "modifiers": modifiers
}

r = requests.post(f"{host}/command", json=params)
print(r.text)