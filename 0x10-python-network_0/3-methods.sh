#!/bin/bash
#displays all HTTP methods the server 
curl -s -X OPTIONS -i "$1" | grep -i "allow" | tr -d '\r' | awk -F ': ' '{print $2}'
