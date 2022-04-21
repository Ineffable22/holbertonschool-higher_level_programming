#!/bin/bash
# This script takes in a URL and displays the size of the body of the response
curl -s -I ${1} | grep "Content-Length" | cut -d " " -f 2
