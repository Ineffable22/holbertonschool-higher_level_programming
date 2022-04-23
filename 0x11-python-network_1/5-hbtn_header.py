#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the
response header"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    value = 'X-Request-Id'
    html = requests.get(url)
    print(html.headers.get(value))
