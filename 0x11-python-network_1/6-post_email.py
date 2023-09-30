#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
The email must be sent in the variable email
use the packages requests and sys
"""

import requests
import sys
if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
