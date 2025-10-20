#!/usr/bin/python3

# File name: speedtest.py
# Version: 1.0.0
# Author: Matthew Meekins
# Maintainer: Joseph Adams
# Email: josephdadams@gmail.com
# Date created: 7/8/2025
# Date last modified: 7/8/2025

# Checks to see amount of available space on the Ki Pro. If the percentage is >= the threshhold, the job succeeds. If it is less, it fails.
# Job succeed/error chaining is then used to send an alert if needed

import sys
import json
import subprocess
import os

# Define the path where the speedtest-cli executable might be found.
# This assumes it's installed globally or in a common bin directory.
# You might need to adjust this if speedtest-cli is in a specific virtual environment.
SPEEDTEST_CLI_PATH = "/root/.local/bin/speedtest" # Assumes it's in the system's PATH

def run_speed_test():
    """
    Executes speedtest-cli and returns the parsed JSON output.
    """
    try:
        # Use --json flag to get structured output
        # Use --no-pre-allocate to avoid issues on some systems
        command = [SPEEDTEST_CLI_PATH, "--json", "--no-pre-allocate"]
        
        # Run the command and capture output
        # `text=True` decodes stdout/stderr as text
        # `check=True` raises CalledProcessError if the command returns a non-zero exit code
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the JSON output
        speed_data = json.loads(result.stdout)
        return speed_data

    except FileNotFoundError:
        print(f"Error: '{SPEEDTEST_CLI_PATH}' command not found.", file=sys.stderr)
        print("Please ensure speedtest-cli is installed and accessible in your system's PATH.", file=sys.stderr)
        print('{ "complete": 1, "code": 999, "description": "Speedtest-CLI not installed." }')
        sys.exit(1) # Exit with error code
    except subprocess.CalledProcessError as e:
        print(f"Error executing speedtest-cli: {e}", file=sys.stderr)
        print(f"STDOUT: {e.stdout}", file=sys.stderr)
        print(f"STDERR: {e.stderr}", file=sys.stderr)
        print('{ "complete": 1, "code": 999, "description": "Error executing speedtest-cli." }')
        sys.exit(1) # Exit with error code
    except json.JSONDecodeError:
        print("Error: Could not parse JSON output from speedtest-cli.", file=sys.stderr)
        print('{ "complete": 1, "code": 999, "description": "Could not parse JSON output." }')
        sys.exit(1) # Exit with error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        print('{ "complete": 1, "code": 999, "description": "Unexpected error." }')
        sys.exit(1) # Exit with error code

def main():
    """
    Main function to run the speed test and print results.
    """
    print("Starting internet speed test...")

    stdinput = sys.stdin.readline()
    data = json.loads(stdinput)

    min_download_mbps = int(data['params']['min_download'])
    min_upload_mbps = int(data['params']['min_upload'])

    print("\n--- Internet Speed Test Minimums ---")
    print(f"Min Download Speed: {min_download_mbps:.2f} Mbps")
    print(f"Min Upload Speed:   {min_upload_mbps:.2f} Mbps")
    print("-----------------------------------\n\n")

    speed_data = run_speed_test()

    if speed_data:
        # speedtest-cli reports speeds in bits per second. Convert to Mbps.
        download_bps = speed_data.get('download')
        upload_bps = speed_data.get('upload')

        if download_bps is not None and upload_bps is not None:
            download_mbps = download_bps / 1_000_000
            upload_mbps = upload_bps / 1_000_000

            # Print results to stdout for Cronicle to capture in logs
            print("\n--- Internet Speed Test Results ---")
            print(f"Download Speed: {download_mbps:.2f} Mbps")
            print(f"Upload Speed:   {upload_mbps:.2f} Mbps")
            print("-----------------------------------\n\n")

            # Optionally, you can print more details if needed
            print(f"Ping: {speed_data.get('ping', 'N/A')} ms")
            print(f"Server: {speed_data.get('server', {}).get('sponsor', 'N/A')} ({speed_data.get('server', {}).get('name', 'N/A')})")
            print(f"Location: {speed_data.get('server', {}).get('country', 'N/A')}, {speed_data.get('server', {}).get('cc', 'N/A')}")
            print(f"ISP: {speed_data.get('isp', 'N/A')}")

            if (upload_mbps < min_upload_mbps):
              msg = f'Speed Test Failed: Min Upload Required: {min_upload_mbps}  Actual Upload Tested: {upload_mbps:.2f}'
              print(f'{{ "complete": 1, "code": 999, "description": "{msg}", "chain_data": {{ "message": "{msg}" }} }}')
              # fail for upload
            elif (download_mbps < min_download_mbps):
              # fail for download
              msg = f'Speed Test Failed: Min Download Required: {min_download_mbps}  Actual Download Tested: {download_mbps:.2f}'
              print(f'{{ "complete": 1, "code": 999, "description": "{msg}", "chain_data": {{ "message": "{msg}" }} }}')
            else:
              # good
              msg = f'Speed Test Passed: Download: {download_mbps:.2f} Mbps, Upload: {upload_mbps:.2f} Mbps'
              print(f'{{ "complete": 1, "code": 0, "description": "{msg}", "chain_data": {{ "message": "{msg}" }} }}')
            sys.exit(0) # Exit with success code
        else:
            msg = "Speed Test Failed: No download or upload speed data found."
            print("Error: Download or upload speed data not found in speedtest-cli output.", file=sys.stderr)
            print(f'{{ "complete": 1, "code": 999, "description": "{msg}", "chain_data": {{ "message": "{msg}" }} }}')
            sys.exit(1) # Exit with error code
    else:
        msg = "Speed Test Failed: No speed test data returned."
        print("Error: No speed test data returned.", file=sys.stderr)
        print(f'{{ "complete": 1, "code": 999, "description": "{msg}", "chain_data": {{ "message": "{msg}" }} }}')
        sys.exit(1) # Exit with error code

if __name__ == "__main__":
    main()