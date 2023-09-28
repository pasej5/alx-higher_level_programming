#!/usr/bin/bash
#Script that sends a delete to the first argument
curl -sX DELETE "$1"
