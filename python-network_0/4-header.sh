#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL,
# and displays the body of the response, with a custom header.
curl -s -X GET -H "X-School-User-Id: 98" "$1"
