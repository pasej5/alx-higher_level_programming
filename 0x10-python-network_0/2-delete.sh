#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Extract the URL from the command line argument
url="$1"

# Use curl to send a DELETE request to the URL and display the response body
response=$(curl -s -X DELETE "$url")
echo "$response"
