#!/bin/bash
#displays all HTTP methods the server 
curl -siX OPTIONS "$1" | awk -F ': ' '/^Allow:/ {print $2}'
