#!/usr/bin/python3
"""Fetch a URL and print its response body or HTTP error code."""
import sys
import urllib.error
import urllib.request


def fetch(url):
    """Print the utf-8 body of url, or 'Error code: <n>' on HTTPError."""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    fetch(sys.argv[1])
