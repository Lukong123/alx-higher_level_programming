#!/usr/bin/python3
'''
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
'''
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
