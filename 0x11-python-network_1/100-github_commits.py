#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

if __name__ == "__main__":
    import requests
    from sys import argv

    rep = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, rep)
    request = requests.get(url)
    count = 0
    for i in request.json():
        print(i.get('sha') + ": " + i.get('commit').get('author').get('name'))
        count += 1
        if count == 10:
            break
