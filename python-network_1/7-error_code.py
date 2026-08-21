#!/usr/bin/python3
"""Fetch a URL and print its body, or an error code if status >= 400."""
import sys
import requests


def fetch(url):
    """Print the body of url, or 'Error code: <n>' if status >= 400."""
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    fetch(sys.argv[1])
