#!/usr/bin/python3
"""Fetch a URL and print the X-Request-Id header from the response."""
import sys
import urllib.request


def print_request_id(url):
    """Send a request to url and print the X-Request-Id header."""
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))


if __name__ == "__main__":
    print_request_id(sys.argv[1])
