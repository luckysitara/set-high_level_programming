#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status and display the response body."""
import urllib.request


def fetch_status():
    """Fetch the status endpoint and print the response body details."""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
