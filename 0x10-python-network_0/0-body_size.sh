#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Extract the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and save the response to a temporary file
response=$(curl -s -o /tmp/curl_response "$url")

# Check if the curl command was successful
if [ $? -eq 0 ]; then
  # Use the 'wc' command to count the number of bytes in the response body
  body_size=$(wc -c < /tmp/curl_response)
  echo "$body_size"
else
  echo "Error: Failed to retrieve the URL."
  exit 1
fi

# Clean up the temporary file
rm -f /tmp/curl_response
