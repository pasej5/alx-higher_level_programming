#!/usr/bin/python3
import urllib.request
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response
html = response.read().decode('utf-8')
