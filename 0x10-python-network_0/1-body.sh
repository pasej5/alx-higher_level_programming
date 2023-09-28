#!/bin/bash
# Displays the size of the body of the response of a given URL with a 200 status code

response=$(curl -s -w "%{http_code}" "$1")

# Check if the response code is 200
if [ "$response" == "200" ]; then
    curl -s "$1" | sed -n '/^$/,$p' | tail -n +2
else
    echo "The response status code is not 200."
fi
