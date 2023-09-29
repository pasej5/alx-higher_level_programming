#!/usr/bin/paython3
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:

    html = response.read().decode('utf-8')
print("Body response:")
print("    - type:", type(html))
print("    - content:", html)
print("    - utf8 content:", html)
