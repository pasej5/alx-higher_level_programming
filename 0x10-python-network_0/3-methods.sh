#!/bin/bash
#Script that takes in a URL and displays all method
curl -s -X OPTIONS -i "$1" | awk
