#!/bin/bash
# This script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -siL "${1}" | tail -n 1
