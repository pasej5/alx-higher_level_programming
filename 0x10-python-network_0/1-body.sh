#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Extract the URL from the command line argument
url="$1"

# Use curl to send a GET request to the URL and save the response to a variable
response=$(curl -s -w "%{http_code}" "$url")

# Extract the HTTP status code from the response
http_status=$(tail -n1 <<< "$response")

# Check if the HTTP status code is 200 (OK)
if [ "$http_status" -eq 200 ]; then
  # Display the response body
  body=$(sed '$d' <<< "$response")
  echo "$body"
else
  echo "Error: HTTP status code $http_status"
  exit 1
fi
