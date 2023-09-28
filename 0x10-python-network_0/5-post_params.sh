#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Extract the URL from the command line argument
url="$1"

# Set the email and subject parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request to the URL with the specified parameters
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")
echo "$response"
