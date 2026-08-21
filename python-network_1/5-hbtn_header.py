#!/usr/bin/python3
"""Fetch a URL and print the X-Request-Id header from the response."""
import sys
import requests


def print_request_id(url):
    """Send a request to url and print the X-Request-Id header."""
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    print_request_id(sys.argv[1])
