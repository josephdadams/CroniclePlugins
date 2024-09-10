#!/usr/bin/python3

# File name: ping.py
# Version: 1.1.0
# Author: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/11/2024
# Date last modified: 9/10/2024

import sys
import json
import subprocess
import time

def send_output(complete, code=None, description="", chain_data=None):
    """
    Send the output in a standard JSON format.
    """
    output = {
        "complete": complete,
        "description": description,
        "chain_data": chain_data or {}
    }
    
    # Only include the 'code' field if it is not None
    if code is not None:
        output["code"] = code
    
    print(json.dumps(output))

def ping_until_up(host, return_code, timeout):
    """
    Pings a host until the specified return code is met or timeout occurs.
    """
    ping_seconds = 0
    while ping_seconds <= timeout:
        print(f"Pinging {host}...")
        status = subprocess.run(["ping", "-c", "3", host], capture_output=True)
        print(f"Return Code: {status.returncode}")
        if status.returncode == return_code:
            return return_code
        ping_seconds += 1
        time.sleep(1)
    return "timeout"

def main():
    try:
        stdinput = sys.stdin.readline()
        data = json.loads(stdinput)
        
        hostname = data['params'].get('hostname', '')
        scenario = data['params'].get('scenario', '')
        timeout = data['params'].get('timeout', 20)

        # Validate inputs
        if not hostname:
            send_output(1, 999, "Hostname is required.")
            return
        
        try:
            timeout = int(timeout)
        except ValueError:
            send_output(1, 999, "Timeout must be an integer.")
            return

        print(f'Ping Scenario: {scenario}')
        response = -1

        if scenario == "Success":
            print('Entering Success scenario')
            response = ping_until_up(hostname, 0, timeout)
            if response == 0:
                message = f"Ping to host {hostname} succeeded."
                send_output(complete=1, description=message, chain_data={"message": message})
            else:
                message = f"Ping to host {hostname} failed. (This is a success scenario, but the host is down and the request hit the max timeout of {timeout} seconds)"
                send_output(complete=1, code=999, description=message, chain_data={"message": message})
        
        elif scenario == "Failure":
            print('Entering Failure scenario')
            response = ping_until_up(hostname, 1, timeout)
            if response == 1:
                message = f"Ping to host {hostname} failed."
                send_output(complete=1, description=message, chain_data={"message": message})
            else:
                message = f"Ping to host {hostname} succeeded. (This is a failure scenario, but the host is up and the request hit the max timeout of {timeout} seconds)"
                send_output(complete=1, code=999, description=message, chain_data={"message": message})
        
        else:
            print('Pinging host once')
            response = subprocess.run(["ping", "-c", "1", hostname], capture_output=True).returncode
            if response == 0:
                message = f"Ping to host {hostname} succeeded."
                send_output(complete=1, description=message, chain_data={"message": message})
            else:
                message = f"Ping to host {hostname} failed."
                send_output(complete=1, code=999, description=message, chain_data={"message": message})
    
    except Exception as e:
        send_output(1, 999, f"Failed to execute. Error: {str(e)}")

if __name__ == "__main__":
    main()
