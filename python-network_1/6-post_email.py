#!/usr/bin/python3
"""Send a POST request with an email parameter to a URL."""
import sys
import requests


def post_email(url, email):
    """POST email to url and print the response body."""
    response = requests.post(url, data={"email": email})
    print(response.text)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
