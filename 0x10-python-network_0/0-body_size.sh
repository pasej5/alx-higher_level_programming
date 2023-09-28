#!/usr/bin/env python3
"""
This script takes a URL as an argument, sends a request to the URL using the 'requests' library,
and prints the size of the response body in bytes.

Usage:
    python3 script.py <URL>

Example:
    python3 script.py https://www.example.com
"""

import sys
import requests

def main():
    # Check if a URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    # Extract the URL from the command line argument
    url = sys.argv[1]

    try:
        # Send a request to the URL and save the response
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the size of the response body in bytes
            body_size = len(response.content)
            print(body_size)
        else:
            print(f"Error: Failed to retrieve the URL (Status Code: {response.status_code})")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
