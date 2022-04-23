#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8)."""
if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
