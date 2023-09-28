#!/bin/bash
# This line is a shebang that specifies to use the Bash interpreter to run the script.

# Takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -i "$1" | grep -i "allow" | tr -d '\r' | awk -F ': ' '{print $2}'
