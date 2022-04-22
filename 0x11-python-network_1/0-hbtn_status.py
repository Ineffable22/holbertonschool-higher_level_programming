#!/usr/bin/python3
# This script fetches https://intranet.hbtn.io/status
import urllib.request
if __name__ == "__main__":
    URL = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(URL) as response:
        html = response.read()

        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(type(html), html, response.msg))
