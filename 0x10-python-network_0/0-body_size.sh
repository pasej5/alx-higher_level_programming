#!/bin/bash
# Bash script that takes in a URL
#displays the size of the body of the response of a given url
#sends a request to that URL
curl -s "$1" | wc -c
