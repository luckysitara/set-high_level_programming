#!/usr/bin/python3
"""Send a POST request with an email parameter to a URL."""
import sys
import urllib.parse
import urllib.request


def post_email(url, email):
    """POST email to url and print the utf-8 decoded response body."""
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
