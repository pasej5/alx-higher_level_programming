#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Extract the URL from the command line argument
url="$1"

# Use curl to send a GET request to the URL with the custom header
response=$(curl -s -H "X-School-User-Id: 98" "$url")
echo "$response"
