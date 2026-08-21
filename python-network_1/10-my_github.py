#!/usr/bin/python3
"""Display the id of the authenticated GitHub user."""
import sys
import requests


def my_github_id(username, password):
    """Print the GitHub id for username, using Basic Auth."""
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)


if __name__ == "__main__":
    my_github_id(sys.argv[1], sys.argv[2])
