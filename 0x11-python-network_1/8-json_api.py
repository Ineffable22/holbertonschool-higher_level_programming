#!/usr/bin/python3
"""This script takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    value = argv[1] if len(argv) > 1 else ""
    request = requests.post(url, data={'q': value})
    try:
        _dict = request.json()
        if _dict == {}:
            print('No result')
        else:
            print("[{}] {}".format(_dict.get('id'), _dict.get('name')))
    except ValueError:
        print('Not a valid JSON')
