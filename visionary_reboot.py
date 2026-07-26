#!/usr/bin/python3

# File name: visionary_reboot.py
# Version: 1.0.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/25/2026
# Description: Reboots a Visionary Solutions encoder/decoder using the wapi.cgi endpoint.
#
# Cronicle stdin example:
# {
#   "params": {
#     "ip": "10.40.51.22",
#     "username": "admin",
#     "password": "admin",
#     "timeout": 10
#   }
# }

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

def main():
    stdinput = sys.stdin.readline()
    data = json.loads(stdinput) if stdinput.strip() else {}
    params = data.get('params', {})

    ip = params.get('ip', '').strip()
    username = params.get('username', 'admin')
    password = params.get('password', 'admin')
    timeout = float(params.get('timeout', 10) or 10)

    if not ip:
        raise Exception("Missing IP address")

    url = f"http://{ip}/cgi-bin/wapi.cgi"

    # CMD=START and CMD=END wrap the command list and the order matters, so the
    # query string is built manually to allow the duplicated CMD key.
    query = "CMD=START&UNIT.ID=ALL&REBOOT=TRUE&CMD=END"

    print(f"Requesting: {url}?{query}")

    resp = requests.get(
        f"{url}?{query}",
        auth=HTTPBasicAuth(username, password),
        headers={"Accept": "*/*", "User-Agent": "Cronicle-Visionary/1.0"},
        timeout=timeout,
    )

    print(f"HTTP {resp.status_code}")
    print(resp.text)

    if resp.status_code == 401:
        raise Exception(f"Authentication failed for {ip} (HTTP 401)")

    if resp.status_code != 200:
        raise Exception(f"Device {ip} returned HTTP {resp.status_code}")

    if "API.STATUS=SUCCESS" not in resp.text:
        raise Exception(f"Device {ip} did not report a successful reboot")

    msg = f"Reboot command sent to Visionary device at {ip}"
    print(json.dumps({
        "complete": 1,
        "code": 0,
        "description": msg,
        "chain_data": {"message": msg}
    }))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {e}")
        print(json.dumps({
            "complete": 1,
            "code": 999,
            "description": str(e),
            "chain_data": {"message": str(e)}
        }))
        sys.exit(1)
