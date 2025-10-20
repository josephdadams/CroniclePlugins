#!/usr/bin/python3

# File name: exterity_decoder.py
# Version: 1.0.0
# Author: Joseph Adams
# Date created: 10/20/2025
# Description: Checks AvediaPlayer status. Passes only if:
#              - playState == "Playing"
#              - decode.video == "Decoding"
#              Uses /cgi-bin/index.json to resolve the device Name.
#
# Cronicle stdin example:
# {
#   "params": {
#     "ip": "10.20.14.10",
#     "username": "admin",
#     "password": "labrador",
#     "timeout": 10,
#   }
# }

import json, requests, sys, time, random, string
from requests.auth import HTTPBasicAuth

def rand_id(n=10):
    alphabet = string.ascii_lowercase + string.digits
    return ''.join(random.choice(alphabet) for _ in range(n))

def get_decoder_name(ip, auth, timeout):
    """
    Resolve a friendly decoder name.
    Order:
      1) index.json -> first segment of "title" (before ' - ')
      2) fallback to IP
    """

    headers = {"User-Agent": "Cronicle-Check/1.1", "Accept": "application/json"}

    # 2) Try /cgi-bin/index.json (Basic Auth required)
    try:
        r = requests.get(f"http://{ip}/cgi-bin/index.json",
                         headers=headers, auth=auth, timeout=timeout)
        if r.ok:
            payload = r.json()

            # Prefer parsing from title:
            title = payload.get("title")
            if isinstance(title, str) and title.strip():
                # Example: "Nursing Mother's Room - Nursing Mother's Room - AvediaPlayer r9300"
                first_dash = title.find(" - ")
                if first_dash > 0:
                    name = title[:first_dash].strip()
                else:
                    # fallback: split on '-' and take first non-empty
                    parts = [p.strip() for p in title.split("-") if p.strip()]
                    name = parts[0] if parts else ""
                if name:
                    return name
            # (Do NOT use 'Name' here — in index.json it's just the field schema, not the value.)
    except Exception:
        pass

    # 2) fallback
    return ip

if __name__ == "__main__":
    try:
        # Read Cronicle stdin
        stdinput = sys.stdin.readline()
        data = json.loads(stdinput) if stdinput.strip() else {}
        params = data.get('params', {})

        ip = params.get('ip')
        username = params.get('username', 'admin')
        password = params.get('password', 'labrador')
        timeout = float(params.get('timeout', 10))

        if not ip:
            print(json.dumps({"error": "Device IP not set"}))
            print('{ "complete": 1, "code": 999, "description": "Missing IP" }')
            sys.exit(1)

        auth = HTTPBasicAuth(username, password)

        # Resolve friendly decoder name from /cgi-bin/index.json
        decoder_name = get_decoder_name(ip, auth, timeout)

        # Build status request to /cgi-bin/json_xfer
        base = f"http://{ip}/cgi-bin/json_xfer"
        query = {
            "play_status": "true",
            "audio_tracks": "true",
            "subtitle_tracks": "true",
            "teletext_tracks": "true",
            "video_info": "true",
            "play_error": "true",
            "currentMode": "true",
            "displayWebpage": "true",
            "volstatus": "true",
            "cur_webpage": "true",
            "playState": "true",
            "outputScreenResolution": "true",
            "aspectRatio": "true",
            "edidStatus": "true",
            "rebooting": "true",
            "network_change": "true",
            "hostname_error": "true",
            "mismatch": "true",
            "tftp_error": "true",
            "upgrading": "true",
            "tv": "true",
            "decode": "true",
            "req_id": rand_id(),
            "_": str(int(time.time() * 1000)),
        }

        headers = {
            "User-Agent": "Cronicle-Check/1.1",
            "Accept": "application/json,text/plain,*/*",
        }

        url = requests.Request("GET", base, params=query).prepare().url
        print(f"Requesting: {url}")

        resp = requests.get(base, params=query, headers=headers, auth=auth, timeout=timeout)
        print(f"HTTP {resp.status_code}")

        if resp.status_code != 200:
            print(resp.text[:500])
            desc = f"{decoder_name} FAIL: HTTP {resp.status_code}"
            print(f'{{ "complete": 1, "code": 999, "description": "{desc}", "chain_data": {{ "message": "{desc}" }} }}')
            sys.exit(1)

        try:
            payload = resp.json()
        except Exception as je:
            print("Failed to parse JSON response")
            print(str(je))
            print(resp.text[:500])
            desc = f"{decoder_name} FAIL: Invalid JSON from device"
            print(f'{{ "complete": 1, "code": 999, "description": "{desc}", "chain_data": {{ "message": "{desc}" }} }}')
            sys.exit(1)

        play_state = str(payload.get("playState", "")).strip()
        decode_video = ""
        decode = payload.get("decode")
        if isinstance(decode, dict):
            decode_video = str(decode.get("video", "")).strip()

        print(f"playState={play_state}, decode.video={decode_video}")

        if play_state == "Playing" and decode_video == "Decoding":
            desc = f"{decoder_name} OK: Playing and Decoding"
            print(f'{{ "complete": 1, "description": "{desc}", "chain_data": {{ "message": "{desc}" }} }}')
            sys.exit(0)
        else:
            desc = f"{decoder_name} FAIL: playState=\'{play_state or "UNKNOWN"}\', decode.video=\'{decode_video or "UNKNOWN"}\'"
            print(f'{{ "complete": 1, "code": 999, "description": "{desc}", "chain_data": {{ "message": "{desc}" }} }}')
            sys.exit(1)

    except Exception as e:
        print("Error:")
        print(str(e))
        print('{ "complete": 1, "code": 999, "description": "Unexpected failure." }')
        sys.exit(1)