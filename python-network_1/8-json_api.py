#!/usr/bin/python3
"""Search the API for a letter and display matching user results."""
import sys
import requests


def search_user(letter):
    """POST letter as q to the search_user endpoint and print results."""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        results = response.json()
    except ValueError:
        print("Not a valid JSON")
        return
    if not results:
        print("No result")
        return
    if isinstance(results, dict):
        results = [results]
    for user in results:
        print("[{}] {}".format(user.get("id"), user.get("name")))


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
